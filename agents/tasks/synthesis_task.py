"""Stage 5: Claude-powered synthesis of all prior stage outputs.

Reads target analyses, pathway mappings, themes, and literature to produce:
- Ranked targets (knowledge_base/synthesis/ranked_targets.md)
- Causal models (knowledge_base/synthesis/causal_models.md)
- Confounder analysis (knowledge_base/synthesis/confounders.md)
- Validation plan (knowledge_base/synthesis/validation_plan.md)

Uses ClaudeClient.query_synthesis() (Sonnet) for most tasks,
query_reasoning() (Opus) for critical review.
"""

import asyncio
import logging
import time
from pathlib import Path

from agents.config import (
    KB_TARGETS, KB_PATHWAYS, KB_THEMES, KB_SYNTHESIS,
    KB_RESEARCH, ORGANISM, TREATMENT, PHENOTYPE, MECHANISM,
)
from agents.claude_client import ClaudeClient
from agents.prompts.claude_synthesis import (
    SYNTHESIS_SYSTEM,
    ranked_targets_prompt,
    causal_models_prompt,
    confounder_analysis_prompt,
    validation_plan_prompt,
)

logger = logging.getLogger(__name__)


def _load_tldr_summaries(directory: Path, max_files: int = 120) -> str:
    """Load TL;DR lines from all markdown files in a directory tree."""
    summaries = []
    count = 0
    for md_file in sorted(directory.rglob("*.md")):
        if md_file.name == "INDEX.md" or count >= max_files:
            continue
        try:
            text = md_file.read_text()
            # Extract TL;DR line
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
    for md_file in sorted(directory.rglob("*.md")):
        if md_file.name == "INDEX.md" or count >= max_files:
            continue
        try:
            content = md_file.read_text()
            # Truncate very long files
            if len(content) > 3000:
                content = content[:3000] + "\n[... truncated]"
            texts.append(content)
            count += 1
        except Exception:
            pass

    return "\n\n---\n\n".join(texts)


async def synthesize_ranked_targets(client: ClaudeClient) -> dict:
    """Produce comprehensive target ranking."""
    logger.info("Synthesizing ranked targets...")

    target_summaries = _load_tldr_summaries(KB_TARGETS)
    pathway_summaries = _load_full_analyses(KB_PATHWAYS, max_files=15)

    prompt = ranked_targets_prompt(target_summaries, pathway_summaries)
    response = await client.query_synthesis(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    output_path = KB_SYNTHESIS / "ranked_targets.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(f"# Ranked Target Analysis\n\n{response}")
    logger.info(f"Wrote ranked targets: {output_path}")

    return {"file": str(output_path), "length": len(response)}


async def synthesize_causal_models(client: ClaudeClient) -> dict:
    """Build alternative causal models."""
    logger.info("Synthesizing causal models...")

    ranked_targets = ""
    rt_path = KB_SYNTHESIS / "ranked_targets.md"
    if rt_path.exists():
        ranked_targets = rt_path.read_text()[:5000]

    pathway_analyses = _load_full_analyses(KB_PATHWAYS, max_files=15)
    theme_analyses = _load_full_analyses(KB_THEMES, max_files=6)

    prompt = causal_models_prompt(ranked_targets, pathway_analyses, theme_analyses)

    # Use Opus for critical model-building
    response = await client.query_reasoning(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    output_path = KB_SYNTHESIS / "causal_models.md"
    output_path.write_text(f"# Causal Models\n\n{response}")
    logger.info(f"Wrote causal models: {output_path}")

    return {"file": str(output_path), "length": len(response)}


async def synthesize_confounders(client: ClaudeClient) -> dict:
    """Analyze potential confounders."""
    logger.info("Analyzing confounders...")

    context = f"""Organism: {ORGANISM}
Treatment: {TREATMENT}
Phenotype: {PHENOTYPE}
Mechanism: {MECHANISM}
Total targets: 109 (21 high, 49 medium, 39 low priority)
Key pathways: hormone signaling, defense/immunity, epigenetic regulation,
ROS/redox, transport/ion homeostasis, metabolic priming
Notable: cry8Ba bacterial protein detected in preparation"""

    prompt = confounder_analysis_prompt(context)
    response = await client.query_reasoning(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    output_path = KB_SYNTHESIS / "confounders.md"
    output_path.write_text(f"# Confounder Analysis\n\n{response}")
    logger.info(f"Wrote confounder analysis: {output_path}")

    return {"file": str(output_path), "length": len(response)}


async def synthesize_validation_plan(client: ClaudeClient) -> dict:
    """Design the 4-tier validation experimental plan."""
    logger.info("Designing validation plan...")

    ranked = ""
    rt_path = KB_SYNTHESIS / "ranked_targets.md"
    if rt_path.exists():
        ranked = rt_path.read_text()[:5000]

    causal = ""
    cm_path = KB_SYNTHESIS / "causal_models.md"
    if cm_path.exists():
        causal = cm_path.read_text()[:5000]

    confounders = ""
    cf_path = KB_SYNTHESIS / "confounders.md"
    if cf_path.exists():
        confounders = cf_path.read_text()[:5000]

    prompt = validation_plan_prompt(ranked, causal, confounders)
    response = await client.query_synthesis(
        prompt=prompt,
        system_instruction=SYNTHESIS_SYSTEM,
        max_output_tokens=16384,
    )

    output_path = KB_SYNTHESIS / "validation_plan.md"
    output_path.write_text(f"# Validation Plan\n\n{response}")
    logger.info(f"Wrote validation plan: {output_path}")

    return {"file": str(output_path), "length": len(response)}


async def run(client: ClaudeClient) -> dict:
    """Execute the full Stage 5 synthesis pipeline.

    Order matters: ranked_targets → (causal_models + confounders) → validation_plan.
    """
    start = time.time()
    results = {}

    # Phase 1: Ranked targets (needed by later phases)
    results["ranked_targets"] = await synthesize_ranked_targets(client)

    # Phase 2: Causal models + Confounders (parallel, both use ranked targets)
    causal_task = synthesize_causal_models(client)
    confounder_task = synthesize_confounders(client)
    causal_result, confounder_result = await asyncio.gather(
        causal_task, confounder_task
    )
    results["causal_models"] = causal_result
    results["confounders"] = confounder_result

    # Phase 3: Validation plan (depends on all above)
    results["validation_plan"] = await synthesize_validation_plan(client)

    duration = time.time() - start
    results["duration_seconds"] = round(duration, 1)
    results["api_stats"] = client.get_stats()

    logger.info(f"Stage 5 synthesis complete in {duration:.0f}s")
    return results
