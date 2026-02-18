"""Writes pathway analysis files to the knowledge base."""

import logging
from datetime import date
from pathlib import Path

from agents.config import KB_PATHWAYS

logger = logging.getLogger(__name__)

# Map pathway keys to display names and filenames
PATHWAY_FILE_MAP = {
    "hormone_signaling": ("Hormone Signaling", "hormone_signaling.md"),
    "defense_immunity": ("Defense & Immunity", "defense_immunity.md"),
    "epigenetic_regulation": ("Epigenetic Regulation", "epigenetic_regulation.md"),
    "ros_redox": ("ROS / Redox Biology", "ros_redox.md"),
    "transport_ion_homeostasis": ("Transport & Ion Homeostasis", "transport_ion_homeostasis.md"),
    "metabolic": ("Metabolic Priming", "metabolic_priming.md"),
    "protein_turnover": ("Protein Turnover (E3/F-box)", "protein_turnover.md"),
    "rna_processing": ("RNA Processing & Splicing", "rna_processing.md"),
    "cell_wall_remodeling": ("Cell Wall Remodeling", "cell_wall_remodeling.md"),
    "signaling": ("General Signaling", "signaling.md"),
    "organelle_biogenesis": ("Organelle Biogenesis", "organelle_biogenesis.md"),
    "dna_repair_replication": ("DNA Repair & Replication", "dna_repair_replication.md"),
    "unknown": ("Unknown Function", "unknown_function.md"),
    "transposon_related": ("Transposon-Related", "transposon_related.md"),
}


def write_pathway_analysis(
    pathway_key: str,
    genes: list[dict],
    analysis: str,
    tldr: str = "",
    base_dir: Path = None,
) -> Path:
    """Write a pathway analysis file.

    Args:
        pathway_key: The pathway identifier key.
        genes: List of gene dicts in this pathway.
        analysis: Full pathway analysis from Gemini.
        tldr: Short summary.
        base_dir: Optional base directory for pathways. When provided,
                  writes to base_dir/ instead of KB_PATHWAYS.

    Returns:
        Path to the written file.
    """
    display_name, filename = PATHWAY_FILE_MAP.get(
        pathway_key, (pathway_key.replace("_", " ").title(), f"{pathway_key}.md")
    )

    output_dir = base_dir if base_dir is not None else KB_PATHWAYS
    filepath = output_dir / filename
    filepath.parent.mkdir(parents=True, exist_ok=True)

    gene_table = "| Gene ID | Annotation | Priority |\n|---------|------------|----------|\n"
    for g in genes:
        gene_table += f"| {g['gene_id']} | {g['annotation']} | {g.get('priority', 'Unknown')} |\n"

    if not tldr:
        lines = [l.strip() for l in analysis.split("\n") if l.strip() and not l.startswith("#")]
        tldr = " ".join(lines[:3])[:300]

    content = f"""# {display_name}
> TL;DR: {tldr}
> Genes: {len(genes)}
> Last Updated: {date.today().isoformat()}

## Genes in Pathway
{gene_table}

## Pathway Analysis

{analysis}
"""

    filepath.write_text(content)
    logger.info(f"Wrote pathway analysis: {filepath}")
    return filepath


def write_cross_pathway_analysis(analysis: str, base_dir: Path = None) -> Path:
    """Write cross-pathway interaction analysis.

    Args:
        analysis: Full cross-pathway analysis text.
        base_dir: Optional base directory for pathways. When provided,
                  writes to base_dir/ instead of KB_PATHWAYS.

    Returns:
        Path to the written file.
    """
    output_dir = base_dir if base_dir is not None else KB_PATHWAYS
    filepath = output_dir / "cross_pathway_interactions.md"
    filepath.parent.mkdir(parents=True, exist_ok=True)

    content = f"""# Cross-Pathway Interactions
> TL;DR: Analysis of interactions between all pathway groups in the exRNA target set.
> Last Updated: {date.today().isoformat()}

## Analysis

{analysis}
"""

    filepath.write_text(content)
    logger.info(f"Wrote cross-pathway analysis: {filepath}")
    return filepath
