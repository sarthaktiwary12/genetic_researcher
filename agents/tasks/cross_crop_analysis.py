"""Cross-crop meta-analysis task.

Orchestrates comparison across all analyzed crops: reads each crop's results,
builds a unified theme matrix, identifies conserved vs species-specific mechanisms.
"""

import asyncio
import logging
import time
from pathlib import Path
from typing import Optional

from agents.config import PROJECT_ROOT, KNOWLEDGE_BASE, KB_SYNTHESIS, CROPS_DIR
from agents.prompts.claude_synthesis import SYNTHESIS_SYSTEM, cross_crop_synthesis_prompt

logger = logging.getLogger(__name__)


def _load_crop_summary(crop: str) -> Optional[str]:
    """Load synthesis summary for a single crop.

    Looks for synthesis/ranked_targets.md or an INDEX.md in the crop's
    knowledge base directory.
    """
    # Try crop-specific knowledge base
    crop_kb = CROPS_DIR / crop / "knowledge_base" / "synthesis"
    if crop_kb.exists():
        ranked = crop_kb / "ranked_targets.md"
        if ranked.exists():
            return ranked.read_text()[:4000]

    # Try shared knowledge base (for the default crop — spinach)
    if crop == "spinach":
        ranked = KB_SYNTHESIS / "ranked_targets.md"
        if ranked.exists():
            return ranked.read_text()[:4000]

    # Try crop-specific targets index
    crop_targets = CROPS_DIR / crop / "knowledge_base" / "targets" / "INDEX.md"
    if crop_targets.exists():
        return crop_targets.read_text()[:4000]

    return None


def _load_all_crop_summaries(crops: list[str]) -> dict[str, str]:
    """Load summaries for all requested crops."""
    summaries = {}
    for crop in crops:
        summary = _load_crop_summary(crop)
        if summary:
            summaries[crop] = summary
        else:
            logger.warning(f"No data found for crop: {crop}")
    return summaries


async def run(
    claude_client,
    crops: Optional[list[str]] = None,
) -> dict:
    """Execute cross-crop meta-analysis.

    Args:
        claude_client: ClaudeClient instance for synthesis queries.
        crops: List of crop names. Defaults to all available.

    Returns:
        Summary dict with output file paths and stats.
    """
    start = time.time()

    if crops is None:
        # Auto-discover crops from the crops/ directory
        crops = []
        if CROPS_DIR.exists():
            crops = [d.name for d in sorted(CROPS_DIR.iterdir()) if d.is_dir()]
        if not crops:
            crops = ["spinach"]

    logger.info(f"Cross-crop analysis for: {crops}")

    # Load summaries
    crop_results = _load_all_crop_summaries(crops)

    if len(crop_results) < 2:
        logger.warning(
            f"Only {len(crop_results)} crop(s) have data. "
            "Need at least 2 for cross-crop analysis."
        )
        if len(crop_results) == 0:
            return {"error": "No crop data found", "crops_available": 0}

    # Generate cross-crop synthesis
    prompt = cross_crop_synthesis_prompt(crop_results)
    response = await claude_client.query_synthesis(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    # Write output
    output_path = KB_SYNTHESIS / "cross_crop_synthesis.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        f"# Cross-Crop Meta-Analysis\n"
        f"> Crops analyzed: {', '.join(crop_results.keys())}\n\n"
        f"{response}"
    )

    # Write the theme matrix as a separate file for easy reference
    matrix_path = KB_SYNTHESIS / "cross_crop_matrix.md"
    matrix_section = _extract_section(response, "Cross-Crop Theme Matrix")
    if matrix_section:
        matrix_path.write_text(
            f"# Cross-Crop Theme Matrix\n\n{matrix_section}"
        )

    duration = time.time() - start
    result = {
        "crops_analyzed": list(crop_results.keys()),
        "output_file": str(output_path),
        "duration_seconds": round(duration, 1),
        "api_stats": claude_client.get_stats(),
    }

    logger.info(f"Cross-crop analysis complete: {result}")
    return result


def _extract_section(text: str, heading: str) -> Optional[str]:
    """Extract a markdown section by its heading."""
    lines = text.split("\n")
    capturing = False
    section_lines = []

    for line in lines:
        if heading.lower() in line.lower() and line.strip().startswith("#"):
            capturing = True
            section_lines.append(line)
            continue
        if capturing:
            if line.strip().startswith("#") and heading.lower() not in line.lower():
                break
            section_lines.append(line)

    return "\n".join(section_lines) if section_lines else None
