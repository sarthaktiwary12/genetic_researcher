# Causal Models — Spinach (Spinacia oleracea)



# Alternative Causal Models: Bacterial exRNA-Mediated Germination Improvement in *Spinacia oleracea*

---

## Preamble: Critical Assumptions and Caveats

Before constructing these models, several foundational uncertainties must be stated explicitly:

1. **exRNA delivery to embryonic cells is unproven in this system.** Cross-kingdom RNA interference has been demonstrated in select plant–fungal (e.g., *Botrytis cinerea*–*Arabidopsis*; Weiberg et al., 2013, *Science*) and plant–parasitic plant systems, but the physical barriers of the spinach seed coat (testa) and endosperm are formidable. Whether bacterial small RNAs can penetrate these layers in biologically relevant quantities during imbibition is unknown. [KNOWN: cross-kingdom RNAi exists; SPECULATIVE: it operates here]

2. **Confounders are substantial.** Bacterial exopolysaccharides (EPS) can act as osmopriming agents, altering water potential gradients. Bacterial lipopolysaccharides and peptidoglycan fragments can act as microbe-associated molecular patterns (MAMPs), triggering or suppressing plant immune responses. Live bacteria alter the spermosphere microbiome. Any or all of these could explain improved germination independently of mRNA silencing.

3. **Spinach genome annotation is incomplete.** Many gene assignments are based on homology to *Arabidopsis thaliana* or *Beta vulgaris* and may not reflect true function in *S. oleracea*.

All three models below assume, for the sake of hypothesis construction, that bacterial exRNAs do reach embryonic cells and engage the plant's RNAi machinery (likely loading into AGO1 or AGO-family proteins to direct target cleavage or translational repression). The models differ in which subset of targets they prioritize as the primary causal drivers and in the temporal logic of the causal chain.

---

## Model 1: The Epigenetic Master Switch Model

**Core hypothesis**: Bacterial exRNAs primarily target the seed's epigenetic silencing machinery, causing a genome-wide de-repression of pro-germination gene programs that were locked in a dormancy-associated chromatin state; all other observed pathway effects are downstream consequences of this transcriptional liberation.

**Causal chain**:

1. **Bacterial exRNA enters seed cells during early imbibition** via symplastic uptake through hydrated cell walls of the micropylar endosperm, potentially facilitated by membrane destabilization during rehydration. Small RNAs (likely 20–24 nt) are loaded into spinach AGO proteins. [SPECULATIVE: delivery mechanism; INFERRED: AGO loading based on conserved plant RNAi machinery]

2. **Three core epigenetic regulators are simultaneously downregulated**:
   - **SOV1g033340.1 (DNA cytosine-5-methyltransferase)** → Reduced maintenance methylation at CG and CHG contexts during the first rounds of DNA replication post-imbibition. This passively demethylates promoters of germination-associated genes (e.g., GA biosynthesis genes *GA3ox*, *GA20ox*; cell wall loosening enzymes; aquaporins). [KNOWN: DNA methylation maintains dormancy gene silencing in Arabidopsis; Nee et al., 2017, *Plant Cell*; INFERRED: analogous in spinach]
   - **SOV4g015450.1 (SUVR5-like histone methyltransferase)** → Reduced deposition of H3K9me2 repressive marks at heterochromatic loci, including dormancy-maintenance genes and transposable element-adjacent regulatory regions. [KNOWN: SUVR5 deposits H3K9me2 in Arabidopsis; Caro et al., 2012; INFERRED: functional conservation]
   - **SOV6g036290.1 (HIRA histone chaperone)** → Disrupted replication-independent deposition of histone variant H3.3 into transcriptionally active loci. Paradoxically, HIRA loss may prevent the re-establishment of specific chromatin states that maintain dormancy gene expression during imbibition. [KNOWN: HIRA deposits H3.3 in Arabidopsis; Nie et al., 2014; INFERRED: dormancy-specific role]

3. **Chromatin readers and transcriptional repressors lose their substrates and targets**:
   - **SOV4g030590.1 (PHD domain protein)** downregulation removes a "reader" of histone methylation marks, breaking the positive feedback loop where repressive marks recruit more silencing machinery. [INFERRED]
   - **SOV4g038060.1 (GIS2 zinc finger)** downregulation removes a transcriptional repressor that, in Arabidopsis, promotes trichome development and represses flowering; its spinach homolog may repress germination-associated transcription factor cascades. [KNOWN: GIS2 function in Arabidopsis; SPECULATIVE: spinach germination role]

4. **Cascading de-repression activates multiple downstream programs simultaneously**:
   - **Hormone signaling genes become transcriptionally accessible**: GA biosynthesis and signaling genes are expressed → DELLA repressors are degraded → germination program initiates. ABA catabolism genes (*CYP707A* family) are de-repressed → ABA levels decline. [KNOWN: epigenetic control of ABA/GA genes; Liu et al., 2013]
   - **Cell wall remodeling enzymes are expressed**: Expansins, endo-β-mannanases, and xyloglucan endotransglucosylase/hydrolases (XTHs) are transcribed from newly accessible chromatin → micropylar endosperm weakening proceeds. [KNOWN: these genes are epigenetically regulated during germination]
   - **Defense genes are collaterally suppressed**: The broad chromatin opening paradoxically reduces expression of some defense genes that were maintained by specific active chromatin states (H3.3-dependent), while the simultaneous exRNA-mediated knockdown of EDR2 and MOS1 (SOV3g043450.1, SOV6g048760.1, SOV5g005530.1) ensures immune suppression is robust. [INFERRED]
   - **Transposon silencing is partially released**: The 5 reverse transcriptase/gag targets (SOV2g004250.1, SOV4g025520.1, SOV3g033520.1, SOV1g003910.1, SOV4g035390.1) may represent a side effect—their transcripts increase due to chromatin opening but are simultaneously targeted by the bacterial exRNAs, creating a fail-safe against genomic instability. [SPECULATIVE]

5. **Net phenotypic outcome**: Accelerated and more uniform radicle emergence due to earlier activation of the full germination transcriptional program. Seedling vigor is enhanced because the epigenetic "reset" allows robust expression of photomorphogenesis and nutrient mobilization genes post-emergence. The effect is predicted to be **persistent** (potentially lasting through early vegetative growth) because epigenetic states, once altered, can be mitotically heritable.

**Supporting evidence**:
- DNA methylation dynamics are causally linked to Arabidopsis seed dormancy cycling [KNOWN: Footitt et al., 2015, *PNAS*]
- Pharmacological inhibition of DNA methylation (5-azacytidine) breaks dormancy in multiple species [KNOWN: Cadman et al., 2006]
- SUVR5 loss-of-function mutants show altered gene expression at hundreds of loci [KNOWN: Caro et al., 2012]
- The model explains why 6 of 6 epigenetic targets are rated "high priority" in the pathway analysis [INFERRED: internal consistency]
- The model accounts for the breadth of affected pathways (14 pathways) through a single upstream mechanism [INFERRED]

**Weaknesses**:
- Does not explain the specificity of downstream effects. If chromatin is globally opened, why are only pro-germination genes activated and not, for example, senescence or flowering programs? The model requires additional specificity layers (e.g., tissue-specific transcription factors already present in the embryo) that are not explicitly targeted by the exRNAs.
- Cannot easily distinguish from EPS-mediated osmopriming, which also accelerates imbibition and could independently trigger epigenetic reprogramming through water-dependent passive demethylation.
- The temporal kinetics are problematic: exRNA-mediated mRNA silencing acts post-transcriptionally and would reduce *new* protein production, but existing DNA methyltransferase protein already present in the dry seed would remain active until turned over. The lag between mRNA knockdown and protein depletion may be too slow for early imbibition effects.
- Does not directly explain the targeting of metabolic enzymes (TPS, 6PGD, LOX) or transport proteins, which would not be primary consequences of chromatin remodeling.

**Testable predictions**:
1. Whole-genome bisulfite sequencing (WGBS) of exRNA-treated vs. untreated seeds at 6, 12, and 24 hours post-imbibition should show reduced methylation at CG and CHG contexts, particularly at promoters of known germination genes (*GA3ox*, *EXPA* family, *MAN* family).
2. ChIP-seq for H3K9me2 should show reduced signal at heterochromatic loci in treated seeds.
3. The germination-promoting effect should be partially phenocopied by 5-azacytidine treatment of spinach seeds.
4. If the model is correct, the exRNA effect should be **irreversible** once established—removing exRNA after 12 hours of imbibition should not abolish the germination advantage.
5. ATAC-seq should reveal increased chromatin accessibility at germination-associated loci in treated seeds.

---

## Model 2: The Hormonal Fulcrum Model

**Core hypothesis**: Bacterial exRNAs target a small number of high-leverage nodes in the ABA–ethylene–JA hormonal network, tipping the hormonal balance decisively toward germination; improved vigor arises from the downstream metabolic, cell wall, and transport consequences of this hormonal shift rather than from direct silencing of those effector pathways.

**Causal chain**:

1. **Bacterial exRNA enters seed cells during imbibition** (mechanism as in Model 1). The critical distinction is that only 3–5 targets need to be silenced efficiently for the full phenotype to manifest; the remaining ~100 targets may represent low-efficiency, biologically inconsequential off-target effects or may be explained by non-exRNA confounders.

2. **Three hormonal hub targets are downregulated with high efficiency**:
   - **SOV3g000150.1 (Ethylene receptor)** → Ethylene receptors (ETR1/EIN4 family) are negative regulators; they constitutively repress ethylene signaling when unoccupied by ethylene. Reducing receptor abundance *derepresses* ethylene signaling even at low ethylene concentrations. [KNOWN: ethylene receptors are negative regulators; Hua & Meyerowitz, 1998, *Cell*; KNOWN: ethylene promotes germination and antagonizes ABA; Linkies et al., 2009, *Plant Cell*]
   - **SOV3g035520.1 (Lipoxygenase, LOX)** → LOX catalyzes the first committed step in jasmonate (JA) biosynthesis. Downregulation reduces JA production. JA synergizes with ABA to inhibit germination in many species. [KNOWN: LOX → JA biosynthesis; KNOWN: JA inhibits germination in Arabidopsis; Dave et al., 2011, *J. Exp. Bot.*; INFERRED: analogous in spinach]
   - **SOV4g032870.1 (AHP-like histidine phosphotransfer protein)** → AHPs relay cytokinin signaling from receptors to response regulators. However, AHP proteins also participate in osmosensing and ABA signaling crosstalk. Downregulation may dampen ABA-responsive gene expression by disrupting phosphorelay to type-B ARR transcription factors that can potentiate ABA responses. [KNOWN: AHP function in cytokinin signaling; INFERRED: ABA crosstalk role; SPECULATIVE: net pro-germination effect of AHP knockdown]

3. **The hormonal shift cascades through multiple effector pathways**:
   - **Enhanced ethylene signaling** (from receptor knockdown):
     - Activates ERF (Ethylene Response Factor) transcription factors → upregulation of cell wall loosening genes (expansins, XTHs) → endosperm weakening → radicle emergence. [KNOWN: ethylene promotes endosperm weakening; Linkies & Leubner-Metzger, 2012]
     - Directly antagonizes ABA signaling at the level of ABI3/ABI5 transcription factor stability → reduced expression of LEA proteins and dormancy-maintenance genes. [KNOWN: ethylene–ABA antagonism; Beaudoin et al., 2000, *Plant Cell*]
     - Promotes ROS production in the apoplast → cell wall loosening via hydroxyl radical-mediated polysaccharide cleavage. This explains the targeting of ROS scavengers (SOV3g038840.1, peroxidase; SOV3g040200.1, GST) as a *reinforcing* rather than primary mechanism. [KNOWN: ROS role in cell wall loosening; Müller et al., 2009]
   - **Reduced JA levels** (from LOX knockdown):
     - Relieves JA-mediated suppression of GA signaling → DELLA degradation proceeds more rapidly → GA-responsive genes activated. [KNOWN: JA–GA antagonism; Yang et al., 2012, *Plant Cell*]
     - Reduces JA-mediated defense gene expression → resource reallocation from defense to growth (explaining the "defense downshift" theme without requiring direct targeting of immune genes). [INFERRED]
   - **Altered ABA sensitivity** (from AHP knockdown):
     - Reduced phosphorelay dampens transcriptional responses to endogenous ABA → the effective ABA "dose" perceived by the embryo is lowered even without changes in ABA concentration. [SPECULATIVE]

4. **Secondary targets amplify the hormonal signal**:
   - **SOV2g009230.1 (Trehalose-phosphate synthase, TPS)** knockdown reduces trehalose-6-phosphate (T6P) levels. T6P is a sugar signal that promotes ABA-mediated dormancy maintenance via SnRK1 pathway modulation. Lower T6P may mimic a "growth-permissive" metabolic state. [KNOWN: T6P–SnRK1–ABA axis; Nunes et al., 2013, *Plant Physiol.*; INFERRED: T6P promotes dormancy in spinach]
   - **SOV3g033920.1 (PP2A regulatory subunit)** knockdown disrupts PP2A phosphatase complexes that are positive regulators of ABA signaling (PP2A dephosphorylates and activates SnRK2 kinases in some contexts, though the relationship is complex). [KNOWN: PP2A role in ABA signaling; Waadt et al., 2015; INFERRED: net effect is reduced ABA sensitivity]

5. **Net phenotypic outcome**: Rapid, uniform germination driven by a decisive hormonal shift: lower ABA sensitivity + lower JA + higher ethylene responsiveness → robust GA-mediated germination program. Seedling vigor is enhanced because ethylene promotes hypocotyl elongation and the JA reduction allows resource investment in growth. The effect is predicted to be **acute and transient**—dependent on continued suppression of the target mRNAs during the critical imbibition-to-radicle-emergence window (typically 24–72 hours in spinach).

**Supporting evidence**:
- Ethylene receptor mutants (*etr1-1*) in Arabidopsis show enhanced germination, especially under stress [KNOWN: Chiwocha et al., 2005]
- LOX-deficient mutants (reduced JA) germinate faster in several species [KNOWN: Dave et al., 2011]
- All three hormone targets were independently rated "high priority" [INFERRED: internal consistency]
- The model is parsimonious: 3 primary targets explain the phenotype; remaining targets are either secondary amplifiers or noise
- Ethylene–ABA antagonism is the single most well-characterized hormonal interaction in germination biology [KNOWN]

**Weaknesses**:
- Does not explain the targeting of epigenetic regulators (HIRA, DNMT, SUVR5), which are unlikely downstream consequences of hormonal shifts on the timescale of germination.
- Cannot account for the transposon-related targets, which have no known hormonal regulation.
- The AHP knockdown effect is ambiguous: AHPs are primarily cytokinin signaling components, and cytokinin often *promotes* germination. Knocking down AHP could therefore *inhibit* germination via reduced cytokinin signaling, creating an internal contradiction. The model requires the ABA-crosstalk function to dominate, which is speculative.
- If the phenotype is primarily hormonal, it should be fully phenocopied by exogenous ethylene (ethephon) + JA biosynthesis inhibitor (ibuprofen/DIECA) treatment—if it is not, additional mechanisms must be invoked.
- Does not explain why so many targets (109 predicted) are needed if only 3–5 are causally important.

**Testable predictions**:
1. Endogenous hormone profiling (LC-MS/MS) of treated vs. untreated seeds should show reduced JA/JA-Ile and unchanged or reduced ABA at 12–24 hours post-imbibition. Ethylene emission (gas chromatography) should be elevated or unchanged (the receptor knockdown enhances *sensitivity*, not necessarily *production*).
2. The germination advantage should be **abolished** by co-treatment with the ethylene perception inhibitor 1-MCP (1-methylcyclopropene) or silver thiosulfate.
3. The germination advantage should be **partially phenocopied** by ethephon (ethylene releaser) + ibuprofen (LOX inhibitor) co-treatment.
4. If only the hormonal targets matter, heat-inactivated bacterial exRNA (destroying secondary structure needed for AGO loading) should abolish the effect, while purified bacterial EPS alone should not replicate it.
5. qRT-PCR of *ETR1*-like, *LOX*, and *AHP* transcripts should show specific reduction in treated seeds within 6–12 hours.

---

## Model 3: The Integrated Growth–Defense Reallocation Model

**Core hypothesis**: Bacterial exRNAs execute a coordinated, multi-pathway reprogramming that cannot be reduced to a single master switch; the germination advantage arises from the *simultaneous* suppression of three resource-consuming programs (immune surveillance, epigenetic maintenance of dormancy, and metabolic stress-readiness) that collectively constitute a "dormancy tax," liberating energy and biosynthetic capacity for germination.

**Causal chain**:

1. **Bacterial exRNAs enter seed cells in a broad, low-efficiency manner during imbibition.** Rather than requiring high-efficiency silencing of a few targets, this model posits that moderate knockdown (~30–50% reduction) of many targets across multiple pathways produces a phenotype through additive and synergistic effects. The exRNA population is diverse (hundreds of small RNA species), and each achieves partial suppression of its cognate target. [SPECULATIVE: quantitative silencing model; INFERRED from the breadth of the target set]

2. **Three resource-draining programs are simultaneously suppressed**:

   **Program A — Immune Surveillance (Defense Downshift)**:
   - SOV3g043450.1 + SOV6g048760.1 (EDR2 × 2) + SOV5g005530.1 (MOS1) + SOV1g021670.1 (R-protein) + SOV3g021300.1 (NST1) are all partially knocked down.
   - EDR2 is a negative regulator of SA-mediated defense; its loss in Arabidopsis causes *constitutive* defense activation, which is costly. However, the simultaneous knockdown of MOS1 (required for R-protein function and SNC1-mediated autoimmunity) and the R-protein itself ensures that the defense pathway cannot be activated even if EDR2 suppression would otherwise derepress it. The net effect is a **defense-incompetent but metabolically liberated** state. [KNOWN: EDR2 is a negative regulator of defense, Vorwerk et al., 2007; KNOWN: MOS1 is required for SNC1-mediated immunity, Li et al., 2010; INFERRED: combined knockdown prevents defense activation]
   - RLKs (SOV1g027650.1, SOV4g000660.1) and calcium signaling components (SOV2g039720.1) are partially suppressed → reduced MAMP perception → the seed does not mount costly PTI responses to soil microbes during imbibition. [INFERRED]
   - **Resource savings**: Defense protein synthesis, SA/JA biosynthesis, callose deposition, and PR protein production are all energetically expensive. Their suppression frees ATP, amino acids, and carbon skeletons. [KNOWN: defense costs are well-documented; Huot et al., 2014, *Mol. Plant*]

   **Program B — Epigenetic Dormancy Maintenance**:
   - SOV1g033340.1 (DNMT) + SOV4g015450.1 (SUVR5) + SOV6g036290.1 (HIRA) + SOV4g030590.1 (PHD reader) + SOV4g038060.1 (GIS2) are partially knocked down.
   - The maintenance of repressive chromatin is itself energetically costly: DNA methylation consumes S-adenosylmethionine (SAM), histone methylation consumes SAM, nucleosome remodeling consumes ATP. Partial knockdown does not fully open chromatin (as in Model 1) but rather **reduces the energetic cost of maintaining the dormant epigenetic state** while allowing stochastic de-repression of pro-germination loci. [KNOWN: SAM consumption by methyltransferases is metabolically significant; Meng et al., 2018; INFERRED: partial knockdown creates a "leaky" chromatin state]
   - This partial de-repression is sufficient to tip the ABA/GA balance when combined with hormonal modulation (Program C, below). [INFERRED]

   **Program C — Metabolic Stress-Readiness**:
   - SOV2g009230.1 (TPS) knockdown → reduced T6P → SnRK1 activation → catabolism of storage reserves is accelerated (SnRK1 promotes autophagy, lipid mobilization, and starch breakdown). [KNOWN: T6P inhibits SnRK1; Baena-González et al., 2007, *Nature*; INFERRED: SnRK1 activation promotes reserve mobilization]
   - SOV6g029280.1 (6-phosphogluconate dehydrogenase) knockdown → reduced NADPH from the oxidative pentose phosphate pathway (oxPPP) → shifts carbon flux toward glycolysis and the TCA cycle for ATP production rather than NADPH-dependent biosynthesis. This prioritizes energy production over anabolic defense compound synthesis. [KNOWN: oxPPP provides NADPH for defense-related secondary metabolism; INFERRED: flux redirection]
   - SOV3g040200.1 (GST) + SOV3g038840.1 (Peroxidase) knockdown → reduced ROS scavenging capacity → ROS accumulates to signaling levels that promote cell wall loosening and ABA catabolism, but does not reach damaging levels because the metabolic shift (above) reduces ROS generation from defense metabolism. [KNOWN: the "oxidative window" concept; Bailly et al., 2008, *C. R. Biologies*; INFERRED: balanced ROS outcome]
   - GDSL esterase/lipases (SOV1g004930.1, SOV4g008190.1, SOV6g042250.1) knockdown → reduced cutin/suberin biosynthesis or modification → thinner seed coat lipid barriers → enhanced water uptake and gas exchange. [INFERRED: GDSL lipases modify seed coat lipids; SPECULATIVE: knockdown improves permeability]

3. **The three programs interact synergistically at the ABA/GA node**:
   - Defense suppression (Program A) reduces JA/SA, both of which potentiate ABA signaling → lower effective ABA. [KNOWN: JA–ABA synergy; INFERRED: SA–ABA interaction in seeds]
   - Epigenetic leakiness (Program B) allows partial expression of GA biosynthesis and ABA catabolism genes → ABA/GA ratio shifts. [INFERRED]
   - Metabolic reallocation (Program C) via TPS knockdown and SnRK1 activation promotes the catabolism of ABA itself (SnRK1 can phosphorylate and activate ABA 8′-hydroxylases in some contexts). [SPECULATIVE]
   - Ethylene receptor knockdown (SOV3g000150.1) amplifies the hormonal shift by derepressing ethylene signaling, which directly antagonizes ABA. [KNOWN]
   - The combined effect at the ABA/GA node is greater than any single pathway perturbation alone. [INFERRED: synergy hypothesis]

4. **Downstream execution proceeds through normal germination physiology**:
   - Cell wall loosening via ROS + ethylene-induced expansins + reduced glycosyltransferase-mediated wall reinforcement (SOV4g010600.1, SOV1g033840.1). [INFERRED]
   - Water uptake enhanced by reduced CCC cotransporter activity (SOV1g021960.1, SOV2g025380.1) → altered osmotic gradients → increased turgor → radicle protrusion. [INFERRED: CCC knockdown alters ion homeostasis; SPECULATIVE: net turgor effect]
   - Transport system reconfiguration: reduced CNGC (SOV1g018480.1) activity modulates Ca²⁺ signaling away from defense-associated Ca²⁺ spikes toward growth-associated Ca²⁺ oscillations. [SPECULATIVE]

5. **Net phenotypic outcome**: Faster, more uniform germination with enhanced seedling vigor, arising from the additive effects of multiple moderate perturbations rather than a single dramatic switch. The phenotype is predicted to be **robust to partial failure**—if any one target escapes silencing, the remaining perturbations still shift the system toward germination. This model predicts that the exRNA effect is **dose-dependent and graded** rather than all-or-nothing.

**Supporting evidence**:
- The growth–defense tradeoff is one of the most robust findings in plant ecology and molecular biology [KNOWN: Züst & Agrawal, 2017, *Annu. Rev. Plant Biol.*]
- Additive/synergistic effects of multi-target perturbations are well-documented in systems biology [KNOWN: general principle]
- The model explains the breadth of the target set (109 genes across 14 pathways) without requiring that all are primary drivers [INFERRED]
- T6P–SnRK1 signaling is a master metabolic switch conserved across angiosperms [KNOWN]
- The model naturally accounts for the observation that multiple bacterial species (with different exRNA profiles) can improve germination—different exRNA cocktails perturb different subsets of targets but converge on the same three programs [SPECULATIVE but parsimonious]
- Explains defense pathway targets (EDR2, MOS1, R-proteins) that are difficult to account for in purely epigenetic or hormonal models [INFERRED]

**Weaknesses**:
- The model is complex and difficult to falsify: because it invokes additive effects of many targets, no single-gene knockout would be expected to abolish the phenotype, making genetic validation challenging.
- The "resource reallocation" argument is qualitatively appealing but quantitatively unsubstantiated. How much ATP/carbon is actually saved by suppressing defense in a seed? The defense cost in a dry, dormant seed may be negligible.
- The model is most vulnerable to the confounder critique: EPS osmopriming could independently improve water uptake, bacterial volatiles could provide ethylene, and MAMP-triggered immunity suppression could occur through receptor desensitization rather than exRNA-mediated gene silencing. Distinguishing the exRNA-specific contribution from these confounders requires rigorous controls.
- The requirement for "moderate knockdown of many targets" is biologically demanding: it assumes the bacterial exRNA population is sufficiently diverse, abundant, and stable to engage >50 distinct mRNA targets simultaneously.
- Does not explain the transposon-related targets in a satisfying way (they are treated as collateral or noise).

**Testable predictions**:
1. Transcriptome-wide analysis (RNA-seq) should show **modest** (not dramatic) downregulation of many targets simultaneously, rather than strong knockdown of a few.
2. The germination advantage should be **partially resistant** to 1-MCP (ethylene inhibitor) or exogenous ABA, because multiple parallel pathways compensate.
3. Purified, protein-free, EPS-free bacterial exRNA fraction should improve germination; heat-denatured exRNA should not. Conversely, EPS fraction alone may partially improve germination through osmopriming, but the effect should be additive with exRNA.
4. Metabolomics should reveal increased ATP/ADP ratio and decreased T6P in treated seeds at 12–24 hours.
5. Defense marker gene expression (e.g., *PR1*, *PDF1.2* homologs) should be reduced in treated seeds even in the presence of MAMP elicitors, confirming immune suppression beyond simple MAMP desensitization.
6. The effect should be **dose-dependent**: serial dilutions of bacterial exRNA should produce a graded germination response.

---

## Model Comparison Table

| Feature | Model 1: Epigenetic Master Switch | Model 2: Hormonal Fulcrum | Model 3: Growth–Defense Reallocation |
|---|---|---|---|
| **Primary targets** | 6 epigenetic regulators (DNMT, SUVR5, HIRA, PHD, GIS2, rDNA regulator) | 3 hormone nodes (ETR, LOX, AHP) | ~25–30 targets across 3 programs (defense, epigenetic, metabolic) |
| **Targets directly explained** | ~30 (epigenetic + downstream cascades) | ~15 (hormone targets + direct downstream effectors) | ~80–90 (most of the 109 targets) |
| **Targets poorly explained** | Metabolic enzymes, transporters, transposons | Epigenetic regulators, transposons, most transporters | Transposons (partially), unknown function genes |
| **Mechanism complexity** | Low (single master switch) | Low (3-target model) | High (multi-pathway, additive) |
| **Temporal dynamics** | Slow onset (requires protein turnover of existing methyltransferases); persistent effect | Fast onset (mRNA knockdown → rapid protein depletion of short-lived receptors); transient effect | Intermediate onset; moderately persistent |
| **Confounder vulnerability** | Moderate (osmopriming could independently trigger passive demethylation) | High (bacterial volatiles could provide ethylene; EPS could alter water potential) | Moderate-high (multiple confounders could each explain part of the phenotype) |
| **Falsifiability** | High (WGBS, ChIP-seq, 5-azacytidine phenocopy) | High (1-MCP abolishment, hormone profiling) | Low (no single experiment can falsify; requires systems-level evidence) |
| **Parsimony** | Moderate | High | Low |
| **Robustness to partial failure** | Low (if DNMT escapes silencing, model collapses) | Low (if ETR escapes silencing, major effect lost) | High (redundancy across pathways) |
| **Explains breadth of target set** | Partially (many targets are "downstream") | Poorly (most targets are "noise") | Well (most targets contribute) |
| **Predicts dose-response** | Threshold effect | Threshold effect | Graded response |
| **Overall plausibility** | ★★★★☆ | ★★★★☆ | ★★★☆☆ (most comprehensive but hardest to test) |

---

## Recommended Model

**Model 2 (Hormonal Fulcrum) is recommended as the primary working hypothesis for experimental prioritization**, with elements of Model 1 incorporated as a secondary mechanism.

### Rationale:

1. **Parsimony and testability**: Model 2 makes the sharpest, most falsifiable predictions. The 1-MCP experiment alone could strongly support or refute the central role of ethylene receptor knockdown. Hormone profiling by LC-MS/MS is straightforward and would provide direct evidence for the predicted ABA/JA reduction. These experiments can be completed in weeks, not months.

2. **Mechanistic coherence with known biology**: The ethylene receptor as a negative regulator of germination is among the most well-established findings in seed biology. [KNOWN] LOX-mediated JA production as a germination inhibitor is similarly well-supported. [KNOWN] These are not speculative targets—they are high-confidence, experimentally validated nodes.

3. **The ethylene receptor is the single highest-ranked target in the entire dataset** (Tier 1, Rank 1 in the ranked target analysis), and all three hormone targets were independently rated "high priority." This internal consistency across independent analyses strengthens confidence.

4. **However, Model 2 alone cannot explain the full target set.** The epigenetic targets (DNMT, SUVR5, HIRA) are too prominent and too well-connected to be dismissed as noise. Therefore, a **hybrid Model 2+1** is most likely correct:
   - The **fast-acting** hormonal shift (Model 2) drives the initial germination decision within the first 12–24 hours of imbibition.
   - The **slower-acting** epigenetic de-repression (Model 1) sustains and amplifies this decision over 24–72 hours, ensuring robust commitment to germination and enhanced seedling vigor post-emergence.
   - The defense and metabolic targets (Model 3 elements) serve as **reinforcing modules** that increase the magnitude and uniformity of the effect but are not individually essential.

5. **Recommended experimental sequence**:
   - **Phase 1 (weeks 1–4)**: Test Model 2 core predictions—1-MCP treatment, ethephon/ibuprofen phenocopy, hormone profiling, qRT-PCR of ETR/LOX/AHP.
   - **Phase 2 (weeks 4–12)**: If Model 2 is supported, test Model 1 overlay—WGBS, ATAC-seq, 5-azacytidine phenocopy.
   - **Phase 3 (months 3–6)**: Purified exRNA fraction experiments with appropriate controls (heat-denatured exRNA, RNase-treated exRNA, purified EPS, synthetic mimics of predicted sRNA sequences targeting ETR/LOX/DNMT) to establish causality and rule out confounders.
   - **Phase 4**: If resources allow, CRISPR-mediated knockdown of top targets (ETR, LOX, DNMT) in spinach hairy root or protoplast systems to validate target identity.

### Final caveat:

All three models remain hypothetical until the fundamental question is answered: **Do bacterial exRNAs actually enter spinach seed cells and silence specific mRNAs?** This should be tested directly using fluorescently labeled synthetic sRNAs matching the predicted bacterial exRNA sequences, applied during imbibition, followed by confocal microscopy and target mRNA quantification. Without this evidence, even the most elegant causal model remains a castle built on sand. [CRITICAL UNKNOWN]