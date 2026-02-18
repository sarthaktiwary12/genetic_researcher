"""Pydantic request/response models for all API endpoints."""

from pydantic import BaseModel, Field
from typing import Optional


# --- Campaign Models ---

class CampaignCreate(BaseModel):
    name: str
    campaign_type: str
    crop: Optional[str] = None
    config: Optional[dict] = None
    budget_limit: Optional[float] = None


class CampaignResponse(BaseModel):
    id: str
    name: str
    campaign_type: str
    crop: Optional[str] = None
    status: str
    progress: float
    current_stage: Optional[str] = None
    total_cost: float = 0.0
    created_at: str
    completed_at: Optional[str] = None
    error_message: Optional[str] = None


class CampaignList(BaseModel):
    campaigns: list[CampaignResponse]
    total: int


# --- Knowledge Graph Models ---

class GeneResponse(BaseModel):
    gene_id: str
    annotation: Optional[str] = None
    pathway: Optional[str] = None
    priority: Optional[str] = None
    organism: Optional[str] = None
    tldr: Optional[str] = None


class PathwayResponse(BaseModel):
    pathway_id: str
    name: Optional[str] = None
    gene_count: int = 0
    tldr: Optional[str] = None


class CypherQuery(BaseModel):
    query: str
    parameters: Optional[dict] = None


class GraphQueryResponse(BaseModel):
    records: list[dict]
    count: int


# --- Search Models ---

class SearchRequest(BaseModel):
    query: str
    collection: str = "gene_narratives"
    n_results: int = Field(default=10, le=50)
    filters: Optional[dict] = None


class SearchResult(BaseModel):
    id: str
    text: str
    metadata: dict = {}
    distance: Optional[float] = None


class SearchResponse(BaseModel):
    results: list[SearchResult]
    total: int
    collection: str


# --- Target Models ---

class TargetListResponse(BaseModel):
    targets: list[GeneResponse]
    total: int
    crop: str


# --- Experiment Models ---

class ExperimentCreate(BaseModel):
    name: str
    crop: str
    experiment_type: str
    description: Optional[str] = None
    target_genes: Optional[list[str]] = None
    protocol: Optional[dict] = None


class ExperimentResultCreate(BaseModel):
    gene_id: Optional[str] = None
    measurement: str
    value: float
    unit: Optional[str] = None
    conditions: Optional[dict] = None
    notes: Optional[str] = None


class ExperimentResponse(BaseModel):
    id: str
    name: str
    crop: str
    experiment_type: str
    status: str
    created_at: str


# --- Budget Models ---

class BudgetResponse(BaseModel):
    year_month: str
    total_spend: float
    gemini_spend: float
    claude_spend: float
    budget_limit: float
    fraction: float
    over_budget: bool


class CostEntry(BaseModel):
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    cost_usd: float
    task_category: Optional[str] = None
    created_at: str


# --- Monitoring Models ---

class HealthResponse(BaseModel):
    status: str
    neo4j: str
    postgres: str
    chromadb: str
    scheduler: str
    uptime_seconds: float


class LiteratureAlertResponse(BaseModel):
    pmid: str
    title: str
    relevance_score: float
    relevance_reason: Optional[str] = None
    matched_keywords: Optional[list[str]] = None
    claims_extracted: Optional[list[dict]] = None
    reviewed: bool
    created_at: str
