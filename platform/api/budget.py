"""Budget and cost tracking API routes.

Endpoints for monitoring API spend, monthly budget status,
and per-campaign cost breakdowns.
"""

import logging
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlalchemy import select, func

from platform.dependencies import get_deps
from platform.db.postgres import MonthlyBudget, ApiCost, Campaign
from platform.models import BudgetResponse, CostEntry

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=BudgetResponse)
async def current_budget(request: Request):
    """Get the current month's budget status.

    Returns total spend, per-provider breakdown, budget limit,
    and whether the budget has been exceeded.
    """
    deps = get_deps(request)
    if deps.progress is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Budget service unavailable (PostgreSQL not connected)"},
        )

    try:
        budget = await deps.progress.check_budget()
        return BudgetResponse(
            year_month=budget["year_month"],
            total_spend=budget.get("total_spend", 0.0),
            gemini_spend=budget.get("gemini_spend", 0.0),
            claude_spend=budget.get("claude_spend", 0.0),
            budget_limit=budget.get("budget_limit", 5000.0),
            fraction=budget.get("fraction", 0.0),
            over_budget=budget.get("over_budget", False),
        )
    except Exception as e:
        logger.error(f"Failed to get budget status: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to get budget status: {e}")


@router.get("/history", response_model=list[BudgetResponse])
async def budget_history(
    request: Request,
    months: int = Query(6, le=24, description="Number of months of history to return"),
):
    """Get monthly spend history.

    Returns budget records for the most recent N months.
    """
    deps = get_deps(request)
    if deps.pg_session_factory is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Budget service unavailable (PostgreSQL not connected)"},
        )

    try:
        async with deps.pg_session_factory() as session:
            result = await session.execute(
                select(MonthlyBudget)
                .order_by(MonthlyBudget.year_month.desc())
                .limit(months)
            )
            records = result.scalars().all()

            return [
                BudgetResponse(
                    year_month=r.year_month,
                    total_spend=round(r.total_spend, 2),
                    gemini_spend=round(r.gemini_spend, 2),
                    claude_spend=round(r.claude_spend, 2),
                    budget_limit=r.budget_limit,
                    fraction=round(
                        r.total_spend / r.budget_limit if r.budget_limit > 0 else 0.0, 4
                    ),
                    over_budget=(r.total_spend >= r.budget_limit) if r.budget_limit > 0 else False,
                )
                for r in records
            ]
    except Exception as e:
        logger.error(f"Failed to get budget history: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to get budget history: {e}")


@router.get("/campaigns/{campaign_id}/costs", response_model=dict)
async def campaign_costs(request: Request, campaign_id: str):
    """Get detailed cost breakdown for a specific campaign.

    Returns individual API call costs, per-provider totals,
    and the campaign's budget limit.
    """
    deps = get_deps(request)
    if deps.pg_session_factory is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Budget service unavailable (PostgreSQL not connected)"},
        )

    try:
        import uuid

        async with deps.pg_session_factory() as session:
            # Verify campaign exists
            campaign_result = await session.execute(
                select(Campaign).where(Campaign.id == uuid.UUID(campaign_id))
            )
            campaign = campaign_result.scalar_one_or_none()
            if not campaign:
                raise HTTPException(status_code=404, detail=f"Campaign {campaign_id} not found")

            # Get all cost entries for this campaign
            costs_result = await session.execute(
                select(ApiCost)
                .where(ApiCost.campaign_id == uuid.UUID(campaign_id))
                .order_by(ApiCost.created_at.desc())
            )
            costs = costs_result.scalars().all()

            # Compute per-provider totals
            provider_totals: dict[str, float] = {}
            total_input_tokens = 0
            total_output_tokens = 0
            total_cost = 0.0

            cost_entries = []
            for c in costs:
                provider_totals[c.provider] = provider_totals.get(c.provider, 0.0) + c.cost_usd
                total_input_tokens += c.input_tokens
                total_output_tokens += c.output_tokens
                total_cost += c.cost_usd

                cost_entries.append(
                    CostEntry(
                        provider=c.provider,
                        model=c.model,
                        input_tokens=c.input_tokens,
                        output_tokens=c.output_tokens,
                        cost_usd=round(c.cost_usd, 6),
                        task_category=c.task_category,
                        created_at=str(c.created_at),
                    ).model_dump()
                )

            return {
                "campaign_id": campaign_id,
                "campaign_name": campaign.name,
                "budget_limit": campaign.budget_limit,
                "total_cost": round(total_cost, 4),
                "total_input_tokens": total_input_tokens,
                "total_output_tokens": total_output_tokens,
                "provider_totals": {k: round(v, 4) for k, v in provider_totals.items()},
                "num_api_calls": len(costs),
                "costs": cost_entries,
            }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get costs for campaign {campaign_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to get campaign costs: {e}")
