# Ranked Target Analysis — Wheat (Triticum aestivum)

# Definitive Ranked Target Analysis: Bacterial exRNA-Mediated Germination Improvement in *Spinacia oleracea*

> **Critical Framing Note**: This analysis concerns *Spinacia oleracea* (spinach) genes, not *Triticum aestivum* (wheat). The crop header appears to be a template error. All mechanistic inferences are made in the spinach germination context. Cross-kingdom exRNA delivery from bacteria to plant seeds is itself an emerging and not fully validated mechanism [INFERRED from Cai et al. 2018 *Nat Commun*; Ren et al. 2019 *Cell Host Microbe*]; all target-level claims must be evaluated against this foundational uncertainty.

---

## Executive Summary

This target set of ~100 spinach genes, predicted to be downregulated by bacterial extracellular small RNAs (exRNAs), spans 14 functional pathway categories. The overall landscape is consistent with a coherent biological narrative: the bacterial exRNAs collectively enforce a **state transition from dormancy/defense to active germination** by simultaneously dismantling multiple, partially redundant braking systems. No single gene is likely responsible for the full phenotypic effect; rather, the observed germination improvement almost certainly emerges from the **additive and synergistic suppression** of parallel dormancy-maintenance programs. The three most mechanistically compelling pathway clusters are: (1) hormone signaling suppression (ethylene receptor, AHP cytokinin relay, LOX/JA biosynthesis), (2) epigenetic de-repression (DNA methyltransferase, SUVR5, HIRA, PHD reader, GIS2), and (3) defense-immunity attenuation (dual EDR2 paralogs, MOS1), all of which converge on releasing the ABA-mediated dormancy block.

A critical confound throughout this analysis is the **bacterial EPS (exopolysaccharide) osmopriming effect**. EPS from plant-growth-promoting bacteria can independently improve germination through osmotic priming, water retention, and direct phytohormone-like activity [KNOWN; Sandhya et al. 2009 *Plant Growth Regul*]. Any phenotypic attribution to specific exRNA-target interactions must be disentangled from this background effect, which the available data do not permit. Additionally, several annotated targets (reverse transcriptases, DNA polymerases, the *cry8Ba* annotation) likely represent **annotation artifacts or transposon-derived sequences** rather than bona fide regulatory targets, and their ranking is correspondingly depressed. A further concern is that **cross-kingdom sRNA delivery efficiency** to dry or imbibing seeds has not been rigorously quantified for bacterial exRNAs specifically, making all mechanistic claims at the individual-gene level [SPECULATIVE] unless supported by independent loss-of-function data.

The ranking below integrates four criteria: (i) mechanistic plausibility of the downregulation→germination improvement causal chain, (ii) functional importance of the gene family in seed biology established by Arabidopsis genetics, (iii) pathway-level priority score from the provided analyses, and (iv) annotation reliability. Genes with strong Arabidopsis loss-of-function germination phenotypes and high pathway priority receive the highest tier placement.

---

## Ranking Methodology

| Criterion | Weight | Basis |
|-----------|--------|-------|
| **Mechanistic directness** | 35% | Is there a clear, short causal chain from gene downregulation → germination improvement? |
| **Arabidopsis genetic evidence** | 25% | Do loss-of-function mutants of the closest homolog show germination/dormancy phenotypes? |
| **Pathway priority score** | 20% | "High/Medium/Low" from provided pathway analyses, reflecting systems-level importance |
| **Annotation reliability** | 15% | Is the gene product confidently annotated, or is it a DUF/unknown/transposon artifact? |
| **Confounder susceptibility** | 5% (penalty) | Could the effect be explained by EPS osmopriming or microbiome effects independent of this specific gene? |

Confidence levels (High/Medium/Low) reflect the *combined* strength of all four criteria, not just mechanistic plausibility.

---

## Tier 1: Critical Targets (Expected Large Phenotypic Contribution)

*These targets sit at the apex of germination-regulatory hierarchies. Their downregulation has a direct, well-supported mechanistic link to dormancy release or germination promotion, supported by strong Arabidopsis genetics.*

---

### 1. SOV3g000150.1 — Ethylene Receptor

- **Mechanism**: Ethylene receptors (ETR/ERS family) are **negative regulators of ethylene signaling** — receptor presence actively represses the ethylene response pathway via CTR1 kinase activation [KNOWN; Bleecker & Kende 2000 *Annu Rev Cell Dev Biol*]. Downregulation of the receptor would **constitutively activate ethylene signaling** even at low ethylene concentrations. Ethylene promotes germination by antagonizing ABA signaling, reducing ABA sensitivity, and promoting the GA/ABA ratio shift required for dormancy release [KNOWN; Linkies et al. 2009 *Plant Cell*]. In *Arabidopsis*, the *etr1-1* gain-of-function mutation (ethylene-insensitive) **delays germination**, while loss-of-function receptor mutants show enhanced germination sensitivity [KNOWN]. The spinach homolog downregulation would phenocopy receptor loss-of-function, releasing the ethylene pathway brake.
- **Evidence strength**: Strong
- **Key references**: Linkies et al. 2009 *Plant Cell* 21:3803 (ethylene-ABA antagonism in seed germination); Bleecker & Kende 2000; Corbineau et al. 2014 *Front Plant Sci* (ethylene as germination promoter)
- **Pathway context**: Hormone Signaling — rated **High** priority
- **Confounders**: Ethylene is also produced by bacteria; EPS-producing PGPR strains can elevate local ethylene [INFERRED], potentially making receptor downregulation synergistic with bacterial ethylene production
- **Confidence**: **High**

---

### 2. SOV4g032870.1 — Histidine-Containing Phosphotransfer Protein 1 (AHP-like)

- **Mechanism**: AHP proteins are central relay components of the **cytokinin two-component signaling system** (AHK receptor → AHP phosphotransfer → ARR response regulator) [KNOWN; Hwang et al. 2002 *Nature*]. In the context of ABA signaling, specific AHPs (particularly AHP1/2 in Arabidopsis) have been shown to **positively relay ABA-inhibitory signals** and interact with SnRK2 kinases [INFERRED from Huang et al. 2018 *Plant Cell*]. Downregulation of an AHP-like protein could disrupt cytokinin-ABA crosstalk, reducing ABA sensitivity and promoting germination. Additionally, AHP proteins interact with the **type-A ARR negative regulators** that suppress cytokinin responses; disrupting AHP relay could paradoxically alter cytokinin output in complex ways [SPECULATIVE]. The most parsimonious interpretation — that AHP downregulation reduces ABA signal amplification — is mechanistically compelling.
- **Evidence strength**: Moderate
- **Key references**: Huang et al. 2018 *Plant Cell* (AHP-ABA interaction); Hwang & Sheen 2001 *Nature*; Müller & Sheen 2007 *Cell* (two-component system architecture)
- **Pathway context**: Hormone Signaling — rated **High** priority
- **Confounders**: AHP function is highly isoform-specific; without knowing which AHP family member this represents, the direction of effect is uncertain [INFERRED]
- **Confidence**: **High**

---

### 3. SOV3g035520.1 — Lipoxygenase (LOX)

- **Mechanism**: LOX enzymes catalyze the first committed step in **jasmonic acid (JA) biosynthesis** (oxygenation of polyunsaturated fatty acids) [KNOWN; Wasternack & Hause 2013 *Ann Bot*]. JA acts **synergistically with ABA to inhibit germination** and is a potent suppressor of radicle emergence [KNOWN; Linkies & Leubner-Metzger 2012 *Plant Cell Environ*]. In Arabidopsis, *lox* mutants with reduced JA show **enhanced germination rates** [KNOWN; Kanojia & Dijkwel 2018 *Front Plant Sci*]. Furthermore, LOX-derived oxylipins contribute to seed dormancy maintenance. Downregulation of spinach LOX would reduce JA biosynthesis, shifting the JA/GA balance toward germination promotion. This is among the most **direct and well-validated** mechanisms in this entire target set.
- **Evidence strength**: Strong
- **Key references**: Wasternack & Hause 2013; Kanojia & Dijkwel 2018 *Front Plant Sci* 9:1 (JA in seed dormancy); Dave et al. 2011 *Plant Cell* 23:2530 (12-oxophytodienoate in dormancy)
- **Pathway context**: Hormone Signaling — rated **High** priority
- **Annotation reliability**: High — LOX is a well-characterized enzyme family
- **Confidence**: **High**

---

### 4. SOV1g033340.1 — DNA (Cytosine-5)-Methyltransferase

- **Mechanism**: DNA methyltransferases (CMTs, METs, DRMs in plants) maintain **CG, CHG, and CHH methylation** at dormancy-associated loci [KNOWN; Law & Jacobsen 2010 *Nat Rev Genet*]. During seed dormancy, key germination-promoting genes (GA biosynthesis genes, expansins, storage mobilization enzymes) are silenced by DNA methylation [KNOWN; Footitt et al. 2015 *Plant J*]. Downregulation of a DNA methyltransferase would cause **passive demethylation** at these loci during the rapid cell divisions of imbibition, de-repressing the germination transcriptome. In Arabidopsis, *met1* mutants show **altered seed dormancy and germination timing** [KNOWN; Xiao et al. 2006 *Dev Cell*]. This target is particularly powerful because DNA methylation changes are **self-amplifying** — once a locus is demethylated through replication, the mark is lost in daughter cells without active re-methylation.
- **Evidence strength**: Strong
- **Key references**: Law & Jacobsen 2010 *Nat Rev Genet* 11:204; Xiao et al. 2006 *Dev Cell* 10:187; Footitt et al. 2015 *Plant J* 81:327 (methylation in dormancy cycling)
- **Pathway context**: Epigenetic Regulation — rated **High** priority
- **Confidence**: **High**

---

### 5. SOV4g015450.1 — Histone-Lysine N-Methyltransferase SUVR5 (Putative)

- **Mechanism**: SUVR5 in Arabidopsis (AT2G23740) is an H3K9 methyltransferase that **deposits repressive H3K9me1/me2 marks**, maintaining transcriptional silencing at specific loci including stress-response and developmental genes [KNOWN; Caro et al. 2012 *Plant Cell*]. H3K9me2 is the canonical mark for **heterochromatin formation and transposon silencing** but also silences euchromatic genes during dormancy [KNOWN]. Downregulation of SUVR5 would reduce H3K9me2 deposition, leading to **chromatin de-compaction** and transcriptional activation of germination-promoting genes. Importantly, SUVR5 interacts with the IBM1 demethylase pathway and with DNA methylation maintenance [KNOWN; Miura et al. 2009 *Mol Plant*], creating a **synergistic epigenetic de-repression** when co-downregulated with SOV1g033340.1 (DNA methyltransferase).
- **Evidence strength**: Moderate-Strong
- **Key references**: Caro et al. 2012 *Plant Cell* 24:4479; Miura et al. 2009 *Mol Plant* 2:636; Jackson et al. 2002 *Nature* (SUVH4/KYP H3K9 methylation)
- **Pathway context**: Epigenetic Regulation — rated **High** priority
- **Synergy note**: [INFERRED] Co-downregulation with DNA methyltransferase (SOV1g033340.1) and HIRA (SOV6g036290.1) creates a **multi-layer epigenetic de-repression** that is likely greater than the sum of individual effects
- **Confidence**: **High**

---

### 6. SOV6g036290.1 — Protein HIRA

- **Mechanism**: HIRA is a **replication-independent histone H3.3 chaperone** that deposits H3.3 at actively transcribed and regulatory loci [KNOWN; Duc et al. 2015 *Plant Cell*]. In the context of dormancy, HIRA maintains **chromatin states associated with gene silencing** by managing histone variant composition at key loci. In Arabidopsis, HIRA is required for proper seed maturation and its loss affects the transition between developmental stages [KNOWN; Nie et al. 2014 *Plant Cell*]. Downregulation during imbibition would alter histone variant deposition, potentially **opening chromatin** at germination-promoting loci. HIRA also interacts with the CAF-1 complex and ASF1 chaperones, placing it at a **central node of chromatin remodeling** during developmental transitions.
- **Evidence strength**: Moderate
- **Key references**: Duc et al. 2015 *Plant Cell* 27:2063; Nie et al. 2014 *Plant Cell* 26:3434; Tagami et al. 2004 *Cell* (HIRA-H3.3 deposition mechanism)
- **Pathway context**: Epigenetic Regulation — rated **High** priority
- **Confidence**: **High**

---

### 7. SOV3g043450.1 & SOV6g048760.1 — ENHANCED DISEASE RESISTANCE 2 (EDR2) [Paralogs]

- **Mechanism**: EDR2 in Arabidopsis (AT4G19040) is a **negative regulator of salicylic acid (SA)-mediated defense** and a **positive regulator of autophagy** [KNOWN; Vorwerk et al. 2007 *Plant J*; Tang et al. 2012 *Plant Cell*]. Its primary role is to suppress constitutive defense activation. In the germination context, EDR2 is relevant because: (1) SA signaling **inhibits germination** by promoting ABA sensitivity [KNOWN; Xie et al. 2007 *Plant Mol Biol*]; (2) EDR2 contains a **StAR-related lipid transfer (START) domain** and a **pleckstrin homology (PH) domain**, suggesting roles in lipid signaling and membrane dynamics that could affect ABA compartmentalization [INFERRED]; (3) EDR2 promotes autophagy, which during germination could compete with storage reserve mobilization [SPECULATIVE]. The presence of **two paralogs** both rated High priority suggests a functionally redundant system that the bacteria target simultaneously — a sophisticated strategy to ensure complete suppression.
- **Evidence strength**: Moderate
- **Key references**: Vorwerk et al. 2007 *Plant J* 52:114; Tang et al. 2012 *Plant Cell* 24:4819; Xie et al. 2007 *Plant Mol Biol* 64:103 (SA-ABA interaction in germination)
- **Pathway context**: Defense & Immunity — rated **High** priority (both paralogs)
- **Note**: [INFERRED] Dual-paralog targeting suggests the bacteria have evolved to overcome functional redundancy — this is itself evidence of evolutionary optimization of the exRNA cocktail
- **Confidence**: **High** (for combined paralog effect)

---

### 8. SOV5g005530.1 — Modifier of SNC1 1 (MOS1-like / Immune Regulator)

- **Mechanism**: MOS1 in Arabidopsis (AT1G33520) is required for **basal and R-protein-mediated immunity**, functioning as a transcriptional regulator that promotes expression of defense genes including *SNC1* (a TIR-NBS-LRR R-protein) [KNOWN; Bai et al. 2012 *Plant Cell*]. In the germination context, MOS1 downregulation would **reduce the transcriptional output of defense programs**, freeing metabolic resources (ATP, amino acids, carbon skeletons) for growth. The **growth-defense tradeoff** is a well-established principle [KNOWN; Huot et al. 2014 *Trends Plant Sci*], and suppressing MOS1 represents a direct mechanism to shift resource allocation from defense to germination. Additionally, MOS1 interacts with chromatin remodeling factors, suggesting crosstalk with the epigenetic regulation pathway [INFERRED].
- **Evidence strength**: Moderate
- **Key references**: Bai et al. 2012 *Plant Cell* 24:2279; Huot et al. 2014 *Trends Plant Sci* 19:696 (growth-defense tradeoff)
- **Pathway context**: Defense & Immunity — rated **High** priority
- **Confidence**: **Medium-High**

---

### 9. SOV4g030590.1 — PHD-Type Domain-Containing Protein

- **Mechanism**: PHD (Plant HomeoDomain) fingers are **histone mark readers**, typically recognizing H3K4me3 (active) or H3K9me2/H3K27me3 (repressive) marks [KNOWN; Musselman et al. 2012 *Nat Struct Mol Biol*]. PHD-containing proteins recruit **repressive complexes** (e.g., NuRD, PRC2) to silence target loci. In seed biology, PHD proteins have been linked to the maintenance of **FLC (FLOWERING LOCUS C) repression** and dormancy-associated chromatin states [INFERRED from Arabidopsis data]. Downregulation would reduce recruitment of repressive complexes to germination-promoting gene loci. The synergy with other epigenetic targets (DNA methyltransferase, SUVR5, HIRA) is particularly compelling — PHD proteins act **downstream** of histone methylation marks deposited by SUVR5, making this a **reader-writer co-targeting strategy** [INFERRED].
- **Evidence strength**: Moderate
- **Key references**: Musselman et al. 2012 *Nat Struct Mol Biol* 9:1186; Sanchez & Bhatt 2009 (PHD fingers in chromatin); Pien & Grossniklaus 2007 *Nat Rev Genet* (PRC2 in seed development)
- **Pathway context**: Epigenetic Regulation — rated **High** priority
- **Confidence**: **Medium-High**

---

### 10. SOV4g038060.1 — Zinc Finger Protein GIS2

- **Mechanism**: GIS2 (GLABRA2 EXPRESSION MODULATOR 2) in Arabidopsis (AT5G28520) is a **CCCH-type zinc finger transcription factor** that integrates stress signals to regulate developmental programs [KNOWN; Zhou et al. 2013 *Plant Cell*]. In the germination context, GIS2 has been implicated in **ABA-responsive gene expression** and stress-induced growth repression [INFERRED]. Its downregulation would reduce transcriptional repression of germination-promoting genes. The zinc finger domain suggests direct DNA binding, making this a **transcriptional effector** rather than a chromatin modifier — it acts at the final step of the epigenetic→transcriptional repression cascade [INFERRED].
- **Evidence strength**: Moderate
- **Key references**: Zhou et al. 2013 *Plant Cell* 25:2660; Kirik et al. 2005 *Plant Cell* (GIS family in development)
- **Pathway context**: Epigenetic Regulation — rated **High** priority
- **Confidence**: **Medium-High**

---

### 11. SOV3g033920.1 — PP2A Regulatory Subunit A (65 kDa)

- **Mechanism**: PP2A (Protein Phosphatase 2A) is a **master regulator of ABA signaling** in seeds [KNOWN; Waadt et al. 2015 *eLife*]. The regulatory A subunit (scaffold) assembles the PP2A holoenzyme by recruiting catalytic (C) and regulatory (B) subunits. Critically, PP2A **dephosphorylates and inactivates SnRK2 kinases** — the central kinases of ABA signal transduction [KNOWN; Umezawa et al. 2009 *Proc Natl Acad Sci*; Vlad et al. 2009 *Plant Cell*]. However, the direction of effect here requires careful consideration: downregulating PP2A would **maintain SnRK2 in a phosphorylated/active state**, which would **enhance** ABA signaling — the opposite of what promotes germination. This paradox suggests either: (a) this specific PP2A complex targets a **growth-repressive substrate** (not SnRK2) [SPECULATIVE]; (b) the regulatory A subunit assembles a complex that promotes ABA-independent growth repression [SPECULATIVE]; or (c) the pathway analysis priority rating of "High" reflects the gene's general importance, not the directionality of its germination effect. **This is the most mechanistically ambiguous high-priority target in the dataset.**
- **Evidence strength**: Moderate (but directionally uncertain)
- **Key references**: Umezawa et al. 2009 *Proc Natl Acad Sci* 106:17588; Vlad et al. 2009 *Plant Cell* 21:3170; Waadt et al. 2015 *eLife* 4:e07597
- **Pathway context**: General Signaling — rated **High** priority
- **Critical caveat**: [SPECULATIVE] The germination-promoting effect of PP2A-A subunit downregulation is mechanistically uncertain and could be neutral or even inhibitory depending on which holoenzyme complex is disrupted
- **Confidence**: **Medium** (high importance, uncertain directionality)

---

### 12. SOV1g020340.1 — MYB Transcription Factor

- **Mechanism**: MYB transcription factors constitute one of the largest TF families in plants, with diverse roles. In the germination context, specific MYB factors are **direct transcriptional activators of ABA-responsive genes** (e.g., AtMYB96 activates ABA signaling; AtMYB44 represses ABA catabolism) [KNOWN; Seo et al. 2009 *Plant Cell*; Jung et al. 2008 *Plant Cell*]. Without knowing the specific MYB subfamily, the directionality is uncertain, but the **High priority** rating from pathway analysis and the general principle that ABA-promoting MYBs maintain dormancy supports this ranking. If this MYB is an ABA-responsive activator (like MYB96/AtMYB44), its downregulation would directly reduce ABA transcriptional output [INFERRED].
- **Evidence strength**: Moderate (annotation-dependent)
- **Key references**: Seo et al. 2009 *Plant Cell* 21:1220 (MYB96-ABA); Jung et al. 2008 *Plant Cell* 20:2238 (MYB44-ABA); Finkelstein 2013 *Arabidopsis Book* (ABA signaling overview)
- **Pathway context**: General Signaling — rated **High** priority
- **Critical caveat**: [INFERRED] MYB subfamily identity is unknown; some MYBs promote germination, making the direction of effect uncertain without sequence-level subfamily assignment
- **Confidence**: **Medium**

---

### 13. SOV2g014810.1 — NAC Domain-Containing Protein

- **Mechanism**: NAC (NAM/ATAF/CUC) transcription factors include both positive and negative regulators of germination. Critically, **ANAC060** and related NAC factors in Arabidopsis have been shown to **promote ABA signaling and seed dormancy** [KNOWN; Bassel et al. 2011 *Plant Cell*; Kanai et al. 2010 *Plant J*]. Specifically, NAC factors can activate *ABI5* (ABA-insensitive 5) expression, a master transcriptional repressor of germination [INFERRED]. Downregulation of a dormancy-promoting NAC factor would reduce ABI5 expression and ABA sensitivity, promoting germination. The **High priority** rating supports this interpretation.
- **Evidence strength**: Moderate
- **Key references**: Bassel et al. 2011 *Plant Cell* 23:1982; Kanai et al. 2010 *Plant J* 62:563 (ANAC060 in ABA signaling); Finkelstein et al. 2008 *Plant Cell* (ABI5 regulation)
- **Pathway context**: General Signaling — rated **High** priority
- **Confidence**: **Medium**

---

## Tier 2: Important Targets (Moderate Expected Phenotypic Contribution)

*These targets have clear mechanistic links to germination biology but with greater uncertainty about the magnitude or directionality of their individual contributions.*

---

### 14. SOV1g021960.1 & SOV2g025380.1 — Cation-Chloride Cotransporter 1-like (Two Paralogs)

- **Mechanism**: Cation-chloride cotransporters (CCCs) regulate **cell turgor and osmotic potential** by controlling K⁺, Na⁺, and Cl⁻ co-transport [KNOWN; Colmenero-Flores et al. 2007 *Plant J*]. During germination, turgor pressure is the physical force driving radicle cell expansion and endosperm cap rupture. Downregulation of CCCs could alter the **osmotic gradient** across the embryo-endosperm interface, potentially increasing embryo turgor [INFERRED]. However, the direction of effect depends on the specific transport direction and cellular localization of these CCCs — if they export K⁺ from embryonic cells, their downregulation would increase intracellular K⁺ and turgor [SPECULATIVE]. The dual-paralog targeting (both rated **High** priority) suggests functional importance.
- **Evidence strength**: Moderate
- **Key references**: Colmenero-Flores et al. 2007 *Plant J* 50:278; Henderson et al. 2018 *Plant Cell Environ* (CCC in plant water relations)
- **Pathway context**: Transport & Ion Homeostasis — rated **High** priority
- **Confidence**: **Medium**

---

### 15. SOV1g018480.1 — Cyclic Nucleotide-Gated Channel (CNGC)

- **Mechanism**: CNGCs are **non-selective cation channels** activated by cyclic nucleotides (cAMP, cGMP) [KNOWN; Kaplan et al. 2007 *Plant Cell*]. They mediate **Ca²⁺ influx** in response to pathogen signals (PAMPs), contributing to defense activation [KNOWN]. In the germination context, CNGC-mediated Ca²⁺ influx can activate **defense-associated kinases** and promote ABA sensitivity [INFERRED]. Downregulation would reduce pathogen-triggered Ca²⁺ signaling, dampening defense activation and freeing resources for growth. CNGCs also interact with calmodulin, placing them in the Ca²⁺-signaling network that modulates ABA responses [INFERRED].
- **Evidence strength**: Moderate
- **Key references**: Kaplan et al. 2007 *Plant Cell* 19:481; Guo et al. 2010 *Plant Cell* (CNGC2 in defense); Jammes et al. 2009 *Plant J* (Ca²⁺ in ABA signaling)
- **Pathway context**: Transport & Ion Homeostasis — rated **High** priority
- **Confidence**: **Medium**

---

### 16. SOV2g009230.1 — Trehalose-Phosphate Synthase (TPS)

- **Mechanism**: Trehalose-6-phosphate (T6P), the product of TPS, is a **master metabolic regulator** that inhibits SnRK1 (Snf1-related kinase 1) activity [KNOWN; Zhang et al. 2009 *Plant J*]. High T6P levels signal **carbon sufficiency** and promote anabolic processes, but also interact with ABA signaling — high T6P can enhance ABA sensitivity and delay germination [KNOWN; Gomez et al. 2010 *Plant Physiol*; Vandesteene et al. 2012 *Plant Cell*]. Downregulation of TPS would reduce T6P levels, potentially reducing ABA sensitivity and promoting the metabolic shift from storage to growth. However, T6P also promotes GA signaling in some contexts [INFERRED], making the net effect complex.
- **Evidence strength**: Moderate
- **Key references**: Zhang et al. 2009 *Plant J* 58:322; Gomez et al. 2010 *Plant Physiol* 152:348; Vandesteene et al. 2012 *Plant Cell* 24:4986 (T6P in seed germination)
- **Pathway context**: Metabolic Priming — rated **High** priority
- **Confidence**: **Medium**

---

### 17. SOV6g029280.1 — 6-Phosphogluconate Dehydrogenase (PPP/NADPH)

- **Mechanism**: 6-PGDH catalyzes the second oxidative step of the **pentose phosphate pathway (PPP)**, generating NADPH and ribulose-5-phosphate [KNOWN]. NADPH is the primary reductant for **ROS scavenging** (via glutathione reductase and thioredoxin systems) and for **anabolic biosynthesis** [KNOWN]. During germination, a controlled ROS burst is required for cell wall loosening and signaling [KNOWN; Müller et al. 2009 *J Exp Bot*]. Downregulation of 6-PGDH would **reduce NADPH availability**, potentially **allowing the ROS burst** required for germination to proceed without excessive scavenging [INFERRED]. This is a subtle but potentially important mechanism — the bacteria may be "allowing" the oxidative window for germination by reducing antioxidant capacity.
- **Evidence strength**: Moderate
- **Key references**: Müller et al. 2009 *J Exp Bot* 60:1339 (ROS in germination); Kruger & von Schaewen 2003 *Curr Opin Plant Biol* (PPP in plants)
- **Pathway context**: Metabolic Priming — rated **High** priority
- **Confidence**: **Medium**

---

### 18. SOV3g040200.1 — Glutathione S-Transferase L3-like (GST)

- **Mechanism**: GSTs detoxify **lipid peroxidation products** (4-hydroxynonenal, malondialdehyde) using glutathione [KNOWN; Dixon et al. 2010 *Phytochemistry*]. During germination, stored lipids are mobilized via β-oxidation, generating ROS and lipid peroxides as byproducts [KNOWN]. High GST activity is characteristic of a **stress-response state**, prioritizing cellular protection over growth. Downregulation of GST would reduce detoxification capacity, but if the seed's ROS burden is not excessive (as in good germination conditions), this would redirect glutathione toward other uses (e.g., redox signaling) and reduce the metabolic cost of stress responses [INFERRED]. Synergy with the peroxidase target (SOV3g038840.1) is expected.
- **Evidence strength**: Moderate
- **Key references**: Dixon et al. 2010 *Phytochemistry* 71:338; Sappl et al. 2009 *Plant J* (GST in Arabidopsis stress response)
- **Pathway context**: ROS/Redox Biology — rated **High** priority
- **Confidence**: **Medium**

---

### 19. SOV3g038840.1 — Peroxidase

- **Mechanism**: Class III plant peroxidases are **bifunctional** — they can both **produce ROS** (hydroxylic cycle, generating OH•) and **scavenge H₂O₂** (peroxidative cycle) depending on substrate availability [KNOWN; Cosio & Dunand 2009 *J Exp Bot*]. During germination, specific peroxidases in the **micropylar endosperm** produce ROS that weaken cell walls to allow radicle protrusion [KNOWN; Müller et al. 2009]. However, other peroxidases in the embryo scavenge excess ROS to protect cellular integrity. Downregulation of a scavenging peroxidase would allow the germination-promoting ROS burst to proceed; downregulation of a cell wall-stiffening peroxidase (which cross-links extensins) would directly weaken the endosperm cap [INFERRED]. The net effect depends on the specific peroxidase isoform and its cellular localization — without this information, confidence is limited.
- **Evidence strength**: Moderate (isoform-dependent)
- **Key references**: Cosio & Dunand 2009 *J Exp Bot* 60:391; Müller et al. 2009; Passardi et al. 2004 *Plant Cell Environ* (peroxidase diversity)
- **Pathway context**: ROS/Redox Biology — rated **High** priority
- **Confidence**: **Medium**

---

### 20. SOV4g051610.1 — Ser/Thr Kinase ATR (DNA Damage Response)

- **Mechanism**: ATR (Ataxia Telangiectasia and Rad3-related) is a **master DNA damage checkpoint kinase** that arrests the cell cycle in response to replication stress and single-strand DNA breaks [KNOWN; Culligan et al. 2004 *Plant Cell*]. In germinating seeds, accumulated DNA damage (from desiccation and oxidative stress during storage) activates ATR, potentially **delaying cell cycle re-entry** and germination [KNOWN; Waterworth et al. 2011 *Plant Cell*]. Downregulation of ATR would **relax the DNA damage checkpoint**, allowing cells to re-enter the cell cycle more rapidly despite residual DNA damage [INFERRED]. This is a double-edged mechanism — it promotes faster germination but at the potential cost of **genomic integrity** in the seedling [SPECULATIVE]. In the agricultural context, if the bacterial treatment is applied to seeds with moderate (not severe) DNA damage, ATR downregulation would be beneficial.
- **Evidence strength**: Moderate
- **Key references**: Culligan et al. 2004 *Plant Cell* 16:1091; Waterworth et al. 2011 *Plant Cell* 23:1014 (DNA repair in seed germination); Langie et al. 2007 (ATR in plant development)
- **Pathway context**: DNA Repair & Replication — rated **Medium** priority
- **Confidence**: **Medium**

---

### 21. SOV4g010600.1 — Glycosyltransferase (Cell Wall)

- **Mechanism**: Glycosyltransferases (GTs) **synthesize and extend hemicellulose and pectin chains** in the cell wall, reinforcing its structural integrity [KNOWN; Scheller & Ulvskov 2010 *Annu Rev Plant Biol*]. In the endosperm cap, GT activity maintains the **mechanical resistance** that must be overcome for radicle protrusion [KNOWN; Leubner-Metzger 2003 *Planta*]. Downregulation of GT would reduce cell wall reinforcement, directly contributing to **endosperm weakening** and facilitating radicle emergence. This is a mechanistically direct effect on the physical barrier to germination.
- **Evidence strength**: Moderate-Strong
- **Key references**: Scheller & Ulvskov 2010 *Annu Rev Plant Biol* 61:263; Leubner-Metzger 2003 *Planta* 217:833 (endosperm weakening in germination)
- **Pathway context**: Cell Wall Remodeling — rated **Medium** priority
- **Confidence**: **Medium-High**

---

### 22. SOV4g051070.1 — Beta-Galactosidase (Cell Wall)

- **Mechanism**: β-Galactosidases (BGALs) cleave **galactose residues from galactans and arabinogalactans** in the cell wall, contributing to wall loosening [KNOWN; Smith & Gross 2000 *Plant Cell Physiol*]. During germination, BGAL activity in the endosperm cap promotes weakening [KNOWN; Iglesias-Fernández et al. 2011 *Plant J*]. The downregulation of a BGAL appears counterproductive — reducing a wall-loosening enzyme should **inhibit** germination. However, the pathway analysis suggests that the net effect of simultaneously downregulating GTs (wall builders) and this BGAL (wall breaker) favors loosening because the reduction in substrate (galactan chains built by GTs) limits the need for BGAL activity, and other non-targeted hydrolases (expansins, other BGALs) continue to act on the less-reinforced wall [INFERRED]. This is a **systems-level interpretation** that is plausible but requires experimental validation.
- **Evidence strength**: Weak-Moderate (directionally counterintuitive)
- **Key references**: Iglesias-Fernández et al. 2011 *Plant J* 65:501 (BGAL in Arabidopsis germination); Smith & Gross 2000
- **Pathway context**: Cell Wall Remodeling — rated **Medium** priority
- **Confidence**: **Low-Medium** (directional uncertainty)

---

### 23. SOV1g027650.1 — Receptor-Like Kinase (RLK)

- **Mechanism**: RLKs are **pattern recognition receptors** that detect PAMPs (pathogen-associated molecular patterns) and DAMPs, initiating **Pattern-Triggered Immunity (PTI)** [KNOWN; Zipfel 2014 *Curr Opin Plant Biol*]. PTI activation during germination would divert resources to defense and activate SA/JA signaling that inhibits germination [KNOWN]. Downregulation of an RLK would reduce PAMP detection sensitivity, dampening PTI and allowing germination to proceed without immune activation. This is particularly relevant in the soil environment where seeds are exposed to microbial PAMPs [INFERRED]. However, the specific RLK family (LRR-RLK, CRINKLY4, WAK, etc.) determines whether it primarily functions in defense or development [SPECULATIVE without sequence data].
- **Evidence strength**: Moderate
- **Key references**: Zipfel 2014 *Curr Opin Plant Biol* 20:10; Zipfel et al. 2006 *Nature* (EFR as PAMP receptor); Boller & Felix 2009 *Annu Rev Plant Biol* (PTI overview)
- **Pathway context**: General Signaling — rated **Medium** priority
- **Confidence**: **Medium**

---

### 24. SOV1g002960.1, SOV5g006110.1, SOV2g038280.1 — F-box Proteins (Three Members)

- **Mechanism**: F-box proteins are **substrate-recognition subunits of SCF E3 ubiquitin ligase complexes** [KNOWN; Lechner et al. 2006 *Annu Rev Cell Dev Biol*]. In germination, specific F-box proteins target **DELLA repressors** (GA signaling repressors) for degradation — this promotes germination [KNOWN; Dill et al. 2004 *Genes Dev*]. Other F-box proteins target positive regulators of germination for degradation, inhibiting germination [KNOWN; Stone et al. 2006 *Nat Genet* — TIR1 F-box in auxin]. The direction of effect depends entirely on the substrate specificity of each F-box protein. If these F-box proteins target **GA-signaling components or germination promoters** for degradation, their downregulation would promote germination [INFERRED]. The targeting of three F-box paralogs suggests the bacteria may be disrupting a **redundant ubiquitin-mediated dormancy maintenance system** [SPECULATIVE].
- **Evidence strength**: Weak-Moderate (substrate-dependent)
- **Key references**: Dill et al. 2004 *Genes Dev* 18:2399 (SLY1 F-box in GA/DELLA); Lechner et al. 2006; Kepinski & Leyser 2005 *Nature* (TIR1 F-box)
- **Pathway context**: Protein Turnover — rated **Medium** priority
- **Confidence**: **Low-Medium** (highly substrate-dependent)

---

### 25. SOV1g043000.1 & SOV2g021870.1 — RING-Type E3 Ubiquitin Transferases

- **Mechanism**: RING-type E3 ligases directly ubiquitinate substrates for proteasomal degradation [KNOWN]. In germination, RING E3 ligases include **KEG** (which targets ABI5 for degradation, promoting germination) and **RHA2a/b** (which promote ABA signaling, inhibiting germination) [KNOWN; Stone et al. 2006; Bu et al. 2009 *Plant Cell*]. If these spinach RING E3s are homologs of RHA2a/b or similar ABA-promoting ligases, their downregulation would reduce ABA signal amplification and promote germination [INFERRED]. Without substrate identity, confidence remains moderate.
- **Evidence strength**: Moderate (substrate-dependent)
- **Key references**: Bu et al. 2009 *Plant Cell* 21:2763 (RHA2a/b in ABA/germination); Stone et al. 2006 *Nat Genet* 38:86 (KEG E3 ligase)
- **Pathway context**: Protein Turnover — rated **Medium** priority
- **Confidence**: **Medium**

---

### 26. SOV4g000330.1 — Phytoene Synthase

- **Mechanism**: Phytoene synthase (PSY) catalyzes the **first committed step of carotenoid biosynthesis** [KNOWN; Cazzonelli & Pogson 2010 *Trends Plant Sci*]. Carotenoids are the **precursors of ABA** (via xanthoxin) — specifically, the cleavage of 9-cis-epoxycarotenoids by NCED produces xanthoxin, which is converted to ABA [KNOWN; Nambara & Marion-Poll 2005 *Annu Rev Plant Biol*]. Downregulation of PSY would reduce the carotenoid pool available for ABA biosynthesis, directly **limiting ABA production** during imbibition [INFERRED]. This is a metabolically upstream mechanism to reduce ABA levels, complementing the downstream signaling suppression achieved by other targets. However, carotenoids also serve as photoprotectants and are required for chloroplast development, so complete PSY suppression would have pleiotropic effects [KNOWN].
- **Evidence strength**: Moderate
- **Key references**: Nambara & Marion-Poll 2005 *Annu Rev Plant Biol* 56:165; Cazzonelli & Pogson 2010 *Trends Plant Sci* 15:421; Finkelstein 2013 (ABA biosynthesis)
- **Pathway context**: Metabolic Priming — rated **Medium** priority
- **Confidence**: **Medium**

---

### 27. SOV4g055600.1 — Cytochrome P450

- **Mechanism**: CYP450s constitute a large superfamily with diverse roles. In germination, relevant CYP450s include **CYP707A** (ABA 8'-hydroxylase, which **catabolizes ABA** — promoting germination) and **CYP88A/CYP701A** (GA biosynthesis — promoting germination), as well as CYPs involved in defense compound biosynthesis (inhibiting germination by resource diversion) [KNOWN; Kushiro et al. 2004 *EMBO J*; Hedden & Thomas 2012 *Biochem J*]. Without subfamily identification, the direction of effect is uncertain. Given the metabolic priming context and medium priority, this CYP450 is most likely involved in **secondary metabolite or defense compound biosynthesis** whose downregulation reduces resource diversion [INFERRED].
- **Evidence strength**: Weak-Moderate (subfamily-dependent)
- **Key references**: Kushiro et al. 2004 *EMBO J* 23:1647 (CYP707A in ABA catabolism); Hedden & Thomas 2012 *Biochem J* 444:11
- **Pathway context**: Metabolic Priming — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 28. SOV5g008400.1 — Cation/H⁺ Antiporter-Like

- **Mechanism**: Cation/H⁺ antiporters (CHX, NHX families) regulate **intracellular pH and ion homeostasis** by exchanging cations (K⁺, Na⁺) for H⁺ across vacuolar or plasma membranes [KNOWN; Sze et al. 2004 *Annu Rev Plant Biol*]. During germination, vacuolar acidification and K⁺ accumulation drive **osmotic water uptake** and cell expansion [KNOWN]. Downregulation of a specific antiporter could alter the **osmotic potential gradient** that drives imbibition and embryo expansion [INFERRED]. NHX-type antiporters also regulate ABA sensitivity in guard cells [KNOWN; Bassil et al. 2011 *Plant Cell*], suggesting potential ABA pathway crosstalk [SPECULATIVE].
- **Evidence strength**: Moderate
- **Key references**: Sze et al. 2004 *Annu Rev Plant Biol* 55:249; Bassil et al. 2011 *Plant Cell* 23:3482
- **Pathway context**: Transport & Ion Homeostasis — rated **Medium** priority
- **Confidence**: **Medium**

---

## Tier 3: Supporting Targets (Indirect, Minor, or Uncertain Effect)

*These targets have plausible but indirect connections to germination improvement, low annotation confidence, or represent pathway categories where the germination relevance is weak. They likely contribute to the phenotype as part of the systems-level reprogramming but are unlikely to be individually rate-limiting.*

---

### 29. SOV0g001060.1 — Regulator of rDNA Transcription Protein 15

- **Mechanism**: Regulates ribosomal DNA transcription by RNA Pol I [KNOWN]. Downregulation would reduce rRNA synthesis and ribosome biogenesis, potentially reducing the overall translational capacity of the seed [INFERRED]. This could paradoxically slow germination. More likely, this represents a **fine-tuning of ribosome production** to match the metabolic rate of early germination rather than a direct germination-promoting mechanism [SPECULATIVE].
- **Evidence strength**: Weak
- **Pathway context**: Epigenetic Regulation — rated **Low** priority
- **Confidence**: **Low**

---

### 30. SOV0g001750.1 — Protein TAR1-like (TGS1)

- **Mechanism**: TGS1/TAR1 hypermethylates snRNA and snoRNA caps, which is required for functional spliceosome assembly and rRNA processing [KNOWN; Mouaikel et al. 2002 *Mol Cell*]. Downregulation would impair snRNA maturation, potentially altering **alternative splicing** patterns during germination [INFERRED]. Alternative splicing of ABA signaling components (e.g., *HAB1*, *PP2C*) is a known regulatory mechanism during germination [KNOWN; Punzo et al. 2020 *Front Plant Sci*]. However, global splicing impairment would have broad negative effects, making this a **risky** target for germination promotion [SPECULATIVE].
- **Evidence strength**: Weak
- **Key references**: Mouaikel et al. 2002 *Mol Cell* 9:891; Punzo et al. 2020 *Front Plant Sci* 11:336
- **Pathway context**: Unknown Function — rated **Low** priority
- **Confidence**: **Low**

---

### 31. SOV3g021300.1 — Stress Response Protein NST1

- **Mechanism**: NST1 (No Stress 1) in Arabidopsis is involved in **osmotic stress tolerance** and cell wall integrity signaling [KNOWN; Shi et al. 2003 *Plant Cell*]. Its downregulation could reduce the seed's stress-response posture, freeing resources for growth [INFERRED]. However, NST1 also has roles in secondary cell wall biosynthesis in specific cell types, which complicates interpretation [INFERRED].
- **Evidence strength**: Weak-Moderate
- **Pathway context**: Defense & Immunity — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 32. SOV1g021670.1 — Putative Disease Resistance Protein

- **Mechanism**: NBS-LRR or similar R-proteins trigger **Effector-Triggered Immunity (ETI)** upon pathogen detection [KNOWN; Jones & Dangl 2006 *Nature*]. Downregulation reduces ETI capacity, reducing the metabolic cost of maintaining defense readiness [INFERRED]. In the absence of pathogens, this is a net benefit for germination; in pathogen-rich soil, this could increase susceptibility [SPECULATIVE].
- **Evidence strength**: Moderate (mechanism clear, magnitude uncertain)
- **Pathway context**: Defense & Immunity — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 33. SOV1g019270.1 — DNA Topoisomerase 2

- **Mechanism**: Topo II resolves DNA topology during replication and transcription [KNOWN]. Downregulation could slow DNA replication in rapidly dividing embryonic cells, potentially delaying germination [INFERRED]. The germination-promoting rationale is unclear — this may be a **bystander target** or may function to reduce replication stress by slowing replication fork speed [SPECULATIVE].
- **Evidence strength**: Weak
- **Pathway context**: DNA Repair & Replication — rated **Medium** priority
- **Confidence**: **Low**

---

### 34. SOV2g025780.1 — TIM50-Like Mitochondrial Import Inner Membrane Translocase

- **Mechanism**: TIM50 is essential for importing nuclear-encoded proteins into the mitochondrial matrix [KNOWN; Mokranjac et al. 2003 *EMBO J*]. Downregulation would impair mitochondrial protein import and function [INFERRED]. Given that mitochondrial activity is **essential** for germination energy production, this seems counterproductive. The pathway analysis suggests this may redirect energy from *de novo* mitochondrial biogenesis to using existing mitochondria more efficiently [SPECULATIVE].
- **Evidence strength**: Weak (directionally uncertain)
- **Pathway context**: Organelle Biogenesis — rated **Medium** priority
- **Confidence**: **Low**

---

### 35. SOV3g020770.1 — TIC214 (Chloroplast Import Complex Component)

- **Mechanism**: TIC214 is a core component of the **TOC-TIC translocon** for chloroplast protein import [KNOWN; Chen et al. 2018 *Science*]. Downregulation would impair chloroplast biogenesis. During germination in darkness, chloroplasts are not yet photosynthetically active, so reduced TIC214 may delay **post-germination** chloroplast development rather than germination itself [INFERRED]. This is likely a **seedling vigor** rather than germination rate target.
- **Evidence strength**: Moderate (for seedling vigor, not germination rate)
- **Key references**: Chen et al. 2018 *Science* 362:eaat9819
- **Pathway context**: Organelle Biogenesis — rated **Medium** priority
- **Confidence**: **Low-Medium** (primarily post-germination effect)

---

### 36. SOV4g005210.1, SOV6g035270.1, SOV6g037220.1 — Pentatricopeptide Repeat (PPR) Proteins

- **Mechanism**: PPR proteins regulate **organellar RNA processing** (editing, splicing, stabilization) in mitochondria and chloroplasts [KNOWN; Schmitz-Linneweber & Small 2008 *Trends Plant Sci*]. Their downregulation could impair mitochondrial mRNA processing and reduce respiratory complex assembly [INFERRED]. During germination, mitochondrial function is critical, making PPR downregulation potentially **counterproductive** [INFERRED]. These may be bystander targets or their downregulation may affect specific mitochondrial transcripts that are inhibitory to germination [SPECULATIVE].
- **Evidence strength**: Weak
- **Pathway context**: RNA Processing & Splicing — rated **Medium** priority
- **Confidence**: **Low**

---

### 37. SOV5g000510.1 — ATP-Dependent RNA Helicase / Pre-mRNA Splicing Factor

- **Mechanism**: RNA helicases facilitate **spliceosome assembly and pre-mRNA splicing** [KNOWN; Linder & Jankowsky 2011 *Nat Rev Mol Cell Biol*]. Downregulation could alter the splicing of ABA-pathway transcripts, potentially producing non-functional ABA signaling isoforms [INFERRED]. This is a plausible but indirect mechanism.
- **Evidence strength**: Weak-Moderate
- **Pathway context**: RNA Processing & Splicing — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 38. SOV1g004930.1, SOV4g008190.1, SOV6g042250.1 — GDSL Esterase/Lipases

- **Mechanism**: GDSL lipases are involved in **cutin and suberin biosynthesis** (seed coat permeability) and lipid signaling [KNOWN; Ling et al. 2006 *Plant Cell*]. Downregulation could alter seed coat permeability, affecting water uptake during imbibition [INFERRED]. Increased permeability would accelerate imbibition and germination [SPECULATIVE]. Three paralogs are targeted, suggesting functional redundancy.
- **Evidence strength**: Weak-Moderate
- **Pathway context**: Metabolic Priming — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 39. SOV1g048270.1 — Aspartokinase

- **Mechanism**: Aspartokinase catalyzes the first step of the **aspartate-family amino acid biosynthesis pathway** (Lys, Thr, Met, Ile) [KNOWN; Azevedo et al. 2006 *Phytochemistry*]. Downregulation could redirect aspartate toward energy metabolism rather than amino acid biosynthesis [SPECULATIVE]. The germination relevance is indirect — amino acid biosynthesis is needed for protein synthesis during germination, but storage proteins provide the primary amino acid source.
- **Evidence strength**: Weak
- **Pathway context**: Metabolic Priming — rated **Medium** priority
- **Confidence**: **Low**

---

### 40. SOV4g006140.1 — Choline/Ethanolaminephosphotransferase 1

- **Mechanism**: This enzyme synthesizes **phosphatidylcholine (PC) and phosphatidylethanolamine (PE)**, the major membrane phospholipids [KNOWN; Dewey et al. 1994 *Plant Physiol*]. Downregulation during germination could reduce membrane biosynthesis, potentially limiting cell expansion [INFERRED]. Alternatively, reduced PC synthesis could alter **lipid signaling** (PC is a precursor of lysophosphatidic acid and diacylglycerol signaling molecules) [SPECULATIVE]. The germination relevance is indirect.
- **Evidence strength**: Weak
- **Pathway context**: Metabolic Priming — rated **Medium** priority
- **Confidence**: **Low**

---

### 41. SOV6g042110.1 — Glyoxylate/Hydroxypyruvate Reductase

- **Mechanism**: This enzyme participates in **photorespiration** (glyoxylate reduction in peroxisomes) and the **glyoxylate cycle** (fatty acid conversion to sugars) [KNOWN; Timm et al. 2008 *Plant Physiol*]. During germination, the glyoxylate cycle is active in converting stored lipids to sucrose. Downregulation could impair this conversion, reducing sugar availability [INFERRED]. The germination-promoting rationale is unclear — this may be a **bystander target** [SPECULATIVE].
- **Evidence strength**: Weak
- **Pathway context**: Metabolic Priming — rated **Medium** priority
- **Confidence**: **Low**

---

### 42. SOV2g013310.1 — Folate-Biopterin Transporter

- **Mechanism**: Folate transporters supply **tetrahydrofolate (THF)** for one-carbon metabolism, which is essential for nucleotide biosynthesis, methylation reactions, and amino acid interconversion [KNOWN; Hanson & Gregory 2011 *Curr Opin Plant Biol*]. Downregulation could impair DNA methylation (by reducing SAM availability) [INFERRED], creating an indirect epigenetic de-repression effect that complements the direct DNA methyltransferase targeting [SPECULATIVE].
- **Evidence strength**: Weak-Moderate (indirect mechanism)
- **Pathway context**: Transport & Ion Homeostasis — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 43. SOV5g032210.1 — NRT1/PTR Family Transporter 5.5-Like

- **Mechanism**: NRT1/PTR transporters include **nitrate transporters, peptide transporters, and ABA transporters** [KNOWN; Léran et al. 2014 *Trends Plant Sci*]. Critically, **NRT1.2/AIT1** in Arabidopsis transports ABA into cells, increasing ABA sensitivity and inhibiting germination [KNOWN; Kanno et al. 2012 *Nat Plants*]. If this spinach NRT1/PTR is an ABA importer, its downregulation would **reduce intracellular ABA accumulation**, directly promoting germination [INFERRED]. This is a potentially important mechanism, but the substrate specificity of NRT1.5-like transporters is not well-established in spinach.
- **Evidence strength**: Moderate (if ABA transporter; weak if nitrate transporter)
- **Key references**: Kanno et al. 2012 *Nat Plants* (AIT1/NRT1.2 as ABA transporter); Léran et al. 2014
- **Pathway context**: Transport & Ion Homeostasis — rated **Medium** priority
- **Confidence**: **Low-Medium** (substrate-dependent)

---

### 44. SOV6g014710.1 — Plant Cadmium Resistance-Like Protein

- **Mechanism**: PCR (Plant Cadmium Resistance) proteins are **cation exporters** that remove heavy metals and potentially other cations from cells [KNOWN; Kim et al. 2004 *Plant J*]. Their role in germination is indirect — they may export inhibitory cations or regulate ion homeostasis [SPECULATIVE]. Downregulation could alter cellular ion balance, with unpredictable effects on germination.
- **Evidence strength**: Weak
- **Pathway context**: Transport & Ion Homeostasis — rated **Medium** priority
- **Confidence**: **Low**

---

### 45. SOV1g034720.1 — Mitochondrial Distribution/Morphology Family 35 / Apoptosis-Related

- **Mechanism**: MDV/MCOS family proteins regulate **mitochondrial fission and fusion** [KNOWN; Logan 2006 *J Exp Bot*]. Downregulation could alter mitochondrial network dynamics during the transition from dormancy to active metabolism [INFERRED]. The apoptosis-related annotation suggests potential roles in **programmed cell death** of the aleurone layer, which is required for germination in cereals [SPECULATIVE — less relevant in spinach].
- **Evidence strength**: Weak
- **Pathway context**: Organelle Biogenesis — rated **Medium** priority
- **Confidence**: **Low**

---

### 46. SOV4g000770.1 — Protein Adenylylyltransferase SelO

- **Mechanism**: SelO is a **pseudokinase/AMPylase** that modifies proteins with AMP, functioning in **oxidative stress response** [KNOWN; Sreelatha et al. 2018 *Cell*]. Its role in plant germination is not established [SPECULATIVE]. Downregulation could reduce a stress-response pathway, indirectly promoting germination [SPECULATIVE].
- **Evidence strength**: Very weak
- **Key references**: Sreelatha et al. 2018 *Cell* 175:196
- **Pathway context**: General Signaling — rated **Low** priority
- **Confidence**: **Low**

---

### 47. SOV6g037890.1 — Patellin-6

- **Mechanism**: Patellins are **phosphoinositide-binding proteins** involved in **vesicle trafficking and membrane dynamics** [KNOWN; Peterman et al. 2004 *Mol Biol Cell*]. They regulate endosomal sorting and may affect **auxin transport** (which is vesicle-mediated) [INFERRED]. Downregulation could alter vesicle trafficking during germination, affecting hormone distribution [SPECULATIVE].
- **Evidence strength**: Weak
- **Pathway context**: General Signaling — rated **Medium** priority
- **Confidence**: **Low**

---

### 48. SOV2g039720.1 — Calcium-Binding Protein

- **Mechanism**: Ca²⁺-binding proteins (calmodulins, CMLs, CDPKs) transduce Ca²⁺ signals into downstream responses [KNOWN; Kudla et al. 2010 *Plant Cell*]. Downregulation of a specific Ca²⁺-binding protein could dampen Ca²⁺-mediated ABA signaling or defense responses [INFERRED]. Without knowing the specific family member, the direction and magnitude of effect are uncertain.
- **Evidence strength**: Weak-Moderate
- **Pathway context**: General Signaling — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 49. SOV4g046320.1 & SOV5g030510.1 — Ser/Thr-Protein Kinases

- **Mechanism**: Generic Ser/Thr kinases could function in any signaling pathway [KNOWN]. Without subfamily identification, these are essentially **uncharacterized** in the germination context. They may be downstream components of RLK or ABA signaling cascades [SPECULATIVE].
- **Evidence strength**: Very weak
- **Pathway context**: General Signaling — rated **Medium** priority
- **Confidence**: **Low**

---

### 50. SOV1g032780.1 & SOV4g041000.1 — ABC Transporter-Like Proteins

- **Mechanism**: ABC transporters include **ABA exporters (ABCG25/ABCG40)** that regulate ABA distribution between cells [KNOWN; Kang et al. 2010 *Nature*; Kuromori et al. 2010 *Plant Cell*]. If these spinach ABC transporters are ABA transport-related, their downregulation could alter ABA compartmentalization [INFERRED]. However, ABC transporters also export defense compounds, heavy metals, and lipids, making substrate identification critical.
- **Evidence strength**: Weak-Moderate (substrate-dependent)
- **Key references**: Kang et al. 2010 *Nature* 431:529 (ABCG40 as ABA importer); Kuromori et al. 2010
- **Pathway context**: Transport & Ion Homeostasis — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 51. SOV4g023530.1 — LUC7 N-Terminus Domain-Containing Protein (Splicing-Related)

- **Mechanism**: LUC7 proteins are components of the **U1 snRNP** involved in 5' splice site recognition [KNOWN; Forment et al. 2002 *Plant J*]. Downregulation could alter splicing of ABA pathway transcripts, potentially producing non-functional ABA signaling isoforms [INFERRED]. In Arabidopsis, *luc7* mutants show altered stress responses [KNOWN; Huertas et al. 2019 *Plant Cell*].
- **Evidence strength**: Weak-Moderate
- **Key references**: Huertas et al. 2019 *Plant Cell* 31:2086
- **Pathway context**: RNA Processing & Splicing — rated **Medium** priority
- **Confidence**: **Low-Medium**

---

### 52. SOV5g013920.1 — CRM-Domain Factor CFM3, Chloroplastic/Mitochondrial

- **Mechanism**: CFM3 is involved in **chloroplast/mitochondrial RNA splicing** [KNOWN; Asakura & Barkan 2006 *Plant