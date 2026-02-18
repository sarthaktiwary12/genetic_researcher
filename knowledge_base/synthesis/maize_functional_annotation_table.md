# Comprehensive Functional Annotation Table: 20 Maize (Zea mays) tRF-RNA Drug Targets

**Prepared:** 2026-02-18
**Organism:** Zea mays (B73 v5 reference genome)
**Agent:** Bacterial-derived G-quadruplex-forming tRNA fragments (tRFs), 16-22 nt, glyco-protected, RNase-resistant
**Uptake:** Nucleolin-mediated endocytosis; 25-30% endosomal escape efficiency
**Validation status:** RT-qPCR confirmed for 5 selected targets; RNA uptake and gene regulation treated as experimentally validated
**Evidence labeling:** [KNOWN] = published peer-reviewed literature; [INFERRED] = logical deduction from conserved biology; [SPECULATIVE] = hypothesis requiring further validation

---

## Master Annotation Table

| # | Gene Model ID | Name/Symbol | Best Functional Annotation | Key Protein Domains | Pathway Involvement | Regulator Type (Growth/Yield) | Expected Effect of Downregulation by tRF Drug | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | Zm00001eb197370_T001 | ABI40 | B3/VP1-type ABA-responsive transcription factor (Viviparous1 family) | B3 DNA-binding, VP1/ABI3 transactivation | ABA signaling, seed dormancy maintenance, LEA/Em gene activation, alpha-amylase repression | NEGATIVE regulator of germination; POSITIVE regulator of dormancy | Derepression of germination program: increased alpha-amylase, reduced ABA sensitivity, accelerated dormancy-to-germination transition | **High** |
| 2 | Zm00001eb154520_T001 | HEX6 | Hexokinase-2-like (ZmHXK family member); dual-function glucose sensor and metabolic enzyme | Hexokinase catalytic domain, sugar kinase superfamily | Glucose phosphorylation (glycolysis entry), glucose-ABA signaling crosstalk, sugar sensing/T6P-SnRK1 network | NEGATIVE regulator of germination (via glucose-ABA feedback) | Disruption of glucose-ABA positive feedback loop; embryo rendered insensitive to glucose-mediated germination delay (gin2-like effect); net pro-germination | **High** |
| 3 | Zm00001eb333290_T001 | PRX91 | Peroxidase 72 precursor; class III secretory peroxidase | Plant peroxidase domain, N-terminal signal peptide, heme-binding site | ROS metabolism (peroxidative and hydroxylic cycles), cell wall cross-linking (lignin/suberin polymerization), H2O2 scavenging, apoplastic redox signaling | NEGATIVE regulator of germination timing (cell wall stiffener) | Increased local H2O2 (pro-germination signaling); reduced cell wall cross-linking at radicle tip; earlier testa/endosperm rupture (Atprx16 precedent) | **High** |
| 4 | Zm00001eb385450_T002 | NPF15 | NRT1/PTR family transporter (PTR2/NPF4.6-like); ABA/peptide/hormone transporter | Major Facilitator Superfamily (MFS) fold, 12 transmembrane helices, NPF/POT domain | ABA import (NPF4.6/AIT1 homolog), GA transport, peptide transport, JA-Ile transport, endodermal development | NEGATIVE regulator of germination (imports ABA into embryo) | Reduced ABA import into embryo, lowering local ABA concentration; accelerated germination (ait1 mutant precedent) | **High** |
| 5 | Zm00001eb065740_T001 | AHL9 | AT-hook nuclear localized protein 5 (AT-hook motif family) | AT-hook motif (DNA binding), PPC/DUF296 domain (protein-protein interaction), nuclear localization | Chromatin remodeling at S/MAR regions, repression of auxin biosynthesis (YUCCA9), H2A.Z deposition via SWR1 complex recruitment | NEGATIVE regulator of growth/elongation | Derepression of auxin biosynthesis genes (YUCCA family); enhanced cell elongation in coleoptile, mesocotyl, and radicle; increased seedling vigor | **High** |
| 6 | Zm00001eb044800_T001 | RING63 | RING-HC (C3H2C3) E3 ubiquitin ligase, Hakai-like subfamily | RING-HC zinc finger, C3H2C3 motif, potential Hakai domain | Ubiquitin-proteasome system, ABA signaling component turnover, protein quality control | AMBIGUOUS (depends on substrate identity) | If substrates are growth promoters: inhibits growth (downregulation = pro-growth). If substrates are ABA signaling repressors (like KEG model): downregulation = anti-growth. Substrate ID required. | **Medium** |
| 7 | Zm00001eb194870_T002 | RING265 | RING-IBR-RING (RBR/TRIAD) E3 ubiquitin ligase | RING1-IBR-RING2 supradomain (Ariadne/Parkin family), zinc-binding | Ubiquitin-proteasome system, protein homeostasis during dormancy-germination transition, potential autophagy regulation | AMBIGUOUS (substrate-dependent) | Altered protein turnover rates; potential acceleration or deceleration of dormancy protein clearance depending on substrates | **Medium** |
| 8 | Zm00001eb303410_T002 | ppr377 | Pentatricopeptide repeat (PPR) protein; organellar RNA processing factor | PPR motifs (tandem 35-aa repeats), potential DYW domain (RNA editing) | Mitochondrial/plastid RNA editing, splicing, stabilization; energy metabolism during imbibition | POSITIVE regulator of energy metabolism (supports mitochondrial function) | Potentially counterproductive: impaired mitochondrial transcript processing could reduce ATP production during imbibition; may cause partial CMS-like respiratory deficiency | **Medium** |
| 9 | Zm00001eb159250_T002 | CYP10 (CYP72A14) | Cytochrome P450 monooxygenase, CYP72A subfamily (NOT cyclophilin) | P450 heme-thiolate fold, oxygen-binding pocket, NADPH-cytochrome P450 reductase interaction domain | Oxidative metabolism of terpenoids/hormones; potential ABA catabolism, brassinolide inactivation, or xenobiotic detoxification | CONTEXT-DEPENDENT | Altered hormone catabolism or secondary metabolite profiles; if involved in GA inactivation, downregulation could increase active GA levels (pro-germination); if involved in ABA catabolism, downregulation could increase ABA (anti-germination) | **Medium** |
| 10 | Zm00001eb187270_T001 | MYBR64 | MYB-related single-repeat (R1-MYB) transcription factor; CCA1/CPC-like subfamily | Single MYB/SANT DNA-binding repeat, SHAQKYF motif | Transcriptional regulation of starch mobilization, circadian clock (CCA1/LHY-like), potential germination repression (ZmMYB59 analog) | Likely NEGATIVE regulator of germination (ZmMYB59 paradigm) | Derepression of starch mobilization genes; enhanced alpha-amylase induction; accelerated reserve mobilization during imbibition | **Medium** |
| 11 | Zm00001eb397700_T001 | IBP1 | Initiator Binding Protein 1; SANT/Myb + ubiquitin-like (UBL) domain transcription factor (NOT BiP/GRP78) | SANT/Myb DNA-binding domain, ubiquitin-like domain | Transcriptional regulation of Shrunken-1 (sucrose synthase) promoter; gibberellin signaling modulation; endosperm gene regulation | NEGATIVE regulator of internode elongation; POSITIVE for Sh1 expression | Altered Shrunken-1 expression affecting sucrose synthase levels; modified gibberellin balance; potential changes in sucrose-starch partitioning during germination | **Medium** |
| 12 | Zm00001eb036320_T002 | LOC100273360 | GDT1-like protein 3; Golgi-localized Ca2+/Mn2+ transporter (UPF0016/TMEM165 family) | UPF0016 domain, 2-3 transmembrane segments, EF-hand-like Ca2+-binding motif | Golgi Ca2+/Mn2+ homeostasis, glycosylation quality control (Mn2+ supply to Golgi glycosyltransferases), cell wall matrix polysaccharide synthesis | POSITIVE for Golgi function and cell wall synthesis | Altered intracellular Ca2+/Mn2+ distribution; impaired Golgi glycosylation; potential cell wall compositional changes affecting extensibility | **Low** |
| 13 | Zm00001eb018090_T002 | PRH130 (PP2C32) | Protein phosphatase 2C, Group A (clade A PP2C); negative regulator of ABA signaling (NOT RNA helicase) | PP2C catalytic domain, Mn2+/Mg2+-dependent phosphatase fold | ABA signaling (dephosphorylates/inactivates SnRK2 kinases), stomatal regulation, stress responses | NEGATIVE regulator of ABA signaling (therefore POSITIVE for germination when active) | PARADOXICAL: Downregulation removes negative regulation of ABA signaling, INCREASING ABA sensitivity, stabilizing active SnRK2, enhancing ABI5 phosphorylation -- expected to DELAY germination. Flagged as potential counterexample/internal control. | **High** (annotation confidence high; biological prediction is paradoxical) |
| 14 | Zm00001eb292850_T002 | si614021b09a | O-methyltransferase ZRP4-like; caffeoyl-CoA O-methyltransferase (CCoAOMT) involved in suberin/lignin monomer biosynthesis | AdoMet-dependent methyltransferase domain (SAM binding), dimerization interface | Phenylpropanoid pathway (lignin/suberin biosynthesis), cell wall fortification, Casparian strip formation, defense-related secondary metabolism | POSITIVE for cell wall rigidity/defense | Reduced suberin and lignin biosynthesis; softer cell walls at radicle tip; facilitated radicle protrusion through surrounding tissues | **Medium** |
| 15 | Zm00001eb388550_T001 | PCO145926 (CML21) | Calmodulin-like protein 21 (CML21); EF-hand Ca2+ sensor relay protein | 4 EF-hand Ca2+-binding domains, no enzymatic activity (signal relay only) | Calcium signaling, defense signal transduction, ROS regulation, pathogen response | POSITIVE for defense responses | Attenuated calcium-mediated defense signaling; reduced metabolic investment in pathogen defense during germination window; metabolic resource reallocation toward growth | **Low** |
| 16 | Zm00001eb408850_T001 | IDP8263 | ABA-responsive protein with PH-GRAM (Pleckstrin Homology-Glucosyltransferases, Rab-like GTPase Activators, Myotubularins) lipid-binding domain | PH-GRAM domain (phosphoinositide binding), potential membrane association | ABA signaling at membrane interface, phospholipid signaling, potential vesicle trafficking | POSITIVE for ABA perception/signaling | Reduced ABA perception at membranes; contributes to multi-pronged reduction of ABA sensitivity alongside ABI40 and NPF15 | **Medium** |
| 17 | Zm00001eb136860_T001 | AI714716 (MOS1-like) | MODIFIER OF SNC1 1 (MOS1)-like protein; BAT2/Myb_Cef domain chromatin/immunity regulator | BAT2 domain, Myb_Cef domain, nuclear localization | Chromatin remodeling at immune gene loci, NB-LRR receptor expression modulation (SNC1 regulation in Arabidopsis), epigenetic defense regulation | POSITIVE for constitutive immunity | Reduced constitutive immune gene expression; freed transcriptional and metabolic resources for germination; suppressed autoimmunity-like resource drain | **Medium** |
| 18 | Zm00001eb403550_T001 | Zm00001d048453 (v4) | LRR receptor-like serine/threonine kinase; defense receptor | Leucine-rich repeat (LRR) ectodomain, transmembrane helix, intracellular Ser/Thr kinase domain | Pattern-triggered immunity (PTI), pathogen recognition, MAPK cascade activation, defense hormone signaling | POSITIVE for defense | Reduced pathogen surveillance at cell surface; attenuated PTI signaling; metabolic reallocation from defense to growth during germination | **Low** |
| 19 | Zm00001eb358860_T001 | Zm00001d011422 (v4) / CYP72A15 | Cytochrome P450 72A15; CYP72A subfamily paralog of CYP10/CYP72A14 (distinct locus, chromosome 8) | P450 heme-thiolate fold, oxygen-binding pocket | Oxidative metabolism (paralog of CYP72A14); potentially overlapping substrate specificity with CYP10 but distinct tissue/temporal expression | CONTEXT-DEPENDENT (same as CYP10) | Similar to CYP10: altered oxidative metabolism of hormones or secondary metabolites; functional redundancy with CYP72A14 means single-target knockdown may have limited effect | **Low** |
| 20 | Zm00001eb066630_T001 | Zm00001d001877 (v4) / PSKR1-like | Phytosulfokine receptor 1-like; LRR receptor kinase for the phytosulfokine peptide hormone | LRR ectodomain (island domain for PSK binding), transmembrane helix, intracellular kinase domain | Phytosulfokine signaling (cell proliferation, expansion, differentiation), wound response, defense modulation, root elongation | DUAL: POSITIVE for cell proliferation/growth AND defense modulation | Complex: downregulation reduces PSK-mediated cell proliferation (anti-growth) but also reduces PSK-dependent defense amplification. Net effect depends on tissue context. During germination, may reduce defense investment but also impair cell division in root meristem. | **Low** |

---

## Physiological Impact Assessment Matrix

| # | Gene | Germination | Vegetative Growth | Root Development | Grain Filling | Yield |
|---|---|---|---|---|---|---|
| 1 | ABI40 | PROMOTE [KNOWN] | Neutral [INFERRED] | Neutral [INFERRED] | May reduce dormancy in developing kernel [INFERRED] | Neutral to slight negative (reduced grain dormancy) [SPECULATIVE] |
| 2 | HEX6 | PROMOTE [INFERRED] | Neutral (family redundancy) [INFERRED] | Neutral [INFERRED] | May impair sugar sensing in grain fill [SPECULATIVE] | Neutral [SPECULATIVE] |
| 3 | PRX91 | PROMOTE [INFERRED] | Context-dependent [SPECULATIVE] | May enhance radicle emergence [INFERRED] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] |
| 4 | NPF15 | PROMOTE [INFERRED] | May alter hormone distribution [SPECULATIVE] | May enhance if ABA suppresses root growth [INFERRED] | May reduce ABA import to developing grain [SPECULATIVE] | Context-dependent [SPECULATIVE] |
| 5 | AHL9 | PROMOTE [INFERRED] | PROMOTE (derepressed auxin/elongation) [KNOWN] | PROMOTE (enhanced elongation) [INFERRED] | Neutral [SPECULATIVE] | Potentially positive via vigor [SPECULATIVE] |
| 6 | RING63 | AMBIGUOUS | AMBIGUOUS | AMBIGUOUS | AMBIGUOUS | AMBIGUOUS |
| 7 | RING265 | AMBIGUOUS | AMBIGUOUS | AMBIGUOUS | AMBIGUOUS | AMBIGUOUS |
| 8 | ppr377 | May INHIBIT (reduced mitochondrial ATP) [INFERRED] | May INHIBIT [INFERRED] | May INHIBIT [INFERRED] | May INHIBIT [SPECULATIVE] | May reduce [SPECULATIVE] |
| 9 | CYP10/CYP72A14 | CONTEXT-DEPENDENT | CONTEXT-DEPENDENT | CONTEXT-DEPENDENT | CONTEXT-DEPENDENT | CONTEXT-DEPENDENT |
| 10 | MYBR64 | PROMOTE (if germination repressor) [INFERRED] | Context-dependent [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] |
| 11 | IBP1 | May PROMOTE (altered GA balance) [INFERRED] | May PROMOTE (internode elongation relief) [INFERRED] | Neutral [SPECULATIVE] | May alter Sh1/sucrose synthase expression [INFERRED] | Context-dependent [SPECULATIVE] |
| 12 | LOC100273360 | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | May impair Golgi function [SPECULATIVE] | Neutral [SPECULATIVE] |
| 13 | PRH130/PP2C32 | PARADOXICAL: likely INHIBIT [INFERRED] | INHIBIT (increased ABA sensitivity) [INFERRED] | INHIBIT [INFERRED] | May enhance grain dormancy [SPECULATIVE] | May reduce via ABA hypersensitivity [SPECULATIVE] |
| 14 | si614021b09a/ZRP4 | PROMOTE (softer cell wall) [INFERRED] | May reduce defense [SPECULATIVE] | May enhance (softer root tip tissues) [INFERRED] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] |
| 15 | PCO145926/CML21 | Weak PROMOTE (defense savings) [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] |
| 16 | IDP8263 | PROMOTE (reduced ABA perception) [INFERRED] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] |
| 17 | AI714716/MOS1 | Weak PROMOTE (defense savings) [INFERRED] | May PROMOTE (reduced immune burden) [INFERRED] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | May reduce disease resistance [SPECULATIVE] |
| 18 | LRR-RLK | Weak PROMOTE (defense savings) [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | Neutral [SPECULATIVE] | May reduce disease resistance [SPECULATIVE] |
| 19 | CYP72A15 | CONTEXT-DEPENDENT | CONTEXT-DEPENDENT | CONTEXT-DEPENDENT | CONTEXT-DEPENDENT | CONTEXT-DEPENDENT |
| 20 | PSKR1-like | MIXED: reduced defense but also reduced cell proliferation [SPECULATIVE] | May INHIBIT (reduced PSK-driven proliferation) [INFERRED] | May INHIBIT (PSKR promotes root growth) [KNOWN] | Neutral [SPECULATIVE] | May reduce via impaired cell proliferation [SPECULATIVE] |

---

## Individual Gene Narratives

---

### 1. ABI40 -- Zm00001eb197370_T001 (B3/VP1-type ABA-responsive TF)

**Arabidopsis ortholog:** ABI3 (AT3G24650). **Rice ortholog:** OsVP1 (Os01g0911700).

[KNOWN] ABI40 belongs to the Viviparous1 (VP1)/ABI3 transcription factor family, the single most important master regulator of seed dormancy in cereals. The founding maize member, VP1, activates late embryogenesis abundant (LEA) and Em genes while simultaneously repressing germination-specific genes such as alpha-amylase. Loss-of-function vp1 alleles in maize cause vivipary -- precocious germination of the kernel while still attached to the ear -- demonstrating that VP1 is both necessary and sufficient for dormancy maintenance (Suzuki et al. 2003). In Arabidopsis, abi3 mutants exhibit reduced dormancy, desiccation intolerance, and accelerated germination. In sorghum, the related factors ABI4 and ABI5 bind GA 2-oxidase promoters, linking ABA transcriptional output to gibberellin catabolism (Cantoro et al. 2013). [INFERRED] Downregulation of ABI40 by the tRF drug would phenocopy partial VP1 loss-of-function, reducing ABA-responsive gene expression and derepressing alpha-amylase and other germination enzymes. Even a 40-50% reduction in ABI40 transcript levels could significantly accelerate the dormancy-to-germination transition. This is the highest-value single target in the entire 20-gene panel.

**Known maize mutants:** vp1 (viviparous1) -- vivipary, precocious germination, loss of desiccation tolerance. **Arabidopsis mutants:** abi3-1 through abi3-9 -- reduced dormancy, green seeds, desiccation-sensitive. **Rice mutants:** osvp1 -- reduced dormancy, pre-harvest sprouting susceptibility.

---

### 2. HEX6 -- Zm00001eb154520_T001 (Hexokinase-2-like; glucose sensor)

**Arabidopsis ortholog:** HXK1/GIN2 (AT4G29130). **Rice ortholog:** OsHXK5/OsHXK6.

[KNOWN] Hexokinases serve a dual role as glycolytic enzymes and intracellular glucose sensors. In Arabidopsis, Moore et al. (2003) demonstrated that HXK1 resides in the nucleus where it forms a complex with VHA-B1 and RPT5B to regulate gene expression independent of its catalytic activity. The gin2 (glucose-insensitive 2) mutant, defective in HXK1, is insensitive to high glucose concentrations that normally delay germination through ABA accumulation (Price et al. 2003). In maize, nine HXK genes have been identified; ZmHXK4-6 and ZmHXK9 are mitochondria-localized, while ZmHXK7-8 are cytosolic (Zheng et al. 2019). ZmHXK promoters contain ABA-responsive and sugar-repression cis-elements. [INFERRED] Downregulation of HEX6 by the tRF drug would break the glucose-ABA positive feedback loop that normally restrains germination speed: as starch is mobilized to glucose during imbibition, the reduced HXK signaling capacity would prevent glucose from triggering ABA biosynthesis, effectively uncoupling reserve mobilization from hormonal braking. The nine-member gene family provides metabolic redundancy, meaning the signaling effect would dominate over any metabolic impairment of glycolysis.

**Known Arabidopsis mutants:** gin2-1 (glucose insensitive 2) -- glucose-insensitive germination, altered ABA sensitivity, reduced growth. **Maize mutants:** No direct hex6 mutant described; family redundancy may mask single-gene loss.

---

### 3. PRX91 -- Zm00001eb333290_T001 (Peroxidase 72 precursor; class III PRX)

**Arabidopsis ortholog:** AtPRX16 (AT2G18980) or AtPRX72 (AT5G66390). **Rice ortholog:** OsPRX family members.

[KNOWN] Class III peroxidases perform a paradoxical dual function: in the peroxidative cycle they consume H2O2 to cross-link cell wall polymers (lignin, suberin, extensin), stiffening the wall; in the hydroxylic cycle they generate superoxide and hydroxyl radicals that cleave polysaccharides, loosening the wall (Passardi et al. 2004). The net function of any individual peroxidase depends on its redox environment, substrate availability, and expression pattern. Jemmat et al. (2020) demonstrated that knockout of Arabidopsis AtPRX16 results in significantly earlier testa and endosperm rupture, directly proving that specific class III peroxidases restrict germination timing through cell wall stiffening. Maize contains 119 non-redundant class III peroxidase genes (Wang et al. 2015). [INFERRED] If PRX91 predominantly operates in the peroxidative (ROS-scavenging/wall-stiffening) cycle, its downregulation would simultaneously increase local H2O2 concentrations (pushing through the pro-germination oxidative window) and reduce cell wall cross-linking at the radicle emergence point. The AtPRX16 knockout precedent strongly supports this interpretation.

**Known Arabidopsis mutants:** atprx16 -- earlier testa/endosperm rupture. **Maize studies:** ZmPrx25 overexpression promotes germination under stress (2025); ZmPRX1 overexpression enhances root lignification (Zhai et al. 2024). No prx91 loss-of-function described.

---

### 4. NPF15 -- Zm00001eb385450_T002 (NRT1/PTR family transporter; NPF4.6-like)

**Arabidopsis ortholog:** NPF4.6/AIT1 (AT1G69850). **Rice ortholog:** OsNPF4 family members.

[KNOWN] The NRT1/PTR family (NPF) constitutes one of the largest transporter families in plants. NPF4.6/AIT1 was identified by Kanno et al. (2012) through a functional screen using the ABA receptor complex as a sensor, demonstrating that AIT1 directly imports ABA into cells. The ait1 mutant shows reduced ABA sensitivity during germination and reduced stomatal closure. NPF transporters also transport gibberellins (NPF3; Tal et al. 2016), jasmonoyl-isoleucine (GTR1/NPF2.10; Saito et al. 2015), and peptides. In maize, ZmPTR1 is specifically expressed in scutellar epithelial cells during germination, where it transports peptides derived from endosperm protein hydrolysis into the embryo (Doan et al. 2013). Maize contains 78 NPF genes (Wang et al. 2023). [INFERRED] The strong homology of NPF15 to AIT1 suggests it functions as an ABA importer. Downregulation would reduce ABA influx into the embryo, lowering local ABA concentration and accelerating germination. This target synergizes with ABI40 (reduced ABA transcriptional output) and IDP8263 (reduced ABA membrane perception) to create a three-pronged assault on the ABA axis.

**Known Arabidopsis mutants:** ait1/npf4.6 -- reduced ABA sensitivity, faster germination, impaired stomatal closure. **Maize mutants:** No npf15 loss-of-function described.

---

### 5. AHL9 -- Zm00001eb065740_T001 (AT-hook nuclear localized protein)

**Arabidopsis ortholog:** AHL29/SOB3 (AT3G46870) or AHL27/ESC (AT1G76500). **Rice ortholog:** OsAHL family.

[KNOWN] AT-hook nuclear localized (AHL) proteins bind AT-rich DNA sequences via the AT-hook motif and interact with each other through PPC/DUF296 domains. In Arabidopsis, SOB3/AHL29 and ESC/AHL27 are well-characterized negative modulators of hypocotyl growth (Street et al. 2008). The mechanism was elucidated by Favero et al. (2024): AHL proteins bind S/MAR (scaffold/matrix attachment region) elements in the promoters of growth-promoting genes (including YUCCA9 for auxin biosynthesis) and recruit the SWR1 chromatin remodeling complex to deposit the repressive histone variant H2A.Z, thereby transcriptionally silencing these genes. sob3-dominant gain-of-function produces short hypocotyls; sob3 loss-of-function produces elongated hypocotyls. The AHL family acts redundantly: Zhao et al. (2013) showed that multiple AHL proteins interact physically to modulate growth. [INFERRED] Downregulation of AHL9 would derepress auxin biosynthesis genes and other growth-promoting targets, leading to enhanced cell elongation in the coleoptile, mesocotyl, and radicle. This directly addresses the observed "seedling vigor" phenotype and represents one of the clearest mechanistic links between a specific target and the growth component of the M-9 response.

**Known Arabidopsis mutants:** sob3-D (dominant) -- short hypocotyl; sob3 loss-of-function -- elongated hypocotyl; esc/ahl27 -- similar elongation phenotype. **Maize mutants:** No ahl9 loss-of-function described.

---

### 6. RING63 -- Zm00001eb044800_T001 (RING-HC E3 ubiquitin ligase, Hakai-like)

**Arabidopsis ortholog:** Hakai-like RING-HC E3 ligases. **Rice ortholog:** Not specifically identified.

[KNOWN] The maize genome encodes 590 RING-type E3 ubiquitin ligases (Li et al. 2025), making this one of the largest protein families. RING E3 ligases are central to ABA signaling: KEG targets ABI5 for degradation during non-stress conditions (Stone et al. 2006); AIP2 targets ABI3 for degradation (Zhang et al. 2005); ZmXerico1/2 target ABA 8'-hydroxylase for degradation, thereby elevating ABA levels (Brugiere et al. 2017). The Hakai subfamily in animals is involved in E-cadherin ubiquitination and epithelial-to-mesenchymal transitions; plant Hakai-like proteins are poorly characterized but may participate in RNA methylation (m6A modification) pathway regulation. [INFERRED] Without knowing the specific substrates of RING63, the direction of its effect on germination cannot be determined. If RING63 targets negative regulators of growth for degradation (analogous to SDIR1), then its downregulation would stabilize growth repressors (anti-germination). If it targets ABA signaling components like ABI3/ABI5 (analogous to AIP2/KEG), its downregulation would stabilize these repressors (also anti-germination). The Hakai-like annotation raises the intriguing possibility of involvement in m6A-mediated mRNA fate regulation during the dormancy-to-germination transition.

**Known maize mutants:** No ring63 mutant. ZmXerico1/2 overexpression increases drought tolerance via elevated ABA (Brugiere et al. 2017).

---

### 7. RING265 -- Zm00001eb194870_T002 (RING-IBR-RING E3 ubiquitin ligase)

**Arabidopsis ortholog:** Ariadne/ARIH family or Parkin-like. **Rice ortholog:** Not specifically identified.

[KNOWN] RING-IBR-RING (RBR) E3 ligases constitute a distinct subfamily characterized by the RING1-IBR-RING2 supradomain. The human Parkin (PARK2) is the best-characterized RBR ligase, involved in mitochondrial quality control and autophagy. In plants, RBR E3 ligases are implicated in protein quality control, stress responses, and hormone signaling. The IBR (In-Between-RING) domain is a zinc-binding fold that positions the RING2 domain for catalysis. RBR ligases have a unique transfer mechanism: ubiquitin is first loaded onto the RING2 active-site cysteine before transfer to the substrate, distinguishing them from conventional RING E3 ligases. [INFERRED] Like RING63, the effect of RING265 downregulation depends on substrate identity. If it mediates quality control of damaged mitochondrial proteins (Parkin-like function), downregulation during the rapid mitochondrial reactivation of imbibition could impair energy metabolism. If it targets dormancy-associated transcription factors, downregulation could alter the timing of their clearance. Combined modulation of RING63 and RING265 would broadly alter the proteostasis landscape during germination.

**Known mutants:** No ring265 loss-of-function in maize. Parkin mutants in Drosophila/human show mitochondrial dysfunction.

---

### 8. ppr377 -- Zm00001eb303410_T002 (PPR protein; organellar RNA processing)

**Arabidopsis ortholog:** AT1G80270 (PPR protein). **Rice ortholog:** Multiple OsPPR members.

[KNOWN] PPR (pentatricopeptide repeat) proteins constitute one of the largest gene families in land plants, with over 400 members in most angiosperms. They are targeted to mitochondria or plastids where they perform sequence-specific RNA recognition, mediating C-to-U editing, group II intron splicing, RNA stabilization, and translation initiation. Loss of specific PPR proteins in maize causes cytoplasmic male sterility (CMS), kernel defects, and embryo lethality. Mitochondrial reactivation during imbibition is extremely rapid: Nietzel et al. (2020) showed that ATP production begins within minutes of hydration, and 412 cysteine residues are redox-switched during this process. [INFERRED] Downregulation of ppr377 could impair the processing of one or more mitochondrial transcripts, reducing respiratory chain complex assembly or function. This would be potentially counterproductive during germination, when energy demand is high. However, if ppr377 is required for editing of a transcript that is dispensable during early germination (e.g., a complex I subunit with partial bypass), the effect might be minimal. This target is flagged as potentially counterproductive.

**Known maize mutants:** emp (empty pericarp) mutations in various PPR genes cause embryo/endosperm defects; dek (defective kernel) mutations in PPR genes impair seed development. No ppr377-specific mutant described.

---

### 9. CYP10 / CYP72A14 -- Zm00001eb159250_T002 (Cytochrome P450 72A14)

**Arabidopsis ortholog:** CYP72A cluster (AT3G14630/CYP72A13, AT3G14620/CYP72A14). **Rice ortholog:** OsCYP72A family.

[KNOWN] The CYP72A subfamily belongs to the CYP72 clan of cytochrome P450 monooxygenases. Maize contains 263 cytochrome P450 genes spanning multiple clans. CYP72A members in various species have been implicated in brassinolide inactivation (CYP72C1/SOB7 in Arabidopsis converts brassinolide to 26-hydroxybrassinolide, an inactive form), triterpenoid oxidation (CYP72A154 in Medicago oxidizes oleanane and hemolytic saponin intermediates), and phytoalexin metabolism. **CRITICAL CORRECTION:** CYP10 was originally misidentified as a cyclophilin due to the shared "CYP" prefix. It is definitively a cytochrome P450 monooxygenase (heme-thiolate fold, NADPH-P450 reductase dependent). [INFERRED] If CYP72A14 inactivates brassinolide (CYP72C1 paradigm), its downregulation would increase active brassinolide levels, promoting cell elongation during germination. If it catalyzes phytoalexin metabolism, downregulation could alter defense compound profiles. The CYP72A subfamily's involvement in brassinolide catabolism is the most pharmacologically interesting possibility.

**Known Arabidopsis mutants:** cyp72c1/sob7 -- overexpression causes dwarfism (excess brassinolide inactivation); loss-of-function may increase active BR levels. No maize cyp72a14 mutant described.

---

### 10. MYBR64 -- Zm00001eb187270_T001 (MYB-related single-repeat R1-MYB TF)

**Arabidopsis ortholog:** CCA1/LHY (circadian clock) or CPC/TRY (trichome/root hair). **Rice ortholog:** OsMYBS1/OsMYBS2.

[KNOWN] MYB-related (single-repeat, R1-MYB) transcription factors are distinguished from R2R3-MYB and 3R-MYB proteins by possessing only one MYB repeat. This subfamily includes the circadian clock components CCA1 and LHY, the trichome/root hair patterning factors CPC and TRY, and the cereal sugar-responsive MYBS1/MYBS2 proteins. In rice, MYBS1 activates alpha-amylase transcription under sugar starvation, while MYBS2 competes for the same promoter elements and represses expression (Lu et al. 2002). In maize, Zhang et al. (2020) demonstrated that ZmMYB59 overexpression negatively regulates germination by reducing GA levels and increasing ABA levels, establishing a direct maize precedent for MYB-mediated germination repression. [INFERRED] If MYBR64 functions analogously to ZmMYB59 or MYBS2 (as a transcriptional repressor of germination/starch mobilization genes), its downregulation would relieve this repression, accelerating alpha-amylase induction and starch mobilization. The R1-MYB classification makes a CCA1/LHY-like or MYBS-like identity most likely.

**Known maize mutants:** ZmMYB59 overexpression lines show reduced germination rate and altered ABA/GA balance (Zhang et al. 2020). No mybr64-specific mutant described.

---

### 11. IBP1 -- Zm00001eb397700_T001 (Initiator Binding Protein 1; SANT/Myb TF)

**Arabidopsis ortholog:** No clear ortholog (novel). **Rice ortholog:** Not identified.

[KNOWN] IBP1 (Initiator Binding Protein 1) was originally cloned from maize as a transcription factor that binds the initiator element of the Shrunken-1 (Sh1) gene promoter. Sh1 encodes sucrose synthase 1, a key enzyme for sucrose metabolism in the endosperm. IBP1 contains a SANT/Myb DNA-binding domain (related to c-Myb) and a ubiquitin-like (UBL) domain, a unique domain architecture among plant transcription factors. Overexpression in tobacco causes reduced internode elongation and altered gibberellin balance, indicating a growth-suppressive function. **CRITICAL CORRECTION:** IBP1 has been repeatedly misannotated as BiP/GRP78 (ER-resident Hsp70 chaperone) in various databases. This is incorrect -- IBP1 is a nuclear transcription factor, not an ER chaperone. The NCBI Gene ID is LOC542426. [INFERRED] Downregulation of IBP1 could relieve transcriptional regulation of Sh1, potentially altering sucrose synthase levels in the endosperm during germination. The gibberellin balance changes observed in tobacco overexpression lines suggest IBP1 downregulation might increase active GA levels, which would promote germination.

**Known maize data:** IBP1 overexpression in tobacco reduces internode elongation. No ibp1 loss-of-function in maize described.

---

### 12. LOC100273360 -- Zm00001eb036320_T002 (GDT1-like Golgi Ca2+/Mn2+ transporter)

**Arabidopsis ortholog:** PAM71/CCHA1 (AT1G64150) for the chloroplast paralog; GDT1/TMEM165 for the Golgi paralog. **Rice ortholog:** OsGDT1-like.

[KNOWN] GDT1-like proteins belong to the UPF0016/TMEM165 family of cation/Ca2+ exchangers localized to the Golgi apparatus (and in some cases chloroplast thylakoids). In yeast, Gdt1p maintains Golgi Ca2+/Mn2+ homeostasis; loss causes glycosylation defects due to Mn2+ depletion in the Golgi lumen (Mn2+ is a cofactor for many glycosyltransferases). In Arabidopsis, the chloroplast-localized paralog PAM71/CCHA1 is required for photosystem II assembly via Mn2+ supply to the oxygen-evolving complex. In humans, TMEM165 mutations cause congenital disorder of glycosylation (CDG) type II. [INFERRED] Downregulation of LOC100273360 could perturb Golgi Ca2+/Mn2+ balance, potentially affecting glycoprotein maturation, cell wall matrix polysaccharide synthesis (which relies on Golgi glycosyltransferases), and calcium-dependent signaling from Golgi stores. The germination relevance is indirect and this target has the lowest priority score (3/10) in the panel.

**Known mutants:** pam71/ccha1 in Arabidopsis -- photosystem II deficiency. gdt1 in yeast -- glycosylation defects. No maize mutant described.

---

### 13. PRH130 / PP2C32 -- Zm00001eb018090_T002 (Protein phosphatase 2C, Group A)

**Arabidopsis ortholog:** ABI1/ABI2/HAB1/PP2CA (Group A PP2Cs). **Rice ortholog:** OsPP2C family.

[KNOWN] Group A PP2C phosphatases are the canonical negative regulators of ABA signaling in the PYR/PYL/RCAR-PP2C-SnRK2 signaling module (Finkelstein et al. 2008). In the absence of ABA, PP2Cs actively dephosphorylate and inactivate SnRK2 kinases. When ABA is present, PYR/PYL receptors bind PP2Cs and inhibit their phosphatase activity, releasing SnRK2s to phosphorylate downstream targets (ABI5, SLAC1, RBOHF, etc.). Loss-of-function pp2c mutants (abi1-1 revertants, hab1, pp2ca) show ABA hypersensitivity: enhanced stomatal closure, delayed germination, and increased stress tolerance. **CRITICAL CORRECTION:** PRH130 was previously confused with an RNA helicase. It is PP2C32, confirmed by NCBI LOC103635536 and the PP2C catalytic domain. [INFERRED] Downregulation of PP2C32 removes a brake on ABA signaling, resulting in constitutively active SnRK2 kinases. This INCREASES ABA sensitivity, which would be expected to DELAY germination, not promote it. **This makes PRH130/PP2C32 a paradoxical target.** Its value lies as an internal control: if M-9 treatment does NOT downregulate PP2C32, it supports the specificity of the tRF drug mechanism. If PP2C32 IS downregulated, the system must rely on other targets overriding this ABA-enhancing effect.

**Known Arabidopsis mutants:** abi1-1 (dominant negative, ABA-insensitive); abi1-1R (revertant, ABA-hypersensitive); hab1 -- ABA hypersensitivity. **Rice mutants:** OsPP2C knockdowns show enhanced drought tolerance and delayed germination.

---

### 14. si614021b09a / ZRP4-like -- Zm00001eb292850_T002 (O-methyltransferase)

**Arabidopsis ortholog:** CCoAOMT1 (AT4G34050) or COMT (AT5G54160). **Rice ortholog:** OsCCoAOMT family.

[KNOWN] ZRP4 was originally identified as a Zea mays Root Preferential gene encoding an O-methyltransferase involved in suberin biosynthesis in the root exodermis and endodermis. The enzyme catalyzes the methylation of caffeoyl-CoA to feruloyl-CoA (CCoAOMT activity) or caffeic acid to ferulic acid/5-hydroxyferulic acid to sinapic acid (COMT activity), both key steps in the phenylpropanoid pathway leading to lignin and suberin monomers. The AdoMet-dependent methyltransferase domain uses S-adenosylmethionine as the methyl donor. Suberin and lignin provide structural integrity, waterproofing, and pathogen resistance to cell walls. [INFERRED] Downregulation of ZRP4-like O-methyltransferase would reduce feruloyl-CoA and sinapoyl-CoA production, resulting in less lignin/suberin deposition. During germination, this would specifically benefit radicle emergence by reducing the mechanical resistance of surrounding pericarp/coleorhiza tissues. The cell wall softening effect is mechanistically complementary to PRX91 downregulation (reduced cross-linking) -- together they represent a two-pronged attack on cell wall rigidity.

**Known Arabidopsis mutants:** ccoaomt1 -- reduced lignin; altered cell wall composition. **Maize studies:** ZRP4 expression is root-preferential, suggesting strongest effect on root tissues.

---

### 15. PCO145926 / CML21 -- Zm00001eb388550_T001 (Calmodulin-like protein)

**Arabidopsis ortholog:** CML21 (AT4G26470) or related CML family members. **Rice ortholog:** OsCML family.

[KNOWN] Calmodulin-like (CML) proteins are EF-hand Ca2+ sensors that relay calcium signals without possessing enzymatic activity themselves. Unlike calmodulins (CaM), CMLs have more divergent structures and are more numerous (approximately 50 CMLs vs. 7 CaMs in Arabidopsis). CMLs participate in defense signaling: CML43 modulates resistance to Pseudomonas syringae, CML37 and CML42 regulate herbivore defense responses, and CML9 modulates both abiotic stress tolerance and innate immunity. CML21 specifically is less well characterized than other family members. [INFERRED] Downregulation of CML21 would attenuate calcium-mediated defense signaling pathways. During the germination window, when defense investment competes with reserve mobilization for metabolic resources, reduced CML21 levels could redirect energy toward growth. However, the effect is likely modest given the large CML gene family redundancy, and the germination relevance is indirect.

**Known Arabidopsis mutants:** cml9 -- altered defense and ABA sensitivity; cml42 -- enhanced herbivore resistance. No cml21-specific mutant phenotype described.

---

### 16. IDP8263 -- Zm00001eb408850_T001 (ABA-responsive PH-GRAM domain protein)

**Arabidopsis ortholog:** Unresolved (PH-GRAM domain proteins). **Rice ortholog:** Not specifically identified.

[KNOWN] The PH-GRAM (Pleckstrin Homology-Glucosyltransferases, Rab-like GTPase Activators, and Myotubularins) domain is a lipid-binding module that recognizes specific phosphoinositides (primarily PI(3,5)P2 and PI(3)P) on endomembranes. PH-GRAM domain proteins function at the membrane-cytosol interface, often involved in vesicle trafficking, autophagy, and signal transduction. The "IDP" prefix derives from the ISU-IBM (Iowa State University-Iowa Breeders) Map4 project, where it was a genetic marker designation, not a gene name. The protein is annotated as ABA-responsive based on expression profiling data (NCBI LOC100285725; Fu et al. 2006). [INFERRED] If IDP8263 functions in ABA perception or signaling at the membrane interface -- perhaps by recruiting ABA signaling components to specific membrane microdomains via phosphoinositide recognition -- its downregulation would reduce ABA signal transduction efficiency. This contributes to the coordinated multi-pronged ABA derepression alongside ABI40 (transcriptional) and NPF15 (transport). The lower annotation confidence (score 7/10) reflects the unresolved Arabidopsis homology.

**Known mutants:** None described for IDP8263 or close homologs in any species.

---

### 17. AI714716 / MOS1-like -- Zm00001eb136860_T001 (Chromatin/immunity regulator)

**Arabidopsis ortholog:** MOS1/AT4G24680. **Rice ortholog:** Not specifically characterized.

[KNOWN] MOS1 (MODIFIER OF SNC1 1) was identified in Arabidopsis through a suppressor screen of snc1 (suppressor of npr1-1, constitutive 1), a gain-of-function TIR-NB-LRR immune receptor that causes constitutive defense activation and dwarfism. MOS1 is required for maintaining proper SNC1 expression levels; mos1 mutants suppress snc1-mediated autoimmunity by reducing SNC1 transcript accumulation. The protein contains a BAT2 (HLA-B-associated transcript 2) domain and a Myb_Cef domain, suggesting chromatin-level regulation of immune gene expression. MOS1 interacts with chromatin at the SNC1 locus and is required for its proper transcriptional regulation. [INFERRED] Downregulation of AI714716/MOS1-like in maize would reduce the expression of NB-LRR immune receptor genes, attenuating constitutive defense gene expression. During germination, when resources are being mobilized from storage to growth, reduced immune gene expression would redirect transcriptional and metabolic resources toward the germination program. The trade-off is increased vulnerability to seed-borne pathogens during imbibition.

**Known Arabidopsis mutants:** mos1 -- suppresses snc1-mediated autoimmunity; reduced NB-LRR expression; enhanced susceptibility to Pseudomonas. No maize AI714716 mutant described.

---

### 18. LRR-RLK -- Zm00001eb403550_T001 (LRR receptor-like Ser/Thr kinase)

**Arabidopsis ortholog:** AT1G12460 or related LRR-RLK XII subfamily. **Rice ortholog:** Not specifically identified.

[KNOWN] LRR-RLKs (Leucine-Rich Repeat Receptor-Like Kinases) comprise the largest receptor kinase family in plants, with over 200 members in Arabidopsis and likely more in maize. They perceive diverse extracellular signals through the LRR ectodomain and transduce them via the intracellular kinase domain to activate MAPK cascades, CDPK pathways, and transcriptional responses. LRR-RLKs mediate both developmental programs (CLAVATA1, BRI1, ERECTA) and defense responses (FLS2, EFR, PEPR1/2). Without precise subfamily classification of this specific gene, functional prediction is limited. The annotation as a defense-related LRR-RLK is based on expression profiling and phylogenetic placement. [INFERRED] Downregulation would reduce cell-surface pathogen surveillance, attenuating pattern-triggered immunity (PTI). During germination, this would free metabolic resources from defense but increase vulnerability to soil-borne pathogens. The low specificity of this annotation (score 4/10) limits confidence in any prediction.

**Known Arabidopsis mutants:** fls2 -- loss of flagellin perception; bri1 -- brassinosteroid insensitive (developmental LRR-RLK). No specific mutant for AT1G12460 described.

---

### 19. CYP72A15 -- Zm00001eb358860_T001 (Cytochrome P450 72A15)

**Arabidopsis ortholog:** CYP72A cluster. **Rice ortholog:** OsCYP72A family.

[KNOWN] CYP72A15 is a paralog of CYP10/CYP72A14, located on a different chromosome (chromosome 8 vs. chromosome 3 for CYP72A14). Both belong to the CYP72A subfamily, confirmed as distinct loci and not duplicates. The CYP72A subfamily in various plant species participates in brassinolide inactivation (CYP72C1 in Arabidopsis), triterpenoid saponin biosynthesis (CYP72A154 in Medicago truncatula), and potentially gibberellin or ABA catabolism. Maize encodes 263 cytochrome P450 genes across multiple families. [INFERRED] CYP72A15 likely has overlapping but not identical substrate specificity with CYP72A14. Simultaneous downregulation of both paralogs by the tRF drug would have a stronger effect than targeting either alone, potentially significantly altering the metabolic flux through whichever pathway they catalyze. If involved in brassinolide inactivation, dual knockdown could substantially increase active brassinolide levels, promoting cell elongation during germination. The lower priority (4/10) reflects less characterization than CYP72A14.

**Known mutants:** No cyp72a15-specific mutant in maize or other species.

---

### 20. PSKR1-like -- Zm00001eb066630_T001 (Phytosulfokine receptor 1-like)

**Arabidopsis ortholog:** PSKR1 (AT2G02220). **Rice ortholog:** OsPSKR1.

[KNOWN] Phytosulfokine (PSK) is a sulfated pentapeptide hormone (Tyr-Ile-Tyr-Thr-Gln, with both Tyr residues sulfonated) that promotes cell proliferation, expansion, and differentiation. PSKR1 is the primary PSK receptor, an LRR-RLK with an island domain in the LRR region that binds PSK. In Arabidopsis, pskr1 mutants show reduced root elongation, smaller rosettes, and altered wound healing. PSK signaling also modulates plant-microbe interactions: it promotes susceptibility to biotrophic pathogens but enhances resistance to necrotrophic pathogens by attenuating salicylic acid signaling and promoting jasmonic acid responses. PSK signaling promotes protoplast growth, callus proliferation, and somatic embryogenesis. [INFERRED] Downregulation of PSKR1-like is a double-edged sword: it would reduce PSK-dependent cell proliferation (potentially anti-growth, especially in root meristems) but also reduce PSK-mediated defense modulation. During germination specifically, the net effect is uncertain. Reduced root meristem activity could impair radicle elongation post-emergence, partially counteracting the pro-germination effects of other targets.

**Known Arabidopsis mutants:** pskr1-1/pskr1-2 -- reduced root length, smaller rosettes, altered callus growth. pskr1 pskr2 double mutants show enhanced phenotypes. **Rice mutants:** OsPSKR knockdown reduces root growth.

---

## Summary Statistics

| Category | Count | Pro-germination | Anti-germination | Ambiguous |
|---|---|---|---|---|
| ABA/dormancy signaling | 4 | 3 (ABI40, NPF15, IDP8263) | 1 (PRH130/PP2C32: paradoxical) | 0 |
| Sugar sensing/metabolism | 2 | 2 (HEX6, MYBR64) | 0 | 0 |
| Chromatin/growth | 2 | 2 (AHL9, IBP1) | 0 | 0 |
| ROS/redox | 1 | 1 (PRX91) | 0 | 0 |
| Proteostasis (E3 ligase) | 2 | 0 | 0 | 2 (RING63, RING265) |
| CYP450 metabolism | 2 | 0 | 0 | 2 (CYP72A14, CYP72A15) |
| Defense reallocation | 4 | 3 (CML21, LRR-RLK, MOS1) | 0 | 1 (PSKR1) |
| Cell wall | 1 | 1 (si614021b09a) | 0 | 0 |
| Organelle RNA | 1 | 0 | 1 (ppr377: potentially counterproductive) | 0 |
| Transport (non-ABA) | 1 | 0 | 0 | 1 (LOC100273360) |
| **TOTAL** | **20** | **12** | **2** | **6** |

### Net Assessment

Of the 20 targets, **12 (60%)** are predicted to have pro-germination effects when downregulated, with evidence ranging from [KNOWN] (ABI40, AHL9) to [INFERRED] (most others). **Two targets (10%)** -- PRH130/PP2C32 and ppr377 -- are predicted to have anti-germination effects when downregulated, serving as important internal controls that argue against a simple "downregulate everything = germination" artifact. **Six targets (30%)** have ambiguous or context-dependent effects that require substrate identification (RING E3 ligases), metabolic characterization (CYP450s), or tissue-specific analysis (PSKR1, GDT1-like) to resolve.

The strong convergence of the top 5 targets (ABI40, HEX6, PRX91, NPF15, AHL9) on a coherent "derepress ABA + accelerate metabolism + loosen cell walls + promote elongation" program provides substantial biological coherence to the overall target list, despite the ambiguous and potentially counterproductive targets.

---

## Key References Used in This Annotation

- Suzuki et al. (2003) Plant Physiol. 132:1664 -- VP1 and viviparous phenotype
- Moore et al. (2003) Science 300:332 -- HXK1 nuclear signaling
- Price et al. (2003) Plant Physiol. 132:1424 -- gin2 germination phenotype
- Kanno et al. (2012) PNAS 109:9653 -- AIT1/NPF4.6 ABA transport
- Street et al. (2008) Plant J. 54:1 -- SOB3/AHL29 growth suppression
- Favero et al. (2024) Nat. Commun. 15:1547 -- AHL-SWR1-H2A.Z mechanism
- Zhang et al. (2020) Front. Plant Sci. 11:564665 -- ZmMYB59 germination repression
- Passardi et al. (2004) Trends Plant Sci. 9:534 -- Peroxidase paradox
- Jemmat et al. (2020) Plant Sci. 298:110565 -- AtPRX16 germination
- Stone et al. (2006) Plant Cell 18:3415 -- KEG/ABI5 degradation
- Zhang et al. (2005) Genes Dev. 19:1532 -- AIP2/ABI3 degradation
- Brugiere et al. (2017) Plant Physiol. 175:1350 -- ZmXerico1/2 ABA homeostasis
- Li et al. (2025) BMC Plant Biol. -- Maize RING gene family
- Finkelstein et al. (2008) Annu. Rev. Plant Biol. 59:387 -- ABA signaling review
- Zheng et al. (2019) BMC Plant Biol. 19:27 -- Maize HXK family
- Wang et al. (2023) Int. J. Mol. Sci. 24:12941 -- Maize NPF family
- Wang et al. (2015) Gene 566:95 -- Maize class III peroxidase family
- Nietzel et al. (2020) PNAS 117:741 -- Mitochondrial reactivation during germination
- Lu et al. (2002) Plant Cell 14:1877 -- MYBS1/MYBS2 alpha-amylase regulation
