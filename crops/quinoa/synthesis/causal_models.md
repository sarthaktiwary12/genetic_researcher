# Causal Models — Quinoa (Chenopodium quinoa)



# Alternative Causal Models: Bacterial exRNA-Mediated Germination Improvement in *Chenopodium quinoa*

> **Critical Note on Species Translation**: The target gene IDs (SOV prefix) derive from *Spinacia oleracea* (spinach). Both spinach and quinoa belong to the Amaranthaceae s.l. (formerly Chenopodiaceae), sharing substantial synteny and gene family conservation. Mechanistic inferences are transferable at the pathway level, but direct ortholog validation in quinoa is essential before any translational application. All models below assume conserved function of spinach orthologs in quinoa. [INFERRED]

---

## Model 1: The Epigenetic Derepression Cascade ("Unlock the Blueprint")

**Core hypothesis**: Bacterial exRNAs primarily target the seed's epigenetic silencing machinery, causing a genome-wide chromatin relaxation event that derepresses dormancy-locked germination programs, with downstream hormonal and metabolic changes occurring as secondary consequences of transcriptional activation.

**Causal chain**:

1. **Bacterial exRNA enters seed cells via vesicle-mediated uptake during imbibition.** During the initial hours of seed hydration, bacterial outer membrane vesicles (OMVs) or free exRNAs (protected by protein complexes or secondary structure) are taken up by the rehydrating embryo cells through endocytosis or direct membrane fusion. The compromised membrane integrity characteristic of early imbibition facilitates entry. [SPECULATIVE — uptake mechanism in seeds is uncharacterized; extrapolated from cross-kingdom RNAi studies in *Arabidopsis* roots and mammalian gut epithelium (Cai et al., 2018, *Nature Plants*; Liu et al., 2012)]

2. **Epigenetic silencing machinery is dismantled (primary targets):**
   - **DNA (cytosine-5)-methyltransferase (SOV1g033340.1)** is downregulated → maintenance methylation at CG and CHG contexts fails during the first round of DNA replication post-imbibition → passive demethylation of promoters controlling GA biosynthesis genes (e.g., *GA3ox*, *GA20ox*), cell wall loosening enzymes, and cell cycle regulators. [KNOWN that maintenance methyltransferases are required to propagate methylation patterns; INFERRED that their loss derepresses germination-specific loci based on Arabidopsis methylome data from Narsai et al., 2017]
   - **SUVR5-like histone methyltransferase (SOV4g015450.1)** is downregulated → H3K9me2 deposition at heterochromatic loci ceases → transposable element (TE)-adjacent genes, which in plants are frequently developmental regulators, become accessible. [KNOWN that SUVR5 deposits repressive marks; INFERRED for germination context]
   - **HIRA histone chaperone (SOV6g036290.1)** is downregulated → altered H3.3 variant deposition dynamics → replication-independent histone turnover is disrupted, favoring retention of activating marks deposited by endogenous germination signals (GA-responsive chromatin remodelers). [KNOWN that HIRA deposits H3.3 at active genes; SPECULATIVE that its downregulation paradoxically favors germination — this could alternatively impair gene activation, representing a key weakness]
   - **GIS2 zinc finger protein (SOV4g038060.1)** is downregulated → stress-responsive transcriptional repression is lifted → growth-promoting genes (e.g., trichome/epidermal differentiation, cell expansion) are derepressed. [INFERRED from Arabidopsis GIS family function in trichome/growth regulation]
   - **PHD-domain protein (SOV4g030590.1)** is downregulated → reduced recruitment of Polycomb Repressive Complex 2 (PRC2) to H3K4me3-marked loci → PRC2-mediated H3K27me3 silencing of germination genes is attenuated. [INFERRED — PHD domains read histone marks; specific substrate unknown]

3. **Chromatin relaxation enables hormone pathway activation (secondary effects):**
   - Derepressed GA biosynthesis genes produce active gibberellins → DELLA repressor proteins are targeted for degradation via the GID1-SCF^SLY1 pathway → GA-responsive transcription factors activate α-amylases, cell wall hydrolases, and expansins. [KNOWN pathway in Arabidopsis and cereals]
   - Simultaneously, the ethylene receptor (SOV3g000150.1) — a negative regulator — is downregulated by exRNAs → constitutive ethylene signaling → EIN3/EIL1 transcription factors stabilized → activation of ethylene-responsive genes that antagonize ABA signaling (e.g., *ERF1* family members). [KNOWN: ethylene receptors are negative regulators; *etr1* loss-of-function enhances germination]
   - LOX (SOV3g035520.1) downregulation → reduced JA biosynthesis → relief of JA-mediated growth suppression and reduced JA-ABA synergistic dormancy maintenance. [KNOWN that JA and ABA synergize to maintain dormancy in many species; Arabidopsis *lox* mutants show altered germination]

4. **Transposon silencing is maintained through exRNA-mediated redundancy:**
   - The five retrotransposon-related genes (SOV2g004250.1, SOV4g025520.1, SOV3g033520.1, SOV1g003910.1, SOV4g035390.1) are directly silenced by bacterial exRNAs → despite the global reduction in host epigenetic silencing machinery, TEs remain suppressed → this prevents the metabolic drain and insertional mutagenesis that would otherwise accompany chromatin relaxation. [SPECULATIVE — this is a key prediction of Model 1 that distinguishes it from Models 2 and 3; it implies the bacterial exRNAs provide a "safety net" for TE control]

5. **Net phenotypic outcome**: Faster, more uniform germination driven by genome-wide transcriptional activation of dormancy-repressed gene programs. Seedling vigor is enhanced because the epigenetic "reset" produces a transcriptional state equivalent to a seed that has undergone complete, natural dormancy release (after-ripening), but achieved in hours rather than weeks/months. Predicted: earlier radicle protrusion (6–12 h advantage), more synchronous germination across a seed lot, and enhanced hypocotyl/radicle elongation rates.

**Supporting evidence**:
- DNA methylation dynamics are central to seed dormancy cycling in Arabidopsis [KNOWN — Footitt et al., 2015, *PNAS*]
- Global demethylation via 5-azacytidine treatment accelerates germination in multiple species [KNOWN]
- SUVR5 loss-of-function in Arabidopsis causes derepression of developmental genes [KNOWN — Caro et al., 2012]
- Cross-kingdom RNA transfer via OMVs is documented in *Botrytis*-plant and *Rhizobium*-soybean systems [KNOWN — Weiberg et al., 2013; Ren et al., 2019]
- Quinoa seeds have notably deep dormancy involving epigenetic regulation [INFERRED from Chenopodium germination biology]

**Weaknesses**:
- **HIRA paradox**: HIRA typically deposits H3.3 at *active* gene bodies; its downregulation could impair rather than promote transcription. The model requires that HIRA's role in seeds is primarily in maintaining dormancy-associated chromatin states (e.g., depositing H3.3 at stress-responsive loci), which is not established. [SPECULATIVE]
- **Lacks temporal resolution**: Epigenetic reprogramming is typically slow (requiring at least one cell division for passive demethylation). Early imbibition effects (0–6 h) may precede any meaningful chromatin changes, suggesting this model cannot explain the earliest germination improvements.
- **Does not directly explain** the cell wall remodeling, transport/ion homeostasis, or ROS pathway targets — these must be treated as downstream or parallel effects.
- **Confounder**: Bacterial EPS osmopriming could independently improve imbibition kinetics, and polysaccharide elicitors could trigger some chromatin changes independently of exRNAs.

**Testable predictions**:
1. **Bisulfite sequencing**: exRNA-treated quinoa embryos should show reduced DNA methylation at germination-promoting gene promoters (e.g., *CqGA3ox1*, *CqEXPA* genes) compared to mock-treated controls at 12–24 h post-imbibition.
2. **ChIP-seq for H3K9me2**: Global reduction in repressive histone marks at non-TE loci in treated seeds.
3. **5-azacytidine phenocopy**: Chemical demethylation should partially mimic the exRNA germination phenotype; combining 5-azacytidine with exRNA treatment should show diminishing returns (epistasis).
4. **TE expression**: Despite global chromatin relaxation, TE transcript levels should remain low in exRNA-treated seeds (due to direct TE silencing by exRNAs) — distinguishing this from simple chemical demethylation where TEs would be activated.
5. **Time-course transcriptomics**: Germination gene derepression should lag behind exRNA uptake by >6 h if this model is correct (epigenetic changes require time).

---

## Model 2: The Hormonal Rebalancing Hub ("Cut the Brakes, Press the Gas")

**Core hypothesis**: Bacterial exRNAs directly and simultaneously target three master hormonal nodes — ethylene perception, JA biosynthesis, and cytokinin relay — to shift the ABA/GA balance decisively toward germination, with all other observed target effects being downstream consequences of this hormonal reprogramming.

**Causal chain**:

1. **Bacterial exRNAs enter embryo cells during early imbibition (0–6 h)** via symplastic uptake through the hydrated seed coat and endosperm, potentially facilitated by plasmodesmata-like connections or receptor-mediated endocytosis of RNA-protein complexes. Mature siRNAs (21–24 nt) are loaded into quinoa AGO proteins (likely AGO1 or AGO4 orthologs) to form functional RISC complexes. [SPECULATIVE for mechanism; KNOWN that plant AGO proteins can load exogenous sRNAs]

2. **Three hormonal nodes are simultaneously disrupted (primary targets):**

   **Node A — Ethylene receptor (SOV3g000150.1) downregulated:**
   - The ethylene receptor is a negative regulator: in its default (ligand-free) state, it activates CTR1 kinase, which phosphorylates and inactivates EIN2, blocking ethylene signaling. [KNOWN]
   - Downregulation of the receptor → loss of CTR1 activation → EIN2 C-terminal fragment is cleaved and translocates to the nucleus → EIN3/EIL1 transcription factors are stabilized → constitutive ethylene response. [KNOWN pathway]
   - Ethylene signaling directly antagonizes ABA: EIN3 promotes expression of ABA catabolic gene *CYP707A* (ABA 8'-hydroxylase) and represses ABA biosynthesis gene *NCED*. [KNOWN — Linkies et al., 2009, *Plant Cell*]
   - Ethylene also promotes endosperm cap weakening via induction of cell wall hydrolases and expansins. [KNOWN in Lepidium, a Brassicaceae; INFERRED for Amaranthaceae]

   **Node B — Lipoxygenase/LOX (SOV3g035520.1) downregulated:**
   - LOX catalyzes the first committed step of JA biosynthesis (oxygenation of α-linolenic acid → 13-HPOT). [KNOWN]
   - Reduced LOX → reduced JA and JA-Ile production → reduced activation of JAZ-MYC2 signaling module. [KNOWN pathway]
   - JA normally synergizes with ABA to maintain dormancy: JA-Ile promotes expression of ABA biosynthesis genes and ABA signaling components (e.g., *ABI3*, *ABI5*). [KNOWN — Dave et al., 2011, *J. Exp. Bot.*]
   - JA also diverts resources to defense (glucosinolate/phenylpropanoid biosynthesis); its reduction frees metabolic precursors for growth. [KNOWN]
   - **Secondary ROS effect**: LOX-derived lipid peroxides are a major source of cytotoxic ROS during imbibition; LOX downregulation reduces oxidative damage to membranes and proteins, improving cellular viability. [KNOWN — Bailly, 2004, *Seed Science Research*]

   **Node C — AHP-like phosphotransfer protein (SOV4g032870.1) downregulated:**
   - AHPs relay phosphoryl groups from histidine kinase receptors (AHKs) to type-B response regulators (ARRs) in the cytokinin two-component signaling system. [KNOWN]
   - Downregulation of AHP → attenuated cytokinin signal transduction. [KNOWN]
   - In the germination context, the effect is complex but likely positive: AHP proteins also participate in ABA signaling crosstalk. In Arabidopsis, *ahp2,3,5* triple mutants show enhanced ABA insensitivity. [KNOWN — Nishimura et al., 2004] → Reduced AHP → reduced ABA sensitivity → germination promoted.
   - Additionally, cytokinin signaling can promote cell differentiation over cell division in certain contexts; its attenuation may favor the rapid, undifferentiated cell expansion needed for radicle emergence. [INFERRED]

3. **Hormonal rebalancing cascades through downstream pathways:**

   - **ABA catabolism activated + ABA biosynthesis suppressed** (via ethylene-EIN3 and JA reduction) → ABA levels drop → ABI5 protein is destabilized by 26S proteasome → DELLA proteins lose ABA-mediated stabilization → GA signaling is fully derepressed. [KNOWN for individual steps; INFERRED for integrated cascade]
   
   - **GA signaling activates cell wall remodeling**: GA-responsive MYB transcription factors induce expression of endo-β-mannanases, expansins, and xyloglucan endotransglucosylases in the endosperm cap. The exRNA-mediated downregulation of glycosyltransferases (SOV4g010600.1, SOV1g033840.1) and beta-galactosidase (SOV4g051070.1) further tips the balance toward net wall loosening by reducing wall reinforcement. [KNOWN for GA-wall enzyme link; INFERRED for specific targets]
   
   - **Defense pathway suppression is a hormonal consequence**: Reduced JA → reduced expression of JA-responsive defense genes → EDR2 (SOV3g043450.1, SOV6g048760.1), R-proteins, and NST1 are no longer maintained at high levels. The exRNA-mediated direct downregulation of these defense genes reinforces the hormonal signal. [INFERRED — defense gene expression is hormone-dependent]
   
   - **Metabolic reprogramming follows hormonal cues**: Reduced ABA → TPS (SOV2g009230.1) expression is no longer maintained (TPS is ABA-responsive in many species) → T6P levels drop → SnRK1 kinase is derepressed → SnRK1 activates catabolic pathways (lipid mobilization, starch degradation) and suppresses anabolic pathways → stored reserves are rapidly mobilized. [KNOWN for T6P-SnRK1 axis; INFERRED for ABA-TPS link in quinoa seeds]

4. **Net phenotypic outcome**: Rapid and decisive shift from ABA-dominated dormancy to GA/ethylene-dominated germination. Predicted: significant reduction in time to 50% germination (T50), particularly under mild abiotic stress (moderate salinity, suboptimal temperature) where ABA would normally delay germination. Enhanced radicle elongation rate due to combined cell wall loosening and turgor-driven expansion. Improved stress tolerance of emerging seedlings due to maintained (but not excessive) ROS signaling.

**Supporting evidence**:
- Ethylene receptor mutants (*etr1-1* gain-of-function = delayed germination; *etr1* loss-of-function = enhanced germination) are among the best-characterized germination phenotypes in Arabidopsis [KNOWN — Bleecker et al., 1988; Chiwocha et al., 2005]
- JA-deficient mutants (*opr3*, *aos*) show enhanced germination under ABA [KNOWN — Dave et al., 2011]
- The ABA-ethylene antagonism in germination is conserved across angiosperms [KNOWN — Linkies & Leubner-Metzger, 2012, *New Phytologist*]
- Quinoa is notably salt-tolerant, and ABA signaling is central to its stress responses; modulation of ABA sensitivity would have outsized effects on germination under the saline conditions where quinoa is often grown [KNOWN for quinoa ABA biology; INFERRED for exRNA relevance]
- The three hormone targets are all rated "high priority" in the pathway analysis [KNOWN from provided data]

**Weaknesses**:
- **Epigenetic targets unexplained as downstream**: This model treats the six epigenetic regulators (DNA methyltransferase, SUVR5, HIRA, GIS2, PHD protein, rDNA regulator) as secondary effects of hormonal changes. However, hormonal signaling does not typically cause rapid downregulation of epigenetic writers — these are more likely direct exRNA targets, suggesting the hormonal model is incomplete.
- **Transport/ion homeostasis targets poorly explained**: The 18 transport genes, including two CCC cotransporters and a CNGC channel, are not obvious downstream targets of ethylene/JA/cytokinin signaling. Their inclusion in the target set suggests a parallel, non-hormonal mechanism.
- **Assumes rapid RISC loading and target cleavage**: For hormonal effects to manifest within the germination timeframe (12–48 h), exRNAs must be loaded into RISC and cleave targets within hours. This is plausible but undemonstrated in seeds.
- **Confounder**: Bacterial volatiles (e.g., 2,3-butanediol, acetoin) are known to promote plant growth via ethylene-independent mechanisms; if the bacterial culture produces volatiles during seed treatment, the ethylene receptor downregulation may be redundant with volatile effects.

**Testable predictions**:
1. **Hormone quantification**: exRNA-treated quinoa seeds should show reduced ABA and JA-Ile levels and elevated ethylene production (or ethylene-independent EIN3 accumulation) at 12–24 h post-imbibition, measurable by LC-MS/MS.
2. **Ethylene receptor epistasis**: Treating quinoa seeds with 1-MCP (ethylene perception inhibitor, blocks at receptor level) should partially abolish the exRNA germination benefit if this model is correct. Conversely, ACC (ethylene precursor) treatment should partially phenocopy exRNA effects.
3. **JA rescue**: Exogenous methyl-JA application should antagonize the exRNA germination benefit in a dose-dependent manner.
4. **ABA sensitivity assay**: exRNA-treated seeds should germinate at higher rates than controls on ABA-supplemented media, demonstrating reduced ABA sensitivity.
5. **Minimal exRNA set**: Synthetic sRNAs targeting only the three hormone nodes (ethylene receptor + LOX + AHP) should recapitulate >50% of the full exRNA germination benefit if this model is correct.

---

## Model 3: The Integrated Defense-to-Growth State Transition ("Flip the Switch")

**Core hypothesis**: Bacterial exRNAs do not act through a single dominant pathway but instead execute a coordinated, multi-target state transition — analogous to a developmental phase change — that simultaneously disarms defense, opens chromatin, rebalances hormones, and reconfigures metabolism, with the synergy between these parallel actions being essential for the full phenotype.

**Causal chain**:

1. **Bacterial exRNAs enter seed cells as a complex mixture (>100 distinct sRNA species) during imbibition**, likely via multiple uptake routes including OMV fusion, clathrin-mediated endocytosis, and passive diffusion through rehydration-damaged membranes. The diversity of sRNA sequences enables simultaneous targeting of genes across all 14 identified pathway groups. Different sRNA species are loaded into different AGO protein paralogs (AGO1 for 21-nt miRNA-like species targeting mRNAs; AGO4 for 24-nt species directing transcriptional silencing via RdDM), enabling both post-transcriptional gene silencing (PTGS) and transcriptional gene silencing (TGS). [SPECULATIVE for dual AGO loading; KNOWN that plants have multiple AGO proteins with size preferences]

2. **Four parallel modules are activated simultaneously (all are primary targets):**

   **Module I — Epigenetic Unlocking (6 targets):**
   - DNA methyltransferase (SOV1g033340.1), SUVR5 (SOV4g015450.1), HIRA (SOV6g036290.1), GIS2 (SOV4g038060.1), PHD protein (SOV4g030590.1) → chromatin relaxation at germination gene loci. [INFERRED]
   - This module operates on a 12–48 h timescale, providing sustained transcriptional activation that amplifies the effects of the other modules over time. [INFERRED]
   - Critically, this module also includes the 5 retrotransposon genes, which are silenced to prevent genomic instability during the chromatin relaxation event. [SPECULATIVE — elegant but unproven]

   **Module II — Hormonal Rebalancing (3 targets):**
   - Ethylene receptor, LOX, AHP → constitutive ethylene signaling, reduced JA, reduced ABA sensitivity (detailed in Model 2). [KNOWN/INFERRED as above]
   - This module operates on a 6–24 h timescale, providing the earliest measurable effects on germination commitment. [INFERRED]

   **Module III — Defense Disarmament & Resource Liberation (5+ targets):**
   - EDR2 × 2 (SOV3g043450.1, SOV6g048760.1), MOS1-like (SOV5g005530.1), R-protein (SOV1g021670.1), NST1 (SOV3g021300.1) → immune signaling capacity is broadly reduced. [INFERRED]
   - MYB (SOV1g020340.1) and NAC (SOV2g014810.1) transcription factors → stress-responsive transcriptional programs are suppressed. [INFERRED — many MYB/NAC members regulate defense/stress]
   - RLKs (SOV1g027650.1, SOV4g000660.1) → surface perception of PAMPs/DAMPs is attenuated. [INFERRED]
   - **Quantitative resource effect**: Defense protein synthesis consumes ~15–30% of cellular ATP and amino acid pools in stress-primed seeds (estimated from defense proteome studies). [SPECULATIVE for exact values; KNOWN that defense is metabolically costly]
   - This module operates on a 6–18 h timescale as existing defense transcripts are degraded and not replaced. [INFERRED]

   **Module IV — Physiological Execution (transport, ROS, metabolism, cell wall — ~40 targets):**
   - **Ion/osmotic reconfiguration**: CCC cotransporters (SOV1g021960.1, SOV2g025380.1) downregulated → altered Cl⁻/K⁺/Na⁺ balance → reduced salt accumulation in embryo cells → improved turgor regulation. CNGC (SOV1g018480.1) downregulated → reduced Ca²⁺ influx through this channel → attenuated Ca²⁺-dependent stress signaling (calmodulin, CDPK pathways). [INFERRED — CCC and CNGC functions extrapolated from Arabidopsis]
   - **ROS window optimization**: Peroxidase (SOV3g038840.1) and GST (SOV3g040200.1) downregulated → reduced ROS scavenging → ROS levels rise to the "oxidative window" that promotes cell wall loosening and ABA catabolism. Simultaneously, LOX downregulation (Module II) prevents excessive lipid peroxidation. The net effect is a *shift in ROS composition* from damaging lipid peroxides toward signaling-competent H₂O₂. [KNOWN for oxidative window concept — Bailly et al., 2008; INFERRED for compositional shift]
   - **Metabolic channeling**: TPS (SOV2g009230.1) downregulated → T6P drops → SnRK1 activated → catabolic mobilization of reserves. 6-PGD (SOV6g029280.1) downregulated → reduced NADPH from oxidative PPP → forces the cell to rely on fermentative/glycolytic ATP production, which is faster (though less efficient) and appropriate for the anaerobic/hypoxic conditions inside an imbibing seed. [KNOWN for T6P-SnRK1; SPECULATIVE for 6-PGD interpretation — could alternatively impair NADPH supply]
   - **Cell wall loosening**: Glycosyltransferases down → reduced wall reinforcement; combined with GA-induced hydrolase expression from Module II → net wall weakening → radicle emergence. [INFERRED]
   - **DNA damage checkpoint attenuation**: ATR kinase (SOV4g051610.1) downregulated → relaxed G2/M checkpoint → cells proceed through division even with some residual DNA damage → faster cell cycle progression in the radicle meristem. This is a "calculated risk" that trades some genomic fidelity for speed. [KNOWN that ATR regulates checkpoint; SPECULATIVE that its reduction is beneficial — could increase mutation rate]
   - This module operates on a 12–72 h timescale, providing the physical and metabolic execution of germination after the decision is made by Modules I–III. [INFERRED]

3. **Synergistic interactions between modules create emergent robustness:**
   - **Module I × Module II**: Epigenetic unlocking makes hormone-responsive promoters accessible, amplifying the effect of hormonal rebalancing. Conversely, ethylene signaling (from Module II) can promote active DNA demethylation via induction of *DEMETER*-like glycosylases. [KNOWN for ethylene-demethylase link in Arabidopsis endosperm — Yao et al., 2012]
   - **Module II × Module III**: Reduced JA (Module II) directly reduces defense gene expression (Module III), creating a feed-forward loop. [KNOWN]
   - **Module III × Module IV**: Resources freed from defense (Module III) are channeled into the metabolic and transport processes of Module IV. [INFERRED]
   - **Module I × Module IV**: Chromatin relaxation at cell wall enzyme gene loci enables their transcription in response to GA signals. [INFERRED]
   - **The system exhibits bistability**: The dormant state (high ABA, closed chromatin, active defense, low metabolism) and the germinating state (low ABA, open chromatin, suppressed defense, high metabolism) are both self-reinforcing. The bacterial exRNAs push the system past a tipping point from one stable state to the other. Once committed, the germination state is maintained by endogenous positive feedback loops even after exRNA degradation. [SPECULATIVE but consistent with dynamical systems models of germination — Topham et al., 2017, *PNAS*]

4. **Net phenotypic outcome**: Maximum germination improvement — faster T50, higher final germination percentage (especially under stress), more uniform emergence, enhanced seedling vigor (longer radicles, heavier seedlings). The multi-module architecture provides robustness: partial failure of any single module is compensated by the others. Predicted: the full phenotype cannot be recapitulated by targeting any single module alone; at least 2–3 modules must be engaged simultaneously.

**Supporting evidence**:
- Systems biology models of Arabidopsis germination identify bistable switches controlled by ABA/GA ratio, ROS levels, and chromatin state [KNOWN — Topham et al., 2017; Née et al., 2017]
- Cross-kingdom RNAi involves diverse sRNA populations targeting multiple genes simultaneously [KNOWN — Weiberg et al., 2013; Cai et al., 2018]
- The target set shows strong enrichment for regulatory/signaling genes over metabolic enzymes, consistent with a state-transition mechanism rather than metabolic perturbation [KNOWN from provided data]
- Quinoa germination is known to be sensitive to the ABA/GA balance, salinity, and temperature — all of which are addressed by different modules in this model [KNOWN for quinoa germination biology]
- Defense-growth tradeoffs are well-documented in Chenopodiaceae, including quinoa responses to biotic stress [KNOWN]
- Multi-target RNAi (e.g., multiplexed CRISPR or cocktail sRNA delivery) produces stronger phenotypes than single-target approaches in plant biotechnology [KNOWN]

**Weaknesses**:
- **Complexity is a liability for falsification**: With >100 targets and 4 interacting modules, this model can accommodate almost any experimental result, making it difficult to rigorously falsify. This is a hallmark of "just-so" stories in systems biology.
- **Assumes all targets are genuine**: Many of the 110+ targets may be off-target effects, annotation errors (e.g., the cry8Ba protein), or targets with no phenotypic consequence. The model's explanatory power is inflated by including low-confidence targets.
- **Dual AGO loading is undemonstrated**: The claim that bacterial exRNAs simultaneously engage PTGS (AGO1) and TGS (AGO4) pathways is elegant but has no direct evidence in any cross-kingdom system.
- **Bistability claim is unfalsifiable without modeling**: Without a quantitative dynamical systems model parameterized with quinoa-specific data, the bistability assertion is hand-waving.
- **Confounders are maximally problematic for this model**: Because the model invokes so many pathways, it is most vulnerable to alternative explanations (EPS osmopriming, bacterial volatile effects, microbiome shifts on the seed surface) that could independently affect subsets of the observed phenotype.

**Testable predictions**:
1. **Module sufficiency test**: Deliver synthetic sRNA cocktails targeting only Module I (epigenetic), only Module II (hormonal), only Module III (defense), or combinations. Prediction: no single module recapitulates >40% of the full exRNA phenotype; the combination of any two modules achieves 60–80%; all three are needed for >90%.
2. **Temporal transcriptomics**: RNA-seq at 3, 6, 12, 24, 48 h post-imbibition should reveal a temporal cascade: defense genes down first (6 h), hormone-responsive genes changing next (12 h), epigenetic target genes declining by 24 h, and metabolic/structural genes shifting last (24–48 h).
3. **sRNA-seq of treated seeds**: Small RNA sequencing of embryo cells should detect bacterial-origin sRNAs loaded into immunoprecipitated AGO1 and AGO4 complexes, confirming dual pathway engagement.
4. **Bistability test**: Seeds treated with exRNAs for only 2 h (brief pulse) then washed should still show improved germination if the system has crossed the tipping point. Untreated seeds given the same 2-h imbibition without exRNAs should not.
5. **Dose-response curve**: If the model is correct, the germination response to exRNA concentration should be sigmoidal (switch-like) rather than linear, reflecting the bistable transition.

---

## Model Comparison Table

| Feature | Model 1: Epigenetic Derepression | Model 2: Hormonal Rebalancing | Model 3: Integrated State Transition |
|---------|----------------------------------|-------------------------------|--------------------------------------|
| **Primary driver** | Chromatin relaxation (6 epigenetic targets) | 3 hormone signaling nodes | Parallel multi-module action (all 110+ targets) |
| **Targets directly explained** | ~17 (epigenetic + TE + downstream hormone) | ~25 (hormone nodes + downstream defense, metabolism, cell wall) | ~100+ (all pathway groups) |
| **Targets requiring secondary explanation** | ~90+ (transport, defense, metabolism treated as downstream) | ~85+ (epigenetic, transport, many metabolic targets) | ~10 (annotation artifacts, unknowns) |
| **Mechanism complexity** | Moderate — single upstream trigger, downstream cascade | Low-moderate — three parallel triggers, known cascades | High — four parallel modules with cross-talk |
| **Temporal prediction** | Slow onset (12–48 h for epigenetic changes) | Fast onset (6–12 h for hormone effects) | Staged onset (6–48 h, different modules at different times) |
| **Falsifiability** | High — specific epigenetic marks can be measured | High — hormone levels and sensitivity directly testable | Low-moderate — complexity makes clean falsification difficult |
| **Explains stress-condition benefits** | Partially (chromatin state affects stress gene regulation) | Strongly (ABA sensitivity reduction directly relevant) | Strongly (multiple stress-relevant modules) |
| **Explains seedling vigor (post-germination)** | Strongly (sustained transcriptional reprogramming) | Moderately (hormonal effects may be transient) | Strongly (metabolic and organellar changes persist) |
| **Vulnerability to confounders** | Moderate (EPS unlikely to cause epigenetic changes) | High (bacterial volatiles could mimic ethylene effects) | Very high (multiple confounders could explain subsets) |
| **Key testable prediction** | Bisulfite-seq shows demethylation at germination loci | 1-MCP blocks >50% of germination benefit | Sigmoidal dose-response; no single module sufficient |
| **Overall plausibility** | ★★★☆☆ (strong mechanism but poor temporal fit for early effects) | ★★★★☆ (parsimonious, testable, explains core phenotype) | ★★★★★ for realism; ★★☆☆☆ for parsimony |

---

## Recommended Model

**Model 2 (Hormonal Rebalancing Hub) is recommended as the primary working hypothesis**, with elements of Model 3 incorporated as the research program matures.

### Rationale:

1. **Parsimony**: Model 2 explains the core germination phenotype through only three high-confidence, high-priority targets (ethylene receptor, LOX, AHP) with well-characterized mechanisms in Arabidopsis. The principle of parsimony favors this model as the starting point. [KNOWN that all three targets are rated "high priority"]

2. **Testability**: Model 2 generates the most cleanly falsifiable predictions. Hormone quantification (ABA, JA-Ile, ethylene), pharmacological epistasis (1-MCP, methyl-JA, ABA sensitivity assays), and synthetic sRNA reconstitution experiments are all feasible with existing quinoa germination assays. If the three-target synthetic sRNA cocktail fails to recapitulate the phenotype, Model 2 is falsified and Model 3 gains support.

3. **Temporal coherence**: Hormonal changes can manifest within 6–12 h of target mRNA degradation, consistent with the rapid germination improvements typically observed in seed priming experiments. Epigenetic changes (Model 1) are too slow to explain early effects, while Model 3's staged cascade, though realistic, is difficult to validate without extensive time-course data.

4. **Translational relevance for quinoa**: Quinoa is frequently cultivated in saline, arid environments where ABA-mediated germination delay is a major agronomic constraint. A model centered on ABA sensitivity reduction has direct breeding and biotechnology implications — e.g., identifying quinoa *CqETR* alleles with reduced expression as targets for marker-assisted selection.

5. **Pathway to Model 3**: Model 2 should be treated as the "minimal sufficient model." As experimental data accumulate (particularly from module sufficiency tests and temporal transcriptomics), Model 3's additional modules can be incorporated if Model 2 proves insufficient to explain the full phenotypic variance. The recommended experimental progression is:
   - **Phase 1**: Test Model 2 predictions (hormone assays, pharmacological epistasis) → establishes whether hormonal rebalancing is necessary and sufficient.
   - **Phase 2**: If Model 2 explains <70% of variance, test epigenetic module (bisulfite-seq, ChIP) → determines if Model 1 elements are needed.
   - **Phase 3**: Full module interaction analysis (combinatorial synthetic sRNAs, systems modeling) → validates or refines Model 3.

> **Final caveat**: All three models assume that bacterial exRNAs are the active agent. The most critical control experiment — testing heat-denatured or RNase-treated bacterial exRNA preparations against intact preparations, with EPS concentration held constant — must be performed before any mechanistic model is pursued. If RNase treatment abolishes the germination benefit, exRNA causality is supported. If not, the phenotype may be driven primarily by EPS osmopriming or other non-RNA bacterial factors, and all three models become moot. [KNOWN experimental design principle; CRITICAL confounder]