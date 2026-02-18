"""Target gene API routes.

Endpoints for listing and retrieving target gene information from the
file system (crops/ and knowledge_base/ directories). Does not require
database connectivity.
"""

import json
import logging
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Request, HTTPException, Query
from fastapi.responses import JSONResponse

from platform.models import GeneResponse, TargetListResponse

logger = logging.getLogger(__name__)

router = APIRouter()

# Project root is two levels up from this file: platform/api/targets.py -> project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def _find_targets_config(crop: str) -> Optional[Path]:
    """Locate the targets config file for a given crop.

    Checks in order:
        1. crops/{crop}/targets_config.json
        2. knowledge_base/targets/
    """
    crops_config = PROJECT_ROOT / "crops" / crop / "targets_config.json"
    if crops_config.exists():
        return crops_config
    return None


def _find_target_markdown_dirs(crop: str) -> list[Path]:
    """Locate directories containing target markdown files for a crop.

    Checks:
        1. crops/{crop}/knowledge_base/targets/
        2. knowledge_base/targets/ (for the default spinach crop)
    """
    dirs = []
    crop_kb = PROJECT_ROOT / "crops" / crop / "knowledge_base" / "targets"
    if crop_kb.exists():
        dirs.append(crop_kb)

    # Also check main knowledge_base for the default (spinach) crop
    main_kb = PROJECT_ROOT / "knowledge_base" / "targets"
    if main_kb.exists():
        dirs.append(main_kb)

    return dirs


def _parse_targets_from_config(config_path: Path) -> list[dict]:
    """Parse targets from a JSON config file."""
    with open(config_path) as f:
        data = json.load(f)

    targets = []
    if isinstance(data, list):
        targets = data
    elif isinstance(data, dict):
        # Could be {"targets": [...]} or {"high_priority": [...], ...}
        if "targets" in data:
            targets = data["targets"]
        else:
            for priority_key in ["high_priority", "medium_priority", "low_priority"]:
                for t in data.get(priority_key, []):
                    if isinstance(t, dict):
                        t.setdefault("priority", priority_key.replace("_priority", ""))
                    targets.append(t)

    return targets


def _scan_markdown_targets(dirs: list[Path]) -> list[dict]:
    """Scan directories for target markdown files and extract basic metadata."""
    targets = []
    seen_ids = set()

    for base_dir in dirs:
        for priority_dir in ["high_priority", "medium_priority", "low_priority"]:
            priority_path = base_dir / priority_dir
            if not priority_path.exists():
                continue

            priority = priority_dir.replace("_priority", "")
            for md_file in sorted(priority_path.glob("*.md")):
                gene_id = md_file.stem
                if gene_id in seen_ids or gene_id == "INDEX":
                    continue
                seen_ids.add(gene_id)

                # Extract annotation from first few lines
                annotation = None
                try:
                    with open(md_file) as f:
                        for line in f:
                            line = line.strip()
                            if line.startswith("# "):
                                annotation = line[2:].strip()
                                break
                except Exception:
                    pass

                targets.append({
                    "gene_id": gene_id,
                    "annotation": annotation,
                    "priority": priority,
                })

        # Also scan flat .md files in the base dir
        for md_file in sorted(base_dir.glob("*.md")):
            gene_id = md_file.stem
            if gene_id in seen_ids or gene_id == "INDEX":
                continue
            seen_ids.add(gene_id)

            annotation = None
            try:
                with open(md_file) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("# "):
                            annotation = line[2:].strip()
                            break
            except Exception:
                pass

            targets.append({"gene_id": gene_id, "annotation": annotation})

    return targets


@router.get("/{crop}", response_model=TargetListResponse)
async def list_targets(
    request: Request,
    crop: str,
    priority: Optional[str] = Query(None, description="Filter by priority: high, medium, low"),
):
    """List all targets for a specific crop.

    Reads from crops/{crop}/targets_config.json if available,
    otherwise scans knowledge_base/targets/ markdown files.
    """
    try:
        targets: list[dict] = []

        # Try JSON config first
        config_path = _find_targets_config(crop)
        if config_path:
            targets = _parse_targets_from_config(config_path)
        else:
            # Fall back to scanning markdown directories
            dirs = _find_target_markdown_dirs(crop)
            if not dirs:
                raise HTTPException(
                    status_code=404,
                    detail=f"No target data found for crop '{crop}'. "
                           f"Expected at crops/{crop}/ or knowledge_base/targets/.",
                )
            targets = _scan_markdown_targets(dirs)

        # Apply priority filter if requested
        if priority:
            targets = [t for t in targets if t.get("priority") == priority]

        gene_responses = [
            GeneResponse(
                gene_id=t.get("gene_id", t.get("id", "unknown")),
                annotation=t.get("annotation"),
                pathway=t.get("pathway"),
                priority=t.get("priority"),
                organism=t.get("organism", crop),
                tldr=t.get("tldr"),
            )
            for t in targets
        ]

        return TargetListResponse(
            targets=gene_responses,
            total=len(gene_responses),
            crop=crop,
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to list targets for {crop}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to list targets: {e}")


@router.get("/{crop}/{gene_id}", response_model=dict)
async def get_target(request: Request, crop: str, gene_id: str):
    """Get the full markdown content for a specific target gene.

    Searches in priority subdirectories and flat files under the crop's
    knowledge base directory.
    """
    try:
        search_dirs = _find_target_markdown_dirs(crop)
        if not search_dirs:
            raise HTTPException(
                status_code=404,
                detail=f"No target data found for crop '{crop}'.",
            )

        # Search for the markdown file
        for base_dir in search_dirs:
            # Check priority subdirectories
            for priority_dir in ["high_priority", "medium_priority", "low_priority"]:
                candidate = base_dir / priority_dir / f"{gene_id}.md"
                if candidate.exists():
                    content = candidate.read_text(encoding="utf-8")
                    return {
                        "gene_id": gene_id,
                        "crop": crop,
                        "priority": priority_dir.replace("_priority", ""),
                        "content": content,
                        "source_path": str(candidate.relative_to(PROJECT_ROOT)),
                    }

            # Check flat file
            candidate = base_dir / f"{gene_id}.md"
            if candidate.exists():
                content = candidate.read_text(encoding="utf-8")
                return {
                    "gene_id": gene_id,
                    "crop": crop,
                    "content": content,
                    "source_path": str(candidate.relative_to(PROJECT_ROOT)),
                }

        raise HTTPException(
            status_code=404,
            detail=f"Target gene '{gene_id}' not found for crop '{crop}'.",
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get target {gene_id} for {crop}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Failed to get target: {e}")
