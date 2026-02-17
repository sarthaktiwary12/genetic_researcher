# Experimental Validation Plan: Final Report
> **TL;DR:** A four-tiered validation plan for the bacterial exRNA germination hypothesis in spinach, ordered from cheapest/fastest/most decisive to most expensive/slowest/most mechanistic. Tier 1 (RNase treatment, EPS fractionation, dose-response) provides the go/no-go gate in 4-6 weeks. Tier 2 (qRT-PCR time-course on 15 specific targets) tests whether predicted silencing actually occurs. Tier 3 (ROS assays, hormone markers, sRNA uptake imaging) connects molecular events to physiology. Tier 4 (degradome sequencing, synthetic mimics, Arabidopsis genetic validation) provides publication-grade causal proof. The Minimum Viable Experiment Set (5 experiments) can deliver a convincing proof-of-concept in 10-12 weeks for approximately $5,000-8,000 in consumables.
>
> Last Updated: 2026-02-17

---

## Overall Strategy

The plan is designed as a sequential risk filter. Each tier is a gate:

- **Tier 1 FAIL** --> Stop. RNA is not the active agent. Redirect program.
- **Tier 1 PASS, Tier 2 FAIL** --> The RNA matters, but the predicted targets are wrong. Redesign the bioinformatics.
- **Tier 1 PASS, Tier 2 PASS** --> Strong preliminary evidence. Proceed to mechanistic validation.
- **Tier 3 + Tier 4** --> Publication-grade evidence for cross-kingdom RNAi in a crop species.

---

## TIER 1: Essential Controls (Is RNA the active molecule?)

*These experiments are non-negotiable. If they fail, the exRNA hypothesis is falsified, saving months of work and tens of thousands of dollars.*

### Experiment 1.1: RNase Treatment

| Field | Detail |
|-------|--------|
| **Priority** | CRITICAL -- do first, before everything else |
| **Difficulty** | Easy |
| **Timeline** | 1-2 weeks |
| **Cost** | ~$200 (RNase A/T1, seeds, plates) |
| **What it proves** | Whether the germination-promoting activity depends on intact RNA |
| **What it disproves** | If phenotype persists after RNase: exRNA hypothesis is falsified |

**Experimental Design:**
1. **Water control:** Spinach seeds imbibed in sterile water (baseline).
2. **M-9 EPS control:** Seeds in standard effective concentration of EPS (positive control).
3. **RNase-treated M-9:** EPS pre-treated with RNase A (10 ug/mL) + RNase T1 (25 U/mL) for 1h at 37C.
4. **Heat-inactivated RNase control:** EPS pre-treated with RNase that was heat-inactivated (95C, 15 min) before addition. This controls for the enzyme protein itself affecting germination.

**Readouts:** Germination percentage at 24h intervals for 7 days; T50 (time to 50% germination); seedling fresh weight at day 7.

**Decision rule:**
- GO: EPS+RNase germination is significantly reduced vs. EPS control (p < 0.05), and EPS+inactive RNase is not significantly different from EPS control.
- NO-GO: EPS+RNase germination is not significantly different from EPS control.

---

### Experiment 1.2: EPS Fractionation

| Field | Detail |
|-------|--------|
| **Priority** | CRITICAL |
| **Difficulty** | Moderate (requires phenol-chloroform extraction, ethanol precipitation) |
| **Timeline** | 3-4 weeks |
| **Cost** | ~$500-800 |
| **What it proves** | Whether the RNA-containing fraction is sufficient and the polysaccharide fraction is insufficient |
| **What it disproves** | If polysaccharide fraction alone replicates phenotype: elicitor effects, not RNA |

**Experimental Design:**
1. Separate crude M-9 EPS by phenol-chloroform extraction:
   - **Aqueous phase:** RNA-enriched fraction
   - **Organic/interphase:** Protein-enriched fraction
   - **Post-extraction aqueous:** Polysaccharide-enriched fraction (ethanol precipitation of depletions)
2. Reconstitute each fraction to original volume in sterile water.
3. Verify RNA content by Qubit RNA assay and Bioanalyzer (or TapeStation).
4. Test treatments: Water, whole M-9, RNA-enriched, polysaccharide-enriched, protein-enriched.

**Decision rule:**
- GO: RNA-enriched fraction recapitulates >= 70% of the whole EPS germination effect.
- NO-GO: Polysaccharide fraction alone replicates the phenotype; RNA fraction has no effect.

---

### Experiment 1.3: Dose-Response Curve

| Field | Detail |
|-------|--------|
| **Priority** | Important |
| **Difficulty** | Easy |
| **Timeline** | 1-2 weeks (can run in parallel with 1.1) |
| **Cost** | ~$150 |
| **What it proves** | That a quantitative relationship exists between EPS/exRNA concentration and phenotype |
| **What it disproves** | Flat response or non-monotonic response suggests non-specific or toxic effects |

**Experimental Design:**
- Serial dilution of M-9 EPS: 0x (water), 0.1x, 0.25x, 0.5x, 1x (standard), 2x, 5x, 10x.
- Minimum 3 biological replicates per concentration, 25 seeds per replicate.
- Measure: germination percentage (daily for 7 days), T50, seedling fresh weight at day 7.

**Expected outcome for GO:** Sigmoidal dose-response curve with clear threshold, linear range, and saturation plateau. Calculate EC50.

---

### Experiment 1.4: Iso-osmotic PEG Control (Osmopriming Test)

| Field | Detail |
|-------|--------|
| **Priority** | CRITICAL |
| **Difficulty** | Easy (requires vapor pressure osmometer access) |
| **Timeline** | 1-2 weeks (run in parallel with 1.1) |
| **Cost** | ~$200 |
| **What it proves** | Whether the phenotype is simply an osmotic/hydropriming effect |
| **What it disproves** | If PEG replicates the phenotype: the entire biological hypothesis is unnecessary |

**Experimental Design:**
1. Measure water potential (MPa) of M-9 solution by vapor pressure osmometry.
2. Prepare PEG 8000 solution at exactly the same water potential.
3. Treatments: Water, M-9 EPS, iso-osmotic PEG, 0.5x osmotic PEG, 2x osmotic PEG.

**Decision rule:**
- GO: PEG germination is not significantly different from water control; M-9 is significantly better.
- NO-GO: PEG matches M-9 performance. Effect is osmotic, not biological.

---

### Experiment 1.5: Bioinformatic Target List Cleanup

| Field | Detail |
|-------|--------|
| **Priority** | CRITICAL (computational, no wet-lab needed) |
| **Difficulty** | Moderate (bioinformatics) |
| **Timeline** | 1 week |
| **Cost** | $0 (compute time only) |
| **What it proves** | Whether the target list survives stringent filtering |
| **What it disproves** | If the list collapses to < 10 targets after filtering: the original analysis was dominated by artifacts |

**Steps:**
1. Re-map all sRNA reads to source bacterial genome(s). Discard reads with 0-1 mismatches.
2. Re-map remaining reads to the *Spinacia oleracea* transcriptome (MAPQ >= 20, no multi-mappers).
3. BLAST all predicted target transcripts against NCBI nr database. Flag and remove non-plant hits.
4. Remove all targets annotated as: transposons, retrotransposons, reverse transcriptase, cry proteins, hypothetical/unknown proteins with no plant homologs.
5. Report: original target count, post-filter target count, identity of removed targets.

**Critical targets to flag for removal:**
- cry8Ba (bacterial contamination)
- SOV2g004250.1 (RT domain, transposon_related)
- Any other non-plant or repetitive element hits

---

## TIER 2: Target Validation (Are the predicted genes silenced?)

*Assumes Tier 1 passes. Tests whether the specific molecular events predicted by the hypothesis actually occur in the seed.*

### Experiment 2.1: qRT-PCR Time-Course of Top 15 Target Genes

| Field | Detail |
|-------|--------|
| **Priority** | CRITICAL (after Tier 1 gate) |
| **Difficulty** | Moderate |
| **Timeline** | 4-6 weeks |
| **Cost** | ~$2,000-3,000 (RNA extraction, cDNA synthesis, primers, qPCR reagents) |
| **What it proves** | That predicted target transcripts are actually downregulated in treated seeds at relevant timepoints |
| **What it disproves** | If no targets are downregulated: the bioinformatic predictions are wrong, even if RNA is the active agent |

**Timepoints:** 0h (dry seed, baseline), 4h (mid-imbibition), 8h (end of soaking), 12h (post-soak), 24h (early germination), 48h (radicle emergence).

**Rationale for timepoints:**
- 0h: establishes baseline transcript abundance before any treatment.
- 4h and 8h: captures the window when exRNAs are present during soaking (the 4-8h soak period).
- 12h: early post-soak; if RNAi is occurring, target downregulation should begin here.
- 24h: the critical window preceding visible radicle emergence; maximum expected silencing effect.
- 48h: post-germination; determines whether silencing is transient or sustained.

**Target Gene Panel (15 genes):**

*High-Priority Targets (10) -- from filtered, high-confidence list:*

| # | Gene ID | Annotation | Pathway | Rationale |
|---|---------|-----------|---------|-----------|
| 1 | SOV1g020340.1 | MYB transcription factor | Signaling | Master TF; negative regulator of germination; ABA-responsive |
| 2 | SOV3g000150.1 | Ethylene receptor | Hormone signaling | Negative regulator of ethylene signaling; reduces pro-germination ethylene response |
| 3 | SOV3g033920.1 | PP2A regulatory subunit A | Signaling | Scaffold for phosphatase holoenzyme; stabilizes DELLA proteins (GA repressors) |
| 4 | SOV2g014810.1 | NAC domain-containing protein | Signaling | TF family involved in ABA signaling and dormancy maintenance |
| 5 | SOV1g033340.1 | DNA (cytosine-5)-methyltransferase | Epigenetic regulation | Maintains repressive methylation; met1 mutants show reduced dormancy |
| 6 | SOV3g038840.1 | Peroxidase | ROS/redox | Cell wall stiffening and ROS generation; inhibits radicle protrusion |
| 7 | SOV3g035520.1 | Lipoxygenase (LOX) | Hormone signaling | JA biosynthesis; ABA cross-talk; lipid peroxidation |
| 8 | SOV4g015450.1 | Histone-lysine N-methyltransferase SUVR5 | Epigenetic regulation | H3K9me2/3 writer; repressive chromatin mark; gene silencing |
| 9 | SOV5g005530.1 | MOS1-like immune regulator | Defense/immunity | Required for NLR-mediated immunity; defense resource allocation |
| 10 | SOV6g036290.1 | Protein HIRA | Epigenetic regulation | H3.3 histone chaperone; chromatin remodeling; defense-associated |

*Secondary Targets (3) -- pathway diversity and validation:*

| # | Gene ID | Annotation | Pathway | Rationale |
|---|---------|-----------|---------|-----------|
| 11 | SOV4g032870.1 | AHP-like phosphotransfer protein | Hormone signaling | Cytokinin two-component signaling relay |
| 12 | SOV2g009230.1 | Trehalose-phosphate synthase (TPS) | Metabolic | Sugar sensing / SnRK1 pathway; contradicts simple prediction (important to test) |
| 13 | SOV4g038060.1 | Zinc finger protein GIS2 | Epigenetic regulation | GATA TF; GA response repressor; chloroplast development |

*Negative Controls (2) -- filtered suspect targets (should NOT change):*

| # | Gene ID | Annotation | Pathway | Rationale |
|---|---------|-----------|---------|-----------|
| 14 | SOV2g004250.1 | Reverse transcriptase domain protein | Transposon-related | Likely mis-mapping artifact; should show no change |
| 15 | cry8Ba-associated | Bacterial crystal protein | N/A (bacterial) | Contamination indicator; should show no change (or be absent) |

**Reference Genes (3, use best 2 based on stability testing):**
- *Actin* (SpACT) -- standard housekeeping gene
- *Elongation Factor 1-alpha* (SpEF1a) -- validated stable reference across plant tissues
- *GAPDH* (SpGAPDH) -- common reference; validate stability across imbibition timepoints

**Important note on reference gene validation:** Run all three reference genes across ALL timepoints in both treatments. Use geNorm or NormFinder software to identify the two most stable references before normalizing target data. Germinating seeds undergo massive transcriptional changes; reference gene stability cannot be assumed.

**Technical specifications:**
- Minimum 3 biological replicates per treatment per timepoint (each replicate = 20-30 pooled seeds).
- RNA extraction: TRIzol or RNeasy Plant Mini Kit; DNase I treatment mandatory.
- cDNA synthesis: oligo(dT) + random hexamer priming; 500 ng total RNA input.
- qPCR: SYBR Green; 3 technical replicates per biological replicate.
- Analysis: delta-delta-Ct method; present as fold-change relative to water control at each timepoint.

**Decision rule:**
- GO: >= 6 of the 10 high-priority targets show significant downregulation (fold-change < 0.5, p < 0.05) at one or more timepoints between 8h-24h. Negative controls show no significant change.
- PARTIAL: 3-5 targets are downregulated. Some targets may be misannotated. Refine the target list.
- NO-GO: Fewer than 3 targets are downregulated. The bioinformatic target predictions are unreliable.

---

### Experiment 2.2: Hormone Pathway Marker Genes (qRT-PCR)

| Field | Detail |
|-------|--------|
| **Priority** | Important |
| **Difficulty** | Moderate (uses same cDNA as Exp 2.1) |
| **Timeline** | 2-3 weeks (after Exp 2.1 cDNA is ready) |
| **Cost** | ~$500 (additional primers and qPCR plates) |
| **What it proves** | That target silencing translates to the predicted hormonal shift |
| **What it disproves** | If targets are silenced but hormone markers are unchanged: the silencing is biologically inconsequential |

**Marker Panel (use same cDNA from Exp 2.1):**

*ABA pathway markers (expect downregulation in M-9 treated):*
- Spinach homolog of *ABI5* (ABA-responsive transcription factor)
- Spinach homolog of *RAB18* (ABA-responsive dehydrin)

*GA pathway markers (expect upregulation in M-9 treated):*
- Spinach homolog of *GA3ox* (GA biosynthesis enzyme)
- Spinach homolog of *GASA* family (GA-stimulated transcript)

*Ethylene pathway markers (expect upregulation in M-9 treated):*
- Spinach homolog of *ERF1* (ethylene response factor)

**Expected signature if hypothesis is correct:** ABA markers DOWN + GA markers UP + Ethylene markers UP in M-9-treated seeds relative to water control, particularly at the 12-24h timepoints.

---

## TIER 3: Mechanistic Validation (How does silencing cause the phenotype?)

*Assumes Tiers 1 and 2 pass. Connects molecular events to physiology.*

### Experiment 3.1: ROS and Oxidative Stress Assays

| Field | Detail |
|-------|--------|
| **Priority** | Important |
| **Difficulty** | Moderate |
| **Timeline** | 3-4 weeks |
| **Cost** | ~$800-1,200 |
| **What it proves** | That the predicted shift in ROS homeostasis (reduced cell-wall stiffening peroxidase activity, reduced LOX-derived lipid peroxidation) actually occurs |
| **What it disproves** | If ROS levels are unchanged or elevated: the growth-defense rebalancing model is wrong |

**Assays (on seeds from 0h, 12h, 24h timepoints, Water vs. M-9):**
1. **H2O2 quantification:** Amplex Red assay on seed protein extracts (quantitative) AND DAB staining on seed cross-sections (spatial).
2. **Peroxidase activity:** Guaiacol peroxidase spectrophotometric assay on protein extracts.
3. **Lipid peroxidation:** MDA (malondialdehyde) assay via TBARS method.
4. **Catalase activity:** Spectrophotometric assay on protein extracts (complementary to peroxidase).

**Expected pattern:** M-9-treated seeds show lower H2O2 accumulation, reduced peroxidase activity, and reduced MDA levels compared to water controls, particularly at 12-24h.

---

### Experiment 3.2: Small RNA Uptake Visualization

| Field | Detail |
|-------|--------|
| **Priority** | Nice-to-have (but essential for high-impact publication) |
| **Difficulty** | Hard |
| **Timeline** | 8-12 weeks |
| **Cost** | ~$3,000-5,000 (Cy3-labeled RNA synthesis, confocal microscopy time) |
| **What it proves** | That exogenous bacterial RNA physically enters seed tissues (embryo, aleurone), not just the seed coat |
| **What it disproves** | If signal is confined to seed coat: the effect may be indirect (receptor-mediated, not RNAi) |

**Experimental Design:**
1. **Method A (fluorescent spike-in):** Synthesize a known abundant bacterial sRNA with 5' Cy3 label. Spike into EPS at 100 nM. Soak seeds for 4-8h. Fix, section, and image by confocal microscopy at 0, 4, 8, 12, and 24h.
2. **Controls:** Cy3-labeled scrambled RNA (same delivery, no target); Cy3-labeled RNA without EPS matrix (tests EPS-facilitated uptake).
3. **Counterstain:** DAPI for nuclei; calcofluor white for cell walls.

**Key question:** Is Cy3 signal inside the embryo cells, or stuck on the seed coat?

---

## TIER 4: Advanced Validation (Can we prove causality?)

*Assumes Tiers 1-3 are largely successful. Provides definitive, publication-grade evidence.*

### Experiment 4.1: Degradome / PARE Sequencing

| Field | Detail |
|-------|--------|
| **Priority** | Nice-to-have |
| **Difficulty** | Hard (specialized library prep + bioinformatics) |
| **Timeline** | 12-16 weeks |
| **Cost** | ~$5,000-8,000 (library prep, sequencing, analysis) |
| **What it proves** | Definitive proof of RNAi-mediated cleavage: identifies the exact nucleotide position where RISC cuts the target mRNA, guided by the bacterial exRNA |
| **What it disproves** | If no cleavage peaks at predicted sites: silencing may occur via translational repression (not disproven) or the mechanism is not RNAi |

**Experimental Design:**
1. Construct degradome (PARE) libraries from M-9-treated seeds at 12h and 24h timepoints.
2. Sequence 5' ends of uncapped, polyadenylated RNAs.
3. Map reads to spinach transcriptome; search for T-plots showing cleavage peaks at positions 10-11 nt from the 5' end of the aligned bacterial sRNA (the canonical AGO cleavage site).
4. Focus analysis on the 10 high-priority targets from Exp 2.1.

---

### Experiment 4.2: Synthetic RNA Mimics

| Field | Detail |
|-------|--------|
| **Priority** | Nice-to-have |
| **Difficulty** | Hard (delivery is the bottleneck) |
| **Timeline** | 8-10 weeks |
| **Cost** | ~$3,000-5,000 |
| **What it proves** | That defined synthetic RNAs targeting specific genes can phenocopy the EPS effect, proving sufficiency |
| **What it disproves** | If synthetic mimics fail: either delivery failed, or the cocktail effect of multiple exRNAs is required |

**Experimental Design:**
1. Synthesize 21-nt siRNA duplexes matching the top 3 bacterial exRNA sequences that target:
   - **SOV1g020340.1** (MYB TF) -- hormonal master regulator
   - **SOV3g000150.1** (Ethylene receptor) -- strongest mechanistic rationale
   - **SOV1g033340.1** (DNA methyltransferase) -- epigenetic hub
2. Test individually (100 nM each) and as a cocktail (100 nM each, 300 nM total).
3. Test with and without EPS matrix to assess whether EPS facilitates delivery.
4. Include scrambled siRNA control at same total concentration.
5. Delivery methods to test: simple imbibition, imbibition with 0.01% Silwet L-77 (surfactant), imbibition in EPS matrix.

---

### Experiment 4.3: Genetic Validation in Arabidopsis

| Field | Detail |
|-------|--------|
| **Priority** | Nice-to-have |
| **Difficulty** | Moderate (ordering mutants, growing plants) |
| **Timeline** | 6-8 weeks |
| **Cost** | ~$500-1,000 (seed stocks, growth chamber time) |
| **What it proves** | That loss-of-function of target gene homologs in a model system produces faster/better germination, validating the gene's predicted role |
| **What it disproves** | If mutant has no germination phenotype: functional divergence between species, or the gene is not a germination regulator |

**Experimental Design:**
1. Obtain T-DNA insertion lines from ABRC for Arabidopsis homologs of:
   - MYB TF (e.g., AtMYB96, AtMYB33 -- closest homologs to SOV1g020340.1)
   - Ethylene receptor (etr1-1, ers1 -- loss-of-function alleles available)
   - DNA methyltransferase (met1 -- well-characterized reduced dormancy)
2. Germination assays: WT Col-0 vs. mutants on water-agar plates at 22C (standard) and under mild ABA stress (0.5 uM ABA) to sensitize the assay.
3. Readouts: germination percentage at 24h intervals, T50, seedling fresh weight.

**Most likely to succeed:** The *met1* and *etr1* mutants have published germination phenotypes (reduced dormancy / faster germination). If the spinach targets are true orthologs, these Arabidopsis mutants should recapitulate the prediction.

---

## Minimum Viable Experiment Set

*If budget and time are constrained, these 5 experiments provide the most convincing proof-of-concept with the least investment.*

### The 5 Experiments That Matter Most

| Rank | Experiment | What It Answers | Timeline | Est. Cost | Combined Verdict |
|------|-----------|----------------|----------|-----------|-----------------|
| **1** | **1.1: RNase Treatment** | Is RNA the active molecule? | 2 weeks | $200 | GO/NO-GO gate for entire program |
| **2** | **1.4: Iso-osmotic PEG Control** | Is it just osmopriming? | 2 weeks (parallel with #1) | $200 | Rules out the most parsimonious alternative |
| **3** | **1.5: Bioinformatic Cleanup** | Is the target list credible? | 1 week (parallel) | $0 | Removes contamination artifacts; produces the clean target list needed for #4 |
| **4** | **2.1: qRT-PCR Time-Course** (top 10 targets) | Are predicted targets actually silenced? | 4-6 weeks | $2,500 | Molecular validation of the RNAi mechanism |
| **5** | **1.2: EPS Fractionation** | Is the RNA fraction sufficient? | 3-4 weeks (parallel with #4) | $700 | Distinguishes RNA from polysaccharide activity |

**Total timeline:** 10-12 weeks (with parallelization).
**Total estimated cost:** ~$3,600 in consumables (excludes equipment access and labor).

### What These 5 Experiments Prove Together

If ALL 5 pass:
- The phenotype depends on intact RNA (not osmotic effects, not polysaccharides).
- The RNA-containing fraction is sufficient.
- The target list is bioinformatically sound.
- Specific predicted target mRNAs are downregulated in the seed during the relevant time window.

This constitutes a strong preliminary case for cross-kingdom RNAi-mediated germination enhancement -- enough for a compelling grant application, a preprint, or a decision to invest in Tiers 3-4.

If ANY of the first 3 fail: Stop. Redirect. The money saved on Tiers 2-4 justifies the investment in Tier 1 controls.

---

## Timeline Summary (Gantt-style)

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

**Gate 1 (Week 3):** RNase + PEG + bioinformatic results in hand. Go/no-go on the entire program.
**Gate 2 (Week 6):** Fractionation and dose-response complete. Full Tier 1 package.
**Data Package (Week 12):** Complete Tier 1 + Tier 2 results. Decision point for Tier 3-4 investment.

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| RNase treatment does not abolish phenotype | Medium-High | Program-ending | Accept the result; redirect to characterizing polysaccharide/osmotic mechanism |
| PEG control replicates phenotype | Medium | Program-ending | Accept the result; the mechanism is osmopriming, not RNAi |
| Reference genes are unstable during germination | Medium | Invalidates qRT-PCR | Run 3 reference genes; validate with geNorm/NormFinder before analyzing targets |
| RNA extraction from dry/imbibing seeds is poor quality | Medium | Delays Tier 2 | Use TRIzol with extended homogenization; add PVP-40 to counter polyphenolics |
| Spinach genome annotation is incomplete | Low-Medium | Some targets may be mis-identified | Cross-reference all targets with Arabidopsis TAIR annotations via reciprocal BLAST |
| Synthetic RNA degrades before entering seed | High | Complicates Tier 4 | Use 2'-O-methyl modified RNA for stability; test EPS as delivery matrix |
