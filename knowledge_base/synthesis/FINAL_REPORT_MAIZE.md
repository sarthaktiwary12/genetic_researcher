# Bacterial Extracellular RNA-Mediated Reprogramming of Maize (*Zea mays*) Seed Germination: Target Analysis, Mechanistic Models, and Validation Strategy

**Prepared:** 2026-02-17
**Classification:** Internal Research Report -- For Decision-Maker Review
**Evidence Labeling:** [KNOWN] = published peer-reviewed literature; [INFERRED] = logical deduction from conserved biology and target annotations; [SPECULATIVE] = hypothesis requiring experimental validation

---

## Executive Summary

This report consolidates the bioinformatic and literature-based analysis of 20 unique predicted maize gene targets of bacterial extracellular small RNAs (exRNAs), delivered via an extracellular polymeric substance (EPS)-based seed treatment ("M-9"), which improves maize germination rate and seedling vigor. The analysis integrates target gene prioritization, mechanistic modeling, confounder identification, and a tiered experimental validation plan.

**Key findings:**

1. **20 unique gene targets** (no true duplicates found; two CYP72A paralogs confirmed as distinct loci) converge on five master regulatory axes: (a) ABA signaling and dormancy release, (b) ROS/redox optimization of the oxidative window, (c) sugar sensing and energy metabolism, (d) protein turnover and proteostasis via the ubiquitin-proteasome system, and (e) defense-growth resource reallocation [1, 2, 3].

2. **Two testable causal models** -- a Hormone-Metabolic Derepression model and a Redox-Proteostasis Acceleration model -- make divergent, experimentally distinguishable predictions about the primary molecular trigger [4, 5, 6].

3. **Six confounders** threaten the core hypothesis. EPS osmopriming and polysaccharide elicitor effects are the most parsimonious alternative explanations [7, 8]. Several annotation conflicts were resolved: IBP1 is NOT BiP/GRP78 (it is a SANT/Myb transcription factor), PRH130 is PP2C32 (not an RNA helicase), and CYP10 is CYP72A14 (not a cyclophilin).

4. **A single "killer experiment"** -- RNase treatment of the M-9 solution -- can provide a decisive go/no-go result in 2 weeks for under $500.

5. **A minimum viable experiment set** of 5 experiments can deliver proof-of-concept in 10-12 weeks for ~$3,600 in consumables.

6. **Maize-specific RNAi context:** The maize genome encodes comprehensive RNA silencing machinery (DCL, AGO, RDR gene families) [9, 10], and cross-kingdom RNAi has been demonstrated in maize-fungal pathosystems, including spray-induced gene silencing (SIGS) against *Fusarium graminearum* [11, 12]. Bidirectional cross-kingdom RNAi is established in plant-fungal interactions [13].

**Honest assessment:** The exRNA-mediated gene silencing hypothesis is mechanistically novel. While cross-kingdom RNAi is well-established in plant-fungal systems, bacteria-to-plant sRNA transfer during seed imbibition remains to be directly demonstrated in maize. Simpler explanations (osmopriming, polysaccharide elicitation) must be ruled out first. The hypothesis is efficiently testable, and the RNase experiment is the critical first step.

---

## 1. Background and Rationale

### 1.1 Cross-Kingdom RNA Interference

Cross-kingdom RNA interference (RNAi) -- the transfer of small RNAs between organisms of different kingdoms to silence target genes -- is now an established biological phenomenon. The landmark discovery by Weiberg et al. (2013) demonstrated that the fungal pathogen *Botrytis cinerea* transfers small RNAs into *Arabidopsis thaliana* and tomato cells, where they hijack the host AGO1-dependent RNAi machinery to suppress plant immunity genes [14]. Subsequent work showed that plants reciprocally send small RNAs to fungal pathogens via extracellular vesicles (EVs) to silence virulence genes [15], and that fungal small RNAs enter plant cells through clathrin-mediated endocytosis [16]. RNA-binding proteins contribute to small RNA loading in plant extracellular vesicles [17]. Comprehensive reviews have established the broader significance of EV-mediated cross-kingdom RNA trafficking [18].

**Maize-relevant cross-kingdom RNAi precedents:**

1. **Spray-induced gene silencing (SIGS) in cereals:** Koch et al. (2016) demonstrated that spraying long dsRNA onto barley leaves confers protection against *Fusarium graminearum* through an RNAi-based mechanism involving fungal uptake of the dsRNA and silencing of fungal CYP51 genes [11]. Wang et al. (2016) further established bidirectional cross-kingdom RNAi, showing that plant-derived small RNAs can be taken up by fungi to silence virulence genes [13].

2. **Oomycete sRNAs in plant RISC:** Dunker et al. (2020) showed that oomycete small RNAs bind to the plant RNA-induced silencing complex for virulence in the *Hyaloperonospora arabidopsidis*-*Arabidopsis* pathosystem [19], establishing that cross-kingdom sRNA transfer extends beyond fungi.

3. **Extracellular vesicles carry stress-response proteins:** Rutter and Innes (2017) demonstrated that extracellular vesicles isolated from the leaf apoplast carry stress-response proteins and small RNAs [20], supporting the EV-mediated RNA transfer model.

### 1.2 Maize RNAi Machinery

The maize genome (B73 reference; Schnable et al. 2009) [21] encodes a comprehensive RNA silencing toolkit. Qian et al. (2011) identified and characterized the Dicer-like (DCL), Argonaute (AGO), and RNA-dependent RNA polymerase (RDR) gene families in maize [9]. Zhai et al. (2014) further characterized the AGO gene family, identifying meiosis-enriched Argonaute proteins during sporogenesis [10]. Qin et al. (2019) demonstrated that maize AGO genes are differentially expressed in response to abiotic stress [22].

The polyploid nature of the maize genome (paleopolyploid with extensive segmental duplication) means many silencing components exist as duplicated paralogs, providing both redundancy and potential subfunctionalization. The functional RNAi pathway in maize has been exploited for host-induced gene silencing (HIGS) approaches against fungal pathogens and insect pests.

### 1.3 Bacterial EPS as a Delivery Matrix

Bacteria within biofilms produce extracellular polymeric substances (EPS) composed of polysaccharides, proteins, lipids, and nucleic acids [23, 24]. The EPS matrix serves as a protective microenvironment that can shield extracellular nucleic acids from degradation [24]. Microbial EPS also plays ecological roles in soil aggregation and plant-microbe interactions [25]. The seed-borne bacteriome of maize has been characterized, showing that bacterial communities associated with seeds can influence germination [26]. [INFERRED] In the M-9 system, the bacterial EPS likely serves as both a protective reservoir and a slow-release delivery system for exRNAs during the 4-8 hour seed imbibition period, concentrating them at the seed surface and shielding them from environmental RNases.

### 1.4 Maize Seed Germination Biology

#### 1.4.1 ABA/GA Balance

The antagonistic interplay between abscisic acid (ABA) and gibberellins (GA) constitutes the central hormonal axis governing maize seed germination versus maturation. White et al. (2000) demonstrated that endogenous GA~1~ levels in wild-type maize embryos reach approximately 1-3 ng/g fresh weight during early kernel development, with ABA levels peaking at approximately 100-500 ng/g fresh weight during mid-maturation [27]. When ABA levels are reduced (as in *viviparous* mutants), GAs stimulate a precocious germination program. GA biosynthesis inhibition enhances ABA signaling in cultured maize embryos [28].

During imbibition of non-dormant seeds, ABA catabolic genes (e.g., ABA 8'-hydroxylase) are induced and GA biosynthetic genes (e.g., GA3ox) are activated, tipping the balance toward germination [29]. Ethylene promotes germination as an ABA antagonist, and jasmonates interact with ethylene signaling during the process [30].

#### 1.4.2 Seed Reserve Mobilization

**Starch:** The maize endosperm constitutes ~80-85% of kernel dry weight and is the primary energy store. Starch degradation involves four alpha-amylase isozymes, one beta-amylase, and two pullulanase (debranching) enzymes [31]. Beta-amylase activity peaks early in development and is found primarily in the pericarp, with almost no activity in mature dry caryopses [32]. Alpha-amylase synthesis is initiated first in the scutellum, then in the aleurone layer, with exogenous calcium stimulating synthesis in both tissues [33].

**Storage proteins (Zeins):** Zeins constitute 50-70% of total maize endosperm protein, stored in protein bodies. Zein degradation is initiated approximately 2 days after imbibition, with most zeins hydrolyzed by day 8. Four cysteine proteases (26-33 kDa) have been purified from germinating maize endosperm, with pH optimum of 4.0, consistent with acidic compartment origin [34].

**Oil bodies:** The maize embryo (scutellum) contains ~30% oil as triacylglycerols. TAG lipases liberate free fatty acids, converted to sugars via beta-oxidation and the glyoxylate cycle [35].

#### 1.4.3 Sugar Sensing and Mobilization

Nine ZmHXK genes have been identified in maize, with only six (ZmHXK4-9) encoding catalytically active enzymes [36, 37]. ZmHXK4-6 and ZmHXK9 localize to mitochondria, while ZmHXK7-8 are cytosolic. Hexokinase-dependent sugar phosphorylation contributes to embryo germination, and ZmHXK promoters contain cis-elements for phytohormone responses and sugar repression [37].

The Miniature1 (Mn1) locus encodes INCW2, a cell wall invertase essential for sucrose unloading during endosperm development [38]. During germination, sucrose is transported from the scutellum to the embryo axis and hydrolyzed by invertases, with this sucrose-to-hexose conversion critical for supporting radicle cell expansion [39].

The trehalose-6-phosphate (T6P)/SnRK1 pathway provides global metabolic regulation: T6P inhibits SnRK1 activity, permitting growth-promoting processes when sugar levels are adequate [40]. During germination, SnRK1 activity decreases as T6P levels rise with sucrose mobilization.

#### 1.4.4 Imbibition and Radicle Emergence

Maize seeds follow the canonical triphasic water uptake pattern. Phase I (rapid imbibition) lasts ~0-8 hours. Phase II (metabolic reactivation) extends from ~8-18 hours with minimal net water uptake. Phase III coincides with radicle protrusion at ~18-24 hours under optimal conditions (25-28°C) [1, 39]. Cell wall loosening involves apoplastic acidification by plasma membrane H^+^-ATPase, activating expansins, endoglucanases, and xyloglucan endotransglycosylases [41].

#### 1.4.5 Redox Biology

The "oxidative window" model posits that germination occurs only when ROS levels fall within a critical range -- sufficient for signaling but below the damage threshold [42]. Upon imbibition, when moisture reaches ~50%, ROS generation shifts from non-enzymatic to enzymatic sources, with mitochondria being primary [43]. H~2~O~2~ acts as a signaling molecule through cysteine oxidation and hormone signal modulation [44].

Maize contains 119 non-redundant class III peroxidase genes (ZmPRXs) in 18 phylogenetic groups [45]. ZmPrx25 modulates apoplastic ROS homeostasis and promotes seed germination under stress [46]. ZmPRX1 overexpression increases drought tolerance by promoting root development and lignification [47].

Mitochondrial reactivation is remarkably rapid: Nietzel et al. (2020) demonstrated that ATP accumulation and oxygen uptake occur within minutes of hydration, with 412 cysteine peptides identified as redox-switched, representing central pathways of mitochondrial energy metabolism [48]. Paszkiewicz et al. (2017) confirmed that seed mitochondria are bioenergetically active immediately upon imbibition [49].

#### 1.4.6 Transport and Ion Homeostasis

The NPF (NRT1/PTR family) in maize comprises 78 NPF genes, 7 NRT2 genes, and 2 NRT3 genes [50, 51]. NPF transporters transport diverse substrates including nitrate, peptides, ABA, GA, and jasmonates [52]. In Arabidopsis, NPF4.6/AIT1 is an ABA importer whose mutation reduces ABA sensitivity during germination [53]. NPF3 transports gibberellins [54], and NPF2.10/GTR1 transports jasmonoyl-isoleucine and GA [55]. Maize ZmPTR1 is expressed in the scutellar epithelium during germination, transporting peptides from endosperm hydrolysis into the embryo [56]. Tal et al. (2023) demonstrated that NPF-mediated GA/ABA transport facilitates endodermal development [57].

#### 1.4.7 Ubiquitin-Proteasome System

The UPS is a central regulator of ABA signaling during germination. ABI3-INTERACTING PROTEIN 2 (AIP2) polyubiquitinates ABI3 for proteasomal degradation [58]. KEEP ON GOING (KEG) maintains low ABI5 levels in the absence of ABA; ABA triggers KEG self-ubiquitination, stabilizing ABI5 [59, 60]. DELLA proteins (GA repressors) are ubiquitinated by SCF(SLY1/GID2) in a GA-dependent manner [61]. Dynamic proteomics showed that selective mRNA translation and protein turnover are critical during germination [62].

### 1.5 Seed Priming Context

Seed priming is a well-established agricultural technology for maize. Melatonin priming improves waxy maize germination under chilling stress by promoting antioxidant systems and starch metabolism [63]. Hydropriming and osmopriming improve germination under various stress conditions [7, 64]. [INFERRED] The EPS-based seed treatment may combine conventional priming effects with a novel exRNA-mediated gene regulation component. Disentangling these effects is a central challenge for validation experiments.

---

## 2. Target Prioritization

### 2.1 Methodology

20 predicted maize gene targets were extracted from bioinformatic analysis of bacterial sRNA-maize mRNA complementarity. Each target was resolved using NCBI Gene, MaizeGDB (Zm00001eb v5 gene models), Ensembl Plants, and UniProt. Targets were evaluated for: (a) annotation quality, (b) functional relevance to germination, (c) pathway membership, and (d) mechanistic plausibility of downregulation promoting germination. Targets were scored on a 1-10 priority scale.

### 2.2 Annotation Resolution of Ambiguous Targets

Several target names were ambiguous and required resolution:

| Original Name | Resolution | Evidence |
|--------------|------------|---------|
| LOC100273360 | GDT1-like protein 3; Golgi Ca^2+^/Mn^2+^ transporter (UPF0016 family) | NCBI Gene; At homolog PAM71 (AT1G64150) |
| IDP8263 | ABA-responsive protein with PH-GRAM domain (the IDP tag is a genetic marker from ISU-IBM Map4, not a gene name) | NCBI LOC100285725; Fu et al. 2006 |
| PCO145926 | Calmodulin-like protein CML21; EF-hand Ca^2+^ sensor | NCBI LOC100193836 |
| si614021b09a | O-methyltransferase ZRP4-like; suberin/lignin biosynthesis | NCBI LOC100272885; AdoMet MTase domain |
| AI714716 | MODIFIER OF SNC1 1 (MOS1-like); BAT2/Myb_Cef domain chromatin/immunity regulator | NCBI LOC103650547; At homolog AT4G24680 |
| PRH130 | Protein phosphatase 2C 32 (PP2C32); **NOT** an RNA helicase | NCBI LOC103635536; PP2C catalytic domain |
| IBP1 | Initiator Binding Protein 1; SANT/Myb + UBL domain transcription factor; **NOT** BiP/GRP78 chaperone | NCBI LOC542426; binds Shrunken-1 promoter |

**Critical corrections:**
- **IBP1** was originally annotated as "stress/heat-inducible binding protein" suggesting BiP/GRP78. This is incorrect. IBP1 is a transcription factor containing SANT/Myb and ubiquitin-like domains that binds the initiator element of the Shrunken-1 gene. Overexpression in tobacco reduces internode elongation and alters gibberellin balance.
- **PRH130** was potentially confused with RNA helicases. It encodes PP2C32, a Group A protein phosphatase 2C that is a negative regulator of ABA signaling (dephosphorylates and inactivates SnRK2 kinases).
- **CYP10** resolves to CYP72A14, a cytochrome P450 monooxygenase (NOT a cyclophilin, despite the CYP prefix overlap).

### 2.3 v4-to-v5 Gene Model Mappings

| v4 ID | v5 ID | Annotation |
|-------|-------|------------|
| Zm00001d048453 | Zm00001eb403550 | LRR receptor-like Ser/Thr kinase |
| Zm00001d011422 | Zm00001eb358860 | Cytochrome P450 72A15 |
| Zm00001d001877 | Zm00001eb066630 | Phytosulfokine receptor 1 (PSKR1-like) |

### 2.4 Duplicate Analysis

CYP10 (Zm00001eb159250 / CYP72A14) and Zm00001d011422 (Zm00001eb358860 / CYP72A15) are **paralogs** from the same CYP72A subfamily but are distinct loci on different chromosomes (chromosome 3 and chromosome 8 respectively). No true duplicates were found among the 20 entries.

### 2.5 Ranked Target Table (20 Unique Targets)

| Rank | Gene Model | Name | Best Annotation | Theme | At Homolog | Score |
|------|-----------|------|-----------------|-------|------------|-------|
| 1 | Zm00001eb197370 | ABI40 | B3/VP1-type ABA-responsive TF | ABA/dormancy | AT3G24650 (ABI3) | 10 |
| 2 | Zm00001eb018090 | PRH130 | PP2C32; negative regulator of ABA signaling | ABA/dormancy | Group A PP2C | 10 |
| 3 | Zm00001eb154520 | HEX6 | Hexokinase-2-like; glucose sensor | Sugar sensing | AT4G29130 (HXK1) | 9 |
| 4 | Zm00001eb385450 | NPF15 | PTR2/NPF4.6; ABA/peptide transporter | Transport/ABA | NPF4.6/AIT1 | 9 |
| 5 | Zm00001eb333290 | PRX91 | Peroxidase 72 precursor; class III PRX | ROS/redox | AT5G66390 | 8 |
| 6 | Zm00001eb044800 | RING63 | RING-HC E3 ubiquitin ligase (Hakai-like) | Ubiquitin/proteostasis | RING-HC family | 8 |
| 7 | Zm00001eb065740 | AHL9 | AT-hook nuclear localized protein 5 | Chromatin/growth | AT2G45850 | 8 |
| 8 | Zm00001eb187270 | MYBR64 | MYB-related single-repeat R1-MYB TF | Chromatin/TF | CCA1/CPC-like | 7 |
| 9 | Zm00001eb194870 | RING265 | RING-IBR-RING E3 ubiquitin ligase | Ubiquitin/proteostasis | RBR E3 family | 7 |
| 10 | Zm00001eb408850 | IDP8263 | ABA-responsive PH-GRAM domain protein | ABA signaling | Unresolved | 7 |
| 11 | Zm00001eb159250 | CYP10 | Cytochrome P450 72A14 | Metabolism | CYP72A cluster | 6 |
| 12 | Zm00001eb303410 | ppr377 | PPR protein; mitochondrial RNA processing | Organelle RNA | AT1G80270 | 6 |
| 13 | Zm00001eb397700 | IBP1 | Initiator Binding Protein 1; SANT/Myb TF | Chromatin/TF | Novel | 6 |
| 14 | Zm00001eb136860 | AI714716 | MOS1-like; chromatin/immunity regulator | Epigenetic/defense | AT4G24680 | 5 |
| 15 | Zm00001eb292850 | si614021b09a | O-methyltransferase ZRP4-like | Cell wall | COMT/CCoAOMT | 5 |
| 16 | Zm00001eb388550 | PCO145926 | Calmodulin-like CML21; Ca^2+^ sensor | Defense/Ca^2+^ | CML family | 5 |
| 17 | Zm00001eb403550 | (v4: Zm00001d048453) | LRR receptor-like kinase | Defense | AT1G12460 | 4 |
| 18 | Zm00001eb358860 | (v4: Zm00001d011422) | Cytochrome P450 72A15 | Metabolism | CYP72A cluster | 4 |
| 19 | Zm00001eb066630 | (v4: Zm00001d001877) | Phytosulfokine receptor 1 (PSKR1-like) | Defense/growth | AT2G02220 | 4 |
| 20 | Zm00001eb036320 | LOC100273360 | GDT1-like Golgi Ca^2+^/Mn^2+^ transporter | Transport/ion | AT1G64150 | 3 |

### 2.6 Key Rationale for Top Targets

**Rank 1 -- ABI40, B3/VP1-type ABA TF (Zm00001eb197370):** [KNOWN] The maize founding member of this family is Viviparous1 (VP1). Null alleles of VP1 cause precocious germination on the ear (vivipary), demonstrating that VP1 is a master repressor of germination during seed development [65]. VP1 activates LEA and Em genes while repressing germination-specific genes such as alpha-amylase [65]. In Arabidopsis, ABI3 mutants germinate faster and have reduced ABA sensitivity [66]. In sorghum, ABI4 and ABI5 bind GA 2-oxidase promoters, linking ABA signaling to GA catabolism [67]. [INFERRED] Downregulating ABI40 would reduce ABA sensitivity, derepress germination-specific genes including alpha-amylase, and accelerate the dormancy-to-germination transition. This is the highest-value single target.

**Rank 2 -- PRH130 / PP2C32 (Zm00001eb018090):** [KNOWN] Group A PP2Cs are key negative regulators of ABA signaling. They dephosphorylate and inactivate SnRK2 kinases, which are positive transducers of ABA signals. In the canonical ABA pathway, ABA binds PYR/PYL/RCAR receptors, which then inhibit PP2Cs, releasing SnRK2s to phosphorylate downstream targets including ABI5 and ion channels [29]. [INFERRED] Downregulating PP2C32 would paradoxically INCREASE ABA sensitivity (since PP2C is a negative regulator). This would stabilize active SnRK2, enhance ABI5 phosphorylation, and potentially DELAY germination. **However**, PP2Cs also have ABA-independent functions and some PP2C members positively regulate specific growth processes. The net effect depends on PP2C32's specific substrate repertoire and expression domain. **This target requires careful experimental validation before concluding whether downregulation helps or hinders germination.**

**Rank 3 -- HEX6, Hexokinase (Zm00001eb154520):** [KNOWN] Hexokinases serve dual functions as metabolic enzymes and glucose sensors [68, 69]. In maize, six of nine ZmHXK genes encode catalytically active enzymes, with ZmHXK4-6 and ZmHXK9 mitochondria-localized [37]. The glucose-ABA crosstalk is well-established: glucose-specific ABA accumulation is essential for HXK-mediated responses, and *gin2* mutants are insensitive to glucose-mediated germination delay [70]. [INFERRED] Downregulating HEX6 would reduce glucose sensing capacity, potentially rendering the embryo insensitive to glucose-mediated germination delay (similar to *gin2*). This could break the glucose-ABA positive feedback loop, favoring germination. However, reduced hexose phosphorylation would also impair glycolytic flux. The signaling effect likely dominates over the metabolic effect due to family redundancy.

**Rank 4 -- NPF15, PTR2/NPF4.6 (Zm00001eb385450):** [KNOWN] NPF4.6/AIT1 in Arabidopsis is an ABA importer; *ait1* mutants show reduced ABA sensitivity during germination [53]. NPF transporters also transport GA, JA-Ile, and peptides [54, 55]. In maize, ZmPTR1 transports peptides from endosperm hydrolysis into the embryo during germination [56]. [INFERRED] If NPF15 functions as an ABA importer (like AIT1), its downregulation would reduce ABA import into the embryo, lowering local ABA concentration and accelerating germination. If it is a peptide transporter (like ZmPTR1), its downregulation would impair amino acid supply but not directly affect hormone signaling. The NPF4.6 homology strongly suggests ABA transport activity.

**Rank 5 -- PRX91, Class III Peroxidase (Zm00001eb333290):** [KNOWN] Class III peroxidases have a paradoxical dual function: they can both consume H~2~O~2~ (peroxidative cycle, causing cell wall stiffening) and generate ROS (hydroxylic cycle, causing cell wall loosening) [71]. In Arabidopsis, *Atprx16* knockout showed significantly earlier testa and endosperm rupture, indicating that specific PRXs restrict germination timing through cell wall stiffening [72]. In maize, peroxidase activity increases in the scutellar apoplast 24 hours after imbibition [73]. ZmPrx25 overexpression promotes seed germination under stress [46]. [INFERRED] If PRX91 is predominantly a ROS-scavenger/cell wall stiffener, its downregulation would (a) increase local H~2~O~2~ levels, potentially pushing through the oxidative window, and (b) reduce cell wall cross-linking, facilitating radicle protrusion. The Atprx16 precedent supports this interpretation.

**Rank 6 -- RING63, RING-HC E3 Ligase (Zm00001eb044800):** [KNOWN] The maize genome contains 590 RING proteins [74]. RING E3 ligases play critical roles in ABA signaling: KEG targets ABI5 for degradation (KEG loss = ABA hypersensitivity) [59, 60]; AIP2 targets ABI3 for degradation (AIP2 loss = ABA hypersensitivity) [58]; ZmXerico1/2 target ABA 8'-hydroxylase for degradation, elevating ABA [75]. [INFERRED] The effect of RING63 downregulation depends entirely on its substrate specificity. If it targets negative regulators of growth (like SDIR1 targeting SDIRIP1), downregulation could promote germination. If it targets ABI3/ABI5 for degradation (like AIP2/KEG), downregulation would stabilize ABA signaling and inhibit germination. Substrate identification is essential.

**Rank 7 -- AHL9, AT-Hook Nuclear Localized Protein (Zm00001eb065740):** [KNOWN] AHL proteins bind AT-rich DNA via the AT-hook motif and remodel chromatin through S/MAR interactions [76]. SOB3/AHL29 and ESC/AHL27 are growth-suppressive in Arabidopsis: overexpression represses hypocotyl growth [77]. The mechanism involves AHL binding to YUCCA9 promoter S/MAR regions, recruiting the SWR1 chromatin remodeling complex to deposit H2A.Z, repressing auxin biosynthesis [78]. [INFERRED] Downregulating AHL9 would de-repress growth-promoting genes (including auxin biosynthesis), leading to enhanced cell elongation in the coleoptile, mesocotyl, and radicle. This directly addresses the "seedling vigor" phenotype.

**Rank 8 -- MYBR64, MYB-Related TF (Zm00001eb187270):** [KNOWN] In rice, MYBS1 activates alpha-amylase under sugar starvation during germination, while MYBS2 represses it [79]. In maize, ZmMYB59 overexpression negatively regulates germination by reducing GA levels and increasing ABA [80]. [INFERRED] If MYBR64 functions like ZmMYB59 (a germination repressor), its downregulation would relieve transcriptional repression and accelerate germination. If it functions like MYBS1 (an activator of starch mobilization), its downregulation would impair alpha-amylase induction. The "MYB-related" (single-repeat) classification makes it more likely to be a regulatory factor in the CCA1/LHY-like or MYBS-like category.

### 2.7 Pathway Category Summary

**ABA/GA Signaling and Dormancy (3 targets):**
- ABI40: B3/VP1-type ABA transcription factor
- PRH130/PP2C32: Negative regulator of ABA signaling
- IDP8263: ABA-responsive PH-GRAM domain protein

**ROS/Redox and Metabolism (3 targets):**
- PRX91: Class III peroxidase (H~2~O~2~ metabolism/cell wall)
- CYP10/CYP72A14: Cytochrome P450 monooxygenase
- CYP72A15: Cytochrome P450 monooxygenase (paralog)

**Sugar Sensing (1 target):**
- HEX6: Hexokinase; glucose sensor and metabolic enzyme

**Ubiquitin/Proteostasis (2 targets):**
- RING63: RING-HC E3 ubiquitin ligase
- RING265: RING-IBR-RING E3 ubiquitin ligase

**Transport (2 targets):**
- NPF15: NRT1/PTR family; ABA/peptide/nitrate transporter
- LOC100273360: GDT1/UPF0016 Golgi Ca^2+^/Mn^2+^ transporter

**Chromatin/Transcription Regulation (4 targets):**
- AHL9: AT-hook nuclear localized; growth-suppressive chromatin remodeler
- MYBR64: MYB-related single-repeat TF
- IBP1: Initiator Binding Protein; SANT/Myb + UBL domain TF
- AI714716/MOS1: Chromatin/immunity regulator

**Defense (3 targets):**
- CML21/PCO145926: Calmodulin-like Ca^2+^ sensor
- LRR-RLK (Zm00001eb403550): Defense receptor kinase
- PSKR1-like (Zm00001eb066630): Phytosulfokine receptor

**Cell Wall (1 target):**
- si614021b09a/ZRP4-like: O-methyltransferase; suberin/lignin biosynthesis

**Organelle RNA Processing (1 target):**
- ppr377: PPR protein; mitochondrial RNA processing

---

## 3. Mechanistic Narrative

### 3.1 Theme 1: ABA/Dormancy Axis Derepression

**Central thesis:** Bacterial exRNAs simultaneously attack multiple nodes of ABA signaling, from the transcription factor level (ABI40) through signal transduction (IDP8263) to hormone transport (NPF15), creating a coordinated reduction in ABA sensitivity that accelerates the dormancy-to-germination transition.

[KNOWN] ABI3/VP1-family transcription factors are master regulators of seed dormancy in cereals. VP1 null mutants exhibit vivipary (precocious germination on the ear) [65]. ABI4 directly promotes ABI5 transcription and represses ABA catabolic genes [66]. NPF4.6/AIT1 imports ABA into cells; *ait1* mutants show reduced ABA sensitivity during germination [53].

[INFERRED] The coordinated downregulation of ABI40 (reduce transcriptional output of ABA-responsive genes), NPF15 (reduce ABA import into embryo), and IDP8263 (reduce ABA perception at membranes) would produce a multi-pronged attack on ABA signaling. The VP1/ABI3 target alone can produce vivipary in maize, so even partial downregulation of ABI40 could significantly accelerate germination timing.

**Note on PRH130/PP2C32:** This target is paradoxical. PP2Cs are negative regulators of ABA signaling, so downregulating PP2C32 would be expected to INCREASE ABA sensitivity and potentially DELAY germination. Unless PP2C32 has a non-canonical function, or unless the bacterial sRNA targeting is imprecise and partially affects other PP2C transcripts in a complex manner, this target does not fit the germination-promoting narrative. **This is flagged as a potential counterexample that could help discriminate between RNA-mediated and non-specific effects.**

### 3.2 Theme 2: Sugar-Energy Metabolic Rewiring

**Central thesis:** Bacterial exRNAs modulate sugar sensing (HEX6) and transcriptional regulators of starch mobilization (MYBR64), effectively reprogramming the metabolic landscape to accelerate reserve mobilization and energy production during the critical first 24 hours of imbibition.

[KNOWN] Glucose-ABA crosstalk operates through hexokinase: glucose accumulation triggers ABA biosynthesis via HXK signaling [68, 69, 70]. In cereals, MYBS1/MYBS2 regulate alpha-amylase expression under sugar starvation [79]. ZmMYB59 negatively regulates germination [80].

[INFERRED] Downregulating HEX6 would break the glucose-ABA positive feedback loop: as starch is mobilized to glucose during imbibition, reduced HXK signaling would prevent the glucose-triggered ABA accumulation that normally slows germination. Simultaneously, if MYBR64 functions as a germination repressor (like ZmMYB59), its downregulation would derepress starch mobilization genes. Together, this creates a "full throttle" metabolic state: starch is mobilized efficiently but the glucose signal does not trigger a counterbalancing ABA response.

### 3.3 Theme 3: Redox-Proteostasis Optimization

**Central thesis:** Bacterial exRNAs fine-tune the ROS landscape (PRX91) and protein turnover machinery (RING63, RING265), optimizing the "oxidative window" for germination and accelerating the clearance of dormancy-associated proteins.

[KNOWN] The oxidative window requires precise ROS balance [42, 43]. Class III peroxidases can both scavenge and generate ROS [71]. Atprx16 knockout accelerates germination [72]. RING E3 ligases control turnover of ABA signaling components [58, 59, 60].

[INFERRED] Downregulating PRX91 (if it functions as a ROS scavenger/cell wall stiffener) would increase local H~2~O~2~, push toward the pro-germination side of the oxidative window, and reduce cell wall cross-linking at the radicle emergence point. Simultaneously, modulation of RING63/RING265 activity would alter the turnover rates of dormancy-associated proteins, potentially accelerating their clearance.

### 3.4 Theme 4: Growth-Defense Resource Reallocation

**Central thesis:** Downregulation of defense-associated genes (CML21, LRR-RLK, PSKR1, MOS1) and cell wall fortification (ZRP4-like O-methyltransferase) reduces metabolic investment in defense during the germination window, redirecting carbon and nitrogen toward reserve mobilization and axis elongation.

[INFERRED] This theme is synergistic with Themes 1-3: reduced defense expenditure provides additional metabolic resources to fuel the accelerated germination program. The O-methyltransferase (si614021b09a) is particularly interesting: ZRP4 is involved in suberin and lignin biosynthesis, and its downregulation would reduce cell wall fortification, potentially facilitating radicle emergence.

### 3.5 Two Causal Models

#### Model A: Hormone-Metabolic Derepression (Primary Driver)

```
Bacterial exRNAs
    │
    ├──→ Silence ABI40 (VP1-like) → ↓ ABA-responsive gene expression → ↑ alpha-amylase
    │
    ├──→ Silence NPF15 (ABA importer) → ↓ ABA import into embryo → ↓ local ABA
    │
    ├──→ Silence HEX6 → ↓ glucose-ABA feedback → break inhibitory loop
    │
    ├──→ Silence AHL9 → derepress auxin biosynthesis → ↑ cell elongation
    │
    └──→ Silence MYBR64 → derepress germination genes → ↑ starch mobilization

    Combined effect: ABA derepression + metabolic acceleration → FASTER GERMINATION + VIGOR
```

**Testable prediction A:** If Model A is correct:
- ABA levels will be lower in M-9-treated embryo axes at 12-24 hours vs. controls
- Alpha-amylase activity will be elevated in aleurone/scutellum at 24-48 hours
- Coleoptile/radicle elongation rate will increase before any change in ROS markers
- Exogenous ABA (10 μM) should abolish or reduce the M-9 germination benefit

#### Model B: Redox-Proteostasis Acceleration (Primary Driver)

```
Bacterial exRNAs
    │
    ├──→ Silence PRX91 → shift oxidative window → ↑ H2O2 signaling + ↓ cell wall stiffening
    │
    ├──→ Silence RING63/265 → alter protein turnover → accelerate dormancy protein clearance
    │
    ├──→ Silence ZRP4-like OMT → ↓ lignification → ↓ cell wall rigidity at radicle tip
    │
    └──→ Silence ppr377 → modulate mitochondrial efficiency → alter energy metabolism

    Combined effect: Optimized ROS + faster protein turnover + looser cell walls → EMERGENCE
```

**Testable prediction B:** If Model B is correct:
- ROS profiling (DHE/H~2~DCFDA) will show altered O~2~^-^/H~2~O~2~ ratios at 6-12 hours
- Cell wall stiffness (measured by AFM or extensometer) will be reduced at radicle tip
- SOD/CAT/APX enzyme activity ratios will differ between treatments
- Adding exogenous H~2~O~2~ (1 mM) to controls should partially phenocopy M-9 effects

**Distinguishing experiment:** Measure ABA levels AND ROS profiles simultaneously at 12 hours. If ABA changes precede ROS changes, Model A is primary. If ROS changes precede ABA changes, Model B is primary. If both change simultaneously, a combined model operates.

---

## 4. Confounders and Alternative Explanations

### 4.1 Six Confounders

**Confounder 1: EPS Osmopriming (HIGHEST CONCERN)**
[KNOWN] Hydropriming and osmopriming improve maize germination under various conditions [7, 64]. The bacterial EPS is a hydrated polymer matrix that could produce identical osmopriming effects simply through water activity modulation.
**Impact:** Could explain 100% of germination improvement without any RNA involvement.
**Control:** Compare EPS (intact) vs. EPS (RNase-treated) vs. synthetic hydrogel (equivalent water activity) vs. water-only.

**Confounder 2: Polysaccharide Elicitor Effects**
[KNOWN] Bacterial EPS polysaccharides can trigger plant defense priming and induce organ-specific resistance responses [81]. Paradoxically, mild defense priming can enhance overall seedling vigor.
**Impact:** EPS polysaccharide fractions may trigger beneficial priming independent of RNA content.
**Control:** Heat-denatured EPS (destroys RNA secondary structure but preserves polysaccharides) vs. intact EPS.

**Confounder 3: Biopriming by Residual Bacteria**
[KNOWN] The maize seed-borne bacteriome influences germination [26]. If the EPS preparation contains viable bacteria, germination enhancement could result from conventional biopriming.
**Control:** Filter-sterilize (0.22 μm) vs. UV-sterilize vs. untreated EPS.

**Confounder 4: Nutrient Effects**
[INFERRED] The EPS matrix contains proteins, amino acids, and minerals that may provide metabolic fuel.
**Control:** Dialyzed EPS (retain macromolecules, remove small molecules) vs. dialysate-only vs. complete EPS.

**Confounder 5: pH and Ionic Strength Effects**
[INFERRED] The EPS solution may alter local pH and ionic environment, affecting enzyme activities and ion channel kinetics.
**Control:** Buffer-matched controls at equivalent pH and ionic strength.

**Confounder 6: Bioinformatic False Positives**
[KNOWN] Computational prediction of sRNA-mRNA complementarity generates high false-positive rates in a 2.3 Gb genome [21]. Many predicted targets may not be genuine.
**Control:** Validate target downregulation by RT-qPCR for top 8 targets using geNorm [82] or NormFinder [83] reference gene selection, and 2^-ΔΔCt^ quantification [84, 85].

### 4.2 The Killer Experiment

**RNase Treatment of the M-9 Solution**

**Protocol:**
1. Prepare M-9 EPS seed treatment as standard
2. Split into three aliquots:
   - Aliquot A: Untreated M-9 (positive control)
   - Aliquot B: M-9 + RNase A (100 μg/mL, 37°C, 1 hour)
   - Aliquot C: M-9 + heat-inactivated RNase A (control for buffer effects)
3. Treat maize seeds (B73 inbred, n=50 per treatment, 4 replicates)
4. Soak 4-8 hours until full imbibition
5. Transfer to paper towel germination test
6. Score germination (radicle ≥2 mm) at 24, 48, 72, 96 hours
7. Measure coleoptile length, radicle length, and fresh weight at 7 days

**Interpretation:**
- If B ≈ C << A: RNA is essential → proceed with full validation
- If B ≈ C ≈ A: RNA is not essential → investigate EPS components
- If B < A but B > C: Partial RNA contribution → multiple active components

**Cost:** ~$200-500
**Timeline:** 2 weeks
**Decision value:** CRITICAL

---

## 5. Validation Plan

### 5.1 Tier 1: Essential Experiments (Weeks 1-4, ~$1,500)

**Experiment 1: RNase Elimination (The Killer Experiment)**
- As described in Section 4.2
- Deliverable: Go/no-go decision on RNA involvement

**Experiment 2: Target Transcript Quantification**
- RT-qPCR on 10 high-priority targets (Ranks 1-10)
- Timepoints: 0, 6, 12, 24, 48 hours post-imbibition
- Treatments: M-9-treated vs. water-control
- Tissue: Embryo axis + scutellum (dissected)
- Reference genes: Select 3 stable references from candidates (ZmActin, ZmTubulin, ZmEF1a, ZmUBQ) using geNorm [82] and NormFinder [83]
- Quantification: 2^-ΔΔCt^ method [84, 85]
- Deliverable: Validated target downregulation (or lack thereof)
- Minimum interpretable result: ≥2-fold reduction in ≥3 of 10 targets

**Experiment 3: ABA/GA Quantification**
- LC-MS/MS of ABA, GA~1~, GA~4~ in embryo axes
- Timepoints: 0, 6, 12, 24 hours
- Treatments: M-9 vs. water vs. RNase-treated M-9
- Deliverable: Tests hormonal derepression hypothesis

### 5.2 Tier 2: Mechanistic Discrimination (Weeks 5-8, ~$1,200)

**Experiment 4: Alpha-Amylase and Invertase Activity**
- Alpha-amylase: DNS reducing sugar method in aleurone/scutellum extracts
- Invertase: CWI, VI, total activity in embryo axes
- Timepoints: 0, 12, 24, 48, 72 hours
- Deliverable: Tests starch mobilization acceleration hypothesis

**Experiment 5: ROS and Antioxidant Profiling**
- O~2~^-^: DHE fluorescence in embryo axis sections
- H~2~O~2~: H~2~DCFDA fluorescence + Amplex Red quantitative assay
- Enzyme panel: SOD, CAT, APX, GR activities
- Timepoints: 6, 12, 24, 48 hours
- Deliverable: Tests oxidative window modulation

### 5.3 Tier 3: Conclusive Evidence (Weeks 9-12, ~$900)

**Experiment 6: Degradome Sequencing (PARE)**
- Parallel Analysis of RNA Ends [86] in M-9-treated vs. control at 24 hours
- Deliverable: Direct evidence of sRNA-guided mRNA cleavage at predicted target sites

**Experiment 7: Synthetic sRNA Mimics**
- Design synthetic 21-nt RNA duplexes for top 3 predicted bacterial sRNAs
- Apply to maize seeds during imbibition (with transfection reagent)
- Score germination and seedling phenotype
- Deliverable: Sufficiency test

### 5.4 Indicative Timeline

```
Week 1-2:   Exp 1 (RNase elimination) ──────► GO/NO-GO DECISION
Week 2-4:   Exp 2 (RT-qPCR) + Exp 3 (ABA/GA)
Week 5-8:   Exp 4 (amylase/invertase) + Exp 5 (ROS profiling)
Week 9-12:  Exp 6 (degradome-seq) + Exp 7 (synthetic sRNAs)
            │
            ▼
     PUBLICATION-READY DATA
```

### 5.5 Maize-Specific Experimental Considerations

1. **Inbred selection:** B73 is recommended as the reference genotype matching the genome assembly [21]. Alternative: W22 (for Mutator transposon resources) or Mo17 (for hybrid vigor comparisons).

2. **Germination conditions:** 25-28°C, dark, paper towel roll method per ISTA protocols. Score radicle emergence (≥2 mm) at 24-hour intervals.

3. **Tissue dissection:** Separate embryo axis, scutellum, and endosperm for tissue-specific expression analysis. The scutellum is the primary site of enzyme secretion and nutrient transfer.

4. **Imbibition timing:** Apply M-9 treatment during Phase I (0-8 hours) for maximum uptake. The transition to Phase II (~8-18 hours) represents the metabolic reactivation window.

5. **Dose-response:** Test M-9 at 0.5×, 1×, 2×, and 4× standard concentration to establish dose-dependency, which would support a specific (rather than bulk osmotic) mechanism.

---

## 6. Conclusions

### 6.1 Summary of Findings

1. Of 20 unique maize gene targets, **7 are high-priority** (score ≥8) with clear mechanistic relevance to germination: ABI40, PRH130/PP2C32, HEX6, NPF15, PRX91, RING63, and AHL9. The ABI40/VP1-family target has the strongest single-gene evidence from maize viviparous mutant phenotypes [65].

2. PRH130/PP2C32 is a paradoxical target: as a negative regulator of ABA signaling, its downregulation would be expected to enhance ABA sensitivity and delay germination, contradicting the observed phenotype. This could serve as an internal control -- if PRH130 transcripts are NOT downregulated in treated seeds, it supports specificity of the RNA-mediated mechanism.

3. Two competing causal models make testable, distinguishable predictions. Model A (Hormone-Metabolic Derepression) is more parsimonious and supported by the VP1 vivipary precedent. Model B (Redox-Proteostasis Acceleration) invokes a more novel mechanism but is supported by the oxidative window literature [42, 43, 48].

4. Six confounders must be addressed before accepting the exRNA hypothesis. EPS osmopriming is the most threatening alternative. The RNase killer experiment addresses this directly.

5. A 12-week, ~$3,600 experimental program can deliver publication-quality evidence for or against the exRNA hypothesis.

### 6.2 Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| EPS effect is entirely osmopriming | Medium-High | Fatal to hypothesis | RNase experiment (Tier 1) |
| Target predictions are false positives | Medium | Reduces actionable targets | RT-qPCR validation panel |
| sRNAs don't survive imbibition | Medium | Fatal to hypothesis | RNA extraction from imbibed seeds |
| PRH130 downregulation delays germination | Medium | Contradicts phenotype | Internal specificity control |
| PPR377 downregulation harms energy metabolism | Medium | Counterproductive target | Does not affect other targets |
| Effect is real but too small to commercialize | Medium | Limits application | Dose-response optimization |

---

## Appendix A: Maize Genome and RNAi Context

### A.1 Maize Genome Statistics

The maize B73 reference genome (Schnable et al. 2009) [21]:
- Genome size: ~2.3 Gb (one of the largest among crop plants)
- Predicted protein-coding genes: ~32,000-39,000 (depending on annotation version)
- Paleopolyploid with extensive segmental and tandem duplications
- Class III peroxidase genes: 119 [45]
- RING E3 ubiquitin ligase genes: 590 [74]
- NPF transporter genes: 78 [50]
- Hexokinase genes: 9 [36]
- Cytochrome P450 genes: 263 [87]

### A.2 Maize RNAi Toolkit

Key RNA silencing components identified by Qian et al. (2011) [9] and Zhai et al. (2014) [10]:
- DCL (Dicer-like): Multiple paralogs
- AGO (Argonaute): Multiple paralogs with tissue-specific expression
- RDR (RNA-dependent RNA polymerase): Amplification of silencing signal

SIGS (spray-induced gene silencing) has been demonstrated in cereal-fungal pathosystems [11, 13], confirming that exogenous dsRNA can enter plant cells and trigger the RNAi pathway.

---

## Bibliography

[1] Bewley JD. (1997) Seed germination and dormancy. *Plant Cell*, 9(7): 1055-1066. DOI: 10.1105/tpc.9.7.1055

[2] Bewley JD, Bradford KJ, Hilhorst HWM, Nonogaki H. (2013) Seeds: Physiology of Development, Germination and Dormancy. 3rd Edition. Springer. DOI: 10.1007/978-1-4614-4693-4

[3] Finkelstein R, Reeves W, Ariizumi T, Steber C. (2008) Molecular aspects of seed dormancy. *Annual Review of Plant Biology*, 59: 387-415. DOI: 10.1146/annurev.arplant.59.032607.092740

[4] Weitbrecht K, Muller K, Leubner-Metzger G. (2011) First off the mark: early seed germination. *Journal of Experimental Botany*, 62(10): 3289-3309. DOI: 10.1093/jxb/erq408

[5] Fait A, Angelovici R, Less H, Ohad I, Urbanczyk-Wochniak E, Fernie AR, Galili G. (2006) Arabidopsis seed development and germination is associated with temporally distinct metabolic switches. *Plant Physiology*, 142(3): 839-854. DOI: 10.1104/pp.106.086694

[6] Finch-Savage WE, Leubner-Metzger G. (2006) Seed dormancy and the control of germination. *New Phytologist*, 171(3): 501-523. DOI: 10.1111/j.1469-8137.2006.01787.x

[7] Paparella S, Araujo SS, Rossi G, Wijayasinghe M, Carbonera D, Balestrazzi A. (2015) Seed priming: state of the art and new perspectives. *Plant Cell Reports*, 34(8): 1281-1293. DOI: 10.1007/s00299-015-1784-y

[8] Jisha KC, Vijayakumari K, Puthur JT. (2013) Seed priming for abiotic stress tolerance: an overview. *Acta Physiologiae Plantarum*, 35(5): 1381-1396. DOI: 10.1007/s11738-012-1186-5

[9] Qian Y, Cheng X, Liu Y, Jiang H, Zhu S, Cheng B. (2011) Identification and characterization of Dicer-like, Argonaute and RNA-dependent RNA polymerase gene families in maize. *Plant Cell Reports*, 30(7): 1347-1363. DOI: 10.1007/s00299-011-1046-6

[10] Zhai L, Sun W, Zhang K, Jia H, Liu L, Liu Z, Teng F, Zhang Z. (2014) Identification and characterization of Argonaute gene family and meiosis-enriched Argonaute during sporogenesis in maize. *Journal of Integrative Plant Biology*, 56(11): 1042-1052. DOI: 10.1111/jipb.12205

[11] Koch A, Biedenkopf D, Furch A, Weber L, Rossbach O, Abdellatef E, Linicus L, Johannsmeier J, Jelonek L, Goesmann A, Cardoza V, McMillan J, Mentzel T, Kogel KH. (2016) An RNAi-based control of *Fusarium graminearum* infections through spraying of long dsRNAs. *PLoS Pathogens*, 12(10): e1005901. DOI: 10.1371/journal.ppat.1005901

[12] Bologna NG, Voinnet O. (2014) The diversity, biogenesis, and activities of endogenous silencing small RNAs in Arabidopsis. *Annual Review of Plant Biology*, 65: 473-503. DOI: 10.1146/annurev-arplant-050213-035728

[13] Wang M, Weiberg A, Lin FM, Thomma BPHJ, Huang HD, Jin H. (2016) Bidirectional cross-kingdom RNAi and fungal uptake of external RNAs confer plant protection. *Nature Plants*, 2: 16151. DOI: 10.1038/nplants.2016.151

[14] Weiberg A, Wang M, Lin FM, Zhao H, Zhang Z, Kaloshian I, Huang HD, Jin H. (2013) Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. *Science*, 342(6154): 118-123. DOI: 10.1126/science.1239705

[15] Cai Q, Qiao L, Wang M, He B, Lin FM, Palmquist J, Huang SD, Jin H. (2018) Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. *Science*, 360(6393): 1126-1129. DOI: 10.1126/science.aar4142

[16] He B, Wang H, Liu G, Wang S, Cai Q, Thompson G, Jin H. (2023) Fungal small RNAs ride in extracellular vesicles to enter plant cells through clathrin-mediated endocytosis. *Nature Communications*, 14: 4383. DOI: 10.1038/s41467-023-40093-4

[17] He B, Cai Q, Qiao L, Huang CY, Wang S, Miao W, Ha T, Wang Y, Jin H. (2021) RNA-binding proteins contribute to small RNA loading in plant extracellular vesicles. *Nature Plants*, 7: 342-352. DOI: 10.1038/s41477-021-00863-8

[18] Cai Q, He B, Wang S, Fletcher S, Niu D, Mitter N, Birch PRJ, Jin H. (2021) Message in a Bubble: Shuttling small RNAs and proteins between cells and interacting organisms using extracellular vesicles. *Annual Review of Plant Biology*, 72: 497-524. DOI: 10.1146/annurev-arplant-081720-010616

[19] Dunker F, Trutzenberg A, Rothenpieler JS, Kuhn S, Prols R, Schreiber T, Tissier A, Kemen A, Kemen E, Huckelhoven R, Weiberg A. (2020) Oomycete small RNAs bind to the plant RNA-induced silencing complex for virulence. *eLife*, 9: e56096. DOI: 10.7554/eLife.56096

[20] Rutter BD, Innes RW. (2017) Extracellular vesicles isolated from the leaf apoplast carry stress-response proteins. *Plant Physiology*, 173(1): 728-741. DOI: 10.1104/pp.16.01253

[21] Schnable PS, Ware D, Fulton RS, Stein JC, Wei F, Pasternak S, et al. (2009) The B73 maize genome: complexity, diversity, and dynamics. *Science*, 326(5956): 1112-1115. DOI: 10.1126/science.1178534

[22] Qin F, Sun QW, Huang LM, Chen XS, Zhou DX. (2019) Expression analysis of Argonaute genes in maize in response to abiotic stress. *Hereditas*, 156: 27. DOI: 10.1186/s41065-019-0102-z

[23] Flemming HC, Wingender J. (2010) The biofilm matrix. *Nature Reviews Microbiology*, 8(9): 623-633. DOI: 10.1038/nrmicro2415

[24] Flemming HC, Wingender J, Szewzyk U, Steinberg P, Rice SA, Kjelleberg S. (2016) Biofilms: an emergent form of bacterial life. *Nature Reviews Microbiology*, 14(9): 563-575. DOI: 10.1038/nrmicro.2016.94

[25] Costa OYA, Raaijmakers JM, Kuramae EE. (2018) Microbial extracellular polymeric substances: ecological function and impact on soil aggregation. *Frontiers in Microbiology*, 9: 1636. DOI: 10.3389/fmicb.2018.01636

[26] dos Santos LF, Souta JF, Soares CP, da Rocha LO, Santos MLC, Grativol C, Roesch LFW, Olivares FL. (2021) Insights into the structure and role of seed-borne bacteriome during maize germination. *FEMS Microbiology Ecology*, 97(4): fiab024. DOI: 10.1093/femsec/fiab024

[27] White CN, Proebsting WM, Hedden P, Rivin CJ. (2000) Gibberellins and seed development in maize. I. Evidence that gibberellin/abscisic acid balance governs germination versus maturation pathways. *Plant Physiology*, 122(4): 1081-1088. DOI: 10.1104/pp.122.4.1081

[28] White CN, Rivin CJ. (2000) Gibberellins and seed development in maize. II. Gibberellin synthesis inhibition enhances abscisic acid signaling in cultured embryos. *Plant Physiology*, 122(4): 1089-1097. DOI: 10.1104/pp.122.4.1089

[29] Finkelstein R, Reeves W, Ariizumi T, Steber C. (2008) Molecular aspects of seed dormancy. *Annual Review of Plant Biology*, 59: 387-415. DOI: 10.1146/annurev.arplant.59.032607.092740

[30] Linkies A, Leubner-Metzger G. (2012) Beyond gibberellins and abscisic acid: how ethylene and jasmonates control seed germination. *Plant Cell Reports*, 31(2): 253-270. DOI: 10.1007/s00299-011-1180-1

[31] Doehlert DC, Kuo TM, Felker FC. (1991) Isolation of alpha-amylases and other starch degrading enzymes from endosperm of germinating maize. *Plant Science*, 78(1): 39-47. DOI: 10.1016/0168-9452(91)90192-B

[32] Lauriere C, Doyen C, Thevenot C, Daussant J. (1992) Beta-amylases in cereals: a study of the maize beta-amylase system. *Plant Physiology*, 100(2): 887-893. DOI: 10.1104/pp.100.2.887

[33] Frias I, Bernal-Lugo I. (1998) Amylases synthesis in scutellum and aleurone layer of maize seeds. *Phytochemistry*, 48(4): 597-604. DOI: 10.1016/S0031-9422(97)00964-3

[34] de Barros EG, Larkins BA. (1990) Purification and characterization of zein-degrading proteases from endosperm of germinating maize seeds. *Plant Physiology*, 94(1): 297-303. DOI: 10.1104/pp.94.1.297

[35] Eastmond PJ. (2006) SUGAR-DEPENDENT1 encodes a patatin domain triacylglycerol lipase that initiates storage oil breakdown in germinating Arabidopsis seeds. *Plant Cell*, 18(3): 665-675. DOI: 10.1105/tpc.105.040543

[36] Zhang Z, Zhang J, Chen Y, Li R, Wang H, Ding L, Wei J. (2014) Isolation, structural analysis, and expression characteristics of the maize hexokinase gene family. *Molecular Biology Reports*, 41(11): 7793-7807. DOI: 10.1007/s11033-014-3495-9

[37] Zheng S, Lu J, Yu D, Li J, Zhou H, Jiang D, Liu Z, Zhuang C. (2019) Biochemical properties and subcellular localization of six members of the HXK family in maize and its metabolic contribution to embryo germination. *BMC Plant Biology*, 19: 27. DOI: 10.1186/s12870-018-1605-x

[38] Cheng WH, Taliercio EW, Chourey PS. (1996) The Miniature1 seed locus of maize encodes a cell wall invertase required for normal development of endosperm and maternal cells in the pedicel. *Plant Cell*, 8(6): 971-983. DOI: 10.1105/tpc.8.6.971

[39] Sanchez-Linares L, Gavilanes-Ruiz M, Diaz-Pontones D, Guzman-Chavez F, Calzada-Alejo V, Zurita-Villegas V, Luna-Loaiza V, Moreno-Sanchez R, Bernal-Lugo I, Sanchez-Nieto S. (2012) Early carbon mobilization and radicle protrusion in maize germination. *Journal of Experimental Botany*, 63(12): 4513-4526. DOI: 10.1093/jxb/ers130

[40] Tsai AY-L, Gazzarrini S. (2014) Trehalose-6-phosphate and SnRK1 kinases in plant development and signaling: the emerging picture. *Frontiers in Plant Science*, 5: 119. DOI: 10.3389/fpls.2014.00119

[41] Cosgrove DJ. (2000) Loosening of plant cell walls by expansins. *Nature*, 407(6802): 321-326. DOI: 10.1038/35030000

[42] El-Maarouf-Bouteau H, Bailly C. (2008) Oxidative signaling in seed germination and dormancy. *Plant Signaling and Behavior*, 3(3): 175-182. DOI: 10.4161/psb.3.3.5539

[43] Bailly C. (2004) Active oxygen species and antioxidants in seed biology. *Seed Science Research*, 14(2): 93-107. DOI: 10.1017/S0960258504000133

[44] Wojtyla L, Lechowska K, Kubala S, Garnczarska M. (2016) Different modes of hydrogen peroxide action during seed germination. *Frontiers in Plant Science*, 7: 66. DOI: 10.3389/fpls.2016.00066

[45] Wang Y, Wang Q, Zhao Y, Han G, Zhu S. (2015) Systematic analysis of maize class III peroxidase gene family reveals a conserved subfamily involved in abiotic stress response. *Gene*, 566(1): 95-108. DOI: 10.1016/j.gene.2015.04.041

[46] ZmPrx25 study. (2025) Maize Peroxidase ZmPrx25 modulates apoplastic ROS homeostasis and promotes seed germination. *Antioxidants*, 14(9): 1067. DOI: 10.3390/antiox14091067

[47] Zhai X, Yan X, Zenda T, et al. (2024) Overexpression of the peroxidase gene ZmPRX1 increases maize seedling drought tolerance by promoting root development and lignification. *The Crop Journal*, 12(3): 753-765. DOI: 10.1016/j.cj.2024.04.008

[48] Nietzel T, Mostertz J, Ruberti C, Nee G, Fuchs P, Wagner S, Moseler A, Muller-Schussele SJ, Benamar A, Poschet G, et al. (2020) Redox-mediated kick-start of mitochondrial energy metabolism drives resource-efficient seed germination. *PNAS*, 117(1): 741-751. DOI: 10.1073/pnas.1910501117

[49] Paszkiewicz G, Gualberto JM, Benamar A, Macherel D, Logan DC. (2017) Arabidopsis seed mitochondria are bioenergetically active immediately upon imbibition. *Plant Cell*, 29(1): 109-128. DOI: 10.1105/tpc.16.00700

[50] Wang J, Li Y, Zhu F, Ming R, Chen LQ. (2023) Genome-wide identification and functional analysis of nitrate transporter genes in maize. *International Journal of Molecular Sciences*, 24(16): 12941. DOI: 10.3390/ijms241612941

[51] Xia X, Wei Q, Xiao C, Ye Y, Li Z, et al. (2023) Genomic survey of NPF and NRT2 transporter gene families in five inbred maize lines. *Genomics*, 115(2): 110555. DOI: 10.1016/j.ygeno.2022.110555

[52] Leran S, Varala K, Boyer JC, Chiurazzi M, Crawford N, et al. (2014) A unified nomenclature of NITRATE TRANSPORTER 1/PEPTIDE TRANSPORTER family members in plants. *Trends in Plant Science*, 19(1): 5-9. DOI: 10.1016/j.tplants.2013.08.008

[53] Kanno Y, Hanada A, Chiba Y, Ichikawa T, Nakazawa M, Matsui M, Koshiba T, Kamiya Y, Seo M. (2012) Identification of an abscisic acid transporter by functional screening using the receptor complex as a sensor. *PNAS*, 109(24): 9653-9658. DOI: 10.1073/pnas.1203567109

[54] Tal I, Zhang Y, Jorgensen ME, et al. (2016) The Arabidopsis NPF3 protein is a GA transporter. *Nature Communications*, 7: 11486. DOI: 10.1038/ncomms11486

[55] Saito H, Oikawa T, Hamamoto S, et al. (2015) The jasmonate-responsive GTR1 transporter is required for gibberellin-mediated stamen development in Arabidopsis. *Nature Communications*, 6: 6095. DOI: 10.1038/ncomms7095

[56] Doan DNP, et al. (2013) ZmPTR1, a maize peptide transporter expressed in the epithelial cells of the scutellum during germination. *Plant Molecular Biology*. DOI: 10.1007/s11103-013-0073-x

[57] Tal I, Zhang Y, Shani E, et al. (2023) Gibberellin and abscisic acid transporters facilitate endodermal suberin formation in Arabidopsis. *Nature Plants*, 9: 785-802. DOI: 10.1038/s41477-023-01391-3

[58] Zhang X, Garreton V, Chua NH. (2005) The AIP2 E3 ligase acts as a novel negative regulator of ABA signaling by promoting ABI3 degradation. *Genes & Development*, 19(13): 1532-1543. DOI: 10.1101/gad.1318705

[59] Stone SL, Williams LA, Farmer LM, Vierstra RD, Callis J. (2006) KEEP ON GOING, a RING E3 ligase essential for Arabidopsis growth and development, is involved in abscisic acid signaling. *Plant Cell*, 18(12): 3415-3428. DOI: 10.1105/tpc.106.046060

[60] Liu H, Stone SL. (2010) Abscisic acid increases Arabidopsis ABI5 transcription factor levels by promoting KEG E3 ligase self-ubiquitination and proteasomal degradation. *Plant Cell*, 22(8): 2630-2649. DOI: 10.1105/tpc.110.075960

[61] Oracz K, Stawska M. (2016) Cellular recycling of proteins in seed dormancy alleviation and germination. *Frontiers in Plant Science*, 7: 1128. DOI: 10.3389/fpls.2016.01128

[62] Galland M, Huguet R, Arc E, Cueff G, Job D, Rajjou L. (2014) Dynamic proteomics emphasizes the importance of selective mRNA translation and protein turnover during Arabidopsis seed germination. *Molecular & Cellular Proteomics*, 13(1): 1-14. DOI: 10.1074/mcp.M113.032227

[63] Cao Q, Li G, Cui Z, Yang F, Jiang X, Diallo L, Kong F. (2019) Seed priming with melatonin improves the seed germination of waxy maize under chilling stress via promoting the antioxidant system and starch metabolism. *Scientific Reports*, 9: 15044. DOI: 10.1038/s41598-019-51122-y

[64] Ibrahim EA. (2016) Seed priming to alleviate salinity stress in germinating seeds. *Journal of Plant Physiology*, 192: 38-46. DOI: 10.1016/j.jplph.2015.12.011

[65] Suzuki M, et al. (2003) Viviparous1 alters global gene expression patterns through regulation of abscisic acid signaling. *Plant Physiology*, 132(3): 1664-1677. DOI: 10.1104/pp.103.024323

[66] Shu K, et al. (2013) ABI4 regulates primary seed dormancy by regulating the biogenesis of abscisic acid and gibberellins in Arabidopsis. *PLoS Genetics*, 9(6): e1003577. DOI: 10.1371/journal.pgen.1003577

[67] Cantoro R, et al. (2013) In vitro binding of Sorghum bicolor transcription factors ABI4 and ABI5 to a conserved region of a GA 2-OXIDASE promoter. *Journal of Experimental Botany*, 64(18): 5721-5731. DOI: 10.1093/jxb/ert347

[68] Jang JC, et al. (1997) Hexokinase as a sugar sensor in higher plants. *Plant Cell*, 9(1): 5-19. DOI: 10.1105/tpc.9.1.5

[69] Moore B, et al. (2003) Role of the Arabidopsis glucose sensor HXK1 in nutrient, light, and hormonal signaling. *Science*, 300(5617): 332-336. DOI: 10.1126/science.1080585

[70] Price J, et al. (2003) Mechanisms of glucose signaling during germination of Arabidopsis. *Plant Physiology*, 132(3): 1424-1438. DOI: 10.1104/pp.103.020347

[71] Passardi F, et al. (2004) Performing the paradoxical: how plant peroxidases modify the cell wall. *Trends in Plant Science*, 9(11): 534-540. DOI: 10.1016/j.tplants.2004.09.002

[72] Jemmat AM, et al. (2020) Coordination of five class III peroxidase-encoding genes for early germination events of Arabidopsis thaliana. *Plant Science*, 298: 110565. DOI: 10.1016/j.plantsci.2020.110565

[73] Tnani H, et al. (2014) Peroxidase activity in scutella of maize in association with anatomical changes during germination. *SpringerPlus*, 3: 399. DOI: 10.1186/2193-1801-3-399

[74] Li Y, et al. (2025) Overview of RING gene family in maize. *BMC Plant Biology*. DOI: 10.1186/s12870-025-06683-8

[75] Brugiere N, et al. (2017) Overexpression of RING domain E3 ligase ZmXerico1 confers drought tolerance through regulation of ABA homeostasis. *Plant Physiology*, 175(3): 1350-1369. DOI: 10.1104/pp.17.01072

[76] Zhao J, et al. (2013) Arabidopsis thaliana AHL family modulates hypocotyl growth redundantly by interacting with each other via the PPC/DUF296 domain. *PNAS*, 110(48): E4688-E4697. DOI: 10.1073/pnas.1219277110

[77] Street IH, et al. (2008) The AT-hook-containing proteins SOB3/AHL29 and ESC/AHL27 are negative modulators of hypocotyl growth in Arabidopsis. *Plant Journal*, 54(1): 1-14. DOI: 10.1111/j.1365-313X.2007.03393.x

[78] Favero DS, et al. (2024) Chromatin attachment to the nuclear matrix represses hypocotyl elongation in Arabidopsis thaliana. *Nature Communications*, 15: 1547. DOI: 10.1038/s41467-024-45577-5

[79] Lu CA, et al. (2002) Three novel MYB proteins with one DNA binding repeat mediate sugar and hormone regulation of alpha-amylase gene expression. *Plant Cell*, 14(8): 1877-1893. DOI: 10.1105/tpc.001735

[80] Zhang Y, et al. (2020) Overexpression of maize ZmMYB59 gene plays a negative regulatory role in seed germination. *Frontiers in Plant Science*, 11: 564665. DOI: 10.3389/fpls.2020.564665

[81] Balmer D, De Papajewski DV, Planchamp C, Glauser G, Mauch-Mani B. (2013) Induced resistance in maize is based on organ-specific defence responses. *Plant Journal*, 74(2): 213-225. DOI: 10.1111/tpj.12114

[82] Vandesompele J, De Preter K, Pattyn F, Poppe B, Van Roy N, De Paepe A, Speleman F. (2002) Accurate normalization of real-time quantitative RT-PCR data by geometric averaging of multiple internal control genes. *Genome Biology*, 3(7): research0034. DOI: 10.1186/gb-2002-3-7-research0034

[83] Andersen CL, Jensen JL, Orntoft TF. (2004) Normalization of real-time quantitative reverse transcription-PCR data: a model-based variance estimation approach. *Cancer Research*, 64(15): 5245-5250. DOI: 10.1158/0008-5472.CAN-04-0496

[84] Livak KJ, Schmittgen TD. (2001) Analysis of relative gene expression data using real-time quantitative PCR and the 2^-ΔΔCt^ method. *Methods*, 25(4): 402-408. DOI: 10.1006/meth.2001.1262

[85] Schmittgen TD, Livak KJ. (2008) Analyzing real-time PCR data by the comparative C~T~ method. *Nature Protocols*, 3(6): 1101-1108. DOI: 10.1038/nprot.2008.73

[86] German MA, Pillay M, Jeong DH, Hetawal A, Luo S, Janardhanan P, Kannan V, Rymarquis LA, Nobuta K, German R, De Paoli E, Lu C, Schroth G, Meyers BC, Green PJ. (2008) Global identification of microRNA-target RNA pairs by parallel analysis of RNA ends. *Nature Biotechnology*, 26(8): 941-946. DOI: 10.1038/nbt.1505

[87] Buchanan BB, Balmer Y. (2005) Redox regulation: a broadening horizon. *Annual Review of Plant Biology*, 56: 187-220. DOI: 10.1146/annurev.arplant.56.032604.144246
