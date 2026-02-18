"""Create per-crop configuration directories from the root targets_config.json.

Reads the project-level targets_config.json and generates structured
per-crop configuration under ``crops/<crop_name>/``. Currently
supports spinach; designed to be extended for additional crops
(soybean, maize, wheat, broccoli, quinoa) as their data becomes available.

Usage:
    python -m platform.migration.crop_config_loader
"""

import asyncio
import json
import logging
import sys
from pathlib import Path

# Ensure project root is on path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from agents.config import (
    CROPS_DIR,
    KNOWLEDGE_BASE,
    ORGANISM,
    PROJECT_ROOT,
    TARGETS_CONFIG,
    TREATMENT,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Crop metadata definitions
# ---------------------------------------------------------------------------

# Known crops in the research engine with their metadata.
# The spinach entry is the primary crop; others are stubs for future use.
CROP_REGISTRY: dict[str, dict] = {
    "spinach": {
        "species": "Spinacia oleracea",
        "common_name": "spinach",
        "treatment": "M-9 bacterial EPS solution",
        "knowledge_base_path": "knowledge_base",
    },
    "soybean": {
        "species": "Glycine max",
        "common_name": "soybean",
        "treatment": "M-9 bacterial EPS solution",
        "knowledge_base_path": "knowledge_base",
    },
    "maize": {
        "species": "Zea mays",
        "common_name": "maize",
        "treatment": "M-9 bacterial EPS solution",
        "knowledge_base_path": "knowledge_base",
    },
    "wheat": {
        "species": "Triticum aestivum",
        "common_name": "wheat",
        "treatment": "M-9 bacterial EPS solution",
        "knowledge_base_path": "knowledge_base",
    },
    "broccoli": {
        "species": "Brassica oleracea var. italica",
        "common_name": "broccoli",
        "treatment": "M-9 bacterial EPS solution",
        "knowledge_base_path": "knowledge_base",
    },
    "quinoa": {
        "species": "Chenopodium quinoa",
        "common_name": "quinoa",
        "treatment": "M-9 bacterial EPS solution",
        "knowledge_base_path": "knowledge_base",
    },
}


# ---------------------------------------------------------------------------
# Config loading and transformation
# ---------------------------------------------------------------------------


def _load_root_config() -> dict:
    """Load and validate the root targets_config.json.

    Returns the parsed JSON dict, or an empty dict on failure.
    """
    if not TARGETS_CONFIG.exists():
        logger.error("Root targets_config.json not found at %s", TARGETS_CONFIG)
        return {}

    try:
        data = json.loads(TARGETS_CONFIG.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        logger.error("Failed to parse targets_config.json: %s", exc)
        return {}

    if "targets" not in data:
        logger.warning("No 'targets' key in targets_config.json")
    if "metadata" not in data:
        logger.warning("No 'metadata' key in targets_config.json")

    return data


def _transform_config_for_crop(
    root_config: dict, crop_name: str, crop_meta: dict
) -> dict:
    """Transform the root targets_config.json for a specific crop.

    For spinach (the primary organism), the targets list is preserved
    as-is. For other crops, an empty targets list is created as a
    placeholder until crop-specific research is conducted.
    """
    is_primary = crop_meta.get("species") == ORGANISM

    metadata = {
        "organism": crop_meta["species"],
        "common_name": crop_meta["common_name"],
        "treatment": crop_meta["treatment"],
        "total_targets": root_config.get("metadata", {}).get("total_targets", 0)
        if is_primary
        else 0,
        "description": root_config.get("metadata", {}).get(
            "description",
            f"Predicted transcripts targeted by bacterial extracellular small RNAs in {crop_meta['common_name']}",
        )
        if is_primary
        else f"Placeholder config for {crop_meta['common_name']} exRNA targets",
    }

    targets = root_config.get("targets", []) if is_primary else []

    return {
        "metadata": metadata,
        "targets": targets,
    }


def _build_crop_metadata(
    crop_name: str, crop_meta: dict, total_targets: int
) -> dict:
    """Build the crop_metadata.json content for a crop directory."""
    return {
        "species": crop_meta["species"],
        "common_name": crop_meta["common_name"],
        "treatment": crop_meta["treatment"],
        "total_targets": total_targets,
        "knowledge_base_path": crop_meta.get("knowledge_base_path", "knowledge_base"),
        "crop_dir": str(CROPS_DIR / crop_name),
        "targets_config": str(CROPS_DIR / crop_name / "targets_config.json"),
    }


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def create_crop_configs(
    crops: list[str] | None = None,
) -> dict[str, Path]:
    """Create per-crop config directories under ``crops/``.

    For each crop:
    1. Creates ``crops/<crop_name>/`` directory
    2. Writes ``crops/<crop_name>/targets_config.json``
       (spinach gets the full config; others get placeholders)
    3. Writes ``crops/<crop_name>/crop_metadata.json``

    Args:
        crops: List of crop names to create. If None, creates only
               spinach (the primary crop with existing data).

    Returns:
        Dict mapping crop name to its directory Path.
    """
    root_config = _load_root_config()
    if not root_config:
        logger.error("Cannot proceed without root targets_config.json")
        return {}

    if crops is None:
        # Default: only create for crops that have data
        crops = ["spinach"]

    created: dict[str, Path] = {}

    for crop_name in crops:
        crop_meta = CROP_REGISTRY.get(crop_name)
        if not crop_meta:
            logger.warning(
                "Unknown crop '%s', skipping. Known crops: %s",
                crop_name,
                list(CROP_REGISTRY.keys()),
            )
            continue

        crop_dir = CROPS_DIR / crop_name
        crop_dir.mkdir(parents=True, exist_ok=True)
        logger.info("Created crop directory: %s", crop_dir)

        # Write per-crop targets_config.json
        crop_config = _transform_config_for_crop(root_config, crop_name, crop_meta)
        targets_path = crop_dir / "targets_config.json"
        targets_path.write_text(
            json.dumps(crop_config, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        logger.info(
            "Wrote %s (%d targets)",
            targets_path,
            len(crop_config.get("targets", [])),
        )

        # Write crop_metadata.json
        total_targets = len(crop_config.get("targets", []))
        crop_metadata = _build_crop_metadata(crop_name, crop_meta, total_targets)
        metadata_path = crop_dir / "crop_metadata.json"
        metadata_path.write_text(
            json.dumps(crop_metadata, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        logger.info("Wrote %s", metadata_path)

        created[crop_name] = crop_dir

    logger.info(
        "Crop config creation complete: %d crops (%s)",
        len(created),
        ", ".join(created.keys()),
    )
    return created


# ---------------------------------------------------------------------------
# Main entrypoint
# ---------------------------------------------------------------------------


async def main():
    """Run the crop config loader as a standalone migration.

    Creates configs for all known crops. Spinach gets the full
    targets_config.json; other crops get placeholder configs.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    logger.info("Starting crop config loader")
    logger.info("Root targets config: %s", TARGETS_CONFIG)
    logger.info("Crops directory: %s", CROPS_DIR)

    # Create for all known crops
    all_crops = list(CROP_REGISTRY.keys())
    result = create_crop_configs(crops=all_crops)

    summary = {
        crop_name: str(crop_path) for crop_name, crop_path in result.items()
    }
    logger.info("Created crop configs: %s", json.dumps(summary, indent=2))
    return result


if __name__ == "__main__":
    asyncio.run(main())
