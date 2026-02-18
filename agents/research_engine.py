#!/usr/bin/env python3
"""Main research engine orchestrator - CLI entrypoint for the ExRNA research pipeline.

Usage:
    python3 agents/research_engine.py --stage gene_analysis
    python3 agents/research_engine.py --stage pathway_mapping
    python3 agents/research_engine.py --stage literature_dive
    python3 agents/research_engine.py --stage theme_extraction
    python3 agents/research_engine.py --stage synthesis
    python3 agents/research_engine.py --stage all
    python3 agents/research_engine.py --crop maize --stage gene_analysis
    python3 agents/research_engine.py --campaign full_crop_analysis --crop rice
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

from agents.config import (
    TARGETS_CONFIG, KB_LOGS, CROPS_DIR, ANTHROPIC_API_KEY, MONTHLY_BUDGET_USD,
)
from agents.gemini_client import GeminiClient
from agents.model_router import ModelRouter, TaskCategory


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
    status = "Success" if "error" not in str(result).lower() else "Partial"

    entry = f"| {timestamp} | {stage} | {json.dumps(result, default=str)[:80]}... | {duration:.0f}s | {status} |\n"

    if "| — | — |" in existing:
        existing = existing.replace("| — | — | — | — | — |", entry)
    else:
        existing = existing.rstrip() + "\n" + entry

    log_path.write_text(existing)


def get_targets_config(crop: str = "spinach") -> Path:
    """Get the targets_config.json path for a given crop."""
    if crop == "spinach":
        return TARGETS_CONFIG

    crop_config = CROPS_DIR / crop / "targets_config.json"
    if crop_config.exists():
        return crop_config

    logging.warning(f"No targets_config.json for crop '{crop}', falling back to default")
    return TARGETS_CONFIG


async def run_stage(
    stage: str,
    gemini_client: GeminiClient,
    claude_client=None,
    crop: str = "spinach",
    router: ModelRouter = None,
) -> dict:
    """Run a specific pipeline stage.

    Stages 1-4 use Gemini (existing behavior).
    Stage 5 (synthesis) uses Claude.
    Model router selects the best model when available.
    """
    if stage == "gene_analysis":
        from agents.tasks.batch_gene_analysis import run
        return await run(gemini_client)

    elif stage == "pathway_mapping":
        from agents.tasks.pathway_analysis import run
        return await run(gemini_client)

    elif stage == "literature_dive":
        from agents.tasks.literature_deep_dive import run
        return await run(gemini_client)

    elif stage == "theme_extraction":
        from agents.tasks.theme_extraction import run
        return await run(gemini_client)

    elif stage == "synthesis":
        if not claude_client:
            logging.warning("No Claude client available for synthesis. Skipping.")
            return {"error": "Claude client not configured", "stage": "synthesis"}
        from agents.tasks.synthesis_task import run
        return await run(claude_client)

    elif stage == "cross_crop":
        if not claude_client:
            logging.warning("No Claude client for cross-crop analysis. Skipping.")
            return {"error": "Claude client not configured", "stage": "cross_crop"}
        from agents.tasks.cross_crop_analysis import run
        return await run(claude_client)

    else:
        raise ValueError(f"Unknown stage: {stage}")


async def run_all(
    gemini_client: GeminiClient,
    claude_client=None,
    crop: str = "spinach",
    router: ModelRouter = None,
) -> dict:
    """Run all pipeline stages in order (1-5)."""
    results = {}
    stages = [
        "gene_analysis", "pathway_mapping", "literature_dive",
        "theme_extraction", "synthesis",
    ]

    for stage in stages:
        logging.info(f"\n{'='*60}")
        logging.info(f"STARTING STAGE: {stage} (crop: {crop})")
        logging.info(f"{'='*60}\n")

        result = await run_stage(
            stage, gemini_client, claude_client, crop, router
        )
        results[stage] = result
        log_run(f"{stage}_{crop}", result)

        logging.info(f"Stage {stage} result: {json.dumps(result, indent=2, default=str)}")

    return results


async def run_campaign(
    campaign_type: str,
    gemini_client: GeminiClient,
    claude_client=None,
    crop: str = "spinach",
    config: dict = None,
) -> dict:
    """Run a named campaign type.

    This is the entry point for scheduler-driven campaigns.
    """
    config = config or {}

    if campaign_type == "full_crop_analysis":
        return await run_all(gemini_client, claude_client, crop)

    elif campaign_type == "pubmed_daily_scan":
        from agents.tasks.literature_monitor import run as run_lit
        from platform.mcp.pubmed_server import PubMedServer

        async with PubMedServer() as pubmed:
            return await run_lit(
                pubmed_server=pubmed,
                gemini_client=gemini_client,
                claude_client=claude_client,
                days_back=config.get("days_back", 1),
            )

    elif campaign_type == "cross_crop_synthesis":
        from agents.tasks.cross_crop_analysis import run as run_cc
        if not claude_client:
            return {"error": "Claude client required for cross-crop synthesis"}
        crops = config.get("crops", ["spinach"])
        return await run_cc(claude_client, crops=crops)

    elif campaign_type == "targeted_query":
        query = config.get("query", "")
        if not query:
            return {"error": "No query provided for targeted campaign"}

        # Use the model router to pick the best model
        router = ModelRouter(monthly_budget=MONTHLY_BUDGET_USD)
        assignment = router.route(TaskCategory.BULK_RESEARCH)

        if assignment.is_gemini:
            response = await gemini_client.query_reasoning(prompt=query)
        elif claude_client:
            response = await claude_client.query_synthesis(prompt=query)
        else:
            response = await gemini_client.query_reasoning(prompt=query)

        return {"query": query, "response_length": len(response), "model": assignment.model}

    else:
        return {"error": f"Unknown campaign type: {campaign_type}"}


async def run_test(gemini_client: GeminiClient, claude_client=None) -> dict:
    """Run a connectivity test."""
    logging.info("Running connectivity test...")
    results = {}

    # Test Gemini
    try:
        response = await gemini_client.query_bulk(
            prompt="What is the role of ABA in seed dormancy? Answer in 2 sentences.",
            system_instruction="You are a plant biology expert.",
            max_output_tokens=256,
        )
        results["gemini"] = {"status": "ok", "preview": response[:200]}
    except Exception as e:
        results["gemini"] = {"status": "failed", "error": str(e)}

    # Test Claude
    if claude_client:
        try:
            response = await claude_client.query_fast(
                prompt="What is gibberellin's role in seed germination? Answer in 2 sentences.",
                system_instruction="You are a plant biology expert.",
                max_output_tokens=256,
            )
            results["claude"] = {"status": "ok", "preview": response[:200]}
        except Exception as e:
            results["claude"] = {"status": "failed", "error": str(e)}
    else:
        results["claude"] = {"status": "not_configured"}

    # Verify targets config
    if TARGETS_CONFIG.exists():
        with open(TARGETS_CONFIG) as f:
            data = json.load(f)
        target_count = len(data.get("targets", []))
        results["targets_loaded"] = target_count
    else:
        results["targets_loaded"] = 0

    results["test"] = "passed" if results.get("gemini", {}).get("status") == "ok" else "failed"
    return results


async def main():
    parser = argparse.ArgumentParser(description="ExRNA Research Engine")
    parser.add_argument(
        "--stage",
        choices=[
            "gene_analysis", "pathway_mapping", "literature_dive",
            "theme_extraction", "synthesis", "cross_crop", "all",
        ],
        help="Pipeline stage to run",
    )
    parser.add_argument("--crop", default="spinach", help="Crop to analyze (default: spinach)")
    parser.add_argument("--campaign", help="Campaign type to run (for scheduler integration)")
    parser.add_argument("--campaign-config", help="JSON config for campaign", default="{}")
    parser.add_argument("--test", action="store_true", help="Run connectivity test")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")

    args = parser.parse_args()
    setup_logging(args.verbose)

    if not args.stage and not args.test and not args.campaign:
        parser.print_help()
        sys.exit(1)

    # Initialize clients
    gemini_client = GeminiClient()

    claude_client = None
    if ANTHROPIC_API_KEY:
        from agents.claude_client import ClaudeClient
        claude_client = ClaudeClient(api_key=ANTHROPIC_API_KEY)

    router = ModelRouter(monthly_budget=MONTHLY_BUDGET_USD)

    if args.test:
        result = await run_test(gemini_client, claude_client)
        print(json.dumps(result, indent=2, default=str))
        sys.exit(0 if result.get("test") == "passed" else 1)

    if args.campaign:
        config = json.loads(args.campaign_config)
        config["crop"] = args.crop
        result = await run_campaign(
            args.campaign, gemini_client, claude_client, args.crop, config
        )
    elif args.stage == "all":
        result = await run_all(gemini_client, claude_client, args.crop, router)
    else:
        result = await run_stage(
            args.stage, gemini_client, claude_client, args.crop, router
        )
        log_run(f"{args.stage}_{args.crop}", result)

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    asyncio.run(main())
