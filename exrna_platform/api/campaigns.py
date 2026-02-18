"""Campaign management API routes.

Endpoints for listing, creating, pausing, and resuming research campaigns.
Uses ProgressTracker for PostgreSQL-backed campaign persistence.
"""

import logging
from typing import Optional

from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse

from exrna_platform.dependencies import get_deps
from exrna_platform.models import CampaignCreate, CampaignResponse, CampaignList

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=CampaignList)
async def list_campaigns(
    request: Request,
    status: Optional[str] = Query(None, description="Filter by status: pending, running, paused, completed, failed"),
):
    """List all campaigns, optionally filtered by status."""
    deps = get_deps(request)
    if deps.progress is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Campaign tracking service unavailable (PostgreSQL not connected)"},
        )

    try:
        campaigns = await deps.progress.list_campaigns(status=status)
        return CampaignList(
            campaigns=[CampaignResponse(**c) for c in campaigns],
            total=len(campaigns),
        )
    except Exception as e:
        logger.error(f"Failed to list campaigns: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to list campaigns: {e}")


@router.post("/", response_model=CampaignResponse, status_code=201)
async def create_campaign(request: Request, body: CampaignCreate):
    """Create and launch a new research campaign."""
    deps = get_deps(request)
    if deps.progress is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Campaign tracking service unavailable (PostgreSQL not connected)"},
        )

    try:
        campaign_id = await deps.progress.create_campaign(
            name=body.name,
            campaign_type=body.campaign_type,
            config=body.config,
            budget_limit=body.budget_limit,
            crop=body.crop,
        )

        # Mark as running immediately after creation
        await deps.progress.mark_running(campaign_id)

        campaign = await deps.progress.get_campaign(campaign_id)
        if not campaign:
            raise HTTPException(status_code=500, detail="Campaign created but could not be retrieved")

        return CampaignResponse(**campaign)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to create campaign: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to create campaign: {e}")


@router.get("/{campaign_id}", response_model=CampaignResponse)
async def get_campaign(request: Request, campaign_id: str):
    """Get details for a specific campaign."""
    deps = get_deps(request)
    if deps.progress is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Campaign tracking service unavailable (PostgreSQL not connected)"},
        )

    try:
        campaign = await deps.progress.get_campaign(campaign_id)
        if not campaign:
            raise HTTPException(status_code=404, detail=f"Campaign {campaign_id} not found")
        return CampaignResponse(**campaign)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get campaign {campaign_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to get campaign: {e}")


@router.post("/{campaign_id}/pause", response_model=CampaignResponse)
async def pause_campaign(request: Request, campaign_id: str):
    """Pause a running campaign."""
    deps = get_deps(request)
    if deps.progress is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Campaign tracking service unavailable (PostgreSQL not connected)"},
        )

    try:
        campaign = await deps.progress.get_campaign(campaign_id)
        if not campaign:
            raise HTTPException(status_code=404, detail=f"Campaign {campaign_id} not found")
        if campaign["status"] != "running":
            raise HTTPException(
                status_code=409,
                detail=f"Campaign is '{campaign['status']}', not 'running'. Cannot pause.",
            )

        # Update status to paused via direct session access
        import uuid
        from sqlalchemy import select
        from exrna_platform.db.postgres import Campaign

        async with deps.pg_session_factory() as session:
            result = await session.execute(
                select(Campaign).where(Campaign.id == uuid.UUID(campaign_id))
            )
            db_campaign = result.scalar_one_or_none()
            if db_campaign:
                db_campaign.status = "paused"
                await session.commit()

        updated = await deps.progress.get_campaign(campaign_id)
        return CampaignResponse(**updated)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to pause campaign {campaign_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to pause campaign: {e}")


@router.post("/{campaign_id}/resume", response_model=CampaignResponse)
async def resume_campaign(request: Request, campaign_id: str):
    """Resume a paused campaign."""
    deps = get_deps(request)
    if deps.progress is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Campaign tracking service unavailable (PostgreSQL not connected)"},
        )

    try:
        campaign = await deps.progress.get_campaign(campaign_id)
        if not campaign:
            raise HTTPException(status_code=404, detail=f"Campaign {campaign_id} not found")
        if campaign["status"] != "paused":
            raise HTTPException(
                status_code=409,
                detail=f"Campaign is '{campaign['status']}', not 'paused'. Cannot resume.",
            )

        # Update status back to running
        await deps.progress.mark_running(campaign_id)

        updated = await deps.progress.get_campaign(campaign_id)
        return CampaignResponse(**updated)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to resume campaign {campaign_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to resume campaign: {e}")
