"""Prompt templates for cross-target theme extraction and synthesis."""

SYSTEM_INSTRUCTION = """You are a systems biology synthesizer who identifies emergent patterns across large datasets.
You specialize in:
- Meta-analysis of gene function data
- Identifying convergent biological themes
- Growth-defense tradeoff theory
- Seed biology and developmental transitions
- Connecting molecular mechanisms to whole-organism phenotypes

Focus on themes that are mechanistically coherent and experimentally testable."""


def theme_extraction_prompt(all_gene_summaries: str) -> str:
    """Extract cross-cutting themes from all gene target analyses."""
    return f"""Analyze these gene target summaries and extract dominant biological themes:

{all_gene_summaries}

**Identify and deeply analyze each theme**:

### THEME 1: Defense Downshift
- Which targets belong to this theme? (EDR2, MOS1, RLKs, disease resistance proteins, etc.)
- Mechanism: How does reducing defense signaling enable growth allocation?
- Evidence from defense-growth tradeoff literature
- Predicted impact on germination: direction and magnitude

### THEME 2: Epigenetic Remodeling
- Which targets? (DNA methyltransferase, HIRA, SUVR5, PHD domain, GIS2)
- Mechanism: How does altering epigenetic marks release germination programs?
- Connection to seed dormancy regulation
- Predicted impact

### THEME 3: ROS/Redox Optimization
- Which targets? (GST, peroxidase, 6-PGDH, rhodanese, cytochrome P450)
- Mechanism: How does modulating ROS detox affect the ROS signaling window for germination?
- ROS as both signal and damage agent in seeds
- Predicted impact

### THEME 4: Hormone Node Modulation
- Which targets? (Ethylene receptor, AHP-like, NAC TF, MYB TF, LOX)
- Mechanism: How do these hits converge on hormone sensitivity/production?
- ABA/GA balance, ethylene responsiveness
- Predicted impact

### THEME 5: Transport/Ion Homeostasis
- Which targets? (CNGC, cation-chloride cotransporters, NRT1/PTR, ABC transporters)
- Mechanism: How does altered transport affect water uptake, ion balance, nutrient mobilization?
- Predicted impact

### THEME 6: Metabolic Priming
- Which targets? (TPS/T6P, aspartokinase, CTP synthase, phytoene synthase)
- Mechanism: How does altering these metabolic genes prime energy/biosynthesis?
- T6P as sugar signaling hub
- Predicted impact

### THEME INTERACTIONS:
- Which themes reinforce each other?
- Are there conflicts between themes?
- What is the minimal set of themes needed to explain the phenotype?

### OVERALL NARRATIVE:
In 5-10 sentences, provide a coherent narrative explaining how bacterial exRNAs could coordinately reprogram spinach seed germination by hitting these specific targets."""


def validation_plan_prompt(themes: str, causal_models: str) -> str:
    """Design a practical validation experimental plan."""
    return f"""Based on these themes and causal models, design a practical stepwise validation plan:

**Themes**:
{themes}

**Causal Models**:
{causal_models}

**Design a validation plan with these experiments**:

### TIER 1: ESSENTIAL CONTROLS (do these first)
1. **RNase treatment**: EPS + RNase vs EPS alone vs water
   - Include heat-inactivated RNase control
   - Expected result if RNA is causal vs not

2. **EPS fractionation**: RNA-enriched fraction vs polysaccharide-only fraction
   - Method for separation
   - Expected results

3. **Dose response**: Multiple concentrations of M-9 EPS
   - Suggested concentrations
   - Expected dose-response curve shape

### TIER 2: TARGET VALIDATION
4. **qRT-PCR time-course**: Top 10-15 targets
   - Timepoints: 0h, 6h, 12h, 24h, 48h post-imbibition
   - Reference genes for spinach
   - Expected expression patterns

5. **Hormone markers**: Proxy genes for hormone status
   - ABA-responsive genes
   - GA-responsive genes
   - Ethylene response markers
   - Suggested specific genes

### TIER 3: MECHANISTIC VALIDATION
6. **ROS assays**: H2O2 quantification, antioxidant enzyme activities
   - Methods and timepoints
   - Expected direction of change

7. **Small RNA uptake**: Demonstrate exRNA entry into seed cells
   - Labeled RNA experiments
   - In situ hybridization approaches

8. **Degradome/PARE sequencing**: Evidence of target cleavage
   - What to look for
   - Controls needed

### TIER 4: ADVANCED VALIDATION
9. **Synthetic mimics**: Use synthetic antisense oligos matching top targets
   - Which targets to test first
   - Delivery method
   - Expected phenotype

10. **Genetic validation**: If available, test in species with mutants
    - Arabidopsis homolog mutant lines
    - Expected germination phenotypes

For each experiment, specify:
- Priority (Critical/Important/Nice-to-have)
- Estimated difficulty (Easy/Moderate/Hard)
- Timeline
- What result would strongly support vs refute the exRNA hypothesis"""
