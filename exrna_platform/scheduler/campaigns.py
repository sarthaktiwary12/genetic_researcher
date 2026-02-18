"""Campaign type definitions and templates.

7 campaign types with pre-built cron schedules, default configs,
and budget limits.
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class CampaignType(Enum):
    """Research campaign categories."""
    FULL_CROP_ANALYSIS = "full_crop_analysis"
    TARGETED_QUERY = "targeted_query"
    PUBMED_DAILY_SCAN = "pubmed_daily_scan"
    CROSS_CROP_SYNTHESIS = "cross_crop_synthesis"
    HYPOTHESIS_UPDATE = "hypothesis_update"
    LITERATURE_DEEP_DIVE = "literature_deep_dive"
    EXPERIMENT_INTEGRATION = "experiment_integration"


@dataclass
class CampaignTemplate:
    """Pre-built campaign configuration template."""
    name: str
    campaign_type: CampaignType
    description: str
    cron_schedule: Optional[dict] = None  # APScheduler CronTrigger kwargs
    default_config: dict = field(default_factory=dict)
    budget_limit: Optional[float] = None
    estimated_cost: float = 0.0
    stages: list[str] = field(default_factory=list)


CAMPAIGN_TEMPLATES: dict[CampaignType, CampaignTemplate] = {
    CampaignType.FULL_CROP_ANALYSIS: CampaignTemplate(
        name="Full Crop Analysis",
        campaign_type=CampaignType.FULL_CROP_ANALYSIS,
        description="Run complete 5-stage pipeline for a single crop: gene analysis, "
                    "pathway mapping, literature dive, theme extraction, synthesis.",
        default_config={
            "stages": ["gene_analysis", "pathway_mapping", "literature_dive",
                       "theme_extraction", "synthesis"],
        },
        budget_limit=10.0,
        estimated_cost=3.50,
        stages=["gene_analysis", "pathway_mapping", "literature_dive",
                "theme_extraction", "synthesis"],
    ),

    CampaignType.TARGETED_QUERY: CampaignTemplate(
        name="Targeted Research Query",
        campaign_type=CampaignType.TARGETED_QUERY,
        description="Run a specific research query against one or more models. "
                    "Used for gap-filling and deep dives on specific topics.",
        default_config={
            "model": "gemini-2.5-pro",
            "max_queries": 5,
        },
        budget_limit=5.0,
        estimated_cost=0.50,
        stages=["query", "synthesize"],
    ),

    CampaignType.PUBMED_DAILY_SCAN: CampaignTemplate(
        name="Daily PubMed Literature Scan",
        campaign_type=CampaignType.PUBMED_DAILY_SCAN,
        description="Daily scan of PubMed for new papers matching research keywords. "
                    "Scores relevance and extracts claims from high-relevance papers.",
        cron_schedule={"hour": 6, "minute": 0},  # 6 AM daily
        default_config={
            "days_back": 1,
            "max_results_per_keyword": 10,
            "relevance_threshold": 0.6,
        },
        budget_limit=1.0,
        estimated_cost=0.30,
        stages=["search", "score", "extract", "store"],
    ),

    CampaignType.CROSS_CROP_SYNTHESIS: CampaignTemplate(
        name="Cross-Crop Meta-Analysis",
        campaign_type=CampaignType.CROSS_CROP_SYNTHESIS,
        description="Synthesize findings across all analyzed crops. Identifies "
                    "conserved vs species-specific mechanisms.",
        cron_schedule={"day_of_week": "sun", "hour": 2, "minute": 0},  # Weekly
        default_config={
            "crops": ["spinach", "maize", "wheat", "broccoli", "quinoa", "soybean"],
        },
        budget_limit=5.0,
        estimated_cost=2.00,
        stages=["load_crop_results", "synthesize", "build_matrix", "write"],
    ),

    CampaignType.HYPOTHESIS_UPDATE: CampaignTemplate(
        name="Monthly Hypothesis Review",
        campaign_type=CampaignType.HYPOTHESIS_UPDATE,
        description="Review and update all active hypotheses based on new evidence "
                    "from literature scans and experiment results.",
        cron_schedule={"day": 1, "hour": 3, "minute": 0},  # 1st of month
        default_config={
            "include_literature": True,
            "include_experiments": True,
        },
        budget_limit=3.0,
        estimated_cost=1.00,
        stages=["load_hypotheses", "gather_evidence", "review", "update"],
    ),

    CampaignType.LITERATURE_DEEP_DIVE: CampaignTemplate(
        name="Literature Deep Dive",
        campaign_type=CampaignType.LITERATURE_DEEP_DIVE,
        description="Comprehensive literature review for specific genes or topics. "
                    "Uses homolog search, PubMed deep dive, and cross-species analysis.",
        default_config={
            "max_genes": 10,
            "priority_filter": "high",
        },
        budget_limit=5.0,
        estimated_cost=1.50,
        stages=["select_targets", "homolog_search", "literature_search", "synthesize"],
    ),

    CampaignType.EXPERIMENT_INTEGRATION: CampaignTemplate(
        name="Experiment Result Integration",
        campaign_type=CampaignType.EXPERIMENT_INTEGRATION,
        description="Integrate wet-lab experiment results with AI predictions. "
                    "Updates hypothesis confidence and target rankings.",
        default_config={
            "update_rankings": True,
            "update_hypotheses": True,
        },
        budget_limit=2.0,
        estimated_cost=0.50,
        stages=["load_results", "compare_predictions", "update_graph", "report"],
    ),
}
