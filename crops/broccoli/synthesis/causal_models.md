# Causal Models — Broccoli (Brassica oleracea var. italica)



# Alternative Causal Models: Bacterial exRNA-Mediated Germination Improvement in *Brassica oleracea* var. *italica* (Broccoli)

> **Cross-Species Caveat**: All target gene IDs derive from *Spinacia oleracea*. Application to *Brassica oleracea* var. *italica* requires conserved target-site complementarity at the sRNA binding loci, which is [SPECULATIVE] given ~100 My divergence between Caryophyllales and Brassicaceae. Ortholog-level functional conservation is more plausible for deeply conserved pathways (epigenetic regulation, hormone signaling, cell wall remodeling) than for rapidly evolving gene families (NLR immune receptors, transposable elements). All models below assume sufficient conservation for the core mechanistic logic to apply.

---

## Model 1: The Epigenetic Derepression Cascade ("Unlock the Blueprint")

**Core hypothesis**: Bacterial exRNAs primarily dismantle the multi-layered epigenetic repressor architecture that locks dormancy-associated chromatin states, and the resulting transcriptional derepression of pro-germination gene programs is the dominant driver of improved germination speed and seedling vigor.

**Causal chain**:

1. **Entry & Loading**: Bacterial exRNAs (likely 20–25 nt small RNAs) are delivered to the seed surface within the bacterial EPS matrix during priming treatment. Upon imbibition, exRNAs enter seed cells — most likely the metabolically active aleurone/endosperm cap and outer embryonic cell layers — via endocytosis of EPS-associated vesicles or through transient membrane permeabilization during rehydration [SPECULATIVE]. Once intracellular, exRNAs are loaded into host AGO proteins (most likely AGO1 or AGO4 orthologs), forming functional RISC complexes [INFERRED from cross-kingdom RNAi precedent in *Botrytis cinerea*–*Arabidopsis* and *C. elegans*–bacteria systems; Weiberg et al., 2013, Science; Cai et al., 2018, Science].

2. **Epigenetic repressor suppression** → Immediate chromatin decompaction:
   - **DNA (cytosine-5)-methyltransferase (SOV1g033340.1)** is downregulated → maintenance methylation at CG and CHG contexts fails during the first rounds of DNA replication post-imbibition → passive demethylation of promoters of GA-responsive genes (e.g., *EXPANSIN*, *α-amylase*, *endo-β-mannanase* orthologs) [INFERRED from Arabidopsis *met1*/*cmt3* mutant phenotypes showing reduced dormancy; Zheng et al., 2012, PNAS].
   - **SUVR5-like histone methyltransferase (SOV4g015450.1)** is downregulated → reduced deposition of H3K9me2 at heterochromatic loci → decompaction of pericentromeric and intergenic regions harboring dormancy-regulated genes [INFERRED from Arabidopsis *suvh4/kyp* mutants].
   - **HIRA histone chaperone (SOV6g036290.1)** is downregulated → altered H3.3 variant deposition dynamics → destabilization of nucleosome occupancy at transcriptional start sites of dormancy-maintaining genes, increasing accessibility to GA-responsive transcription factors [INFERRED from Arabidopsis HIRA functional studies; Nie et al., 2014].
   - **PHD-domain protein (SOV4g030590.1)** is downregulated → loss of a "reader" that recruits PRC2 or other repressive complexes to H3K4me0 marks → failure to reinforce Polycomb-mediated silencing of growth genes [INFERRED].
   - **GIS2 zinc-finger protein (SOV4g038060.1)** is downregulated → loss of a transcriptional repressor that integrates stress signals to suppress growth; in Arabidopsis, GIS family members regulate trichome/epidermal differentiation and interact with GA/cytokinin pathways [KNOWN for Arabidopsis GIS; Sun et al., 2015].

3. **Chromatin decompaction enables downstream transcriptional activation**:
   - With repressive DNA methylation, H3K9me2, and PRC2-mediated H3K27me3 all simultaneously reduced, the chromatin landscape shifts globally toward a euchromatic, transcriptionally permissive state [INFERRED].
   - GA-responsive promoters become accessible → endogenous GA (even at basal levels) can now drive expression of cell wall loosening enzymes, storage mobilization enzymes, and cell cycle re-entry genes [INFERRED].
   - This creates a feed-forward loop: derepressed GA biosynthesis genes produce more GA → further activation of GA-responsive targets [SPECULATIVE but consistent with GA-epigenetic crosstalk models].

4. **Downstream amplification through secondary pathway effects**:
   - The epigenetic "unlock" potentiates the effects of all other targeted pathways. Specifically:
     - Hormone signaling targets (AHP, LOX, ethylene receptor) are more effectively suppressed because their regulatory regions are now in an open chromatin context accessible to exRNA-guided RISC [SPECULATIVE].
     - Cell wall remodeling genes that *promote* germination (non-targeted expansins, mannanases) are transcriptionally derepressed [INFERRED].
     - Defense gene loci that were epigenetically maintained in a "poised" state lose their repressive marks, but because the defense pathway activators (EDR2, MOS1, RLKs) are simultaneously targeted by exRNAs, the net effect is defense suppression rather than activation [INFERRED].

5. **Net phenotypic outcome**: Faster, more synchronous radicle protrusion (reduced T50) due to earlier activation of the germination transcriptional program; improved seedling vigor due to earlier mobilization of storage reserves and earlier onset of cell division in the embryonic axis. Predicted effect: 20–40% reduction in mean germination time, with improved uniformity (reduced T90–T10 spread).

**Supporting evidence**:
- Arabidopsis seeds with reduced DNA methylation (*met1*, *ddm1* mutants) show decreased primary dormancy [KNOWN; Zheng et al., 2012, PNAS; Footitt et al., 2015]
- SUVH4/KYP loss-of-function reduces seed dormancy in Arabidopsis [KNOWN; Zheng et al., 2012]
- Histone deacetylase inhibitors (trichostatin A) can break dormancy in multiple species [KNOWN; reviewed in Nonogaki, 2014, Plant Science]
- Cross-kingdom RNAi via small RNAs loaded into host AGO proteins is established for fungal–plant and nematode–bacteria interactions [KNOWN; Weiberg et al., 2013; Cai et al., 2018]
- Six epigenetic targets are co-downregulated, providing pathway-level redundancy [KNOWN from target list]
- GIS2 is a known GA-pathway interactor in Arabidopsis [KNOWN]

**Weaknesses**:
- This model positions epigenetic derepression as the *primary* driver, but it cannot easily explain rapid germination effects (within 12–24 h) because passive demethylation requires at least one round of DNA replication, which occurs only after cell cycle re-entry — a chicken-and-egg problem [KNOWN limitation].
- The model does not account for the large number of non-epigenetic targets (transport, metabolic, defense) except as secondary beneficiaries. If epigenetic derepression were truly dominant, one would expect fewer non-epigenetic targets to be necessary.
- Cannot distinguish exRNA-specific effects from EPS-mediated osmopriming, which alone can improve Brassica germination by 15–40% [KNOWN].
- Assumes exRNAs can enter the nucleus and/or guide transcriptional gene silencing (TGS) in addition to post-transcriptional gene silencing (PTGS); nuclear import of exRNA-RISC is not established in plants [SPECULATIVE].
- Broccoli-specific dormancy is typically shallow and thermodormancy-dominated; the epigenetic dormancy locks described here may be less relevant than in deeply dormant species [KNOWN for Brassica; Wurr et al., 2002].

**Testable predictions**:
1. Bisulfite sequencing of exRNA-treated vs. untreated broccoli seeds at 12 h and 24 h post-imbibition should show reduced methylation at GA-responsive promoters (e.g., *BolC.GA3ox1*, *BolC.EXP2*) in treated seeds.
2. ATAC-seq or MNase-seq should reveal increased chromatin accessibility at germination-associated loci in treated seeds.
3. Co-treatment with 5-azacytidine (DNA methylation inhibitor) should partially phenocopy the exRNA effect; combining exRNA treatment with 5-azacytidine should show diminishing returns (epistasis) if they act through the same mechanism.
4. If this model is correct, exRNA treatment should be ineffective on seeds that have already undergone stratification-induced epigenetic remodeling (i.e., fully after-ripened, non-dormant seeds should show minimal additional benefit).

---

## Model 2: The Hormonal Rebalancing and Mechanical Release Model ("Cut the Brakes, Weaken the Wall")

**Core hypothesis**: Bacterial exRNAs simultaneously suppress ABA-pathway amplifiers and defense-associated hormone nodes while reducing cell wall reinforcement enzyme activity, directly lowering the mechanical resistance threshold for radicle protrusion — the rate-limiting biophysical step in germination.

**Causal chain**:

1. **Entry & Loading**: Same as Model 1. exRNAs enter seed cells during imbibition, are loaded into AGO-RISC complexes, and act primarily via post-transcriptional gene silencing (mRNA cleavage or translational repression) in the cytoplasm [INFERRED]. This model does not require nuclear entry of RISC, making it mechanistically simpler.

2. **Hormone signaling node suppression** → Shift from ABA dominance to GA/ethylene dominance:
   - **AHP-like phosphotransfer protein (SOV4g032870.1)** is downregulated → disruption of the two-component cytokinin/ABA relay system → reduced amplification of ABA signaling in the embryo. In Arabidopsis, AHP proteins relay phosphosignals from AHK receptors to type-B ARR transcription factors; some AHPs positively regulate ABA sensitivity during germination [KNOWN; Nishimura et al., 2004; reviewed in Hwang et al., 2012]. Loss of AHP function can phenocopy reduced ABA sensitivity [INFERRED for this specific paralog].
   - **Lipoxygenase (SOV3g035520.1)** is downregulated → reduced JA biosynthesis (LOX catalyzes the first committed step in the octadecanoid pathway) → loss of JA-ABA synergistic inhibition of germination [KNOWN that JA inhibits germination synergistically with ABA; Dave et al., 2011, J Exp Bot]. Additionally, reduced LOX activity decreases production of oxylipins that promote lipid peroxidation and membrane damage during imbibition [INFERRED].
   - **Ethylene receptor (SOV3g000150.1)** is downregulated → constitutive ethylene signaling (ethylene receptors are negative regulators; in their absence, the pathway is "on") → ethylene response antagonizes ABA-mediated dormancy maintenance [KNOWN; Beaudoin et al., 2000, Plant Cell; Ghassemian et al., 2000; the *etr1* loss-of-function in Arabidopsis shows reduced ABA sensitivity during germination].
   - **PP2A regulatory subunit (SOV3g033920.1)** is downregulated → altered phosphatase activity. PP2A dephosphorylates SnRK2 kinases, but the regulatory A subunit scaffolds specific PP2A holoenzymes; depending on the specific complex, this could either enhance or reduce ABA signaling. In Arabidopsis, specific PP2A complexes positively regulate ABA signaling by dephosphorylating negative regulators [KNOWN; Waadt et al., 2015]. Downregulation of this scaffolding subunit likely disrupts multiple PP2A holoenzymes, with the net effect of destabilizing ABA signal transduction [INFERRED].

3. **Defense pathway suppression** → Elimination of the JA/SA growth penalty:
   - **EDR2 (SOV3g043450.1, SOV6g048760.1)** downregulation: EDR2 is a negative regulator of SA-mediated defense in Arabidopsis [KNOWN; Vorwerk et al., 2007]. Its downregulation would paradoxically *increase* SA pathway activity. However, this is compensated by simultaneous downregulation of positive immune regulators:
   - **MOS1-like (SOV5g005530.1)** downregulation → reduced R-protein–mediated immunity (MOS1 is required for SNC1-mediated autoimmunity in Arabidopsis) [KNOWN; Li et al., 2010].
   - **MYB and NAC transcription factors (SOV1g020340.1, SOV2g014810.1)** downregulation → suppression of stress-responsive transcriptional programs that compete with growth [INFERRED; many MYB and NAC TFs are positive regulators of ABA-responsive gene expression].
   - Net effect: reduced metabolic allocation to defense, freeing carbon and nitrogen for growth [INFERRED].

4. **Cell wall mechanical threshold is lowered** → Direct facilitation of radicle protrusion:
   - **Glycosyltransferases (SOV4g010600.1, SOV1g033840.1)** are downregulated → reduced *de novo* synthesis of cell wall polysaccharides (hemicelluloses, pectins) in the micropylar endosperm cap → the wall is not reinforced during imbibition [INFERRED].
   - **Beta-galactosidase (SOV4g051070.1)** is downregulated → this appears counterintuitive (BGALs degrade wall), but specific BGALs in seeds function in galactolipid turnover or cell wall remodeling that *stiffens* the wall (e.g., by removing galactan side chains from rhamnogalacturonan I, increasing pectin gel strength) [KNOWN; Sampedro et al., 2012; specific BGAL isoforms promote wall stiffening].
   - **Peroxidase (SOV3g038840.1)** is downregulated → reduced oxidative cross-linking of wall phenolics and extensins → wall remains extensible [KNOWN; class III peroxidases catalyze lignin/suberin polymerization and diferulate cross-linking in the testa; Müller et al., 2009].
   - Combined with the hormonal shift (reduced ABA removes transcriptional support for wall-strengthening programs; increased ethylene signaling promotes expansin expression), the micropylar endosperm cap becomes mechanically weaker [INFERRED].

5. **ROS homeostasis is retuned to favor the "oxidative window"**:
   - Downregulation of **GST-L3 (SOV3g040200.1)** and **peroxidase (SOV3g038840.1)** reduces ROS scavenging capacity → allows accumulation of H₂O₂ in the apoplast of the endosperm cap → non-enzymatic oxidative cleavage of wall polysaccharides → further wall weakening [KNOWN; Müller et al., 2009; Leymarie et al., 2012].
   - The "oxidative window" hypothesis: germination requires ROS levels high enough to signal and weaken walls, but not so high as to cause lethal oxidative damage. Reducing scavenging enzymes widens this window [KNOWN; Bailly et al., 2008, C.R. Biologies].

6. **Net phenotypic outcome**: The embryo's growth potential (turgor-driven expansion) exceeds the mechanical resistance of the weakened endosperm cap at an earlier time point → radicle protrusion occurs sooner. Predicted effect: 25–50% reduction in T50, with the largest effect under suboptimal conditions (high temperature thermodormancy in broccoli, where ABA/mechanical resistance is the primary constraint) [INFERRED].

**Supporting evidence**:
- Ethylene receptor mutants (*etr1-1*) in Arabidopsis show reduced dormancy and ABA insensitivity [KNOWN; Beaudoin et al., 2000]
- LOX-deficient seeds show reduced JA and improved germination under stress [KNOWN; Dave et al., 2011]
- Micropylar endosperm weakening is the rate-limiting step for germination in Brassicaceae [KNOWN; Müller et al., 2006, Plant Cell; Linkies et al., 2009]
- Class III peroxidases and ROS are directly implicated in endosperm cap weakening in *Lepidium sativum* (Brassicaceae) [KNOWN; Müller et al., 2009]
- The hormone-wall-ROS axis is the most mechanistically direct path to radicle protrusion [KNOWN]
- Three hormone targets + three cell wall targets + three ROS targets = nine genes forming a coherent, proximal-to-phenotype module [KNOWN from target list]

**Weaknesses**:
- This model explains speed of germination well but is less compelling for *seedling vigor* (post-germination growth), which would require sustained effects beyond the initial protrusion event.
- The EDR2 downregulation paradox (EDR2 is a negative regulator of defense; its suppression should increase defense, not decrease it) creates an internal contradiction unless the net immune suppression from MOS1/RLK/MYB/NAC downregulation overrides it. This requires careful quantitative consideration [KNOWN limitation].
- Does not fully explain why 110 genes are targeted if only ~9 core genes in this model are sufficient. The remaining targets would need to be either (a) functionally redundant backup targets, (b) contributors to seedling vigor rather than germination *per se*, or (c) off-target effects of exRNA activity.
- Cannot easily separate from EPS osmopriming: osmopriming alone advances imbibition phase II → III transition and promotes endosperm weakening [KNOWN; Chen & Arora, 2013].
- The TPS (trehalose-phosphate synthase) target, one of the highest-priority metabolic genes, is not well integrated into this model.

**Testable predictions**:
1. Puncture-force measurements on micropylar endosperm caps of exRNA-treated vs. untreated broccoli seeds should show significantly reduced mechanical resistance in treated seeds at 12–24 h post-imbibition.
2. Exogenous ABA application should partially rescue (delay) the germination-promoting effect of exRNA treatment in a dose-dependent manner, if ABA pathway suppression is a major driver.
3. In *Arabidopsis etr1-1* (constitutive ethylene signaling) mutant seeds, exRNA treatment should show reduced additional benefit compared to wild-type, indicating epistasis at the ethylene receptor node.
4. DAB (3,3'-diaminobenzidine) staining for H₂O₂ in the micropylar region should show earlier and stronger ROS accumulation in exRNA-treated seeds.
5. The effect should be largest under thermodormancy-inducing conditions (35°C for broccoli), where ABA-mediated inhibition is the dominant constraint [KNOWN; Huo et al., 2013].

---

## Model 3: The Metabolic Reallocation and Checkpoint Override Model ("Spend Now, Verify Later")

**Core hypothesis**: Bacterial exRNAs reprogram the seed's metabolic resource allocation strategy by simultaneously suppressing energy-expensive defense and stress-preparedness programs, overriding DNA damage and cell cycle checkpoints, and redirecting carbon/nitrogen flux from storage-protective to growth-promoting metabolism — effectively forcing the seed to "bet on growth" rather than "hedge against risk."

**Causal chain**:

1. **Entry & Loading**: Same as Models 1 and 2. exRNAs act primarily via PTGS (cytoplasmic mRNA degradation/translational inhibition) [INFERRED].

2. **Metabolic reallocation from defense to growth** → Carbon and nitrogen flux redirection:
   - **Trehalose-phosphate synthase (TPS; SOV2g009230.1)** is downregulated → reduced trehalose-6-phosphate (T6P) levels → T6P is a sugar-signaling metabolite that inhibits SnRK1 kinase activity. Lower T6P releases SnRK1, which activates catabolic pathways and inhibits anabolic pathways [KNOWN; Schluepmann et al., 2003; reviewed in Figueroa & Lunn, 2016]. Paradoxically, SnRK1 activation can also promote ABA signaling. However, in the germination context, the primary effect of reduced T6P may be to signal "low energy status" → triggering aggressive mobilization of stored reserves (lipids, proteins, starch) [INFERRED].
   - **6-phosphogluconate dehydrogenase (6PGDH; SOV6g029280.1)** is downregulated → reduced flux through the oxidative pentose phosphate pathway (oxPPP) → reduced NADPH production. This seems counterintuitive (NADPH is needed for biosynthesis), but: (a) reduced NADPH limits the regeneration of reduced glutathione, synergizing with GST/peroxidase downregulation to permit the pro-germination ROS burst [INFERRED]; (b) it may redirect glucose-6-phosphate toward glycolysis and respiration (ATP production) rather than NADPH-consuming biosynthetic pathways, prioritizing energy over building blocks in the earliest phase of germination [SPECULATIVE].
   - **GDSL esterases/lipases (SOV1g004930.1, SOV4g008190.1, SOV6g042250.1)** — three paralogs are downregulated → reduced lipid hydrolysis. This is initially paradoxical (lipid mobilization is needed for germination). However, GDSL lipases have diverse roles including cuticle biosynthesis, cell wall modification, and defense compound release. Their downregulation may reduce cutin/suberin deposition on the testa (reducing mechanical barrier) or suppress release of antimicrobial lipid derivatives, redirecting lipid metabolism toward β-oxidation for energy [INFERRED; Lai et al., 2017].
   - **Phytoene synthase (SOV4g000330.1)** is downregulated → reduced carotenoid biosynthesis → reduced ABA precursor availability (ABA is synthesized from carotenoid precursors via the MEP/carotenoid pathway) [KNOWN; Nambara & Marion-Poll, 2005]. This directly reduces ABA biosynthetic capacity, reinforcing the hormonal shift in Model 2 through a metabolic rather than signaling mechanism.
   - **Cytochrome P450 (SOV4g055600.1)** is downregulated → CYP450s are involved in diverse biosynthetic pathways including ABA catabolism, GA biosynthesis, brassinosteroid biosynthesis, and secondary metabolite production. Without knowing the specific CYP family, the most parsimonious interpretation is suppression of a defense-associated secondary metabolite pathway (e.g., glucosinolate biosynthesis, which is prominent in Brassicaceae and metabolically expensive) [INFERRED; Bak et al., 2011].

3. **DNA damage checkpoint override** → Faster cell cycle re-entry:
   - **ATR kinase (SOV4g051610.1)** is downregulated → reduced DNA damage checkpoint stringency. ATR is the master kinase for replication stress and single-strand break responses; it phosphorylates CHK1, WEE1, and SOG1 to arrest the cell cycle at G2/M [KNOWN; Culligan et al., 2004; Yoshiyama et al., 2013]. Seeds accumulate DNA damage during desiccation and storage. Normally, cells must repair this damage before dividing. Reducing ATR activity allows cells to proceed through the cell cycle with unrepaired damage [INFERRED].
   - **DNA topoisomerase 2 (SOV1g019270.1)** downregulation → reduced resolution of topological constraints → this could slow replication, but in the context of reduced checkpoint stringency, cells may tolerate replication stress and proceed anyway [SPECULATIVE].
   - **DNA polymerases (SOV4g011580.1, SOV3g022260.1, SOV3g003500.1)** downregulation → seems counterproductive for DNA replication. However, these may represent specialized repair polymerases (e.g., translesion synthesis polymerases or organellar polymerases) rather than the replicative Pol ε/δ. Downregulating repair-specific polymerases would further reduce checkpoint activation by preventing detection of repair intermediates [SPECULATIVE].
   - Net effect: cells in the radicle meristem re-enter the cell cycle faster, even with some unrepaired DNA damage → earlier onset of cell division → faster radicle elongation [INFERRED].

4. **Defense resource reallocation** → Metabolic "peace dividend":
   - Same defense suppression as in Model 2 (EDR2, MOS1, RLKs, MYB, NAC, NST1 downregulation).
   - Additionally, **CTP synthase (SOV5g001320.1)** downregulation → reduced *de novo* pyrimidine biosynthesis. CTP is needed for RNA synthesis, membrane lipid synthesis (CDP-diacylglycerol), and DNA synthesis. Downregulation may seem counterproductive, but: (a) seeds contain large stores of nucleotides from maturation; (b) reducing *de novo* synthesis forces reliance on salvage pathways, which are more energy-efficient; (c) CTP is specifically required for immune-associated RNA production (e.g., defense gene transcripts) — reducing CTP availability preferentially limits the most transcriptionally active programs, which in a stressed seed would be defense [SPECULATIVE].
   - **Aspartokinase (SOV1g048270.1)** downregulation → reduced flux into the aspartate-derived amino acid pathway (threonine, methionine, isoleucine, lysine). This may redirect aspartate toward asparagine (a nitrogen transport/storage amino acid) or toward the TCA cycle via oxaloacetate, prioritizing energy production over *de novo* amino acid synthesis during the earliest germination phase when stored amino acids from seed protein degradation are abundant [INFERRED].

5. **Organelle streamlining** → Energy efficiency:
   - Downregulation of chloroplast import (TIC214) and biogenesis (RETICULATA) components → delayed chloroplast development → saves the enormous energy cost of building photosynthetic machinery that is useless underground [INFERRED].
   - Mitochondrial targets (TIM50, cytochrome c biogenesis) are partially downregulated → this may represent fine-tuning rather than wholesale suppression; reducing mitochondrial *biogenesis* while relying on existing mitochondria forces efficient use of the current organelle population rather than energy-expensive *de novo* construction [INFERRED].

6. **Net phenotypic outcome**: The seed adopts a "fast-and-risky" germination strategy — mobilizing reserves aggressively, dividing before full DNA repair, suppressing defense, and delaying organelle biogenesis — to achieve the fastest possible radicle emergence and early seedling establishment. Predicted effect: significant reduction in T50 (30–50%) and increased hypocotyl/radicle length at 72 h, but potentially at the cost of increased sensitivity to post-emergence pathogen attack and slightly elevated mutation rate in the first generation. Seedling vigor is improved in the short term but may show vulnerability under biotic stress.

**Supporting evidence**:
- T6P/SnRK1 signaling is a master regulator of the starvation/growth switch in plants [KNOWN; Baena-González et al., 2007]
- Phytoene synthase downregulation reduces ABA precursor availability [KNOWN; Nambara & Marion-Poll, 2005; Li et al., 2008 demonstrated PSY RNAi reduces ABA in rice]
- ATR mutants in Arabidopsis show faster cell cycle progression but increased genomic instability [KNOWN; Culligan et al., 2004]
- Brassica seeds contain substantial nucleotide and amino acid reserves from maturation [KNOWN; Baud et al., 2002]
- Glucosinolate biosynthesis consumes ~15% of total sulfur and significant carbon in Brassicaceae seeds [KNOWN; Grubb & Abel, 2006]
- 15 metabolic targets + 6 DNA repair targets + 6 organelle targets = 27 genes forming a coherent "metabolic reallocation" module [KNOWN from target list]

**Weaknesses**:
- This is the most complex model, invoking the largest number of targets and the most speculative mechanistic steps. Occam's razor disfavors it relative to Models 1 and 2.
- The checkpoint override component is risky: if DNA damage is severe (old seed lots), bypassing repair could lead to seedling lethality rather than vigor. This model predicts that exRNA treatment should be *detrimental* to aged seeds with high DNA damage loads — a testable but potentially problematic prediction.
- Several mechanistic steps are internally contradictory (e.g., downregulating DNA polymerases while promoting faster cell division; downregulating 6PGDH while needing NADPH for biosynthesis). These contradictions require invoking functional specialization of paralogs (repair vs. replicative polymerases) or temporal phasing of effects, both of which are [SPECULATIVE].
- The T6P/SnRK1 paradox: SnRK1 activation by reduced T6P should promote ABA signaling via phosphorylation of ABI5 [KNOWN; Tsai & Gazzarrini, 2012]. This directly contradicts the ABA-suppression narrative of Model 2. Resolving this requires either (a) the ABA-suppressive effects of other targets overriding SnRK1-mediated ABI5 activation, or (b) the primary role of TPS downregulation being something other than SnRK1 activation (e.g., reducing T6P's direct inhibition of hexokinase-mediated sugar signaling) [SPECULATIVE].
- Hardest model to distinguish from EPS osmopriming effects, since osmopriming itself advances metabolic activation and reserve mobilization.

**Testable predictions**:
1. Metabolomic profiling (LC-MS) of exRNA-treated vs. untreated seeds at 6–12 h should show reduced T6P levels, reduced carotenoid intermediates, and altered glucosinolate profiles in treated seeds.
2. Flow cytometry of radicle tip cells should show earlier S-phase entry (higher 4C:2C ratio at 18–24 h) in exRNA-treated seeds.
3. Comet assays on radicle meristem cells should show *higher* residual DNA damage in exRNA-treated seedlings at 48 h (due to checkpoint bypass), despite faster germination.
4. exRNA treatment of artificially aged seeds (controlled deterioration test) should show *reduced* benefit or even detrimental effects compared to fresh seeds, if checkpoint override is a major mechanism.
5. Combining exRNA treatment with caffeine (ATR/ATM inhibitor) should show diminishing returns if checkpoint override is already achieved by exRNA-mediated ATR suppression.
6. ^13C-glucose feeding experiments should show altered flux partitioning (more toward glycolysis/TCA, less toward PPP and secondary metabolism) in treated seeds.

---

## Model Comparison Table

| Feature | Model 1: Epigenetic Derepression | Model 2: Hormonal Rebalancing & Mechanical Release | Model 3: Metabolic Reallocation & Checkpoint Override |
|---|---|---|---|
| **Core mechanism** | Chromatin decompaction unlocks germination gene programs | ABA/JA suppression + ethylene activation + wall weakening | Resource redirection + faster cell cycle + defense suppression |
| **Primary targets explained** | 6 epigenetic + 5 transposon (11 genes) | 3 hormone + 3 cell wall + 3 ROS + 5 defense (14 genes) | 15 metabolic + 6 DNA repair + 6 organelle + 5 defense (32 genes) |
| **Total targets well-integrated** | ~17/110 (15%) directly; remainder as downstream beneficiaries | ~20/110 (18%) directly; remainder as amplifiers | ~38/110 (35%) directly; best coverage |
| **Mechanism complexity** | Low–moderate (single master switch) | Moderate (three parallel proximal mechanisms) | High (many parallel mechanisms with internal tensions) |
| **Speed of expected effect** | Slow (requires DNA replication for passive demethylation; hours to days) | Fast (PTGS of existing mRNAs; minutes to hours for protein turnover) | Moderate (metabolic flux changes within hours; checkpoint effects at first S-phase) |
| **Explains germination speed** | Yes, but with temporal lag | Yes, most directly | Yes |
| **Explains seedling vigor** | Yes (sustained transcriptional reprogramming) | Partially (initial protrusion advantage may not persist) | Yes (continued metabolic efficiency and resource mobilization) |
| **Broccoli thermodormancy relevance** | Moderate (thermodormancy involves ABA but epigenetic component less characterized) | High (thermodormancy is ABA-mediated; endosperm weakening is rate-limiting in Brassicaceae) | Moderate (metabolic effects relevant but checkpoint override less so) |
| **Distinguishable from EPS osmopriming** | Yes (epigenetic marks are specific; osmopriming doesn't alter methylation) | Partially (osmopriming also advances endosperm weakening) | Difficult (osmopriming also activates metabolism) |
| **Internal contradictions** | Minimal | EDR2 paradox (minor) | T6P/SnRK1 paradox; DNA polymerase paradox (significant) |
| **Key testable prediction** | Reduced DNA methylation at GA-responsive promoters | Reduced micropylar endosperm puncture force | Earlier S-phase entry + higher residual DNA damage |
| **Risk to plant** | Low (reversible transcriptional changes) | Low (physiological hormone shift) | Moderate–high (genomic instability from checkpoint bypass) |
| **Overall plausibility** | ★★★★☆ | ★★★★★ | ★★★☆☆ |

---

## Recommended Model

**Model 2 (Hormonal Rebalancing and Mechanical Release)** is the best-supported causal framework, for the following reasons:

1. **Mechanistic proximity to the rate-limiting step**: Germination in Brassicaceae is defined by radicle protrusion through the micropylar endosperm cap. Model 2 directly addresses the two determinants of this event — the growth potential of the embryo (hormonal) and the restraint of the covering layers (mechanical/cell wall) [KNOWN; Finch-Savage & Leubner-Metzger, 2006]. This is the most parsimonious path from molecular targets to phenotype.

2. **Speed of action**: PTGS-mediated mRNA degradation and translational repression can reduce target protein levels within hours of exRNA loading into RISC [KNOWN]. This matches the timescale of germination improvement (typically measured within 24–72 h of imbibition). Model 1's requirement for DNA replication-dependent passive demethylation introduces a temporal bottleneck that is difficult to reconcile with rapid effects.

3. **Broccoli-specific relevance**: Broccoli thermodormancy — the most commercially important germination defect in this crop — is primarily mediated by elevated ABA levels and enhanced ABA sensitivity at high temperatures [KNOWN; Huo et al., 2013; Huang et al., 2017]. Model 2 directly targets this axis through three independent mechanisms (AHP suppression, LOX/JA suppression, ethylene receptor suppression), providing robust, multi-node intervention against the specific constraint most relevant to broccoli production.

4. **Fewest internal contradictions**: The EDR2 paradox is the only significant internal tension, and it is resolvable by the quantitative dominance of positive immune regulator suppression (MOS1, R-proteins, RLKs, stress TFs) over the loss of a single negative regulator.

5. **Experimentally tractable**: The key predictions (endosperm puncture force, ABA dose-response epistasis, ROS imaging, ethylene receptor mutant epistasis) are all achievable with established techniques in Brassica seed biology.

**However, the recommended synthesis is that Model 2 operates as the primary, fast-acting mechanism, with Model 1 (epigenetic derepression) providing a slower-acting but more sustained reinforcement layer.** This two-phase model explains both the rapid germination improvement and the extended seedling vigor: exRNAs first shift hormone balance and weaken the wall (hours), then progressively unlock the epigenetic landscape to sustain pro-growth transcription (days). Model 3 components (metabolic reallocation, particularly phytoene synthase → ABA precursor reduction and TPS → reserve mobilization signaling) likely contribute as quantitative modifiers but are not the primary drivers.

The critical next experiment to distinguish between models is a **time-course experiment** combining (a) micropylar endosperm puncture-force assays (Model 2), (b) bisulfite-seq at GA-responsive loci (Model 1), and (c) metabolomic profiling of T6P and carotenoid intermediates (Model 3) at 6, 12, 24, and 48 h post-imbibition in exRNA-treated vs. mock-treated (EPS-only) vs. water-only broccoli seeds. This design also controls for the EPS osmopriming confounder, which is essential for attributing any effect specifically to the exRNA cargo.