"""SQLAlchemy async models for PostgreSQL.

Tables:
    campaigns       — Research campaign tracking
    api_costs       — Per-request API cost log
    monthly_budget  — Aggregated monthly spend
    experiments     — Wet-lab experiment definitions
    experiment_results — Wet-lab result entries
    hypotheses      — AI-generated hypotheses
    literature_alerts — Daily PubMed scan results
"""

import uuid
from datetime import datetime, date
from typing import Optional

from sqlalchemy import (
    String, Float, Integer, Text, Boolean, Date, DateTime,
    ForeignKey, Index, Enum as SAEnum, func,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all models."""
    pass


class Campaign(Base):
    __tablename__ = "campaigns"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    campaign_type: Mapped[str] = mapped_column(String(50), nullable=False)
    crop: Mapped[Optional[str]] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(20), default="pending")  # pending, running, paused, completed, failed
    progress: Mapped[float] = mapped_column(Float, default=0.0)
    current_stage: Mapped[Optional[str]] = mapped_column(String(50))
    config: Mapped[Optional[dict]] = mapped_column(JSONB)
    budget_limit: Mapped[Optional[float]] = mapped_column(Float)
    total_cost: Mapped[float] = mapped_column(Float, default=0.0)
    error_message: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime)

    costs: Mapped[list["ApiCost"]] = relationship(back_populates="campaign")

    __table_args__ = (
        Index("ix_campaigns_status", "status"),
        Index("ix_campaigns_crop", "crop"),
    )


class ApiCost(Base):
    __tablename__ = "api_costs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    campaign_id: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True), ForeignKey("campaigns.id"))
    provider: Mapped[str] = mapped_column(String(20), nullable=False)  # "gemini" or "claude"
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    input_tokens: Mapped[int] = mapped_column(Integer, default=0)
    output_tokens: Mapped[int] = mapped_column(Integer, default=0)
    cost_usd: Mapped[float] = mapped_column(Float, nullable=False)
    task_category: Mapped[Optional[str]] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    campaign: Mapped[Optional["Campaign"]] = relationship(back_populates="costs")

    __table_args__ = (
        Index("ix_api_costs_provider", "provider"),
        Index("ix_api_costs_created", "created_at"),
    )


class MonthlyBudget(Base):
    __tablename__ = "monthly_budget"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    year_month: Mapped[str] = mapped_column(String(7), unique=True, nullable=False)  # "2026-02"
    total_spend: Mapped[float] = mapped_column(Float, default=0.0)
    gemini_spend: Mapped[float] = mapped_column(Float, default=0.0)
    claude_spend: Mapped[float] = mapped_column(Float, default=0.0)
    budget_limit: Mapped[float] = mapped_column(Float, default=5000.0)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())


class Experiment(Base):
    __tablename__ = "experiments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    crop: Mapped[str] = mapped_column(String(100), nullable=False)
    experiment_type: Mapped[str] = mapped_column(String(50))  # germination, qPCR, phenotyping
    target_genes: Mapped[Optional[list]] = mapped_column(JSONB)
    protocol: Mapped[Optional[dict]] = mapped_column(JSONB)
    status: Mapped[str] = mapped_column(String(20), default="planned")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    results: Mapped[list["ExperimentResult"]] = relationship(back_populates="experiment")


class ExperimentResult(Base):
    __tablename__ = "experiment_results"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    experiment_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("experiments.id"))
    gene_id: Mapped[Optional[str]] = mapped_column(String(100))
    measurement: Mapped[str] = mapped_column(String(100))  # e.g., "germination_rate", "expression_fold_change"
    value: Mapped[float] = mapped_column(Float)
    unit: Mapped[Optional[str]] = mapped_column(String(50))
    conditions: Mapped[Optional[dict]] = mapped_column(JSONB)
    notes: Mapped[Optional[str]] = mapped_column(Text)
    recorded_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    experiment: Mapped["Experiment"] = relationship(back_populates="results")


class Hypothesis(Base):
    __tablename__ = "hypotheses"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    crop: Mapped[str] = mapped_column(String(100))
    target_genes: Mapped[Optional[list]] = mapped_column(JSONB)
    evidence_level: Mapped[str] = mapped_column(String(20), default="inferred")  # known, inferred, speculative
    source_campaign: Mapped[Optional[uuid.UUID]] = mapped_column(UUID(as_uuid=True))
    supporting_papers: Mapped[Optional[list]] = mapped_column(JSONB)
    status: Mapped[str] = mapped_column(String(20), default="active")  # active, tested, refuted, confirmed
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())


class LiteratureAlert(Base):
    __tablename__ = "literature_alerts"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pmid: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    authors: Mapped[Optional[str]] = mapped_column(Text)
    journal: Mapped[Optional[str]] = mapped_column(String(255))
    pub_date: Mapped[Optional[date]] = mapped_column(Date)
    abstract: Mapped[Optional[str]] = mapped_column(Text)
    relevance_score: Mapped[float] = mapped_column(Float, default=0.0)
    relevance_reason: Mapped[Optional[str]] = mapped_column(Text)
    matched_keywords: Mapped[Optional[list]] = mapped_column(JSONB)
    matched_genes: Mapped[Optional[list]] = mapped_column(JSONB)
    claims_extracted: Mapped[Optional[list]] = mapped_column(JSONB)
    reviewed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    __table_args__ = (
        Index("ix_literature_alerts_relevance", "relevance_score"),
        Index("ix_literature_alerts_reviewed", "reviewed"),
    )


# --- Database Engine Factory ---

async def create_db_engine(database_url: str):
    """Create async engine and return engine + session factory."""
    engine = create_async_engine(database_url, echo=False, pool_size=5, max_overflow=10)
    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    return engine, session_factory


async def init_db(engine):
    """Create all tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
