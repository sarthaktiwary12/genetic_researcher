# Causal Models



# Alternative Causal Models: Bacterial exRNA-Mediated Germination Enhancement in *Spinacia oleracea*

---

## Preamble: Shared Assumptions and Caveats

All three models below share a common upstream assumption: bacterial extracellular small RNAs (exRNAs) are delivered to seed cells and engage the host RNA-induced silencing complex (RISC) to post-transcriptionally downregulate specific mRNA targets. **This assumption itself is unvalidated in this system** [SPECULATIVE]. The mechanism of uptake (vesicle-mediated, pore-mediated, or passive during imbibition through a compromised testa) is unknown. All models must be evaluated against the critical confounder set: (i) EPS-mediated osmopriming, (ii) bacterial polysaccharide elicitor effects (PAMP/DAMP modulation), (iii) microbiome community restructuring on the seed surface, and (iv) small-molecule metabolites co-delivered with exRNAs. The three models are not mutually exclusive; they represent alternative *primary causal logics* that assign different hierarchical weights to the 103 targets.

---

## Model 1: The Hormonal Fulcrum Model — "Tip the ABA/GA Balance, Everything Else Follows"

**Core hypothesis**: Bacterial exRNAs primarily target three hormonal signaling nodes whose simultaneous downregulation shifts the ABA/GA/ethylene balance decisively toward germination, with all other observed target effects being secondary consequences of this hormonal reprogramming.

**Causal chain**:

1. **Bacterial exRNA enters seed cells via imbibition-facilitated uptake.** During Phase I/II of water uptake, the hydrating testa and endosperm become permeable. Bacterial exRNAs, potentially packaged in outer membrane vesicles (OMVs) or associated with RNA-binding proteins, are taken up passively or via endocytosis into embryo and endosperm cells. Once internalized, exRNAs are loaded onto AGO1 or AGO4-containing RISC complexes [SPECULATIVE — cross-kingdom RISC loading demonstrated in *Arabidopsis*–*Botrytis* system (Weiberg et al., 2013 *Science*), but not in bacteria-to-plant seed contexts].

2. **Three hormonal master targets are downregulated simultaneously:**

   - **SOV3g000150.1 (Ethylene receptor)** is silenced → constitutive de-repression of ethylene signaling [KNOWN mechanism in Arabidopsis: ethylene receptors are negative regulators; *etr1* loss-of-function mutants show constitutive ethylene responses (Bleecker & Kende, 2000)]. Active ethylene signaling directly antagonizes ABA action via EIN3-mediated degradation of ABI5 and promotes GA biosynthesis through upregulation of *GA20ox* and *GA3ox* [KNOWN — Linkies et al. (2009) *Plant Cell*; Corbineau et al. (2014) *Plant Sci*]. Ethylene also directly promotes endosperm weakening via induction of cell wall hydrolases [KNOWN — Müller et al. (2006)].

   - **SOV3g035520.1 (Lipoxygenase / LOX)** is silenced → reduction of jasmonic acid (JA) biosynthesis and ABA precursor production [KNOWN — LOX catalyzes the first committed step in JA biosynthesis via the octadecanoid pathway; LOX also generates reactive aldehydes that promote ABA accumulation in seeds (Feussner & Wasternack, 2002 *Annu Rev Plant Biol*)]. Reduced JA removes a synergistic inhibitor of germination that normally cooperates with ABA [KNOWN — JA and ABA synergistically inhibit germination in Arabidopsis (Dave et al., 2011 *Plant Cell*)]. Reduced lipid peroxidation also lowers oxidative damage during imbibition [INFERRED].

   - **SOV4g032870.1 (AHP-like histidine phosphotransfer protein)** is silenced → disruption of cytokinin two-component signaling [KNOWN — AHPs relay phosphotransfer from cytokinin receptors (AHKs) to type-B ARR transcription factors]. In the germination context, cytokinin signaling can promote ABA sensitivity and inhibit germination in some species [KNOWN — Guan et al. (2014) showed AHP-mediated cytokinin signaling enhances ABI5 stability in Arabidopsis]. Silencing AHP thus reduces ABA sensitivity [INFERRED]. However, this target is complex because some AHPs negatively regulate ABA signaling (e.g., AHP2/3/5 in Arabidopsis), meaning the net effect depends on which AHP homolog is involved [CAVEAT — spinach AHP functional specificity is unknown].

3. **The hormonal shift cascades through downstream pathways:**

   - **Elevated ethylene + reduced ABA/JA → increased GA/ABA ratio** [INFERRED]. This ratio is the master switch for germination commitment [KNOWN — Finch-Savage & Leubner-Metzger (2006) *New Phytol*].
   - The increased GA/ABA ratio activates DELLA protein degradation via the GID1-SCFSLY1 pathway [KNOWN], which de-represses GA-responsive transcription including cell wall hydrolases (mannanases, XTHs, expansins), storage reserve mobilization enzymes (α-amylases), and growth-promoting genes.
   - Reduced ABA signaling leads to ABI5 destabilization [KNOWN — Lopez-Molina et al. (2001) *PNAS*], releasing the transcriptional brake on post-germinative growth.
   - The epigenetic targets (SOV1g033340.1, DNA methyltransferase; SOV4g015450.1, SUVR5) are explained as *secondary*: the hormonal shift toward GA/ethylene dominance transcriptionally downregulates maintenance methyltransferases and repressive histone modifiers as part of the normal developmental transition from dormancy to growth [INFERRED — GA signaling promotes chromatin decondensation at germination loci in Arabidopsis (Müller et al., 2012)]. In this model, exRNA-mediated silencing of epigenetic targets merely accelerates what the hormonal shift would eventually accomplish.
   - The defense targets (EDR2, MOS1, R-proteins) are explained as downstream of reduced JA: since JA is a major defense hormone, its reduction naturally attenuates defense pathway expression [INFERRED].

4. **Net phenotypic outcome**: Faster, more uniform radicle emergence due to earlier commitment to the germination developmental program; enhanced endosperm weakening from ethylene-induced hydrolases; more vigorous seedling growth from earlier DELLA degradation and reserve mobilization. **Specific prediction**: germination speed improvement should be greatest under conditions where ABA levels are elevated (e.g., osmotic stress, high temperature), because the hormonal targets remove the ABA-mediated block.

**Supporting evidence**:
- Ethylene receptor loss-of-function (*etr1-1*) constitutively activates germination in Arabidopsis [KNOWN — Bleecker lab, multiple publications]
- LOX antisense lines show reduced dormancy in barley [KNOWN — Bailly et al. (2002)]
- The three hormonal targets are all ranked Tier 1 (highest priority) in the ranked analysis [KNOWN from provided data]
- Cross-kingdom RNA silencing has been demonstrated for fungal sRNAs targeting plant AGO1-loaded RISC [KNOWN — Weiberg et al. (2013)]
- Ethylene priming of seeds is a well-established agricultural practice [KNOWN]

**Weaknesses**:
- This model treats 100 of 103 targets as secondary/downstream, which is parsimonious but potentially oversimplified. If many targets are independently silenced by distinct exRNA species, a purely hormonal model underestimates the direct contribution of other pathways.
- Cannot explain why so many distinct exRNA-target pairs would evolve if only three matter. The bacterial genome would be under no selective pressure to produce exRNAs targeting, e.g., DNA polymerases or reverse transcriptases, if the phenotype is entirely hormone-driven.
- The AHP target is ambiguous: depending on the specific homolog, its silencing could either promote or inhibit germination [CAVEAT].
- The model predicts that exogenous ABA application should partially rescue the germination-inhibitory state; if it does not, the hormonal primacy is weakened.
- **Major confounder**: Ethylene is produced during bacterial metabolism, and EPS osmopriming itself can alter the ABA/GA ratio. The observed hormonal shift may not require exRNA-mediated gene silencing at all.

**Testable predictions**:
1. **AGO-immunoprecipitation (AGO-IP)** from imbibing seeds treated with bacterial exRNAs should recover exRNA-SOV3g000150.1 (ethylene receptor) duplexes at high frequency.
2. **Exogenous ABA rescue**: Treating exRNA-primed seeds with 10–100 µM ABA should substantially (>50%) reverse the germination acceleration if the hormonal fulcrum is the primary mechanism.
3. **Ethylene-insensitive spinach mutants** (if available, or generated via EIN2 CRISPR knockout) should show dramatically reduced response to bacterial exRNA treatment.
4. **LOX activity assay**: 13-HPOT/13-HPOD levels should be measurably reduced in exRNA-treated seeds within 12–24 h of imbibition.
5. **Hormone profiling**: GC-MS/LC-MS quantification of ABA, GA₄, JA, and ACC/ethylene in treated vs. untreated seeds at 6, 12, 24, 48 h post-imbibition should show significantly elevated GA/ABA ratio and reduced JA in treated seeds.

---

## Model 2: The Epigenetic Derepression Model — "Unlock the Chromatin, Release the Growth Program"

**Core hypothesis**: Bacterial exRNAs primarily target epigenetic maintenance machinery, causing a premature and accelerated opening of chromatin at pro-germination loci; the hormonal, metabolic, and defense changes are downstream consequences of this genome-wide transcriptional reprogramming.

**Causal chain**:

1. **Bacterial exRNAs enter seed cells and are loaded into RISC** [SPECULATIVE, as above]. A subset of exRNAs may additionally be loaded into AGO4-containing complexes that participate in RNA-directed DNA methylation (RdDM), potentially interfering with the plant's own RdDM pathway [SPECULATIVE — this would represent a novel mechanism where bacterial sRNAs compete for AGO4 loading, titrating it away from endogenous siRNAs that maintain methylation at transposons and dormancy loci].

2. **The six epigenetic targets are downregulated as the primary event:**

   - **SOV1g033340.1 (DNA cytosine-5-methyltransferase)** is silenced → genome-wide reduction in maintenance DNA methylation, particularly at CG and CHG contexts [KNOWN mechanism — in Arabidopsis, *met1* and *cmt3* mutants show global hypomethylation]. In seeds, DNA methylation at promoters of GA biosynthesis genes (*GA20ox*, *GA3ox*), cell wall remodeling genes, and storage mobilization genes maintains their repression during dormancy [INFERRED from Arabidopsis data — Narsai et al. (2017) showed methylation dynamics at germination loci]. Loss of maintenance methylation during imbibition would prematurely activate these loci.

   - **SOV4g015450.1 (SUVR5-like histone methyltransferase)** is silenced → reduced deposition of H3K9me2 repressive marks [KNOWN — SUVR5 deposits H3K9me in Arabidopsis (Caro et al., 2012)]. H3K9me2 and DNA methylation form a self-reinforcing loop via CMT3-KRYPTONITE interaction [KNOWN — Jackson et al. (2002) *Nature*]. Simultaneously disrupting both the DNA methyltransferase and the histone methyltransferase breaks this reinforcing loop, causing a more rapid and complete chromatin opening than either alone [INFERRED — synergistic derepression].

   - **SOV6g036290.1 (HIRA histone chaperone)** is silenced → disrupted replication-independent histone H3.3 deposition [KNOWN — HIRA deposits H3.3 at actively transcribed genes and regulatory regions in Arabidopsis (Nie et al., 2014)]. Paradoxically, HIRA silencing might seem detrimental, but HIRA also maintains repressive chromatin states at specific developmental loci by depositing H3.3 in a context-dependent manner [INFERRED]. In seeds, HIRA may help maintain the "poised but repressed" chromatin state at dormancy-associated loci. Its loss could destabilize these repressive domains.

   - **SOV4g030590.1 (PHD domain protein)** is silenced → loss of a "reader" that recognizes repressive histone marks and recruits silencing complexes [INFERRED — PHD domains typically bind H3K4me0 or methylated lysines to recruit NuRD or PRC complexes].

   - **SOV4g038060.1 (GIS2 zinc finger)** is silenced → in Arabidopsis, GIS/GIS2 regulate trichome development and are involved in developmental phase transitions via epigenetic mechanisms [KNOWN — Gan et al. (2007)]. In the seed context, GIS2 may function as a transcriptional repressor of growth-associated genes during dormancy [INFERRED].

   - **SOV0g001060.1 (RRP15-like rDNA regulator)** is silenced → reduced rDNA transcription control. rDNA loci are epigenetically regulated and their transcriptional state reflects global chromatin permissiveness [KNOWN]. This is a lower-priority target but consistent with the theme.

3. **Chromatin opening cascades into pathway-level changes:**

   - **Hormonal genes are derepressed**: Pro-germination genes including *GA20ox*, *GA3ox*, *EXP* (expansins), and ethylene biosynthesis genes (*ACS*, *ACO*) that were silenced by DNA methylation and H3K9me2 become transcriptionally active [INFERRED]. This explains the hormonal shift (elevated GA, ethylene) without requiring direct silencing of hormone signaling genes — though the model does not exclude additive effects from direct exRNA targeting of SOV3g000150.1 (ethylene receptor).

   - **Defense genes lose epigenetic priming**: Many defense genes are maintained in a "poised" state by specific histone marks (H3K4me3 + H3K27me3 bivalent marks). Loss of the maintenance machinery shifts these loci to a fully repressed or disorganized state, explaining the defense downshift [INFERRED].

   - **Transposon silencing is collateral damage**: The five reverse transcriptase / retrotransposon targets are normally silenced by the same DNA methylation and H3K9me2 machinery. Their transient derepression would be an expected but potentially costly side effect. However, the exRNAs simultaneously target these transposon transcripts for PTGS degradation, creating an elegant "safety net": the epigenetic machinery is dismantled to open chromatin, but the transposon transcripts that escape are caught by the exRNA-RISC pathway [SPECULATIVE but internally consistent].

4. **Net phenotypic outcome**: Accelerated and more complete transition from the dormant chromatin state to the germinative chromatin state, compressing the normal timeline of epigenetic reprogramming from days to hours. This produces faster germination and more vigorous seedlings because the entire pro-growth transcriptional program is activated earlier and more synchronously. **Specific prediction**: the effect should be most pronounced in deeply dormant seeds or aged seeds where epigenetic repression is strongest, and least pronounced in non-dormant seeds where chromatin is already permissive.

**Supporting evidence**:
- DNA methylation dynamics are critical regulators of seed dormancy and germination in Arabidopsis [KNOWN — Narsai et al. (2017); Kawakatsu et al. (2017) *Cell*]
- *met1* mutants in Arabidopsis show reduced dormancy and faster germination [KNOWN — Xiao et al. (2006)]
- The H3K9me2-DNA methylation reinforcing loop is well-characterized [KNOWN — Jackson et al. (2002); Du et al. (2012)]
- Five of six epigenetic targets are ranked "high priority" in the provided data [KNOWN from provided data]
- Cross-kingdom sRNAs have been shown to induce DNA methylation changes in target organisms [KNOWN — Shahid et al. (2018) showed *Cuscuta* sRNAs direct methylation in host plants]
- The simultaneous targeting of transposon transcripts provides a coherent "safety net" narrative [INFERRED]

**Weaknesses**:
- **Timing problem**: Epigenetic changes (especially passive demethylation through dilution during DNA replication) typically require cell divisions to manifest. During early imbibition (Phase I–II), there is minimal DNA replication. Active demethylation via ROS1/DME pathways could be faster, but these are not directly targeted. The model requires that reduced *de novo* and maintenance methylation during the first few hours of imbibition is sufficient to open key loci — this is plausible but undemonstrated [CAVEAT].
- **Specificity problem**: Global hypomethylation would affect thousands of loci, not just pro-germination ones. This could activate deleterious genes, transposons, and stress-response programs. The model must invoke the transposon "safety net" and assume that the net balance is positive, which is not guaranteed.
- **Confounder**: EPS-mediated osmopriming involves controlled hydration-dehydration cycles that themselves cause epigenetic changes (DNA methylation reprogramming during priming is well-documented) [KNOWN — Paparella et al. (2015)]. The epigenetic effects observed may be due to osmopriming rather than exRNA-mediated gene silencing.
- The model does not parsimoniously explain the 18 transport/ion homeostasis targets or the 11 protein turnover targets, which would need to be treated as secondary effects.

**Testable predictions**:
1. **Whole-genome bisulfite sequencing (WGBS)** of exRNA-treated vs. untreated seeds at 12 and 24 h post-imbibition should show targeted hypomethylation at pro-germination loci (e.g., *GA20ox*, *GA3ox* promoters) in treated seeds.
2. **ChIP-seq for H3K9me2** should show reduced signal at germination-associated loci in treated seeds.
3. **5-azacytidine (DNA methylation inhibitor) treatment** of untreated seeds should partially phenocopy the exRNA germination effect. If it does, this supports the epigenetic model; if exRNA treatment provides additional benefit beyond 5-azacytidine, other mechanisms are also operating.
4. **ATAC-seq** at 12–24 h should show earlier chromatin accessibility at pro-germination loci in exRNA-treated seeds.
5. **Transposon transcript quantification** (RT-qPCR for LTR retrotransposon families): if the "safety net" hypothesis is correct, transposon mRNAs should be transiently elevated then rapidly degraded in treated seeds, but stably elevated in seeds treated with a DNA methylation inhibitor alone.
6. Seeds from a spinach line overexpressing SOV1g033340.1 (DNA methyltransferase) should be resistant to the exRNA germination effect.

---

## Model 3: The Resource Liberation Model — "Shut Down the Costly Programs, Fund the Growth"

**Core hypothesis**: Bacterial exRNAs act as a broad-spectrum "austerity program," simultaneously downregulating multiple energy-intensive processes (defense, DNA damage checkpoints, organelle biogenesis, protein turnover, complex biosynthesis) to liberate ATP, NADPH, amino acids, and nucleotides for the singular purpose of powering radicle emergence and early seedling growth. The hormonal and epigenetic changes are facilitators, not drivers.

**Causal chain**:

1. **Bacterial exRNAs enter seed cells and silence a broad set of targets across multiple energy-consuming pathways** [SPECULATIVE]. Unlike Models 1 and 2, which invoke a small number of "master switch" targets, this model proposes that the *breadth* of targeting is the mechanism — no single target is critical, but the aggregate effect of downregulating ~100 genes across 12 pathways creates a massive energy surplus.

2. **Multiple costly programs are simultaneously throttled:**

   - **Defense & immunity shutdown (5 targets)**: EDR2 (×2), MOS1-like, R-protein, NST1 are silenced → the seed does not invest in synthesizing defense proteins, phytoalexins, or mounting PTI/ETI responses. **Estimated energy savings**: Defense protein synthesis and signaling consumes 10–30% of cellular ATP in stressed plant cells [INFERRED from growth-defense tradeoff literature — Huot et al. (2014) *Mol Plant*; Züst & Agrawal (2017) *Annu Rev Plant Biol*].

   - **DNA damage checkpoint bypass (6 targets)**: ATR kinase (SOV4g051610.1), DNA topoisomerase 2, DNA polymerases (×3), RNase H are silenced → the DNA damage response (DDR) checkpoint is disabled [INFERRED]. Seeds accumulate DNA damage during storage; upon imbibition, ATR normally surveys the genome and imposes cell cycle arrest if damage is detected [KNOWN — Waterworth et al. (2011) *Plant Cell*]. By silencing ATR and the repair machinery, the exRNAs force the seed to bypass this checkpoint and proceed directly to growth. This is analogous to how oncogenes bypass p53-mediated checkpoints in mammalian cells [KNOWN analogy]. **Critical risk**: this trades long-term genomic integrity for short-term growth speed. **Estimated time savings**: DDR-mediated cell cycle arrest can delay germination by 12–48 h in damaged seeds [INFERRED from Waterworth et al. (2016)].

   - **Organelle biogenesis deferral (6 targets)**: TIM50 (mitochondrial import), TIC214 (chloroplast import), cytochrome c biogenesis, RETICULATA, CFM3, MDM35-like are silenced → *de novo* organelle construction is paused [INFERRED]. The seed relies on existing pro-mitochondria for initial respiration rather than investing in building new organelles. Chloroplast biogenesis, which is unnecessary in the dark underground phase, is completely suppressed. **Estimated energy savings**: Organelle biogenesis (protein import, ETC assembly, thylakoid construction) is one of the most ATP-intensive processes in plant cells [KNOWN].

   - **Protein turnover reduction (11 targets)**: RING E3 ligases (×3), F-box proteins (×3), DnaJ chaperone, ULP protease, PNGase, TPR protein, Nardilysin are silenced → the ubiquitin-proteasome system (UPS) is broadly attenuated [INFERRED]. The UPS consumes ~30% of cellular ATP in actively dividing cells [KNOWN — Peth et al. (2013)]. By reducing protein turnover, the seed conserves both the ATP cost of ubiquitination/proteolysis and the amino acids that would be recycled. **Critical caveat**: this also stabilizes proteins that would normally be degraded, including both pro- and anti-germination factors. The model predicts that the net effect is positive because the stabilized pro-germination factors (e.g., GA signaling components) outweigh the stabilized anti-germination factors (e.g., DELLAs), particularly when combined with the hormonal shift from other targets.

   - **Metabolic streamlining (15 targets)**: Phytoene synthase (carotenoid/ABA precursor pathway), TPS (T6P signaling), GDSL lipases (×3), CTP synthase, aspartokinase, and others are modulated → biosynthetic flux is redirected away from secondary metabolites and dormancy-associated compounds toward core primary metabolism [INFERRED]. Notably, downregulating phytoene synthase (SOV4g000330.1) cuts off the carotenoid pathway, which is the biosynthetic source of ABA precursors [KNOWN — carotenoid cleavage by NCED produces xanthoxin, the ABA precursor]. This creates a hormone-level effect (reduced ABA) through a metabolic mechanism rather than a signaling mechanism.

   - **ROS scavenging reduction (3 targets)**: GST, peroxidase, rhodanese are silenced → reduced investment in antioxidant defense allows a controlled ROS burst that serves as a pro-germination signal [INFERRED — the "oxidative window" hypothesis: Bailly et al. (2008) *CR Biol*]. The energy saved from not synthesizing glutathione conjugates and running the ascorbate-glutathione cycle is redirected to growth [INFERRED].

   - **Transport reconfiguration (18 targets)**: Cation-chloride cotransporters, CNGCs, ABC transporters, and vesicular trafficking components are modulated → the cell's transport budget is simplified, reducing the ATP cost of maintaining multiple active transport systems [INFERRED]. Specifically, downregulating stress-responsive transporters (detoxification proteins, cadmium resistance proteins) eliminates the energetic cost of pumping xenobiotics and heavy metals out of the cell — a cost that is unnecessary in the controlled environment of a primed seed [INFERRED].

3. **The aggregate energy surplus funds rapid germination:**

   The combined ATP, NADPH, amino acid, and nucleotide savings from shutting down these programs creates a "war chest" of resources. This surplus is channeled into:
   - **Turgor-driven cell expansion**: Water uptake and vacuolar ion accumulation for radicle elongation [KNOWN — this is the primary physical mechanism of germination].
   - **Rapid protein synthesis**: Translation of stored mRNAs encoding cell wall loosening enzymes, aquaporins, and metabolic enzymes [KNOWN].
   - **Cell wall modification**: The cell wall remodeling pathway is not shut down but rather *liberated* — with reduced glycosyltransferase activity (less wall reinforcement) and maintained beta-galactosidase activity (continued wall loosening), the net effect favors wall extensibility [INFERRED].

4. **Net phenotypic outcome**: Faster germination and enhanced seedling vigor due to more efficient resource utilization during the critical imbibition-to-radicle-emergence window. The effect is predicted to be most pronounced under resource-limited conditions (e.g., low-nutrient soils, suboptimal temperatures where metabolic rates are low) because the relative benefit of resource conservation is greatest when total resources are scarce. **Specific prediction**: the germination improvement should scale with the degree of resource limitation — maximal benefit under stress, minimal benefit under optimal conditions where resources are not limiting.

**Supporting evidence**:
- The growth-defense tradeoff is one of the most robust principles in plant biology [KNOWN — Herms & Mattson (1992); Huot et al. (2014)]
- ATR-mediated checkpoint bypass accelerates cell cycle progression in multiple systems [KNOWN — Waterworth et al. (2016) demonstrated that *atr* mutants germinate faster but accumulate more mutations]
- The UPS consumes a major fraction of cellular ATP [KNOWN — Peth et al. (2013)]
- Seed priming (hydropriming, osmopriming) improves germination partly by allowing DNA repair to occur *before* the germination attempt, reducing the DDR delay [KNOWN — Paparella et al. (2015)]
- The breadth of targeting (103 genes across 12 pathways) is more consistent with a broad resource-liberation strategy than with a narrow master-switch model [INFERRED]
- Carotenoid pathway disruption (phytoene synthase silencing) reducing ABA levels is well-established [KNOWN — *psy* mutants in tomato and Arabidopsis show reduced ABA]

**Weaknesses**:
- **Lacks mechanistic elegance**: Invoking ~100 targets as co-equal contributors is descriptively accurate but mechanistically unsatisfying. It is difficult to test the "aggregate energy surplus" hypothesis directly because no single gene knockdown would recapitulate the phenotype.
- **Checkpoint bypass is risky**: Disabling the DDR checkpoint (ATR silencing) would increase mutation rates in the germinating seedling. If the bacterial treatment is applied across many generations, this could have fitness costs that are not apparent in single-generation germination assays [CAVEAT].
- **Protein turnover paradox**: Broadly attenuating the UPS should stabilize DELLA proteins and ABI5, which are *anti*-germination factors normally degraded by the UPS to permit germination [KNOWN — Piskurewicz et al. (2008) *Plant Cell*; McGinnis et al. (2003)]. The model must assume that either (a) the specific E3 ligases targeted are not the ones that degrade DELLAs/ABI5 (the SLY1 and KEG E3 ligases are not in the target list) [INFERRED — this is consistent with the data], or (b) the hormonal shift from other targets is sufficient to overcome DELLA/ABI5 stabilization.
- **Major confounder**: The "resource liberation" effect is indistinguishable from osmopriming, which achieves a similar outcome (pre-completion of energy-consuming preparatory steps during a controlled hydration period) without requiring gene silencing. EPS-mediated osmopriming could explain the entire phenotype.
- Does not explain why the bacterial species would evolve exRNAs that target these specific genes if the effect is merely aggregate resource savings.

**Testable predictions**:
1. **ATP/ADP ratio measurement** (luciferase-based or HPLC) in exRNA-treated vs. untreated seeds at 6, 12, 24 h should show significantly higher ATP pools in treated seeds if resource liberation is the primary mechanism.
2. **Metabolic flux analysis** (¹³C-glucose labeling) should show redirected carbon flux from secondary metabolism toward primary metabolism (glycolysis, TCA cycle) in treated seeds.
3. **Individual pathway inhibition**: If the model is correct, no single pathway inhibition (e.g., defense suppression alone via SA/JA inhibitors, or DDR bypass alone via ATR inhibitor caffeine) should fully recapitulate the exRNA effect, but combinations of 3+ pathway interventions should approach it.
4. **Dose-response under stress**: Germination improvement from exRNA treatment should be proportionally greater under osmotic stress (PEG treatment), cold stress, or nutrient limitation than under optimal conditions.
5. **Comet assay** on seedling root tips: exRNA-treated seedlings should show elevated DNA damage (more tail DNA) compared to controls if DDR checkpoint bypass is occurring, particularly in aged seeds.
6. **Proteomic analysis** at 24 h: if UPS is attenuated, total protein turnover rate (measured by ³⁵S-Met pulse-chase or TMT-based proteomics) should be reduced in treated seeds, and specific pro-germination factors should show increased steady-state levels.

---

## Model Comparison Table

| Feature | Model 1: Hormonal Fulcrum | Model 2: Epigenetic Derepression | Model 3: Resource Liberation |
|---|---|---|---|
| **Primary targets** | 3 (ethylene receptor, LOX, AHP) | 6 (DNA-MeTase, SUVR5, HIRA, PHD, GIS2, RRP15) | ~100 (broad, distributed) |
| **Targets directly explained** | 3 primary + ~20 secondary (hormone-responsive) | 6 primary + ~15 secondary (epigenetically regulated) + 5 transposons | ~90 (nearly all) |
| **Targets poorly explained** | Transport (18), protein turnover (11), DNA repair (6) — must invoke indirect effects | Transport (18), protein turnover (11), metabolic (15) — treated as downstream | Epigenetic targets (6) — their silencing is redundant if broad shutdown is the goal |
| **Mechanism complexity** | Low (3 nodes → 1 hormonal ratio) | Medium (6 nodes → chromatin state → transcriptome) | High (12 pathways × multiple genes each) |
| **Temporal logic** | Fast (signaling within minutes–hours) | Slow (epigenetic changes require hours–days) | Intermediate (metabolic reallocation within hours) |
| **Elegance / parsimony** | High | Medium | Low |
| **Confounder vulnerability** | High (bacterial ethylene, EPS osmopriming mimic hormonal effects) | High (osmopriming causes epigenetic changes) | Very high (osmopriming achieves resource liberation without gene silencing) |
| **Risk to organism** | Low (hormonal shift is reversible) | Medium (genome-wide hypomethylation; transposon risk) | Medium-high (DDR bypass → mutations; defense loss → pathogen vulnerability) |
| **Testable predictions** | ABA rescue, ethylene mutant resistance, hormone profiling | WGBS, ChIP-seq, 5-azacytidine phenocopy, ATAC-seq | ATP measurement, metabolic flux, comet assay, combinatorial inhibition |
| **Evolutionary logic** | Strong (bacteria benefit from faster plant growth → more root exudates) | Moderate (requires precise targeting of plant epigenetic machinery) | Weak (broad targeting lacks specificity expected of evolved exRNAs) |
| **Overall plausibility** | ★★★★☆ | ★★★☆☆ | ★★★☆☆ |

---

## Recommended Model

**Model 1 (Hormonal Fulcrum) is recommended as the primary explanatory framework, with elements of Model 2 (Epigenetic Derepression) incorporated as a synergistic secondary mechanism.**

### Rationale:

1. **Parsimony**: Model 1 explains the largest phenotypic effect with the fewest primary targets. The ABA/GA ratio is the single most important determinant of germination in angiosperms [KNOWN], and the three hormonal targets directly and plausibly shift this ratio. Occam's razor favors this model.

2. **Temporal coherence**: Hormonal signaling operates on a minutes-to-hours timescale, which matches the germination acceleration phenotype. Epigenetic changes (Model 2) are slower, and aggregate resource liberation (Model 3) requires the simultaneous silencing of ~100 targets, which is kinetically less likely to be coordinated.

3. **Evolutionary logic**: If bacteria benefit from faster plant germination (e.g., through earlier root exudate production that feeds rhizosphere communities), natural selection would favor the evolution of exRNAs targeting the minimum number of high-leverage nodes. Three hormonal master switches represent a far more evolvable and maintainable strategy than 100 distributed targets [INFERRED].

4. **Epigenetic synergy**: However, the six epigenetic targets are too high-confidence and too mechanistically coherent to dismiss as secondary. The recommended integrated model proposes that:
   - **Phase 1 (0–12 h)**: Hormonal targets (ethylene receptor, LOX, AHP) are silenced first, rapidly shifting the ABA/GA balance and committing the seed to germination [INFERRED].
   - **Phase 2 (12–48 h)**: Epigenetic targets (DNA methyltransferase, SUVR5, HIRA) are silenced, accelerating the chromatin opening that the hormonal shift has initiated, producing a more robust and sustained growth program [INFERRED].
   - **Amplification loop**: The hormonal shift promotes epigenetic reprogramming (GA signaling opens chromatin at growth loci), and the epigenetic opening enhances hormonal signaling (derepressed GA biosynthesis genes produce more GA). This creates a positive feedback loop that explains the vigor phenotype beyond simple germination speed [SPECULATIVE].

5. **Confounder management**: While all models are vulnerable to the EPS/osmopriming confounder, the hormonal + epigenetic model generates the most specific and falsifiable predictions. If AGO-IP recovers exRNA–ethylene receptor duplexes, and if WGBS shows locus-specific (not global) hypomethylation at GA biosynthesis promoters, the exRNA-specific mechanism can be distinguished from osmopriming effects, which would produce global rather than targeted changes.

### Critical next experiments (prioritized):

1. **RNase-treated exRNA controls**: Compare germination with intact bacterial exRNA extract vs. RNase A/III-treated extract vs. heat-inactivated extract. If RNase treatment abolishes the germination effect, exRNA (not EPS or metabolites) is the active agent. **This is the single most important control experiment.**
2. **AGO-IP + small RNA sequencing** from treated seeds to confirm exRNA loading into plant RISC and identify actual target duplexes.
3. **Hormone profiling time course** (ABA, GA₁, GA₄, JA, JA-Ile, ACC, ethylene) at 6, 12, 24, 48 h.
4. **WGBS at 24 h** to test for targeted vs. global methylation changes.
5. **Synthetic exRNA mimics**: Design synthetic 21-nt sRNAs matching the predicted exRNA sequences targeting SOV3g000150.1 (ethylene receptor) and SOV1g033340.1 (DNA methyltransferase). Apply individually and in combination. If the combination recapitulates >70% of the full bacterial exRNA effect, the integrated hormonal + epigenetic model is strongly supported.