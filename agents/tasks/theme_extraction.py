"""Stage 4: Theme extraction - identify cross-cutting themes across all targets."""

import asyncio
import json
import logging
from datetime import date, datetime
from pathlib import Path

from agents.config import (
    TARGETS_CONFIG,
    KB_TARGETS,
    KB_PATHWAYS,
    KB_THEMES,
    KB_SYNTHESIS,
    KNOWLEDGE_BASE,
)
from agents.crop_context import CropContext, strip_llm_preamble
from agents.gemini_client import GeminiClient
from agents.prompts.theme_synthesis import (
    SYSTEM_INSTRUCTION,
    theme_extraction_prompt,
    validation_plan_prompt,
)
from agents.prompts.mechanism_analysis import (
    SYSTEM_INSTRUCTION as MECHANISM_SYSTEM,
    causal_model_prompt,
    confounder_analysis_prompt,
)
from agents.writers.index_writer import (
    update_themes_index,
    update_master_index,
)

logger = logging.getLogger(__name__)

THEME_FILES = {
    "Defense Downshift": "defense_downshift.md",
    "Epigenetic Remodeling": "epigenetic_remodeling.md",
    "ROS Optimization": "ros_optimization.md",
    "Hormone Nodes": "hormone_nodes.md",
    "Transport / Ion Homeostasis": "transport_ion_homeostasis.md",
    "Metabolic Priming": "metabolic_priming.md",
}


def load_targets() -> list[dict]:
    """Load gene targets from config (legacy fallback)."""
    with open(TARGETS_CONFIG) as f:
        data = json.load(f)
    return data["targets"]


def load_all_summaries(kb_targets_dir: Path = None) -> str:
    """Load TL;DR summaries from all target analysis files.

    Args:
        kb_targets_dir: Optional base directory for targets. Falls back to
                        KB_TARGETS when None.
    """
    targets_dir = kb_targets_dir if kb_targets_dir is not None else KB_TARGETS
    summaries = []
    for priority_dir in ["high_priority", "medium_priority", "low_priority"]:
        dir_path = targets_dir / priority_dir
        if not dir_path.exists():
            continue
        for f in sorted(dir_path.glob("*.md")):
            try:
                content = f.read_text()
                # Extract TL;DR and first few meaningful lines
                lines = content.split("\n")
                header = ""
                tldr = ""
                for line in lines:
                    if line.startswith("# "):
                        header = line
                    elif line.startswith("> TL;DR:"):
                        tldr = line
                if header or tldr:
                    summaries.append(f"{header}\n{tldr}")
            except Exception as e:
                logger.warning(f"Could not read {f}: {e}")

    return "\n\n".join(summaries) if summaries else ""


def load_pathway_summaries(kb_pathways_dir: Path = None) -> str:
    """Load summaries from pathway analysis files.

    Args:
        kb_pathways_dir: Optional base directory for pathways. Falls back to
                         KB_PATHWAYS when None.
    """
    pathways_dir = kb_pathways_dir if kb_pathways_dir is not None else KB_PATHWAYS
    summaries = []
    if not pathways_dir.exists():
        return ""

    for f in sorted(pathways_dir.glob("*.md")):
        if f.name == "INDEX.md":
            continue
        try:
            content = f.read_text()
            lines = content.split("\n")
            header = ""
            tldr = ""
            for line in lines:
                if line.startswith("# "):
                    header = line
                elif line.startswith("> TL;DR:"):
                    tldr = line
            if header or tldr:
                summaries.append(f"{header}\n{tldr}")
        except Exception as e:
            logger.warning(f"Could not read {f}: {e}")

    return "\n\n".join(summaries) if summaries else ""


async def extract_themes(
    client: GeminiClient,
    gene_summaries: str,
    themes_dir: Path = None,
    synthesis_dir: Path = None,
) -> dict:
    """Extract biological themes from gene summaries."""
    prompt = theme_extraction_prompt(gene_summaries)

    out_themes = themes_dir if themes_dir is not None else KB_THEMES
    out_synthesis = synthesis_dir if synthesis_dir is not None else KB_SYNTHESIS

    try:
        result = await client.query_reasoning(
            prompt=prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=16384,
        )

        # Strip LLM preamble
        result = strip_llm_preamble(result)

        # Parse themes from result and write individual theme files
        # Write the full theme analysis
        themes_written = {}
        for theme_name, filename in THEME_FILES.items():
            filepath = out_themes / filename
            filepath.parent.mkdir(parents=True, exist_ok=True)

            # Extract the section for this theme from the result
            theme_section = _extract_theme_section(result, theme_name)

            content = f"""# {theme_name}
> TL;DR: Cross-cutting theme analysis for {theme_name.lower()} in exRNA-mediated germination improvement.
> Last Updated: {date.today().isoformat()}

{theme_section if theme_section else f"See full theme analysis for {theme_name} details."}
"""
            filepath.write_text(content)
            themes_written[theme_name] = {
                "filename": filename,
                "tldr": f"Theme analysis for {theme_name.lower()}",
            }

        # Write complete theme analysis to synthesis
        out_synthesis.mkdir(parents=True, exist_ok=True)
        full_themes_path = out_synthesis / "theme_analysis_full.md"
        full_content = f"""# Complete Theme Analysis
> TL;DR: Full cross-cutting theme extraction across all gene targets.
> Last Updated: {date.today().isoformat()}

{result}
"""
        full_themes_path.write_text(full_content)

        return {"status": "success", "themes": themes_written}

    except Exception as e:
        logger.error(f"Theme extraction failed: {e}")
        return {"status": "error", "error": str(e)}


async def build_causal_models(
    client: GeminiClient,
    gene_summaries: str,
    pathway_summaries: str,
    synthesis_dir: Path = None,
) -> dict:
    """Build causal models from targets to phenotype."""
    prompt = causal_model_prompt(gene_summaries, pathway_summaries)

    out_synthesis = synthesis_dir if synthesis_dir is not None else KB_SYNTHESIS

    try:
        result = await client.query_reasoning(
            prompt=prompt,
            system_instruction=MECHANISM_SYSTEM,
            max_output_tokens=16384,
        )

        # Strip LLM preamble
        result = strip_llm_preamble(result)

        out_synthesis.mkdir(parents=True, exist_ok=True)
        filepath = out_synthesis / "causal_models.md"
        content = f"""# Causal Models
> TL;DR: Mechanistic models linking bacterial exRNA targeting to germination improvement.
> Last Updated: {date.today().isoformat()}

{result}
"""
        filepath.write_text(content)

        return {"status": "success", "filepath": str(filepath)}

    except Exception as e:
        logger.error(f"Causal model building failed: {e}")
        return {"status": "error", "error": str(e)}


async def analyze_confounders(
    client: GeminiClient,
    synthesis_dir: Path = None,
    organism: str = "Spinacia oleracea",
    common_name: str = "spinach",
) -> dict:
    """Analyze confounding variables."""
    context = f"""Experiment: {common_name.capitalize()} ({organism}) seeds soaked in bacterial EPS solution "M-9" (4-8h until imbibition).
Control: Water-soaked seeds.
Phenotype: Improved germination rate, vigor, early seedling growth.
ExRNAs extracted from M-9 EPS, sequenced, antisense-aligned to {common_name} transcriptome.
~100 predicted target transcripts identified.
Key concern: Distinguishing exRNA effects from EPS/polysaccharide/microbiome effects."""

    prompt = confounder_analysis_prompt(context)

    out_synthesis = synthesis_dir if synthesis_dir is not None else KB_SYNTHESIS

    try:
        result = await client.query_reasoning(
            prompt=prompt,
            system_instruction=MECHANISM_SYSTEM,
            max_output_tokens=8192,
        )

        # Strip LLM preamble
        result = strip_llm_preamble(result)

        out_synthesis.mkdir(parents=True, exist_ok=True)
        filepath = out_synthesis / "confounders.md"
        content = f"""# Confounders & Alternative Explanations
> TL;DR: Critical analysis of confounding variables that could explain germination improvement independently of exRNA-mediated gene silencing.
> Last Updated: {date.today().isoformat()}

{result}
"""
        filepath.write_text(content)

        return {"status": "success", "filepath": str(filepath)}

    except Exception as e:
        logger.error(f"Confounder analysis failed: {e}")
        return {"status": "error", "error": str(e)}


async def design_validation_plan(
    client: GeminiClient,
    themes: str,
    causal_models: str,
    synthesis_dir: Path = None,
) -> dict:
    """Design experimental validation plan."""
    prompt = validation_plan_prompt(themes, causal_models)

    out_synthesis = synthesis_dir if synthesis_dir is not None else KB_SYNTHESIS

    try:
        result = await client.query_reasoning(
            prompt=prompt,
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=8192,
        )

        # Strip LLM preamble
        result = strip_llm_preamble(result)

        out_synthesis.mkdir(parents=True, exist_ok=True)
        filepath = out_synthesis / "validation_plan.md"
        content = f"""# Experimental Validation Plan
> TL;DR: Stepwise validation plan for testing the exRNA hypothesis with practical experiments.
> Last Updated: {date.today().isoformat()}

{result}
"""
        filepath.write_text(content)

        return {"status": "success", "filepath": str(filepath)}

    except Exception as e:
        logger.error(f"Validation plan design failed: {e}")
        return {"status": "error", "error": str(e)}


def _extract_theme_section(full_text: str, theme_name: str) -> str:
    """Extract a specific theme section from the full analysis text."""
    # Look for the theme header in various formats
    markers = [
        f"### THEME",
        f"### {theme_name}",
        f"## {theme_name}",
        theme_name.upper(),
    ]

    lines = full_text.split("\n")
    start_idx = None
    end_idx = None

    for i, line in enumerate(lines):
        if start_idx is None:
            for marker in markers:
                if marker.lower() in line.lower() and theme_name.lower().split()[0] in line.lower():
                    start_idx = i
                    break
        elif line.startswith("### THEME") or line.startswith("### OVERALL") or line.startswith("## THEME"):
            if theme_name.lower().split()[0] not in line.lower():
                end_idx = i
                break

    if start_idx is not None:
        end_idx = end_idx or len(lines)
        return "\n".join(lines[start_idx:end_idx])

    return ""


async def run(client: GeminiClient, ctx: CropContext = None) -> dict:
    """Execute Stage 4: Theme Extraction + Synthesis.

    Args:
        client: GeminiClient instance.
        ctx: Optional CropContext. When provided, reads from crop-specific
             targets/pathways and writes themes/synthesis to crop-specific
             directories. Falls back to legacy shared paths when None.

    Returns:
        Summary dict with results.
    """
    logger.info("=" * 60)
    logger.info("STAGE 4: THEME EXTRACTION & SYNTHESIS")
    logger.info("=" * 60)

    from agents.qc import preflight_check
    preflight_check(ctx.crop if ctx else "spinach", "theme_extraction")

    if ctx is not None:
        ctx.ensure_dirs()
        kb_targets_dir = ctx.kb_targets
        kb_pathways_dir = ctx.kb_pathways
        themes_dir = ctx.kb_themes
        synthesis_dir = ctx.kb_synthesis
        kb_dir = ctx.kb
        organism = ctx.organism
        common_name = ctx.common_name
        index_themes_dir = ctx.kb_themes
    else:
        kb_targets_dir = None
        kb_pathways_dir = None
        themes_dir = None
        synthesis_dir = None
        kb_dir = None
        organism = "Spinacia oleracea"
        common_name = "spinach"
        index_themes_dir = None

    start_time = datetime.now()

    gene_summaries = load_all_summaries(kb_targets_dir=kb_targets_dir)
    pathway_summaries = load_pathway_summaries(kb_pathways_dir=kb_pathways_dir)
    logger.info(f"Loaded summaries ({len(gene_summaries)} chars genes, {len(pathway_summaries)} chars pathways)")

    from agents.qc import validate_non_empty_string, CostGate
    validate_non_empty_string(gene_summaries, "gene summaries for Stage 4", min_chars=200)
    validate_non_empty_string(pathway_summaries, "pathway summaries for Stage 4", min_chars=100)

    # Run theme extraction and confounder analysis in parallel
    logger.info("Running theme extraction, causal models, and confounder analysis...")
    theme_result, causal_result, confounder_result = await asyncio.gather(
        extract_themes(client, gene_summaries, themes_dir=themes_dir, synthesis_dir=synthesis_dir),
        build_causal_models(client, gene_summaries, pathway_summaries, synthesis_dir=synthesis_dir),
        analyze_confounders(
            client, synthesis_dir=synthesis_dir,
            organism=organism, common_name=common_name,
        ),
    )

    # Build validation plan (depends on themes + causal models)
    logger.info("Designing validation plan...")
    themes_text = gene_summaries[:3000]  # Use summaries as proxy
    causal_text = ""
    if causal_result["status"] == "success":
        try:
            causal_text = Path(causal_result["filepath"]).read_text()[:3000]
        except Exception:
            pass

    validation_result = await design_validation_plan(
        client, themes_text, causal_text, synthesis_dir=synthesis_dir,
    )

    duration = (datetime.now() - start_time).total_seconds()

    # Update theme index
    if theme_result["status"] == "success":
        update_themes_index(theme_result["themes"], base_dir=index_themes_dir)

    # Update master index
    if ctx is not None:
        targets = ctx.load_targets()
    else:
        targets = load_targets()

    high = sum(1 for t in targets if t["priority"] == "high")
    medium = sum(1 for t in targets if t["priority"] == "medium")
    low = sum(1 for t in targets if t["priority"] == "low")

    update_master_index(
        {
            "total_targets": len(targets),
            "high_priority": high,
            "medium_priority": medium,
            "low_priority": low,
            "pathways_analyzed": len(set(t["pathway"] for t in targets)),
            "themes_extracted": len(THEME_FILES),
            "stages_complete": ["gene_analysis", "pathway_mapping", "literature_dive", "theme_extraction"],
            "organism": organism,
            "common_name": common_name,
        },
        base_dir=kb_dir,
    )

    stats = client.get_stats()
    logger.info(f"Stage 4 complete in {duration:.0f}s")

    return {
        "stage": "theme_extraction",
        "themes": theme_result["status"],
        "causal_models": causal_result["status"],
        "confounders": confounder_result["status"],
        "validation_plan": validation_result["status"],
        "duration_seconds": duration,
        "api_stats": stats,
    }
