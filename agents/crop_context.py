"""Crop-specific context for pipeline execution.

Provides per-crop paths so each crop writes to its own knowledge base
directory instead of the shared spinach knowledge base.
"""

import json
import logging
import re
from pathlib import Path

from agents.config import PROJECT_ROOT, CROPS_DIR

logger = logging.getLogger(__name__)


class CropContext:
    """Carries crop-specific paths and metadata through the pipeline."""

    def __init__(self, crop: str):
        self.crop = crop
        self.crop_dir = CROPS_DIR / crop

        # Load metadata
        meta_path = self.crop_dir / "crop_metadata.json"
        if meta_path.exists():
            self.metadata = json.loads(meta_path.read_text())
        else:
            self.metadata = {}
            logger.warning(f"No crop_metadata.json for '{crop}'. Pipeline QC may fail.")

        self.organism = self.metadata.get("species", "Unknown")
        self.common_name = self.metadata.get("common_name", crop)

        # Per-crop knowledge base
        self.kb = self.crop_dir / "knowledge_base"

        # Subdirectories
        self.kb_targets = self.kb / "targets"
        self.kb_targets_high = self.kb_targets / "high_priority"
        self.kb_targets_medium = self.kb_targets / "medium_priority"
        self.kb_targets_low = self.kb_targets / "low_priority"
        self.kb_pathways = self.kb / "pathways"
        self.kb_themes = self.kb / "themes"
        self.kb_synthesis = self.crop_dir / "synthesis"
        self.kb_research = self.kb / "research"
        self.kb_research_lit = self.kb_research / "literature"
        self.kb_research_homologs = self.kb_research / "homologs"
        self.kb_research_mechanisms = self.kb_research / "mechanisms"
        self.kb_logs = self.kb / "logs"

        # Targets config
        self.targets_config = self.crop_dir / "targets_config.json"

    def ensure_dirs(self):
        """Create all knowledge base directories."""
        for d in [
            self.kb_targets_high, self.kb_targets_medium, self.kb_targets_low,
            self.kb_pathways, self.kb_themes, self.kb_synthesis,
            self.kb_research_lit, self.kb_research_homologs,
            self.kb_research_mechanisms, self.kb_logs,
        ]:
            d.mkdir(parents=True, exist_ok=True)

    def load_targets(self) -> list[dict]:
        """Load targets from this crop's config.

        Raises QCError subclasses if config is missing, empty, or has
        mismatched gene IDs. This prevents silent empty-data propagation.
        """
        from agents.qc import validate_targets_config
        return validate_targets_config(self.crop)

    def priority_dir(self, priority: str) -> Path:
        """Get the target directory for a priority level."""
        dirs = {
            "high": self.kb_targets_high,
            "medium": self.kb_targets_medium,
            "low": self.kb_targets_low,
        }
        return dirs.get(priority.lower(), self.kb_targets_low)


def strip_llm_preamble(text: str) -> str:
    """Remove common LLM response preambles from Gemini output.

    Strips lines like:
    - "Of course. As a plant systems biologist, I will analyze..."
    - "Certainly! Here is my analysis..."
    - "I'll analyze the..."
    """
    lines = text.split("\n")
    cleaned = []
    skip_initial = True

    for line in lines:
        stripped = line.strip()
        if skip_initial and stripped:
            # Skip preamble patterns
            if re.match(
                r"^(Of course|Certainly|Sure|Absolutely|I('ll| will| would)|"
                r"Here is|Let me|As a |Thank you)",
                stripped, re.IGNORECASE
            ):
                continue
            skip_initial = False
        cleaned.append(line)

    return "\n".join(cleaned).strip()
