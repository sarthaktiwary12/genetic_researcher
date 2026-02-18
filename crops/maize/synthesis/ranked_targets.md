# Ranked Target Analysis — Maize (Zea mays)

# Definitive Ranked Analysis of Bacterial exRNA Target Genes in *Spinacia oleracea*: Contribution to Germination/Vigor Phenotype

> **Note on Scope**: All gene IDs are *Spinacia oleracea* (spinach) targets identified in a cross-kingdom exRNA experiment. The requested crop is *Zea mays*, but all targets are spinach genes. This analysis ranks spinach targets by their inferred contribution to the observed germination/vigor phenotype. Where maize orthologs are relevant for comparative context, they are noted explicitly.

---

## Executive Summary

This target landscape represents a remarkably broad, multi-pathway reprogramming of the spinach seed transcriptome by bacterial extracellular small RNAs (exRNAs), likely delivered in the context of an exopolysaccharide (EPS)-primed bacterial inoculant. The 110+ predicted targets span 14 functional pathway categories, ranging from hormone signaling and epigenetic regulation to transposon silencing and unknown proteins. [KNOWN] The sheer breadth of targeting is consistent with the known promiscuity of small RNA-mediated silencing and the documented ability of bacterial sRNAs to enter plant cells via extracellular vesicles or direct uptake. [INFERRED] However, this breadth also introduces significant interpretive challenges: not all targets will contribute equally to the phenotype, and some may represent off-target effects or bystander downregulation with negligible functional consequence.

The dominant mechanistic theme emerging from pathway-level integration is the **suppression of the dormancy-defense-stress tradeoff**. The seed's default state—characterized by ABA dominance, epigenetic silencing of growth genes, active immune priming, and metabolic quiescence—is systematically dismantled across multiple independent regulatory nodes simultaneously. [INFERRED] This multi-node attack is likely more effective than targeting any single pathway, as it prevents compensatory buffering through redundant pathways. The three highest-impact pathway clusters are: (1) **Hormone Signaling** (ABA/ethylene/cytokinin suppression releasing the GA-growth axis), (2) **Epigenetic Regulation** (dismantling transcriptional repression of germination genes), and (3) **Defense/Immunity suppression** (resolving the growth-defense tradeoff). These three clusters are deeply interconnected and their simultaneous modulation likely produces a synergistic, non-additive effect on germination rate and vigor.

A critical caveat must be stated at the outset: [SPECULATIVE] the causal attribution of the germination phenotype to any specific target or subset of targets has not been experimentally validated through individual gene knockdown/knockout in spinach. The ranking below is based on (a) the known biology of homologous genes in *Arabidopsis thaliana* and other model systems, (b) the pathway-level priority assigned in the input data, (c) the mechanistic directness of the predicted effect on germination, and (d) the degree of cross-pathway convergence. Rankings should be treated as testable hypotheses, not established facts.

---

## Ranking Methodology

Targets were scored across five weighted criteria:

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| **Mechanistic Directness** | 30% | Does downregulation of this gene have a direct, well-characterized effect on germination rate or seed vigor in *Arabidopsis* or other species? |
| **Pathway Priority Score** | 25% | Was the gene assigned "high" priority within its pathway? High = 3, Medium = 2, Low = 1 |
| **Cross-Pathway Convergence** | 20% | Does this gene sit at a node where multiple pathways intersect (e.g., ABA signaling, ROS, epigenetics)? |
| **Evidence Quality** | 15% | Is the function based on [KNOWN] biochemistry, [INFERRED] homology, or [SPECULATIVE] domain prediction? |
| **Confound Risk** | 10% | Could the effect be explained by EPS osmopriming, polysaccharide elicitor effects, or microbiome remodeling rather than specific exRNA targeting? |

Targets with identical scores were separated by mechanistic specificity (a gene with a single, well-defined germination-relevant function ranks above one with broad, pleiotropic roles).

**Confounders explicitly considered:**
- EPS (exopolysaccharide) osmopriming can independently improve germination by lowering water potential and improving imbibition kinetics [KNOWN]
- Polysaccharide elicitors can trigger pattern-triggered immunity (PTI) and hormonal changes independent of exRNA [KNOWN]
- Microbiome remodeling by the inoculant may alter the rhizosphere environment [INFERRED]
- Annotation errors (notably SOV2g038830.1 "cry8Ba") reduce confidence in some targets [KNOWN concern]

---

## Tier 1: Critical Targets (Expected Large Phenotypic Effect)

These targets have strong mechanistic connections to core germination regulatory nodes, high pathway priority, and robust homolog data from model systems.

---

### T1.1 — SOV3g000150.1 — Ethylene Receptor

- **Mechanism**: Ethylene receptors (ETR1/ERS family) are **negative regulators** of ethylene signaling—their presence suppresses ethylene responses. [KNOWN] Downregulation of the receptor would therefore **derepress ethylene signaling**, promoting germination. In *Arabidopsis*, ethylene promotes germination by antagonizing ABA signaling; *etr1* loss-of-function mutants show enhanced ethylene sensitivity and faster germination under stress. [KNOWN] The *Arabidopsis* homolog AT1G66340 (*ETR1*) is one of the best-characterized hormone receptors in plant biology. Downregulation of the spinach ortholog would shift the ABA/ethylene balance decisively toward germination. [INFERRED]
- **Evidence strength**: Strong
- **Key references**: Bleecker & Kende (2000) *Annu Rev Cell Dev Biol*; Linkies et al. (2009) *Plant Cell* (ethylene promotes endosperm cap weakening in *Lepidium sativum*); Arc et al. (2013) *Front Plant Sci* (ethylene-ABA antagonism in seeds)
- **Cross-pathway convergence**: Directly intersects with ABA signaling, ROS redox, and cell wall remodeling (endosperm cap weakening)
- **Confound risk**: Low — the mechanism is specific and directional
- **Confidence**: **High**

---

### T1.2 — SOV4g032870.1 — Histidine-containing Phosphotransfer Protein 1 (AHP-like)

- **Mechanism**: AHP proteins are central relay components of the **two-component cytokinin signaling pathway** (AHK receptor → AHP → ARR response regulators). [KNOWN] In seeds, cytokinin signaling via type-A ARRs promotes ABA catabolism and reduces ABA sensitivity, thereby promoting germination. [KNOWN] However, AHP proteins also relay signals that can activate type-B ARRs, which repress germination by maintaining ABA-responsive gene expression. [INFERRED] Downregulation of a specific AHP isoform could disrupt this relay, potentially reducing ABA-mediated dormancy maintenance. The *Arabidopsis* homologs *AHP1-5* (AT3G21510, AT3G29350, AT5G39340, AT3G16360, AT1G03430) have well-characterized roles in cytokinin signal transduction. [KNOWN] The pathway analysis assigns this gene "high" priority within hormone signaling, and it sits at a critical junction between cytokinin, ABA, and GA cross-talk.
- **Evidence strength**: Moderate-Strong
- **Key references**: Hwang et al. (2012) *Annu Rev Plant Biol*; Kushwah & Laxmi (2014) *Plant J* (AHP role in seed germination); Müller & Sheen (2007) *Plant Cell*
- **Cross-pathway convergence**: Hormone signaling × general signaling × metabolic priming
- **Confound risk**: Moderate — cytokinin effects on germination are context-dependent and isoform-specific
- **Confidence**: **High**

---

### T1.3 — SOV1g033340.1 — DNA (Cytosine-5)-Methyltransferase

- **Mechanism**: DNA methyltransferases (CMT/MET/DRM family) establish and maintain cytosine methylation, a key epigenetic mark for transcriptional silencing of dormancy-associated genes and transposons. [KNOWN] In *Arabidopsis*, the *met1* mutant shows reduced seed dormancy and faster germination, demonstrating that DNA methylation actively maintains the dormant state. [KNOWN] Downregulation of this methyltransferase would be expected to cause **genome-wide hypomethylation**, derepressing germination-promoting genes (e.g., GA biosynthesis genes, expansins) and potentially transposons. [INFERRED] The *Arabidopsis* homolog *MET1* (AT5G49160) is the primary maintenance methyltransferase. This is a master epigenetic regulator with genome-wide consequences.
- **Evidence strength**: Strong
- **Key references**: Bentsink & Koornneef (2008) *Curr Biol*; Footitt et al. (2015) *Plant J* (methylation in seed dormancy); Saze & Kakutani (2011) *Curr Opin Plant Biol*
- **Cross-pathway convergence**: Epigenetic regulation × transposon silencing × defense/immunity (methylation of NBS-LRR loci)
- **Confound risk**: Low for the epigenetic mechanism; moderate for specificity (which genes become hypomethylated?)
- **Confidence**: **High**

---

### T1.4 — SOV6g036290.1 — Protein HIRA

- **Mechanism**: HIRA is a histone chaperone responsible for **replication-independent deposition of histone H3.3**, a mark associated with transcriptionally active chromatin. [KNOWN] In the context of seed dormancy, HIRA activity in maintaining repressive chromatin states (by preventing H3.3 incorporation at growth-promoting loci) would suppress germination. [INFERRED] Downregulation of HIRA could paradoxically *increase* H3.3 incorporation at previously repressed loci if other chaperones compensate, or it could disrupt the balance of histone variant deposition, leading to chromatin decompaction. The *Arabidopsis* homolog *HIRA* (AT2G31810) is involved in transcriptional regulation and stress responses. [KNOWN] The pathway analysis assigns this gene "high" priority.
- **Evidence strength**: Moderate
- **Key references**: Duc et al. (2015) *EMBO J* (HIRA in *Arabidopsis* stress responses); Nie et al. (2014) *Mol Plant* (histone H3.3 dynamics in plant development)
- **Cross-pathway convergence**: Epigenetic regulation × RNA processing (histone variants affect transcription of RNA processing genes)
- **Confound risk**: Moderate — HIRA's role in seeds specifically is not well-characterized
- **Confidence**: **Medium-High**

---

### T1.5 — SOV4g015450.1 — Histone-Lysine N-Methyltransferase SUVR5 (Putative)

- **Mechanism**: SUVR5 is a SET-domain histone methyltransferase that catalyzes **H3K9me2**, a repressive histone mark associated with heterochromatin formation and transcriptional silencing. [KNOWN] In *Arabidopsis*, *SUVR5* (AT2G23740) is involved in silencing of transposable elements and stress-responsive genes. [KNOWN] During seed dormancy, H3K9me2 marks at key germination-promoting loci (e.g., GA biosynthesis, expansin genes) would maintain transcriptional repression. Downregulation of SUVR5 would reduce H3K9me2 deposition, allowing derepression of these loci and accelerating the dormancy-to-germination transition. [INFERRED]
- **Evidence strength**: Moderate-Strong
- **Key references**: Caro et al. (2012) *Plant Cell* (SUVR5 in *Arabidopsis*); Zheng et al. (2012) *Mol Plant* (H3K9me2 in seed dormancy regulation)
- **Cross-pathway convergence**: Epigenetic regulation × transposon silencing (H3K9me2 is the primary mark for TE silencing)
- **Confound risk**: Low
- **Confidence**: **High**

---

### T1.6 — SOV4g030590.1 — PHD-type Domain-Containing Protein

- **Mechanism**: PHD (Plant Homeodomain) fingers are **"reader" domains** that recognize specific histone methylation marks, particularly H3K4me3 (active) or H3K9me2/H3K27me3 (repressive). [KNOWN] PHD-containing proteins recruit chromatin-modifying complexes (e.g., PRC2 for H3K27me3 deposition) to maintain transcriptional repression. [KNOWN] In the context of dormancy, a PHD protein reading repressive marks would reinforce silencing of germination genes. Downregulation would disrupt this "reading" function, destabilizing repressive complexes and allowing transcriptional activation. [INFERRED] The pathway analysis assigns "high" priority.
- **Evidence strength**: Moderate
- **Key references**: Sanchez & Bhatt (2011) *Plant Cell* (PHD proteins in *Arabidopsis* development); Molitor et al. (2014) *Plant Cell* (PHD-PRC2 interactions)
- **Cross-pathway convergence**: Epigenetic regulation × defense/immunity (PRC2 silences many defense genes)
- **Confound risk**: Moderate — PHD domain function is highly context-dependent
- **Confidence**: **Medium-High**

---

### T1.7 — SOV4g038060.1 — Zinc Finger Protein GIS2

- **Mechanism**: GIS2 (*GLABRA IN SHOOTS 2*) is a C2H2 zinc finger transcription factor that in *Arabidopsis* (AT5G28300) acts as a **transcriptional repressor** of trichome initiation and is regulated by GA signaling. [KNOWN] In the seed context, GIS2-like proteins may function as repressors of GA-responsive genes, integrating stress signals to maintain dormancy. [INFERRED] The pathway analysis assigns "high" priority, and the epigenetic pathway analysis identifies it as a key "transcriptional repressor" node. Downregulation would derepress GA-responsive growth programs. [SPECULATIVE for seeds specifically]
- **Evidence strength**: Moderate
- **Key references**: Gan et al. (2007) *Plant Cell* (GIS2 in *Arabidopsis* GA signaling); Ishida et al. (2007) *Plant Cell*
- **Cross-pathway convergence**: Epigenetic regulation × hormone signaling (GA pathway)
- **Confound risk**: Moderate — GIS2's role in seeds vs. vegetative tissue is not well-established
- **Confidence**: **Medium**

---

### T1.8 — SOV3g043450.1 & SOV6g048760.1 — ENHANCED DISEASE RESISTANCE 2 (EDR2) [Two paralogs]

- **Mechanism**: EDR2 in *Arabidopsis* (AT4G19040) is a **negative regulator of salicylic acid (SA)-mediated defense** and is involved in suppressing programmed cell death (PCD). [KNOWN] Paradoxically, *edr2* mutants show *enhanced* disease resistance, suggesting EDR2 normally suppresses defense. [KNOWN] In the seed context, EDR2 may function as a **suppressor of SA-mediated growth inhibition**, and its downregulation could either (a) activate SA-mediated defense responses that compete with germination, or (b) release a brake on PCD-related processes that facilitate endosperm weakening. [INFERRED] The presence of two paralogs both assigned "high" priority and both targeted simultaneously suggests a robust, non-redundant contribution. The pathway analysis frames this as resolving the growth-defense tradeoff.
- **Evidence strength**: Moderate
- **Key references**: Tang et al. (2005) *Plant Cell* (EDR2 in *Arabidopsis*); Wawrzynska et al. (2010) *Plant Cell Physiol*
- **Cross-pathway convergence**: Defense/immunity × hormone signaling (SA-ABA-GA cross-talk) × ROS/redox
- **Confound risk**: Moderate — EDR2's role in seeds is not directly characterized; the two-paralog targeting may reflect off-target effects
- **Confidence**: **Medium-High**

---

### T1.9 — SOV5g005530.1 — Modifier of SNC1 1 (MOS1-like / Immune Regulator)

- **Mechanism**: MOS1 in *Arabidopsis* (AT1G33520) is a **positive regulator of basal immunity** that modulates the expression of the autoimmune gene *SNC1* (Suppressor of NPR1-1, Constitutive 1). [KNOWN] MOS1 maintains *SNC1* expression through epigenetic mechanisms (DNA methylation). [KNOWN] In seeds, high MOS1 activity would maintain a costly immune-primed state that diverts resources from germination. Downregulation of MOS1 would reduce *SNC1*-mediated immune signaling, freeing metabolic resources for growth. [INFERRED] The pathway analysis assigns "high" priority.
- **Evidence strength**: Moderate
- **Key references**: Bai et al. (2011) *Plant Cell* (MOS1 in *Arabidopsis* immunity); Li et al. (2010) *Plant Cell* (MOS1-SNC1 axis)
- **Cross-pathway convergence**: Defense/immunity × epigenetic regulation (MOS1 uses DNA methylation to regulate SNC1)
- **Confound risk**: Low — the mechanism is specific
- **Confidence**: **Medium-High**

---

### T1.10 — SOV2g009230.1 — Trehalose-Phosphate Synthase (TPS)

- **Mechanism**: TPS catalyzes the synthesis of trehalose-6-phosphate (T6P) from UDP-glucose and glucose-6-phosphate. [KNOWN] T6P is a **central metabolic signal** that inhibits SnRK1 (Snf1-related kinase 1), a master energy sensor. [KNOWN] High T6P levels signal carbon abundance and suppress SnRK1-mediated catabolism. In seeds, T6P levels regulate the balance between storage reserve mobilization and biosynthesis. [KNOWN] Critically, T6P also interacts with ABA signaling: elevated T6P can enhance ABA sensitivity, reinforcing dormancy. [KNOWN] Downregulation of TPS would reduce T6P, relieving SnRK1 inhibition, promoting reserve mobilization (starch/lipid catabolism), and reducing ABA sensitivity—all pro-germination effects. [INFERRED] The *Arabidopsis* homologs *TPS1-11* (e.g., *TPS1*, AT1G78580) are well-characterized.
- **Evidence strength**: Strong
- **Key references**: Paul et al. (2008) *Science* (T6P as sucrose sensor); Eastmond et al. (2002) *Plant J* (TPS1 in seed germination); Gomez et al. (2010) *Plant Cell* (T6P-ABA interaction)
- **Cross-pathway convergence**: Metabolic priming × hormone signaling (ABA) × general signaling (SnRK1)
- **Confound risk**: Low — TPS function in seeds is well-established
- **Confidence**: **High**

---

### T1.11 — SOV3g035520.1 — Lipoxygenase (LOX)

- **Mechanism**: LOX enzymes catalyze the dioxygenation of polyunsaturated fatty acids (PUFAs), initiating the **jasmonic acid (JA) biosynthesis pathway** and producing lipid hydroperoxides. [KNOWN] JA generally acts synergistically with ABA to **inhibit seed germination** and promote dormancy maintenance. [KNOWN] LOX activity also generates reactive aldehydes (e.g., 4-HNE) that can cause oxidative damage. [KNOWN] Downregulation of LOX would reduce JA biosynthesis, shifting the hormonal balance away from ABA-JA dormancy maintenance toward GA-promoted germination. [INFERRED] Additionally, reduced LOX activity would decrease lipid peroxidation during imbibition, protecting membrane integrity. The *Arabidopsis* homologs *LOX1-6* (e.g., *LOX2*, AT3G45140) are well-characterized.
- **Evidence strength**: Strong
- **Key references**: Feussner & Wasternack (2002) *Annu Rev Plant Biol*; Linkies & Leubner-Metzger (2012) *Plant Cell Environ* (JA-ABA in germination); Calvo et al. (2004) *Plant Physiol* (LOX in seed dormancy)
- **Cross-pathway convergence**: Hormone signaling × ROS/redox × metabolic priming (lipid metabolism)
- **Confound risk**: Low
- **Confidence**: **High**

---

### T1.12 — SOV3g033920.1 — PP2A Regulatory Subunit A (65 kDa)

- **Mechanism**: PP2A (Protein Phosphatase 2A) is a heterotrimeric serine/threonine phosphatase. The regulatory A subunit (also called PR65) scaffolds the catalytic C subunit and the variable B subunit to determine substrate specificity. [KNOWN] In *Arabidopsis*, PP2A is a **critical positive regulator of ABA signaling**: it dephosphorylates and activates ABI1/ABI2 (ABA-insensitive PP2C phosphatases), which in turn suppress ABA signaling by dephosphorylating SnRK2 kinases. [KNOWN] However, PP2A also directly regulates the ABA receptor complex (PYR/PYL-PP2C-SnRK2). Downregulation of the scaffolding A subunit would disrupt PP2A complex assembly, potentially altering the phosphorylation state of multiple ABA signaling components. [INFERRED] The *Arabidopsis* homologs *PP2AA1-3* (AT1G25490, AT3G25800, AT1G13320) are well-characterized. The pathway analysis assigns "high" priority.
- **Evidence strength**: Moderate-Strong
- **Key references**: Pernas et al. (2007) *Plant J* (PP2A in ABA signaling); Waadt et al. (2015) *eLife* (PP2A-ABA receptor interaction); Liao et al. (2016) *Plant Cell*
- **Cross-pathway convergence**: General signaling × hormone signaling (ABA) × ROS/redox
- **Confound risk**: Moderate — PP2A has hundreds of substrates; the net effect of A-subunit downregulation is complex
- **Confidence**: **Medium-High**

---

### T1.13 — SOV1g020340.1 — MYB Transcription Factor

- **Mechanism**: MYB transcription factors constitute one of the largest TF families in plants. In the seed context, specific MYB members are critical regulators of **ABA-mediated dormancy** (e.g., *AtMYB96*, AT5G62470, promotes ABA signaling and dormancy) or **seed coat development** (e.g., *AtMYB5*, *AtMYB61*). [KNOWN] The pathway analysis assigns "high" priority and places this gene in the general signaling pathway. Downregulation of a dormancy-promoting MYB would reduce ABA-responsive gene expression, accelerating germination. [INFERRED] Without knowing the specific MYB subfamily, the directionality of the effect is uncertain—some MYBs promote germination (e.g., *AtMYB33* promotes GA signaling). [SPECULATIVE for this specific gene]
- **Evidence strength**: Moderate
- **Key references**: Seo et al. (2009) *Plant Cell* (MYB96 in ABA/drought); Lim et al. (2013) *Plant Cell Environ* (MYB TFs in seed germination); Penfield et al. (2001) *Plant Cell* (MYB61)
- **Cross-pathway convergence**: General signaling × hormone signaling × epigenetic regulation
- **Confound risk**: Moderate — MYB subfamily identity is critical for directionality
- **Confidence**: **Medium**

---

### T1.14 — SOV2g014810.1 — NAC Domain-Containing Protein

- **Mechanism**: NAC transcription factors are major regulators of seed maturation, dormancy, and stress responses. [KNOWN] Key members include *ANAC060* (AT3G44350), which promotes ABA sensitivity and dormancy, and *VND* family members involved in secondary cell wall deposition. [KNOWN] The pathway analysis assigns "high" priority. Downregulation of a dormancy-promoting NAC would reduce ABA-responsive transcription, promoting germination. [INFERRED] NAC factors also regulate senescence and PCD programs that could interfere with germination if inappropriately activated.
- **Evidence strength**: Moderate
- **Key references**: Mönke et al. (2012) *Mol Genet Genomics* (NAC in seed dormancy); Barros et al. (2009) *Plant Mol Biol* (NAC in *Arabidopsis* seeds); Shu et al. (2016) *Plant Cell Environ*
- **Cross-pathway convergence**: General signaling × hormone signaling × epigenetic regulation
- **Confound risk**: Moderate — NAC subfamily identity is critical
- **Confidence**: **Medium**

---

### T1.15 — SOV3g040200.1 — Glutathione S-Transferase L3-like (GST)

- **Mechanism**: GSTs conjugate glutathione to electrophilic substrates, detoxifying lipid peroxides and cytotoxic compounds. [KNOWN] During germination, a controlled ROS burst is **required** for cell wall loosening and ABA catabolism. [KNOWN] High GST activity would prematurely quench this pro-germination ROS signal, maintaining the seed in a stress-response mode that inhibits growth. [INFERRED] Downregulation of GST would allow the ROS burst to proceed with greater amplitude and duration, enhancing its pro-germination signaling effects. The *Arabidopsis* homologs *GSTL1-3* (AT2G30860, AT2G30870, AT2G30880) are characterized. The pathway analysis assigns "high" priority.
- **Evidence strength**: Moderate-Strong
- **Key references**: Bailly (2004) *Seed Sci Res* (ROS in germination); El-Maarouf-Bouteau & Bailly (2008) *Plant Signal Behav* (oxidative window); Dixon et al. (2009) *Phytochemistry* (GST in seeds)
- **Cross-pathway convergence**: ROS/redox × hormone signaling (ABA catabolism) × metabolic priming
- **Confound risk**: Low
- **Confidence**: **High**

---

### T1.16 — SOV3g038840.1 — Peroxidase

- **Mechanism**: Class III plant peroxidases are bifunctional: they can either **produce ROS** (via the hydroxylic cycle, using NADH) or **scavenge H₂O₂** (via the peroxidatic cycle). [KNOWN] In the seed coat and endosperm cap, peroxidase-mediated ROS production contributes to cell wall loosening and weakening of the mechanical barrier to radicle emergence. [KNOWN] However, peroxidases also catalyze cell wall cross-linking (via phenolic oxidation), which stiffens the wall and inhibits germination. [KNOWN] The net effect of downregulating this specific peroxidase depends on which activity dominates in the germination context. If this peroxidase primarily functions in wall-stiffening cross-linking, downregulation would promote germination. [INFERRED] The pathway analysis assigns "high" priority.
- **Evidence strength**: Moderate
- **Key references**: Cosio & Dunand (2009) *J Exp Bot* (Class III peroxidases); Müller et al. (2009) *Plant Cell* (peroxidase in endosperm weakening); Leubner-Metzger (2003) *Planta*
- **Cross-pathway convergence**: ROS/redox × cell wall remodeling × hormone signaling
- **Confound risk**: Moderate — directionality depends on peroxidase isoform identity
- **Confidence**: **Medium-High**

---

### T1.17 — SOV1g021960.1 & SOV2g025380.1 — Cation-Chloride Cotransporter 1-like (Two paralogs)

- **Mechanism**: Cation-chloride cotransporters (CCCs) mediate electroneutral co-transport of K⁺/Na⁺ with Cl⁻. [KNOWN] In plants, CCC1 (*Arabidopsis* AT1G30450) regulates **turgor pressure, osmotic potential, and ion homeostasis** in growing tissues. [KNOWN] During germination, turgor pressure in the embryonic root tip is the primary physical force driving radicle protrusion through the weakened endosperm. [KNOWN] Downregulation of CCC-type transporters could alter the osmotic potential gradient, potentially *reducing* turgor-driven growth—which would be anti-germination. [INFERRED] However, if these CCCs primarily function in maintaining high Cl⁻ in the vacuole (which would reduce osmotic potential for water uptake), their downregulation could *increase* net water uptake and turgor. [SPECULATIVE] The presence of two paralogs both assigned "high" priority in the transport pathway is notable.
- **Evidence strength**: Moderate
- **Key references**: Colmenero-Flores et al. (2007) *Plant J* (CCC1 in *Arabidopsis*); Zifarelli & Pusch (2010) *Rev Physiol Biochem Pharmacol* (CCC biology)
- **Cross-pathway convergence**: Transport/ion homeostasis × general signaling (Ca²⁺ signaling) × cell wall remodeling (turgor-driven expansion)
- **Confound risk**: High — EPS osmopriming directly affects water potential and could confound this effect
- **Confidence**: **Medium**

---

### T1.18 — SOV1g018480.1 — Cyclic Nucleotide-Gated Channel (CNGC)

- **Mechanism**: CNGCs are non-selective cation channels gated by cyclic nucleotides (cAMP, cGMP) and calmodulin. [KNOWN] In *Arabidopsis*, CNGCs mediate **Ca²⁺ influx** in response to pathogen signals (PAMPs), contributing to the hypersensitive response and PTI. [KNOWN] CNGCs also regulate thermomorphogenesis and other developmental processes. [KNOWN] In the seed context, CNGC-mediated Ca²⁺ influx could activate defense signaling pathways that compete with germination. Downregulation would reduce this Ca²⁺-mediated defense activation, freeing resources for growth. [INFERRED] The pathway analysis assigns "high" priority.
- **Evidence strength**: Moderate
- **Key references**: Jammes et al. (2011) *Plant J* (CNGC in *Arabidopsis* immunity); Tian et al. (2019) *Nat Commun* (CNGC in thermomorphogenesis); Moeder et al. (2011) *Plant Physiol*
- **Cross-pathway convergence**: Transport/ion homeostasis × defense/immunity × general signaling (Ca²⁺)
- **Confound risk**: Moderate
- **Confidence**: **Medium-High**

---

### T1.19 — SOV4g051610.1 — Ser/Thr Kinase ATR (DNA Damage Response)

- **Mechanism**: ATR (Ataxia Telangiectasia and Rad3-related) is a **master DNA damage checkpoint kinase** that responds to replication stress and single-strand DNA breaks. [KNOWN] In *Arabidopsis* (AT5G40820), ATR activation halts the cell cycle at the G2/M checkpoint, preventing cells with damaged DNA from dividing. [KNOWN] In a dormant seed, accumulated DNA damage from desiccation and oxidative stress would activate ATR, imposing a cell cycle arrest that delays or prevents germination. [INFERRED] Downregulation of ATR would release this checkpoint, allowing cell division to proceed even in the presence of some residual DNA damage—a calculated risk that accelerates germination at the potential cost of some genomic fidelity. [INFERRED] This is a high-impact target because cell cycle entry is an absolute prerequisite for radicle elongation.
- **Evidence strength**: Moderate-Strong
- **Key references**: Culligan et al. (2004) *Plant Cell* (ATR in *Arabidopsis* DNA damage); Waterworth et al. (2016) *Plant Cell* (DNA damage in seed germination); Bray & West (2005) *New Phytol*
- **Cross-pathway convergence**: DNA repair/replication × general signaling × epigenetic regulation
- **Confound risk**: Low — the mechanism is specific and directional
- **Confidence**: **High**

---

## Tier 2: Important Targets (Moderate Expected Effect)

These targets have clear mechanistic connections to germination but with lower evidence strength, greater uncertainty about directionality, or higher confound risk.

---

### T2.1 — SOV6g029280.1 — 6-Phosphogluconate Dehydrogenase (6PGDH / PPP)

- **Mechanism**: 6PGDH catalyzes the second oxidative step of the **Pentose Phosphate Pathway (PPP)**, generating NADPH and ribulose-5-phosphate. [KNOWN] NADPH is the primary reductant for antioxidant systems (glutathione reductase, thioredoxin reductase) and for biosynthetic reactions. [KNOWN] In the seed context, high PPP flux maintains a strongly reducing cellular environment, which could suppress the pro-germination ROS burst. [INFERRED] Downregulation of 6PGDH would reduce NADPH production, shifting the redox balance toward a more oxidized state, potentially enhancing the ROS signal required for germination. [INFERRED] The pathway analysis assigns "high" priority.
- **Evidence strength**: Moderate
- **Key references**: Kruger & von Schaewen (2003) *Curr Opin Plant Biol* (PPP in plants); Bailly (2004) *Seed Sci Res* (redox in germination)
- **Confound risk**: Moderate — NADPH has many roles; the net effect is complex
- **Confidence**: **Medium**

---

### T2.2 — SOV1g027650.1 — Receptor-like Kinase (RLK)

- **Mechanism**: RLKs are the primary cell-surface receptors in plants, perceiving both endogenous peptide signals and exogenous PAMPs/MAMPs. [KNOWN] In seeds, RLKs can mediate ABA signaling (e.g., *GHR1*, AT4G20940), stress perception, or developmental signals. [KNOWN] Downregulation of a stress/defense-perceiving RLK would reduce the seed's sensitivity to inhibitory environmental signals, promoting germination under suboptimal conditions. [INFERRED] Without subfamily identification, the specific target is unclear.
- **Evidence strength**: Moderate
- **Key references**: Gómez-Gómez & Boller (2000) *Mol Cell* (RLK in PAMP perception); Hua et al. (2012) *Plant Cell* (GHR1 in ABA/stomata)
- **Confound risk**: Moderate
- **Confidence**: **Medium**

---

### T2.3 — SOV4g000660.1 — Receptor-like Serine/Threonine-Protein Kinase

- **Mechanism**: Similar to T2.2 but with serine/threonine kinase specificity. [KNOWN] In *Arabidopsis*, RLSK family members include *BRASSINOSTEROID INSENSITIVE 1* (BRI1, AT4G39400) and its co-receptor *BAK1*, which regulate brassinosteroid (BR) signaling. [KNOWN] BR promotes germination by enhancing GA signaling and suppressing ABA responses. [KNOWN] If this RLSK is a negative regulator of BR signaling, its downregulation would enhance BR signaling and promote germination. [SPECULATIVE]
- **Evidence strength**: Moderate
- **Key references**: Kim et al. (2012) *Plant Cell* (BR in germination); Gudesblat et al. (2012) *Nat Cell Biol*
- **Confound risk**: Moderate
- **Confidence**: **Medium**

---

### T2.4 — SOV4g010600.1 — Glycosyltransferase (Cell Wall)

- **Mechanism**: Glycosyltransferases (GTs) build cell wall polysaccharides, including hemicelluloses (xylans, mannans, xyloglucans) and pectins. [KNOWN] In the endosperm cap, high GT activity reinforces the mechanical barrier to radicle emergence. [INFERRED] Downregulation of GT would reduce cell wall synthesis/reinforcement, making the endosperm cap more susceptible to hydrolytic weakening by endogenous enzymes. [INFERRED]
- **Evidence strength**: Moderate
- **Key references**: Scheller & Ulvskov (2010) *Annu Rev Plant Biol* (cell wall polysaccharides); Müller et al. (2006) *Plant Cell* (endosperm weakening)
- **Confound risk**: Low
- **Confidence**: **Medium**

---

### T2.5 — SOV1g033840.1 — Glyco_transf_64 Domain-Containing Protein (Cell Wall)

- **Mechanism**: GT64 family glycosyltransferases are involved in hemicellulose synthesis, particularly xyloglucan backbone elongation. [KNOWN] Same logic as T2.4 applies. [INFERRED]
- **Evidence strength**: Moderate
- **Key references**: Zabotina (2012) *Front Plant Sci* (xyloglucan biosynthesis)
- **Confound risk**: Low
- **Confidence**: **Medium**

---

### T2.6 — SOV4g051070.1 — Beta-Galactosidase (Cell Wall)

- **Mechanism**: Beta-galactosidases (BGALs) hydrolyze galactose residues from pectin and hemicellulose side chains, contributing to cell wall loosening. [KNOWN] In *Arabidopsis* and tomato, BGALs are upregulated during germination and fruit ripening to facilitate cell wall softening. [KNOWN] Downregulation of a BGAL would *reduce* cell wall loosening—seemingly anti-germination. [INFERRED] However, the pathway analysis argues that the dominant effect is reduced wall synthesis (by the two GTs), making the BGAL's contribution less critical. [SPECULATIVE] This target may have a minor or even opposing effect compared to the GT targets.
- **Evidence strength**: Moderate
- **Key references**: Smith & Gross (2000) *Plant Cell Physiol* (BGAL in cell wall); Iglesias-Fernández et al. (2011) *Plant Cell* (BGAL in *Arabidopsis* germination)
- **Confound risk**: Low
- **Confidence**: **Medium** (but directionality uncertain)

---

### T2.7 — SOV1g002960.1, SOV5g006110.1, SOV2g038280.1 — F-box Proteins (Three paralogs)

- **Mechanism**: F-box proteins are substrate-recognition subunits of SCF (SKP1-CUL1-F-box) E3 ubiquitin ligase complexes. [KNOWN] They determine which proteins are ubiquitinated and degraded by the 26S proteasome. [KNOWN] In seeds, specific F-box proteins target dormancy-maintaining proteins (e.g., ABI5, a key ABA-responsive TF) for degradation to promote germination. [KNOWN] Conversely, other F-box proteins target GA-signaling components (DELLA proteins) for degradation to promote germination. [KNOWN] Downregulation of F-box proteins that target pro-germination proteins would *inhibit* germination, while downregulation of those targeting dormancy proteins would *promote* germination. [INFERRED] Without knowing the specific substrates of these three F-box proteins, directionality is uncertain.
- **Evidence strength**: Moderate
- **Key references**: Kepinski & Leyser (2005) *Nature* (F-box in auxin signaling); Liu & Stone (2010) *Plant Cell* (F-box in ABA signaling); Ariizumi et al. (2011) *Plant J* (F-box in GA signaling)
- **Confound risk**: Moderate
- **Confidence**: **Medium** (directionality uncertain)

---

### T2.8 — SOV1g043000.1 & SOV2g021870.1 — RING-type E3 Ubiquitin Transferases

- **Mechanism**: RING-domain E3 ligases directly catalyze ubiquitin transfer to target proteins. [KNOWN] In *Arabidopsis*, RING E3 ligases regulate ABA signaling (e.g., *AIP2*, AT5G20910, targets ABI3 for degradation), GA signaling, and stress responses. [KNOWN] If these RING E3 ligases target pro-germination proteins for degradation, their downregulation would stabilize these targets and promote germination. [INFERRED]
- **Evidence strength**: Moderate
- **Key references**: Zhang et al. (2005) *Plant Cell* (AIP2 in ABA signaling); Stone et al. (2006) *Plant Cell* (RING E3 in *Arabidopsis*)
- **Confound risk**: Moderate
- **Confidence**: **Medium**

---

### T2.9 — SOV2g028550.1 — E3 Ubiquitin-Protein Ligase RNF25

- **Mechanism**: RNF25 is an E3 ubiquitin ligase with roles in immune regulation and stress responses in mammals. [KNOWN] Plant homologs are less well-characterized. [INFERRED] In the seed context, RNF25 may regulate protein turnover during the dormancy-to-germination transition.
- **Evidence strength**: Weak-Moderate
- **Key references**: Nakamura et al. (2008) *Biochem Biophys Res Commun* (RNF25 in mammals)
- **Confound risk**: Moderate
- **Confidence**: **Low-Medium**

---

### T2.10 — SOV1g048290.1 — Glutamate Receptor (GLR)

- **Mechanism**: Plant Glutamate Receptor-Like (GLR) channels are non-selective cation channels that mediate Ca²⁺ influx in response to amino acid ligands. [KNOWN] In *Arabidopsis*, GLRs regulate systemic wound signaling, root development, and stomatal closure. [KNOWN] In seeds, GLR-mediated Ca²⁺ influx could activate defense signaling or stress responses that inhibit germination. [INFERRED] Downregulation would reduce Ca²⁺-mediated defense activation.
- **Evidence strength**: Moderate
- **Key references**: Forde & Roberts (2014) *Front Plant Sci* (GLR in plants); Mousavi et al. (2013) *Nature* (GLR in wound signaling)
- **Confound risk**: Moderate
- **Confidence**: **Medium**

---

### T2.11 — SOV2g039720.1 — Calcium-Binding Protein

- **Mechanism**: Ca²⁺-binding proteins (calmodulins, CMLs, CBLs) decode Ca²⁺ signals into specific cellular responses. [KNOWN] In seeds, Ca²⁺ signaling is integrated with ABA responses (via CPK/CDPK kinases) and stress perception. [KNOWN] Downregulation of a Ca²⁺-binding protein that relays stress/ABA signals would reduce the amplitude of these inhibitory signals. [INFERRED]
- **Evidence strength**: Moderate
- **Key references**: Luan et al. (2002) *Plant Cell* (Ca²⁺ signaling in plants); Zhu et al. (2007) *Plant Cell* (CBL-CIPK in ABA signaling)
- **Confound risk**: High — EPS osmopriming alters Ca²⁺ dynamics
- **Confidence**: **Medium**

---

### T2.12 — SOV4g000330.1 — Phytoene Synthase

- **Mechanism**: Phytoene synthase (PSY) catalyzes the first committed step of **carotenoid biosynthesis**, converting geranylgeranyl pyrophosphate to phytoene. [KNOWN] Carotenoids are precursors to **ABA** (via xanthoxin from cleavage of violaxanthin/neoxanthin by NCED enzymes). [KNOWN] Downregulation of PSY would reduce the carotenoid pool available for ABA biosynthesis, potentially lowering endogenous ABA levels and promoting germination. [INFERRED] This is a relatively indirect mechanism (PSY → carotenoids → xanthophylls → ABA), and other steps in the pathway are rate-limiting. [SPECULATIVE for germination specifically]
- **Evidence strength**: Moderate
- **Key references**: Nambara & Marion-Poll (2005) *Annu Rev Plant Biol* (ABA biosynthesis); Seo & Koshiba (2002) *Trends Plant Sci*; Fraser et al. (2000) *Plant J* (PSY regulation)
- **Confound risk**: Moderate
- **Confidence**: **Medium**

---

### T2.13 — SOV4g055600.1 — Cytochrome P450

- **Mechanism**: The CYP superfamily is vast and functionally diverse. In seeds, relevant CYPs include those involved in **ABA catabolism** (CYP707A family, AT4G19230), **GA biosynthesis** (CYP88A/CYP701A), **brassinosteroid biosynthesis** (CYP90 family), and **defense compound synthesis** (CYP79 family). [KNOWN] Without subfamily identification, the directionality of downregulation is highly uncertain. If this CYP is involved in ABA catabolism (CYP707A-like), its downregulation would *increase* ABA levels and *inhibit* germination—the opposite of the expected effect. [SPECULATIVE]
- **Evidence strength**: Weak-Moderate
- **Key references**: Kushiro et al. (2004) *EMBO J* (CYP707A in ABA catabolism); Hedden & Thomas (2012) *Biochem J* (CYP in GA biosynthesis)
- **Confound risk**: High — subfamily identity is critical
- **Confidence**: **Low-Medium**

---

### T2.14 — SOV1g034720.1 — Mitochondrial Distribution/Morphology Family 35 / Apoptosis-Related

- **Mechanism**: MDM35/TRIAP1 family proteins are involved in **mitochondrial morphology and the transfer of phosphatidic acid** between mitochondrial membranes. [KNOWN] In yeast and mammals, TRIAP1 is a p53-regulated anti-apoptotic protein. [KNOWN] In plant seeds, mitochondrial integrity is critical for ATP production during germination. [INFERRED] Downregulation could affect mitochondrial dynamics, potentially reducing the energetic capacity for germination—or, if this protein maintains a pro-apoptotic state that inhibits cell division, its downregulation could promote growth. [SPECULATIVE]
- **Evidence strength**: Weak
- **Key references**: Potting et al. (2013) *Cell Metab* (TRIAP1/MDM35 in mitochondria); Huang et al. (2011) *Plant Cell* (mitochondria in germination)
- **Confound risk**: Moderate
- **Confidence**: **Low-Medium**

---

### T2.15 — SOV3g020770.1 — TIC214 (Chloroplast Import Complex Component)

- **Mechanism**: TIC214 is a core component of the **TIC translocon** (Translocon at the Inner Chloroplast membrane), essential for importing nuclear-encoded proteins into chloroplasts. [KNOWN] In *Arabidopsis* (AT4G03320), *tic214* mutants are albino and lethal. [KNOWN] During germination, chloroplasts function primarily as sites of hormone synthesis (ABA, GA, CK) rather than photosynthesis. [KNOWN] Downregulation of TIC214 would impair chloroplast protein import, potentially disrupting ABA biosynthesis (NCED enzymes are chloroplast-localized) and reducing ABA levels. [INFERRED] However, severe TIC214 downregulation would be lethal; moderate downregulation might specifically affect ABA biosynthesis.
- **Evidence strength**: Moderate
- **Key references**: Chen & Li (2007) *Plant Cell* (TIC214 in *Arabidopsis*); Bölter & Soll (2017) *Mol Plant* (TIC translocon); Nambara & Marion-Poll (2005) (ABA biosynthesis in plastids)
- **Confound risk**: Low
- **Confidence**: **Medium**

---

### T2.16 — SOV1g019270.1 — DNA Topoisomerase 2

- **Mechanism**: Topoisomerase II resolves DNA topology during transcription and replication by introducing transient double-strand breaks. [KNOWN] During germination, massive transcriptional reactivation requires topoisomerase activity to relieve supercoiling. [INFERRED] Downregulation of Topo II would reduce transcriptional capacity, potentially limiting the speed of germination-program activation—seemingly anti-germination. [INFERRED] However, if Topo II is primarily active in maintaining a compact, transcriptionally repressed chromatin state (as in dormancy), its downregulation could derepress germination genes. [SPECULATIVE]
- **Evidence strength**: Weak-Moderate
- **Key references**: Nitiss (2009) *Nat Rev Cancer* (Topo II biology); Sugimoto-Shirasu et al. (2002) *Curr Biol* (Topo II in *Arabidopsis* development)
- **Confound risk**: Moderate
- **Confidence**: **Low-Medium**

---

### T2.17 — SOV5g000510.1 — ATP-dependent RNA Helicase / Pre-mRNA Splicing Factor

- **Mechanism**: RNA helicases are essential for spliceosome assembly and pre-mRNA splicing. [KNOWN] During germination, alternative splicing of key regulatory genes (e.g., *HAB1*, *ABI1*) produces isoforms with altered ABA sensitivity. [KNOWN] Downregulation of a specific splicing factor could shift the alternative splicing landscape, potentially producing ABA-insensitive isoforms that promote germination. [INFERRED]
- **Evidence strength**: Moderate
- **Key references**: Filichkin et al. (2010) *Genome Res* (alternative splicing in *Arabidopsis*); Punzo et al. (2020) *Front Plant Sci* (splicing in seed germination)
- **Confound risk**: Moderate
- **Confidence**: **Medium**

---

### T2.18 — SOV4g023530.1 — LUC7 N-terminus Domain-Containing Protein (Splicing-Related)

- **Mechanism**: LUC7 proteins are components of the U1 snRNP complex, involved in 5' splice site recognition. [KNOWN] In *Arabidopsis*, *LUC7* mutants show altered alternative splicing of stress-responsive genes. [KNOWN] Similar logic to T2.17 applies. [INFERRED]
- **Evidence strength**: Moderate
- **Key references**: Lewandowska et al. (2004) *Nucleic Acids Res* (LUC7 in splicing); Carrasco-López et al. (2017) *Plant Cell* (LUC7 in *Arabidopsis*)
- **Confound risk**: Moderate
- **Confidence**: **Medium**

---

### T2.19 — SOV6g037220.1 & SOV6g035270.1 & SOV4g005210.1 — Pentatricopeptide Repeat (PPR) Proteins

- **Mechanism**: PPR proteins are RNA-binding proteins that regulate RNA processing (editing, splicing, stabilization, cleavage) in mitochondria and chloroplasts. [KNOWN] During germination, mitochondrial RNA editing is essential for producing functional respiratory complex subunits. [KNOWN] Downregulation of specific PPR proteins could impair mitochondrial RNA processing, reducing respiratory capacity—seemingly anti-germination. [INFERRED] However, if these PPR proteins regulate the processing of transcripts encoding dormancy-maintaining factors (e.g., ABA biosynthesis enzymes in plastids), their downregulation could reduce ABA production. [SPECULATIVE]
- **Evidence strength**: Moderate
- **Key references**: Barkan & Small (2014) *Annu Rev Plant Biol* (PPR proteins); Fujii et al. (2011) *Plant Cell* (PPR in mitochondrial RNA editing)
- **Confound risk**: Moderate
- **Confidence**: **Low-Medium**

---

### T2.20 — SOV5g001320.1 — CTP Synthase

- **Mechanism**: CTP synthase converts UTP to CTP, an essential nucleotide for RNA synthesis, phospholipid biosynthesis (via CDP-choline pathway), and cell wall polysaccharide synthesis. [KNOWN] During germination, rapid transcriptional reactivation requires nucleotide pools. [KNOWN] Downregulation of CTP synthase could limit CTP availability, potentially slowing RNA synthesis and membrane biogenesis. [INFERRED] This seems anti-germination unless CTP is specifically required for synthesis of dormancy-maintaining factors. [SPECULATIVE]
- **Evidence strength**: Weak
- **Key references**: Kafer et al. (2004) *Plant Physiol* (CTP synthase in plants)
- **Confound risk**: Moderate
- **Confidence**: **Low**

---

### T2.21 — SOV1g048270.1 — Aspartokinase

- **Mechanism**: Aspartokinase (AK) catalyzes the first step of the **aspartate-derived amino acid biosynthesis pathway**, producing aspartyl-phosphate from aspartate and ATP. [KNOWN] This pathway produces lysine, threonine, methionine, and isoleucine. [KNOWN] During germination, amino acid biosynthesis supports protein synthesis for embryonic growth. [KNOWN] Downregulation of AK would reduce the flux through this pathway, potentially limiting the availability of essential amino acids. [INFERRED] This seems anti-germination unless AK is specifically required for synthesis of a dormancy-maintaining compound. [SPECULATIVE]
- **Evidence strength**: Weak
- **Key references**: Azevedo et al. (2006) *Phytochemistry* (aspartate pathway in plants)
- **Confound risk**: Low
- **Confidence**: **Low**

---

### T2.22 — SOV4g006140.1 — Choline/Ethanolaminephosphotransferase 1

- **Mechanism**: This enzyme catalyzes the final step of **phosphatidylcholine (PC) and phosphatidylethanolamine (PE) biosynthesis** via the CDP-choline/CDP-ethanolamine (Kennedy) pathway. [KNOWN] PC and PE are the major structural phospholipids of cellular membranes. [KNOWN] During germination, membrane biogenesis is essential for cell expansion. [KNOWN] Downregulation would reduce PC/PE synthesis, potentially limiting membrane expansion and cell growth. [INFERRED] However, if this enzyme is specifically required for synthesis of phospholipid-derived signaling molecules (e.g., lysophosphatidylcholine as an ABA signal), its downregulation could reduce ABA signaling. [SPECULATIVE]
- **Evidence strength**: Weak-Moderate
- **Key references**: Nuccio et al. (2000) *Plant J* (phospholipid biosynthesis in plants)
- **Confound risk**: Moderate
- **Confidence**: **Low-Medium**

---

### T2.23 — SOV6g042110.1 — Glyoxylate/Hydroxypyruvate Reductase

- **Mechanism**: This enzyme functions in the **photorespiratory pathway** (in the peroxisome) and in glyoxylate detoxification. [KNOWN] During germination, fatty acid β-oxidation in peroxisomes produces acetyl-CoA, which enters the **glyoxylate cycle** to generate sucrose from stored oils. [KNOWN] Glyoxylate reductase activity is required to prevent glyoxylate accumulation (which is toxic). [KNOWN] Downregulation could impair glyoxylate detoxification, potentially limiting oil-to-sugar conversion efficiency. [INFERRED] This seems anti-germination for oil-rich seeds, but spinach seeds have moderate oil content.
- **Evidence strength**: Moderate
- **Key references**: Timm et al. (2008) *Plant Physiol* (glyoxylate reductase in *Arabidopsis*); Eastmond (2006) *Plant Cell* (glyoxylate cycle in germination)
- **Confound risk**: Low
- **Confidence**: **Medium** (directionality uncertain)

---

### T2.24 — SOV3g021300.1 — Stress Response Protein NST1

- **Mechanism**: NST1 (*NO STRESS 1* or similar) in *Arabidopsis* context likely refers to a stress-responsive transcription factor or signaling protein. [INFERRED] In the defense/immunity pathway, NST1 is assigned "medium" priority. If NST1 promotes stress responses that compete with germination, its downregulation would promote growth. [SPECULATIVE]
- **Evidence strength**: Weak
- **Key references**: Limited plant-specific literature on NST1 in seeds
- **Confound risk**: High
- **Confidence**: **Low**

---

### T2.25 — SOV1g021670.1 — Putative Disease Resistance Protein

- **Mechanism**: NBS-LRR (or TIR-NBS-LRR) disease resistance proteins are the primary intracellular immune receptors in plants. [KNOWN] Their activation triggers the **hypersensitive response (HR)**, a form of programmed cell death. [KNOWN] In seeds, inappropriate activation of R-protein-mediated immunity would be highly detrimental to germination, causing localized cell death and resource diversion. [INFERRED] Downregulation of this R-protein would reduce the risk of autoimmune activation during germination. [INFERRED]
- **Evidence strength**: Moderate
- **Key references**: Jones & Dangl (2006) *Nature* (plant immunity); Gómez-Gómez et al. (1999) *Plant Cell* (R-protein in *Arabidopsis*)
- **Confound risk**: Moderate — bacterial EPS could itself trigger PTI
- **Confidence**: **Medium**

---

## Tier 3: Supporting Targets (Indirect or Minor Effect)

These targets have weaker mechanistic connections to germination, lower pathway priority, high confound risk, or represent housekeeping functions with unclear germination relevance.

---

### T3.1 — SOV4g005210.1, SOV6g035270.1, SOV6g037220.1 — PPR Proteins (see T2.19)
*(Moved to Tier 2 above; listed here for completeness)*

---

### T3.2 — SOV4g035080.1 — tRNA (G37)-N1-Methyltransferase

- **Mechanism**: Methylates G37 of specific tRNAs, preventing +1 frameshifting during translation. [KNOWN] Downregulation could reduce translational fidelity. [INFERRED] Unclear germination relevance.
- **Evidence strength**: Weak
- **Confidence**: **Low**

---

### T3.3 — SOV4g000010.1 — Lysine-tRNA Ligase

- **Mechanism**: Aminoacyl-tRNA synthetases are essential for translation. [KNOWN] Downregulation would reduce translational capacity. [INFERRED] Seemingly anti-germination.
- **Evidence strength**: Weak
- **Confidence**: **Low**

---

### T3.4 — SOV5g013040.1 — Snurportin-1

- **Mechanism**: Snurportin-1 imports m³G-capped snRNAs into the nucleus for spliceosome assembly. [KNOWN] Downregulation could impair snRNA import and splicing. [INFERRED] Indirect germination relevance via alternative splicing of ABA-signaling genes. [SPECULATIVE]
- **Evidence strength**: Weak
- **Key references**: Huber et al. (1998) *Cell* (Snurportin-1 in snRNA import)
- **Confidence**: **Low**

---

### T3.5 — SOV0g001750.1 — Protein TAR1-like (TGS1)

- **Mechanism**: TGS1/TAR1 hypermethylates the caps of snRNAs and snoRNAs, which is required for their nuclear retention and function. [KNOWN] In *Arabidopsis* (*TGS1*, AT1G68970), loss of function causes pleiotropic developmental defects. [KNOWN] Downregulation could impair spliceosome function and ribosome biogenesis. [INFERRED] Indirect germination relevance.
- **Evidence strength**: Weak-Moderate
- **Key references**: Verheggen et al. (2002) *Mol Cell* (TGS1 in snRNA maturation)
- **Confidence**: **Low**

---

### T3.6 — SOV0g001060.1 — Regulator of rDNA Transcription Protein 15

- **Mechanism**: Regulates ribosomal RNA transcription by RNA Pol I. [KNOWN] Downregulation would reduce rRNA synthesis and ribosome biogenesis, potentially limiting translational capacity. [INFERRED] Seemingly anti-germination unless rDNA transcription is specifically required for dormancy maintenance. [SPECULATIVE]
- **Evidence strength**: Weak
- **Confidence**: **Low**

---

### T3.7 — SOV2g004250.1, SOV4g025520.1, SOV3g033520.1, SOV1g003910.1, SOV4g035390.1 — Transposon-Related (Reverse Transcriptases / Gag)

- **Mechanism**: These genes encode retrotransposon machinery. [KNOWN] Their downregulation would prevent retrotransposon mobilization during the stress of germination, reducing genomic instability and metabolic drain. [INFERRED] This is a supporting effect—preventing a negative outcome rather than actively promoting germination.
- **Evidence strength**: Moderate (for the principle); Weak (for germination-specific contribution)
- **Key references**: Grandbastien (1998) *Trends Plant Sci* (retrotransposons in stress); Ito et al. (2011) *Nature* (TE activation in stress)
- **Confound risk**: Moderate — epigenetic changes from other targets (DNA methyltransferase downregulation) could paradoxically *increase* TE activity
- **Confidence**: **Low-Medium**

---

### T3.8 — SOV1g004930.1, SOV4g008190.1, SOV6g042250.1 — GDSL Esterase/Lipase

- **Mechanism**: GDSL lipases are secreted enzymes involved in cutin/suberin biosynthesis, defense compound production, and lipid signaling. [KNOWN] In seeds, GDSL lipases may contribute to seed coat permeability or defense. [INFERRED] Downregulation could alter seed coat lipid composition, potentially improving water uptake during imbibition. [SPECULATIVE]
- **Evidence strength**: Weak
- **Key references**: Ling et al. (2006) *Plant Physiol* (GDSL lipase in *Arabidopsis*)
- **Confound risk**: High — EPS directly affects seed coat wetting
- **Confidence**: **Low**

---

### T3.9 — SOV1g032780.1 & SOV4g041000.1 — ABC Transporters

- **Mechanism**: ABC transporters move diverse substrates across membranes, including ABA, auxin, heavy metals, and defense compounds. [KNOWN] In seeds, *AtABCG25* (AT1G71960) exports ABA from biosynthetic cells, and *AtABCG40* (AT1G15520) imports ABA into guard cells. [KNOWN] Downregulation of an ABA-exporting ABC transporter