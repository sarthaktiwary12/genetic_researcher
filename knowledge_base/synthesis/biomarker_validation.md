# UNIVERSAL BIOMARKER PANEL AND CROSS-CROP VALIDATION ROADMAP

## For Bacterial exRNA/EPS-Mediated Germination Enhancement

**Date**: 2026-02-17
**Crops analyzed**: Spinach, Broccoli, Maize, Wheat, Quinoa, Soybean
**Purpose**: Design a universal biomarker panel and validation strategy to (1) determine whether RNA or EPS drives the germination phenotype, (2) identify conserved molecular mechanisms across crops, and (3) establish a publication-grade evidence package.

---

## A. UNIVERSAL BIOMARKER PANEL (14 Genes)

### Category 1: RNA-SPECIFIC MARKERS (4 genes)

These markers should change ONLY if exogenous RNA is the active agent causing sequence-specific silencing. They are direct targets of the predicted bacterial sRNAs and would NOT be affected by osmopriming alone.

---

**1. ABI3/VP1-family ABA-responsive transcription factor**

- **Function**: Master B3-domain transcription factor controlling seed maturation and dormancy maintenance; directly regulates ABA-responsive gene expression including alpha-amylase repression
- **Why universal**: Targeted in spinach (MYB/NAC TFs SOV1g020340.1, SOV2g014810.1 executing ABA programs), maize (ABI40/Zm00001eb197370, score 10/10, VP1-null = vivipary), and functionally central to the ABA/GA switch in all 6 crops. The ABI3/VP1 pathway is the most conserved dormancy regulator across angiosperms.
- **Predicted direction**:
  - RNA model: DOWN (2-5 fold at 12-24h post-imbibition; sequence-specific sRNA-mediated silencing)
  - EPS model: UNCHANGED or mildly down (indirect effect of improved hydration on ABA catabolism, not target-specific)
- **Specific gene IDs per crop**:
  - Spinach: SOV1g020340.1 (MYB TF), SOV2g014810.1 (NAC domain protein) -- downstream ABA executors
  - Broccoli: Bo7g114200.1 (ARF repressor-type, activates ABI3)
  - Maize: Zm00001eb197370 (ABI40/VP1-like) -- HIGHEST PRIORITY
  - Wheat: TraesCS7D02G384400 (SnRK2, phosphorylates ABI5/ABF), TraesCS5B02G275200 (NAC38)
  - Quinoa: Not directly targeted; monitor CqSnRK2.12 (Zhu et al. 2022)
  - Soybean: GLYMA_01G215100 (PLDbeta1, ABA signal amplifier)
- **RT-qPCR primer design notes**: Target the conserved B3 DNA-binding domain (exons 4-6 in most species). Use species-specific 3' UTR primers to distinguish homeologs in polyploids. For wheat, design homeolog-specific primers using A/B/D SNPs. Amplicon size 100-200 bp. Avoid regions with predicted sRNA binding sites (these may be degraded).

---

**2. DNA methyltransferase / Methylation reader (epigenetic silencing machinery)**

- **Function**: Establishes or reads repressive DNA methylation marks (5mC) at germination-promoting gene loci, maintaining dormancy through epigenetic silencing
- **Why universal**: Targeted in spinach (SOV1g033340.1, DNA cytosine-5-methyltransferase), broccoli (Bo8g066360.1, MBD10 methylation reader; Bo8g102500.1, RDR for RdDM pathway), and wheat (TraesCS7A02G074600, DDM1 chromatin remodeler). Epigenetic reprogramming during germination is universal across angiosperms (Kawakatsu et al. 2017). The methylation-dormancy axis is conserved.
- **Predicted direction**:
  - RNA model: DOWN (sequence-specific silencing of methyltransferase/reader transcripts)
  - EPS model: UNCHANGED (osmopriming does not target specific epigenetic regulators)
- **Specific gene IDs per crop**:
  - Spinach: SOV1g033340.1 (DNA cytosine-5-methyltransferase), SOV4g015450.1 (SUVR5 H3K9 methyltransferase)
  - Broccoli: Bo8g066360.1 (MBD10), Bo8g102500.1 (RDR2/6)
  - Maize: Zm00001eb136860 (MOS1-like, chromatin/immunity interface)
  - Wheat: TraesCS7A02G074600 (DDM1)
  - Quinoa: Not directly targeted; monitor via global 5mC levels (bisulfite-seq proxy)
  - Soybean: Not directly targeted; monitor via global 5mC levels
- **RT-qPCR primer design notes**: For DNA methyltransferase, target the conserved catalytic domain (motifs I, IV, VI, VIII, IX, X). For MBD10, use the methyl-CpG binding domain. For DDM1, use the SNF2 helicase domain. Species-specific primers required due to rapid 3' UTR divergence.

---

**3. Ethylene receptor / Hormone signaling node (negative regulator)**

- **Function**: Ethylene receptors are negative regulators of ethylene signaling; their downregulation creates ethylene hypersensitivity, strongly promoting germination. LOX provides JA/ABA precursors.
- **Why universal**: Targeted in spinach (SOV3g000150.1, ethylene receptor -- Rank 1 target; SOV3g035520.1, LOX), and functionally relevant in all crops (ethylene-ABA antagonism is conserved). Soybean germination involves ethylene-ROS crosstalk (Ishibashi et al. 2013). The ethylene receptor as a NEGATIVE regulator is the best-characterized pro-germination mechanism.
- **Predicted direction**:
  - RNA model: DOWN (sequence-specific silencing; loss of negative regulator = constitutive ethylene signaling)
  - EPS model: UNCHANGED or mildly UP (ethylene production may increase from priming-associated stress, but receptor levels are not specifically targeted)
- **Specific gene IDs per crop**:
  - Spinach: SOV3g000150.1 (Ethylene receptor) -- TOP TARGET
  - Broccoli: Not directly targeted; monitor BoETR1/ERS1 as reference
  - Maize: Not directly targeted; monitor ZmETR2 as reference
  - Wheat: Not directly targeted; monitor TaERS1 as reference
  - Quinoa: Not directly targeted; monitor CqETR homologs
  - Soybean: Not directly targeted; monitor GmETR1
- **RT-qPCR primer design notes**: Ethylene receptor family is highly conserved. Target the GAF domain or histidine kinase domain. For LOX, target the conserved lipoxygenase domain (PLAT + LH2). Use degenerate primers across crops for initial screening, then species-specific for validation.

---

**4. Class III Peroxidase (ROS scavenger / cell wall modifier)**

- **Function**: Dual function -- scavenges H2O2 (peroxidative cycle) and stiffens cell walls via lignification/cross-linking. Downregulation shifts the seed into the pro-germination "oxidative window" and reduces mechanical resistance to radicle emergence.
- **Why universal**: Targeted in spinach (SOV3g038840.1, peroxidase), maize (PRX91/Zm00001eb333290, score 8/10, Atprx16 knockout = earlier germination), and wheat (374 class III peroxidases, PARP-ROS connection). The oxidative window concept is universal. Class III PRX is the largest multigene family affected.
- **Predicted direction**:
  - RNA model: DOWN (sequence-specific silencing of targeted isoform)
  - EPS model: UNCHANGED at specific isoform level (total PRX activity may change from hydration effects, but not isoform-specific)
- **Specific gene IDs per crop**:
  - Spinach: SOV3g038840.1 (Peroxidase)
  - Broccoli: Not directly targeted (CRK-mediated NADPH oxidase suppression is the ROS route)
  - Maize: Zm00001eb333290 (PRX91/Peroxidase 72 precursor)
  - Wheat: TraesCS1A02G328000 (PARP -- modulates ROS indirectly via NAD+); 374 PRX genes
  - Quinoa: Not directly targeted; monitor via H2O2 quantification
  - Soybean: GLYMA_03G196400 (glutaredoxin -- related redox regulator)
- **RT-qPCR primer design notes**: Class III peroxidases are massive multigene families (119 in maize, 374 in wheat). Design isoform-specific primers using 3' UTR sequences. Include a "total PRX" primer pair targeting the conserved heme-binding domain for normalization. Amplicon 80-150 bp.

---

### Category 2: TREATMENT-RESPONSE MARKERS (4 genes)

These markers should change regardless of whether RNA or EPS drives the effect. They report on the PHYSIOLOGICAL STATE of the germinating seed -- if germination is accelerated by any mechanism, these genes will respond.

---

**5. Alpha-amylase (reserve mobilization marker)**

- **Function**: Hydrolyzes starch in the endosperm/perisperm to provide sugars for embryonic axis growth. GA-induced, ABA-repressed. The canonical readout of germination commitment.
- **Why universal**: Alpha-amylase induction is the single most conserved germination marker across all angiosperms. In maize, aleurone alpha-amylase is GA-responsive via GAMYB (Gubler et al. 1995). In wheat, alpha-amylase/subtilisin inhibitor is linked to PHS resistance. In soybean, invertase rather than amylase is rate-limiting (Kuo et al. 1990), but amylase still increases.
- **Predicted direction**:
  - RNA model: UP (3-10 fold by 24-48h; derepressed by ABI3/VP1 silencing)
  - EPS model: UP (1.5-3 fold; earlier metabolic activation from priming)
  - Key discriminator: MAGNITUDE and TIMING of induction, not direction
- **Specific gene IDs per crop**:
  - Spinach: Use SpAMY1 (high-pI alpha-amylase homolog)
  - Broccoli: Use BoAMY1 (Arabidopsis AMY1/AT1G69830 ortholog)
  - Maize: ZmAMY3 (aleurone-specific GA-responsive isoform)
  - Wheat: TaAMY1 (alpha-amylase 1, the classical wheat germination marker)
  - Quinoa: CqAMY (starch amylase for perisperm mobilization)
  - Soybean: GmINV-CWI (cell wall invertase -- the functional equivalent; GLYMA_05G068700 inhibitor is silenced)
- **RT-qPCR primer design notes**: Alpha-amylases are highly conserved. Target the catalytic domain (GH13 family). For soybean, also measure cell wall invertase activity enzymatically (DNS reducing sugar assay).

---

**6. Expansin (cell wall loosening / radicle emergence marker)**

- **Function**: Non-enzymatic cell wall loosening protein that disrupts hydrogen bonds between cellulose microfibrils and hemicellulose, enabling turgor-driven cell expansion essential for radicle protrusion
- **Why universal**: Expansins are required for radicle emergence in all species studied. GA-induced in the micropylar endosperm cap. Reported as highly expressed during germination in soybean (Sangi et al. 2019), wheat, and Arabidopsis.
- **Predicted direction**:
  - RNA model: UP (downstream of GA/ABA rebalancing; indirect consequence of defense/ABA suppression)
  - EPS model: UP (accelerated hydration activates earlier)
  - Key discriminator: Timing relative to ABA/GA changes
- **Specific gene IDs per crop**:
  - Spinach: SpEXPA (alpha-expansin homolog)
  - Broccoli: BoEXPA10 (Arabidopsis EXPA2/AT5G05290 ortholog, endosperm cap)
  - Maize: ZmEXPB1 (beta-expansin, pollen/germination-associated)
  - Wheat: TaEXPA6 (EXPA family, radicle-expressed)
  - Quinoa: CqEXPA (micropylar endosperm cap expressed)
  - Soybean: GmEXPA (embryonic axis expressed; Sangi et al. 2019)
- **RT-qPCR primer design notes**: Use DPBB_1 domain for universal primers. Alpha-expansins (EXPA) are more relevant for germination than beta-expansins in most dicots; beta-expansins dominate in grasses. Species-specific isoform selection critical.

---

**7. GA3ox / GA20ox (GA biosynthesis marker)**

- **Function**: Rate-limiting enzymes in gibberellin biosynthesis. GA3ox converts GA20 to bioactive GA1; GA20ox converts GA12/GA53 to GA20. Their induction signals the shift from ABA-dominated dormancy to GA-dominated germination.
- **Why universal**: GA biosynthesis activation is the most fundamental hormonal switch in germination across all 6 crops. ABA catabolism (CYP707A) is the reciprocal marker. If the exRNA treatment shifts the ABA/GA ratio, GA biosynthesis genes MUST increase.
- **Predicted direction**:
  - RNA model: UP (2-5 fold; consequence of epigenetic derepression and ABA pathway suppression)
  - EPS model: UP (1.5-2 fold; priming pre-activates GA pathway)
- **Specific gene IDs per crop**:
  - Spinach: SpGA3ox1 (ortholog of AtGA3ox1/AT1G15550)
  - Broccoli: BoGA3ox1 (close Arabidopsis ortholog)
  - Maize: ZmGA3ox2 (known d1/dwarf1 gene family)
  - Wheat: TaGA3ox2 (linked to Rht semi-dwarfing alleles)
  - Quinoa: CqGA3ox (Chen et al. 2024, CqGAox family)
  - Soybean: GmGA3ox (Gazara et al. 2019)
- **RT-qPCR primer design notes**: 2-oxoglutarate-dependent dioxygenase domain is conserved. Target the Fe(II)/2-OG binding pocket region. Distinguish GA3ox from GA20ox using C-terminal divergence.

---

**8. CYP707A (ABA catabolism marker)**

- **Function**: ABA 8'-hydroxylase (cytochrome P450) that catalyzes the first committed step of ABA catabolism. Its induction marks the irreversible commitment to germination by destroying the dormancy-maintaining hormone.
- **Why universal**: CYP707A induction is the single best indicator that the ABA/GA balance has shifted toward germination. Documented as rate-limiting for dormancy release in Arabidopsis, barley, wheat, and rice.
- **Predicted direction**:
  - RNA model: UP (3-8 fold; derepressed by epigenetic changes and reduced ABI3/VP1 signaling)
  - EPS model: UP (1.5-3 fold; hydration-triggered ABA catabolism)
- **Specific gene IDs per crop**:
  - Spinach: SpCYP707A (ortholog of AtCYP707A2)
  - Broccoli: BoCYP707A2 (Arabidopsis ortholog AT2G29090)
  - Maize: ZmCYP707A (ABA 8'-hydroxylase family)
  - Wheat: TaCYP707A1 (the critical after-ripening responsive gene; Barrero et al. 2013)
  - Quinoa: CqCYP707A (inferred from expanded ABA gene families; Jarvis et al. 2017)
  - Soybean: GmCYP707A (Shuai et al. 2017)
- **RT-qPCR primer design notes**: Highly conserved CYP450 family. Use the oxygen-binding domain and heme-binding motif (FXXGXRXCXG) for universal primers. Species-specific primers using 3' UTR.

---

### Category 3: NEGATIVE CONTROLS (3 genes)

These genes should NOT change in either model. If they do change, it indicates non-specific effects, RNA degradation artifacts, or off-target phenomena.

---

**9. Rubisco large subunit (rbcL) -- chloroplast-encoded**

- **Function**: Ribulose-1,5-bisphosphate carboxylase/oxygenase, the most abundant protein on Earth. Chloroplast-encoded (not nuclear), photosynthesis-specific, not expressed during the dark heterotrophic phase of germination.
- **Why negative control**: (1) Chloroplast-encoded genes are NOT susceptible to nuclear AGO-mediated RNAi; (2) Not expressed during early germination (dark phase); (3) Not predicted as a target in any crop. Any change would indicate non-specific transcriptional disruption or contamination.
- **Predicted direction**:
  - RNA model: NO CHANGE
  - EPS model: NO CHANGE
- **Specific gene IDs**: Chloroplast genome-encoded in all 6 crops; use species-specific rbcL primers
- **RT-qPCR primer design notes**: Universal primers available; amplicon within the highly conserved catalytic domain. Include as a negative control for nuclear gene expression normalization.

---

**10. Histone H4 (constitutive chromatin structural protein)**

- **Function**: Core histone protein. Constitutively expressed and among the most conserved proteins in eukaryotes. Not predicted as a target in any crop.
- **Why negative control**: (1) Extremely conserved and constitutively expressed; (2) Multiple gene copies ensure stable expression; (3) Not a predicted sRNA target; (4) Required at constant levels during DNA replication in germination. Any change would indicate global transcriptional disruption.
- **Predicted direction**:
  - RNA model: NO CHANGE
  - EPS model: NO CHANGE
- **Specific gene IDs**: Multiple copies in all species; use consensus H4 primers
- **RT-qPCR primer design notes**: Histone H4 is 92-95% identical across all plants. Universal primers targeting the core domain work across all 6 crops. Amplicon 100-120 bp.

---

**11. 18S ribosomal RNA**

- **Function**: Structural component of the small (40S) ribosomal subunit. Constitutively transcribed by RNA Polymerase I at levels proportional to translational demand.
- **Why negative control**: (1) Transcribed by Pol I, not Pol II (sRNA-mediated silencing targets Pol II transcripts via AGO); (2) Not susceptible to RISC-mediated cleavage; (3) Extremely stable (half-life > 5 days). Any change would indicate massive cellular disruption.
- **Predicted direction**:
  - RNA model: NO CHANGE
  - EPS model: NO CHANGE
- **RT-qPCR primer design notes**: Universal 18S primers well-established. Use as a normalizer only for total RNA content quality check, NOT as primary reference gene (expression levels too high, creating Ct value mismatch with target genes).

---

### Category 4: HOUSEKEEPING NORMALIZERS (2 genes)

---

**12. Actin (ACT)**

- **Function**: Cytoskeletal structural protein with stable expression across germination stages
- **Validated in**: Maize (ZmActin), wheat (TaActin), soybean (GmActin), broccoli (BoActin)
- **RT-qPCR primer design notes**: Use ACT2/ACT8 orthologs. Amplicon 100-150 bp. Verify stability across treatment conditions using geNorm (Vandesompele et al. 2002) and NormFinder (Andersen et al. 2004) with minimum 3 candidate reference genes.

---

**13. Ubiquitin (UBQ)**

- **Function**: Ubiquitin conjugating protein with constitutive expression
- **Validated in**: All 6 crops have characterized UBQ reference genes
- **RT-qPCR primer design notes**: UBQ10 orthologs recommended. Design primers spanning an intron to exclude genomic DNA contamination. Validate alongside ACT and EF1-alpha; select the two most stable for delta-delta-Ct normalization.

---

**14. Elongation Factor 1-alpha (EF1a) -- backup normalizer**

- **Function**: Translation elongation factor; highly stable across developmental stages
- **Validated in**: Maize (ZmEF1a), wheat (TaEF1a), soybean (GmEF1a)
- **RT-qPCR primer design notes**: Highly conserved across eukaryotes. Use the GTP-binding domain region. Include as the third candidate reference gene for geNorm validation; use the best two of three (ACT, UBQ, EF1a) for final normalization.

---

### SUMMARY TABLE: Universal Biomarker Panel

| # | Gene Family | Category | Crops Directly Targeted | RNA Model | EPS Model | Key Discriminator |
|---|------------|----------|------------------------|-----------|-----------|-------------------|
| 1 | ABI3/VP1/SnRK2 (ABA TF axis) | RNA-specific | Spinach, Maize, Wheat, Soybean | DOWN 2-5x | No change | Target-specific downregulation |
| 2 | DNA methyltransferase/MBD/DDM1 | RNA-specific | Spinach, Broccoli, Wheat | DOWN 2-5x | No change | Epigenetic machinery suppression |
| 3 | Ethylene receptor/LOX | RNA-specific | Spinach | DOWN 2-5x | No change | Specific isoform silencing |
| 4 | Class III Peroxidase | RNA-specific | Spinach, Maize | DOWN 2-5x | No change | Isoform-specific change |
| 5 | Alpha-amylase/Invertase | Treatment-response | All 6 (indirect) | UP 3-10x | UP 1.5-3x | Magnitude difference |
| 6 | Expansin | Treatment-response | All 6 (indirect) | UP 2-5x | UP 1-2x | Timing difference |
| 7 | GA3ox/GA20ox | Treatment-response | All 6 (indirect) | UP 2-5x | UP 1.5-2x | Magnitude difference |
| 8 | CYP707A (ABA catabolism) | Treatment-response | All 6 (indirect) | UP 3-8x | UP 1.5-3x | Magnitude and timing |
| 9 | rbcL (chloroplast) | Negative control | None | No change | No change | Any change = artifact |
| 10 | Histone H4 | Negative control | None | No change | No change | Any change = artifact |
| 11 | 18S rRNA | Negative control | None | No change | No change | Any change = artifact |
| 12 | Actin | Normalizer | None | Stable | Stable | Reference gene |
| 13 | Ubiquitin | Normalizer | None | Stable | Stable | Reference gene |
| 14 | EF1-alpha | Normalizer (backup) | None | Stable | Stable | Reference gene |

---

## B. MINIMAL VALIDATION ROADMAP

### Tier 1: Go/No-Go Decision (1 crop, 4 weeks, <$2,000)

**Objective**: Determine whether RNA is the active agent or EPS osmopriming explains the phenotype. This is the single most important experiment in the entire program.

**Crop**: Maize (B73 inbred) -- chosen for genomic resources, fast germination (48-72h), large seeds (easy manipulation), established cross-kingdom RNAi precedents (Koch et al. 2016 SIGS)

**Experiment 1.1: RNase Elimination ("The Killer Experiment")**
- Cost: ~$300
- Timeline: Week 1-2
- Design: 4 treatments x 4 biological replicates x 50 seeds each = 800 seeds
  - (A) Intact M-9 EPS (positive control)
  - (B) M-9 + RNase A (100 ug/mL, 37C, 1h; destroys RNA)
  - (C) M-9 + heat-inactivated RNase A (65C, 20 min; controls for buffer/protein effects)
  - (D) Water only (negative control)
- Readouts: Germination % at 24, 48, 72, 96h; T50 (time to 50% germination); radicle length at 72h; seedling fresh weight at 7 days
- Decision matrix:
  - If A >> B and B = D: RNA IS essential. PROCEED to Tier 2.
  - If A = B = C >> D: RNA is NOT essential; EPS is sufficient. PIVOT to EPS mechanism study.
  - If A > B > D: Partial RNA contribution + EPS contribution. PROCEED with modified Tier 2 accounting for combined model.
  - If A = B = C = D: No treatment effect. RE-EVALUATE the entire pipeline.
- Statistical analysis: Two-way ANOVA with Tukey HSD post-hoc; alpha = 0.05; power analysis indicates n=4 replicates sufficient for detecting 15% germination rate difference

**Experiment 1.2: RT-qPCR on Top 5 Biomarkers**
- Cost: ~$800
- Timeline: Week 2-3
- Targets: From the Universal Panel, measure in B73 maize:
  1. ABI40/VP1 (Zm00001eb197370) -- RNA-specific marker
  2. PRX91 (Zm00001eb333290) -- RNA-specific marker
  3. ZmAMY3 (alpha-amylase) -- Treatment-response marker
  4. ZmGA3ox2 (GA biosynthesis) -- Treatment-response marker
  5. ZmActin + ZmUBQ + ZmEF1a (normalizers; select best 2 by geNorm)
- Plus: Histone H4 (negative control)
- Timepoints: 0, 6, 12, 24, 48h post-imbibition
- Treatments: EPS-treated vs. water control (minimum); ideally also RNase-treated EPS
- Analysis: 2^(-delta-delta-Ct) method; geNorm validation of reference genes
- Decision: If RNA-specific markers show 2-fold or greater target-specific downregulation at 12-24h in treated vs. control, and negative controls are stable, this is strong evidence for RNA-mediated silencing

**Experiment 1.3: ABA/GA Hormone Quantification**
- Cost: ~$800
- Timeline: Week 3-4
- Method: LC-MS/MS (outsource to specialized facility if no in-house capability)
- Analytes: ABA, GA1, GA4, (optional: JA, SA, IAA)
- Tissue: Embryo axes, dissected from endosperm at 0, 6, 12, 24h
- Treatments: EPS-treated vs. water control
- Decision: If ABA is significantly lower and/or GA significantly higher in treated embryos at 12-24h, the hormonal mechanism is confirmed (regardless of whether RNA or EPS drives it)

**Tier 1 Total Cost**: ~$1,900
**Tier 1 Total Time**: 4 weeks
**Tier 1 Deliverable**: Go/no-go decision on RNA hypothesis with supporting hormone and gene expression data

---

### Tier 2: Mechanistic Confirmation (2 crops, 8 weeks, <$8,000)

**Objective**: Establish whether bacterial sRNAs physically enter plant cells, are loaded into AGO complexes, and direct target-specific mRNA cleavage.

**Crops**: Maize (B73) + Soybean (Williams 82) -- soybean chosen because of the Ren et al. (2019) Science precedent showing bacterial tRNA fragments → soybean AGO1-dependent silencing

**Experiment 2.1: Degradome/PARE Sequencing**
- Cost: ~$3,000 (2 crops x 2 conditions x 1 timepoint)
- Timeline: Week 1-4
- Method: Parallel Analysis of RNA Ends (PARE-seq; German et al. 2008) on treated vs. control seeds at 24h
- Expectation: If RNA model is correct, PARE-seq will reveal enriched cleavage signatures at the predicted sRNA binding sites on target mRNAs, producing the characteristic "cleavage peak" between positions 10-11 of the sRNA:mRNA duplex
- Analysis: T-plot analysis; p-value for enrichment of cleavage at predicted sites
- This is the GOLD STANDARD evidence for sRNA-guided mRNA cleavage

**Experiment 2.2: sRNA-seq of EPS Solution**
- Cost: ~$1,500 (library prep + sequencing)
- Timeline: Week 1-3
- Method: Small RNA extraction from M-9 EPS solution; size-select 18-30 nt; library prep; Illumina sequencing
- Expectation: Identify bacterial-origin sRNAs with antisense complementarity to plant targets
- Analysis: Map reads to bacterial genome(s); identify sRNAs with 18-24 nt complementarity to predicted plant targets; compute thermodynamic stability (delta-G) of sRNA:mRNA duplexes
- Critical control: Also sequence RNase-treated EPS (should show complete RNA degradation)

**Experiment 2.3: AGO Co-Immunoprecipitation (AGO-RIP)**
- Cost: ~$2,000
- Timeline: Week 4-8
- Method: Anti-AGO1 (or pan-AGO) immunoprecipitation from treated soybean seed protein extracts at 12h and 24h post-imbibition, followed by RNA extraction and RT-qPCR or sRNA-seq
- Expectation: Bacterial-origin sRNAs should be enriched in AGO-IP fraction from treated seeds but absent from controls
- Critical: This directly demonstrates that exogenous bacterial sRNAs are loaded into the host RNAi machinery
- Note: Anti-AtAGO1 antibodies may cross-react with GmAGO1 given >70% identity; validate by western blot first

**Experiment 2.4: Time-Course Transcriptomics (RNA-seq)**
- Cost: ~$2,500 (2 crops x 2 conditions x 3 timepoints = 12 libraries, low-depth)
- Timeline: Week 1-6
- Method: Full transcriptome RNA-seq at 6h, 12h, 24h in treated vs. control for maize and soybean
- Expectation: RNA-specific markers should show significant downregulation; treatment-response markers should show significant upregulation; negative controls should be stable
- Analysis: DESeq2; gene set enrichment analysis for defense, ABA signaling, GA signaling, and epigenetic pathways
- Bonus: Global transcriptome data enables discovery of additional targets not predicted bioinformatically

**Tier 2 Total Cost**: ~$9,000 (over budget; can reduce by dropping soybean RNA-seq to $7,000)
**Tier 2 Total Time**: 8 weeks
**Tier 2 Deliverable**: Mechanistic evidence package: (1) cleavage signatures at target sites (PARE), (2) bacterial sRNAs in the preparation (sRNA-seq), (3) bacterial sRNAs in plant AGO (AGO-RIP), (4) global transcriptomic changes consistent with predictions

---

### Tier 3: Cross-Crop Translation (4+ crops, 16 weeks, <$25,000)

**Objective**: Determine whether the mechanism is universal or species-specific. Apply the 14-gene biomarker panel across all 6 crops.

**Experiment 3.1: Universal Biomarker Panel Application**
- Cost: ~$6,000 (6 crops x 14 genes x 3 timepoints x 2 conditions; bulk RT-qPCR plates)
- Timeline: Week 1-6
- Method: RT-qPCR panel on all 6 crops at 6h, 12h, 24h post-imbibition; treated vs. control
- Analysis: Cross-crop heatmap of fold changes; hierarchical clustering to identify conserved vs. species-specific responses
- Deliverable: Definitive answer on which pathways are universally affected and which are crop-specific

**Experiment 3.2: Dose-Response Curves**
- Cost: ~$3,000
- Timeline: Week 4-10
- Method: Test 5 EPS concentrations (0.25x, 0.5x, 1x, 2x, 4x standard) on 3 crops (maize, soybean, spinach)
- Readouts: Germination %, T50, seedling vigor, top 5 biomarker gene expression at 24h
- Analysis: Sigmoid dose-response modeling; calculate EC50 for germination improvement and compare with EC50 for target gene silencing
- Key question: Does dose-response curve fit a saturable model (consistent with RNA mechanism) or a linear/osmotic model (consistent with EPS priming)?

**Experiment 3.3: Synthetic sRNA Mimic Experiments**
- Cost: ~$8,000
- Timeline: Week 6-14
- Method: Design 3-5 synthetic 21-nt RNA duplexes matching the top predicted bacterial sRNAs targeting:
  1. ABI40/VP1 (maize)
  2. MBD10 (broccoli)
  3. Ethylene receptor (spinach)
  4. Invertase inhibitor (soybean)
  5. SnRK2 (wheat)
- Apply synthetic dsRNAs to seeds during imbibition with a transfection agent (Mirus TransIT-X2 or similar)
- Readouts: Germination phenotype + target gene expression
- Controls: Scrambled dsRNA of same length/GC content; no-treatment; transfection agent only
- This is the SUFFICIENCY test: if synthetic sRNAs targeting these genes reproduce the germination phenotype, it confirms the RNA mechanism

**Experiment 3.4: Field Trial Design (planning only at this stage)**
- Cost: ~$5,000 (planning, materials, limited pilot)
- Timeline: Week 10-16
- Design: Small-plot randomized complete block design (RCBD) with 4 blocks
- Treatments: M-9 EPS (standard), RNase-treated EPS, water, PEG osmopriming (matched water potential)
- Crops: Maize + soybean (best-characterized targets)
- Readouts: Emergence %, days to emergence, seedling stand count, early vigor rating
- Scale: 100 seeds per plot, 4 plots per treatment per crop = 3,200 seeds
- Note: This is a PILOT field trial. Full field validation requires Tier 4.

**Tier 3 Total Cost**: ~$22,000
**Tier 3 Total Time**: 16 weeks
**Tier 3 Deliverable**: Cross-crop biomarker response matrix; dose-response data; synthetic sRNA sufficiency data; pilot field trial results

---

### Tier 4: Publication-Grade Evidence Package

**Objective**: Assemble evidence sufficient for a high-impact (Nature/Science/Cell) publication establishing bacterial exRNA-mediated cross-kingdom regulation of seed germination.

**What Nature/Science/Cell requires:**

1. **Demonstration of bacterial sRNA transfer into plant cells** (Tier 2: AGO-RIP + confocal imaging of fluorescently labeled sRNAs)
2. **Mechanism of action** (Tier 2: PARE-seq + RNA-seq + hormone quantification)
3. **Specificity** (Tier 3: RNase elimination + synthetic sRNA mimics + dose-response)
4. **Generalizability** (Tier 3: Cross-crop biomarker panel)
5. **Biological significance** (Tier 3-4: Field trials showing agronomic relevance)

**Additional experiments for publication grade:**
- **Fluorescent sRNA tracking**: Label synthetic sRNAs with Cy3/Cy5; apply to seeds; confocal microscopy at 6h, 12h, 24h to visualize uptake into seed cells. Cost: ~$5,000.
- **Arabidopsis mutant validation**: Test germination of ago1-27, dcl1-9, rdr6-15 mutants with EPS treatment (if RNA mechanism requires AGO1, these mutants should be insensitive). Cost: ~$3,000.
- **Bacterial mutant panel**: Generate M-9 bacterial strains with deletions in sRNA biogenesis genes (hfq, rne); test whether sRNA-deficient bacteria produce EPS that still improves germination. Cost: ~$15,000.
- **Full-scale field trials**: 3 locations x 2 seasons x 4 crops x 4 treatments = 96 field plots. Cost: ~$50,000.

**Statistical Framework:**
- All experiments: minimum 4 biological replicates
- Gene expression: 2^(-delta-delta-Ct) with geometric mean of 2 validated reference genes
- Germination: Generalized linear model (binomial family) for germination percentage; linear model for T50, radicle length, fresh weight
- Multiple testing correction: Benjamini-Hochberg FDR < 0.05 for transcriptomics; Bonferroni for individual gene comparisons
- Effect sizes: Report Cohen's d alongside p-values
- Pre-registration: Consider pre-registering Tier 1 experiments on OSF for credibility

**Controls Checklist:**
- [ ] Water-only negative control
- [ ] RNase-treated EPS (critical discriminator)
- [ ] Heat-inactivated RNase + EPS (RNase buffer control)
- [ ] Heat-denatured EPS (destroys RNA structure, preserves polysaccharides)
- [ ] PEG at matched water potential (osmopriming control)
- [ ] Filter-sterilized (0.22 um) EPS (removes live bacteria)
- [ ] Scrambled dsRNA + transfection agent (specificity control for synthetic sRNAs)
- [ ] Transfection agent only (vehicle control)
- [ ] Exogenous ABA (10 uM; should abolish/reduce germination benefit if ABA pathway is the target)
- [ ] Arabidopsis ago1/dcl1/rdr6 mutants (RNAi machinery requirement)
- [ ] geNorm/NormFinder validation of reference genes for EVERY crop/condition combination

---

## C. RISK ASSESSMENT TABLE

| # | Risk | Probability | Impact | Mitigation | Cost of Failure |
|---|------|-------------|--------|------------|-----------------|
| 1 | **RNA is a bystander; EPS osmopriming explains 100% of the effect** | MEDIUM-HIGH (40%) | FATAL to RNA hypothesis | RNase elimination experiment (Tier 1.1) provides definitive answer within 2 weeks for ~$300. If confirmed, pivot to EPS mechanism research, which is still publishable (novel biostimulant characterization). | $2,000 (Tier 1 costs sunk) |
| 2 | **Predicted sRNA targets are bioinformatic false positives** | MEDIUM (30%) | HIGH -- undermines all downstream analysis | RT-qPCR validation of top 5 targets (Tier 1.2); PARE-seq (Tier 2.1) provides sequence-level evidence; degradome data resolves false positives definitively. | $2,800 (Tiers 1-2 sunk up to PARE) |
| 3 | **Effect is real but species-specific (e.g., works in maize but not broccoli)** | MEDIUM (35%) | MODERATE -- limits commercial scope but still publishable | Cross-crop biomarker panel (Tier 3.1) tests all 6 crops simultaneously. Even species-specific results are publishable as "differential cross-kingdom regulatory capacity." | $10,000 (if discovered at Tier 3) |
| 4 | **AGO/RNAi pathway not active during seed imbibition** | LOW-MEDIUM (20%) | FATAL to RNA model | AGO-RIP (Tier 2.3) directly tests AGO loading. Literature supports AGO activity during imbibition (stored mRNA translation requires RISC clearance). Qin et al. (2019) showed stress-responsive AGO expression in maize. | $5,000 (Tiers 1-2 sunk) |
| 5 | **sRNAs degrade before reaching target cells** | MEDIUM (30%) | FATAL to RNA model | sRNA-seq of EPS (Tier 2.2) + sRNA-seq of treated seeds at 6h/12h shows whether sRNAs survive imbibition. EPS matrix may protect sRNAs from RNase degradation. | $3,000 |
| 6 | **Combined EPS + RNA model operates; effects are inseparable** | MEDIUM (35%) | LOW -- actually the most likely and publishable scenario | Design experiments that can detect PARTIAL RNA contributions (Tier 1.1 statistical power for 15% differences). A combined model is more biologically realistic and still novel. | Minimal; most experiments already designed for this |
| 7 | **Confounders: live bacteria (PGPR), nutrients, pH effects** | MEDIUM (25%) | MODERATE | Filter-sterilization (removes bacteria), dialysis (removes small molecules), pH-buffered controls. Cost: ~$500 in additional controls. | $1,000 |
| 8 | **Synthetic sRNA mimics fail due to delivery issues, not mechanism** | HIGH (50%) | MODERATE -- complicates sufficiency argument | Use multiple transfection methods (lipofection, electroporation, nanoparticle). Positive control: known miR160 targeting ARF10 in Arabidopsis. | $5,000 |
| 9 | **Paradoxical targets (PP2C, BOP1, profilin) contradict the model** | MEDIUM (30%) | LOW-MODERATE | These targets are already flagged in the claims analysis. If confirmed as genuine targets, they may represent bacterial manipulation (suppressing host translational capacity) rather than mutualistic germination enhancement. Report honestly. | Minimal |
| 10 | **Regulatory/IP complications prevent commercialization** | LOW (15%) | HIGH for commercial application | Early freedom-to-operate analysis. RNA-based biostimulants face evolving regulatory landscape. Seek provisional patent before publication. | Variable |

---

## D. CROSS-CROP EXPERIMENTAL PRIORITIZATION

### Ranking of 6 Crops for First Validation Experiments

| Rank | Crop | Score | Rationale |
|------|------|-------|-----------|
| **1** | **Maize (Zea mays, B73)** | 9.5/10 | **Best first crop.** Reasons: (a) Most complete RNAi machinery characterization (Qian et al. 2011; Zhai et al. 2014); (b) SIGS precedent -- spray-induced gene silencing works in maize against Fusarium (Koch et al. 2016); (c) AGO genes stress-responsive (Qin et al. 2019); (d) Highest-confidence single target (ABI40/VP1, score 10/10) with viviparous mutant phenotype providing clear positive control; (e) Fast germination (48-72h at 25-28C); (f) Large seeds (~300 mg) are easy to manipulate, dissect (embryo vs. scutellum vs. endosperm), and provide abundant tissue for molecular analysis; (g) Established inbred lines (B73, W22, Mo17) with complete genome sequences; (h) Paper towel germination assay is standardized (ISTA protocols); (i) 119 class III peroxidases and 590 RING proteins provide gene family redundancy context; (j) Paleopolyploid genome provides moderate buffering for target redundancy. |
| **2** | **Soybean (Glycine max, Wm82)** | 9.0/10 | **Best second crop for mechanistic confirmation.** Reasons: (a) THE CRITICAL PRECEDENT -- Ren et al. (2019) Science demonstrated bacterial (Bradyrhizobium) tRNA-derived sRNAs transfer to soybean and silence genes via AGO1-dependent pathway. This is the only crop where bacteria-to-host sRNA transfer has been experimentally validated; (b) Highest-confidence target for a unique mechanism (invertase inhibitor, score 10/10, validated in three species); (c) Duplicated RNAi machinery from paleopolyploidy (Liu et al. 2014); (d) Large seeds (~200 mg); (e) Moderate germination time (72-96h); (f) Nitrogen-fixing legume with pre-existing infrastructure for bacterial signal reception; (g) Isoflavonoid defense pathway provides unique metabolic marker for defense-growth tradeoff. **Limitation**: Slightly slower germination than maize; more complex seed structure. |
| **3** | **Broccoli (Brassica oleracea)** | 7.5/10 | **Best crop for Arabidopsis mutant proxy validation.** Reasons: (a) Closest relative to Arabidopsis (~15-20 Mya divergence), enabling direct validation using Arabidopsis T-DNA insertion mutants (crk26, mbd10, rdr2, arf10); (b) Well-characterized two-step germination (testa rupture then endosperm rupture); (c) WGT provides "buffered knockdown" model -- paradoxical targets explained by paralog compensation; (d) Strong epigenetic targets (MBD10 + RDR = two-pronged derepression); (e) Moderately fast germination (24-72h); (f) Small seeds (~3 mg) are cost-effective for large-N experiments. **Limitations**: Small seeds are harder to dissect for tissue-specific analysis; WGT complicates homeolog-specific qPCR; smaller B. oleracea research community means fewer validated tools. |
| **4** | **Wheat (Triticum aestivum, Chinese Spring)** | 7.0/10 | **Best crop for defense-pathway analysis.** Reasons: (a) Unprecedented 24% of targets in defense pathways -- the dominant theme unique among crops; (b) PARP target is the most well-validated single target across all crops (>10% biomass increase in PARP-deficient plants; De Block et al. 2005); (c) ADC-polyamine target provides unique mechanism not seen in other crops; (d) DDM1 epigenetic target in an 85% repetitive genome could have large effects; (e) Massive existing genetic resources (IWGSC RefSeq v1.1, Chinese Spring deletion lines, TILLING populations); (f) Agricultural importance (largest crop by acreage globally). **Limitations**: Hexaploid genome (17 Gb) massively complicates homeolog-specific qPCR -- primers must distinguish A/B/D copies using 3' UTR SNPs; slow germination for a monocot (72-120h); seeds are intermediate size (~40 mg); many paradoxical/detrimental targets (BOP1, profilin, kinesin, AOX) complicate interpretation. |
| **5** | **Spinach (Spinacia oleracea)** | 6.5/10 | **The original model system with the most targets.** Reasons: (a) 109 predicted targets -- the most comprehensive target list; (b) Six well-defined mechanistic themes with clear synergistic models; (c) Ethylene receptor (Rank 1) is the strongest single pro-germination target with etr1-1 mutant evidence; (d) Spinach is in the Amaranthaceae/Caryophyllales, sharing betalain biology with quinoa, enabling clade-specific comparisons. **Limitations**: (a) No genome-wide mutant collections; (b) Limited RNAi machinery characterization; (c) Smaller research community than maize/wheat/soybean; (d) Seed germination is heterogeneous (achene pericarp creates variability); (e) Diploid genome lacks polyploid buffering for safe knockdown; (f) The M-9 treatment was originally developed for spinach, so osmopriming confounds may be optimized for this species specifically. |
| **6** | **Quinoa (Chenopodium quinoa)** | 5.0/10 | **Most unique but least experimentally tractable.** Reasons: (a) Unique halophyte biology -- the ONLY crop where K+/Na+ discrimination and salt tolerance intersect with exRNA effects; (b) 100% Bacillus endophyte colonization with vertical transmission suggests deep co-evolutionary context for cross-kingdom RNA communication; (c) Expanded RNAi machinery (21 AGO, 8 DCL, 11 RDR); (d) Perisperm-based reserve system (unique among crops); (e) Betalain antioxidant pathway (unique to Caryophyllales). **Limitations**: (a) Only 4 of 31 targets confidently resolved (12.9%); (b) Perisperm biology is poorly characterized; (c) Limited genomic tools (no mutant collections, no VIGS system validated); (d) Saponin seed coat may impede sRNA uptake; (e) Allotetraploid with limited subgenome-specific resources; (f) Smaller research community; (g) Variable germination under standard conditions. Best reserved as a "unique biology" case study after mechanism is established in model crops. |

---

### Recommended Experimental Sequence

```
WEEK 1-4:   Tier 1 in MAIZE (Go/No-Go decision)
            |
            v
     [If GO] -------> [If NO-GO: Pivot to EPS mechanism study]
            |
WEEK 5-12:  Tier 2 in MAIZE + SOYBEAN (Mechanistic confirmation)
            |
            v
WEEK 13-28: Tier 3 in MAIZE + SOYBEAN + BROCCOLI + WHEAT (Cross-crop translation)
            (Spinach and Quinoa added if resources permit)
            |
            v
WEEK 29-52: Tier 4 (Publication-grade package)
            Arabidopsis mutant validation
            Fluorescent sRNA tracking
            Bacterial mutant panel
            Pilot field trials
```

### Budget Summary

| Tier | Timeline | Cost | Decision Point |
|------|----------|------|----------------|
| Tier 1 | Weeks 1-4 | $1,900 | Go/No-Go on RNA hypothesis |
| Tier 2 | Weeks 5-12 | $7,000-9,000 | Mechanistic confirmation |
| Tier 3 | Weeks 13-28 | $22,000 | Cross-crop universality |
| Tier 4 | Weeks 29-52 | $73,000+ | Publication-grade + field trials |
| **TOTAL** | **52 weeks** | **$104,000-106,000** | **Nature/Science-level paper** |

**Critical path**: The entire program hinges on the $300 RNase elimination experiment in Week 1. If RNA is not essential, the remaining $100,000+ investment is redirected rather than wasted.

---

## Appendix: Cross-Crop Conserved Pathway Summary

### Pathways Targeted Across Multiple Crops

| Pathway | Spinach | Broccoli | Maize | Wheat | Quinoa | Soybean | Conservation |
|---------|---------|----------|-------|-------|--------|---------|-------------|
| ABA signaling suppression | EDR2, LOX, AHP, Phytoene synthase | ARF, CDPK15, PP2A | ABI40, NPF15, HEX6, IDP8263 | SnRK2, ADC, NAC38, BTB | CNGC14 (indirect) | PLDbeta1, ROP9, CKX3 | **6/6 crops** |
| Defense downshift | MOS1, EDR2, RLKs, R-proteins | CRK26/29, Chitinase, RDR, ABCG37 | CML21, LRR-RLK, MOS1, PSKR1 | 6 F-box, 5 LRR-RLK, 2 NB-LRR, 3 ABC | NLR candidate, antimicrobial peptides, BRL2 | TIR-NBS-LRR, ERECTA-like | **6/6 crops** |
| Epigenetic derepression | DNA methyltransferase, SUVR5, HIRA, PHD | MBD10, RDR, TRFL7 | MOS1-like (chromatin) | DDM1, Bromodomain, Homeobox-DDT | -- | -- | **4/6 crops** |
| ROS/Redox optimization | GST, Peroxidase, 6-PGDH | COPT5, TrxL2.2, CRK-RBOH | PRX91 | PARP, AOX (paradox) | CYP76AD (betalain) | Glutaredoxin | **6/6 crops** |
| Hormone node manipulation | Ethylene receptor, LOX | ARF, HD-ZIP | HEX6-ABA crosstalk | ADC-polyamine/ABA, ARF | CNGC14-Ca2+-ABA | CKX3, PLDbeta1 | **6/6 crops** |
| Cell wall/mechanical | Peroxidase | PME, BGAL10, GH17 | ZRP4 O-methyltransferase | -- | -- | CesA4 | **4/6 crops** |
| Transport/ion homeostasis | CCC, CNGC, ABC | COPT5, PDR9 | NPF15, GDT1-like | ABC, MFS, MscS, Mg transporter | CqHAK5, CqCNGC14 | -- | **5/6 crops** |

### Key Conclusion

**ABA signaling suppression** and **defense downshift** are the only two pathways targeted in ALL 6 crops, making them the strongest candidates for universal mechanisms. The epigenetic derepression theme is prominent in 4 of 6 crops (absent in quinoa and soybean target lists, though may be indirect). ROS optimization is present in all 6 but through different specific mechanisms. This convergence across dicots (spinach, broccoli, quinoa, soybean) and monocots (maize, wheat) spanning 3 plant orders (Caryophyllales, Brassicales/Fabales, Poales) strongly suggests that ABA suppression + defense reallocation is a conserved bacterial strategy for manipulating plant germination.

---

*Report generated: 2026-02-17*
*Analysis based on: spinach_claims.md (109 targets), broccoli_claims.md (89 targets), maize_claims.md (20 targets), wheat_claims.md (75 targets), quinoa_claims.md (31 targets), soybean_claims.md (18 targets)*
*Total unique predicted targets across all crops: ~342*
