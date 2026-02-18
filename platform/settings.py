"""Centralized configuration using Pydantic Settings.

Extends agents/config.py by consolidating all configuration into a
validated, environment-driven settings class. All DB URLs, API keys,
model names, and rate limits are defined here.
"""

from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8", "extra": "ignore"}

    # --- API Keys ---
    gemini_api_key: str = Field(..., description="Google Gemini API key")
    anthropic_api_key: str = Field(..., description="Anthropic API key")

    # --- Gemini Models ---
    gemini_model_reasoning: str = "gemini-2.5-pro"
    gemini_model_bulk: str = "gemini-2.5-flash"

    # --- Claude Models ---
    claude_model_opus: str = "claude-opus-4-6"
    claude_model_sonnet: str = "claude-sonnet-4-6"
    claude_model_haiku: str = "claude-haiku-4-5-20251001"

    # --- Rate Limiting ---
    max_concurrent_requests: int = 15
    gemini_requests_per_minute: int = 300
    claude_requests_per_minute: int = 60
    retry_max_attempts: int = 5
    retry_base_delay: float = 1.0
    retry_max_delay: float = 60.0

    # --- Database URLs ---
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "exrna_research_2024"
    postgres_url: str = "postgresql+asyncpg://exrna:exrna_research@localhost:5432/exrna_platform"
    redis_url: str = "redis://localhost:6379/0"
    chroma_persist_dir: str = "./data/chromadb"

    # --- Budget ---
    monthly_budget_usd: float = 5000.0
    budget_warning_threshold: float = 0.8  # Warn at 80%

    # --- Paths ---
    project_root: Path = Path(__file__).parent.parent
    knowledge_base: Path = Field(default=None)
    targets_config: Path = Field(default=None)

    # --- Research Context ---
    default_organism: str = "Spinacia oleracea"
    default_treatment: str = "M-9 bacterial EPS solution"

    # --- Server ---
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    debug: bool = False

    def model_post_init(self, __context):
        """Set derived paths after initialization."""
        if self.knowledge_base is None:
            self.knowledge_base = self.project_root / "knowledge_base"
        if self.targets_config is None:
            self.targets_config = self.project_root / "targets_config.json"

    @property
    def kb_targets(self) -> Path:
        return self.knowledge_base / "targets"

    @property
    def kb_targets_high(self) -> Path:
        return self.knowledge_base / "targets" / "high_priority"

    @property
    def kb_targets_medium(self) -> Path:
        return self.knowledge_base / "targets" / "medium_priority"

    @property
    def kb_targets_low(self) -> Path:
        return self.knowledge_base / "targets" / "low_priority"

    @property
    def kb_pathways(self) -> Path:
        return self.knowledge_base / "pathways"

    @property
    def kb_themes(self) -> Path:
        return self.knowledge_base / "themes"

    @property
    def kb_synthesis(self) -> Path:
        return self.knowledge_base / "synthesis"

    @property
    def kb_research(self) -> Path:
        return self.knowledge_base / "research"

    @property
    def kb_research_lit(self) -> Path:
        return self.knowledge_base / "research" / "literature"

    @property
    def kb_research_homologs(self) -> Path:
        return self.knowledge_base / "research" / "homologs"

    @property
    def kb_research_mechanisms(self) -> Path:
        return self.knowledge_base / "research" / "mechanisms"

    @property
    def kb_logs(self) -> Path:
        return self.knowledge_base / "logs"


def get_settings() -> Settings:
    """Factory function for settings singleton."""
    return Settings()
