"""Prompt templates optimized for Claude synthesis tasks.

Different from Gemini prompts: more structured output, explicit evidence-labeling
instructions, and formatted for Claude's strengths in structured reasoning.
"""

SYNTHESIS_SYSTEM = """You are an expert plant molecular biologist and systems biology
synthesizer specializing in seed germination, cross-kingdom RNA biology, and
agricultural biotechnology. You produce rigorous, evidence-based scientific analyses.

CRITICAL RULES:
- Label all claims: [KNOWN], [INFERRED], or [SPECULATIVE]
- Never invent fold changes, p-values, or experimental data
- Cite specific gene IDs, pathways, and literature where possible
- Separate mechanistic certainty from speculation
- Consider confounders: EPS osmopriming, polysaccharide elicitor effects, microbiome effects
- Use structured markdown output with clear headers"""


def ranked_targets_prompt(target_summaries: str, pathway_summaries: str) -> str:
    """Produce a comprehensive ranking of all gene targets."""
    return f"""Analyze the following gene target summaries and pathway analyses to produce
a definitive ranked list of all targets by their likely contribution to the observed
germination/vigor phenotype.

## TARGET SUMMARIES
{target_summaries}

## PATHWAY CONTEXT
{pathway_summaries}

## REQUIRED OUTPUT FORMAT

### Executive Summary
2-3 paragraphs summarizing the overall target landscape.

### Tier 1: Critical Targets (expected large phenotypic effect)
For each target:
- **Gene ID** — Annotation
- **Mechanism**: How downregulation improves germination [KNOWN/INFERRED/SPECULATIVE]
- **Evidence strength**: Strong/Moderate/Weak
- **Key references**: Arabidopsis homolog data if available
- **Confidence**: High/Medium/Low

### Tier 2: Important Targets (moderate expected effect)
[Same format]

### Tier 3: Supporting Targets (indirect or minor effect)
[Same format]

### Ranking Methodology
Explain the criteria used for ranking.

### Unresolved Questions
List key unknowns that affect ranking confidence."""


def causal_models_prompt(
    ranked_targets: str,
    pathway_analyses: str,
    theme_analyses: str,
) -> str:
    """Build alternative causal models from exRNA to phenotype."""
    return f"""Using the ranked targets, pathway analyses, and theme analyses below,
construct 2-3 alternative causal models explaining how bacterial exRNA-mediated
downregulation of these targets leads to improved germination and seedling vigor.

## RANKED TARGETS
{ranked_targets}

## PATHWAY ANALYSES
{pathway_analyses}

## THEME ANALYSES
{theme_analyses}

## REQUIRED OUTPUT FORMAT

### Model 1: [Descriptive Name]
**Core hypothesis**: [One sentence]
**Causal chain**:
1. Bacterial exRNA enters seed cells via [mechanism]
2. Target X is downregulated → [immediate effect]
3. This leads to → [downstream effect]
4. Net phenotypic outcome: [specific prediction]

**Supporting evidence**: [List with evidence labels]
**Weaknesses**: [What this model doesn't explain]
**Testable predictions**: [Specific experiments]

### Model 2: [Descriptive Name]
[Same format]

### Model 3: [Descriptive Name]
[Same format]

### Model Comparison Table
| Feature | Model 1 | Model 2 | Model 3 |
|---------|---------|---------|---------|
| Targets explained | | | |
| Mechanism complexity | | | |
| Testable predictions | | | |
| Overall plausibility | | | |

### Recommended Model
Which model best fits the evidence and why."""


def confounder_analysis_prompt(experimental_context: str) -> str:
    """Critically analyze potential confounders."""
    return f"""Perform a rigorous critical analysis of potential confounders in the
exRNA germination improvement system. The goal is to identify what portion of the
observed phenotype might NOT be due to antisense RNA targeting.

## EXPERIMENTAL CONTEXT
{experimental_context}

## REQUIRED OUTPUT FORMAT

### 1. EPS Osmopriming Effect
- Mechanism: How EPS solution itself could improve germination
- Expected magnitude vs observed effect
- Controls needed to distinguish from exRNA effect
- Evidence level: [KNOWN/INFERRED/SPECULATIVE]

### 2. Polysaccharide Elicitor Effects
- Known defense/growth priming by bacterial polysaccharides
- Relevant plant receptors and signaling pathways
- Overlap with observed target gene changes

### 3. Microbiome Effects
- Could the bacterial treatment alter seed microbiome?
- Known microbiome effects on germination
- Separation from direct exRNA mechanism

### 4. RNA Stability & Dosage Concerns
- Expected half-life of exRNA in seed coat environment
- Required copy number for antisense effect
- Evidence for/against sufficient dosage

### 5. Non-specific RNA Effects
- Could any RNA sequence trigger similar responses?
- Pattern-triggered immunity from dsRNA
- Controls: scrambled sequence, RNase treatment

### 6. Contamination Signals
- cry8Ba bacterial protein detected — implications
- Other bacterial contaminants in the preparation
- Quality control recommendations

### Confounder Impact Matrix
| Confounder | Likelihood | Impact if True | Distinguishable? | Priority |
|-----------|-----------|----------------|-------------------|----------|

### Recommended Controls
Prioritized list of experiments to rule out confounders."""


def validation_plan_prompt(
    ranked_targets: str,
    causal_models: str,
    confounders: str,
) -> str:
    """Design a 4-tier validation experimental plan."""
    return f"""Design a comprehensive 4-tier validation plan for the exRNA germination
improvement system, accounting for the ranked targets, causal models, and identified
confounders.

## RANKED TARGETS
{ranked_targets}

## CAUSAL MODELS
{causal_models}

## CONFOUNDERS
{confounders}

## REQUIRED OUTPUT FORMAT

### Tier 1: Essential Controls (do first)
For each experiment:
- **Experiment**: Name and brief description
- **Hypothesis tested**: What this confirms/rules out
- **Method**: Protocol outline
- **Expected result if exRNA mechanism is real**: [specific prediction]
- **Expected result if confounder**: [specific prediction]
- **Timeline**: Estimated duration
- **Difficulty**: Low/Medium/High
- **Priority**: Critical/High/Medium

### Tier 2: Target Validation
[Same format — focus on top 5-10 targets]

### Tier 3: Mechanistic Studies
[Same format — pathway-level experiments]

### Tier 4: Advanced/Translational
[Same format — field trials, multi-crop, optimization]

### Resource Requirements
| Tier | Experiments | Est. Duration | Key Equipment | Est. Cost |
|------|------------|---------------|---------------|-----------|

### Decision Tree
Flowchart logic: if Tier 1 results show X, proceed to Y; if Z, reconsider model."""


def cross_crop_synthesis_prompt(crop_results: dict[str, str]) -> str:
    """Synthesize findings across multiple crops."""
    crop_sections = "\n\n".join(
        f"## {crop.upper()}\n{summary}" for crop, summary in crop_results.items()
    )

    return f"""Analyze the following research results across multiple crops to identify
conserved vs species-specific mechanisms of exRNA-mediated germination improvement.

{crop_sections}

## REQUIRED OUTPUT FORMAT

### Conserved Mechanisms
Mechanisms/targets that appear across multiple crops:
- **Mechanism**: Description
- **Crops observed**: List
- **Conservation evidence**: [KNOWN/INFERRED]
- **Significance**: Why this conservation matters

### Species-Specific Mechanisms
Mechanisms unique to one or few crops:
- **Mechanism**: Description
- **Crop**: Which species
- **Possible explanation**: Why this differs

### Cross-Crop Theme Matrix
| Theme | Spinach | Maize | Wheat | Broccoli | Quinoa | Soybean |
|-------|---------|-------|-------|----------|--------|---------|

### Evolutionary Conservation Analysis
- Core conserved pathways
- Monocot vs dicot differences
- Implications for mechanism universality

### Translational Priorities
Which crops/mechanisms should be prioritized for agricultural applications."""
