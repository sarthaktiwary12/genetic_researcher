# Validation Plan — Soybean (Glycine max)

# Comprehensive 4-Tier Validation Plan: Bacterial exRNA-Mediated Germination Improvement System

## Critical Prefatory Notes

> **Species Reconciliation**: The ranked targets and causal models supplied carry SOV-prefix gene IDs consistent with *Spinacia oleracea* (spinach), not *Glycine max* (soybean) as stated in the crop header. This validation plan is written for **soybean** as the experimental crop, with the following adaptations: (1) all SOV target genes are treated as *predicted functional analogs* requiring identification of confirmed *Glycine max* orthologs before molecular validation; (2) soybean-specific germination biology, seed physiology, and genomic resources are used throughout; (3) where spinach-specific mechanisms are invoked, this is flagged explicitly. The plan is designed to be mechanistically agnostic enough to test the exRNA hypothesis regardless of which species' targets are ultimately validated.

> **Epistemic Framing**: The exRNA germination improvement hypothesis rests on a causal chain with multiple unvalidated links: (1) bacterial exRNAs are produced in sufficient quantity and appropriate sequence composition; (2) exRNAs survive the EPS matrix and seed coat barrier; (3) exRNAs enter seed cells and are loaded into RISC or equivalent silencing machinery; (4) exRNAs silence the predicted target genes; (5) target gene silencing causes germination improvement; (6) this effect exceeds or is separable from EPS osmopriming, polysaccharide elicitor effects, and microbiome-mediated indirect effects. **Each link must be validated independently.** The tier structure below is organized to test these links in order of logical priority.

---

## Tier 1: Essential Controls

*Purpose: Establish whether the germination phenotype is real, reproducible, and attributable to RNA-mediated mechanisms rather than physicochemical or immune-elicitor properties of the bacterial preparation. These experiments must be completed before any molecular mechanistic work is justified.*

---

### Experiment 1.1: Phenotypic Baseline and Dose-Response Characterization

**Experiment**: Comprehensive germination phenotyping of soybean seeds treated with the full bacterial EPS preparation across a concentration gradient, with rigorous environmental controls.

**Hypothesis tested**: The bacterial EPS preparation produces a reproducible, dose-dependent improvement in soybean germination rate, germination percentage, and seedling vigor that is distinguishable from untreated controls. This establishes the phenotype that all subsequent experiments must explain.

**Method**:
- Soybean cultivar: Use a single, well-characterized cultivar with published germination kinetics (e.g., Williams 82, the reference genome cultivar [KNOWN — Schmutz et al., 2010, *Nature*])
- Seed lot: Single lot, tested for baseline germination percentage (must be ≥85% for ISTA standards), moisture content, and accelerated aging index
- Treatment groups (n=8 replicates of 50 seeds each, conducted across 3 independent seed lots):
  - T0: Dry seed control (no treatment)
  - T1: Distilled water soak (matched duration to EPS treatment)
  - T2: EPS preparation at 0.1× working concentration
  - T3: EPS preparation at 0.5× working concentration
  - T4: EPS preparation at 1× working concentration (standard treatment)
  - T5: EPS preparation at 2× working concentration
  - T6: EPS preparation at 5× working concentration
- Germination conditions: 25°C constant temperature, 16h light/8h dark, on moistened germination paper (standard ISTA protocol)
- Measurements at 24h intervals for 7 days:
  - Germination percentage (radicle ≥2mm)
  - Mean germination time (MGT): MGT = Σ(n×t)/Σn where n = seeds germinating on day t
  - Germination uniformity (coefficient of variation of germination time)
  - Radicle length at 48h, 72h, 96h
  - Hypocotyl length at 96h
  - Seedling fresh weight and dry weight at 7 days
  - Seedling vigor index: SVI = germination% × mean seedling length
- Statistical analysis: Two-way ANOVA with Tukey HSD post-hoc; calculate effect sizes (Cohen's d) for each treatment vs. T0; fit dose-response curves (4-parameter logistic model)
- Repeat under two stress conditions: cold stress (15°C) and osmotic stress (PEG 6000 at −0.3 MPa) to assess whether the treatment effect is stress-dependent

**Expected result if exRNA mechanism is real**: A dose-dependent improvement in germination rate and seedling vigor, with the optimal dose corresponding to the RNA concentration range sufficient for RISC loading (predicted: micromolar range of total RNA). The effect should be reproducible across seed lots and enhanced under stress conditions where dormancy mechanisms are more active. [SPECULATIVE — no dose-response data exist for this specific system]

**Expected result if confounder (osmopriming)**: A non-monotonic dose-response (improvement at intermediate concentrations, inhibition at high concentrations due to excessive osmotic stress), with the optimal dose corresponding to water potentials of −0.5 to −1.5 MPa [KNOWN osmopriming window for soybean — Ghassemi-Golezani et al., 2008]. The effect would be indistinguishable from PEG-primed controls at matched water potential.

**Expected result if confounder (elicitor/ISR)**: Improvement would be associated with upregulation of JA/ET marker genes (see Experiment 1.3) and would be abolished by inhibitors of these pathways (e.g., DIECA for ET, coronatine-insensitive1 mutants if available).

**Timeline**: 6–8 weeks (including three independent biological replicates with different seed lots)

**Difficulty**: Low

**Priority**: Critical — no subsequent experiment is interpretable without this baseline

---

### Experiment 1.2: Physicochemical Confounder Separation Panel

**Experiment**: Systematic comparison of the full EPS preparation against a panel of physicochemically matched controls that lack RNA activity, to partition the germination phenotype into RNA-dependent and RNA-independent components.

**Hypothesis tested**: A significant fraction of the germination improvement observed with the full EPS preparation is attributable to the RNA component specifically, not to osmotic, ionic, polysaccharide elicitor, or protein components.

**Method**:
- Prepare the following treatment solutions, all adjusted to identical water potential (measured by vapor pressure osmometry, target: the water potential of the 1× EPS preparation) and identical pH (buffered to pH 6.8 with MES):
  - **C1**: Full EPS preparation (positive control)
  - **C2**: EPS preparation + RNase A (100 μg/mL, 37°C, 30 min pre-treatment) — degrades ssRNA [KNOWN]
  - **C3**: EPS preparation + RNase III (10 U/mL, 37°C, 30 min) — degrades dsRNA and siRNA-like molecules [KNOWN]
  - **C4**: EPS preparation + RNase A + RNase III (combined)
  - **C5**: EPS preparation heated to 95°C for 10 min (denatures RNA and proteins, preserves polysaccharide)
  - **C6**: EPS preparation treated with Proteinase K (100 μg/mL, 37°C, 30 min, then heat-inactivated) — removes protein components
  - **C7**: Purified EPS polysaccharide fraction only (RNA and protein removed by phenol-chloroform extraction and ethanol precipitation of polysaccharides)
  - **C8**: PEG 6000 solution matched to identical water potential as C1 (osmotic control)
  - **C9**: Purified total RNA extracted from the bacterial preparation, resuspended in water at matched RNA concentration
  - **C10**: Boiled total RNA (denatured, fragmented) at matched concentration
  - **C11**: Synthetic scrambled RNA oligonucleotides at matched concentration (sequence-nonspecific RNA control)
  - **C12**: Water control (matched volume)
- Apply all treatments to Williams 82 seeds (n=6 replicates of 50 seeds, single seed lot)
- Measure: germination rate, MGT, SVI, radicle length at 72h (primary endpoints)
- Verify RNase treatment efficacy: run aliquots of C2–C4 on Bioanalyzer or TapeStation to confirm RNA degradation before seed application
- Verify water potential: measure all solutions by osmometry on day of use
- Statistical analysis: One-way ANOVA with Dunnett's test vs. C1 (full preparation) and vs. C12 (water)

**Critical interpretive logic**:
- If C2 (RNase A) = C1: ssRNA is not responsible → exRNA hypothesis weakened
- If C2 < C1 and C3 < C1: RNA component contributes → proceed to Tier 2
- If C4 ≈ C12: RNA is the dominant active component → strong support for exRNA hypothesis
- If C7 ≈ C1: polysaccharide alone is sufficient → elicitor confounder dominant
- If C8 ≈ C1: osmotic effect alone is sufficient → osmopriming confounder dominant
- If C9 > C12 but C10 ≈ C12: intact RNA structure is required → consistent with exRNA mechanism
- If C11 ≈ C9: sequence-nonspecific RNA effect → dsRNA immune elicitation confounder [KNOWN — dsRNA triggers plant innate immunity; Niehl et al., 2016, *Nature Plants*]

**Expected result if exRNA mechanism is real**: C4 (combined RNase) should significantly reduce the germination improvement relative to C1, while C8 (PEG osmotic control) should show less improvement than C1. C9 (purified RNA) should partially recapitulate the C1 effect, and C11 (scrambled RNA) should show less effect than C9. [SPECULATIVE — this prediction assumes the exRNA sequences are specifically required]

**Expected result if osmopriming dominates**: C8 ≈ C1 ≈ C2 ≈ C3 ≈ C4; RNase treatment has no effect on the phenotype.

**Timeline**: 8–10 weeks (including preparation of all control solutions, verification of treatment efficacy, and three independent germination trials)

**Difficulty**: Medium (requires osmometry, RNase treatments, RNA quality verification)

**Priority**: Critical — this is the primary confounder separation experiment

---

### Experiment 1.3: Molecular Marker Panel for Confounder Discrimination

**Experiment**: Transcriptomic and hormonal profiling of seeds treated with the full EPS preparation versus the confounder controls from Experiment 1.2, to determine whether the molecular signature of treatment is consistent with exRNA-mediated gene silencing, osmopriming, or immune elicitation.

**Hypothesis tested**: The molecular response to the full EPS preparation includes specific downregulation of predicted target gene orthologs in soybean, and this pattern is distinguishable from the transcriptomic signatures of osmopriming and immune elicitation.

**Method**:

*Part A: Ortholog identification (prerequisite, 2–3 weeks)*
- Identify *Glycine max* orthologs of the top 20 SOV-prefix target genes using:
  - SoyBase (soybase.org) BLAST against Wm82.a4.v1 genome assembly [KNOWN resource]
  - OrthoFinder v2 [KNOWN tool — Emms & Kelly, 2019, *Genome Biology*] with spinach and soybean proteomes
  - Synteny analysis using MCScanX [KNOWN tool]
  - Note: soybean is a paleopolyploid with ~75% of genes present in duplicate [KNOWN — Schmutz et al., 2010]; both homeologs must be identified and tracked
- Compile a target gene list with Glyma gene IDs for all confirmed orthologs
- Include positive control marker genes for each confounder:
  - **Osmopriming markers**: *GmLEA* (late embryogenesis abundant proteins, *Glyma.08G108200*), *GmRAB18* (ABA-responsive), *GmDREB* transcription factors [KNOWN markers of priming response]
  - **Immune elicitation/ISR markers**: *GmPR1* (*Glyma.12G236800*), *GmPR2*, *GmPDF1.2*, *GmWRKY* transcription factors, *GmLOX* (JA biosynthesis) [KNOWN ISR markers in soybean — Ding et al., 2018]
  - **GA signaling markers**: *GmGID1* (GA receptor), *GmSLR1/DELLA* genes, *GmGA20ox* [KNOWN]
  - **ABA signaling markers**: *GmABI3*, *GmABI5*, *GmPYL* receptors [KNOWN]
  - **Germination progression markers**: *GmαAMY* (α-amylase), *GmEXPA* (expansin), *GmXTH* [KNOWN]

*Part B: Time-course sampling*
- Treat seeds with C1 (full EPS), C4 (RNase-treated EPS), C8 (PEG osmotic control), C11 (scrambled RNA), and C12 (water)
- Harvest embryonic axes (dissected under RNase-free conditions) at:
  - 0h (dry seed)
  - 6h post-imbibition (early Phase I)
  - 12h post-imbibition (late Phase I / early Phase II)
  - 24h post-imbibition (Phase II, pre-germination)
  - 48h post-imbibition (radicle emergence in fast-germinating seeds)
- n=3 biological replicates per timepoint per treatment (pool 10 embryonic axes per replicate)
- Extract RNA using CTAB method optimized for soybean seed tissue [KNOWN — high lipid and polysaccharide content requires modified extraction]

*Part C: Expression analysis*
- **Targeted qRT-PCR panel** (primary analysis): Design primers for all identified Glyma orthologs of SOV targets, all confounder markers listed above, and 3 reference genes (*GmUBC2*, *GmACTIN11*, *GmEF1α* — validated reference genes for soybean germination [KNOWN — Jian et al., 2008, *Plant Cell Reports*])
- **RNA-seq** (secondary, discovery analysis): Conduct on 0h, 12h, and 48h timepoints for C1, C4, C8, and C12 (n=3 biological replicates; 150bp paired-end, minimum 30M reads per sample)
  - Align to Wm82.a4.v1 using STAR [KNOWN]
  - Differential expression: DESeq2 [KNOWN — Love et al., 2014, *Genome Biology*]
  - Gene ontology enrichment: clusterProfiler [KNOWN]
  - Compare differentially expressed gene sets between C1 vs. C12 and C8 vs. C12 to identify C1-specific signatures

*Part D: Hormone quantification*
- Quantify ABA, GA₃, GA₄, JA, JA-Ile, ACC (ethylene precursor), and SA in embryonic axes at 12h and 24h timepoints using LC-MS/MS [KNOWN method — Müller & Munné-Bosch, 2011]
- n=3 biological replicates (pool 20 embryonic axes per replicate)

**Expected result if exRNA mechanism is real**:
- Predicted target gene orthologs are specifically downregulated in C1 vs. C12 at 12–24h, but this downregulation is attenuated or absent in C4 (RNase-treated) [SPECULATIVE — requires the exRNA hypothesis to be correct]
- The C1 transcriptomic signature shows enrichment for GO terms related to dormancy dissolution (GA signaling, cell wall remodeling, seed storage mobilization) beyond what is seen in C8
- ABA levels decline faster in C1 than in C8 or C12; GA levels rise faster in C1
- ISR marker genes are not specifically elevated in C1 relative to C11 (scrambled RNA control)

**Expected result if osmopriming dominates**: C1 and C8 transcriptomic signatures are highly correlated (r > 0.85); osmopriming marker genes (LEA, RAB18) are elevated in both; target gene downregulation is not specific to C1.

**Expected result if immune elicitation dominates**: C1 and C11 (scrambled RNA) show similar upregulation of PR genes, WRKY transcription factors, and JA/SA pathway genes; the C1 vs. C12 differentially expressed gene set is enriched for defense GO terms.

**Timeline**: 12–16 weeks (ortholog identification: 3 weeks; seed treatment and sampling: 2 weeks; RNA extraction and qRT-PCR: 3 weeks; RNA-seq library preparation and sequencing: 4 weeks; bioinformatics analysis: 4 weeks; parallel with wet lab work)

**Difficulty**: High (requires RNA-seq infrastructure, LC-MS/MS for hormones, soybean embryonic axis dissection at scale)

**Priority**: Critical — this experiment determines whether any molecular signature supports the exRNA hypothesis before investing in target-specific validation

---

### Experiment 1.4: exRNA Characterization and Uptake Verification

**Experiment**: Characterize the small RNA content of the bacterial EPS preparation and determine whether bacterial-sequence small RNAs are detectable inside soybean seed cells following treatment.

**Hypothesis tested**: The EPS preparation contains bacterial small RNAs of appropriate size (18–25 nt) and sequence to mediate cross-kingdom RNAi, and these RNAs are taken up by soybean seed cells and are detectable intracellularly following treatment.

**Method**:

*Part A: Characterization of exRNA in the preparation*
- Extract total RNA from the EPS preparation using TRIzol LS (optimized for liquid samples)
- Size-select small RNAs (15–40 nt) using PAGE or magnetic bead-based size selection
- Prepare small RNA-seq library (NEBNext Small RNA Library Prep Kit or equivalent)
- Sequence at high depth (minimum 50M reads) on Illumina platform
- Bioinformatics pipeline:
  - Adapter trimming: Cutadapt [KNOWN]
  - Map to bacterial genome (identify the M-9 strain; sequence its genome if not available using Nanopore or PacBio long-read sequencing)
  - Identify bacterial sRNA species: size distribution, sequence composition, predicted secondary structures
  - Predict plant targets: use psRNATarget [KNOWN — Dai et al., 2018, *Nucleic Acids Research*] with *Glycine max* transcriptome as target database; apply stringent parameters (maximum expectation score ≤3.0, minimum complementarity score ≥18)
  - Cross-reference predicted targets with the SOV-prefix target list (via orthology) to assess overlap
- Characterize RNA stability in EPS matrix: incubate RNA in EPS solution at 25°C for 0, 1, 2, 4, 8, 24h; measure integrity by Bioanalyzer; determine half-life

*Part B: Uptake verification*
- **Fluorescent labeling approach**: Label purified bacterial exRNA preparation with Cy3 or Alexa Fluor 647 using Label IT Nucleic Acid Labeling Kit (Mirus Bio) [KNOWN method used in cross-kingdom RNA uptake studies — Cai et al., 2018]
  - Apply labeled RNA to imbibing soybean seeds for 6h and 12h
  - Wash seeds extensively (5× PBS washes) to remove surface-bound RNA
  - Dissect embryonic axes under RNase-free conditions
  - Fix in 4% paraformaldehyde, section at 10 μm on cryostat
  - Image by confocal microscopy (Zeiss LSM 880 or equivalent); co-stain with DAPI (nuclei) and FM4-64 (membranes)
  - Quantify intracellular fluorescence vs. cell wall/apoplast fluorescence
  - Include controls: labeled scrambled RNA, labeled RNA + RNase treatment before application, unlabeled RNA + anti-RNA antibody staining
- **Molecular detection approach**: Apply unlabeled bacterial exRNA preparation; after 12h, wash seeds, dissect embryonic axes, extract total small RNA
  - Prepare small RNA-seq library from treated and untreated seed tissue
  - Map reads to bacterial genome: any reads mapping to bacterial sequences in treated (but not untreated) seeds indicate uptake
  - Quantify: reads per million mapping to bacterial sequences
  - This approach has been used to detect cross-kingdom sRNA transfer in plant-fungal systems [KNOWN — Weiberg et al., 2013, *Science*; Wang et al., 2017, *Nature Plants*]
- **RISC loading verification** (if uptake is confirmed): Immunoprecipitate AGO1 protein from treated soybean embryonic axes using anti-AGO1 antibody (validated for soybean: *GmAGO1a/b*, *Glyma.02G003200/Glyma.10G003100*) [INFERRED — antibody cross-reactivity with soybean AGO1 must be verified]; sequence co-immunoprecipitated small RNAs; determine whether bacterial-sequence sRNAs are enriched in AGO1 immunoprecipitate relative to input

**Expected result if exRNA mechanism is real**:
- Small RNA-seq of the EPS preparation reveals 18–25 nt bacterial sRNAs with predicted complementarity to soybean target gene orthologs (≥18/21 nt complementarity in the seed region)
- Fluorescent RNA is detectable intracellularly (not just in cell walls or apoplast) in embryonic axis cells after 12h treatment
- Bacterial-sequence reads are detectable in small RNA-seq data from treated seed tissue (predicted: low abundance, perhaps 0.01–1% of total small RNA reads) [SPECULATIVE — no quantitative benchmark exists for this system]
- Bacterial sRNAs are enriched in AGO1 immunoprecipitate [SPECULATIVE]

**Expected result if exRNA hypothesis fails at uptake step**: Fluorescent RNA is confined to seed coat and outer cell layers; no bacterial-sequence reads are detected in embryonic axis small RNA-seq; AGO1 IP contains no bacterial sequences.

**Timeline**: 16–20 weeks (bacterial genome sequencing: 4 weeks; small RNA-seq of preparation: 4 weeks; uptake experiments: 6 weeks; AGO1 IP: 4 weeks; bioinformatics: parallel)

**Difficulty**: High (requires small RNA-seq, confocal microscopy, AGO1 immunoprecipitation, bacterial genome sequencing)

**Priority**: Critical — if uptake cannot be demonstrated, the exRNA mechanism is not operative regardless of phenotypic effects

---

## Tier 2: Target Validation

*Purpose: Validate that specific predicted target genes in soybean are downregulated by the exRNA treatment in an RNA-sequence-dependent manner, and that their downregulation contributes causally to germination improvement. Focus on the top-ranked targets from the causal models, translated to confirmed Glyma orthologs.*

**Prerequisite**: Tier 1 experiments must demonstrate: (1) a phenotype that is at least partially RNA-dependent (Experiment 1.2); (2) a molecular signature consistent with target gene downregulation (Experiment 1.3); and (3) detectable exRNA uptake (Experiment 1.4). If any of these prerequisites fail, Tier 2 experiments should be redesigned or suspended pending model revision.

**Target prioritization for soybean**: Based on the ranked target analysis, the following functional categories are prioritized for ortholog identification and validation in soybean, in order:

| Priority | Functional Category | Predicted SOV Target | Soybean Ortholog Strategy |
|----------|--------------------|--------------------|--------------------------|
| 1 | Ethylene receptor | SOV3g000150.1 | *GmETR1/2* (*Glyma.03G036700*, *Glyma.19G036500*) [KNOWN] |
| 2 | DNA methyltransferase | SOV1g033340.1 | *GmMET1* (*Glyma.10G294200*, *Glyma.20G166900*) [INFERRED] |
| 3 | HIRA histone chaperone | SOV6g036290.1 | *GmHIRA* (ortholog TBD by OrthoFinder) [INFERRED] |
| 4 | AHP cytokinin relay | SOV4g032870.1 | *GmAHP* family (multiple paralogs) [INFERRED] |
| 5 | EDR2 paralogs | SOV3g043450.1, SOV6g048760.1 | *GmEDR2* orthologs (TBD) [INFERRED] |
| 6 | Cation-Cl cotransporters | SOV1g021960.1, SOV2g025380.1 | *GmCCC* family [INFERRED] |
| 7 | MYB transcription factor | SOV1g020340.1 | *GmMYB* family (>150 members in soybean) [KNOWN — Du et al., 2012] |
| 8 | TPS enzyme | SOV2g009230.1 | *GmTPS* (*Glyma.06G209300* and paralogs) [INFERRED] |
| 9 | PP2A regulatory subunit | SOV3g033920.1 | *GmPP2A-B* regulatory subunits [INFERRED] |
| 10 | LOX enzyme | SOV3g035520.1 | *GmLOX* family (*Glyma.13G174400* and others) [KNOWN] |

---

### Experiment 2.1: Soybean Ortholog Identification and Sequence-Based Target Prediction

**Experiment**: Systematic identification of *Glycine max* orthologs for all top-ranked SOV targets, followed by computational prediction of whether the bacterial exRNAs identified in Experiment 1.4 have sequence complementarity to soybean target mRNAs.

**Hypothesis tested**: The bacterial exRNAs present in the EPS preparation have predicted complementarity to soybean orthologs of the ranked spinach targets, providing a mechanistic basis for cross-kingdom silencing in soybean specifically.

**Method**:
- Input: bacterial small RNA sequences identified in Experiment 1.4 (Part A)
- Input: *Glycine max* Wm82.a4.v1 CDS and 3'UTR sequences for all Glyma orthologs of SOV targets
- Run psRNATarget [KNOWN] with parameters: maximum expectation ≤3.0, HSP size 19, maximum mismatches in seed region (positions 2–13) ≤2, no mismatches at positions 10–11 (cleavage site)
- Run TargetFinder [KNOWN — Fahlgren & Carrington, 2010] as orthogonal prediction tool
- For each predicted exRNA-target pair, compute:
  - Minimum free energy of duplex (RNAfold, Vienna RNA package [KNOWN])
  - Accessibility of target site (RNAplfold [KNOWN])
  - Conservation of target site across soybean homeologs
- Rank predicted target pairs by combined score
- Cross-reference with Experiment 1.3 RNA-seq data: are computationally predicted targets among the differentially expressed genes in C1 vs. C12?
- Output: a refined list of high-confidence exRNA-target pairs in soybean for experimental validation

**Expected result if exRNA mechanism is real**: At least a subset of bacterial exRNAs show predicted complementarity (expectation score ≤3.0) to soybean orthologs of the top-ranked SOV targets, and these targets are among the downregulated genes in the C1 RNA-seq dataset. [SPECULATIVE — this depends entirely on the actual sequences of bacterial exRNAs, which are unknown]

**Expected result if exRNA hypothesis fails at sequence level**: Bacterial exRNAs show no significant complementarity to soybean target mRNAs (all expectation scores >5.0); any germination improvement must be explained by non-sequence-specific mechanisms.

**Timeline**: 4–6 weeks (computational, can run in parallel with Tier 1 wet lab experiments)

**Difficulty**: Medium (requires bioinformatics expertise, access to bacterial genome sequence from Experiment 1.4)

**Priority**: Critical for Tier 2 — determines which targets to pursue experimentally

---

### Experiment 2.2: VIGS-Based Functional Validation of Top 5 Targets

**Experiment**: Use Virus-Induced Gene Silencing (VIGS) to individually silence the top 5 soybean target gene orthologs and determine whether silencing of each gene phenocopies the germination improvement observed with the full EPS treatment.

**Hypothesis tested**: Downregulation of individual target genes (ethylene receptor, DNA methyltransferase, HIRA, AHP, EDR2) is sufficient to improve soybean germination rate and seedling vigor, consistent with their proposed roles as dormancy-maintenance factors.

**Method**:
- VIGS system: Bean Pod Mottle Virus (BPMV)-based VIGS, which is well-established in soybean [KNOWN — Zhang & Ghabrial, 2006, *Virology*; Burch-Smith et al., 2006, *Plant Physiology*]
  - Note: BPMV-VIGS is typically applied to young seedlings, not seeds; for seed-specific silencing, an alternative approach using Agrobacterium-mediated floral dip or seed imbibition with dsRNA may be required [INFERRED — see dsRNA approach below]
- **Alternative approach — dsRNA-mediated silencing** (more directly relevant to the exRNA hypothesis):
  - Design gene-specific dsRNA (300–500 bp) targeting each of the 5 priority genes
  - Synthesize dsRNA in vitro using T7 RNA polymerase and gene-specific PCR templates [KNOWN method]
  - Apply dsRNA to dry soybean seeds by imbibition (same protocol as EPS treatment) at concentrations of 1, 10, 100 ng/μL
  - Include controls: scrambled dsRNA at matched concentration, water, full EPS preparation
  - Measure germination phenotype (same endpoints as Experiment 1.1)
  - Verify gene silencing by qRT-PCR at 24h and 48h post-imbibition
  - This approach directly tests whether sequence-specific RNA silencing of individual targets is sufficient to improve germination [INFERRED — dsRNA imbibition has been demonstrated to silence plant genes in several species; Dalakouras et al., 2020, *Plant Physiology*]
- For each target gene, design two independent dsRNA constructs targeting non-overlapping regions (to control for off-target effects)
- If soybean has two homeologs for a given target (common given paleopolyploidy), design dsRNA to silence both simultaneously (target conserved region) or separately (to determine which homeolog is functionally relevant)
- Measure:
  - Target gene mRNA levels (qRT-PCR, both homeologs if applicable)
  - Germination rate, MGT, SVI (primary phenotypic endpoints)
  - Secondary: ABA and GA levels at 24h (subset of samples)

**Expected result if exRNA mechanism is real**: dsRNA targeting of individual high-priority genes (especially ethylene receptor, DNA methyltransferase) produces a measurable improvement in germination rate (predicted: 5–20% improvement in MGT) that is gene-specific (scrambled dsRNA has no effect) and dose-dependent. Silencing of multiple targets simultaneously (combining dsRNAs) produces additive or synergistic effects. [SPECULATIVE — magnitude is unknown; additive effects would support the multi-target model from the causal analysis]

**Expected result if individual targets are not causal**: dsRNA silencing of individual targets produces no germination phenotype, suggesting either (a) the targets are not functionally relevant in soybean, (b) redundancy prevents single-gene effects, or (c) the exRNA mechanism operates through a different set of targets. This would support a model where the phenotype requires simultaneous silencing of multiple targets (consistent with the "dormancy dissolution" multi-target model).

**Timeline**: 20–24 weeks (dsRNA synthesis: 4 weeks; germination trials: 8 weeks; qRT-PCR validation: 4 weeks; repeat with independent constructs: 8 weeks)

**Difficulty**: High (dsRNA synthesis at scale, multiple gene targets, homeolog complexity in soybean)

**Priority**: High — provides the most direct test of whether individual target silencing is sufficient

---

### Experiment 2.3: Synthetic exRNA Mimics — Sequence Specificity Test

**Experiment**: Synthesize short RNA oligonucleotides (21–23 nt) matching the sequences of the bacterial exRNAs predicted to target soybean genes (from Experiment 2.1), and test whether these synthetic mimics recapitulate the germination improvement phenotype in a sequence-dependent manner.

**Hypothesis tested**: The germination-promoting activity of the bacterial exRNA preparation can be recapitulated by synthetic RNA oligonucleotides matching specific bacterial exRNA sequences, and this activity is abolished by scrambled sequences of identical nucleotide composition.

**Method**:
- Select top 10 predicted exRNA-target pairs from Experiment 2.1 (highest complementarity scores, targets in the top-priority list)
- Synthesize the following RNA oligonucleotides (chemically synthesized, HPLC-purified):
  - **Authentic sequence**: 21 nt matching the bacterial exRNA sequence
  - **Scrambled control**: same nucleotide composition, randomized sequence (verified to have no predicted plant targets with expectation score <5.0)
  - **Seed-region mismatch**: 2 mismatches at positions 10–11 (disrupts cleavage but not binding) [KNOWN — positions 10–11 are critical for RISC-mediated cleavage; Baumberger & Baulcombe, 2005, *PNAS*]
  - **2'-O-methyl modified**: chemically stabilized version to test whether stability affects activity
- Apply each oligonucleotide to soybean seeds at 3 concentrations (10, 100, 1000 nM) in water
- Measure germination phenotype (n=6 replicates of 50 seeds per treatment)
- Measure target gene mRNA levels by qRT-PCR at 24h
- Pool the top 5 individual oligonucleotides and test the combination vs. individual oligos (tests multi-target model)
- Include full EPS preparation as positive control

**Critical controls**:
- Verify that synthetic RNA oligonucleotides are not themselves acting as immune elicitors: measure PR1, PR2, WRKY marker gene expression in treated seeds; compare to scrambled RNA control
- Verify that the water potential of oligonucleotide solutions is not significantly different from water (at nM concentrations, osmotic contribution is negligible)

**Expected result if exRNA mechanism is real**: Authentic-sequence oligonucleotides targeting the highest-priority genes produce measurable germination improvement at ≥100 nM; scrambled controls do not; seed-region mismatch controls show reduced activity; the combination of 5 oligonucleotides shows greater improvement than any individual oligonucleotide. [SPECULATIVE — this is the strongest possible positive result; partial results (e.g., only 2/10 sequences active) would still support the hypothesis]

**Expected result if sequence specificity is absent**: Authentic and scrambled oligonucleotides produce identical germination phenotypes; any improvement is attributable to non-specific RNA effects (immune elicitation, dsRNA sensing).

**Timeline**: 16–20 weeks (oligonucleotide synthesis: 4 weeks; germination trials: 8 weeks; qRT-PCR: 4 weeks)

**Difficulty**: Medium-High (requires chemical synthesis of multiple RNA oligonucleotides, careful handling of RNA)

**Priority**: High — provides the cleanest test of sequence specificity

---

### Experiment 2.4: AGO1 Immunoprecipitation and Target Cleavage Verification

**Experiment**: Verify that the exRNA-mediated silencing of target genes occurs through the canonical RISC/AGO1 pathway by immunoprecipitating AGO1 from treated soybean seeds and confirming: (1) bacterial exRNA sequences are loaded into AGO1, and (2) target mRNAs show cleavage products at the predicted AGO1 cleavage site.

**Hypothesis tested**: Bacterial exRNAs are loaded into soybean AGO1 protein and direct sequence-specific cleavage of target mRNAs at the predicted complementarity site, confirming canonical cross-kingdom RNAi.

**Method**:

*Part A: AGO1 immunoprecipitation*
- Identify and validate anti-AGO1 antibody cross-reactivity with soybean GmAGO1a (*Glyma.02G003200*) and GmAGO1b (*Glyma.10G003100*) by Western blot using recombinant protein or overexpression lines [INFERRED — commercial anti-Arabidopsis AGO1 antibodies may cross-react; must be verified]
- Treat soybean seeds with full EPS preparation or water for 24h; dissect embryonic axes (pool 50 axes per replicate, n=3)
- Lyse in native lysis buffer; immunoprecipitate with anti-AGO1 antibody + Protein A/G beads
- Verify IP efficiency by Western blot
- Extract co-immunoprecipitated RNA; prepare small RNA-seq library
- Map reads to bacterial genome: enrichment of bacterial sRNA sequences in AGO1 IP vs. input indicates RISC loading
- Map reads to soybean genome: identify endogenous miRNAs and siRNAs as positive controls for AGO1 loading

*Part B: 5' RACE for target cleavage verification*
- For each confirmed target gene, perform modified 5' RACE (5' Rapid Amplification of cDNA Ends) to detect the 3' cleavage fragment of the target mRNA [KNOWN method — Llave et al., 2002, *Science*; Allen et al., 2005, *Nature Genetics*]
- The 3' cleavage fragment will have a 5' monophosphate end at the position complementary to nucleotide 10–11 of the guide sRNA
- Alternatively, use degradome sequencing (PARE — Parallel Analysis of RNA Ends) [KNOWN — German et al., 2008, *Nature Biotechnology*] to genome-wide map all mRNA cleavage events
  - Compare degradome profiles of EPS-treated vs. water-treated seeds
  - Identify cleavage peaks at predicted exRNA target sites
  - This approach simultaneously validates all predicted targets in a single experiment

**Expected result if exRNA mechanism is real**: Bacterial sRNA sequences are enriched in AGO1 IP relative to input (enrichment ratio >5-fold); 5' RACE or PARE identifies cleavage products at the predicted target sites in EPS-treated but not water-treated seeds. [SPECULATIVE — this is the gold-standard result for cross-kingdom RNAi verification, analogous to what was demonstrated in plant-fungal systems by Weiberg et al., 2013]

**Expected result if AGO1 loading fails**: No bacterial sequences in AGO1 IP; no target cleavage products detected; mechanism must be AGO1-independent (e.g., translational repression, RNA-directed DNA methylation, or non-RNAi mechanisms).

**Timeline**: 20–24 weeks (antibody validation: 4 weeks; IP optimization: 4 weeks; small RNA-seq and PARE: 6 weeks; bioinformatics: 6 weeks)

**Difficulty**: Very High (AGO1 IP from seed tissue is technically demanding; PARE requires high-quality RNA and specialized library preparation)

**Priority**: High — provides mechanistic proof of canonical cross-kingdom RNAi; however, can be deferred if Tier 1 results are ambiguous

---

### Experiment 2.5: Loss-of-Function Genetic Validation Using Soybean Mutants

**Experiment**: Test whether soybean mutants with loss-of-function alleles in the top-priority target genes show constitutively improved germination, and whether these mutants show reduced or absent response to the EPS treatment (epistasis test).

**Hypothesis tested**: Loss-of-function mutations in the target genes phenocopy the EPS treatment effect, and EPS treatment of these mutants shows no additional germination improvement (epistasis), confirming that the target genes are in the causal pathway.

**Method**:
- Source soybean mutant lines from:
  - SoyTFDB and SoyBase mutant databases
  - USDA Soybean Germplasm Collection (GRIN database)
  - *Glycine max* TILLING population (EMS-mutagenized Williams 82; available from USDA-ARS [KNOWN — Cooper et al., 2008, *BMC Genomics*])
  - Published CRISPR-edited soybean lines (check literature for existing *GmETR1*, *GmMET1* knockouts)
- If mutant lines are unavailable, generate CRISPR-Cas9 knockouts:
  - Design guide RNAs targeting conserved exons of priority genes using CRISPR-P 2.0 [KNOWN]
  - Transform Williams 82 via Agrobacterium-mediated cotyledonary node transformation [KNOWN — Paz et al., 2006, *Plant Cell Reports*]
  - Screen T0 plants by PCR/Sanger sequencing; advance homozygous T2 lines
  - Note: soybean transformation is slow (6–9 months per cycle) and has low efficiency (~1–5%); this is a major timeline constraint [KNOWN]
- For each mutant line:
  - Confirm target gene loss of function by RT-PCR and Western blot
  - Measure baseline germination phenotype (mutant vs. wild-type Williams 82) under standard and stress conditions
  - Apply EPS treatment to mutant and wild-type seeds; compare germination phenotype
  - Epistasis interpretation:
    - If mutant germination = WT + EPS treatment AND mutant + EPS = mutant alone: target gene is in the causal pathway (EPS acts through this gene)
    - If mutant germination > WT + EPS treatment: target gene is not the only relevant target (consistent with multi-target model)
    - If mutant germination = WT AND mutant + EPS > mutant alone: target gene is not relevant to the EPS effect

**Expected result if exRNA mechanism is real**: Loss-of-function mutants in ethylene receptor (*GmETR1/2*) and DNA methyltransferase (*GmMET1*) show improved germination rate relative to wild-type; EPS treatment of these mutants shows reduced additional improvement (partial epistasis), consistent with these genes being among multiple targets of the exRNA preparation. [INFERRED — based on known biology of ETR1 and MET1 in Arabidopsis germination; Bleecker et al., 1988, *Science*; Zheng et al., 2012, *Plant Cell*]

**Expected result if targets are not causal**: Mutants show no germination phenotype; EPS treatment of mutants shows the same improvement as wild-type; the target genes are not rate-limiting for germination in soybean.

**Timeline**: 24–36 months if CRISPR generation is required; 12–18 months if TILLING mutants are available

**Difficulty**: Very High (soybean transformation is slow and technically demanding)

**Priority**: High (long-term) — provides definitive genetic proof; should be initiated early given the long timeline, but results will not be available until Tier 3/4 timeframe

---

## Tier 3: Mechanistic Studies

*Purpose: Elucidate the pathway-level mechanisms by which exRNA-mediated target gene silencing leads to germination improvement, test the causal models (epigenetic master switch, hormonal reprogramming, multi-target dormancy dissolution), and identify potential negative consequences of the treatment (off-target effects, seedling fitness costs).*

**Prerequisite**: Tier 2 experiments must have confirmed: (1) at least partial sequence-specificity of the germination effect; (2) downregulation of at least 3 predicted target genes in an RNA-dependent manner; (3) detectable exRNA uptake and RISC loading (or a credible alternative mechanism).

---

### Experiment 3.1: Epigenome Profiling — Testing the Epigenetic Master Switch Model

**Experiment**: Determine whether EPS treatment causes genome-wide changes in DNA methylation and histone modification patterns in soybean embryonic axes, consistent with the epigenetic master switch causal model.

**Hypothesis tested**: Downregulation of GmMET1 (DNA methyltransferase) and GmHIRA (histone chaperone) by exRNAs leads to measurable changes in the soybean seed epigenome that precede and predict transcriptional de-repression of germination-promoting genes.

**Method**:
- Treat Williams 82 seeds with full EPS preparation (C1), RNase-treated EPS (C4), and water (C12)
- Harvest embryonic axes at 12h and 24h post-imbibition (n=3 biological replicates, pool 30 axes per replicate)
- **Whole-genome bisulfite sequencing (WGBS)** for DNA methylation:
  - Extract genomic DNA; bisulfite convert using EZ DNA Methylation-Gold Kit (Zymo Research)
  - Prepare WGBS libraries; sequence at 30× coverage
  - Align to Wm82.a4.v1 using Bismark [KNOWN]
  - Analyze CG, CHG, CHH methylation contexts separately
  - Identify differentially methylated regions (DMRs) between C1 and C12 at 12h and 24h
  - Annotate DMRs: promoters, gene bodies, TEs, intergenic regions
  - Test whether DMRs are enriched at promoters of germination-promoting genes (GA biosynthesis, cell wall hydrolases, expansins)
- **ChIP-seq for histone modifications**:
  - Chromatin immunoprecipitation from embryonic axis tissue using antibodies against H3K9me2 (repressive), H3K27me3 (Polycomb repressive), H3K4me3 (active), H3K36me3 (transcribed)
  - Validate antibody specificity by Western blot on soybean nuclear extracts
  - Sequence ChIP and input libraries at 30M reads per sample
  - Identify differentially enriched regions between C1 and C12
  - Integrate with WGBS data: do regions losing DNA methylation also lose H3K9me2?
  - Integrate with RNA-seq data from Experiment 1.3: do genes gaining H3K4me3 show increased expression?
- **ATAC-seq for chromatin accessibility**:
  - Apply ATAC-seq (Assay for Transposase-Accessible Chromatin) to embryonic axis nuclei [KNOWN — Buenrostro et al., 2013, *Nature Methods*]
  - Identify regions of increased chromatin accessibility in C1 vs. C12 at 12h
  - Test whether accessibility changes precede transcriptional changes (compare 12h ATAC-seq with 24h RNA-seq)

**Expected result if epigenetic master switch model is correct**: EPS treatment causes measurable loss of DNA methylation at CG and CHG contexts at promoters of GA-biosynthesis and cell wall remodeling genes by 24h; concurrent loss of H3K9me2 and gain of H3K4me3 at these loci; increased chromatin accessibility at germination-promoting gene promoters; these changes are attenuated in C4 (RNase-treated) samples. [SPECULATIVE — the timescale of epigenetic reprogramming in 24h is uncertain; passive demethylation requires cell division, which may not occur in this timeframe]

**Critical caveat**: [INFERRED] Passive DNA demethylation (loss of maintenance methylation) requires DNA replication and cell division. In the 24–48h window of early imbibition, limited cell division occurs in the embryonic axis. Therefore, if DNA methylation changes are observed, they may reflect active demethylation (by ROS1/DML family demethylases) rather than passive loss due to MET1 silencing. This distinction has mechanistic implications and should be tested by measuring ROS1/DML expression.

**Timeline**: 20–24 weeks (tissue collection: 2 weeks; WGBS, ChIP-seq, ATAC-seq library preparation: 6 weeks; sequencing: 4 weeks; bioinformatics: 8 weeks)

**Difficulty**: Very High (ChIP-seq from seed tissue is technically demanding due to high starch/lipid content; requires large amounts of starting material)

**Priority**: High — directly tests the primary causal model

---

### Experiment 3.2: Hormone Flux Analysis — Testing the Hormonal Reprogramming Model

**Experiment**: Conduct a comprehensive time-resolved analysis of hormone biosynthesis, catabolism, and signaling in EPS-treated vs. control soybean seeds, to determine whether the hormonal reprogramming model (ABA decline + GA rise + ethylene activation) is the primary driver of germination improvement.

**Hypothesis tested**: EPS treatment accelerates the ABA-to-GA hormonal transition that normally occurs during germination, and this acceleration is dependent on the RNA component of the EPS preparation (not just osmotic priming).

**Method**:
- Time course: 0, 6, 12, 24, 36, 48h post-imbibition
- Treatments: C1 (full EPS), C4 (RNase-treated EPS), C8 (PEG osmotic control), C12 (water)
- Tissue: embryonic axes (dissected) and cotyledons (separate analysis)
- n=4 biological replicates per timepoint per treatment (pool 15 embryonic axes per replicate)

*Hormone quantification by LC-MS/MS*:
- ABA and ABA catabolites: ABA, phaseic acid (PA), dihydrophaseic acid (DPA), ABA-glucose ester (ABA-GE) [KNOWN — quantification of ABA catabolism provides information on CYP707A activity]
- GA species: GA₁, GA₃, GA₄, GA₈, GA₂₀, GA₂₉ (active and inactive GAs to assess biosynthesis vs. catabolism) [KNOWN — GA₄ is the primary bioactive GA in Arabidopsis seeds; GA₁ may be more important in soybean — INFERRED]
- Cytokinin species: tZ, tZR, iP, iPR, cZ (trans-zeatin, isopentenyladenine, cis-zeatin) [KNOWN]
- Ethylene: measure ACC (1-aminocyclopropane-1-carboxylic acid) by LC-MS/MS as ethylene precursor; measure ethylene gas evolution by GC from intact seeds in sealed vials [KNOWN method]
- JA and JA-Ile: quantify by LC-MS/MS [KNOWN]
- SA: quantify by LC-MS/MS [KNOWN]

*Transcriptional analysis of hormone pathway genes*:
- qRT-PCR panel for key biosynthesis and catabolism enzymes:
  - ABA: *GmNCED* (9-cis-epoxycarotenoid dioxygenase, biosynthesis), *GmCYP707A* (catabolism) [KNOWN]
  - GA: *GmGA20ox*, *GmGA3ox* (biosynthesis), *GmGA2ox* (catabolism) [KNOWN]
  - Ethylene: *GmACS* (ACC synthase), *GmACO* (ACC oxidase) [KNOWN]
  - Signaling: *GmABI3*, *GmABI5*, *GmGID1*, *GmSLR1/DELLA*, *GmETR1/2* [KNOWN]

*Hormone sensitivity assay*:
- Treat seeds with exogenous ABA (1, 10, 100 μM) or GA₃ (1, 10, 100 μM) ± EPS preparation
- Determine whether EPS treatment alters sensitivity to exogenous hormones (shifts dose-response curve)
- Reduced ABA sensitivity or increased GA sensitivity in EPS-treated seeds would indicate signaling pathway changes beyond hormone level changes

**Expected result if hormonal reprogramming model is correct**: EPS-treated seeds show faster decline in ABA levels (lower ABA at 12–24h), faster rise in GA₄ levels, and higher ACC/ethylene production relative to water controls; these changes are partially attenuated in C4 (RNase-treated) and C8 (PEG) controls; *GmCYP707A* expression is higher in C1 than C12 at 12h; *GmETR1/2* expression is lower in C1 than C12 (consistent with exRNA targeting). [INFERRED — based on known ABA-GA dynamics during germination and the predicted exRNA targets]

**Expected result if hormonal changes are secondary to osmopriming**: C1 and C8 show identical hormone profiles; the hormonal shift is a consequence of faster imbibition, not exRNA activity.

**Timeline**: 16–20 weeks (LC-MS/MS method development for soybean tissue: 4 weeks; time-course sampling: 3 weeks; analysis: 4 weeks; qRT-PCR: 3 weeks; hormone sensitivity assays: 4 weeks)

**Difficulty**: High (LC-MS/MS hormone quantification requires specialized equipment and method development for each hormone class)

**Priority**: High — hormonal reprogramming is the most tractable mechanistic hypothesis and directly connects to known germination biology

---

### Experiment 3.3: Off-Target Effect and Seedling Fitness Assessment

**Experiment**: Determine whether exRNA treatment causes unintended silencing of non-target soybean genes, and whether any germination improvement comes at the cost of reduced seedling fitness, stress tolerance, or yield.

**Hypothesis tested**: The exRNA treatment does not cause significant off-target gene silencing in soybean, and germination-improved seedlings show normal or enhanced subsequent growth, stress tolerance, and reproductive fitness.

**Method**:

*Part A: Off-target transcriptome analysis*
- From Experiment 1.3 RNA-seq data: identify all genes significantly downregulated in C1 vs. C12 (FDR < 0.05, |log₂FC| > 1)
- For each downregulated gene, determine whether it has predicted complementarity to any bacterial exRNA (from Experiment 2.1)
- Classify downregulated genes as: (a) predicted exRNA targets, (b) secondary effects (downstream of predicted targets), (c) potential off-targets (no predicted exRNA complementarity but downregulated)
- For off-target genes: assess functional categories by GO enrichment; flag any genes whose downregulation could impair seedling development (e.g., photosynthesis, primary metabolism, stress response)
- Quantify: what fraction of the transcriptome is affected? (expected: <5% for a specific mechanism; >20% would suggest non-specific effects) [SPECULATIVE — no benchmark exists for this system]

*Part B: Seedling fitness assessment*
- Grow EPS-treated and control seeds to maturity in greenhouse conditions
- Measure at seedling stage (V1–V3):
  - Hypocotyl and root length, fresh and dry weight
  - Chlorophyll content (SPAD meter)
  - Photosynthetic rate (LI-COR 6800 or equivalent)
  - Root architecture (WinRHIZO scanning)
  - Nodulation: count and weigh nodules at V3 (critical for soybean nitrogen fixation [KNOWN])
- Measure at reproductive stage (R1–R8):
  - Days to flowering, days to maturity
  - Pod number, seed number per pod, seed weight
  - Seed protein and oil content (NIR spectroscopy)
  - Seed germination of F1 seeds (does treatment affect next-generation germination?)
- Stress tolerance tests:
  - Drought stress: withhold water at V2 for 7 days; measure recovery
  - Pathogen challenge: inoculate with *Phytophthora sojae* (major soybean pathogen [KNOWN]); measure disease severity
  - Cold stress: grow at 15°C for 2 weeks; measure survival and growth

*Part C: Microbiome impact assessment*
- Collect rhizosphere soil from EPS-treated and control plants at V3 and R1
- Extract DNA; perform 16S rRNA amplicon sequencing (V3-V4 region, Illumina MiSeq)
- Assess: does EPS treatment alter the rhizosphere microbiome composition? Does it affect *Bradyrhizobium japonicum* colonization (critical for soybean nodulation [KNOWN])?
- This addresses the microbiome-mediated indirect effect confounder

**Expected result if exRNA mechanism is safe and specific**: Off-target transcriptome changes are limited (<5% of genes); seedling growth, nodulation, yield components, and stress tolerance are not significantly different from water-treated controls; rhizosphere microbiome composition is not significantly altered. [SPECULATIVE — safety profile is unknown]

**Expected result if off-target effects are significant**: Broad transcriptome disruption (>10% of genes affected); reduced seedling vigor, impaired nodulation, or altered stress tolerance; these findings would require reformulation of the exRNA preparation to improve specificity before agricultural application.

**Timeline**: 18–24 months (full growing season required for reproductive fitness assessment; can be initiated in parallel with Tier 2 experiments)

**Difficulty**: High (requires greenhouse facilities, plant pathology capabilities, microbiome sequencing)

**Priority**: High — essential for any translational application; safety data must be generated before field trials

---

### Experiment 3.4: Mechanistic Model Discrimination — Epigenetic vs. Hormonal vs. Multi-Target

**Experiment**: Use pharmacological and genetic interventions to determine which causal model (epigenetic master switch, hormonal reprogramming, or multi-target dormancy dissolution) best explains the germination improvement phenotype.

**Hypothesis tested**: The three causal models make distinct, testable predictions about which interventions should block or enhance the EPS treatment effect; by testing these interventions, the dominant mechanism can be identified.

**Method**:

*Pharmacological intervention panel*:
Apply the following inhibitors/activators to soybean seeds simultaneously with EPS treatment (or water control), measuring germination phenotype:

| Intervention | Target | Prediction if Epigenetic Model | Prediction if Hormonal Model | Prediction if Multi-Target Model |
|-------------|--------|-------------------------------|------------------------------|----------------------------------|
| 5-Azacytidine (10 μM) | DNA methyltransferase inhibitor | Mimics EPS effect; no additive effect with EPS | Partial mimicry | Partial mimicry |
| Zebularine (100 μM) | DNA methyltransferase inhibitor (alternative) | Same as above | Same | Same |
| Trichostatin A (1 μM) | HDAC inhibitor (promotes chromatin opening) | Additive with EPS | No effect | Partial additive |
| Paclobutrazol (10 μM) | GA biosynthesis inhibitor | No effect (upstream of epigenetic changes) | Blocks EPS effect | Partial block |
| Fluridone (10 μM) | ABA biosynthesis inhibitor | Additive with EPS | Additive with EPS | Partial additive |
| ABA (10 μM) exogenous | ABA signaling activation | Partially blocks EPS effect | Strongly blocks EPS effect | Partially blocks |
| Ethephon (100 μM) | Ethylene-releasing compound | Additive with EPS | Additive (if ETR1 is target) | Partial additive |
| Silver nitrate (1 mM) | Ethylene perception inhibitor | No effect | Blocks EPS effect (if ETR1 is key target) | Partial block |
| Methyl jasmonate (10 μM) | JA pathway activation | No effect | Partial block | Partial block |
| Sodium orthovanadate (1 mM) | PP2A inhibitor | No effect | Partial effect | Partial effect |

- For each intervention: n=6 replicates of 50 seeds; measure germination rate, MGT, SVI
- Interpret results using the prediction matrix above: which model is most consistent with the observed pattern of inhibition/enhancement?

*Genetic model discrimination*:
- If CRISPR mutants from Experiment 2.5 are available:
  - Test whether *GmMET1* knockout seeds respond to hormonal inhibitors differently from wild-type (tests whether epigenetic changes are upstream of hormonal changes)
  - Test whether *GmETR1* knockout seeds respond to 5-azacytidine (tests whether hormonal changes are upstream of epigenetic changes)
  - The direction of epistasis between epigenetic and hormonal mutants will discriminate between the models

**Expected result if epigenetic master switch model is correct**: 5-Azacytidine mimics and is not additive with EPS treatment; paclobutrazol does not block EPS effect; TSA is additive with EPS. [SPECULATIVE]

**Expected result if hormonal reprogramming model is correct**: Paclobutrazol blocks EPS effect; fluridone is additive; silver nitrate blocks EPS effect (if ETR1 is a key target); 5-azacytidine has little effect on EPS response. [SPECULATIVE]

**Expected result if multi-target model is correct**: No single intervention fully blocks or mimics the EPS effect; partial effects are seen with multiple interventions; the combination of 5-azacytidine + fluridone + ethephon most closely mimics EPS treatment. [SPECULATIVE — this is the prediction most consistent with the "dormancy dissolution" multi-target causal model]

**Timeline**: 12–16 weeks (pharmacological panel: 8 weeks; genetic epistasis: dependent on CRISPR line availability)

**Difficulty**: Medium-High (pharmacological treatments are straightforward; genetic epistasis requires mutant lines)

**Priority**: Medium-High — provides mechanistic insight but is not prerequisite for translational development

---

## Tier 4: Advanced and Translational Studies

*Purpose: Translate validated mechanisms into agricultural applications, optimize the exRNA preparation for field use, assess performance across multiple soybean cultivars and environments, and evaluate regulatory and commercial viability.*

**Prerequisite**: Tier 3 experiments must have established: (1) a mechanistically validated causal model; (2) an acceptable off-target and safety profile; (3) a defined active component (specific exRNA sequences or preparation conditions) that can be standardized for manufacturing.

---

### Experiment 4.1: Multi-Cultivar and Multi-Environment Performance Evaluation

**Experiment**: Test the optimized exRNA preparation across a panel of commercially relevant soybean cultivars spanning different maturity groups, seed qualities, and stress tolerances, under controlled environment and field conditions.

**Hypothesis tested**: The germination improvement conferred by the exRNA preparation is consistent across diverse soybean genetic backgrounds and environmental conditions, and is not cultivar-specific or environment-specific in ways that would limit commercial applicability.

**Method**:

*Cultivar panel*:
- Select 12–15 soybean cultivars representing:
  - Maturity groups II–V (major commercial range in North America)
  - High-yielding elite lines (e.g., AG36X6, P38T83)
  - Stress-tolerant lines (drought-tolerant, cold-tolerant)
  - High-protein and high-oil specialty cultivars
  - Williams 82 (reference, for comparison with controlled experiments)
  - At least 2 cultivars with documented poor germination under cold stress (relevant to early planting)

*Treatment optimization*:
- Based on Tier 2 results, define the optimal exRNA preparation: concentration, formulation (EPS matrix vs. purified RNA vs. synthetic oligonucleotide cocktail), treatment duration, and drying-back protocol
- Test 3 formulations: (a) full EPS preparation, (b) purified exRNA fraction, (c) synthetic oligonucleotide cocktail (if Experiment 2.3 identified active sequences)
- Compare to commercial seed treatment standards: hydropriming (water, 8h), PEG osmopriming (−0.5 MPa, 8h), commercial biostimulant (e.g., Bacillus-based PGPR product)

*Controlled environment trials*:
- Germination chamber trials at 3 temperatures: 15°C (cold stress), 25°C (optimal), 35°C (heat stress)
- Germination paper and sand substrate (to assess soil-relevant conditions)
- n=6 replicates of 50 seeds per cultivar per treatment per temperature
- Measure: germination rate, MGT, uniformity, seedling vigor index

*Field trials (Year 1)*:
- Locations: minimum 3 geographically distinct sites representing major soybean production regions (e.g., Iowa, Illinois, Indiana for US context; or equivalent for target market)
- Design: randomized complete block design (RCBD) with 4 blocks per location; plot size minimum 4 rows × 10m
- Treatments: exRNA preparation, PEG osmopriming, commercial biostimulant, untreated control
- Planting dates: 2 per location (optimal and early planting to stress-test cold germination)
- Measurements:
  - Field emergence rate and uniformity (count at 7, 14, 21 