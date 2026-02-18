"""FastAPI application with lifespan management for all services."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from exrna_platform.dependencies import AppState
from exrna_platform.api import campaigns, knowledge, search, targets, experiments, monitoring, budget

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize and shutdown application services."""
    logger.info("Starting ExRNA Research Platform...")

    # Initialize all services
    state = AppState()
    await state.init()
    app.state.deps = state

    logger.info("All services initialized")
    yield

    # Shutdown
    logger.info("Shutting down...")
    await state.close()
    logger.info("Shutdown complete")


app = FastAPI(
    title="ExRNA Autonomous Research Platform",
    description="Level 3 autonomous research platform for extracellular RNA biology",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(campaigns.router, prefix="/api/campaigns", tags=["campaigns"])
app.include_router(knowledge.router, prefix="/api/knowledge", tags=["knowledge"])
app.include_router(search.router, prefix="/api/search", tags=["search"])
app.include_router(targets.router, prefix="/api/targets", tags=["targets"])
app.include_router(experiments.router, prefix="/api/experiments", tags=["experiments"])
app.include_router(monitoring.router, prefix="/api/monitoring", tags=["monitoring"])
app.include_router(budget.router, prefix="/api/budget", tags=["budget"])
