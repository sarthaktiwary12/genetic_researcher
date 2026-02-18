"""Pipeline QC module — validates data before every API call.

Prevents wasted API spend by checking:
- Required files exist and contain real data
- Gene IDs match the expected crop (no cross-contamination)
- Known placeholder strings are never sent to LLMs
- Minimum data thresholds are met before expensive calls

Usage:
    from agents.qc import preflight_check, QCError
    try:
        preflight_check("broccoli", "pathway_mapping")
    except QCError as e:
        print(f"Pipeline halted: {e}")
"""

import json
import logging
import re
from pathlib import Path

from agents.config import CROPS_DIR, KNOWLEDGE_BASE

logger = logging.getLogger(__name__)


def _kb_dirs(crop: str, subpath: str) -> list[Path]:
    """Return directories to check for a crop's data.

    The pipeline originally wrote spinach data to the shared knowledge_base/.
    For spinach, we check both crop-specific and shared KB.
    For other crops, only check crop-specific (shared KB is spinach data).
    """
    crop_path = CROPS_DIR / crop / "knowledge_base" / subpath
    if crop == "spinach":
        return [crop_path, KNOWLEDGE_BASE / subpath]
    return [crop_path]


# ---------------------------------------------------------------------------
# Exception hierarchy
# ---------------------------------------------------------------------------

class QCError(Exception):
    """Base — halts pipeline."""


class MissingDataError(QCError):
    """Required file or directory missing."""


class EmptyDataError(QCError):
    """Data exists but is empty or below threshold."""


class GeneIDMismatchError(QCError):
    """Wrong crop's gene IDs detected in loaded text."""


class PlaceholderDataError(QCError):
    """Known placeholder string found in prompt text."""


class CostGateError(QCError):
    """Input too small to justify an API call."""


class StageOutputMissingError(QCError):
    """Upstream stage didn't produce expected output."""


# ---------------------------------------------------------------------------
# Gene ID prefix registry
# ---------------------------------------------------------------------------

GENE_ID_PREFIXES = {
    "spinach": "SOV",
    "broccoli": "Bo",
    "wheat": "TraesCS",
    "maize": "Zm",
    "quinoa": "AUR",
    "soybean": "GLYMA",
}

KNOWN_PLACEHOLDERS = [
    "(No analyses available yet)",
    "(No pathway analyses available)",
    "(No prior analysis available)",
    "(No individual analysis available)",
]


# ---------------------------------------------------------------------------
# Validation functions
# ---------------------------------------------------------------------------

def validate_targets_config(crop: str) -> list[dict]:
    """Validate targets_config.json exists and has correct gene IDs.

    Returns the target list on success.
    Raises MissingDataError, EmptyDataError, or GeneIDMismatchError on failure.
    """
    config_path = CROPS_DIR / crop / "targets_config.json"
    if not config_path.exists():
        raise MissingDataError(
            f"targets_config.json missing for '{crop}': {config_path}"
        )

    data = json.loads(config_path.read_text())
    targets = data.get("targets", [])

    if len(targets) == 0:
        raise EmptyDataError(
            f"targets_config.json for '{crop}' has 0 targets"
        )

    # Check gene ID prefixes
    expected_prefix = GENE_ID_PREFIXES.get(crop)
    if expected_prefix:
        bad_ids = []
        for t in targets:
            gid = t.get("gene_id", "")
            if not gid.startswith(expected_prefix):
                bad_ids.append(gid)
        if bad_ids and len(bad_ids) == len(targets):
            raise GeneIDMismatchError(
                f"All {len(targets)} gene IDs in '{crop}' targets_config lack "
                f"expected prefix '{expected_prefix}'. Sample: {bad_ids[:3]}"
            )
        if bad_ids:
            logger.warning(
                f"{len(bad_ids)}/{len(targets)} gene IDs in '{crop}' lack "
                f"prefix '{expected_prefix}': {bad_ids[:3]}"
            )

    return targets


def validate_crop_metadata(crop: str) -> dict:
    """Validate crop_metadata.json exists with required fields.

    Returns metadata dict on success.
    Raises MissingDataError or EmptyDataError on failure.
    """
    meta_path = CROPS_DIR / crop / "crop_metadata.json"
    if not meta_path.exists():
        raise MissingDataError(
            f"crop_metadata.json missing for '{crop}': {meta_path}"
        )

    meta = json.loads(meta_path.read_text())
    required = ["species", "common_name", "family"]
    missing = [k for k in required if not meta.get(k)]
    if missing:
        raise EmptyDataError(
            f"crop_metadata.json for '{crop}' missing fields: {missing}"
        )

    return meta


def validate_directory_has_md_files(
    directory: Path, label: str, min_files: int = 1,
) -> int:
    """Validate directory exists with at least min_files .md files (excluding INDEX.md).

    Returns count of .md files found.
    Raises StageOutputMissingError on failure.
    """
    if not directory.exists():
        raise StageOutputMissingError(
            f"{label}: directory does not exist: {directory}"
        )

    md_files = [
        f for f in directory.rglob("*.md")
        if f.name != "INDEX.md"
    ]

    if len(md_files) < min_files:
        raise StageOutputMissingError(
            f"{label}: found {len(md_files)} .md files, need ≥{min_files} "
            f"in {directory}"
        )

    return len(md_files)


def validate_non_empty_string(
    data: str, label: str, min_chars: int = 100,
) -> None:
    """Validate string is non-empty, not a placeholder, and meets min length.

    Raises EmptyDataError or PlaceholderDataError on failure.
    """
    if not data or not data.strip():
        raise EmptyDataError(f"{label}: data is empty")

    stripped = data.strip()
    for placeholder in KNOWN_PLACEHOLDERS:
        if stripped == placeholder:
            raise PlaceholderDataError(
                f"{label}: contains known placeholder: '{placeholder}'"
            )

    if len(stripped) < min_chars:
        raise EmptyDataError(
            f"{label}: only {len(stripped)} chars (min: {min_chars})"
        )


def validate_loaded_data_gene_ids(text: str, crop: str) -> None:
    """Check that no gene IDs from OTHER crops appear in loaded text.

    Raises GeneIDMismatchError if foreign gene IDs are found.
    """
    for other_crop, prefix in GENE_ID_PREFIXES.items():
        if other_crop == crop:
            continue
        # Look for gene-ID-like patterns: prefix followed by alphanumerics
        pattern = rf"\b{re.escape(prefix)}[A-Za-z0-9_.]+\b"
        matches = re.findall(pattern, text)
        if len(matches) >= 3:
            raise GeneIDMismatchError(
                f"Data for '{crop}' contains {len(matches)} gene IDs from "
                f"'{other_crop}' (prefix '{prefix}'). Sample: {matches[:3]}. "
                f"Likely cross-contamination."
            )


# ---------------------------------------------------------------------------
# CostGate
# ---------------------------------------------------------------------------

class CostGate:
    """Gate that refuses API calls when input data is too small."""

    @staticmethod
    def check(
        model: str,
        description: str,
        input_chars: int,
        n_files: int = 0,
        min_chars: int = 100,
    ) -> None:
        logger.info(
            f"[COST GATE] {model} | {description} | "
            f"{input_chars} chars, {n_files} files"
        )
        if input_chars < min_chars:
            raise CostGateError(
                f"Refusing {model} call for '{description}': "
                f"only {input_chars} chars (min: {min_chars})"
            )


# ---------------------------------------------------------------------------
# Per-stage preflight functions
# ---------------------------------------------------------------------------

def preflight_stage1(crop: str) -> dict:
    """Preflight for Stage 1 (gene_analysis): targets_config + crop_metadata."""
    targets = validate_targets_config(crop)
    validate_crop_metadata(crop)
    return {
        "stage": "gene_analysis",
        "crop": crop,
        "status": "PASSED",
        "targets": len(targets),
    }


def _count_target_md_files(crop: str) -> int:
    """Count .md target files across applicable KB directories."""
    total_md = 0
    for subdir in ["high_priority", "medium_priority", "low_priority"]:
        for d in _kb_dirs(crop, f"targets/{subdir}"):
            if d.exists():
                total_md += len([
                    f for f in d.glob("*.md") if f.name != "INDEX.md"
                ])
    return total_md


def preflight_stage2(crop: str) -> dict:
    """Preflight for Stage 2 (pathway_mapping): Stage 1 checks + target .md files."""
    info = preflight_stage1(crop)

    total_md = _count_target_md_files(crop)

    if total_md == 0:
        raise StageOutputMissingError(
            f"Stage 1 output: found 0 .md target files for '{crop}'. "
            f"Run gene_analysis first."
        )

    info["stage"] = "pathway_mapping"
    info["target_md_files"] = total_md
    return info


def preflight_stage3(crop: str) -> dict:
    """Preflight for Stage 3 (literature_dive): high-priority targets exist."""
    targets = validate_targets_config(crop)
    validate_crop_metadata(crop)

    high = [t for t in targets if t.get("priority") == "high"]
    if len(high) == 0:
        raise EmptyDataError(
            f"targets_config for '{crop}' has 0 high-priority targets. "
            f"Stage 3 has nothing to analyze."
        )

    # Check high-priority .md files exist
    hp_count = 0
    for d in _kb_dirs(crop, "targets/high_priority"):
        if d.exists():
            hp_count += len([f for f in d.glob("*.md") if f.name != "INDEX.md"])

    if hp_count == 0:
        raise StageOutputMissingError(
            f"Stage 1 high-priority output: found 0 .md files for '{crop}'. "
            f"Run gene_analysis first."
        )

    return {
        "stage": "literature_dive",
        "crop": crop,
        "status": "PASSED",
        "high_priority_targets": len(high),
        "high_priority_md_files": hp_count,
    }


def preflight_stage4(crop: str) -> dict:
    """Preflight for Stage 4 (theme_extraction): Stage 2 checks + pathway .md files."""
    info = preflight_stage2(crop)

    n_pathways = 0
    for d in _kb_dirs(crop, "pathways"):
        if d.exists():
            n_pathways += len([
                f for f in d.glob("*.md") if f.name != "INDEX.md"
            ])

    if n_pathways == 0:
        raise StageOutputMissingError(
            f"Stage 2 output: found 0 pathway .md files for '{crop}'. "
            f"Run pathway_mapping first."
        )

    info["stage"] = "theme_extraction"
    info["pathway_md_files"] = n_pathways
    return info


def preflight_stage5(crop: str) -> dict:
    """Preflight for Stage 5 (synthesis): Stage 4 checks (includes 1+2)."""
    info = preflight_stage4(crop)
    info["stage"] = "synthesis"
    return info


def preflight_reports(crop: str) -> dict:
    """Preflight for report generation: crop_metadata + all 4 synthesis files exist."""
    validate_crop_metadata(crop)

    synth_dir = CROPS_DIR / crop / "synthesis"
    required_files = [
        "ranked_targets.md",
        "causal_models.md",
        "confounders.md",
        "validation_plan.md",
    ]

    missing = []
    for fname in required_files:
        if not (synth_dir / fname).exists():
            missing.append(fname)

    if missing:
        raise StageOutputMissingError(
            f"Report generation for '{crop}': missing synthesis files: {missing}. "
            f"NO shared KB fallback — run synthesis stage for this crop first."
        )

    return {
        "stage": "reports",
        "crop": crop,
        "status": "PASSED",
        "synthesis_files": len(required_files) - len(missing),
    }


# ---------------------------------------------------------------------------
# Main dispatcher
# ---------------------------------------------------------------------------

STAGE_MAP = {
    "gene_analysis": preflight_stage1,
    "pathway_mapping": preflight_stage2,
    "literature_dive": preflight_stage3,
    "theme_extraction": preflight_stage4,
    "synthesis": preflight_stage5,
    "reports": preflight_reports,
}


def preflight_check(crop: str, stage: str) -> dict:
    """Single entry point for preflight validation.

    Args:
        crop: Crop name (e.g. "spinach", "broccoli").
        stage: Pipeline stage name.

    Returns:
        Dict with status info on success.

    Raises:
        QCError subclass on failure.
    """
    fn = STAGE_MAP.get(stage)
    if fn is None:
        logger.warning(f"No preflight defined for stage '{stage}', skipping QC")
        return {"stage": stage, "crop": crop, "status": "SKIPPED"}

    logger.info(f"[QC] Preflight check: {crop} / {stage}")
    result = fn(crop)
    logger.info(f"[QC] PASSED: {crop} / {stage} — {result}")
    return result


def validate_all_stages(crop: str) -> dict:
    """Run all preflight checks for a crop. Returns dict of stage → result.

    Does NOT raise — catches errors and records them.
    Used by the --validate CLI flag.
    """
    results = {}
    for stage_name, fn in STAGE_MAP.items():
        try:
            results[stage_name] = fn(crop)
        except QCError as e:
            results[stage_name] = {
                "stage": stage_name,
                "crop": crop,
                "status": "FAILED",
                "error": str(e),
                "error_type": type(e).__name__,
            }
    return results
