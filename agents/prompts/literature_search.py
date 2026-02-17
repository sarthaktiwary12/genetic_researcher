"""Prompt templates for literature and homolog research."""

SYSTEM_INSTRUCTION = """You are a plant biology literature expert with deep knowledge of:
- Arabidopsis thaliana functional genomics
- Seed germination molecular biology
- Cross-kingdom RNA communication
- Extracellular vesicle and RNA biology
- Plant-microbe interactions at the molecular level

Provide evidence-based literature analysis. Cite specific studies where possible.
Clearly distinguish between well-established findings and recent/preliminary work."""


def homolog_search_prompt(gene_id: str, annotation: str) -> str:
    """Search for homolog information and functional studies."""
    return f"""Research the closest characterized homologs of this spinach gene:

**Gene**: {gene_id} - {annotation}
**Species**: Spinacia oleracea (spinach)

**Provide**:

1. **ARABIDOPSIS HOMOLOG**: What is the closest Arabidopsis thaliana homolog?
   - Gene name and locus ID (e.g., AT1G...)
   - Known mutant phenotypes (especially germination-related)
   - Key publications characterizing this gene

2. **OTHER MODEL SPECIES**: Any relevant homologs in rice, tomato, or other crops?
   - Germination or seedling vigor phenotypes if known

3. **FUNCTIONAL EVIDENCE**:
   - Loss-of-function (knockout/knockdown) phenotypes
   - Overexpression phenotypes
   - Expression patterns during germination (if known)
   - Protein interaction partners

4. **GERMINATION-SPECIFIC DATA**:
   - Is this gene known to be regulated during seed imbibition/germination?
   - ABA/GA regulation of this gene?
   - Any dormancy-related functions?

5. **CROSS-KINGDOM RNA RELEVANCE**:
   - Has this gene or homolog been identified as an sRNA target before?
   - Any evidence of cross-kingdom targeting of this gene family?

Cite specific studies with author, year, and journal where possible."""


def literature_deep_dive_prompt(gene_id: str, annotation: str, initial_analysis: str) -> str:
    """Deep literature dive for high-priority targets."""
    return f"""Conduct a comprehensive literature review for this high-priority spinach gene target:

**Gene**: {gene_id} - {annotation}

**Previous analysis summary**:
{initial_analysis}

**Deep dive tasks**:

1. **MECHANISTIC DETAIL**: What is known about the molecular mechanism of this protein?
   - Enzymatic activity, substrates, products
   - Protein domains and their functions
   - Subcellular localization
   - Post-translational regulation

2. **GERMINATION BIOLOGY**: Detailed role in seed germination:
   - Expression timing (dry seed → imbibition → radicle emergence → seedling establishment)
   - Regulation by hormones (ABA, GA, ethylene, auxin)
   - Response to abiotic stress during germination
   - Known genetic interactions with germination regulators

3. **LOSS-OF-FUNCTION EVIDENCE**: What happens when this gene is missing/reduced?
   - Mutant phenotypes in any species
   - RNAi/VIGS knockdown results
   - Natural variation associated with this locus

4. **NETWORK CONTEXT**: What biological network does this gene participate in?
   - Direct protein-protein interactions
   - Transcriptional regulation (upstream regulators, downstream targets)
   - Metabolic pathway position

5. **SPINACH-SPECIFIC**: Any spinach-specific information?
   - Spinach genome annotation quality for this locus
   - Expression data from spinach transcriptome studies
   - Closest Chenopodium/Amaranthaceae homologs

6. **THERAPEUTIC/AGRICULTURAL RELEVANCE**:
   - Has manipulation of this gene/pathway been used for crop improvement?
   - Seed treatment or priming connections?

Provide detailed, evidence-rich analysis with citations."""


def exrna_biology_prompt() -> str:
    """Research cross-kingdom RNA biology fundamentals."""
    return """Provide a comprehensive review of cross-kingdom extracellular RNA biology relevant to plant-bacteria interactions:

1. **MECHANISMS OF exRNA TRANSFER**:
   - How do bacterial small RNAs reach plant cells?
   - Extracellular vesicle-mediated vs free RNA vs protein-associated
   - Evidence for uptake during seed imbibition specifically

2. **KNOWN EXAMPLES**:
   - Documented cases of bacterial sRNAs affecting plant gene expression
   - Cross-kingdom RNAi examples (fungal, bacterial, any)
   - Evidence quality and reproducibility concerns

3. **MOLECULAR MACHINERY**:
   - Plant AGO proteins involved in processing foreign sRNAs
   - Compatibility of bacterial sRNAs with plant silencing machinery
   - Antisense vs siRNA-like mechanisms

4. **BARRIERS AND SKEPTICISM**:
   - Major criticisms of cross-kingdom RNA transfer
   - Dosage/stoichiometry concerns
   - Technical artifacts to watch for
   - How to experimentally distinguish true exRNA effects from artifacts

5. **EPS MATRIX CONTEXT**:
   - Role of bacterial exopolysaccharides in RNA protection
   - EPS as delivery vehicle for RNAs
   - Distinction between EPS effects and RNA effects

Cite key review papers and primary studies."""
