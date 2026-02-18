"""Experiment management API routes.

Endpoints for creating and querying wet-lab experiments and their results.
Uses PostgreSQL via SQLAlchemy async sessions.
"""

import uuid
import logging
from typing import Optional

from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from exrna_platform.dependencies import get_deps
from exrna_platform.db.postgres import Experiment, ExperimentResult
from exrna_platform.models import (
    ExperimentCreate,
    ExperimentResponse,
    ExperimentResultCreate,
)

logger = logging.getLogger(__name__)

router = APIRouter()


def _pg_unavailable() -> JSONResponse:
    """Standard 503 response when PostgreSQL is not connected."""
    return JSONResponse(
        status_code=503,
        content={"detail": "Experiment service unavailable (PostgreSQL not connected)"},
    )


def _experiment_to_response(exp: Experiment) -> ExperimentResponse:
    """Convert an Experiment ORM instance to an API response."""
    return ExperimentResponse(
        id=str(exp.id),
        name=exp.name,
        crop=exp.crop,
        experiment_type=exp.experiment_type,
        status=exp.status,
        created_at=str(exp.created_at),
    )


def _result_to_dict(r: ExperimentResult) -> dict:
    """Convert an ExperimentResult ORM instance to a dict."""
    return {
        "id": str(r.id),
        "experiment_id": str(r.experiment_id),
        "gene_id": r.gene_id,
        "measurement": r.measurement,
        "value": r.value,
        "unit": r.unit,
        "conditions": r.conditions,
        "notes": r.notes,
        "recorded_at": str(r.recorded_at),
    }


@router.get("/", response_model=list[ExperimentResponse])
async def list_experiments(
    request: Request,
    crop: Optional[str] = Query(None, description="Filter by crop"),
    status: Optional[str] = Query(None, description="Filter by status: planned, running, completed"),
    limit: int = Query(50, le=200),
):
    """List all experiments with optional filters."""
    deps = get_deps(request)
    if deps.pg_session_factory is None:
        return _pg_unavailable()

    try:
        async with deps.pg_session_factory() as session:
            query = select(Experiment).order_by(Experiment.created_at.desc()).limit(limit)
            if crop:
                query = query.where(Experiment.crop == crop)
            if status:
                query = query.where(Experiment.status == status)

            result = await session.execute(query)
            experiments = result.scalars().all()

            return [_experiment_to_response(e) for e in experiments]
    except Exception as e:
        logger.error(f"Failed to list experiments: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to list experiments: {e}")


@router.post("/", response_model=ExperimentResponse, status_code=201)
async def create_experiment(request: Request, body: ExperimentCreate):
    """Create a new experiment record."""
    deps = get_deps(request)
    if deps.pg_session_factory is None:
        return _pg_unavailable()

    try:
        async with deps.pg_session_factory() as session:
            experiment = Experiment(
                name=body.name,
                crop=body.crop,
                experiment_type=body.experiment_type,
                description=body.description,
                target_genes=body.target_genes,
                protocol=body.protocol,
                status="planned",
            )
            session.add(experiment)
            await session.commit()
            await session.refresh(experiment)

            return _experiment_to_response(experiment)
    except Exception as e:
        logger.error(f"Failed to create experiment: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to create experiment: {e}")


@router.get("/{experiment_id}", response_model=dict)
async def get_experiment(request: Request, experiment_id: str):
    """Get full experiment details including description and protocol."""
    deps = get_deps(request)
    if deps.pg_session_factory is None:
        return _pg_unavailable()

    try:
        async with deps.pg_session_factory() as session:
            result = await session.execute(
                select(Experiment).where(Experiment.id == uuid.UUID(experiment_id))
            )
            experiment = result.scalar_one_or_none()
            if not experiment:
                raise HTTPException(status_code=404, detail=f"Experiment {experiment_id} not found")

            return {
                "id": str(experiment.id),
                "name": experiment.name,
                "crop": experiment.crop,
                "experiment_type": experiment.experiment_type,
                "description": experiment.description,
                "target_genes": experiment.target_genes,
                "protocol": experiment.protocol,
                "status": experiment.status,
                "created_at": str(experiment.created_at),
            }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get experiment {experiment_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to get experiment: {e}")


@router.post("/{experiment_id}/results", response_model=dict, status_code=201)
async def add_experiment_result(
    request: Request,
    experiment_id: str,
    body: ExperimentResultCreate,
):
    """Add a result entry to an experiment."""
    deps = get_deps(request)
    if deps.pg_session_factory is None:
        return _pg_unavailable()

    try:
        async with deps.pg_session_factory() as session:
            # Verify experiment exists
            exp_result = await session.execute(
                select(Experiment).where(Experiment.id == uuid.UUID(experiment_id))
            )
            experiment = exp_result.scalar_one_or_none()
            if not experiment:
                raise HTTPException(status_code=404, detail=f"Experiment {experiment_id} not found")

            result_entry = ExperimentResult(
                experiment_id=uuid.UUID(experiment_id),
                gene_id=body.gene_id,
                measurement=body.measurement,
                value=body.value,
                unit=body.unit,
                conditions=body.conditions,
                notes=body.notes,
            )
            session.add(result_entry)
            await session.commit()
            await session.refresh(result_entry)

            return _result_to_dict(result_entry)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to add result to experiment {experiment_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to add experiment result: {e}")


@router.get("/{experiment_id}/results", response_model=list[dict])
async def get_experiment_results(
    request: Request,
    experiment_id: str,
    gene_id: Optional[str] = Query(None, description="Filter results by gene ID"),
):
    """Get all results for an experiment."""
    deps = get_deps(request)
    if deps.pg_session_factory is None:
        return _pg_unavailable()

    try:
        async with deps.pg_session_factory() as session:
            # Verify experiment exists
            exp_result = await session.execute(
                select(Experiment).where(Experiment.id == uuid.UUID(experiment_id))
            )
            experiment = exp_result.scalar_one_or_none()
            if not experiment:
                raise HTTPException(status_code=404, detail=f"Experiment {experiment_id} not found")

            query = (
                select(ExperimentResult)
                .where(ExperimentResult.experiment_id == uuid.UUID(experiment_id))
                .order_by(ExperimentResult.recorded_at.desc())
            )
            if gene_id:
                query = query.where(ExperimentResult.gene_id == gene_id)

            result = await session.execute(query)
            results = result.scalars().all()

            return [_result_to_dict(r) for r in results]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get results for experiment {experiment_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to get experiment results: {e}")
