"""Stage 2: Pathway analysis - group targets by pathway and analyze interactions."""

import asyncio
import json
import logging
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

from agents.config import TARGETS_CONFIG, KB_TARGETS_HIGH, KB_TARGETS_MEDIUM, KB_TARGETS_LOW
from agents.crop_context import CropContext, strip_llm_preamble
from agents.gemini_client import GeminiClient
from agents.prompts.pathway_mapping import (
    SYSTEM_INSTRUCTION,
    pathway_analysis_prompt,
    cross_pathway_prompt,
)
from agents.writers.pathway_writer import (
    write_pathway_analysis,
    write_cross_pathway_analysis,
    PATHWAY_FILE_MAP,
)
from agents.writers.index_writer import update_pathways_index, update_research_index

logger = logging.getLogger(__name__)


def load_targets() -> list[dict]:
    """Load gene targets from config file (legacy fallback)."""
    with open(TARGETS_CONFIG) as f:
        data = json.load(f)
    return data["targets"]


def group_by_pathway(targets: list[dict]) -> dict[str, list[dict]]:
    """Group targets by their pathway classification."""
    groups = defaultdict(list)
    for t in targets:
        groups[t["pathway"]].append(t)
    return dict(groups)


def load_gene_analyses(
    targets: list[dict],
    priority_dirs: dict[str, Path] = None,
) -> dict[str, str]:
    """Load existing gene analysis files to provide context for pathway analysis.

    Args:
        targets: List of gene target dicts.
        priority_dirs: Optional dict mapping priority level to directory Path.
                       Falls back to hardcoded config paths when None.
    """
    analyses = {}

    if priority_dirs is None:
        priority_dirs = {
            "high": KB_TARGETS_HIGH,
            "medium": KB_TARGETS_MEDIUM,
            "low": KB_TARGETS_LOW,
        }

    for target in targets:
        priority_dir = priority_dirs.get(target["priority"], priority_dirs.get("low", KB_TARGETS_LOW))
        # Try to find the analysis file
        if not priority_dir.exists():
            continue
        for f in priority_dir.glob(f"{target['gene_id'].replace('.', '_')}*.md"):
            try:
                content = f.read_text()
                # Extract just the TL;DR and key findings
                lines = content.split("\n")
                summary_lines = []
                for line in lines:
                    if line.startswith("> TL;DR:"):
                        summary_lines.append(line)
                    elif line.startswith("## Key Findings") or line.startswith("## Analysis"):
                        # Grab next few lines
                        idx = lines.index(line)
                        summary_lines.extend(lines[idx:idx + 10])
                        break
                analyses[target["gene_id"]] = "\n".join(summary_lines) if summary_lines else content[:500]
            except Exception as e:
                logger.warning(f"Could not read analysis for {target['gene_id']}: {e}")

    return analyses


async def analyze_pathway(
    client: GeminiClient,
    pathway_key: str,
    genes: list[dict],
    gene_analyses: dict[str, str],
    base_dir: Path = None,
) -> dict:
    """Analyze a single pathway group."""
    # Compile gene analyses for this pathway
    analyses_text = ""
    for g in genes:
        gene_id = g["gene_id"]
        if gene_id in gene_analyses:
            analyses_text += f"\n### {gene_id} - {g['annotation']}\n{gene_analyses[gene_id]}\n"
        else:
            analyses_text += f"\n### {gene_id} - {g['annotation']}\n(No individual analysis available)\n"

    prompt = pathway_analysis_prompt(
        pathway_name=pathway_key.replace("_", " ").title(),
        genes=genes,
        gene_analyses=analyses_text,
    )

    try:
        analysis = await client.query_reasoning(
            prompt=prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=8192,
        )

        # Strip LLM preamble
        analysis = strip_llm_preamble(analysis)

        # Extract TL;DR
        lines = [l.strip() for l in analysis.split("\n") if l.strip() and not l.startswith("#")]
        tldr = " ".join(lines[:2])[:250]

        filepath = write_pathway_analysis(
            pathway_key=pathway_key,
            genes=genes,
            analysis=analysis,
            tldr=tldr,
            base_dir=base_dir,
        )

        return {
            "pathway": pathway_key,
            "status": "success",
            "filepath": str(filepath),
            "gene_count": len(genes),
            "tldr": tldr,
        }

    except Exception as e:
        logger.error(f"Failed pathway {pathway_key}: {e}")
        return {"pathway": pathway_key, "status": "error", "error": str(e)}


async def run(client: GeminiClient, ctx: CropContext = None) -> dict:
    """Execute Stage 2: Pathway Analysis.

    Args:
        client: GeminiClient instance.
        ctx: Optional CropContext. When provided, reads targets and gene analyses
             from crop-specific paths and writes pathway files to crop-specific
             directories. Falls back to legacy shared paths when None.

    Returns:
        Summary dict with results.
    """
    logger.info("=" * 60)
    logger.info("STAGE 2: PATHWAY ANALYSIS")
    logger.info("=" * 60)

    from agents.qc import preflight_check
    preflight_check(ctx.crop if ctx else "spinach", "pathway_mapping")

    if ctx is not None:
        ctx.ensure_dirs()
        targets = ctx.load_targets()
        priority_dirs = {
            "high": ctx.kb_targets_high,
            "medium": ctx.kb_targets_medium,
            "low": ctx.kb_targets_low,
        }
        pathways_base_dir = ctx.kb_pathways
        index_pathways_dir = ctx.kb_pathways
        index_research_dir = ctx.kb_research
    else:
        targets = load_targets()
        priority_dirs = None
        pathways_base_dir = None
        index_pathways_dir = None
        index_research_dir = None

    pathway_groups = group_by_pathway(targets)
    logger.info(f"Found {len(pathway_groups)} pathway groups")

    # Load existing gene analyses for context
    gene_analyses = load_gene_analyses(targets, priority_dirs=priority_dirs)
    logger.info(f"Loaded {len(gene_analyses)} existing gene analyses")

    start_time = datetime.now()

    # Phase 1: Analyze each pathway
    logger.info("Phase 1: Analyzing individual pathways...")
    pathway_tasks = [
        analyze_pathway(client, key, genes, gene_analyses, base_dir=pathways_base_dir)
        for key, genes in pathway_groups.items()
    ]
    pathway_results = await asyncio.gather(*pathway_tasks)

    successes = [r for r in pathway_results if r["status"] == "success"]
    failures = [r for r in pathway_results if r["status"] == "error"]

    # Phase 2: Cross-pathway analysis
    logger.info("Phase 2: Cross-pathway interaction analysis...")
    pathway_summaries = ""
    for r in successes:
        pathway_summaries += f"\n### {r['pathway']}\n{r.get('tldr', 'No summary')}\nGenes: {r['gene_count']}\n"

    try:
        cross_analysis = await client.query_reasoning(
            prompt=cross_pathway_prompt(pathway_summaries),
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=8192,
        )
        # Strip LLM preamble
        cross_analysis = strip_llm_preamble(cross_analysis)
        write_cross_pathway_analysis(cross_analysis, base_dir=pathways_base_dir)
    except Exception as e:
        logger.error(f"Cross-pathway analysis failed: {e}")

    duration = (datetime.now() - start_time).total_seconds()

    # Update pathway index
    pathway_info = {}
    for r in successes:
        key = r["pathway"]
        _, filename = PATHWAY_FILE_MAP.get(key, (key, f"{key}.md"))
        pathway_info[key] = {
            "filename": filename,
            "gene_count": r["gene_count"],
            "tldr": r.get("tldr", ""),
        }
    update_pathways_index(pathway_info, base_dir=index_pathways_dir)

    stats = client.get_stats()
    logger.info(f"Stage 2 complete in {duration:.0f}s")

    return {
        "stage": "pathway_mapping",
        "pathways_total": len(pathway_groups),
        "pathways_succeeded": len(successes),
        "pathways_failed": len(failures),
        "duration_seconds": duration,
        "api_stats": stats,
    }
