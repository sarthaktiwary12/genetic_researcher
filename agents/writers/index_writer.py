"""Updates INDEX.md files with summaries from completed analyses."""

import logging
from datetime import date
from pathlib import Path

from agents.config import (
    KNOWLEDGE_BASE,
    KB_TARGETS,
    KB_PATHWAYS,
    KB_THEMES,
    KB_RESEARCH,
)

logger = logging.getLogger(__name__)


def update_targets_index(targets: list[dict], analyses_written: dict) -> Path:
    """Update the targets INDEX.md with summary of all analyzed targets.

    Args:
        targets: Full list of gene target dicts from config.
        analyses_written: Dict mapping gene_id to {'priority': str, 'filepath': str, 'tldr': str}.

    Returns:
        Path to the updated index file.
    """
    filepath = KB_TARGETS / "INDEX.md"

    high = [t for t in targets if t.get("priority") == "high"]
    medium = [t for t in targets if t.get("priority") == "medium"]
    low = [t for t in targets if t.get("priority") == "low"]

    # Build summary table
    table = "| Gene ID | Annotation | Pathway | Priority | Status |\n"
    table += "|---------|------------|---------|----------|--------|\n"
    for t in sorted(targets, key=lambda x: {"high": 0, "medium": 1, "low": 2}.get(x.get("priority", "low"), 3)):
        status = "Analyzed" if t["gene_id"] in analyses_written else "Pending"
        table += f"| {t['gene_id']} | {t['annotation']} | {t['pathway']} | {t['priority'].capitalize()} | {status} |\n"

    content = f"""# Gene Targets Index
> TL;DR: {len(targets)} spinach gene targets predicted to be downregulated by bacterial exRNAs. {len(high)} high priority, {len(medium)} medium, {len(low)} low.
> Last Updated: {date.today().isoformat()}

## Priority Distribution
| Priority | Count | Directory |
|----------|-------|-----------|
| High | {len(high)} | [high_priority/](high_priority/) |
| Medium | {len(medium)} | [medium_priority/](medium_priority/) |
| Low | {len(low)} | [low_priority/](low_priority/) |

## Analysis Status
- Analyzed: {len(analyses_written)} / {len(targets)}

## All Targets
{table}
"""

    filepath.write_text(content)
    logger.info(f"Updated targets index: {filepath}")
    return filepath


def update_pathways_index(pathways: dict) -> Path:
    """Update the pathways INDEX.md.

    Args:
        pathways: Dict mapping pathway_key to {'gene_count': int, 'filename': str, 'tldr': str}.

    Returns:
        Path to the updated index file.
    """
    filepath = KB_PATHWAYS / "INDEX.md"

    table = "| Pathway | File | Targets | Summary |\n"
    table += "|---------|------|---------|----------|\n"
    for key, info in sorted(pathways.items()):
        name = key.replace("_", " ").title()
        table += f"| {name} | [{info['filename']}]({info['filename']}) | {info['gene_count']} | {info.get('tldr', 'Pending')[:80]} |\n"

    content = f"""# Pathway Analysis Index
> TL;DR: Gene targets grouped by {len(pathways)} biological pathways. Key pathways include hormone signaling, defense/immunity, epigenetics, ROS/redox, transport, and metabolic priming.
> Last Updated: {date.today().isoformat()}

## Pathways
{table}

## Cross-Pathway Analysis
See [cross_pathway_interactions.md](cross_pathway_interactions.md)
"""

    filepath.write_text(content)
    logger.info(f"Updated pathways index: {filepath}")
    return filepath


def update_themes_index(themes: dict) -> Path:
    """Update the themes INDEX.md.

    Args:
        themes: Dict mapping theme_name to {'filename': str, 'tldr': str}.

    Returns:
        Path to the updated index file.
    """
    filepath = KB_THEMES / "INDEX.md"

    table = "| Theme | File | Summary |\n"
    table += "|-------|------|---------|\n"
    for name, info in themes.items():
        table += f"| {name} | [{info['filename']}]({info['filename']}) | {info.get('tldr', 'Pending')[:100]} |\n"

    content = f"""# Themes Index
> TL;DR: {len(themes)} cross-cutting biological themes extracted from target analysis.
> Last Updated: {date.today().isoformat()}

## Themes
{table}

## Theme Interactions
See individual theme files for cross-theme analysis.
"""

    filepath.write_text(content)
    logger.info(f"Updated themes index: {filepath}")
    return filepath


def update_research_index(runs: list[dict]) -> Path:
    """Update the research log INDEX.md.

    Args:
        runs: List of dicts with 'date', 'stage', 'description', 'output_dir', 'status'.

    Returns:
        Path to the updated index file.
    """
    filepath = KB_RESEARCH / "INDEX.md"

    table = "| Date | Stage | Description | Output | Status |\n"
    table += "|------|-------|-------------|--------|--------|\n"
    for run in runs:
        table += f"| {run['date']} | {run['stage']} | {run['description']} | {run['output_dir']} | {run['status']} |\n"

    content = f"""# Research Log Index
> TL;DR: {len(runs)} Gemini research runs completed.
> Last Updated: {date.today().isoformat()}

## Research Runs
{table}

## Directories
- [literature/](literature/) - Raw Gemini literature search outputs
- [homologs/](homologs/) - Homolog analysis results
- [mechanisms/](mechanisms/) - Mechanistic research outputs
"""

    filepath.write_text(content)
    logger.info(f"Updated research index: {filepath}")
    return filepath


def update_master_index(stats: dict) -> Path:
    """Update the master knowledge_base INDEX.md.

    Args:
        stats: Dict with 'total_targets', 'high_priority', 'medium_priority', 'low_priority',
               'pathways_analyzed', 'themes_extracted', 'stages_complete'.

    Returns:
        Path to the updated index file.
    """
    filepath = KNOWLEDGE_BASE / "INDEX.md"

    stages = stats.get("stages_complete", [])
    stage_checks = {
        "gene_analysis": "Stage 1: Batch Gene Analysis",
        "pathway_mapping": "Stage 2: Pathway Mapping",
        "literature_dive": "Stage 3: Literature Deep-Dive",
        "theme_extraction": "Stage 4: Theme Extraction",
        "synthesis": "Stage 5: Claude Synthesis",
    }

    stage_list = ""
    for key, label in stage_checks.items():
        check = "x" if key in stages else " "
        stage_list += f"- [{check}] {label}\n"

    content = f"""# ExRNA Biology Research Engine - Master Index
> TL;DR: Knowledge base for investigating how bacterial extracellular small RNAs improve spinach germination. {stats.get('total_targets', '~100')} predicted gene targets organized by pathway and priority.
> Last Updated: {date.today().isoformat()}

## Research Question
Which spinach transcripts, if downregulated by bacterial exRNAs (antisense), explain improved germination and seedling vigor?

## Knowledge Base Structure
| Directory | Contents | Status |
|-----------|----------|--------|
| [targets/](targets/INDEX.md) | Individual gene target analyses | {stats.get('total_targets', '?')} targets analyzed |
| [pathways/](pathways/INDEX.md) | Pathway-level groupings | {stats.get('pathways_analyzed', '?')} pathways |
| [themes/](themes/INDEX.md) | Cross-cutting biological themes | {stats.get('themes_extracted', '?')} themes |
| [synthesis/](synthesis/) | Final ranked targets, causal models, validation plan | {'Complete' if 'synthesis' in stages else 'Pending'} |
| [research/](research/INDEX.md) | Raw Gemini research outputs | See log |

## Pipeline Status
{stage_list}

## Quick Stats
- Total targets: {stats.get('total_targets', '~100')}
- High priority: {stats.get('high_priority', '?')}
- Medium priority: {stats.get('medium_priority', '?')}
- Low priority: {stats.get('low_priority', '?')}
- Pathways covered: {stats.get('pathways_analyzed', '?')}
- Organism: Spinacia oleracea (spinach)
- Treatment: M-9 bacterial EPS solution
"""

    filepath.write_text(content)
    logger.info(f"Updated master index: {filepath}")
    return filepath
