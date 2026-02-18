# Confounder Analysis — Quinoa (Chenopodium quinoa)



# Critical Analysis of Potential Confounders in the exRNA Germination Improvement System

## Preamble

This analysis assumes the following experimental setup: *Chenopodium quinoa* seeds are treated with an exopolysaccharide (EPS) solution derived from an M-9 bacterial strain, and the solution contains extracellular small RNAs (exRNAs) proposed to act via antisense targeting of 31 plant transcripts. The observed phenotype is improved germination rate, vigor, and early seedling growth. My goal is to rigorously evaluate what fraction of this phenotype could arise from mechanisms **other than** sequence-specific antisense RNA silencing.

---

## 1. EPS Osmopriming Effect

### Mechanism
[KNOWN] Osmopriming is one of the most well-established seed priming techniques in agriculture. Seeds exposed to osmotic solutions (PEG, mannitol, or polysaccharide solutions) undergo controlled hydration without completing germination (Phase II imbibition arrest), allowing pre-germinative metabolic activation — including DNA repair, mitochondrial biogenesis, mRNA accumulation, and antioxidant system upregulation — before the seed is placed in germination conditions (Paparella et al., 2015, *Plant Cell Reports*; Ibrahim, 2016).

[KNOWN] Bacterial EPS solutions are inherently viscous, high-molecular-weight polysaccharide solutions that exert significant osmotic effects. EPS from *Pseudomonas*, *Bacillus*, *Rhizobium*, and other genera typically have water potentials in the range of −0.5 to −1.5 MPa depending on concentration, which falls squarely in the effective osmopriming range (Chen et al., 2007).

### Expected Magnitude vs. Observed Effect
[KNOWN] Osmopriming alone routinely produces:
- **10–30% increases in germination rate** under normal conditions
- **20–50% increases under stress conditions** (salinity, drought)
- Significant improvements in germination uniformity (reduced T50)
- Enhanced early seedling vigor metrics (root length, shoot length, seedling dry weight)

[INFERRED] This magnitude of effect substantially overlaps with the phenotype described in the quinoa exRNA system. Without knowing the precise fold-change in germination metrics, **osmopriming alone could plausibly account for a large fraction — potentially the majority — of the observed improvement**, particularly if the EPS solution was applied at concentrations that produce meaningful water potential depression.

### Controls Needed
| Control | Purpose |
|---------|---------|
| Heat-denatured EPS solution (autoclaved, same concentration) | Retains osmotic properties, destroys RNA |
| Size-matched polysaccharide solution (e.g., xanthan gum, dextran at matched viscosity/osmolality) | Osmopriming without bacterial-specific elicitor or RNA |
| PEG 6000 at matched water potential | Pure osmopriming control |
| Water-only imbibition at matched duration | Hydropriming baseline |
| EPS solution + RNase A/RNase III treatment | Destroys RNA while retaining all other EPS properties |

**Evidence level for confounding: [KNOWN] — This is the single most likely confounder and must be rigorously excluded.**

---

## 2. Polysaccharide Elicitor Effects

### Known Defense/Growth Priming by Bacterial Polysaccharides
[KNOWN] Bacterial EPS and lipopolysaccharides (LPS) are well-characterized microbe-associated molecular patterns (MAMPs) that trigger pattern-triggered immunity (PTI) in plants. Key findings:

- **EPS from plant-beneficial bacteria** (e.g., *Bacillus subtilis*, *Pseudomonas fluorescens*) can prime systemic defense responses including upregulation of PR genes, callose deposition, and ROS burst modulation (Trdá et al., 2015, *Plant Physiology*; Desaki et al., 2018).
- **β-glucans, peptidoglycans, and other polysaccharide fragments** are recognized by plant LysM-type receptors (e.g., CERK1/LYK5 in Arabidopsis), triggering MAPK cascades and defense gene expression (Gust et al., 2012, *Annual Review of Phytopathology*).
- [KNOWN] Bacterial EPS can also directly stimulate **jasmonic acid (JA) and salicylic acid (SA) signaling**, ethylene biosynthesis, and abscisic acid (ABA) modulation — all of which are central to germination regulation.

### Relevant Plant Receptors and Signaling Pathways
[KNOWN/INFERRED] In the context of quinoa:
- **LysM-RLKs** (receptor-like kinases): Likely present in *C. quinoa* genome (annotated in CqV2 genome assembly), would recognize bacterial polysaccharide fragments
- **WAK (Wall-Associated Kinases)**: Respond to oligogalacturonides and potentially bacterial EPS fragments
- **MAPK cascades** (MPK3/MPK6 orthologs): Downstream of MAMP perception
- **WRKY transcription factors**: Defense-associated, known to cross-regulate germination (e.g., WRKY41 represses ABI3 in Arabidopsis)

### Critical Overlap with Observed Target Gene Changes
[INFERRED] This is a major concern. The 31 reported exRNA targets include genes in:

| Target Pathway | Also Activated by EPS Elicitor? | Overlap Concern |
|---|---|---|
| **Defense/immunity** | YES — direct MAMP response | **HIGH** |
| **Hormone signaling** (ABA, JA, ethylene) | YES — PTI modulates all three | **HIGH** |
| **ROS/redox** | YES — oxidative burst is a primary PTI output | **HIGH** |
| **Epigenetic regulation** | Possible — defense priming involves chromatin remodeling (Jaskiewicz et al., 2011) | **MODERATE** |
| **Transport/ion homeostasis** | Possible — ion fluxes are early PTI events | **MODERATE** |
| **Metabolic priming** | Indirect — defense priming reallocates metabolic resources | **LOW-MODERATE** |

[INFERRED] **The overlap is extensive.** At least 4 of 6 target pathway categories are directly modulated by polysaccharide elicitor perception. This means that changes in transcript levels of these 31 targets could reflect **plant responses to EPS as a MAMP**, not antisense-mediated silencing. Critically, MAMP-triggered transcriptional reprogramming could produce either up- or down-regulation of defense and hormone genes, making it difficult to distinguish from antisense knockdown without strand-specific, target-junction-level evidence.

**Evidence level: [KNOWN] for elicitor effects; [INFERRED] for the degree of overlap with the specific 31-target set.**

---

## 3. Microbiome Effects

### Could the Bacterial Treatment Alter the Seed Microbiome?
[KNOWN] Seeds harbor a complex endophytic and epiphytic microbiome (the "spermosphere") that plays documented roles in germination and seedling establishment (Nelson, 2018, *Annual Review of Phytopathology*; Shade et al., 2017).

[INFERRED] Application of M-9 bacterial EPS solution to quinoa seeds could alter the seed microbiome through several mechanisms:
1. **Direct introduction of viable M-9 bacteria** — unless the preparation is filter-sterilized (0.22 μm) or autoclaved, live bacteria or spores may be present
2. **Selective medium effect** — EPS as a carbon source could selectively enrich certain seed-borne microbes
3. **Competitive exclusion** — bacterial metabolites in the EPS preparation (antibiotics, siderophores, organic acids) could suppress seed-borne pathogens
4. **Biofilm formation** — EPS promotes bacterial biofilm on seed surfaces, altering the physical and chemical microenvironment

### Known Microbiome Effects on Germination
[KNOWN] Specific examples:
- *Pseudomonas* and *Bacillus* spp. produce gibberellins and cytokinins that directly promote germination (Bottini et al., 2004)
- ACC deaminase-producing bacteria lower ethylene levels, modulating germination timing (Glick, 2014)
- Seed-borne fungi (*Fusarium*, *Alternaria*) can inhibit germination; their suppression by applied bacteria improves germination rates independent of any RNA mechanism
- Volatile organic compounds (VOCs) from bacteria (e.g., 2,3-butanediol, acetoin) promote plant growth through ISR (Ryu et al., 2003, *PNAS*)

### Separation from Direct exRNA Mechanism
[INFERRED] This confounder is difficult to separate without:
- Confirming the EPS preparation is **cell-free** (viable count = 0 CFU/mL)
- Characterizing the **metabolome** of the EPS preparation (phytohormones, VOCs, siderophores)
- Performing germination assays under **axenic/gnotobiotic conditions** to eliminate microbiome variables

**Evidence level: [KNOWN] for microbiome effects on germination; [INFERRED] for relevance to this specific system, depending on preparation sterility.**

---

## 4. RNA Stability & Dosage Concerns

### Expected Half-Life of exRNA in the Seed Coat Environment
[KNOWN] Extracellular RNA is highly labile:
- **Naked ssRNA** in biological fluids: half-life of **seconds to minutes** due to ubiquitous RNases (Houseley & Tollervey, 2009)
- **Naked dsRNA** is more stable but still degrades within **minutes to hours** in soil/plant surface environments (Dubelman et al., 2014, *PLOS ONE*: dsRNA T½ in soil ≈ 15–35 hours; on leaf surfaces, faster)
- The **seed coat (testa) of quinoa** is rich in saponins and phenolic compounds that create a harsh chemical environment; additionally, seed imbibition releases RNases as part of normal germination physiology (Rajjou et al., 2012)

[KNOWN] Some bacterial exRNAs are packaged in **outer membrane vesicles (OMVs)** or associated with **RNA-binding proteins** or **EPS matrix**, which can extend half-life significantly (Tsatsaronis et al., 2018). However:
- [INFERRED] The degree of protection in this specific M-9 EPS preparation is unknown
- [SPECULATIVE] If exRNAs are simply dissolved in the EPS solution without vesicular packaging, functional half-life may be very short

### Required Copy Number for Antisense Effect
[KNOWN] For canonical RNAi/PTGS in plants:
- **siRNA-mediated silencing** requires loading into AGO proteins (typically AGO1 in plants) and operates catalytically — one RISC complex can cleave multiple targets
- However, **initial loading** requires sufficient siRNA concentration in the cytoplasm. In transgenic RNAi systems, continuous production from a hairpin construct ensures steady-state levels
- **Exogenous dsRNA application** studies (spray-induced gene silencing, SIGS) typically require **2–20 μg of dsRNA per plant** for detectable gene silencing in leaves (Koch et al., 2016, *PLOS Pathogens*; Mitter et al., 2017, *Nature Plants*)
- For **seed treatment**, the relevant compartment is much smaller, but the RNA must traverse the seed coat and reach the embryo

[INFERRED] Critical quantitative concerns:
1. **What is the total RNA concentration in the EPS preparation?** — Bacterial exRNA in culture supernatants is typically in the **low ng/mL to μg/mL range** (Blenkiron et al., 2016)
2. **What fraction of total exRNA corresponds to the specific 31 antisense sequences?** — Likely a small fraction; each individual antisense species may be present at **pg/mL levels**
3. **How many copies reach the embryo?** — After seed coat barrier, dilution into embryo volume, and RNase degradation, the number of functional antisense molecules per cell may be **extremely low**

[INFERRED] A rough calculation:
- Assume 1 μg/mL total exRNA in EPS solution, 10 μL applied per seed
- Total RNA applied: ~10 ng
- Fraction as specific antisense for one target: ~1/1000 (generous) = 10 pg = ~10⁷ copies of a 21-nt RNA
- Quinoa embryo: ~10⁴–10⁵ cells
- Maximum copies per cell (no losses): ~100–1000
- After degradation and barrier losses (conservatively 99%): **1–10 copies per cell**

[INFERRED] This is at or below the threshold for reliable gene silencing, especially without amplification. In plants, **RDR6-dependent secondary siRNA amplification** can amplify an initial signal, but this requires initial target cleavage and is typically associated with transgene or viral contexts, not exogenous small RNA application.

**Evidence level: [KNOWN] for RNA stability data; [INFERRED] for dosage calculations (order-of-magnitude estimates with stated assumptions); the dosage concern is SERIOUS.**

---

## 5. Non-Specific RNA Effects

### Could Any RNA Sequence Trigger Similar Responses?
[KNOWN] Yes, through multiple mechanisms:

#### 5a. Pattern-Triggered Immunity from dsRNA
[KNOWN] Plants possess **dsRNA receptors** that trigger immune responses independent of sequence:
- **SORE1 (SENSITIVE TO ORAL ELICITATION 1)** — identified in *Arabidopsis* as a receptor for exogenous dsRNA that triggers PTI-like responses including ROS burst, MAPK activation, and defense gene expression (Niehl et al., 2016, *PLOS Pathogens*)
- This response is **sequence-independent** and **length-dependent** (dsRNA >21 bp is more effective)
- [INFERRED] If the M-9 exRNA preparation contains structured RNAs or dsRNA intermediates, these could trigger defense priming and growth modulation **regardless of their antisense complementarity** to quinoa transcripts

#### 5b. RNA as a Phosphorus/Nitrogen Source
[KNOWN] Degraded RNA provides bioavailable phosphorus and nitrogen. During seed imbibition, exogenous nucleotides could serve as:
- Precursors for de novo nucleotide synthesis (salvage pathway)
- Phosphorus source (seeds are often P-limited during early germination)
- Signaling molecules (extracellular ATP/adenosine signaling via DORN1/P2K1 receptor; Choi et al., 2014, *Science*)

#### 5c. RNA-Mediated Modulation of Seed Coat Permeability
[SPECULATIVE] Polyanionic RNA molecules could interact with seed coat components (saponins, tannins) and alter permeability, indirectly affecting imbibition kinetics.

### Controls Required
| Control | What It Tests |
|---------|--------------|
| **Scrambled-sequence RNA** (same length, GC content, structure, but no complementarity to quinoa transcripts) | Sequence-specificity of the effect |
| **RNase A + RNase III pre-treatment** of EPS solution | Eliminates all ssRNA and dsRNA |
| **Poly(I:C)** (synthetic dsRNA analog) at matched concentration | dsRNA-triggered PTI without specific targeting |
| **Yeast total RNA** at matched concentration | Non-specific RNA/nutrient effect |
| **DNase-treated EPS** (to rule out DNA contamination effects) | Eliminates potential DNA-mediated effects |

**Evidence level: [KNOWN] for dsRNA-triggered immunity; [INFERRED] for relevance to this system.**

---

## 6. Contamination Signals

### cry8Ba Bacterial Protein Detected — Implications
[KNOWN] Cry8Ba is a **Bacillus thuringiensis (Bt) crystal protein** — a pesticidal protein active against Coleopteran insects. Its detection in the EPS preparation raises several serious concerns:

#### 6a. Source Identification
[INFERRED] The presence of cry8Ba suggests one or more of the following:
1. **The M-9 strain is a *Bt* strain or *Bt*-related organism** — many *Bacillus* species carry cry genes on plasmids
2. **The EPS preparation is contaminated with *Bt* proteins** from the production environment
3. **The detection is an artifact** (e.g., cross-reactive antibody, misidentified mass spec peptide)

[INFERRED] If the M-9 strain carries cry genes, the entire preparation may contain a complex mixture of bacterial proteins, including:
- Other Cry/Cyt toxins
- Vegetative insecticidal proteins (VIPs)
- Chitinases, proteases, and other secreted enzymes
- Potential **phytohormone-modulating enzymes** (e.g., IAA biosynthesis enzymes common in *Bacillus*)

#### 6b. Biological Implications for Germination
[KNOWN] Bt Cry proteins at high concentrations can have non-target effects:
- **Pore-forming activity** in membranes (not limited to insect midgut at high concentrations)
- [SPECULATIVE] Could potentially affect seed coat membrane permeability during imbibition
- [KNOWN] Bt supernatants contain many bioactive metabolites beyond Cry proteins: lipopeptides (surfactin, iturin, fengycin) that have well-documented **plant growth-promoting** and **antifungal** activities (Ongena & Jacques, 2008, *Trends in Microbiology*)

#### 6c. Quality Control Recommendations
1. **Full proteomics** of the EPS preparation (LC-MS/MS) to identify all bacterial proteins present
2. **Metabolomics** to detect lipopeptides, phytohormones (IAA, cytokinins, gibberellins), siderophores, and VOCs
3. **16S rRNA sequencing** of the M-9 strain to confirm taxonomic identity
4. **Whole-genome sequencing** of M-9 to identify all biosynthetic gene clusters
5. **Endotoxin assay** (LAL or equivalent) to quantify LPS contamination
6. **Viable cell count** (CFU/mL) of the EPS preparation to confirm cell-free status
7. **Electron microscopy** to check for outer membrane vesicles (OMVs) in the preparation

**Evidence level: [KNOWN] for Cry protein biology; [INFERRED] for contamination implications in this specific preparation. The cry8Ba detection is a RED FLAG requiring immediate follow-up.**

---

## Confounder Impact Matrix

| Confounder | Likelihood of Contributing | Impact if True (% of phenotype explained) | Distinguishable from exRNA? | Priority for Control Experiments |
|---|---|---|---|---|
| **EPS osmopriming** | **VERY HIGH** | **30–80%** | Yes, with proper controls | **#1 — CRITICAL** |
| **Polysaccharide elicitor/MAMP effects** | **HIGH** | **10–40%** | Yes, but requires careful design | **#2 — HIGH** |
| **Bacterial metabolite contamination** (lipopeptides, phytohormones, per cry8Ba flag) | **HIGH** | **10–50%** | Yes, with metabolomics + fractionation | **#3 — HIGH** |
| **Non-specific dsRNA immune priming** | **MODERATE-HIGH** | **5–30%** | Yes, with scrambled RNA controls | **#4 — HIGH** |
| **RNA dosage insufficiency** (i.e., antisense mechanism not physically plausible) | **MODERATE-HIGH** | **100%** (mechanism invalid) | Yes, with quantitative RNA analysis | **#5 — HIGH** |
| **Microbiome alteration** | **MODERATE** | **5–20%** | Yes, with axenic systems | **#6 — MODERATE** |
| **Nutrient effect of RNA** (P, N source) | **LOW-MODERATE** | **1–10%** | Yes, with nucleotide controls | **#7 — LOW** |
| **Seed coat permeability alteration** | **LOW** | **1–5%** | Difficult | **#8 — LOW** |

### Critical Note on Additivity
[INFERRED] These confounders are **not mutually exclusive** — they can act additively or synergistically. An EPS preparation simultaneously provides osmotic priming + MAMP elicitation + bacterial metabolites + non-specific RNA effects. The **combined non-antisense effects could plausibly account for 60–100% of the observed phenotype** without invoking any sequence-specific RNA silencing.

---

## Recommended Controls — Prioritized Experimental Program

### Tier 1: Essential (Must be completed before claiming antisense mechanism)

**Experiment 1: RNase Treatment Control**
- Treat EPS solution with RNase A (ssRNA) + RNase III (dsRNA) + Proteinase K (to expose protein-protected RNA), then heat-inactivate enzymes
- Compare germination phenotype: RNase-treated EPS vs. untreated EPS vs. water
- **Expected if antisense is the mechanism:** RNase treatment abolishes the phenotypic improvement beyond the EPS baseline
- **Expected if confounders dominate:** RNase treatment has minimal effect on phenotype

**Experiment 2: Matched Osmotic Control**
- Prepare solutions of commercial xanthan gum, carboxymethylcellulose, or PEG 6000 at matched osmolality and viscosity to the EPS preparation
- Compare germination phenotype
- **Expected if osmopriming dominates:** Similar improvement from all osmotic solutions

**Experiment 3: RNA Quantification and Characterization**
- Extract and quantify total RNA from EPS preparation (Bioanalyzer/TapeStation)
- Perform small RNA sequencing to confirm presence, abundance, and structure of the 31 proposed antisense species
- Calculate copies per seed treatment volume
- **Threshold:** If individual antisense species are below ~10⁶ copies per seed treatment, the dosage argument becomes very difficult to sustain

**Experiment 4: Scrambled RNA Control**
- Synthesize RNA of identical length, GC content, and secondary structure to the proposed antisense RNAs, but with scrambled sequence (no complementarity to quinoa transcripts)
- Add to RNase-treated EPS at the same concentration as endogenous exRNA
- Compare phenotype to untreated EPS
- **Expected if sequence-specific:** Scrambled RNA does not rescue the phenotype lost by RNase treatment

### Tier 2: Strongly Recommended

**Experiment 5: Full Biochemical Characterization of EPS Preparation**
- Proteomics (LC-MS/MS)
- Metabolomics (untargeted LC-MS and GC-MS)
- Phytohormone profiling (IAA, cytokinins, gibberellins, ABA)
- Lipopeptide detection (surfactin, iturin, fengycin)
- Endotoxin/LPS quantification
- Viable cell count

**Experiment 6: Target Transcript Validation**
- RT-qPCR or RNA-seq of the 31 target transcripts in treated vs. control seeds at multiple timepoints during imbibition
- **Critical:** Include RNase-treated EPS control and osmotic control
- If antisense mechanism is real: target transcripts should be **specifically downregulated** in intact EPS treatment but **not** in RNase-treated EPS or osmotic controls
- Perform **5' RACE** on candidate targets to detect AGO-mediated cleavage products at the predicted antisense binding site — this is the **gold standard** for confirming antisense-mediated cleavage

**Experiment 7: Dose-Response with Synthetic Antisense RNA**
- Synthesize the top 3–5 candidate antisense RNAs
- Apply to quinoa seeds at a range of concentrations (1 ng to 100 μg per seed) in water (no EPS)
- Measure germination phenotype and target transcript levels
- **Expected if antisense is the mechanism:** Dose-dependent improvement in germination and dose-dependent reduction in target transcripts

### Tier 3: Informative but Not Essential

**Experiment 8: Axenic Germination System**
- Surface-sterilize seeds and germinate under gnotobiotic conditions
- Apply sterile-filtered EPS vs. controls
- Rules out microbiome-mediated effects

**Experiment 9: Fluorescently Labeled RNA Uptake**
- Apply Cy3- or Cy5-labeled synthetic antisense RNA to seeds
- Track uptake through seed coat into embryo tissues using confocal microscopy
- Confirms whether exogenous RNA physically reaches target cells

**Experiment 10: AGO-Immunoprecipitation**
- IP quinoa AGO1 from treated embryos
- Sequence associated small RNAs
- **If antisense mechanism is real:** Bacterial-derived antisense sequences should be loaded into plant AGO complexes
- This is the most definitive molecular evidence possible

---

## Overall Assessment

[INFERRED] **The current evidence base, as described, is insufficient to attribute the observed germination phenotype to sequence-specific antisense RNA silencing.** The experimental system as described has multiple overlapping confounders — any one of which could account for the observed phenotype — and the most parsimonious explanations (osmopriming, MAMP elicitation, bacterial metabolite effects) do not require invoking a cross-kingdom RNA silencing mechanism.

[INFERRED] The detection of cry8Ba protein is particularly concerning, as it suggests the EPS preparation contains a complex, incompletely characterized mixture of bacterial products with known bioactivity.

[INFERRED] The RNA dosage calculation raises fundamental feasibility concerns. Without quantitative evidence that sufficient copies of specific antisense RNAs reach the embryo cytoplasm and are loaded into AGO complexes, the proposed mechanism remains **physically unsubstantiated**.

[KNOWN] Cross-kingdom RNA silencing has been documented in specific contexts (e.g., *Botrytis cinerea* sRNAs silencing plant immunity genes via host AGO1; Weiberg et al., 2013, *Science*), but these involve **intimate, sustained physical contact** between organisms, **active delivery mechanisms** (OMVs, haustoria), and **evolutionary selection** for effective silencing sequences. A bacterial EPS wash applied to a seed surface represents a fundamentally different — and far less favorable — delivery scenario.

### Bottom Line Estimate
| Component | Estimated Contribution to Phenotype |
|---|---|
| Osmopriming + physicochemical effects | 30–60% |
| MAMP/elicitor signaling | 10–25% |
| Bacterial metabolite contamination | 5–20% |
| Non-specific RNA/immune effects | 2–10% |
| Sequence-specific antisense silencing | **0–15%** (undemonstrated) |

[INFERRED] Until Tier 1 controls are completed — particularly the RNase treatment experiment and the scrambled RNA control — **the null hypothesis that the phenotype is entirely explained by non-RNA confounders cannot be rejected.**