"""Stage 1: Batch gene analysis - analyze all ~100 targets in parallel."""

import asyncio
import json
import logging
from datetime import date, datetime

from agents.config import TARGETS_CONFIG, KB_RESEARCH_LIT
from agents.crop_context import CropContext, strip_llm_preamble
from agents.gemini_client import GeminiClient
from agents.prompts.gene_analysis import (
    SYSTEM_INSTRUCTION,
    single_gene_prompt,
    batch_gene_summary_prompt,
    priority_ranking_prompt,
)
from agents.writers.target_writer import write_target_analysis, write_batch_summary
from agents.writers.index_writer import update_targets_index, update_research_index

logger = logging.getLogger(__name__)

BATCH_SIZE = 10  # Genes per batch for summary analysis


def load_targets() -> list[dict]:
    """Load gene targets from config file (legacy fallback)."""
    with open(TARGETS_CONFIG) as f:
        data = json.load(f)
    return data["targets"]


async def analyze_single_gene(
    client: GeminiClient,
    gene: dict,
    base_dir=None,
) -> dict:
    """Run deep analysis on a single gene target."""
    prompt = single_gene_prompt(
        gene_id=gene["gene_id"],
        annotation=gene["annotation"],
        pathway=gene["pathway"],
    )

    try:
        analysis = await client.query_bulk(
            prompt=prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=4096,
        )

        # Strip LLM preamble before further processing
        analysis = strip_llm_preamble(analysis)

        # Extract a TL;DR from the first paragraph
        lines = [l.strip() for l in analysis.split("\n") if l.strip() and not l.startswith("#")]
        tldr = " ".join(lines[:2])[:250]

        # Write the analysis file
        filepath = write_target_analysis(
            gene_id=gene["gene_id"],
            annotation=gene["annotation"],
            pathway=gene["pathway"],
            priority=gene["priority"],
            analysis=analysis,
            tldr=tldr,
            base_dir=base_dir,
        )

        return {
            "gene_id": gene["gene_id"],
            "status": "success",
            "filepath": str(filepath),
            "tldr": tldr,
            "priority": gene["priority"],
        }

    except Exception as e:
        logger.error(f"Failed to analyze {gene['gene_id']}: {e}")
        return {
            "gene_id": gene["gene_id"],
            "status": "error",
            "error": str(e),
            "priority": gene["priority"],
        }


async def analyze_batch_summary(
    client: GeminiClient,
    genes: list[dict],
    batch_id: int,
    batch_base_dir=None,
) -> dict:
    """Run batch summary analysis on a group of genes."""
    prompt = batch_gene_summary_prompt(genes)

    try:
        analysis = await client.query_bulk(
            prompt=prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=4096,
        )

        # Strip LLM preamble
        analysis = strip_llm_preamble(analysis)

        filepath = write_batch_summary(
            genes, analysis, batch_id, base_dir=batch_base_dir,
        )

        return {
            "batch_id": batch_id,
            "status": "success",
            "filepath": str(filepath),
            "gene_count": len(genes),
        }

    except Exception as e:
        logger.error(f"Failed batch {batch_id}: {e}")
        return {"batch_id": batch_id, "status": "error", "error": str(e)}


async def run(client: GeminiClient, ctx: CropContext = None) -> dict:
    """Execute Stage 1: Batch Gene Analysis.

    Args:
        client: GeminiClient instance.
        ctx: Optional CropContext. When provided, reads targets from the
             crop-specific config and writes to crop-specific directories.
             Falls back to legacy shared paths when None.

    Returns:
        Summary dict with results.
    """
    logger.info("=" * 60)
    logger.info("STAGE 1: BATCH GENE ANALYSIS")
    logger.info("=" * 60)

    if ctx is not None:
        ctx.ensure_dirs()
        targets = ctx.load_targets()
        targets_base_dir = ctx.kb_targets
        batch_base_dir = ctx.kb_research_lit
        index_targets_dir = ctx.kb_targets
        index_research_dir = ctx.kb_research
    else:
        targets = load_targets()
        targets_base_dir = None
        batch_base_dir = None
        index_targets_dir = None
        index_research_dir = None

    logger.info(f"Loaded {len(targets)} targets from config")

    start_time = datetime.now()

    # Phase 1: Individual gene analyses (all in parallel)
    logger.info(f"Phase 1: Analyzing {len(targets)} individual genes...")
    individual_tasks = [
        analyze_single_gene(client, gene, base_dir=targets_base_dir)
        for gene in targets
    ]
    individual_results = await asyncio.gather(*individual_tasks)

    successes = [r for r in individual_results if r["status"] == "success"]
    failures = [r for r in individual_results if r["status"] == "error"]
    logger.info(f"Individual analysis: {len(successes)} succeeded, {len(failures)} failed")

    # Phase 2: Batch summaries (groups of BATCH_SIZE)
    logger.info(f"Phase 2: Running batch summaries (batch size {BATCH_SIZE})...")
    batches = [targets[i:i + BATCH_SIZE] for i in range(0, len(targets), BATCH_SIZE)]
    batch_tasks = [
        analyze_batch_summary(client, batch, idx, batch_base_dir=batch_base_dir)
        for idx, batch in enumerate(batches)
    ]
    batch_results = await asyncio.gather(*batch_tasks)

    duration = (datetime.now() - start_time).total_seconds()

    # Update indexes
    analyses_written = {
        r["gene_id"]: r for r in individual_results if r["status"] == "success"
    }
    update_targets_index(targets, analyses_written, base_dir=index_targets_dir)

    update_research_index(
        [{
            "date": date.today().isoformat(),
            "stage": "gene_analysis",
            "description": f"Analyzed {len(targets)} gene targets individually + {len(batches)} batch summaries",
            "output_dir": "targets/, research/literature/",
            "status": f"{len(successes)}/{len(targets)} succeeded ({duration:.0f}s)",
        }],
        base_dir=index_research_dir,
    )

    stats = client.get_stats()
    logger.info(f"Stage 1 complete in {duration:.0f}s")
    logger.info(f"API stats: {stats['total_requests']} requests, {stats['total_tokens_used']} tokens")

    return {
        "stage": "gene_analysis",
        "targets_total": len(targets),
        "individual_successes": len(successes),
        "individual_failures": len(failures),
        "batch_summaries": len(batch_results),
        "duration_seconds": duration,
        "api_stats": stats,
        "failed_genes": [r["gene_id"] for r in failures],
    }
