# Confounder Analysis — Soybean (Glycine max)



# Critical Analysis of Potential Confounders in the exRNA Germination Improvement System

## Preamble

This analysis assumes the experimental system involves treating *Glycine max* seeds with an EPS (exopolysaccharide) solution derived from an M-9 bacterial strain, where the proposed mechanism is cross-kingdom antisense RNA silencing of 18 plant target genes. The central question is: **what fraction of the observed germination/vigor phenotype can be confidently attributed to antisense RNA targeting versus alternative mechanisms inherent to the treatment?**

---

## 1. EPS Osmopriming Effect

### Mechanism
[KNOWN] Seed priming with osmotic solutions is one of the oldest and most robust methods for improving germination uniformity and speed. EPS solutions are viscous, high-molecular-weight polysaccharide matrices that create a controlled water potential environment around the seed.

- **Hydropriming and osmopriming** allow seeds to undergo Phase I and early Phase II of imbibition (metabolic reactivation, DNA repair, mitochondrial biogenesis, mRNA recruitment to polysomes) without completing germination (radicle emergence). Upon drying-back and re-imbibition, seeds germinate faster and more uniformly. [KNOWN — reviewed in Paparella et al., 2015, *Plant Cell Reports*; Lutts et al., 2016]
- EPS solutions from bacteria such as *Pseudomonas*, *Bacillus*, *Rhizobium*, and others typically have water potentials in the range of **−0.5 to −2.0 MPa** depending on concentration, which falls squarely within the effective osmopriming window (typically −0.5 to −1.5 MPa for soybean). [KNOWN]
- The polysaccharide matrix may also provide a **controlled hydration envelope** around the seed, slowing imbibition and reducing imbibition damage — a known problem in large-seeded legumes like soybean where rapid water uptake causes mechanical damage to cotyledons and embryonic axes. [KNOWN — Powell & Matthews, 1978; Woodstock & Taylorson, 1981]

### Expected Magnitude vs. Observed Effect
- [KNOWN] PEG osmopriming of soybean seeds routinely improves germination rate by **10–25%** under optimal conditions and **20–50%** under stress conditions (reviewed in Sadeghi et al., 2011; Ghassemi-Golezani et al., 2008).
- [KNOWN] Hydropriming alone (water, no osmoticum) can improve soybean germination by **5–15%** and seedling vigor indices by **10–30%** (Sadeghi et al., 2011).
- [INFERRED] If the observed germination improvement falls within the **5–25% range**, the entire phenotype could plausibly be explained by osmopriming alone. Only effects substantially exceeding this range, or showing pathway-specific molecular signatures inconsistent with general priming, would require an additional mechanism.
- [INFERRED] Early seedling growth improvement (hypocotyl/radicle length, dry weight accumulation) is a **classic hallmark** of seed priming and is not diagnostic of exRNA activity.

### Controls Needed
1. **EPS solution without RNA** — autoclaved or RNase A/III-treated EPS at identical concentration and water potential
2. **PEG 6000/8000 control** — matched to the same water potential as the EPS solution (measured by osmometry)
3. **Water-primed control** — hydropriming for the same duration
4. **Dry seed control** — untreated
5. **Water potential measurement** of the EPS solution itself (critical and often omitted)

### Evidence Level
- That EPS acts as an osmopriming agent: **[KNOWN]**
- That this alone could explain the germination phenotype: **[INFERRED — HIGH PROBABILITY]**
- That osmopriming is the *dominant* contributor: **[INFERRED — requires controls to quantify]**

---

## 2. Polysaccharide Elicitor Effects

### Known Defense/Growth Priming by Bacterial Polysaccharides
[KNOWN] Bacterial EPS are potent microbe-associated molecular patterns (MAMPs) and damage-associated signals that activate plant innate immunity and growth modulation:

- **β-glucans, lipopolysaccharides (LPS), and EPS fragments** are recognized by plant pattern recognition receptors (PRRs). Specifically:
  - *CERK1* (chitin elicitor receptor kinase 1, *Glyma.02G270800* and orthologs) — recognizes oligosaccharide patterns [KNOWN]
  - *LYK* family receptors — involved in peptidoglycan and polysaccharide sensing [KNOWN]
  - *BAK1/SERK3* co-receptor — required for many MAMP signaling cascades [KNOWN]
  - *LORE* (lipooligosaccharide-specific receptor) in some species [KNOWN]

- [KNOWN] EPS from PGPR (plant growth-promoting rhizobacteria) triggers **induced systemic resistance (ISR)** through jasmonic acid (JA) and ethylene (ET) signaling pathways, and in some cases through salicylic acid (SA) pathways (Reviewed in Pieterse et al., 2014, *Annual Review of Phytopathology*).

- [KNOWN] *Rhizobium* and *Sinorhizobium* EPS (succinoglycan, galactoglucan) are specifically recognized during soybean nodulation and modulate defense suppression via Nod factor signaling (*NFR1*, *NFR5*, *SYMRK* in *Glycine max*). Even non-rhizobial EPS can partially activate these pathways. [KNOWN — Kawaharada et al., 2015]

### Critical Overlap with Observed Target Gene Changes
[INFERRED] The reported target pathways — **hormone signaling, defense/immunity, epigenetic regulation, ROS/redox** — show extensive overlap with known EPS elicitor responses:

| Reported Pathway | EPS Elicitor Overlap | Concern Level |
|---|---|---|
| Hormone signaling (ABA, GA, ET, JA) | EPS triggers JA/ET/SA signaling; ABA-GA balance shifts during priming | **HIGH** |
| Defense/immunity | EPS is a direct MAMP; triggers PTI | **VERY HIGH** |
| ROS/redox | MAMP perception triggers oxidative burst (RBOHD/F); priming induces antioxidant systems | **VERY HIGH** |
| Epigenetic regulation | Priming is known to involve chromatin remodeling and DNA methylation changes | **HIGH** |
| Transport/ion homeostasis | Osmotic treatment alters ion channel expression | **MODERATE** |
| Metabolic priming | General priming effect on central metabolism | **HIGH** |

[INFERRED] **This is the most concerning confounder.** Virtually every pathway attributed to exRNA targeting is independently activated by polysaccharide elicitor signaling. Without rigorous controls, it is impossible to attribute transcript-level changes to antisense RNA rather than to canonical MAMP signaling.

### Specific Molecular Concerns
- [KNOWN] MAMP-triggered immunity (MTI/PTI) activates WRKY transcription factors, MAP kinase cascades (MPK3, MPK6), and defense gene expression within minutes to hours.
- [KNOWN] EPS can trigger callose deposition, ROS burst, and phytoalexin biosynthesis — all of which overlap with "defense/immunity" targets.
- [KNOWN] Bacterial polysaccharides can also suppress defense (as in symbiotic interactions), creating a complex, context-dependent response.

### Evidence Level
- That bacterial EPS activates plant defense/hormone signaling: **[KNOWN]**
- That this overlaps with the claimed exRNA targets: **[INFERRED — VERY HIGH CONFIDENCE]**
- That EPS elicitor effects could fully explain the molecular changes: **[INFERRED]**

---

## 3. Microbiome Effects

### Could the Bacterial Treatment Alter Seed Microbiome?
[KNOWN] Seeds harbor endophytic and epiphytic microbial communities (the "spermosphere" microbiome) that influence germination and early seedling establishment. Soybean seeds specifically harbor *Bacillus*, *Pseudomonas*, *Pantoea*, and *Methylobacterium* as core seed-associated taxa (Rochefort et al., 2021; Simonin et al., 2022).

- [INFERRED] Application of an M-9 bacterial EPS solution likely introduces live or dead bacterial cells, cell wall fragments, and metabolites in addition to EPS and RNA. Even "cell-free" preparations may contain:
  - Outer membrane vesicles (OMVs) carrying proteins, lipids, and nucleic acids
  - Residual viable cells (if not filter-sterilized through 0.1 μm)
  - Bacterial metabolites (siderophores, volatiles, phytohormones)

- [KNOWN] Many PGPR produce **phytohormones** (IAA, cytokinins, gibberellins) that directly promote germination and seedling growth. Even dead bacterial cells release these compounds upon lysis. [KNOWN — Spaepen et al., 2007; Cassán et al., 2014]

- [KNOWN] Bacterial volatile organic compounds (VOCs) such as 2,3-butanediol and acetoin from *Bacillus* spp. promote plant growth via ET and cytokinin signaling. [KNOWN — Ryu et al., 2003]

### Known Microbiome Effects on Germination
- [KNOWN] Seed biopriming (coating seeds with beneficial bacteria) improves germination by 10–30% across multiple crop species through a combination of:
  - Competitive exclusion of seed-borne pathogens
  - Phytohormone production
  - Nutrient solubilization
  - Induced systemic resistance

- [INFERRED] If the EPS preparation contains any viable bacteria or bacterial metabolites, the observed phenotype may partially or fully reflect classical biopriming rather than exRNA activity.

### Separation from Direct exRNA Mechanism
[INFERRED] This is extremely difficult to separate without:
1. Quantitative culture of the EPS preparation to confirm sterility
2. LC-MS metabolomics of the preparation to detect phytohormones
3. 16S rRNA gene sequencing of treated vs. untreated seed surfaces
4. Comparison with heat-killed bacterial preparations

### Evidence Level
- That bacterial preparations alter seed microbiome/spermosphere: **[KNOWN]**
- That this could contribute to germination improvement: **[KNOWN]**
- Magnitude of contribution in this specific system: **[UNKNOWN — requires characterization]**

---

## 4. RNA Stability & Dosage Concerns

### Expected Half-Life of exRNA in the Seed Coat Environment

[KNOWN] Extracellular RNA is highly labile:
- **Naked ssRNA** half-life in soil: **minutes to hours** (Levy-Booth et al., 2007)
- **Naked ssRNA** in biological fluids: **seconds to minutes** due to ubiquitous RNases (Tsui et al., 2002)
- **dsRNA** is more stable than ssRNA but still degrades within **hours to days** in soil and aqueous environments (Dubelman et al., 2014; Parker et al., 2019)
- **Soybean seed coat** contains peroxidases, phenolic compounds, and nucleases that create a hostile environment for RNA stability [KNOWN]

[KNOWN] RNA in OMVs or protein complexes (e.g., Argonaute-bound) is protected and can survive longer, but:
- Bacterial small RNAs in OMVs have been demonstrated primarily in animal pathogen contexts (*Pseudomonas aeruginosa*, *Helicobacter pylori*) [KNOWN — Koeppen et al., 2016]
- Evidence for functional delivery of bacterial sRNAs to plant cells via OMVs is extremely limited [INFERRED]

### Required Copy Number for Antisense Effect

[KNOWN] For canonical RNAi/PTGS in plants:
- **Effective siRNA** concentrations in plant cells are typically **100–1,000 copies per cell** for moderate silencing (Molnar et al., 2010)
- **Systemic silencing** requires amplification by RNA-dependent RNA polymerases (RDR6 in *Arabidopsis*, orthologs in soybean: *Glyma.05G157300*)
- **Cross-kingdom RNAi** (the most relevant precedent) has been demonstrated in:
  - *Botrytis cinerea* → *Arabidopsis/tomato*: fungal sRNAs hijack plant AGO1 [KNOWN — Weiberg et al., 2013]
  - *Cuscuta campestris* → host plants: parasitic plant miRNAs silence host genes [KNOWN — Shahid et al., 2018]
  - **In all demonstrated cases**, the donor organism is in intimate, sustained physical contact with the host, allowing continuous delivery over hours to days.

[INFERRED] For a **seed soaking treatment**:
- Contact time is limited (typically minutes to hours)
- RNA must traverse the seed coat (a formidable barrier with cuticular layers, palisade cells, and hourglass cells in soybean)
- RNA must survive the highly oxidative, nuclease-rich spermosphere
- RNA must be loaded into plant AGO complexes to function

### Quantitative Feasibility Assessment

[INFERRED] A back-of-the-envelope calculation:
- Assume EPS solution contains **10⁶–10⁸ sRNA copies/mL** (typical for bacterial culture supernatants — Ghosal et al., 2015)
- Assume **1 mL** treatment volume per seed
- Assume **1%** of RNA survives degradation during treatment
- Assume **0.1%** penetrates the seed coat
- Assume **0.1%** reaches target cells in the embryo
- Net delivery: **10⁶ × 0.01 × 0.001 × 0.001 = 0.01 copies per seed**

[INFERRED] Even with generous assumptions (10¹⁰ copies/mL starting, 10% survival, 1% penetration, 1% cellular uptake), delivery would be **~100 copies per seed** — distributed across millions of cells, yielding **<0.001 copies per cell**. This is **orders of magnitude below** the threshold for antisense silencing.

[SPECULATIVE] Unless:
1. The EPS matrix specifically protects RNA and facilitates uptake (no evidence)
2. An amplification mechanism (RDR-dependent secondary siRNA production) is triggered by even trace amounts (possible but undemonstrated for bacterial sRNAs)
3. The RNA is concentrated in specific cell types (e.g., seed coat surface cells) where local concentrations are higher

### Evidence Level
- RNA instability in extracellular environments: **[KNOWN]**
- Required dosage for silencing: **[KNOWN]**
- Insufficiency of likely delivered dose: **[INFERRED — HIGH CONFIDENCE]**
- Possibility of amplification rescue: **[SPECULATIVE]**

**This is arguably the most critical confounder — it challenges the fundamental mechanistic plausibility of the system.**

---

## 5. Non-specific RNA Effects

### Could Any RNA Sequence Trigger Similar Responses?

[KNOWN] Plants possess innate immune receptors for nucleic acids:

- **dsRNA sensing**: Plants recognize dsRNA as a PAMP/MAMP. In *Arabidopsis*, dsRNA triggers defense gene expression, SA accumulation, and pathogen resistance independent of sequence. Key findings:
  - Niehl et al. (2016, *Science*) demonstrated that dsRNA, regardless of sequence, triggers PTI through **SERK1** and induces antiviral resistance
  - This response is **sequence-independent** and **Dicer-independent**
  - dsRNA perception occurs at the cell surface

- [KNOWN] Bacterial RNA (including tRNA, rRNA fragments) can act as MAMPs in animal systems (TLR3, TLR7, TLR8 ligands). While plants lack TLRs, analogous RNA sensing mechanisms exist. [KNOWN for animals; INFERRED for plants]

- [KNOWN] Poly(I:C) (synthetic dsRNA analog) triggers defense responses in plants [KNOWN — Niehl et al., 2016]

### Pattern-Triggered Immunity from dsRNA

[INFERRED] If the M-9 EPS preparation contains bacterial RNA (virtually certain unless RNase-treated), any observed defense pathway activation could reflect:
1. **dsRNA-triggered PTI** (sequence-independent)
2. **ssRNA-triggered responses** (less characterized in plants but plausible)
3. **CpG DNA-triggered responses** from contaminating bacterial DNA

[INFERRED] The defense/immunity, ROS/redox, and hormone signaling changes attributed to specific antisense targeting could be entirely explained by non-specific nucleic acid MAMP perception.

### Controls Required
1. **RNase A + RNase III treatment** of EPS solution (degrades ssRNA and dsRNA respectively) → compare phenotype
2. **Scrambled sequence RNA** at equivalent concentration and structure
3. **Sense-orientation RNA** (same targets, opposite strand) → should not silence if antisense mechanism is real
4. **Poly(U) or poly(A) RNA** at equivalent concentration → non-specific RNA control
5. **DNase treatment** to control for bacterial DNA effects

### Evidence Level
- dsRNA triggers sequence-independent defense in plants: **[KNOWN]**
- This could explain defense/ROS/hormone pathway changes: **[INFERRED — HIGH CONFIDENCE]**
- Specific antisense targeting has not been distinguished from non-specific effects: **[INFERRED]**

---

## 6. Contamination Signals

### cry8Ba Bacterial Protein Detection — Implications

[KNOWN] Detection of Cry8Ba (a *Bacillus thuringiensis* insecticidal crystal protein) in the preparation has significant implications:

1. **Source identification**: Cry8Ba is produced by *Bt* strains, particularly those active against Coleoptera. Its presence suggests:
   - The M-9 strain may be a *Bt* strain or closely related *Bacillus* [INFERRED]
   - The preparation contains substantial bacterial protein contamination [INFERRED]
   - If Cry8Ba protein is present, the preparation is NOT a purified RNA/EPS fraction [KNOWN]

2. **Protein-mediated effects**: 
   - Cry proteins are known to interact with membrane receptors (aminopeptidase N, cadherin-like proteins, ABC transporters) in insects. While plant homologs exist, direct effects on plant germination are not established. [KNOWN for insect receptors; SPECULATIVE for plant effects]
   - However, the presence of Cry8Ba indicates **co-purification of diverse bacterial proteins**, which may include:
     - Phytohormone-modifying enzymes (IAA, cytokinin biosynthesis)
     - Cell wall-degrading enzymes that could facilitate seed coat penetration
     - Other signaling proteins

3. **Preparation purity**: [INFERRED] If a 130+ kDa crystal protein is present, the preparation almost certainly contains:
   - Bacterial ribosomes and ribosomal RNA
   - Bacterial DNA
   - Lipoproteins and LPS
   - Diverse metabolites
   - Potentially viable spores (Cry proteins are associated with sporulation in *Bt*)

### Quality Control Recommendations

| Analysis | Method | Purpose |
|---|---|---|
| Total protein quantification | Bradford/BCA assay | Assess protein contamination level |
| Proteomics | LC-MS/MS | Identify all bacterial proteins present |
| RNA characterization | Bioanalyzer + small RNA-seq | Confirm presence, size, and identity of sRNAs |
| DNA contamination | qPCR for 16S rRNA gene | Quantify bacterial DNA |
| Endotoxin/LPS | LAL assay | Quantify LPS contamination |
| Viable cell count | Plate counting on LB/nutrient agar | Confirm sterility |
| Metabolomics | LC-MS | Detect phytohormones, siderophores, VOCs |
| Water potential | Vapor pressure osmometry | Characterize osmotic properties |
| Spore viability | Heat treatment + plating | Detect *Bacillus* spores |

### Evidence Level
- Cry8Ba indicates significant protein contamination: **[KNOWN from detection]**
- Preparation is likely a complex mixture, not purified exRNA: **[INFERRED — HIGH CONFIDENCE]**
- Multiple non-RNA components could drive the phenotype: **[INFERRED]**

---

## Confounder Impact Matrix

| Confounder | Likelihood | Impact if True | Distinguishable? | Priority | Est. Phenotype Contribution |
|---|---|---|---|---|---|
| **EPS osmopriming** | Very High (>90%) | Could explain 50–100% of germination phenotype | Yes, with water potential-matched controls | **CRITICAL** | 30–70% |
| **Polysaccharide elicitor/MAMP signaling** | Very High (>90%) | Could explain defense, ROS, hormone changes | Partially, with autoclaved EPS controls | **CRITICAL** | 20–50% |
| **Non-specific RNA/nucleic acid MAMP effects** | High (70–90%) | Could explain defense/immunity pathway changes | Yes, with RNase + scrambled controls | **HIGH** | 10–30% |
| **Bacterial protein contamination** | Very High (>95%, given Cry8Ba) | Unknown magnitude; confounds all molecular analyses | Yes, with protease + ultrafiltration | **HIGH** | 5–30% |
| **Phytohormone contamination** | High (60–80%) | Could directly explain growth promotion | Yes, with LC-MS quantification | **HIGH** | 10–40% |
| **Microbiome alteration** | Moderate (40–60%) | Could explain sustained growth effects | Partially, with 16S profiling | **MODERATE** | 5–20% |
| **RNA dosage insufficiency** | Very High (>95%) | Would invalidate the entire antisense mechanism | Yes, with quantitative RNA tracking | **CRITICAL** | N/A (mechanistic) |
| **Viable bacterial cells/spores** | Moderate (30–50%) | Classical biopriming effect | Yes, with sterility testing | **MODERATE** | 0–30% |

### Summary Assessment

[INFERRED] **Conservative estimate**: 70–95% of the observed germination/vigor phenotype can be plausibly explained by known confounders (osmopriming + elicitor effects + contaminating bioactive molecules) without invoking any antisense RNA mechanism.

[INFERRED] **The antisense RNA mechanism faces a fundamental dosage problem** that has not been addressed. Without demonstrating (a) that sufficient RNA reaches target cells and (b) that specific target transcripts are cleaved or translationally repressed in a sequence-dependent manner, the mechanism remains **[SPECULATIVE]**.

---

## Recommended Controls — Prioritized

### Tier 1: CRITICAL (Must be done before any mechanistic claims)

| Priority | Experiment | Rationale | Expected Outcome if exRNA is NOT the mechanism |
|---|---|---|---|
| **1** | **RNase A + RNase III treatment of EPS solution** → compare germination phenotype | Destroys all RNA while preserving EPS, proteins, metabolites | No significant reduction in germination improvement |
| **2** | **Water potential-matched PEG control** | Isolates osmopriming contribution | PEG control shows similar germination improvement |
| **3** | **Autoclaved EPS solution** (121°C, 20 min) | Destroys RNA and proteins; preserves polysaccharides | Substantial germination improvement persists |
| **4** | **Quantitative small RNA-seq of the preparation** | Confirms presence, identity, and abundance of putative antisense RNAs | Antisense RNAs absent, at trace levels, or not complementary to claimed targets |

### Tier 2: HIGH PRIORITY (Needed for mechanistic validation)

| Priority | Experiment | Rationale |
|---|---|---|
| **5** | **Labeled RNA tracking** (Cy3/Cy5-labeled synthetic antisense RNAs applied in EPS matrix) → confocal microscopy of seed sections at timepoints | Determines whether exogenous RNA penetrates seed coat and reaches embryonic cells |
| **6** | **5' RACE or degradome sequencing** of treated seeds | Detects AGO-mediated cleavage products at predicted target sites — the gold standard for confirming RNAi |
| **7** | **Scrambled sequence RNA control** (same base composition, no complementarity to soybean transcripts) applied in same EPS matrix | Distinguishes sequence-specific from non-specific RNA effects |
| **8** | **Sense-strand RNA control** | Same targets, opposite orientation — should not trigger antisense silencing |
| **9** | **Protease K treatment of EPS solution** → compare phenotype | Removes protein contaminants including Cry8Ba |

### Tier 3: IMPORTANT (For comprehensive mechanistic understanding)

| Priority | Experiment | Rationale |
|---|---|---|
| **10** | **LC-MS metabolomics** of EPS preparation | Detect IAA, cytokinins, gibberellins, ABA, siderophores |
| **11** | **Sterility testing** (aerobic + anaerobic culture, heat-shock for spores) | Rule out viable cell biopriming |
| **12** | **Target transcript quantification** (RT-qPCR of all 18 targets) in RNase-treated vs. untreated EPS-treated seeds | If transcript changes persist after RNase treatment, they are not due to antisense RNA |
| **13** | **Single-target synthetic antisense RNA** application (one target at a time, high concentration in EPS matrix) | Tests whether individual antisense RNAs can produce measurable target knockdown |
| **14** | **Dose-response curve** with purified synthetic antisense RNAs | Determines minimum effective concentration |
| **15** | **AGO-immunoprecipitation + small RNA-seq** from treated seeds | Determines whether exogenous bacterial sRNAs are loaded into plant AGO complexes |

### Tier 4: DEFINITIVE (Publication-grade evidence)

| Priority | Experiment | Rationale |
|---|---|---|
| **16** | **Soybean mutants** in key RNAi pathway genes (*dcl2/dcl4*, *ago1*, *rdr6*) treated with EPS → if phenotype persists, exRNA mechanism is falsified | Genetic requirement for silencing machinery |
| **17** | **Target gene overexpression lines** → if exRNA mechanism is real, overexpression should partially resist the treatment | Genetic complementation |
| **18** | **Synthetic biology reconstruction**: purified synthetic antisense RNAs (all 18) in RNase-free buffer vs. in EPS matrix vs. EPS alone | Full factorial design to decompose contributions |

---

## Conclusion

[INFERRED] **The current evidence base, as described, does not permit confident attribution of the germination phenotype to antisense RNA targeting.** The system contains at minimum five major confounders (osmopriming, polysaccharide elicitation, non-specific nucleic acid sensing, protein contamination, and potential microbiome effects), each of which independently produces phenotypes overlapping with the observed results. The RNA dosage problem represents a fundamental mechanistic challenge that must be addressed quantitatively.

[INFERRED] The most parsimonious explanation for the observed phenotype is a **combination of osmopriming and MAMP-elicitor effects** from the EPS preparation, with possible contributions from contaminating bacterial proteins and metabolites. The antisense RNA mechanism, while intellectually appealing, requires extraordinary evidence given the extraordinary claims of cross-kingdom RNA silencing from a brief seed treatment — evidence that can only come from the Tier 1–2 controls outlined above.

[SPECULATIVE] It remains possible that a small fraction (estimated 0–15%) of the phenotype is attributable to sequence-specific RNA effects, particularly if the preparation contains RNA in protected forms (OMVs, protein complexes) and if plant RDR-dependent amplification can be triggered by very low initial template concentrations. However, this possibility cannot be evaluated without the recommended controls.

**Bottom line: The experiment as described is testing a complex biological mixture against a complex biological system. Without subtractive controls that isolate the RNA component, any mechanistic attribution to antisense targeting is premature.**