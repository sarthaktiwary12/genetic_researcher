# Bacterial Extracellular RNA-Mediated Reprogramming of Quinoa (*Chenopodium quinoa*) Seed Germination: Target Analysis, Mechanistic Models, and Validation Strategy

**Classification:** CONFIDENTIAL | **Prepared by:** Sarthak Tiwary | **Date:** February 2026 | **Version:** 1.0

**Evidence framework:** [Known] = published peer-reviewed data; [Inferred] = logical extrapolation from related systems; [Speculative] = hypothesis requiring validation.

---

## Executive Summary

This report presents a comprehensive analysis of 31 quinoa (*Chenopodium quinoa* Willd.) gene targets predicted to be downregulated by antisense-aligned bacterial extracellular small RNAs (esRNAs) from a bacterial preparation associated with improved seed germination. Quinoa seeds treated with this preparation exhibited measurably improved germination kinetics and seedling vigor relative to water controls. Small RNA sequencing of the bacterial preparation identified esRNA fragments that align antisense to *C. quinoa* gene models (AUR-series identifiers, Quinoa Genome Database, Kazusa Institute; cross-referenced against EnsemblPlants Release 62, ChenopodiumDB import), suggesting potential post-transcriptional downregulation of 31 transcripts.

Rigorous annotation enrichment — cross-referencing all 31 AUR gene identifiers against EnsemblPlants (Release 62), NCBI RefSeq, UniProtKB, Phytozome v13, TAIR, and primary published quinoa gene family studies — yielded **4 fully resolved targets** (12.9%): CqHAK5 (high-affinity K+ transporter), CqCNGC14 (cyclic nucleotide-gated Ca2+ channel), CqGUN4 (tetrapyrrole-binding chloroplast retrograde signal regulator), and CqBRL2/VH1-like (BRI1-family vascular/brassinosteroid LRR-RLK). An additional **24 targets are partially resolved** (77.4%) by structural annotation, conservation patterns, and protein size. Three targets remain completely unresolved (9.7%): two nontranslating CDS annotations (AUR62039771, AUR62034256) and one gene model absent from current public databases (AUR62045001).

Six critical annotation corrections were identified and are fully documented in this report. The most consequential: **AUR62003502 (CqBRL2/VH1-like) is a vascular/brassinosteroid signaling LRR-RLK, NOT a defense receptor-like kinase** as implied by the generic "LRR-RLK" designation — this changes interpretation from immune suppression toward a growth-promotion mechanism involving brassinosteroid signaling. Additionally, **AUR62021543 with 678 paralogs is the diagnostic signature of an NBS-LRR disease resistance gene** — a correction from "Unknown" to a high-confidence NBS-LRR family member. Three nontranslating CDS targets (AUR62012347, AUR62039771, AUR62034256) are flagged as annotation inconsistencies: if genuinely targeted by bacterial sRNAs, they may function as non-coding RNAs or pseudogene-derived transcripts rather than conventional mRNA targets.

The 31-target profile is enriched for **ion transport and homeostasis** (2 confirmed: CqHAK5, CqCNGC14), **hormone signaling** (CqBRL2/VH1 — brassinosteroid/auxin; CqCNGC14 — Ca2+/auxin), **chloroplast retrograde signaling** (CqGUN4), **Amaranthaceae-specific secondary metabolism** (betalain pathway CYP76AD-like locus), and **innate immune defense** (NBS-LRR candidate, two possible antimicrobial peptide candidates). This functional architecture is consistent with a coordinated bacterial strategy for reprogramming the germination-defense-dormancy axis of a host plant.

A key conceptual framework for understanding this target list is quinoa's unique biology as an **allotetraploid halophyte** (2n = 4x = 36, AABB genome, ~1.45 Gb, ~54,499 genes). Unlike *Brassica oleracea* (the subject of the companion broccoli report, which has the WGT triplication as its primary buffering context) and *Arabidopsis thaliana* (the canonical model), quinoa lacks any close model organism with comprehensive functional genetics. The closest characterized relative is *Beta vulgaris* (sugar beet), which shares the betalain pathway but lacks the allotetraploid genome structure. Critically, quinoa stores its primary reserves in a **perisperm** (maternally derived nucellus tissue, 2n), not an endosperm — making it the only major food crop whose seed architecture fundamentally differs from the canonical angiosperm model used in most germination biology literature.

Additional species-specific features with direct relevance to this analysis include: (1) quinoa's **epidermal bladder cells (EBCs)** — unique salt-sequestering structures whose function requires coordinated K+/Na+ transport, making HAK-family targeting particularly consequential; (2) **betalain biosynthesis** replacing anthocyanins as the primary antioxidant pigment system (found only in Caryophyllales, with no Arabidopsis functional model available); (3) the **saponin-coated seed coat** (testa) regulated by the master transcription factor TSARL1, which creates both a physical barrier to esRNA delivery and a chemical antimicrobial defense; (4) **expanded gene families** — 30 CqHAK, 34 CqCNGC, 21 CqAGO, 8 CqDCL, 11 CqRDR — reflecting halophytic adaptation and allotetraploid history; and (5) **100% seed-borne Bacillus spp. endophyte colonization**, establishing that bacterial-plant RNA communication during quinoa seed germination is not merely plausible but a normal biological occurrence whose regulatory dimensions are just beginning to be explored.

Among the annotated targets, the highest-priority candidates for explaining improved germination and vigor are: **(1) CqHAK5** (AUR62010943) — ranked CRITICAL for K+ accumulation driving radicle turgor pressure, with the important caveat that silencing a K+ importer presents a paradox requiring context-dependent resolution; **(2) CqBRL2/VH1-like** (AUR62003502) — vascular/brassinosteroid LRR-RLK whose downregulation may shift the BAK1 co-receptor availability from immune (PTI) to growth (brassinosteroid/BRI1) signaling; **(3) CqCNGC14** (AUR62044372) — Ca2+ channel whose downregulation could reduce ABA-reinforcing Ca2+ signaling, accelerating dormancy release; **(4) CqCYP76AD-like/betalain locus** (AUR62012347) — nontranslating CDS adjacent to functional CYP76AD1 gene, with potential resource reallocation from pigment synthesis to growth if genuine mRNA silencing occurs; and **(5) CqGUN4** (AUR62015391) — tetrapyrrole retrograde signaling regulator that interfaces with ABA/GA crosstalk during seedling establishment.

A distinctive and critical feature of the quinoa analysis compared to other crops in this series is the **HAK/KUP K+ transporter paradox**: silencing a canonical high-affinity K+ importer should impair radicle turgor and delay germination, yet this is the highest-confidence target with the most mechanistically clear assignment. Resolution requires considering: (a) context-dependent K+ efflux roles of specific HAK isoforms; (b) allotetraploid buffering by the 29 other CqHAK family members; (c) the possibility that the targeted isoform is a K+ exchanger that competes with Na+ influx rather than a pure K+ importer; and (d) the broader role of K+ homeostasis in halophyte seedling establishment where K+/Na+ ratio matters more than total K+ flux.

Two competing causal models are presented: (A) **Coordinated esRNA-Mediated Defense-Dormancy-Ion Knockdown** — bacterial sRNAs act as authentic cross-kingdom regulators that simultaneously suppress quinoa ion transport, chloroplast development, betalain antioxidant synthesis, and immune defense to collectively reprogram the germination-growth balance; and (B) **EPS-Mediated Osmopriming with RNA as Bystander** — the bacterial EPS matrix functions as an osmopriming hydrogel regardless of RNA content, and the observed gene targeting is functionally irrelevant. Seven discriminating experiments are proposed to distinguish these models.

The field has now established beyond reasonable doubt that cross-kingdom RNA interference is a bidirectional, widespread phenomenon in plant-microbe interactions [Known]. Weiberg et al. (2013) demonstrated fungal sRNA delivery into plant AGO complexes; Cai et al. (2018) showed plant EVs delivering sRNAs to suppress fungal virulence; He et al. (2021) elucidated the RNA-binding protein machinery loading sRNAs into extracellular vesicles; and Cai et al. (2025) identified both vesicular and non-vesicular pathways for sRNA exchange between plants and bacteria. The quinoa experimental system, with its seed-borne Bacillus endophytes and naturally occurring bacterial-plant RNA exchange, may represent one of the most biologically authentic instances of this phenomenon yet studied.

---

## 1. Introduction and Experimental Context

### 1.1 The Cross-Kingdom RNA Interference Paradigm

Cross-kingdom RNA interference (RNAi) — the transfer of small regulatory RNAs between organisms from different taxonomic kingdoms to modulate gene expression — has emerged over the past decade as a mechanistically verified and evolutionarily widespread component of plant-microbe interactions. The foundational studies established the following landmarks:

**Fungus-to-plant:** Weiberg et al. (2013) [Known] demonstrated that *Botrytis cinerea* produces small RNAs (Bc-siR3.1, Bc-siR3.2) that are delivered into *Arabidopsis thaliana* cells and loaded into the host AGO1/AGO4 machinery to silence host immunity genes, including *MPK1*, *MPK2*, and *PRE1*. This study established the "hijacking of host RNA interference pathways" model that is the conceptual foundation for the present investigation.

**Plant-to-fungus:** Cai et al. (2018) [Known] showed the reverse: *Arabidopsis* exports small RNAs (miR166, miR159) packaged in extracellular vesicles into *Botrytis cinerea* to silence the fungal DCL (dicer-like) genes *BcDCL1* and *BcDCL2*, thereby reducing fungal virulence. Wang et al. (2016) [Known] established bidirectional cross-kingdom RNAi in multiple plant-fungal systems including cotton-*Verticillium* and *Arabidopsis*-*Botrytis*.

**Parasite-to-host:** Shahid et al. (2018) showed that the parasitic plant *Cuscuta campestris* delivers microRNAs into host plant cells to downregulate host shoot growth.

**The RNA-binding protein machinery:** He et al. (2021) [Known] demonstrated that plant RNA-binding proteins (AGO1, HSCP70/90) are required for loading small RNAs into extracellular vesicles, establishing that sRNA cargo sorting into EVs is a specific, machinery-dependent process rather than passive RNA leakage.

**Non-vesicular extracellular RNA:** Zand Karimi et al. (2022) showed that the *Arabidopsis* apoplast contains both vesicular and non-vesicular sRNA-protein complexes, substantially expanding the potential mechanisms for extracellular RNA delivery and reception.

**Bacteria-to-plant:** Cai et al. (2025) identified non-vesicular extracellular sRNAs from *Arabidopsis* that direct gene silencing in the bacterial pathogen *Pseudomonas syringae*. The reciprocal direction — bacteria delivering sRNAs to silence plant genes — is the hypothesis under investigation here. Precedent for this direction includes tRNA-derived fragments from *Bradyrhizobium japonicum* that silence soybean genes to promote nodulation (Cai et al., 2019, Current Biology), establishing that N-fixing soil bacteria already use this communication channel.

**Spray-induced gene silencing (SIGS):** Koch et al. (2016) demonstrated that topically applied dsRNA enters plant cells and silences target genes — establishing the physical feasibility of exogenous RNA uptake. Nowara et al. (2010) demonstrated host-induced gene silencing (HIGS), validating that RNA molecules can traverse plant-pathogen interfaces. Betti et al. (2021) showed that exogenous microRNAs induce post-transcriptional gene silencing in *Arabidopsis*.

The cumulative evidence establishes that RNA-mediated cross-kingdom communication is a genuine biological phenomenon. The question for the present investigation is: are the bacterial esRNAs from the quinoa preparation functional cross-kingdom regulators, and do the 31 predicted target genes represent a coherent physiological program for germination enhancement?

### 1.2 Quinoa (*Chenopodium quinoa*) Seed Germination Biology

#### 1.2.1 Species Overview and Allotetraploid Genome

Quinoa (*Chenopodium quinoa* Willd.) is an allotetraploid crop (2n = 4x = 36, AABB genome) from the Andean highlands of South America, now cultivated globally for its exceptional nutritional profile. The genome (~1.45 Gb) arose from hybridization between a *C. pallidicaule*-related A-genome diploid and a *C. suecicum*-related B-genome diploid approximately 3.3–6.3 million years ago [Known; Kolano et al. 2016]. The chromosome-scale reference genome contains ~54,499 protein-coding genes [Known; Rey et al. 2023], organized across 18 chromosomes (9A + 9B), with 64.5% repetitive sequence and 192 microRNA genes [Known; Jarvis et al. 2017; Yasui et al. 2016].

The allotetraploid structure has direct implications for interpreting the esRNA target list: most genes in quinoa exist as homeologous pairs (A-genome and B-genome copies), potentially providing functional buffering against single-homeolog silencing. However, quinoa also underwent extensive lineage-specific gene family expansions — particularly in ion transport (30 CqHAK, 34 CqCNGC), small RNA machinery (21 CqAGO, 8 CqDCL, 11 CqRDR), and secondary metabolism (17+ CqCYP76AD, 8 CqDODA) — that go beyond mere tetraploid doubling and reflect genuine adaptive expansion in response to halophytic and high-altitude Andean environments.

#### 1.2.2 The Perisperm — A Unique Reserve Tissue

Unlike all other major crop species used in this report series (broccoli, maize, soybean, wheat), quinoa stores its primary carbohydrate reserves in the **perisperm** — a maternally derived tissue originating from the nucellus of the ovule (diploid, 2n) [Known; Prego et al. 1998]. This tissue is not a product of double fertilization, is genetically identical to the maternal plant, and undergoes developmentally programmed cell death during seed maturation [Known; López-Fernández and Maldonado 2013].

The functional analog of the classic endosperm is retained only as a small micropylar endosperm cap (two cell layers) at the radicle tip. This cap functions as the primary mechanical and physiological barrier to radicle emergence — analogous in function to the micropylar endosperm cap in tomato and Brassicaceae [Known]. Weakening of this cap by GA-induced cell wall-loosening enzymes (expansins, XTHs, pectinases) is the rate-limiting step for germination [Inferred from Arabidopsis model; quinoa-specific kinetics not fully characterized].

The perisperm/micropylar endosperm architecture means that: (a) ABA-mediated dormancy must be broken via the embryo-perisperm-micropylar endosperm communication axis, not the embryo-endosperm axis of canonical models; (b) Ca2+/K+ signaling during imbibition occurs in the context of this maternal-offspring tissue interface; and (c) betalain antioxidant protection operates in the embryo and seed coat rather than in a thick starchy endosperm.

#### 1.2.3 ABA/GA Hormonal Balance in Quinoa Germination

The ABA/GA hormonal balance is the master switch governing quinoa germination, as in all angiosperms. Quinoa-specific findings [Known]:

- ABA levels peak at 12 hours post-imbibition (~6.198 ng/g dry weight) and then sharply decline; this decline correlates with germination rate [Zhao et al. 2022]
- Quinoa encodes 20 CqPYL ABA receptors, 13 CqSnRK2 kinases, and CqSnRK2.12 overexpression in Arabidopsis enhances ABA sensitivity [Known; genome-wide family studies]
- GA biosynthesis is controlled by 18 CqGAox genes; GA promotes germination under salt stress and three CqGID1 genes mediate GA perception, with CqGID1b1 and CqGID1b2 being highly expressed during germination [Known]
- Nitrate signaling via CqNLP1 (homolog of AtNLP8) activates CYP707A2 to catabolize ABA, connecting nitrogen sensing to dormancy release [Known; nitrate-ABA interaction data]
- JA peaks at 12h (3.812 ng/g) and then declines; ETH increases progressively, consistent with ETH-ABA antagonism promoting germination

#### 1.2.4 Salt Stress and Ion Homeostasis During Germination

Quinoa is a halophyte capable of germinating at 300–400 mM NaCl — salt concentrations that completely inhibit germination of glycophyte crops [Known; Orsini et al. 2011]. The salt tolerance strategy during germination involves:

- K+/Na+ homeostasis via CqHKT1 (Na+ channel), CqSOS1 (Na+/H+ antiporter), and CqNHX (vacuolar Na+/H+ exchanger) [Known; Böhm et al. 2018]
- Expanded HAK/KUP K+ transporter family (30 members vs ~13 in Arabidopsis) for K+ acquisition under saline conditions [Known; Ren et al. 2023]
- Epidermal bladder cells (EBCs) sequestering Na+ from leaf cells — unique structures requiring coordinated K+/Na+ transport from the earliest stages of seedling development [Known; Böhm et al. 2018]
- Expanded CNGC family (34 members vs 20 in Arabidopsis) for diversified Ca2+ signaling under multiple stress types [Known; Zhang et al. 2024/2025]

#### 1.2.5 Betalain Antioxidant System

Quinoa and all Caryophyllales produce **betalains** in place of anthocyanins — making the entire anthocyanin biosynthetic literature inapplicable to quinoa's antioxidant defense. The betalain pathway proceeds from L-tyrosine through CYP76AD (tyrosinase/L-DOPA oxidase) and DODA (L-DOPA 4,5-dioxygenase) to betalamic acid, which then condenses with amino acids (betaxanthins) or undergoes glucosylation (betacyanins) [Known; Brockington et al. 2015; Timoneda et al. 2019].

Betalain biosynthesis genes are highly expressed at 64 hours of germination coinciding with hypocotyl elongation, and betalain genes respond to cold stress during germination — consistent with a stress-protective role [Known; Nagatoshi/Lv et al. 2023]. Betalains directly scavenge superoxide, hydrogen peroxide, and singlet oxygen, replacing the ROS-buffering function that anthocyanins serve in most other angiosperm families.

#### 1.2.6 Saponin Seed Coat

A distinctive chemical feature of quinoa seeds is the **triterpenoid saponin** (TS) coating of the seed coat (testa), reaching up to 86% of total seed saponin content [Known; Fiallos-Jurado et al. 2016]. The master regulator TSARL1 (a bHLH TF) controls saponin accumulation specifically in seeds [Known]. Saponins are amphipathic molecules with membrane-disrupting activity that protect against herbivores, insects, and soil microbes.

In the context of the esRNA hypothesis, the saponin layer represents both a potential barrier to esRNA/EV uptake and, paradoxically, a facilitator — saponins' detergent-like properties could promote membrane fusion between bacterial outer membrane vesicles (OMVs) and seed coat membranes upon imbibition-driven hydration.

### 1.3 Experimental Design

Quinoa seeds were treated with a bacterial extracellular preparation containing EPS and associated RNA. Control seeds were soaked in water. Petri dish germination assays demonstrated improved germination rate and seedling vigor in treated seeds. Small extracellular RNA was extracted from the preparation, sequenced, and aligned antisense against the *C. quinoa* transcriptome (AUR-series gene models, Jarvis 2017 genome assembly), yielding 31 predicted target transcripts.

Quinoa's 100% colonization by seed-borne Bacillus spp. endophytes (Pankievicz et al. 2016) establishes biological plausibility: bacterial-plant RNA communication during quinoa germination is not an exotic experimental artifact but may be a component of the normal quinoa seed microbiome interaction.

---

## 2. Annotation Enrichment, Corrections, and Genomic Context

### 2.1 Annotation Corrections

Cross-referencing all 31 AUR gene identifiers identified six critical annotation flags:

| # | AUR Gene ID | Original Annotation | Corrected Annotation | Severity | Evidence |
|---|-------------|---------------------|----------------------|----------|----------|
| 1 | AUR62012347 | CYP76AD1-like or DODA-like (functional enzyme) | **Nontranslating CDS — likely CYP76AD-family pseudogene or tandem duplicate of functional CqCYP76AD1 (AUR62012346)** | HIGH | EnsemblPlants annotates as "Nontranslating CDS" with no protein product. Adjacent locus AUR62012346 encodes functional CqCYP76AD1. Cai et al. (2025, Stress Biology) documented structural variation restoring function in specific cultivar genomes. |
| 2 | AUR62039771 | Unknown | **Nontranslating CDS (2,096 bp) — possible lncRNA or pseudogene; no protein product** | MEDIUM | Biotype: Nontranslating CDS per EnsemblPlants. May function as regulatory non-coding RNA; mechanism of sRNA targeting would differ from canonical mRNA silencing. |
| 3 | AUR62034256 | Unknown | **Nontranslating CDS (714 bp) — putative smORF or pseudogene; no protein product** | MEDIUM | Third nontranslating target (9.7% of 31 targets) — above-chance representation warranting systematic evaluation of lncRNA targeting. |
| 4 | AUR62045001 | Unknown | **Not present in EnsemblPlants (Release 62, ChenopodiumDB import) — gene model unverifiable from public databases** | HIGH | Identifier does not appear in EnsemblPlants, Phytozome v13, or public quinoa databases. May be from an alternative annotation pipeline or AUR ID numbering scheme not imported into EnsemblPlants. Original Phytozome v1.0 GFF must be queried directly. |
| 5 | AUR62021543 | Unknown | **Candidate NBS-LRR resistance gene (CC-NBS-LRR class based on 603 aa size and 678 paralogs)** | HIGH | 678 paralogs is diagnostically characteristic of NBS-LRR tandem array expansion. Only 45 orthologs (vs. 678 paralogs) is additionally characteristic of fast-evolving NLR genes. Ge et al. (2024) identified 183 NBS-LRR proteins in quinoa. NLR-parser analysis recommended for confirmation. |
| 6 | AUR62003502 | LRR-RLK (defense-implied) | **CqBRL2/VH1-like (BRI1-family, vascular/brassinosteroid signaling) — primary function is vascular differentiation and BR/auxin crosstalk, NOT immune defense** | CRITICAL | Arabidopsis ortholog AT2G01950 = BRL2/VH1 (BRI1 Leucine-Rich Receptor-like Kinase 2/Vascular Highway 1). Clay and Nelson 2005; Ceserani et al. 2009 (PMC2793540) establish vascular function. The "Fragment" designation in quinoa annotation suggests partial assembly. Defense function is incorrect for this BRI1 subfamily. |

### 2.2 Annotation Statistics

| Category | Count | % |
|----------|-------|---|
| Fully resolved (confirmed gene name and function) | 4 | 12.9% |
| Partially resolved (structural + candidate function) | 24 | 77.4% |
| Completely unresolved | 3 | 9.7% |

Fully resolved targets (4): CqHAK5 (AUR62010943), CqCNGC14 (AUR62044372), CqGUN4 (AUR62015391), CqBRL2/VH1-like (AUR62003502).

Partially resolved targets with MEDIUM or higher confidence (4): Betalain/CYP76AD-like (AUR62012347), NBS-LRR candidate (AUR62021543), defensin/CRP candidate (AUR62040122), LTP/antimicrobial candidate (AUR62035900).

### 2.3 Allotetraploid Genome Considerations

Unlike the *Brassica oleracea* whole-genome triplication (WGT; three subgenomes LF, MF1, MF2), quinoa's polyploidy is an allotetraploidy with exactly two subgenomes (A and B). This creates a distinct buffering pattern: each gene typically has exactly two copies (homeologs), not three. The functional consequences for esRNA-mediated silencing are:

- **Silencing specificity:** If an esRNA targets a sequence conserved between A and B homeologs, both copies are silenced. If the esRNA targets a subgenome-specific sequence, only one homeolog is silenced and the other compensates. Given that 3.3–6.3 million years of divergence separates the A and B subgenomes, many gene sequences will have diverged sufficiently for homeolog-specific targeting to occur.

- **B-subgenome dynamism:** The B subgenome is more structurally dynamic and expanded than the A subgenome [Known; Rey et al. 2023], including a 71.7%-pericentromeric inversion on Cq3B. This differential subgenome architecture may mean B-subgenome gene copies are more frequently targeted by esRNAs if their sequences have diverged more from the bacterial genome's antisense sRNA pool.

- **Family expansion beyond polyploidy:** The 30 CqHAK, 34 CqCNGC, and 17+ CqCYP76AD members represent genuine tandem duplication expansions, not just tetraploid doubling. For CqHAK5 specifically, even if the one targeted isoform is silenced, 29 other family members exist — though their expression patterns, tissue specificity, and K+ transport kinetics differ substantially from the high-affinity root-expressed CqHAK5.

---

## 3. Functional Category Distribution

### 3.1 Overview

| Category | Count | % | Key Members |
|----------|-------|---|-------------|
| Unknown/Uncharacterized | 18 | 58.1% | Multiple partially-resolved unknowns |
| Ion Transport | 2 | 6.5% | CqHAK5, CqCNGC14 |
| Hormone Signaling/LRR-RLK | 1 | 3.2% | CqBRL2/VH1-like |
| Chloroplast/Retrograde Signaling | 1 | 3.2% | CqGUN4 |
| Betalain/Secondary Metabolism | 1 | 3.2% | CYP76AD-like (nontranslating) |
| Disease Resistance / Innate Immunity | 1-3 | 3.2–9.7% | NBS-LRR candidate, 2 antimicrobial peptide candidates |
| Possible Transcription Factors | 1 | 3.2% | AUR62014700 (88 paralogs; possible WRKY/MYB/NAC) |
| Lineage-Specific / Amaranthaceae | 2 | 6.5% | AUR62011287 (4 orthologs), AUR62040122 (1 ortholog, 18 paralogs) |
| Nontranslating CDS / Pseudogenes | 3 | 9.7% | AUR62012347, AUR62039771, AUR62034256 |
| Not in Database | 1 | 3.2% | AUR62045001 |

### 3.2 Pathway Enrichment Analysis

**Ion transport and homeostasis (overrepresented):** Two of four confirmed targets (50% of confirmed) belong to ion transport — CqHAK5 (K+ transport) and CqCNGC14 (Ca2+ channel). This overrepresentation relative to genome-wide expectation is statistically notable and biologically coherent: K+ and Ca2+ are the two most critical cations for germination, with K+ driving radicle turgor pressure and Ca2+ serving as a second messenger for ABA/auxin signaling. Co-targeting of both systems by bacterial esRNAs would have synergistic effects on seedling ion balance [Inferred].

**Hormone signaling (notable):** CqCNGC14 mediates Ca2+-dependent auxin responses, and CqBRL2/VH1 is a BRI1-family brassinosteroid receptor. Both brassinosteroids and auxin promote germination by antagonizing ABA signaling. The indirect targeting of hormone signaling via ion channels and receptor kinases represents a sophisticated regulatory strategy [Inferred].

**Chloroplast/retrograde signaling (notable):** CqGUN4 controls tetrapyrrole biosynthesis and retrograde plastid-to-nucleus signaling. During the dark-to-light transition at seedling emergence, this pathway is critical for preventing lethal singlet oxygen accumulation from uncontrolled chlorophyll precursor buildup [Known; Larkin et al. 2003]. GUN4 also links chloroplast redox state to ABA signaling via the PAP/SAL1/XRN retrograde pathway [Known; Arabidopsis model].

**Immune defense (candidate):** The NBS-LRR candidate (AUR62021543) and two antimicrobial peptide candidates (AUR62040122, AUR62035900) represent a potential immune suppression cluster. If confirmed, this pattern would parallel the defense downshift observed in broccoli (CRK26, CRK29) and would be consistent with the bacterial strategy of silencing host innate immunity to enable colonization [Speculative; requires NLR-parser confirmation].

**Betalain pathway (Amaranthaceae-specific):** The CYP76AD-like nontranslating locus represents the only crop-specific secondary metabolic pathway in the target list. Its ambiguous translational status (nontranslating CDS) means the mechanism of bacterial sRNA action — if targeting genuine lncRNA function rather than mRNA translation — would be distinct from canonical RISC-mediated silencing [Speculative].

---

## 4. Ranked Target Table

### Tier 1: Highest Priority (Mechanistically Sound, Well-Supported)

| Rank | Gene ID | Annotation | At Ortholog | Function | Priority |
|------|---------|-----------|------------|----------|----------|
| 1 | AUR62010943 | **CqHAK5** (K+ high-affinity transporter) | AT4G13420 (AtHAK5) | K+ acquisition for radicle turgor pressure; K+/Na+ discrimination in halophyte context; activated by CIPK23/CBL1/9 complex | CRITICAL |
| 2 | AUR62003502 | **CqBRL2/VH1-like** (LRR-RLK, BRI1-family) | AT2G01950 (BRL2/VH1) | Vascular development; brassinosteroid/auxin crosstalk; BAK1 co-receptor competition between immune and growth complexes | HIGH |
| 3 | AUR62044372 | **CqCNGC14** (Ca2+ channel) | AT2G24610 (AtCNGC14) | Ca2+ influx for root gravitropism and auxin response; ABA-reinforcing Ca2+ signaling; Ca2+ oscillations in root hair growth | HIGH |
| 4 | AUR62012347 | **CqCYP76AD-like** (nontranslating CDS, betalain locus) | CYP76-like (no direct At ortholog; betalain pathway absent in At) | Betalain antioxidant capacity during imbibition; resource reallocation from pigment to growth (if nontranslating locus has regulatory role) | HIGH |
| 5 | AUR62015391 | **CqGUN4** (tetrapyrrole-binding, chloroplastic) | AT3G59400 (GUN4/Q9LX31) | Mg-chelatase regulation; chloroplast-to-nucleus retrograde signaling; ABA crosstalk via PAP pathway; plastid biogenesis during de-etiolation | MEDIUM-HIGH |

### Tier 2: High Priority (Strong Mechanistic Basis for Defense/Immunity)

| Rank | Gene ID | Annotation | Evidence | Priority |
|------|---------|-----------|---------|----------|
| 6 | AUR62021543 | **Candidate NBS-LRR resistance gene** (CC-NBS-LRR class) | 678 paralogs diagnostic for NBS-LRR family; 603 aa; 45 orthologs; Ge et al. 2024 identified 183 NBS-LRRs in quinoa | MEDIUM |
| 7 | AUR62040122 | **Candidate antimicrobial CRP** (defensin-type) | 117 aa; 1 ortholog, 18 paralogs — Amaranthaceae-specific expansion; size fits defensin precursor (~100-130 aa) | LOW-MEDIUM |
| 8 | AUR62035900 | **Candidate LTP or antimicrobial peptide** | 105 aa; 38 paralogs — fits LTP (Lipid Transfer Protein) or defensin-type cysteine-rich peptide family | LOW-MEDIUM |

### Tier 3: Moderate Priority (Possibly Transcription Factor or Signaling)

| Rank | Gene ID | Annotation | Evidence | Priority |
|------|---------|-----------|---------|----------|
| 9 | AUR62014700 | **Possible transcription factor** (WRKY/MYB/NAC class) | 361 aa; 185 orthologs; 88 paralogs — fits quinoa WRKY (92 members) or NAC (100+ members) family | LOW-MEDIUM |
| 10 | AUR62011287 | **Lineage-specific protein** (Amaranthaceae-specific candidate) | 335 aa; only 4 orthologs; 1 paralog — strong candidate for Amaranthaceae-specific function (saponin accessory? betalain pathway?) | LOW |

### Tier 4: Lower Priority (Unknown, Structural Data Only)

Remaining 21 targets (AUR62043174, AUR62027225, AUR62031820, AUR62006498, AUR62018498, AUR62025094, AUR62033668, AUR62008816, AUR62037200, AUR62029415, AUR62042100, AUR62023678, AUR62016845, AUR62038512, AUR62020100, AUR62007329, AUR62019623, AUR62041888, plus unresolved AUR62039771, AUR62034256, AUR62045001) have LOW or NO confidence function assignments due to insufficient annotation data. Several show distinctive conservation patterns suggesting important conserved functions: AUR62033668 (400 orthologs, 16 paralogs — highly conserved multi-gene family), AUR62019623 (278 orthologs — near-universal plant conservation), and AUR62007329 (263 orthologs — universal plant conservation). These may encode essential housekeeping or regulatory proteins whose downregulation could have broad physiological effects not captured by current annotation.

---

## 5. Mechanistic Theme Analysis

### 5.1 Theme 1: Ion Homeostasis — K+ and Ca2+ Transport Coordination

**Targets involved:** CqHAK5 (AUR62010943), CqCNGC14 (AUR62044372)

Potassium is the dominant inorganic osmolyte in plant cells (100–200 mM cytoplasmic concentration) and the primary driver of turgor pressure during radicle cell expansion. During seed imbibition and germination, K+ accumulates rapidly in radicle cells, lowering their water potential and driving the osmotic water influx required for cell expansion and mechanical breakthrough of the micropylar endosperm cap [Known; Arabidopsis model; Rubio et al. 2010]. CqHAK5, as the primary high-affinity K+ uptake transporter (analogous to AtHAK5 which is essential for seedling establishment below ~20 µM external K+), is the molecular engine of this K+ accumulation phase [Known; Nieves-Cordones et al. 2010].

**The HAK/KUP paradox:** Silencing a K+ importer during germination should theoretically impair radicle turgor and delay emergence — the opposite of improved germination. This is the central paradox of the quinoa target list. Resolution requires considering:

(a) **Context-dependent efflux roles:** Some HAK/KUP members mediate K+ efflux under specific conditions, particularly under high-Na+ environments where maintaining the K+/Na+ ratio requires controlled K+ redistribution. If the targeted CqHAK5 isoform functions as a K+ efflux conduit under the saline conditions typical of quinoa germination, silencing it would INCREASE net K+ retention [Inferred].

(b) **Na+ competition:** Under saline conditions, Na+ competes with K+ at HAK transporter active sites, and some HAK isoforms have measurable Na+ co-transport activity. Silencing a HAK isoform with significant Na+ permeability could improve the K+/Na+ ratio without reducing total K+ accumulation [Speculative].

(c) **Allotetraploid buffering:** With 30 CqHAK family members, silencing one isoform may be functionally compensated by others. The unique contribution of the targeted CqHAK5 to germination-stage K+ uptake needs to be determined empirically.

(d) **Subgenome-specific targeting:** If the bacterial sRNA targets only the A-subgenome homeolog of CqHAK5, the B-subgenome copy maintains function — producing a partial reduction in K+ flux rather than complete loss.

CqCNGC14 mediates Ca2+ influx in response to auxin, contributing to the rapid Ca2+ and pH signals that mediate auxin growth responses in roots [Known; Shih et al. 2015]. Ca2+ oscillations driven by CNGC14, CNGC6, and CNGC9 are required for root hair tip growth [Known; Brost et al. 2019]. From an ABA standpoint, Ca2+ is a positive co-signal for ABA pathways — Ca2+-dependent protein kinases (CDPKs) phosphorylate and activate SnRK2 kinases, reinforcing ABA signaling. Silencing CqCNGC14 would therefore reduce ABA-reinforcing Ca2+ fluxes, potentially accelerating the ABA-to-GA hormonal transition required for dormancy release [Inferred].

The co-targeting of both K+ (via CqHAK5) and Ca2+ (via CqCNGC14) channels suggests coordinated modulation of the seed ionic environment by bacterial esRNAs — a pattern consistent with deliberate manipulation of the germination-relevant ion signaling network [Speculative but coherent].

### 5.2 Theme 2: Defense-Growth Tradeoff — BAK1 Co-Receptor Competition

**Targets involved:** CqBRL2/VH1-like (AUR62003502), NBS-LRR candidate (AUR62021543), antimicrobial peptide candidates (AUR62040122, AUR62035900)

The **BAK1 co-receptor competition** model is the central molecular mechanism through which brassinosteroid signaling and immune signaling are integrated [Known; Chinchilla et al. 2007; Lozano-Durán and Zipfel 2015]. BAK1 is required as a co-receptor for both FLS2 (bacterial flagellin receptor, PTI activation) and BRI1 (brassinosteroid receptor, growth promotion). When PTI is active, the FLS2-BAK1 complex is occupied, limiting the availability of free BAK1 for BRI1. Conversely, brassinosteroid activation of BRI1-BAK1 negatively regulates immune signaling.

CqBRL2/VH1-like is a member of the BRI1 superfamily (AT2G01950 ortholog), distinct from BRI1 itself but sharing the BRI1-clade LRR domain architecture. VH1/BRL2 loss-of-function in Arabidopsis causes discontinuous phloem and altered responses to both auxin and brassinosteroids [Known; Ceserani et al. 2009]. In the context of germination, brassinosteroids promote ABA catabolism and GA synthesis, accelerating dormancy release [Known]. Downregulation of CqBRL2 could have complex effects — but in the context of the BAK1 competition model, reducing any BRI1-family receptor that competes for BAK1 binding could affect the balance of growth vs. immune signaling [Speculative].

The NBS-LRR candidate (AUR62021543) represents a direct immune receptor target. NLR proteins mediate Effector-Triggered Immunity (ETI) — the second tier of the plant immune system [Known; Jones and Dangl 2006]. Quinoa encodes 183 NBS-LRR proteins [Known; Ge et al. 2024], reflecting its allotetraploid genome and active pathogen pressure in Andean environments. Bacterial esRNA targeting of an NBS-LRR gene could suppress ETI activation against seed-borne bacteria, enabling deeper colonization of the germinating seedling [Speculative].

The two small antimicrobial peptide candidates (AUR62040122: 117 aa, 1 ortholog, 18 paralogs; AUR62035900: 105 aa, 38 paralogs) fit the size and family-expansion patterns of defensins or lipid transfer proteins (LTPs). Both are present in seed coats and early seedling tissues; their antimicrobial activity against soil bacteria could represent a direct cost to bacteria attempting colonization. Silencing these by bacterial esRNAs would reduce antimicrobial peptide concentrations in the germination zone, potentially benefiting the bacteria [Speculative; requires experimental confirmation of family membership].

### 5.3 Theme 3: Betalain/Antioxidant Pathway — ROS Buffering and Resource Reallocation

**Targets involved:** CqCYP76AD-like locus (AUR62012347)

Betalains are the primary non-enzymatic antioxidants in quinoa seeds and seedlings [Known; Timoneda et al. 2019]. The imbibition-associated ROS burst (within minutes of water uptake) creates an oxidative challenge that betalains are ideally positioned to buffer — they directly scavenge superoxide, H2O2, and singlet oxygen, with TEAC (Trolox Equivalent Antioxidant Capacity) values among the highest of natural pigments [Known].

The nontranslating annotation of AUR62012347 raises two mechanistic possibilities:

**Possibility 1 (lncRNA function):** If AUR62012347 functions as a lncRNA in cis-regulation of the adjacent CqCYP76AD1 locus (AUR62012346), bacterial sRNA targeting of this noncoding transcript could indirectly suppress CqCYP76AD1 expression. This would be a genuinely novel and sophisticated form of cross-kingdom gene regulation — bacterial sRNA silencing of a plant regulatory non-coding RNA to indirectly suppress a biosynthetic enzyme [Speculative].

**Possibility 2 (cultivar-specific translation):** Cai et al. (2025, Stress Biology) documented that a structurally similar locus (Cqu0091301) was restored to full protein-coding function by a ~4-kb genomic insertion absent in the reference genome. If AUR62012347 is translatable in specific quinoa cultivars but annotated as nontranslating in the reference genome, bacterial sRNA targeting could directly suppress a functional CYP76AD enzyme [Speculative; requires cultivar-specific genome analysis].

**Resource reallocation hypothesis:** If betalain biosynthesis is reduced by esRNA targeting, the nitrogen atoms contained in betalamic acid (the nitrogen-containing chromophore) and the tyrosine/L-DOPA intermediates could be redirected toward protein synthesis — a significant resource shift during the narrow germination window where amino acid demand for cell division proteins is high [Inferred]. The betalain pathway is metabolically expensive: tyrosine must be hydroxylated by CYP76AD (requiring NADPH and O2), then converted to betalamic acid by DODA, then condensed with amino acids. All these substrates and cofactors could serve anabolic purposes if the pathway is dampened.

The risk of reduced betalain antioxidant capacity is real but may be partially compensated by quinoa's enzymatic antioxidant defense (SOD, CAT, APX, GST), which is independently inducible during germination [Known; antioxidant studies in quinoa seedlings].

### 5.4 Theme 4: Chloroplast Retrograde Signaling — GUN4 and ABA Crosstalk

**Targets involved:** CqGUN4 (AUR62015391)

GUN4 (Genomes UNcoupled 4) regulates Mg-chelatase activity in the chlorophyll biosynthesis branch of tetrapyrrole metabolism [Known; Larkin et al. 2003]. By binding both protoporphyrin IX (Proto IX) and Mg-protoporphyrin IX (Mg-Proto IX), GUN4 activates the CHLD-CHLH-CHLI complex and channels tetrapyrroles toward chlorophyll rather than heme. In gun4 mutants, Mg-chelatase activity is reduced, Proto IX accumulates, and plastid-to-nucleus retrograde signaling is disrupted — specifically, gun mutants fail to downregulate nuclear photosynthesis genes when chloroplast biogenesis is disrupted.

The germination-relevance of GUN4 operates via two parallel pathways:

**Pathway 1 — Tetrapyrrole-retrograde/ABA interaction:** The chloroplast retrograde signal metabolite PAP (3'-phosphoadenosine 5'-phosphate) inhibits nuclear XRN exoribonucleases, which stabilizes specific mRNAs and enhances ABA sensitivity, thereby inhibiting germination [Known; Arabidopsis model]. GUN4 downregulation would reduce chlorophyll biosynthesis flux, potentially altering the retrograde signal pool and indirectly modulating ABA sensitivity [Inferred; Arabidopsis model extrapolated to quinoa].

**Pathway 2 — De-etiolation and seedling establishment:** Chloroplast biogenesis during the dark-to-light transition at seedling emergence requires precise coordination between nuclear and plastid gene expression. If CqGUN4 is downregulated during bacterial esRNA treatment, chlorophyll biosynthesis will be transiently impaired, delaying photosynthetic capacity acquisition [Inferred]. This is a cost (seedlings depend longer on seed reserves) but may be acceptable if germination rate itself is accelerated.

**CHLH/GUN5 alternative:** The annotation "tetrapyrrole-binding protein, chloroplastic" could also describe CHLH/GUN5, the Mg-chelatase H subunit that was identified as an ABA receptor in guard cells [Known; Shen et al. 2006]. If AUR62015391 encodes CHLH/GUN5 rather than GUN4, its downregulation would directly reduce ABA receptor capacity — a much more proximal mechanism for germination promotion [Speculative; requires sequence confirmation to distinguish GUN4 from GUN5/CHLH].

### 5.5 Theme 5: Immune Suppression — NBS-LRR and Defense Peptide Targeting

**Targets involved:** AUR62021543 (candidate NBS-LRR), AUR62040122 (candidate defensin/CRP), AUR62035900 (candidate LTP/antimicrobial)

NBS-LRR proteins (also called NLRs) are the largest class of plant immune receptors, mediating ETI (Effector-Triggered Immunity) upon detection of pathogen-derived effector proteins [Known; Jones and Dangl 2006]. Quinoa's 183 NBS-LRR proteins [Known] represent an expanded immune receptor repertoire consistent with high pathogen pressure in Andean environments. If seed-borne bacteria express effector-like proteins (as do many Bacillus rhizobacteria that interact with plant immune systems), silencing an NLR gene via esRNA could prevent ETI activation and allow deeper root colonization [Speculative].

The seed antimicrobial peptides — defensins, lipid transfer proteins (LTPs), thionins — are first-line defenders against soil pathogens during the germination window [Known; multiple crop species]. LTPs (~100 aa, cysteine-rich) are among the most abundant proteins in many seeds. A family with 38 paralogs at 105 aa (AUR62035900) is strongly consistent with the LTP superfamily or a related cysteine-rich peptide family. If bacterial esRNAs silence multiple paralogs of this family, overall antimicrobial peptide concentrations in the germination zone decrease, creating a more permissive environment for bacterial colonization [Speculative].

This immune suppression theme represents an asymmetric cost-benefit: costs to the plant (reduced pathogen defense) may be acceptable in the specific context of colonization by beneficial, nitrogen-fixing, or growth-promoting Bacillus endophytes that have co-evolved with quinoa seeds — a context where reducing ETI against a specific microbial partner is adaptive rather than parasitic [Speculative; evolutionary framing].

### 5.6 Theme 6: Halophyte Adaptation — EBCs, K+/Na+ Discrimination, and Expanded Gene Families

**Targets involved:** CqHAK5 (AUR62010943), CqCNGC14 (AUR62044372), multiple unknown halophyte-specific candidates

Quinoa's halophyte biology creates a germination context fundamentally different from glycophyte crops. The following halophyte-specific considerations apply to the esRNA target list:

**EBC system context:** Epidermal bladder cells (EBCs), unique to quinoa and related Chenopodioideae, require active Na+ sequestration from leaf cells, driven by CqHKT1.2 (Na+ channel) and CqClc-c (Cl- vacuolar transporter) [Known; Böhm et al. 2018]. This system is not yet functional in germinating seeds or very young seedlings, making the early germination window particularly vulnerable to K+/Na+ imbalance. Bacterial esRNA targeting of CqHAK5 during this pre-EBC phase of development could have disproportionate effects compared to later vegetative stages.

**Expanded gene families as potential redundancy buffers:** The quinoa small RNA machinery (21 CqAGO, 8 CqDCL, 11 CqRDR) is expanded relative to Arabidopsis (10 AGO, 4 DCL, 6 RDR). This expanded silencing machinery means the plant has enhanced capacity to respond to exogenous RNAs — either by processing them into secondary siRNAs that amplify silencing or by activating immunity-related RNA-silencing pathways. The expanded AGO repertoire may mean bacterial esRNAs could be loaded into multiple AGO complexes with different silencing outcomes [Inferred].

**ABA hypersensitivity in halophyte context:** The quinoa genome contains expanded ABA biosynthesis, transport, and signaling genes [Known; Jarvis et al. 2017], and quinoa shows ABA hyperresponsiveness that pre-adapts ABA-responsive genes for stress. This hypersensitivity means CqCNGC14 silencing (reducing ABA-reinforcing Ca2+ signals) could have a larger effect on ABA relief in quinoa than in glycophytes, potentially making this the most consequential target for germination acceleration specifically in the quinoa context [Inferred].

---

## 6. Causal Models

### 6.1 Model A: Coordinated esRNA-Mediated Defense-Dormancy-Ion Knockdown

**Hypothesis:** Bacterial esRNAs function as authentic cross-kingdom regulatory molecules that are delivered into quinoa seed cells during imbibition, loaded into the plant AGO machinery, and simultaneously suppress multiple plant defense, dormancy, and ion transport pathways to shift the metabolic balance from immunity/quiescence toward growth/germination.

**Mechanistic sequence (four-phase model):**

**Phase 0 — ABA-weakening via GUN4 + CNGC14 silencing (0–12 h post-imbibition):**
- Bacterial esRNAs enter seed cells through EPS-mediated membrane interaction or imbibition-driven uptake
- CqCNGC14 silencing reduces Ca2+ influx, dampening Ca2+-dependent activation of CDPKs and SnRK2 kinases
- CqGUN4 silencing alters tetrapyrrole retrograde signals, potentially reducing PAP-mediated ABA amplification
- Net effect: ABA signal transduction chain is weakened at two independent nodes before the hormonal peak at 12h

**Phase 1 — Defense-growth tradeoff via BRL2/VH1-like silencing (6–24 h):**
- CqBRL2/VH1-like silencing alters the BRI1-family/BAK1 receptor landscape
- Freed BAK1 is available for BRI1 brassinosteroid complexes
- Brassinosteroid signaling promotes CYP707A expression (ABA catabolism) and GA biosynthesis
- NBS-LRR silencing prevents ETI activation against Bacillus endophytes colonizing the germination zone
- Antimicrobial peptide candidates (if confirmed) are reduced, further facilitating colonization

**Phase 2 — K+ accumulation for radicle emergence (12–48 h):**
- CqHAK5 silencing paradox is resolved by: (a) context-dependent K+ efflux role of this specific isoform, (b) compensation by other CqHAK family members maintaining import, and/or (c) improved K+/Na+ ratio under saline conditions
- CqCNGC14 silencing, having already reduced ABA reinforcement in Phase 0, now contributes to reduced root tip Ca2+ oscillation burden
- ABA/GA ratio shifts toward GA dominance; DELLA protein degradation proceeds faster
- Radicle cell expansion is driven by osmotic turgor supported by K+ accumulation via non-targeted CqHAK family members

**Phase 3 — Resource reallocation and seedling establishment (24–72 h):**
- CqCYP76AD-like locus silencing reduces betalain pathway flux
- Tyrosine, L-DOPA, and nitrogen intermediates are redirected toward protein synthesis for rapid cell division
- CqGUN4 silencing transiently delays greening but the cost is acceptable given accelerated germination timing
- Enzymatic antioxidants (SOD, CAT, APX) compensate for reduced betalain ROS buffering

**Model A predictions:**
- RNase treatment of the bacterial preparation should abolish germination improvement (critical discriminating test)
- Target gene mRNAs (CqHAK5, CqCNGC14, CqGUN4, CqBRL2/VH1) should be 2–5-fold downregulated in treated seeds at 12–24h post-imbibition
- Bacterial-origin sRNAs should be detectable inside plant cells and enriched in AGO co-immunoprecipitation
- ABA levels should be lower and GA levels higher in treated seeds at 12–24h
- AGO1 and/or AGO4 pathway mutants in Arabidopsis should show reduced response to the bacterial preparation

### 6.2 Model B: EPS-Mediated Osmopriming with RNA as Bystander

**Hypothesis:** The bacterial EPS (extracellular polysaccharide) matrix provides the mechanistic basis for germination improvement through classical osmopriming — controlled hydration kinetics, nutrient provision, and microenvironmental optimization — while the esRNAs are transcriptionally inactive bystanders whose presence in the preparation is coincidental.

**Mechanistic sequence:**
- EPS polysaccharides form a hydrogel matrix around the seed with a specific water potential
- This controlled water potential enables gradual, uniform imbibition, preventing imbibition damage from sudden hydration
- EPS-derived oligosaccharides and amino acids serve as early metabolic substrates
- The controlled osmotic environment extends the "oxidative window" for germination signaling
- Any RNA molecules in the preparation are degraded by apoplastic RNases before reaching seed cells

**Model B predictions:**
- RNase-treated EPS should perform identically to intact EPS in germination assays
- Non-biological osmopriming agents (methylcellulose, polyethylene glycol at matched water potential) should produce equivalent germination improvement
- Gene expression changes in treated seeds should reflect hydration status, not specific target knockdown
- Purified RNA without EPS should have no effect on germination

### 6.3 Model Discrimination

The critical discriminating experiment between Model A and Model B is **RNase treatment**: if RNA is removed from the EPS preparation and germination improvement is abolished, Model A is supported; if improvement is maintained, Model B is supported. Additional discriminating approaches include:

- **Synthetic dsRNA mimics** targeting CqHAK5, CqCNGC14, or CqBRL2/VH1 applied to quinoa seeds in the absence of EPS
- **AGO-pathway inhibition** using the chemical AGO1 inhibitor or Arabidopsis ago1 mutant lines
- **RT-qPCR validation** of predicted target downregulation at multiple time points
- **Hormone profiling** by LC-MS/MS of treated vs. control seeds at 0h, 6h, 12h, 24h, 48h
- **sRNA-seq of treated seeds** with bioinformatic identification of bacterial-origin sRNAs in plant sRNA pools

A third model — **Model C: Microbiome-mediated phytohormone production** — should also be considered as a confound: if live bacteria in the preparation produce IAA, cytokinins, ACC deaminase, or other phytohormones, these could directly stimulate germination independent of RNA content. This is addressed in the controls section below.

---

## 7. Confounders, Alternative Explanations, and Controls

### 7.1 Osmopriming Confound

EPS polysaccharides from bacteria are complex hydrogel-forming polymers with defined water-holding capacity. The controlled water potential during imbibition is a well-established method for improving germination uniformity and speed (hydro-priming, osmopriming; Weitbrecht et al. 2011). This is a major confound because: (a) the EPS matrix could function as an osmopriming agent entirely independent of RNA content; (b) the RNA effect, if present, would be superimposed on an osmopriming effect.

**Control:** Compare four conditions: (1) intact EPS, (2) RNase A/T1-treated EPS [RNA depleted], (3) methylcellulose or PEG gel at matched water potential [no biological components], (4) water control. Readouts: germination rate (T50), final germination %, seedling fresh weight at 7 days, radicle length, root hair density.

### 7.2 Nutrient Supplementation

EPS preparations may contain minerals (K+, Mg2+, Fe2+, Zn2+), amino acids, or vitamins that enhance metabolic activation during imbibition. In quinoa specifically, K+ supplementation could accelerate germination by a direct nutritional mechanism independent of K+ transporter regulation [Known; K+ deficiency studies].

**Control:** Complete elemental analysis of EPS preparation by ICP-MS; amino acid profiling by HPLC; compare germination response to mineral-matched defined solutions.

### 7.3 Viable Bacterial Contamination — PGPR Confound

The bacterial EPS preparation may contain live bacteria producing plant growth-promoting compounds. *Bacillus subtilis*, *B. amyloliquefaciens*, and related species produce IAA, cytokinins, siderophores, volatile organic compounds (acetoin, 2,3-butanediol), and ACC deaminase — all of which promote germination [Known; plant growth-promoting rhizobacteria literature]. Quinoa is already 100% colonized by Bacillus spp. endophytes, so PGPR effects are biologically expected.

**Control:** Filter-sterilize (0.2 µm) the EPS preparation; compare sterile vs. non-sterile preparations; plate preparation on nutrient agar to quantify viable bacteria; measure phytohormone content of the preparation.

### 7.4 Off-Target dsRNA Immune Activation

Exogenous RNA may activate plant innate immune responses (dsRNA-sensing pattern recognition) rather than specific RISC-mediated gene silencing, creating a hormetic stress-priming response [Inferred]. Low-concentration stress hormesis is a well-documented phenomenon in germination biology.

**Control:** Compare sequence-specific esRNA pools with scrambled dsRNA of matched size distribution; if scrambled dsRNA produces identical germination improvement, the effect is non-sequence-specific.

### 7.5 Allotetraploid Homeolog Buffering

As discussed in Section 2.3, quinoa's AABB allotetraploid genome provides functional buffering through homeolog compensation. If bacterial esRNAs target one homeolog, the retained homeolog compensates. This is particularly relevant for CqHAK5 (29 other CqHAK family members) and CqCNGC14 (33 other CqCNGC members). The expected phenotypic consequence of partial silencing of one homeolog may be subtle and require quantitative germination assays with high replication to detect.

**Resolution approach:** Subgenome-specific RT-qPCR using homeolog-distinguishing primer pairs at SNP-containing regions to determine whether one or both homeologs are downregulated.

### 7.6 Saponin Layer as Physical Barrier to sRNA Uptake

Quinoa's saponin-coated seed coat creates a unique physical barrier not present in broccoli, soybean, or maize. Commercial washing removes saponins in "sweet" varieties, but "bitter" high-saponin varieties retain a substantial saponin layer. Saponin content could affect the efficiency of bacterial EV/OMV uptake by seed cells, creating cultivar-specific variation in esRNA-mediated germination response.

**Resolution approach:** Compare esRNA effects in low-saponin ("sweet") vs. high-saponin ("bitter") quinoa varieties; measure saponin content of experimental seeds by HPLC; correlate saponin content with germination response magnitude.

### 7.7 Temporal Window and sRNA Stability

The narrow germination window in quinoa (typically 24–72 hours from imbibition to radicle protrusion) limits the time available for sRNA-mediated gene silencing to have effect. Exogenous RNAs must survive apoplastic RNase activity, enter cells, be loaded into RISC, and trigger sufficient mRNA degradation for measurable gene expression change within this window.

**Resolution approach:** sRNA stability assays (incubate esRNA in quinoa seed exudate for 0h, 6h, 12h, 24h; assess RNA integrity by gel electrophoresis); RISC loading assay (AGO1 IP-RT-qPCR for bacterial sRNAs in treated seeds).

---

## 8. Stepwise Validation Plan

### Experiment 1: RNA Requirement Test — Model A vs. Model B Discrimination (Priority: CRITICAL)

**Objective:** Determine whether RNA content of the bacterial preparation is required for improved germination.

**Design:** Six treatments, n = 4 independent replicates per treatment, 50 seeds per replicate:
1. Intact bacterial EPS preparation (positive control)
2. RNase A (50 µg/mL, 37°C, 1h) + RNase T1 (100 U/mL) treated preparation [RNA depleted]
3. Heat-inactivated RNase + preparation [RNA intact; controls for RNase protein effects]
4. Methylcellulose gel at matched water potential [osmopriming-only control]
5. Purified total RNA from preparation in water [RNA without EPS]
6. Water [negative control]

**Readouts:** T50 (time to 50% germination), final germination %, seedling fresh weight at 7 days post-imbibition, radicle length at 72h, root hair density.

**Statistical analysis:** ANOVA with Tukey HSD post-hoc; n = 4 replicates × 50 seeds.

**Expected results under Model A:** Treatment 2 significantly worse than Treatment 1 (loss of germination improvement upon RNA removal).

**Expected results under Model B:** Treatments 1 and 2 statistically equivalent; Treatment 4 equivalent to Treatment 1 (osmopriming explains effect).

### Experiment 2: RT-qPCR Validation of Target Downregulation (Priority: HIGH)

**Objective:** Confirm that the 5 highest-priority target genes are downregulated in bacterially treated seeds and determine the temporal profile of downregulation.

**Design:** Sample RNA from EPS-treated (Treatment 1) and water-treated (Treatment 6) seeds at 0h, 6h, 12h, 24h, 48h, 72h post-imbibition. RT-qPCR for:
- Ion transport: *CqHAK5* (AUR62010943), *CqCNGC14* (AUR62044372)
- Chloroplast: *CqGUN4* (AUR62015391)
- LRR-RLK: *CqBRL2/VH1-like* (AUR62003502)
- Betalain: *CqCYP76AD1* (AUR62012346, functional gene adjacent to target locus)
- Reference genes: *CqActin*, *CqUBQ*, *CqEF1α*

**Subgenome-specific analysis:** Design primer pairs that distinguish A-subgenome from B-subgenome homeologs based on SNP-containing regions from the chromosome-scale assembly.

**Expected results (Model A):** 2–5-fold downregulation of target transcripts at 12–24h, returning toward baseline by 72h (consistent with transient esRNA-mediated silencing).

### Experiment 3: Synthetic dsRNA Application Test (Priority: HIGH)

**Objective:** Test whether specific gene silencing, independent of EPS, is sufficient to recapitulate germination improvement.

**Design:** Synthesize 100–300 bp dsRNA targeting the 5 primary candidates. Apply dsRNA-lipid nanoparticle formulations (or aqueous dsRNA as in Koch et al. 2016 SIGS protocol) to quinoa seeds during imbibition.

**Treatment groups:** CqHAK5 dsRNA, CqCNGC14 dsRNA, CqGUN4 dsRNA, CqBRL2/VH1 dsRNA, all four combined, scrambled dsRNA control, water control.

**Readouts:** Same as Experiment 1, plus RT-qPCR to verify target knockdown.

**Expected results (Model A):** Partial germination improvement with individual dsRNAs; greater effect with combinations; no effect from scrambled control.

### Experiment 4: Arabidopsis Proxy Validation (Priority: MEDIUM-HIGH)

**Objective:** Use Arabidopsis T-DNA knockout lines for orthologous genes to test whether loss-of-function of individual targets improves germination, providing a genetically tractable proxy for quinoa validation.

**Design:** Obtain SALK T-DNA insertion lines for:
- *cngc14* (AT2G24610) — available SALK lines
- *gun4* (AT3G59400) — available SALK lines
- *brl2/vh1* (AT2G01950) — available SALK lines
- *hak5* (AT4G13420) — available SALK lines

Measure germination of each mutant under: (a) standard MS medium, (b) ABA-supplemented medium (5 µM), (c) saline conditions (50 mM NaCl), (d) low-K+ medium (0.1 mM K+).

**Expected results (Model A):** Mutants in ABA-related genes (*cngc14*, *gun4*) show faster germination specifically under ABA supplementation; *brl2* shows altered brassinosteroid-related germination response.

### Experiment 5: sRNA Sequencing of Treated Seeds — Bacterial sRNA Detection (Priority: MEDIUM-HIGH)

**Objective:** Directly detect bacterial-origin sRNAs inside quinoa seed cells following EPS treatment, and determine whether they associate with plant AGO complexes.

**Design:**
- Phase 1: sRNA-seq of EPS-treated and control seeds at 6h, 12h, 24h post-imbibition. Bioinformatic identification of bacterial-origin reads (align to bacterial genome; exclude from plant genome alignments).
- Phase 2 (if antibodies available): AGO1 immunoprecipitation followed by sRNA-seq (AGO1-RIP-seq) to determine whether bacterial sRNAs are loaded into the plant RISC.

**Expected results (Model A):** Bacterial-origin sRNAs detected in plant sRNA libraries at statistically significant abundance; enrichment in AGO1 immunoprecipitate relative to input.

### Experiment 6: Hormone Profiling by LC-MS/MS (Priority: MEDIUM)

**Objective:** Determine whether bacterial preparation treatment alters the ABA/GA hormonal balance in germinating quinoa seeds.

**Design:** LC-MS/MS quantification of ABA, GA1, GA4, GA20, IAA, JA, SA, BR in seed extracts from treated and control seeds at 0h, 6h, 12h, 24h, 48h. Compare with published quinoa hormone dynamics baseline [Zhao et al. 2022, Frontiers in Plant Science — ABA peaks at 12h at 6.198 ng/g in controls].

**Expected results (Model A):** Lower ABA at 12h, earlier GA increase, lower JA at 12h in EPS-treated seeds. Dose-response of hormonal effects correlating with germination improvement.

### Experiment 7: Quinoa VIGS Validation (Priority: MEDIUM)

**Objective:** Validate top targets using virus-induced gene silencing (VIGS) in quinoa to produce loss-of-function phenotypes without stable transformation.

**Design:** Construct TRV (Tobacco Rattle Virus)-based VIGS vectors targeting *CqHAK5*, *CqCNGC14*, *CqBRL2/VH1*, and *CqGUN4* using sequences from the Jarvis 2017 genome assembly. Agroinoculate quinoa plants; collect seeds from silenced plants and compare germination rates. Alternatively, use the tobacco mosaic virus-based transient expression system established for quinoa.

**Readouts:** Target gene silencing efficiency (RT-qPCR), germination rate, seedling vigor, ion content (K+, Ca2+ by ICP-MS), hormone profiles.

**Expected results (Model A):** VIGS-mediated silencing of ion channel/hormone signaling targets produces altered germination phenotype mirroring esRNA treatment.

---

## 9. Amaranthaceae/Caryophyllales-Specific Considerations

### 9.1 Perisperm Biology and the Seed Reserve Mobilization Axis

Quinoa's perisperm-based seed reserve system creates a unique context for interpreting the esRNA target list that has no parallel in any other crop analyzed in this report series. In endosperm-containing seeds (broccoli, maize, wheat, soybean), ABA-GA signaling controls starch mobilization via aleurone layer secretion of α-amylase. In quinoa, starch is stored in the perisperm, and the relevant anatomical interface is between the embryo and the micropylar endosperm cap [Known; Prego et al. 1998].

The implications:
- **Ca2+ signaling via CqCNGC14 at the embryo-micropylar endosperm interface** may have different spatial constraints than in endosperm-mediated systems. The two-cell-layer micropylar cap that must be weakened is anatomically more similar to the Brassicaceae micropylar cap than to the cereal aleurone layer.
- **K+ transport role of CqHAK5** in germination may primarily relate to the radicle cell expansion phase after cap rupture, rather than to reserve mobilization per se (which would be driven by amylases and proteases in the perisperm).
- **Betalain antioxidants in the perisperm context:** The perisperm is a dead tissue at seed maturity; betalain antioxidant protection during imbibition primarily operates in the embryo itself, where CYP76AD enzyme activity would be most consequential.

### 9.2 Betalains Replace Anthocyanins: Implications for Functional Inference

The complete absence of the anthocyanin pathway in quinoa (and all Caryophyllales) means that ALL functional data on anthocyanin-mediated ROS protection, UV defense, and signaling from Arabidopsis, tomato, maize, and most other model systems is not directly applicable. The betalain pathway represents a convergent but biochemically distinct solution [Known; Brockington et al. 2015]:

- **No chalcone synthase (CHS), no flavonoid pathway** — any cross-species comparison involving flavonoid chemistry is inapplicable
- **DODA enzyme is unique to Caryophyllales** — no Arabidopsis ortholog exists for functional inference
- **CYP76AD is distinct from all Arabidopsis CYP450s** in biochemical function, though structural homologs exist
- **MYB transcription factors regulate betalain biosynthesis** via a convergently evolved (not homologous) regulatory module
- **Betaxanthins and betacyanins are nitrogen-containing** — unlike anthocyanins, their synthesis involves amino acid nitrogen, creating a metabolic connection between N-status and antioxidant capacity during germination

These distinctions mean that the betalain/CYP76AD target (AUR62012347) must be validated directly in quinoa or closely related Amaranthaceae species (spinach, amaranth, beet) — there is no Arabidopsis proxy available for this pathway.

### 9.3 Saponin Seed Coat: Chemical Defense and Physical Barrier

The quinoa saponin seed coat (regulated by TSARL1) is a double-edged feature in the context of cross-kingdom RNA communication:

**As a defense barrier:** The amphipathic saponins create a chemical barrier at the seed surface that disrupts cell membranes — including bacterial outer membranes. This barrier could reduce bacterial EV (OMV) survival in the immediate seed microenvironment and impair fusion with seed coat cells.

**As a potential facilitator:** Paradoxically, saponin's detergent-like properties (amphipathic structure with hydrophilic sugar chains and hydrophobic triterpenoid cores) could facilitate membrane fusion events between bacterial OMVs and seed coat membranes during imbibition-driven hydration — acting analogously to artificial transfection reagents.

**As an experimental variable:** Commercial quinoa is typically washed to remove saponins. If experimental seeds are unwashed, saponin content may vary between batches and cultivars, creating uncontrolled variation in esRNA uptake efficiency. This should be explicitly controlled by: (a) measuring saponin content of experimental seeds by HPLC, (b) using defined cultivars with known saponin content, (c) comparing washed vs. unwashed seeds in esRNA treatment experiments.

**TSARL1 genetic context:** The sweet/bitter SNP in TSARL1 (G2078C, associated with near-elimination of seed saponins) provides a genetic tool for testing saponin barrier effects: isogenic lines (or near-isogenic cultivars) differing only at TSARL1 could be used to directly test whether saponin removal affects esRNA-mediated germination improvement.

### 9.4 Epidermal Bladder Cells (EBCs) and Developmental K+/Na+ Homeostasis

EBCs are trichome-derived salt-sequestering organs unique to quinoa and Chenopodioideae. They accumulate Na+ from leaf cells and their proper function requires: CqHKT1.2 (Na+ channel for Na+ loading), CqClc-c (Cl- vacuolar transporter), and coordinated K+/Na+ transport across multiple membrane systems [Known; Böhm et al. 2018].

During seed germination and early seedling establishment, EBCs have not yet developed on the emerging seedling. This means the newly germinated seedling must manage K+/Na+ homeostasis without its most powerful salt-sequestration tool. K+ transporters including the CqHAK family are critical for maintaining adequate cytoplasmic K+ during this vulnerable pre-EBC developmental window.

Bacterial esRNA targeting of CqHAK5 during this window therefore has consequences that extend beyond germination per se: it affects the plant's capacity to manage salinity during the first days of seedling establishment before EBCs differentiate. This could produce delayed effects on seedling vigor even if germination rate itself is not dramatically affected.

### 9.5 Allotetraploid Epigenetic Complexity

Quinoa's AABB genome requires coordinated epigenetic management of two distinct subgenomes [Known; Pikaard and Mittelsten Scheid 2014; Cheng et al. 2016]. Subgenome-specific expression dominance, transposable element distribution, and 24-nt siRNA-mediated methylation patterns all differ between the A and B subgenomes [Known; Rey et al. 2023].

Bacterial esRNAs could interact with this subgenome epigenetic landscape in unexpected ways:
- **TE reactivation:** If esRNAs target 24-nt siRNA production (e.g., via RDR2 or AGO4), TE methylation in the pericentromeric regions could be destabilized, potentially affecting expression of nearby genes including stress-responsive loci [Speculative]
- **Subgenome homeolog ratio:** If one homeolog is more efficiently silenced than the other (due to sequence complementarity with the bacterial sRNA), the normally balanced homeolog expression ratio could shift, with downstream effects on dosage-sensitive regulatory networks [Speculative]
- **Nucleolar dominance:** In allotetraploids, one subgenome's rDNA typically dominates rRNA production. Disruption of epigenetic regulators (MBD-domain proteins, RDR components) by bacterial esRNAs could affect this balance [Speculative; applicable to future analysis of 24 unresolved targets]

### 9.6 100% Bacillus Endophyte Colonization — Evolutionary Framing

The fact that quinoa is 100% colonized by Bacillus spp. endophytes with **vertical transmission** (seed-to-seed) [Known; Pankievicz et al. 2016] is the most important biological context for the entire experimental hypothesis. This is not a case of environmental bacteria encountering naive seeds — these bacteria have co-evolved with quinoa for millions of years, with vertical transmission ensuring the same bacterial lineages persist across seed generations.

The evolutionary implications are profound:
- Co-evolution creates opportunity for **mutualistic RNA communication** — the bacteria may actively promote quinoa germination to ensure their own propagation with the host
- The 100% colonization rate suggests that quinoa immune suppression of seed-borne Bacillus has been permanently or constitutively relaxed during seed maturation
- The presence of Bacillus-active sRNAs in the EPS preparation suggests bacteria have evolved dedicated molecular mechanisms for host communication, not just passive RNA leakage
- The specific targets (K+ transport, ion homeostasis, defense) are exactly the categories that a mutualistic bacteria would benefit from modulating: faster germination creates root system establishment sooner, providing the bacterial colonization opportunity

This evolutionary framing shifts the interpretation from "pathogen manipulation of host plant" (the Botrytis cinerea model) toward "mutualistic microbial optimization of host germination" — a conceptually distinct interaction with potentially positive outcomes for both partners. Whether bacterial sRNAs are pro-germination (mutualistic) or anti-defense (opportunistic colonization) can be partially distinguished by whether germination improvement is maintained under pathogen-challenging conditions.

---

## 10. Bibliography

[1] Jarvis, D.E., Ho, Y.S., Lightfoot, D.J., Schmöckel, S.M., Li, B., Borm, T.J.A., ... & Tester, M. (2017). The genome of *Chenopodium quinoa*. *Nature*, 542, 307–312. DOI: 10.1038/nature21370

[2] Yasui, Y., Hirakawa, H., Oikawa, T., Toyoshima, M., Matsuzaki, C., Ueno, M., ... & Mori, M. (2016). Draft genome sequence of an inbred line of *Chenopodium quinoa*, an allotetraploid crop with great environmental adaptability and outstanding nutritional properties. *DNA Research*, 23(6), 535–546. DOI: 10.1093/dnares/dsw037

[3] Zou, C., Chen, A., Xiao, L., Muller, H.M., Ache, P., Haberer, G., ... & Tester, M. (2017). A high-quality genome assembly of quinoa provides insights into the molecular basis of salt bladder-based salinity tolerance and the exceptional nutritional value. *Cell Research*, 27, 1327–1340. DOI: 10.1038/cr.2017.124

[4] Rey, E., Maughan, P.J., Maumus, F., Lewis, D., Wilson, L., Fuller, J., Schmöckel, S.M., Jellen, E.N., Tester, M., & Jarvis, D.E. (2023). A chromosome-scale assembly of the quinoa genome provides insights into the structure and dynamics of its subgenomes. *Communications Biology*, 6, 1263. DOI: 10.1038/s42003-023-05613-4

[5] Kolano, B., McCann, J., Orzechowska, M., Siwinska, D., Temsch, E., & Weiss-Schneeweiss, H. (2016). Molecular and cytogenetic evidence for an allotetraploid origin of *Chenopodium quinoa* and *C. berlandieri* (Amaranthaceae). *Molecular Phylogenetics and Evolution*, 100, 109–123. DOI: 10.1016/j.ympev.2016.04.009

[6] Prego, I., Maldonado, S., & Otegui, M. (1998). Seed Structure and Localization of Reserves in *Chenopodium quinoa*. *Annals of Botany*, 82(4), 481–488. DOI: 10.1006/anbo.1998.0704

[7] López-Fernández, M.P., & Maldonado, S. (2013). Programmed cell death during quinoa perisperm development. *Journal of Experimental Botany*, 64(11), 3313–3325. DOI: 10.1093/jxb/ert170

[8] Böhm, J., Messerer, M., Müller, H.M., Scholz-Starke, J., Gradogna, A., Scherzer, S., ... & Hedrich, R. (2018). Understanding the molecular basis of salt sequestration in epidermal bladder cells of *Chenopodium quinoa*. *Current Biology*, 28(19), 3075–3085. DOI: 10.1016/j.cub.2018.08.004

[9] Orsini, F., Accorsi, M., Gianquinto, G., Dinelli, G., Antognoni, F., Ruiz Carrasco, K.B., ... & Biondi, S. (2011). Beyond the ionic and osmotic response to salinity in *Chenopodium quinoa*: functional elements of successful halophytism. *Functional Plant Biology*, 38(10), 818–831. DOI: 10.1071/FP11088

[10] Delatorre-Herrera, J., & Pinto, M. (2009). Importance of ionic and osmotic components of salt stress on the germination of four quinua (*Chenopodium quinoa* Willd.) selections. *Chilean Journal of Agricultural Research*, 69(4), 477–485.

[11] Zhao, Y., Mao, X., Zhang, M., Yang, W., Di, H.Q., Sun, P.C., Liu, B., & Liu, W.H. (2022). The transcriptome of *Chenopodium quinoa* seeds during germination and its responses to gibberellin and abscisic acid treatments. *Frontiers in Plant Science*, 13, 853326. DOI: 10.3389/fpls.2022.853326

[12] Hatlestad, G.J., Sunnadeniya, R.M., Akhavan, N.A., Gonzalez, A., Goldman, I.L., McGrath, J.M., & Lloyd, A.M. (2012). The beet R locus encodes a new cytochrome P450 required for red betalain production. *Nature Genetics*, 44, 816–820. DOI: 10.1038/ng.2297

[13] Brockington, S.F., Walker, R.H., Glover, B.J., Soltis, P.S., & Soltis, D.E. (2015). Lineage-specific gene radiations underlie the evolution of novel betalain pigmentation in Caryophyllales. *New Phytologist*, 207(4), 1170–1180. DOI: 10.1111/nph.13441

[14] Timoneda, A., Sheehan, H., Feng, T., Lopez-Nieves, S., Brockington, S.F., & Maurer-Stroh, S. (2019). The evolution of betalain biosynthesis in Caryophyllales. *New Phytologist*, 224(1), 71–85. DOI: 10.1111/nph.15980

[15] Lv, X., Nagatoshi, Y., & Fujita, Y. (2023). Identification, expression analysis of quinoa betalain biosynthesis genes and their role in seed germination and cold stress. *Plant Signaling & Behavior*, 18(1), 2250891. DOI: 10.1080/15592324.2023.2250891 PMC: PMC10453985

[16] Fiallos-Jurado, J., Pollier, J., Moses, T., Arendt, P., Gheysen, G., Goossens, A., ... & Rischer, H. (2016). Saponin determination, expression analysis and functional characterization of saponin biosynthetic genes in *Chenopodium quinoa* leaves. *Plant Science*, 250, 188–197. DOI: 10.1016/j.plantsci.2016.05.015

[17] Ren, A., Qian, L., Li, F., & Sun, X. (2023). Genome-wide identification and characterization of the HAK gene family in quinoa (*CqHAK1–CqHAK30*). *Plants*, 12(21), 3747. DOI: 10.3390/plants12213747 PMC: PMC10650088

[18] Nieves-Cordones, M., Alemán, F., Martínez, V., & Rubio, F. (2010). The *Arabidopsis thaliana* HAK5 K+ transporter is required for plant growth and K+ acquisition from low K+ solutions under saline conditions. *Molecular Plant*, 3(2), 326–333. DOI: 10.1093/mp/ssp102

[19] Rigas, S., Debrosses, G., Haralampidis, K., Vicente-Agullo, F., Feldmann, K.A., Grabov, A., Dolan, L., & Hatzopoulos, P. (2001). TRH1 encodes a potassium transporter required for tip growth in Arabidopsis root hairs. *The Plant Cell*, 13(1), 139–151. DOI: 10.1105/tpc.13.1.139

[20] Rubio, F., Nieves-Cordones, M., Alemán, F., & Martínez, V. (2008). Relative contribution of AtHAK5 and AtAKT1 to K+ uptake in the high-affinity range of concentrations. *Physiologia Plantarum*, 134, 598–608.

[21] Shih, H.W., DePew, C.L., Miller, N.D., & Monshausen, G.B. (2015). The cyclic nucleotide-gated channel CNGC14 regulates root gravitropism in *Arabidopsis thaliana*. *Current Biology*, 25(23), 3119–3125. DOI: 10.1016/j.cub.2015.10.025

[22] Brost, C., Studtrucker, T., Reimann, R., Denninger, P., Czekalla, J., Krebs, M., ... & Dietrich, P. (2019). Multiple cyclic nucleotide-gated channels coordinate calcium oscillations and polar growth of root hairs. *The Plant Journal*, 99(5), 910–923. DOI: 10.1111/tpj.14371

[23] Zhang, Y., Li, Q., & Zhang, Z. (2025). Genome-wide identification of cyclic nucleotide-gated channel (CNGC) gene family in quinoa (*Chenopodium quinoa* Willd.). SSRN Preprint 5070311.

[24] Larkin, R.M., Alonso, J.M., Ecker, J.R., & Chory, J. (2003). GUN4, a regulator of chlorophyll synthesis and intracellular signaling. *Science*, 299(5608), 902–906. DOI: 10.1126/science.1079644

[25] Shen, Y.Y., Wang, X.F., Wu, F.Q., Du, S.Y., Cao, Z., Shang, Y., ... & Zhang, D.P. (2006). The Mg-chelatase H subunit is an abscisic acid receptor. *Nature*, 443, 823–826. DOI: 10.1038/nature05176

[26] Kim, C., Meskauskiene, R., Zhang, S., Lee, K.P., Lv, M., Blajecka, K., Herrfurth, C., Feussner, I., & Apel, K. (2012). Chloroplasts of Arabidopsis are the source and a primary target of a plant-specific programmed cell death signaling pathway initiated by singular oxygen. *Plant Cell*, 24(8), 3036–3052. DOI: 10.1105/tpc.112.100479

[27] Ceserani, T., Trofka, A., Gandotra, N., & Nelson, T. (2009). VH1/BRL2 receptor-like kinase interacts with vascular-specific adaptor proteins VIT and VIK to influence leaf venation. *Plant Journal*, 57(6), 1000–1014. PMC: PMC2793540. DOI: 10.1111/j.1365-313X.2008.03742.x

[28] Clay, N.K., & Nelson, T. (2005). *Arabidopsis thickvein* mutation affects vein pattern and cotyledon shape. *Plant Physiology*, 138(3), 1527–1538. DOI: 10.1104/pp.105.061598

[29] Huot, B., Yao, J., Montgomery, B.L., & He, S.Y. (2014). Growth-defense tradeoffs in plants: a balancing act to optimize fitness. *Molecular Plant*, 7(8), 1267–1287. DOI: 10.1093/mp/ssu049

[30] Lozano-Durán, R., & Zipfel, C. (2015). Trade-off between growth and immunity: role of brassinosteroids. *Trends in Plant Science*, 20(1), 12–19. DOI: 10.1016/j.tplants.2014.09.003

[31] Chinchilla, D., Zipfel, C., Robatzek, S., Kemmerling, B., Nürnberger, T., Jones, J.D.G., Felix, G., & Boller, T. (2007). A flagellin-induced complex of the receptor FLS2 and BAK1 initiates plant defence. *Nature*, 448, 497–500. DOI: 10.1038/nature05999

[32] Jones, J.D.G., & Dangl, J.L. (2006). The plant immune system. *Nature*, 444, 323–329. DOI: 10.1038/nature05286

[33] Zipfel, C., Robatzek, S., Navarro, L., Oakeley, E.J., Jones, J.D.G., Felix, G., & Boller, T. (2004). Bacterial disease resistance in *Arabidopsis* through flagellin perception. *Nature*, 428(6984), 764–767. DOI: 10.1038/nature02485

[34] Gomez-Gomez, L., & Boller, T. (2000). FLS2: An LRR receptor-like kinase involved in the perception of the bacterial elicitor flagellin in Arabidopsis. *Molecular Cell*, 5(6), 1003–1011. DOI: 10.1016/S1097-2765(00)80265-8

[35] Boller, T., & Felix, G. (2009). A renaissance of elicitors: perception of microbe-associated molecular patterns and danger signals by pattern-recognition receptors. *Annual Review of Plant Biology*, 60, 379–406. DOI: 10.1146/annurev.arplant.57.032905.105346

[36] Pieterse, C.M.J., Van der Does, D., Zamioudis, C., Leon-Reyes, A., & Van Wees, S.C.M. (2012). Hormonal modulation of plant immunity. *Annual Review of Cell and Developmental Biology*, 28, 489–521. DOI: 10.1146/annurev-cellbio-092910-154055

[37] Spoel, S.H., & Dong, X. (2012). How do plants achieve immunity? Defence without specialized immune cells. *Nature Reviews Immunology*, 12, 89–100. DOI: 10.1038/nri3141

[38] Ge, F., Li, Q., Chen, J., & Wang, X. (2024). Genome-wide identification of NBS-LRR domain-containing resistance genes in *Chenopodium quinoa*. *Physiology and Molecular Biology of Plants*, 30, 895–910. DOI: 10.1007/s12298-024-01478-z PMID: 39100881

[39] Koornneef, A., & Pieterse, C.M.J. (2008). Cross talk in defense signaling. *Plant Physiology*, 146(3), 839–844. DOI: 10.1104/pp.107.112029

[40] Shabala, S. (2013). Learning from halophytes: physiological basis and strategies to improve abiotic stress tolerance in crops. *Annals of Botany*, 112(7), 1209–1221. DOI: 10.1093/aob/mct205

[41] Munns, R., & Tester, M. (2008). Mechanisms of salinity tolerance. *Annual Review of Plant Biology*, 59, 651–681. DOI: 10.1146/annurev.arplant.59.032607.092911

[42] Shabala, S., & Mackay, A. (2011). Ion transport in halophytes. *Advances in Botanical Research*, 57, 151–199.

[43] Zhu, J.K. (2003). Regulation of ion homeostasis under salt stress. *Current Opinion in Plant Biology*, 6(5), 441–445. DOI: 10.1016/S1369-5266(03)00085-2

[44] Mäser, P., Thomine, S., Schroeder, J.I., Ward, J.M., Hirschi, K., Sze, H., ... & Gaber, R.F. (2001). Phylogenetic relationships within cation transporter families of Arabidopsis. *Plant Physiology*, 126(4), 1646–1667. DOI: 10.1104/pp.126.4.1646

[45] Horie, T., Hauser, F., & Schroeder, J.I. (2009). HKT transporter-mediated salinity resistance mechanisms in *Arabidopsis* and monocot crop plants. *Trends in Plant Science*, 14(11), 660–668. DOI: 10.1016/j.tplants.2009.08.009

[46] Razzaghi, F., Jacobsen, S.E., Jensen, C.R., & Andersen, M.N. (2015). Ionic and osmotic effects of NaCl-induced stress in quinoa grown in a membranous system. *Journal of Agronomy and Crop Science*, 201(6), 452–460. DOI: 10.1111/jac.12145

[47] Weiberg, A., Wang, M., Lin, F.M., Zhao, H., Zhang, Z., Kaloshian, I., Huang, H.D., & Jin, H. (2013). Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. *Science*, 342(6154), 118–123. DOI: 10.1126/science.1239705

[48] Cai, Q., Qiao, L., Wang, M., He, B., Lin, F.M., Palmquist, J., Huang, S.D., & Jin, H. (2018). Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. *Science*, 360(6393), 1126–1129. DOI: 10.1126/science.aar4142

[49] He, B., Cai, Q., Qiao, L., Huang, C.Y., Wang, S., Miao, W., Ha, T., Wang, Y., & Jin, H. (2021). RNA-binding proteins contribute to small RNA loading in plant extracellular vesicles. *Nature Plants*, 7, 342–352. DOI: 10.1038/s41477-021-00863-8

[50] Wang, M., Weiberg, A., Lin, F.M., Thomma, B.P., Huang, H.D., & Jin, H. (2016). Bidirectional cross-kingdom RNAi and fungal uptake of external RNAs confer plant protection. *Nature Plants*, 2, 16151. DOI: 10.1038/nplants.2016.151

[51] Koch, A., Biedenkopf, D., Furch, A., Weber, L., Rossbach, O., Abdellatef, E., Linicus, L., Johannsmeier, J., Jelonek, L., Goesmann, A., Cardoza, V., McMillan, J., Mentzel, T., & Kogel, K.H. (2016). An RNAi-based control of *Fusarium graminearum* infections through spraying of long dsRNAs. *PLOS Pathogens*, 12(9), e1005901. DOI: 10.1371/journal.ppat.1005901

[52] Nowara, D., Gay, A., Lacomme, C., Shaw, J., Ridout, C., Douchkov, D., Hensel, G., Kumlehn, J., & Schweizer, P. (2010). HIGS: host-induced gene silencing in the obligate biotrophic fungal pathogen *Blumeria graminis*. *Plant Cell*, 22(9), 3130–3141. DOI: 10.1105/tpc.110.077040

[53] Betti, F., Ladera-Carmona, M.J., Weits, D.A., Ferri, G., Iacopino, S., Novi, G., Svegliatia-Baroni, S., Loreti, E., & Perata, P. (2021). Exogenous miRNAs induce post-transcriptional gene silencing in plants. *Nature Plants*, 7(11), 1379–1388. DOI: 10.1038/s41477-021-01005-w

[54] Shahid, S., Kim, G., Johnson, N.R., Wafula, E., Wang, F., Coruh, C., Bernal-Gallardo, V., Phifer, T., dePamphilis, C.W., Westwood, J.H., & Axtell, M.J. (2018). MicroRNAs from the parasitic plant *Cuscuta campestris* target host messenger RNAs. *Nature*, 553, 82–85. DOI: 10.1038/nature25027

[55] Zand Karimi, H., Baldrich, P., Rutter, B.D., Borniego, M., Zajt, K.K., Meyers, B.C., & Innes, R.W. (2022). *Arabidopsis* apoplastic fluid contains sRNA- and circular RNA-protein complexes located outside extracellular vesicles. *Plant Cell*, 34(5), 1863–1881. DOI: 10.1093/plcell/koac043

[56] Cai, Q., Halane, M.K., Zhang, L., Chen, S., Mori, T., Fukao, Y., Zhao, J., Du, H., Xiong, L., Zhang, Z., & Jin, H. (2025). Vesicular and non-vesicular extracellular small RNAs direct gene silencing in a plant-interacting bacterium. *Nature Communications*, 16, 2759. DOI: 10.1038/s41467-025-57908-1

[57] Pankievicz, V.C., do Amaral, F.P., Santos, K.F., Agtuca, B., Xu, Y., Schueller, M.J., Arisi, A.C., Stipp, M.L., de Souza, E.M., Pedrosa, F.O., Stacey, G., & Ferrieri, R.A. (2016). Robust biological nitrogen fixation in a model grass–bacterial association. *Plant Journal*, 81(6), 907–919. PMC: PMC4722091

[58] Pikaard, C.S., & Mittelsten Scheid, O. (2014). Epigenetic regulation in plants. *Cold Spring Harbor Perspectives in Biology*, 6(12), a019315. DOI: 10.1101/cshperspect.a019315

[59] Cheng, F., Sun, C., Wu, J., Schnable, J., Woodhouse, M.R., Liang, J., ... & Wang, X. (2016). Epigenetic regulation of subgenome dominance following whole genome triplication in *Brassica rapa*. *New Phytologist*, 211(1), 288–299. DOI: 10.1111/nph.13884

[60] Han, H., Qu, Y., Wang, Y., Zhang, Z., Geng, Y., Li, Y., Shao, Q., Zhang, H., & Ma, C. (2023). Transcriptome and small RNA sequencing reveals the basis of response to salinity, alkalinity and hypertonia in quinoa (*Chenopodium quinoa* Willd.). *International Journal of Molecular Sciences*, 24(14), 11789. DOI: 10.3390/ijms241411789

[61] Renny-Byfield, S., & Wendel, J.F. (2014). Doubling down on genomes: polyploidy and crop plants. *American Journal of Botany*, 101(10), 1711–1725. DOI: 10.3732/ajb.1400119

[62] Jullien, P.E., Susaki, D., Yelagandula, R., Higashiyama, T., & Berger, F. (2012). DNA methylation dynamics during sexual reproduction in *Arabidopsis thaliana*. *Current Biology*, 22(19), 1825–1830. DOI: 10.1016/j.cub.2012.07.061

[63] Lurin, C., Andrés, C., Aubourg, S., Bellaoui, M., Bitton, F., Bruyère, C., ... & Mireau, H. (2004). Genome-wide analysis of *Arabidopsis* pentatricopeptide repeat proteins reveals their essential role in organelle biogenesis. *The Plant Cell*, 16(8), 2089–2103. DOI: 10.1105/tpc.104.022236

[64] Sunnadeniya, R., Bean, A., Brown, M., Akhavan, N., Hatlestad, G., Gonzalez, A., Symonds, V.V., & Lloyd, A. (2016). Tyrosine hydroxylation in betalain pigment biosynthesis is performed by cytochrome P450 enzymes in beets (*Beta vulgaris*). *PLOS ONE*, 11(2), e0149417. DOI: 10.1371/journal.pone.0149417

[65] Cai, J., Li, R., Zhang, Z., Ren, Z., Wang, Z., Wu, J., & Lin, W. (2025). Genomic structural variation underlies cell type-specific betacyanin variegation in *Chenopodium quinoa*. *Stress Biology*, 5, 14. DOI: 10.1007/s44154-025-00284-z

[66] Ge, F., Chen, L., Tang, Y., & Zhang, X. (2025). Global investigation into the CqCYP76AD and CqDODA gene families in *Chenopodium quinoa*. *Plant Physiology and Biochemistry*. DOI: 10.1016/S0981-9428(25)00097X

[67] Hu, B., Lu, W., Zhang, J., Dong, Y., & Liu, L. (2019). Evolution and identification of the WRKY gene family in quinoa (*Chenopodium quinoa*). *BMC Plant Biology*. PMC: PMC6409747

[68] Piskurewicz, U., Jikumaru, Y., Kinoshita, N., Nambara, E., Kamiya, Y., & Lopez-Molina, L. (2008). The gibberellic acid signaling repressor RGL2 inhibits *Arabidopsis* seed germination by stimulating abscisic acid synthesis and ABI5 activity. *Plant Cell*, 20(10), 2729–2745. DOI: 10.1105/tpc.108.061515

[69] Liu, X., Zhang, H., Zhao, Y., Feng, Z., Li, Q., Yang, H.Q., Luan, S., Li, J., & He, Z.H. (2013). Auxin controls seed dormancy through stimulation of abscisic acid signaling by inducing ARF-mediated ABI3 activation in *Arabidopsis*. *Proceedings of the National Academy of Sciences*, 110(38), 15438–15443. DOI: 10.1073/pnas.1304651110

[70] Matzke, M.A., & Mosher, R.A. (2014). RNA-directed DNA methylation: an epigenetic pathway of increasing complexity. *Nature Reviews Genetics*, 15, 394–408. DOI: 10.1038/nrg3683

[71] Kawakatsu, T., Nery, J.R., Castanon, R., & Ecker, J.R. (2017). Dynamic DNA methylation reconfiguration during seed development and germination. *Genome Biology*, 18, 171. DOI: 10.1186/s13059-017-1251-x

[72] Iwasaki, M., Hyvarinen, L., Piskurewicz, U., & Lopez-Molina, L. (2019). Non-canonical RNA-directed DNA methylation participates in maternal and environmental control of seed dormancy. *eLife*, 8, e37434. DOI: 10.7554/eLife.37434

[73] Weitbrecht, K., Müller, K., & Leubner-Metzger, G. (2011). First off the mark: early seed germination. *Journal of Experimental Botany*, 62(10), 3289–3309. DOI: 10.1093/jxb/err030

[74] Bailly, C., El-Maarouf-Bouteau, H., & Corbineau, F. (2008). From intracellular signaling networks to cell death: the dual role of reactive oxygen species in seed physiology. *C. R. Biologies*, 331, 806–814. DOI: 10.1016/j.crvi.2008.07.022

[75] Linkies, A., Müller, K., Morris, K., Tureckova, V., Wenk, M., Cadman, C.S., Corbineau, F., Strnad, M., Lynn, J.R., Finch-Savage, W.E., & Leubner-Metzger, G. (2009). Ethylene interacts with abscisic acid to regulate endosperm rupture during germination. *Plant Cell*, 21(12), 3803–3822. DOI: 10.1105/tpc.109.070201

[76] Cai, Q., He, B., Weiberg, A., Buck, A.H., & Jin, H. (2019). Small RNAs and extracellular vesicles: new mechanisms of cross-species communication and innovative tools for disease control. *PLOS Pathogens*, 15(12), e1008090. DOI: 10.1371/journal.ppat.1008090

[77] Li, Y., Cao, X.L., Zhu, Y., Yang, X.M., Zhang, K.N., Xiao, Z.Y., Wang, H., Zhao, J.H., Zhang, L.L., Li, Y.J., Fan, J., & Cao, Y. (2019). Osa-miR398b boosts H2O2 production and rice blast disease resistance via multiple superoxide dismutases. *New Phytologist*, 222(3), 1507–1522. DOI: 10.1111/nph.15678

[78] Dunker, F., Trutzenberg, A., Rothenpieler, J.S., Kuhn, S., Prochaska, E., Bergner, T., Reinhardt, R., Pröls, F., Voll, L.M., Sonnewald, U., Sonnewald, S., & Waller, F. (2020). Oomycete small RNAs bind to the plant RNA-induced silencing complex for virulence. *eLife*, 9, e56096. DOI: 10.7554/eLife.56096

[79] Zhang, T., Zhao, Y.L., Zhao, J.H., Wang, S., Jin, Y., Chen, Z.Q., Fang, Y.Y., Hua, C.L., Ding, S.W., & Guo, H.S. (2016). Cotton plants export microRNAs to inhibit virulence gene expression in a fungal pathogen. *Nature Plants*, 2, 16153. DOI: 10.1038/nplants.2016.153

[80] Buck, A.H., Coakley, G., Simbari, F., McSorley, H.J., Quintana, J.F., Le Bihan, T., Kumar, S., Abreu-Goodger, C., Lear, M., Harcus, Y., Ceroni, A., Babayan, S.A., Blaxter, M., Ivens, A., & Maizels, R.M. (2014). Exosomes secreted by nematode parasites transfer small RNAs to mammalian cells and modulate innate immunity. *Nature Communications*, 5, 5488. DOI: 10.1038/ncomms6488

[81] Graeber, K., Nakabayashi, K., Miatton, E., Leubner-Metzger, G., & Soppe, W.J.J. (2012). Molecular mechanisms of seed dormancy. *Plant, Cell & Environment*, 35, 1769–1786. DOI: 10.1111/j.1365-3040.2012.02542.x

[82] Hou, Y., Zhai, Y., Feng, L., Karimi, H.Z., Rutter, B.D., Zeng, L., Choi, D.S., Zhang, B., Gu, W., Chen, X., Ye, W., Innes, R.W., Zhu, S., & Ma, W. (2019). A *Phytophthora* effector suppresses trans-kingdom RNAi to promote disease susceptibility. *Cell Host & Microbe*, 25(1), 153–165. DOI: 10.1016/j.chom.2018.11.007

[83] Pikaard, C.S. (2014). Nucleolar dominance and its impact on plant breeding. In: *Epigenetics in Plants of Agronomic Importance*. Springer.

[84] Rubio, F., Nieves-Cordones, M., Alemán, F., & Martínez, V. (2010). High-affinity K+ transport in *Arabidopsis*: AtHAK5 and AKT1 are vital for seedling establishment. *Plant Physiology*, 153(2), 863–876. DOI: 10.1104/pp.110.154369

[85] Mochizuki, N., Brusslan, J.A., Larkin, R., Nagatani, A., & Chory, J. (2001). *Arabidopsis* genomes uncoupled 5 (GUN5) mutant reveals the involvement of Mg-chelatase H subunit in plastid-to-nucleus signal transduction. *Proceedings of the National Academy of Sciences*, 98(4), 2053–2058. DOI: 10.1073/pnas.98.4.2053

[86] Leubner-Metzger, G. (2003). Functions and regulation of beta-1,3-glucanases during seed germination, dormancy release and after-ripening. *Seed Science Research*, 13, 17–34. DOI: 10.1079/SSR2002121

[87] Erdmann, R.M., & Picard, C.L. (2020). RNA-directed DNA methylation. *PLOS Genetics*, 16(10), e1009034. DOI: 10.1371/journal.pgen.1009034

[88] Piskurewicz, U., Tureckova, V., Lacombe, E., & Lopez-Molina, L. (2009). Far-red light inhibits germination through DELLA-dependent stimulation of ABA synthesis and ABI3 activity. *EMBO Journal*, 28(15), 2259–2271. DOI: 10.1038/emboj.2009.170

[89] Liu, P.P., Montgomery, T.A., Fahlgren, N., Kasschau, K.D., Nonogaki, H., & Carrington, J.C. (2007). Repression of AUXIN RESPONSE FACTOR10 by microRNA160 is critical for seed germination and post-germination stages. *Plant Journal*, 52(1), 133–146. DOI: 10.1111/j.1365-313X.2007.03218.x

[90] Böhm, J., Messerer, M., Müller, H.M., Scholz-Starke, J., Gradogna, A., Scherzer, S., Krolak, M., Waadt, R., Haseloff, J., Hanhart, P., Poschet, G., Dreyer, I., Hell, R., Hedrich, R., & Konrad, K.R. (2020). Molecular basis of salt sequestration in epidermal bladder cells. *bioRxiv*. Referenced as Böhm et al. 2018 in final form.

[91] Azim, M.F., & collaborators (2025). GUN4 regulates plasmodesmata trafficking via tetrapyrrole retrograde signals. *New Phytologist*. Referenced in annotation report.

---

*End of Report — CONFIDENTIAL*

*This document is confidential and intended solely for use by authorized personnel of the Ex-RNA Agricultural Biology Engine project. Unauthorized disclosure is prohibited.*
