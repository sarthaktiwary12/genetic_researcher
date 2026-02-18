"""Routes tasks to the appropriate AI model based on category and budget.

8 task categories map to specific models. Budget-aware fallback
downgrades Opus→Sonnet→Gemini when spend is high.
"""

import logging
from enum import Enum
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


class TaskCategory(Enum):
    """Research task categories with default model assignments."""
    BULK_RESEARCH = "bulk_research"
    PATHWAY_ANALYSIS = "pathway_analysis"
    SYNTHESIS = "synthesis"
    CRITICAL_REVIEW = "critical_review"
    LITERATURE_SCAN = "literature_scan"
    CLAIM_EXTRACTION = "claim_extraction"
    CROSS_CROP = "cross_crop"
    VALIDATION_DESIGN = "validation_design"


@dataclass
class ModelAssignment:
    """A model assignment with provider, model name, and cost tier."""
    provider: str  # "gemini" or "claude"
    model: str
    cost_tier: int  # 1=cheapest, 5=most expensive

    @property
    def is_claude(self) -> bool:
        return self.provider == "claude"

    @property
    def is_gemini(self) -> bool:
        return self.provider == "gemini"


# Default model assignments per task category
_DEFAULT_ASSIGNMENTS = {
    TaskCategory.BULK_RESEARCH: ModelAssignment("gemini", "gemini-2.5-flash", 1),
    TaskCategory.PATHWAY_ANALYSIS: ModelAssignment("gemini", "gemini-2.5-pro", 3),
    TaskCategory.SYNTHESIS: ModelAssignment("claude", "claude-sonnet-4-6", 3),
    TaskCategory.CRITICAL_REVIEW: ModelAssignment("claude", "claude-opus-4-6", 5),
    TaskCategory.LITERATURE_SCAN: ModelAssignment("gemini", "gemini-2.5-flash", 1),
    TaskCategory.CLAIM_EXTRACTION: ModelAssignment("claude", "claude-sonnet-4-6", 3),
    TaskCategory.CROSS_CROP: ModelAssignment("claude", "claude-sonnet-4-6", 3),
    TaskCategory.VALIDATION_DESIGN: ModelAssignment("claude", "claude-opus-4-6", 5),
}

# Fallback chains: ordered from most expensive to cheapest
_FALLBACK_CHAIN = [
    ModelAssignment("claude", "claude-opus-4-6", 5),
    ModelAssignment("claude", "claude-sonnet-4-6", 3),
    ModelAssignment("gemini", "gemini-2.5-pro", 3),
    ModelAssignment("gemini", "gemini-2.5-flash", 1),
]


class ModelRouter:
    """Routes tasks to AI models with budget-aware fallback.

    When budget is running low, expensive models are downgraded:
    - >80% budget used: Opus → Sonnet
    - >90% budget used: Sonnet → Gemini Pro
    - >95% budget used: Everything → Gemini Flash
    """

    def __init__(
        self,
        monthly_budget: float = 5000.0,
        current_spend: float = 0.0,
    ):
        self.monthly_budget = monthly_budget
        self.current_spend = current_spend

    @property
    def budget_fraction(self) -> float:
        if self.monthly_budget <= 0:
            return 1.0
        return self.current_spend / self.monthly_budget

    def update_spend(self, amount: float):
        """Record additional spend."""
        self.current_spend += amount
        logger.debug(
            f"Budget: ${self.current_spend:.2f} / ${self.monthly_budget:.2f} "
            f"({self.budget_fraction:.1%})"
        )

    def route(
        self,
        category: TaskCategory,
        force_model: Optional[str] = None,
    ) -> ModelAssignment:
        """Get the model assignment for a task category.

        Args:
            category: The task type to route.
            force_model: Override model (bypasses budget logic).

        Returns:
            ModelAssignment with provider and model name.
        """
        if force_model:
            for assignment in _FALLBACK_CHAIN:
                if assignment.model == force_model:
                    return assignment
            return ModelAssignment("gemini", force_model, 2)

        default = _DEFAULT_ASSIGNMENTS[category]
        fraction = self.budget_fraction

        if fraction < 0.8:
            return default

        if fraction >= 0.95:
            logger.warning(
                f"Budget critical ({fraction:.0%}). All tasks → Gemini Flash."
            )
            return ModelAssignment("gemini", "gemini-2.5-flash", 1)

        if fraction >= 0.9:
            if default.cost_tier >= 3:
                downgraded = ModelAssignment("gemini", "gemini-2.5-pro", 3)
                logger.warning(
                    f"Budget high ({fraction:.0%}). "
                    f"Downgrading {default.model} → {downgraded.model}"
                )
                return downgraded
            return default

        # 0.8 <= fraction < 0.9
        if default.cost_tier >= 5:
            downgraded = ModelAssignment("claude", "claude-sonnet-4-6", 3)
            logger.warning(
                f"Budget elevated ({fraction:.0%}). "
                f"Downgrading {default.model} → {downgraded.model}"
            )
            return downgraded

        return default

    def get_status(self) -> dict:
        """Return routing status summary."""
        return {
            "monthly_budget": self.monthly_budget,
            "current_spend": round(self.current_spend, 2),
            "budget_fraction": round(self.budget_fraction, 4),
            "active_downgrades": self.budget_fraction >= 0.8,
        }
