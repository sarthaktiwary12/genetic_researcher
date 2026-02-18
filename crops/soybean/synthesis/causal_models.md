# Causal Models — Soybean (Glycine max)



# Alternative Causal Models: Bacterial exRNA-Mediated Germination Improvement in *Spinacia oleracea*

> **Species Note**: As correctly identified in the ranked target analysis, all gene IDs (SOV prefix) correspond to *Spinacia oleracea* (spinach), not *Glycine max*. All models below pertain to spinach seed germination biology. Arabidopsis homologs are used as functional proxies where spinach-specific data are unavailable.

---

## Model 1: The Epigenetic Master Switch — Chromatin De-repression Cascades to Dormancy Dissolution

**Core hypothesis**: Bacterial exRNAs primarily target the seed's epigenetic silencing machinery, causing a genome-wide de-repression of pro-germination gene programs; all other observed changes (hormonal, metabolic, defense) are downstream consequences of this transcriptional unlocking.

**Causal chain**:

1. **Entry**: Bacterial exRNAs (likely 20–25 nt sRNAs, potentially stabilized within extracellular vesicles or bound to RNA-binding proteins within the EPS matrix) are taken up by imbibing spinach seed cells through endocytosis or direct membrane penetration facilitated by the hydrated seed coat. [SPECULATIVE — cross-kingdom sRNA uptake is documented in plant-fungal systems (Cai et al., 2018, *Cell Host Microbe*; Weiberg et al., 2013, *Science*), but the delivery mechanism in a bacterial EPS-to-seed context is uncharacterized]

2. **Primary targets — Epigenetic repressors are silenced**:
   - **SOV1g033340.1 (DNA cytosine-5-methyltransferase)** is downregulated → maintenance methylation at CG and CHG contexts fails during early cell divisions post-imbibition → passive demethylation of promoters of GA-responsive genes (e.g., α-amylases, expansins, cell wall hydrolases) [INFERRED — Arabidopsis *met1* and *cmt3* mutants show reduced dormancy; Zheng et al., 2012, *Plant Cell*]
   - **SOV4g015450.1 (SUVR5-like H3K9 methyltransferase)** is downregulated → loss of repressive H3K9me2 marks at heterochromatic loci harboring dormancy-associated genes → chromatin transitions from closed to open state [INFERRED — SUVR5 in Arabidopsis deposits H3K9me2 and H3K27me3; Caro et al., 2012, *PLoS Genetics*]
   - **SOV6g036290.1 (HIRA histone chaperone)** is downregulated → reduced deposition of histone variant H3.3 at specific loci → altered nucleosome dynamics favoring transcriptional activation at germination loci [INFERRED — HIRA deposits H3.3 at genic regions; loss may paradoxically destabilize repressive nucleosome configurations at dormancy loci]
   - **SOV4g038060.1 (GIS2 zinc finger)** is downregulated → de-repression of trichome and growth-related developmental programs; in Arabidopsis, GIS-family members regulate epidermal differentiation downstream of GA/cytokinin [KNOWN for Arabidopsis GIS; INFERRED for spinach ortholog]
   - **SOV4g030590.1 (PHD domain protein)** is downregulated → loss of a "reader" that recruits Polycomb Repressive Complex 2 (PRC2) to H3K4me0 marks → reduced H3K27me3 deposition at pro-germination loci [INFERRED]

3. **Secondary cascade — Chromatin opening enables hormone pathway reconfiguration**:
   - With promoter demethylation and loss of repressive histone marks, GA-biosynthesis genes and GA-signaling components become transcriptionally accessible [INFERRED]
   - Simultaneously, ABA catabolism genes (e.g., *CYP707A* family) are de-repressed, reducing endogenous ABA levels [INFERRED — ABA catabolism genes are known targets of DNA methylation-mediated silencing in Arabidopsis seeds; Nonogaki, 2014, *Annual Review of Plant Biology*]
   - The exRNA-mediated downregulation of **SOV3g000150.1 (ethylene receptor)** now synergizes with the epigenetic de-repression: ethylene receptor is a negative regulator of ethylene signaling [KNOWN], so its loss activates constitutive ethylene responses → ethylene antagonizes ABA signaling and promotes GA sensitivity [KNOWN — Linkies et al., 2009, *Plant Cell*]
   - **SOV4g032870.1 (AHP1-like)** downregulation disrupts a cytokinin-ABA signaling relay that normally reinforces ABA sensitivity [INFERRED]

4. **Tertiary effects — Defense, metabolism, and growth respond to the new hormonal landscape**:
   - GA-dominant state activates endogenous cell wall hydrolases → endosperm weakening → radicle protrusion [KNOWN mechanism]
   - ABA decline releases the defense-growth tradeoff → defense genes (EDR2, MOS1, R-proteins) are no longer maintained at high expression, consistent with their observed downregulation [INFERRED — the exRNA targeting of defense genes may be partially redundant with the hormonal shift, or may serve as a "belt-and-suspenders" reinforcement]
   - Metabolic enzymes shift from stress/storage mode to mobilization mode (TPS downregulation removes T6P-mediated growth inhibition; LOX downregulation reduces JA biosynthesis) [INFERRED]

5. **Net phenotypic outcome**: Faster, more uniform radicle emergence due to genome-wide transcriptional de-repression of germination programs, amplified by a decisive ABA→GA hormonal shift. Seedling vigor is enhanced because the epigenetic reprogramming also unlocks post-germinative growth genes (photomorphogenesis, nutrient mobilization).

**Supporting evidence**:
- DNA methylation and histone modification are established master regulators of seed dormancy/germination transitions in Arabidopsis [KNOWN — Nonogaki, 2014; Footitt et al., 2015, *PNAS*]
- Cross-kingdom sRNAs can direct DNA methylation via the RdDM pathway in recipient cells [KNOWN — demonstrated in *Cuscuta*–host interactions; Shahid et al., 2018, *Nature*]
- The epigenetic target set in this analysis is unusually coherent (DNA methyltransferase + histone methyltransferase + histone chaperone + chromatin reader + transcriptional repressor), suggesting coordinated pathway targeting rather than random off-target effects [INFERRED]
- Passive demethylation during early cell divisions is sufficient to de-repress dormancy genes without requiring active demethylases [KNOWN — maintenance methylation failure phenocopies active demethylation in many contexts]

**Weaknesses**:
- This model positions epigenetic changes as the *primary* cause, but epigenetic reprogramming is inherently slow (requires at least one round of DNA replication for passive demethylation). This creates a temporal problem: improved germination speed implies effects within hours of imbibition, before significant DNA replication occurs. The model may therefore overweight the causal primacy of epigenetics relative to direct hormone signaling effects.
- Does not adequately explain why transposon-related genes (5 reverse transcriptases, 1 Gag protein) are targeted — if chromatin is opening globally, transposon de-repression would be a dangerous side effect. Their separate targeting by exRNAs suggests a more direct silencing mechanism (post-transcriptional) rather than a purely epigenetic cascade.
- Cannot distinguish epigenetic effects from direct post-transcriptional gene silencing (PTGS) of the same targets by the exRNAs. The exRNAs may silence these genes via mRNA degradation/translational inhibition, not via transcriptional gene silencing (TGS).
- The EPS matrix is itself an osmopriming agent [KNOWN — bacterial exopolysaccharides modulate water potential], and osmotic priming is known to alter DNA methylation patterns in seeds [KNOWN — Paparella et al., 2015, *Plant Cell Reports*]. This is a critical confounder: observed epigenetic changes may be EPS-mediated rather than exRNA-mediated.

**Testable predictions**:
1. **Bisulfite sequencing** of treated vs. untreated spinach seeds at 12, 24, and 48 hours post-imbibition should reveal reduced methylation specifically at promoters of GA-responsive and germination-associated genes, not genome-wide random demethylation.
2. **RNase-treated EPS controls**: If the EPS matrix is pre-treated with RNase A/III to degrade exRNAs but preserve polysaccharide structure, the epigenetic changes should be abolished while osmopriming effects persist. Germination improvement should be significantly reduced but not eliminated.
3. **ChIP-seq for H3K9me2 and H3K27me3** should show reduced repressive marks at germination loci in exRNA-treated seeds compared to controls.
4. **Application of 5-azacytidine** (DNA methylation inhibitor) to untreated seeds should partially phenocopy the exRNA treatment's germination acceleration, and the combination should not be additive (epistasis test).
5. A **met1/cmt3-like CRISPR mutant** in spinach (targeting SOV1g033340.1) should show constitutively reduced dormancy, partially mimicking the exRNA effect even without bacterial treatment.

---

## Model 2: The Hormonal Checkpoint Collapse — Coordinated Dismantling of ABA-Ethylene-JA Signaling Brakes

**Core hypothesis**: Bacterial exRNAs directly silence a small number of critical hormone signaling nodes (ethylene receptor, AHP1-like, LOX, TPS), causing a rapid collapse of the ABA-dominant hormonal state; all other target changes are either secondary consequences of this hormonal shift or represent parallel reinforcement of the same pro-germination outcome.

**Causal chain**:

1. **Entry**: Bacterial exRNAs are delivered to seed cells during imbibition, likely via vesicle-mediated uptake. The exRNAs are loaded into the host AGO1-containing RISC complex and direct post-transcriptional gene silencing (PTGS) of target mRNAs via sequence-complementary cleavage or translational repression. [SPECULATIVE for this specific system; KNOWN mechanism for cross-kingdom RNAi generally — Weiberg et al., 2013]

2. **Primary targets — Three hormone signaling brakes are simultaneously released**:
   - **SOV3g000150.1 (Ethylene receptor)** is silenced → constitutive ethylene signaling is activated. In Arabidopsis, ethylene receptors (ETR1, ERS1, ETR2, EIN4, ERS2) are negative regulators: they actively suppress the ethylene response pathway when ethylene is absent [KNOWN — Chang et al., 1993, *Science*; Hua & Meyerowitz, 1998, *Cell*]. Loss-of-function of ethylene receptors mimics constitutive ethylene signaling → activation of EIN2 → EIN3/EIL1 transcription factors → promotion of germination. In Arabidopsis, *etr1* loss-of-function mutants show enhanced germination, especially under salt stress [KNOWN — Wilson et al., 2014, *Plant Physiology*; Chiwocha et al., 2005, *Plant Journal*]. Ethylene directly antagonizes ABA signaling by promoting ABA catabolism (via CYP707A2 upregulation) and reducing ABA sensitivity [KNOWN].
   - **SOV3g035520.1 (Lipoxygenase, LOX)** is silenced → reduced production of 13-HPOT and downstream oxylipins, including jasmonic acid (JA) and its bioactive conjugate JA-Ile [INFERRED — LOX is the first committed step in JA biosynthesis via the octadecanoid pathway; KNOWN]. JA acts synergistically with ABA to maintain dormancy and inhibit germination [KNOWN — Dave et al., 2011, *Plant Cell*]. Loss of LOX activity breaks this ABA-JA synergy, further weakening the dormancy program.
   - **SOV4g032870.1 (AHP1-like histidine phosphotransfer protein)** is silenced → disruption of the two-component signaling relay that transduces cytokinin and potentially ABA signals from receptors to nuclear response regulators [INFERRED]. In Arabidopsis, AHP proteins shuttle between cytoplasm and nucleus to relay phosphorelay signals; some AHP family members positively regulate ABA sensitivity [INFERRED from Arabidopsis *ahp* mutant studies showing altered stress responses; Hutchison et al., 2006, *Plant Cell*]. Downregulation reduces ABA signal amplification.

3. **Critical amplification node — TPS downregulation creates a metabolic "starvation signal"**:
   - **SOV2g009230.1 (Trehalose-phosphate synthase, TPS)** is silenced → reduced trehalose-6-phosphate (T6P) levels. T6P is a master metabolic signal that reports sugar sufficiency to the SnRK1 kinase complex [KNOWN — Schluepmann et al., 2003, *PNAS*; Zhang et al., 2009, *Plant Cell*]. When T6P is low, SnRK1 is activated → SnRK1 phosphorylates and activates ABI5 degradation while promoting catabolic pathways [KNOWN — Tsai & Gazzarrini, 2014, *Plant Journal*]. Paradoxically, the "starvation signal" from low T6P promotes reserve mobilization, accelerating the conversion of stored lipids and starch into usable energy. This directly feeds germination vigor.
   - T6P reduction also relieves T6P-mediated inhibition of SnRK1, which promotes autophagy and catabolism [KNOWN], further accelerating reserve mobilization.

4. **Downstream consequences of the hormonal shift**:
   - **ABA levels decline** due to: (a) ethylene-induced upregulation of ABA 8'-hydroxylase (CYP707A family); (b) loss of JA-ABA synergy; (c) SnRK1-mediated destabilization of ABA signaling components [INFERRED from combined pathway logic]
   - **GA sensitivity increases** as ABA-mediated DELLA stabilization is relieved → DELLA degradation → activation of GA-responsive transcription [KNOWN mechanism]
   - **Defense genes decline secondarily**: With ABA and JA both reduced, the transcriptional programs they sustain (including EDR2, MOS1, NST1, R-proteins, stress MYB/NAC TFs) lose their inductive signals and decay. The exRNA-mediated targeting of defense genes (SOV3g043450.1, SOV6g048760.1, SOV5g005530.1, SOV1g021670.1) provides **redundant insurance** ensuring defense suppression even if hormonal changes are incomplete [INFERRED]
   - **Epigenetic changes occur secondarily**: The hormonal shift from ABA to GA alters the expression of chromatin modifiers endogenously. GA signaling is known to promote histone acetylation at target loci [KNOWN — Zentella et al., 2007, *Plant Cell*]. The exRNA-mediated silencing of epigenetic repressors (SOV1g033340.1, SOV4g015450.1, SOV6g036290.1) reinforces this endogenous process but is not the primary driver [INFERRED]

5. **ROS optimization as a hormone-dependent secondary effect**:
   - **SOV3g038840.1 (Peroxidase)** and **SOV3g040200.1 (GST)** downregulation → reduced ROS scavenging capacity → transient ROS accumulation in the apoplast [INFERRED]
   - This transient ROS burst is now *beneficial* because it occurs in the context of a GA-dominant hormonal state: ROS promotes cell wall loosening via oxidative scission of polysaccharides in the micropylar endosperm [KNOWN — Müller et al., 2009, *Plant Journal*; Leymarie et al., 2012, *Plant Cell & Environment*]
   - Without the hormonal shift, the same ROS increase could be damaging; the hormone context determines whether ROS is a germination signal or an oxidative stress event [KNOWN principle]

6. **Net phenotypic outcome**: Rapid collapse of the ABA/JA-dominant dormancy state within hours of imbibition (faster than epigenetic reprogramming), leading to accelerated endosperm weakening, radicle emergence, and reserve mobilization. Seedling vigor is enhanced by SnRK1-mediated metabolic activation and ethylene-promoted hypocotyl elongation.

**Supporting evidence**:
- Ethylene receptor loss-of-function is one of the best-characterized single-gene mutations promoting germination in Arabidopsis [KNOWN]
- LOX-mediated JA biosynthesis is a validated dormancy maintenance mechanism; *lox* mutants show reduced dormancy [KNOWN — Dave et al., 2011]
- T6P-SnRK1 signaling is a master metabolic switch with direct connections to ABA signaling [KNOWN]
- The three primary hormone targets (ethylene receptor, LOX, AHP1) are all Tier 1 high-priority targets in the ranked analysis, consistent with their causal primacy [INFERRED]
- Hormonal effects are rapid (minutes to hours for receptor-level changes) compared to epigenetic reprogramming (hours to days), better matching the expected kinetics of germination improvement [KNOWN principle]

**Weaknesses**:
- This model treats the six epigenetic targets as secondary, but their coherence as a pathway (DNA methyltransferase + histone methyltransferase + chaperone + reader + TF) is difficult to explain as mere downstream hormone effects. If epigenetic changes were purely secondary, we would not expect the exRNAs to specifically target these genes — the endogenous hormone-driven chromatin remodeling would suffice.
- The model assumes exRNAs act primarily via PTGS (mRNA cleavage/translational repression), but some exRNAs may act via TGS (directing DNA methylation at target loci). If TGS is the primary mechanism, then the "speed advantage" of this model over Model 1 is diminished.
- Does not explain the targeting of DNA repair/replication checkpoint genes (ATR kinase, DNA polymerases, topoisomerase) — these are not obvious downstream targets of hormone signaling.
- The role of the 18 transport/ion homeostasis genes is underexplained. While some transporters are hormone-responsive, the specific targeting of two cation-chloride cotransporters and a CNGC channel suggests direct functional relevance beyond hormonal secondary effects.
- **Confounder**: Ethylene is produced endogenously during seed imbibition, and EPS-mediated physical priming could alter ethylene diffusion kinetics. The observed "ethylene receptor downregulation" effect might be partially mimicked by enhanced ethylene accumulation due to EPS coating [SPECULATIVE].

**Testable predictions**:
1. **Hormone quantification**: LC-MS/MS measurement of ABA, JA, JA-Ile, GA₁, GA₃, and ethylene (by GC) in exRNA-treated vs. control seeds at 6, 12, 24, and 48 hours should show: (a) earlier ABA decline; (b) reduced JA/JA-Ile accumulation; (c) elevated ethylene or ethylene-response gene expression.
2. **Epistasis with ethylene pathway mutants**: If a spinach *ein2*-like mutant (ethylene-insensitive) is treated with the bacterial exRNAs, the germination improvement should be significantly attenuated but not abolished (because LOX and AHP silencing provide parallel pathways).
3. **Exogenous ABA rescue**: Application of exogenous ABA (1–10 μM) to exRNA-treated seeds should partially restore dormancy, confirming that ABA pathway suppression is a primary mechanism. The dose required to restore dormancy should be higher in exRNA-treated seeds than in controls (reflecting reduced ABA sensitivity).
4. **T6P measurement**: Direct quantification of T6P by anion-exchange LC-MS/MS should show reduced T6P in exRNA-treated seeds, with concomitant increase in SnRK1 activity (measured by phosphorylation of the SnRK1 target peptide AMARA).
5. **Synthetic exRNA validation**: Delivery of synthetic 21-nt siRNAs targeting only the three primary hormone nodes (ethylene receptor + LOX + AHP1) should recapitulate >50% of the germination improvement phenotype. Adding TPS-targeting siRNA should increase the effect further.

---

## Model 3: The Multi-Layered Immune Suppression and Resource Reallocation Model — Defense-Growth Tradeoff as the Primary Axis

**Core hypothesis**: The bacterial exRNAs primarily function as an immune evasion strategy that evolved to suppress host defense responses; the germination improvement is a *secondary consequence* of the massive resource reallocation from defense to growth, combined with the removal of defense-mediated growth inhibition.

**Causal chain**:

1. **Entry and evolutionary context**: The bacterial exRNAs evolved as virulence/colonization factors to suppress plant immunity and establish a favorable niche on the seed surface or in the spermosphere. The germination-promoting effect is an emergent, possibly coincidental benefit of immune suppression. [SPECULATIVE but consistent with cross-kingdom RNAi in pathogenic fungi — Weiberg et al., 2013; and with the observation that many PGPR suppress plant immunity to colonize roots — Zamioudis & Pieterse, 2012, *Molecular Plant-Microbe Interactions*]

2. **Primary targets — Direct suppression of the immune signaling network**:
   - **SOV3g043450.1 and SOV6g048760.1 (two EDR2 paralogs)** are silenced → In Arabidopsis, EDR2 is a negative regulator of SA-mediated defense and programmed cell death [KNOWN — Vorwerk et al., 2007, *Plant Journal*]. Loss of EDR2 *enhances* disease resistance. However, this enhanced resistance comes at a severe growth cost: *edr2* mutants show spontaneous lesion formation and constitutive defense activation [KNOWN]. The paradox: why would the bacterium silence a *negative* regulator of defense? **Resolution**: In the seed context, EDR2 may function differently than in leaves. EDR2 contains a PH domain and a START lipid-transfer domain and localizes to the ER and plasma membrane [KNOWN]. It may regulate lipid signaling and vesicle trafficking during germination. Alternatively, the exRNAs may target EDR2 to prevent the seed from mounting an *excessive* defense response that would include programmed cell death of the endosperm — a process that must be tightly controlled for germination [INFERRED]. A third possibility: EDR2 downregulation in seeds does not trigger the compensatory SA burst seen in mature leaves because the SA biosynthetic machinery is not fully active in dry/imbibing seeds [SPECULATIVE].
   - **SOV5g005530.1 (MOS1-like immune regulator)** is silenced → MOS1 (Modifier of SNC1) in Arabidopsis is required for proper R-gene expression and NB-LRR protein stability [KNOWN — Li et al., 2010, *Plant Cell*]. Loss of MOS1 reduces the accumulation of functional R-proteins → reduced capacity for effector-triggered immunity (ETI) [KNOWN]. This directly benefits the bacterium by preventing recognition.
   - **SOV1g021670.1 (Putative disease resistance R-protein)** is silenced → direct elimination of a specific pathogen recognition receptor [INFERRED]
   - **SOV3g021300.1 (NST1 stress response protein)** is silenced → NST1 in yeast and plants is associated with cell death and stress granule formation [INFERRED]. Downregulation prevents stress-induced growth arrest.

3. **Amplification through signaling network suppression**:
   - **SOV1g027650.1 and SOV4g000660.1 (Receptor-like kinases)** are silenced → reduced PAMP perception at the cell surface → dampened pattern-triggered immunity (PTI) [INFERRED — many RLKs function as co-receptors in PTI; e.g., BAK1, CERK1]
   - **SOV1g020340.1 (MYB TF)** and **SOV2g014810.1 (NAC TF)** are silenced → these transcription factor families include major regulators of defense gene expression. MYB TFs regulate phenylpropanoid biosynthesis (lignification, flavonoid defense compounds); NAC TFs regulate programmed cell death and secondary wall biosynthesis [KNOWN for families; INFERRED for these specific members]. Their loss prevents transcriptional amplification of the defense response.
   - **SOV3g033920.1 (PP2A regulatory subunit A)** is silenced → PP2A complexes are critical regulators of both defense and ABA signaling. In Arabidopsis, PP2A dephosphorylates and activates SnRK2 kinases in the ABA pathway [KNOWN — Waadt et al., 2015, *Plant Cell*]. Loss of PP2A regulatory subunit disrupts PP2A complex assembly → reduced ABA signal transduction. PP2A also regulates defense signaling through dephosphorylation of MAPK cascade components [KNOWN]. This node is a **convergence point** linking defense suppression to ABA pathway attenuation.

4. **Resource reallocation — The growth dividend of immune suppression**:
   - Defense suppression liberates substantial metabolic resources. In Arabidopsis, constitutive defense activation (e.g., in autoimmune mutants like *snc1*) reduces growth by 30–60% [KNOWN — Huot et al., 2014, *Annual Review of Plant Biology*]. The converse — defense suppression — should release equivalent resources.
   - **SOV3g035520.1 (LOX)** silencing reduces JA biosynthesis → JA is both a defense hormone and a metabolically expensive pathway (consumes membrane lipids as substrates) [KNOWN]. LOX silencing simultaneously suppresses defense and conserves lipid reserves for β-oxidation and energy production [INFERRED].
   - **SOV2g009230.1 (TPS)** silencing reduces T6P → activates SnRK1 → promotes catabolic mobilization of stored reserves [KNOWN mechanism; INFERRED application]. The metabolic "starvation signal" redirects carbon flux from defense-associated secondary metabolism to primary growth metabolism.
   - **SOV4g000330.1 (Phytoene synthase)** silencing reduces carotenoid biosynthesis → conserves isoprenoid precursors (GGPP, IPP) that would otherwise be diverted from GA biosynthesis (which shares the same precursor pool) [INFERRED — GA and carotenoids compete for GGPP; Rodríguez-Villalón et al., 2009, *Plant Cell*]. This is a direct metabolic link between defense compound reduction and GA pathway enhancement.
   - **SOV1g048270.1 (Aspartokinase)** silencing reduces flux into the aspartate-derived amino acid pathway (Thr, Met, Lys, Ile) → may redirect nitrogen toward other amino acids needed for storage protein mobilization and de novo protein synthesis during germination [SPECULATIVE]

5. **Epigenetic and cell wall changes as tertiary consequences**:
   - The defense-to-growth metabolic shift alters the substrate availability for chromatin modifications (e.g., S-adenosylmethionine for DNA/histone methylation depends on Met biosynthesis, which is being redirected) [SPECULATIVE]
   - Cell wall remodeling genes (SOV4g010600.1, SOV1g033840.1, SOV4g051070.1) are downregulated because defense-associated cell wall reinforcement (callose deposition, lignification) is no longer being actively maintained [INFERRED]
   - The ROS scavenging reduction (peroxidase, GST downregulation) is a direct consequence of reduced defense activation: these enzymes are typically induced by SA/JA signaling, which is now suppressed [INFERRED]

6. **Net phenotypic outcome**: Germination improves because the seed's default "high-alert" immune posture is dismantled, releasing 30–50% of metabolic capacity [SPECULATIVE estimate based on Arabidopsis autoimmune mutant growth penalties] for embryo growth, cell wall loosening, and reserve mobilization. The hormonal shift toward GA dominance is a secondary consequence of resource reallocation (more GGPP for GA) and removal of JA/ABA defense-associated signaling.

**Supporting evidence**:
- The growth-defense tradeoff is one of the most robustly documented principles in plant biology [KNOWN — Züst & Agrawal, 2017, *Annual Review of Plant Biology*]
- Bacterial PGPR are known to suppress host immunity as part of their colonization strategy (e.g., via ISR modulation, effector secretion) [KNOWN — Pieterse et al., 2014, *Annual Review of Phytopathology*]
- Cross-kingdom sRNAs from *Botrytis cinerea* specifically target host immunity genes [KNOWN — Weiberg et al., 2013]
- The target set is enriched for immune regulators (EDR2 ×2, MOS1, R-protein, NST1, 2 RLKs, MYB, NAC) — this is a disproportionate representation relative to the ~110 total targets [INFERRED]
- Phytoene synthase downregulation directly links defense metabolite reduction to GA precursor availability [INFERRED but biochemically sound]
- Seeds treated with defense-suppressing compounds (e.g., SA biosynthesis inhibitors) show improved germination under stress conditions [KNOWN in some systems]

**Weaknesses**:
- This model positions the bacterium's evolutionary "intent" as immune evasion, with germination improvement as a side effect. However, if the bacterium is a genuine PGPR (plant growth-promoting rhizobacterium), the germination benefit may be under positive selection, not merely coincidental. The evolutionary framing is unfalsifiable without population genomic data on the bacterial exRNA loci.
- The model underexplains the targeting of DNA repair/replication checkpoint genes (ATR, polymerases, topoisomerase). These are not obviously related to defense suppression or resource reallocation.
- The quantitative claim that defense suppression releases "30–50% of metabolic capacity" is extrapolated from mature plant autoimmune phenotypes. Seeds have a fundamentally different metabolic architecture (heterotrophic, relying on stored reserves), and the defense cost in seeds is unquantified [SPECULATIVE].
- The EDR2 paradox (silencing a negative regulator of defense should *increase* defense) remains incompletely resolved. The seed-specific function of EDR2 is unknown.
- **Confounder**: Bacterial EPS polysaccharides are themselves known immune elicitors (e.g., activating PTI through perception as PAMPs) [KNOWN — Newman et al., 2013, *Plant Cell*]. The exRNA-mediated immune suppression may be *necessary* to counteract the immune activation caused by the EPS itself. In this case, the net immune effect of the treatment (EPS + exRNA) might be neutral, and the germination benefit would derive entirely from EPS osmopriming. This is a devastating confounder for this model.

**Testable predictions**:
1. **Defense gene expression profiling**: RT-qPCR or RNA-seq of canonical defense markers (PR1, PR2, PDF1.2, LOX2 equivalents in spinach) should show reduced expression in exRNA-treated seeds. If defense markers are *elevated* (due to EPS elicitation), this model is weakened.
2. **EPS-only vs. EPS+exRNA factorial experiment**: Compare (a) intact bacterial EPS with exRNAs, (b) RNase-treated EPS (exRNA-depleted), (c) purified exRNAs without EPS, (d) buffer control. If Model 3 is correct, treatment (c) should suppress defense markers but provide minimal germination benefit (no osmopriming), while treatment (a) should show both defense suppression and germination improvement.
3. **Metabolic flux analysis**: ¹³C-glucose labeling of imbibing seeds should show that exRNA-treated seeds redirect more carbon toward primary metabolism (glycolysis, TCA cycle) and less toward phenylpropanoid/flavonoid pathways compared to controls.
4. **Phytoene synthase complementation**: Overexpression of SOV4g000330.1 (phytoene synthase) in exRNA-treated seeds should partially reverse the germination benefit by competing for GGPP with GA biosynthesis.
5. **SA/JA quantification**: Direct measurement of SA, JA, and JA-Ile should show reduced levels in exRNA-treated seeds. If levels are unchanged or elevated, the defense suppression model is falsified.
6. **Immune-compromised seed test**: If spinach seeds are pre-treated with an SA biosynthesis inhibitor (e.g., 1-aminobenzotriazole) AND the bacterial exRNAs, the germination improvement should not be significantly greater than exRNA alone (epistasis), confirming that defense suppression is the shared mechanism.

---

## Model Comparison Table

| Feature | Model 1: Epigenetic Master Switch | Model 2: Hormonal Checkpoint Collapse | Model 3: Immune Suppression & Resource Reallocation |
|---------|----------------------------------|--------------------------------------|---------------------------------------------------|
| **Primary targets** | 6 epigenetic regulators (SOV1g033340.1, SOV4g015450.1, SOV6g036290.1, SOV4g030590.1, SOV4g038060.1, SOV0g001060.1) | 4 hormone nodes (SOV3g000150.1, SOV3g035520.1, SOV4g032870.1, SOV2g009230.1) | 9+ defense/signaling genes (EDR2 ×2, MOS1, R-protein, NST1, RLK ×2, MYB, NAC) |
| **Targets directly explained** | ~25 (epigenetic + downstream hormone/defense as secondary) | ~40 (hormone targets + defense/metabolic as downstream) | ~35 (defense + metabolic reallocation targets) |
| **Targets poorly explained** | DNA repair/replication (6 genes), transport (18 genes) | Epigenetic coherence (6 genes specifically targeted), transposon genes (5) | DNA repair/replication (6 genes), epigenetic specificity (6 genes) |
| **Mechanism complexity** | High — requires TGS or passive demethylation across multiple loci | Moderate — 3-4 direct PTGS events cascade through known hormone networks | Moderate-High — many direct targets but relies on quantitative resource reallocation |
| **Temporal kinetics** | Slow (hours to days for epigenetic changes) | Fast (minutes to hours for receptor silencing and hormone shifts) | Intermediate (hours for defense gene suppression; days for metabolic reallocation) |
| **Evolutionary logic** | Mutualistic: bacterium provides epigenetic "wake-up" signal | Mutualistic: bacterium provides hormonal "all-clear" signal | Potentially parasitic/commensal: immune evasion with coincidental growth benefit |
| **EPS confounder vulnerability** | High — osmopriming alters DNA methylation independently | Moderate — osmopriming affects ABA but not ethylene receptor levels | Very High — EPS elicits immunity, potentially canceling exRNA-mediated suppression |
| **Key testable prediction** | Bisulfite-seq shows targeted demethylation at germination loci | Hormone quantification shows rapid ABA decline + JA reduction | Defense marker suppression + metabolic flux redirection |
| **Falsification criterion** | No methylation changes at germination gene promoters | No change in ABA/JA/ethylene levels within 24h | Defense markers elevated (not suppressed) in treated seeds |
| **Overall plausibility** | ★★★☆☆ (coherent but temporally problematic) | ★★★★☆ (best kinetic fit, strongest single-gene evidence) | ★★★☆☆ (strong conceptual framework but major confounder issues) |

---

## Recommended Model

### **Model 2 (Hormonal Checkpoint Collapse) is the best-supported primary model, with elements of Models 1 and 3 operating as reinforcing secondary mechanisms.**

**Rationale**:

1. **Kinetic fit**: Germination improvement requires effects within hours of imbibition. Hormone receptor silencing via PTGS (mRNA degradation) can alter signaling within 2–6 hours, matching the expected kinetics. Epigenetic reprogramming (Model 1) requires DNA replication cycles and is too slow to be the primary driver, though it likely contributes to sustained effects and seedling vigor post-germination. [INFERRED]

2. **Genetic evidence strength**: The ethylene receptor is the single best-characterized germination regulator in the target set. Loss-of-function of ethylene receptors in Arabidopsis is *sufficient* to promote germination [KNOWN]. No other single target in the set has equally strong genetic evidence for a germination phenotype. This makes it the most parsimonious primary mechanism.

3. **Pathway coherence**: The four primary targets of Model 2 (ethylene receptor, LOX, AHP1, TPS) converge on ABA pathway suppression through four independent mechanisms (ethylene antagonism, JA removal, phosphorelay disruption, SnRK1 activation). This multi-pronged convergence on a single output (ABA decline) is a hallmark of robust biological regulation and is consistent with the "multiple brakes released simultaneously" architecture described in the ranked target analysis. [INFERRED]

4. **Confounder resilience**: Model 2 is moderately resistant to the EPS confounder. While EPS osmopriming can reduce ABA levels, it cannot explain the specific downregulation of the ethylene receptor or LOX. RNase-treated EPS controls should cleanly separate these effects. [INFERRED]

5. **Integrative synthesis**: The recommended working model is a **temporal hierarchy**:
   - **Phase 1 (0–6 hours)**: exRNA-mediated PTGS silences hormone signaling nodes (Model 2 targets) → rapid ABA decline, ethylene activation, JA suppression → hormonal "green light" for germination [Model 2 primary]
   - **Phase 1b (0–6 hours, parallel)**: exRNA-mediated PTGS silences defense pathway components (Model 3 targets) → reduced metabolic drain, resource reallocation to growth [Model 3 as parallel reinforcement]
   - **Phase 2 (6–24 hours)**: Hormone-driven and exRNA-directed suppression of epigenetic repressors (Model 1 targets) → chromatin opening at germination loci → sustained transcriptional activation of GA-responsive genes, cell wall hydrolases, reserve mobilization enzymes [Model 1 as secondary amplifier]
   - **Phase 3 (24–72 hours)**: Full germination program execution — endosperm weakening, radicle protrusion, reserve mobilization, seedling establishment — driven by the combined hormonal, epigenetic, and metabolic reprogramming [All models converge]

6. **Critical experiment to distinguish models**: A **time-course experiment** measuring (a) target mRNA levels by RT-qPCR, (b) hormone levels by LC-MS/MS, (c) DNA methylation by methylation-sensitive restriction + qPCR, and (d) defense marker expression, at 2, 6, 12, 24, and 48 hours post-imbibition, in exRNA-treated vs. RNase-treated EPS vs. buffer controls, would definitively establish the temporal hierarchy and identify the primary causal mechanism. If hormone changes precede epigenetic changes, Model 2 is supported as primary. If epigenetic changes precede or co-occur with hormone changes, Model 1 gains support. If defense suppression is the earliest and largest-magnitude change, Model 3 is supported.

> **Final caveat** [CRITICAL]: All three models assume that the observed target downregulation is genuinely caused by bacterial exRNA-mediated PTGS/TGS. The alternative null hypothesis — that germination improvement is entirely due to EPS osmopriming, with the transcriptomic changes being a secondary physiological response to improved hydration rather than a cause of it — has not been excluded. The RNase-treated EPS control is the single most important experiment to perform before investing in mechanistic dissection of any model.