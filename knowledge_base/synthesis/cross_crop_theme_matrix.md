# CROSS-CROP THEME MATRIX: Bacterial exRNA-Mediated Germination Enhancement

**Date**: 2026-02-17
**Crops analyzed**: Spinach (Spinacia oleracea), Broccoli (Brassica oleracea), Maize (Zea mays), Wheat (Triticum aestivum), Quinoa (Chenopodium quinoa), Soybean (Glycine max)
**Method**: Systematic extraction from 6 crop-specific mechanistic claims files; scoring based exclusively on evidence presented therein.

---

## A. CROSS-CROP THEME MATRIX

### Scoring Key
- **0** = Theme absent / no evidence in target list
- **1** = Weak evidence (1 low-priority target, speculative mechanism)
- **2** = Moderate evidence (2-5 targets, mechanistically plausible)
- **3** = Strong evidence (>5 targets or high-priority targets with strong mechanistic rationale)

Gene counts in parentheses refer to distinct gene loci assigned to that theme.

### Table: RNA-Mediated MoA Themes

| MoA Theme | Spinach | Broccoli | Maize | Wheat | Quinoa | Soybean | Cross-Crop Score |
|-----------|---------|----------|-------|-------|--------|---------|------------------|
| **Defense Downshift** | 3 (10+) | 3 (7) | 2 (5) | 3 (18) | 2 (4) | 2 (3) | **15/18** |
| **Epigenetic Derepression** | 3 (6) | 3 (5) | 1 (2) | 2 (3) | 0 | 0 | **9/18** |
| **Hormone Rebalancing (ABA/GA axis)** | 3 (6) | 3 (5) | 3 (4) | 3 (4) | 2 (2) | 3 (3) | **17/18** |
| **ROS/Redox Optimization** | 3 (5) | 2 (3) | 2 (1) | 2 (2) | 1 (1) | 2 (2) | **12/18** |
| **Cell Wall Remodeling** | 1 (1) | 2 (4) | 1 (1) | 1 (2) | 0 | 2 (2) | **7/18** |
| **Metabolic Priming** | 2 (5) | 2 (4) | 2 (2) | 1 (2) | 1 (1) | 3 (2) | **11/18** |
| **Transport/Ion Homeostasis** | 2 (7) | 2 (3) | 2 (2) | 2 (5) | 3 (2) | 0 | **11/18** |
| **Cell Cycle/Growth** | 0 | 2 (3) | 0 | 1 (3) | 0 | 0 | **3/18** |
| **RNA Processing** | 1 (1) | 2 (3) | 1 (1) | 2 (3) | 0 | 1 (2) | **7/18** |

### Detailed Scoring Rationale

#### Defense Downshift

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 3 | EDR2 x2, MOS1, R-protein, NST1, 4 RLKs, LOX (defense arm) | 10+ defense/immunity targets; multi-layered: perception (RLKs), regulation (MOS1, EDR2), execution (NST1); canonical growth-defense tradeoff |
| Broccoli | 3 | CRK26, CRK29, Chitinase, GH17, ABCG37/PDR9, RING/U-box E3, RDR | 7 defense targets; CRK26/29 FLS2-complex association documented; chitinase PR protein; ABCG37 multiply targeted by sRNAs |
| Maize | 2 | CML21, LRR-RLK, PSKR1-like, MOS1-like, ZRP4-like OMT | 5 targets; CML21 Ca2+-mediated defense; LRR-RLK generic receptor; MOS1-like chromatin/immunity; O-methyltransferase (cell wall/defense) |
| Wheat | 3 | 6 F-box, 5 LRR-RLKs, 2 NB-LRR, 3 ABC transporters, Gnk2, LURP1 | 18 targets = 24% of all wheat targets; unprecedented dominance; includes homeolog pairs on chr 5 and chr 6 |
| Quinoa | 2 | NLR candidate (AUR62021543), 2 antimicrobial peptide candidates, BRL2/VH1-like | 4 targets; NLR with 678 paralogs; antimicrobial peptides (defensin/LTP candidates); BRL2 annotation corrected from generic "LRR-RLK" |
| Soybean | 2 | TIR-NBS-LRR, ERECTA-like LRR-RLK, LrgB-like | 3 targets; 319 NBS-LRR genes in soybean genome; isoflavonoid defense pathway cost; growth-defense tradeoff documented |

#### Epigenetic Derepression

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 3 | DNA methyltransferase, SUVR5, HIRA, PHD-domain reader, GIS2, RRP15 | 6 targets attacking writers (DNA MTase, SUVR5), readers (PHD), remodelers (HIRA), and TFs (GIS2); coordinated multi-layer dismantling |
| Broccoli | 3 | MBD10, RDR (dual defense/epigenetic), TRFL7, TRM1-like, CCCH ZnF | 5 targets; MBD10 reads methylation marks; RDR produces siRNAs for RdDM; TRFL7 recruits PRC2; two-pronged derepression |
| Maize | 1 | AHL9, MOS1-like (chromatin/immunity) | 2 targets with chromatin function; AHL9 AT-hook protein derepresses auxin biosynthesis via chromatin remodeling; MOS1-like modulates SNC1 expression via chromatin. Evidence is moderate but targets are primarily classified elsewhere |
| Wheat | 2 | DDM1, Bromodomain/GTE8, Homeobox-DDT | 3 targets; DDM1 is an SNF2-family chromatin remodeler maintaining DNA methylation; hexaploid genome with 85% repeats sensitive to DDM1 modulation |
| Quinoa | 0 | None | No epigenetic targets identified among the 31 predicted targets |
| Soybean | 0 | None | No epigenetic targets among 18 predicted targets |

#### Hormone Rebalancing (ABA/GA axis)

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 3 | Ethylene receptor, LOX, AHP-like, Phytoene synthase, MYB TF, NAC TF | 6 targets; ethylene receptor (negative regulator, strongest single target); LOX cuts JA+ABA precursors; phytoene synthase starves ABA pathway |
| Broccoli | 3 | ARF (repressor-type), HD-ZIP TF, CDPK15, PP2A-A, SBI1 | 5 targets; ARF-ABI3 dormancy pathway; CDPK15 reduces Ca2+-mediated ABA signaling; PP2A modulates multiple hormone pathways |
| Maize | 3 | ABI40/VP1-like, NPF15/AIT1 (ABA transporter), HEX6 (glucose-ABA), IDP8263 | 4 targets; ABI40 score 10/10 (VP1 null = vivipary); NPF15 ABA importer; HEX6 breaks glucose-ABA feedback loop |
| Wheat | 3 | SnRK2 kinase, ADC, BTB/POZ, NAC38 | 4 targets; SnRK2 directly reduces ABA signal transduction (phenocopies after-ripening); ADC shifts polyamine ratio from ABA-promoting to GA-promoting |
| Quinoa | 2 | CqCNGC14 (Ca2+-ABA link), CqGUN4 (retrograde-ABA link) | 2 targets; CNGC14 silencing reduces Ca2+-dependent ABA reinforcement; GUN4 modulates ABA via retrograde signaling; indirect but mechanistically clear |
| Soybean | 3 | PLDbeta1 (PA-ABA amplifier), CKX3 (cytokinin oxidase), ROP GTPase | 3 targets; PLDbeta1 directly reduces PA-mediated ABA amplification; CKX3 elevates cytokinins; highest-scoring hormone targets |

#### ROS/Redox Optimization

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 3 | GST L3, Peroxidase, 6-PGDH, Rhodanese, CYP450 | 5 targets; three-pronged: reduce direct scavenging (GST), reduce H2O2 removal/cell wall stiffening (Peroxidase), reduce NADPH supply (6-PGDH); creates "oxidative window" |
| Broccoli | 2 | COPT5, TrxL2.2, CRK26/29 (dual defense/ROS) | 3 targets; COPT5 reduces Cu-mediated Fenton chemistry; TrxL2.2 is atypical oxidizing thioredoxin; CRKs reduce NADPH oxidase-mediated ROS bursts |
| Maize | 2 | PRX91 (class III peroxidase) | 1 target but high quality; Atprx16 knockout = earlier germination; PRX91 dual ROS/cell wall function; score 8/10. RING63/RING265 contribute indirectly via proteostasis |
| Wheat | 2 | PARP, AOX (paradoxical) | 2 targets; PARP is the single most robust target (>10% biomass increase in PARP-deficient plants); AOX downregulation is contradictory/detrimental. PARP alone warrants score 2 |
| Quinoa | 1 | CqCYP76AD-like (betalain/antioxidant locus) | 1 target; nontranslating CDS adjacent to betalain biosynthesis gene; betalains are primary non-enzymatic antioxidants in Caryophyllales; resource reallocation hypothesis |
| Soybean | 2 | Glutaredoxin, PLDbeta1 (NADPH oxidase modulation) | 2 targets; glutaredoxin regulates thiol-disulfide redox; PLDbeta1 modulates NADPH oxidase via PA; zeatin riboside as superoxide scavenger (CKX3 link) |

#### Cell Wall Remodeling

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 1 | Peroxidase (dual ROS/cell wall) | 1 target with cell wall function; peroxidase reduces lignification/cross-linking, facilitating radicle protrusion |
| Broccoli | 2 | PME, BGAL10, GH17 glucanase, Glycosyltransferase | 4 targets; complex tissue-dependent effects; PME downregulation may maintain pectin flexibility; BGAL10 and GH17 are paradoxical (growth-promoting functions) |
| Maize | 1 | ZRP4-like OMT (suberin/lignin biosynthesis) | 1 target; reduces cell wall fortification at radicle tip; also classified under defense |
| Wheat | 1 | GH17 glucanases x2 (ambiguous defense vs. mobilization) | 2 targets; beta-glucanases could facilitate endosperm degradation but likely defense-related; paradoxical for mobilization |
| Quinoa | 0 | None | No cell wall remodeling targets identified |
| Soybean | 2 | CesA4, Invertase/PME inhibitor (dual function) | 2 targets; CesA4 downregulation reduces secondary cell wall rigidity; invertase/PME inhibitor also affects pectin remodeling |

#### Metabolic Priming

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 2 | TPS, Aspartokinase, CTP synthase, PP2A, GDSL esterases x3 | 5 targets; TPS/T6P signaling (flagged as uncertain); PP2A modulates multiple pathways; GDSL esterases alter lipid metabolism |
| Broccoli | 2 | THIC (thiamine, essential), BCKDH (BCAA catabolism), CTP synthase, CYP703A2 | 4 targets; THIC multiply targeted by sRNAs; BCKDH reduces amino acid catabolism; CTP synthase paradoxical |
| Maize | 2 | HEX6 (glucose sensor/metabolic enzyme), MYBR64 (starch mobilization TF) | 2 targets; HEX6 breaks glucose-ABA feedback; MYBR64 if germination repressor, derepresses starch mobilization; both scored 7-9/10 |
| Wheat | 1 | SQD1 x2 (redirects UDP-glucose), sugar transporters x2 | 2-4 targets; SQD1 dispensable during dark germination; MFS sugar transporters speculative |
| Quinoa | 1 | CqCYP76AD-like (betalain resource reallocation) | 1 target; nitrogen and NADPH reallocation from betalain pathway to protein synthesis; Amaranthaceae-specific |
| Soybean | 3 | Invertase/PME inhibitor (derepresses CWI), CKX3 (cytokinin/metabolic) | 2 targets but strongest cross-species validation; invertase inhibitor silencing = elevated CWI, increased hexoses in soybean (Tang 2017), Arabidopsis (Su 2016), tomato (Jin 2009) |

#### Transport/Ion Homeostasis

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 2 | CCC1 x2, CNGC, Cation/H+ antiporter, ABC transporters x2, NRT1/PTR | 7 targets; both CCC1 paralogs targeted; CNGC modulates Ca2+; overall reconfiguration of ion transport infrastructure |
| Broccoli | 2 | COPT5 (copper transporter), ABCG37/PDR9, GDI | 3 targets; COPT5 Cu mobilization; ABCG37 exports IBA/coumarins; GDI modulates vesicle trafficking |
| Maize | 2 | NPF15/AIT1 (ABA transporter), GDT1-like (Golgi Ca2+/Mn2+) | 2 targets; NPF15 is high priority (score 9/10) as ABA importer; GDT1 lowest priority |
| Wheat | 2 | Mg transporter, MscS channels x2, MFS sugar transporters x2 | 5 targets; mechanosensitive channels for imbibition osmotic stress; Mg transporter possibly chloroplast-targeted |
| Quinoa | 3 | CqHAK5 (K+ high-affinity transporter), CqCNGC14 (Ca2+ channel) | 2 targets but both highest-confidence confirmed targets (50% of confirmed targets are ion transport); K+ drives radicle turgor; Ca2+ mediates ABA/auxin signaling; halophyte context amplifies importance |
| Soybean | 0 | None confirmed | CURT1-like has annotation conflict (cation transport vs. thylakoid); no confident ion transport targets |

#### Cell Cycle/Growth

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 0 | None | No cell cycle targets identified |
| Broccoli | 2 | FZR3/CCS52B (APC/C activator), CAK1AT, EXO84B | 3 targets; FZR3 downregulation could accelerate G1-to-S transition; CAK1AT modulates cell cycle/transcription; EXO84B paradoxical |
| Maize | 0 | None | No direct cell cycle targets |
| Wheat | 1 | CDC27/APC3, Kinesin (detrimental), Profilin (detrimental) | 3 targets but 2 are predicted detrimental; CDC27 moderates premature division; kinesin and profilin required for cell division |
| Quinoa | 0 | None | No cell cycle targets |
| Soybean | 0 | None | No cell cycle targets |

#### RNA Processing

| Crop | Score | Genes | Rationale |
|------|-------|-------|-----------|
| Spinach | 1 | RRP15 (rDNA transcription regulator) | 1 target; modulates ribosome biogenesis; speculative resource allocation role |
| Broccoli | 2 | TFIIIC5 (Pol III transcription, multiply targeted), PPR protein (multiply targeted), CCCH ZnF (mRNA metabolism) | 3 targets; TFIIIC5 essential for tRNA/rRNA production; PPR for organellar RNA; both multiply targeted by sRNAs |
| Maize | 1 | ppr377 (mitochondrial RNA processing) | 1 target; potentially counterproductive (mitochondrial energy metabolism); score 6/10 |
| Wheat | 2 | PPR protein, mTERF, ASCH domain protein | 3 targets; PPR for organellar RNA processing; mTERF for transcription termination; ASCH domain for RNA modification |
| Quinoa | 0 | None | No RNA processing targets |
| Soybean | 1 | Exosome Rrp46-like, Urb2/Npa2 ribosome biogenesis | 2 targets; exosome subunit for mRNA turnover; ribosome biogenesis factor; both speculative |

---

### Separate Assessment: EPS Priming MoA (Non-RNA Mechanisms)

All 6 crops describe EPS osmopriming as the highest-concern confounder. The following effects are attributable to the EPS matrix itself (without RNA):

| EPS Effect | Universal? | Notes |
|-----------|-----------|-------|
| Controlled hydration / osmopriming | Yes (all 6) | Well-established priming technology; could explain 100% of germination improvement |
| Polysaccharide elicitor (MAMP) effects | Yes (all 6) | Mild defense priming / hormesis |
| Nutrient supplementation | Yes (all 6) | EPS contains amino acids, minerals |
| Hydration film / imbibition uniformity | Yes (all 6) | Physical microenvironment effect |
| pH / ionic strength modulation | Likely (all 6) | EPS alters local chemical environment |

The RNase elimination experiment is universally recommended as the critical discriminating test.

---

## B. CORE MoA IDENTIFICATION

### 1. PRIMARY MECHANISM: Hormone Rebalancing (ABA/GA Axis Shift)

**Cross-crop score: 17/18 (score >= 2 in ALL 6 crops)**

This is the only theme achieving score >= 2 in every crop analyzed. The ABA/GA (or more broadly ABA/growth-hormone) axis is the universal master switch for seed germination across angiosperms, and the bacterial exRNAs attack it through crop-specific but functionally convergent mechanisms:

| Crop | Primary ABA/GA Intervention | Key Gene(s) | Evidence Quality |
|------|---------------------------|-------------|------------------|
| Spinach | Ethylene receptor silencing (creates ethylene hypersensitivity that antagonizes ABA) + LOX silencing (cuts ABA precursor supply) + phytoene synthase (starves carotenoid/ABA pathway) | SOV3g000150.1, SOV3g035520.1, SOV4g000330.1 | **Strong** -- named genes with Arabidopsis mutant phenotypes |
| Broccoli | Repressor-type ARF silencing (releases ABI3-mediated dormancy) + CDPK15 (reduces Ca2+-ABA signal transduction) + PP2A-A (modulates hormone crosstalk) | Bo7g114200.1, Bo1g025790.1, Bo9g011330.1 | **Strong** -- miR160-ARF10 germination precedent in Arabidopsis |
| Maize | ABI40/VP1-like silencing (master dormancy regulator; VP1 null = vivipary) + NPF15/AIT1 (ABA importer) + HEX6 (glucose-ABA feedback) | Zm00001eb197370, Zm00001eb385450, Zm00001eb154520 | **Strongest** -- VP1 vivipary phenotype is definitive; HXK1/gin2 precedent |
| Wheat | SnRK2 silencing (central ABA signal transducer; phenocopies after-ripening) + ADC (polyamine-ABA crosstalk) + NAC38 (ABA-inducible stress TF) | TraesCS7D02G384400, TraesCS2A02G071200, TraesCS5B02G275200 | **Strong** -- wheat PKABA1 was first SnRK2 characterized; after-ripening mechanism known |
| Quinoa | CNGC14 silencing (reduces Ca2+-dependent ABA reinforcement) + GUN4 (retrograde-ABA crosstalk) | AUR62044372, AUR62015391 | **Moderate** -- indirect mechanisms; halophyte ABA hypersensitivity amplifies effect |
| Soybean | PLDbeta1 silencing (reduces PA-mediated ABA amplification) + CKX3 (elevates cytokinins that oppose ABA) + ROP GTPase (ABA signal transduction) | GLYMA_01G215100, GLYMA_09G063900, GLYMA_09G192700 | **Strong** -- PA-ABA link well-validated; CKX function established |

**Weight by gene-level anchors**: Named genes with established mutant phenotypes (ABI40/VP1 in maize, ethylene receptor in spinach, SnRK2 in wheat, ARF10-type in broccoli) provide the strongest anchors. Quinoa has the weakest gene-level support (indirect Ca2+ and retrograde signaling mechanisms).

**RNA-specific vs. EPS-explainable**: The downregulation of specific transcription factors (ABI40, ARFs, NAC38), signal transducers (SnRK2, CDPK15), and receptors (ethylene receptor) at the transcript level requires sequence-specific RNA-mediated silencing. EPS osmopriming cannot explain the selective downregulation of named ABA signaling components.

### 2. SECONDARY MECHANISMS

#### Secondary Mechanism 1: Defense Downshift (Cross-crop score: 15/18; score >= 2 in ALL 6 crops)

The defense downshift is present in all 6 crops at score >= 2, making it nearly as universal as hormone rebalancing. However, it is designated secondary because:
- Defense-to-growth resource reallocation is an INDIRECT germination mechanism (frees resources rather than directly triggering germination)
- The specific defense components targeted vary widely across crops (kinase receptors in spinach/broccoli/wheat, NLR genes in wheat/quinoa/soybean, antimicrobial peptides in quinoa, isoflavonoid pathway in soybean)
- Some defense downshift effects (reduced immune surveillance) could also be explained by EPS-mediated MAMP desensitization

**Unique contribution**: The massive targeting of defense genes in wheat (24% of all targets = 18 genes) is the most extreme example. The defense downshift may serve a dual purpose: (1) freeing metabolic resources for germination, and (2) facilitating beneficial interaction between the bacterial EPS source organism and the germinating seed. This parallels the Botrytis cinerea cross-kingdom RNAi paradigm (Weiberg et al. 2013) but in a mutualistic context.

#### Secondary Mechanism 2: ROS/Redox Optimization (Cross-crop score: 12/18; score >= 2 in 5 of 6 crops)

Present at score >= 2 in all crops except quinoa (which has only the CYP76AD-like betalain locus as a weak redox target). The "oxidative window" concept -- that germination requires ROS levels within a specific beneficial range -- is well-supported and the exRNAs modulate this window through crop-specific mechanisms:

- **Spinach**: Direct scavenger suppression (GST, Peroxidase) + reductant supply reduction (6-PGDH)
- **Broccoli**: Cu-mediated Fenton chemistry reduction (COPT5) + atypical thioredoxin modulation (TrxL2.2)
- **Maize**: Peroxidase PRX91 (dual ROS/cell wall function)
- **Wheat**: PARP (NAD+ conservation; the single most robustly validated target across ALL crops)
- **Soybean**: Glutaredoxin (thiol-disulfide redox)

**RNA-specific**: The targeting of specific ROS-managing enzymes (named peroxidases, GSTs, PARP, glutaredoxins) requires sequence-specific silencing and cannot be explained by EPS effects alone.

#### Secondary Mechanism 3: Epigenetic Derepression (Cross-crop score: 9/18; score >= 2 in 3 of 6 crops)

This mechanism is prominent in spinach (score 3) and broccoli (score 3), moderate in wheat (score 2), weak in maize (score 1), and absent in quinoa and soybean. It is therefore NOT universal but represents a strong eudicot/Brassicaceae mechanism:

- **Spinach**: Most comprehensive -- attacks writers (DNA MTase, SUVR5), readers (PHD), remodelers (HIRA), and developmental TFs (GIS2)
- **Broccoli**: Two-pronged -- MBD10 (methylation reader) + RDR (siRNA/methylation producer)
- **Wheat**: DDM1 (chromatin remodeler maintaining DNA methylation)
- **Maize/Quinoa/Soybean**: Absent or minimal

### 3. MECHANISM WEIGHTING BY GENE-LEVEL ANCHORS

**Tier 1 -- Named genes with established loss-of-function mutant phenotypes directly affecting germination:**
- ABI40/VP1-like (Maize): VP1 null = vivipary. Score 10/10.
- Ethylene receptor (Spinach): etr1-1 = faster germination. Strong.
- Invertase inhibitor (Soybean): GmCIF1 RNAi = elevated CWI, AtCIF1 loss = accelerated germination. Score 10/10.
- PARP (Wheat): PARP-deficient plants = >10% biomass increase. Score highest.
- SnRK2 (Wheat): PKABA1/SnRK2 = central ABA transducer. Score high.
- PRX91/Atprx16 (Maize): Atprx16 knockout = earlier germination. Score 8/10.
- DNA methyltransferase (Spinach): met1 = reduced dormancy. Score moderate-strong.

**Tier 2 -- Named genes with strong functional annotation but indirect germination evidence:**
- ARF repressor-type (Broccoli, Wheat): miR160-ARF10 germination control established
- PLDbeta1 (Soybean): PA-ABA link validated
- CKX3 (Soybean): CKX function established; zeatin riboside as superoxide scavenger
- MBD10 (Broccoli): Methylation reader; germination epigenetic transition
- EDR2 (Spinach): Dual defense/ABA role
- LOX (Spinach): JA + ABA precursor biosynthesis
- ADC (Wheat): Polyamine-ABA crosstalk
- HEX6 (Maize): gin2 precedent for glucose-ABA
- CRK26/CRK29 (Broccoli): FLS2 complex association documented

**Tier 3 -- Genes with functional annotation but speculative germination link:**
- Most defense kinases (RLKs, NLRs across all crops)
- Ion transporters (HAK5 in quinoa, CCC in spinach)
- PPR proteins (broccoli, maize, wheat)

### 4. RNA-SPECIFIC vs. EPS OSMOPRIMING DISCRIMINATION

| Mechanism | RNA-Specific? | EPS-Explainable? | Discrimination |
|-----------|--------------|-------------------|----------------|
| Specific TF/kinase transcript downregulation | YES | NO | Only RNA can silence ABI40, SnRK2, ARFs, etc. |
| Defense gene coordinated suppression | YES | PARTIALLY (MAMPs can modulate defense) | Specific NLR/F-box/RLK transcript reduction = RNA |
| Epigenetic derepression | YES | NO | DNA methyltransferase/MBD10/DDM1 silencing requires RNA |
| ROS scavenger modulation | YES | PARTIALLY (osmopriming affects ROS) | Named enzyme (GST, PARP) transcript reduction = RNA |
| Improved imbibition uniformity | NO | YES | Physical EPS property |
| Controlled hydration kinetics | NO | YES | Physical EPS property |
| Nutrient supplementation | NO | YES | Chemical EPS property |

### 5. CROP-SPECIFIC UNIQUE MECHANISMS

| Crop | Unique Feature | Genes/Pathway | Significance |
|------|---------------|---------------|-------------|
| Quinoa | Betalain antioxidant pathway targeting | CqCYP76AD-like (AUR62012347) | Caryophyllales-specific; betalains replace anthocyanins; resource reallocation from betalain to protein synthesis |
| Quinoa | Halophyte K+/Na+ management | CqHAK5 (AUR62010943) | HAK/KUP paradox; context-dependent in halophyte with pre-EBC vulnerability window |
| Broccoli | WGT-buffered knockdown | Multiple paradoxical targets (BGAL10, GH17, SBI1, EXO84B) | Whole-genome triplication provides safety net for broad targeting |
| Wheat | PARP-mediated energy conservation | TraesCS1A02G328000 | Most robustly validated single target; >10% biomass increase documented |
| Wheat | Polyamine-ABA crosstalk | TraesCS2A02G071200 (ADC) | Wheat-specific polyamine-dormancy axis; putrescine-ABA-GA interplay |
| Soybean | Invertase inhibitor derepression | GLYMA_05G068700 | Strongest cross-species experimental validation (soybean, Arabidopsis, tomato); direct CWI activity elevation |
| Soybean | Bradyrhizobium sRNA precedent | Ren et al. 2019 Science | Only crop with published bacteria-to-host sRNA transfer validation in the same species |
| Maize | Vivipary phenotype anchor | ABI40/VP1-like (Zm00001eb197370) | VP1 null = precocious germination on ear; strongest single-gene loss-of-function evidence |

---

## C. CROSS-CROP TARGET HOMOLOGY TABLE

### Defense-Related Gene Families

| Gene Family | Spinach | Broccoli | Maize | Wheat | Quinoa | Soybean | Confidence |
|-------------|---------|----------|-------|-------|--------|---------|------------|
| **NBS-LRR / NLR** | R-protein (SOV1g021670.1) | -- | -- | 2 NB-LRR (TraesCS5D02G521900, TraesCS5B02G559900) | NLR candidate (AUR62021543, 678 paralogs) | TIR-NBS-LRR (GLYMA_06G259700) | HIGH -- conserved innate immune receptors targeted in 4/6 crops |
| **LRR-RLK** | 4 RLKs (SOV1g027650.1, SOV4g000660.1, SOV4g046320.1, SOV5g030510.1) | CRK26, CRK29 (Bo7g119590.1, Bo7g107400.1) | LRR-RLK (Zm00001eb403550), PSKR1-like (Zm00001eb066630) | 5 LRR-RLKs (TraesCS7D02G379600, etc.) | BRL2/VH1-like (AUR62003502) | ERECTA-like (GLYMA_10G242300) | HIGH -- receptor kinases targeted in all 6 crops |
| **MOS1 / chromatin-immunity** | SOV5g005530.1 (MOS1-like) | -- | AI714716 (Zm00001eb136860, MOS1-like) | -- | -- | -- | MODERATE -- chromatin-level immune regulation in 2 crops |
| **ABC transporters** | SOV1g032780.1, SOV4g041000.1 | Bo6g067490.1 (ABCG37/PDR9) | -- | 3 ABC transporters (TraesCS7B02G381000, etc.) | -- | -- | MODERATE -- defense compound/xenobiotic transport in 3 crops |

### ABA/Hormone Signaling Gene Families

| Gene Family | Spinach | Broccoli | Maize | Wheat | Quinoa | Soybean | Confidence |
|-------------|---------|----------|-------|-------|--------|---------|------------|
| **ABI3/VP1 family** | -- | ARF-ABI3 axis (Bo7g114200.1 ARF) | ABI40/VP1-like (Zm00001eb197370) | -- | -- | -- | HIGH for maize/broccoli; ABI3/VP1 master dormancy regulators |
| **SnRK2 / protein kinase** | -- | CDPK15 (Bo1g025790.1) | -- | SnRK2 kinase (TraesCS7D02G384400) | -- | ROP GTPase (GLYMA_09G192700) | MODERATE -- ABA signal transduction kinases in 3 crops |
| **PP2A / phosphatase** | SOV3g033920.1 (PP2A-A subunit) | Bo9g011330.1 (PP2A-A subunit) | -- | BTB/POZ (TraesCS3D02G394800, stabilizes PP2Cs) | -- | PLDbeta1 (indirect PP2A link) | MODERATE -- PP2A targeted or modulated in 3-4 crops |
| **Ethylene receptor** | SOV3g000150.1 | -- | -- | -- | -- | -- | HIGH for spinach only -- strongest single target but crop-specific |
| **NPF/AIT transporters** | SOV5g032210.1 (NRT1/PTR) | -- | NPF15 (Zm00001eb385450) | -- | -- | -- | MODERATE -- hormone transporters in 2 crops |
| **MYB/NAC TFs** | SOV1g020340.1 (MYB), SOV2g014810.1 (NAC) | -- | MYBR64 (Zm00001eb187270) | NAC38 (TraesCS5B02G275200) | -- | -- | MODERATE -- stress/hormone-responsive TFs in 3 crops |

### Epigenetic Gene Families

| Gene Family | Spinach | Broccoli | Maize | Wheat | Quinoa | Soybean | Confidence |
|-------------|---------|----------|-------|-------|--------|---------|------------|
| **DNA methylation (writers/readers/remodelers)** | DNA MTase (SOV1g033340.1) | MBD10 (Bo8g066360.1) | -- | DDM1 (TraesCS7A02G074600) | -- | -- | HIGH -- different nodes of DNA methylation pathway in 3 crops |
| **Histone modification** | SUVR5 (SOV4g015450.1), PHD reader (SOV4g030590.1) | -- | -- | Bromodomain/GTE8 (TraesCS3A02G122200) | -- | -- | MODERATE -- histone code writers/readers in 2 crops |
| **Chromatin remodeling** | HIRA (SOV6g036290.1) | RDR (Bo8g102500.1, dual) | AHL9 (Zm00001eb065740) | DDM1 (TraesCS7A02G074600) | -- | -- | MODERATE -- chromatin architecture modifiers in 4 crops |

### ROS/Redox Gene Families

| Gene Family | Spinach | Broccoli | Maize | Wheat | Quinoa | Soybean | Confidence |
|-------------|---------|----------|-------|-------|--------|---------|------------|
| **Class III peroxidases** | SOV3g038840.1 (Peroxidase) | -- | PRX91 (Zm00001eb333290) | -- | -- | -- | HIGH -- peroxidase function well-characterized; Atprx16 germination data |
| **Glutathione system** | SOV3g040200.1 (GST L3) | -- | -- | -- | -- | GLYMA_03G196400 (glutaredoxin) | MODERATE -- GSH/GRX systems in 2 crops |
| **PARP** | -- | -- | -- | TraesCS1A02G328000 (PARP) | -- | -- | HIGH for wheat only -- best-validated single target but crop-specific |
| **Cu/Fe transport (Fenton)** | -- | Bo9g151660.1 (COPT5) | -- | -- | -- | -- | MODERATE for broccoli only |

### Metabolic Gene Families

| Gene Family | Spinach | Broccoli | Maize | Wheat | Quinoa | Soybean | Confidence |
|-------------|---------|----------|-------|-------|--------|---------|------------|
| **CTP synthase** | SOV5g001320.1 | Bo5g064420.1 | -- | -- | -- | -- | LOW -- pyrimidine nucleotide pools in 2 crops |
| **Hexokinase / sugar sensing** | -- | -- | HEX6 (Zm00001eb154520) | -- | -- | Invertase inhibitor (GLYMA_05G068700) | HIGH -- sugar-ABA crosstalk in 2 crops with strong mutant data |
| **PPR proteins** | -- | Bo4g076880.1 (multiply targeted) | ppr377 (Zm00001eb303410) | TraesCS3B02G123400 | -- | -- | MODERATE -- organellar RNA processing in 3 crops |
| **RING E3 ubiquitin ligases** | -- | Bo1g141380.1 | RING63, RING265 | 6 F-box proteins | -- | -- | MODERATE -- ubiquitin-proteasome pathway in 3 crops |

### Ion Transport Gene Families

| Gene Family | Spinach | Broccoli | Maize | Wheat | Quinoa | Soybean | Confidence |
|-------------|---------|----------|-------|-------|--------|---------|------------|
| **CNGC (Ca2+ channels)** | SOV1g018480.1 | -- | -- | -- | CqCNGC14 (AUR62044372) | -- | MODERATE -- Ca2+ signaling in 2 crops |
| **HAK/KUP (K+ transporters)** | -- | -- | -- | -- | CqHAK5 (AUR62010943) | -- | HIGH for quinoa only -- halophyte-specific |
| **ABC transporters** | SOV1g032780.1, SOV4g041000.1 | Bo6g067490.1 (ABCG37) | -- | 3 targets | -- | -- | MODERATE -- broadly present in 3 crops |

---

## D. THEME EVIDENCE SUMMARY

### 1. Defense Downshift

The defense downshift is the most broadly represented theme, present at score >= 2 in all 6 crops. Wheat provides the strongest evidence with 18 defense-related targets (24% of all targets), including coordinated suppression of F-box proteins (6), LRR-RLKs (5), NB-LRR immune receptors (2 homeologs), ABC defense transporters (3), and antifungal proteins (2). Broccoli provides the best-characterized individual targets (CRK26/CRK29 with documented FLS2 complex association and 18-fold flg22 induction). Spinach shows multi-layered suppression from perception (RLKs) through regulation (EDR2, MOS1) to execution (NST1). The weakest support comes from quinoa (candidate NLR and unconfirmed antimicrobial peptides) and soybean (only 3 defense targets). The defense downshift is mechanistically coherent with the growth-defense tradeoff paradigm and parallels the Botrytis cinerea cross-kingdom RNAi model (Weiberg et al. 2013), but in a mutualistic rather than parasitic context.

### 2. Epigenetic Derepression

Epigenetic derepression is strongly represented in spinach and broccoli but absent in quinoa and soybean, making it a eudicot-enriched rather than universal mechanism. Spinach provides the most comprehensive evidence with 6 epigenetic targets spanning the entire silencing cascade: DNA methyltransferase (writer), SUVR5 H3K9me (writer), PHD domain (reader), HIRA (remodeler), GIS2 (developmental TF), and RRP15 (ribosome biogenesis). Broccoli adds the MBD10 methylation reader and RDR (siRNA producer for RdDM pathway), with documented Brassicaceae-specific importance of RdDM in seed development (Grover et al. 2018). Wheat contributes DDM1, an SNF2-family chromatin remodeler critical for maintaining DNA methylation in the highly repetitive (85%) hexaploid genome. The absence of epigenetic targets in quinoa and soybean may reflect smaller target lists (31 and 18 respectively) rather than biological irrelevance, but it weakens the universality claim.

### 3. Hormone Rebalancing (ABA/GA Axis)

This is the PRIMARY mechanism, achieving score >= 2 in all 6 crops and score 3 in 4 of 6. The strongest crop-specific evidence comes from maize (ABI40/VP1-like, where VP1 null = vivipary -- the most definitive single-gene germination phenotype), spinach (ethylene receptor as negative regulator -- etr1-1 mutants show faster germination), and soybean (invertase inhibitor silencing validated in soybean, Arabidopsis, and tomato). The mechanism attacks the ABA/GA axis through diverse crop-specific entry points: transcription factors (ABI40, ARFs, NAC38, MYB), signal transducers (SnRK2, CDPK15, ROP GTPase), receptors (ethylene receptor), transporters (NPF15/AIT1), biosynthetic enzymes (LOX, ADC, phytoene synthase), and lipid signaling (PLDbeta1/PA). Quinoa provides the weakest support, with only indirect mechanisms (CNGC14 Ca2+-ABA crosstalk, GUN4 retrograde-ABA), reflecting both the smaller confirmed target set and the unique halophyte biology.

### 4. ROS/Redox Optimization

ROS/redox optimization is present at score >= 2 in 5 of 6 crops, with quinoa as the exception. The strongest individual target is wheat PARP (TraesCS1A02G328000), which is the most robustly validated single target across all crops: PARP-deficient Arabidopsis and oilseed rape showed >10% biomass increase with broad-spectrum stress tolerance (De Block et al. 2005), confirmed by both genetic and pharmacological inhibition (Schulz et al. 2012). Spinach provides the most mechanistically complete model with its three-pronged approach: reducing direct scavenging (GST), reducing H2O2 removal/cell wall stiffening (peroxidase), and reducing NADPH supply (6-PGDH). Maize contributes the Atprx16 germination precedent. Soybean adds glutaredoxin modulation with the "redox kick-start" concept (Nietzel et al. 2020). The "oxidative window" model (Bailly et al. 2008) provides the unifying theoretical framework: germination requires ROS within a beneficial range, and the exRNAs fine-tune this window.

### 5. Cell Wall Remodeling

Cell wall remodeling is the weakest universally represented theme, present at only modest levels in 5 of 6 crops (absent in quinoa) and never exceeding score 2. Broccoli provides the most targets (PME, BGAL10, GH17 glucanase, glycosyltransferase) but several are paradoxical -- BGAL10 is growth-promoting and its downregulation should impair rather than improve germination. Soybean contributes CesA4 (secondary cell wall cellulose synthase) and the dual-function invertase/PME inhibitor. The general weakness of this theme likely reflects that cell wall loosening during germination is primarily achieved through endogenous GA-mediated processes (expansin induction, etc.) that are indirectly promoted by the ABA/GA axis shift rather than through direct targeting of cell wall enzymes.

### 6. Metabolic Priming

Metabolic priming is moderately represented, achieving score >= 2 in 4 of 6 crops. Soybean provides the strongest evidence with the invertase inhibitor (GLYMA_05G068700), which has the best cross-species experimental validation of any single target: RNAi of GmCIF1 elevated CWI activity in soybean (Tang et al. 2017), AtCIF1 loss accelerated germination in Arabidopsis (Su et al. 2016), and INVINH1 silencing increased hexoses in tomato (Jin et al. 2009). Maize contributes HEX6 (hexokinase-glucose-ABA feedback) with the gin2 precedent. Spinach includes TPS (T6P/SnRK1 pathway, though flagged as uncertain) and biosynthetic enzymes. The theme is weakest in quinoa (only betalain resource reallocation) and wheat (SQD1 redirecting UDP-glucose). The crop-specific nature of the metabolic priming targets (invertase in soybean, hexokinase in maize, T6P in spinach) reflects the different primary storage reserves and metabolic architectures of each species.

### 7. Transport/Ion Homeostasis

Transport and ion homeostasis is moderately represented, achieving score >= 2 in 5 of 6 crops (absent in soybean). Quinoa provides the strongest and most mechanistically significant evidence, with CqHAK5 and CqCNGC14 representing 50% of confirmed targets -- reflecting the halophyte context where K+/Na+ homeostasis is critical for germination, especially during the pre-EBC vulnerability window. Spinach has the most targets (7) but most are low confidence. Wheat contributes mechanosensitive channels relevant to imbibition osmotic stress. The HAK/KUP paradox in quinoa (silencing a K+ importer should impair germination) remains unresolved and requires experimental testing under varying salinity conditions.

### 8. Cell Cycle/Growth

Cell cycle regulation is the least universal theme, present at score >= 2 only in broccoli (FZR3/CCS52B, CAK1AT, EXO84B). Wheat has 3 cell cycle targets but 2 (kinesin, profilin) are predicted to be detrimental. The near-absence of cell cycle targets in spinach, maize, quinoa, and soybean suggests that the exRNAs primarily promote germination through upstream hormonal and metabolic reprogramming rather than direct cell cycle acceleration.

### 9. RNA Processing

RNA processing targets appear in 4 of 6 crops at modest levels. The most notable are broccoli's TFIIIC5 (Pol III transcription, multiply targeted by sRNAs) and PPR proteins (organellar RNA processing, present in broccoli, maize, and wheat). The biological significance is ambiguous: some RNA processing targets (PPR proteins for mitochondrial function) could be counterproductive if they impair energy metabolism during the critical imbibition phase. The multiply targeted nature of TFIIIC5 and PPR in broccoli suggests convergent selection pressure, but whether this reflects a beneficial germination mechanism or a bacterial strategy to limit host translational capacity remains unclear.

---

## Summary Hierarchy

```
PRIMARY MoA (Universal):
  Hormone Rebalancing / ABA-GA Axis Shift
  Score >= 2 in ALL 6 crops (17/18 total)
  Best gene anchors: ABI40/VP1 (maize), Ethylene receptor (spinach),
                      SnRK2 (wheat), PLDbeta1 (soybean)

SECONDARY MoA #1 (Universal):
  Defense Downshift / Growth-Defense Reallocation
  Score >= 2 in ALL 6 crops (15/18 total)
  Best gene anchors: CRK26/29 (broccoli), F-box x6 + NB-LRR (wheat),
                      EDR2 x2 + MOS1 (spinach)

SECONDARY MoA #2 (Near-universal):
  ROS/Redox Optimization
  Score >= 2 in 5/6 crops (12/18 total)
  Best gene anchors: PARP (wheat), GST + Peroxidase + 6-PGDH (spinach),
                      PRX91 (maize)

SECONDARY MoA #3 (Eudicot-enriched):
  Epigenetic Derepression
  Score >= 2 in 3/6 crops (9/18 total)
  Best gene anchors: DNA MTase + SUVR5 (spinach), MBD10 + RDR (broccoli),
                      DDM1 (wheat)

CROP-SPECIFIC UNIQUE:
  - Quinoa: Betalain pathway targeting (Caryophyllales-specific)
  - Quinoa: HAK/KUP K+ paradox (halophyte-specific)
  - Broccoli: WGT-buffered broad targeting
  - Wheat: PARP energy conservation (best single target)
  - Wheat: ADC polyamine-ABA axis
  - Soybean: Invertase inhibitor (best cross-species validation)
  - Soybean: Bradyrhizobium sRNA precedent (Ren et al. 2019)
  - Maize: VP1/ABI40 vivipary anchor (best single-gene phenotype)
```

---

*Analysis based exclusively on evidence from crop-specific mechanistic claims files. No data were invented. Crops lacking gene-level support for specific themes are marked with score 0 or noted as absent. The EPS osmopriming confounder remains the primary alternative hypothesis across all crops; the RNase elimination experiment is the universally recommended discriminating test.*
