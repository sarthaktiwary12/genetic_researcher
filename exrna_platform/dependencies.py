"""Dependency injection: DB sessions, API clients, and shared state."""

import os
import logging
from typing import Optional

from fastapi import Request

from exrna_platform.db.neo4j_client import Neo4jClient
from exrna_platform.db.chroma_client import ChromaClient
from exrna_platform.db.postgres import create_db_engine, init_db
from exrna_platform.scheduler.progress import ProgressTracker

logger = logging.getLogger(__name__)


class AppState:
    """Holds all application-level dependencies initialized at startup."""

    def __init__(self):
        self.neo4j: Optional[Neo4jClient] = None
        self.chroma: Optional[ChromaClient] = None
        self.pg_engine = None
        self.pg_session_factory = None
        self.progress: Optional[ProgressTracker] = None

    async def init(self):
        """Initialize all service connections."""
        # Neo4j
        neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        neo4j_user = os.getenv("NEO4J_USER", "neo4j")
        neo4j_password = os.getenv("NEO4J_PASSWORD", "exrna_research_2024")
        self.neo4j = Neo4jClient(neo4j_uri, neo4j_user, neo4j_password)
        try:
            await self.neo4j.connect()
        except Exception as e:
            logger.warning(f"Neo4j connection failed (non-fatal): {e}")
            self.neo4j = None

        # ChromaDB
        chroma_dir = os.getenv("CHROMA_PERSIST_DIR", "./data/chromadb")
        self.chroma = ChromaClient(persist_dir=chroma_dir)

        # PostgreSQL
        pg_url = os.getenv(
            "POSTGRES_URL",
            "postgresql+asyncpg://exrna:exrna_research@localhost:5432/exrna_platform",
        )
        try:
            self.pg_engine, self.pg_session_factory = await create_db_engine(pg_url)
            await init_db(self.pg_engine)
            self.progress = ProgressTracker(self.pg_session_factory)
        except Exception as e:
            logger.warning(f"PostgreSQL connection failed (non-fatal): {e}")

    async def close(self):
        """Close all service connections."""
        if self.neo4j:
            await self.neo4j.close()
        if self.pg_engine:
            await self.pg_engine.dispose()

    def get_pg_session(self):
        """Get a new async PostgreSQL session."""
        if not self.pg_session_factory:
            raise RuntimeError("PostgreSQL not initialized")
        return self.pg_session_factory()


def get_deps(request: Request) -> AppState:
    """FastAPI dependency to get the application state."""
    return request.app.state.deps
