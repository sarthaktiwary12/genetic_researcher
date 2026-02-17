"""Prompt templates for mechanistic reasoning and causal modeling."""

SYSTEM_INSTRUCTION = """You are a mechanistic biologist who builds causal models from molecular data.
You specialize in:
- Signal transduction cascades in plants
- Hormone-mediated developmental switches
- Systems biology and network modeling
- Distinguishing causation from correlation

Always explicitly state assumptions and identify where the causal chain is weakest."""


def causal_model_prompt(ranked_targets: str, pathway_analyses: str) -> str:
    """Build causal models from exRNA to phenotype."""
    return f"""Based on the ranked target list and pathway analyses below, construct mechanistic causal models explaining how bacterial exRNAs improve spinach germination:

**Ranked Targets**:
{ranked_targets}

**Pathway Analyses**:
{pathway_analyses}

**Build at least 2 alternative causal models**:

### MODEL 1: [Name this model]
Build a complete causal chain:
```
Bacterial exRNAs in EPS
  → [Uptake mechanism]
  → [Primary targets silenced]
  → [Immediate molecular consequence]
  → [Pathway-level shift]
  → [Physiological change]
  → [Germination phenotype]
```

For each arrow, state:
- The evidence supporting this step
- The confidence level (High/Medium/Low)
- What would break this model

### MODEL 2: [Name this model]
[Same structure as above but different primary mechanism]

### MODEL COMPARISON:
| Feature | Model 1 | Model 2 |
|---------|---------|---------|
| Primary targets | | |
| Key pathway | | |
| Strongest evidence | | |
| Weakest link | | |
| Distinguishing experiment | | |

### PREDICTIONS:
For each model, what specific, testable predictions does it make?
- qRT-PCR targets that should be down at specific timepoints
- Hormone changes expected
- ROS changes expected
- Phenotypic outcomes under specific conditions"""


def confounder_analysis_prompt(experimental_context: str) -> str:
    """Analyze confounding variables and alternative explanations."""
    return f"""Critically analyze confounding variables for this experiment:

{experimental_context}

**Evaluate each potential confounder**:

1. **EPS OSMOPRIMING**:
   - Can EPS polysaccharides themselves alter water uptake kinetics?
   - Would this alone explain germination improvement?
   - How to control: [specific experimental design]

2. **POLYSACCHARIDE ELICITOR EFFECTS**:
   - Could EPS components trigger plant immune priming (independent of RNA)?
   - Known elicitor activities of bacterial polysaccharides
   - How to control: [specific experimental design]

3. **MICROBIOME EFFECTS**:
   - Could residual bacteria on seeds explain the phenotype?
   - Difference between killed bacteria + EPS vs live bacteria effects
   - How to control: [specific experimental design]

4. **CONTAMINATION / MISANNOTATION**:
   - The target list includes cry8Ba (Bt crystal protein) - likely bacterial contamination in sequencing
   - Reverse transcriptase domains - could be transposon artifacts
   - How to filter: [bioinformatic and experimental approaches]

5. **RNA STABILITY AND DOSAGE**:
   - Are exRNAs stable enough in soaking solution to enter seeds?
   - Is the stoichiometry sufficient for gene silencing?
   - What concentration of exRNA is needed?

6. **NON-SPECIFIC RNA EFFECTS**:
   - Could any dsRNA/ssRNA (not sequence-specific) trigger general responses?
   - PAMPs/DAMPs from foreign nucleic acids
   - How to control: scrambled RNA sequences

For each confounder, provide:
- Likelihood of being the true explanation (High/Medium/Low)
- Specific control experiment to rule it out
- Expected result if this IS vs IS NOT the true explanation"""
