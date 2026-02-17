"""Configuration for the Gemini research engine."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- API Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment. Check .env file.")

# Model selection
MODEL_REASONING = "gemini-2.5-pro"   # For deep analysis and reasoning
MODEL_BULK = "gemini-2.5-flash"       # For bulk research and literature search

# --- Rate Limiting ---
MAX_CONCURRENT_REQUESTS = 15          # Semaphore limit for asyncio
REQUESTS_PER_MINUTE = 300             # Tier 1 rate limit
RETRY_MAX_ATTEMPTS = 5
RETRY_BASE_DELAY = 1.0                # Seconds, exponential backoff base
RETRY_MAX_DELAY = 60.0                # Max backoff delay

# --- Paths ---
PROJECT_ROOT = Path(__file__).parent.parent
KNOWLEDGE_BASE = PROJECT_ROOT / "knowledge_base"
TARGETS_CONFIG = PROJECT_ROOT / "targets_config.json"

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
