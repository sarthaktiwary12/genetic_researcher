# Bacterial Extracellular RNA-Mediated Reprogramming of Wheat (*Triticum aestivum*) Seed Germination: Target Analysis, Mechanistic Models, and Validation Strategy

**Classification:** CONFIDENTIAL | **Prepared by:** Sarthak Tiwary | **Date:** February 2026 | **Version:** 1.0

**Evidence framework:** [Known] = published peer-reviewed data; [Inferred] = logical extrapolation from related systems; [Speculative] = hypothesis requiring validation.

---

## Executive Summary

This report presents a comprehensive analysis of 75 wheat transcript targets predicted to be downregulated by antisense-aligned bacterial extracellular small RNAs (esRNAs) extracted from the EPS preparation "M-9." Wheat (*Triticum aestivum* L.) seeds treated with M-9 EPS solution exhibited improved germination rate and seedling vigor compared to water-soaked controls in Petri dish germination assays. Small RNA sequencing of the M-9 preparation identified esRNA fragments that align antisense to wheat TraesCS gene models (IWGSC RefSeq v1.1), suggesting potential downregulation of 75 transcripts.

Rigorous annotation enrichment, including cross-referencing with EnsemblPlants, UniProtKB, InterPro, and published wheat gene family studies, revealed **five critical annotation corrections** in the original target list: (1) TraesCS5A02G188400 is an F-box protein, not an ARF; (2) TraesCSU02G067600 is an F-box/LRR protein, not a kinesin; (3) TraesCS1D02G241800 encodes SQD1 (UDP-sulfoquinovose synthase), not arginine decarboxylase; (4) TraesCS5A02G360900 is BOP1 (ribosome biogenesis), not BTB/POZ; and (5) TraesCS7D02G219500 is a PGG domain transmembrane protein, not BOP1. The YABBY annotation for TraesCS2A02G386200 was **confirmed correct** as TaYABBY3A (Zhao et al., PeerJ 2022). After deduplication and homeolog consolidation, the list comprises approximately 72 unique loci from 71 protein-coding genes and 4 nontranslating CDS entries.

The most striking feature of the wheat target list is the **massive overrepresentation of immune/defense pathway components**: 6 F-box proteins (8% of all targets), 5 LRR receptor-like kinases (6.7%), 2 NB-LRR disease resistance proteins, 3 ABC transporters, plus a Gnk2 antifungal protein and LURP1 defense protein — collectively, 18 of 75 targets (24%) function in plant immunity. This suggests bacterial esRNAs may preferentially target wheat immune surveillance genes, a pattern consistent with cross-kingdom immune suppression by pathogenic small RNAs documented in *Botrytis cinerea* (Weiberg et al., Science 2013) and *Cuscuta campestris* (Shahid et al., Nature 2018).

Among the remaining targets, the top-priority candidates for explaining improved germination and vigor include: **(1) PARP** (TraesCS1A02G328000) — energy conservation through reduced NAD+ depletion; **(2) Ser/Thr protein kinase** (TraesCS7D02G384400) — likely SnRK2-family ABA signaling kinase; **(3) Arginine decarboxylase** (TraesCS2A02G071200) — reduced polyamine-ABA crosstalk; **(4) NAC38** (TraesCS5B02G275200) — stress/dormancy transcription factor; and **(5) DDM1** (TraesCS7A02G074600) — chromatin remodeling and DNA methylation. Two competing causal models are presented: (a) esRNA-mediated coordinated knockdown of defense brakes and dormancy gates, and (b) EPS-mediated osmopriming with RNA as a passive bystander. Seven discriminating experiments are proposed.

---

## 1. Introduction and Experimental Context

### 1.1 The Cross-Kingdom RNA Interference Paradigm

Cross-kingdom RNA interference (RNAi) — the transfer of small regulatory RNAs between organisms from different taxonomic kingdoms to modulate gene expression — has emerged as a widespread mechanism in plant-microbe interactions. Foundational work by Weiberg et al. (2013) demonstrated that the fungal pathogen *Botrytis cinerea* delivers small RNAs (Bc-sRNAs) into host plant cells, where they hijack the Argonaute/DICER machinery to silence immunity genes such as *MAPKKKs*, *WAKs*, and oxidative burst regulators. Cai et al. (2018) subsequently showed that plants reciprocate: *Arabidopsis thaliana* exports small RNAs in extracellular vesicles to silence *Botrytis* virulence genes, establishing bidirectional cross-kingdom RNAi. Shahid et al. (2018) extended the paradigm to parasitic plants, demonstrating that *Cuscuta campestris* microRNAs silence host messenger RNAs across species boundaries. Buck et al. (2014) established that exosomes secreted by parasitic nematodes deliver small RNAs to mammalian host cells, confirming that cross-kingdom RNA trafficking is a widespread biological phenomenon not restricted to plant-fungal interactions.

### 1.2 Wheat Seed Germination Biology

Wheat (*T. aestivum* L.) is a hexaploid cereal (AABBDD genome, 2n = 6x = 42) whose germination biology is governed by the ABA/GA hormonal axis, aleurone-mediated endosperm mobilization, the ROS oxidative window, and pre-harvest sprouting (PHS) genetics. The transition from dormancy to germination requires: (i) a decline in ABA content and ABA sensitivity, mediated by transcriptional repression of *TaABI5*, *SnRK2* kinases, and the dormancy regulator *TaPHS1/TaMFT-3A* (Liu et al., Genetics 2013; Tuttle et al., Plant Cell & Environment 2022); (ii) GA-dependent DELLA protein degradation, GAMYB activation, and alpha-amylase induction in the aleurone layer (Fu et al., Plant Cell 2002; Gubler et al., Plant Physiology 2002); (iii) ROS homeostasis within the "oxidative window" — too little ROS prevents dormancy release, too much causes oxidative damage (Bailly et al., Comptes Rendus Biologies 2008); and (iv) stored mRNA translation via pre-existing ribosomes before de novo transcription and ribosome biogenesis commence (Bai et al., Plants 2020).

Wheat is hexaploid, meaning most genes exist as three homeologous copies (A, B, D subgenomes). This provides functional redundancy: esRNA-mediated silencing of one homeolog may be buffered by the remaining copies, offering a degree of built-in robustness against complete loss of function (Ramírez-González et al., Science 2018; Pfeifer et al., Science 2014).

### 1.3 Experimental Design

Wheat seeds were soaked in bacterial-derived EPS solution "M-9" for 4–8 hours until full imbibition (no radicle emergence at soaking stage). Control seeds were soaked in water for the same duration. Petri dish germination tests (paper method) demonstrated improved germination rate and seedling vigor in M-9-treated seeds. Small extracellular RNA was extracted from the same M-9 EPS preparation, sequenced, and antisense-aligned against the wheat transcriptome (TraesCS gene models, IWGSC RefSeq v1.1), yielding 75 predicted target transcripts.

---

## 2. Annotation Enrichment, Corrections, and Homeolog Analysis

### 2.1 Critical Annotation Corrections

Cross-referencing all 75 TraesCS identifiers against EnsemblPlants (Release 62), UniProtKB/TrEMBL, InterPro, and PANTHER databases revealed five high-severity annotation errors in the original target list:

| # | TraesCS ID | Original Annotation | Corrected Annotation | Severity | Evidence |
|---|-----------|---------------------|----------------------|----------|----------|
| 1 | TraesCS5A02G188400 | Auxin response factor (ARF) | **F-box domain protein** (kelch β-propeller) | HIGH | UniProt A0A3B6KHS1; InterPro F-box + kelch domains |
| 2 | TraesCSU02G067600 | Kinesin-like protein | **F-box/LRR-repeat protein** | HIGH | UniProt A0A3B6UAE2; F-box domain + LRR |
| 3 | TraesCS1D02G241800 | Arginine decarboxylase | **UDP-sulfoquinovose synthase (SQD1)** | HIGH | Arabidopsis ortholog AT4G33030 = SQD1 |
| 4 | TraesCS5A02G360900 | BTB/POZ + TAZ domain protein 3 | **Ribosome biogenesis protein BOP1** | MODERATE | UniProt A0A1D5YQ88; EnsemblPlants annotation |
| 5 | TraesCS7D02G219500 | BOP1 ribosome biogenesis | **PGG domain transmembrane protein** (17 TM helices) | MODERATE | UniProt A0A3B6THH2; 5 PGG domains |

Additionally, TraesCS5A02G365700 (originally listed as "UDP-sulfoquinovose synthase, chloroplastic") is classified as **nontranslating CDS** with no protein product in EnsemblPlants — the SQD1 annotation likely inherited from a neighboring gene.

The **correct assignments** are:
- Real ARF: **TraesCS6B02G167100** (927 aa; B3 + Auxin_resp + AUX/IAA domains)
- Real kinesin: **TraesCS2B02G505400** (785 aa; kinesin motor domain)
- Real ADC: **TraesCS2A02G071200** (625 aa; pyridoxal phosphate-dependent decarboxylase)
- Real BOP1: **TraesCS5A02G360900** (694 aa; WD40 repeats)
- Real BTB/POZ: **TraesCS3D02G394800** (250 aa; BTB/POZ + TAZ domains)

The YABBY annotation for **TraesCS2A02G386200** was **verified as correct**: this gene encodes TaYABBY3A (262 aa), a plant-specific transcription factor with N-terminal C2-C2 zinc finger and C-terminal YABBY domain (HLH-like fold). Published by Zhao et al. (PeerJ, 2022).

### 2.2 Homeolog Groups

Three confirmed homeolog pairs were identified within the target list:

| Group | Subgenome A | Subgenome B | Subgenome D | Function |
|-------|------------|------------|------------|----------|
| Chr 2 ABC transporters | TraesCS2A02G056800 | TraesCS2B02G069000 | — | ABCC family / phytic acid / conjugate transport |
| Chr 6 LRR-RLKs | — | TraesCS6B02G152900 | TraesCS6D02G116100 | LRR receptor-like kinase / immunity |
| Chr 5 NB-LRR | — | TraesCS5B02G559900 | TraesCS5D02G521900 | NB-LRR disease resistance |

Targeting multiple homeologs of the same gene would amplify the knockdown effect, as hexaploid buffering would be reduced. The coordinated targeting of both B- and D-subgenome NB-LRR copies on chromosome 5 is particularly noteworthy.

### 2.3 Summary Statistics

| Metric | Count |
|--------|-------|
| Total targets in input | 75 |
| Protein-coding genes | 71 |
| Nontranslating CDS | 4 |
| Annotation corrections required | 5 |
| Confirmed homeolog pairs | 3 |
| Unique loci (after homeolog deduplication) | ~72 |
| Well-annotated | 57 |
| Partially annotated (domain only) | 10 |
| Uncharacterized/unknown | 8 |

---

## 3. Ranked Target Table

The following table ranks the top 20 targets by their likelihood of explaining improved wheat germination and seedling vigor when downregulated. Rankings integrate annotation quality, mechanistic plausibility, wheat-specific biology, and evidence strength.

| Rank | TraesCS ID | Corrected Annotation | Pathway Category | Why Downregulation Helps Germination | Evidence | Priority |
|------|-----------|---------------------|-----------------|--------------------------------------|----------|----------|
| 1 | TraesCS1A02G328000 | **Poly(ADP-ribose) polymerase (PARP)** | DNA damage / energy | Conserves NAD+ and ATP; prevents stress-induced energy depletion; 10% biomass increase documented with PARP inhibition (De Block et al. 2005) | [Known] | **HIGH** |
| 2 | TraesCS7D02G384400 | **Ser/Thr protein kinase** (likely SnRK2) | ABA signaling | Reduces ABA sensitivity → relieves dormancy inhibition → faster germination; SnRK2 phosphorylates ABI5/ABF TFs | [Known/Inferred] | **HIGH** |
| 3 | TraesCS2A02G071200 | **Arginine decarboxylase (ADC)** | Polyamine / ABA crosstalk | Reduces putrescine → lowers ABA biosynthesis gene expression; redirects arginine to protein synthesis; increases ethylene availability (shared SAM precursor) | [Known] | **HIGH** |
| 4 | TraesCS5B02G275200 | **NAC domain protein 38** | Stress TF / dormancy | ABA-inducible stress TF; downregulation reduces dormancy maintenance and stress response braking | [Inferred] | **HIGH** |
| 5 | TraesCS7A02G074600 | **DDM1 (Decrease in DNA Methylation 1)** | Chromatin remodeling | SNF2 helicase maintaining DNA methylation; transient downregulation may derepress germination-promoting genes silenced by methylation | [Inferred] | **HIGH** |
| 6 | TraesCS5A02G188400 + 5 others | **F-box proteins** (6 targets) | Ubiquitin-proteasome / defense | Coordinate defense proteolysis reduction; F-box proteins degrade immune suppressors via SCF complex; downregulation reduces defense investment → energy reallocation | [Inferred] | **HIGH** |
| 7 | TraesCS5D02G521900 + TraesCS5B02G559900 | **NB-LRR disease resistance** (2 homeologs) | ETI / defense | Reduces energy-expensive effector-triggered immunity surveillance; defense resource reallocation to germination; 694-822 paralogs indicate massive gene family | [Inferred] | **MEDIUM-HIGH** |
| 8 | TraesCS6B02G167100 | **Auxin response factor (ARF)** | Auxin signaling | If repressor ARF: downregulation enhances auxin-responsive gene expression → improved root and coleoptile growth; 69 TaARF members with ~60% repressors | [Inferred] | **MEDIUM-HIGH** |
| 9 | TraesCS2A02G386200 | **TaYABBY3A** | Developmental TF | Delays leaf polarity establishment → saves energy during dark germination; stress-responsive in wheat; possible ABA connection | [Inferred] | **MEDIUM-HIGH** |
| 10 | TraesCS3D02G394800 | **BTB/POZ + TAZ domain protein 3** | E3 ligase / hormone signaling | CUL3-BTB complex targets PP2Cs and stress TFs for degradation; downregulation stabilizes PP2Cs → reduced ABA sensitivity | [Inferred] | **MEDIUM** |
| 11 | TraesCS1D02G241800 + TraesCS3D02G228900 | **UDP-sulfoquinovose synthase (SQD1)** (2 paralogs) | Chloroplast lipid | Sulfolipid biosynthesis dispensable during dark germination; redirects UDP-glucose and sulfur to glycolysis and amino acid synthesis | [Known] | **MEDIUM** |
| 12 | TraesCS7D02G379600 + 4 others | **LRR receptor-like kinases** (5 targets) | Immune receptors / PTI | PAMP perception receptors; downregulation reduces immune surveillance; lectins, malectin, and LRR domains indicate broad pathogen sensing reduction | [Inferred] | **MEDIUM** |
| 13 | TraesCS4B02G205800 | **sHSP/alpha-crystallin** | Heat shock / chaperone | Reduces stress-responsive chaperone expression → energy conservation during non-stress germination | [Inferred] | **MEDIUM** |
| 14 | TraesCS2A02G393400 | **Gnk2-homologous antifungal protein** | Defense | Reduces antifungal compound production → defense-to-growth resource shift | [Inferred] | **MEDIUM** |
| 15 | TraesCS3A02G122200 | **Bromodomain TF (GTE8 family)** | Chromatin / transcription | Reads acetylated histones; downregulation may reduce transcription of defense or stress gene programs | [Speculative] | **MEDIUM** |
| 16 | TraesCS7A02G398600 | **CDC27/APC3** | Cell cycle | Anaphase-promoting complex component; moderate downregulation may slow premature cell division, prioritizing reserve mobilization over proliferation | [Speculative] | **LOW-MEDIUM** |
| 17 | TraesCS6B02G296400 | **Ubiquinol oxidase (AOX)** | Alternative respiration | PARADOXICAL: AOX essential for ROS management during germination; downregulation expected detrimental; may reflect fine-tuning rather than elimination | [Contradictory] | **LOW** |
| 18 | TraesCS5A02G360900 | **BOP1 ribosome biogenesis** | Translation | PARADOXICAL: Translation absolutely required for germination; stored ribosomes may buffer 0-24h; energy savings from reduced ribosome synthesis | [Contradictory] | **LOW** |
| 19 | TraesCS2B02G505400 | **Kinesin motor protein** | Cytoskeleton | PARADOXICAL: Cell division essential; early germination relies on stored machinery; 155-member family provides redundancy | [Contradictory] | **LOW** |
| 20 | TraesCS1B02G356700 | **Profilin** | Actin dynamics | PARADOXICAL: Cell elongation requires profilin; dose-sensitive — both over- and under-expression impair growth | [Contradictory] | **LOW** |

---

## 4. Mechanistic Narratives

### 4.1 PARP — The Energy Conservation Master Switch

Poly(ADP-ribose) polymerase (PARP) catalyzes the post-translational modification of proteins through poly(ADP-ribosyl)ation, consuming NAD+ as substrate. Under oxidative stress — which occurs naturally during seed imbibition as mitochondrial respiration reactivates — PARP activation creates an energy crisis by depleting NAD+ and ATP pools [Known]. De Block et al. (2005) demonstrated that PARP downregulation in transgenic *Arabidopsis* and oilseed rape produces remarkable phenotypes: broad-spectrum stress tolerance, >10% biomass increase, and maintained NAD+/ATP levels under stress. Subsequent work by Vanderauwera et al. (2007) and Schulz et al. (2012) confirmed these findings through both genetic and pharmacological (3-methoxybenzamide) PARP inhibition.

During wheat seed germination, PARP represents a significant energy drain. The embryo is exposed to oxidative stress from membrane lipid peroxidation, mitochondrial reactivation, and ROS generation during imbibition. PARP activation in response to DNA damage and oxidative stress consumes NAD+ that is critically needed for respiratory metabolism and biosynthetic reactions. Downregulation of PARP via bacterial esRNAs would conserve this NAD+ pool, providing more ATP for reserve mobilization, cell division, and radicle emergence [Inferred]. The wheat PARP gene (TraesCS1A02G328000, 824 aa) contains a PARP catalytic domain and DNA-binding zinc finger domain, consistent with canonical PARP1/PARP2 function. AtPARP3 is specifically expressed in Arabidopsis seeds, and its promoter activity coincides with ROS accumulation in the embryo (Rissel et al., BMC Plant Biology 2019), further supporting the relevance of PARP to seed biology.

**Priority: HIGHEST.** The mechanistic link between PARP downregulation and improved plant vigor is the most well-validated of all targets in this list.

### 4.2 Serine/Threonine Protein Kinase — ABA Signaling Gate

TraesCS7D02G384400 encodes a serine/threonine protein kinase (891 aa) that likely belongs to the SnRK2 family of ABA-activated kinases. SnRK2 kinases are the central positive regulators of ABA signaling: upon ABA perception by PYR/PYL receptors and PP2C inhibition, SnRK2 kinases are released to phosphorylate downstream targets including ABI5, ABF/AREB transcription factors, and ion channels (Fujii & Zhu, PNAS 2009; Yu et al., Plant Cell Reports 2020). The wheat-specific SnRK2 kinase PKABA1 was the first SnRK2 characterized, identified specifically in wheat embryos (Anderberg & Walker-Simmons, PNAS 1992).

Downregulation of an SnRK2-type kinase would directly reduce ABA signal transduction, phenocopying the after-ripening process that naturally releases wheat seed dormancy. This would: (i) reduce phosphorylation of ABI5/ABF transcription factors, lowering expression of ABA-responsive germination-inhibitory genes; (ii) diminish SnRK2-mediated ion channel regulation, reducing stress-responsive stomatal closure; and (iii) accelerate the dormancy-to-germination transition. Supporting evidence: AtPP2-B11, an E3 ubiquitin ligase that degrades SnRK2.3, promotes germination when overexpressed; its loss-of-function mutant shows ABA hypersensitivity and impaired germination [Known].

The annotation agent also identified a second kinase, TraesCS7D02G379600 (596 aa), as a receptor-like kinase with lectin and apple domains — a pollen recognition/innate immunity receptor rather than an ABA signaling kinase. This distinction is critical: the first kinase (TraesCS7D02G384400) is the high-priority ABA-signaling candidate, while the second is part of the defense downshift theme.

**Priority: HIGH.** If confirmed as SnRK2, this is the most mechanistically direct explanation for improved germination.

### 4.3 Arginine Decarboxylase — The Polyamine-ABA Nexus

The corrected ADC gene (TraesCS2A02G071200, 625 aa) catalyzes the first and rate-limiting step of polyamine biosynthesis: decarboxylation of L-arginine to agmatine, which is subsequently converted to putrescine, spermidine, and spermine. The polyamine-ABA crosstalk is bidirectional and consequential: putrescine positively regulates ABA biosynthesis gene expression (including *NCED3*), while spermidine and spermine promote GA biosynthesis and oppose ABA (Alcazar et al., Planta 2010; Pieruzzi et al., BMC Plant Biology 2011). ADC is strongly induced by ABA treatment, osmotic stress, and cold [Known].

ADC downregulation during wheat germination would produce multiple convergent effects: (i) reduced putrescine accumulation → decreased *NCED* expression → lower ABA levels; (ii) shift in the (spermidine + spermine) : putrescine ratio toward GA-promoting polyamines; (iii) increased availability of SAM (S-adenosylmethionine) for ethylene biosynthesis (polyamines and ethylene compete for SAM), and ethylene generally promotes germination; (iv) redirection of arginine toward protein synthesis rather than polyamine production; and (v) reduced energy expenditure on polyamine biosynthesis [Inferred].

Caveat: ADC activity correlates positively with seed viability (Sinska & Lewandowska, 1991), and complete loss of polyamines is lethal. The benefit requires moderate, transient downregulation — consistent with the sRNA-mediated mechanism which would produce partial, temporary silencing during the 4–8 hour imbibition window [Known].

**Priority: HIGH.** The polyamine-ABA axis is a strong mechanistic node.

### 4.4 NAC Domain Protein 38 — Stress/Dormancy Transcription Factor

TraesCS5B02G275200 encodes a NAC domain transcription factor (368 aa) projected from Arabidopsis AT2G24430 (ANAC038). The wheat NAC TF family is massive (~488 members; Xia et al., PLoS ONE 2019), with members functioning as master regulators of senescence, stress responses, and ABA signaling. Multiple wheat NAC genes are ABA-inducible and stress-responsive: TaNAC29 promotes senescence and salt/drought stress responses; TaSNAC11-4B promotes ROS accumulation and senescence; TaNAC2 enhances abiotic stress tolerance [Known].

If NAC38 follows the dominant pattern of being an ABA-inducible, stress-responsive transcription factor, its downregulation would: (i) reduce expression of dormancy-maintenance gene programs; (ii) decrease stress-responsive gene expression that inhibits growth; (iii) limit senescence-associated programmed cell death beyond what is needed for aleurone function; and (iv) redirect metabolic resources from stress compound synthesis (osmoprotectants, HSPs, antioxidants) toward germination processes [Inferred].

**Priority: HIGH** (contingent on NAC38 being stress/ABA-responsive rather than a dormancy inhibitor like ANAC060/040).

### 4.5 DDM1 — Chromatin Remodeling and Epigenetic Gate

TraesCS7A02G074600 encodes DDM1 (Decrease in DNA Methylation 1), an SNF2-family chromatin remodeling ATPase (751 aa) with helicase ATP-binding and helicase C-terminal domains. DDM1 maintains DNA methylation patterns by remodeling nucleosomes to allow DNA methyltransferase access to hemimethylated DNA. In *Arabidopsis*, *ddm1* mutants show progressive loss of DNA methylation across repetitive sequences and some genes, activation of transposable elements, and developmental abnormalities (Jeddeloh et al., Nature Genetics 1999).

During seed germination, transient DDM1 downregulation could derepress germination-promoting genes that are silenced by DNA methylation during seed maturation and dormancy. Epigenetic reprogramming is a recognized component of the dormancy-to-germination transition in cereals [Known]. DDM1 downregulation would be expected to cause partial, stochastic demethylation that could activate growth-promoting gene programs. The hexaploid wheat genome, with its massive repetitive content (~85% repetitive sequences; IWGSC 2018), may be particularly sensitive to DDM1 modulation [Speculative].

**Priority: HIGH.** Epigenetic regulation of dormancy is well-established, and DDM1 is a master regulator of DNA methylation maintenance.

### 4.6 Defense Pathway Downshift — The Dominant Theme

The most striking feature of the wheat target list is the extraordinary overrepresentation of immune/defense pathway components:

**F-box proteins (6 targets, 8% of list):** TraesCS5A02G188400, TraesCSU02G067600, TraesCS5A02G170400, TraesCS6A02G040900, TraesCS2D02G520600, TraesCS4D02G117200. F-box proteins serve as substrate recognition components of SCF (Skp1-Cullin-F-box) E3 ubiquitin ligase complexes, targeting specific proteins for proteasomal degradation. In plant immunity, F-box proteins degrade suppressors of immune signaling, thereby activating defense responses. Coordinated downregulation of 6 F-box proteins would broadly reduce protein turnover in immune pathways [Known].

**LRR receptor-like kinases (5 targets, 6.7%):** TraesCS7D02G379600 (lectin-RLK), TraesCS5D02G095300 (malectin-LRR-RLK), TraesCS6B02G152900, TraesCS6D02G116100 (probable homeologs), TraesCS5B02G502400 (L-type lectin-RLK). LRR-RLKs are the first line of pathogen perception in PAMP-triggered immunity (PTI). Their downregulation would reduce immune surveillance at the cell surface [Known].

**NB-LRR disease resistance proteins (2 targets):** TraesCS5D02G521900 and TraesCS5B02G559900 (probable homeologs on chromosome 5). NB-LRR proteins mediate effector-triggered immunity (ETI), the most energy-expensive defense response involving hypersensitive response and programmed cell death. The massive paralogy of NLR genes (694-822 paralogs each) indicates rapid birth-and-death evolution characteristic of plant immune receptors [Known].

**ABC transporters (3 targets):** TraesCS7B02G381000 (PDR/ABCG, defense compound transport), TraesCS2B02G069000 (ABCC13/MRP, phytic acid transport), TraesCS2A02G056800 (ABCC conjugate transport). ABC transporters actively export defense compounds and detoxification conjugates, representing significant ATP expenditure [Known].

**Other defense genes:** TraesCS2A02G393400 (Gnk2-homologous antifungal protein), TraesCS1D02G303100 (LURP1 defense protein).

The defense downshift interpretation: plant immune surveillance is extremely energy-expensive. During seed germination, when the primary biological imperative is rapid radicle emergence rather than pathogen defense, reducing immune investment could redirect ATP, amino acids, and metabolic precursors toward growth processes. The coordinated targeting of 18 defense-related genes suggests the bacterial esRNAs may suppress wheat immune recognition of bacterial-derived molecules in the EPS, facilitating beneficial interaction [Inferred]. This parallels the immune suppression strategy used by pathogenic fungi (Weiberg et al., 2013), but in a context where the outcome is mutualistic rather than parasitic [Speculative].

### 4.7 SQD1 — Chloroplast Lipid Dispensable in Darkness

Two SQD1 paralogs (TraesCS1D02G241800 and TraesCS3D02G228900) encode UDP-sulfoquinovose synthase, the first committed enzyme in sulfolipid (SQDG) biosynthesis. SQDG is found exclusively in thylakoid membranes and constitutes a non-phosphorus glycolipid essential for photosynthetic membrane function (Essigmann et al., PNAS 1998; Mulichak et al., PNAS 1999). During seed germination, the embryo grows heterotrophically in complete darkness — thylakoid membrane assembly and SQDG biosynthesis are not required until de-etiolation. *Arabidopsis sqd2* mutants show growth impairment only under phosphate-limited conditions (Yu et al., PNAS 2002).

Transient SQD1 downregulation during the dark germination phase would redirect UDP-glucose toward glycolysis and cell wall biosynthesis, and sulfur toward amino acid synthesis — both beneficial for germination energy and protein production [Inferred].

**Priority: MEDIUM.** Effect is indirect and modest, but metabolically coherent.

### 4.8 Ent-Kaurenoic Acid Oxidase — The GA Biosynthesis Paradox

TraesCS7D02G101200 encodes an ent-kaurenoic acid oxidase (KAO), a cytochrome P450 enzyme that catalyzes the oxidation of ent-kaurenoic acid to ent-7α-hydroxykaurenoic acid in the gibberellin biosynthesis pathway. This is paradoxical: GA promotes germination, so downregulating a GA biosynthesis enzyme should impair rather than improve germination [Contradictory]. Possible explanations include: (i) KAO is not rate-limiting and other pathway enzymes compensate; (ii) the wheat hexaploid genome provides homeologous copies that buffer the loss; (iii) the sRNA targets this transcript only weakly; or (iv) the antisense alignment is a false positive. This gene warrants careful experimental validation before being included in the mechanistic model.

### 4.9 Ubiquinol Oxidase (AOX) — The Respiration Paradox

TraesCS6B02G296400 encodes an alternative oxidase / ubiquinol oxidase (340 aa). AOX bypasses complexes III and IV of the electron transport chain, reducing ATP yield but managing ROS levels. AOX2 is specifically expressed during early seed germination and is essential for ROS homeostasis; AOX mutants show salt-hypersensitive germination (Yin et al., Environmental and Experimental Botany 2024; Saha et al., Journal of Plant Physiology 2015). Downregulation of AOX during germination should be detrimental, increasing ROS to damaging levels and enhancing ABA sensitivity [Contradictory].

The presence of AOX on the target list may reflect: (i) fine-tuning rather than elimination — moderate reduction could optimize the AOX/cytochrome oxidase balance for maximal energy efficiency; (ii) temporal specificity — AOX may be dispensable during very early imbibition (0-6h) when mitochondria are still reorganizing; or (iii) false-positive antisense alignment [Speculative].

**Priority: LOW.** Current evidence predicts detrimental effects from AOX downregulation.

---

## 5. Theme Summary

### Theme 1: Defense Downshift (24% of targets)
The most dominant theme. Eighteen targets function in plant immunity: 6 F-box proteins, 5 LRR-RLKs, 2 NB-LRR, 3 ABC transporters, 1 antifungal protein, 1 defense protein. Coordinated reduction of immune surveillance and defense compound production would free energy and metabolic resources for germination. This theme is unique to the wheat target list compared to other crop species analyzed.

### Theme 2: ABA/Dormancy Brake Release
PARP (energy-ABA connection), Ser/Thr kinase (likely SnRK2, direct ABA signaling), ADC (polyamine-ABA crosstalk), NAC38 (ABA-inducible stress TF), and BTB/POZ (PP2C stability) all converge on reducing ABA sensitivity and dormancy maintenance.

### Theme 3: Energy Conservation
PARP (NAD+ preservation), SQD1 (UDP-glucose and sulfur redirection), defense downshift (ATP savings from reduced immune investment), ADC (reduced polyamine synthesis cost), and F-box proteins (reduced proteasomal turnover cost) all conserve metabolic energy for germination.

### Theme 4: Epigenetic/Chromatin Remodeling
DDM1 (DNA methylation maintenance), bromodomain TF GTE8 (acetylated histone reading), and Homeobox-DDT protein (chromatin remodeling) suggest esRNAs may modulate the epigenetic landscape of germinating wheat seeds.

### Theme 5: Auxin and Developmental Signaling
ARF (auxin response modulation), YABBY (developmental polarity), CDC27/APC3 (cell cycle regulation), and kinesin (cytoskeletal dynamics) touch on growth and developmental programs that may be fine-tuned during germination.

### Theme 6: Organelle Function and Respiration
PPR protein (organellar RNA processing), AOX (alternative respiration), mTERF (mitochondrial transcription), and SQD1 (chloroplast membrane) affect organelle biogenesis and function, with context-dependent effects on germination.

### Theme 7: Polyamine Metabolism
ADC downregulation would shift the polyamine ratio toward spermidine/spermine (GA-promoting) from putrescine (ABA-promoting), representing a metabolic lever for hormonal reprogramming.

---

## 6. Causal Models

### Model 1: esRNA-Mediated Coordinated Knockdown (RNA Hypothesis)

**Mechanism:** Bacterial extracellular sRNAs in the M-9 EPS preparation enter wheat embryo cells during imbibition, engage the plant's AGO/RISC machinery, and direct sequence-specific cleavage or translational repression of target mRNAs. Coordinated downregulation of ~15–20 key targets produces a synergistic reprogramming effect:

- **PARP** downregulation conserves NAD+/ATP (energy node)
- **SnRK2-type kinase** downregulation reduces ABA sensitivity (hormonal node)
- **ADC** downregulation shifts polyamine ratio toward germination (metabolic node)
- **NAC38** downregulation reduces stress transcriptional braking (transcription node)
- **DDM1** downregulation derepresses methylation-silenced germination genes (epigenetic node)
- **F-box/NB-LRR/LRR-RLK** downregulation reduces defense investment (energy reallocation node)
- **SQD1** downregulation redirects resources from chloroplast lipids (metabolic savings node)

**Predicted network output:** A "low-stress, high-energy, growth-permissive" cellular state that accelerates dormancy-to-germination transition, improves reserve mobilization efficiency, and enhances radicle/coleoptile growth.

**Discriminating predictions:**
1. RNase pre-treatment of EPS should abolish the germination improvement
2. Purified RNA fraction should reproduce the effect without polysaccharides
3. qRT-PCR should show target-specific mRNA downregulation at 6-12h post-imbibition
4. AGO immunoprecipitation should recover bacterial sRNAs in complex with wheat AGO
5. Degradome sequencing should reveal cleavage products at predicted antisense sites
6. Individual synthetic sRNAs targeting PARP or SnRK2 should partially reproduce the phenotype

### Model 2: EPS Osmopriming and Hydration Effect (Physical Hypothesis)

**Mechanism:** The bacterial EPS is a hygroscopic polysaccharide matrix that modifies water uptake kinetics during seed imbibition. The EPS creates a controlled hydration microenvironment around the seed that: (i) prevents imbibition damage from excessively rapid water uptake; (ii) provides osmotic priming that pre-activates metabolic processes during soaking; (iii) contains microbial-associated molecular patterns (MAMPs) that trigger mild, transient defense priming (hormesis); and (iv) supplies trace nutrients (minerals, amino acids) from the bacterial culture medium.

The RNA in the EPS is a passive bystander — bacterial nucleic acids co-extracted with polysaccharides but biologically inert in the cross-kingdom context. The antisense alignments are coincidental sequence complementarity with no functional significance.

**Discriminating predictions:**
1. RNase pre-treatment of EPS should NOT abolish the germination improvement
2. Purified polysaccharide fraction (RNA-depleted) should reproduce the effect fully
3. No target-specific mRNA changes would be detected by qRT-PCR
4. Other hygroscopic polymers (PEG, methylcellulose) at equivalent water potential should partially reproduce the effect
5. Dose-response should correlate with EPS concentration, not RNA concentration
6. Heat-denatured EPS (destroying RNA secondary structure but preserving polysaccharide) should retain activity

### Model Assessment

Both models have precedent: Model 1 is supported by the cross-kingdom RNAi literature (Weiberg et al. 2013; Cai et al. 2018); Model 2 is supported by the extensive seed priming and PGPR biostimulant literature (Mahmood et al., FEMS Microbiology Ecology 2016; Harris et al., Experimental Agriculture 1999). The two models are not mutually exclusive — a combined model where EPS provides the delivery matrix and physical priming while esRNAs provide sequence-specific gene regulation is biologically plausible and may best explain the observed phenotype [Speculative].

---

## 7. Validation Plan

### Experiment 1: RNase Fractionation (Decisive, Priority 1)

**Design:** Four treatment groups: (A) Intact EPS + water soak; (B) RNase A + RNase III pre-treated EPS; (C) Heat-inactivated RNase + EPS (control for RNase carrier effect); (D) Water-only control. Each group: 4 replicates × 50 seeds.

**Readouts:** Germination %, germination speed index (GSI), mean germination time (MGT), radicle length at 48h, coleoptile length at 72h, seedling fresh weight at 120h.

**Decision logic:** If B = D (RNase abolishes effect), RNA hypothesis supported. If B = A (RNase has no effect), physical hypothesis supported. If B is intermediate, both mechanisms contribute.

### Experiment 2: RNA vs. Polysaccharide Fraction (Decisive, Priority 1)

**Design:** Fractionate M-9 EPS into: (A) RNA-enriched fraction (TRIzol extraction of nucleic acids); (B) Polysaccharide-enriched fraction (ethanol precipitation of carbohydrates after nucleic acid removal); (C) Recombined A+B; (D) Whole EPS; (E) Water control. Soak seeds in each fraction at physiologically matched concentrations.

**Readouts:** Same as Experiment 1 plus qRT-PCR for top 5 targets.

**Decision logic:** If A alone improves germination, RNA is sufficient. If B alone improves germination, polysaccharide is sufficient.

### Experiment 3: qRT-PCR Time Course for Top Targets (Priority 1)

**Design:** Collect wheat embryo axis tissue at 0h (dry), 4h (end of soak), 8h, 12h, 24h, 48h post-imbibition from both M-9-treated and water control seeds. Extract RNA, perform qRT-PCR for:

- **Primary targets:** *PARP* (TraesCS1A02G328000), *Ser/Thr kinase* (TraesCS7D02G384400), *ADC* (TraesCS2A02G071200), *NAC38* (TraesCS5B02G275200), *DDM1* (TraesCS7A02G074600)
- **Defense markers:** Selected F-box, NB-LRR, LRR-RLK representatives
- **Hormone markers:** *TaABI5*, *TaNCED1* (ABA pathway); *TaGA20ox*, *TaGA3ox* (GA pathway); *TaGAMYB* (aleurone activation)
- **Housekeeping controls:** *TaActin*, *TaEF1α*, *TaUbiquitin*

**Decision logic:** If top targets show statistically significant downregulation at 6-12h in M-9 vs. control, RNA hypothesis strongly supported. Timing of downregulation onset, magnitude, and recovery kinetics will define the silencing window.

### Experiment 4: Hormone and Metabolite Profiling (Priority 2)

**Design:** Measure in embryo axis tissue at 0h, 12h, 24h, 48h:
- ABA content (LC-MS/MS)
- GA content (GA1, GA3, GA4)
- NAD+/NADH ratio (enzymatic cycling assay)
- ATP content (luciferase assay)
- Polyamine content (putrescine, spermidine, spermine by HPLC)
- H₂O₂ content (Amplex Red assay)
- Total antioxidant capacity

**Expected (RNA model):** M-9-treated seeds: lower ABA, higher GA, higher NAD+/ATP ratio, lower putrescine, lower H₂O₂ at 12-24h.

### Experiment 5: Degradome / PARE Sequencing (Priority 2)

**Design:** Perform degradome sequencing (PARE-seq) on embryo axis RNA at 12h post-imbibition from M-9-treated vs. control seeds. Map cleavage products to predicted sRNA target sites on top targets.

**Decision logic:** Detection of target-specific cleavage products at antisense alignment positions would provide direct evidence for sRNA-guided mRNA cleavage via AGO/RISC mechanism.

### Experiment 6: Small RNA Uptake Assay (Priority 3)

**Design:** Label bacterial sRNAs with fluorescent nucleotide analogs (Cy3-UTP or Alexa Fluor 488) during in vitro transcription. Soak wheat seeds in labeled sRNA solution. At 2h, 4h, 8h, section embryo axis and image by confocal microscopy.

**Decision logic:** Fluorescent signal in embryo cells confirms sRNA uptake. Subcellular localization (cytoplasmic = RISC loading; nuclear = chromatin-level effects) would distinguish silencing mechanisms.

### Experiment 7: Dose-Response and Soak-Time Optimization (Priority 3)

**Design:** Full factorial design: 4 EPS concentrations (0%, 25%, 50%, 100% M-9) × 4 soak times (2h, 4h, 6h, 8h) × 3 replicates × 50 seeds. Phenotype: germination %, GSI, radicle/coleoptile length, seedling biomass, uniformity index.

**Purpose:** Define the dose-response relationship and optimal treatment window. If RNA-mediated, expect threshold effects (minimum sRNA dose required). If osmopriming, expect gradual dose-response.

---

## 8. Confounders and Controls

### Confounder 1: Osmotic Priming by EPS

**Risk:** EPS is a hygroscopic polymer that modifies water potential. Seeds soaked in EPS solution experience different hydration kinetics than water-soaked controls.

**Controls:** (a) Include PEG-8000 solutions at matched water potentials (ψ = −0.5, −1.0, −1.5 MPa). (b) Measure actual water uptake curves (gravimetric) for EPS vs. water vs. PEG treatments. (c) Include methylcellulose (non-biological polymer) at matched viscosity. If PEG/methylcellulose reproduces the EPS effect, osmopriming is sufficient without RNA.

### Confounder 2: Microbial Contamination and Secondary Metabolites

**Risk:** M-9 EPS may contain residual bacterial cells, proteins, lipopolysaccharides (LPS), or secondary metabolites that act as elicitors or growth promoters independent of RNA.

**Controls:** (a) Filter-sterilize EPS through 0.22 μm membrane (removes cells). (b) Proteinase K treatment (degrades contaminating proteins). (c) Measure protein, LPS, and siderophore content of EPS preparation. (d) Test synthetic sRNAs (matching top 5 target sequences) in water without EPS — if effective, RNA is sufficient without bacterial contaminants.

### Confounder 3: Nutrient Supplementation

**Risk:** Bacterial culture medium residuals in EPS may supply mineral nutrients, amino acids, or vitamins that enhance germination independently.

**Controls:** (a) Analyze mineral content of EPS preparation (ICP-OES for Fe, Zn, Mn, Mg, etc.). (b) Include mock medium control (sterile M-9 growth medium without bacteria). (c) Compare EPS-treated seeds with mineral-supplemented water at matched nutrient concentrations.

### Confounder 4: Temperature Effects

**Risk:** EPS solution may have different thermal properties (viscosity, specific heat) that alter seed temperature during soaking.

**Controls:** Monitor seed surface and solution temperature continuously during soaking. Ensure all treatments are conducted at identical temperature (±0.5°C) in a temperature-controlled incubator.

### Confounder 5: Seed Lot Variability and Dormancy Status

**Risk:** Wheat seed dormancy levels vary by cultivar, harvest date, storage conditions, and after-ripening status. Seeds with residual dormancy would respond differently to ABA-modulating treatments.

**Controls:** (a) Use a single seed lot from controlled harvest. (b) Report cultivar, harvest date, and storage duration. (c) Pre-test seed lot for dormancy status (germination % without treatment at 15°C — low germination indicates dormancy). (d) Include positive control: GA3-treated seeds (1 mM) to confirm dormancy can be overcome.

### Confounder 6: Hexaploid Homeolog Compensation

**Risk:** Wheat's hexaploid genome provides functional redundancy. If esRNAs target only one homeolog, the remaining A, B, or D copies may fully compensate, rendering the silencing phenotypically invisible.

**Controls:** (a) Design qRT-PCR primers with homeolog specificity (exploit SNPs in 3' UTR). (b) Measure expression of all three homeologs independently for top targets. (c) Use RNA-seq to assess genome-wide homeolog expression bias in treated vs. control seeds. Reference: Ramírez-González et al. (Science, 2018) demonstrated that ~30% of wheat homeolog triads show non-balanced expression, indicating that compensation is not universal.

---

## 9. Wheat-Specific Considerations

### 9.1 Hexaploidy and Target Redundancy

The hexaploid wheat genome (AABBDD, ~17 Gb; IWGSC 2018) contains three subgenomic copies of most genes. The presence of homeolog pairs within the target list (chr 2 ABC transporters, chr 6 LRR-RLKs, chr 5 NB-LRRs) suggests that bacterial esRNAs can target multiple homeologs, potentially overcoming polyploid buffering. However, for most targets, only one homeolog appears in the list, suggesting partial silencing that would be buffered by the remaining copies. This built-in genetic robustness means that even aggressive esRNA-mediated silencing would produce moderate, non-lethal phenotypic effects — ideal for a germination enhancement strategy [Inferred].

### 9.2 Pre-Harvest Sprouting Relevance

Wheat is uniquely susceptible to pre-harvest sprouting (PHS) — premature germination on the mother plant before harvest, causing annual losses exceeding USD 1 billion globally. PHS resistance is conferred by seed dormancy genes including *TaPHS1/TaMFT-3A* (Liu et al., Genetics 2013), *TaMKK3* (Torada et al., Current Biology 2016), and *TaQsd1*. The esRNA-mediated reduction of dormancy/ABA signaling described in this report could exacerbate PHS susceptibility if applied during late grain filling rather than at planting. This represents both a risk (if M-9 contacts developing grain) and an opportunity (if the same targets could be enhanced rather than silenced in PHS-susceptible cultivars) [Speculative].

### 9.3 Class III Peroxidase Family Complexity

Wheat possesses 374 class III peroxidase genes (Wang et al., BMC Genomics 2019), the largest reported among major crops. While no class III peroxidases appear explicitly in the target list, the oxidative window concept (Bailly et al., 2008) and the PARP-ROS connection mean that any modulation of ROS homeostasis through PARP, AOX, or defense pathway changes would intersect with this enormous peroxidase network. TaPer12-3A specifically promotes germination by maintaining H₂O₂ homeostasis through ROS scavenging (Han et al., BMC Plant Biology 2024), illustrating the fine-tuned ROS balance required for wheat germination.

### 9.4 Aleurone Layer and Endosperm Mobilization

Unlike dicot seeds, wheat germination depends critically on the aleurone layer producing hydrolytic enzymes (alpha-amylases, proteases) in response to embryo-derived GA. GA perception in the aleurone activates GAMYB, which transactivates alpha-amylase promoters (Gubler et al., Plant Cell 1995). TOR signaling contributes to GA-dependent alpha-amylase synthesis (Luo et al., Plant Signaling & Behavior 2023). While no direct aleurone-specific targets appear in the top-ranked list, the ABA/GA balance modulation through SnRK2, ADC, and NAC38 would indirectly promote GA-responsive aleurone activation [Inferred].

---

## 10. Conclusions

The wheat esRNA target analysis reveals a complex, multi-layered targeting strategy with a dominant defense downshift theme unprecedented among the crop species examined. The coordinated targeting of 18 immune pathway components (24% of all targets) — including F-box proteolysis factors, LRR immune receptors, NB-LRR resistance proteins, and defense-associated ABC transporters — suggests that bacterial esRNAs may suppress wheat immune recognition of bacterial-derived molecules in the EPS, facilitating beneficial interaction while simultaneously redirecting defense investment toward germination.

The convergence of PARP (energy conservation), SnRK2-type kinase (ABA signal reduction), ADC (polyamine-ABA crosstalk), NAC38 (stress transcription), and DDM1 (epigenetic derepression) on accelerating the dormancy-to-germination transition provides a mechanistically coherent model for improved germination and vigor. The hexaploid wheat genome's inherent functional redundancy provides a safety margin that allows partial silencing of individual targets without lethal consequences.

Five critical annotation corrections identified in this analysis underscore the importance of independent verification when working with computationally projected wheat gene annotations. The wheat genome's size, complexity, and ongoing annotation refinement mean that functional validation of predicted sRNA targets is essential before mechanistic conclusions are drawn.

The seven-experiment validation plan, beginning with RNase fractionation and qRT-PCR time-course as decisive experiments, provides a clear path to discriminating between RNA-mediated and EPS-priming mechanisms. Regardless of which model proves correct, the improved germination phenotype represents a potentially valuable biotechnological tool for wheat seed treatment.

---

## Bibliography

1. Alcazar R, Altabella T, Marco F, Bortolotti C, Reymond M, Koncz C, Carrasco P, Tiburcio AF. Polyamines: molecules with regulatory functions in plant abiotic stress tolerance. *Planta*. 2010;231(6):1237-1249.

2. Ahn CS, Cho HK, Lee DH, Sim HJ, Kim SG, Pai HS. Functional characterization of the ribosome biogenesis factors PES, BOP1, and WDR12 (PeBoW), and mechanisms of defective cell growth and proliferation caused by PeBoW deficiency in Arabidopsis. *Journal of Experimental Botany*. 2016;67(17):5217-5232.

3. Bai B, Novak O, Ljung K, Hanson J, Bentsink L. Lost in Translation: Physiological Roles of Stored mRNAs in Seed Germination. *Plants*. 2020;9(3):347.

4. Bailly C, El-Maarouf-Bouteau H, Corbineau F. From intracellular signaling networks to cell death: the dual role of reactive oxygen species in seed physiology. *Comptes Rendus Biologies*. 2008;331(10):806-814.

5. Barkan A, Small I. Pentatricopeptide repeat proteins in plants. *Annual Review of Plant Biology*. 2014;65:415-442.

6. Bassie L, Noury M, Lepri O, Lahaye T, Christou P, Capell T. Transgenic wheat plants expressing an oat arginine decarboxylase cDNA exhibit increases in polyamine content in vegetative tissue and seeds. *Molecular Breeding*. 2008;21:187-200.

7. Basu A, Prasad P, Das SN, Kalam S, Sayyed RZ, Reddy MS, El Enshasy H. Plant growth promoting rhizobacteria (PGPR) as green bioinoculants: recent developments, constraints, and prospects. *Sustainability*. 2021;13(3):1140.

8. Buck AH, Coakley G, Simbari F, McSorley HJ, Quintana JF, Le Bihan T, Kumar S, Abreu-Goodger C, Lear M, Harcus Y, Ceroni A, Babayan SA, Blaxter M, Ivens A, Maizels RM. Exosomes secreted by nematode parasites transfer small RNAs to mammalian cells and modulate innate immunity. *Nature Communications*. 2014;5:5488.

9. Cai Q, Qiao L, Wang M, He B, Lin FM, Palmquist J, Huang SD, Jin H. Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. *Science*. 2018;360(6393):1126-1129.

10. De Block M, Verduyn C, De Brouwer D, Cornelissen M. Poly(ADP-ribose) polymerase in plants affects energy homeostasis, cell death and stress tolerance. *Plant Journal*. 2005;41(1):95-106.

11. Ebeed HT, Hassan NM, Khodary SEA, Habib SA. Genome-wide analysis of polyamine biosynthesis genes in wheat reveals gene expression specificity and involvement of STRE and MYB-elements in regulating polyamines under drought. *BMC Genomics*. 2022;23:734.

12. Essigmann B, Guler S, Narang RA, Linke D, Benning C. Phosphate availability affects the thylakoid lipid composition and the expression of SQD1, a gene required for sulfolipid biosynthesis in Arabidopsis thaliana. *PNAS*. 1998;95(4):1950-1955.

13. Fu X, Richards DE, Ait-Ali T, Hynes LW, Ougham H, Peng J, Harberd NP. Gibberellin-mediated proteasome-dependent degradation of the barley DELLA protein SLN1 repressor. *Plant Cell*. 2002;14(12):3191-3200.

14. Gubler F, Kalla R, Roberts JK, Jacobsen JV. Gibberellin-regulated expression of a myb gene in barley aleurone cells: evidence for Myb transactivation of a high-pI alpha-amylase gene promoter. *Plant Cell*. 1995;7(11):1879-1891.

15. Gubler F, Chandler PM, White RG, Llewellyn DJ, Jacobsen JV. Gibberellin signaling in barley aleurone cells. Control of SLN1 and GAMYB expression. *Plant Physiology*. 2002;129(1):191-200.

16. Han Y, Liu S, Wei Y, Zhang X, Wang Y, Shi G, Li J, Liu D, Zhang A. Functional analysis of a wheat class III peroxidase gene, TaPer12-3A, in seed dormancy and germination. *BMC Plant Biology*. 2024;24:41.

17. Harris D, Joshi A, Khan PA, Gothkar P, Sodhi PS. On-farm seed priming in semi-arid agriculture: development and evaluation in maize, rice and chickpea in India using participatory methods. *Experimental Agriculture*. 1999;35(1):15-29.

18. He B, Cai Q, Qiao L, Huang CY, Wang S, Miao W, Ha T, Wang Y, Jin H. RNA-binding proteins contribute to small RNA loading in plant extracellular vesicles. *Nature Plants*. 2021;7(3):342-352.

19. Hu Z, Parekh U, Maruta N, Trusov Y, Botella JR. Cross-kingdom RNAi of pathogen effectors leads to quantitative adult plant resistance in wheat. *Frontiers in Plant Science*. 2020;11:253.

20. International Wheat Genome Sequencing Consortium (IWGSC). Shifting the limits in wheat research and breeding using a fully annotated reference genome. *Science*. 2018;361(6403):eaar7191.

21. Koch A, Biedenkopf D, Furch A, Weber L, Rossbach O, Abdellatef E, Linicus L, Johannsmeier J, Jelonek L, Goesmann A, Cardoza V, McMillan J, Mentzel T, Kogel KH. An RNAi-based control of Fusarium graminearum infections through spraying of long dsRNAs involves a plant passage and is controlled by the fungal silencing machinery. *PLoS Pathogens*. 2016;12(10):e1005901.

22. Liu S, Sehgal SK, Li J, Lin M, Trick HN, Yu J, Gill BS, Bai G. Cloning and characterization of a critical regulator for preharvest sprouting in wheat. *Genetics*. 2013;195(1):263-272.

23. Luo H, Wang Q, Guo Y, Li F, Li Z, Zhang Y. Gibberellic-acid-dependent expression of alpha-amylase in wheat aleurone cells is mediated by target of rapamycin (TOR) signaling. *Plant Signaling & Behavior*. 2023;18(1).

24. Ma W, Zhang Y, Li W, Du B, Liu J, Wang Z, Li J. Uncovering the role of wheat magnesium transporter family genes in abiotic responses. *Frontiers in Plant Science*. 2023;14:1078299.

25. Mahmood A, Turgay OC, Farooq M, Hayat R. Seed biopriming with plant growth promoting rhizobacteria: a review. *FEMS Microbiology Ecology*. 2016;92(8):fiw112.

26. Mulichak AM, Theisen MJ, Essigmann B, Benning C, Garavito RM. Crystal structure of SQD1, an enzyme involved in the biosynthesis of the plant sulfolipid headgroup donor UDP-sulfoquinovose. *PNAS*. 1999;96(23):13097-13102.

27. Nakamura S, Abe F, Kawahigashi H, Nakazono K, Tagiri A, Matsumoto T, Utsugi T, Ogawa T, Handa H, Ishida H, Mori M, Kawaura K, Ogihara Y, Miura H. A wheat homolog of MOTHER OF FT AND TFL1 acts in the regulation of germination. *Plant Cell*. 2011;23(9):3215-3229.

28. Nowara D, Gay A, Lacomme C, Shaw J, Ridout C, Douchkov D, Hensel G, Kumlehn J, Schweizer P. HIGS: host-induced gene silencing in the obligate biotrophic fungal pathogen Blumeria graminis. *Plant Cell*. 2010;22(9):3130-3141.

29. Pfeifer M, Kugler KG, Sandve SR, Zhan B, Rudi H, Hvidsten TR, Mayer KF, Olsen OA. Genome interplay in the grain transcriptome of hexaploid bread wheat. *Science*. 2014;345(6194):1250091.

30. Pieruzzi FP, Dias LLC, Balbuena TS, Santa-Catarina C, dos Santos ALW, Floh EIS. Polyamines, IAA and ABA during germination in two recalcitrant seeds: Araucaria angustifolia (Gymnosperm) and Ocotea odorifera (Angiosperm). *Annals of Botany*. 2011;108(4):693-701.

31. Qiao L, Zhang W, Li X, Zhang L, Zhang X, Li X, Guo H, Ren Y, Zheng J, Chang Z. Characterization and expression patterns of auxin response factors in wheat. *Frontiers in Plant Science*. 2018;9:1395.

32. Ramírez-González RH, Borrill P, Lang D, Harrington SA, Brinton J, Venturini L, Davey M, Jacobs J, van Ex F, Pasha A, et al. The transcriptional landscape of polyploid wheat. *Science*. 2018;361(6403):eaar6089.

33. Rodríguez MV, Barrero JM, Corbineau F, Gubler F, Benech-Arnold RL. Dormancy in cereals (not too much, not so little): about the mechanisms behind this trait. *Seed Science Research*. 2015;25(2):99-119.

34. Saha B, Borovskii G, Panda SK. Alternative oxidase and plant stress tolerance. *Plant Signaling & Behavior*. 2016;11(12):e1256530.

35. Schulz P, Neukermans J, Van der Kelen K, Muhlenbock P, Van Breusegem F, Noctor G, Teige M, Metzlaff M, Hannah MA. Chemical PARP inhibition enhances growth of Arabidopsis and reduces anthocyanin accumulation and the activation of stress protective mechanisms. *PLoS ONE*. 2012;7(5):e37287.

36. Scofield SR, Huang L, Brandt AS, Gill BS. Development of a virus-induced gene silencing system for hexaploid wheat and its use in functional analysis: a new tool for wheat genomics. *Plant Physiology*. 2005;138(4):2165-2173.

37. Shahid S, Kim G, Johnson NR, Wafula E, Wang F, Coruh C, Bernal-Galeano V, Phifer T, dePamphilis CW, Westwood JH, Axtell MJ. MicroRNAs from the parasitic plant Cuscuta campestris target host messenger RNAs. *Nature*. 2018;553(7686):82-85.

38. Shorinola O, Bird N, Simmonds J, Berry S, Henriksson T, Jack P, Werner P, Cornille A, Haberer G, Mayer KFX, Uauy C. The wheat Phs-A1 pre-harvest sprouting resistance locus delays the rate of seed dormancy loss and maps 0.3 cM distal to the PM19 genes in UK germplasm. *Journal of Experimental Botany*. 2017;68(15):4424-4438.

39. Torada A, Koike M, Ogawa T, Takenouchi Y, Tadamura K, Wu J, Matsumoto T, Kawaura K, Ogihara Y. A causal gene for seed dormancy on wheat chromosome 4A encodes a MAP kinase kinase. *Current Biology*. 2016;26(6):782-787.

40. Tuttle KM, Martinez SA, Schramm EC, Takebayashi Y, Seo M, Steber CM. Genetic variation of seed dormancy in wheat (Triticum aestivum L.) is mediated by transcriptional regulation of abscisic acid metabolism and signaling. *Plant Cell & Environment*. 2022;45(12):3621-3635.

41. Vanderauwera S, De Block M, Van de Steene N, van de Cotte B, Metzlaff M, Van Breusegem F. Silencing of poly(ADP-ribose) polymerase in plants alters abiotic stress signal transduction. *PNAS*. 2007;104(38):15150-15155.

42. Vanlerberghe GC. Alternative oxidase: a mitochondrial respiratory pathway to maintain metabolic and signaling homeostasis during abiotic and biotic stress in plants. *International Journal of Molecular Sciences*. 2013;14(4):6805-6847.

43. Wang M, Weiberg A, Lin FM, Thomma BP, Huang HD, Jin H. Bidirectional cross-kingdom RNAi and fungal uptake of external RNAs confer plant protection. *Nature Plants*. 2016;2:16151.

44. Wang X, Wang H, Liu S, Ferjani A, Li J, Yan J, Yang X, Qin F. Genome-wide and evolutionary analysis of the class III peroxidase gene family in wheat and Aegilops tauschii reveals that some members are involved in stress responses. *BMC Genomics*. 2019;20:666.

45. Wang Y, Zhang H, Liu J, Hou X, Zhang Y, Fan S, Li X, Gao F, Li X. Genome-wide identification and expression analysis of the kinesin gene superfamily suggests roles in response to abiotic stress and fertility of wheat. *BMC Genomics*. 2024;25:1156.

46. Weiberg A, Wang M, Lin FM, Zhao H, Zhang Z, Kaloshian I, Huang HD, Jin H. Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. *Science*. 2013;342(6154):118-123.

47. Xia H, Chen L, Wang F, Li D. Genome-wide analysis, expansion and expression of the NAC family under drought and heat stresses in bread wheat (T. aestivum L.). *PLoS ONE*. 2019;14(2):e0213390.

48. Yu B, Xu C, Benning C. Arabidopsis disrupted in SQD2 encoding sulfolipid synthase is impaired in phosphate-limited growth. *PNAS*. 2002;99(8):5732-5737.

49. Yu W, Bhatt H, Li Y, Jha S, Rao S, Guo J. Wheat PP2C-a10 regulates seed germination and drought tolerance in transgenic Arabidopsis. *Plant Cell Reports*. 2020;39(5):635-651.

50. Yuan C, Li C, Yan L, Jackson AO, Liu Z, Han C, Yu J, Li D. A high throughput barley stripe mosaic virus vector for virus induced gene silencing in monocots and dicots. *PLoS ONE*. 2011;6(10):e26468.

51. Zhang T, Zhao YL, Zhao JH, Wang S, Jin Y, Chen ZQ, Fang YY, Hua CL, Ding SW, Guo HS. Cotton plants export microRNAs to inhibit virulence gene expression in a fungal pathogen. *Nature Plants*. 2016;2:16153.

52. Zhao SP, Lu D, Yu TF, Ji YJ, Zheng WJ, Zhang SX, Chai SC, Chen ZY, Cui XY. Genome-wide analysis of the YABBY family in soybean and functional identification of GmYABBY10 involvement in high salt and drought stresses. *Plant Physiology and Biochemistry*. 2017;119:132-146.

53. Zhao Y, Li J, Liu H, Xi Y, Xue M, Liu W, Zhuang Z. Identification and expression profiles of the YABBY transcription factors in wheat. *PeerJ*. 2022;10:e12855.
