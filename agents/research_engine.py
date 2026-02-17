#!/usr/bin/env python3
"""Main research engine orchestrator - CLI entrypoint for the ExRNA research pipeline.

Usage:
    python3 agents/research_engine.py --stage gene_analysis
    python3 agents/research_engine.py --stage pathway_mapping
    python3 agents/research_engine.py --stage literature_dive
    python3 agents/research_engine.py --stage theme_extraction
    python3 agents/research_engine.py --stage all
    python3 agents/research_engine.py --test
"""

import argparse
import asyncio
import json
import logging
import sys
from datetime import datetime
from pathlib import Path

# Ensure project root is on path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from agents.config import TARGETS_CONFIG, KB_LOGS
from agents.gemini_client import GeminiClient


def setup_logging(verbose: bool = False):
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def log_run(stage: str, result: dict):
    """Append run result to the agent log."""
    KB_LOGS.mkdir(parents=True, exist_ok=True)
    log_path = KB_LOGS / "agent_runs.md"

    # Read existing content
    existing = ""
    if log_path.exists():
        existing = log_path.read_text()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    duration = result.get("duration_seconds", 0)
    api_stats = result.get("api_stats", {})
    status = "Success" if "error" not in str(result).lower() else "Partial"

    entry = f"| {timestamp} | {stage} | {json.dumps(result, default=str)[:80]}... | {duration:.0f}s | {status} |\n"

    # Insert the entry into the table
    if "| — | — |" in existing:
        existing = existing.replace("| — | — | — | — | — |", entry)
    else:
        # Append to existing table
        existing = existing.rstrip() + "\n" + entry

    log_path.write_text(existing)


async def run_stage(stage: str, client: GeminiClient) -> dict:
    """Run a specific pipeline stage."""
    if stage == "gene_analysis":
        from agents.tasks.batch_gene_analysis import run
        return await run(client)

    elif stage == "pathway_mapping":
        from agents.tasks.pathway_analysis import run
        return await run(client)

    elif stage == "literature_dive":
        from agents.tasks.literature_deep_dive import run
        return await run(client)

    elif stage == "theme_extraction":
        from agents.tasks.theme_extraction import run
        return await run(client)

    else:
        raise ValueError(f"Unknown stage: {stage}")


async def run_all(client: GeminiClient) -> dict:
    """Run all pipeline stages in order."""
    results = {}
    stages = ["gene_analysis", "pathway_mapping", "literature_dive", "theme_extraction"]

    for stage in stages:
        logging.info(f"\n{'='*60}")
        logging.info(f"STARTING STAGE: {stage}")
        logging.info(f"{'='*60}\n")

        result = await run_stage(stage, client)
        results[stage] = result
        log_run(stage, result)

        logging.info(f"Stage {stage} result: {json.dumps(result, indent=2, default=str)}")

    return results


async def run_test(client: GeminiClient) -> dict:
    """Run a connectivity test with a single query."""
    logging.info("Running connectivity test...")

    try:
        response = await client.query_bulk(
            prompt="What is the role of ABA in seed dormancy? Answer in 2 sentences.",
            system_instruction="You are a plant biology expert.",
            max_output_tokens=256,
        )
        logging.info(f"Test response: {response[:200]}")

        # Verify targets config exists
        if TARGETS_CONFIG.exists():
            with open(TARGETS_CONFIG) as f:
                data = json.load(f)
            target_count = len(data.get("targets", []))
            logging.info(f"Targets config: {target_count} targets loaded")
        else:
            logging.warning(f"Targets config not found at {TARGETS_CONFIG}")
            target_count = 0

        return {
            "test": "passed",
            "response_preview": response[:200],
            "targets_loaded": target_count,
            "api_stats": client.get_stats(),
        }

    except Exception as e:
        logging.error(f"Test failed: {e}")
        return {"test": "failed", "error": str(e)}


async def main():
    parser = argparse.ArgumentParser(description="ExRNA Research Engine")
    parser.add_argument(
        "--stage",
        choices=["gene_analysis", "pathway_mapping", "literature_dive", "theme_extraction", "all"],
        help="Pipeline stage to run",
    )
    parser.add_argument("--test", action="store_true", help="Run connectivity test")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")

    args = parser.parse_args()
    setup_logging(args.verbose)

    if not args.stage and not args.test:
        parser.print_help()
        sys.exit(1)

    client = GeminiClient()

    if args.test:
        result = await run_test(client)
        print(json.dumps(result, indent=2, default=str))
        sys.exit(0 if result.get("test") == "passed" else 1)

    if args.stage == "all":
        result = await run_all(client)
    else:
        result = await run_stage(args.stage, client)
        log_run(args.stage, result)

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    asyncio.run(main())
