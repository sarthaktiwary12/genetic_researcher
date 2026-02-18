"""Configuration for the ExRNA research engine.

Provides both Gemini and Claude API config, database connection strings,
and all path constants. Values are loaded from environment variables.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- API Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment. Check .env file.")

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Gemini model selection
MODEL_REASONING = os.getenv("GEMINI_MODEL_REASONING", "gemini-2.5-pro")
MODEL_BULK = os.getenv("GEMINI_MODEL_BULK", "gemini-2.5-flash")

# Claude model selection
CLAUDE_MODEL_OPUS = os.getenv("CLAUDE_MODEL_OPUS", "claude-opus-4-6")
CLAUDE_MODEL_SONNET = os.getenv("CLAUDE_MODEL_SONNET", "claude-sonnet-4-6")
CLAUDE_MODEL_HAIKU = os.getenv("CLAUDE_MODEL_HAIKU", "claude-haiku-4-5-20251001")

# --- Rate Limiting ---
MAX_CONCURRENT_REQUESTS = int(os.getenv("MAX_CONCURRENT_REQUESTS", "15"))
REQUESTS_PER_MINUTE = int(os.getenv("GEMINI_REQUESTS_PER_MINUTE", "300"))
CLAUDE_REQUESTS_PER_MINUTE = int(os.getenv("CLAUDE_REQUESTS_PER_MINUTE", "60"))
RETRY_MAX_ATTEMPTS = 5
RETRY_BASE_DELAY = 1.0                # Seconds, exponential backoff base
RETRY_MAX_DELAY = 60.0                # Max backoff delay

# --- Database URLs ---
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "exrna_research_2024")
POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql+asyncpg://exrna:exrna_research@localhost:5432/exrna_platform")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./data/chromadb")

# --- Budget ---
MONTHLY_BUDGET_USD = float(os.getenv("MONTHLY_BUDGET_USD", "5000.0"))

# --- Paths ---
PROJECT_ROOT = Path(__file__).parent.parent
KNOWLEDGE_BASE = PROJECT_ROOT / "knowledge_base"
TARGETS_CONFIG = PROJECT_ROOT / "targets_config.json"
CROPS_DIR = PROJECT_ROOT / "crops"

# Knowledge base subdirectories
KB_TARGETS = KNOWLEDGE_BASE / "targets"
KB_TARGETS_HIGH = KB_TARGETS / "high_priority"
KB_TARGETS_MEDIUM = KB_TARGETS / "medium_priority"
KB_TARGETS_LOW = KB_TARGETS / "low_priority"
KB_PATHWAYS = KNOWLEDGE_BASE / "pathways"
KB_THEMES = KNOWLEDGE_BASE / "themes"
KB_SYNTHESIS = KNOWLEDGE_BASE / "synthesis"
KB_RESEARCH = KNOWLEDGE_BASE / "research"
KB_RESEARCH_LIT = KB_RESEARCH / "literature"
KB_RESEARCH_HOMOLOGS = KB_RESEARCH / "homologs"
KB_RESEARCH_MECHANISMS = KB_RESEARCH / "mechanisms"
KB_LOGS = KNOWLEDGE_BASE / "logs"

# --- Research Context ---
ORGANISM = "Spinacia oleracea"
TREATMENT = "M-9 bacterial EPS solution"
PHENOTYPE = "Germination rate increase, vigor increase, early seedling growth improvement"
MECHANISM = "Extracellular small RNAs from bacteria targeting plant transcripts via antisense"
