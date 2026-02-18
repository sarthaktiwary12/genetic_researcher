"""Writes per-target analysis files to the knowledge base."""

import logging
from datetime import date
from pathlib import Path

from agents.config import KB_TARGETS_HIGH, KB_TARGETS_MEDIUM, KB_TARGETS_LOW

logger = logging.getLogger(__name__)


def _sanitize_filename(gene_id: str, annotation: str) -> str:
    """Create a safe filename from gene ID and annotation."""
    # Take the gene ID and first few words of annotation
    short_annotation = annotation.lower().replace(" ", "_").replace("/", "_")
    short_annotation = "".join(c for c in short_annotation if c.isalnum() or c == "_")
    # Trim to reasonable length
    short_annotation = short_annotation[:50].rstrip("_")
    gene_part = gene_id.replace(".", "_")
    return f"{gene_part}_{short_annotation}.md"


def _get_priority_dir(priority: str, base_dir: Path = None) -> Path:
    """Get the directory for a given priority level.

    Args:
        priority: Priority level (high/medium/low).
        base_dir: Optional base directory for targets. When provided,
                  uses base_dir/{high|medium|low}_priority/ instead of
                  the hardcoded config paths.
    """
    if base_dir is not None:
        dirs = {
            "high": base_dir / "high_priority",
            "medium": base_dir / "medium_priority",
            "low": base_dir / "low_priority",
        }
        return dirs.get(priority.lower(), base_dir / "low_priority")

    dirs = {
        "high": KB_TARGETS_HIGH,
        "medium": KB_TARGETS_MEDIUM,
        "low": KB_TARGETS_LOW,
    }
    return dirs.get(priority.lower(), KB_TARGETS_LOW)


def write_target_analysis(
    gene_id: str,
    annotation: str,
    pathway: str,
    priority: str,
    analysis: str,
    tldr: str = "",
    base_dir: Path = None,
) -> Path:
    """Write a single gene target analysis file.

    Args:
        gene_id: The gene identifier (e.g., SOV3g000150.1).
        annotation: Gene annotation/description.
        pathway: Pathway classification.
        priority: Priority level (high/medium/low).
        analysis: Full analysis text from Gemini.
        tldr: Short summary (auto-extracted if empty).
        base_dir: Optional base directory for targets. When provided,
                  writes to base_dir/{priority}_priority/ instead of
                  the hardcoded config paths.

    Returns:
        Path to the written file.
    """
    priority_dir = _get_priority_dir(priority, base_dir=base_dir)
    priority_dir.mkdir(parents=True, exist_ok=True)

    filename = _sanitize_filename(gene_id, annotation)
    filepath = priority_dir / filename

    if not tldr:
        # Extract first meaningful paragraph as TL;DR
        lines = [l.strip() for l in analysis.split("\n") if l.strip() and not l.startswith("#")]
        tldr = " ".join(lines[:3])[:300]

    content = f"""# {gene_id} - {annotation}
> TL;DR: {tldr}
> Priority: {priority.capitalize()}
> Pathway: {pathway}
> Last Updated: {date.today().isoformat()}

## Gene Information
- **Gene ID**: {gene_id}
- **Annotation**: {annotation}
- **Pathway**: {pathway}
- **Priority**: {priority.capitalize()}

## Analysis

{analysis}
"""

    filepath.write_text(content)
    logger.info(f"Wrote target analysis: {filepath}")
    return filepath


def write_batch_summary(
    genes: list[dict],
    batch_analysis: str,
    batch_id: int,
    base_dir: Path = None,
) -> Path:
    """Write a batch summary for a group of genes.

    Args:
        genes: List of gene dicts from the batch.
        batch_analysis: The batch analysis text.
        batch_id: Numeric batch identifier.
        base_dir: Optional base directory for research output. When provided,
                  writes to base_dir/ instead of KB_RESEARCH_LIT.

    Returns:
        Path to the written file.
    """
    if base_dir is not None:
        output_dir = base_dir
    else:
        from agents.config import KB_RESEARCH_LIT
        output_dir = KB_RESEARCH_LIT

    filepath = output_dir / f"batch_{batch_id:03d}_summary.md"
    filepath.parent.mkdir(parents=True, exist_ok=True)

    gene_list = "\n".join(f"- {g['gene_id']}: {g['annotation']}" for g in genes)

    content = f"""# Batch {batch_id} Gene Analysis Summary
> TL;DR: Batch analysis of {len(genes)} gene targets.
> Last Updated: {date.today().isoformat()}

## Genes in Batch
{gene_list}

## Analysis

{batch_analysis}
"""

    filepath.write_text(content)
    logger.info(f"Wrote batch summary: {filepath}")
    return filepath
