# Causal Models — Wheat (Triticum aestivum)



# Alternative Causal Models: Bacterial exRNA-Mediated Germination Improvement in Spinach (*Spinacia oleracea*)

> **Species Note**: As correctly identified in the ranked target analysis, the gene IDs (SOV prefix) and pathway annotations correspond to *Spinacia oleracea* (spinach), not *Triticum aestivum* (wheat). All models below are constructed in the spinach context. The wheat crop header is treated as a template error. [KNOWN]

> **Foundational Uncertainty**: Cross-kingdom delivery of functional bacterial small RNAs to plant seed cells remains an emerging and incompletely validated mechanism. While vesicle-mediated sRNA transfer has been demonstrated in fungal-plant (Cai et al. 2018 *Nature*) and bacterial-plant (Ren et al. 2019 *Cell Host Microbe*) interactions in vegetative tissues, direct evidence for functional delivery to dry or imbibing seeds is lacking. All three models below rest on this unproven premise. [INFERRED/SPECULATIVE]

---

## Model 1: The Epigenetic Master Switch — Chromatin De-repression Cascades to Systemic Dormancy Release

**Core hypothesis**: Bacterial exRNAs primarily target the seed's epigenetic silencing machinery, causing a genome-wide shift from repressive to permissive chromatin at dormancy-regulated loci, which then secondarily activates hormone, metabolic, and growth programs as a downstream consequence of transcriptional de-repression.

**Causal chain**:

1. **Entry**: Bacterial outer membrane vesicles (OMVs) containing 21–24 nt small RNAs are adsorbed onto the seed surface during imbibition. Vesicle cargo is internalized by endocytosis or direct membrane fusion as seed coat permeability increases during Phase I water uptake. [SPECULATIVE — extrapolated from Ren et al. 2019 showing *Pseudomonas* OMV uptake by *Arabidopsis* root cells; no seed-specific data exist]

2. **Primary targets — the epigenetic repression apparatus is dismantled**:
   - **SOV1g033340.1 (DNA cytosine-5-methyltransferase)** is downregulated → maintenance methylation at CG and CHG contexts fails during the first rounds of DNA replication post-imbibition → progressive, passive demethylation of promoters of GA-responsive genes (e.g., *ent-kaurene synthase*, expansins, α-amylase orthologs). [INFERRED — Arabidopsis *met1* and *cmt3* mutants show reduced dormancy; Zheng et al. 2012 *Plant Cell*]
   - **SOV4g015450.1 (SUVR5-like H3K9 methyltransferase)** is downregulated → loss of H3K9me2 deposition at heterochromatic and euchromatic targets → de-compaction of chromatin at loci encoding germination-promoting transcription factors and hormone biosynthesis enzymes. [INFERRED — SUVR5 in Arabidopsis represses FLC and interacts with the RdDM pathway; Caro et al. 2012 *PLoS Genet*]
   - **SOV6g036290.1 (HIRA histone chaperone)** is downregulated → reduced deposition of histone variant H3.3 at specific loci. In Arabidopsis, HIRA deposits H3.3 at actively transcribed genes but also at heterochromatic regions for silencing maintenance. Loss of HIRA could destabilize silencing at dormancy-associated loci. [INFERRED — Nie et al. 2014 *Mol Plant*]
   - **SOV4g030590.1 (PHD-domain protein)** and **SOV4g038060.1 (GIS2 zinc finger)** are downregulated → loss of "reader" proteins that recruit Polycomb Repressive Complex 2 (PRC2) and other repressive complexes to H3K4me3 or H3K27me3 marks → failure to maintain repressive loops at germination gene clusters. [INFERRED — PHD fingers are known PRC2 recruiters in plants; Molitor et al. 2014 *Genome Biol*]

3. **Secondary cascade — hormone and metabolic gene de-repression**:
   - With repressive chromatin marks failing to be maintained, promoters of GA biosynthesis genes, ethylene-responsive factors, and cell wall loosening enzymes become transcriptionally accessible.
   - This explains the observed downregulation effects on hormone signaling targets (SOV3g000150.1, ethylene receptor; SOV3g035520.1, LOX) not as direct exRNA targets of equal importance, but as genes whose regulatory context is transformed by the epigenetic shift. The ethylene receptor and LOX may be direct exRNA targets that *reinforce* the epigenetically-driven state change.
   - GA signaling activates → DELLA degradation → cell wall remodeling enzymes induced → endosperm weakening.
   - ABA catabolism genes (CYP707A family) become accessible → ABA levels drop → dormancy release.

4. **Tertiary execution — growth programs activated**:
   - Transposon silencing is partially maintained by residual siRNA pathways even as maintenance methylation declines, but the metabolic cost of transposon defense is reduced (5 RT-domain genes downregulated: SOV2g004250.1, SOV4g025520.1, SOV3g033520.1, SOV1g003910.1, SOV4g035390.1). [SPECULATIVE]
   - Defense genes (EDR2 paralogs, MOS1) lose their epigenetic priming, reducing basal immunity and freeing resources. [INFERRED]
   - Net phenotypic outcome: **Accelerated and more uniform radicle protrusion due to genome-wide transcriptional reprogramming, with earlier onset of GA-responsive gene expression and faster ABA decline. Seedling vigor is improved because the epigenetic "reset" also de-represses genes for reserve mobilization and photomorphogenesis preparedness.**

**Supporting evidence**:
- Arabidopsis seeds with reduced DNA methylation (*met1*, *ddm1*) show altered dormancy and often reduced primary dormancy [KNOWN; Soppe et al. 2000 *Plant Cell*; Zheng et al. 2012 *Plant Cell*]
- H3K9me2 marks are enriched at dormancy-associated loci in Arabidopsis and are dynamically removed during germination [KNOWN; Müller et al. 2012 *Plant J*]
- HIRA-mediated H3.3 deposition is required for proper developmental transitions in plants [KNOWN; Nie et al. 2014 *Mol Plant*]
- The target set includes 5/6 epigenetic pathway genes rated "high priority," the densest cluster of high-priority targets in any single pathway [KNOWN from provided data]
- Cross-kingdom sRNA-mediated gene silencing typically operates through AGO-loaded guide strands directing mRNA cleavage or translational inhibition, which could target epigenetic regulator transcripts [INFERRED; Weiberg et al. 2013 *Science*]

**Weaknesses**:
- This model predicts broad, somewhat non-specific transcriptional changes. It does not easily explain why only ~100 genes appear as targets rather than thousands being affected by global demethylation.
- Passive demethylation requires DNA replication, which occurs relatively late in germination (Phase III). The model struggles to explain very early germination effects (Phase I–II) unless the epigenetic targets also have immediate post-transcriptional consequences.
- The model does not adequately explain the specificity of the transport/ion homeostasis targets (18 genes), which seem too pathway-specific to arise solely from chromatin de-repression.
- Cannot distinguish from EPS osmopriming effects, which could independently accelerate imbibition and DNA replication timing.

**Testable predictions**:
1. **Bisulfite sequencing** of treated vs. untreated seeds at 12h and 24h post-imbibition should reveal reduced methylation specifically at GA-responsive and germination-associated gene promoters in exRNA-treated seeds.
2. **ATAC-seq** at 6h post-imbibition should show increased chromatin accessibility at dormancy-regulated loci in treated seeds.
3. Seeds of a spinach line with **reduced methylation** (e.g., via 5-azacytidine pre-treatment) should show a diminished marginal benefit from bacterial exRNA treatment, as the epigenetic "brake" is already partially released.
4. **Heat-denatured exRNA** (destroying secondary structure and AGO-loading capacity) should abolish the germination benefit, while purified bacterial EPS alone should produce a smaller, osmotic-only effect.

---

## Model 2: The Hormonal Fulcrum — Coordinated Suppression of ABA/JA/Stress Signaling Tips the Hormone Balance Toward Germination

**Core hypothesis**: Bacterial exRNAs directly and simultaneously suppress multiple nodes of the ABA–JA–ethylene signaling network and their downstream stress-response effectors, decisively shifting the hormone balance from dormancy-maintenance to germination-promotion, with epigenetic and metabolic changes occurring as secondary consequences of this hormonal shift.

**Causal chain**:

1. **Entry**: Bacterial exRNAs (likely 20–24 nt, potentially loaded into extracellular AGO-like complexes or OMVs) are taken up during early imbibition (Phase I). The rapid hydration of the seed coat and pericarp creates transient membrane permeability that facilitates uptake. [SPECULATIVE — mechanism extrapolated from pollen tube and root hair uptake studies]

2. **Primary targets — the hormonal "brake" system is simultaneously attacked at three independent nodes**:
   - **Node A — Ethylene de-repression**: SOV3g000150.1 (ethylene receptor) is downregulated → constitutive ethylene signaling even at basal ethylene concentrations (ethylene receptors are negative regulators; their loss-of-function activates the pathway) [KNOWN — *etr1* loss-of-function in Arabidopsis causes constitutive ethylene response; Chang et al. 1993 *Science*] → EIN3/EIL1 transcription factors stabilized → direct antagonism of ABA signaling through transcriptional repression of ABI3/ABI5 orthologs → reduced ABA sensitivity.
   - **Node B — JA biosynthesis suppression**: SOV3g035520.1 (Lipoxygenase/LOX) is downregulated → reduced flux through the octadecanoid pathway → lower JA/JA-Ile levels [KNOWN — LOX is the committed step in JA biosynthesis; Wasternack & Hause 2013 *Ann Bot*] → removal of JA-mediated germination inhibition. JA synergizes with ABA to maintain dormancy in many species [KNOWN; Dave et al. 2011 *PNAS*], so its reduction amplifies the effect of ABA pathway suppression.
   - **Node C — Cytokinin relay attenuation**: SOV4g032870.1 (AHP-like histidine phosphotransfer protein) is downregulated → disrupted cytokinin two-component signaling relay → reduced nuclear accumulation of phosphorylated type-B ARR transcription factors. While cytokinins can promote germination in some contexts, AHPs also relay signals from cytokinin-independent histidine kinases (including AHK1, an osmosensor implicated in ABA signaling). Loss of AHP function may specifically attenuate osmotic stress → ABA amplification loops. [INFERRED — AHP proteins relay multiple HK signals; Hutchison et al. 2006 *Plant Cell*]

3. **Secondary amplification — defense and stress pathways collapse, freeing resources**:
   - The reduced JA levels (from LOX suppression) directly diminish defense gene activation, explaining the defense pathway targets:
     - SOV3g043450.1 & SOV6g048760.1 (dual EDR2 paralogs): EDR2 is a negative regulator of SA-mediated defense. Its downregulation might seem to activate SA defense, but in the context of simultaneously reduced JA, the net effect is suppression of the entire JA–SA defense sector. [INFERRED — the JA-SA antagonism means reduced JA removes the "push" toward JA-defense, while EDR2 loss removes the "brake" on SA, but without pathogen-derived SA induction, the SA pathway remains inactive]
     - SOV5g005530.1 (MOS1-like): MOS1 is required for proper R-gene function. Its loss reduces NB-LRR-mediated immune surveillance. [KNOWN — Zhang & Li 2005 *Plant Cell*]
   - **PP2A regulatory subunit** (SOV3g033920.1): PP2A complexes containing specific B-subunits are positive regulators of ABA signaling (they dephosphorylate and activate SnRK2 kinases or maintain ABI5 stability). Downregulation of the A-subunit scaffold disrupts PP2A holoenzyme assembly → reduced ABA signal transduction. [KNOWN — PP2A regulates ABA signaling; Waadt et al. 2015 *Plant Physiol*]
   - **MYB** (SOV1g020340.1) and **NAC** (SOV2g014810.1) transcription factors: Many MYB and NAC family members are ABA-responsive transcriptional activators of stress tolerance genes. Their downregulation removes transcriptional amplification of the ABA/stress program. [INFERRED — specific family members not identified; MYB96 and ANAC055 are known ABA-responsive TFs in Arabidopsis]

4. **Tertiary consequences — metabolic and epigenetic changes follow the hormonal shift**:
   - Reduced ABA signaling → reduced TPS expression requirement (SOV2g009230.1, trehalose-phosphate synthase): T6P is a sugar-status signal that interacts with ABA pathways. With ABA suppressed, the T6P "starvation signal" brake is less relevant. [INFERRED]
   - Reduced ABA → reduced demand for ROS scavenging (SOV3g038840.1 peroxidase, SOV3g040200.1 GST): ABA promotes ROS production as a stress signal; with ABA suppressed, excessive scavenging capacity becomes unnecessary and its downregulation allows the pro-germination "oxidative window" to open. [INFERRED — Bailly et al. 2008 *C R Biol*]
   - Epigenetic changes (methyltransferase, SUVR5, HIRA downregulation) are viewed in this model as *reinforcing* rather than *initiating* — the hormonal shift activates demethylases and chromatin remodelers endogenously, and the exRNA-mediated suppression of methyltransferases prevents re-establishment of repressive marks during the transition.
   - Net phenotypic outcome: **Faster germination due to rapid ABA sensitivity reduction and constitutive ethylene activation, with improved seedling vigor from early reserve mobilization driven by GA-dominant hormone status. The effect is most pronounced under suboptimal conditions (mild salt, osmotic stress) where ABA would normally delay germination.**

**Supporting evidence**:
- All three hormone signaling targets are rated "high priority" [KNOWN from provided data]
- Ethylene receptor loss-of-function (*etr1-1*, *ers1*) promotes germination in Arabidopsis, especially under salt stress [KNOWN; Wilson et al. 2014 *Plant Physiol*]
- LOX-derived JA inhibits germination synergistically with ABA [KNOWN; Dave et al. 2011 *PNAS*]
- The *ahp1,2,3* triple mutant in Arabidopsis shows altered ABA sensitivity [KNOWN; Hutchison et al. 2006 *Plant Cell*]
- PP2A is a known positive regulator of ABA signaling [KNOWN; Waadt et al. 2015]
- The defense downshift theme (EDR2, MOS1, RLKs) is mechanistically coherent with JA pathway suppression [INFERRED]
- This model explains the largest number of high-priority targets through a single initiating mechanism (hormone rebalancing)

**Weaknesses**:
- This model treats the 6 epigenetic targets as secondary, yet they represent the largest cluster of high-priority genes. If epigenetic changes are merely consequential, why would the bacterial exRNAs specifically target 5 high-priority chromatin regulators?
- The model does not clearly explain the 18 transport/ion homeostasis targets or the 6 DNA repair/replication targets, which have no obvious direct connection to hormone signaling.
- The AHP target's role is ambiguous — AHPs relay cytokinin signals that can *promote* germination, so their downregulation could have negative effects that this model does not address.
- Constitutive ethylene signaling (from receptor loss) can inhibit hypocotyl elongation and root growth in established seedlings (the "triple response"), potentially reducing seedling vigor rather than improving it. The model must assume that the receptor downregulation is partial, not complete. [KNOWN — the triple response is a well-established ethylene phenotype]
- Cannot be distinguished from bacterial volatile organic compounds (VOCs including ethylene itself) that could independently activate ethylene signaling without requiring exRNA uptake.

**Testable predictions**:
1. **Hormone profiling** (LC-MS) of exRNA-treated vs. untreated seeds at 6h, 12h, and 24h should show reduced ABA and JA-Ile levels and/or reduced ABA sensitivity (measured by ABA dose-response germination assays) in treated seeds.
2. Exogenous **ABA application** at supraphysiological concentrations should partially rescue (delay) the germination acceleration in exRNA-treated seeds, as the downstream ABA response machinery is still intact even if sensitivity is reduced.
3. **Ethylene-insensitive spinach lines** (if available, or pharmacologically via 1-MCP treatment) should show reduced benefit from exRNA treatment, as the ethylene receptor downregulation effect would be bypassed.
4. **LOX inhibitor** (e.g., NDGA) applied to untreated seeds should partially phenocopy the exRNA treatment by reducing JA biosynthesis.
5. Transcriptomic analysis should show that **ABA-responsive genes** (e.g., LEA proteins, dehydrins) are among the most strongly downregulated genes in exRNA-treated seeds, even though they are not direct exRNA targets.

---

## Model 3: The Integrated De-repression Network — Parallel, Redundant Brake Release Across Multiple Regulatory Layers

**Core hypothesis**: No single pathway is primary. Bacterial exRNAs simultaneously target partially redundant dormancy-maintenance programs across epigenetic, hormonal, defense, metabolic, and cell-structural layers, and the germination improvement emerges from the *additive and synergistic* removal of multiple independent "brakes" — a strategy that is robust precisely because it does not depend on any single target.

**Causal chain**:

1. **Entry**: Bacterial exRNAs are delivered as a diverse pool of ~100 distinct small RNA species within OMVs. The pool composition reflects the bacterial transcriptome and is not specifically "designed" for plant gene targeting. However, by stochastic complementarity across the ~100 targets, a sufficient number achieve functional silencing in seed cells during imbibition. Delivery efficiency varies by target and cell type, meaning not all targets are equally suppressed in every cell. [SPECULATIVE — this model explicitly embraces the stochastic nature of cross-kingdom RNAi]

2. **Layer 1 — Epigenetic brake release (partial)**:
   - SOV1g033340.1 (DNA methyltransferase), SOV4g015450.1 (SUVR5), SOV6g036290.1 (HIRA), SOV4g030590.1 (PHD), SOV4g038060.1 (GIS2) are each partially downregulated.
   - No single epigenetic target achieves complete silencing, but the *combined* partial reduction across DNA methylation, H3K9 methylation, histone deposition, and chromatin reading creates a cumulative reduction in repressive chromatin maintenance capacity.
   - Effect: ~30–50% reduction in repressive mark re-establishment at each cell division → progressive de-repression of dormancy-regulated loci over 12–24h. [SPECULATIVE — quantitative estimate for illustration]

3. **Layer 2 — Hormonal brake release (partial)**:
   - SOV3g000150.1 (ethylene receptor), SOV3g035520.1 (LOX), SOV4g032870.1 (AHP) are each partially downregulated.
   - Partial ethylene receptor loss → modest increase in ethylene sensitivity (not full constitutive response, avoiding the triple-response problem of Model 2).
   - Partial LOX reduction → modest JA decrease → slightly reduced ABA–JA synergy.
   - Partial AHP reduction → modestly attenuated stress-signal relay.
   - Effect: The ABA/GA ratio shifts incrementally toward GA dominance, but not as dramatically as in Model 2. The shift is sufficient to cross the germination threshold earlier, especially in seeds that were close to the threshold already (explaining improved uniformity). [INFERRED]

4. **Layer 3 — Defense/immunity brake release (partial)**:
   - SOV3g043450.1 & SOV6g048760.1 (EDR2 × 2), SOV5g005530.1 (MOS1), SOV1g021670.1 (R-protein), SOV3g021300.1 (NST1) are partially downregulated.
   - Reduced immune surveillance → reduced constitutive defense gene expression → metabolic savings estimated at 5–15% of total ATP budget during early germination. [SPECULATIVE — the "cost of defense" is documented in principle but not quantified for spinach seeds; Huot et al. 2014 *Annu Rev Plant Biol*]
   - These savings are not directed by any regulatory logic but simply become available for growth processes by mass action.

5. **Layer 4 — Metabolic and transport reconfiguration (partial)**:
   - SOV2g009230.1 (TPS) partially reduced → altered T6P/sucrose signaling → modestly accelerated reserve mobilization. [INFERRED]
   - SOV6g029280.1 (6PGD) partially reduced → redirected carbon flux from pentose phosphate pathway toward glycolysis, favoring ATP production over NADPH/nucleotide biosynthesis during early imbibition. [INFERRED — this is counterintuitive and may represent a timing effect: early germination needs ATP more than NADPH]
   - Transport targets (18 genes): partial reduction of cation-chloride cotransporters (SOV1g021960.1, SOV2g025380.1), CNGC (SOV1g018480.1), and ABC transporters → altered ion fluxes that may reduce ABA import, modify Ca²⁺ signaling dynamics, and reduce sequestration of GA precursors. [SPECULATIVE]
   - Cell wall targets: partial reduction of glycosyltransferases (SOV4g010600.1, SOV1g033840.1) → reduced cell wall reinforcement in endosperm cap → lower mechanical resistance to radicle protrusion. [INFERRED — endosperm weakening is a well-established germination requirement; Nonogaki et al. 2010 *Ann Rev Plant Biol*]

6. **Layer 5 — ROS window optimization (partial)**:
   - SOV3g038840.1 (peroxidase) and SOV3g040200.1 (GST) partially reduced → modest decrease in ROS scavenging capacity → the pro-germination oxidative window is reached earlier and maintained longer.
   - This is synergistic with Layer 2 (reduced ABA reduces stress-induced ROS overproduction) and Layer 4 (cell wall loosening is enhanced by apoplastic ROS). [INFERRED — Bailly et al. 2008; Müller et al. 2009 *Plant Cell*]

7. **Emergent phenotype**: The germination improvement arises not from any single dramatic molecular event but from the **simultaneous, modest relaxation of 5+ independent dormancy-maintenance systems**. Each layer contributes a small but real acceleration. The combined effect is:
   - **Faster germination**: Seeds cross the germination threshold 6–18h earlier due to additive brake release.
   - **Improved uniformity**: Seeds with naturally variable dormancy depths all receive the same multi-layered push, compressing the distribution of germination times.
   - **Enhanced seedling vigor**: Early reserve mobilization, reduced defense costs, and optimized ROS signaling produce seedlings with greater root length and biomass at 7 days.
   - **Robustness**: Because no single target is essential, natural variation in exRNA delivery efficiency or target accessibility does not prevent the phenotype from manifesting.

**Supporting evidence**:
- The target set spans 14 functional categories with no single category containing >18 genes, consistent with a distributed rather than focused strategy [KNOWN from provided data]
- Germination is known to be controlled by multiple partially redundant regulatory mechanisms; single-gene knockouts rarely produce dramatic germination phenotypes outside the core ABA/GA pathway [KNOWN; Finch-Savage & Leubner-Metzger 2006 *New Phytol*]
- Bacterial sRNA pools are diverse and would not be expected to produce perfectly matched guides for a small number of targets; a "shotgun" strategy targeting many genes modestly is more biologically plausible for a non-coevolved system [INFERRED]
- Additive effects of multiple small perturbations are well-documented in quantitative genetics of germination (QTL studies reveal many small-effect loci) [KNOWN; Bentsink et al. 2010 *PNAS*]
- The model naturally accommodates the observation that both high-priority (epigenetic, hormonal) and medium/low-priority (transport, RNA processing, organelle) targets are present — all contribute, but with different effect sizes

**Weaknesses**:
- This model is the least falsifiable because it does not make strong predictions about which targets are essential. It is, in some sense, the "null model" of multi-target effects.
- It does not explain *why* bacterial exRNAs would target this particular set of ~100 genes rather than a random set. If the targeting is stochastic, many exRNAs should also hit pro-germination genes, potentially canceling the benefit. The model requires that the bacterial sRNA pool is somehow biased toward sequences complementary to dormancy-maintenance transcripts, which demands explanation.
- The model predicts small individual effect sizes, making single-target validation experiments likely to produce null results, which could be interpreted as either supporting the model (no single target matters) or refuting the entire exRNA hypothesis.
- It is extremely difficult to distinguish this model's predictions from a simple **EPS osmopriming effect**, which would also produce modest, distributed improvements across multiple germination parameters without requiring any specific gene targeting.
- The model does not address the energetic cost of maintaining the exRNA delivery and silencing machinery, which may exceed the benefit of modest multi-target suppression.

**Testable predictions**:
1. **Dose-response experiments**: If this model is correct, the germination benefit should scale continuously with exRNA concentration (more exRNA → more targets suppressed → greater benefit), rather than showing a threshold effect (which would favor Models 1 or 2).
2. **Partial target sets**: Synthetic sRNA pools targeting only the epigenetic layer (5 targets) or only the hormone layer (3 targets) should each produce a *partial* germination benefit, and combining them should produce a *greater-than-additive* benefit. This distinguishes Model 3 from Models 1 and 2, which predict that one layer alone should be sufficient.
3. **Transcriptomic breadth**: RNA-seq of treated seeds should show modest (1.5–2-fold) downregulation across many targets rather than dramatic (>5-fold) suppression of a few key targets. The effect should be detectable only with adequate statistical power (n ≥ 4 biological replicates).
4. **Scrambled exRNA control**: A size-matched but sequence-scrambled RNA pool should produce no germination benefit (ruling out non-specific RNA effects like TLR activation), while heat-denatured exRNA should also fail (ruling out nucleotide nutrient effects).
5. **Multi-omics integration**: Proteomic, methylomic, and hormonomic analyses should each show modest but consistent shifts in the predicted directions, with no single -omic layer showing a dramatic change.

---

## Model Comparison Table

| Feature | Model 1: Epigenetic Master Switch | Model 2: Hormonal Fulcrum | Model 3: Integrated De-repression Network |
|---|---|---|---|
| **Primary initiating event** | Chromatin de-repression | ABA/JA/ethylene rebalancing | Simultaneous multi-layer brake release |
| **Targets directly explained** | 6 epigenetic + 5 transposon (11 direct, remainder secondary) | 3 hormone + 5 defense + 3 signaling + 3 ROS (14 direct, remainder secondary) | All ~100 targets as direct, parallel contributors |
| **High-priority targets explained** | 5/6 epigenetic (excellent); hormone targets as secondary | 3/3 hormone + 2/2 EDR2 + MOS1 + PP2A + MYB + NAC (excellent); epigenetic as secondary | All high-priority targets explained equally |
| **Mechanism complexity** | Low (single initiating layer → cascade) | Medium (3 hormone nodes + downstream amplification) | High (5+ parallel layers, no hierarchy) |
| **Explains transport/ion targets (18 genes)?** | Poorly — indirect at best | Partially — ABA transport nodes | Yes — as one of many parallel layers |
| **Explains DNA repair targets (6 genes)?** | Partially — chromatin state affects replication checkpoint | Poorly | Yes — as checkpoint relaxation layer |
| **Temporal prediction** | Slow onset (requires DNA replication for passive demethylation) | Fast onset (post-transcriptional hormone signaling within hours) | Intermediate (varies by layer) |
| **Distinguishable from EPS osmopriming?** | Yes — specific methylation changes predicted | Partially — hormone changes could overlap with EPS effects | Difficult — distributed effects mimic osmopriming |
| **Falsifiability** | High — bisulfite-seq and ATAC-seq provide clear tests | High — hormone quantification and pharmacological epistasis | Low — requires multi-target combinatorial experiments |
| **Risk of ethylene "triple response"** | Low — ethylene receptor is secondary target | High — constitutive ethylene could inhibit growth | Low — partial receptor reduction avoids threshold |
| **Overall plausibility** | Medium-High | Medium-High | Medium |

---

## Recommended Model

### **Model 2 (Hormonal Fulcrum) is recommended as the primary working model, with elements of Model 1 incorporated as a reinforcing mechanism.**

**Rationale**:

1. **Speed of action**: Germination improvement is typically assessed within 24–72h of imbibition. Hormone signaling operates on a timescale of minutes to hours (receptor-level effects are nearly immediate upon transcript reduction), while epigenetic reprogramming (Model 1) requires at least one round of DNA replication for passive demethylation effects to manifest. The hormonal model better explains rapid germination acceleration. [INFERRED]

2. **Genetic precedent**: The strongest single-gene germination phenotypes in Arabidopsis involve hormone perception and signaling mutants (*abi1*, *abi3*, *etr1*, *gai*, *rga*, *della* quintuple). Epigenetic mutants show dormancy effects but typically require homozygosity across multiple loci. This supports hormone nodes as higher-leverage targets. [KNOWN]

3. **Target quality**: All three hormone signaling targets are rated "high priority" with strong mechanistic directness scores. The ethylene receptor, in particular, sits at the apex of a well-characterized negative regulatory cascade where even partial loss-of-function has documented germination effects. [KNOWN]

4. **Explanatory breadth with parsimony**: Model 2 directly explains the hormone, defense (via JA suppression), ROS (via ABA-ROS crosstalk), and signaling (PP2A, MYB, NAC) targets through a coherent mechanistic chain. Adding the epigenetic layer from Model 1 as a *reinforcing* mechanism (the exRNAs target both the hormonal triggers AND the epigenetic maintenance machinery to ensure the dormancy program cannot be re-established) explains the epigenetic targets without requiring them to be the primary driver.

5. **Testability**: Model 2 generates the most specific, falsifiable predictions (hormone quantification, pharmacological epistasis with ABA/1-MCP/NDGA, ethylene-insensitive line experiments) that can be executed with standard plant biology tools.

**However**, the recommended working model should be understood as a **"Hormonal Fulcrum reinforced by Epigenetic Locking"** — a hybrid of Models 1 and 2:

> *Bacterial exRNAs rapidly shift the hormone balance toward germination by suppressing the ethylene receptor, LOX/JA biosynthesis, and AHP stress relay (Model 2 core). Simultaneously, they suppress the epigenetic maintenance machinery (DNA methyltransferase, SUVR5, HIRA, PHD reader, GIS2) to prevent the re-establishment of repressive chromatin at germination-promoting loci, effectively "locking in" the hormonal shift at the transcriptional level (Model 1 reinforcement). The defense downshift and metabolic reconfiguration are downstream consequences of both layers, providing the resources and cellular infrastructure to execute the germination program.*

This hybrid model explains the high-priority status of both the hormone and epigenetic target clusters, accounts for the temporal dynamics of germination, and generates testable predictions at multiple levels of biological organization. The key experiment to distinguish the hybrid from pure Model 2 would be to show that **exRNA treatment produces lasting methylation changes at hormone-responsive loci** — if so, the epigenetic reinforcement is real; if not, Model 2 alone suffices.

**Critical caveat**: All models remain [SPECULATIVE] until (1) functional delivery of bacterial exRNAs to spinach seed cells is demonstrated, (2) target transcript reduction is confirmed by RT-qPCR or degradome sequencing, and (3) the germination benefit is shown to require sequence-specific RNA (not EPS, VOCs, or nutrient effects) through appropriate controls.