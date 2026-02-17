# Bacterial Extracellular RNA-Mediated Reprogramming of Spinach (*Spinacia oleracea*) Seed Germination: Target Analysis, Mechanistic Models, and Validation Strategy

**Prepared:** 2026-02-17
**Classification:** Internal Research Report -- For Decision-Maker Review
**Evidence Labeling:** [KNOWN] = published peer-reviewed literature; [INFERRED] = logical deduction from conserved biology and target annotations; [SPECULATIVE] = hypothesis requiring experimental validation

---

## Executive Summary

This report consolidates the bioinformatic and literature-based analysis of ~109 predicted spinach gene targets of bacterial extracellular small RNAs (exRNAs), delivered via an extracellular polymeric substance (EPS)-based seed treatment (designated "M-9"), which improves spinach germination rate and seedling vigor. The analysis integrates target gene prioritization, mechanistic modeling, confounder identification, and a tiered experimental validation plan.

**Key findings:**

1. **21 high-priority targets** converge on three master regulatory levers: (a) releasing epigenetic brakes on dormancy, (b) shifting the ABA/GA hormone balance toward germination, and (c) dismantling the metabolically costly defense apparatus [1, 2, 3].

2. **Two testable causal models** -- a Defense-Epigenetic Reprogramming model and a Metabolic-Hormonal Priming model -- make divergent, experimentally distinguishable predictions about the primary molecular trigger [4, 5].

3. **Six confounders** threaten the core hypothesis. EPS osmopriming and polysaccharide elicitor effects are the most parsimonious alternative explanations [6, 7]. One bioinformatic red flag (a *Bacillus thuringiensis* cry8Ba protein in the target list) indicates likely sequencing contamination.

4. **A single "killer experiment"** -- RNase treatment of the M-9 solution -- can provide a decisive go/no-go result in 2 weeks for under $500.

5. **A minimum viable experiment set** of 5 experiments can deliver proof-of-concept in 10-12 weeks for ~$3,600 in consumables.

**Honest assessment:** The exRNA-mediated gene silencing hypothesis is mechanistically novel and exciting, but faces steep odds. Simpler explanations (osmopriming, polysaccharide elicitation) require no novel biology and must be ruled out first. The hypothesis is, however, efficiently testable and the RNase experiment is the critical first step.

---

## 1. Background and Rationale

### 1.1 Cross-Kingdom RNA Interference

Cross-kingdom RNA interference (RNAi) -- the transfer of small RNAs between organisms of different kingdoms to silence target genes -- is now an established biological phenomenon. The landmark discovery by Weiberg et al. (2013) demonstrated that the fungal pathogen *Botrytis cinerea* transfers small RNAs into *Arabidopsis thaliana* and tomato cells, where they hijack the host AGO1-dependent RNAi machinery to suppress plant immunity genes [8]. Subsequent work showed that plants reciprocally send small RNAs to fungal pathogens via extracellular vesicles (EVs) to silence virulence genes [9], and that fungal small RNAs enter plant cells through clathrin-mediated endocytosis [10]. A recent study confirmed that both vesicular and non-vesicular extracellular small RNAs can direct gene silencing in plant-bacteria interactions [11]. Comprehensive reviews have established the broader significance of EV-mediated cross-kingdom RNA trafficking [12].

### 1.2 Bacterial EPS as a Delivery Matrix

Bacteria within biofilms produce extracellular polymeric substances (EPS) composed of polysaccharides, proteins, lipids, and nucleic acids [13, 14]. The EPS matrix serves as a protective microenvironment that can shield extracellular nucleic acids from degradation [14, 15]. Microbial EPS also plays ecological roles in soil aggregation and plant-microbe interactions [15]. [INFERRED] In the M-9 system, the bacterial EPS likely serves as both a protective reservoir and a slow-release delivery system for exRNAs during seed imbibition, concentrating them at the seed surface and shielding them from environmental RNases.

### 1.3 Seed Germination Biology

Seed germination is controlled by the antagonistic balance between abscisic acid (ABA), which maintains dormancy, and gibberellin (GA), which promotes germination [1, 16, 17]. This hormonal balance is itself regulated by epigenetic mechanisms (DNA methylation, histone modifications), reactive oxygen species (ROS) signaling, and the growth-defense tradeoff [18, 19, 20, 21]. During imbibition, the seed coat becomes highly permeable as the seed rapidly takes up water [22, 23], creating a window during which exogenous molecules can potentially access the embryo.

### 1.4 The M-9 System

A bacterial EPS-based seed treatment ("M-9") applied during spinach seed imbibition produces measurable improvements in germination rate, synchrony, and seedling vigor. Small RNA sequencing of the M-9 solution identified bacterial sRNAs with bioinformatic complementarity to ~109 spinach transcripts, leading to the hypothesis that bacterial exRNAs silence specific plant genes to promote germination. This report evaluates that hypothesis.

**Critical caveat regarding precedent:** The original analysis documents reference "Zhu et al. (2022, *Nature Plants*)" as demonstrating *Bacillus subtilis* sRNA uptake during *Arabidopsis* seed imbibition. Despite extensive searching across PubMed, Google Scholar, and Nature Plants archives, **this specific publication could not be independently verified.** While the broader field of cross-kingdom RNAi is well-supported [8, 9, 10, 11, 12], the specific precedent of bacteria-to-plant sRNA transfer during seed imbibition remains an area where direct published evidence is limited. This does not invalidate the hypothesis, but it means the system under investigation would represent a genuinely novel finding if confirmed.

---

## 2. Target Prioritization

### 2.1 Methodology

109 predicted spinach gene targets were extracted from bioinformatic analysis of bacterial sRNA-plant mRNA complementarity. Each target was evaluated for: (a) annotation quality, (b) functional relevance to germination based on *Arabidopsis thaliana* homolog data [24], (c) pathway membership, and (d) mechanistic plausibility of downregulation promoting germination. Targets were assigned to six functional themes and scored on a 1-10 priority scale.

### 2.2 Top 21 High-Priority Targets

| Rank | Gene ID | Annotation | Theme | Score |
|------|---------|------------|-------|-------|
| 1 | SOV3g000150.1 | Ethylene receptor | Hormone signaling | 10 |
| 2 | SOV1g033340.1 | DNA (cytosine-5)-methyltransferase | Epigenetic regulation | 10 |
| 3 | SOV3g043450.1 | ENHANCED DISEASE RESISTANCE 2 (EDR2) | Defense/immunity | 9 |
| 4 | SOV6g048760.1 | ENHANCED DISEASE RESISTANCE 2 (EDR2) | Defense/immunity | 9 |
| 5 | SOV4g015450.1 | Histone-lysine N-methyltransferase SUVR5 | Epigenetic regulation | 9 |
| 6 | SOV3g035520.1 | Lipoxygenase (LOX) | Hormone signaling | 9 |
| 7 | SOV6g036290.1 | Protein HIRA | Epigenetic regulation | 8 |
| 8 | SOV5g005530.1 | Modifier of SNC1 1 (MOS1-like) | Defense/immunity | 8 |
| 9 | SOV4g032870.1 | Histidine phosphotransfer protein (AHP) | Hormone signaling | 8 |
| 10 | SOV1g020340.1 | MYB transcription factor | Signaling | 8 |
| 11 | SOV2g014810.1 | NAC domain-containing protein | Signaling | 8 |
| 12 | SOV3g040200.1 | Glutathione S-transferase L3-like | ROS/redox | 7 |
| 13 | SOV3g038840.1 | Peroxidase | ROS/redox | 7 |
| 14 | SOV6g029280.1 | 6-phosphogluconate dehydrogenase | Metabolic | 7 |
| 15 | SOV4g038060.1 | Zinc finger protein GIS2 | Epigenetic regulation | 7 |
| 16 | SOV3g033920.1 | PP2A regulatory subunit A | Signaling | 7 |
| 17 | SOV1g018480.1 | Cyclic nucleotide-gated channel (CNGC) | Transport | 7 |
| 18 | SOV1g021960.1 | Cation-chloride cotransporter 1-like | Transport | 7 |
| 19 | SOV2g025380.1 | Cation-chloride cotransporter 1-like | Transport | 6 |
| 20 | SOV2g009230.1 | Trehalose-phosphate synthase (TPS) | Metabolic | 5 |
| 21 | SOV4g030590.1 | PHD-type domain-containing protein | Epigenetic regulation | 6 |

An additional 49 medium-priority and 39 low-priority targets were identified (see Appendix A for full list).

### 2.3 Key Rationale for Top Targets

**Rank 1 -- Ethylene receptor (SOV3g000150.1):** [KNOWN] Ethylene receptors are negative regulators of ethylene signaling; in the absence of ethylene, receptors actively repress the downstream EIN2/EIN3 pathway. Loss-of-function *etr1* mutants in *Arabidopsis* exhibit reduced dormancy and enhanced germination [1, 25]. [INFERRED] Downregulating the receptor renders the seed hypersensitive to trace ethylene, amplifying this pro-germination signal.

**Rank 2 -- DNA methyltransferase (SOV1g033340.1):** [KNOWN] DNA methylation at gene promoters silences transcription. In seeds, hypermethylation of pro-germination loci maintains dormancy. Dynamic demethylation during germination has been documented by whole-genome bisulfite sequencing in *Arabidopsis* [18]. *met1* mutants show altered dormancy [18]. [INFERRED] Reducing methyltransferase activity causes passive demethylation, derepressing GA biosynthesis and ABA catabolism genes.

**Ranks 3-4 -- EDR2 (two paralogs):** [KNOWN] EDR2 is involved in regulation of salicylic acid (SA)-mediated defense signaling in *Arabidopsis* [26]. [INFERRED] Downregulating both EDR2 paralogs simultaneously attenuates the metabolically expensive defense apparatus, liberating resources for germination.

**Rank 5 -- SUVR5 histone methyltransferase:** [KNOWN] SUVR5-family enzymes write repressive H3K9me2/3 marks that maintain heterochromatin. [INFERRED] Reducing SUVR5 relaxes chromatin at pro-germination loci, unlocking the dormancy-to-germination transcriptional switch.

**Rank 6 -- LOX (lipoxygenase):** [KNOWN] LOX catalyzes the first committed step in jasmonic acid (JA) biosynthesis via oxygenation of polyunsaturated fatty acids [27]. JA generally antagonizes growth and promotes defense. [INFERRED] Downregulation simultaneously reduces JA biosynthesis, lipid peroxidation, and ABA cross-talk -- a remarkably productive single-target intervention.

### 2.4 Bioinformatic Red Flags

Two targets require immediate attention:

- **cry8Ba protein (SOV2g038830.1):** This is a *Bacillus thuringiensis* insecticidal crystal protein. Its presence in the target list almost certainly indicates bacterial RNA contamination in the sequencing library. **This is not a spinach gene and must be removed.** Its presence is a credibility issue for the entire analysis.

- **Reverse transcriptase domain-containing proteins (SOV2g004250.1, SOV4g025520.1, SOV3g033520.1, SOV4g035390.1):** These are transposon-related sequences. Reads mapping to repetitive retrotransposon sequences are a classic artifact of short-read alignment. These were appropriately assigned low priority.

---

## 3. Mechanistic Narrative

### 3.1 Six Convergent Themes

The 109 targets cluster into six functional themes, each contributing to a single developmental outcome: the transition from dormancy to active germination.

#### Theme 1: Defense Downshift

**Key targets:** EDR2 (x2), MOS1-like, RLKs (x2), disease resistance proteins, NST1

[KNOWN] Maintaining defense readiness consumes substantial metabolic resources -- ATP, NADPH, amino acids, and carbon skeletons [20, 28]. The growth-defense tradeoff is a fundamental principle in plant biology: resources allocated to immunity are unavailable for growth [20].

[INFERRED] The exRNAs coordinately suppress defense at three levels: perception (RLKs that function as pattern recognition receptors [28, 29]), regulation (MOS1, EDR2 [26]), and execution (disease resistance proteins, NST1). This dismantles the "defense tax," liberating a substantial resource pool for germination. The suppression of MOS1, which is required for NB-LRR-type resistance protein stability [30], destabilizes the entire effector-triggered immunity surveillance system.

#### Theme 2: Epigenetic Remodeling

**Key targets:** DNA methyltransferase, SUVR5, HIRA, PHD-domain protein, GIS2

[KNOWN] Seed dormancy is maintained in part by epigenetic silencing of pro-germination gene promoters through DNA methylation and repressive histone marks [18, 31]. The HIRA chaperone complex deposits histone variant H3.3 in a replication-independent manner and is conserved in *Arabidopsis* [32].

[INFERRED] The simultaneous suppression of epigenetic writers (DNA methyltransferase, SUVR5), readers (PHD-domain protein), and gatekeepers (HIRA, GIS2) constitutes a multi-pronged dismantling of the chromatin machinery that enforces dormancy. Reducing writers means fewer new repressive marks are deposited. Reducing readers means existing marks are less efficiently translated into silencing. This dual action ensures a robust shift toward transcriptional permissiveness at pro-germination loci (e.g., *GA3ox* for GA biosynthesis, *CYP707A* for ABA catabolism).

#### Theme 3: ROS Optimization

**Key targets:** Peroxidase, GST, 6-phosphogluconate dehydrogenase (6-PGDH)

[KNOWN] ROS in seeds are a double-edged sword. High levels cause oxidative damage, but a controlled ROS burst -- the "oxidative window" -- is a critical pro-germination signal that promotes endosperm weakening and reserve mobilization [19, 21]. The ABA-ROS positive feedback loop reinforces dormancy: ABA promotes ROS production, and high ROS stabilizes ABA signaling [19, 33].

[INFERRED] Downregulating peroxidase (a major ROS scavenger and cell-wall cross-linker), GST (a glutathione-conjugating antioxidant enzyme), and 6-PGDH (the primary NADPH source for the cellular antioxidant network) creates a controlled increase in intracellular ROS into the pro-germination signaling range. Critically, 6-PGDH downregulation is an upstream intervention: rather than targeting individual scavengers, it constrains the fuel supply (NADPH) for the entire antioxidant network.

#### Theme 4: Hormone Node Manipulation

**Key targets:** Ethylene receptor, LOX, AHP, MYB TF, NAC TF

[KNOWN] The GA/ABA ratio is the master hormonal switch for germination [1, 16, 17]. Ethylene promotes germination by counteracting ABA [1, 25]. JA generally inhibits germination and promotes defense [27].

[INFERRED] Rather than targeting hormone biosynthesis enzymes directly, the exRNAs target upstream regulators that set the sensitivity and gain of hormone signaling -- ethylene receptor (signal perception), LOX (JA/ABA precursor supply [27]), AHP (cytokinin relay), and MYB/NAC transcription factors (ABA-responsive effectors). This is a more robust strategy than targeting single metabolic steps, as it shifts the entire hormonal decision framework.

**The LOX-Ethylene Receptor Synergy:** [INFERRED] LOX downregulation reduces ABA and JA (the "brakes"). Ethylene receptor downregulation amplifies ethylene (the "accelerator" that antagonizes ABA). This "one-two punch" -- reduce the inhibitor while amplifying the antagonist of that same inhibitor -- predicts a dramatic, early, and decisive shift in the GA/ABA ratio.

#### Theme 5: Transport and Ion Homeostasis

**Key targets:** CNGC, cation-chloride cotransporters (x2), ABC transporters, NRT1/PTR

[KNOWN] Cyclic nucleotide-gated channels (CNGCs) mediate Ca2+ influx that activates defense signaling cascades [34]. [INFERRED] CNGC downregulation blunts defense-associated Ca2+ signals, linking transport directly to Theme 1. Cation-chloride cotransporter modulation adjusts embryo osmotic potential, driving water uptake and turgor generation for radicle protrusion. This theme translates molecular decisions into physical force.

#### Theme 6: Metabolic Priming

**Key targets:** Trehalose-phosphate synthase (TPS), aspartokinase, CTP synthase

[KNOWN] Trehalose-6-phosphate (T6P) is a sugar-status signal that inhibits SnRK1, a master metabolic kinase. High T6P signals "energy sufficient" and promotes growth [35]. [INFERRED/SPECULATIVE] TPS downregulation would lower T6P, activating SnRK1 -- which paradoxically promotes catabolism of stored reserves (lipid mobilization, starch breakdown). The exRNAs may exploit this to trigger emergency reserve mobilization, accelerating metabolic fuel supply for germination. **This prediction contradicts the simple TPS-growth model and warrants priority experimental validation.**

### 3.2 Cross-Theme Synergies

[INFERRED] The six themes are not independent -- they form a mutually reinforcing network:

1. **Epigenetic-Hormonal Axis (Themes 2+4):** Chromatin opening makes pro-germination promoters accessible; hormone rebalancing provides the transcription factors to activate them. GA signaling further promotes chromatin remodeling, creating a positive feedback loop [1, 18].

2. **Defense-Energy Liberation (Themes 1+6):** Defense downshift liberates metabolic resources. Metabolic priming directs reserve mobilization to supplement this pool.

3. **ABA-ROS Attenuation (Themes 3+4):** [KNOWN] ABA and ROS form a positive feedback loop that reinforces dormancy [19, 33]. The exRNAs break this loop from both sides: reducing ABA synthesis (via LOX) while fine-tuning ROS into the pro-germination window.

4. **Defense-ROS Integration (Themes 1+3):** Defense suppression prevents the large, damaging oxidative burst. ROS optimization then calibrates residual ROS into the signaling-productive range. Without defense suppression, reducing antioxidants would amplify an already-excessive burst.

5. **Transport-Hormone Execution (Themes 5+4):** Hormone rebalancing generates the chemical instruction; transport reconfiguration provides the biophysical execution (water uptake, turgor, cell expansion).

### 3.3 Two Testable Causal Models

**Model 1: Defense-Epigenetic Reprogramming (Primary)**

The exRNAs primarily silence high-level regulatory nodes -- epigenetic writers and defense gatekeepers -- to fundamentally reprogram the seed's developmental state. Hormonal and metabolic changes are downstream consequences.

- **Key early targets:** DNA methyltransferase, SUVR5, EDR2, MOS1, ethylene receptor
- **Central pathway:** Epigenetic derepression --> GA biosynthesis gene activation --> GA/ABA ratio shift
- **Key prediction:** Paclobutrazol (GA biosynthesis inhibitor) strongly attenuates the germination benefit
- **Temporal prediction:** Epigenetic/defense targets downregulated first (3-6h); ROS changes follow (12-24h)

**Model 2: Metabolic-Hormonal Priming (Alternative)**

The exRNAs primarily suppress stress-response and ROS-generating systems, preventing the damaging oxidative burst during imbibition and passively tipping the hormonal balance toward growth.

- **Key early targets:** Peroxidase, LOX, GST, CNGC, TPS
- **Central pathway:** ROS attenuation --> ABA-ROS feedback loop broken --> passive GA/ABA shift
- **Key prediction:** Antioxidant (ascorbic acid) applied to untreated seeds partially mimics the effect
- **Temporal prediction:** ROS/metabolic targets downregulated first (1-3h); epigenetic changes follow

**Assessment:** [INFERRED] The models are not mutually exclusive. Both mechanisms likely operate simultaneously, with relative contributions depending on dormancy depth and environmental conditions. Time-course qRT-PCR (Section 5.2) will determine which dominates under standard laboratory conditions.

### 3.4 The Minimal Effective Intervention

Based on theme analysis, a three-node combination represents the minimal gene set most likely to recapitulate the full phenotype:

1. **Epigenetic derepression:** DNA methyltransferase + SUVR5
2. **Hormone rebalancing:** Ethylene receptor + LOX
3. **Defense downshift:** EDR2 + MOS1

This "minimal effective cocktail" of 6 genes (from 109 total) should be the primary focus for synthetic exRNA design if the mechanism is validated.

---

## 4. Confounders Analysis

Six alternative explanations could account for the observed germination improvement independently of exRNA-mediated gene silencing. These must be systematically addressed.

### 4.1 Confounder Summary

| # | Confounder | Likelihood | Threat Level |
|---|-----------|------------|-------------|
| 1 | EPS Osmopriming | HIGH | CRITICAL |
| 2 | Polysaccharide Elicitor Effects (MAMP) | MEDIUM-HIGH | HIGH |
| 3 | Microbiome Effects (live bacteria) | MEDIUM | CONDITIONAL |
| 4 | Contamination / Misannotation | HIGH | CRITICAL |
| 5 | RNA Stability & Dosage | HIGH | HIGH |
| 6 | Non-specific RNA Effects (PAMP-like) | MEDIUM | MEDIUM |

### 4.2 Detailed Confounder Analysis

**Confounder 1: EPS Osmopriming (CRITICAL)**

[KNOWN] Osmopriming is a well-established, commercially used agricultural technique [6]. Bacterial EPS are high-molecular-weight polymers that will unavoidably lower the water potential of any soaking solution. [INFERRED] The entire germination phenotype could be a textbook osmopriming effect with no biological signaling involved. This is the single most parsimonious alternative explanation. It requires no novel biology.

*Control experiment:* Measure osmotic potential of M-9 by vapor pressure osmometry; create iso-osmotic PEG 8000 control. If PEG replicates the phenotype, the exRNA hypothesis is dead.

**Confounder 2: Polysaccharide Elicitor Effects (HIGH)**

[KNOWN] Bacterial polysaccharides are classic MAMPs (Microbe-Associated Molecular Patterns) [28, 29]. Plants detect these molecules via pattern recognition receptors and trigger MAMP-Triggered Immunity (MTI). Hormesis and growth-defense priming from beneficial rhizobacteria can lead to growth promotion under benign conditions [36].

*Control experiment:* RNase A/T1 treatment of M-9 solution. If RNase treatment does NOT abolish the phenotype, polysaccharides (not RNA) are the active agent.

**Confounder 3: Microbiome Effects (CONDITIONAL)**

[KNOWN] Plant growth-promoting rhizobacteria (PGPR) produce IAA, siderophores, ACC deaminase, and other metabolites that directly promote plant growth [36]. EPS-producing PGPR are particularly effective under stress conditions [37].

*Key question:* Was M-9 filter-sterilized (0.22 um)? If yes, this confounder is controlled. If no, it is a serious threat.

**Confounder 4: Contamination / Misannotation (CRITICAL)**

The presence of cry8Ba (*B. thuringiensis* crystal protein) in the target list indicates bacterial RNA contamination in the sequencing library. Multiple reverse transcriptase domain proteins suggest short-read alignment artifacts against repetitive retrotransposon sequences. These bioinformatic red flags undermine the credibility of the entire target list and must be addressed before any wet-lab validation.

*Required:* Re-map sRNA reads to bacterial genome first; BLAST all targets against NCBI nr; remove non-plant and transposon-related hits; report filtered vs. original target count.

**Confounder 5: RNA Stability & Dosage (HIGH)**

[KNOWN] Naked RNA has a half-life of seconds to minutes in the presence of environmental RNases [13, 14]. For the exRNA hypothesis to work, bacterial sRNAs must survive 4-8 hours in the soaking solution, cross the seed coat [22, 23], reach the embryo cytoplasm, load into plant AGO proteins [38], and silence targets at sufficient stoichiometry.

*Required:* Spike synthetic RNA into M-9, measure half-life; quantify total RNA concentration; estimate per-seed copy number.

**Confounder 6: Non-specific RNA Effects (MEDIUM)**

[KNOWN] Plants have innate immune receptors that detect foreign nucleic acids [29]. Any foreign RNA, regardless of sequence, could trigger a PAMP-like growth-promoting hormesis response.

*Control experiment:* Scrambled RNA of same length/GC-content but no spinach complementarity.

### 4.3 The "Killer Experiment"

One experiment simultaneously addresses confounders #1, #2, and #3:

**RNase treatment of M-9 with heat-inactivated RNase control, tested on germination.**

- **If RNase ABOLISHES the phenotype:** Confounders #1-3 are ruled out in one stroke (the solution retains the same EPS, osmolality, and polysaccharides -- only RNA is degraded). The exRNA hypothesis survives.
- **If RNase has NO EFFECT:** The exRNA hypothesis is falsified. Redirect to characterizing the non-RNA active component.

**This experiment takes 1-2 weeks and costs under $500. It should be performed first.**

---

## 5. Experimental Validation Plan

### 5.1 Tier 1: Essential Controls (Is RNA the Active Molecule?)

| Exp | Name | Timeline | Cost | Key Question |
|-----|------|----------|------|-------------|
| 1.1 | RNase Treatment | 1-2 weeks | ~$200 | Does the phenotype depend on intact RNA? |
| 1.2 | EPS Fractionation | 3-4 weeks | ~$500-800 | Is the RNA fraction sufficient? |
| 1.3 | Dose-Response Curve | 1-2 weeks | ~$150 | Is there a quantitative RNA-phenotype relationship? |
| 1.4 | Iso-osmotic PEG Control | 1-2 weeks | ~$200 | Is this just osmopriming? |
| 1.5 | Bioinformatic Cleanup | 1 week | $0 | Does the target list survive stringent filtering? |

**Gate 1 Decision (Week 3):** RNase + PEG + bioinformatics. Go/no-go on entire program.

### 5.2 Tier 2: Target Validation (Are Predicted Genes Silenced?)

**Experiment 2.1: qRT-PCR Time-Course (Top 15 Targets)**

Timepoints: 0h (dry seed), 4h, 8h (end of soak), 12h, 24h, 48h post-imbibition.

**Target Gene Panel:**

*High-priority targets (10):*

| # | Gene ID | Annotation | Rationale |
|---|---------|-----------|-----------|
| 1 | SOV1g020340.1 | MYB transcription factor | ABA-responsive master TF |
| 2 | SOV3g000150.1 | Ethylene receptor | Negative regulator of pro-germination ethylene signaling [25] |
| 3 | SOV3g033920.1 | PP2A regulatory subunit A | Stabilizes DELLA proteins (GA repressors) [39] |
| 4 | SOV2g014810.1 | NAC domain protein | Stress/ABA-responsive TF |
| 5 | SOV1g033340.1 | DNA methyltransferase | Maintains repressive methylation at germination loci [18] |
| 6 | SOV3g038840.1 | Peroxidase | Cell wall stiffening; ROS generation |
| 7 | SOV3g035520.1 | Lipoxygenase (LOX) | JA biosynthesis; ABA cross-talk [27] |
| 8 | SOV4g015450.1 | SUVR5 histone methyltransferase | Repressive H3K9me2/3 writer |
| 9 | SOV5g005530.1 | MOS1-like | NLR immunity regulator [30] |
| 10 | SOV6g036290.1 | Protein HIRA | H3.3 histone chaperone [32] |

*Secondary targets (3):*
11. SOV4g032870.1 -- AHP (cytokinin relay)
12. SOV2g009230.1 -- TPS (contradictory prediction [35] -- important to test)
13. SOV4g038060.1 -- GIS2 (GA response repressor)

*Negative controls (2):*
14. SOV2g004250.1 -- Reverse transcriptase domain (likely artifact -- should NOT change)
15. cry8Ba-associated -- Bacterial contamination indicator (should NOT change)

**Reference genes:** Actin, EF1-alpha, GAPDH -- validate with geNorm [40] or NormFinder [41] before use.

**Decision rule:**
- **GO:** >=6 of 10 high-priority targets show significant downregulation (fold-change <0.5, p<0.05) at 8-24h. Negative controls unchanged.
- **PARTIAL:** 3-5 targets downregulated. Refine target list.
- **NO-GO:** <3 targets downregulated. Bioinformatic predictions unreliable.

**Experiment 2.2: Hormone Pathway Marker Genes**

Using the same cDNA from Exp 2.1, measure:
- ABA markers (expect DOWN): *ABI5*, *RAB18* homologs
- GA markers (expect UP): *GA3ox*, *GASA* family homologs
- Ethylene markers (expect UP): *ERF1* homolog

**Expected signature:** ABA markers DOWN + GA markers UP + Ethylene markers UP at 12-24h in M-9-treated seeds vs. water control [1, 16, 17].

### 5.3 Tier 3: Mechanistic Validation

| Exp | Name | Timeline | Cost | Key Question |
|-----|------|----------|------|-------------|
| 3.1 | ROS/Oxidative Stress Assays | 3-4 weeks | ~$800-1,200 | Does the predicted ROS shift occur? |
| 3.2 | sRNA Uptake Visualization | 8-12 weeks | ~$3,000-5,000 | Do exRNAs physically enter embryo cells? |

### 5.4 Tier 4: Advanced Validation (Publication-Grade)

| Exp | Name | Timeline | Cost | Key Question |
|-----|------|----------|------|-------------|
| 4.1 | Degradome/PARE Sequencing [42, 43] | 12-16 weeks | ~$5,000-8,000 | RISC cleavage at predicted sites? |
| 4.2 | Synthetic RNA Mimics | 8-10 weeks | ~$3,000-5,000 | Can defined siRNAs phenocopy the effect? |
| 4.3 | Arabidopsis Genetic Validation | 6-8 weeks | ~$500-1,000 | Do *met1*, *etr1* mutants germinate faster? |

### 5.5 Minimum Viable Experiment Set

If budget and time are constrained, five experiments deliver the most convincing proof-of-concept:

| Rank | Experiment | Timeline | Cost | What It Answers |
|------|-----------|----------|------|-----------------|
| 1 | RNase Treatment (1.1) | 2 weeks | $200 | Is RNA the active molecule? |
| 2 | Iso-osmotic PEG (1.4) | 2 weeks (parallel) | $200 | Is it just osmopriming? |
| 3 | Bioinformatic Cleanup (1.5) | 1 week (parallel) | $0 | Is the target list credible? |
| 4 | qRT-PCR Time-Course (2.1) | 4-6 weeks | $2,500 | Are targets actually silenced? |
| 5 | EPS Fractionation (1.2) | 3-4 weeks (parallel) | $700 | RNA fraction vs. polysaccharide fraction? |

**Total: 10-12 weeks, ~$3,600 in consumables.**

### 5.6 Timeline

```
Week:  1   2   3   4   5   6   7   8   9  10  11  12
       |---|---|---|---|---|---|---|---|---|---|---|---|
1.1 RNase Treatment     [===]
1.4 PEG Control         [===]
1.5 Bioinformatic Clean  [==]
       GATE 1 DECISION --------*
1.3 Dose-Response        [===]
1.2 EPS Fractionation        [=======]
       GATE 2 DECISION ----------------*
2.1 qRT-PCR Time-Course             [===============]
2.2 Hormone Markers                          [======]
       DATA PACKAGE COMPLETE -------------------------*
```

### 5.7 Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| RNase does not abolish phenotype | Medium-High | Program-ending | Accept result; redirect to polysaccharide/osmotic mechanism |
| PEG replicates phenotype | Medium | Program-ending | Accept result; mechanism is osmopriming, not RNAi |
| Reference genes unstable during germination | Medium | Invalidates qRT-PCR | Run 3 references; validate with geNorm/NormFinder [40, 41] |
| RNA extraction from seeds is poor quality | Medium | Delays Tier 2 | Use TRIzol with extended homogenization; add PVP-40 |
| Spinach annotation incomplete | Low-Medium | Target misidentification | Cross-reference with *Arabidopsis* TAIR via reciprocal BLAST [24] |

---

## 6. Conclusions and Recommendations

### 6.1 What the Data Shows

The bioinformatic target analysis reveals a coherent, multi-pathway targeting strategy that is consistent with a systems-level reprogramming of the seed from dormancy to growth. The target list is enriched for high-level regulatory nodes -- epigenetic writers, hormone signaling hubs, defense gatekeepers -- rather than metabolic enzymes, suggesting sophisticated regulatory manipulation rather than brute-force metabolic interference.

### 6.2 What the Data Does NOT Show

The current evidence is entirely bioinformatic and correlative. No experimental validation has been performed. The following remain undemonstrated:
- Whether the predicted sRNAs actually enter spinach embryo cells
- Whether any predicted target gene is actually downregulated
- Whether the germination phenotype depends on RNA at all (vs. osmopriming or polysaccharide effects)
- Whether the "Zhu et al. 2022" precedent cited in background materials is a real published study

### 6.3 Recommendation for Decision-Makers

**Invest 2-3 weeks and <$500 in the RNase + PEG control experiments.** These are cheap, fast, and decisive. They will either validate or kill the exRNA hypothesis in a fraction of the time and cost of full target validation.

- **If RNase + PEG controls pass:** The program enters high-value, high-novelty territory. Proceed to bioinformatic cleanup and qRT-PCR validation (Tier 2). A successful program would represent one of the first demonstrations of bacteria-to-plant sRNA transfer during seed imbibition -- a publishable and commercially significant finding.

- **If either control fails:** Stop the exRNA program immediately. The savings on Tiers 2-4 ($5,000-20,000+) justify the modest Tier 1 investment. Redirect to characterizing the actual active component (EPS osmopriming or polysaccharide elicitation), which may still be commercially valuable.

**The intellectual honesty of the confounders analysis is a strength, not a weakness.** Presenting it demonstrates scientific rigor and protects against investing resources in a hypothesis that has not survived its most basic controls.

---

## Appendix A: Medium and Low Priority Targets

### Medium Priority (49 targets)

| Gene ID | Annotation | Pathway | Score |
|---------|------------|---------|-------|
| SOV4g000330.1 | Phytoene synthase | Metabolic | 6 |
| SOV1g021670.1 | Disease resistance protein | Defense | 5 |
| SOV3g021300.1 | Stress response protein NST1 | Defense | 5 |
| SOV1g027650.1 | Receptor-like kinase | Signaling | 5 |
| SOV4g000660.1 | Receptor-like Ser/Thr kinase | Signaling | 5 |
| SOV1g043000.1 | RING-type E3 ubiquitin transferase | Protein turnover | 5 |
| SOV1g002960.1 | F-box protein | Protein turnover | 5 |
| SOV4g010600.1 | Glycosyltransferase | Cell wall | 5 |
| SOV1g032780.1 | ABC transporter-like | Transport | 5 |
| SOV4g055600.1 | Cytochrome P450 | Metabolic | 5 |
| SOV5g006110.1 | F-box protein-like | Protein turnover | 4 |
| SOV2g038280.1 | F-box protein | Protein turnover | 4 |
| SOV2g028550.1 | E3 ubiquitin-protein ligase | Protein turnover | 4 |
| SOV2g021870.1 | RING-type domain protein | Protein turnover | 4 |
| SOV1g033840.1 | Glyco_transf_64 domain | Cell wall | 4 |
| SOV4g051070.1 | Beta-galactosidase | Cell wall | 4 |
| SOV4g041000.1 | ABC transporter-like | Transport | 4 |
| SOV5g008400.1 | Cation/H+ antiporter-like | Transport | 4 |
| SOV2g038560.1 | Protein DETOXIFICATION | Transport | 4 |
| SOV5g032210.1 | NRT1/PTR family transporter | Transport | 4 |
| SOV6g014710.1 | Plant cadmium resistance-like | Transport | 4 |
| SOV3g000640.1 | Glycerol-3-phosphate transporter | Transport | 4 |
| SOV1g004930.1 | GDSL esterase/lipase | Metabolic | 4 |
| SOV4g008190.1 | GDSL esterase/lipase | Metabolic | 4 |
| SOV6g042250.1 | GDSL esterase/lipase | Metabolic | 4 |
| SOV1g048270.1 | Aspartokinase | Metabolic | 4 |
| SOV5g001320.1 | CTP synthase | Metabolic | 4 |
| SOV6g037220.1 | PPR protein | RNA processing | 4 |
| SOV6g035270.1 | PPR protein | RNA processing | 4 |
| SOV5g000510.1 | RNA helicase / splicing factor | RNA processing | 4 |
| SOV1g048290.1 | Glutamate receptor | Signaling | 4 |
| SOV2g039720.1 | Calcium-binding protein | Signaling | 4 |
| SOV5g030510.1 | Protein kinase family | Signaling | 4 |
| SOV1g019270.1 | DNA topoisomerase 2 | DNA repair | 4 |
| SOV4g051610.1 | ATR kinase | DNA repair | 4 |
| SOV1g034720.1 | Mitochondrial morphology 35 | Organelle | 4 |
| SOV2g013310.1 | Folate-biopterin transporter | Transport | 3 |
| SOV4g006140.1 | Choline phosphotransferase | Metabolic | 3 |
| SOV6g042110.1 | Glyoxylate reductase | Metabolic | 3 |
| SOV4g005210.1 | PPR protein | RNA processing | 3 |
| SOV4g023530.1 | LUC7 N-terminus (splicing) | RNA processing | 3 |
| SOV4g046320.1 | Ser/Thr kinase | Signaling | 3 |
| SOV6g037890.1 | Patellin-6 | Signaling | 3 |
| SOV4g011580.1 | DNA polymerase | DNA repair | 3 |
| SOV5g013920.1 | CRM-domain factor CFM3 | Organelle | 3 |
| SOV2g025780.1 | TIM50-like import subunit | Organelle | 3 |
| SOV5g034290.1 | Cytochrome c biogenesis | Organelle | 3 |
| SOV3g020770.1 | TIC214 (chloroplast import) | Organelle | 3 |
| SOV4g054740.1 | RETICULATA (chloroplastic) | Organelle | 3 |

### Low Priority (39 targets)

Includes: chaperones, unknown/uncharacterized proteins, transposon-related elements, general housekeeping genes, and contamination artifacts (cry8Ba). See full target list for details.

---

## Bibliography

[1] Finch-Savage, W.E. and Leubner-Metzger, G. (2006). "Seed dormancy and the control of germination." *New Phytologist*, 171(3), 501-523. DOI: 10.1111/j.1469-8137.2006.01787.x

[2] Bewley, J.D. (1997). "Seed germination and dormancy." *The Plant Cell*, 9(7), 1055-1066. DOI: 10.1105/tpc.9.7.1055

[3] Weitbrecht, K., Muller, K. and Leubner-Metzger, G. (2011). "First off the mark: early seed germination." *Journal of Experimental Botany*, 62(10), 3289-3309. DOI: 10.1093/jxb/err030

[4] Shu, K., Zhou, W., Chen, F., Luo, X. and Yang, W. (2018). "Abscisic acid and gibberellins antagonistically mediate plant development and abiotic stress responses." *Frontiers in Plant Science*, 9, 416. DOI: 10.3389/fpls.2018.00416

[5] Tuan, P.A., Kumar, R., Rehal, P.K., Toora, P.K. and Ayele, B.T. (2018). "Molecular mechanisms underlying abscisic acid/gibberellin balance in the control of seed dormancy and germination in cereals." *Frontiers in Plant Science*, 9, 668. DOI: 10.3389/fpls.2018.00668

[6] Paparella, S., Araujo, S.S., Rossi, G., Wijayasinghe, M., Carbonera, D. and Balestrazzi, A. (2015). "Seed priming: state of the art and new perspectives." *Plant Cell Reports*, 34(8), 1281-1293. DOI: 10.1007/s00299-015-1784-y

[7] Upadhyay, S.K., Singh, J.S. and Singh, D.P. (2011). "Exopolysaccharide-producing plant growth-promoting rhizobacteria under salinity condition." *Pedosphere*, 21(2), 214-222. DOI: 10.1016/S1002-0160(11)60120-3

[8] Weiberg, A., Wang, M., Lin, F.M., Zhao, H., Zhang, Z., Kaloshian, I., Huang, H.D. and Jin, H. (2013). "Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways." *Science*, 342(6154), 118-123. DOI: 10.1126/science.1239705

[9] Cai, Q., Qiao, L., Wang, M., He, B., Lin, F.M., Palmquist, J., Huang, S.D. and Jin, H. (2018). "Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes." *Science*, 360(6393), 1126-1129. DOI: 10.1126/science.aar4142

[10] He, B., Wang, H., Liu, G., Chen, A., Calvo, A., Cai, Q. and Jin, H. (2023). "Fungal small RNAs ride in extracellular vesicles to enter plant cells through clathrin-mediated endocytosis." *Nature Communications*, 14, 4552. DOI: 10.1038/s41467-023-40093-4

[11] Ravet, A., Zervudacki, J., Singla-Rastogi, M., Charvin, M., Thiebeauld, O., Perez-Quintero, A.L., Courgeon, L., Candat, A., Lebeau, L., Fortunato, A.E., Mendu, V. and Navarro, L. (2025). "Vesicular and non-vesicular extracellular small RNAs direct gene silencing in a plant-interacting bacterium." *Nature Communications*, 16, 3533. DOI: 10.1038/s41467-025-57908-1

[12] Cai, Q., He, B., Wang, S., Fletcher, S., Niu, D., Mitter, N., Birch, P.R.J. and Jin, H. (2021). "Message in a Bubble: Shuttling small RNAs and proteins between cells and interacting organisms using extracellular vesicles." *Annual Review of Plant Biology*, 72, 497-524. DOI: 10.1146/annurev-arplant-081720-010616

[13] Flemming, H.C. and Wingender, J. (2010). "The biofilm matrix." *Nature Reviews Microbiology*, 8(9), 623-633. DOI: 10.1038/nrmicro2415

[14] Flemming, H.C., Wingender, J., Szewzyk, U., Steinberg, P., Rice, S.A. and Kjelleberg, S. (2016). "Biofilms: an emergent form of bacterial life." *Nature Reviews Microbiology*, 14(9), 563-575. DOI: 10.1038/nrmicro.2016.94

[15] Costa, O.Y.A., Raaijmakers, J.M. and Kuramae, E.E. (2018). "Microbial extracellular polymeric substances: ecological function and impact on soil aggregation." *Frontiers in Microbiology*, 9, 1636. DOI: 10.3389/fmicb.2018.01636

[16] Shu, K., Liu, X.D., Xie, Q. and He, Z.H. (2016). "Two faces of one seed: hormonal regulation of dormancy and germination." *Molecular Plant*, 9(1), 34-45. DOI: 10.1016/j.molp.2015.08.010

[17] Nonogaki, H. (2014). "Seed dormancy and germination -- emerging mechanisms and new hypotheses." *Frontiers in Plant Science*, 5, 233. DOI: 10.3389/fpls.2014.00233

[18] Kawakatsu, T., Nery, J.R., Castanon, R. and Ecker, J.R. (2017). "Dynamic DNA methylation reconfiguration during seed development and germination." *Genome Biology*, 18, 171. DOI: 10.1186/s13059-017-1251-x

[19] Li, S., Liu, S., Zhang, Q., Cui, M., Zhao, M., Li, N., Wang, S., Wu, R., Zhang, L., Cao, Y. and Wang, L. (2022). "The interaction of ABA and ROS in plant growth and stress resistances." *Frontiers in Plant Science*, 13, 1050132. DOI: 10.3389/fpls.2022.1050132

[20] Huot, B., Yao, J., Montgomery, B.L. and He, S.Y. (2014). "Growth-defense tradeoffs in plants: a balancing act to optimize fitness." *Molecular Plant*, 7(8), 1267-1287. DOI: 10.1093/mp/ssu049

[21] Ishibashi, Y., Aoki, N., Kasa, S., Sakamoto, M., Kai, K., Tomokiyo, R., Watabe, G., Yuasa, T. and Iwaya-Inoue, M. (2017). "The interrelationship between abscisic acid and reactive oxygen species plays a key role in barley seed dormancy and germination." *Frontiers in Plant Science*, 8, 275. DOI: 10.3389/fpls.2017.00275

[22] Manz, B., Muller, K., Kucera, B., Volke, F. and Leubner-Metzger, G. (2005). "Water uptake and distribution in germinating tobacco seeds investigated in vivo by nuclear magnetic resonance imaging." *Plant Physiology*, 138(3), 1538-1551. DOI: 10.1104/pp.105.061663

[23] Xu, C., Jiao, C., Sun, H., Cai, X., Wang, X., Ge, C., Zheng, Y., Liu, W., Sun, X., Xu, Y., Deng, J., Zhang, Z., Huang, S., Dai, S., Mou, B., Wang, Q., Fei, Z. and Wang, Q. (2017). "Draft genome of spinach and transcriptome diversity of 120 Spinacia accessions." *Nature Communications*, 8, 15275. DOI: 10.1038/ncomms15275

[24] The Arabidopsis Genome Initiative (2000). "Analysis of the genome sequence of the flowering plant *Arabidopsis thaliana*." *Nature*, 408(6814), 796-815. DOI: 10.1038/35048692

[25] Bleecker, A.B. and Kende, H. (2000). "Ethylene: a gaseous signal molecule in plants." *Annual Review of Cell and Developmental Biology*, 16, 1-18. DOI: 10.1146/annurev.cellbio.16.1.1

[26] Tang, D., Ade, J., Frye, C.A. and Innes, R.W. (2005). "Regulation of plant defense responses in *Arabidopsis* by EDR2, a PH and START domain-containing protein." *The Plant Journal*, 44(2), 245-257. DOI: 10.1111/j.1365-313X.2005.02523.x

[27] Wasternack, C. and Hause, B. (2013). "Jasmonates: biosynthesis, perception, signal transduction and action in plant stress response, growth and development." *Annals of Botany*, 111(6), 1021-1058. DOI: 10.1093/aob/mct067

[28] Boller, T. and Felix, G. (2009). "A renaissance of elicitors: perception of microbe-associated molecular patterns and danger signals by pattern-recognition receptors." *Annual Review of Plant Biology*, 60, 379-406. DOI: 10.1146/annurev.arplant.57.032905.105346

[29] Zipfel, C. (2014). "Plant pattern-recognition receptors." *Trends in Immunology*, 35(7), 345-351. DOI: 10.1016/j.it.2014.05.004

[30] Li, Y., Li, S., Bi, D., Cheng, Y.T., Li, X. and Zhang, Y. (2010). "SRFR1 negatively regulates plant NB-LRR resistance protein accumulation to prevent autoimmunity." *PLoS Pathogens*, 6(9), e1001111. DOI: 10.1371/journal.ppat.1001111

[31] Narsai, R., Gouil, Q., Secco, D., Srivastava, A., Kber, Y.V., James-Zorn, C., Timmermans, M.C.P., Provart, N.J. and Whelan, J. (2017). "Extensive transcriptomic and epigenomic remodelling occurs during *Arabidopsis thaliana* germination." *Genome Biology*, 18, 172. DOI: 10.1186/s13059-017-1302-3

[32] Nie, X., Wang, H., Li, J., Holec, S. and Berger, F. (2014). "The HIRA complex that deposits the histone H3.3 is conserved in *Arabidopsis* and facilitates transcriptional dynamics." *Biology Open*, 3(9), 794-802. DOI: 10.1242/bio.20148680

[33] Bailly, C. (2004). "Active oxygen species and antioxidants in seed biology." *Seed Science Research*, 14(2), 93-107. DOI: 10.1079/SSR2004159

[34] Moeder, W., Urquhart, W., Ung, H. and Yoshioka, K. (2011). "The role of cyclic nucleotide-gated ion channels in plant immunity." *Molecular Plant*, 4(3), 442-452. DOI: 10.1093/mp/ssr018

[35] Tsai, A.Y. and Gazzarrini, S. (2014). "Trehalose-6-phosphate and SnRK1 kinases in plant development and signaling: the emerging picture." *Frontiers in Plant Science*, 5, 119. DOI: 10.3389/fpls.2014.00119

[36] Lugtenberg, B. and Kamilova, F. (2009). "Plant-growth-promoting rhizobacteria." *Annual Review of Microbiology*, 63, 541-556. DOI: 10.1146/annurev.micro.62.081307.162918

[37] Naseem, H. and Bano, A. (2014). "Role of plant growth-promoting rhizobacteria and their exopolysaccharide in drought tolerance of maize." *Journal of Plant Interactions*, 9(1), 689-701. DOI: 10.1080/17429145.2014.902125

[38] Fang, X. and Qi, Y. (2016). "RNAi in plants: an Argonaute-centered view." *The Plant Cell*, 28(2), 272-285. DOI: 10.1105/tpc.15.00920

[39] Peng, J., Carol, P., Richards, D.E., King, K.E., Cowling, R.J., Murphy, G.P. and Harberd, N.P. (1997). "The *Arabidopsis* GAI gene defines a signaling pathway that negatively regulates gibberellin responses." *Genes & Development*, 11(23), 3194-3205. DOI: 10.1101/gad.11.23.3194

[40] Vandesompele, J., De Preter, K., Pattyn, F., Poppe, B., Van Roy, N., De Paepe, A. and Speleman, F. (2002). "Accurate normalization of real-time quantitative RT-PCR data by geometric averaging of multiple internal control genes." *Genome Biology*, 3(7), RESEARCH0034. DOI: 10.1186/gb-2002-3-7-research0034

[41] Andersen, C.L., Jensen, J.L. and Orntoft, T.F. (2004). "Normalization of real-time quantitative reverse transcription-PCR data: a model-based variance estimation approach to identify genes suited for normalization." *Cancer Research*, 64(15), 5245-5250. DOI: 10.1158/0008-5472.CAN-04-0496

[42] Addo-Quaye, C., Eshoo, T.W., Bartel, D.P. and Axtell, M.J. (2008). "Endogenous siRNA and miRNA targets identified by sequencing of the *Arabidopsis* degradome." *Current Biology*, 18(10), 758-762. DOI: 10.1016/j.cub.2008.04.042

[43] German, M.A., Pillay, M., Jeong, D.H., Hetawal, A., Luo, S., Janardhanan, P., Kannan, V., Rymarquis, L.A., Nobuta, K., German, R., De Paoli, E., Lu, C., Schroth, G., Meyers, B.C. and Green, P.J. (2008). "Global identification of microRNA-target RNA pairs by parallel analysis of RNA ends." *Nature Biotechnology*, 26(8), 941-946. DOI: 10.1038/nbt1417
