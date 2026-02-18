# Validation Plan — Spinach (Spinacia oleracea)

# Comprehensive 4-Tier Validation Plan: Bacterial exRNA-Mediated Germination Improvement in *Spinacia oleracea*

---

## Preamble: Validation Philosophy

This plan is designed around a **falsification-first** logic. The most important experiments are those capable of *disproving* the exRNA mechanism, not merely confirming it. Given the substantial confounders identified (EPS osmopriming, polysaccharide elicitor effects, microbiome conditioning), the burden of proof requires demonstrating that:

1. Sequence-specific RNA silencing occurs in embryonic cells [not just osmotic priming]
2. Specific target mRNAs are reduced in abundance in treated seeds [not just transcriptome-wide stress responses]
3. Target reduction is causally linked to germination improvement [not merely correlated]
4. The effect is reproducible across environmental conditions and seed lots [not an artifact of a single experiment]

**Label conventions throughout**: [KNOWN], [INFERRED], [SPECULATIVE] applied to all mechanistic claims. All experimental predictions are falsifiable hypotheses, not guaranteed outcomes.

---

## Tier 1: Essential Controls — Confounder Elimination

*These experiments must be completed and interpreted before any mechanistic work begins. A positive result from Tier 1 (i.e., the exRNA mechanism survives confounder testing) is the prerequisite gate for all subsequent tiers.*

---

### Experiment T1.1: RNA-Depleted EPS Control

**Experiment**: Enzymatic RNA depletion from bacterial EPS preparation to isolate EPS osmopriming effects from exRNA effects.

**Hypothesis tested**: Is the observed germination improvement attributable to the RNA component of the bacterial preparation, or is it fully explained by the EPS matrix acting as an osmopriming agent?

**Method**:
1. Prepare bacterial EPS solution at standard treatment concentration using established protocol
2. Split preparation into four aliquots:
   - **Treatment A**: Intact EPS preparation (positive control, standard treatment)
   - **Treatment B**: EPS + RNase A (100 µg/mL, 37°C, 2h) + RNase III (1 U/µL, 37°C, 1h) + RNase T1 (10 U/µL, 37°C, 1h) — degrades ssRNA, dsRNA, and ssRNA at G residues respectively; heat-inactivate at 95°C for 10 min
   - **Treatment C**: EPS + heat-inactivated RNase cocktail (boiled 15 min before addition) — protein denaturation control to verify RNase treatment does not introduce confounding proteins
   - **Treatment D**: Water control (no EPS, no RNA)
3. Verify RNA depletion in Treatment B by: (a) Bioanalyzer RNA 6000 Pico chip — confirm absence of RNA peaks; (b) RT-qPCR with universal bacterial 16S primers on the preparation — confirm no amplifiable RNA; (c) Fluorometric RNA quantification (RiboGreen assay) — confirm >99% RNA removal
4. Measure osmotic potential (ψ) of Treatments A and B using vapor pressure osmometer (Wescor VAPRO or equivalent) — confirm ψ is not significantly altered by RNA removal
5. Apply all four treatments to spinach seeds (minimum n=4 biological replicates, 50 seeds per replicate per treatment) under controlled germination conditions (20°C, 12h light/dark, filter paper, Petri dish)
6. Record: germination percentage at 24h, 48h, 72h, 96h, 120h; T50 (time to 50% germination); radicle length at 120h; seedling fresh weight at 7 days

**Expected result if exRNA mechanism is real**: Treatment A (intact) significantly outperforms Treatment B (RNA-depleted) in germination rate and/or percentage. Treatment B performs similarly to Treatment D (water) or to the osmotic equivalent control (see T1.2). The difference between A and B is attributable to the RNA component. [INFERRED from exRNA hypothesis]

**Expected result if EPS osmopriming is the primary confounder**: Treatment A and Treatment B perform equivalently (no significant difference in germination metrics). Both outperform Treatment D. The EPS matrix, not the RNA, drives the phenotype. [KNOWN: osmopriming mechanism is well-established; Paparella et al., 2015]

**Critical confound within this experiment**: RNase treatment could alter EPS structure, viscosity, or introduce contaminating proteins. Treatment C controls for protein contamination. Viscosity should be measured (Brookfield viscometer) for Treatments A and B to confirm equivalence. If viscosity changes, a viscosity-matched methylcellulose control must be added.

**Timeline**: 3–4 weeks (1 week preparation and verification, 2–3 weeks germination assays with replication)

**Difficulty**: Medium — RNase treatment is routine; vapor pressure osmometry requires specialized equipment but is widely available; Bioanalyzer access may require core facility scheduling

**Priority**: **Critical** — This is the single most important experiment in the entire validation plan. No mechanistic interpretation is valid without this control.

---

### Experiment T1.2: Osmotic Equivalence Control

**Experiment**: Match the water potential of the EPS solution with inert osmolytes (PEG 6000, PEG 8000) to determine whether osmotic priming alone explains the phenotype.

**Hypothesis tested**: Is the germination improvement attributable to the specific molecular identity of bacterial EPS/exRNA, or is it a non-specific consequence of altered water potential during imbibition?

**Method**:
1. Measure ψ of the bacterial EPS preparation precisely (vapor pressure osmometer, minimum 3 technical replicates)
2. Prepare PEG 6000 and PEG 8000 solutions at matched ψ using the Michel & Kaufmann (1973) equation: ψ (MPa) = −(1.18 × 10⁻²)C − (1.18 × 10⁻⁴)C² + (2.67 × 10⁻⁴)CT + (8.39 × 10⁻⁷)C²T, where C = g PEG per kg water, T = temperature in °C
3. Prepare methylcellulose solution at matched viscosity (not matched ψ) as a viscosity control
4. Prepare mannitol solution at matched ψ as a small-molecule osmolyte control (eliminates polymer effects)
5. Germination assay: same protocol as T1.1, with treatments: (a) EPS intact, (b) PEG 6000 at matched ψ, (c) PEG 8000 at matched ψ, (d) mannitol at matched ψ, (e) methylcellulose at matched viscosity, (f) water control
6. Statistical analysis: one-way ANOVA with Tukey HSD post-hoc; effect sizes (Cohen's d) reported for all pairwise comparisons

**Expected result if exRNA mechanism is real**: EPS intact treatment significantly outperforms all osmotic equivalents. The specific molecular composition of the EPS preparation (i.e., the RNA component) provides benefit beyond osmotic priming. [INFERRED]

**Expected result if osmopriming is the primary mechanism**: PEG solutions at matched ψ perform equivalently to EPS intact treatment. No significant difference between EPS and osmotic equivalents. [KNOWN: PEG osmopriming is well-characterized in spinach; Demir & Mavi, 2004, *Scientia Horticulturae*]

**Note on spinach-specific context**: [KNOWN] Spinach germination is particularly sensitive to osmotic conditions due to the pericarp (fruit wall) that restricts water uptake. Osmopriming is already used commercially for spinach seed enhancement. This makes the osmopriming confounder especially potent in this species.

**Timeline**: 3–4 weeks

**Difficulty**: Low-Medium — PEG solutions are routine; vapor pressure osmometry is the rate-limiting step

**Priority**: **Critical**

---

### Experiment T1.3: Polysaccharide Elicitor Specificity Control

**Hypothesis tested**: Does the bacterial EPS activate plant pattern recognition receptors (PRRs) as a MAMP, triggering ISR/defense priming that secondarily improves germination, independent of RNA content?

**Method**:
1. Prepare: (a) intact EPS treatment; (b) RNA-depleted EPS (from T1.1); (c) purified commercial bacterial polysaccharides at matched concentration — specifically: laminarin (β-1,3-glucan, known elicitor), chitosan (positive MAMP control), and lipopolysaccharide (LPS, gram-negative MAMP); (d) flg22 peptide (canonical MAMP, 1 µM) as positive elicitor control; (e) water control
2. **Germination assay**: Standard protocol, same metrics as T1.1
3. **Defense marker assay**: At 24h and 48h post-treatment, harvest seed/seedling tissue (pool 10 seeds per sample, n=4 biological replicates), extract RNA, perform RT-qPCR for: *PR1* (pathogenesis-related 1, SA marker), *PDF1.2* (plant defensin, JA/ET marker), *WRKY33* (defense TF), *MPK3/MPK6* (MAPK cascade markers). Use spinach-specific primers designed against SOV genome sequences.
4. **Hormone profiling**: At 48h, measure ABA and SA levels by LC-MS/MS in treated vs. control seeds (minimum 200 mg fresh weight per sample)

**Expected result if exRNA mechanism is real**: Intact EPS outperforms all purified polysaccharide elicitors. Defense markers are not significantly elevated in EPS-treated seeds compared to water control (or are elevated less than in flg22-treated seeds). [INFERRED]

**Expected result if polysaccharide elicitor effect is the primary mechanism**: Laminarin or LPS treatments produce germination improvement comparable to intact EPS. Defense markers (PR1, PDF1.2) are elevated in EPS-treated seeds, consistent with ISR priming. [KNOWN: bacterial EPS can trigger ISR; Pieterse et al., 2014]

**Timeline**: 4–5 weeks (includes LC-MS/MS scheduling)

**Difficulty**: Medium-High — LC-MS/MS requires specialized equipment and expertise; RT-qPCR requires validated spinach-specific primers

**Priority**: **Critical**

---

### Experiment T1.4: Microbiome Exclusion Control

**Hypothesis tested**: Does the presence of live bacteria (or their metabolites beyond EPS/RNA) in the spermosphere alter the seed microbiome in ways that independently improve germination?

**Method**:
1. Prepare: (a) live bacterial treatment (standard); (b) filter-sterilized EPS preparation (0.22 µm membrane filtration — removes bacteria but retains EPS and RNA); (c) autoclaved preparation (121°C, 20 min — kills bacteria, degrades RNA, partially degrades EPS); (d) gamma-irradiated preparation (25 kGy — kills bacteria, partially degrades RNA, preserves EPS structure better than autoclaving); (e) water control
2. Verify sterility of treatments b–d by plating on LB agar (48h, 37°C)
3. Verify RNA integrity in treatment b by Bioanalyzer; verify RNA degradation in c and d
4. **Germination assay**: Standard protocol
5. **Spermosphere microbiome profiling** (optional but strongly recommended): At 48h post-treatment, collect spermosphere soil/filter paper wash, extract DNA, perform 16S rRNA amplicon sequencing (V3-V4 region, Illumina MiSeq) to characterize microbial community shifts

**Expected result if exRNA mechanism is real**: Filter-sterilized preparation (b) performs similarly to live bacterial treatment (a). Autoclaved and gamma-irradiated preparations (c, d) perform worse than b, consistent with RNA degradation reducing efficacy. [INFERRED]

**Expected result if live bacteria/microbiome is the primary driver**: Live bacterial treatment (a) significantly outperforms filter-sterilized preparation (b). Filter-sterilized preparation performs no better than water control. [INFERRED from microbiome priming literature]

**Timeline**: 4–6 weeks (microbiome sequencing adds 2–3 weeks)

**Difficulty**: Medium — filter sterilization is routine; microbiome sequencing requires bioinformatics capacity

**Priority**: **High**

---

### Experiment T1.5: Dose-Response and Sequence Specificity Baseline

**Hypothesis tested**: Does the germination improvement show a dose-response relationship consistent with RNA-mediated silencing (saturable, sequence-dependent) rather than osmotic effects (linear with concentration)?

**Method**:
1. Prepare EPS/exRNA preparation at 6 concentrations spanning 3 orders of magnitude (e.g., 0.001×, 0.01×, 0.1×, 1×, 10×, 100× standard treatment concentration)
2. Measure ψ at each concentration
3. Germination assay at all concentrations (standard protocol)
4. Fit dose-response curves: (a) linear model (expected for osmotic effects); (b) sigmoidal/Hill equation model (expected for receptor-mediated or RNAi-mediated effects); (c) compare model fits by AIC/BIC
5. **Sequence scramble control** [SPECULATIVE but critical]: If the bacterial exRNA sequences are known, synthesize scrambled-sequence RNA oligonucleotides of identical length, GC content, and secondary structure (use Mfold or RNAfold to match ΔG) and incorporate into EPS matrix at equivalent concentration. Compare germination improvement of native vs. scrambled RNA in EPS matrix.

**Expected result if exRNA mechanism is real**: Sigmoidal dose-response curve with a saturation plateau (consistent with AGO loading saturation). Scrambled RNA in EPS matrix performs significantly worse than native sequence RNA in EPS matrix. [INFERRED from RNAi mechanism]

**Expected result if osmotic priming is the primary mechanism**: Linear dose-response relationship correlating with ψ. Scrambled RNA performs equivalently to native RNA when incorporated into EPS matrix at matched concentration. [INFERRED]

**Note**: The scrambled RNA control is [SPECULATIVE] in its design assumptions but is the most direct test of sequence specificity available without transgenic plant lines.

**Timeline**: 5–6 weeks

**Difficulty**: High — scrambled RNA synthesis is expensive; sequence information about exRNAs must be available; matching secondary structure is technically demanding

**Priority**: **High**

---

## Tier 2: Target Validation — Top 10 Priority Targets

*These experiments assume Tier 1 has demonstrated that the RNA component contributes meaningfully to the phenotype beyond EPS osmopriming alone. The goal is to confirm that specific predicted target mRNAs are downregulated in treated seeds and that this downregulation is causally linked to germination improvement.*

---

### Experiment T2.1: Target mRNA Quantification Panel — RT-qPCR Time Course

**Experiment**: Quantify expression of all top-ranked target mRNAs in treated vs. control seeds across a germination time course.

**Hypothesis tested**: Are the predicted target mRNAs specifically downregulated in exRNA-treated seeds compared to RNA-depleted EPS controls, and does the timing of downregulation precede or coincide with germination improvement?

**Method**:
1. **Seed treatment groups** (minimum n=5 biological replicates, 50 seeds per replicate per time point):
   - Group A: Intact EPS/exRNA treatment
   - Group B: RNA-depleted EPS (from T1.1 — critical comparator)
   - Group C: Water control
   - Group D: PEG osmotic equivalent (from T1.2)
2. **Harvest time points**: 0h (dry seed), 6h, 12h, 24h, 48h, 72h post-treatment (covering Phase I and Phase II of imbibition through radicle emergence)
3. **RNA extraction**: Embryo dissection from pericarp under RNase-free conditions (critical — pericarp contains high tannin/polyphenol content that inhibits RNA extraction; use CTAB-based protocol with PVP-40 and β-mercaptoethanol, or Spectrum Plant Total RNA Kit with on-column DNase treatment). Verify RNA quality by Bioanalyzer (RIN ≥ 7.0 required) and A260/A280 ratio (≥ 1.8)
4. **RT-qPCR panel** — design primers for top 10 targets using Primer3Plus, validate efficiency (90–110%) by standard curve, test for genomic DNA contamination with no-RT controls:

| Priority | Gene ID | Target Name | Expected Direction |
|----------|---------|-------------|-------------------|
| 1 | SOV3g000150.1 | Ethylene receptor | Downregulated |
| 2 | SOV1g033340.1 | DNA methyltransferase | Downregulated |
| 3 | SOV6g036290.1 | HIRA histone chaperone | Downregulated |
| 4 | SOV4g015450.1 | SUVR5 histone methyltransferase | Downregulated |
| 5 | TPS gene(s) | Trehalose-phosphate synthase | Downregulated |
| 6 | CCC gene(s) | Cation-chloride cotransporter | Downregulated |
| 7 | EDR2 homolog | Enhanced disease resistance 2 | Downregulated |
| 8 | MOS1 homolog | Modifier of snc1 | Downregulated |
| 9 | SOV4g030590.1 | PHD domain protein | Downregulated |
| 10 | SOV4g038060.1 | GIS2 zinc finger | Downregulated |

5. **Reference genes**: Validate minimum 3 reference genes for spinach seed germination (candidates: *UBQ10*, *PP2A*, *EF1α*; validate stability using geNorm or NormFinder across all time points and treatments)
6. **Statistical analysis**: Two-way ANOVA (treatment × time) with Benjamini-Hochberg FDR correction for multiple comparisons; report fold changes with 95% confidence intervals; require ≥1.5-fold change AND FDR-adjusted p < 0.05 for a target to be considered validated

**Expected result if exRNA mechanism is real**: Targets are significantly downregulated in Group A (intact EPS) compared to Group B (RNA-depleted EPS) and Group C (water) at one or more time points. Downregulation should be detectable by 12–24h (consistent with RNAi kinetics). Not all 10 targets need to be downregulated — even 3–4 confirmed targets would be a meaningful positive result. [INFERRED]

**Expected result if exRNA mechanism is absent**: No significant difference in target mRNA levels between Group A and Group B. Any differences between Group A and Group C are replicated by Group D (osmotic equivalent), indicating osmotic regulation of these transcripts rather than sequence-specific silencing. [INFERRED]

**Critical caveat**: [KNOWN] Many germination-associated genes are regulated by imbibition itself, independent of any treatment. The RNA-depleted EPS comparator (Group B) is essential — comparing only to water control would be insufficient and misleading.

**Timeline**: 8–10 weeks (primer design and validation: 3 weeks; time-course experiment with replication: 5–7 weeks)

**Difficulty**: High — embryo dissection from spinach seeds is technically demanding; RNA extraction from seed tissue is challenging; primer validation for 10 targets requires significant effort

**Priority**: **Critical**

---

### Experiment T2.2: Small RNA Sequencing of Treated Seeds — Identifying the Silencing Agent

**Experiment**: Identify which bacterial small RNAs are present inside spinach embryonic cells after treatment, and determine whether they are loaded into plant AGO complexes.

**Hypothesis tested**: Do bacterial exRNAs physically enter spinach embryonic cells and associate with plant AGO proteins, confirming the delivery step of the proposed mechanism?

**Method**:
1. **Small RNA sequencing (sRNA-seq)**:
   - Treat seeds as in T2.1 (Groups A, B, C); harvest embryos at 24h and 48h
   - Extract total RNA (Trizol + phase separation; size-select 15–40 nt fraction by PAGE)
   - Prepare sRNA libraries (NEBNext Small RNA Library Prep Kit or equivalent)
   - Sequence: Illumina NextSeq 2000, minimum 20 million reads per sample, 75 bp single-end
   - **Bioinformatics pipeline**: (a) Trim adapters (Trimmomatic/Cutadapt); (b) Map to spinach genome (SOV genome v2.0 or most current assembly) to identify endogenous plant sRNAs; (c) Map unmapped reads to bacterial genome to identify bacterial-origin reads present inside plant cells; (d) Quantify bacterial sRNA reads as fraction of total mapped reads; (e) Predict target sites in spinach transcriptome using psRNATarget or TargetFinder with bacterial sRNA sequences as queries
   - **Critical control**: Group B (RNA-depleted EPS) should show no bacterial sRNA reads in embryo tissue

2. **AGO immunoprecipitation (AGO-IP)**:
   - Generate or obtain antibody against spinach AGO1 (or use cross-reactive Arabidopsis AGO1 antibody — AtAGO1 antibody from Agrisera has documented cross-reactivity with some Brassicales; test cross-reactivity by Western blot first)
   - Alternatively: use a tagged AGO1 approach if transgenic spinach lines are available [SPECULATIVE for spinach — transgenic spinach is possible but not routine]
   - Perform AGO-IP from embryo protein extracts at 24h and 48h post-treatment
   - Extract RNA from immunoprecipitate; prepare sRNA library; sequence as above
   - **Positive result**: Bacterial-origin small RNAs are enriched in AGO-IP fraction compared to input, confirming loading into plant RNAi machinery [INFERRED from cross-kingdom RNAi mechanism; KNOWN in Botrytis-Arabidopsis system: Weiberg et al., 2013]

3. **Confound check**: Verify that bacterial sRNA reads in embryo tissue are not due to surface contamination by: (a) surface-sterilize embryos with 0.5% NaOCl for 30 sec before RNA extraction; (b) include a surface-wash fraction as a separate sequencing library to quantify surface-associated vs. internalized RNA

**Expected result if exRNA mechanism is real**: Bacterial-origin small RNAs are detectable in embryo tissue of Group A but not Group B. These reads are enriched in AGO-IP fraction. The bacterial sRNA sequences show complementarity to the predicted target mRNAs (SOV3g000150.1, SOV1g033340.1, etc.). [INFERRED]

**Expected result if exRNA delivery does not occur**: No bacterial-origin reads detected in embryo tissue above background. AGO-IP fraction contains only endogenous plant sRNAs. The entire exRNA mechanism hypothesis is falsified at the delivery step. [INFERRED]

**Timeline**: 10–12 weeks (library preparation: 3 weeks; sequencing: 1–2 weeks; bioinformatics: 4–6 weeks)

**Difficulty**: Very High — AGO-IP from seed tissue is technically demanding; bioinformatics requires expertise in distinguishing bacterial from plant sRNA reads; spinach AGO antibody may require custom generation

**Priority**: **Critical** — This is the most direct test of the delivery mechanism

---

### Experiment T2.3: Ethylene Receptor (SOV3g000150.1) Functional Validation

**Experiment**: Validate the ethylene receptor as a causal target using pharmacological ethylene signaling manipulation.

**Hypothesis tested**: Does enhanced ethylene signaling (mimicking the predicted effect of ethylene receptor downregulation) recapitulate the germination improvement observed with exRNA treatment?

**Method**:
1. **Ethylene signaling enhancement treatments**:
   - **ACC (1-aminocyclopropane-1-carboxylic acid)**: Ethylene precursor; apply at 0, 1, 10, 100 µM in germination assay — activates ethylene signaling downstream of receptor [KNOWN]
   - **AgNO₃**: Ethylene perception inhibitor (blocks receptor); apply at 0, 10, 50, 100 µM — should *reduce* germination if ethylene signaling is important [KNOWN]
   - **1-MCP (1-methylcyclopropene)**: Competitive ethylene receptor inhibitor; apply at 0, 1, 10 ppm gas phase — should block any ethylene-mediated germination improvement [KNOWN]
   - **Ethylene gas**: Apply at 0, 1, 10, 100 ppm in sealed chambers
2. **Epistasis test**: Apply ACC + intact EPS treatment simultaneously; if ethylene receptor downregulation is the primary mechanism, ACC should not provide additive benefit (ceiling effect). Apply 1-MCP + intact EPS; if ethylene receptor is the primary target, 1-MCP should partially suppress the EPS treatment benefit.
3. **RT-qPCR**: Measure SOV3g000150.1 expression in ACC-treated vs. EPS-treated vs. control seeds to confirm that ACC treatment does not itself downregulate the receptor (which would indicate a feedback loop confound)
4. **Downstream marker genes**: Measure expression of ethylene-responsive genes (*ERF* family members, *EIN3* targets) by RT-qPCR to confirm ethylene pathway activation in EPS-treated seeds

**Expected result if ethylene receptor is a primary target**: ACC treatment partially phenocopies EPS treatment (improved germination rate). 1-MCP treatment partially suppresses EPS treatment benefit. Ethylene-responsive genes are upregulated in EPS-treated seeds. [INFERRED from ethylene-dormancy antagonism; KNOWN: ethylene promotes germination in Arabidopsis; Linkies & Leubner-Metzger, 2012]

**Expected result if ethylene receptor is not a primary target**: ACC treatment has no effect on germination (or inhibits at high concentrations). 1-MCP does not suppress EPS treatment benefit. Ethylene-responsive genes are not differentially expressed in EPS-treated seeds. [INFERRED]

**Critical caveat**: [KNOWN] Ethylene effects on germination are concentration- and context-dependent. High ethylene can inhibit germination in some species. Spinach-specific ethylene dose-response must be characterized before interpreting epistasis experiments.

**Timeline**: 6–8 weeks

**Difficulty**: Medium — pharmacological treatments are routine; gas-phase treatments require specialized chambers

**Priority**: **High**

---

### Experiment T2.4: Epigenetic Target Validation — DNA Methylation Profiling

**Experiment**: Determine whether exRNA treatment causes global or locus-specific changes in DNA methylation consistent with SOV1g033340.1 (DNA methyltransferase) downregulation.

**Hypothesis tested**: Does exRNA treatment reduce DNA methylation at promoters of pro-germination genes, consistent with the Epigenetic Master Switch Model?

**Method**:
1. **Global methylation assessment**:
   - Extract genomic DNA from embryos at 24h and 48h post-treatment (Groups A, B, C from T2.1)
   - **ELISA-based global 5-methylcytosine quantification** (Epigentek MethylFlash kit or equivalent): rapid, low-input method for global methylation changes; requires ~100 ng DNA per sample
   - **HPLC-MS/MS**: Gold standard for absolute 5mC quantification; requires ~1 µg DNA; provides 5mC, 5hmC, and unmodified cytosine levels simultaneously

2. **Locus-specific methylation — Bisulfite sequencing**:
   - Select 5–8 candidate loci: promoters of GA biosynthesis genes (*GA3ox*, *GA20ox* spinach homologs), ABA catabolism genes (*CYP707A* homologs), and cell wall loosening genes (*EXP* family)
   - Bisulfite convert DNA (EZ DNA Methylation Kit, Zymo Research)
   - PCR amplify target loci with bisulfite-specific primers (design using BiSearch or MethPrimer)
   - Clone PCR products into pGEM-T vector; sequence minimum 20 clones per locus per treatment
   - Alternatively: amplicon bisulfite sequencing (Illumina) for higher throughput and quantitative methylation levels

3. **Whole-genome bisulfite sequencing (WGBS)** [optional, high priority if budget allows]:
   - 30× coverage per sample; 3 biological replicates per treatment group
   - Bioinformatics: Bismark pipeline; DMR (differentially methylated region) calling with DSS or MethylKit
   - Annotate DMRs relative to gene features (promoter, gene body, TE) using SOV genome annotation

**Expected result if DNA methyltransferase downregulation is causal**: Global 5mC levels are reduced in Group A vs. Group B and Group C at 48h. Locus-specific bisulfite sequencing shows hypomethylation at promoters of GA biosynthesis and ABA catabolism genes in Group A. WGBS reveals DMRs enriched at promoters of germination-associated genes. [INFERRED from DNA methylation-dormancy literature; KNOWN: Nee et al., 2017, *Plant Cell*]

**Expected result if DNA methyltransferase is not a primary target**: No significant difference in global or locus-specific methylation between Groups A and B. Any methylation changes are replicated by osmotic equivalent treatment (Group D from T1.2), indicating imbibition-associated demethylation rather than exRNA-specific effects. [INFERRED]

**Critical caveat**: [KNOWN] DNA methylation changes during normal imbibition are well-documented (passive demethylation due to replication without maintenance methylation). The RNA-depleted EPS comparator is essential to distinguish exRNA-specific effects from imbibition-associated demethylation.

**Timeline**: 12–16 weeks (WGBS adds significant time; locus-specific bisulfite sequencing can be completed in 8–10 weeks)

**Difficulty**: High — bisulfite conversion is technically demanding; WGBS requires significant bioinformatics capacity; spinach genome annotation quality affects DMR interpretation

**Priority**: **High**

---

### Experiment T2.5: HIRA Histone Chaperone and Chromatin State Validation

**Experiment**: Assess histone variant H3.3 deposition and H3K9me2 marks in treated seeds to validate HIRA (SOV6g036290.1) and SUVR5 (SOV4g015450.1) as functional targets.

**Hypothesis tested**: Does exRNA treatment alter chromatin state at dormancy-associated loci in a manner consistent with HIRA and SUVR5 downregulation?

**Method**:
1. **Chromatin Immunoprecipitation (ChIP)**:
   - Cross-link embryo tissue with 1% formaldehyde (10 min, room temperature); quench with glycine
   - Sonicate to 200–500 bp fragments (Bioruptor or focused ultrasonicator)
   - Immunoprecipitate with: (a) anti-H3K9me2 antibody (Abcam ab1220 — well-validated); (b) anti-H3.3 antibody (Millipore 09-838); (c) anti-H3 (total, loading control); (d) IgG (negative control)
   - **ChIP-qPCR**: Quantify enrichment at: promoters of GA biosynthesis genes, ABA signaling genes (*ABI3*, *ABI5* homologs), and known heterochromatic loci (45S rDNA, centromeric repeats as positive controls for H3K9me2)
   - **ChIP-seq** [if budget allows]: Genome-wide H3K9me2 and H3.3 mapping; minimum 10 million mapped reads per sample; peak calling with MACS2; compare between Groups A and B

2. **H3.3 incorporation assay**:
   - Pulse-label replicating cells with EdU (5-ethynyl-2'-deoxyuridine) to mark newly synthesized DNA
   - Co-immunostain with anti-H3.3 antibody
   - Confocal microscopy to assess H3.3 incorporation at EdU-positive (replicating) vs. EdU-negative (non-replicating, HIRA-dependent) loci [SPECULATIVE: this approach requires embryo cell isolation and immunostaining optimization for spinach]

**Expected result if HIRA/SUVR5 are functional targets**: H3K9me2 enrichment is reduced at dormancy-maintenance loci in Group A vs. Group B. H3.3 distribution is altered at pro-germination gene loci. [INFERRED from chromatin biology; KNOWN: SUVR5 deposits H3K9me2 in Arabidopsis, Caro et al., 2012]

**Expected result if HIRA/SUVR5 are not primary targets**: No significant difference in H3K9me2 or H3.3 distribution between Groups A and B. Chromatin state changes are replicated by osmotic equivalent treatment. [INFERRED]

**Timeline**: 12–16 weeks

**Difficulty**: Very High — ChIP from seed tissue requires large amounts of starting material (difficult to obtain for spinach embryos); antibody cross-reactivity with spinach histones must be validated; ChIP-seq requires significant bioinformatics expertise

**Priority**: **Medium-High** — important for mechanistic understanding but technically challenging; consider prioritizing ChIP-qPCR over ChIP-seq initially

---

### Experiment T2.6: TPS (Trehalose-Phosphate Synthase) Target Validation

**Experiment**: Validate TPS as a target by measuring trehalose-6-phosphate (T6P) levels and assessing the metabolic consequences of TPS downregulation.

**Hypothesis tested**: Does exRNA treatment reduce T6P accumulation in seeds, and does this correlate with altered sucrose signaling and germination improvement?

**Method**:
1. **T6P quantification by LC-MS/MS**:
   - Extract metabolites from embryo tissue at 24h and 48h (Groups A, B, C)
   - Quantify T6P, trehalose, sucrose, glucose, fructose, and UDP-glucose by LC-MS/MS (use ¹³C-labeled internal standards for absolute quantification)
   - Minimum 5 biological replicates, 200 mg fresh weight per sample

2. **TPS enzyme activity assay**:
   - Extract soluble protein from embryo tissue
   - Measure TPS activity: incubate with UDP-glucose and glucose-6-phosphate; quantify T6P production by LC-MS/MS or colorimetric phosphate release assay
   - Compare enzyme activity between Groups A, B, C

3. **Sucrose signaling markers**:
   - Measure expression of SnRK1 target genes (known to be regulated by T6P/sucrose ratio) by RT-qPCR: *ASN1* (asparagine synthetase 1), *DIN6* (dark-inducible 6), *bZIP11* targets [KNOWN: T6P inhibits SnRK1 activity; Eastmond et al., 2002; Paul et al., 2008]

**Expected result if TPS is a functional target**: T6P levels are reduced in Group A vs. Group B. TPS enzyme activity is reduced in Group A. SnRK1 target genes show altered expression consistent with reduced T6P-mediated SnRK1 inhibition (i.e., SnRK1 is more active). [INFERRED from T6P-SnRK1 signaling; KNOWN in Arabidopsis seeds: Gomez et al., 2010]

**Expected result if TPS is not a primary target**: No significant difference in T6P levels between Groups A and B. Metabolic differences between A and C are replicated by osmotic equivalent. [INFERRED]

**Timeline**: 8–10 weeks

**Difficulty**: High — LC-MS/MS for T6P requires specialized expertise; T6P is present at very low concentrations in plant tissue (pmol/g FW range) and requires careful extraction and quantification

**Priority**: **Medium-High**

---

### Experiment T2.7: Cation-Chloride Cotransporter (CCC) Functional Validation

**Experiment**: Validate CCC as a target by measuring ion homeostasis and turgor pressure changes in treated seeds.

**Hypothesis tested**: Does exRNA treatment alter chloride and potassium transport in embryonic cells in a manner consistent with CCC downregulation, and does this affect turgor-driven radicle emergence?

**Method**:
1. **Ion content measurement**:
   - Extract ions from embryo tissue at 24h and 48h (Groups A, B, C)
   - Measure Cl⁻, K⁺, Na⁺ by ICP-OES (inductively coupled plasma optical emission spectrometry) or ion chromatography
   - Minimum 5 biological replicates

2. **Osmotic potential of embryo cells**:
   - Measure osmotic potential of embryo cell sap by vapor pressure osmometry (Peltier effect psychrometer or pressure bomb)
   - Compare between treatment groups

3. **Radicle emergence mechanics**:
   - Time-lapse imaging of radicle emergence (hourly photography, 0–120h)
   - Measure radicle elongation rate and force of emergence (using a texture analyzer with a flat probe — measure force required to penetrate the pericarp as a proxy for turgor-driven emergence force) [SPECULATIVE: this approach is not standard but is technically feasible]

4. **Pharmacological validation**:
   - Apply furosemide (CCC inhibitor, 100–500 µM) to seeds in germination assay
   - If CCC downregulation improves germination, furosemide should partially phenocopy the EPS treatment effect [KNOWN: furosemide inhibits plant CCC; Colmenero-Flores et al., 2007]

**Expected result if CCC is a functional target**: Cl⁻ accumulation is reduced in embryo cells of Group A vs. Group B (consistent with reduced Cl⁻ import). Osmotic potential of embryo cells is altered. Furosemide treatment partially phenocopies EPS treatment. [INFERRED from CCC function in plant ion homeostasis; KNOWN: CCC loss-of-function affects turgor in Arabidopsis]

**Timeline**: 8–10 weeks

**Difficulty**: Medium — ICP-OES is widely available; furosemide pharmacology is straightforward; texture analysis requires specialized equipment

**Priority**: **Medium**

---

### Experiment T2.8: EDR2/MOS1 Immune Regulator Validation

**Experiment**: Validate EDR2 and MOS1 homologs as targets by assessing defense-growth tradeoff in treated seeds.

**Hypothesis tested**: Does exRNA treatment suppress immune priming in seeds, and does this suppression correlate with improved germination through resource reallocation from defense to growth?

**Method**:
1. **Defense gene expression panel** (RT-qPCR at 24h, 48h, 72h):
   - *PR1*, *PR2*, *PR5* (SA-responsive)
   - *PDF1.2*, *VSP2* (JA-responsive)
   - *WRKY33*, *WRKY40*, *WRKY70* (defense TFs)
   - *EDR2* and *MOS1* homologs themselves

2. **Callose deposition assay**:
   - Stain embryo sections with aniline blue (callose-specific fluorochrome)
   - Quantify callose deposits by confocal microscopy (measure fluorescence intensity per unit area)
   - Callose is a marker of immune activation; reduced callose in EPS-treated seeds would indicate immune suppression [KNOWN: callose deposition is a hallmark of PTI; Luna et al., 2011]

3. **Salicylic acid quantification**:
   - LC-MS/MS measurement of free SA and SA glucoside in embryo tissue at 24h and 48h

4. **Disease resistance test** [important safety check]:
   - Germinate EPS-treated and control seeds in soil inoculated with *Pythium ultimum* or *Fusarium oxysporum* (common spinach pathogens)
   - Assess damping-off incidence at 7 and 14 days
   - **Critical**: If exRNA treatment suppresses immunity, it must not increase disease susceptibility — this is an agronomic safety concern [INFERRED from growth-defense tradeoff; KNOWN: EDR2 loss-of-function increases powdery mildew susceptibility in Arabidopsis; Vorwerk et al., 2007]

**Expected result if EDR2/MOS1 are functional targets**: Defense gene expression is reduced in Group A vs. Group B. Callose deposition is reduced. SA levels are lower in Group A. Critically: disease susceptibility is NOT significantly increased (if the immune suppression is transient and limited to the germination window). [INFERRED]

**Expected result if immune suppression is a concern**: Increased damping-off incidence in EPS-treated seedlings. This would represent a significant agronomic liability that must be reported and addressed before any field application. [INFERRED]

**Timeline**: 10–12 weeks (disease resistance test requires additional 4 weeks)

**Difficulty**: Medium — callose staining requires confocal microscopy; disease resistance assay requires containment facilities if using live pathogens

**Priority**: **High** — both for mechanistic validation and agronomic safety assessment

---

### Experiment T2.9: Genetic Validation Using Arabidopsis Homolog Mutants

**Experiment**: Use available Arabidopsis T-DNA insertion mutants for homologs of the top spinach targets to confirm that loss-of-function of these genes improves germination, providing genetic proof-of-concept.

**Hypothesis tested**: Do loss-of-function mutations in Arabidopsis homologs of the top spinach targets phenocopy the germination improvement predicted by the exRNA mechanism?

**Rationale**: [KNOWN] Arabidopsis has extensive mutant collections (SALK, SAIL, GABI-Kat) and well-characterized germination assays. While Arabidopsis is not spinach, genetic validation in Arabidopsis provides the strongest available causal evidence for gene function in the absence of spinach transgenic tools.

**Method**:
1. **Identify Arabidopsis homologs** of top spinach targets using BLAST against TAIR10 genome; select homologs with >60% amino acid identity
2. **Obtain T-DNA insertion lines** from ABRC (Arabidopsis Biological Resource Center) for:
   - *ETR1*, *EIN4* (ethylene receptors — *etr1-1*, *ein4-1* are classic mutants with known germination phenotypes) [KNOWN]
   - *MET1* (DNA methyltransferase — *met1-3* mutant available) [KNOWN]
   - *HIRA* (histone chaperone — *hira* mutant available; Nie et al., 2014) [KNOWN]
   - *SUVR5* (*suvr5* mutant available; Caro et al., 2012) [KNOWN]
   - *TPS1*, *TPS2* (trehalose-phosphate synthase) [KNOWN]
   - *CCC* (cation-chloride cotransporter — *ccc* mutant; Colmenero-Flores et al., 2007) [KNOWN]
3. **Germination assays** in Arabidopsis:
   - Stratification: 4°C, 4 days (standard dormancy release protocol)
   - Germination on ½ MS agar with and without ABA (0.5, 1, 2 µM) to assess ABA sensitivity
   - Germination under osmotic stress (PEG, NaCl) to assess stress tolerance
   - Record: germination percentage at 24h, 48h, 72h, 96h; T50; root length at 7 days
4. **Predicted outcomes based on known literature**:
   - *etr1* and *ein4* mutants: reduced ethylene sensitivity; germination phenotype is complex (gain-of-function *etr1-1* is ethylene-insensitive; loss-of-function should enhance ethylene response) [KNOWN — must use appropriate allele]
   - *met1* mutants: genome-wide hypomethylation; germination phenotype under investigation [INFERRED]
   - *hira* mutants: chromatin state changes; germination phenotype not well-characterized [SPECULATIVE]

**Expected result if targets are causal**: Loss-of-function mutants in the top-ranked targets show improved germination rate, reduced ABA sensitivity, or improved germination under stress conditions compared to wild-type Col-0. [INFERRED]

**Expected result if targets are not causal**: Mutants show no germination phenotype, or show pleiotropic developmental defects that confound interpretation. [INFERRED]

**Critical caveat**: Arabidopsis results do not directly validate spinach function. Arabidopsis validation is necessary but not sufficient — spinach-specific validation (VIGS, CRISPR) is ultimately required.

**Timeline**: 12–16 weeks (seed ordering: 2–4 weeks; plant growth and seed harvest: 6–8 weeks; germination assays: 4 weeks)

**Difficulty**: Medium — Arabidopsis work is routine in most plant biology labs; mutant lines are freely available

**Priority**: **High** — provides genetic causal evidence at relatively low cost and difficulty

---

### Experiment T2.10: Virus-Induced Gene Silencing (VIGS) in Spinach for Target Validation

**Experiment**: Use VIGS to transiently silence individual target genes in spinach and assess germination phenotype of seeds from VIGS-treated plants.

**Hypothesis tested**: Does silencing of individual target genes in spinach recapitulate the germination improvement observed with exRNA treatment?

**Method**:
1. **VIGS system selection**: Tobacco rattle virus (TRV)-based VIGS is the most widely used system in Solanaceae but has been adapted to other species. For spinach, Beet necrotic yellow vein virus (BNYVV) or Beet black scorch virus (BBSV) vectors may be more appropriate given spinach's membership in Amaranthaceae [SPECULATIVE: VIGS in spinach is not well-established; this represents a significant technical development challenge]
   - Alternative: Use *Agrobacterium tumefaciens*-mediated transient expression of artificial microRNA (amiRNA) targeting the gene of interest in spinach seedlings, then assess seed quality from treated plants [SPECULATIVE: amiRNA in spinach requires optimization]
2. **Target gene fragments**: Clone 200–400 bp fragments of each target gene (avoiding conserved domains to prevent off-target silencing) into the VIGS vector
3. **Agroinfiltration**: Infiltrate spinach seedlings (3–4 leaf stage) with *Agrobacterium* carrying VIGS constructs; include: (a) empty vector control; (b) *PDS* (phytoene desaturase) positive control (photobleaching confirms VIGS efficiency)
4. **Seed harvest**: Allow VIGS-treated plants to flower and set seed; harvest mature seeds
5. **Germination assay**: Standard protocol on seeds from VIGS-treated plants vs. empty vector controls

**Expected result if targets are causal**: Seeds from plants with VIGS-mediated silencing of target genes show improved germination rate compared to empty vector control seeds. [INFERRED — note: VIGS in maternal plant may not directly affect seed gene expression; this is a significant caveat]

**Expected result if VIGS is not effective in spinach**: Photobleaching control (*PDS*) fails to show bleaching, indicating VIGS system is not functional. In this case, CRISPR-Cas9 editing must be pursued instead. [INFERRED]

**Critical caveat**: VIGS in the maternal plant silences gene expression in vegetative tissue; whether this affects seed gene expression depends on whether the target gene is expressed in the maternal seed coat vs. the embryo. For embryo-expressed targets, VIGS in the maternal plant may be insufficient — direct embryo transformation or CRISPR editing would be required. [KNOWN: VIGS limitations in seed tissue are well-documented]

**Timeline**: 20–24 weeks (VIGS system optimization: 8 weeks; plant growth and seed set: 12–16 weeks)

**Difficulty**: Very High — VIGS in spinach is not established; significant method development required

**Priority**: **Medium** — important for causal validation but technically challenging; pursue in parallel with Arabidopsis mutant work (T2.9)

---

## Tier 3: Mechanistic Studies — Pathway-Level Experiments

*These experiments assume Tier 1 and Tier 2 have confirmed that: (a) the RNA component contributes to the phenotype beyond EPS osmopriming; (b) at least 3–5 target mRNAs are specifically downregulated in exRNA-treated seeds; and (c) at least one target shows causal evidence (pharmacological or genetic) for its role in germination improvement. Tier 3 experiments dissect the mechanistic pathways in depth.*

---

### Experiment T3.1: Transcriptome-Wide Response — RNA-seq Time Course

**Experiment**: Characterize the full transcriptome response to exRNA treatment across the germination time course to identify all pathway changes and their temporal ordering.

**Hypothesis tested**: Does exRNA treatment cause a coherent, temporally ordered transcriptome reprogramming consistent with the predicted causal models, and can we distinguish exRNA-specific effects from osmotic priming effects at the transcriptome level?

**Method**:
1. **Experimental design**: Groups A (intact EPS), B (RNA-depleted EPS), C (water), D (PEG osmotic equivalent); time points: 0h, 12h, 24h, 48h, 72h; n=4 biological replicates per group per time point; embryo tissue only (dissected from pericarp)
2. **RNA-seq**: Total RNA, rRNA depletion (plant rRNA depletion kit — do NOT use poly-A selection, as many regulatory RNAs are not polyadenylated), Illumina NovaSeq 6000, minimum 30 million paired-end reads per sample (150 bp PE)
3. **Bioinformatics pipeline**:
   - Quality control: FastQC, Trimmomatic
   - Alignment: STAR to SOV genome (most current assembly)
   - Quantification: featureCounts or Salmon
   - Differential expression: DESeq2 (Group A vs. B at each time point — this is the critical comparison); FDR < 0.05, |log₂FC| > 1
   - **Key analysis**: Identify genes that are differentially expressed in A vs. B but NOT in A vs. D (i.e., exRNA-specific effects not explained by osmotic priming)
   - Gene ontology enrichment: topGO or clusterProfiler
   - Weighted gene co-expression network analysis (WGCNA): identify co-expression modules associated with treatment and time
   - **Predicted target validation**: Confirm that the 10 RT-qPCR targets from T2.1 are differentially expressed in RNA-seq data (cross-validation)

4. **Temporal ordering analysis**:
   - Identify "early response" genes (differentially expressed at 12h) vs. "late response" genes (differentially expressed at 48–72h)
   - Test whether early response genes are enriched for epigenetic regulators (consistent with Model 1) or hormone signaling genes (consistent with Model 2) or immune suppressors (consistent with Model 3)
   - This temporal ordering test directly discriminates between the three causal models

**Expected result if Epigenetic Master Switch Model (Model 1) is correct**: Epigenetic regulators (HIRA, SUVR5, DNA methyltransferase) are among the earliest downregulated genes (12h); downstream hormone signaling and cell wall genes are differentially expressed later (24–48h). [INFERRED from Model 1 causal chain]

**Expected result if Hormone Signaling Convergence Model (Model 2) is correct**: Hormone signaling genes (ethylene receptor, ABA pathway components) are among the earliest differentially expressed genes; epigenetic changes are secondary. [INFERRED from Model 2]

**Expected result if Immune Suppression Model (Model 3) is correct**: Defense-related genes are among the earliest downregulated; growth-promoting genes are upregulated later as resources are reallocated. [INFERRED from Model 3]

**Expected result if exRNA mechanism is absent**: No significant difference between Groups A and B at any time point. All transcriptome differences between A and C are replicated by D (osmotic equivalent). [INFERRED]

**Timeline**: 16–20 weeks (experiment: 6 weeks; sequencing: 2–3 weeks; bioinformatics: 8–10 weeks)

**Difficulty**: Very High — large experimental design (80 samples minimum); bioinformatics requires significant computational resources and expertise; spinach genome annotation quality limits functional interpretation

**Priority**: **High** — provides the most comprehensive mechanistic picture; also serves as a discovery platform for additional targets

---

### Experiment T3.2: Hormone Profiling — ABA/GA/Ethylene Dynamics

**Experiment**: Quantify key germination hormones (ABA, GA₁, GA₄, ACC/ethylene, IAA) across the germination time course in treated vs. control seeds.

**Hypothesis tested**: Does exRNA treatment alter the ABA/GA ratio and ethylene production in a manner consistent with the predicted hormonal convergence model, and is this alteration exRNA-specific or explainable by osmotic priming?

**Method**:
1. **Hormone extraction**: Embryo tissue from Groups A, B, C, D at 0h, 12h, 24h, 48h, 72h (n=5 biological replicates, minimum 200 mg FW per sample — pool 20 embryos per sample)
2. **LC-MS/MS quantification**:
   - ABA, ABA-GE (ABA glucose ester, inactive conjugate), PA (phaseic acid, ABA catabolite): use deuterated internal standards (d₆-ABA, d₅-PA)
   - GA₁, GA₃, GA₄, GA₇, GA₂₀: use ¹³C-labeled GA internal standards
   - IAA, IAA-Asp, IAA-Glu: use d₅-IAA internal standard
   - ACC (ethylene precursor): use d₄-ACC internal standard
   - Method: reverse-phase C18 column, ESI negative mode for ABA/GAs/IAA; positive mode for ACC
3. **Ethylene emission measurement**:
   - Seal seeds in gas-tight vials (1 mL headspace per seed)
   - Measure ethylene by GC-FID or GC-MS at 24h, 48h, 72h
   - Minimum 10 seeds per vial, n=5 replicates

**Expected result if hormone model is correct**: ABA levels decrease more rapidly in Group A vs. Group B and C. GA levels increase more rapidly in Group A. Ethylene emission is higher in Group A (consistent with ethylene receptor downregulation → enhanced ethylene signaling → increased ethylene biosynthesis feedback). [INFERRED from hormone-dormancy models; KNOWN: ABA/GA ratio determines dormancy depth in seeds; Finkelstein et al., 2008]

**Expected result if osmopriming explains hormone changes**: Hormone profiles of Group A and Group D (PEG osmotic equivalent) are not significantly different. [KNOWN: osmopriming alters ABA/GA ratio; Chen & Arora, 2013]

**Timeline**: 10–12 weeks

**Difficulty**: High — LC-MS/MS for plant hormones requires specialized expertise and equipment; hormone levels in spinach seeds are very low (fmol/mg FW range)

**Priority**: **High**

---

### Experiment T3.3: Proteomics — Confirming mRNA-to-Protein Translation

**Experiment**: Determine whether target mRNA downregulation translates to reduced protein levels, confirming that exRNA-mediated silencing affects protein abundance and not merely transcript levels.

**Hypothesis tested**: Are the predicted target proteins reduced in abundance in exRNA-treated seeds, confirming that mRNA downregulation has functional consequences at the protein level?

**Rationale**: [KNOWN] mRNA levels do not always predict protein levels, particularly in seeds where translational control is a major regulatory mechanism. Seeds contain stored mRNAs that are translationally repressed during dormancy and activated during imbibition. exRNA-mediated target mRNA reduction may not affect protein levels if the target protein is already translated from stored mRNA pools or has a long half-life. [KNOWN: translational control in seeds; Layat et al., 2014]

**Method**:
1. **Protein extraction**: Embryo tissue from Groups A and B at 24h, 48h, 72h (n=4 biological replicates, minimum 100 mg FW per sample)
2. **Quantitative proteomics (TMT-labeling or LFQ)**:
   - TMT 10-plex or 16-plex labeling for multiplexed quantification
   - LC-MS/MS on Orbitrap instrument (Thermo Q Exactive HF or equivalent)
   - Minimum 5,000 proteins quantified per sample
   - Database search against SOV proteome (translated from genome annotation)
   - Differential protein abundance: MSstats or Perseus; FDR < 0.05, |log₂FC| > 0.5

3. **Targeted proteomics (PRM — parallel reaction monitoring)** for top 10 targets:
   - Design PRM assays for each target protein (identify 2–3 proteotypic peptides per protein)
   - Quantify target protein abundance with high sensitivity and specificity
   - Use isotope-labeled synthetic peptides as internal standards for absolute quantification

4. **Polysome profiling** [optional but highly informative]:
   - Separate polysomes from monosomes by sucrose gradient centrifugation
   - Quantify target mRNAs in polysome vs. monosome fractions by RT-qPCR
   - Determine whether exRNA treatment affects translational efficiency (polysome association) of target mRNAs, not just mRNA abundance [KNOWN: translational repression is a major RNAi mechanism in addition to mRNA cleavage]

**Expected result if exRNA mechanism is real**: Target proteins are reduced in abundance in Group A vs. Group B at 48–72h (protein turnover is slower than mRNA turnover, so protein changes lag behind mRNA changes). Polysome profiling shows reduced polysome association of target mRNAs in Group A. [INFERRED]

**Expected result if translational control overrides mRNA changes**: Target mRNA levels are reduced in Group A vs. Group B (confirmed by T2.1), but protein levels are not significantly different (because the protein is translated from stored mRNA pools or has a long half-life). In this case, the functional significance of mRNA downregulation is uncertain. [INFERRED]

**Timeline**: 12–16 weeks

**Difficulty**: Very High — quantitative proteomics from seed tissue is technically demanding; spinach proteome database is incomplete; PRM assay development requires significant time

**Priority**: **Medium-High** — important for confirming functional consequences of mRNA downregulation

---

### Experiment T3.4: Reactive Oxygen Species (ROS) Dynamics and Redox State

**Experiment**: Characterize ROS dynamics in treated seeds to determine whether exRNA treatment modulates the oxidative burst associated with germination and whether this is exRNA-specific or osmopriming-associated.

**Hypothesis tested**: Does exRNA treatment alter the timing and magnitude of the germination-associated ROS burst in a manner consistent with specific target downregulation (e.g., RBOH/NADPH oxidase regulation) rather than non-specific osmotic priming?

**Method**:
1. **In vivo ROS imaging**:
   - Stain seeds with H₂DCFDA (2',7'-dichlorodihydrofluorescein diacetate, general ROS indicator) or OxyBurst Green H₂HFF BSA (extracellular H₂O₂)
   - Confocal microscopy of embryo sections at 12h, 24h, 48h
   - Quantify fluorescence intensity in radicle tip, endosperm cap, and cotyledon regions separately

2. **Biochemical ROS quantification**:
   - H₂O₂: Amplex Red assay (Thermo Fisher) — fluorometric, highly sensitive
   - Superoxide: NBT (nitroblue tetrazolium) reduction assay
   - Lipid peroxidation: TBARS (thiobarbituric acid reactive substances) assay as marker of oxidative damage

3. **Antioxidant enzyme activities**:
   - APX (ascorbate peroxidase), CAT (catalase), SOD (superoxide dismutase), GR (glutathione reductase) — spectrophotometric enzyme assays
   - Compare between Groups A, B, C, D

4. **Glutathione and ascorbate redox state**:
   - Measure GSH/GSSG ratio and AsA/DHA ratio by HPLC or enzymatic cycling assay
   - These ratios are sensitive indicators of cellular redox state and are known to change during germination [KNOWN: redox regulation of germination; Kranner et al., 2010]

**Expected result if exRNA treatment specifically modulates ROS**: ROS dynamics in Group A differ from Group B in timing or magnitude. The germination-associated H₂O₂ burst (known to promote cell wall loosening and radicle emergence) occurs earlier or at higher magnitude in Group A. [INFERRED from ROS-germination literature; KNOWN: H₂O₂ promotes germination; Müller et al., 2009]

**Expected result if ROS changes are osmopriming-associated**: ROS dynamics in Groups A and D (PEG osmotic equivalent) are not significantly different. [KNOWN: osmopriming activates antioxidant systems; Wojtyla et al., 2016]

**Timeline**: 8–10 weeks

**Difficulty**: Medium — ROS assays are routine; confocal imaging requires access to microscope and image analysis software

**Priority**: **Medium**

---

### Experiment T3.5: Cell Wall Remodeling — Mechanical and Biochemical Analysis

**Experiment**: Characterize cell wall composition and mechanical properties of the endosperm cap and radicle tip in treated seeds to validate cell wall loosening as a downstream consequence of exRNA treatment.

**Hypothesis tested**: Does exRNA treatment accelerate endosperm cap weakening and radicle cell wall loosening, and is this effect consistent with specific target downregulation (e.g., expansin inhibitors, XTH regulators) rather than osmotic effects?

**Method**:
1. **Endosperm cap puncture force measurement**:
   - Texture analyzer with spherical probe (1 mm diameter)
   - Measure force required to puncture endosperm cap at 24h, 48h, 72h post-treatment
   - Groups A, B, C, D; n=20 seeds per group per time point
   - [KNOWN: endosperm cap weakening is a key step in spinach germination; Bradford et al., 2000]

2. **Cell wall composition analysis**:
   - Alcohol-insoluble residue (AIR) preparation from endosperm cap tissue
   - Monosaccharide composition by GC-MS after acid hydrolysis (TFA) and alditol acetate derivatization
   - Quantify: glucose (cellulose/mixed-linkage glucan), xylose (xylan), mannose (glucomannan), galactose (pectin), uronic acids (pectin)
   - Cellulose content: Updegraff method

3. **Expansin and XTH activity assays**:
   - Expansin activity: paper extension assay (measure extension of filter paper strips in the presence of cell wall extracts under acidic pH) [KNOWN: expansin activity assay; McQueen-Mason et al., 1992]
   - XTH (xyloglucan endotransglucosylase/hydrolase) activity: fluorescent XTH substrate assay

4. **Immunolocalization**:
   - Antibodies against: esterified pectin (JIM7), de-esterified pectin (JIM5), xyloglucan (LM15), extensin (JIM11)
   - Confocal microscopy of embryo sections at 24h and 48h
   - Quantify epitope abundance in endosperm cap vs. radicle tip regions

**Expected result if cell wall loosening is a downstream consequence**: Endosperm cap puncture force is reduced more rapidly in Group A vs. Group B. Cell wall composition shows earlier pectin de-esterification and xyloglucan modification in Group A. Expansin activity is higher in Group A. [INFERRED from cell wall-germination literature; KNOWN: endosperm cap weakening requires expansins and XTHs in Arabidopsis; Müller et al., 2013]

**Timeline**: 10–12 weeks

**Difficulty**: High — texture analysis is straightforward; cell wall composition analysis and immunolocalization require specialized expertise

**Priority**: **Medium**

---

## Tier 4: Advanced and Translational Studies

*These experiments assume Tier 1–3 have confirmed the exRNA mechanism, identified the primary causal targets, and characterized the mechanistic pathway. Tier 4 experiments optimize the system for agricultural application, assess safety, and test generalizability.*

---

### Experiment T4.1: Field Trial — Germination and Stand Establishment Under Commercial Conditions

**Experiment**: Evaluate exRNA treatment efficacy under commercial spinach production conditions across multiple environments, seasons, and seed lots.

**Hypothesis tested**: Does the exRNA treatment improve germination rate, germination uniformity