"""Prompt templates for pathway-level analysis."""

SYSTEM_INSTRUCTION = """You are an expert plant systems biologist specializing in:
- Hormone signaling networks (ABA, GA, ethylene, auxin, BR, JA/SA)
- Defense-growth tradeoff mechanisms
- ROS/redox signaling in seed germination
- Epigenetic regulation of developmental transitions
- Nutrient transport and metabolic priming in seeds

Provide pathway-level analysis that connects individual gene functions to emergent pathway behaviors.
Always consider crosstalk between pathways."""


def pathway_analysis_prompt(
    pathway_name: str,
    genes: list[dict],
    gene_analyses: str,
) -> str:
    """Analyze a group of genes belonging to the same pathway."""
    gene_list = "\n".join(
        f"- {g['gene_id']}: {g['annotation']}" for g in genes
    )
    return f"""Analyze this pathway in the context of bacterial exRNA-mediated germination improvement in spinach:

**Pathway**: {pathway_name}
**Genes in this pathway**:
{gene_list}

**Individual gene analysis summaries**:
{gene_analyses}

**Provide**:

1. **PATHWAY OVERVIEW**: How does this pathway normally function during seed germination?

2. **COORDINATED DOWNREGULATION**: If ALL these genes in this pathway are simultaneously reduced by bacterial exRNAs, what is the predicted net effect on:
   - The pathway's overall activity
   - Germination timing and rate
   - Seedling vigor and growth

3. **SYNERGISTIC vs REDUNDANT EFFECTS**: Among these genes:
   - Which pairs/groups would have synergistic effects if co-downregulated?
   - Which might be redundant (same effect)?
   - Are any antagonistic (downregulating one might counteract another)?

4. **CROSSTALK**: How does modulating this pathway affect other key germination pathways?
   - Hormone balance
   - ROS signaling
   - Growth-defense allocation
   - Energy/carbon metabolism

5. **NET PREDICTION**: Overall, does downregulation of this gene set HELP or HINDER germination? Rate confidence (High/Medium/Low).

6. **KEY UNKNOWNS**: What information is missing that would strengthen this analysis?

Format as structured markdown."""


def cross_pathway_prompt(pathway_summaries: str) -> str:
    """Analyze interactions between multiple pathways."""
    return f"""Given these pathway-level analyses of spinach genes targeted by bacterial exRNAs:

{pathway_summaries}

**Analyze cross-pathway interactions**:

1. **CONVERGENCE POINTS**: Where do multiple pathways converge on the same germination-relevant outcome?

2. **AMPLIFICATION LOOPS**: Are there positive feedback loops where downregulation in one pathway amplifies effects in another?

3. **POTENTIAL CONFLICTS**: Are any pathway-level effects contradictory? How might they resolve?

4. **MASTER REGULATORS**: Which individual genes sit at pathway intersection points and would have outsized effects?

5. **EMERGENT PROPERTIES**: What system-level properties emerge from simultaneous modulation of all these pathways that wouldn't be predicted from any single pathway?

Provide a network diagram description (text-based) showing key interactions."""
