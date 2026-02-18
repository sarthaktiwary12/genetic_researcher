# Maize Grain Filling MoA Dossier: From Seed Imbibition to Kernel Composition

## How Early-Stage Gene Downregulation Translates to Grain Filling, Kernel Composition, and Yield

**Prepared:** 2026-02-18
**Classification:** Internal Research Supplement to FINAL_REPORT_MAIZE.md
**Evidence Labeling:** [KNOWN] = published peer-reviewed literature; [INFERRED] = logical deduction from conserved biology and target annotations; [SPECULATIVE] = hypothesis requiring experimental validation
**Scope:** This dossier addresses the central translational question: How can gene downregulation during a 4-8 hour seed soak propagate forward through vegetative development to affect grain filling, kernel composition, and yield at R1-R6?

---

## Table of Contents

1. [Conceptual Framework: Bridging Germination to Grain Fill](#1-conceptual-framework)
2. [Comprehensive Grain Filling Pathway Analysis](#2-grain-filling-pathway-analysis)
3. [Sweetness (Sucrose) and Starch Prediction](#3-sweetness-and-starch-prediction)
4. [Protein Content Prediction](#4-protein-content-prediction)
5. [Quantitative Prediction Ranges](#5-quantitative-prediction-ranges)
6. [Synthesis: Target-to-Grain-Fill Connectivity Map](#6-synthesis)
7. [References](#7-references)

---

## 1. Conceptual Framework: Bridging Germination to Grain Fill

### 1.1 The Temporal Gap Problem

The RNA drug is applied at seed imbibition (0-8 hours). Grain filling occurs at R1-R6 (approximately 55-100 days after planting). This represents a temporal gap of 55-100 days. Three mechanistic bridges could connect early gene downregulation to late-season phenotypes:

**Bridge 1: Epigenetic Memory / Transgenerational Stress Priming**
[KNOWN] Seed priming can induce epigenetic changes (DNA methylation, histone modifications, small RNA profiles) that persist beyond the initial treatment window and affect later developmental stages. Louis (2023) demonstrated that seed priming can retain stress tolerance across developmental stages and even subsequent generations through epigenetic modifications. In *Zea mays*, transgenerational memory of heat and drought stress has been linked to differential expression of small RNAs targeting stress-responsive transcription factors, contributing to improved seedling vigor and root development in progeny.

[INFERRED] If the tRF RNA drug triggers RdDM (RNA-directed DNA methylation) at target loci during imbibition, the resulting methylation marks could persist through cell divisions and affect gene expression at grain filling. This is the strongest mechanistic bridge but requires experimental validation of persistent epigenetic marks.

**Bridge 2: Early Vigor Advantage / Compound Growth Effect**
[KNOWN] Seeds that germinate faster and establish more robust seedlings capture more light, water, and nutrients early in the season, creating a compound growth advantage that persists through the reproductive phase. A 2023 Frontiers study showed that biostimulant seed treatments increased maize grain yield by 5.1%, with the effect attributable to early vigor translating to better canopy establishment and more efficient resource capture during grain fill.

[INFERRED] Faster germination (Theme 1: ABA derepression) and enhanced seedling vigor (Theme 5: AHL9-mediated auxin derepression) would establish a larger, more vigorous plant that captures more photosynthate during grain filling. This is the most conservative and well-supported bridge.

**Bridge 3: Persistent Transcriptomic Reprogramming**
[SPECULATIVE] If the exRNA-mediated silencing triggers secondary siRNA amplification through the plant's RDR (RNA-dependent RNA polymerase) machinery, the silencing signal could be amplified and maintained beyond the initial treatment window. In maize, the RNAi toolkit includes functional RDR genes capable of signal amplification. However, the duration of amplified silencing from a single exogenous trigger in maize seeds is unknown and could range from hours to weeks.

### 1.2 Most Likely Scenario

The most scientifically conservative explanation for any grain-filling effects is **Bridge 2: the compound growth effect**. A plant that germinates 12-24 hours earlier, establishes a deeper root system by V3, and captures 3-5% more intercepted radiation through V6-VT will have more photosynthate available to partition to ears during grain fill. This does NOT require persistent gene silencing -- it requires only the initial germination/vigor advantage to propagate through normal developmental physiology.

---

## 2. Grain Filling Pathway Analysis

### 2.1 Overview of Maize Grain Filling

[KNOWN] Maize grain filling spans stages R1 (silking) through R6 (physiological maturity), approximately 45-65 days. The mature kernel comprises:
- **Starch**: 70-75% of dry weight (endosperm)
- **Protein**: 8-12% of dry weight (mainly zeins in endosperm; globulins/albumins in embryo)
- **Oil**: 3-6% of dry weight (mainly in embryo/scutellum)
- **Fiber**: 2-3% of dry weight (pericarp)
- **Sugars**: 1-3% of dry weight (sucrose, glucose, fructose)

The grain filling process requires: (a) photosynthate production in source leaves, (b) phloem loading and long-distance transport, (c) phloem unloading at the ear, (d) post-phloem transport through the basal endosperm transfer layer (BETL), and (e) metabolic conversion to starch, protein, and oil within the endosperm and embryo.

### 2.2 Sucrose Transport to the Ear: Phloem Unloading Mechanisms

[KNOWN] Sucrose arrives at the developing maize kernel via the phloem. At the maternal-filial boundary (the pedicel-BETL interface), phloem unloading switches from symplastic to apoplastic. This is a critical control point for sink strength.

**Key Steps:**
1. **Phloem unloading** into the pedicel apoplast (symplastic in early development, apoplastic at grain fill)
2. **Sucrose hydrolysis** by cell wall invertase (INCW2/Miniature1) in the pedicel region, generating glucose + fructose
3. **Hexose import** across the BETL plasma membrane via SWEET transporters and hexose transporters
4. **Re-synthesis** to sucrose or direct use for starch biosynthesis in endosperm cells

**Connection to target genes:**

| Target Gene | Connection to Sucrose Transport | Evidence Level |
|-------------|--------------------------------|----------------|
| HEX6 (hexokinase) | After hexose import, HXK phosphorylates glucose to G6P, feeding glycolysis and starch biosynthesis. HXK also acts as a sugar sensor regulating gene expression. If HEX6 is persistently downregulated, sugar sensing would be attenuated, potentially altering source-sink signaling. | [INFERRED] Indirect. HXK family redundancy (9 members in maize) buffers against single-gene effects. |
| NPF15 (NRT1/PTR transporter) | NPF transporters have been shown to transport diverse substrates. ZmNPF7.9 (SUGCAR1) was recently identified as a sugar transporter critical for grain filling, expressed in BETL. If NPF15 has sugar or peptide transport activity in the pedicel/BETL, its modulation could affect nutrient flux. The dek407 mutant (encoding NPF1.5) shows reduced kernel size and delayed grain filling. | [SPECULATIVE] NPF15 is annotated as NPF4.6/AIT1-like (ABA transporter), not a sugar transporter. But NPF family substrate promiscuity means this cannot be excluded. |
| MYBR64 (MYB-related TF) | ZmMYBR29, a MYB-related TF homologous to MYBR64, was shown in 2024 to be specifically expressed in the basal cellularized endosperm and required for grain filling. Loss-of-function zmmybr29 mutant showed 26.7% decrease in average grain filling rate and smaller kernels. ZmMYBR29 regulates genes involved in starch and sucrose metabolism. | [KNOWN/INFERRED] This is a critical finding. If MYBR64 is orthologous or paralogous to ZmMYBR29, its downregulation during germination could have significant implications for grain filling IF the downregulation persists. However, ZmMYBR29 loss DECREASES grain filling, so downregulating a homolog would be DETRIMENTAL to grain fill, not beneficial. |

### 2.3 SWEET Transporters in Maize (ZmSWEET Family)

[KNOWN] The SWEET (Sugars Will Eventually be Exported Transporters) family facilitates sugar transport across membranes. In maize kernel development:

- **ZmSWEET4c**: The critical hexose transporter at the BETL. Mediates transepithelial hexose transport at the entry point of nutrients into the seed. Mutants are defective in seed filling. ZmSWEET4c shows signatures of selection during domestication, suggesting it was recruited to enhance sugar import into the endosperm (Sosso et al., 2015, *Nature Genetics*).
- **ZmSWEET11**: Constitutively expressed in BETL.
- **ZmSWEET3a/13a**: Expressed at the grain set stage.
- **ZmSWEET6b, 13b, 14b, 15a**: Expressed during germination.

**Connection to target genes:**

| Target Gene | Connection to SWEET Transporters | Evidence Level |
|-------------|----------------------------------|----------------|
| ABI40 (VP1-like) | VP1/ABI3 regulates embryo maturation programs including scutellum development. VP1 directly regulates intra-kernel protein reallocation through scutellum development (Yang et al., 2019, *Plant Cell*). VP1 loss affects nutrient assimilation pathways in the kernel. ABI40 downregulation could alter the maturation program that establishes BETL identity and SWEET transporter expression patterns. | [SPECULATIVE] VP1 primarily regulates embryo programs; SWEET expression in BETL is regulated by other TFs (e.g., MRP1/ZmMYBR29). |
| AHL9 (AT-hook protein) | AHL proteins remodel chromatin at S/MAR regions. If AHL9 targets include SWEET gene promoters, its downregulation could derepress SWEET expression. | [SPECULATIVE] No direct evidence links AHL9 to SWEET regulation. |

**Assessment:** None of the 20 target genes directly encode SWEET transporters or their known regulators. Any effect on SWEET-mediated sugar transport would be highly indirect.

### 2.4 SUT/SUC Sucrose Transporters

[KNOWN] Seven genes encoding sucrose transporters exist in maize: ZmSUT1-ZmSUT7. ZmSUT1 is expressed in the BETL and functions in sucrose retrieval and phloem loading/unloading. SUT1 is critical for maintaining sucrose gradients that drive bulk flow.

**Connection to target genes:** No direct connection. None of the 20 targets encode SUTs or their known regulators.

### 2.5 Starch Biosynthesis Pathway

[KNOWN] The maize endosperm starch biosynthesis pathway involves:

| Enzyme | Gene(s) | Function | Mutant Phenotype |
|--------|---------|----------|------------------|
| **Sucrose Synthase (SuSy)** | *Shrunken1* (Sh1), SUS1 | Cleaves sucrose to UDP-glucose + fructose; dominant substrate supplier for starch biosynthesis | sh1: >90% loss of SuSy activity; dramatically reduced starch; increased soluble sugars; shrunken kernels |
| **AGPase** (large subunit) | *Shrunken2* (Sh2) | Synthesizes ADP-glucose from G1P + ATP; rate-limiting step | sh2: severely reduced starch (~75% of endosperm starch depends on cytosolic AGPase) |
| **AGPase** (small subunit) | *Brittle2* (Bt2) | Catalytic partner of Sh2 | bt2: similar to sh2; defective kernels with reduced starch |
| **Granule-bound starch synthase (GBSS)** | *Waxy* (Wx) | Synthesizes amylose within granules | wx: 0% amylose, 100% amylopectin (waxy starch) |
| **Soluble starch synthase I** | SSI | Elongates short glucan chains | Altered amylopectin fine structure |
| **Soluble starch synthase IIa** | SSIIa | Elongates intermediate chains | Altered amylopectin |
| **Starch branching enzyme** | *Amylose Extender1* (Ae1) / SBEIIb | Introduces alpha-1,6 branch points | ae1: increased amylose (>50%) |
| **Starch debranching enzyme (ISA1)** | *Sugary1* (Su1) | Trims excess branches; crystallization of amylopectin | su1: phytoglycogen accumulation; increased sucrose; sweet corn phenotype |
| **Invertase (cell wall)** | *Miniature1* (Mn1) / INCW2 | Hydrolyzes sucrose at BETL; establishes sink strength | mn1: >70% reduction in kernel weight |

**Connection to target genes:**

| Target Gene | Connection to Starch Biosynthesis | Evidence Level |
|-------------|-----------------------------------|----------------|
| **IBP1** (Initiator Binding Protein 1) | [KNOWN] IBP1 binds the initiator element of the *Shrunken-1* promoter. Sh1 encodes sucrose synthase, the dominant substrate supplier for starch biosynthesis. IBP1 downregulation could alter Sh1 transcription. If IBP1 is a positive regulator, its downregulation would reduce Sh1 expression, reducing starch and increasing soluble sugars (analogous to sh1 mutant). If IBP1 is a negative regulator, its downregulation would increase Sh1 expression and potentially enhance starch biosynthesis. | **This is the most direct connection between any target gene and starch biosynthesis.** The direction of effect is uncertain. |
| **HEX6** (hexokinase) | [INFERRED] HXK phosphorylates fructose/glucose produced by invertase and SuSy. Reduced HXK activity would slow hexose phosphorylation, potentially creating a metabolic bottleneck between sucrose hydrolysis and starch synthesis. However, 9 HXK genes provide redundancy. HXK also functions as a sugar sensor: reduced HXK signaling could alter expression of starch biosynthesis genes through sugar-response pathways. | Indirect; buffered by gene family redundancy. |
| **MYBR64** (MYB-related TF) | [KNOWN] ZmMYBR29 (MYB-related, same subfamily as MYBR64) loss-of-function reduces grain filling rate by 26.7% and downregulates starch and sucrose metabolism genes. ZmMYB155 (2025) is involved in starch synthesis and BETL development. If MYBR64 is a positive regulator of grain filling like ZmMYBR29, its downregulation would be DETRIMENTAL to starch accumulation. | **This is a potential negative effect of the RNA drug on grain fill.** |
| **ppr377** (PPR protein) | [INFERRED] PPR proteins process mitochondrial/chloroplast transcripts. Mitochondrial efficiency determines ATP supply for starch biosynthesis (AGPase requires ATP). Reduced PPR function could impair energy supply to the starch synthesis pathway. | Indirect; potentially counterproductive. |
| **RING63/RING265** (E3 ubiquitin ligases) | [INFERRED] E3 ligases control turnover of metabolic enzymes. If RING63/265 target starch biosynthesis enzymes for degradation, their downregulation would stabilize these enzymes and increase starch. If they target negative regulators, the opposite occurs. Substrate specificity is unknown. | Ambiguous; substrate-dependent. |

### 2.6 Invertases: Miniature1 and Beyond

[KNOWN] The Miniature1 (Mn1) locus encodes INCW2, the dominant cell wall invertase in the BETL. INCW2 catalyzes irreversible sucrose hydrolysis to glucose + fructose in the apoplast, generating the hexose gradient that drives sugar import. The mn1 mutant loses >70% of kernel weight, demonstrating that INCW2 is the single most important determinant of kernel sink strength.

Additional invertases include:
- **INCW1**: Second cell wall invertase; expressed at lower levels
- **IVR1**: Vacuolar invertase; soluble, cleaves sucrose within the vacuole
- **IVR2**: Perianth/maternal tissue invertase, stress-responsive

[KNOWN] Cell wall invertase-deficient mn1 kernels have altered phytohormone levels, including reduced IAA and increased ABA, demonstrating that sugar metabolism and hormone signaling are tightly coupled during grain filling.

**Connection to target genes:**

| Target Gene | Connection to Invertases | Evidence Level |
|-------------|--------------------------|----------------|
| ABI40 (VP1-like) | [KNOWN] VP1/ABI3 regulates maturation programs. In vp1 mutants, the scutellum develops abnormally and cannot respond to nutrient signals (Yang et al., 2019). However, mn1 kernels show that invertase loss increases ABA, and VP1 mediates ABA responses. ABI40 downregulation could alter the ABA-invertase feedback loop during kernel development. | [INFERRED] Complex feedback; direction uncertain. VP1 primarily acts in embryo, while INCW2 acts in BETL. |
| HEX6 (hexokinase) | [INFERRED] HXK phosphorylates the hexose products of invertase (glucose + fructose). Reduced HXK activity would slow the metabolic utilization of invertase products, potentially causing hexose accumulation in the BETL apoplast. This could alter the concentration gradient driving further sucrose unloading. | Indirect metabolic effect. |

### 2.7 Sucrose Synthase (SuSy / Sh1)

[KNOWN] Sucrose synthase (SuSy) encoded by Shrunken1 (Sh1) is the primary enzyme directing carbon from sucrose toward starch biosynthesis in maize endosperm. Sh1 is primarily expressed in endosperm, while SUS1 accumulates mainly in embryo. The sh1 mutation causes >90% loss of SuSy activity, with dramatic consequences: reduced starch content, increased soluble sugars (including sucrose, glucose, fructose), extremely high osmolality, kernel swelling, and the shrunken phenotype. SH1 overexpression (ZmSUS1) alters starch content and composition.

**Critical connection: IBP1 binds the Sh1 promoter.** This is the single most direct link between any of the 20 target genes and the starch biosynthesis machinery. IBP1 downregulation would alter Sh1 transcription, but the direction depends on whether IBP1 activates or represses Sh1. IBP1 overexpression in tobacco reduces internode elongation and alters gibberellin balance, suggesting it is a growth modulator. Its binding to the Sh1 initiator suggests a role in fine-tuning Sh1 expression.

### 2.8 Sink Strength Regulators

[KNOWN] Sink strength in maize kernels is determined by:

1. **INCW2/Mn1**: Apoplastic sucrose hydrolysis (see Section 2.6)
2. **SWEET4c**: Hexose transport across BETL membranes
3. **Auxin (IAA)**: Promotes cell division in endosperm; auxin and ABA promote glucose metabolism in reactivated young kernels. ZmYUCCA genes catalyze auxin biosynthesis in developing kernels.
4. **Cytokinins**: Promote cell division during the lag phase (0-12 DAP); positively correlated with grain filling rate
5. **ABA**: Promotes grain filling by enhancing mobilization of carbon assimilates into grains; ABA content correlates positively with grain filling rate during active fill

**Connection to target genes:**

| Target Gene | Connection to Sink Strength | Evidence Level |
|-------------|----------------------------|----------------|
| **ABI40** (VP1-like) | [KNOWN] ABA promotes grain filling. VP1/ABI3 mediates ABA-responsive gene expression. Reducing VP1-like activity could impair ABA-mediated grain filling promotion. However, during germination, ABI40 downregulation accelerates the dormancy-to-germination transition (beneficial). At grain filling, reduced ABA sensitivity could be DETRIMENTAL because ABA is a positive regulator of starch accumulation during maturation. | **CRITICAL DUALITY: ABI40 downregulation is beneficial at germination but potentially detrimental at grain fill.** This is only a concern if silencing persists to R-stages. |
| **AHL9** (AT-hook protein) | [KNOWN] AHL proteins repress auxin biosynthesis by recruiting SWR1 to YUCCA promoters (Favero et al., 2024). AHL9 downregulation derepresses auxin biosynthesis. Enhanced auxin levels during vegetative growth produce larger plants. During ear development, auxin promotes kernel set and endosperm cell division. | [INFERRED] Enhanced auxin from AHL9 downregulation could improve kernel set and reduce kernel abortion, increasing kernel number per ear. This is a positive pathway. |
| **NPF15** (NRT1/PTR transporter) | [KNOWN] ZmNPF7.9 is essential for seed development (nitrate transport in BETL). Dek407 (NPF1.5) mutation causes reduced kernel size and delayed grain filling. If NPF15 has transport activity in developing kernels, its modulation could affect nutrient delivery. | [SPECULATIVE] NPF15 is annotated as NPF4.6 (ABA/GA transporter), not NPF7.9. Functional overlap within the 78-member family is possible but undemonstrated. |

### 2.9 Kernel Abortion Mechanisms and ABA/GA Balance

[KNOWN] Kernel abortion in maize occurs primarily at the ear tip during the lag phase (0-12 DAP) when photosynthate supply is insufficient to support all fertilized ovules. The least competitive kernels (tip kernels) abort first.

Key regulators of kernel abortion:
- **Sucrose supply**: Low sucrose to ear tips triggers abortion
- **Auxin (IAA)**: Maintains kernel viability; auxin-deficient kernels abort
- **ABA**: At moderate levels, promotes grain filling; at high levels during stress, promotes abortion
- **Ethylene**: Stress-induced ethylene promotes kernel abortion
- **Cytokinins**: Prevent abortion by maintaining cell division

[KNOWN] Exogenous ABA application to ears under drought alleviates dysplasia by altering photosynthesis and sucrose transport. GA4+7 application during grain filling increases 1000-grain weight and antioxidant activity. The ABA/GA balance is crucial: appropriate ABA promotes maturation and starch accumulation, while excessive ABA or insufficient GA inhibits grain fill.

**Connection to target genes:**

The ABI40 target has the strongest relevance. If ABI40 downregulation persists to the reproductive phase:
- [INFERRED] Reduced ABA sensitivity could reduce kernel abortion under mild drought (positive for yield)
- [INFERRED] Reduced ABA sensitivity could also impair the ABA-dependent maturation program, reducing starch deposition (negative for kernel weight)
- The net effect depends on: (a) whether silencing persists, (b) the magnitude of ABI40 downregulation, and (c) environmental conditions (stress vs. optimal)

### 2.10 Cob Size Determinants

[KNOWN] Cob size (ear length, ear diameter, row number) is determined primarily by:
1. **Inflorescence meristem activity** during V5-V12 (ear initiation and development)
2. **Auxin transport and signaling** (PIN proteins, auxin maxima determine kernel row number)
3. **CLAVATA-WUSCHEL signaling** (CLV/FEA/TD1 pathway determines meristem size)
4. **Photosynthate availability** during ear initiation (source strength)

**Connection to target genes:**

| Target Gene | Connection to Cob Size | Evidence Level |
|-------------|------------------------|----------------|
| AHL9 (AT-hook protein) | [INFERRED] AHL9 downregulation derepresses auxin biosynthesis (YUCCA genes). Enhanced auxin during V5-V12 could promote inflorescence meristem activity, potentially increasing ear length and kernel row number. | [SPECULATIVE] Auxin effects on ear development are dose-dependent; excess auxin could have negative effects. |
| ABI40 (VP1-like) | [SPECULATIVE] No direct connection to ear morphogenesis. Any effect would be indirect through altered hormone balance. | Very indirect. |

**Assessment:** Cob size is primarily determined by genetics and environmental conditions during V5-V12. The RNA drug applied at seed soak would need to produce either (a) persistent epigenetic effects altering meristem genes, or (b) an early vigor advantage that improves photosynthate supply during ear initiation. Bridge 2 (compound growth effect) is the most plausible mechanism for any cob size increase.

---

## 3. Sweetness (Sucrose) and Starch Prediction

### 3.1 Can the Gene Set Increase Sweetness?

**Definition:** "Sweetness" in mature grain maize is primarily sucrose content (1-3% of kernel dry weight in field corn; 10-20% in sweet corn at harvest). Higher sweetness would mean higher free sugar content (sucrose, glucose, fructose) in the kernel at a given harvest time.

### 3.2 Pathway-by-Pathway Assessment

#### 3.2.1 SWEET Transporters
**Effect of 20-gene downregulation on SWEET expression:** No direct effect. None of the 20 targets encode SWEET proteins or their characterized regulators.
**Indirect route:** [SPECULATIVE] If AHL9 downregulation increases auxin, and auxin influences SWEET4c expression, there could be an indirect enhancement of hexose import. However, no evidence links auxin to SWEET4c transcription.
**Verdict:** No plausible direct mechanism to alter sweetness via SWEET transporters.

#### 3.2.2 SUT/SUC Sucrose Transporters
**Effect:** No direct connection. No targets encode SUTs.
**Verdict:** No mechanism.

#### 3.2.3 Sucrose Synthase (SuSy/Sh1)
**Effect:** IBP1 binds the Sh1 promoter. If IBP1 is a positive regulator of Sh1, its downregulation reduces SuSy activity, which would INCREASE free sucrose (less sucrose cleavage) and DECREASE starch. This is the sh1-like phenotype.
**If IBP1 is a negative regulator of Sh1**, its downregulation increases SuSy, DECREASING free sucrose and INCREASING starch.
**Verdict:** [INFERRED] IBP1 downregulation could shift the sucrose/starch balance through Sh1 regulation, but the direction depends on IBP1's regulatory polarity, which is not established.

#### 3.2.4 Invertases (CWI/VI)
**Effect:** No direct connection. Invertase genes (INCW1, INCW2/Mn1, IVR1, IVR2) are not among the 20 targets.
**Indirect route:** [INFERRED] If HEX6 downregulation reduces hexokinase-mediated sugar signaling, this could alter feedback regulation of invertase gene expression. Hexokinase-dependent sugar signaling normally represses certain genes when glucose is abundant. Reduced HXK signaling could derepress invertase expression.
**Verdict:** Highly indirect; uncertain magnitude.

#### 3.2.5 AGPase (Sh2/Bt2)
**Effect:** No direct connection. AGPase genes are not targets.
**Indirect route:** [INFERRED] ABA promotes AGPase expression during grain fill. If ABI40 downregulation reduces ABA-responsive gene expression and this persists to grain filling, AGPase expression could be reduced, lowering the flux from G1P to ADP-glucose. Less ADP-glucose means less starch and more residual sugars.
**Verdict:** [SPECULATIVE] Only relevant if ABI40 silencing persists to R-stages. Conservative estimate: silencing does NOT persist that long.

#### 3.2.6 Starch Synthases (SSI, SSII, GBSS/Waxy)
**Effect:** No direct connection. No targets encode starch synthases.
**Verdict:** No mechanism.

#### 3.2.7 Starch Branching Enzyme (SBE/Ae1)
**Effect:** No direct connection.
**Verdict:** No mechanism.

#### 3.2.8 The su1 (sugary1) Pathway
[KNOWN] The sugary1 (su1) gene encodes isoamylase-type starch debranching enzyme (ISA1). su1 mutations cause: (1) increased sucrose concentration, (2) decreased amylopectin, (3) accumulation of phytoglycogen (highly branched water-soluble polysaccharide). The su1 phenotype is the basis of traditional sweet corn.

**Could any of the 20 targets affect the su1 pathway?**

| Mechanism | Assessment |
|-----------|------------|
| Direct silencing of su1 | No. su1 is not among the 20 targets. |
| Transcriptional regulation of su1 | [SPECULATIVE] If MYBR64 regulates su1 expression, its downregulation could alter debranching enzyme levels. However, su1 expression is primarily controlled by developmental programs, not MYB-related TFs. No evidence links MYBR64 to su1. |
| Altered starch granule initiation | [SPECULATIVE] If RING63/265 ubiquitinate starch biosynthesis enzymes and their downregulation stabilizes these enzymes, the ratio of branching to debranching activity could shift. This is extremely indirect. |

**Verdict:** No plausible mechanism connects the 20 target genes to the su1 pathway.

### 3.3 Summary: Sweetness Prediction

| Route | Plausibility | Direction | Magnitude |
|-------|-------------|-----------|-----------|
| IBP1 -> Sh1 (SuSy) -> sucrose/starch balance | Medium (IF IBP1 silencing persists and IBP1 is a positive Sh1 regulator) | Increase sucrose, decrease starch | Small (IBP1 is one of multiple Sh1 regulators) |
| HEX6 -> sugar sensing -> invertase feedback | Low | Uncertain | Minimal |
| ABI40 -> ABA signaling -> AGPase expression | Very low (requires persistent silencing to R-stages) | Increase residual sugars | Minimal |
| Any target -> su1 pathway | No plausible mechanism | N/A | N/A |

**Overall assessment:** [INFERRED] The 20-gene set does NOT contain direct mechanisms to substantially increase kernel sweetness in field corn. The only credible route is through IBP1's regulation of Sh1, and even this is weak because (a) IBP1's regulatory polarity on Sh1 is unknown, (b) the magnitude would likely be small given other Sh1 regulators, and (c) it requires persistent silencing through grain fill.

---

## 4. Protein Content Prediction

### 4.1 Nitrogen Assimilation and the Target Genes

[KNOWN] Kernel protein content depends on:
1. **Nitrogen uptake** from soil (primarily as nitrate or ammonium)
2. **Nitrogen assimilation** via GS/GOGAT pathway into amino acids
3. **Nitrogen remobilization** from vegetative tissues to grain during senescence
4. **Amino acid transport** to kernels via phloem and BETL
5. **Storage protein synthesis** (zeins regulated by O2/PBF/OHP transcription factor network)

**Key nitrogen transporters for kernel filling:**
- **NRT/NPF family**: Nitrate and peptide transport
- **AAP (Amino Acid Permease) family**: ZmAAP6 is expressed in immature seeds, especially in BETL. ZmAAP6 null mutants show decreased total protein and zein content; overexpression increases protein content.
- **CAT (Cationic Amino Acid Transporter) family**: Lysine and arginine transport

[KNOWN] In maize, 71 AAAP (amino acid/auxin permease) genes have been identified. These are critical for nitrogen import into developing kernels. A SnRK1-ZmRFWD3-O2 signaling axis coordinates carbon and nitrogen assimilation in developing seeds.

**Connection to target genes:**

| Target Gene | Connection to N Assimilation/Protein | Evidence Level |
|-------------|--------------------------------------|----------------|
| **NPF15** (NPF4.6-like transporter) | [KNOWN] NPF transporters transport nitrate, peptides, and hormones. ZmNPF7.9 is essential for kernel development and nitrogen transport in BETL. If NPF15 has nitrate or peptide transport activity in roots or vascular tissue, its downregulation could impair nitrogen uptake or long-distance transport. However, NPF15 is annotated as an ABA transporter (NPF4.6-like), not a primary nitrate transporter. | [SPECULATIVE] Indirect; unlikely to substantially affect N flux given 78-member NPF family redundancy. |
| **ABI40** (VP1-like TF) | [KNOWN] VP1 directly regulates intra-kernel protein reallocation. In vp1 embryos, misshapen scutellum cells contain less cellular content and cannot respond to nutrient signals (Yang et al., 2019, *Plant Cell*). VP1 transactivates genes involved in sulfur assimilation and nutrient metabolism. VP1 mutants show altered protein distribution between endosperm and embryo. | **This is the most direct connection to kernel protein content.** If ABI40 downregulation persists, it could impair VP1-mediated protein reallocation. However, VP1 loss would reduce embryo protein, not necessarily total kernel protein. |
| **HEX6** (hexokinase / sugar sensor) | [INFERRED] Sugar-nitrogen coordination: SnRK1-dependent signaling links carbon status to nitrogen assimilation. HXK signaling feeds into SnRK1 regulation through T6P levels. Reduced HXK signaling could alter C/N balance sensing, potentially affecting the partitioning of resources between starch and protein. | Very indirect. |
| **RING63/265** (E3 ubiquitin ligases) | [INFERRED] E3 ligases control protein turnover. ZmRFWD3 (a RING-type E3 ligase) is part of the SnRK1-ZmRFWD3-O2 signaling axis that coordinates C/N assimilation. If RING63 or RING265 have analogous roles in regulating transcription factor stability, their downregulation could alter the O2-PBF zein regulatory network. | [SPECULATIVE] No evidence that RING63/265 specifically target the O2/PBF network. |

### 4.2 Zein Storage Protein Regulation

[KNOWN] Zeins constitute 50-70% of maize endosperm protein. They are regulated by three master transcription factors acting additively and synergistically:
- **Opaque2 (O2)**: bZIP TF; activates 22-kDa alpha-zein genes
- **Prolamine Box-binding Factor (PBF)**: DOF TF; activates 27-kDa gamma-zein
- **O2 Heterodimerizing Proteins (OHPs)**: bZIP TFs; synergize with O2

None of the 20 target genes encode O2, PBF, or OHPs. None are direct regulators of zein biosynthesis.

### 4.3 The Dilution Effect

[KNOWN] If yield (total biomass per kernel or per plant) increases while nitrogen supply remains constant, protein percentage will decrease even though total protein per kernel may remain unchanged or increase slightly. This "dilution effect" is well-documented in cereals:
- In wheat: yield increases from breeding have been accompanied by 0.5-1.0% decline in grain protein content per decade
- In maize: the negative correlation between grain yield and protein % is approximately r = -0.3 to -0.5

[INFERRED] If the RNA drug increases yield through the early vigor mechanism, kernel protein % would be expected to DECREASE slightly (dilution effect) unless nitrogen uptake also increases proportionally.

### 4.4 Grain Protein Content (GPC) Regulation

[KNOWN] In wheat, the NAM-B1 (GPC-B1) gene, encoding a NAC transcription factor, accelerates senescence and promotes nitrogen remobilization to grain. GPC regulation in maize is less well characterized but involves:
- **Nitrogen Remobilization Efficiency (NRE)**: How efficiently N moves from leaves/stems to grain during senescence
- **Stay-green trait**: Delays senescence but can reduce NRE, lowering grain protein %
- **Source-sink N ratio**: Determined by soil N, N uptake efficiency, and N utilization efficiency

**Connection to target genes:**

| Target Gene | Connection to GPC | Evidence Level |
|-------------|-------------------|----------------|
| ABI40 (VP1-like) | [INFERRED] ABA promotes leaf senescence and nitrogen remobilization. If ABI40 downregulation reduces ABA sensitivity, it could delay senescence (stay-green phenotype), reducing NRE and grain protein %. | [SPECULATIVE] Requires persistent silencing to senescence stage (implausible from seed soak). |
| ppr377 (PPR protein) | [INFERRED] Mitochondrial efficiency affects C/N metabolism. Altered mitochondrial function could change the balance of carbon and nitrogen compounds available for grain filling. | Very indirect. |

### 4.5 Summary: Protein Content Prediction

| Effect | Direction | Mechanism | Plausibility |
|--------|-----------|-----------|-------------|
| Total protein per kernel | Neutral to slightly decreased | VP1/ABI40 downregulation could impair protein reallocation IF persistent | Low (requires persistent silencing) |
| Protein % | Slightly decreased | Dilution effect from yield increase | Medium (consistent with early vigor -> yield gain) |
| Zein composition | Unchanged | No targets in O2/PBF/OHP network | High confidence |
| Lysine/tryptophan content | Unchanged | No targets affect amino acid composition | High confidence |

**Overall assessment:** [INFERRED] The RNA drug is unlikely to substantially alter kernel protein content or composition. The most likely effect is a slight decrease in protein % due to the dilution effect if yield increases. No mechanism exists within the 20-gene set to directly enhance or reduce zein biosynthesis.

---

## 5. Quantitative Prediction Ranges

### Methodological Note

These predictions are based on:
1. Published seed priming meta-analyses for magnitude calibration
2. Known mutant phenotypes for maximum plausible effect sizes
3. Conservative downward adjustments for: (a) partial gene silencing (not knockout), (b) uncertain persistence of silencing, (c) gene family redundancy, (d) genotype x environment variation

**CRITICAL CAVEAT**: These predictions assume the RNA drug works through the early vigor mechanism (Bridge 2). If the mechanism is purely osmopriming (Confounder 1), similar predictions would apply but from a different mechanism. If the mechanism involves persistent epigenetic reprogramming (Bridge 1), effect sizes could be larger but this is undemonstrated.

### 5.1 Yield Increase (% Over Control)

| Parameter | Value | Basis |
|-----------|-------|-------|
| **Conservative estimate** | +3 to +8% | Seed priming meta-analysis (Lutts et al., 2016): on-farm priming typically yields 5-20% increase in developing-country conditions, 2-8% under optimal conditions. Biostimulant seed treatments in maize showed +5.1% in field trials (2023 Frontiers study). |
| **Central estimate** | +5 to +10% | Combining early vigor advantage (+5%) with potential improved stress tolerance from reduced ABA sensitivity during mid-season moisture stress (+3-5%). |
| **Optimistic estimate** | +10 to +15% | If persistent epigenetic effects enhance multiple developmental stages. Combined biostimulant + early vigor hybrid showed +14% in controlled trials. |
| **Uncertainty range** | +0 to +15% | Lower bound reflects possibility that effect is entirely within-season noise; upper bound reflects best-case persistent effects. |

**Key assumptions:**
- [INFERRED] Primary mechanism is early vigor (Bridge 2), not persistent gene silencing
- Effect size is environment-dependent: larger under suboptimal conditions (drought, cold), smaller under optimal conditions
- [KNOWN] Genetic gains in maize yield from breeding: ~1-1.5% per year; the RNA drug effect should be calibrated against this baseline

**Literature basis:**
- Paparella et al. (2015): Seed priming review; 5-20% yield increase typical under stress
- Frontiers 2023 biostimulant study: +5.1% grain yield from seed-applied biostimulant in maize
- Meta-analysis of on-farm priming (Lutts et al., 2016): Highly variable; median ~10% under stress

### 5.2 Cob Size Increase (%)

| Parameter | Value | Basis |
|-----------|-------|-------|
| **Conservative estimate** | +0 to +3% | Cob size is primarily genetically determined. Seed priming effects on cob morphology are minimal under optimal conditions. |
| **Central estimate** | +2 to +5% | Ear length may increase through better photosynthate supply during ear initiation (V5-V12) from early vigor advantage. 2022-2023 field data showed ear length increases of 6.2-9.4% from N management optimization. |
| **Optimistic estimate** | +5 to +8% | If auxin derepression (AHL9 silencing) persists and enhances inflorescence development. |
| **Uncertainty range** | +0 to +8% | |

**Key assumptions:**
- [INFERRED] Any cob size increase comes from better resource availability during V5-V12, not direct genetic effects on meristem
- Ear diameter and row number are highly heritable and unlikely to change from seed treatment
- Ear length is more plastic and responsive to environmental conditions

### 5.3 Kernel Number Per Cob Increase (%)

| Parameter | Value | Basis |
|-----------|-------|-------|
| **Conservative estimate** | +2 to +5% | Reduced tip kernel abortion from better photosynthate supply. Kernel number accounts for ~63% of yield gains in maize breeding (Fernandez et al., 2022). |
| **Central estimate** | +3 to +8% | If AHL9-mediated auxin derepression enhances kernel set and reduces abortion. Auxin promotes kernel viability during the lag phase. |
| **Optimistic estimate** | +5 to +12% | If both auxin enhancement and reduced ABA-mediated abortion contribute under stress conditions. |
| **Uncertainty range** | +0 to +12% | |

**Key assumptions:**
- [INFERRED] Primary mechanism is reduced kernel abortion from better resource supply, not more ovules
- [KNOWN] Kernel number is the dominant yield component in maize (63% of yield variance)
- Tip kernel abortion is common (10-30% of ovules abort in stressed plants) and responsive to management

### 5.4 100-Kernel Weight Increase (%)

| Parameter | Value | Basis |
|-----------|-------|-------|
| **Conservative estimate** | +0 to +2% | Kernel weight is highly genetically determined. Seed priming typically has minimal effect on individual kernel weight. |
| **Central estimate** | +1 to +4% | Small increase from better photosynthate supply during grain fill. 100-grain weight increased 13.4% from N optimization in field trials. |
| **Optimistic estimate** | +3 to +6% | If early vigor produces substantially larger plants with more source capacity. |
| **Uncertainty range** | +0 to +6% | |

**Key assumptions:**
- [KNOWN] Kernel weight explains only ~7% of yield variance (Fernandez et al., 2022)
- Increased kernel number often comes at the cost of reduced kernel weight (yield component compensation)
- 100-grain weight is less responsive to seed treatments than kernel number

**CRITICAL NOTE on IBP1 -> Sh1 connection:** If IBP1 downregulation alters Sh1 (SuSy) expression AND this persists to grain fill, it could directly affect kernel weight by modifying carbon flux to starch. The sh1 mutant shows dramatically reduced kernel weight. Even a 10-20% reduction in SuSy activity could reduce kernel weight by 2-5%. **This is a potential NEGATIVE effect that must be monitored.**

### 5.5 Sugar Content Change (% or Brix)

| Parameter | Value | Basis |
|-----------|-------|-------|
| **Conservative estimate** | 0 to +0.2% dry weight | No direct mechanism to increase sweetness in field corn. |
| **Central estimate** | 0 to +0.5% dry weight (0 to +0.3 Brix at fresh harvest) | If IBP1 -> Sh1 connection reduces SuSy activity slightly, free sucrose would increase marginally. |
| **Optimistic estimate** | +0.5 to +1.0% dry weight | If multiple indirect pathways converge (HXK signaling + IBP1/Sh1 + ABA/AGPase). |
| **Uncertainty range** | -0.5 to +1.0% dry weight | Could decrease if Sh1 activity increases (IBP1 as negative regulator). |

**Key assumptions:**
- [KNOWN] Field corn typically has 1-3% free sugars at dry maturity
- [KNOWN] Sweet corn (su1 mutant) has 10-20% sugars -- this requires major pathway disruption not achievable by these targets
- Any sugar change would be subtle and commercially insignificant for field corn
- For silage corn, slight increases in sugar could improve palatability

### 5.6 Starch Content Change (%)

| Parameter | Value | Basis |
|-----------|-------|-------|
| **Conservative estimate** | -1 to +1% of kernel dry weight | Essentially no change; starch content is robust against subtle perturbations. |
| **Central estimate** | -0.5 to +1.5% of kernel dry weight | Slight increase possible if early vigor leads to larger plants with more photosynthate partitioned to grain. |
| **Optimistic estimate** | +1 to +3% of kernel dry weight | If compound growth effect substantially increases source strength during grain fill. |
| **Uncertainty range** | -2 to +3% of kernel dry weight | |

**Key assumptions:**
- [KNOWN] Normal field corn starch is 70-75% of kernel dry weight
- [INFERRED] Starch content changes are more likely to come from changes in total kernel weight than from changes in starch:kernel ratio
- **RISK:** If IBP1 downregulation reduces Sh1 (SuSy) expression, starch could DECREASE. The sh1 mutant has severely reduced starch. Even partial reduction in SuSy could lower starch by 1-3%.
- **RISK:** If MYBR64 is homologous to ZmMYBR29 and its downregulation persists, grain filling rate could decrease, reducing starch accumulation

### 5.7 Protein % Change

| Parameter | Value | Basis |
|-----------|-------|-------|
| **Conservative estimate** | -0.3 to 0% | Dilution effect from yield increase. |
| **Central estimate** | -0.5 to -0.2% | Typical dilution effect for a 5-10% yield increase with constant N supply. |
| **Optimistic estimate** | -0.2 to +0.3% | If improved root vigor enhances N uptake proportionally to yield increase. |
| **Uncertainty range** | -0.8 to +0.3% | |

**Key assumptions:**
- [KNOWN] Normal maize kernel protein is 8-12%
- [KNOWN] Negative correlation between yield and protein % (r = -0.3 to -0.5)
- [INFERRED] No direct mechanism to increase protein synthesis from these targets
- Total protein per kernel likely increases slightly (larger kernel), but protein % decreases (dilution)

### 5.8 Consolidated Prediction Table

| Trait | Conservative | Central | Optimistic | Confidence | Key Uncertainty |
|-------|-------------|---------|-----------|------------|-----------------|
| Yield (% increase) | +3 to +8% | +5 to +10% | +10 to +15% | Medium | Magnitude of early vigor; environment |
| Cob size (% increase) | +0 to +3% | +2 to +5% | +5 to +8% | Low | Ear length vs diameter; genetics |
| Kernel number/cob (% increase) | +2 to +5% | +3 to +8% | +5 to +12% | Medium | Abortion rate; stress dependence |
| 100-kernel weight (% increase) | +0 to +2% | +1 to +4% | +3 to +6% | Low | IBP1/Sh1 risk; compensation |
| Sugar content (% DW change) | 0 to +0.2% | 0 to +0.5% | +0.5 to +1.0% | Very low | IBP1 regulatory polarity; persistence |
| Starch content (% DW change) | -1 to +1% | -0.5 to +1.5% | +1 to +3% | Low | IBP1/Sh1; MYBR64/ZmMYBR29 risk |
| Protein % change | -0.3 to 0% | -0.5 to -0.2% | -0.2 to +0.3% | Medium | Dilution effect; N uptake |

---

## 6. Synthesis: Target-to-Grain-Fill Connectivity Map

### 6.1 Direct Connections (Evidence-Based)

Only **three** of the 20 target genes have evidence-based connections to grain filling pathways:

1. **IBP1 -> Shrunken-1 (SuSy) promoter binding** [KNOWN]
   - IBP1 binds the Sh1 initiator element
   - Sh1 encodes the dominant sucrose synthase for starch biosynthesis
   - IBP1 downregulation would alter Sh1 expression (direction unknown)
   - **Risk assessment:** Potentially detrimental to starch accumulation if IBP1 is a positive Sh1 regulator

2. **ABI40/VP1 -> Intra-kernel protein reallocation** [KNOWN]
   - VP1 directly regulates scutellum development and nutrient assimilation (Yang et al., 2019)
   - VP1 transactivates genes in sulfur assimilation and nutrient metabolism
   - **Risk assessment:** ABI40 downregulation is beneficial at germination but potentially detrimental at grain fill (reduces ABA-mediated maturation program)

3. **MYBR64 -> Grain filling rate (via ZmMYBR29 homology)** [KNOWN for ZmMYBR29; INFERRED for MYBR64]
   - ZmMYBR29 loss-of-function reduces grain filling rate by 26.7%
   - ZmMYBR29 regulates starch and sucrose metabolism genes in endosperm
   - **Risk assessment:** If MYBR64 is functionally similar to ZmMYBR29, its downregulation could REDUCE grain filling rate. **This is a potential negative effect.**

### 6.2 Indirect Connections (Inferred)

4. **AHL9 -> Auxin biosynthesis -> Kernel set/abortion** [INFERRED]
   - AHL proteins repress YUCCA (auxin biosynthesis) gene expression
   - Enhanced auxin promotes kernel viability and reduces abortion
   - **Assessment:** Positive for kernel number; requires persistence of AHL9 silencing

5. **HEX6 -> Sugar sensing -> C/N balance** [INFERRED]
   - Reduced HXK signaling alters sugar-ABA-SnRK1 crosstalk
   - Could affect partitioning between starch and protein
   - **Assessment:** Highly indirect; buffered by 9-member HXK family

6. **NPF15 -> Nutrient/hormone transport to ear** [SPECULATIVE]
   - NPF family members transport nitrate, peptides, ABA, GA to developing kernels
   - ZmNPF7.9 is essential for kernel development (BETL-expressed)
   - NPF15 is annotated as NPF4.6 (ABA transporter), not a seed-filling transporter
   - **Assessment:** Very uncertain; substrate specificity of NPF15 is uncharacterized

7. **RING63/RING265 -> Proteostasis of metabolic enzymes** [SPECULATIVE]
   - E3 ligases control stability of metabolic enzymes and signaling components
   - Could affect starch biosynthesis enzyme turnover or O2/PBF stability
   - **Assessment:** No substrate data available; effect is entirely speculative

8. **ppr377 -> Mitochondrial efficiency -> ATP for starch synthesis** [INFERRED]
   - PPR proteins process mitochondrial transcripts
   - Mitochondrial ATP drives AGPase and other energy-requiring steps
   - **Assessment:** Potentially counterproductive; reduced mitochondrial efficiency would impair grain filling

### 6.3 The Persistence Problem: Why Most Grain-Fill Effects Are Unlikely

The fundamental constraint is **temporal persistence of gene silencing**. The RNA drug is applied at imbibition (0-8 hours). For the gene downregulation to directly affect grain filling pathways, silencing must persist through:

| Developmental Stage | Days After Treatment | Cell Divisions | Persistence Likelihood |
|---------------------|---------------------|----------------|----------------------|
| Germination (VE) | 0-5 days | 0-3 | **HIGH** |
| Seedling (V1-V3) | 5-20 days | 5-10 | Medium |
| Vegetative (V3-VT) | 20-60 days | 10-20+ | **LOW** |
| Ear initiation (V5-V12) | 25-50 days | 15+ | **LOW** |
| Grain fill (R1-R6) | 55-100 days | 20-30+ | **VERY LOW** |

[KNOWN] In maize, each cell division dilutes non-amplified siRNA signals. Without RDR-mediated amplification (which requires a dsRNA trigger), silencing decays exponentially with cell divisions. Typical siRNA half-lives in plants are hours to days, not weeks.

[INFERRED] The most likely scenario is that direct gene silencing effects are confined to germination and early seedling stages (V0-V3). Any grain-filling effects are almost certainly mediated through:
- **Bridge 2 (compound growth)**: Early vigor -> larger plant -> more photosynthate -> better grain fill
- **Bridge 1 (epigenetic memory)**: IF RdDM occurs at target loci during imbibition, methylation marks could persist. This is plausible but undemonstrated.

### 6.4 Risk Matrix: Potential Negative Effects on Grain Fill

| Target | Risk | Mechanism | Severity | Probability |
|--------|------|-----------|----------|-------------|
| **IBP1** | Reduced starch | Altered Sh1/SuSy expression | High (sh1 phenotype = severely shrunken) | Low (requires persistent silencing AND IBP1 as positive Sh1 regulator) |
| **MYBR64** | Reduced grain filling rate | ZmMYBR29 homolog loss = -26.7% fill rate | High | Low (requires persistent silencing AND MYBR64 = ZmMYBR29 functional homolog) |
| **ABI40** | Impaired maturation program | Reduced ABA-mediated starch/protein accumulation | Medium | Very Low (requires silencing to R-stages) |
| **ppr377** | Reduced mitochondrial efficiency | Impaired ATP supply for biosynthesis | Medium | Very Low (requires persistent silencing) |
| **PRH130/PP2C32** | Enhanced ABA sensitivity at grain fill | Could accelerate premature maturation | Low | Very Low |

**Overall risk assessment:** The probability of persistent silencing to grain-filling stages is LOW to VERY LOW. The most likely outcome is that direct gene silencing effects do not reach R-stages, and any grain-filling phenotype is mediated entirely through the compound growth effect (Bridge 2), which is positive for yield.

### 6.5 Key Experimental Tests for Grain-Fill Effects

To distinguish between direct silencing effects and compound growth effects at grain fill:

1. **RT-qPCR at R1**: Measure transcript levels of the 20 targets in developing ears of M-9-treated vs. control plants. If targets are NOT downregulated at R1, the compound growth mechanism is supported.

2. **Bisulfite sequencing at V6 and R1**: Assess DNA methylation status at target loci. If RdDM marks persist, the epigenetic memory mechanism is supported.

3. **Growth equalization experiment**: Thin M-9-treated and control plots to identical plant densities and manage to identical LAI at V6. If grain-fill differences disappear, the compound growth mechanism is confirmed.

4. **IBP1-specific test**: Measure Sh1 transcript levels in developing endosperm of M-9-treated kernels. If Sh1 is altered, IBP1-mediated effects on starch are occurring.

---

## 7. References

### Grain Filling and Source-Sink Biology

[GF1] Sosso D, Luo D, Li QB, Sber J, Yang B, Hummel AW, Frommer WB. (2015) Seed filling in domesticated maize and rice depends on SWEET-mediated hexose transport. *Nature Genetics*, 47: 1489-1493. DOI: 10.1038/ng.3422

[GF2] Shen S, Ma S, Chen Y, et al. (2022) A transcriptional landscape underlying sugar import for grain set in maize. *The Plant Journal*, 110(1): 228-242. DOI: 10.1111/tpj.15668

[GF3] Sosso D, Luo D, Li QB, et al. (2023) Spatial transcriptomics uncover sucrose post-phloem transport during maize kernel development. *Nature Communications*, 14: 7204. DOI: 10.1038/s41467-023-43006-7

[GF4] Cheng WH, Taliercio EW, Chourey PS. (1996) The Miniature1 seed locus of maize encodes a cell wall invertase required for normal development of endosperm and maternal cells in the pedicel. *Plant Cell*, 8(6): 971-983. DOI: 10.1105/tpc.8.6.971

[GF5] LeClere S, Schmelz EA, Chourey PS. (2007) Cell wall invertase-deficient miniature1 kernels have altered phytohormone levels. *Phytochemistry*, 68(22-24): 2603-2612. DOI: 10.1016/j.phytochem.2007.05.031

[GF6] Kang BH, Xiong Y, Williams DS, Pozueta-Romero D, Chourey PS. (2009) Miniature1-encoded cell wall invertase is essential for assembly and function of wall-in-growth in the maize endosperm transfer cell. *Plant Physiology*, 151(3): 1366-1376. DOI: 10.1104/pp.109.142331

[GF7] Chourey PS, Jang JK, Carlson S. (1999) A re-evaluation of the relative roles of two invertases, INCW2 and IVR1, in developing maize kernels. *Plant Physiology*, 121(3): 1093-1094.

### Starch Biosynthesis

[GF8] Hannah LC, Giroux M, Boyer C. (1993) Biotechnological modification of carbohydrates for sweet corn and maize improvement. *Scientia Horticulturae*, 55(1-2): 177-197.

[GF9] Li N, Zhang S, Zhao Y, Li B, Zhang J. (2011) Over-expression of AGPase genes enhances seed weight and starch content in transgenic maize. *Planta*, 233: 241-250. DOI: 10.1007/s00425-010-1296-5

[GF10] Nair SK, Babu R, Magorokosho C, et al. (2015) Genetic basis of maize kernel starch content revealed by high-density SNP markers in a RIL population. *BMC Plant Biology*, 15: 288. DOI: 10.1186/s12870-015-0699-z

[GF11] Boehlein SK, Shaw JR, Stewart JD, Hannah LC. (2018) Fundamental differences in starch synthesis in the maize leaf, embryo, ovary and endosperm. *The Plant Journal*, 96(3): 595-606. DOI: 10.1111/tpj.14053

### Sucrose Synthase and Sh1

[GF12] Zhang L, Ren Y, Lu B, et al. (2020) SH1-dependent maize seed development and starch synthesis via modulating carbohydrate flow and osmotic potential balance. *BMC Plant Biology*, 20: 264. DOI: 10.1186/s12870-020-02478-1

[GF13] Chourey PS, Taliercio EW, Carlson SJ, Ruan YL. (1998) Genetic evidence that the two isozymes of sucrose synthase present in developing maize endosperm are critical, one for cell wall integrity and the other for starch biosynthesis. *Molecular and General Genetics*, 259: 88-96.

[GF14] Hou J, Tong X, Chen X, et al. (2023) Overexpression of the ZmSUS1 gene alters the content and composition of endosperm starch in maize. *Planta*, 258: 38. DOI: 10.1007/s00425-023-04133-z

### Sugary1 and Sweet Corn

[GF15] James MG, Robertson DS, Myers AM. (1995) Characterization of the maize gene sugary1, a determinant of starch composition in kernels. *Plant Cell*, 7(4): 417-429. DOI: 10.1105/tpc.7.4.417

[GF16] Tracy WF. (2019) Maize sugary enhancer1 (se1) is a gene affecting endosperm starch metabolism. *PNAS*, 116(38): 19235-19240. DOI: 10.1073/pnas.1902747116

[GF17] Pan D, Nelson OE. (1984) Molecular structure of three mutations at the maize sugary1 locus and their allele-specific phenotypic effects. *Genetics*, 121(4): 827-838.

### VP1/ABI3 and Kernel Development

[GF18] Yang T, Guo L, Ji C, et al. (2019) Intra-kernel reallocation of proteins in maize depends on VP1-mediated scutellum development and nutrient assimilation. *Plant Cell*, 31(11): 2613-2635. DOI: 10.1105/tpc.19.00444

### Protein Content and Nitrogen Metabolism

[GF19] Zhang Z, Yang J, Wu Y. (2015) Transcriptional regulation of zein gene expression in maize through the additive and synergistic action of opaque2, prolamine-box binding factor, and O2 heterodimerizing proteins. *Plant Cell*, 27(4): 1025-1040. DOI: 10.1105/tpc.15.00150

[GF20] Guo Y, Li T, Liu Y, et al. (2022) Amino acid permease 6 regulates grain protein content in maize. *The Crop Journal*, 10(5): 1400-1410. DOI: 10.1016/j.cj.2022.03.007

[GF21] Peng B, Li Y, Wang Y, et al. (2019) The regulation of zein biosynthesis in maize endosperm. *Theoretical and Applied Genetics*, 132: 1-11. DOI: 10.1007/s00122-019-03437-7

[GF22] Yang J, Ji C, Wu Y. (2016) Divergent transactivation of maize storage protein zein genes by the transcription factors opaque2 and OHPs. *Genetics*, 204(2): 581-591. DOI: 10.1534/genetics.116.192385

### MYB Transcription Factors and Grain Filling

[GF23] Chen Z, Ren X, Qi L, et al. (2024) A MYB-related transcription factor ZmMYBR29 is involved in grain filling. *BMC Plant Biology*, 24: 445. DOI: 10.1186/s12870-024-05163-9

[GF24] He Y, Zhou T, Chen J, et al. (2025) ZmMYB155 is involved in starch synthesis and basal endosperm transfer layer development in maize. *Plant Cell Reports*, 44: 149. DOI: 10.1007/s00299-025-03569-9

### NPF Transporters and Kernel Development

[GF25] Deng Z, Chen J, Li X, et al. (2023) Maize Dek407 encodes the nitrate transporter 1.5 and is required for kernel development. *Plant Physiology and Biochemistry*, 205: 108191.

[GF26] Yang J, Li C, Kong D, et al. (2021) A nitrate transporter encoded by ZmNPF7.9 is essential for maize seed development. *Plant Science*, 308: 110901. DOI: 10.1016/j.plantsci.2021.110901

### Hormone Regulation of Grain Filling

[GF27] Chen H, Li G, Zhang X, et al. (2023) Auxin and abscisic acid play important roles in promoting glucose metabolism of reactivated young kernels of maize. *Plant Science*, 337: 111876. DOI: 10.1016/j.plantsci.2023.111876

[GF28] Ma D, Luo J, Qi P, et al. (2023) Understanding the regulation of cereal grain filling: The way forward. *Journal of Integrative Plant Biology*, 65(4): 945-963. DOI: 10.1111/jipb.13456

[GF29] Borrás L, Westgate ME. (2006) Predicting maize kernel sink capacity early in development. *Field Crops Research*, 95(2-3): 223-233.

### Seed Priming and Yield

[GF30] Lutts S, Benincasa P, Wojtyla L, et al. (2016) Seed priming: new comprehensive approaches for an old empirical technique. *New Challenges in Seed Biology*, InTech.

[GF31] Paparella S, Araújo SS, Rossi G, et al. (2015) Seed priming: state of the art and new perspectives. *Plant Cell Reports*, 34: 1281-1293. DOI: 10.1007/s00299-015-1784-y

[GF32] Louis S. (2023) Seed priming can enhance and retain stress tolerance in ensuing generations by inducing epigenetic changes and trans-generational memory. *Physiologia Plantarum*, 175(1): e13881. DOI: 10.1111/ppl.13881

### Yield Components

[GF33] Fernandez JA, DeBruin J, Messina CD, Ciampitti IA. (2022) Kernel weight contribution to yield genetic gain of maize. *Journal of Experimental Botany*, 73(18): 6300-6311.

### Hexokinase in Cereals

[GF34] Zheng S, Lu J, Yu D, et al. (2019) Biochemical properties and subcellular localization of six members of the HXK family in maize and its metabolic contribution to embryo germination. *BMC Plant Biology*, 19: 27. DOI: 10.1186/s12870-018-1605-x

[GF35] Cho JI, Ryoo N, Ko S, et al. (2006) Structure, expression, and functional analysis of the hexokinase gene family in rice. *Planta*, 224: 598-611. DOI: 10.1007/s00425-006-0251-y

---

## Appendix: Target Gene Connectivity to Grain Filling -- Quick Reference

| Target | Direct Grain-Fill Connection | Indirect Connection | Net Expected Effect | Confidence |
|--------|------------------------------|---------------------|---------------------|------------|
| **ABI40** | VP1 -> protein reallocation [KNOWN] | ABA sensitivity -> maturation program | Dual: + at germination, ? at grain fill | Medium |
| **PRH130** | None | ABA signaling modulation | Uncertain (paradoxical target) | Very Low |
| **HEX6** | None | Sugar sensing -> C/N balance -> starch/protein ratio | Minimal; buffered by 9 HXK genes | Low |
| **NPF15** | None | NPF family -> nutrient/hormone transport to ear | Minimal; NPF4.6-like, not seed-filling transporter | Very Low |
| **PRX91** | None | None at grain fill | None | N/A |
| **RING63** | None | Proteostasis of metabolic enzymes (substrate unknown) | Unknown | Very Low |
| **AHL9** | None | Auxin -> kernel set/abortion reduction | Positive for kernel number | Low-Medium |
| **MYBR64** | ZmMYBR29 homology -> grain filling rate [KNOWN for ZmMYBR29] | Starch/sucrose metabolism genes | **Potentially negative** (-26.7% fill rate in mutant) | Medium |
| **RING265** | None | Proteostasis (substrate unknown) | Unknown | Very Low |
| **IDP8263** | None | None at grain fill | None | N/A |
| **CYP10** | None | Hormone catabolism (uncharacterized) | Unknown | Very Low |
| **ppr377** | None | Mitochondrial efficiency -> ATP supply | Potentially negative | Low |
| **IBP1** | **Sh1 promoter binding [KNOWN]** | SuSy -> starch biosynthesis flux | **Direction unknown; potentially negative** | Medium |
| **AI714716** | None | None at grain fill | None | N/A |
| **si614021b09a** | None | None at grain fill | None | N/A |
| **PCO145926** | None | None at grain fill | None | N/A |
| **LRR-RLK** | None | None at grain fill | None | N/A |
| **CYP72A15** | None | None at grain fill | None | N/A |
| **PSKR1-like** | None | None at grain fill | None | N/A |
| **LOC100273360** | None | Golgi Ca/Mn homeostasis | None | N/A |

---

*This dossier was prepared as a supplement to the FINAL_REPORT_MAIZE.md. All claims are labeled with evidence levels. No data were invented. Quantitative predictions are calibrated against published literature and explicitly flagged with uncertainty ranges.*
