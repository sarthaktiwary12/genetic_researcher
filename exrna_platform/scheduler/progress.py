"""Campaign progress tracking and API cost recording.

Creates campaign records in PostgreSQL, updates status/progress,
records per-request API costs, and checks budget limits.
"""

import uuid
import logging
from datetime import datetime
from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from exrna_platform.db.postgres import Campaign, ApiCost, MonthlyBudget

logger = logging.getLogger(__name__)


class ProgressTracker:
    """Tracks campaign progress and API costs in PostgreSQL."""

    def __init__(self, session_factory, monthly_budget_limit: float = 5000.0):
        self.session_factory = session_factory
        self.monthly_budget_limit = monthly_budget_limit

    async def create_campaign(
        self,
        name: str,
        campaign_type: str,
        config: Optional[dict] = None,
        budget_limit: Optional[float] = None,
        crop: Optional[str] = None,
    ) -> str:
        """Create a new campaign record. Returns campaign ID."""
        campaign_id = str(uuid.uuid4())
        async with self.session_factory() as session:
            campaign = Campaign(
                id=uuid.UUID(campaign_id),
                name=name,
                campaign_type=campaign_type,
                config=config,
                budget_limit=budget_limit,
                crop=crop,
                status="pending",
            )
            session.add(campaign)
            await session.commit()

        logger.info(f"Created campaign: {name} (id={campaign_id})")
        return campaign_id

    async def mark_running(self, campaign_id: str, stage: Optional[str] = None):
        """Mark campaign as running."""
        async with self.session_factory() as session:
            result = await session.execute(
                select(Campaign).where(Campaign.id == uuid.UUID(campaign_id))
            )
            campaign = result.scalar_one_or_none()
            if campaign:
                campaign.status = "running"
                if stage:
                    campaign.current_stage = stage
                await session.commit()

    async def update_progress(
        self,
        campaign_id: str,
        progress: float,
        stage: Optional[str] = None,
    ):
        """Update campaign progress (0.0 to 1.0)."""
        async with self.session_factory() as session:
            result = await session.execute(
                select(Campaign).where(Campaign.id == uuid.UUID(campaign_id))
            )
            campaign = result.scalar_one_or_none()
            if campaign:
                campaign.progress = progress
                if stage:
                    campaign.current_stage = stage
                await session.commit()

    async def mark_completed(self, campaign_id: str, result: Optional[dict] = None):
        """Mark campaign as completed."""
        async with self.session_factory() as session:
            result_q = await session.execute(
                select(Campaign).where(Campaign.id == uuid.UUID(campaign_id))
            )
            campaign = result_q.scalar_one_or_none()
            if campaign:
                campaign.status = "completed"
                campaign.progress = 1.0
                campaign.completed_at = datetime.utcnow()
                await session.commit()

        logger.info(f"Campaign {campaign_id} completed")

    async def mark_failed(self, campaign_id: str, error_message: str):
        """Mark campaign as failed with error message."""
        async with self.session_factory() as session:
            result = await session.execute(
                select(Campaign).where(Campaign.id == uuid.UUID(campaign_id))
            )
            campaign = result.scalar_one_or_none()
            if campaign:
                campaign.status = "failed"
                campaign.error_message = error_message
                await session.commit()

        logger.error(f"Campaign {campaign_id} failed: {error_message}")

    async def record_api_cost(
        self,
        provider: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        cost_usd: float,
        campaign_id: Optional[str] = None,
        task_category: Optional[str] = None,
    ):
        """Record an API call cost. Triggers monthly_budget update via DB trigger."""
        async with self.session_factory() as session:
            cost = ApiCost(
                campaign_id=uuid.UUID(campaign_id) if campaign_id else None,
                provider=provider,
                model=model,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                cost_usd=cost_usd,
                task_category=task_category,
            )
            session.add(cost)
            await session.commit()

    async def check_budget(self) -> dict:
        """Check current month's budget status.

        Returns:
            Dict with total_spend, budget_limit, fraction, and over_budget flag.
        """
        year_month = datetime.now().strftime("%Y-%m")
        async with self.session_factory() as session:
            result = await session.execute(
                select(MonthlyBudget).where(MonthlyBudget.year_month == year_month)
            )
            budget = result.scalar_one_or_none()

            if not budget:
                return {
                    "year_month": year_month,
                    "total_spend": 0.0,
                    "budget_limit": self.monthly_budget_limit,
                    "fraction": 0.0,
                    "over_budget": False,
                }

            fraction = budget.total_spend / budget.budget_limit if budget.budget_limit > 0 else 0.0
            return {
                "year_month": year_month,
                "total_spend": round(budget.total_spend, 2),
                "gemini_spend": round(budget.gemini_spend, 2),
                "claude_spend": round(budget.claude_spend, 2),
                "budget_limit": budget.budget_limit,
                "fraction": round(fraction, 4),
                "over_budget": fraction >= 1.0,
            }

    async def get_campaign(self, campaign_id: str) -> Optional[dict]:
        """Get campaign details."""
        async with self.session_factory() as session:
            result = await session.execute(
                select(Campaign).where(Campaign.id == uuid.UUID(campaign_id))
            )
            campaign = result.scalar_one_or_none()
            if not campaign:
                return None

            return {
                "id": str(campaign.id),
                "name": campaign.name,
                "campaign_type": campaign.campaign_type,
                "crop": campaign.crop,
                "status": campaign.status,
                "progress": campaign.progress,
                "current_stage": campaign.current_stage,
                "total_cost": round(campaign.total_cost, 4),
                "created_at": str(campaign.created_at),
                "completed_at": str(campaign.completed_at) if campaign.completed_at else None,
                "error_message": campaign.error_message,
            }

    async def list_campaigns(
        self,
        status: Optional[str] = None,
        limit: int = 20,
    ) -> list[dict]:
        """List campaigns, optionally filtered by status."""
        async with self.session_factory() as session:
            query = select(Campaign).order_by(Campaign.created_at.desc()).limit(limit)
            if status:
                query = query.where(Campaign.status == status)

            result = await session.execute(query)
            campaigns = result.scalars().all()

            return [
                {
                    "id": str(c.id),
                    "name": c.name,
                    "campaign_type": c.campaign_type,
                    "crop": c.crop,
                    "status": c.status,
                    "progress": c.progress,
                    "total_cost": round(c.total_cost, 4),
                    "created_at": str(c.created_at),
                }
                for c in campaigns
            ]
