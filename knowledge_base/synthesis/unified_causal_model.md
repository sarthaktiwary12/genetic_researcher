# UNIFIED CAUSAL MODEL: Bacterial exRNA-Mediated Germination Enhancement Across Six Crop Species

**Date**: 2026-02-17
**Crops analyzed**: Spinach (Spinacia oleracea), Broccoli (Brassica oleracea), Maize (Zea mays), Wheat (Triticum aestivum), Quinoa (Chenopodium quinoa), Soybean (Glycine max)
**Status**: Hypothesis under test -- NOT a conclusion

---

## A. UNIFIED CAUSAL MODEL

### Conceptual Framework

Across all six crops, bacterial exRNAs delivered via M-9 EPS solution during seed imbibition are predicted to orchestrate germination improvement through a conserved multi-pathway strategy. Despite wide phylogenetic divergence (monocots vs. eudicots, diploids vs. polyploids, glycophytes vs. halophytes), the same functional themes recur with species-specific mechanistic variations. The unified model describes four sequential phases.

---

### 1. Entry Mechanism: EPS Matrix --> Imbibition Uptake --> AGO Loading

**Step 1 -- EPS as delivery vehicle**: The bacterial extracellular polysaccharide (EPS) matrix encapsulates small RNAs (likely 20-24 nt) in a hydrogel that protects them from extracellular RNases during the 4-8 hour seed soaking period. The EPS may also contain outer membrane vesicles (OMVs) that package sRNAs with RNA-binding proteins, as documented for plant EVs (He et al. 2021, Nature Plants).

**Step 2 -- Imbibition-driven uptake**: During Phase I imbibition (0-6h), rapid water influx through the seed coat carries dissolved and vesicle-associated sRNAs into the embryo. In soybean, the seed coat becomes highly permeable within minutes (Meyer et al. 2007). In quinoa, the saponin-rich seed coat may paradoxically facilitate OMV-membrane fusion through its detergent-like properties. Cell wall loosening during early imbibition creates pores large enough for sRNA-protein complexes (~40-100 kDa).

**Step 3 -- AGO loading**: Once inside plant cells, bacterial sRNAs are loaded into endogenous Argonaute (AGO) protein complexes -- primarily AGO1 for post-transcriptional gene silencing (PTGS) and AGO4 for RNA-directed DNA methylation (RdDM). This step is supported by:
- **Soybean**: Direct experimental precedent -- Ren et al. (2019, Science) demonstrated that Bradyrhizobium japonicum tRNA-derived sRNAs are loaded into soybean AGO1 to regulate nodulation genes
- **Broccoli**: Close phylogenetic proximity to Arabidopsis, where cross-kingdom AGO loading is well-documented (Weiberg et al. 2013; Dunker et al. 2020)
- **Maize**: Comprehensive RNAi toolkit with tissue-specific AGO expression (Qian et al. 2011; Zhai et al. 2014)
- **Quinoa**: Expanded RNAi machinery (21 CqAGO, 8 CqDCL, 11 CqRDR) that may enhance exogenous sRNA processing capacity (Xu et al. 2023)
- **Wheat**: Cross-kingdom RNAi of pathogen effectors demonstrated (Hu et al. 2020)

**Key uncertainty**: The efficiency of bacterial sRNA uptake into seed cells has not been directly measured in any of the six crops during imbibition. The soybean Ren et al. (2019) precedent involves rhizobial colonization during nodulation, not seed imbibition.

---

### 2. Phase 1 (0-6h): Seed Soaking -- ABA Sensitivity Reduction and Immune Dampening

During the soaking period, the earliest-acting sRNA targets are those that reduce ABA sensitivity and begin dampening innate immunity. These represent the "first wave" of silencing because they target signaling components with rapid turnover.

**ABA axis suppression (conserved across all 6 crops)**:

| Crop | Target(s) | Mechanism | Evidence |
|------|-----------|-----------|----------|
| Spinach | Ethylene receptor (SOV3g000150.1), LOX (SOV3g035520.1), Phytoene synthase (SOV4g000330.1) | Ethylene hypersensitivity + cut JA/ABA precursors + starve ABA of carotenoid precursors | Strong (etr1 mutant data) |
| Broccoli | ARF repressor (Bo7g114200.1), CDPK15 (Bo1g025790.1), PP2A-A (Bo9g011330.1) | Suppress ABI3-mediated dormancy + reduce Ca2+-ABA signaling + alter hormone crosstalk | High (ARF-ABI3 pathway known) |
| Maize | ABI40/VP1-like (Zm00001eb197370), NPF15/ABA transporter (Zm00001eb385450), HEX6 (Zm00001eb154520) | Reduce ABA transcriptional output + block ABA import + break glucose-ABA feedback | Highest (VP1 null = vivipary) |
| Wheat | SnRK2 kinase (TraesCS7D02G384400), ADC (TraesCS2A02G071200), BTB/POZ (TraesCS3D02G394800) | Reduce ABA signal transduction + shift polyamine ratio + stabilize PP2Cs | Strong (PKABA1 precedent) |
| Quinoa | CqCNGC14 (AUR62044372), CqGUN4 (AUR62015391) | Dampen Ca2+-dependent ABA reinforcement + alter retrograde ABA signaling | High (CNGC14 function known) |
| Soybean | PLDbeta1 (GLYMA_01G215100), ROP GTPase (GLYMA_09G192700), CKX3 (GLYMA_09G063900) | Reduce PA-mediated ABA amplification + modulate ABA transduction + elevate cytokinins | Strong (PA-ABA link validated) |

**Immune surveillance reduction (conserved across all 6 crops)**:

| Crop | Target(s) | Layer of immunity affected |
|------|-----------|---------------------------|
| Spinach | EDR2 (x2), MOS1, RLKs (x4), R-protein, NST1 | PTI receptors + ETI regulators + defense execution |
| Broccoli | CRK26, CRK29, Chitinase, RDR, ABCG37/PDR9 | PTI receptors (FLS2-associated) + defense effectors + defense compound export |
| Maize | LRR-RLK, PSKR1-like, CML21, MOS1-like | PTI receptors + Ca2+-defense signaling + chromatin-level immune regulation |
| Wheat | 6 F-box proteins, 5 LRR-RLKs, 2 NB-LRRs, 3 ABC transporters, Gnk2, LURP1 | All layers: SCF-mediated immune proteolysis + PTI + ETI + defense compound transport + antimicrobials (24% of all targets) |
| Quinoa | NBS-LRR candidate (AUR62021543), antimicrobial peptides (AUR62040122, AUR62035900), BRL2/VH1-like | ETI + antimicrobial defense + BAK1 co-receptor competition |
| Soybean | TIR-NBS-LRR (GLYMA_06G259700), ERECTA-like RLK (GLYMA_10G242300) | ETI + growth-defense balance receptor + isoflavonoid pathway flux |

**Unified Phase 1 principle**: The bacterial sRNAs create a permissive metabolic state by simultaneously (a) reducing ABA sensitivity through multiple orthogonal mechanisms (transcriptional, transport, signaling, biosynthetic), and (b) suppressing constitutive immune surveillance that would otherwise consume significant ATP, NADPH, amino acids, and carbon skeletons. The defense suppression is particularly pronounced in wheat (24% of targets) and parallels the immune suppression strategy documented for pathogenic Botrytis cinerea (Weiberg et al. 2013), but in a mutualistic context.

---

### 3. Phase 2 (6-24h): Early Imbibition -- Epigenetic Unlocking and ROS Optimization

As the seed transitions from quiescence to active metabolism, a second wave of sRNA effects manifests at the chromatin and redox levels.

**Epigenetic derepression (conserved across 4 of 6 crops)**:

| Crop | Target(s) | Epigenetic mechanism | Germination gene classes derepressed |
|------|-----------|---------------------|-------------------------------------|
| Spinach | DNA methyltransferase (SOV1g033340.1), SUVR5 (SOV4g015450.1), HIRA (SOV6g036290.1), PHD reader (SOV4g030590.1), GIS2 (SOV4g038060.1) | Writers (DNA-me, H3K9me) + reader (PHD) + remodeler (HIRA) + TF (GIS2) -- multi-pronged dismantling of repressive chromatin | GA biosynthesis, cell wall loosening, metabolic reactivation genes |
| Broccoli | MBD10 (Bo8g066360.1), RDR (Bo8g102500.1), TRFL7 (Bo8g114370.1) | Methylation reader (MBD10) + siRNA producer (RDR/RdDM) + PRC2 recruiter (TRFL7) | Germination-promoting genes silenced in dry seeds; reduced RdDM-mediated dormancy |
| Wheat | DDM1 (TraesCS7A02G074600), Bromodomain TF (TraesCS3A02G122200), Homeobox-DDT (TraesCS2A02G124800) | Chromatin remodeling ATPase + acetylated histone reader + chromatin remodeler | Germination genes silenced by DNA methylation during maturation |
| Maize | AHL9 (Zm00001eb065740), MOS1-like (Zm00001eb136860) | AT-hook chromatin remodeler + chromatin-level immune regulator | Auxin biosynthesis (YUCCA9) and growth-promoting genes |

**ROS/redox optimization (conserved across all 6 crops)**:

The "oxidative window" concept (Bailly et al. 2008) posits that germination requires ROS within a defined signaling range -- too low maintains dormancy, too high causes oxidative damage. Across all six crops, targets converge on tuning ROS into this window:

| Crop | Target(s) | ROS modulation mechanism |
|------|-----------|--------------------------|
| Spinach | GST-L3 (SOV3g040200.1), Peroxidase (SOV3g038840.1), 6-PGDH (SOV6g029280.1) | Reduce ROS scavenging (GST) + reduce H2O2 removal/cell wall stiffening (Prx) + reduce NADPH supply for antioxidant systems (6-PGDH) |
| Broccoli | COPT5 (Bo9g151660.1), TrxL2.2 (Bo9g181290.1), CRK26/29 (defense ROS) | Reduce Cu-Fenton ROS (COPT5) + dampen oxidative signaling cascades (TrxL2.2) + prevent defense ROS burst (CRK) |
| Maize | PRX91 (Zm00001eb333290) | Reduce cell wall stiffening at radicle tip + shift toward pro-germination H2O2 signaling |
| Wheat | PARP (TraesCS1A02G328000) | Conserve NAD+ pool (preventing PARP-mediated NAD+ depletion); >10% biomass increase in PARP-deficient plants (De Block et al. 2005) |
| Quinoa | CqCYP76AD-like (AUR62012347) -- betalain pathway | Reduce betalain antioxidant flux, redirecting nitrogen/tyrosine to growth; enzymatic antioxidants (SOD, CAT, APX) compensate |
| Soybean | Glutaredoxin (GLYMA_03G196400) | Alter thiol-disulfide balance; potentially accelerate reductive activation of metabolic enzymes; zeatin riboside from elevated cytokinins acts as superoxide scavenger (Gidrol et al. 1994) |

**Unified Phase 2 principle**: The epigenetic targets remove the chromatin-level "locks" that maintain dormancy programs, while redox targets shift the cellular environment into the germination-permissive oxidative window. These effects are synergistic: epigenetic derepression allows transcription of pro-germination genes, while ROS optimization provides the signaling context for those genes to drive germination.

---

### 4. Phase 3 (24-72h): Radicle Emergence and Early Seedling Growth

The third phase reflects the downstream consequences of Phase 1-2 reprogramming and involves cell wall remodeling, metabolic mobilization, and physical emergence.

**Cell wall modification for radicle protrusion**:

| Crop | Target(s) | Wall modification mechanism |
|------|-----------|----------------------------|
| Spinach | Peroxidase (SOV3g038840.1), CCC cotransporters (x2) | Reduced cell wall stiffening + altered turgor/ion fluxes for expansion |
| Broccoli | PME (Bo7g098960.1), BGAL10 (Bo3g103050.1), GH17 glucanase | Maintain pectin flexibility + (WGT-buffered) xyloglucan modification |
| Maize | PRX91, ZRP4-like O-methyltransferase (Zm00001eb292850) | Reduced cell wall cross-linking + reduced suberin/lignin biosynthesis at radicle tip |
| Wheat | No direct cell wall targets; indirect via ARF-mediated auxin signaling (TraesCS6B02G167100) | Auxin-driven cell elongation and coleoptile growth |
| Quinoa | CqHAK5 (AUR62010943) -- K+ transport paradox | K+ homeostasis for turgor-driven radicle expansion (resolution via allotetraploid buffering or context-dependent efflux) |
| Soybean | CesA4 (GLYMA_09G051100), Invertase/PME inhibitor (GLYMA_05G068700) | Reduced secondary cell wall rigidity + derepressed CWI floods axes with hexose sugars for growth |

**Metabolic mobilization acceleration**:

| Crop | Target(s) | Metabolic effect |
|------|-----------|-----------------|
| Spinach | GDSL esterases (x3), TPS, Aspartokinase | Altered lipid metabolism + recalibrated energy sensing + optimized amino acid flux |
| Broccoli | BCKDH E1-beta (Bo3g185280.1), SBI1 (Bo3g185500.1) | Preserved branched-chain amino acids for protein synthesis + (paradoxical) RFO mobilization |
| Maize | HEX6 (Zm00001eb154520), MYBR64 (Zm00001eb187270) | Break glucose-ABA feedback + derepress starch mobilization = "full throttle" metabolic state |
| Wheat | SQD1 (TraesCS1D02G241800), PARP (TraesCS1A02G328000) | Redirect UDP-glucose to glycolysis + conserve NAD+/ATP for biosynthesis |
| Quinoa | GUN4 (AUR62015391) -- chloroplast metabolism delay | Accept transient greening delay in exchange for accelerated germination timing |
| Soybean | Invertase inhibitor (GLYMA_05G068700), CKX3 (GLYMA_09G063900) | Elevated hexose sugars + elevated cytokinins = "sugar is abundant, divide and grow" |

**Unified Phase 3 principle**: The cell wall and metabolic targets ensure that the hormonal and epigenetic reprogramming from Phases 1-2 translates into physical radicle emergence and vigorous early growth. The specific targets vary by species (reflecting differences in seed anatomy -- perisperm in quinoa, aleurone in wheat, cotyledons in soybean) but converge on the same functional outcome: reduced mechanical barriers and accelerated energy mobilization.

---

### Unified Model Summary Diagram

```
PHASE 0 (0h): Bacterial sRNAs in EPS matrix --> imbibition uptake --> AGO loading
         |
PHASE 1 (0-6h): Two simultaneous first-wave effects
         |
         |--- ABA AXIS SUPPRESSION (all 6 crops)
         |    Spinach: Ethylene receptor + LOX + Phytoene synthase
         |    Broccoli: ARF + CDPK15 + PP2A
         |    Maize: ABI40/VP1 + NPF15/ABA transporter + HEX6
         |    Wheat: SnRK2 + ADC + BTB/POZ
         |    Quinoa: CNGC14 + GUN4
         |    Soybean: PLDbeta1 + ROP + CKX3
         |
         |--- IMMUNE DAMPENING (all 6 crops)
         |    Spinach: EDR2(x2) + MOS1 + RLKs + R-protein
         |    Broccoli: CRK26/29 + Chitinase + RDR + ABCG37
         |    Maize: LRR-RLK + CML21 + MOS1-like
         |    Wheat: F-box(x6) + LRR-RLK(x5) + NB-LRR(x2) + ABC(x3)
         |    Quinoa: NBS-LRR + AMPs + BRL2/VH1
         |    Soybean: TIR-NBS-LRR + ERECTA-like
         |
PHASE 2 (6-24h): Second-wave effects on chromatin and redox
         |
         |--- EPIGENETIC UNLOCKING (4/6 crops)
         |    Spinach: DNA-MTase + SUVR5 + HIRA + PHD + GIS2
         |    Broccoli: MBD10 + RDR + TRFL7
         |    Maize: AHL9 + MOS1-like (chromatin)
         |    Wheat: DDM1 + Bromodomain + Homeobox-DDT
         |
         |--- ROS WINDOW OPTIMIZATION (all 6 crops)
         |    [Species-specific targets converge on
         |     beneficial oxidative signaling range]
         |
PHASE 3 (24-72h): Physical emergence and vigor
         |
         |--- CELL WALL LOOSENING (species-specific)
         |--- RESERVE MOBILIZATION (species-specific)
         |--- RADICLE PROTRUSION + SEEDLING GROWTH
```

---

## B. ALTERNATIVE MODELS

### Alternative Model 1: EPS Osmopriming Model

**Description**: The bacterial EPS solution functions as a classical osmopriming agent. The hydrogel matrix provides controlled hydration kinetics, preventing imbibition injury and allowing metabolic pre-activation before full germination. The RNA molecules in the preparation are biologically inert bystanders -- coincidental nucleic acid content with no functional role in the germination phenotype. This is the null hypothesis for the exRNA model and must be excluded before any RNA-specific claims can be supported.

**What it explains well**:
- Germination rate improvement: Osmopriming with PEG, methylcellulose, and polysaccharide gels is well-established across all six crops, with decades of literature documenting 10-30% germination rate improvements
- Seedling vigor increase: Primed seeds show faster metabolic reactivation, more uniform emergence, and enhanced stress tolerance
- Cross-species universality: Osmopriming works on essentially all crops, regardless of phylogeny, matching the cross-species pattern observed
- The 4-8 hour soaking protocol is precisely the standard osmopriming window
- EPS-specific benefits: EPS hydrogel maintains hydrated film, distributes water uniformly, prevents desiccation stress, and may release trace nutrients

**What it fails to explain**:
- Target-specific transcript downregulation (if demonstrated by RT-qPCR)
- The specific, coordinated suppression of defense, epigenetic, and hormonal pathways at the molecular level
- Any dose-response relationship that differs from simple osmotic effects
- Strain specificity (if M-9 EPS performs differently from other bacterial EPS at equivalent water potential)
- Sequence-dependent effects (if scrambled dsRNA performs differently from target-specific sRNAs)

**Key assumptions**:
- Bacterial sRNAs in the EPS are degraded by apoplastic and intracellular RNases before reaching AGO complexes
- The antisense complementarity between bacterial sRNAs and plant transcripts is coincidental in a large genome
- All gene expression changes in treated seeds are secondary consequences of altered hydration status

---

### Alternative Model 2: MAMP Elicitor Model

**Description**: The bacterial EPS polysaccharides are recognized by plant pattern recognition receptors (PRRs) as microbe-associated molecular patterns (MAMPs), triggering a mild, transient defense response. This defense priming creates a hormetic effect -- a mild stress that paradoxically enhances subsequent growth and germination by pre-activating metabolic and stress-response machinery. The RNA content is irrelevant; the polysaccharide is the active agent.

**What it explains well**:
- The universal defense gene expression changes observed across crops: MAMP perception would activate then subsequently downregulate defense genes as the transient response wanes
- Cross-species generality: MAMP perception is deeply conserved across all angiosperms
- Metabolic acceleration: Defense priming activates mitochondrial respiration, ROS management, and protein synthesis
- The observation that some "defense downshift" genes are downregulated: post-priming return to baseline could look like suppression relative to un-primed controls
- EPS-specific effects: Bacterial EPS (beta-glucans, lipopolysaccharides) are well-documented MAMPs (Boller and Felix 2009)

**What it fails to explain**:
- Antisense sequence specificity: MAMP responses are sequence-independent -- they should not produce target-specific mRNA changes
- The downregulation of non-defense genes (epigenetic modifiers, hormone regulators, metabolic enzymes) that are not part of canonical MAMP responses
- Why 24% of wheat targets are immune genes being *downregulated* rather than *upregulated* (MAMP perception would initially *upregulate* defense)
- Species-specific target sets: MAMP perception activates the same core signaling cascade (BAK1-BIK1-MAPK) in all species, not different gene sets
- The downregulation of RDR in broccoli, which would impair rather than enhance MAMP-triggered silencing responses

**Key assumptions**:
- EPS polysaccharides contain MAMP-active structures (beta-glucan, LPS fragments)
- Plant PRRs in seeds are active during imbibition (not established for most species)
- The hormetic dose-response window produces net benefit rather than net cost
- All target gene changes reflect MAMP-induced transcriptional reprogramming, not sRNA-directed silencing

---

### Alternative Model 3: Microbiome/PGPR Model

**Description**: The M-9 EPS preparation contains viable bacteria (or bacterial metabolites) that act as plant growth-promoting rhizobacteria (PGPR). These bacteria produce phytohormones (IAA, cytokinins, gibberellins), ACC deaminase (lowering ethylene), siderophores, and volatile organic compounds that directly stimulate germination. The germination improvement is a classical biopriming effect, not an RNA interference phenomenon.

**What it explains well**:
- Germination rate and vigor improvements matching documented biopriming effects: Miljakovic et al. (2022) showed Bradyrhizobium japonicum + Bacillus megaterium biopriming improves soybean germination; Griesbach et al. (2024) documented PGPR effects on broccoli
- Phytohormone production: Bacillus, Pseudomonas, and other PGPR genera produce IAA, cytokinins, gibberellins that directly shift the ABA/GA ratio
- ACC deaminase activity: Bacterial ACC deaminase converts the ethylene precursor ACC to alpha-ketobutyrate, reducing ethylene-mediated germination inhibition under stress
- Species-universal effects: PGPR biopriming works across all major crops
- The 100% Bacillus endophyte colonization in quinoa seeds (Pankievicz et al. 2016) suggests pre-adapted bacterial-seed interactions

**What it fails to explain**:
- Target-specific mRNA downregulation (if demonstrated)
- Effects that persist after filter-sterilization (0.22 um) of the EPS preparation
- Sequence-specific responses distinguishing target sRNAs from scrambled controls
- The pattern of immune gene suppression (PGPR typically *induce* ISR rather than suppress defense)
- Why purified RNA fraction would have any effect (sufficiency test)

**Key assumptions**:
- The EPS preparation contains viable, metabolically active bacteria
- Bacterial colonization occurs during the 4-8 hour soaking period
- Phytohormone concentrations in the EPS are biologically significant
- Gene expression changes reflect bacterial metabolite signaling rather than sRNA silencing

---

### Alternative Model 4: Non-specific RNA Model (Immune Hormesis)

**Description**: Foreign double-stranded RNA (dsRNA) from bacteria is detected by plant innate immune sensors, triggering a non-specific RNA-activated defense/hormesis response. The critical feature is that ANY foreign dsRNA would produce the same effect -- the nucleotide sequence is irrelevant. The response involves transient activation of RNAi machinery, metabolic mobilization associated with defense priming, and subsequent enhanced growth as a hormetic rebound.

**What it explains well**:
- The broad spectrum of gene expression changes: a non-specific dsRNA response could pleiotropically affect many pathways
- Cross-species universality: dsRNA sensing is conserved in plants (DCL proteins process exogenous dsRNA in all angiosperms)
- Defense gene suppression: post-hormetic rebound could suppress defense genes relative to controls
- RDR downregulation in broccoli: if the plant's RNAi system is overwhelmed by exogenous dsRNA, negative feedback could suppress RDR expression
- The observation that some targets are paradoxical (harmful if silenced): in a non-specific model, these are simply collateral effects of broad dsRNA-triggered responses

**What it fails to explain**:
- Antisense complementarity between bacterial sRNAs and specific plant targets: if the response is non-specific, why do the bacterial sRNAs show antisense alignment to functionally coherent gene sets?
- Differential effects of target-specific vs. scrambled dsRNA (critical experiment)
- The observation that the same functional themes (ABA suppression, defense downshift, epigenetic unlocking) recur across species with different target genes: a non-specific response would produce species-independent (not species-specific) gene changes
- Dose-response at very low RNA concentrations below the dsRNA sensing threshold
- Why degradome sequencing (PARE) would show cleavage at predicted sRNA target sites

**Key assumptions**:
- Plant cells can detect and respond to exogenous dsRNA during imbibition
- The dsRNA concentration in EPS is sufficient to trigger innate immune detection
- The hormetic response window produces net germination benefit
- Antisense complementarity is coincidental and does not contribute to the phenotype

---

## C. DISCRIMINATING EXPERIMENTS

### Universal First-Line Test: THE KILLER EXPERIMENT (RNase Treatment)

**Experiment name**: RNase Elimination Test

**Protocol**:
1. Prepare M-9 EPS solution as standard
2. Split into four aliquots:
   - (A) Untreated EPS (positive control)
   - (B) EPS + RNase A (100 ug/mL, 37C, 1 hour) -- destroys RNA
   - (C) EPS + heat-inactivated RNase A (95C, 15 min before addition) -- controls for RNase protein/buffer effects
   - (D) Water only (negative control)
3. Treat seeds (n=50 per treatment, 4 biological replicates, 6 crops)
4. Soak 4-8 hours at standard conditions
5. Score germination (radicle emergence >= 2 mm) at 24, 48, 72, 96 hours
6. Measure seedling fresh weight and radicle length at 7 days

**Predicted outcome under RNA model**: B approximately equal to D << A approximately equal to C. RNase destroys the active RNA component; germination improvement is abolished. Heat-inactivated RNase does not destroy RNA, so improvement persists.

**Predicted outcome under Osmopriming model**: A approximately equal to B approximately equal to C >> D. RNase has no effect because the polysaccharide matrix (not RNA) is the active agent.

**Predicted outcome under MAMP model**: A approximately equal to B approximately equal to C >> D. Same as osmopriming -- the polysaccharide MAMP is unaffected by RNase.

**Predicted outcome under PGPR model**: Depends on whether RNase treatment kills bacteria. If EPS is cell-free, A approximately equal to B approximately equal to C >> D.

**Predicted outcome under Non-specific RNA model**: B approximately equal to D << A approximately equal to C. Same as RNA model -- any dsRNA destruction would abolish the effect.

**Cost estimate**: $200-500 per crop; $1,200-3,000 for all 6 crops
**Timeline**: 2-3 weeks per crop; 4-6 weeks for all 6 crops run in parallel
**Decision value**: CRITICAL. This is the go/no-go experiment. If RNase has no effect, the entire RNA hypothesis is falsified. If RNase abolishes the effect, it eliminates osmopriming, MAMP, and PGPR models (but does not distinguish RNA model from non-specific RNA model).

---

### Experiment 2: RNA Model vs. Osmopriming Model

**Experiment name**: Polymer Substitution Test

**Protocol**:
1. Prepare five treatments at matched water potential (water activity):
   - (A) M-9 EPS (full treatment)
   - (B) PEG-6000 solution (equivalent water activity, no RNA, no bacterial components)
   - (C) Methylcellulose gel (equivalent water activity, no RNA)
   - (D) Autoclaved EPS (destroys RNA secondary structure, partially degrades polysaccharides)
   - (E) Water only
2. Measure water activity of all solutions with aw meter
3. Soak seeds, score germination and vigor as in Experiment 1
4. Perform RT-qPCR on top 5 target genes per crop at 12h and 24h

**Predicted outcome under RNA model**: A >> B approximately equal to C approximately equal to D approximately equal to E. Only the intact EPS with functional sRNAs produces the full effect. Target genes are downregulated only in treatment A.

**Predicted outcome under Osmopriming model**: A approximately equal to B approximately equal to C approximately equal to D >> E. Any polymer at equivalent water potential works. No target-specific gene changes.

**Cost estimate**: $500-1,000 per crop; $3,000-6,000 for all 6 crops
**Timeline**: 3-4 weeks
**Decision value**: HIGH. Directly distinguishes RNA-mediated from physical priming effects. The RT-qPCR component provides molecular evidence for or against target-specific silencing.

---

### Experiment 3: RNA Model vs. MAMP Elicitor Model

**Experiment name**: Sequence Specificity Test

**Protocol**:
1. Prepare five treatments:
   - (A) M-9 EPS (full treatment)
   - (B) EPS + synthetic dsRNA mimics targeting top 3 predicted target genes (21-nt duplexes with transfection reagent)
   - (C) EPS + scrambled dsRNA (same length, GC content, and concentration but randomized sequence) + transfection reagent
   - (D) Purified EPS polysaccharide fraction (RNA-depleted by RNase treatment + phenol-chloroform extraction)
   - (E) Water + transfection reagent (vehicle control)
2. Score germination, vigor, and target gene expression by RT-qPCR

**Predicted outcome under RNA model**: A approximately equal to B >> C approximately equal to D approximately equal to E. Sequence-specific dsRNA mimics reproduce the effect; scrambled dsRNA does not; purified polysaccharide alone does not. Target genes downregulated in A and B but not C.

**Predicted outcome under MAMP model**: A approximately equal to D >> B approximately equal to C approximately equal to E. The polysaccharide fraction (not RNA) drives the effect. Synthetic dsRNA alone has no impact.

**Cost estimate**: $2,000-5,000 per crop (includes dsRNA synthesis at ~$200-500 per sequence)
**Timeline**: 4-6 weeks
**Decision value**: VERY HIGH. This is the definitive sequence-specificity test. If scrambled dsRNA performs equivalently to target-specific dsRNA, the non-specific RNA model gains support over the sequence-specific RNA model.

---

### Experiment 4: RNA Model vs. PGPR Model

**Experiment name**: Live Bacteria Elimination Test

**Protocol**:
1. Prepare five treatments:
   - (A) M-9 EPS (full preparation)
   - (B) Filter-sterilized EPS (0.22 um filtration -- removes all viable bacteria; retains RNA, polysaccharides, small molecules)
   - (C) UV-sterilized EPS (254 nm, 30 min -- kills bacteria but degrades RNA)
   - (D) Heat-sterilized EPS (121C, 15 min -- kills bacteria, denatures RNA and some polysaccharides)
   - (E) Water only
2. Plate each treatment on nutrient agar to confirm sterility of B, C, D
3. Score germination and vigor
4. Measure phytohormone content (IAA, CK, GA, ABA) of all EPS preparations by LC-MS/MS
5. Perform RT-qPCR on top 5 targets at 24h

**Predicted outcome under RNA model**: A approximately equal to B >> C approximately equal to D approximately equal to E. Filter-sterilized EPS retains sRNAs and full activity. UV-sterilized EPS loses RNA function. Target genes downregulated in A and B.

**Predicted outcome under PGPR model**: A >> B approximately equal to C approximately equal to D approximately equal to E. Removing live bacteria (by any method) abolishes the effect.

**Cost estimate**: $1,000-2,000 per crop; $6,000-12,000 for all 6 crops (includes LC-MS/MS phytohormone profiling)
**Timeline**: 3-5 weeks
**Decision value**: HIGH. Distinguishes bacterial metabolite effects from molecular cargo effects. LC-MS/MS data on phytohormone content of EPS preparations is independently valuable.

---

### Experiment 5: RNA Model vs. Non-specific RNA Model

**Experiment name**: Degradome Sequencing (PARE) + AGO Immunoprecipitation

**Protocol**:
1. Treat seeds with M-9 EPS; collect embryos at 12h and 24h post-imbibition
2. Perform degradome sequencing (Parallel Analysis of RNA Ends; German et al. 2008) on treated vs. untreated embryos
3. Perform AGO1 immunoprecipitation followed by sRNA sequencing (AGO-RIP-seq) at 24h
4. Map degradome cleavage sites to predicted sRNA target positions
5. Map AGO1-bound sRNAs to bacterial genome; confirm bacterial origin

**Predicted outcome under RNA model**: Degradome shows specific cleavage events at predicted sRNA target sites (5' end of cleaved mRNA maps to position 10-11 of the complementary sRNA). AGO1-bound fraction contains bacterial-origin sRNAs mapping to the M-9 genome.

**Predicted outcome under Non-specific RNA model**: No enrichment of cleavage at predicted target sites. AGO1 may contain bacterial sRNAs but they do not produce site-specific cleavage. Degradome changes are diffuse and pathway-nonspecific.

**Cost estimate**: $5,000-15,000 per crop (degradome-seq + AGO-RIP-seq)
**Timeline**: 6-10 weeks
**Decision value**: DEFINITIVE. This is the gold-standard experiment for proving sequence-specific, AGO-mediated gene silencing by exogenous sRNAs. If degradome shows target-site-specific cleavage, the RNA model is strongly supported. If not, the non-specific RNA model or alternative models gain support.

---

### Experiment Priority and Decision Tree

```
Step 1: RNase Elimination Test (Experiment 1)
  |
  |-- RNA NOT required --> STOP. Osmopriming or MAMP model.
  |                         Proceed to Polymer Substitution (Exp 2).
  |
  |-- RNA IS required --> Proceed to Step 2
  |
Step 2: Polymer Substitution Test (Experiment 2)
  |
  |-- Polymers work equivalently --> Osmopriming + RNA combined model
  |
  |-- Only EPS works --> Proceed to Step 3
  |
Step 3: Live Bacteria Elimination (Experiment 4) + Sequence Specificity (Experiment 3)
  |
  |-- Filter-sterilized retains activity --> Not PGPR.
  |-- Scrambled dsRNA = target dsRNA --> Non-specific RNA model.
  |-- Target dsRNA >> scrambled --> Sequence-specific RNA model.
  |
Step 4: Degradome + AGO-RIP-seq (Experiment 5)
  |
  |-- Target-site cleavage confirmed --> SEQUENCE-SPECIFIC exRNA MODEL VALIDATED
  |-- No specific cleavage --> Re-evaluate; non-specific or combined model
```

---

## D. MODEL COMPARISON TABLE

| Feature | RNA Model (sequence-specific silencing) | EPS Osmopriming | MAMP Elicitor | PGPR/Microbiome | Non-specific RNA (immune hormesis) |
|---------|----------------------------------------|-----------------|---------------|-----------------|-----------------------------------|
| **Target specificity** | High: specific mRNAs downregulated at predicted sRNA binding sites | None: gene expression changes secondary to hydration | Low: canonical MAMP response genes only | Low: phytohormone-responsive genes only | Low: broad pleiotropic effects from dsRNA sensing |
| **Dose-response** | Correlates with sRNA concentration in EPS | Correlates with water potential / polymer concentration | Correlates with MAMP (polysaccharide) concentration | Correlates with viable bacterial count | Correlates with total dsRNA mass, not sequence |
| **RNase sensitivity** | YES: RNase abolishes effect | NO: polysaccharide unaffected | NO: polysaccharide unaffected | NO (unless RNase kills bacteria, unlikely) | YES: RNase abolishes effect |
| **Sequence dependence** | YES: scrambled dsRNA fails; target-specific dsRNA succeeds | NO | NO | NO | NO: any dsRNA of similar size should work |
| **Cross-species transferability** | Partial: same sRNAs may not have complementary targets in all genomes; species-specific target sets predicted | Universal: any polymer works on any crop | Universal: MAMP perception conserved | Universal: PGPR work across crops | Universal: dsRNA sensing conserved |
| **Temporal dynamics** | sRNA effects wane as exogenous RNAs degrade (24-72h); transient window matching imbibition | Priming effect persists through metabolic memory | Transient defense activation then return to baseline | Continuous while bacteria are viable | Transient dsRNA sensing response |
| **Degradome signature** | Specific cleavage at sRNA-mRNA duplex position 10-11 | No specific cleavage events | No sRNA-directed cleavage; defense gene induction | No sRNA-directed cleavage | No target-site-specific cleavage |
| **AGO loading** | Bacterial sRNAs found in AGO1/AGO4 immunoprecipitate | No foreign sRNAs in AGO complexes | No foreign sRNAs in AGO complexes | No foreign sRNAs in AGO complexes | Bacterial sRNAs in AGO but without sequence-specific silencing |
| **Strain specificity** | YES: different bacterial strains produce different sRNA repertoires targeting different genes | NO: any polysaccharide gel works | Partial: different MAMPs trigger different response intensities | YES: different PGPR strains have different metabolic capabilities | NO: any dsRNA source should work |
| **Explains paradoxical targets** | Partially: some may be false positives; polyploid buffering explains some | N/A | N/A | N/A | YES: non-specific effects naturally produce some harmful collateral |
| **Explains defense downshift** | YES: targeted suppression of immune genes mirrors Botrytis cinerea cross-kingdom RNAi | Only as hydration-secondary effect | Partially: post-MAMP rebound could suppress defense | NO: PGPR typically induce ISR (systemic resistance) | Partially: dsRNA hormesis could suppress defense post-rebound |
| **Explains epigenetic changes** | YES: sRNA-directed RdDM via AGO4 pathway; specific chromatin modifiers targeted | NO | NO | NO | Partially: dsRNA could trigger non-specific RdDM |
| **Precedent strength** | Strong: Ren et al. 2019 (bacteria-to-soybean sRNA transfer); Weiberg et al. 2013 (fungi-to-plant); Cai et al. 2018 (plant-to-fungus) | Very strong: decades of priming literature | Moderate: MAMP perception well-characterized but seed-stage perception poorly studied | Strong: biopriming literature extensive | Weak: non-specific dsRNA sensing in seeds not documented |
| **Falsification criterion** | No target-site cleavage in degradome; no bacterial sRNAs in AGO-IP; scrambled dsRNA equals target dsRNA | RNase abolishes effect; target genes specifically downregulated | Target-specific gene changes not explained by MAMP pathway; sequence-specific dsRNA outperforms scrambled | Filter-sterilized EPS retains full activity | Scrambled dsRNA equals target dsRNA in all assays |
| **Parsimony** | Low: requires multiple untested assumptions (uptake, AGO loading, silencing efficiency) | Highest: simplest mechanistic explanation | Moderate | High: well-established mechanism | Moderate: requires dsRNA sensing but not sequence specificity |
| **Commercial potential** | Highest: if validated, enables rational design of crop-specific sRNA formulations | Moderate: commodity product (any polymer) | Low: generic elicitor | Moderate: PGPR products already commercial | Low: any dsRNA works equally |

---

## Honest Assessment of Uncertainties

1. **The RNA model is the hypothesis being tested, not a conclusion.** No experiment has yet demonstrated that bacterial sRNAs from M-9 EPS are loaded into plant AGO complexes during seed imbibition in any of the six crops.

2. **Osmopriming remains the most parsimonious explanation.** Until the RNase elimination test is performed, we cannot exclude the possibility that 100% of the germination improvement comes from the polysaccharide matrix.

3. **Target predictions are bioinformatic, not experimental.** The antisense complementarity between bacterial sRNAs and plant transcripts has not been validated by RT-qPCR, degradome sequencing, or any other experimental method in any crop. False positive rates in sRNA target prediction are high, especially in large polyploid genomes (wheat: ~17 Gb; maize: ~2.3 Gb).

4. **Paradoxical targets exist in every crop.** In wheat, AOX and BOP1 downregulation should be detrimental. In broccoli, BGAL10 and SBI1 downregulation is counterproductive. In quinoa, CqHAK5 silencing should impair germination. In maize, PRH130/PP2C32 downregulation should increase ABA sensitivity. These paradoxical targets could indicate: (a) false positive predictions, (b) polyploid buffering, (c) context-dependent functions that differ from model species, or (d) minor costs overwhelmed by benefits from other targets.

5. **The defense downshift may be a bacterial self-interest strategy rather than a mutualistic germination-promoting mechanism.** Suppressing plant immunity benefits the bacteria regardless of whether it helps the seed. The "mutualistic" framing is aspirational, not proven.

6. **No fold-change data exist.** All predictions are binary (targeted vs. not targeted). We do not know whether the predicted silencing achieves 10%, 50%, or 90% knockdown -- and the biological consequences differ dramatically across this range.

7. **The sRNA uptake mechanism remains the weakest link.** How bacterial sRNAs traverse the seed coat, cell wall, and plasma membrane to reach the cytoplasm and nucleus is unknown. The EPS matrix may facilitate this (OMV-mediated delivery, imbibition-driven bulk flow), but no direct evidence exists for sRNA uptake during seed imbibition in any crop system.

---

*This unified causal model integrates mechanistic claims from 6 crop-specific analyses totaling >300 individual gene targets. It should be treated as a comprehensive hypothesis-generating framework, not as established fact. The discriminating experiments outlined above provide a clear decision tree for validating or falsifying the RNA model relative to alternatives.*

*Report generated: 2026-02-17*
