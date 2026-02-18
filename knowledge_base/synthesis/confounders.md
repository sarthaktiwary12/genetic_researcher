# Confounder Analysis



# Critical Analysis of Potential Confounders in the exRNA Germination Improvement System

## Preamble: Framing the Problem

The central claim — that bacterially-derived extracellular small RNAs (exRNAs) enter *Spinacia oleracea* seeds and modulate germination via antisense targeting of 109 plant transcripts — is a mechanistically bold hypothesis. Cross-kingdom RNA interference (ckRNAi) is documented but remains contentious regarding efficiency, dosage requirements, and biological relevance outside a few well-characterized systems (*Cai et al., 2018, Science; Shahid et al., 2018, Nature*). The EPS delivery matrix introduces multiple confounders that could independently or synergistically account for part or all of the observed phenotype. This analysis systematically dissects each.

---

## 1. EPS Osmopriming Effect

### Mechanism
**[KNOWN]** Exopolysaccharides (EPS) are high-molecular-weight hydrophilic polymers (typically >10⁶ Da) that form viscous, hydrated matrices. When applied to seeds, EPS solutions create a controlled water potential environment functionally equivalent to hydropriming or osmopriming.

- **Osmopriming** is one of the most well-established seed enhancement technologies. Seeds imbibe water slowly under reduced water potential (typically −0.5 to −1.5 MPa), allowing pre-germinative metabolic activation (Phase II of imbibition) without radicle protrusion. Upon transfer to favorable conditions, primed seeds germinate faster and more uniformly (*Paparella et al., 2015, Plant Cell Reports*). **[KNOWN]**
- Bacterial EPS solutions, depending on concentration, can generate osmotic potentials in the range relevant for priming. Xanthan gum, alginate, and other microbial EPS are used commercially as seed coating agents precisely for this water-management property. **[KNOWN]**
- The viscous EPS matrix would also slow oxygen diffusion, potentially reducing oxidative damage during early imbibition — a known contributor to improved germination vigor. **[INFERRED]**

### Expected Magnitude vs. Observed Effect
- **[KNOWN]** Osmopriming alone typically improves germination rate by 10–30% in suboptimal conditions and reduces mean germination time (T₅₀) by 12–48 hours in species like spinach, lettuce, and tomato (*Heydecker & Coolbear, 1977; Bradford, 1986*).
- Spinach (*S. oleracea*) is particularly responsive to priming because its fruit coat (pericarp) contains germination inhibitors (oxalates, phenolics) and creates physical/chemical barriers. Any treatment that modulates water uptake kinetics can have outsized effects. **[KNOWN]**
- **Critical point:** If the observed germination improvement falls within the 10–30% range achievable by osmopriming alone, the exRNA hypothesis is not required to explain the phenotype. **[INFERRED]**

### Controls Needed
1. **EPS-only control (heat-denatured/RNase-treated):** Identical EPS preparation treated with RNase A/T1 cocktail + Proteinase K to destroy RNA and protein while preserving polysaccharide structure and osmotic properties.
2. **Osmotic equivalent control:** PEG-6000 or PEG-8000 solution calibrated to identical water potential as the EPS preparation.
3. **Commercial EPS control:** Xanthan gum or bacterial alginate at equivalent viscosity/concentration.
4. **Water potential measurement:** Direct measurement of EPS solution Ψ using a vapor pressure osmometer (e.g., WP4C Dewpoint Potentiometer).

### Evidence Level: **[KNOWN]** that EPS can osmoprime; **[INFERRED]** that this specific preparation does so; magnitude comparison **not yet determinable** without quantitative phenotype data and water potential measurements.

---

## 2. Polysaccharide Elicitor Effects

### Known Defense/Growth Priming by Bacterial Polysaccharides
**[KNOWN]** Bacterial EPS and their oligosaccharide fragments are well-characterized microbe-associated molecular patterns (MAMPs) / damage-associated molecular patterns (DAMPs) that trigger plant innate immune signaling:

- **Oligogalacturonides (OGs)**, chitooligosaccharides, and bacterial EPS fragments are recognized by plant pattern recognition receptors (PRRs), including Wall-Associated Kinases (WAKs), LysM-domain receptor kinases (e.g., *CERK1/LYK5*), and leucine-rich repeat receptor kinases (LRR-RKs). **[KNOWN]**
- EPS from *Bacillus* spp., *Pseudomonas* spp., and other PGPR activate Induced Systemic Resistance (ISR) pathways involving jasmonic acid (JA) and ethylene (ET) signaling, often through *MYC2*, *NPR1*-independent pathways, and WRKY transcription factors. **[KNOWN]** (*Pieterse et al., 2014, Annual Review of Phytopathology*)
- **Priming of defense** (sensitization without full activation) leads to faster and stronger responses upon subsequent challenge — this is a well-documented epigenetic phenomenon involving histone modifications (H3K4me3, H3K27me3) at defense gene loci. **[KNOWN]** (*Conrath et al., 2015, Annual Review of Phytopathology*)

### Relevant Plant Receptors and Signaling Pathways
- **WAK1/WAK2** — pectin/OG receptors; activate MAPK cascades (MPK3/MPK6)
- **CERK1 (CHITIN ELICITOR RECEPTOR KINASE 1)** — chitin and peptidoglycan recognition
- **FLS2/BAK1** — if any flagellin contamination exists in EPS preparation
- **PEPR1/PEPR2** — endogenous peptide danger signals that amplify PTI
- Downstream: **MAPK cascades → WRKY TFs → defense gene expression; Ca²⁺ signaling → CDPK activation → ROS burst via RBOHD/F**

### Critical Overlap with Observed Target Gene Changes
This is where the confounder becomes most problematic. The reported exRNA target pathways include:

| Reported exRNA Target Pathway | Also Activated by EPS Elicitation? | Overlap Severity |
|---|---|---|
| Hormone signaling (JA, ET, ABA, GA) | **Yes** — ISR activates JA/ET; defense-growth tradeoffs alter ABA/GA balance | **HIGH** |
| Defense/immunity | **Yes** — direct MAMP/elicitor activation | **VERY HIGH** |
| Epigenetic regulation | **Yes** — defense priming involves chromatin remodeling | **HIGH** |
| ROS/redox | **Yes** — MAMP perception triggers RBOH-dependent oxidative burst | **HIGH** |
| Transport/ion homeostasis | **Yes** — Ca²⁺ influx, K⁺/H⁺ exchange during PTI | **MODERATE** |
| Metabolic priming | **Yes** — callose synthesis, phenylpropanoid pathway activation | **MODERATE** |

**[INFERRED]** The overlap between EPS elicitor-triggered transcriptional changes and the reported exRNA target pathways is extensive — potentially 60–80% of the "medium" and "low" priority targets could show expression changes from polysaccharide elicitation alone, without any RNA-mediated silencing.

**[KNOWN]** Critically, defense priming by EPS can itself improve germination vigor through enhanced antioxidant capacity (SOD, CAT, APX upregulation), improved membrane integrity, and accelerated reserve mobilization — all of which are standard priming responses.

### Controls Needed
1. **Purified EPS fraction (RNA-free, protein-free):** Size-exclusion chromatography or ethanol precipitation of polysaccharides, confirmed RNA/protein-free by Bioanalyzer and Bradford assay.
2. **Defined MAMP controls:** Treat seeds with known concentrations of flg22, chitin oligomers, or commercial bacterial LPS to benchmark elicitor-driven germination changes.
3. **Transcriptomic comparison:** RNA-seq of seeds treated with (a) complete EPS+exRNA, (b) EPS only (RNase-treated), (c) purified exRNA in buffer, (d) water control. Compare DEG overlap.

---

## 3. Microbiome Effects

### Could the Bacterial Treatment Alter Seed Microbiome?
**[KNOWN]** Seeds harbor a complex endophytic and epiphytic microbiome (*Truyens et al., 2015, Microbiological Research; Nelson, 2018, Annual Review of Phytopathology*). The spermosphere (zone around germinating seed) is a dynamic microbial habitat.

- Application of bacterial EPS solution introduces bacterial metabolites, residual viable or non-viable cells, and a carbon-rich matrix that can selectively enrich or suppress endogenous seed microbiota. **[INFERRED]**
- The detection of **cry8Ba protein** (a *Bacillus thuringiensis* crystal protein) strongly suggests the presence of intact or lysed bacterial cells, not merely purified EPS. This means the preparation may contain peptidoglycan, lipoteichoic acid, bacterial DNA (CpG motifs), and other microbial components. **[INFERRED]**
- **[KNOWN]** PGPR colonization of seeds can improve germination through: volatile organic compound (VOC) production (acetoin, 2,3-butanediol), siderophore-mediated iron mobilization, phosphate solubilization, ACC deaminase activity (reducing ethylene), and IAA production.

### Known Microbiome Effects on Germination
- **[KNOWN]** *Bacillus* spp. and *Pseudomonas* spp. seed treatments routinely improve germination by 5–25% across multiple crop species through the mechanisms above (*Ryu et al., 2003, PNAS; Lugtenberg & Kamilova, 2009, Annual Review of Microbiology*).
- **[KNOWN]** Bacterial VOCs alone (without physical contact) can promote *Arabidopsis* growth and alter hormone signaling — particularly auxin redistribution and cytokinin-like effects.
- **[SPECULATIVE]** If the M-9 bacterial culture contains even low levels of viable cells, colonization effects could dominate the phenotype.

### Separation from Direct exRNA Mechanism
This is extremely difficult to separate without:
1. **Viability testing** of the EPS preparation (CFU plating, Live/Dead staining)
2. **Filter-sterilized conditioned medium** controls (0.1 µm filtration to remove all cells)
3. **Autoclaved EPS preparation** (destroys cells and RNA but alters polysaccharide structure — imperfect control)
4. **Axenic germination system** to prevent microbiome establishment

---

## 4. RNA Stability & Dosage Concerns

### Expected Half-Life of exRNA in Seed Coat Environment

**[KNOWN]** Extracellular RNA is extremely labile:
- Naked ssRNA half-life in soil: **minutes to hours** (*Zhu et al., 2022*). In biological fluids with RNase activity: **seconds to minutes**.
- dsRNA is more stable but still degrades within hours in non-sterile aqueous environments.
- The seed coat (testa + pericarp in spinach) is rich in oxidative compounds (phenolics, peroxidases) and nucleases that would rapidly degrade unprotected RNA. **[KNOWN]**

**[KNOWN]** However, EPS matrices can protect RNA through:
- Physical encapsulation in polysaccharide gel matrix
- Binding to positively charged matrix components
- Exclusion of nucleases by size/charge
- Association with extracellular vesicles (EVs) or outer membrane vesicles (OMVs) if bacterial cells were lysed during preparation

**[INFERRED]** If the exRNAs are packaged in OMVs (which is the primary mechanism of bacterial exRNA secretion; *Blenkiron et al., 2016*), stability could extend to hours-days, and OMVs could facilitate uptake by plant cells through endocytosis or membrane fusion.

### Required Copy Number for Antisense Effect

This is a critical quantitative concern:

- **[KNOWN]** Effective RNAi in plants typically requires delivery of **10⁶–10⁸ copies per cell** for exogenous dsRNA (*Dalakouras et al., 2020, Plant Cell*). This is why high-pressure spray application of dsRNA pesticides requires concentrations of **1–10 µg/cm²** of leaf surface.
- **[KNOWN]** A single plant cell contains approximately **10⁴–10⁵ copies** of a moderately expressed mRNA. To achieve meaningful knockdown (>50%), the antisense RNA must be present at comparable or higher stoichiometry, OR must be amplified by the plant's own RdRP machinery (RDR1, RDR2, RDR6) to generate secondary siRNAs.
- **[KNOWN]** In cross-kingdom RNAi, *Botrytis cinerea* delivers sRNAs via extracellular vesicles at the intimate host-pathogen interface, with continuous production during infection. This is fundamentally different from a one-time seed treatment. (*Weiberg et al., 2013, Science*)
- **[INFERRED]** For a one-time seed soak in EPS solution, the total RNA delivered is finite and non-renewable. Unless the bacterial sRNAs are amplified by plant RDR6/DCL4 (which requires initial loading into AGO proteins and generation of secondary siRNAs from the target transcript), the effect would be transient and quantitatively insufficient.

### Quantitative Estimation
- **[SPECULATIVE]** Assume EPS preparation contains ~1 µg/mL total small RNA (optimistic for bacterial culture supernatant). A seed soak of 1 mL delivers ~1 µg = ~3 × 10¹³ molecules of 21-nt RNA. Distributed across 109 targets, that's ~3 × 10¹¹ molecules per target. A spinach seed embryo contains ~10⁵–10⁶ cells. That yields ~3 × 10⁵–10⁶ molecules per cell per target — potentially sufficient IF delivery efficiency is high (unlikely — most will degrade or fail to enter cells). Realistic delivery efficiency for topical RNA application is estimated at **0.01–1%** (*Dalakouras et al., 2020*), reducing effective copies to **3 × 10³–10⁴ per cell per target** — marginal at best.

### Controls Needed
1. **Quantify total small RNA** in EPS preparation by Qubit/Bioanalyzer
2. **Track labeled RNA:** Apply Cy3- or Cy5-labeled synthetic sRNAs matching top targets in EPS matrix; image uptake by confocal microscopy in seed sections at 1h, 6h, 24h, 48h
3. **Detect bacterial sRNAs in planta:** Stem-loop RT-qPCR for specific bacterial sRNA sequences in treated seed tissues at multiple time points
4. **Secondary siRNA detection:** Look for 21-nt secondary siRNAs mapping to target genes (hallmark of RDR6-dependent amplification) by sRNA-seq

---

## 5. Non-specific RNA Effects

### Could Any RNA Sequence Trigger Similar Responses?

**[KNOWN]** Yes — and this is a major confounder:

- **dsRNA-triggered PTI:** Plants recognize dsRNA as a PAMP through a pathway that is at least partially independent of sequence-specific RNAi. *Niehl et al. (2016, Plant Journal)* demonstrated that dsRNA (including synthetic poly(I:C)) activates *SERK1*-dependent defense signaling in *Arabidopsis*, inducing *PR1*, *PR2*, ethylene biosynthesis genes, and MAPK phosphorylation. **[KNOWN]**
- **[KNOWN]** *Duran-Flores & Heil (2018, New Phytologist)* showed that exogenous RNA (including self-RNA, non-self RNA, and synthetic RNA) can trigger defense priming in a **sequence-independent** manner, activating ROS production, callose deposition, and SA/JA signaling.
- **[KNOWN]** This "RNA-triggered immunity" (RTI) would activate many of the same pathways reported as exRNA targets: defense/immunity, ROS/redox, hormone signaling, and epigenetic regulation.

### Pattern-Triggered Immunity from dsRNA
- **[KNOWN]** The receptor for extracellular dsRNA in plants is not fully characterized but involves SERK family co-receptors and potentially LRR-RKs. This pathway is **independent of DCL/AGO** — confirmed by the fact that *dcl2/dcl3/dcl4* triple mutants still show dsRNA-triggered PTI.
- **[INFERRED]** Any bacterial RNA preparation — regardless of whether it contains specific antisense sequences — would trigger RTI and could account for defense priming, ROS modulation, and hormone signaling changes.

### Controls Needed (ESSENTIAL)
1. **Scrambled sequence control:** Synthesize RNA of identical length distribution, GC content, and secondary structure propensity but with randomized/scrambled sequences. Apply in identical EPS matrix.
2. **RNase treatment control:** Treat complete EPS preparation with RNase A (ssRNA) + RNase III (dsRNA) + Turbo DNase; confirm degradation by Bioanalyzer; apply to seeds.
3. **Non-bacterial RNA control:** Total RNA from *E. coli* (no predicted spinach targets) at equivalent concentration in EPS matrix.
4. **Purified synthetic target sRNAs:** Synthesize the top 5 predicted antisense sRNAs; apply individually and in combination at quantified concentrations.
5. **Dose-response curve:** If the effect is sequence-specific RNAi, there should be a dose-dependent knockdown of specific targets. If the effect is non-specific RTI, any RNA at sufficient concentration should work.

---

## 6. Contamination Signals

### cry8Ba Bacterial Protein — Implications

**[KNOWN]** Cry8Ba is a crystal (Cry) δ-endotoxin from *Bacillus thuringiensis* (*Bt*), specifically targeting coleopteran insects. Its detection in the EPS preparation has several critical implications:

1. **The preparation is not pure EPS.** Cry proteins are intracellular crystalline inclusions released upon sporulation and cell lysis. Their presence indicates significant bacterial cell lysis and/or sporulation in the preparation. **[KNOWN]**
2. **The preparation likely contains:** intact or fragmented bacterial cells, peptidoglycan, lipoteichoic acid (Gram-positive MAMPs), bacterial DNA (CpG motifs — known PAMP in animals, less characterized in plants), bacterial proteins (including potential effectors, enzymes, and toxins), spores (if *Bt*-derived). **[INFERRED]**
3. **Cry proteins themselves may have plant effects.** While primarily studied as insecticidal proteins, Cry proteins bind to glycolipids and glycoproteins. **[SPECULATIVE]** Potential interactions with plant membrane components cannot be excluded, though no direct plant growth-promoting effect of Cry proteins is established.
4. **Regulatory and biosafety concern:** If this preparation is intended for agricultural use, the presence of *Bt* toxin proteins requires disclosure and potentially regulatory review.

### Source Organism Identity
- **[INFERRED]** The detection of cry8Ba suggests the M-9 bacterial strain is either a *Bacillus thuringiensis* strain or a closely related *Bacillus cereus* group member. This is important because:
  - *Bt* strains produce numerous secondary metabolites (zwittermicin A, thuricin, etc.) with antimicrobial and potentially plant-active properties
  - *B. cereus* group bacteria are known PGPR but also opportunistic pathogens
  - The specific EPS composition depends on species/strain identity

### Other Likely Bacterial Contaminants
| Contaminant Class | Likely Present? | Plant-Active? | Confounder Risk |
|---|---|---|---|
| Peptidoglycan fragments | Yes (cell lysis) | Yes — MAMP, activates CERK1 pathway | HIGH |
| Lipoteichoic acid | Yes (Gram-positive) | Yes — MAMP | HIGH |
| Bacterial DNA (CpG) | Yes | Possibly — less characterized in plants | MODERATE |
| Bacterial proteins (diverse) | Yes | Variable — enzymes, effectors | MODERATE |
| Spores | Possibly | Yes — germination → colonization | HIGH |
| Secondary metabolites | Possibly | Yes — antimicrobial, siderophores, IAA | HIGH |
| Outer membrane vesicles / EVs | Likely | Yes — cargo delivery vehicle | HIGH |

### Quality Control Recommendations
1. **Full compositional analysis:** SDS-PAGE + LC-MS/MS proteomics of the preparation
2. **RNA characterization:** sRNA-seq of the preparation; Bioanalyzer size distribution
3. **Viability assay:** CFU plating on LB and selective media
4. **Endotoxin/MAMP quantification:** Limulus assay (LPS), peptidoglycan ELISA
5. **Metabolomics:** LC-MS untargeted metabolomics of the preparation
6. **Strain identification:** Full 16S rRNA sequencing and whole-genome sequencing of M-9

---

## Confounder Impact Matrix

| Confounder | Likelihood of Contributing | Impact on Phenotype if True | Distinguishable from exRNA? | Experimental Priority |
|---|---|---|---|---|
| **EPS osmopriming** | **VERY HIGH** (near certain) | **HIGH** (could explain 50–100% of germination rate improvement) | **YES** — with RNase-treated EPS control | **CRITICAL — #1** |
| **Polysaccharide elicitation/ISR** | **HIGH** | **HIGH** (could explain defense, hormone, ROS, and epigenetic changes) | **YES** — with purified EPS vs. purified RNA controls | **CRITICAL — #2** |
| **Non-specific RNA-triggered immunity** | **HIGH** | **MODERATE-HIGH** (could explain defense/ROS/hormone subset) | **YES** — with scrambled RNA and RNase controls | **CRITICAL — #3** |
| **Bacterial cell/spore contamination** | **HIGH** (cry8Ba evidence) | **HIGH** (PGPR effects well-documented) | **PARTIALLY** — with filter-sterilized/autoclaved controls | **CRITICAL — #4** |
| **Bacterial metabolites** | **MODERATE-HIGH** | **MODERATE** (IAA, siderophores, VOCs) | **YES** — with dialysis/size fractionation | **HIGH — #5** |
| **Insufficient RNA dosage** | **MODERATE-HIGH** | **CRITICAL** (would nullify entire exRNA hypothesis) | **YES** — with quantification + labeled RNA tracking | **CRITICAL — #6** |
| **Microbiome restructuring** | **MODERATE** | **MODERATE** | **PARTIALLY** — with axenic system | **MODERATE — #7** |
| **Cry protein direct effects** | **LOW** | **LOW** (no known plant growth effects) | **YES** — with purified Cry protein control | **LOW — #8** |

---

## Recommended Controls — Prioritized Experimental Design

### Tier 1: ESSENTIAL (must be performed before any exRNA mechanism claim)

**Experiment 1: The RNase Elimination Test**
- **Design:** Treat identical aliquots of EPS preparation with (a) RNase A + RNase III cocktail, (b) heat-inactivated RNase cocktail (control for buffer effects), (c) no treatment. Confirm RNA degradation by Bioanalyzer. Apply all three to seeds.
- **Prediction if exRNA is causal:** RNase-treated preparation shows significantly reduced germination improvement.
- **Prediction if confounders dominate:** No difference between RNase-treated and untreated preparations.
- **Timeline:** 2–3 weeks. **HIGHEST PRIORITY.**

**Experiment 2: Osmotic Equivalence Control**
- **Design:** Measure water potential of EPS preparation. Prepare PEG-8000 solution at identical Ψ. Compare germination: (a) EPS + exRNA, (b) EPS + RNase, (c) PEG at same Ψ, (d) water.
- **Rationale:** Isolates osmopriming from all biological effects.
- **Timeline:** 2 weeks.

**Experiment 3: Scrambled RNA Control**
- **Design:** Synthesize 21-nt RNA pool with same nucleotide composition and concentration as measured in EPS preparation but randomized sequences. Apply in RNase-treated EPS matrix. Compare to complete preparation and water control.
- **Rationale:** Distinguishes sequence-specific RNAi from non-specific RTI.
- **Timeline:** 3–4 weeks.

**Experiment 4: RNA Quantification and Tracking**
- **Design:** (a) Quantify total sRNA in preparation by Qubit + Bioanalyzer. (b) Synthesize Cy3-labeled versions of top 3 predicted antisense sRNAs. (c) Apply in EPS matrix. (d) Section seeds at 2h, 6h, 12h, 24h, 48h. (e) Confocal imaging for uptake. (f) Stem-loop RT-qPCR for bacterial sRNAs in embryo tissue.
- **Rationale:** Demonstrates physical delivery — a prerequisite for any RNAi mechanism.
- **Timeline:** 4–6 weeks.

### Tier 2: STRONGLY RECOMMENDED

**Experiment 5: Target Transcript Validation**
- **Design:** RT-qPCR for top 10 high-priority target transcripts in seeds treated with (a) complete preparation, (b) RNase-treated preparation, (c) water. At 12h, 24h, 48h post-imbibition.
- **Prediction if exRNA is causal:** Specific downregulation of targets in (a) but not (b).
- **Prediction if confounders dominate:** Similar expression changes in (a) and (b), or changes consistent with defense/priming rather than specific knockdown.

**Experiment 6: Preparation Deconvolution**
- **Design:** Fractionate preparation by size: (a) >100 kDa (polysaccharides, vesicles), (b) 10–100 kDa (proteins, large RNA), (c) <10 kDa (small RNA, metabolites). Test each fraction independently. Also test recombined fractions.
- **Rationale:** Identifies which molecular class carries the bioactivity.

**Experiment 7: Viability and Colonization Assessment**
- **Design:** CFU plating of preparation. 16S amplicon sequencing of treated vs. untreated seed surfaces and embryos at 0h, 24h, 48h, 72h.
- **Rationale:** Determines if live bacteria contribute to the phenotype.

### Tier 3: INFORMATIVE

**Experiment 8: sRNA-seq of Treated Seeds**
- **Design:** sRNA-seq (15–30 nt fraction) of seeds treated with complete preparation vs. RNase-treated vs. water at 24h post-imbibition. Map reads to both *S. oleracea* genome and M-9 bacterial genome.
- **Rationale:** Detect bacterial sRNAs in planta; detect secondary siRNAs (21-nt, phased) at target loci as evidence of RDR6 amplification.

**Experiment 9: 5'-RACE / Degradome-seq**
- **Design:** Perform degradome-seq (PARE-seq) on treated seeds. Look for specific cleavage signatures at predicted antisense target sites.
- **Rationale:** Gold-standard evidence for AGO-mediated slicing at predicted target sites.

---

## Summary Assessment

### Estimated Phenotype Attribution (Pre-Control Experiments)

| Mechanism | Estimated Contribution to Observed Phenotype | Confidence |
|---|---|---|
| EPS osmopriming | **30–50%** | **[INFERRED]** — high confidence this contributes substantially |
| Polysaccharide elicitation / ISR | **15–30%** | **[INFERRED]** — based on known MAMP biology |
| Non-specific RNA-triggered immunity | **5–15%** | **[INFERRED]** — depends on total RNA concentration |
| Bacterial cell / metabolite effects | **10–25%** | **[INFERRED]** — cry8Ba evidence suggests significant contamination |
| Sequence-specific exRNA antisense silencing | **0–20%** | **[SPECULATIVE]** — cannot be estimated without controls |

**[INFERRED]** Based on this analysis, **80–100% of the observed germination phenotype could potentially be explained by confounders** that do not require sequence-specific antisense RNA targeting. This does not mean the exRNA mechanism is absent — it means it has not yet been isolated from confounders.

### Critical Path Forward
The exRNA hypothesis is scientifically interesting and worth pursuing, but it currently rests on correlative evidence (predicted antisense complementarity + observed phenotype). The **single most informative experiment** is the **RNase elimination test** (Experiment 1). If RNase treatment abolishes the germination improvement, all other confounders become secondary and the RNA-dependent mechanism gains strong support. If RNase treatment has no effect, the exRNA hypothesis is effectively falsified for this system, and the phenotype should be attributed to EPS/elicitor/microbiome effects.

**The burden of proof for cross-kingdom RNAi is high, and appropriately so.** The field has been criticized for overclaiming based on bioinformatic predictions without functional validation (*Tosar et al., 2021; Witwer, 2018*). The 109-target prediction set, while computationally derived, requires experimental triage through the control hierarchy outlined above before mechanistic claims can be supported.