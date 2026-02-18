# Confounder Analysis — Wheat (Triticum aestivum)



# Critical Analysis of Potential Confounders in the exRNA Germination Improvement System

## Preamble

This analysis assumes a system in which a bacterial exopolysaccharide (EPS) preparation from an M-9 strain (likely *Bacillus* or related genus, given the cry8Ba detection) is applied to wheat seeds, with the claimed mechanism being cross-kingdom antisense RNA targeting of 75 plant transcripts. The central question is: **what fraction of the observed germination phenotype is attributable to sequence-specific antisense RNA activity versus confounding physicochemical and biological effects of the preparation itself?**

---

## 1. EPS Osmopriming Effect

### Mechanism
[KNOWN] Seed priming — controlled hydration followed by drying — is one of the most robust and well-documented methods for improving germination rate, synchrony, and seedling vigor in wheat and other cereals (Parera & Cantliffe, 1994; Bewley et al., 2013). EPS solutions are inherently viscous, hydrophilic polymer matrices. When seeds are soaked in or coated with bacterial EPS:

- **Controlled water uptake**: EPS creates a hydrated gel matrix around the seed coat, enabling slow, uniform imbibition. This is functionally equivalent to hydropriming or osmopriming with PEG solutions. [KNOWN]
- **Water potential modulation**: Bacterial EPS (e.g., levan, alginate, xanthan analogs) can lower water potential in the immediate seed environment, controlling the rate of Phase I imbibition and allowing pre-germinative metabolic activation (DNA repair, mitochondrial biogenesis, mRNA synthesis) without radicle emergence. [KNOWN]
- **Desiccation protection**: If seeds are re-dried after treatment, the EPS film can protect against imbibition damage upon re-wetting, a well-known benefit of film-coating and polymer priming. [KNOWN]
- **Improved seed-soil contact**: EPS mucilage improves hydraulic conductivity at the seed-soil interface. [KNOWN]

### Expected Magnitude vs. Observed Effect
[KNOWN] Osmopriming alone in wheat typically produces:
- **Germination rate increase**: 10–30% improvement under suboptimal conditions (drought, salinity, cold), and 5–15% even under optimal conditions (Farooq et al., 2005; Jisha et al., 2013).
- **Vigor indices**: Mean germination time reduction of 1–3 days; seedling dry weight increases of 10–25%. [KNOWN]
- **Root/shoot length**: Increases of 15–40% in early seedling growth are routinely reported from priming alone. [KNOWN]

[INFERRED] If the observed phenotype falls within these ranges, **the entire effect could plausibly be explained by osmopriming without invoking any RNA-mediated mechanism**. Only effects exceeding the osmopriming ceiling — or showing gene-specific molecular signatures — would require an additional explanatory mechanism.

### Controls Needed
| Control | Purpose |
|---------|---------|
| **Heat-denatured EPS solution** (autoclaved, 121°C, 20 min) | Preserves polysaccharide osmopriming; destroys RNA |
| **RNase A/III-treated EPS solution** | Degrades ssRNA and dsRNA while preserving EPS matrix |
| **Equivalent-viscosity PEG-6000 or methylcellulose solution** | Matches osmotic and rheological properties without biological molecules |
| **Pure water priming (hydropriming)** | Baseline priming control |
| **Dry seed (unprimed)** | Negative control |
| **Purified EPS (dialyzed, protein/nucleic acid-depleted)** | Isolates polysaccharide effect from all other components |

**Evidence level**: The osmopriming confounder is [KNOWN] and represents the **single most likely alternative explanation** for the observed phenotype.

---

## 2. Polysaccharide Elicitor Effects

### Known Defense/Growth Priming by Bacterial Polysaccharides
[KNOWN] Bacterial EPS and related polysaccharides are well-established microbe-associated molecular patterns (MAMPs) and elicitors in plants:

- **β-glucans, peptidoglycans, and lipopolysaccharides (LPS)** from Gram-positive and Gram-negative bacteria trigger pattern-triggered immunity (PTI) in plants. [KNOWN]
- *Bacillus* EPS specifically has been shown to induce systemic resistance (ISR) in multiple crop species (Raaijmakers et al., 2010; Lastochkina et al., 2017). [KNOWN]
- EPS from PGPR (*Bacillus subtilis*, *B. amyloliquefaciens*, *Pseudomonas*) enhances salinity and drought tolerance through priming of antioxidant defense systems (SOD, CAT, APX upregulation). [KNOWN]

### Relevant Plant Receptors and Signaling Pathways
[KNOWN] The following receptor systems could be activated by bacterial polysaccharide components in the EPS preparation:

- **CERK1/LYK5 complex**: Chitin/peptidoglycan receptor; recognizes N-acetylglucosamine-containing polymers. Bacterial peptidoglycan contamination in EPS preparations is common. [KNOWN]
- **LORE (lipooligosaccharide-specific reduced elicitation)**: Responds to bacterial medium-chain 3-hydroxy fatty acids, likely present as EPS-associated lipids. [KNOWN in *Arabidopsis*; INFERRED in wheat]
- **WAK (Wall-Associated Kinases)**: Respond to oligogalacturonides and potentially to bacterial EPS fragments. [INFERRED]
- **BAK1/SERK3 co-receptor**: Central hub for multiple MAMP signaling cascades. [KNOWN]

### Signaling Cascades Triggered
[KNOWN] Downstream of MAMP perception:
- **MAPK cascade activation** (MPK3/MPK6 orthologs in wheat) → defense gene transcription
- **ROS burst** via RBOHD (respiratory burst oxidase homolog D) → oxidative signaling
- **Calcium influx** → CDPKs → defense gene activation
- **Salicylic acid (SA) and jasmonic acid (JA) pathway induction**
- **Ethylene biosynthesis modulation**
- **Callose deposition and cell wall reinforcement**

### Critical Overlap with Claimed exRNA Targets
[INFERRED] This is a major concern. The 75 claimed exRNA targets include genes in:

| Claimed target pathway | Also activated by polysaccharide elicitors? | Overlap concern |
|----------------------|-------------------------------------------|----------------|
| Defense/immunity | **Yes** — direct MAMP response | **HIGH** |
| ROS/redox | **Yes** — RBOH-mediated burst is canonical MAMP response | **HIGH** |
| Hormone signaling (SA, JA, ET, ABA) | **Yes** — ISR involves all four pathways | **HIGH** |
| Epigenetic regulation | **Yes** — defense priming involves histone modifications (H3K4me3, H3K27me3) | **MODERATE** |
| Transport/ion homeostasis | **Partially** — calcium channels, H⁺-ATPases involved in PTI | **MODERATE** |
| Metabolic priming | **Partially** — primary metabolism reprogramming during defense | **MODERATE** |

[INFERRED] **The overlap is striking**: virtually every pathway category attributed to exRNA targeting is independently modulated by polysaccharide elicitor signaling. Without molecular evidence of antisense-mediated transcript cleavage (e.g., 5'-RACE mapping of cleavage sites, degradome sequencing), the transcriptomic changes could be entirely explained by MAMP-triggered transcriptional reprogramming.

**Evidence level**: [KNOWN] for elicitor effects; [INFERRED] for the degree of overlap with claimed exRNA targets.

---

## 3. Microbiome Effects

### Could the Bacterial Treatment Alter Seed Microbiome?
[KNOWN] Yes, unambiguously:

- Seed treatments with bacterial preparations routinely alter the epiphytic and endophytic microbiome of the spermosphere and rhizosphere (Nelson, 2018). [KNOWN]
- EPS itself serves as a carbon source for specific microbial taxa, selectively enriching beneficial microorganisms. [KNOWN]
- The M-9 preparation likely contains viable or non-viable bacterial cells, cell wall fragments, metabolites, siderophores, and volatile organic compounds (VOCs) in addition to EPS and RNA. [INFERRED]
- The detection of cry8Ba protein (see Section 6) confirms that bacterial cellular material is present in the preparation. [KNOWN from experimental context]

### Known Microbiome Effects on Germination
[KNOWN] The seed microbiome profoundly influences germination:

- **Spermosphere bacteria** produce gibberellins (GA₃, GA₄), cytokinins, and auxin (IAA), directly promoting germination. *Bacillus* spp. are among the most prolific phytohormone producers. [KNOWN]
- **ACC deaminase** production by PGPR reduces ethylene levels, preventing germination inhibition under stress. [KNOWN]
- **Volatile organic compounds** (2,3-butanediol, acetoin) from *Bacillus* spp. promote plant growth via unknown receptors. [KNOWN]
- **Phosphate solubilization and siderophore production** improve early nutrient acquisition. [KNOWN]
- **Biofilm formation** on seed coat improves water retention (overlaps with osmopriming). [KNOWN]

### Separation from Direct exRNA Mechanism
[INFERRED] Separating microbiome effects from exRNA effects requires:

1. **Filter-sterilized, cell-free preparations** (0.22 µm filtration) — removes viable cells but retains RNA and EPS
2. **Autoclaved preparation** — destroys both cells and RNA but retains heat-stable metabolites and EPS
3. **Axenic germination assays** (sterile seeds on sterile media) — eliminates microbiome variable entirely
4. **16S/ITS amplicon sequencing** of treated vs. untreated seed surfaces at multiple time points
5. **CFU plating** of treated seeds to quantify viable bacterial load

[INFERRED] If the germination phenotype persists in axenic conditions with filter-sterilized, RNase-treated preparation, the microbiome explanation is excluded. If it disappears with RNase treatment but persists with filter sterilization, the RNA hypothesis gains support.

**Evidence level**: [KNOWN] for microbiome effects on germination; [INFERRED] for their contribution to this specific system.

---

## 4. RNA Stability and Dosage Concerns

### Expected Half-Life of exRNA in the Seed Coat Environment

[KNOWN] Extracellular RNA is highly labile:

- **Naked ssRNA half-life** in soil: minutes to hours (Levy-Booth et al., 2007). [KNOWN]
- **Naked ssRNA half-life** in aqueous solution with biological material: 30 seconds to 30 minutes, depending on RNase load (Tsui et al., 2002). [KNOWN]
- **Seed coat surface**: Rich in RNases, peroxidases, and phenolic compounds. Wheat seed coat (testa + pericarp) contains abundant nucleases as part of antimicrobial defense. [KNOWN]
- **dsRNA stability**: Substantially greater than ssRNA; half-life of hours to days in soil and on plant surfaces (Dubelman et al., 2014). [KNOWN]
- **Extracellular vesicle (EV)-encapsulated RNA**: If bacterial exRNAs are packaged in outer membrane vesicles (OMVs), stability increases dramatically (hours to days). [KNOWN for mammalian EVs; INFERRED for bacterial OMVs in plant context]

[INFERRED] Unless the exRNAs are (a) double-stranded, (b) chemically modified (e.g., 2'-O-methylation, which some bacteria produce), or (c) encapsulated in membrane vesicles or protein complexes, **the expected half-life on the wheat seed surface is minutes, not hours**. The window for uptake and activity is extremely narrow.

### Required Copy Number for Antisense Effect

[KNOWN] For RNAi-mediated silencing in plants:
- **Effective siRNA concentration**: Typically requires >100–1000 copies per cell for measurable target knockdown in plant RNAi studies (Melnyk et al., 2011). [KNOWN]
- **Spray-induced gene silencing (SIGS)**: Requires application of 2–20 µg dsRNA per plant for detectable effects; this represents ~10⁹–10¹¹ molecules (Koch et al., 2016; Wang et al., 2016). [KNOWN]
- **Amplification**: Plants possess RNA-dependent RNA polymerases (RDRs) that can amplify silencing signals, but this requires initial loading into AGO proteins and production of secondary siRNAs. [KNOWN]

[INFERRED] For 75 targets to be simultaneously regulated, the preparation would need to contain sufficient copies of each of the 75 antisense species to independently achieve silencing. Assuming:
- Minimum ~10⁴ copies per target per seed (conservative, assuming RDR amplification)
- 75 targets
- Total requirement: ~7.5 × 10⁵ specific RNA molecules per seed minimum

[SPECULATIVE] Bacterial cultures typically produce exRNAs at concentrations of 1–100 ng/mL in culture supernatant (Tsatsaronis et al., 2018). If the EPS preparation is concentrated, perhaps 100–1000 ng/mL total RNA. Of this, only a fraction would be the specific antisense sequences. **It is questionable whether sufficient copies of each of 75 specific antisense species would be present at biologically relevant concentrations.**

### Key Unknowns
- What is the actual RNA concentration in the M-9 EPS preparation? [UNKNOWN]
- What fraction consists of the specific 75 antisense sequences vs. total RNA? [UNKNOWN]
- Are the exRNAs encapsulated in OMVs? [UNKNOWN]
- Is there evidence of secondary siRNA amplification from these specific triggers? [UNKNOWN]

**Evidence level**: RNA instability is [KNOWN]; dosage insufficiency is [INFERRED] to [SPECULATIVE] without quantitative data from the preparation.

---

## 5. Non-specific RNA Effects

### Could Any RNA Sequence Trigger Similar Responses?

[KNOWN] Yes, through multiple mechanisms:

#### 5a. Pattern-Triggered Immunity from dsRNA
- **dsRNA is a MAMP/DAMP**: Plants recognize dsRNA through SERK1 and potentially other receptors, triggering PTI-like responses independent of sequence (Niehl et al., 2016; Niehl & Heinlein, 2019). [KNOWN in *Arabidopsis*]
- **SERK1-mediated dsRNA sensing** activates MAPK cascades, ethylene signaling, and defense gene expression — overlapping substantially with the claimed target pathways. [KNOWN]
- This response occurs with synthetic dsRNA of any sequence, including poly(I:C) and GFP dsRNA (no plant target). [KNOWN]
- In wheat specifically, dsRNA perception has not been fully characterized, but SERK family members are conserved. [INFERRED]

#### 5b. RNA as a Phosphorus/Nitrogen Source
- Extracellular RNA is degraded by apoplastic nucleases and can serve as a phosphorus and nitrogen source, potentially stimulating early seedling metabolism. [KNOWN] (Bhat & Ryu, 2016)

#### 5c. Non-specific Nucleic Acid Effects
- Exogenous DNA and RNA can trigger chromatin remodeling and epigenetic changes in plants through sequence-independent mechanisms (Yakushiji et al., 2009). [KNOWN but poorly characterized]
- CpG and other motifs in bacterial nucleic acids can trigger innate immune responses in plants analogous to TLR9 responses in animals, though plant receptors are less well defined. [SPECULATIVE]

#### 5d. Hormesis
- Low-level stress signals (including foreign nucleic acids) can trigger hormetic responses — mild stress priming that improves subsequent stress tolerance. [KNOWN as a general principle; SPECULATIVE for this specific system]

### Controls Required
| Control | Purpose |
|---------|---------|
| **Scrambled-sequence RNA** of equivalent length, GC content, and concentration | Tests sequence specificity |
| **GFP or LacZ dsRNA** (no wheat target) | Tests for non-specific dsRNA response |
| **Poly(I:C)** | Canonical dsRNA MAMP; tests for PTI activation |
| **RNase III-treated preparation** (degrades dsRNA specifically) | Distinguishes dsRNA-mediated from ssRNA-mediated effects |
| **RNase A-treated preparation** (degrades ssRNA) | Distinguishes ssRNA from dsRNA contributions |
| **Equivalent mass of yeast tRNA** | Non-specific RNA control |
| **DNase-treated preparation** | Excludes DNA-mediated effects |

[INFERRED] **If scrambled-sequence RNA or GFP dsRNA produces similar germination improvements, the sequence-specific antisense hypothesis is falsified.** This is arguably the single most important control experiment.

**Evidence level**: Non-specific dsRNA effects are [KNOWN]; their magnitude relative to sequence-specific effects in this system is [UNKNOWN].

---

## 6. Contamination Signals

### cry8Ba Bacterial Protein Detection — Implications

[KNOWN] cry8Ba encodes a crystal protein (δ-endotoxin) from *Bacillus thuringiensis* (Bt). Its detection in the preparation has several critical implications:

1. **Strain identity**: The M-9 strain is likely a *Bacillus thuringiensis* strain or a closely related *Bacillus cereus* group member. [INFERRED]
2. **Protein contamination**: If Cry8Ba protein is detectable, the preparation contains significant bacterial protein content, meaning it is **not a purified EPS/RNA preparation** but rather a crude or semi-purified bacterial extract. [INFERRED]
3. **Other co-purifying proteins**: If Cry8Ba is present, other bacterial proteins are almost certainly present, including:
   - **Chitinases and glucanases** — known plant defense elicitors [KNOWN]
   - **Flagellin** — potent MAMP recognized by FLS2 receptor [KNOWN]
   - **Surfactins and lipopeptides** — *Bacillus* biosurfactants that trigger ISR [KNOWN]
   - **Phospholipases, proteases** — membrane-active enzymes [KNOWN]
   - **Phytohormones** (IAA, cytokinins, GA) produced by *Bacillus* spp. [KNOWN]
4. **Cry protein effects on plants**: While Cry proteins are primarily insecticidal, some studies report direct effects on plant cells, including membrane permeabilization at high concentrations. [SPECULATIVE for germination effects]

### Quality Control Concerns
[INFERRED] The presence of Cry8Ba protein indicates that the preparation is a **complex biological mixture**, not a defined exRNA preparation. This fundamentally undermines the ability to attribute any phenotype to a specific component (exRNA) without rigorous fractionation and reconstitution experiments.

### Quality Control Recommendations
1. **Full proteomics** (LC-MS/MS) of the preparation to catalog all protein contaminants
2. **Endotoxin (LPS) quantification** via LAL assay
3. **Small RNA sequencing** of the preparation to verify presence and abundance of claimed antisense species
4. **Size-exclusion chromatography or density gradient ultracentrifugation** to separate OMVs, free RNA, EPS, and protein fractions
5. **Activity-guided fractionation**: Test each fraction independently for germination activity
6. **Reconstitution experiments**: Combine purified fractions to test for synergistic effects

**Evidence level**: Cry8Ba detection is [KNOWN from experimental context]; implications for preparation purity are [INFERRED]; specific effects of contaminants are [KNOWN] for individual molecules but [UNKNOWN] for this preparation.

---

## Confounder Impact Matrix

| Confounder | Likelihood of Contributing | Impact if True (% of phenotype explained) | Distinguishable with proper controls? | Experimental Priority |
|---|---|---|---|---|
| **EPS osmopriming** | **Very High (>90%)** | **30–100%** | Yes — PEG/methylcellulose controls | **1 (CRITICAL)** |
| **Polysaccharide elicitor/MAMP effects** | **High (70–85%)** | **20–60%** | Yes — purified EPS vs. autoclaved prep | **2 (HIGH)** |
| **Non-specific dsRNA/PTI activation** | **High (60–80%)** | **15–50%** | Yes — scrambled RNA, GFP dsRNA controls | **3 (HIGH)** |
| **Bacterial protein contaminants (Cry8Ba, etc.)** | **High (70–80%)** | **10–40%** | Yes — proteinase K treatment, fractionation | **4 (HIGH)** |
| **Bacterial metabolites/phytohormones** | **Moderate (40–60%)** | **10–30%** | Partially — chemical analysis, dialysis | **5 (MODERATE)** |
| **Microbiome alteration** | **Moderate (30–50%)** | **10–30%** | Yes — axenic assays, filter sterilization | **6 (MODERATE)** |
| **RNA as nutrient source (P, N)** | **Low-Moderate (20–40%)** | **5–15%** | Yes — equivalent P/N supplementation | **7 (LOW)** |
| **Dosage insufficiency (RNA too dilute)** | **High (60–80%)** | **N/A (undermines mechanism)** | Yes — quantitative small RNA-seq of preparation | **3 (HIGH, tied)** |
| **RNA instability (degraded before uptake)** | **High (50–70%)** | **N/A (undermines mechanism)** | Yes — RNA integrity analysis, time-course | **3 (HIGH, tied)** |

### Interpretation of Matrix
[INFERRED] **Conservatively, confounders could explain 60–100% of the observed phenotype.** The osmopriming effect alone could account for the entire germination improvement. When combined with MAMP elicitor effects and non-specific RNA responses, the residual phenotype requiring a sequence-specific antisense explanation may be **zero to marginal**.

---

## Recommended Controls — Prioritized Experimental Program

### Tier 1: CRITICAL (Must be performed before any mechanistic claims)

**Experiment 1: Osmopriming equivalence test**
- Compare: (A) M-9 EPS preparation, (B) PEG-6000 matched for water potential, (C) methylcellulose matched for viscosity, (D) hydropriming (water), (E) dry seed
- Readout: Germination rate, mean germination time, seedling vigor index
- If A ≈ B or C → osmopriming explains phenotype

**Experiment 2: RNase elimination test**
- Compare: (A) M-9 EPS preparation, (B) RNase A + RNase III-treated EPS preparation (destroys all RNA), (C) RNase-treated + exogenous purified RNA add-back
- Readout: Germination phenotype
- If A ≈ B → RNA is not required for phenotype
- If A > B and C rescues → RNA contributes (but specificity still untested)

**Experiment 3: RNA quantification and characterization**
- Perform small RNA-seq on the M-9 EPS preparation
- Quantify total RNA concentration (Qubit/Bioanalyzer)
- Map reads to wheat genome — verify that the 75 claimed antisense sequences are actually present and at what abundance
- Calculate copies per seed at application dose
- **If the 75 antisense species are absent or at <100 copies per seed, the mechanism is implausible**

### Tier 2: HIGH PRIORITY (Required for mechanistic validation)

**Experiment 4: Sequence specificity test**
- Compare: (A) M-9 preparation, (B) equivalent concentration of scrambled-sequence RNA in purified EPS, (C) GFP dsRNA in purified EPS, (D) purified EPS alone
- Readout: Germination phenotype + RT-qPCR of 5–10 claimed target genes
- **This is the gold-standard test for sequence-specific antisense activity**

**Experiment 5: Molecular target validation**
- Perform 5'-RACE or degradome sequencing (PARE-seq/GMUCT) on treated seedlings
- Map cleavage sites on claimed target transcripts
- Antisense RNA-guided cleavage produces a characteristic cleavage signature at the predicted target site
- **Without this, transcript-level changes cannot be attributed to antisense cleavage vs. transcriptional regulation by other stimuli**

**Experiment 6: Proteinase K treatment**
- Compare: (A) M-9 preparation, (B) Proteinase K-treated preparation (removes all proteins including Cry8Ba, flagellin, etc.)
- Readout: Germination phenotype
- Distinguishes protein-mediated effects from RNA/EPS effects

### Tier 3: IMPORTANT (For complete mechanistic understanding)

**Experiment 7: Axenic germination assay**
- Surface-sterilize seeds (NaOCl or H₂O₂), confirm sterility, germinate on sterile media with filter-sterilized (0.22 µm) preparation
- Eliminates microbiome variable

**Experiment 8: Fractionation and reconstitution**
- Separate preparation into: (i) >100 kDa fraction (EPS, OMVs), (ii) 10–100 kDa (proteins), (iii) <10 kDa (small RNA, metabolites)
- Test each fraction and combinations
- Identify the active fraction(s)

**Experiment 9: Uptake verification**
- Apply fluorescently labeled (Cy3/Cy5) synthetic versions of claimed antisense RNAs
- Track uptake into seed tissues via confocal microscopy
- Verify that exogenous small RNAs actually penetrate the seed coat and reach target cells

**Experiment 10: Dose-response with synthetic antisense RNAs**
- Synthesize 5–10 of the most confidently predicted antisense sequences
- Apply at defined concentrations to seeds in purified EPS carrier
- Measure germination phenotype and target gene expression
- **This is the definitive gain-of-function test**

---

## Summary Assessment

### Strength of the exRNA Antisense Hypothesis

| Criterion | Status | Assessment |
|-----------|--------|------------|
| Antisense RNAs confirmed present in preparation | **UNKNOWN** | Not verified by sequencing |
| Sufficient dosage for biological activity | **UNKNOWN** | Not quantified |
| RNA stability in seed coat environment | **DOUBTFUL** | Known rapid degradation of naked exRNA [KNOWN] |
| Uptake into plant cells demonstrated | **UNKNOWN** | Not shown |
| Target cleavage validated (5'-RACE/degradome) | **UNKNOWN** | Not performed |
| Sequence specificity demonstrated | **UNKNOWN** | No scrambled controls |
| Confounders excluded | **NO** | Major confounders uncontrolled |

### Bottom Line

[INFERRED] **In the absence of the Tier 1 and Tier 2 controls described above, the most parsimonious explanation for the observed germination phenotype is a combination of osmopriming by the EPS matrix, MAMP/elicitor-triggered defense priming by bacterial polysaccharides and protein contaminants, and potentially non-specific RNA-triggered immunity.** The sequence-specific antisense RNA mechanism, while intellectually appealing and not impossible, is currently the **least well-supported** explanation and faces significant thermodynamic (stability), stoichiometric (dosage), and biological (uptake, RISC loading) barriers.

[SPECULATIVE] If forced to estimate the partition of the observed phenotype, a reasonable prior distribution might be:
- Osmopriming: **30–50%**
- MAMP/elicitor effects: **20–30%**
- Non-specific RNA/nucleic acid effects: **10–20%**
- Microbiome + metabolite effects: **5–15%**
- **Sequence-specific antisense RNA effects: 0–15%**

These estimates are [SPECULATIVE] and should be updated as controlled experiments are performed. The experimental program outlined above would resolve these ambiguities within 2–3 experimental cycles.

---

*Analysis completed with the caveat that the underlying experimental data were not directly reviewed; all assessments are based on the described experimental context and established literature on seed priming, MAMP signaling, and cross-kingdom RNA biology.*