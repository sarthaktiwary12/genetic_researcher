"""Stage 3: Literature deep-dive for high-priority targets."""

import asyncio
import json
import logging
from datetime import date, datetime
from pathlib import Path

from agents.config import (
    TARGETS_CONFIG,
    KB_TARGETS_HIGH,
    KB_RESEARCH_LIT,
    KB_RESEARCH_HOMOLOGS,
    KB_RESEARCH_MECHANISMS,
)
from agents.crop_context import CropContext, strip_llm_preamble
from agents.gemini_client import GeminiClient
from agents.prompts.literature_search import (
    SYSTEM_INSTRUCTION,
    homolog_search_prompt,
    literature_deep_dive_prompt,
    exrna_biology_prompt,
)
from agents.writers.index_writer import update_research_index

logger = logging.getLogger(__name__)


def load_high_priority_targets() -> list[dict]:
    """Load only high-priority targets from config (legacy fallback)."""
    with open(TARGETS_CONFIG) as f:
        data = json.load(f)
    return [t for t in data["targets"] if t["priority"] == "high"]


def load_existing_analysis(gene_id: str, targets_high_dir: Path = None) -> str:
    """Load existing analysis for a gene to provide context for deep dive.

    Args:
        gene_id: The gene identifier.
        targets_high_dir: Optional directory to search for high-priority analyses.
                          Falls back to KB_TARGETS_HIGH when None.
    """
    search_dir = targets_high_dir if targets_high_dir is not None else KB_TARGETS_HIGH
    if not search_dir.exists():
        return ""
    for f in search_dir.glob(f"{gene_id.replace('.', '_')}*.md"):
        try:
            return f.read_text()[:2000]  # First 2000 chars
        except Exception:
            pass
    return ""


async def homolog_research(
    client: GeminiClient,
    gene: dict,
    homologs_dir: Path = None,
) -> dict:
    """Research homologs for a single gene."""
    prompt = homolog_search_prompt(gene["gene_id"], gene["annotation"])

    output_dir = homologs_dir if homologs_dir is not None else KB_RESEARCH_HOMOLOGS

    try:
        result = await client.query_bulk(
            prompt=prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=4096,
        )

        # Strip LLM preamble
        result = strip_llm_preamble(result)

        filepath = output_dir / f"{gene['gene_id'].replace('.', '_')}_homologs.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)

        content = f"""# Homolog Research: {gene['gene_id']} - {gene['annotation']}
> TL;DR: Homolog analysis for {gene['annotation']}
> Last Updated: {date.today().isoformat()}

{result}
"""
        filepath.write_text(content)

        return {"gene_id": gene["gene_id"], "status": "success", "type": "homolog"}

    except Exception as e:
        logger.error(f"Homolog research failed for {gene['gene_id']}: {e}")
        return {"gene_id": gene["gene_id"], "status": "error", "error": str(e)}


async def deep_literature_research(
    client: GeminiClient,
    gene: dict,
    targets_high_dir: Path = None,
    mechanisms_dir: Path = None,
) -> dict:
    """Deep literature dive for a single gene."""
    existing_analysis = load_existing_analysis(
        gene["gene_id"], targets_high_dir=targets_high_dir,
    )
    prompt = literature_deep_dive_prompt(
        gene["gene_id"], gene["annotation"], existing_analysis
    )

    output_dir = mechanisms_dir if mechanisms_dir is not None else KB_RESEARCH_MECHANISMS

    try:
        result = await client.query_reasoning(
            prompt=prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=8192,
        )

        # Strip LLM preamble
        result = strip_llm_preamble(result)

        filepath = output_dir / f"{gene['gene_id'].replace('.', '_')}_deep_dive.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)

        content = f"""# Deep Literature Dive: {gene['gene_id']} - {gene['annotation']}
> TL;DR: Comprehensive literature review for {gene['annotation']}
> Priority: High
> Last Updated: {date.today().isoformat()}

{result}
"""
        filepath.write_text(content)

        return {"gene_id": gene["gene_id"], "status": "success", "type": "deep_dive"}

    except Exception as e:
        logger.error(f"Deep dive failed for {gene['gene_id']}: {e}")
        return {"gene_id": gene["gene_id"], "status": "error", "error": str(e)}


async def exrna_background_research(
    client: GeminiClient,
    lit_dir: Path = None,
) -> dict:
    """Research cross-kingdom exRNA biology fundamentals."""
    prompt = exrna_biology_prompt()

    output_dir = lit_dir if lit_dir is not None else KB_RESEARCH_LIT

    try:
        result = await client.query_reasoning(
            prompt=prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=8192,
        )

        # Strip LLM preamble
        result = strip_llm_preamble(result)

        filepath = output_dir / "exrna_biology_background.md"
        filepath.parent.mkdir(parents=True, exist_ok=True)

        content = f"""# Cross-Kingdom Extracellular RNA Biology
> TL;DR: Background review of exRNA biology relevant to plant-bacteria interactions and seed treatment.
> Last Updated: {date.today().isoformat()}

{result}
"""
        filepath.write_text(content)

        return {"status": "success", "type": "exrna_background"}

    except Exception as e:
        logger.error(f"exRNA background research failed: {e}")
        return {"status": "error", "error": str(e)}


async def run(client: GeminiClient, ctx: CropContext = None) -> dict:
    """Execute Stage 3: Literature Deep-Dive.

    Args:
        client: GeminiClient instance.
        ctx: Optional CropContext. When provided, reads targets from
             crop-specific config and writes to crop-specific research
             directories. Falls back to legacy shared paths when None.

    Returns:
        Summary dict with results.
    """
    logger.info("=" * 60)
    logger.info("STAGE 3: LITERATURE DEEP-DIVE")
    logger.info("=" * 60)

    from agents.qc import preflight_check
    preflight_check(ctx.crop if ctx else "spinach", "literature_dive")

    if ctx is not None:
        ctx.ensure_dirs()
        all_targets = ctx.load_targets()
        high_targets = [t for t in all_targets if t["priority"] == "high"]
        targets_high_dir = ctx.kb_targets_high
        homologs_dir = ctx.kb_research_homologs
        mechanisms_dir = ctx.kb_research_mechanisms
        lit_dir = ctx.kb_research_lit
        index_research_dir = ctx.kb_research
    else:
        high_targets = load_high_priority_targets()
        targets_high_dir = None
        homologs_dir = None
        mechanisms_dir = None
        lit_dir = None
        index_research_dir = None

    if len(high_targets) == 0:
        raise RuntimeError("0 high-priority targets. Stage 3 has nothing to analyze.")
    logger.info(f"Found {len(high_targets)} high-priority targets for deep dive")

    start_time = datetime.now()

    # Phase 1: Homolog research for all high-priority targets
    logger.info("Phase 1: Homolog research...")
    homolog_tasks = [
        homolog_research(client, gene, homologs_dir=homologs_dir)
        for gene in high_targets
    ]

    # Phase 2: Deep literature dive for all high-priority targets
    logger.info("Phase 2: Deep literature dives...")
    deep_tasks = [
        deep_literature_research(
            client, gene,
            targets_high_dir=targets_high_dir,
            mechanisms_dir=mechanisms_dir,
        )
        for gene in high_targets
    ]

    # Phase 3: exRNA background (single query)
    logger.info("Phase 3: exRNA biology background...")

    # Run all phases in parallel
    all_tasks = homolog_tasks + deep_tasks + [
        exrna_background_research(client, lit_dir=lit_dir)
    ]
    all_results = await asyncio.gather(*all_tasks)

    homolog_results = all_results[:len(high_targets)]
    deep_results = all_results[len(high_targets):2 * len(high_targets)]
    exrna_result = all_results[-1]

    duration = (datetime.now() - start_time).total_seconds()

    homolog_successes = sum(1 for r in homolog_results if r["status"] == "success")
    deep_successes = sum(1 for r in deep_results if r["status"] == "success")

    stats = client.get_stats()
    logger.info(f"Stage 3 complete in {duration:.0f}s")
    logger.info(f"Homologs: {homolog_successes}/{len(high_targets)}, Deep dives: {deep_successes}/{len(high_targets)}")

    return {
        "stage": "literature_dive",
        "high_priority_targets": len(high_targets),
        "homolog_successes": homolog_successes,
        "deep_dive_successes": deep_successes,
        "exrna_background": exrna_result["status"],
        "duration_seconds": duration,
        "api_stats": stats,
    }
