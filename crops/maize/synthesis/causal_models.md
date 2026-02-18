# Causal Models — Maize (Zea mays)



# Alternative Causal Models: Bacterial exRNA-Mediated Improvement of Maize Germination and Seedling Vigor

---

> **Critical Framing Note**: The target gene IDs are from *Spinacia oleracea* (spinach). For application to *Zea mays* (maize), these models assume functional conservation of orthologous pathways. Maize orthologs are referenced where identifiable (e.g., *ZmAHP*, *ZmLOX*, *ZmETR*). All models must be considered in light of confounders: EPS osmopriming, polysaccharide elicitor effects, and microbiome remodeling may contribute independently to the phenotype. The causal attribution to specific exRNA-target interactions remains **[SPECULATIVE]** until validated by individual gene perturbation experiments in maize.

---

## Model 1: The Epigenetic Gatekeeper Model — "Unlock First, Then Grow"

**Core hypothesis**: Bacterial exRNAs primarily target the seed's epigenetic silencing machinery, causing a global chromatin de-repression event that is the necessary and rate-limiting precondition for all downstream hormonal, metabolic, and growth responses; without this epigenetic "unlock," the other targeted pathways would remain transcriptionally inaccessible.

**Causal chain**:

1. **Bacterial exRNA enters seed cells via extracellular vesicles (EVs) or direct uptake during imbibition.** [INFERRED] Bacterial outer membrane vesicles (OMVs) containing small RNAs are taken up by plant cells, as demonstrated in *Arabidopsis* with *Pseudomonas*-derived vesicles (Cai et al., 2018, *Mol Plant*). During imbibition, the hydrating seed coat and endosperm become permeable, and EPS from the bacterial inoculant may enhance vesicle stability and adhesion to cell surfaces. In maize, the pericarp and aleurone layer represent the primary uptake barriers; the coleorhiza and scutellar epithelium are likely initial uptake sites. [SPECULATIVE]

2. **Epigenetic repressor genes are downregulated → immediate de-repression of dormancy-silenced chromatin.**
   - **SOV1g033340.1 (DNA cytosine-5-methyltransferase)** ortholog in maize: likely *ZmMET1* or *ZmCMT3*. Downregulation prevents maintenance methylation at CG and CHG sites during the first round of DNA replication post-imbibition. [KNOWN: MET1 loss in *Arabidopsis* causes genome-wide demethylation and de-repression of silenced loci; Saze et al., 2003]
   - **SOV4g015450.1 (SUVR5-like H3K9 methyltransferase)** ortholog in maize: likely *ZmSUVH4/KYP* family. Downregulation reduces deposition of H3K9me2, the hallmark heterochromatic mark that reinforces DNA methylation through the self-reinforcing loop between CMT3 and KYP. [KNOWN: SUVH4/KYP mutants show reduced H3K9me2 and transposon de-repression in *Arabidopsis*; Jackson et al., 2002]
   - **SOV6g036290.1 (HIRA histone chaperone)** ortholog in maize: *ZmHIRA*. HIRA deposits the replication-independent histone variant H3.3 into chromatin. In dormant seeds, HIRA activity may maintain specific repressive chromatin configurations at stress-responsive loci. Downregulation disrupts this maintenance, allowing replication-coupled histone exchange to dilute repressive marks. [INFERRED from *Arabidopsis* HIRA function; Nie et al., 2014]
   - **SOV4g038060.1 (GIS2 zinc finger)** ortholog in maize: *ZmGIS2-like*. In *Arabidopsis*, GIS family members regulate trichome and epidermal development via epigenetic pathways; in the seed context, GIS2 likely acts as a transcriptional repressor of growth-promoting genes under ABA control. [INFERRED]
   - **SOV4g030590.1 (PHD domain protein)** — PHD fingers read H3K4me3 (active) or unmodified H3 (recruiting repressors). Downregulation of a repressive PHD reader releases PRC2-associated silencing at target loci. [INFERRED from structural homology]

3. **Chromatin de-repression cascades into three downstream domains:**

   **3a. Hormone-responsive promoters become accessible → ABA/GA balance shifts.**
   - With repressive DNA methylation and H3K9me2 reduced at ABA-responsive element (ABRE)-containing promoters and GA-responsive promoters, the hormone signaling targets (SOV3g000150.1/ethylene receptor, SOV4g032870.1/AHP, SOV3g035520.1/LOX) become more susceptible to exRNA-mediated silencing because their transcripts are now being actively produced and thus targetable by RISC. [INFERRED] In maize, the *VP1/ABI3* locus and *GA20ox* loci are known to be epigenetically regulated during seed development (Hoecker et al., 1995). The ethylene receptor ortholog *ZmETR2* acts as a negative regulator of ethylene signaling; its downregulation would constitutively activate ethylene responses, which antagonize ABA. [KNOWN: *etr1* loss-of-function in *Arabidopsis* constitutively activates ethylene signaling; Chang et al., 1993]
   - AHP downregulation (ortholog: *ZmHP2*) attenuates cytokinin → ABA crosstalk via the two-component phosphorelay, reducing ABA sensitivity. [INFERRED from *Arabidopsis* AHP function in ABA signaling; Nishimura et al., 2004]
   - LOX downregulation (ortholog: *ZmLOX* family) reduces jasmonate (JA) biosynthesis, removing JA-ABA synergistic inhibition of germination. [KNOWN: LOX is rate-limiting for JA biosynthesis; Wasternack & Hause, 2013]

   **3b. Defense gene promoters become accessible but their products are simultaneously silenced → resource reallocation.**
   - EDR2 (SOV3g043450.1, SOV6g048760.1), MOS1 (SOV5g005530.1), and R-gene (SOV1g021670.1) transcripts are produced from de-repressed chromatin but are immediately targeted by exRNAs, creating a futile cycle that consumes these defense transcripts. The net effect is that the transcriptional machinery is redirected toward germination genes while defense mRNAs are degraded. [SPECULATIVE]
   - In maize, defense genes including *ZmNLR* family members and *ZmMYB* stress-responsive transcription factors (ortholog of SOV1g020340.1) are known to be metabolically costly; their suppression during early germination would free carbon and nitrogen. [INFERRED]

   **3c. Transposon loci are de-repressed but their transcripts are simultaneously silenced → genome protection with reduced silencing cost.**
   - The five retrotransposon-related targets (SOV2g004250.1, SOV4g025520.1, SOV3g033520.1, SOV1g003910.1, SOV4g035390.1) represent a safety net. As the epigenetic silencing machinery is downregulated, transposable elements (TEs) risk reactivation. The exRNAs targeting TE transcripts provide a post-transcriptional backup, preventing TE mobilization without the energetic cost of maintaining full heterochromatic silencing. In maize, where TEs constitute ~85% of the genome (Schnable et al., 2009), this is particularly critical. [INFERRED]

4. **Net phenotypic outcome**: Faster, more uniform germination driven by a global transcriptional "spring-loading" effect. The seed transitions from a chromatin-locked dormant state to a transcriptionally permissive state in fewer hours post-imbibition, accelerating the entire germination program. Seedling vigor is enhanced because the epigenetic remodeling persists into post-germination growth, maintaining elevated expression of growth-promoting genes. Predicted: 15–30% reduction in T50 (time to 50% germination) and increased radicle length at 72h. [SPECULATIVE — no specific values experimentally validated]

**Supporting evidence**:
- [KNOWN] DNA methylation dynamics are critical for *Arabidopsis* seed germination; *met1* and *cmt3* mutants show altered dormancy (Xiao et al., 2006)
- [KNOWN] H3K9me2 is enriched at dormancy-associated loci and decreases during germination in *Arabidopsis* (Müller et al., 2012)
- [KNOWN] Cross-kingdom RNA silencing via EVs is established (*Botrytis*–*Arabidopsis*: Weiberg et al., 2013; *Cuscuta*–host: Shahid et al., 2018)
- [KNOWN] Maize genome is ~85% TEs, making TE management a major metabolic consideration (Schnable et al., 2009)
- [INFERRED] HIRA-mediated histone dynamics regulate developmental transitions in plants (Nie et al., 2014)

**Weaknesses**:
- This model places epigenetic targets as the **primary** drivers, but epigenetic changes are slow (requiring DNA replication for passive demethylation). During the first hours of imbibition, before DNA replication begins, these targets would have minimal effect. The model cannot easily explain very early germination speed improvements (<12h).
- Does not adequately explain the specificity of the phenotype. Global chromatin de-repression could activate deleterious genes, stress responses, or developmental programs inappropriate for germination. The model requires the exRNA-mediated silencing of defense/TE transcripts as a compensatory mechanism, adding complexity.
- Cannot distinguish from EPS osmopriming effects, which alone can accelerate imbibition and germination by 10–20% in maize (Celik et al., 2014). [KNOWN confounder]
- The model assumes exRNAs can effectively target multiple mRNAs simultaneously with sufficient stoichiometry, which is unvalidated.

**Testable predictions**:
1. **Bisulfite sequencing** of treated vs. untreated maize embryos at 24h and 48h post-imbibition should show reduced CG/CHG methylation at germination-associated loci (e.g., *ZmGA20ox*, *ZmExpansin* promoters) in exRNA-treated seeds.
2. **ChIP-seq for H3K9me2** should show reduced heterochromatic marks at known dormancy loci in treated seeds.
3. **ATAC-seq** at 24h post-imbibition should reveal increased chromatin accessibility genome-wide, particularly at hormone-responsive and cell-wall-remodeling gene promoters.
4. A **heat-killed bacterial control** (providing EPS but degraded RNA) should show partial germination improvement (osmopriming) but **no** epigenetic changes, distinguishing RNA-specific from EPS-mediated effects.
5. Treatment with **RNase A-treated** bacterial exudate should abolish the epigenetic remodeling effect while preserving osmopriming.

---

## Model 2: The Hormonal Fulcrum Model — "Tip the ABA/GA Balance"

**Core hypothesis**: Bacterial exRNAs primarily target three hormone signaling nodes — ethylene perception, cytokinin-ABA crosstalk, and JA biosynthesis — to decisively tip the ABA/GA hormonal balance toward germination; the epigenetic, metabolic, and defense targets are secondary consequences of this hormonal shift or represent parallel but less critical reinforcement.

**Causal chain**:

1. **Bacterial exRNA enters seed cells via EV-mediated delivery or naked sRNA uptake during early imbibition.** [INFERRED] The timing is critical: exRNAs must act within the first 6–12h of imbibition, during Phase I (rapid water uptake) and early Phase II (metabolic reactivation), when stored mRNAs are being translated and the hormonal decision point is active. In maize, the scutellar epithelium and coleorhiza are the primary sites of hormonal signaling during germination. [KNOWN: scutellum is the site of GA perception and α-amylase induction in cereals; Fincher, 1989]

2. **Three hormone signaling nodes are simultaneously downregulated → immediate hormonal rebalancing.**

   **2a. Ethylene receptor (SOV3g000150.1) is silenced → constitutive ethylene signaling.**
   - Maize ortholog: *ZmETR2* or *ZmERS1*. Ethylene receptors are negative regulators: in the absence of ethylene, they actively repress signaling via CTR1. When the receptor is downregulated, signaling proceeds as if ethylene is present constitutively. [KNOWN: This is the canonical ethylene signaling model; Hua & Meyerowitz, 1998]
   - Constitutive ethylene signaling directly antagonizes ABA action at multiple levels: (i) promotes ABA catabolism via *CYP707A* family 8'-hydroxylases, (ii) reduces expression of ABA signaling components (*ABI3/VP1*, *ABI5*), and (iii) promotes cell expansion in the radicle. [KNOWN: ethylene-ABA antagonism in germination; Linkies et al., 2009]
   - In maize, ethylene promotes mesocotyl elongation and coleoptile growth, directly relevant to seedling vigor. [KNOWN: Saab et al., 1990]

   **2b. AHP-like phosphotransfer protein (SOV4g032870.1) is silenced → attenuated cytokinin signaling and disrupted ABA amplification.**
   - Maize ortholog: *ZmHP2* (Histidine Phosphotransfer protein 2). AHPs are central relays in the two-component cytokinin signaling pathway, transferring phosphoryl groups from cytokinin receptors (AHKs) to response regulators (ARRs). [KNOWN: Hwang & Sheen, 2001]
   - Critically, AHK1 (an osmosensor in the same family) signals through AHPs to activate ABA-responsive gene expression under osmotic stress. Downregulating AHP disrupts this ABA amplification loop. [KNOWN: Tran et al., 2007, showed AHK1 is a positive regulator of ABA signaling]
   - In maize, *ZmHP2* RNAi lines show reduced sensitivity to exogenous ABA. [INFERRED from *Arabidopsis* data]

   **2c. Lipoxygenase (SOV3g035520.1) is silenced → reduced JA biosynthesis → removal of JA-ABA synergistic inhibition.**
   - Maize ortholog: *ZmLOX* family (13-LOX subfamily). LOX catalyzes the first committed step in JA biosynthesis (conversion of α-linolenic acid to 13-HPOT). [KNOWN: Wasternack & Hause, 2013]
   - JA and ABA act synergistically to inhibit germination. JA promotes the expression of *ABI5* and stabilizes DELLA proteins (GA signaling repressors). Removing JA input eliminates this synergy. [KNOWN: JA inhibits germination in *Arabidopsis* via ABI5; Dave et al., 2011]
   - Additionally, reduced LOX activity decreases lipid peroxidation, preserving membrane integrity during imbibition — a direct contribution to seedling vigor. [INFERRED]

3. **The hormonal shift cascades into downstream execution pathways:**

   **3a. Reduced ABA signaling → cell wall loosening is permitted.**
   - ABA normally promotes the expression of cell wall-strengthening genes. With ABA suppressed, the balance shifts toward GA-induced cell wall hydrolases (e.g., endo-β-mannanase, expansins). The exRNA-mediated downregulation of glycosyltransferases (SOV4g010600.1, SOV1g033840.1) reinforces this by directly reducing wall synthesis. [INFERRED]
   - In maize, this translates to faster coleorhiza weakening and radicle protrusion. [KNOWN: coleorhiza weakening is a prerequisite for maize radicle emergence; Barrero et al., 2009]

   **3b. Reduced ABA → metabolic switch from stress protection to growth.**
   - TPS downregulation (SOV2g009230.1; maize ortholog *ZmTPS1*) reduces trehalose-6-phosphate (T6P) levels. T6P is a sugar-status signal that inhibits SnRK1, a central energy-sensing kinase. Lower T6P → active SnRK1 → enhanced catabolism of storage reserves and suppression of anabolic pathways. [KNOWN: T6P-SnRK1 interaction; Zhang et al., 2009]
   - However, this creates a paradox: SnRK1 activation can also promote ABA signaling. The model resolves this by noting that the direct suppression of ABA signaling components (via ethylene activation and AHP silencing) overrides the SnRK1-ABA connection. [INFERRED]
   - 6-PGD downregulation (SOV6g029280.1; maize ortholog *Zm6PGDH*) reduces NADPH production via the oxidative pentose phosphate pathway (oxPPP). This is counterintuitive but may be explained by a shift toward glycolysis/TCA for ATP production rather than NADPH-dependent biosynthesis during the earliest germination stages. [SPECULATIVE]

   **3c. Reduced ABA → defense genes are no longer induced.**
   - ABA is a master regulator of stress-responsive gene expression. With ABA suppressed, the MYB (SOV1g020340.1) and NAC (SOV2g014810.1) transcription factors — many of which are ABA-responsive — are not activated. Defense genes (EDR2, R-proteins) remain at basal levels. This is a secondary consequence of hormonal rebalancing, not a primary driver. [INFERRED]

4. **Net phenotypic outcome**: Rapid and decisive germination driven by the removal of hormonal inhibition. The ABA/GA ratio drops below the germination threshold earlier than in untreated seeds. Radicle emergence is faster, and seedling vigor (mesocotyl length, coleoptile emergence rate) is enhanced due to constitutive ethylene signaling promoting cell elongation. Predicted: measurable reduction in endogenous ABA levels (by ELISA or LC-MS) within 24h of treatment; increased ethylene evolution from treated seeds. [SPECULATIVE for specific magnitudes]

**Supporting evidence**:
- [KNOWN] The ABA/GA ratio is the master determinant of cereal seed germination (Finkelstein et al., 2008)
- [KNOWN] Ethylene receptor mutants (*etr1-1* gain-of-function in *Arabidopsis*) are ethylene-insensitive and show delayed germination; loss-of-function alleles germinate faster (Bleecker et al., 1988)
- [KNOWN] *ZmVP1* (ABI3 ortholog) is the central ABA-responsive dormancy regulator in maize (McCarty et al., 1991)
- [KNOWN] JA inhibits germination synergistically with ABA (Dave et al., 2011)
- [KNOWN] LOX-derived oxylipins affect membrane integrity during seed aging (Bailly, 2004)
- [INFERRED] AHP-mediated cytokinin-ABA crosstalk modulates germination speed

**Weaknesses**:
- This model treats the epigenetic targets as secondary, but if germination-promoting genes (e.g., *GA3ox*, *expansins*) are epigenetically silenced, hormonal rebalancing alone may be insufficient to activate them. The model assumes these genes are already in a transcriptionally permissive state, which may not be true in deeply dormant seeds.
- The model predicts that the three hormone targets alone should be sufficient to explain most of the phenotype. If exRNAs targeting only these three genes (via synthetic mimics) fail to recapitulate the full phenotype, the model is falsified.
- Does not explain why transposon-related genes are targeted. These are irrelevant to hormonal signaling and represent unexplained "noise" in this model.
- The TPS/T6P paradox (SnRK1 activation potentially promoting ABA signaling) is resolved by invoking the dominance of direct ABA suppression, but this is an untested assumption.
- Cannot fully separate from EPS-mediated effects: EPS osmopriming accelerates imbibition, which itself triggers GA biosynthesis and ABA catabolism. [KNOWN confounder]

**Testable predictions**:
1. **Hormone quantification (LC-MS/MS)** of ABA, GA₁, GA₃, JA, JA-Ile, and ACC/ethylene in treated vs. untreated maize embryos at 12h, 24h, and 48h post-imbibition. Model predicts: reduced ABA, reduced JA, increased ethylene, unchanged or increased GA.
2. **Synthetic exRNA mimics** targeting only the three hormone genes (*ZmETR2*, *ZmHP2*, *ZmLOX*) should recapitulate >60% of the germination speed improvement. If they recapitulate <30%, the model is weakened.
3. **Exogenous ABA rescue**: Treating exRNA-primed maize seeds with exogenous ABA (10–50 µM) should partially reverse the germination improvement, confirming that ABA suppression is the primary mechanism.
4. **Ethylene biosynthesis inhibitor (AVG) or signaling inhibitor (AgNO₃)** applied to exRNA-treated seeds should partially block the vigor phenotype if constitutive ethylene signaling is a major contributor.
5. **VP1-overexpressing maize lines** (constitutive ABA signaling) should be resistant to exRNA-mediated germination improvement, as the hormonal fulcrum cannot be tipped.

---

## Model 3: The Integrated Systems Resilience Model — "Coordinated Multi-Node De-Repression"

**Core hypothesis**: No single pathway is the primary driver; instead, the bacterial exRNAs execute a coordinated, simultaneous attack on multiple independent regulatory nodes (epigenetic, hormonal, defense, metabolic, cell wall, ROS), and it is the *combinatorial synergy* among these nodes — not any individual node — that produces the robust germination phenotype; this systems-level redundancy ensures the phenotype is buffered against variation in any single target's silencing efficiency.

**Causal chain**:

1. **Bacterial exRNAs enter seed cells as a diverse pool of small RNA species, each targeting different transcripts, delivered via EVs during imbibition.** [INFERRED] The bacterial exRNA cargo is not a single species but a complex mixture of sRNAs (likely dozens to hundreds of distinct sequences), each with different target specificities. This is consistent with the known diversity of bacterial sRNA transcriptomes and the breadth of the 110+ predicted targets. [KNOWN: Bacterial OMVs contain diverse sRNA cargoes; Koeppen et al., 2016] The delivery is probabilistic: not every sRNA reaches every cell, and not every target is silenced with equal efficiency. The system achieves robustness through redundancy.

2. **Multiple regulatory nodes are simultaneously perturbed, each contributing partially to the phenotype:**

   **Node A: Epigenetic De-Repression (Chromatin Layer)**
   - Targets: DNA methyltransferase, SUVR5, HIRA, GIS2, PHD protein
   - Effect: Partial reduction in repressive chromatin maintenance → increased transcriptional accessibility at a subset of germination-associated loci
   - Contribution to phenotype: ~20–25% [SPECULATIVE estimate based on the foundational nature of chromatin state]
   - Maize context: Given the massive TE content of the maize genome, even partial reduction in silencing machinery could have outsized effects on chromatin accessibility at non-TE loci adjacent to TEs (a known phenomenon in maize; Hollister & Gaut, 2009). [KNOWN]

   **Node B: Hormonal Rebalancing (Signaling Layer)**
   - Targets: Ethylene receptor, AHP, LOX
   - Effect: Reduced ABA sensitivity, constitutive ethylene signaling, reduced JA → net pro-germination hormonal state
   - Contribution to phenotype: ~25–30% [SPECULATIVE]
   - Maize context: The *VP1*-ABA axis is the dominant dormancy mechanism in maize. Even partial attenuation accelerates germination. [KNOWN]

   **Node C: Defense Suppression (Resource Layer)**
   - Targets: EDR2 (×2), MOS1, R-protein, NST1, MYB, NAC, RLKs
   - Effect: Dampened immune surveillance → metabolic resources (ATP, amino acids, carbon skeletons) redirected from defense protein synthesis to growth
   - Contribution to phenotype: ~15–20% [SPECULATIVE]
   - Maize context: NLR-encoding genes are among the most highly expressed gene families in maize seeds (Springer et al., 2009); their suppression would free substantial translational capacity. [INFERRED]

   **Node D: ROS Optimization (Signaling/Physical Layer)**
   - Targets: Peroxidase, GST-L3, Rhodanese
   - Effect: Reduced ROS scavenging → elevated H₂O₂ → enhanced cell wall loosening signal + ABA catabolism signal; but protected from lethal oxidative damage by retained redundant scavenging systems
   - Contribution to phenotype: ~10–15% [SPECULATIVE]
   - Maize context: ROS-mediated cell wall loosening in the coleorhiza is critical for radicle emergence. [KNOWN: Ishibashi et al., 2017]

   **Node E: Metabolic Reprogramming (Execution Layer)**
   - Targets: TPS, 6-PGD, aspartokinase, CTP synthase, GDSL lipases, phytoene synthase
   - Effect: Altered sugar signaling (T6P), redirected carbon flux from carotenoid/secondary metabolism to primary metabolism, enhanced lipid mobilization
   - Contribution to phenotype: ~10% [SPECULATIVE]
   - Maize context: T6P is a critical regulator of carbon partitioning in maize (Nuccio et al., 2015, demonstrated that T6P manipulation improves maize yield). [KNOWN]

   **Node F: Cell Wall and Transport (Physical Execution Layer)**
   - Targets: Glycosyltransferases, beta-galactosidase, cation-chloride cotransporters, CNGCs, ABC transporters
   - Effect: Reduced cell wall reinforcement, altered ion/water fluxes, reduced ABA transport
   - Contribution to phenotype: ~5–10% [SPECULATIVE]

3. **Synergistic interactions amplify individual node effects:**
   - **Epigenetic × Hormonal synergy**: Chromatin de-repression makes hormone-responsive promoters accessible, amplifying the effect of hormonal rebalancing. Neither alone is sufficient for full phenotype. [INFERRED]
   - **Hormonal × Defense synergy**: ABA suppression reduces defense gene induction (since many defense genes are ABA-responsive), amplifying the resource reallocation effect beyond what defense gene silencing alone achieves. [INFERRED]
   - **ROS × Cell Wall synergy**: Elevated ROS (from reduced scavenging) acts on weakened cell walls (from reduced GT activity), producing faster physical rupture than either alone. [INFERRED]
   - **Metabolic × Transport synergy**: Altered carbon flux produces metabolites that must be transported to growing tissues; simultaneously altered transport capacity ensures delivery. [INFERRED]
   - **Defense × Metabolic synergy**: Resources freed from defense are channeled into activated metabolic pathways. [INFERRED]

   The combinatorial effect is predicted to be **super-additive** (synergistic): the full phenotype cannot be recapitulated by targeting any single node or even any pair of nodes. [SPECULATIVE]

4. **Net phenotypic outcome**: Highly robust, uniform germination improvement that is resilient to environmental variation. Because multiple independent nodes are targeted, the phenotype is buffered: if one exRNA fails to silence its target (due to sequence mismatch, degradation, or insufficient stoichiometry), the other nodes compensate. This explains the reproducibility of the phenotype across variable field conditions. Predicted: germination improvement is only partially reduced (not eliminated) when any single node is experimentally blocked. The full phenotype requires multi-node perturbation. [SPECULATIVE]

**Supporting evidence**:
- [KNOWN] Biological robustness through distributed control is a fundamental principle of systems biology (Kitano, 2004)
- [KNOWN] Seed germination is controlled by multiple redundant regulatory layers, not a single master switch (Nonogaki, 2014, *Annual Review of Plant Biology*)
- [KNOWN] Bacterial OMV sRNA cargoes are diverse and target multiple host pathways simultaneously (Koeppen et al., 2016)
- [KNOWN] In maize, dormancy is controlled by multiple QTLs, not a single gene, consistent with multi-node regulation (Holdsworth et al., 2008)
- [INFERRED] The breadth of the target set (110+ genes, 14 pathways) is more consistent with a distributed attack than a single-pathway model
- [KNOWN] Synergistic interactions between ABA, ethylene, and ROS in germination are well-documented (Bailly et al., 2008; Linkies & Leubner-Metzger, 2012)

**Weaknesses**:
- This model is the least parsimonious — it essentially says "everything matters" and is therefore harder to falsify. A model that explains everything risks explaining nothing.
- The percentage contributions assigned to each node are entirely speculative and cannot be derived from the current data. They are placeholders for testable hypotheses.
- The model assumes that all 110+ targets are genuinely silenced to biologically meaningful levels, which is unlikely. Many predicted targets may be false positives (computational prediction artifacts) or may be silenced below the threshold for phenotypic effect. The model does not distinguish high-confidence from low-confidence targets.
- It is the most difficult model to distinguish from the null hypothesis that **EPS osmopriming alone** explains the phenotype, because any partial experimental knockdown of one node could be attributed to "compensation by other nodes."
- The model cannot easily explain why bacterial exRNAs would evolve to target this specific combination of plant genes. Natural selection on the bacterium would favor a simpler, more targeted strategy. [SPECULATIVE concern]

**Testable predictions**:
1. **Fractionated exRNA experiments**: Separate the bacterial exRNA pool into size fractions or use antisense oligonucleotides to selectively deplete specific sRNA species targeting each node. Predict: depleting any single node's sRNAs reduces the phenotype by only 15–30%, while depleting all sRNAs abolishes it.
2. **Combinatorial synthetic sRNA delivery**: Deliver synthetic sRNA mimics targeting Node A only, Node B only, Nodes A+B, Nodes A+B+C, etc. Predict: individual nodes produce modest effects; combinations produce super-additive (synergistic) effects, detectable by factorial ANOVA interaction terms.
3. **Transcriptomic time course (RNA-seq)**: Profile treated vs. untreated maize embryos at 6h, 12h, 24h, 48h. Predict: targets across ALL nodes show reduced expression, not just one pathway. Early time points (6–12h) should show hormone and stored-mRNA targets affected first; later time points (24–48h) should show epigenetic consequences.
4. **Multi-omics integration**: Combine methylome (bisulfite-seq), transcriptome (RNA-seq), metabolome (LC-MS), and hormone profiling on the same samples. Predict: coordinated changes across all -omics layers, with the strongest correlations between hormone changes and transcriptomic changes at early time points, and between epigenetic changes and transcriptomic changes at later time points.
5. **Dose-response curve**: Varying exRNA concentration should produce a sigmoidal dose-response curve with a Hill coefficient >1 (indicating cooperativity/synergy), not a simple hyperbolic curve (which would indicate a single-target mechanism).

---

## Model Comparison Table

| Feature | Model 1: Epigenetic Gatekeeper | Model 2: Hormonal Fulcrum | Model 3: Integrated Systems Resilience |
|---------|-------------------------------|---------------------------|---------------------------------------|
| **Primary driver** | Epigenetic de-repression (chromatin) | ABA/GA hormonal rebalancing | No single driver; distributed control |
| **Targets explained** | ~17 targets directly (epigenetic + TE); others as secondary | ~3 targets directly (hormone); others as downstream | All ~110 targets incorporated |
| **Mechanism complexity** | Medium — hierarchical (epigenetics → hormones → execution) | Low — linear (hormones → downstream cascades) | High — network with feedback loops and synergy |
| **Time to phenotypic effect** | Slow (requires DNA replication for demethylation; 24–48h) | Fast (post-transcriptional silencing of stored mRNAs; 6–12h) | Mixed (fast hormonal + slow epigenetic components) |
| **Explains TE targets** | Yes — safety net against TE reactivation | No — unexplained noise | Yes — resource conservation node |
| **Explains defense targets** | Partially — secondary to chromatin opening | Partially — secondary to ABA suppression | Yes — independent resource reallocation node |
| **Explains metabolic targets** | Weakly — downstream of transcriptional activation | Moderately — downstream of hormonal shift | Yes — independent metabolic reprogramming node |
| **Parsimony** | Moderate | High (most parsimonious) | Low (least parsimonious) |
| **Falsifiability** | High — specific epigenetic predictions | High — specific hormonal predictions | Moderate — harder to falsify due to compensation |
| **Robustness to single-target failure** | Low — if epigenetic targets fail, model collapses | Low — if hormone targets fail, model collapses | High — built-in redundancy |
| **EPS confounder risk** | Medium — EPS doesn't affect chromatin directly | High — EPS osmopriming can shift ABA/GA balance | Medium — EPS explains some but not all nodes |
| **Key testable prediction** | Bisulfite-seq shows demethylation at germination loci | Synthetic hormone-node sRNAs recapitulate >60% phenotype | Combinatorial sRNAs show super-additive interactions |
| **Maize-specific relevance** | High (TE-rich genome makes epigenetic effects outsized) | High (VP1-ABA axis is dominant dormancy mechanism) | High (multiple dormancy QTLs support distributed control) |
| **Overall plausibility** | ★★★★☆ | ★★★★☆ | ★★★★★ |

---

## Recommended Model

### **Model 3 (Integrated Systems Resilience) is the best-supported model, but with important caveats.**

**Rationale for selection:**

1. **Best fit to the data breadth.** The most striking feature of this dataset is the sheer number and diversity of targets — 110+ genes across 14 functional categories. Models 1 and 2 must dismiss the majority of these targets as secondary or irrelevant, which is possible but wasteful of the available information. Model 3 is the only framework that incorporates all targets as potentially contributing components of a distributed regulatory attack. [INFERRED]

2. **Consistent with known germination biology.** Seed germination is not controlled by a single master switch but by multiple, partially redundant regulatory layers (epigenetic, hormonal, metabolic, physical). This is evidenced by the multi-QTL architecture of dormancy in maize and other cereals [KNOWN: Holdsworth et al., 2008]. A multi-node intervention is therefore biologically plausible and consistent with the target architecture of the system being manipulated.

3. **Consistent with bacterial sRNA biology.** Bacterial OMVs contain diverse sRNA cargoes, not a single species [KNOWN]. The delivery mechanism naturally produces a multi-target intervention. It would be more surprising if all sRNAs converged on a single pathway.

4. **Explains phenotypic robustness.** If the germination improvement phenotype is reproducible across different seed lots, environmental conditions, and application methods (as implied by its agricultural relevance), a distributed mechanism is more likely than one dependent on efficient silencing of a single target. Single-target mechanisms are fragile; multi-target mechanisms are robust.

**However, the recommended experimental strategy should begin with Model 2 (Hormonal Fulcrum) as the null hypothesis to test against:**

- Model 2 is the most parsimonious and generates the most specific, falsifiable predictions. If synthetic sRNAs targeting only the three hormone nodes (*ZmETR2*, *ZmHP2*, *ZmLOX*) recapitulate the majority of the phenotype, Model 2 is sufficient and Model 3's additional complexity is unnecessary.
- If the hormone-only intervention produces <40% of the full phenotype, and adding epigenetic-targeting sRNAs produces a super-additive improvement, this supports Model 3 over Models 1 and 2.
- The critical discriminating experiment is the **combinatorial synthetic sRNA delivery with factorial design**, which can simultaneously test all three models by measuring individual and interaction effects of each node.

**Practical recommendation for maize agricultural application:**

Regardless of which mechanistic model is correct, the applied strategy should deliver the **full exRNA complement** (not a reduced set), because: (a) the multi-target approach provides phenotypic robustness [INFERRED]; (b) the cost of delivering additional sRNA species in an EV/EPS matrix is negligible compared to the cost of identifying the minimal effective set; and (c) the EPS carrier itself provides beneficial osmopriming effects that synergize with any RNA-mediated mechanism [KNOWN]. The mechanistic dissection is valuable for intellectual property, regulatory approval, and optimization, but the full cocktail is the pragmatic starting point for field trials.