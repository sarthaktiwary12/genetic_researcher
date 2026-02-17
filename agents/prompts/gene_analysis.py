"""Prompt templates for individual gene target analysis."""

SYSTEM_INSTRUCTION = """You are an expert Plant Molecular Biology researcher specialized in:
- Seed germination physiology (Spinacia oleracea)
- Hormone regulation (ABA/GA/ethylene/auxin/BR)
- ROS/redox biology
- Epigenetic regulation and RNAi/sRNA mechanisms
- Cross-kingdom extracellular RNA effects

You think like a PI + reviewer: mechanistic, evidence-driven, critical about confounders.
Always clearly separate KNOWN facts from INFERRED conclusions from SPECULATIVE hypotheses.
Never invent fold changes or experimental data."""


def single_gene_prompt(gene_id: str, annotation: str, pathway: str) -> str:
    """Generate a comprehensive analysis prompt for a single gene target."""
    return f"""Analyze this spinach gene target predicted to be downregulated by bacterial extracellular small RNAs:

**Gene ID**: {gene_id}
**Annotation**: {annotation}
**Assigned Pathway**: {pathway}

**Experimental Context**:
- Organism: Spinacia oleracea (spinach)
- Treatment: Seeds soaked in bacterial EPS solution "M-9" (4-8 hours)
- Observed phenotype: Improved germination rate, vigor, and early seedling growth
- Mechanism: Bacterial extracellular small RNAs with antisense complementarity to spinach transcripts

**Analyze the following**:

1. **FUNCTION**: What is the known/predicted function of this gene? Use Arabidopsis/model plant homologs if spinach-specific data is limited. Flag any uncertainty in annotation.

2. **GERMINATION RELEVANCE**: How does this gene normally function during seed germination and early seedling development?

3. **DOWNREGULATION EFFECT**: If this transcript is reduced/silenced by bacterial exRNAs, what would be the predicted effect on:
   - Germination rate
   - Seedling vigor
   - Hormone balance (ABA/GA ratio, ethylene sensitivity)
   - ROS homeostasis
   - Growth-defense tradeoffs

4. **MECHANISTIC MODEL**: Provide the most likely mechanistic chain:
   exRNA targeting → transcript reduction → [immediate molecular effect] → [pathway-level effect] → [phenotype]

5. **EVIDENCE STRENGTH**: Rate the evidence supporting this mechanism:
   - Strong: Direct evidence from loss-of-function mutants in germination context
   - Moderate: Evidence from related species/contexts, logical inference
   - Weak: Mostly speculative, limited functional data
   - Unknown: Cannot assess due to poor annotation

6. **KEY REFERENCES**: List 2-5 key papers or known findings supporting your analysis (author, year, key finding). If specific papers are unknown, describe the type of evidence that exists.

Format your response as structured markdown with clear headers."""


def batch_gene_summary_prompt(gene_list: list[dict]) -> str:
    """Generate a prompt for quick-scoring a batch of genes."""
    genes_text = "\n".join(
        f"- {g['gene_id']}: {g['annotation']} [{g['pathway']}]"
        for g in gene_list
    )
    return f"""Quickly assess these spinach gene targets for their relevance to germination improvement when downregulated by bacterial exRNAs:

{genes_text}

**Context**: Seeds soaked in bacterial EPS "M-9" show improved germination and vigor. ExRNAs may silence these transcripts.

For each gene, provide a ONE-LINE assessment:
Gene ID | Priority (High/Medium/Low) | Key reason downregulation helps germination | Evidence strength (Strong/Moderate/Weak/Unknown)

Then provide a 3-line summary of the most interesting patterns you see across this batch."""


def priority_ranking_prompt(gene_analyses: str) -> str:
    """Generate a prompt for ranking genes after individual analyses."""
    return f"""Based on the following individual gene analyses, create a prioritized ranking:

{gene_analyses}

**Task**: Rank ALL genes into three tiers:

**HIGH PRIORITY** (strong mechanistic link to germination improvement):
- List each gene with a 1-sentence rationale
- These should have clear, evidence-based mechanisms

**MEDIUM PRIORITY** (plausible but less direct):
- List each gene with a 1-sentence rationale

**LOW PRIORITY** (unlikely, unknown, or housekeeping):
- List each gene with a 1-sentence rationale

Format as a markdown table:
| Rank | Gene ID | Annotation | Priority | Key Mechanism | Evidence |"""
