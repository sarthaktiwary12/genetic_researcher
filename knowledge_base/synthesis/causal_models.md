# Causal Models



# Alternative Causal Models: Bacterial exRNA-Mediated Germination Enhancement in *Spinacia oleracea*

---

## Model 1: The Epigenetic Master Switch Model

**Core hypothesis**: Bacterial exRNAs primarily target the epigenetic silencing machinery that maintains seed dormancy, causing a cascading de-repression of germination-promoting loci; all other observed effects (hormonal shifts, defense suppression, metabolic activation) are downstream consequences of this chromatin remodeling.

**Causal chain**:

1. Bacterial exRNAs (likely 21–24 nt sRNAs) are delivered to seed cells during imbibition, potentially packaged in outer membrane vesicles (OMVs) or stabilized by EPS matrix association; they are loaded into the plant AGO1/AGO4-containing RISC complex in the cytoplasm and/or nucleus. [SPECULATIVE — cross-kingdom RISC loading demonstrated in limited systems, e.g., *Botrytis*–*Arabidopsis* (Weiberg et al. 2013, *Science*), but not validated for beneficial bacteria–seed interactions]

2. **Primary targets — the epigenetic gatekeepers — are downregulated:**
   - **SOV1g033340.1 (DNA cytosine-5-methyltransferase)** is silenced → maintenance methylation at CG and CHG contexts fails during the first rounds of DNA replication upon imbibition → passive demethylation of promoters of GA-responsive genes (e.g., *EXPANSIN*, *α-amylase* homologs), ABA catabolism genes (*CYP707A* family), and cell-cycle re-entry genes. [KNOWN that MET1/CMT3 loss causes global hypomethylation in *Arabidopsis*; INFERRED for these specific germination loci in spinach]
   - **SOV4g015450.1 (SUVR5-like H3K9 methyltransferase)** is silenced → loss of repressive H3K9me2 marks at heterochromatic and euchromatic loci → chromatin decompaction at dormancy-associated gene clusters. [KNOWN that SUVR5 contributes to H3K9me2 in *Arabidopsis* (Caro et al. 2012, *PLoS Genetics*); INFERRED for spinach dormancy loci]
   - **SOV6g036290.1 (HIRA histone chaperone)** is silenced → reduced deposition of histone variant H3.3 at specific loci; in the dormancy context, HIRA may maintain repressive nucleosome occupancy at germination-promoting genes, and its loss destabilizes these nucleosomes. [KNOWN that HIRA deposits H3.3 in *Arabidopsis*; SPECULATIVE that this specifically represses germination loci]
   - **SOV4g030590.1 (PHD-domain protein)** and **SOV4g038060.1 (GIS2 zinc finger)** are silenced → loss of "reader" proteins that recruit Polycomb Repressive Complex 2 (PRC2) and other repressive complexes to H3K4me0/H3K27me3-marked chromatin → further chromatin opening. [INFERRED from PHD-PRC2 interactions in *Arabidopsis*; SPECULATIVE for GIS2 in this context]

3. **Cascading transcriptional de-repression:**
   - Chromatin opening at hormone biosynthesis/signaling loci leads to increased GA biosynthesis (*GA3ox*, *GA20ox*), increased ABA catabolism (*CYP707A*), and increased ethylene biosynthesis (*ACS*, *ACO*) — effectively recapitulating the hormonal shift from ABA-dominant to GA/ethylene-dominant without directly targeting hormone pathway genes. [INFERRED — this is the known transcriptional program activated during *Arabidopsis* germination upon epigenetic de-repression]
   - Chromatin opening at defense regulon promoters paradoxically makes them accessible, but the simultaneous direct targeting of **EDR2** (SOV3g043450.1, SOV6g048760.1) and **MOS1** (SOV5g005530.1) by exRNAs ensures that immune signaling remains dampened even as chromatin opens — this represents a "selective unlocking" where growth genes are activated but defense genes are kept suppressed by a secondary layer of post-transcriptional silencing. [SPECULATIVE]
   - The hormone shift (↑GA, ↓ABA) then drives all downstream execution: cell wall loosening (via GA-induced α-amylase, expansins, XTHs), ROS window establishment, reserve mobilization, and water uptake.

4. **Net phenotypic outcome**: Accelerated and more uniform radicle emergence (improved T50 and germination synchrony) due to earlier and more complete activation of the germination transcriptional program. Seedling vigor is enhanced because the epigenetic "reset" also de-represses post-germination growth genes (photomorphogenesis, root elongation programs) ahead of schedule.

**Supporting evidence**:
- DNA methylation dynamics are causally linked to dormancy cycling in *Arabidopsis*: seeds of *met1* and *cmt3* mutants show reduced dormancy [KNOWN] (Xiao et al. 2006; Zheng et al. 2012)
- SUVR5 loss-of-function in *Arabidopsis* causes ectopic gene expression at normally silenced loci [KNOWN] (Caro et al. 2012)
- The GA/ABA ratio is the master determinant of germination timing, and both pathways are epigenetically regulated [KNOWN] (Graeber et al. 2012, *Plant Cell*)
- Cross-kingdom sRNA-mediated gene silencing has been demonstrated for fungal pathogens targeting plant immunity genes [KNOWN] (Weiberg et al. 2013)
- 5 of 6 epigenetic pathway genes are ranked "high priority" in the target analysis, the highest density of any pathway

**Weaknesses**:
- This model requires that epigenetic changes occur *fast enough* during imbibition (hours) to influence germination, yet passive demethylation requires at least one round of DNA replication; early germination in many species occurs without cell division (cell expansion only), so the timing is problematic [KNOWN constraint]
- Does not directly explain why specific transport/ion homeostasis genes (CNGC, CCC cotransporters) are targeted — these would need to be coincidental targets or explained as secondary effects
- Assumes that the bacterial exRNAs can access the nucleus and/or that cytoplasmic RISC can silence nuclear-localized transcripts of chromatin modifiers — mechanistically uncertain [SPECULATIVE]
- Cannot distinguish from EPS-mediated osmopriming, which also accelerates imbibition and could independently activate demethylation pathways via earlier replication onset

**Testable predictions**:
1. **Bisulfite sequencing**: Seeds treated with bacterial exRNAs (vs. EPS-only controls) should show reduced DNA methylation at specific germination-promoting loci (e.g., *GA3ox*, *CYP707A* promoter homologs) within 12–24 h of imbibition
2. **ChIP-qPCR**: H3K9me2 levels at target loci should decrease in exRNA-treated seeds relative to controls
3. **Pharmacological test**: Co-treatment with the DNA methyltransferase inhibitor 5-azacytidine should partially phenocopy the exRNA effect; combining exRNA + 5-azacytidine should show diminishing returns (epistasis) if they act through the same pathway
4. **Time-course RNA-seq**: If this model is correct, the transcriptomic signature of exRNA-treated seeds should resemble a "temporally advanced" version of the normal germination program (earlier activation of the same genes, not activation of novel genes)
5. **Genetic test**: Overexpression of *SOV1g033340.1* (DNA methyltransferase) in spinach hairy roots or transient assays should partially rescue the exRNA-mediated phenotype

---

## Model 2: The Hormonal Fulcrum Model

**Core hypothesis**: Bacterial exRNAs simultaneously target three critical nodes in the hormone signaling network — ethylene perception, JA biosynthesis, and cytokinin relay — creating a synergistic, multi-axis shift in the ABA/GA balance that directly and rapidly triggers germination without requiring prior epigenetic reprogramming.

**Causal chain**:

1. Bacterial exRNAs enter seed cells during imbibition via OMV fusion with the plasma membrane or endocytic uptake facilitated by EPS-mediated membrane perturbation. sRNAs are loaded into cytoplasmic AGO1-RISC, which targets mRNAs of hormone signaling components for cleavage or translational repression. [SPECULATIVE for mechanism; KNOWN that plant AGO1 can load exogenous sRNAs in some experimental systems]

2. **Three hormone signaling nodes are simultaneously disrupted:**

   **Node A — Ethylene signaling activated:**
   - **SOV3g000150.1 (Ethylene receptor)** is downregulated → loss of the receptor, which is a negative regulator of ethylene signaling → constitutive activation of the ethylene response pathway (EIN2→EIN3/EIL1 cascade). [KNOWN: ethylene receptors repress signaling; *etr1* loss-of-function = constitutive ethylene responses in *Arabidopsis*]
   - Activated ethylene signaling directly antagonizes ABA: EIN3 promotes transcription of *ABI5* degradation machinery (via SCFEBF1/2 E3 ligase) and suppresses ABA-responsive gene expression. [KNOWN] (Linkies et al. 2009)
   - Ethylene also promotes endosperm cap weakening by inducing cell wall hydrolases. [KNOWN in *Lepidium*, INFERRED for spinach]

   **Node B — JA biosynthesis suppressed:**
   - **SOV3g035520.1 (Lipoxygenase/LOX)** is downregulated → reduced flux through the octadecanoid pathway → lower JA/JA-Ile levels. [KNOWN that LOX is rate-limiting for JA biosynthesis]
   - JA normally synergizes with ABA to maintain dormancy and suppress GA responses. Reduced JA removes this reinforcement of the ABA-dominant state. [KNOWN] (Dave et al. 2011, *PNAS*: *lox* mutants show reduced dormancy in *Arabidopsis*)
   - JA suppression also reduces the defense-growth tradeoff cost: JA-mediated defense gene expression (VSP, PDF1.2, etc.) is dampened, liberating resources. [KNOWN]

   **Node C — Cytokinin signaling relay dampened:**
   - **SOV4g032870.1 (AHP-like histidine phosphotransfer protein)** is downregulated → disruption of the His-Asp phosphorelay that transmits cytokinin signals from membrane-bound receptors (AHK2/3/4) to nuclear response regulators (ARRs). [KNOWN for AHP function]
   - In the germination context, this is counterintuitive because cytokinins generally promote germination. However, AHPs also relay signals from AHK1 (an osmosensor) and participate in ABA signaling crosstalk. Specific AHP knockdowns in *Arabidopsis* can reduce ABA sensitivity. [KNOWN] (Hutchison et al. 2006, *Plant Cell*) [INFERRED that the net effect in seeds is reduced ABA sensitivity rather than reduced CK signaling per se]
   - Additionally, dampening this relay may prevent stress-induced cytokinin signaling from activating type-A ARR negative feedback loops that would otherwise limit growth responses.

3. **Convergent downstream effects:**
   - The combined effect of ↑ethylene + ↓JA + altered CK/ABA crosstalk creates a decisive shift: ABA sensitivity drops below the threshold required to maintain dormancy. [INFERRED from individual pathway effects; SPECULATIVE for synergistic magnitude]
   - GA signaling is de-repressed (DELLA proteins become more susceptible to GA-mediated degradation when ABA opposition is removed). [KNOWN]
   - Cell wall hydrolases are induced in the micropylar endosperm. [KNOWN downstream of GA/ethylene]
   - The ROS scavenging enzymes **SOV3g038840.1 (Peroxidase)** and **SOV3g040200.1 (GST)** are concurrently downregulated by exRNAs → the "oxidative window" is widened, allowing ROS to accumulate to levels that promote cell wall loosening and ABA catabolism. [INFERRED]
   - Defense pathway targets (EDR2, MOS1, R-proteins) are simultaneously silenced, preventing the JA-independent immune activation that might otherwise be triggered by the bacterial treatment itself. [INFERRED — this may be a bacterial "self-protection" mechanism]

4. **Net phenotypic outcome**: Rapid germination (reduced time to radicle emergence) driven by the direct hormonal shift, occurring within hours of imbibition — faster than epigenetic reprogramming could achieve. Seedling vigor is improved because the early hormonal environment (high ethylene, low JA, favorable GA/ABA ratio) promotes hypocotyl/radicle elongation and chloroplast development upon light exposure.

**Supporting evidence**:
- Ethylene receptor mutants (*etr1-7*, *ers1-3*) in *Arabidopsis* show enhanced germination under stress conditions [KNOWN] (Wilson et al. 2014)
- *lox2* and *lox3* mutants show reduced seed dormancy [KNOWN] (Dave et al. 2011)
- Ethylene + GA act synergistically to promote germination in multiple species [KNOWN] (Linkies & Leubner-Metzger 2012, *J. Exp. Bot.*)
- All three hormone signaling targets are ranked Tier 1 / high priority
- The speed of hormone signaling (minutes to hours for receptor-level effects) matches the rapid phenotypic response expected during imbibition
- Exogenous ethylene application promotes spinach germination, particularly under high-temperature stress (thermoinhibition) [KNOWN] (Nascimento et al. 2004)

**Weaknesses**:
- This model treats epigenetic targets as secondary or parallel effects, but 6 high-priority epigenetic targets represent a large investment by the bacterial exRNA repertoire — difficult to explain as "bystander" targeting
- The AHP downregulation effect is ambiguous: it could reduce either CK signaling (anti-germination) or ABA crosstalk (pro-germination), and the net effect depends on which receptor complex the specific AHP preferentially serves in spinach seeds — this is unknown [SPECULATIVE]
- Does not explain the targeting of DNA repair/replication checkpoint genes (ATR, polymerases) or transport/ion homeostasis genes, which would need to be treated as independent, additive effects
- The LOX target could be involved in lipid mobilization (oxylipin-independent roles) rather than JA biosynthesis — downregulation might impair reserve mobilization, creating a potential conflict [KNOWN confounder]
- Cannot rule out that EPS osmopriming alone shifts hormone balance; would need exRNA-depleted EPS controls

**Testable predictions**:
1. **Hormone quantification**: LC-MS/MS measurement of ABA, GA₄, JA-Ile, and ACC/ethylene in exRNA-treated vs. control seeds at 6, 12, 24 h post-imbibition should show reduced ABA and JA-Ile, with increased ethylene evolution (measured by GC)
2. **Epistasis with ethylene inhibitors**: Co-treatment of exRNA-treated seeds with 1-MCP (ethylene perception inhibitor) or AVG (ethylene biosynthesis inhibitor) should partially block the germination enhancement — if ethylene activation is a primary driver
3. **Reporter assays**: If available, *ABI5::GUS* or *RGA::GFP* (DELLA) reporter lines in spinach or heterologous *Arabidopsis* system should show reduced ABI5 accumulation and enhanced DELLA degradation in exRNA-treated seeds
4. **Exogenous hormone rescue**: Application of exogenous JA (methyl jasmonate) or ABA to exRNA-treated seeds should dose-dependently antagonize the germination benefit, with JA specifically counteracting the LOX-silencing arm
5. **Target-specific validation**: Transient expression of a non-targetable (synonymous mutation) version of the ethylene receptor in spinach protoplasts should be resistant to exRNA-mediated silencing, confirmed by qRT-PCR

---

## Model 3: The Integrated Osmo-Mechanical Model

**Core hypothesis**: Bacterial exRNAs primarily target the physical and osmotic barriers to radicle emergence — ion/water transport, cell wall architecture, and turgor generation — while defense and checkpoint suppression prevents the seed from aborting this mechanically-driven germination program; epigenetic and hormonal effects are modulatory rather than causal.

**Causal chain**:

1. Bacterial exRNAs are delivered to seed cells during the initial rapid phase of imbibition (Phase I water uptake), potentially facilitated by the hygroscopic EPS matrix that maintains prolonged contact between bacterial vesicles/free sRNAs and the seed surface. Entry occurs through the micropyle and/or damaged testa regions where membrane permeability is highest. sRNAs are loaded into RISC in the cytoplasm. [SPECULATIVE for delivery route; KNOWN that micropyle is the primary water entry point]

2. **Primary targets — the osmotic and mechanical gatekeepers — are downregulated:**

   **Arm A — Turgor pressure generation is enhanced:**
   - **SOV1g021960.1 and SOV2g025380.1 (Cation-chloride cotransporters, CCC1-like)** are downregulated → reduced Cl⁻ and K⁺/Na⁺ efflux from embryonic cells → increased intracellular solute concentration → increased osmotic potential → enhanced water uptake and turgor pressure. [KNOWN that CCC transporters mediate Cl⁻/cation efflux; INFERRED that their loss increases turgor in seeds]
   - **SOV1g018480.1 (Cyclic nucleotide-gated channel, CNGC)** is downregulated → reduced Ca²⁺ influx through this specific channel → two effects: (a) prevents Ca²⁺-triggered signaling cascades that activate stress/defense responses and ABA signaling [KNOWN that CNGCs mediate Ca²⁺ signaling in defense]; (b) may alter the Ca²⁺/K⁺ balance in favor of K⁺ accumulation, further driving osmotic water uptake [INFERRED]
   - **SOV5g008400.1 (Cation/H⁺ antiporter)** downregulation modifies vacuolar ion sequestration dynamics, potentially increasing cytoplasmic osmolarity. [SPECULATIVE]

   **Arm B — Cell wall mechanical resistance is reduced:**
   - **SOV4g010600.1 and SOV1g033840.1 (Glycosyltransferases)** are downregulated → reduced synthesis and cross-linking of cell wall polysaccharides (hemicelluloses, pectins) in the endosperm cap → the wall is not maintained or reinforced during imbibition. [INFERRED from GT function]
   - **SOV3g038840.1 (Peroxidase)** is downregulated → reduced oxidative cross-linking of cell wall phenolics and extensin proteins → the wall remains extensible rather than rigidifying. [KNOWN that class III peroxidases mediate wall stiffening via lignin/suberin cross-linking]
   - **SOV4g051070.1 (Beta-galactosidase)** downregulation is seemingly contradictory (BGALs can loosen walls), but specific BGALs in the endosperm may be involved in galactomannan remodeling that *maintains* wall integrity; alternatively, this may be a "bystander" target. [SPECULATIVE]
   - The net effect: endosperm mechanical resistance decreases while embryo turgor increases → the force balance tips decisively toward radicle protrusion.

   **Arm C — Checkpoint and defense suppression prevents abort signals:**
   - **SOV4g051610.1 (ATR kinase)** downregulation → the DNA damage checkpoint is relaxed → cells proceed through S-phase and into mitosis despite residual DNA damage accumulated during seed storage → faster cell division in the radicle meristem. [KNOWN that ATR activates cell cycle arrest; INFERRED that relaxation accelerates germination]
   - **SOV2g009230.1 (Trehalose-phosphate synthase, TPS)** downregulation → reduced T6P levels → the SnRK1 energy-sensing kinase is de-repressed → SnRK1 activates catabolic pathways (autophagy, lipid β-oxidation, starch degradation) and suppresses anabolic pathways → rapid mobilization of seed reserves to fuel the mechanical process of emergence. [KNOWN for T6P-SnRK1 nexus in *Arabidopsis*] (Zhang et al. 2009, *Plant Cell*)
   - Defense genes (EDR2, MOS1, R-proteins, RLKs) are silenced → the seed does not interpret the bacterial treatment as a pathogen attack → no SA/JA-mediated growth arrest. [INFERRED — this may be essential for the bacterial strategy to function at all]

3. **The physical process of germination is accelerated:**
   - Enhanced turgor (Arm A) pushes against a weakened endosperm cap (Arm B) → radicle protrusion occurs earlier.
   - Relaxed cell cycle checkpoints (Arm C) allow faster cell division in the radicle tip, contributing to sustained elongation post-emergence.
   - Hormonal and epigenetic effects (ethylene receptor, DNA methyltransferase, SUVR5, etc.) serve as *modulatory amplifiers*: they reinforce the osmomechanical program by ensuring the correct transcriptional environment, but they are not the rate-limiting step. The physical force balance is.

4. **Net phenotypic outcome**: Earlier radicle protrusion (reduced T50) driven primarily by biophysical changes in turgor and wall mechanics. Seedling vigor (post-emergence growth rate) is enhanced by the combination of faster cell division (relaxed checkpoints), efficient reserve mobilization (↓T6P → ↑SnRK1), and reduced defense costs. The effect should be most pronounced under osmotic stress conditions (salt, drought, thermodormancy) where turgor generation is the primary limiting factor.

**Supporting evidence**:
- Endosperm weakening is the rate-limiting mechanical step for germination in many species, including Amaranthaceae relatives of spinach [KNOWN] (Nonogaki et al. 2010)
- CCC transporter mutants in *Arabidopsis* show altered ion homeostasis and growth phenotypes [KNOWN] (Colmenero-Flores et al. 2007, *Plant Cell*)
- CNGC mutants affect Ca²⁺ signaling and pathogen responses [KNOWN] (multiple studies)
- ATR mutants show accelerated cell cycle progression but increased genomic instability [KNOWN] (Culligan et al. 2004, *Plant Cell*)
- T6P is a central metabolic signal; *tps1* mutants are embryo-lethal, but partial reduction alters growth-metabolism coupling [KNOWN]
- Peroxidase-mediated wall stiffening is a well-characterized barrier to cell expansion [KNOWN]
- 18 transport/ion homeostasis genes represent the largest single pathway category in the target set, suggesting this axis is heavily targeted

**Weaknesses**:
- Treats epigenetic targets (6 genes, mostly high priority) as modulatory rather than causal — this is difficult to justify given the strength of evidence linking epigenetics to dormancy
- The CCC cotransporter function in seeds is essentially uncharacterized; the turgor hypothesis is extrapolated from root/shoot physiology [SPECULATIVE]
- Relaxing the ATR checkpoint could increase mutation load in the seedling, representing a fitness cost not captured in short-term germination assays [KNOWN risk]
- The model predicts the strongest effects under osmotic stress, but if the experimental phenotype is observed under optimal conditions, this weakens the osmomechanical primacy argument
- Beta-galactosidase downregulation is difficult to reconcile — most models of germination require BGAL activity for wall loosening, not its suppression
- Does not explain why the bacterial exRNA repertoire would invest heavily in targeting hormone and epigenetic genes if the physical mechanism is sufficient

**Testable predictions**:
1. **Biomechanical measurement**: Puncture force assays on endosperm caps of exRNA-treated vs. control seeds at 12, 24, 36 h post-imbibition should show reduced mechanical resistance in treated seeds
2. **Turgor measurement**: Pressure probe or incipient plasmolysis assays on embryonic radicle cells should show higher turgor in exRNA-treated seeds
3. **Osmotic challenge**: The germination benefit of exRNA treatment should be *proportionally greater* under osmotic stress (NaCl, PEG) than under optimal conditions — if the osmomechanical model is primary
4. **Ion flux measurement**: Non-invasive MIFE (microelectrode ion flux estimation) at the radicle tip should show altered K⁺, Cl⁻, and Ca²⁺ fluxes in exRNA-treated seeds
5. **Cell cycle analysis**: Flow cytometry of radicle tip nuclei should show earlier S-phase entry and higher mitotic index in exRNA-treated seeds
6. **SnRK1 activity**: In vitro kinase assays or phosphorylation of SnRK1 targets (e.g., bZIP63 homolog) should show increased SnRK1 activity in exRNA-treated seeds, consistent with T6P reduction

---

## Model Comparison Table

| Feature | Model 1: Epigenetic Master Switch | Model 2: Hormonal Fulcrum | Model 3: Integrated Osmo-Mechanical |
|---------|----------------------------------|--------------------------|--------------------------------------|
| **Primary driver** | Chromatin de-repression | Hormone balance shift | Turgor + wall mechanics |
| **Tier 1 targets explained** | 5/6 epigenetic + indirectly all hormonal | 3/3 hormonal + 2/3 ROS | 5/18 transport + 3/3 cell wall + ATR + TPS |
| **Total targets directly explained** | ~20 (epigenetic + downstream cascading) | ~15 (hormonal + ROS + defense) | ~30 (transport + cell wall + checkpoint + metabolic) |
| **Temporal dynamics** | Slow onset (requires DNA replication for passive demethylation; 12–24+ h) | Rapid onset (receptor-level effects within minutes–hours) | Rapid onset (ion flux changes within minutes; wall effects within hours) |
| **Mechanism complexity** | Low (single upstream node → cascade) | Medium (3 parallel nodes converging) | High (3 arms + modulatory layers) |
| **Strongest evidence type** | Genetic (methylation mutant phenotypes) | Pharmacological (hormone applications) | Biophysical (force/turgor measurements) |
| **Key testable prediction** | Bisulfite-seq shows hypomethylation at germination loci | 1-MCP blocks germination benefit | Effect amplified under osmotic stress |
| **Greatest vulnerability** | Timing: too slow for early germination effects | AHP ambiguity; LOX dual function | Epigenetic targets unexplained as primary |
| **EPS confounder susceptibility** | Medium (EPS osmopriming could accelerate replication → demethylation) | Low (EPS unlikely to directly shift ethylene/JA) | High (EPS osmopriming directly affects water uptake/turgor) |
| **Overall plausibility** | ★★★★☆ | ★★★★★ | ★★★☆☆ |

---

## Recommended Model

### **Model 2 (Hormonal Fulcrum) is the best-supported primary model, but the true mechanism is almost certainly a hybrid of Models 1 and 2.**

**Rationale for Model 2 as the lead framework:**

1. **Temporal coherence**: Germination improvement likely manifests within the first 24–48 h of imbibition. Hormone receptor-level effects (ethylene receptor silencing → constitutive ethylene signaling) operate on the timescale of mRNA turnover (hours), which is compatible with the phenotypic window. Model 1's requirement for DNA replication-dependent passive demethylation introduces a temporal lag that may be too slow to explain the earliest germination benefits. [INFERRED]

2. **Mechanistic parsimony with maximum impact**: The three hormone targets (ethylene receptor, LOX, AHP) sit at the apex of the germination decision hierarchy. The ABA/GA/ethylene balance is the single most important determinant of whether a seed germinates [KNOWN], and Model 2 attacks this balance from three independent angles simultaneously, creating redundancy and synergy.

3. **Consistency with spinach biology**: Spinach seeds are notoriously susceptible to thermoinhibition (high-temperature germination failure), which is mediated by elevated ABA and reduced ethylene sensitivity [KNOWN] (Nascimento et al. 2004). A bacterial strategy that constitutively activates ethylene signaling and suppresses JA/ABA would directly counteract the most common germination limitation in this crop.

4. **Lowest EPS confounder susceptibility**: Unlike Models 1 and 3, the specific hormone signaling shifts predicted by Model 2 are difficult to explain by EPS osmopriming alone, providing a clearer attribution to the exRNA component.

**However, a hybrid Model 1+2 is most realistic because:**

- The heavy investment in epigenetic targets (6 genes, 5 high-priority) is difficult to dismiss as coincidental. [INFERRED]
- Epigenetic de-repression and hormonal shifting are known to be mutually reinforcing: GA signaling promotes active DNA demethylation via DME/ROS1 family demethylases [KNOWN], while chromatin opening at hormone biosynthesis loci amplifies the hormonal signal. [KNOWN]
- The most parsimonious synthesis is a **two-phase model**: (Phase 1) Rapid hormone rebalancing via Model 2 targets initiates the germination program within hours; (Phase 2) Epigenetic de-repression via Model 1 targets consolidates and amplifies this program over 12–48 h, ensuring robust seedling vigor post-emergence. The exRNA repertoire targets both phases simultaneously because seeds that receive both signals germinate more reliably than those receiving either alone. [SPECULATIVE but mechanistically coherent]

**Critical experimental priority**: The single most informative experiment to discriminate between models would be a **time-resolved, multi-omic comparison** of exRNA-treated vs. EPS-only vs. water-only seeds at 3, 6, 12, 24, and 48 h post-imbibition, measuring: (a) hormone levels (LC-MS/MS), (b) global DNA methylation (WGBS or RRBS), (c) transcriptome (RNA-seq), and (d) endosperm cap puncture force. If hormone changes precede methylation changes, which precede transcriptomic reprogramming, which precedes mechanical weakening, this would strongly support the hybrid Model 1+2 with Model 2 as the initiating event.