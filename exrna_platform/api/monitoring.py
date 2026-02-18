"""Monitoring and health check API routes.

Endpoints for system health checks, overall status, and literature alerts.
Uses all dependency services to report comprehensive system state.
"""

import time
import logging
from typing import Optional

from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlalchemy import select, func

from exrna_platform.dependencies import get_deps
from exrna_platform.db.postgres import Campaign, LiteratureAlert
from exrna_platform.models import HealthResponse, LiteratureAlertResponse

logger = logging.getLogger(__name__)

router = APIRouter()

# Track application start time for uptime calculation
_start_time = time.time()


@router.get("/health", response_model=HealthResponse)
async def health_check(request: Request):
    """Check connectivity to all backend services.

    Returns individual status for Neo4j, PostgreSQL, ChromaDB, and the scheduler.
    Overall status is 'healthy' only if all critical services are reachable.
    """
    deps = get_deps(request)

    neo4j_status = "unavailable"
    postgres_status = "unavailable"
    chroma_status = "unavailable"
    scheduler_status = "unavailable"

    # Check Neo4j
    if deps.neo4j is not None:
        try:
            await deps.neo4j.run_query("RETURN 1 AS ping")
            neo4j_status = "healthy"
        except Exception as e:
            neo4j_status = f"error: {e}"

    # Check PostgreSQL
    if deps.pg_session_factory is not None:
        try:
            async with deps.pg_session_factory() as session:
                await session.execute(select(func.now()))
            postgres_status = "healthy"
        except Exception as e:
            postgres_status = f"error: {e}"

    # Check ChromaDB
    if deps.chroma is not None:
        try:
            deps.chroma.get_collection_stats()
            chroma_status = "healthy"
        except Exception as e:
            chroma_status = f"error: {e}"

    # Scheduler status: healthy if progress tracker is available
    if deps.progress is not None:
        scheduler_status = "healthy"

    # Overall status
    critical_healthy = (
        postgres_status == "healthy"
    )
    overall = "healthy" if critical_healthy else "degraded"

    uptime = time.time() - _start_time

    return HealthResponse(
        status=overall,
        neo4j=neo4j_status,
        postgres=postgres_status,
        chromadb=chroma_status,
        scheduler=scheduler_status,
        uptime_seconds=round(uptime, 2),
    )


@router.get("/status", response_model=dict)
async def system_status(request: Request):
    """Get overall system status including campaigns, documents, and service states."""
    deps = get_deps(request)

    status: dict = {
        "services": {
            "neo4j": deps.neo4j is not None,
            "postgres": deps.pg_session_factory is not None,
            "chromadb": deps.chroma is not None,
            "progress_tracker": deps.progress is not None,
        },
        "campaigns": {"running": 0, "completed": 0, "failed": 0, "total": 0},
        "documents": {},
        "uptime_seconds": round(time.time() - _start_time, 2),
    }

    # Campaign counts from PostgreSQL
    if deps.pg_session_factory is not None:
        try:
            async with deps.pg_session_factory() as session:
                for campaign_status in ["running", "completed", "failed", "paused", "pending"]:
                    result = await session.execute(
                        select(func.count(Campaign.id)).where(
                            Campaign.status == campaign_status
                        )
                    )
                    count = result.scalar() or 0
                    status["campaigns"][campaign_status] = count
                    status["campaigns"]["total"] = status["campaigns"].get("total", 0) + count
        except Exception as e:
            logger.warning(f"Failed to get campaign counts: {e}")

    # Document counts from ChromaDB
    if deps.chroma is not None:
        try:
            status["documents"] = deps.chroma.get_collection_stats()
        except Exception as e:
            logger.warning(f"Failed to get document counts: {e}")

    # Node counts from Neo4j
    if deps.neo4j is not None:
        try:
            records = await deps.neo4j.run_query(
                "MATCH (n) RETURN labels(n)[0] AS label, count(n) AS count "
                "ORDER BY count DESC LIMIT 20"
            )
            status["graph_nodes"] = {r["label"]: r["count"] for r in records if r["label"]}
        except Exception as e:
            logger.warning(f"Failed to get graph node counts: {e}")

    return status


@router.get("/literature-alerts", response_model=list[LiteratureAlertResponse])
async def list_literature_alerts(
    request: Request,
    reviewed: Optional[bool] = Query(None, description="Filter by reviewed status"),
    min_relevance: Optional[float] = Query(None, description="Minimum relevance score"),
    limit: int = Query(50, le=200),
):
    """List recent literature alerts from daily PubMed scans."""
    deps = get_deps(request)
    if deps.pg_session_factory is None:
        return JSONResponse(
            status_code=503,
            content={"detail": "Literature alert service unavailable (PostgreSQL not connected)"},
        )

    try:
        async with deps.pg_session_factory() as session:
            query = (
                select(LiteratureAlert)
                .order_by(LiteratureAlert.created_at.desc())
                .limit(limit)
            )

            if reviewed is not None:
                query = query.where(LiteratureAlert.reviewed == reviewed)
            if min_relevance is not None:
                query = query.where(LiteratureAlert.relevance_score >= min_relevance)

            result = await session.execute(query)
            alerts = result.scalars().all()

            return [
                LiteratureAlertResponse(
                    pmid=a.pmid,
                    title=a.title,
                    relevance_score=a.relevance_score,
                    relevance_reason=a.relevance_reason,
                    matched_keywords=a.matched_keywords,
                    claims_extracted=a.claims_extracted,
                    reviewed=a.reviewed,
                    created_at=str(a.created_at),
                )
                for a in alerts
            ]
    except Exception as e:
        logger.error(f"Failed to list literature alerts: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to list literature alerts: {e}")
