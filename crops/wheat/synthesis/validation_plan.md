# Validation Plan — Wheat (Triticum aestivum)

# Comprehensive 4-Tier Validation Plan: Bacterial exRNA-Mediated Germination Improvement System

## Critical Prefatory Notes

> **Species Discrepancy [KNOWN]**: The ranked targets, causal models, and confounder analyses all concern *Spinacia oleracea* (spinach; SOV gene IDs), while the crop header specifies *Triticum aestivum* (wheat). This validation plan is designed to be **applicable to both species** where possible, with explicit flags where wheat-specific or spinach-specific adaptations are required. Where wheat orthologs of SOV targets are cited, these are [INFERRED] based on synteny and BLAST homology and require independent confirmation.

> **Foundational Uncertainty [INFERRED]**: Cross-kingdom delivery of functional bacterial small RNAs to plant seed cells is an emerging, incompletely validated mechanism. The entire validation plan is structured to first establish *whether* the mechanism operates before characterizing *how* it operates. Experiments are ordered to maximize falsifiability at minimum cost.

> **Confounder Priority [KNOWN]**: EPS osmopriming is the single most likely alternative explanation for any observed phenotypic improvement. Tier 1 is designed almost entirely around ruling this out before any mechanistic investment is made.

---

## Tier 1: Essential Controls (Confounder Elimination)

*Rationale: Before any molecular mechanism is investigated, the phenotypic effect must be demonstrated to be (a) real, (b) reproducible, (c) attributable to RNA rather than EPS physicochemistry, and (d) sequence-specific. These experiments should be completed and interpreted before Tier 2 begins. Failure to pass Tier 1 gates invalidates the entire downstream mechanistic framework.*

---

### Experiment 1.1 — Phenotypic Baseline and Dose-Response Characterization

**Experiment**: Systematic germination assay across a full dose-response matrix of the bacterial EPS/exRNA preparation, with multiple germination metrics quantified under optimal and suboptimal conditions.

**Hypothesis tested**: Does the preparation produce a statistically robust, dose-dependent germination improvement that is reproducible across seed lots, growth conditions, and independent laboratories? This is the prerequisite for all downstream experiments.

**Method**:
- Use minimum 5 independently prepared seed lots (wheat: cv. Chinese Spring or local adapted variety; spinach: cv. Bloomsdale or equivalent) to capture seed lot variance
- Apply preparation at 5 concentrations: 0×, 0.1×, 0.5×, 1× (standard), 5× working concentration
- Germination conditions: (a) optimal (25°C, continuous moisture, dark), (b) mild drought stress (−0.3 MPa PEG-6000 osmoticum), (c) salinity stress (100 mM NaCl), (d) cold stress (10°C)
- Metrics: Final germination percentage (FGP), mean germination time (MGT), germination index (GI), seedling vigor index (SVI), root length at 7 days, shoot length at 7 days
- Minimum n = 50 seeds per replicate, 4 biological replicates per condition
- Statistical analysis: Two-way ANOVA with Tukey post-hoc correction; effect size (Cohen's d) reported alongside p-values
- Pre-register the study on OSF or equivalent before data collection [RECOMMENDED]

**Expected result if exRNA mechanism is real**: Dose-dependent improvement in FGP, MGT, and SVI that plateaus at saturation; effect is reproducible across seed lots with CV < 20%; effect is larger under stress conditions where dormancy-maintenance programs are more active (consistent with the model that exRNAs dismantle dormancy braking systems)

**Expected result if confounder (osmopriming)**: Improvement is observed but is not dose-dependent above a threshold concentration; effect is similar across stress and optimal conditions; effect is comparable to published osmopriming benchmarks (10–30% FGP improvement, 1–3 day MGT reduction) [KNOWN; Farooq et al. 2005]

**Timeline**: 4–6 weeks (including seed lot procurement, treatment preparation, germination assays, statistical analysis)

**Difficulty**: Low

**Priority**: Critical — no downstream experiments are justified without a robust phenotype

---

### Experiment 1.2 — RNA Destruction Controls: Separating EPS Physicochemistry from RNA Activity

**Experiment**: Parallel germination assays comparing intact preparation against RNA-destroyed versions that preserve all non-RNA components, to determine what fraction of the phenotype requires intact RNA.

**Hypothesis tested**: Is the germination improvement dependent on intact RNA molecules, or is it fully explained by the EPS matrix and associated non-RNA components?

**Method**:
- Prepare five treatment arms from the same preparation batch:
  1. **Intact preparation** (positive control)
  2. **RNase A-treated** (10 μg/mL, 37°C, 60 min): degrades single-stranded RNA; preserves EPS, proteins, lipids, DNA
  3. **RNase III-treated** (2 U/mL, 37°C, 60 min): degrades double-stranded RNA and structured RNA; preserves EPS
  4. **Combined RNase A + III treatment**: comprehensive RNA destruction
  5. **Heat-denatured** (121°C, 20 min autoclave): destroys RNA and proteins; preserves polysaccharide osmopriming capacity; may alter EPS structure
  6. **Proteinase K-treated** (100 μg/mL, 55°C, 60 min): degrades proteins; preserves RNA and EPS — tests protein contribution
  7. **Molecular weight cutoff (MWCO) fractionation**: 10 kDa MWCO spin column separates small RNA fraction (< 10 kDa) from EPS and protein fraction (> 10 kDa); test both fractions independently
- Verify RNA destruction by Bioanalyzer or TapeStation before seed application
- Verify EPS preservation by phenol-sulfuric acid assay (total carbohydrate)
- Apply all arms to seeds; measure FGP, MGT, SVI as in Experiment 1.1
- Conduct in both optimal and stress conditions

**Expected result if exRNA mechanism is real**: RNase A+III treatment significantly reduces phenotypic improvement (ideally to near-baseline); heat denaturation also reduces effect; the < 10 kDa fraction retains substantial activity; the > 10 kDa fraction shows reduced but non-zero activity (EPS osmopriming component); proteinase K treatment has minimal effect

**Expected result if confounder (osmopriming)**: RNase treatment has no significant effect on phenotype; heat denaturation may partially reduce effect (altered EPS rheology) but substantial improvement persists; both fractions show similar activity proportional to their EPS content; the pattern matches pure osmopriming controls

**Critical interpretation note [INFERRED]**: A partial reduction by RNase treatment would be the most likely real-world outcome if both mechanisms operate simultaneously. A decision threshold must be pre-specified: e.g., "if RNase treatment reduces the phenotype by < 30% of the intact preparation effect, we conclude the RNA contribution is minor relative to EPS osmopriming." This threshold should be pre-registered.

**Timeline**: 6–8 weeks (including preparation of all treatment arms, verification assays, germination assays)

**Difficulty**: Medium

**Priority**: Critical — this is the primary mechanistic gate experiment

---

### Experiment 1.3 — Matched Physicochemical Controls: Osmotic and Rheological Equivalence

**Experiment**: Compare the EPS preparation against solutions matched for osmotic potential, viscosity, and water activity but containing no biological molecules, to isolate the osmopriming contribution with precision.

**Hypothesis tested**: Can the observed germination improvement be fully recapitulated by a non-biological solution with equivalent physicochemical properties?

**Method**:
- Characterize the EPS preparation: measure osmotic potential (vapor pressure osmometry), viscosity (rheometer, 25°C), water activity (Aw meter), pH, conductivity
- Prepare matched controls:
  1. **PEG-6000** at matched osmotic potential (standard osmopriming agent) [KNOWN benchmark]
  2. **Methylcellulose** at matched viscosity (polymer control without osmopriming activity)
  3. **Hydroxyethyl cellulose** at matched viscosity and osmotic potential
  4. **Xanthan gum** at matched viscosity (bacterial EPS analog, no plant-active RNA)
  5. **Pure water** (hydropriming control)
  6. **Dry seed** (unprimed negative control)
- Apply all controls under identical conditions to Experiment 1.1
- Include the intact preparation and RNase-treated preparation as internal references
- Measure FGP, MGT, SVI, root architecture (primary root length, lateral root number at 7 days)

**Expected result if exRNA mechanism is real**: The EPS preparation significantly outperforms all physicochemical controls, including PEG-6000 at matched osmotic potential; the excess improvement above PEG-6000 is the "RNA-attributable" component; this excess is abolished by RNase treatment

**Expected result if confounder (osmopriming)**: The EPS preparation performs comparably to PEG-6000 or other matched controls; no statistically significant difference between EPS and physicochemically equivalent non-biological solutions; the effect is fully explained by controlled hydration kinetics

**Timeline**: 6–8 weeks (parallel with Experiment 1.2)

**Difficulty**: Low-Medium

**Priority**: Critical

---

### Experiment 1.4 — Sequence Specificity Control: Scrambled RNA and Heterologous RNA

**Experiment**: Test whether the RNA effect (if confirmed in 1.2) is sequence-specific or a non-specific RNA effect (e.g., dsRNA innate immune priming, RNA-mediated osmopriming).

**Hypothesis tested**: Is the germination improvement dependent on the specific nucleotide sequences of the bacterial exRNAs, or would any RNA of similar size and structure produce the same effect?

**Method**:
- Synthesize or purchase:
  1. **Scrambled sequence RNA**: same nucleotide composition as the top 5 predicted exRNA sequences, but randomized order (no predicted complementarity to any plant transcript); synthesize as 21–24 nt single-stranded RNA
  2. **Irrelevant dsRNA**: poly(I:C) at matched concentration (non-sequence-specific dsRNA immune elicitor)
  3. **Plant-irrelevant bacterial RNA**: total RNA from a non-PGPR bacterium (*E. coli* K-12) at matched concentration
  4. **Synthetic mimics of top predicted exRNAs**: chemically synthesized 21–24 nt RNAs matching the predicted sequences (if sequences are known from sequencing data)
  5. **Antisense controls**: reverse-complement of the predicted exRNA sequences (tests strand specificity)
- Encapsulate all RNA preparations in liposomes or chitosan nanoparticles to match the vesicular delivery mode of OMV-associated exRNAs [INFERRED delivery mechanism]
- Apply to seeds; measure FGP, MGT, SVI
- Include intact preparation and RNase-treated preparation as references

**Expected result if exRNA mechanism is real**: Scrambled RNA shows no improvement above RNase-treated baseline; synthetic mimics of predicted exRNAs partially or fully recapitulate the improvement; irrelevant bacterial RNA shows no improvement; antisense controls show no improvement; poly(I:C) may show a non-specific immune priming effect that is distinguishable from the sequence-specific effect

**Expected result if confounder (non-specific RNA effect)**: Scrambled RNA, poly(I:C), and *E. coli* RNA all improve germination comparably to the intact preparation; no sequence specificity is observed; the effect correlates with RNA concentration rather than sequence

**Timeline**: 8–10 weeks (RNA synthesis/procurement adds lead time)

**Difficulty**: Medium-High

**Priority**: Critical — this experiment distinguishes sequence-specific silencing from non-specific RNA effects

---

### Experiment 1.5 — Microbiome Confounder: Sterile vs. Non-Sterile Conditions

**Experiment**: Determine whether the observed effect requires viable bacteria or is mediated by cell-free components, and whether seed microbiome perturbation contributes to the phenotype.

**Hypothesis tested**: Is the germination improvement caused by the cell-free exRNA/EPS preparation itself, or does it require live bacterial colonization, microbiome restructuring, or indirect effects on the seed-associated microbial community?

**Method**:
- Compare:
  1. **Live bacterial suspension** (positive control for colonization effects)
  2. **Cell-free supernatant** (standard preparation): 0.22 μm filtered to remove cells
  3. **Sterile-filtered + UV-irradiated supernatant**: additional RNA photodegradation step
  4. **Sterile seeds** (surface-sterilized with 1% NaOCl, 70% ethanol): eliminates seed microbiome
  5. **Non-sterile seeds** (standard surface cleaning only): retains seed microbiome
  6. **Gnotobiotic system** (if available): germination in sterile agar medium under laminar flow
- Cross all treatment arms with sterile/non-sterile seed conditions (2×3 factorial minimum)
- Characterize seed microbiome by 16S rRNA amplicon sequencing (V3-V4 region) before and after treatment
- Measure FGP, MGT, SVI as standard

**Expected result if exRNA mechanism is real**: Cell-free supernatant improves germination comparably to live bacteria; effect is observed in sterile seeds (eliminating microbiome restructuring as explanation); UV irradiation reduces effect; microbiome composition changes are not correlated with germination improvement across treatment arms

**Expected result if confounder (microbiome effect)**: Live bacteria outperform cell-free supernatant substantially; sterile seeds show reduced response; 16S data show consistent microbiome shifts in responding seeds; the effect correlates with colonization density rather than exRNA concentration

**Timeline**: 10–12 weeks (16S sequencing adds 4–6 weeks)

**Difficulty**: Medium-High

**Priority**: High

---

### Experiment 1.6 — Multi-Genotype and Multi-Environment Reproducibility

**Experiment**: Validate the phenotype across multiple wheat/spinach genotypes and at least two independent laboratory environments to confirm reproducibility and generalizability.

**Hypothesis tested**: Is the germination improvement genotype-specific (suggesting specific target gene polymorphisms matter) or broadly applicable (suggesting a conserved mechanism)?

**Method**:
- For wheat: test minimum 5 genotypes spanning diversity: (a) Chinese Spring (reference), (b) a modern high-yielding variety, (c) a drought-tolerant landrace, (d) a winter wheat variety, (e) a durum wheat (*T. turgidum* subsp. *durum*) as outgroup
- For spinach (if primary species): test minimum 3 commercial varieties with known dormancy differences
- Conduct identical protocols at two independent institutions (inter-laboratory reproducibility)
- Include all Tier 1 controls (RNase-treated, PEG-matched, scrambled RNA) at each site
- Pre-specify the minimum effect size considered biologically meaningful (e.g., ≥ 10% FGP improvement AND ≥ 15% MGT reduction relative to RNase-treated control)

**Expected result if exRNA mechanism is real**: Improvement is observed across most genotypes, with magnitude variation reflecting target gene expression levels or sequence polymorphisms in target sites; inter-laboratory reproducibility is high (CV < 25% across sites)

**Expected result if confounder**: Effect magnitude is uniform across genotypes (consistent with non-specific osmopriming); inter-laboratory reproducibility may be high (osmopriming is robust) but is not genotype-dependent

**Timeline**: 12–16 weeks (multi-site coordination adds time)

**Difficulty**: High

**Priority**: High

---

## Tier 2: Target Validation

*Rationale: Tier 2 begins only if Tier 1 establishes that (a) a robust phenotype exists, (b) it is at least partially RNA-dependent (Experiment 1.2), and (c) it shows sequence specificity (Experiment 1.4). The goal is to validate that specific predicted target genes are actually downregulated in treated seeds, and that their downregulation causally contributes to the phenotype. The top 5–8 targets from the ranked analysis are prioritized.*

---

### Experiment 2.1 — Transcriptome-Wide Target Confirmation: RNA-seq of Treated Seeds

**Experiment**: Genome-wide transcriptome profiling of seeds treated with intact preparation, RNase-treated preparation, and scrambled RNA control, at multiple time points during imbibition, to identify which predicted targets are actually downregulated in an RNA-dependent and sequence-specific manner.

**Hypothesis tested**: Are the 75+ predicted target transcripts (SOV gene IDs in spinach; wheat orthologs TBD) actually downregulated in treated seeds in a manner that requires intact, sequence-specific RNA?

**Method**:
- Time points: 0h (dry seed), 6h, 12h, 24h, 48h post-imbibition (capturing Phase I–III water uptake and early germination)
- Treatments: (a) intact preparation, (b) RNase A+III-treated preparation, (c) scrambled RNA + EPS, (d) PEG-6000 matched control, (e) water control
- Tissue: whole seed (wheat) or embryo + endosperm dissected separately (spinach, if feasible)
- RNA extraction: CTAB method for seed tissue; ribosomal RNA depletion (not poly-A selection, to capture all RNA classes including small RNAs)
- Sequencing: 30M paired-end reads per sample, 150 bp; 3 biological replicates per time point per treatment = minimum 75 libraries
- Small RNA-seq: parallel 15M single-end reads, 50 bp, to detect bacterial exRNAs in plant tissue
- Analysis pipeline: STAR alignment to species reference genome; DESeq2 differential expression; WGCNA co-expression network analysis; target prediction: RNAhybrid or psRNATarget for sRNA-mRNA complementarity scoring
- **Key validation criterion**: A predicted target is "confirmed" only if it is (i) significantly downregulated (FDR < 0.05, |log2FC| > 0.5) in intact vs. RNase-treated preparation, AND (ii) not significantly downregulated in scrambled RNA control vs. water control

**Expected result if exRNA mechanism is real**: 
- A subset of the 75 predicted targets (realistically 20–40%) shows RNA-dependent downregulation
- Downregulation is time-point-specific, peaking at 12–24h post-imbibition
- Small RNA-seq detects bacterial exRNA sequences in plant tissue (critical positive control)
- Co-expression analysis reveals coordinated downregulation of pathway clusters (epigenetic, hormone signaling) consistent with the causal models
- The ethylene receptor ortholog (wheat: *TaETR1/TaERS1*), DNA methyltransferase ortholog (*TaMET1*), and SUVR5 ortholog show the most consistent RNA-dependent downregulation

**Expected result if confounder**: 
- Transcriptome changes in intact vs. RNase-treated preparations are minimal or not enriched for predicted targets
- Differentially expressed genes are enriched for stress-response and osmotic adjustment pathways (consistent with osmopriming)
- No bacterial exRNA sequences are detected in plant tissue by small RNA-seq
- Scrambled RNA control shows similar transcriptome changes to intact preparation

**Timeline**: 16–20 weeks (including library preparation, sequencing, bioinformatics)

**Difficulty**: High

**Priority**: Critical (Tier 2 entry point)

**Wheat-specific note [INFERRED]**: The wheat genome (IWGSC RefSeq v2.1) contains homeologous triads on A, B, and D subgenomes for most target genes. All three homeologs must be monitored; partial suppression of one homeolog may be insufficient for phenotypic effect due to functional redundancy. This substantially increases the complexity of wheat target validation relative to diploid spinach.

---

### Experiment 2.2 — Target 1 Validation: Ethylene Receptor Ortholog (SOV3g000150.1 / TaETR1)

**Experiment**: Validate that the ethylene receptor is downregulated in an RNA-dependent manner and that this downregulation causally promotes germination.

**Hypothesis tested**: Does exRNA-mediated downregulation of the ethylene receptor constitutively activate ethylene signaling in treated seeds, and does this account for a measurable fraction of the germination phenotype?

**Method**:

*Part A — Expression validation*:
- RT-qPCR of ethylene receptor transcript(s) at 6h, 12h, 24h, 48h post-imbibition across all Tier 1 treatment arms
- Wheat: design primers spanning all three homeologs (TaETR1-A, -B, -D) using homeolog-specific primer design (avoid conserved regions)
- Reference genes: *TaActin*, *TaGAPDH*, *TaUBC* (geometric mean normalization per MIQE guidelines)
- Protein confirmation: Western blot with anti-ETR1 antibody (cross-reactive to wheat; verify specificity) or targeted proteomics (PRM-MS) if antibody unavailable

*Part B — Ethylene signaling activity*:
- Measure ethylene production by treated seeds using gas chromatography (GC-FID) at 12h and 24h post-imbibition
- Measure expression of ethylene-responsive genes (*TaERF1*, *TaEIN3*) as downstream reporters
- Apply ethylene biosynthesis inhibitor (AVG, aminoethoxyvinylglycine, 10 μM) to intact preparation-treated seeds: if ethylene signaling mediates the effect, AVG should partially suppress the germination improvement

*Part C — Causal test (if wheat mutants unavailable)*:
- Apply exogenous ethylene (ethephon, 100 μM) to RNase-treated seeds: does exogenous ethylene partially rescue the germination improvement lost by RNA destruction?
- Apply ethylene receptor antagonist (1-MCP, 1-methylcyclopropene, 1 μL/L): does blocking ethylene signaling suppress the intact preparation effect?
- In spinach: if *Arabidopsis etr1* mutant seeds are available, test whether the exRNA preparation provides additional germination benefit beyond the constitutive ethylene signaling of *etr1* (epistasis test)

**Expected result if exRNA mechanism is real**: 
- Ethylene receptor transcript reduced ≥ 30% (RNA-dependent) at 12–24h
- Ethylene-responsive gene expression increased in intact preparation vs. RNase control
- AVG partially suppresses the germination improvement (≥ 20% reduction in effect size)
- Ethephon partially rescues the RNase-treated preparation effect
- 1-MCP suppresses the intact preparation effect

**Expected result if confounder**: 
- Ethylene receptor expression unchanged between intact and RNase-treated preparations
- Ethylene production not elevated in treated seeds
- AVG has no differential effect on intact vs. RNase-treated preparations
- 1-MCP does not suppress the intact preparation effect

**Timeline**: 10–12 weeks

**Difficulty**: Medium

**Priority**: Critical (Tier 1 ranked target)

---

### Experiment 2.3 — Target 2 Validation: DNA Methyltransferase Ortholog (SOV1g033340.1 / TaMET1)

**Experiment**: Validate that the DNA methyltransferase is downregulated in an RNA-dependent manner and that this causes measurable epigenetic changes at germination-regulatory loci.

**Hypothesis tested**: Does exRNA-mediated downregulation of maintenance DNA methyltransferase cause progressive demethylation at GA-responsive and ABA-responsive promoters during imbibition, contributing to transcriptional de-repression of germination programs?

**Method**:

*Part A — Expression validation*:
- RT-qPCR of *TaMET1* (all homeologs) across treatment arms and time points (as in 2.2)
- Immunofluorescence with anti-5-methylcytosine antibody on embryo sections: global methylation level comparison between intact and RNase-treated preparations

*Part B — Locus-specific methylation*:
- Bisulfite sequencing (targeted amplicon bisulfite-seq, TABS-seq) at promoters of:
  - *TaGA20ox* (GA biosynthesis): expected demethylation in intact preparation
  - *TaCYP707A* (ABA catabolism): expected demethylation
  - *TaABI3/TaVP1* (ABA signaling master regulator): expected demethylation or maintained methylation (complex)
  - Transposon-rich regions (Ta-CACTA, Ta-BARE1): expected maintained methylation (test for off-target effects)
- Compare methylation levels: intact preparation vs. RNase-treated vs. water control at 24h and 48h post-imbibition

*Part C — Functional consequence*:
- Apply 5-azacytidine (DNA methylation inhibitor, 10 μM) to RNase-treated seeds: does chemical demethylation partially rescue the germination improvement?
- Measure GA and ABA levels by ELISA or LC-MS/MS in treated seeds: is the hormone ratio shift consistent with epigenetic de-repression of biosynthesis genes?

**Expected result if exRNA mechanism is real**: 
- *TaMET1* downregulated ≥ 25% (RNA-dependent)
- Reduced global 5mC signal by immunofluorescence in intact preparation
- Targeted demethylation at GA biosynthesis gene promoters (≥ 10% reduction in CG methylation)
- 5-azacytidine partially rescues RNase-treated preparation effect
- GA:ABA ratio elevated in intact preparation vs. RNase control

**Expected result if confounder**: 
- *TaMET1* expression unchanged between intact and RNase-treated preparations
- No differential methylation at target loci
- 5-azacytidine has similar effects on intact and RNase-treated preparations
- GA:ABA ratio changes are equivalent between intact preparation and PEG-6000 control (consistent with osmopriming)

**Timeline**: 14–18 weeks (bisulfite sequencing adds significant time)

**Difficulty**: High

**Priority**: High

---

### Experiment 2.4 — Target 3 Validation: SUVR5-like H3K9 Methyltransferase (SOV4g015450.1 / TaSUVR5)

**Experiment**: Validate SUVR5 downregulation and its consequence for H3K9me2 deposition at germination-regulatory chromatin domains.

**Hypothesis tested**: Does exRNA-mediated downregulation of the H3K9 methyltransferase reduce repressive histone marks at dormancy-associated loci, contributing to the epigenetic de-repression cascade proposed in Causal Model 1?

**Method**:

*Part A — Expression validation*:
- RT-qPCR of *TaSUVR5* homeologs across treatment arms and time points

*Part B — Histone modification profiling*:
- ChIP-qPCR (chromatin immunoprecipitation) using anti-H3K9me2 antibody on embryo chromatin from intact preparation vs. RNase-treated preparation at 24h post-imbibition
- Target loci for ChIP-qPCR: same as bisulfite-seq targets in Experiment 2.3, plus transposon-rich regions
- If material permits: CUT&RUN (Cleavage Under Targets and Release Using Nuclease) as a lower-input alternative to ChIP

*Part C — Functional consequence*:
- Apply chaetocin (H3K9 methyltransferase inhibitor, 1 μM) to RNase-treated seeds: does chemical H3K9me2 reduction rescue the germination improvement?

**Expected result if exRNA mechanism is real**: 
- *TaSUVR5* downregulated ≥ 20% (RNA-dependent)
- Reduced H3K9me2 at GA biosynthesis and germination TF loci in intact preparation
- Chaetocin partially rescues RNase-treated preparation effect

**Expected result if confounder**: 
- *TaSUVR5* expression unchanged
- No differential H3K9me2 at target loci
- Chaetocin has equivalent effects on intact and RNase-treated preparations

**Timeline**: 12–16 weeks

**Difficulty**: High (ChIP from seed tissue is technically challenging due to cell wall, starch, and low cell number)

**Priority**: High

**Technical note [KNOWN]**: ChIP from wheat seed embryo tissue is technically demanding due to the small amount of embryo material per seed, high starch content interfering with chromatin isolation, and the large, repetitive wheat genome complicating ChIP-seq analysis. CUT&RUN is strongly preferred as it requires 10–100× less starting material and has lower background. [INFERRED recommendation based on published wheat epigenomics challenges]

---

### Experiment 2.5 — Target 4 Validation: EDR2 Paralogs (Defense Attenuation Pathway)

**Experiment**: Validate downregulation of EDR2-like genes and test whether defense attenuation contributes to germination improvement by freeing metabolic resources.

**Hypothesis tested**: Does exRNA-mediated downregulation of EDR2-like defense regulators reduce basal immunity costs in germinating seeds, contributing to improved germination vigor through resource reallocation?

**Method**:

*Part A — Expression validation*:
- RT-qPCR of wheat EDR2 orthologs (identify by BLAST against TaEDR2 candidates in IWGSC database)
- Measure marker genes of PTI activation: *TaPR1*, *TaWRKY33*, *TaMPK6* expression as downstream reporters

*Part B — Defense-germination tradeoff test*:
- Apply flg22 peptide (flagellin-derived MAMP, 1 μM) to seeds to artificially activate PTI: does PTI activation suppress germination, and does the intact preparation overcome this suppression?
- Measure reactive oxygen species (ROS) burst in treated seeds using luminol-based assay: is ROS production reduced in intact preparation vs. RNase control?
- Measure salicylic acid (SA) and jasmonic acid (JA) levels by LC-MS/MS: are defense hormone levels reduced in intact preparation?

*Part C — Causal test*:
- Apply SA biosynthesis inhibitor (NahG expression or paclobutrazol as SA analog inhibitor) to RNase-treated seeds: does reducing defense hormone levels rescue germination improvement?

**Expected result if exRNA mechanism is real**: 
- EDR2 orthologs downregulated ≥ 20% (RNA-dependent)
- Reduced PTI marker gene expression in intact preparation
- Reduced ROS burst in intact preparation
- Reduced SA/JA levels in intact preparation
- flg22 suppresses germination in RNase-treated but not intact preparation

**Expected result if confounder**: 
- EDR2 expression unchanged between intact and RNase-treated preparations
- ROS and defense hormone levels not differentially affected
- flg22 suppression of germination is equivalent across treatment arms

**Timeline**: 10–12 weeks

**Difficulty**: Medium

**Priority**: High

---

### Experiment 2.6 — Target 5 Validation: LOX/Jasmonate Biosynthesis (SOV3g035520.1)

**Experiment**: Validate LOX downregulation and test whether reduced JA biosynthesis contributes to dormancy release by relieving JA-mediated germination suppression.

**Hypothesis tested**: Does exRNA-mediated downregulation of lipoxygenase reduce JA biosynthesis in germinating seeds, thereby reducing JA-mediated suppression of germination?

**Method**:

*Part A — Expression validation*:
- RT-qPCR of wheat LOX orthologs (*TaLOX1*, *TaLOX2*; identify homeologs)
- Measure JA and JA-Ile levels by LC-MS/MS in treated seeds at 12h and 24h post-imbibition

*Part B — Causal test*:
- Apply exogenous methyl-JA (MeJA, 10 μM) to intact preparation-treated seeds: does exogenous JA suppress the germination improvement?
- Apply JA biosynthesis inhibitor (DIECA, 1 mM) to RNase-treated seeds: does JA reduction rescue germination improvement?

*Part C — Interaction with ABA pathway*:
- JA and ABA interact synergistically to suppress germination [KNOWN; Linkies & Leubner-Metzger 2012]. Measure ABA levels in LOX-suppressed (intact preparation) vs. control (RNase-treated) seeds: is ABA reduction correlated with LOX downregulation?

**Expected result if exRNA mechanism is real**: 
- LOX transcript reduced ≥ 25% (RNA-dependent)
- JA/JA-Ile levels reduced in intact preparation vs. RNase control
- MeJA suppresses the germination improvement of the intact preparation
- DIECA partially rescues RNase-treated preparation effect
- ABA levels are reduced in intact preparation, correlated with JA reduction

**Expected result if confounder**: 
- LOX expression unchanged
- JA levels not differentially affected
- MeJA and DIECA have equivalent effects across treatment arms

**Timeline**: 10–12 weeks

**Difficulty**: Medium (LC-MS/MS for hormone quantification requires specialized equipment)

**Priority**: High

---

### Experiment 2.7 — Bacterial exRNA Detection in Plant Tissue: Cross-Kingdom Delivery Confirmation

**Experiment**: Directly detect bacterial exRNA sequences within plant seed cells after treatment, to confirm the foundational premise of cross-kingdom RNA delivery.

**Hypothesis tested**: Do bacterial exRNAs physically enter seed cells during imbibition, and are they detectable at concentrations consistent with functional RISC loading?

**Method**:
- **Small RNA-seq**: As described in Experiment 2.1; specifically map reads to bacterial genome to identify bacterial-origin small RNAs in plant tissue. Strict filtering: require ≥ 2 mismatches to plant genome to exclude plant-derived reads mapping to bacterial sequences by chance
- **Northern blot**: Probe for top 3 predicted exRNA sequences in total RNA from treated seeds; compare signal between intact and RNase-treated preparations
- **In situ hybridization (ISH)**: Fluorescent ISH (FISH) with probes against top 2 predicted exRNA sequences on embryo sections; determine which cell types contain bacterial exRNAs (aleurone, embryo axis, endosperm)
- **RISC loading assay**: Immunoprecipitate AGO1 (or wheat AGO1 ortholog) from treated seed extracts; sequence associated small RNAs; determine whether bacterial exRNA sequences are enriched in AGO1-IP relative to total small RNA fraction
- **Quantification**: Estimate copy number per cell using spike-in controls (synthetic RNA of known concentration added before extraction)

**Expected result if exRNA mechanism is real**: 
- Bacterial exRNA sequences detected in plant tissue by small RNA-seq (≥ 10 reads per million mapping to bacterial sequences, above background)
- Northern blot signal present in intact preparation, absent in RNase-treated preparation
- FISH signal in embryo axis cells (the primary germination-executing tissue)
- AGO1-IP enriches bacterial exRNA sequences ≥ 3-fold relative to input
- Copy number ≥ 1 bacterial exRNA per cell (minimum threshold for functional silencing) [INFERRED threshold from animal RNAi literature; plant threshold unknown]

**Expected result if confounder**: 
- No bacterial exRNA sequences detected above background in plant tissue
- Northern blot negative
- FISH signal absent or restricted to seed surface (not internalized)
- AGO1-IP does not enrich bacterial exRNA sequences

**Critical note [SPECULATIVE]**: The minimum copy number of exogenous sRNA required for functional gene silencing in plant cells is unknown. Even if bacterial exRNAs are detected, their functional sufficiency for RISC-mediated silencing at the concentrations achieved cannot be assumed. This experiment is necessary but not sufficient to confirm the mechanism.

**Timeline**: 16–20 weeks

**Difficulty**: Very High (FISH on seed tissue and AGO1-IP from limited seed material are technically demanding)

**Priority**: Critical (foundational premise validation)

---

### Experiment 2.8 — Annotation Artifact Screening: Transposon-Derived and DUF Targets

**Experiment**: Systematically evaluate whether predicted targets annotated as reverse transcriptases, DNA polymerases, or DUF proteins represent genuine regulatory targets or annotation artifacts.

**Hypothesis tested**: Are the 5 reverse transcriptase-annotated targets (SOV2g004250.1, SOV4g025520.1, SOV3g033520.1, SOV1g003910.1, SOV4g035390.1) genuine protein-coding genes regulated during germination, or are they transposon-derived sequences whose "expression" reflects transposon activity rather than functional gene regulation?

**Method**:
- BLAST all 5 RT-domain sequences against RepBase transposon database and TREP (Triticeae Repeat Sequence Database for wheat)
- Map RT-domain transcripts to genome: determine whether they originate from annotated transposable elements (TEs)
- Examine RNA-seq read distribution: genuine mRNAs show 5' cap and 3' poly-A signal; TE transcripts show different patterns
- Check for open reading frames and ribosome profiling data (if available for spinach/wheat) to confirm translation
- Examine expression across developmental stages: genuine regulatory genes show developmental stage-specificity; TE transcripts may be constitutive or stress-induced
- Decision rule: if ≥ 3 of 5 criteria indicate TE origin, deprioritize these targets from further validation

**Expected result**: [INFERRED] At least 3 of 5 RT-domain targets are likely TE-derived sequences; their "downregulation" may reflect reduced TE activity rather than suppression of a functional protein-coding gene. This would not necessarily eliminate them as relevant targets (TE silencing has epigenetic consequences) but would change the mechanistic interpretation.

**Timeline**: 4–6 weeks (primarily bioinformatics)

**Difficulty**: Medium (bioinformatics-intensive)

**Priority**: High (prevents wasted experimental effort on artifact targets)

---

## Tier 3: Mechanistic Studies

*Rationale: Tier 3 begins only if Tier 2 confirms that (a) multiple predicted targets are genuinely downregulated in an RNA-dependent manner, (b) bacterial exRNAs are detectable in plant tissue, and (c) at least one causal test (pharmacological rescue) supports the mechanistic model. The goal is to establish pathway-level mechanisms and test the three causal models against each other.*

---

### Experiment 3.1 — Causal Model Discrimination: Epigenetic vs. Hormone vs. Defense as Primary Driver

**Experiment**: Use pathway-specific inhibitors and activators to determine the relative contribution of the three proposed causal models (epigenetic de-repression, hormone signaling cascade, defense attenuation) to the overall germination phenotype.

**Hypothesis tested**: Which causal model accounts for the largest fraction of the RNA-dependent germination improvement? Are the three pathways additive, synergistic, or hierarchically organized?

**Method**:
- Design a factorial inhibitor experiment with 7 treatment arms applied to intact preparation-treated seeds:
  1. **Intact preparation alone** (positive control)
  2. **Intact preparation + 5-azacytidine** (DNA methylation inhibitor, epigenetic pathway activator — tests if epigenetic de-repression is already maximal)
  3. **Intact preparation + chaetocin** (H3K9me2 inhibitor — as above)
  4. **Intact preparation + AVG** (ethylene biosynthesis inhibitor — blocks hormone pathway)
  5. **Intact preparation + paclobutrazol** (GA biosynthesis inhibitor — blocks GA arm of hormone pathway)
  6. **Intact preparation + flg22** (PTI activator — re-activates defense pathway)
  7. **Intact preparation + all three pathway inhibitors** (tests for additivity/synergy)
- Apply same inhibitor panel to RNase-treated preparation (tests whether inhibitors affect the osmopriming baseline)
- Measure FGP, MGT, SVI, and pathway-specific markers (hormone levels, histone marks, defense gene expression)
- Quantify the fraction of the RNA-dependent effect (intact minus RNase-treated) suppressed by each inhibitor

**Expected result if Causal Model 1 (epigenetic) is primary**: 
- 5-azacytidine and chaetocin do not further improve the intact preparation effect (epigenetic de-repression already achieved)
- AVG and paclobutrazol suppress the intact preparation effect substantially (hormone changes are downstream of epigenetic de-repression)
- flg22 partially suppresses the effect
- Triple inhibitor combination suppresses ≥ 70% of the RNA-dependent effect

**Expected result if Causal Model 2 (hormone cascade) is primary**: 
- AVG and paclobutrazol suppress ≥ 50% of the RNA-dependent effect independently
- 5-azacytidine and chaetocin have smaller effects
- The hormone pathway is the dominant driver

**Expected result if Causal Model 3 (defense attenuation) is primary**: 
- flg22 suppresses ≥ 40% of the RNA-dependent effect
- Defense pathway inhibition is the dominant driver

**Timeline**: 12–16 weeks

**Difficulty**: High

**Priority**: High

---

### Experiment 3.2 — RISC Mechanism Confirmation: AGO Mutant or RNAi Knockdown Test

**Experiment**: Determine whether the exRNA effect requires the plant's RNA-induced silencing complex (RISC) machinery, specifically AGO1, to mediate target gene suppression.

**Hypothesis tested**: Is the bacterial exRNA effect dependent on the plant's endogenous sRNA pathway (AGO1/RISC-mediated), or does it operate through an AGO-independent mechanism (e.g., RNA-RNA hybridization blocking translation, dsRNA-triggered immune response)?

**Method**:

*Option A (Arabidopsis proxy system)*:
- Test the intact preparation on *Arabidopsis thaliana ago1-27* hypomorphic mutant seeds vs. wild-type Col-0
- *ago1-27* has reduced RISC activity but is viable [KNOWN; Morel et al. 2002]
- If the exRNA effect is abolished in *ago1-27*, RISC-dependence is confirmed
- Also test *ago2*, *ago4*, *ago6* mutants (different AGO family members with different sRNA class preferences)
- Note: this is an Arabidopsis proxy; results are [INFERRED] to apply to spinach/wheat

*Option B (wheat/spinach VIGS)*:
- Virus-induced gene silencing (VIGS) of *TaAGO1* in wheat seedlings, then test whether the exRNA preparation retains activity in AGO1-depleted plants
- VIGS in wheat: use Barley Stripe Mosaic Virus (BSMV)-based VIGS system [KNOWN; Holzberg et al. 2002]
- Limitation: VIGS efficiency in seeds is low; this may need to be conducted in seedlings with a modified assay

*Option C (biochemical)*:
- In vitro RISC assembly assay: prepare plant cell-free extract from imbibing seeds; add synthetic bacterial exRNA sequences; measure cleavage of synthetic target mRNA; compare with scrambled RNA control
- This directly tests whether bacterial exRNAs can be loaded into plant RISC and direct target cleavage [SPECULATIVE — this assay has not been established for seed extracts]

**Expected result if exRNA mechanism is real**: 
- *ago1-27* seeds show significantly reduced response to intact preparation compared to wild-type
- VIGS-mediated AGO1 knockdown reduces the preparation effect in seedling assays
- In vitro RISC assay shows bacterial exRNA-directed cleavage of target mRNA

**Expected result if confounder or AGO-independent mechanism**: 
- *ago1-27* seeds respond comparably to wild-type
- VIGS-AGO1 does not reduce the preparation effect
- In vitro RISC assay shows no bacterial exRNA-directed cleavage

**Timeline**: 16–20 weeks (Arabidopsis mutant procurement + germination assays; VIGS requires 4–6 weeks for silencing establishment)

**Difficulty**: Very High

**Priority**: High

---

### Experiment 3.3 — Temporal Dynamics: When Does exRNA Activity Occur During Imbibition?

**Experiment**: Determine the critical window during imbibition when exRNA delivery and target suppression must occur to produce the germination phenotype.

**Hypothesis tested**: Is there a specific phase of imbibition (Phase I: passive water uptake; Phase II: plateau/lag; Phase III: radicle emergence) during which exRNA activity is essential, and does this match the predicted delivery mechanism?

**Method**:
- Apply intact preparation at different time windows:
  1. **Pre-soak treatment**: seeds soaked in preparation for 4h, then transferred to water for germination
  2. **Phase I only** (0–6h): preparation present only during initial water uptake
  3. **Phase II only** (6–24h): preparation added after initial uptake, removed before radicle emergence
  4. **Phase III only** (24–48h): preparation added just before radicle emergence
  5. **Continuous treatment**: preparation present throughout germination
  6. **Dry seed coating**: preparation applied to dry seeds, air-dried, then germinated in water
- Measure FGP, MGT, SVI for each window
- Correlate with exRNA detection (small RNA-seq) at each time point to determine when bacterial exRNAs are most abundant in plant tissue

**Expected result if exRNA mechanism is real**: 
- Phase I treatment is sufficient (or most effective) because seed coat permeability is highest during initial water uptake
- Dry seed coating retains some activity (vesicle-mediated delivery during initial imbibition)
- Phase III treatment is ineffective (too late for transcriptional reprogramming)
- exRNA detection peaks at 6–12h post-imbibition

**Expected result if confounder (osmopriming)**: 
- Phase I treatment is most effective (consistent with osmopriming kinetics)
- The critical window matches published osmopriming optimal duration (4–8h for wheat)
- Dry seed coating is less effective (reduced osmotic contact)

**Timeline**: 8–10 weeks

**Difficulty**: Medium

**Priority**: Medium

---

### Experiment 3.4 — Pathway Flux Analysis: Hormone Quantification Across the Causal Chain

**Experiment**: Quantify the complete hormone profile (ABA, GA, ethylene, JA, SA, cytokinin) in treated seeds across imbibition time points to map the hormone flux changes predicted by the causal models.

**Hypothesis tested**: Does the intact preparation produce a hormone profile shift (reduced ABA, increased GA, increased ethylene, reduced JA) consistent with the predicted causal models, and is this shift RNA-dependent?

**Method**:
- LC-MS/MS quantification of: ABA, PA (phaseic acid, ABA catabolite), GA1, GA3, GA4, GA20, JA, JA-Ile, SA, iP (isopentenyladenine, cytokinin), tZ (trans-zeatin)
- Ethylene: GC-FID from headspace gas of germinating seeds
- Time points: 0h, 6h, 12h, 24h, 48h post-imbibition
- Treatments: intact preparation, RNase-treated, PEG-6000 matched, water control
- Tissue: whole seed (wheat) or embryo + endosperm separately (spinach)
- Minimum 3 biological replicates; 50 seeds per replicate for sufficient material

**Expected result if exRNA mechanism is real**: 
- ABA levels lower in intact preparation vs. RNase-treated at 12–24h (RNA-dependent ABA reduction)
- GA4/GA1 levels higher in intact preparation (RNA-dependent GA increase)
- Ethylene production higher in intact preparation (consistent with ethylene receptor downregulation)
- JA/JA-Ile lower in intact preparation (consistent with LOX downregulation)
- Cytokinin levels lower in intact preparation (consistent with AHP downregulation)
- The hormone profile of intact preparation is distinct from PEG-6000 control (rules out osmopriming as sole explanation)

**Expected result if confounder**: 
- Hormone profiles of intact preparation and PEG-6000 control are statistically indistinguishable
- No RNA-dependent differences in ABA, GA, or JA levels
- The hormone changes match published osmopriming effects on wheat hormone profiles

**Timeline**: 12–14 weeks

**Difficulty**: High (LC-MS/MS requires specialized equipment and expertise)

**Priority**: High

---

### Experiment 3.5 — Network Analysis: Co-expression and Pathway Crosstalk

**Experiment**: Use the RNA-seq data from Experiment 2.1 to build a gene regulatory network of the exRNA effect, testing whether the three causal models operate as predicted (hierarchical epigenetic → hormone → defense, or parallel independent pathways).

**Hypothesis tested**: Do the transcriptome changes in treated seeds form a coherent regulatory network consistent with one of the three proposed causal models, or do they suggest an alternative network architecture?

**Method**:
- WGCNA (Weighted Gene Co-expression Network Analysis) on RNA-seq data from Experiment 2.1
- Identify modules of co-expressed genes; test for enrichment of predicted target genes within specific modules
- Construct causal inference network using:
  - Granger causality analysis across time points (which gene changes precede others?)
  - ARACNE (Algorithm for the Reconstruction of Accurate Cellular Networks) for mutual information-based network inference
  - Compare inferred network topology to the three causal model predictions
- Identify hub genes: genes with highest connectivity in the RNA-dependent differential expression network
- Test whether epigenetic targets (MET1, SUVR5) are upstream hubs (consistent with Model 1) or downstream nodes (inconsistent with Model 1)

**Expected result if Causal Model 1 (epigenetic) is correct**: 
- Epigenetic regulators (MET1, SUVR5, HIRA) change earliest (6h) and are upstream hubs
- Hormone biosynthesis genes change later (12–24h) as downstream consequences
- Defense genes change in parallel or later

**Expected result if Causal Model 2 (hormone cascade) is correct**: 
- Ethylene receptor and LOX changes are earliest and most central
- Epigenetic changes are secondary or absent
- Hormone-responsive TFs are the primary hubs

**Timeline**: 8–10 weeks (bioinformatics, using data from Experiment 2.1)

**Difficulty**: High (bioinformatics expertise required)

**Priority**: Medium

---

### Experiment 3.6 — Wheat Homeolog Specificity: Which Subgenome Targets Are Functionally Relevant?

**Experiment**: Determine whether exRNA-mediated suppression affects all three homeologs of each target gene equally, or whether subgenome-specific targeting occurs, with implications for the functional sufficiency of partial suppression.

**Hypothesis tested**: Given the hexaploid wheat genome (AABBDD), does suppression of one or two homeologs of a target gene produce a detectable phenotype, or is simultaneous suppression of all three homeologs required?

**Method**:
- Design homeolog-specific RT-qPCR primers for the A, B, and D homeologs of each top-5 target gene (using SNP-based discrimination at the 3' end of primers)
- Measure homeolog-specific expression in intact preparation vs. RNase-treated seeds
- Predict which homeologs are targeted by each exRNA using RNAhybrid: do predicted exRNAs have complementarity to all three homeologs, or only one/two?
- Compare homeolog expression ratios between treated and control seeds: is there preferential suppression of specific homeologs?
- Use TILLING populations (if available) or CRISPR knockouts of individual homeologs to test whether single-homeolog loss-of-function produces a germination phenotype

**Expected result if exRNA mechanism is real**: 
- exRNAs preferentially suppress homeologs with highest sequence complementarity
- Partial homeolog suppression (1 or 2 of 3) may produce intermediate phenotypes
- CRISPR single-homeolog knockouts show partial germination improvement, with triple knockouts showing the strongest effect

**Expected result if confounder**: 
- No homeolog-specific differential expression between intact and RNase-treated preparations
- All homeologs change equivalently (consistent with non-specific stress response)

**Timeline**: 16–20 weeks (CRISPR wheat transformation is slow; TILLING population screening is faster)

**Difficulty**: Very High

**Priority**: Medium (wheat-specific; lower priority than cross-species validation)

---

## Tier 4: Advanced and Translational Studies

*Rationale: Tier 4 begins only if Tier 3 establishes a mechanistic model with sufficient confidence to justify investment in translational development. These experiments address agricultural applicability, regulatory considerations, safety, and optimization for field deployment.*

---

### Experiment 4.1 — Field Trial: Agronomic Performance Under Real-World Conditions

**Experiment**: Multi-site, multi-year field trial of the exRNA preparation on wheat germination, establishment, and yield under diverse agronomic conditions.

**Hypothesis tested**: Does the laboratory germination improvement translate to improved field establishment, canopy closure, and ultimately grain yield under real-world conditions including variable temperature, moisture, soil microbiome, and agronomic management?

**Method**:
- **Sites**: Minimum 3 geographically distinct locations representing major wheat-growing environments (e.g., semi-arid dryland, irrigated, temperate maritime)
- **Years**: Minimum 2 growing seasons (year-to-year variability is critical for wheat)
- **Varieties**: 3 commercial wheat varieties per site (site × variety interaction)
- **Treatments**: Intact preparation, RNase-treated preparation (osmopriming control), commercial seed treatment (fungicide + insecticide standard), untreated control
- **Application method**: Seed coating (slurry application, air-dried) vs. in-furrow liquid application
- **Metrics**:
  - Emergence rate and uniformity (daily counts for 14 days)
  - Plant stand at 21 days (plants/m²)
  - Tiller number at jointing (GS31)
  - Canopy cover at GS61 (anthesis)
  - Grain yield (t/ha), thousand grain weight, protein content
  - Root architecture at tillering (shovelomics)
- **Statistical design**: Randomized complete block design with 4 replicates per site; mixed-effects model with site and year as random effects
- **Regulatory note**: Field trials of preparations containing bacterial-derived RNA may require regulatory notification depending on jurisdiction; consult national biosafety authority before trial initiation [KNOWN regulatory requirement in EU, US, AU]

**Expected result if exRNA mechanism is real and agronomically relevant**: 
- Improved emergence rate (≥ 10% improvement in plants/m² at 14 days) in intact preparation vs. RNase control
- Improved stand uniformity (reduced CV of emergence timing)
- Yield improvement ≥ 5% in at least 2 of 3 sites in both years
- Effect is larger under stress conditions (drought, cold spring)

**Expected result if effect is laboratory artifact**: 
- No significant emergence improvement in field conditions
- Yield differences not significant or inconsistent across sites and years
- Effect is confounded by soil microbiome, temperature variation, and agronomic management

**Timeline**: 2–3 years (minimum 2 growing seasons)

**Difficulty**: Very High

**Priority**: High (translational endpoint)

**Cost note**: Field trials are the most expensive component of the validation plan; budget accordingly. Consider partnering with national agricultural research institutes or seed companies to share costs.

---

### Experiment 4.2 — Preparation Optimization: Stability, Formulation, and Delivery Enhancement

**Experiment**: Optimize the exRNA preparation for stability during storage and transport, and test alternative delivery vehicles to enhance seed penetration efficiency.

**Hypothesis tested**: Can the preparation be formulated to maintain RNA integrity and biological activity under commercial storage conditions (25°C, 40% RH, 12 months), and can delivery efficiency be improved by encapsulation?

**Method**:

*Part A — Stability testing*:
- Store preparation under: (a) −80°C (reference), (b) −20°C, (c) 4°C, (d) 25°C, (e) 37°C (accelerated aging)
- Sample at: 0, 1, 3, 6, 12 months
- Assess: RNA integrity (Bioanalyzer RIN score), biological activity (germination assay), EPS viscosity, microbial contamination
- Lyophilization: test freeze-dried preparation reconstituted at each time point

*Part B — Encapsulation*:
- Compare delivery vehicles:
  1. **Native OMVs** (baseline)
  2. **Chitosan nanoparticles** (positively charged; enhanced plant cell wall penetration) [KNOWN; Mitter et al. 2017 *Nat Plants*]
  3. **Liposomes** (phospholipid bilayer; mimics OMV structure)
  4. **Clay nanosheets** (BioClay platform) [KNOWN; Mitter et al. 2017]
  5. **Exosome-like plant-derived vesicles** (homologous delivery vehicle) [SPECULATIVE for this application]
- Measure: delivery efficiency (exRNA detection in plant tissue by small RNA-seq), germination improvement, phytotoxicity (root elongation assay at 10× concentration)

*Part C — Application method optimization*:
- Compare: seed soaking (4h, 8h, 16h), seed coating (polymer binder + preparation), pelleting (clay + preparation), in-furrow spray
- Measure: exRNA retention on seed surface (fluorescent label), germination improvement, seedling emergence in soil

**Expected result**: 
- Lyophilized preparation retains ≥ 80% activity after 12 months at −20°C; activity declines at 25°C (RNA degradation)
- Chitosan nanoparticles or BioClay improve delivery efficiency ≥ 2-fold relative to native OMVs
- Seed coating with polymer binder retains activity and is compatible with commercial seed treatment equipment

**Timeline**: 18–24 months (stability testing requires long duration)

**Difficulty**: High

**Priority**: Medium (optimization; depends on positive Tier 1–3 results)

---

### Experiment 4.3 — Safety and Environmental Risk Assessment

**Experiment**: Evaluate the environmental fate of bacterial exRNAs and EPS after field application, and assess potential off-target effects on non-target organisms.

**Hypothesis tested**: Do bacterial exRNAs persist in the soil environment after application, and do they pose risks to non-target organisms (soil microbiome, earthworms, pollinators, aquatic organisms)?

**Method**:

*Part A — Environmental persistence*:
- Soil microcosm study: apply preparation to 3 soil types (sandy loam, clay loam, organic); sample at 0, 1, 7, 14, 28, 56 days; measure RNA persistence by RT-qPCR for specific exRNA sequences
- Aquatic fate: apply preparation to water microcosms; measure RNA persistence and EPS degradation over 28 days
- UV degradation: expose preparation to simulated sunlight (UV-B, 280–315 nm); measure RNA half-life

*Part B — Non-target organism testing*:
- **Soil microbiome**: 16S rRNA amplicon sequencing of soil before and 28 days after application; compare to untreated control
- **Earthworms** (*Eisenia fetida*): OECD 222 reproduction test with preparation at 1× and 10× field concentration
- **Honeybees** (*Apis mellifera*): acute oral and contact toxicity (OECD 213/214) with preparation
- **Aquatic invertebrates** (*Daphnia magna*): acute immobilization test (OECD 202)
- **Algae** (*Raphidocelis subcapitata*): growth inhibition test (OECD 201)
- **Mammalian cell lines**: cytotoxicity (MTT assay) at 1×, 10×, 100× field concentration

*Part C — Off-target plant effects*:
- Test preparation on 5 non-target plant species (weeds, cover crops, neighboring crops): does it improve germination of non-target species? (Potential weed promotion risk)
- Bioinformatic screen: BLAST predicted exRNA sequences against transcriptomes of non-target species; identify potential off-target complementarity

**Expected result**: 
- RNA half-life in soil: < 24h (RNA is rapidly degraded by soil RNases) [INFERRED; consistent with known RNA environmental fate]
- EPS is biodegraded within 28 days (consistent with bacterial polysaccharide degradation rates)
- No significant effects on earthworm reproduction, bee survival, Daphnia, or algae at field concentrations
- Soil microbiome composition not significantly altered at 28 days
- Off-target plant effects are minimal (sequence specificity limits cross-species activity)

**Timeline**: 18–24 months (regulatory testing timelines)

**Difficulty**: High

**Priority**: High (regulatory requirement for commercialization)

---

### Experiment 4.4 — Multi-Crop Transferability: Does the System Work in Other Cereals?

**Experiment**: Test whether the bacterial exRNA preparation improves germination in related cereals (*Hordeum vulgare*, *Zea mays*, *Oryza sativa*) and whether the same target genes are responsible, to assess the breadth of the technology.

**Hypothesis tested**: Is the germination improvement wheat-specific (requiring specific sequence complementarity to wheat target genes) or broadly applicable to other cereals (suggesting either conserved target sequences or non-specific effects)?

**Method**:
- Apply intact preparation, RNase-treated preparation, and scrambled RNA control to:
  1. *Hordeum vulgare* (barley): closely related to wheat; high target gene sequence conservation expected
  2. *Zea mays* (maize): more distant; lower sequence conservation
  3. *Oryza sativa* (rice): most distant among major cereals
  4. *Spinacia oleracea* (spinach): the species for which targets were originally predicted
- Measure FGP, MGT, SVI for each species
- Bioinformatic prediction: for each species, predict which of the 75 target genes have sufficient sequence complementarity to the bacterial exRNAs (≥ 18/21 nt match with ≤ 3 mismatches in seed region)
- Correlate predicted complementarity scores with observed germination improvement across species

**Expected result if exRNA mechanism is real and sequence-specific**: 
- Barley shows improvement comparable to wheat (high sequence conservation)
- Maize and rice show reduced improvement (lower sequence conservation)
- Spinach shows improvement (original target species)
- Germination improvement across species correlates with predicted complementarity scores (r > 0.7)

**Expected result if confounder (non-specific effect)**: 
- All species show comparable improvement
- No correlation between predicted complementarity and germination improvement
- The effect in all species matches the osmopriming benchmark

**Timeline**: 8–10 weeks (parallel germination assays)

**Difficulty**: Medium

**Priority**: Medium

---

### Experiment 4.5 — Regulatory and Intellectual Property Landscape Assessment

**Experiment**: Conduct a comprehensive regulatory pathway analysis and freedom-to-operate (FTO) assessment for the exRNA germination improvement technology.

**Hypothesis tested**: Is the technology commercially viable given existing regulatory frameworks for RNA-based agricultural products and existing patent landscape?

**Method**:

*Regulatory analysis*:
- Map regulatory classification in key markets:
  - **USA**: EPA (FIFRA) and USDA (APHIS) jurisdiction; RNA-based pesticides have established regulatory pathway (EPA's RNAi guidance, 2014; BiologicsTM precedents) [KNOWN]
  - **EU**: Novel food/feed regulation; GMO directive applicability to exRNA preparations; EFSA assessment requirements [KNOWN]
  - **Australia**: APVMA registration; OGTR assessment for RNA-based products [KNOWN]
  - **China, India, Brazil**: Emerging regulatory frameworks for RNA-based agricultural inputs
- Assess whether the preparation is classified as: (a) a biological pesticide, (b) a plant biostimulant, (c) a seed treatment, or (d) a novel entity requiring new regulatory category
- Estimate regulatory timeline and cost to market for each jurisdiction

*Patent landscape*:
- Search: USPTO, EPO, WIPO databases for patents covering: (a) cross-kingdom RNA delivery to plants, (b) bacterial exRNA for plant trait modification, (c) RNA-based seed treatments, (d) specific target genes (ETR1, MET1, SUVR5) as RNA silencing targets in seeds
- Identify freedom-to-operate risks and licensing requirements

*Data package requirements*:
- Identify what Tier 1–4 data are required for regulatory submission in each jurisdiction
- Estimate total cost of regulatory package preparation

**Expected output**: A regulatory roadmap document identifying the fastest path to market, key data gaps for regulatory submission, FTO risks, and estimated commercialization timeline (5–10 years for novel agricultural biologicals is typical) [KNOWN]

**Timeline**: 3–6 months (desk research and legal consultation)

**Difficulty**: High (requires regulatory and IP expertise)

**Priority**: Medium (parallel with Tier 3–4 experimental work)

---

## Resource Requirements

| Tier | Experiments | Est. Duration | Key Equipment | Est. Cost (USD) |
|------|-------------|---------------|---------------|-----------------|
| **Tier 1** | 1.1–1.6 (