"""Stage 5: Claude-powered synthesis of all prior stage outputs.

Produces per-crop synthesis in crops/{crop}/synthesis/:
- ranked_targets.md
- causal_models.md
- confounders.md
- validation_plan.md

Uses ClaudeClient.query_synthesis() (Sonnet) for most tasks,
query_reasoning() (Opus) for critical review.
"""

import asyncio
import json
import logging
import time
from pathlib import Path

from agents.config import (
    KB_TARGETS, KB_PATHWAYS, KB_THEMES,
    KB_RESEARCH, ORGANISM, TREATMENT, PHENOTYPE, MECHANISM,
    CROPS_DIR, PROJECT_ROOT,
)
from agents.crop_context import CropContext, strip_llm_preamble
from agents.claude_client import ClaudeClient
from agents.prompts.claude_synthesis import (
    SYNTHESIS_SYSTEM,
    ranked_targets_prompt,
    causal_models_prompt,
    confounder_analysis_prompt,
    validation_plan_prompt,
)

logger = logging.getLogger(__name__)


def _get_crop_context(crop: str) -> dict:
    """Load crop metadata for synthesis prompts."""
    meta_path = CROPS_DIR / crop / "crop_metadata.json"
    if meta_path.exists():
        return json.loads(meta_path.read_text())
    return {"species": ORGANISM, "common_name": crop, "treatment": TREATMENT}


def _get_output_dir(crop: str, ctx: CropContext = None) -> Path:
    """Get the synthesis output directory for a crop."""
    if ctx is not None:
        ctx.kb_synthesis.mkdir(parents=True, exist_ok=True)
        return ctx.kb_synthesis
    output_dir = CROPS_DIR / crop / "synthesis"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def _resolve_targets_dir(ctx: CropContext = None) -> Path:
    """Get the targets directory, preferring crop-specific when available."""
    if ctx is not None:
        return ctx.kb_targets
    return KB_TARGETS


def _resolve_pathways_dir(ctx: CropContext = None) -> Path:
    """Get the pathways directory, preferring crop-specific when available."""
    if ctx is not None:
        return ctx.kb_pathways
    return KB_PATHWAYS


def _resolve_themes_dir(ctx: CropContext = None) -> Path:
    """Get the themes directory, preferring crop-specific when available."""
    if ctx is not None:
        return ctx.kb_themes
    return KB_THEMES


def _load_tldr_summaries(directory: Path, max_files: int = 120) -> str:
    """Load TL;DR lines from all markdown files in a directory tree."""
    summaries = []
    count = 0
    if not directory.exists():
        return ""
    for md_file in sorted(directory.rglob("*.md")):
        if md_file.name == "INDEX.md" or count >= max_files:
            continue
        try:
            text = md_file.read_text()
            for line in text.split("\n"):
                if line.strip().startswith("> TL;DR:"):
                    header = text.split("\n")[0].strip("# ").strip()
                    summaries.append(f"**{header}**: {line.strip('> TL;DR: ').strip()}")
                    break
            count += 1
        except Exception as e:
            logger.warning(f"Could not read {md_file}: {e}")

    return "\n".join(summaries)


def _load_full_analyses(directory: Path, max_files: int = 20) -> str:
    """Load full content from markdown files (for smaller collections)."""
    texts = []
    count = 0
    if not directory.exists():
        return ""
    for md_file in sorted(directory.rglob("*.md")):
        if md_file.name == "INDEX.md" or count >= max_files:
            continue
        try:
            content = md_file.read_text()
            if len(content) > 3000:
                content = content[:3000] + "\n[... truncated]"
            texts.append(content)
            count += 1
        except Exception as e:
            logger.warning(f"Could not read {md_file}: {e}")

    return "\n\n---\n\n".join(texts)


async def synthesize_ranked_targets(
    client: ClaudeClient, crop: str, ctx: CropContext = None,
) -> dict:
    """Produce comprehensive target ranking for a specific crop."""
    meta = _get_crop_context(crop) if ctx is None else ctx.metadata
    output_dir = _get_output_dir(crop, ctx=ctx)
    species = meta.get("species", ORGANISM)
    common_name = meta.get("common_name", crop)

    logger.info(f"Synthesizing ranked targets for {crop} ({species})...")

    targets_dir = _resolve_targets_dir(ctx)
    pathways_dir = _resolve_pathways_dir(ctx)

    target_summaries = _load_tldr_summaries(targets_dir)
    pathway_summaries = _load_full_analyses(pathways_dir, max_files=15)

    from agents.qc import validate_non_empty_string, validate_loaded_data_gene_ids, CostGate
    validate_non_empty_string(target_summaries, f"target summaries for '{crop}'", min_chars=200)
    validate_loaded_data_gene_ids(target_summaries, crop)

    prompt = f"Crop: {species} ({common_name})\n\n" + ranked_targets_prompt(target_summaries, pathway_summaries)
    CostGate.check("claude-sonnet", f"ranked targets for {crop}", len(prompt))
    response = await client.query_synthesis(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    output_path = output_dir / "ranked_targets.md"
    output_path.write_text(f"# Ranked Target Analysis -- {common_name.title()} ({species})\n\n{response}")
    logger.info(f"Wrote ranked targets: {output_path}")

    return {"file": str(output_path), "length": len(response)}


async def synthesize_causal_models(
    client: ClaudeClient, crop: str, ctx: CropContext = None,
) -> dict:
    """Build alternative causal models for a specific crop."""
    meta = _get_crop_context(crop) if ctx is None else ctx.metadata
    output_dir = _get_output_dir(crop, ctx=ctx)
    species = meta.get("species", ORGANISM)
    common_name = meta.get("common_name", crop)

    logger.info(f"Synthesizing causal models for {crop}...")

    ranked_targets = ""
    rt_path = output_dir / "ranked_targets.md"
    if rt_path.exists():
        ranked_targets = rt_path.read_text()[:5000]

    pathways_dir = _resolve_pathways_dir(ctx)
    themes_dir = _resolve_themes_dir(ctx)

    pathway_analyses = _load_full_analyses(pathways_dir, max_files=15)
    theme_analyses = _load_full_analyses(themes_dir, max_files=6)

    from agents.qc import validate_non_empty_string, validate_loaded_data_gene_ids, CostGate
    combined = ranked_targets + pathway_analyses + theme_analyses
    validate_non_empty_string(combined, f"causal model inputs for '{crop}'", min_chars=200)
    validate_loaded_data_gene_ids(combined, crop)

    prompt = f"Crop: {species} ({common_name})\n\n" + causal_models_prompt(ranked_targets, pathway_analyses, theme_analyses)
    CostGate.check("claude-opus", f"causal models for {crop}", len(prompt))

    response = await client.query_reasoning(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    output_path = output_dir / "causal_models.md"
    output_path.write_text(f"# Causal Models -- {common_name.title()} ({species})\n\n{response}")
    logger.info(f"Wrote causal models: {output_path}")

    return {"file": str(output_path), "length": len(response)}


async def synthesize_confounders(
    client: ClaudeClient, crop: str, ctx: CropContext = None,
) -> dict:
    """Analyze potential confounders for a specific crop."""
    meta = _get_crop_context(crop) if ctx is None else ctx.metadata
    output_dir = _get_output_dir(crop, ctx=ctx)
    species = meta.get("species", ORGANISM)
    common_name = meta.get("common_name", crop)
    total = meta.get("total_targets", 0)

    logger.info(f"Analyzing confounders for {crop}...")

    context = f"""Organism: {species} ({common_name})
Treatment: {meta.get('treatment', TREATMENT)}
Phenotype: {PHENOTYPE}
Mechanism: {MECHANISM}
Total targets: {total}
Key pathways: hormone signaling, defense/immunity, epigenetic regulation,
ROS/redox, transport/ion homeostasis, metabolic priming"""

    from agents.qc import validate_non_empty_string, CostGate
    validate_non_empty_string(context, f"confounder context for '{crop}'", min_chars=50)

    prompt = confounder_analysis_prompt(context)
    CostGate.check("claude-opus", f"confounders for {crop}", len(prompt))
    response = await client.query_reasoning(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    output_path = output_dir / "confounders.md"
    output_path.write_text(f"# Confounder Analysis -- {common_name.title()} ({species})\n\n{response}")
    logger.info(f"Wrote confounder analysis: {output_path}")

    return {"file": str(output_path), "length": len(response)}


async def synthesize_validation_plan(
    client: ClaudeClient, crop: str, ctx: CropContext = None,
) -> dict:
    """Design the 4-tier validation experimental plan for a specific crop."""
    output_dir = _get_output_dir(crop, ctx=ctx)
    meta = _get_crop_context(crop) if ctx is None else ctx.metadata
    species = meta.get("species", ORGANISM)
    common_name = meta.get("common_name", crop)

    logger.info(f"Designing validation plan for {crop}...")

    ranked = ""
    rt_path = output_dir / "ranked_targets.md"
    if rt_path.exists():
        ranked = rt_path.read_text()[:5000]

    causal = ""
    cm_path = output_dir / "causal_models.md"
    if cm_path.exists():
        causal = cm_path.read_text()[:5000]

    confounders = ""
    cf_path = output_dir / "confounders.md"
    if cf_path.exists():
        confounders = cf_path.read_text()[:5000]

    from agents.qc import validate_non_empty_string, CostGate
    combined = ranked + causal + confounders
    validate_non_empty_string(combined, f"validation plan inputs for '{crop}'", min_chars=200)

    prompt = f"Crop: {species} ({common_name})\n\n" + validation_plan_prompt(ranked, causal, confounders)
    CostGate.check("claude-sonnet", f"validation plan for {crop}", len(prompt))
    response = await client.query_synthesis(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    output_path = output_dir / "validation_plan.md"
    output_path.write_text(f"# Validation Plan -- {common_name.title()} ({species})\n\n{response}")
    logger.info(f"Wrote validation plan: {output_path}")

    return {"file": str(output_path), "length": len(response)}


async def run(
    client: ClaudeClient,
    crop: str = "spinach",
    ctx: CropContext = None,
) -> dict:
    """Execute the full Stage 5 synthesis pipeline for a specific crop.

    Args:
        client: ClaudeClient instance.
        crop: Crop name (used when ctx is None for legacy compatibility).
        ctx: Optional CropContext. When provided, reads from crop-specific
             knowledge base directories and writes synthesis output to
             crop-specific paths. Falls back to legacy shared paths when None.

    Order matters: ranked_targets -> (causal_models + confounders) -> validation_plan.
    """
    if ctx is not None:
        ctx.ensure_dirs()
        crop = ctx.crop

    from agents.qc import preflight_check
    preflight_check(crop, "synthesis")

    start = time.time()
    results = {"crop": crop}

    # Phase 1: Ranked targets (needed by later phases)
    results["ranked_targets"] = await synthesize_ranked_targets(client, crop, ctx=ctx)

    # Phase 2: Causal models + Confounders (parallel)
    causal_task = synthesize_causal_models(client, crop, ctx=ctx)
    confounder_task = synthesize_confounders(client, crop, ctx=ctx)
    causal_result, confounder_result = await asyncio.gather(
        causal_task, confounder_task
    )
    results["causal_models"] = causal_result
    results["confounders"] = confounder_result

    # Phase 3: Validation plan (depends on all above)
    results["validation_plan"] = await synthesize_validation_plan(client, crop, ctx=ctx)

    duration = time.time() - start
    results["duration_seconds"] = round(duration, 1)
    results["api_stats"] = client.get_stats()

    logger.info(f"Stage 5 synthesis for {crop} complete in {duration:.0f}s")
    return results
