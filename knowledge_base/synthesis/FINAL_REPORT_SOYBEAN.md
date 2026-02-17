# Bacterial Extracellular RNA-Mediated Reprogramming of Soybean (*Glycine max*) Seed Germination: Target Analysis, Mechanistic Models, and Validation Strategy

**Prepared:** 2026-02-17
**Classification:** Internal Research Report -- For Decision-Maker Review
**Evidence Labeling:** [KNOWN] = published peer-reviewed literature; [INFERRED] = logical deduction from conserved biology and target annotations; [SPECULATIVE] = hypothesis requiring experimental validation

---

## Executive Summary

This report consolidates the bioinformatic and literature-based analysis of 18 unique predicted soybean gene targets of bacterial extracellular small RNAs (exRNAs), delivered via an extracellular polymeric substance (EPS)-based seed treatment, which aims to improve soybean germination rate and seedling vigor. The analysis integrates target gene prioritization, mechanistic modeling, confounder identification, and a tiered experimental validation plan.

**Key findings:**

1. **18 unique gene targets** (resolved from 23 original entries after deduplication and KRH-to-GLYMA mapping) converge on four master regulatory levers: (a) rewiring hormone signaling (ABA/GA/cytokinin balance), (b) boosting sugar availability through invertase derepression, (c) optimizing the ROS-redox axis for pro-germination signaling, and (d) dismantling the metabolically costly defense apparatus [1, 2, 3].

2. **Two testable causal models** -- a Hormone-Sugar Metabolic Priming model and a Defense-Redox Reallocation model -- make divergent, experimentally distinguishable predictions about the primary molecular trigger [4, 5, 6].

3. **Six confounders** threaten the core hypothesis. EPS osmopriming and polysaccharide elicitor effects are the most parsimonious alternative explanations [7, 8]. One annotation conflict (KRH47986 labeled "cation transport regulator" but mapping to a CURT1 thylakoid protein) indicates potential mis-annotation across genome assembly versions.

4. **A single "killer experiment"** -- RNase treatment of the EPS solution -- can provide a decisive go/no-go result in 2 weeks for under $500.

5. **A minimum viable experiment set** of 5 experiments can deliver proof-of-concept in 10-12 weeks for ~$3,600 in consumables.

6. **Critical soybean-specific precedent:** Ren et al. (2019) demonstrated that *Bradyrhizobium japonicum* transfers tRNA-derived small RNA fragments to soybean, where they regulate nodulation via an AGO1-dependent mechanism [5]. This establishes bacteria-to-soybean sRNA transfer as an experimentally validated phenomenon.

**Honest assessment:** The exRNA-mediated gene silencing hypothesis is mechanistically novel and supported by the Ren et al. (2019) bacteria-to-soybean sRNA precedent. However, simpler explanations (osmopriming, polysaccharide elicitation) require no novel biology and must be ruled out first. The hypothesis is efficiently testable, and the RNase experiment is the critical first step.

---

## 1. Background and Rationale

### 1.1 Cross-Kingdom RNA Interference

Cross-kingdom RNA interference (RNAi) -- the transfer of small RNAs between organisms of different kingdoms to silence target genes -- is now an established biological phenomenon. The landmark discovery by Weiberg et al. (2013) demonstrated that the fungal pathogen *Botrytis cinerea* transfers small RNAs into *Arabidopsis thaliana* and tomato cells, where they hijack the host AGO1-dependent RNAi machinery to suppress plant immunity genes [9]. Subsequent work showed that plants reciprocally send small RNAs to fungal pathogens via extracellular vesicles (EVs) to silence virulence genes [10], and that fungal small RNAs enter plant cells through clathrin-mediated endocytosis [11]. Comprehensive reviews have established the broader significance of EV-mediated cross-kingdom RNA trafficking [12].

**Soybean-specific cross-kingdom RNAi precedents:** Two findings are directly relevant to the soybean system:

1. **Bacteria-to-soybean sRNA transfer:** Ren et al. (2019) demonstrated in *Science* that *Bradyrhizobium japonicum* produces tRNA-derived small RNA fragments (tRFs) that are transferred to soybean host cells during the symbiotic interaction, where they silence target genes to regulate nodulation through an AGO1-dependent mechanism [5]. This is the most directly relevant precedent, establishing that bacterial small RNAs can enter soybean cells and direct gene silencing via the canonical RNAi pathway.

2. **Nematode-to-soybean sRNA transfer:** Ste-Croix et al. (2023) characterized microRNAs in the soybean cyst nematode (*Heterodera glycines*) and identified candidate effector sRNAs involved in cross-kingdom interactions with soybean [13].

3. **Systemic RNAi in soybean:** Subramanian et al. (2005) demonstrated that RNAi of soybean isoflavone synthase genes led to silencing in tissues distal to the transformation site, confirming that soybean possesses functional systemic RNAi machinery [14].

### 1.2 Soybean RNAi Machinery

The soybean genome (*Glycine max* Wm82 reference genome; Schmutz et al. 2010) [15] encodes a comprehensive RNA silencing toolkit. Liu et al. (2014) conducted a systematic identification of RNA silencing components in soybean, identifying multiple copies of DCL (Dicer-like), AGO (Argonaute), RDR (RNA-dependent RNA polymerase), and HEN1 genes [16]. The paleopolyploid nature of the soybean genome means many silencing components exist as duplicated paralogs, providing both redundancy and potential subfunctionalization.

Host-induced gene silencing (HIGS) has been successfully demonstrated in soybean against the soybean cyst nematode (*Heterodera glycines*), with stable transgenic soybean lines expressing dsRNA against nematode fitness genes (HgY25, HgPrp17) showing effective silencing [17, 18, 19]. These studies confirm that the soybean RNAi pathway can process exogenous double-stranded RNA precursors into functional siRNAs.

HEN1-mediated 2'-O-methylation protects small RNAs from 3'-end uridylation and degradation in plants [20], a mechanism relevant to understanding the stability of exogenous sRNAs within the soybean cellular environment.

### 1.3 Bacterial EPS as a Delivery Matrix

Bacteria within biofilms produce extracellular polymeric substances (EPS) composed of polysaccharides, proteins, lipids, and nucleic acids [21, 22]. The EPS matrix serves as a protective microenvironment that can shield extracellular nucleic acids from degradation [22]. Microbial EPS also plays ecological roles in soil aggregation and plant-microbe interactions [23]. [INFERRED] In the seed treatment system, the bacterial EPS likely serves as both a protective reservoir and a slow-release delivery system for exRNAs during seed imbibition, concentrating them at the seed surface and shielding them from environmental RNases.

### 1.4 Soybean Seed Germination Biology

#### 1.4.1 ABA/GA Balance

The balance between abscisic acid (ABA) and gibberellins (GA) is the central hormonal axis controlling soybean seed germination [24, 25]. When the ABA/GA ratio is high, seeds remain dormant; a lower ratio promotes germination. Quantitative measurements in soybean show that dry seeds contain approximately 32 ng g^-1 ABA and undetectably low GA levels. After 6 hours of imbibition, active GA~1~ and GA~4~ increase to 0.6 and 0.4 ng g^-1 respectively, while ABA concentration drops to approximately 14 ng g^-1 [24]. Shuai et al. (2017) further demonstrated that exogenous auxin represses soybean seed germination by enhancing ABA biosynthesis while impairing GA biogenesis [24].

Transcriptome analysis of soybean embryonic axes during germination confirmed extensive hormonal crosstalk, with genes involved in brassinosteroid, auxin, jasmonic acid, ABA, and cytokinin signaling being differentially expressed [26, 27].

#### 1.4.2 Ethylene-ROS Axis

Reactive oxygen species (ROS) produced in the soybean embryonic axis after imbibition induce endogenous ethylene production, which in turn promotes cell elongation in the root tip [28]. This ethylene-ROS crosstalk establishes a direct mechanistic link between redox signaling and germination progression. Early work by Gidrol et al. (1994) demonstrated that in soybean seeds, Cu,Zn-SOD and Mn-SOD activities were significantly increased in low-viability seeds, with catalase induction failing, resulting in damaging H~2~O~2~ accumulation [29]. Zeatin riboside (an endogenous cytokinin) was found to act as a superoxide scavenger, suggesting an unexpected antioxidant role for cytokinins in soybean seed viability [29].

The "oxidative window" concept posits that a critical ROS concentration range promotes germination signaling without causing oxidative damage [30, 31]. SOD is the most dynamically regulated antioxidant enzyme during soybean imbibition, with activities of catalase, peroxidase, and ascorbate-glutathione cycle enzymes undergoing rapid changes [32, 33].

#### 1.4.3 Seed Reserve Mobilization

Soybean seeds contain two dominant storage protein families: 7S (beta-conglycinin, vicilin type) and 11S (glycinin, legumin type) globulins, comprising ~70-80% of total seed protein [34]. Proteolytic mobilization occurs in protein storage vacuoles (PSVs), initiated by subtilisin-like protease C1 under acidic conditions following PSV acidification mediated by vacuolar H^+^-ATPase [35, 36]. Beta-conglycinin degrades faster than glycinin, with alpha and alpha-prime subunits disappearing by 96 hours [34]. Soybean mutants lacking abundant storage proteins (BSH-2 line) show significantly reduced germination rates, directly linking protein composition to germination performance [37].

Triacylglycerol (TAG) mobilization is initiated by SDP1-family lipases (GmSDP1-1 through GmSDP1-4), with expression increasing 2-4 fold after 1 day of imbibition [38]. Liberated fatty acids are converted to sugars through beta-oxidation and the glyoxylate cycle.

#### 1.4.4 Sugar Sensing and Imbibition

Sugar metabolism during soybean germination involves a unique sorbitol pathway in embryonic axes. Sucrose decreases while glucose, fructose, and sorbitol accumulate from day 1 of germination, with invertase activity driving hexose accumulation [39]. The soybean genome contains 32 putative invertase genes across three classes: cell wall invertases (CWI), vacuolar invertases (VI), and cytoplasmic/neutral invertases [40]. Sugar signaling operates through hexokinase (HXK)-dependent and HXK-independent pathways, with 17 GmHXK genes identified in soybean [41].

The trehalose-6-phosphate (T6P)/SnRK1 pathway provides global metabolic regulation: T6P inhibits SnRK1 activity, permitting growth-promoting processes when sugar levels are adequate. Twenty TPS genes are present in the soybean genome, with GmTPS12a positively regulating seed germination under stress by repressing the ABA response [42, 43].

Soybean seed imbibition follows the classic three-phase water uptake model. Water entry commences within 10 minutes, with seeds absorbing 25-30% of dry weight within the first few hours [44]. Radicle elongation occurs after approximately 24 hours at 25°C. Cell wall loosening during germination involves 2,143 identified cell wall genes, including expansins, cellulose synthases, and xyloglucan endotransglycosylases [45].

#### 1.4.5 Ion Homeostasis and Calcium Signaling

Potassium (K^+^), the most abundant inorganic cation in plants (up to 10% of dry weight), plays essential roles in turgor regulation, cell elongation, and enzyme activation during germination [46]. In rice, OsHAK9 was shown to regulate seed germination under salt stress by preventing GA degradation through mediating OsGA2ox7, directly linking K^+^ transport to hormonal control of germination [47].

The soybean genome encodes 50 GmCDPK (calcium-dependent protein kinase) genes -- the highest number among characterized species -- grouped into 4 phylogenetic clusters [48]. CDPKs decode calcium signatures in ABA signaling; in *Arabidopsis*, CPK4 and CPK11 loss-of-function produces ABA-insensitive germination phenotypes. Additionally, 41 GmCML (calmodulin-like) genes have been identified, with GmCML5 and GmCML6 functioning in nodulation [49].

#### 1.4.6 Defense-Growth Tradeoff

Soybean pathogens and pests cause annual yield losses averaging 21.4% [50]. The genome contains 319 putative NBS-LRR disease resistance genes across three structural classes: TIR-NBS-LRR (TNL), CC-NBS-LRR (CNL), and ULP1-NBS-LRR [51]. Isoflavonoid biosynthesis -- a legume-specific metabolic investment -- produces phytoalexins (glyceollins) from daidzein, representing a significant carbon and nitrogen cost [52]. [INFERRED] During germination, constitutive expression of defense genes diverts resources from growth processes; selective downregulation of specific defense genes could liberate metabolic resources for faster radicle emergence.

### 1.5 Seed Priming Context

Seed priming is a well-established agricultural technology. In soybean specifically, biopriming with *Bradyrhizobium japonicum* and *Bacillus megaterium* improves germination and initial seedling growth [7], while PEG-6000 osmopriming improves aged soybean seed vigor through carbon metabolism, ROS scavenging, and hormone signaling [8]. [INFERRED] The EPS-based seed treatment may combine conventional priming effects with a novel exRNA-mediated gene regulation component. Disentangling these effects is a central challenge for validation experiments.

---

## 2. Target Prioritization

### 2.1 Methodology

23 predicted soybean gene targets were extracted from bioinformatic analysis of bacterial sRNA-soybean mRNA complementarity. After deduplication (5 duplicates removed) and resolution of KRH protein accessions to GLYMA gene loci via NCBI Protein and SoyBase databases, 18 unique gene targets were identified. Each was evaluated for: (a) annotation quality, (b) functional relevance to germination based on *Arabidopsis thaliana* homolog data, (c) pathway membership, and (d) mechanistic plausibility of downregulation promoting germination. Targets were assigned to functional categories and scored on a 1-10 priority scale.

**Annotation sources:** NCBI Protein, SoyBase (Wm82.a2.v1 / Glyma 4.0), Ensembl Plants, TAIR (*Arabidopsis* homologs).

### 2.2 KRH Accession Resolution

Nine KRH protein accessions from the original target list were resolved to GLYMA gene loci:

| KRH Accession | GLYMA Locus | Status | Annotation |
|---------------|-------------|--------|------------|
| KRH47986 | GLYMA_07G060700 | NCBI record REMOVED | CURT1-like thylakoid protein (annotation conflict -- see Section 2.5) |
| KRH55503 | GLYMA_06G259700 | Active | TIR-NBS-LRR disease resistance protein |
| KRH37200 | GLYMA_09G051100 | Active (duplicate) | Cellulose synthase A4 |
| KRH57561 | GLYMA_05G068700 | Active | Invertase/PME inhibitor superfamily |
| KRH33075 | GLYMA_10G097500 | NCBI record REMOVED | Hypothetical protein (uncharacterized) |
| KRH35424 | GLYMA_10G242300 | Active | ERECTA-like LRR receptor-like kinase |
| KRH35861 | GLYMA_10G268800 | Active | Hypothetical protein (61 aa, very short) |
| KRH5227* | GLYMA_06G057500 | Truncated accession | DUF1677 protein |
| KRH25272 | GLYMA_12G091900 | NCBI record REMOVED | Hypothetical membrane protein |

*KRH5227 appears truncated; likely KRH52271 or KRH52270, both mapping to the same gene.

### 2.3 Gene ID Correction

**GLYMA_09G19270** was identified as having an incorrect number of digits. SoyBase validation confirmed the correct ID as **GLYMA_09G192700** (ROP GTPase, chromosome 9, positions 41,734,808-41,738,603), encoding a RHO-related protein from plants with 153 orthologues confirmed in Ensembl Plants.

### 2.4 Ranked Target Table (18 Unique Targets)

| Rank | Gene ID | Annotation | Theme | At Homolog | Score | Key Domains |
|------|---------|------------|-------|------------|-------|-------------|
| 1 | GLYMA_05G068700 | Invertase/PME inhibitor | Sugar sensing | AT5G46940 | 10 | Inv/PME inhibitor (PF04043) |
| 2 | GLYMA_01G215100 | Phospholipase D beta 1 | ABA/GA signaling | AT2G42010 | 10 | C2; PLD active site; PLD C-term |
| 3 | GLYMA_09G063900 | Cytokinin oxidase 3 (CKX3) | Hormone metabolism | AT5G56970 | 9 | FAD binding; CKX dehydrogenase |
| 4 | GLYMA_03G196400 | Glutaredoxin family protein | ROS/redox | AT5G03870 | 9 | Glutaredoxin (PF00462) |
| 5 | GLYMA_09G192700 | ROP GTPase (ROP9) | ABA signaling | AT4G28950 | 9 | Ras GTPase domain |
| 6 | GLYMA_06G259700 | TIR-NBS-LRR disease resistance | Defense | AT5G45250 | 8 | TIR; NBS; LRR |
| 7 | GLYMA_09G051100 | Cellulose synthase A4 (CesA4) | Cell wall | AT5G44030 | 7 | Cellulose synthase (PF03552) |
| 8 | GLYMA_10G242300 | ERECTA-like LRR-RLK | Defense/development | AT5G07180 | 7 | Protein kinase; LRR |
| 9 | GLYMA_01G009900 | LrgB-like membrane protein | Defense/cell death | AT1G32080 | 6 | LrgB domain (PF04172) |
| 10 | GLYMA_09G261100 | Exosome subunit Rrp46-like | RNA processing | AT3G46210 | 5 | 3' exoribonuclease; RNase PH |
| 11 | GLYMA_02G220600 | UFM1-specific peptidase | Protein QC | AT5G24680 | 5 | Peptidase C78 (PF07910) |
| 12 | GLYMA_08G231200 | Urb2/Npa2 ribosome biogenesis | Ribosome biogenesis | AT4G30150 | 4 | Urb2/Npa2 domain |
| 13 | GLYMA_01G091700 | hAT transposon protein | TE-related | AT4G15020 | 4 | DUF659 (PF04937) |
| 14 | GLYMA_07G060700 | CURT1-like thylakoid protein | Photosynthesis | AT4G01150 | 3 | Transmembrane domains |
| 15 | GLYMA_06G057500 | DUF1677 protein | Unknown | AT1G72510 | 3 | DUF1677 |
| 16 | GLYMA_12G091900 | Hypothetical membrane protein | Unknown | AT5G22340 | 2 | Transmembrane domains |
| 17 | GLYMA_10G097500 | Hypothetical protein | Unknown | AT3G57440 | 2 | Unknown |
| 18 | GLYMA_10G268800 | Hypothetical protein (61 aa) | Unknown | Unassigned | 1 | Unknown |

### 2.5 Key Rationale for Top Targets

**Rank 1 -- Invertase/PME inhibitor (GLYMA_05G068700 / KRH57561):** [KNOWN] In soybean, Tang et al. (2017) demonstrated that RNAi suppression of the invertase inhibitor GmCIF1 produced marked elevation of cell wall invertase (CWI) activity, increased seed weight, and higher accumulations of hexoses, starch, and protein [53]. In *Arabidopsis*, loss-of-function of the orthologous AtCIF1 accelerated seed germination independently of exogenous ABA, with a drastic increase in CWI activity and boosted hexose levels by 24 hours after imbibition onset [54]. In tomato, silencing INVINH1 increased seed weight and fruit hexose levels [55]. [INFERRED] Downregulating the soybean invertase inhibitor would derepress CWI activity, flood germinating embryonic axes with hexose sugars, and accelerate metabolic activation. This represents the most directly actionable target with the strongest cross-species validation.

**Rank 2 -- Phospholipase D beta 1 (GLYMA_01G215100):** [KNOWN] PLDbeta1 generates phosphatidic acid (PA), a key lipid second messenger in ABA signaling and stress responses. In *Arabidopsis*, PA produced by PLDbeta1 promotes ABA-mediated stomatal closure and enhances drought tolerance. [INFERRED] Downregulating PLDbeta1 would reduce PA-mediated ABA signal amplification, effectively lowering the ABA/GA ratio and favoring germination. PA also activates NADPH oxidase, so reduced PA could modulate the ROS burst during imbibition.

**Rank 3 -- Cytokinin oxidase 3 (GLYMA_09G063900):** [KNOWN] Cytokinin oxidases (CKX) irreversibly degrade cytokinins via oxidative side-chain cleavage. Cytokinins promote cell division and interact with the ABA/GA balance during germination. [INFERRED] Downregulating CKX3 would elevate endogenous cytokinin levels, promoting cell division in the embryonic axis and radicle meristem. Elevated cytokinins may also enhance zeatin riboside levels, which Gidrol et al. (1994) showed acts as a superoxide scavenger in soybean seeds [29], potentially optimizing the oxidative window.

**Rank 4 -- Glutaredoxin (GLYMA_03G196400):** [KNOWN] The soybean genome encodes 12 Grx genes involved in thiol-disulfide redox homeostasis [56]. Glutaredoxins regulate the "redox kick-start" of mitochondrial metabolism during seed germination; seeds lacking thiol redox machinery use resources less efficiently [57]. In rice, CRISPR knockout of OsGRX3/PHS9 produced delayed germination phenotypes, suggesting the wild-type protein facilitates rather than inhibits germination [57]. [INFERRED] Context-dependent: if GLYMA_03G196400 functions as a dormancy-associated Grx (analogous to those maintaining disulfide bridges on storage proteins during desiccation), its downregulation during imbibition could accelerate the reductive activation of metabolic enzymes. However, if it functions as a pro-germination Grx (like OsGRX3), downregulation could be counterproductive.

**Rank 5 -- ROP GTPase (GLYMA_09G192700):** [KNOWN] ROP (RHO of Plants) GTPases act as molecular switches in ABA signal transduction. In *Arabidopsis*, ROP10 negatively regulates ABA signaling; *rop10* mutants are hypersensitive to ABA in germination assays. ROP GTPases also regulate ROS production through NADPH oxidase activation and polar auxin transport. [INFERRED] Depending on which specific ROP signaling module GLYMA_09G192700 participates in, downregulation could either sensitize or desensitize ABA signaling. If this ROP functions analogously to AtROP10 (negative regulator of ABA), downregulation would enhance ABA sensitivity and potentially inhibit germination -- making this a complex target requiring experimental validation.

**Rank 6 -- TIR-NBS-LRR (GLYMA_06G259700 / KRH55503):** [KNOWN] Soybean contains 319 NBS-LRR disease resistance genes [51]. Constitutive activation of NBS-LRR genes imposes significant fitness costs through autoimmune-like metabolic drain [50]. [INFERRED] Downregulating a single TIR-NBS-LRR gene during germination reduces the constitutive defense metabolic burden, redirecting carbon and nitrogen from isoflavonoid biosynthesis and defense protein synthesis toward reserve mobilization and axis elongation.

**Rank 7 -- Cellulose synthase A4 (GLYMA_09G051100 / KRH37200):** [KNOWN] CesA4 is a secondary cell wall cellulose synthase. [INFERRED] Transient downregulation during imbibition could reduce cell wall rigidity, facilitating radicle protrusion through the seed coat -- consistent with the established role of cell wall loosening in germination [45]. However, sustained downregulation could compromise seedling structural integrity.

**Rank 8 -- ERECTA-like LRR-RLK (GLYMA_10G242300 / KRH35424):** [KNOWN] ERECTA-family receptor-like kinases regulate both developmental processes (organ shape, stomatal patterning) and pathogen defense. The *Arabidopsis* ERECTA pathway integrates growth and immunity signals. [INFERRED] Downregulating the soybean ERECTA-like RLK could shift the growth-defense balance toward growth during the germination window, while potentially affecting organ morphology in later development.

### 2.6 Annotation Conflicts and Flags

1. **KRH47986 annotation conflict:** The original target list described this as "cation transport regulator-like protein 2-like," but SoyBase annotation for GLYMA_07G060700 indicates a CURT1-like thylakoid membrane protein (AT4G01150 homolog). CURT1 proteins are NOT cation transporters. The discrepancy may reflect different annotation pipeline versions or the fact that the KRH47986 NCBI record was removed, meaning the original annotation may have differed from current SoyBase entries.

2. **Three removed NCBI records:** KRH47986, KRH33075, and KRH25272 have been removed from NCBI, indicating these gene models may have been revised in newer genome assemblies.

3. **Six uncharacterized targets:** GLYMA_10G097500, GLYMA_10G268800, GLYMA_06G057500, GLYMA_12G091900, GLYMA_08G231200, and GLYMA_01G091700 remain poorly characterized with no experimentally validated function. These would benefit from domain prediction via InterProScan or AlphaFold structure analysis.

### 2.7 Pathway Category Summary

**ABA/GA and Hormone Signaling (4 targets):**
- GLYMA_01G215100: Phospholipase D beta 1 (PA-mediated ABA signaling)
- GLYMA_09G192700: ROP GTPase (ABA signal transduction switch)
- GLYMA_09G063900: Cytokinin oxidase 3 (cytokinin degradation)
- GLYMA_10G242300: ERECTA-like LRR-RLK (developmental/defense signaling)

**Sugar Sensing and Cell Wall (2 targets):**
- GLYMA_05G068700: Invertase/PME inhibitor (CWI regulation, sugar partitioning)
- GLYMA_09G051100: Cellulose synthase A4 (cell wall biogenesis)

**ROS/Redox (1 target):**
- GLYMA_03G196400: Glutaredoxin (thiol-disulfide redox homeostasis)

**Defense (3 targets):**
- GLYMA_06G259700: TIR-NBS-LRR disease resistance
- GLYMA_01G009900: LrgB-like anti-cell-death membrane protein
- GLYMA_10G242300: ERECTA-like RLK (partially defense-associated)

**Unknown/Uncharacterized (8 targets):**
- GLYMA_09G261100, GLYMA_01G091700, GLYMA_02G220600, GLYMA_08G231200, GLYMA_10G097500, GLYMA_10G268800, GLYMA_06G057500, GLYMA_12G091900, GLYMA_07G060700

---

## 3. Mechanistic Narrative

### 3.1 Theme 1: Hormone-Sugar Metabolic Priming

**Central thesis:** The bacterial exRNAs simultaneously shift the ABA/GA ratio toward germination AND flood the embryonic axis with hexose sugars, creating a metabolically primed state that accelerates germination.

[KNOWN] The invertase inhibitor-CWI axis is a validated germination control point. In soybean, GmCIF1 silencing elevates CWI activity and increases hexose accumulation [53]. In *Arabidopsis*, AtCIF1 knockout accelerates germination with dramatically increased CWI activity by 24 hours post-imbibition [54]. Sugar metabolism in germinating soybean axes involves a unique sorbitol pathway where hexose accumulation correlates with invertase activity [39].

[KNOWN] PLDbeta1-generated phosphatidic acid (PA) amplifies ABA signaling. Cytokinin oxidase CKX3 degrades cytokinins that promote cell division. ROP GTPases modulate ABA signal transduction. Each represents a distinct node in the hormone signaling network.

[INFERRED] The coordinated downregulation of the invertase inhibitor (derepress CWI → more hexoses), PLDbeta1 (reduce PA → weaken ABA signaling), and CKX3 (elevate cytokinins → promote cell division) creates a convergent metabolic-hormonal signal: "sugar is abundant, ABA is low, divide and grow." This three-pronged attack on germination-limiting pathways may explain why the seed treatment produces effects beyond what any single target downregulation would achieve.

**Predicted molecular signature:**
- Elevated CWI activity in treated vs. control seeds at 12-24 hours post-imbibition
- Increased hexose (glucose + fructose) in embryonic axes
- Reduced PA levels
- Elevated cytokinin (zeatin, zeatin riboside) levels
- Decreased ABA/GA ratio relative to controls

### 3.2 Theme 2: Defense-Redox Reallocation

**Central thesis:** The bacterial exRNAs selectively suppress constitutive defense gene expression, liberating metabolic resources (carbon, nitrogen, energy) that are reallocated to germination processes, while simultaneously fine-tuning the ROS landscape to optimize the "oxidative window."

[KNOWN] Soybean contains 319 NBS-LRR genes [51], and constitutive immune activation is metabolically costly with documented growth-defense tradeoffs [50]. Isoflavonoid biosynthesis is a major nitrogen and carbon sink in legumes. The metabolic cost of defense in soybean seeds is evidenced by metabolic rerouting during *Fusarium fujikuroi* infection, where glycine-serine-threonine metabolism and tryptophan metabolism are induced alongside isoflavone biosynthesis [52].

[KNOWN] The soybean glutaredoxin family (12 GmGrx genes) participates in thiol-disulfide redox homeostasis with evidence of translational regulation under stress [56]. The ROS "oxidative window" during germination requires precise balance between O~2~^-^ and H~2~O~2~ levels [30, 31]. Soybean embryonic axes produce both superoxide and H~2~O~2~ with dynamic changes in SOD, catalase, and ascorbate-glutathione cycle enzymes [32, 33].

[INFERRED] Downregulating the TIR-NBS-LRR gene (GLYMA_06G259700) and the ERECTA-like RLK (GLYMA_10G242300) reduces constitutive defense protein synthesis and isoflavonoid pathway flux. The freed carbon and nitrogen are redirected to storage protein mobilization and cell wall expansion. Simultaneously, modulation of the glutaredoxin (GLYMA_03G196400) fine-tunes the redox state, potentially widening the oxidative window to allow stronger pro-germination ROS signaling without crossing into oxidative damage territory.

**Predicted molecular signature:**
- Reduced TIR-NBS-LRR transcript levels in treated seeds
- Decreased isoflavonoid (daidzein, genistein) accumulation in embryonic axes during first 48 hours
- Altered SOD/catalase activity ratios
- Modified glutathione/glutaredoxin redox state
- Faster reserve protein mobilization (earlier beta-conglycinin degradation)

### 3.3 Two Causal Models

#### Model A: Hormone-Sugar Metabolic Priming (Primary Driver)

```
Bacterial exRNAs
    │
    ├──→ Silence invertase inhibitor → ↑ CWI activity → ↑ hexose → ↑ metabolic fuel
    │
    ├──→ Silence PLDbeta1 → ↓ PA → ↓ ABA signaling → ↑ GA/ABA ratio
    │
    ├──→ Silence CKX3 → ↑ cytokinins → ↑ cell division + ↑ zeatin antioxidant
    │
    └──→ Silence ROP GTPase → altered ABA signal transduction

    Combined effect: Metabolic priming + hormonal permissiveness → ACCELERATED GERMINATION
```

**Testable prediction A:** If Model A is correct, then:
- Exogenous glucose (10 mM) application to untreated seeds should partially phenocopy the germination acceleration
- ABA/GA measurements will show altered ratios in treated seeds by 12 hours
- Invertase activity assays will show elevated CWI in treated vs. control by 24 hours

#### Model B: Defense-Redox Reallocation (Primary Driver)

```
Bacterial exRNAs
    │
    ├──→ Silence TIR-NBS-LRR → ↓ defense protein synthesis → ↑ free amino acids
    │
    ├──→ Silence ERECTA-like RLK → ↓ immune surveillance → ↓ metabolic cost
    │
    ├──→ Modulate glutaredoxin → altered thiol-disulfide balance → optimized ROS window
    │
    └──→ Silence LrgB → altered programmed cell death regulation

    Combined effect: Resource reallocation + optimized ROS → ACCELERATED GERMINATION
```

**Testable prediction B:** If Model B is correct, then:
- Treated seeds will show reduced isoflavonoid levels compared to controls
- Adding exogenous salicylic acid (which activates defense) should abolish the germination benefit
- ROS profiling (DHE/H~2~DCFDA staining) will show altered O~2~^-^/H~2~O~2~ ratios in treated seeds
- Amino acid profiling will show increased free amino acids from reduced defense protein synthesis

**Distinguishing experiment:** Apply exogenous glucose to untreated seeds AND measure isoflavonoid levels in treated seeds. If glucose phenocopies the effect but isoflavonoid levels are unchanged, Model A is primary. If isoflavonoid levels are reduced but glucose alone doesn't phenocopy, Model B is primary. If both effects are observed, a combined model operates.

---

## 4. Confounders and Alternative Explanations

### 4.1 Six Confounders

**Confounder 1: EPS Osmopriming (HIGHEST CONCERN)**
[KNOWN] PEG-6000 osmopriming improves aged soybean seed vigor through carbon metabolism, ROS scavenging, and hormone signaling [8]. The bacterial EPS is a hydrated polymer matrix that could produce identical osmopriming effects simply through water activity modulation.
**Impact:** Could explain 100% of germination improvement without any RNA involvement.
**Control:** Compare EPS (intact) vs. EPS (RNase-treated) vs. synthetic hydrogel (equivalent water activity) vs. water-only.

**Confounder 2: Polysaccharide Elicitor Effects**
[KNOWN] Bacterial EPS polysaccharides can trigger plant innate immune responses and prime defense systems [23]. Paradoxically, mild defense priming can enhance overall seedling vigor through "priming memory" that improves stress tolerance.
**Impact:** EPS polysaccharide fractions may trigger beneficial priming independent of RNA content.
**Control:** Heat-denatured EPS (destroys RNA secondary structure but preserves polysaccharides) vs. intact EPS.

**Confounder 3: Biopriming by Residual Bacteria**
[KNOWN] Biopriming with *Bradyrhizobium japonicum* and *Bacillus megaterium* improves soybean germination [7]. If the EPS preparation contains viable bacteria, any germination enhancement could result from conventional biopriming rather than exRNA transfer.
**Impact:** Living bacteria on seed surface produce growth hormones, siderophores, and volatiles.
**Control:** Filter-sterilize (0.22 μm) vs. UV-sterilize vs. untreated EPS.

**Confounder 4: Nutrient Effects**
[INFERRED] The EPS matrix contains proteins, amino acids, and minerals. These nutrients may simply provide metabolic fuel for faster germination, particularly for aged or stressed seeds.
**Control:** Dialyzed EPS (retain macromolecules, remove small molecules) vs. dialysate-only vs. complete EPS.

**Confounder 5: pH and Ionic Strength Effects**
[INFERRED] The EPS solution may alter the local pH and ionic environment of the seed coat during imbibition, affecting enzyme activities and ion channel kinetics independent of RNA content.
**Control:** Buffer-matched controls at equivalent pH and ionic strength.

**Confounder 6: Bioinformatic False Positives in Target Prediction**
[KNOWN] Computational prediction of sRNA-mRNA complementarity generates high rates of false positives, especially with short sequences in a 1.1 Gb genome [15]. Many predicted targets may not be genuine biological targets.
**Impact:** Some or many of the 18 targets may not actually be regulated by the bacterial sRNAs.
**Control:** Validate target downregulation by RT-qPCR (minimum 5 high-priority targets) using validated reference genes with geNorm [58] or NormFinder [59] selection, and 2^-ΔΔCt^ quantification [60, 61].

### 4.2 The Killer Experiment

**RNase Treatment of the EPS Solution**

**Rationale:** If the germination-promoting activity of the EPS preparation is RNA-dependent, then degrading the RNA component should abolish or significantly reduce the effect.

**Protocol:**
1. Prepare EPS seed treatment as standard
2. Split into three aliquots:
   - Aliquot A: Untreated EPS (positive control)
   - Aliquot B: EPS + RNase A (100 μg/mL, 37°C, 1 hour)
   - Aliquot C: EPS + heat-inactivated RNase A (negative control for RNase buffer effects)
3. Treat soybean seeds (var. Williams 82, n=50 per treatment, 4 replicates)
4. Score germination (radicle emergence ≥2 mm) at 24, 48, 72, 96 hours
5. Score at VE stage (emergence) per Fehr & Caviness staging system [62]

**Interpretation:**
- If B ≈ C << A: RNA is essential → proceed with full validation
- If B ≈ C ≈ A: RNA is not essential → investigate EPS components instead
- If B < A but B > C: Partial RNA contribution → RNA is one of multiple active components

**Cost:** ~$200-500 (RNase A, seeds, basic germination supplies)
**Timeline:** 2 weeks
**Decision value:** CRITICAL -- determines whether entire exRNA hypothesis merits further investment

---

## 5. Validation Plan

### 5.1 Tier 1: Essential Experiments (Weeks 1-4, ~$1,500)

**Experiment 1: RNase Elimination (The Killer Experiment)**
- As described in Section 4.2
- Deliverable: Go/no-go decision on RNA involvement

**Experiment 2: Target Transcript Quantification**
- RT-qPCR on 8 high-priority targets (Ranks 1-8 from Table 2.4)
- Timepoints: 0, 12, 24, 48 hours post-imbibition
- Treatments: EPS-treated vs. water-control
- Reference genes: Select 3 stable references from candidates (GmACT11, GmTUB4, GmEF1a, GmUBC2) using geNorm [58] and NormFinder [59] algorithms
- Quantification: 2^-ΔΔCt^ method [60, 61]
- Deliverable: Validated target downregulation (or lack thereof)
- Minimum interpretable result: ≥2-fold reduction in ≥3 of 8 targets in treated vs. control seeds

**Experiment 3: Invertase Activity Assay**
- Measure CWI, VI, and total invertase activity in embryonic axes
- Timepoints: 0, 12, 24, 48 hours post-imbibition
- Treatments: EPS-treated vs. water-control
- Method: Enzymatic assay (DNS reducing sugar method)
- Deliverable: Functional validation of invertase derepression hypothesis

### 5.2 Tier 2: Mechanistic Discrimination (Weeks 5-8, ~$1,200)

**Experiment 4: Hormone Quantification**
- LC-MS/MS quantification of ABA, GA~1~, GA~4~, zeatin, zeatin riboside, IAA
- Timepoints: 0, 6, 12, 24, 48 hours post-imbibition
- Treatments: EPS-treated vs. water-control vs. RNase-treated EPS
- Deliverable: Discriminates between Model A (altered ABA/GA ratio) and Model B (unchanged hormones)

**Experiment 5: ROS and Redox Profiling**
- O~2~^-^ detection: DHE (dihydroethidium) fluorescence in embryonic axis sections
- H~2~O~2~ detection: H~2~DCFDA fluorescence + Amplex Red quantitative assay
- Antioxidant enzyme panel: SOD, CAT, APX, GR activities
- Timepoints: 6, 12, 24, 48 hours
- Deliverable: Tests whether EPS treatment modifies the oxidative window

### 5.3 Tier 3: Conclusive Evidence (Weeks 9-12, ~$900)

**Experiment 6: Degradome Sequencing (PARE)**
- Parallel Analysis of RNA Ends to identify cleaved transcripts [63]
- Compare EPS-treated vs. water-control at 24 hours
- Deliverable: Direct evidence of sRNA-guided mRNA cleavage at predicted target sites
- Note: This is the gold-standard experiment for demonstrating RNAi-mediated target cleavage

**Experiment 7: Synthetic sRNA Mimics**
- Design synthetic 21-nt RNA duplexes matching top 3 predicted bacterial sRNAs
- Apply to soybean seeds during imbibition (with transfection reagent)
- Score germination phenotype
- Deliverable: Sufficiency test -- can synthetic sRNAs alone phenocopy the EPS effect?

### 5.4 Indicative Timeline

```
Week 1-2:   Exp 1 (RNase elimination) ──────► GO/NO-GO DECISION
Week 2-4:   Exp 2 (RT-qPCR) + Exp 3 (invertase assay)
Week 5-8:   Exp 4 (hormones) + Exp 5 (ROS profiling)
Week 9-12:  Exp 6 (degradome-seq) + Exp 7 (synthetic sRNAs)
            │
            ▼
     PUBLICATION-READY DATA
```

### 5.5 Soybean-Specific Experimental Considerations

1. **Cultivar selection:** Williams 82 (Wm82) is recommended as the reference genotype matching the genome assembly used for target prediction [15]. Alternative: Clark (for storage protein mutant comparisons [37]).

2. **Developmental staging:** Use the Fehr & Caviness (1977) system [62] for standardized reporting: VE (emergence), VC (unifoliolate), V1 (first trifoliolate).

3. **Germination conditions:** 25°C, dark, paper towel roll method or between-paper method per ISTA protocols. Score radicle emergence (≥2 mm) at 24-hour intervals.

4. **Imbibition kinetics:** Water entry commences within 10 minutes; two-phase imbibition (coat-dominated, then cotyledon-dominated) [44]. EPS treatment should be applied during Phase I (0-6 hours) for maximum uptake.

5. **Storage protein baseline:** Document 7S/11S ratio in seed lots, as this affects germination performance [37].

---

## 6. Conclusions

### 6.1 Summary of Findings

1. Of 18 unique soybean gene targets, **6 are high-priority** (score ≥8) with clear mechanistic relevance to germination: invertase inhibitor, PLDbeta1, CKX3, glutaredoxin, ROP GTPase, and TIR-NBS-LRR. The invertase inhibitor target has the strongest experimental support from soybean-specific loss-of-function studies [53, 54, 55].

2. Two competing causal models make testable, distinguishable predictions. Model A (Hormone-Sugar Metabolic Priming) is more parsimonious and better supported by existing soybean data. Model B (Defense-Redox Reallocation) invokes a more novel mechanism but is consistent with the defense-growth tradeoff literature [50, 52].

3. Six confounders must be addressed before accepting the exRNA hypothesis. EPS osmopriming is the most threatening alternative explanation. The RNase killer experiment addresses this directly.

4. The bacteria-to-soybean sRNA transfer precedent (Ren et al. 2019) [5] provides critical biological plausibility, distinguishing soybean from systems where such transfer has not been demonstrated.

5. A 12-week, ~$3,600 experimental program can deliver publication-quality evidence for or against the exRNA hypothesis.

### 6.2 Recommended Priorities

1. **Immediate (Week 1):** Execute the RNase killer experiment
2. **Contingent (Weeks 2-4):** If RNase result is positive, validate top 8 targets by RT-qPCR and measure invertase activity
3. **Extended (Weeks 5-12):** Hormone and ROS profiling followed by degradome sequencing

### 6.3 Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| EPS effect is entirely osmopriming | Medium-High | Fatal to hypothesis | RNase experiment (Tier 1) |
| Target predictions are false positives | Medium | Reduces actionable targets | RT-qPCR validation panel |
| sRNAs don't survive imbibition | Medium | Fatal to hypothesis | RNA extraction from imbibed seeds |
| Effect is real but too small to commercialize | Medium | Limits application | Dose-response and combinatorial optimization |
| ROP GTPase downregulation is counterproductive | Medium | Loses one target | Does not affect other targets |
| Glutaredoxin downregulation worsens redox | Low-Medium | Loses one target | Does not affect other targets |

---

## Appendix A: Soybean Genome and RNAi Context

### A.1 Soybean Genome Statistics

The soybean genome (*Glycine max* Wm82 reference) was published by Schmutz et al. (2010) [15]:
- Genome size: ~1.1 Gb
- Predicted protein-coding genes: 46,430 (SoyBase annotation) to 56,044 (Phytozome)
- Paleopolyploid: ~75% of genes are present in multiple copies due to two whole-genome duplication events
- NBS-LRR disease resistance genes: 319 [51]
- CDPK calcium signaling genes: 50 [48]
- Calmodulin-like genes: 41 [49]
- Invertase genes: 32 [40]
- Trehalose-6-phosphate synthase genes: 20

### A.2 Soybean RNAi Toolkit

Key RNA silencing components identified by Liu et al. (2014) [16]:
- DCL (Dicer-like): Multiple paralogs for processing dsRNA into 21-24 nt siRNAs
- AGO (Argonaute): Multiple paralogs for RISC assembly and target cleavage
- RDR (RNA-dependent RNA polymerase): Amplification of silencing signal
- HEN1: 2'-O-methylation protecting small RNA stability [20]

Functional HIGS in soybean has been demonstrated using stable transgenics [17, 18, 19], and systemic RNAi has been confirmed [14].

### A.3 Imbibition Biology Relevant to exRNA Uptake

During Phase I imbibition (0-6 hours), the soybean seed coat becomes highly permeable [44]. The two-phase imbibition model (coat-first, then cotyledon hydration) creates a temporal window during which exogenous molecules at the seed surface have maximal access to the embryo. In the legume model, cell wall loosening begins early, with expansins, XTH, and cellulose synthases being transcriptionally activated [45, 64]. This cell wall remodeling may facilitate the uptake of macromolecular complexes, including EPS-bound sRNAs.

---

## Bibliography

[1] Shu K, Liu XD, Xie Q, He ZH. (2016) Two faces of one seed: hormonal regulation of dormancy and germination. *Molecular Plant*, 9(1): 34-45. DOI: 10.1016/j.molp.2015.08.010

[2] Koch K. (2004) Sucrose metabolism: regulatory mechanisms and pivotal roles in sugar sensing and plant development. *Current Opinion in Plant Biology*, 7(3): 235-246. DOI: 10.1016/j.pbi.2004.03.014

[3] Rajjou L, Duval M, Gallardo K, Catusse J, Bally J, Job C, Job D. (2012) Seed germination and vigor. *Annual Review of Plant Biology*, 63: 507-533. DOI: 10.1146/annurev-arplant-042811-105550

[4] Bewley JD, Bradford KJ, Hilhorst HWM, Nonogaki H. (2013) Seeds: Physiology of Development, Germination and Dormancy. 3rd Edition. Springer. ISBN: 978-1-4614-4692-7. DOI: 10.1007/978-1-4614-4693-4

[5] Ren B, Wang X, Duan J, Ma J. (2019) Rhizobial tRNA-derived small RNAs are signal molecules regulating plant nodulation. *Science*, 365(6456): 919-922. DOI: 10.1126/science.aav8907

[6] Bologna NG, Voinnet O. (2014) The diversity, biogenesis, and activities of endogenous silencing small RNAs in Arabidopsis. *Annual Review of Plant Biology*, 65: 473-503. DOI: 10.1146/annurev-arplant-050213-035728

[7] Miljakovic D, Marinkovic J, Tamindzic G, Djordjevic V, Tintor B, Milosevic D, Ignjatov M, Nikolic Z. (2022) Bio-priming of soybean with *Bradyrhizobium japonicum* and *Bacillus megaterium*: strategy to improve seed germination and the initial seedling growth. *Plants*, 11(15): 1927. DOI: 10.3390/plants11151927

[8] Wang Y, Zhou E, Yao M, Xue D, Zhao N, Zhou Y, Li B, Wang K, Miao Y, Gu C, et al. (2023) PEG-6000 priming improves aged soybean seed vigor via carbon metabolism, ROS scavenging, hormone signaling, and lignin synthesis regulation. *Agronomy*, 13(12): 3021. DOI: 10.3390/agronomy13123021

[9] Weiberg A, Wang M, Lin FM, Zhao H, Zhang Z, Kaloshian I, Huang HD, Jin H. (2013) Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. *Science*, 342(6154): 118-123. DOI: 10.1126/science.1239705

[10] Cai Q, Qiao L, Wang M, He B, Lin FM, Palmquist J, Huang SD, Jin H. (2018) Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. *Science*, 360(6393): 1126-1129. DOI: 10.1126/science.aar4142

[11] He B, Wang H, Liu G, Chen A, Calvo A, Cai Q, Jin H. (2023) Fungal small RNAs ride in extracellular vesicles to enter plant cells through clathrin-mediated endocytosis. *Nature Communications*, 14: 4383. DOI: 10.1038/s41467-023-40093-4

[12] Cai Q, He B, Wang S, Fletcher S, Niu D, Mitter N, Birch PRJ, Jin H. (2021) Message in a Bubble: Shuttling small RNAs and proteins between cells and interacting organisms using extracellular vesicles. *Annual Review of Plant Biology*, 72: 497-524. DOI: 10.1146/annurev-arplant-081720-010616

[13] Ste-Croix DT, Belanger RR, Mimee B. (2023) Characterization of microRNAs in the cyst nematode *Heterodera glycines* identifies possible candidates involved in cross-kingdom interactions with its host *Glycine max*. *RNA Biology*, 20(1): 614-628. DOI: 10.1080/15476286.2023.2244790

[14] Subramanian S, Graham MY, Yu O, Graham TL. (2005) RNA interference of soybean isoflavone synthase genes leads to silencing in tissues distal to the transformation site and to enhanced susceptibility to *Phytophthora sojae*. *Plant Physiology*, 137(4): 1345-1353. DOI: 10.1104/pp.104.057257

[15] Schmutz J, Cannon SB, Schlueter J, Ma J, Mitros T, Nelson W, et al. (2010) Genome sequence of the palaeopolyploid soybean. *Nature*, 463(7278): 178-183. DOI: 10.1038/nature08670

[16] Liu X, Lu T, Dou Y, Yu B, Zhang C. (2014) Identification of RNA silencing components in soybean and sorghum. *BMC Bioinformatics*, 15: 4. DOI: 10.1186/1471-2105-15-4

[17] Li J, Todd TC, Oakley TR, Lee J, Trick HN. (2010) Host-derived suppression of nematode reproductive and fitness genes decreases fecundity of *Heterodera glycines* Ichinohe. *Planta*, 232(3): 775-785. DOI: 10.1007/s00425-010-1209-7

[18] Li J, Todd TC, Lee J, Trick HN. (2011) Biotechnological application of functional genomics towards plant-parasitic nematode control. *Plant Biotechnology Journal*, 9(9): 936-944. DOI: 10.1111/j.1467-7652.2011.00601.x

[19] Li J, Todd TC, Trick HN. (2019) Host-derived gene silencing of parasite fitness genes improves resistance to soybean cyst nematodes in stable transgenic soybean. *Theoretical and Applied Genetics*, 133(3): 1187-1198. DOI: 10.1007/s00122-019-03379-0

[20] Li J, Yang Z, Yu B, Liu J, Chen X. (2005) Methylation protects miRNAs and siRNAs from a 3'-end uridylation activity in Arabidopsis. *Current Biology*, 15(16): 1501-1507. DOI: 10.1016/j.cub.2005.07.029

[21] Flemming HC, Wingender J. (2010) The biofilm matrix. *Nature Reviews Microbiology*, 8(9): 623-633. DOI: 10.1038/nrmicro2415

[22] Flemming HC, Wingender J, Szewzyk U, Steinberg P, Rice SA, Kjelleberg S. (2016) Biofilms: an emergent form of bacterial life. *Nature Reviews Microbiology*, 14(9): 563-575. DOI: 10.1038/nrmicro.2016.94

[23] Costa OYA, Raaijmakers JM, Kuramae EE. (2018) Microbial extracellular polymeric substances: ecological function and impact on soil aggregation. *Frontiers in Microbiology*, 9: 1636. DOI: 10.3389/fmicb.2018.01636

[24] Shuai H, Meng Y, Luo X, Chen F, Zhou W, Dai Y, Qi Y, Du J, Yang F, Liu J, Yang W, Shu K. (2017) Exogenous auxin represses soybean seed germination through decreasing the gibberellin/abscisic acid (GA/ABA) ratio. *Scientific Reports*, 7: 12620. DOI: 10.1038/s41598-017-13093-w

[25] Gazara RK, de Oliveira EAG, Rodrigues BC, Nunes da Fonseca R, Oliveira AEA, Venancio TM. (2019) Transcriptional landscape of soybean (*Glycine max*) embryonic axes during germination in the presence of paclobutrazol. *Scientific Reports*, 9: 9601. DOI: 10.1038/s41598-019-45898-2

[26] Bellieny-Rabelo D, De Oliveira EAG, Ribeiro ES, Costa EP, Oliveira AEA, Venancio TM. (2016) Transcriptome analysis uncovers key regulatory and metabolic aspects of soybean embryonic axes during germination. *Scientific Reports*, 6: 36009. DOI: 10.1038/srep36009

[27] Vaucheret H. (2008) Plant ARGONAUTES. *Trends in Plant Science*, 13(7): 350-358. DOI: 10.1016/j.tplants.2008.04.007

[28] Ishibashi Y, Koda Y, Zheng SH, Yuasa T, Iwaya-Inoue M. (2013) Regulation of soybean seed germination through ethylene production in response to reactive oxygen species. *Annals of Botany*, 111(1): 95-102. DOI: 10.1093/aob/mcs240

[29] Gidrol X, Lin WS, Degousee N, Yip SF, Kush A. (1994) Accumulation of reactive oxygen species and oxidation of cytokinin in germinating soybean seeds. *European Journal of Biochemistry*, 224(1): 21-28. DOI: 10.1111/j.1432-1033.1994.tb19990.x

[30] Bailly C. (2004) Active oxygen species and antioxidants in seed biology. *Seed Science Research*, 14(2): 93-107. DOI: 10.1079/SSR2004159

[31] El-Maarouf-Bouteau H, Bailly C. (2008) Oxidative signaling in seed germination and dormancy. *Plant Signaling and Behavior*, 3(3): 175-182. DOI: 10.4161/psb.3.3.5539

[32] Puntarulo S, Galleano M, Sanchez RA, Boveris A. (1991) Superoxide anion and hydrogen peroxide metabolism in soybean embryonic axes during germination. *Biochimica et Biophysica Acta*, 1074(2): 277-283. DOI: 10.1016/0304-4165(91)90164-c

[33] Puntarulo S, Sanchez RA, Boveris A. (1988) Hydrogen peroxide metabolism in soybean embryonic axes at the onset of germination. *Plant Physiology*, 86(2): 626-630. DOI: 10.1104/pp.86.2.626

[34] Kim HT, Choi UK, Ryu HS, Lee SJ, Kwon OS. (2011) Mobilization of storage proteins in soybean seed (*Glycine max* L.) during germination and seedling growth. *Biochimica et Biophysica Acta -- Proteins and Proteomics*, 1814(9): 1178-1187. DOI: 10.1016/j.bbapap.2011.05.004

[35] He F, Huang F, Wilson KA, Tan-Wilson A. (2007) Protein storage vacuole acidification as a control of storage protein mobilization in soybeans. *Journal of Experimental Botany*, 58(5): 1059-1070. DOI: 10.1093/jxb/erl267

[36] Wilson KA, Chavda BJ, Pierre-Louis G, Quinn A, Tan-Wilson A. (2016) Role of vacuolar membrane proton pumps in the acidification of protein storage vacuoles following germination. *Plant Physiology and Biochemistry*, 104: 242-249. DOI: 10.1016/j.plaphy.2016.03.031

[37] Wei X, Kim WS, Song B, Oehrle NW, Liu S, Krishnan HB. (2020) Soybean mutants lacking abundant seed storage proteins are impaired in mobilization of storage reserves and germination. *ACS Omega*, 5(14): 8065-8075. DOI: 10.1021/acsomega.0c00128

[38] Kanai M, Yamada T, Hayashi M, Mano S, Nishimura M. (2019) Soybean (*Glycine max* L.) triacylglycerol lipase GmSDP1 regulates the quality and quantity of seed oil. *Scientific Reports*, 9: 8924. DOI: 10.1038/s41598-019-45331-8

[39] Kuo TM, Doehlert DC, Crawford CG. (1990) Sugar metabolism in germinating soybean seeds: evidence for the sorbitol pathway in soybean axes. *Plant Physiology*, 93(4): 1514-1520. DOI: 10.1104/pp.93.4.1514

[40] Ni DA, et al. (2018) Genome-wide survey of invertase encoding genes and functional characterization of an extracellular fungal pathogen-responsive invertase in *Glycine max*. *International Journal of Molecular Sciences*, 19(8): 2395. DOI: 10.3390/ijms19082395

[41] Macovei A, Pagano A, Cappuccio M, Gallotti L, Dondi D, De Sousa Araujo S, Fevereiro P, Balestrazzi A. (2019) A snapshot of the trehalose pathway during seed imbibition in *Medicago truncatula*. *Frontiers in Plant Science*, 10: 1590. DOI: 10.3389/fpls.2019.01590

[42] Sainz MM, Filippi CV, Eastman G, Sotelo-Silveira J, Borsani O, Sotelo-Silveira M. (2022) Analysis of thioredoxins and glutaredoxins in soybean: evidence of translational regulation under water restriction. *Antioxidants*, 11(8): 1622. DOI: 10.3390/antiox11081622

[43] Martinez-Ballesta MC, Egea-Gilabert C, Conesa E, Ochoa J, Vicente MJ, Franco JA, Banon S, Martinez JJ, Fernandez JA. (2020) The importance of ion homeostasis and nutrient status in seed development and germination. *Agronomy*, 10(4): 504. DOI: 10.3390/agronomy10040504

[44] Meyer CJ, Steudle E, Peterson CA. (2007) Patterns and kinetics of water uptake by soybean seeds. *Journal of Experimental Botany*, 58(3): 717-732. DOI: 10.1093/jxb/erl244

[45] Sangi S, Santos MLC, Alexandrino CR, Da Cunha M, Coelho FS, Ribeiro GP, Lenz D, Ballesteros H, Hemerly AS, Venancio TM, Oliveira AEA, Grativol C. (2019) Cell wall dynamics and gene expression on soybean embryonic axes during germination. *Planta*, 250(4): 1325-1337. DOI: 10.1007/s00425-019-03231-1

[46] Hettenhausen C, Sun G, He Y, Zhuang H, Sun T, Qi J, Wu J. (2016) Genome-wide identification of calcium-dependent protein kinases in soybean and analyses of their transcriptional responses to insect herbivory and drought stress. *Scientific Reports*, 6: 18973. DOI: 10.1038/srep18973

[47] Yadav M, Pandey J, Chakraborty A, Hassan MI, Kundu JK, Roy A, Singh IK, Singh A. (2022) A comprehensive analysis of calmodulin-like proteins of *Glycine max* indicates their role in calcium signaling and plant defense against insect attack. *Frontiers in Plant Science*, 13: 817950. DOI: 10.3389/fpls.2022.817950

[48] Gao M, Hao Z, Ning Y, He Z. (2024) Revisiting growth-defence trade-offs and breeding strategies in crops. *Plant Biotechnology Journal*, 22(5): 1198-1205. DOI: 10.1111/pbi.14258

[49] Kang YJ, Kim KH, Shim S, Yoon MY, Sun S, Kim MY, Van K, Lee SH. (2012) Genome-wide mapping of NBS-LRR genes and their association with disease resistance in soybean. *BMC Plant Biology*, 12: 139. DOI: 10.1186/1471-2229-12-139

[50] Chang X, Li X, Meng H, Li H, Wu X, Gong G, Chen H, Yang C, Zhang M, Liu T, Chen W, Yang W. (2022) Physiological and metabolic analyses provide insight into soybean seed resistance to *Fusarium fujikuroi* causing seed decay. *Frontiers in Plant Science*, 13: 993519. DOI: 10.3389/fpls.2022.993519

[51] Tang X, Su T, Han M, Wei L, Wang W, Yu Z, Xue Y, Wei H, Du Y, Greiner S, Rausch T, Liu L. (2017) Suppression of extracellular invertase inhibitor gene expression improves seed weight in soybean (*Glycine max*). *Journal of Experimental Botany*, 68(3): 469-482. DOI: 10.1093/jxb/erw425

[52] Su T, Wolf S, Han M, Zhao H, Wei H, Greiner S, Rausch T. (2016) Reassessment of an Arabidopsis cell wall invertase inhibitor AtCIF1 reveals its role in seed germination and early seedling growth. *Plant Molecular Biology*, 90(1-2): 137-155. DOI: 10.1007/s11103-015-0402-2

[53] Jin Y, Ni DA, Ruan YL. (2009) Posttranslational elevation of cell wall invertase activity by silencing its inhibitor in tomato delays leaf senescence and increases seed weight and fruit hexose level. *The Plant Cell*, 21(7): 2072-2089. DOI: 10.1105/tpc.108.063719

[54] Sainz MM, Filippi CV, Eastman G, Sotelo-Silveira J, Borsani O, Sotelo-Silveira M. (2022) Analysis of thioredoxins and glutaredoxins in soybean: evidence of translational regulation under water restriction. *Antioxidants*, 11(8): 1622. DOI: 10.3390/antiox11081622

[55] Nietzel T, Mostertz J, Ruberti C, Née G, Fuchs P, Wagner S, Moseler A, Müller-Schüssele SJ, Benamar A, Poschet G, et al. (2020) Redox-mediated kick-start of mitochondrial energy metabolism drives resource-efficient seed germination. *Proceedings of the National Academy of Sciences USA*, 117(1): 741-751. DOI: 10.1073/pnas.1910501117

[56] Vandesompele J, De Preter K, Pattyn F, Poppe B, Van Roy N, De Paepe A, Speleman F. (2002) Accurate normalization of real-time quantitative RT-PCR data by geometric averaging of multiple internal control genes. *Genome Biology*, 3(7): research0034. DOI: 10.1186/gb-2002-3-7-research0034

[57] Andersen CL, Jensen JL, Orntoft TF. (2004) Normalization of real-time quantitative reverse transcription-PCR data: a model-based variance estimation approach. *Cancer Research*, 64(15): 5245-5250. DOI: 10.1158/0008-5472.CAN-04-0496

[58] Livak KJ, Schmittgen TD. (2001) Analysis of relative gene expression data using real-time quantitative PCR and the 2^-ΔΔCt^ method. *Methods*, 25(4): 402-408. DOI: 10.1006/meth.2001.1262

[59] Schmittgen TD, Livak KJ. (2008) Analyzing real-time PCR data by the comparative C~T~ method. *Nature Protocols*, 3(6): 1101-1108. DOI: 10.1038/nprot.2008.73

[60] Fehr WR, Caviness CE. (1977) Stages of soybean development. Special Report 80. Iowa State University. 11 pp.

[61] German MA, Pillay M, Jeong DH, Hetawal A, Luo S, Janardhanan P, Kannan V, Rymarquis LA, Nobuta K, German R, De Paoli E, Lu C, Schroth G, Meyers BC, Green PJ. (2008) Global identification of microRNA-target RNA pairs by parallel analysis of RNA ends. *Nature Biotechnology*, 26(8): 941-946. DOI: 10.1038/nbt1417

[62] Hernandez-Nistal J, Labrador E, Martin I, Jimenez T, Dopico B. (2006) Transcriptional profiling of cell wall protein genes in chickpea embryonic axes during germination and growth. *Plant Physiology and Biochemistry*, 44(11-12): 684-692. DOI: 10.1016/j.plaphy.2006.10.017

[63] Lin F, Chhapekar SS, Vieira CC, Da Silva MP, Rojas A, et al. (2022) Breeding for disease resistance in soybean: a global perspective. *Theoretical and Applied Genetics*, 135(11): 3773-3872. DOI: 10.1007/s00122-022-04101-3

[64] Paparella S, Araujo SS, Rossi G, Wijayasinghe M, Carbonera D, Balestrazzi A. (2015) Seed priming: state of the art and new perspectives. *Plant Cell Reports*, 34(8): 1281-1293. DOI: 10.1007/s00299-015-1784-y
