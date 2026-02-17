# MAIZE (Zea mays) -- Mechanistic Claims Extraction

## Overview
- Organism: Zea mays (B73 reference genome, ~2.3 Gb)
- Treatment: M-9 bacterial EPS (extracellular polymeric substance) solution, seed soaking 4-8 hours
- Total predicted targets: 20 unique (no true duplicates; two CYP72A paralogs confirmed as distinct loci)
- Evidence level: Gene-level bioinformatic prediction + literature-based mechanistic inference
- Unique features: Paleopolyploid (ancient WGD with extensive segmental duplication), C4 photosynthesis, comprehensive RNAi toolkit (DCL, AGO, RDR gene families), established cross-kingdom RNAi precedents (SIGS, HIGS)
- Phenotype: Germination rate increase, seedling vigor increase, early seedling growth improvement
- Report date: February 2026
- Evidence labeling: [KNOWN] = published peer-reviewed literature; [INFERRED] = logical deduction from conserved biology and target annotations; [SPECULATIVE] = hypothesis requiring experimental validation

---

## Theme 1: ABA/Dormancy Axis Derepression

**Central thesis:** Bacterial exRNAs simultaneously attack multiple nodes of ABA signaling, from the transcription factor level (ABI40) through signal transduction (IDP8263) to hormone transport (NPF15), creating a coordinated reduction in ABA sensitivity that accelerates the dormancy-to-germination transition.

### Claims:

- **Claim 1.1**: Downregulation of ABI40 (VP1-like) reduces ABA sensitivity, derepresses germination-specific genes including alpha-amylase, and accelerates the dormancy-to-germination transition.
  - Genes: ABI40 / Zm00001eb197370 (B3/VP1-type ABA-responsive transcription factor)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] ABI3/VP1-family TFs are master regulators of seed dormancy in cereals. VP1 null mutants exhibit vivipary (precocious germination on the ear) [65]. ABI4 directly promotes ABI5 transcription and represses ABA catabolic genes [66]. In sorghum, ABI4 and ABI5 bind GA 2-oxidase promoters, linking ABA signaling to GA catabolism [67]. [INFERRED] Downregulating ABI40 would reduce ABA sensitivity, derepress germination-specific genes including alpha-amylase, and accelerate the dormancy-to-germination transition. The VP1/ABI3 target alone can produce vivipary in maize, so even partial downregulation of ABI40 could significantly accelerate germination timing.
  - Evidence: Score 10/10 (highest priority). Strongest single-gene evidence from maize viviparous mutant phenotypes.
  - Germination link: Accelerated dormancy-to-germination transition; derepression of alpha-amylase and other germination-specific genes; reduced ABA sensitivity
  - References: Suzuki et al. (2003) [65]; Shu et al. (2013) [66]; Cantoro et al. (2013) [67]; Finkelstein et al. (2008) [29]
  - At homolog: AT3G24650 (ABI3)

- **Claim 1.2**: Downregulation of PRH130/PP2C32 has a paradoxical effect on ABA signaling -- as a negative regulator, its silencing would INCREASE ABA sensitivity and potentially DELAY germination, making it a potential counterexample.
  - Genes: PRH130 / Zm00001eb018090 (Protein phosphatase 2C 32 / PP2C32; Group A PP2C)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] Group A PP2Cs are key negative regulators of ABA signaling. They dephosphorylate and inactivate SnRK2 kinases, which are positive transducers of ABA signals. In the canonical ABA pathway, ABA binds PYR/PYL/RCAR receptors, which then inhibit PP2Cs, releasing SnRK2s to phosphorylate downstream targets including ABI5 and ion channels [29]. [INFERRED] Downregulating PP2C32 would paradoxically INCREASE ABA sensitivity (since PP2C is a negative regulator). This would stabilize active SnRK2, enhance ABI5 phosphorylation, and potentially DELAY germination. **However**, PP2Cs also have ABA-independent functions and some PP2C members positively regulate specific growth processes. The net effect depends on PP2C32's specific substrate repertoire and expression domain. **This target requires careful experimental validation before concluding whether downregulation helps or hinders germination.**
  - Evidence: Score 10/10 (high priority due to informational value as internal control). Flagged as a potential counterexample that could help discriminate between RNA-mediated and non-specific effects.
  - Germination link: Paradoxical -- expected to delay germination if PP2C negative regulatory function is primary. Could serve as internal specificity control: if PRH130 transcripts are NOT downregulated in treated seeds, it supports specificity of the RNA-mediated mechanism.
  - References: Finkelstein et al. (2008) [29]; Stone et al. (2006) [59]; Liu & Stone (2010) [60]
  - At homolog: Group A PP2C family
  - **CRITICAL NOTE**: Originally confused with RNA helicase. Correctly annotated as PP2C32 (NOT an RNA helicase). NCBI LOC103635536; PP2C catalytic domain.

- **Claim 1.3**: Downregulation of IDP8263 reduces ABA perception at membranes, contributing to the multi-pronged attack on ABA signaling.
  - Genes: IDP8263 / Zm00001eb408850 (ABA-responsive PH-GRAM domain protein)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] PH-GRAM domain proteins are involved in membrane-associated signaling. The IDP tag is from ISU-IBM Map4 (a genetic marker, not a gene name). NCBI LOC100285725; Fu et al. 2006. [INFERRED] If IDP8263 functions in ABA perception at membranes, its downregulation would reduce ABA perception, contributing to the coordinated reduction in ABA sensitivity alongside ABI40 and NPF15.
  - Evidence: Score 7/10. Annotation quality is lower; homolog relationship "Unresolved" in Arabidopsis.
  - Germination link: Reduced ABA perception at membranes; contributes to multi-pronged ABA derepression
  - References: Fu et al. (2006); NCBI LOC100285725

- **Claim 1.4**: The coordinated downregulation of ABI40, NPF15, and IDP8263 produces a multi-pronged attack on ABA signaling: reduced transcriptional output (ABI40), reduced ABA import into the embryo (NPF15), and reduced ABA perception at membranes (IDP8263).
  - Genes: ABI40 (Zm00001eb197370), NPF15 (Zm00001eb385450), IDP8263 (Zm00001eb408850)
  - Direction: All downregulated
  - Mechanism: [INFERRED] Three distinct nodes of ABA signaling are simultaneously suppressed, creating a coordinated reduction in ABA sensitivity. This multi-target approach is more robust than single-gene intervention because it attacks the pathway at transcription, transport, and perception levels.
  - Evidence: Multi-target inference based on individual gene evidence
  - Germination link: Accelerated dormancy-to-germination transition through coordinated ABA pathway suppression
  - References: [29, 53, 65, 66, 67]

---

## Theme 2: Sugar-Energy Metabolic Rewiring

**Central thesis:** Bacterial exRNAs modulate sugar sensing (HEX6) and transcriptional regulators of starch mobilization (MYBR64), effectively reprogramming the metabolic landscape to accelerate reserve mobilization and energy production during the critical first 24 hours of imbibition.

### Claims:

- **Claim 2.1**: Downregulation of HEX6 breaks the glucose-ABA positive feedback loop, rendering the embryo insensitive to glucose-mediated germination delay.
  - Genes: HEX6 / Zm00001eb154520 (Hexokinase-2-like; glucose sensor and metabolic enzyme)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] Hexokinases serve dual functions as metabolic enzymes and glucose sensors [68, 69]. In maize, six of nine ZmHXK genes encode catalytically active enzymes, with ZmHXK4-6 and ZmHXK9 mitochondria-localized [37]. Glucose-ABA crosstalk is well-established: glucose accumulation triggers ABA biosynthesis via HXK signaling [68, 69, 70]. The *gin2* mutants are insensitive to glucose-mediated germination delay [70]. [INFERRED] Downregulating HEX6 would reduce glucose sensing capacity, potentially rendering the embryo insensitive to glucose-mediated germination delay (similar to *gin2*). This could break the glucose-ABA positive feedback loop, favoring germination. However, reduced hexose phosphorylation would also impair glycolytic flux. The signaling effect likely dominates over the metabolic effect due to family redundancy.
  - Evidence: Score 9/10. Strong ABA-glucose crosstalk literature.
  - Germination link: Breaks glucose-ABA inhibitory feedback loop; prevents glucose-triggered ABA accumulation during starch mobilization; analogous to *gin2* phenotype
  - References: Jang et al. (1997) [68]; Moore et al. (2003) [69]; Price et al. (2003) [70]; Zhang et al. (2014) [36]; Zheng et al. (2019) [37]
  - At homolog: AT4G29130 (HXK1)

- **Claim 2.2**: Downregulation of MYBR64 relieves transcriptional repression of germination/starch mobilization genes if it functions as a germination repressor like ZmMYB59.
  - Genes: MYBR64 / Zm00001eb187270 (MYB-related single-repeat R1-MYB transcription factor)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] In rice, MYBS1 activates alpha-amylase under sugar starvation, while MYBS2 represses it [79]. In maize, ZmMYB59 overexpression negatively regulates germination by reducing GA levels and increasing ABA [80]. [INFERRED] If MYBR64 functions like ZmMYB59 (a germination repressor), its downregulation would relieve transcriptional repression and accelerate germination. If it functions like MYBS1 (an activator of starch mobilization), its downregulation would impair alpha-amylase induction. The "MYB-related" (single-repeat) classification makes it more likely to be a CCA1/LHY-like or MYBS-like category.
  - Evidence: Score 7/10. MYB-related classification leaves functional ambiguity.
  - Germination link: Derepression of starch mobilization genes; accelerated reserve mobilization
  - References: Lu et al. (2002) [79]; Zhang et al. (2020) [80]
  - At homolog: CCA1/CPC-like

- **Claim 2.3**: Combined HEX6 and MYBR64 downregulation creates a "full throttle" metabolic state where starch is mobilized efficiently but glucose accumulation does not trigger counterbalancing ABA responses.
  - Genes: HEX6 (Zm00001eb154520), MYBR64 (Zm00001eb187270)
  - Direction: Both downregulated
  - Mechanism: [INFERRED] As starch is mobilized to glucose during imbibition, reduced HXK signaling would prevent glucose-triggered ABA accumulation. Simultaneously, if MYBR64 is a germination repressor, its downregulation would derepress starch mobilization genes. Together, this creates a "full throttle" metabolic state: starch is mobilized efficiently but the glucose signal does not trigger a counterbalancing ABA response.
  - Evidence: Combinatorial inference
  - Germination link: Accelerated reserve mobilization without hormone-mediated feedback inhibition
  - References: [37, 68, 69, 70, 79, 80]

---

## Theme 3: Redox-Proteostasis Optimization

**Central thesis:** Bacterial exRNAs fine-tune the ROS landscape (PRX91) and protein turnover machinery (RING63, RING265), optimizing the "oxidative window" for germination and accelerating the clearance of dormancy-associated proteins.

### Claims:

- **Claim 3.1**: Downregulation of PRX91 shifts the oxidative window toward pro-germination H2O2 signaling and reduces cell wall stiffening at the radicle tip.
  - Genes: PRX91 / Zm00001eb333290 (Peroxidase 72 precursor; class III PRX)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] Class III peroxidases have a paradoxical dual function: they can both consume H2O2 (peroxidative cycle, causing cell wall stiffening) and generate ROS (hydroxylic cycle, causing cell wall loosening) [71]. In Arabidopsis, *Atprx16* knockout showed significantly earlier testa and endosperm rupture, indicating that specific PRXs restrict germination timing through cell wall stiffening [72]. In maize, peroxidase activity increases in the scutellar apoplast 24 hours after imbibition [73]. ZmPrx25 overexpression promotes seed germination under stress [46]. [INFERRED] If PRX91 is predominantly a ROS-scavenger/cell wall stiffener, its downregulation would (a) increase local H2O2 levels, potentially pushing through the oxidative window, and (b) reduce cell wall cross-linking, facilitating radicle protrusion. The *Atprx16* precedent supports this interpretation.
  - Evidence: Score 8/10. Strong precedent from Arabidopsis peroxidase knockouts.
  - Germination link: Enhanced H2O2 signaling; reduced cell wall stiffening at radicle emergence point; earlier testa/endosperm rupture
  - References: Passardi et al. (2004) [71]; Jemmat et al. (2020) [72]; Tnani et al. (2014) [73]; ZmPrx25 study (2025) [46]
  - At homolog: AT5G66390

- **Claim 3.2**: Downregulation of RING63 alters protein turnover rates of ABA signaling components, with outcome depending on substrate specificity.
  - Genes: RING63 / Zm00001eb044800 (RING-HC E3 ubiquitin ligase, Hakai-like)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] The maize genome contains 590 RING proteins [74]. RING E3 ligases play critical roles in ABA signaling: KEG targets ABI5 for degradation (KEG loss = ABA hypersensitivity) [59, 60]; AIP2 targets ABI3 for degradation (AIP2 loss = ABA hypersensitivity) [58]; ZmXerico1/2 target ABA 8'-hydroxylase for degradation, elevating ABA [75]. [INFERRED] The effect of RING63 downregulation depends entirely on its substrate specificity. If it targets negative regulators of growth (like SDIR1 targeting SDIRIP1), downregulation could promote germination. If it targets ABI3/ABI5 for degradation (like AIP2/KEG), downregulation would stabilize ABA signaling and inhibit germination. Substrate identification is essential.
  - Evidence: Score 8/10. High relevance but ambiguous direction without substrate data.
  - Germination link: Altered proteolytic clearance of dormancy-associated or growth-associated proteins
  - References: Li et al. (2025) [74]; Zhang et al. (2005) [58]; Stone et al. (2006) [59]; Liu & Stone (2010) [60]; Brugiere et al. (2017) [75]
  - At homolog: RING-HC family

- **Claim 3.3**: Downregulation of RING265 similarly alters ubiquitin-mediated protein turnover, with effects dependent on substrate specificity.
  - Genes: RING265 / Zm00001eb194870 (RING-IBR-RING E3 ubiquitin ligase)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [INFERRED] RING-IBR-RING (RBR) family E3 ligases are involved in proteostasis. Like RING63, the effect on germination depends on which proteins are targeted for degradation. Together with RING63, modulation of these two E3 ligases would alter the turnover rates of dormancy-associated proteins, potentially accelerating their clearance.
  - Evidence: Score 7/10. Lower annotation confidence than RING63.
  - Germination link: Altered protein turnover during dormancy-to-germination transition
  - References: [58, 59, 60, 74]
  - At homolog: RBR E3 family

- **Claim 3.4**: Combined PRX91 and RING63/RING265 modulation optimizes ROS levels while accelerating dormancy protein clearance, facilitating radicle emergence.
  - Genes: PRX91 (Zm00001eb333290), RING63 (Zm00001eb044800), RING265 (Zm00001eb194870)
  - Direction: All downregulated
  - Mechanism: [INFERRED] Downregulating PRX91 increases local H2O2 (pushing through the oxidative window and loosening cell walls), while modulation of RING63/RING265 alters protein turnover rates of dormancy-associated proteins. Combined effect: Optimized ROS + faster protein turnover + looser cell walls = EMERGENCE.
  - Evidence: Combinatorial inference
  - Germination link: Optimized oxidative window plus accelerated proteolytic clearance of dormancy proteins
  - References: [42, 43, 48, 58, 59, 60, 71, 72]

---

## Theme 4: Growth-Defense Reallocation

**Central thesis:** Downregulation of defense-associated genes (CML21, LRR-RLK, PSKR1, MOS1) and cell wall fortification (ZRP4-like O-methyltransferase) reduces metabolic investment in defense during the germination window, redirecting carbon and nitrogen toward reserve mobilization and axis elongation.

### Claims:

- **Claim 4.1**: Downregulation of CML21/PCO145926 reduces calcium-mediated defense signaling, reallocating energy toward germination.
  - Genes: PCO145926 / Zm00001eb388550 (Calmodulin-like protein CML21; EF-hand Ca2+ sensor)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [INFERRED] Calmodulin-like proteins act as Ca2+ sensors in defense signaling. Reducing CML21 levels would attenuate calcium-mediated defense responses, freeing metabolic resources for germination processes.
  - Evidence: Score 5/10. Defense/Ca2+ category; less direct germination relevance.
  - Germination link: Reduced defense expenditure; metabolic reallocation toward growth
  - References: NCBI LOC100193836
  - At homolog: CML family

- **Claim 4.2**: Downregulation of LRR-RLK reduces defense receptor signaling at the cell surface.
  - Genes: Zm00001eb403550 (v4: Zm00001d048453; LRR receptor-like Ser/Thr kinase)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [INFERRED] LRR-RLKs mediate pathogen recognition and defense signaling. During germination, reducing defense receptor activity frees resources for growth.
  - Evidence: Score 4/10. Generic defense receptor; low germination specificity.
  - Germination link: Reduced defense signaling; metabolic reallocation
  - References: NCBI; v5 mapping Zm00001eb403550
  - At homolog: AT1G12460

- **Claim 4.3**: Downregulation of PSKR1-like phytosulfokine receptor alters growth-defense balance.
  - Genes: Zm00001eb066630 (v4: Zm00001d001877; Phytosulfokine receptor 1, PSKR1-like)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [INFERRED] Phytosulfokine (PSK) signaling promotes cell proliferation and growth but also modulates defense. PSKR1 downregulation could shift the balance depending on the dominant function during germination.
  - Evidence: Score 4/10. Dual function complicates interpretation.
  - Germination link: Altered growth-defense balance during germination
  - References: v5 mapping Zm00001eb066630
  - At homolog: AT2G02220

- **Claim 4.4**: Downregulation of MOS1-like/AI714716 reduces chromatin-level immune regulation, potentially derepressing growth genes.
  - Genes: AI714716 / Zm00001eb136860 (MODIFIER OF SNC1 1, MOS1-like; BAT2/Myb_Cef domain chromatin/immunity regulator)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] MOS1 in Arabidopsis modulates SNC1 (a TIR-NB-LRR immune receptor) expression through chromatin remodeling. [INFERRED] Downregulating MOS1-like activity could reduce constitutive immune gene expression, freeing transcriptional and metabolic resources for germination and growth.
  - Evidence: Score 5/10. Epigenetic/immunity interface; indirect germination link.
  - Germination link: Reduced immune gene expression; resource reallocation toward growth
  - References: NCBI LOC103650547; At homolog AT4G24680

- **Claim 4.5**: Downregulation of si614021b09a/ZRP4-like O-methyltransferase reduces suberin/lignin biosynthesis, facilitating radicle emergence.
  - Genes: si614021b09a / Zm00001eb292850 (O-methyltransferase ZRP4-like; suberin/lignin biosynthesis; AdoMet MTase domain)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [INFERRED] ZRP4 is involved in suberin and lignin biosynthesis. Downregulation would reduce cell wall fortification, particularly suberin deposition, potentially facilitating radicle emergence by reducing the mechanical resistance of surrounding tissues.
  - Evidence: Score 5/10. Cell wall category; mechanically relevant to emergence.
  - Germination link: Reduced cell wall rigidity at radicle tip; facilitated radicle protrusion
  - References: NCBI LOC100272885; CCoAOMT homolog

- **Claim 4.6**: The growth-defense reallocation theme is synergistic with Themes 1-3: reduced defense expenditure provides additional metabolic resources to fuel the accelerated germination program.
  - Genes: PCO145926, LRR-RLK, PSKR1-like, AI714716, si614021b09a
  - Direction: All downregulated
  - Mechanism: [INFERRED] Collectively, reduced defense gene expression and cell wall fortification redirect carbon and nitrogen toward reserve mobilization and axis elongation. The O-methyltransferase (si614021b09a) is particularly interesting: its downregulation would reduce cell wall fortification, potentially facilitating radicle emergence.
  - Evidence: Synergistic inference across themes
  - Germination link: Metabolic reallocation from defense to growth during germination window
  - References: [81]

---

## Theme 5: Chromatin/Transcription Regulation

### Claims:

- **Claim 5.1**: Downregulation of AHL9 derepresses auxin biosynthesis and growth-promoting genes, enhancing cell elongation in coleoptile, mesocotyl, and radicle.
  - Genes: AHL9 / Zm00001eb065740 (AT-hook nuclear localized protein 5)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] AHL proteins bind AT-rich DNA via the AT-hook motif and remodel chromatin through S/MAR interactions [76]. SOB3/AHL29 and ESC/AHL27 are growth-suppressive in Arabidopsis: overexpression represses hypocotyl growth [77]. The mechanism involves AHL binding to YUCCA9 promoter S/MAR regions, recruiting the SWR1 chromatin remodeling complex to deposit H2A.Z, repressing auxin biosynthesis [78]. [INFERRED] Downregulating AHL9 would de-repress growth-promoting genes (including auxin biosynthesis), leading to enhanced cell elongation in the coleoptile, mesocotyl, and radicle. This directly addresses the "seedling vigor" phenotype.
  - Evidence: Score 8/10. Strong Arabidopsis precedent for growth suppression.
  - Germination link: Enhanced cell elongation; seedling vigor; derepression of auxin biosynthesis
  - References: Zhao et al. (2013) [76]; Street et al. (2008) [77]; Favero et al. (2024) [78]
  - At homolog: AT2G45850

- **Claim 5.2**: Downregulation of IBP1 alters Shrunken-1 promoter regulation and gibberellin balance.
  - Genes: IBP1 / Zm00001eb397700 (Initiator Binding Protein 1; SANT/Myb + UBL domain transcription factor)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] IBP1 is a transcription factor containing SANT/Myb and ubiquitin-like domains that binds the initiator element of the Shrunken-1 gene. Overexpression in tobacco reduces internode elongation and alters gibberellin balance. **CRITICAL CORRECTION**: IBP1 was originally annotated as "stress/heat-inducible binding protein" suggesting BiP/GRP78. This is incorrect. IBP1 is NOT BiP/GRP78 chaperone. [INFERRED] Downregulating IBP1 could alter Shrunken-1 expression (sucrose synthase) and gibberellin signaling during germination.
  - Evidence: Score 6/10. Novel chromatin/TF category.
  - Germination link: Altered gibberellin balance; modified Shrunken-1 (sucrose synthase) regulation
  - References: NCBI LOC542426

---

## Theme 6: Transport and Ion Homeostasis

### Claims:

- **Claim 6.1**: Downregulation of NPF15/PTR2/NPF4.6 reduces ABA import into the embryo, lowering local ABA concentration and accelerating germination.
  - Genes: NPF15 / Zm00001eb385450 (PTR2/NPF4.6; ABA/peptide transporter)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] NPF4.6/AIT1 in Arabidopsis is an ABA importer; *ait1* mutants show reduced ABA sensitivity during germination [53]. NPF transporters also transport GA, JA-Ile, and peptides [54, 55]. In maize, ZmPTR1 transports peptides from endosperm hydrolysis into the embryo during germination [56]. Tal et al. (2023) demonstrated that NPF-mediated GA/ABA transport facilitates endodermal development [57]. [INFERRED] If NPF15 functions as an ABA importer (like AIT1), its downregulation would reduce ABA import into the embryo, lowering local ABA concentration and accelerating germination. If it is a peptide transporter (like ZmPTR1), its downregulation would impair amino acid supply but not directly affect hormone signaling. The NPF4.6 homology strongly suggests ABA transport activity.
  - Evidence: Score 9/10. Strong homology to AIT1 (ABA importer) with direct germination phenotype.
  - Germination link: Reduced ABA import into embryo; lower local ABA; accelerated germination
  - References: Kanno et al. (2012) [53]; Tal et al. (2016) [54]; Saito et al. (2015) [55]; Doan et al. (2013) [56]; Tal et al. (2023) [57]
  - At homolog: NPF4.6/AIT1

- **Claim 6.2**: Downregulation of LOC100273360/GDT1-like Golgi Ca2+/Mn2+ transporter alters intracellular calcium homeostasis.
  - Genes: LOC100273360 / Zm00001eb036320 (GDT1-like protein 3; Golgi Ca2+/Mn2+ transporter, UPF0016 family)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [INFERRED] GDT1-like transporters maintain Ca2+/Mn2+ homeostasis in the Golgi. Downregulation could alter intracellular calcium distribution, potentially affecting calcium-dependent signaling during germination.
  - Evidence: Score 3/10. Lowest priority target. Indirect germination relevance.
  - Germination link: Altered calcium homeostasis; potential effects on calcium-dependent germination signaling
  - References: NCBI Gene; At homolog PAM71 (AT1G64150)

---

## Theme 7: Organelle RNA Processing

### Claims:

- **Claim 7.1**: Downregulation of ppr377 modulates mitochondrial RNA processing, altering energy metabolism during germination.
  - Genes: ppr377 / Zm00001eb303410 (PPR protein; pentatricopeptide repeat; mitochondrial RNA processing)
  - Direction: Downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] PPR proteins are essential for organellar RNA processing (editing, splicing, stabilization). Mitochondrial reactivation is rapid during imbibition: ATP accumulation and oxygen uptake occur within minutes of hydration [48]. Seed mitochondria are bioenergetically active immediately upon imbibition [49]. [INFERRED] Downregulating ppr377 could modulate mitochondrial transcript processing, altering energy metabolism. However, reduced mitochondrial function during germination would likely be detrimental, making this a potentially counterproductive target.
  - Evidence: Score 6/10. Important organelle RNA processing function but potentially counterproductive.
  - Germination link: Altered mitochondrial energy metabolism; potentially counterproductive
  - References: Nietzel et al. (2020) [48]; Paszkiewicz et al. (2017) [49]
  - At homolog: AT1G80270

---

## Theme 8: Cytochrome P450 Metabolism

### Claims:

- **Claim 8.1**: Downregulation of CYP10/CYP72A14 and its paralog CYP72A15 alters cytochrome P450-mediated metabolism.
  - Genes: CYP10 / Zm00001eb159250 (Cytochrome P450 72A14) and Zm00001eb358860 (v4: Zm00001d011422; Cytochrome P450 72A15)
  - Direction: Both downregulated by exRNA-mediated silencing
  - Mechanism: [KNOWN] CYP72A subfamily members are involved in diverse metabolic reactions. CYP10 resolves to CYP72A14, a cytochrome P450 monooxygenase (NOT a cyclophilin, despite the CYP prefix overlap). CYP72A14 and CYP72A15 are **paralogs** from the same CYP72A subfamily but are distinct loci on different chromosomes (chromosome 3 and chromosome 8 respectively). [INFERRED] CYP72A enzymes may participate in hormone catabolism or secondary metabolism relevant to germination timing.
  - Evidence: CYP72A14 score 6/10; CYP72A15 score 4/10. Metabolic category; functional specificity unclear.
  - Germination link: Altered hormone catabolism or secondary metabolism
  - References: Maize genome cytochrome P450 genes: 263 [87]; NCBI
  - **NOTE**: No true duplicates among the 20 targets. These are confirmed paralogs on distinct chromosomes.

---

## Top Targets (ranked)

| Rank | Gene ID | Annotation | Score | Pathway | Why Top |
|------|---------|------------|-------|---------|---------|
| 1 | Zm00001eb197370 (ABI40) | B3/VP1-type ABA-responsive TF | 10 | ABA/dormancy | VP1 null = vivipary; master regulator of dormancy; strongest single-gene evidence |
| 2 | Zm00001eb018090 (PRH130) | PP2C32; negative regulator of ABA signaling | 10 | ABA/dormancy | Paradoxical target (may DELAY germination); critical internal control |
| 3 | Zm00001eb154520 (HEX6) | Hexokinase-2-like; glucose sensor | 9 | Sugar sensing | Glucose-ABA crosstalk; *gin2* precedent; breaks inhibitory feedback loop |
| 4 | Zm00001eb385450 (NPF15) | PTR2/NPF4.6; ABA/peptide transporter | 9 | Transport/ABA | AIT1 homology; *ait1* mutant reduced ABA sensitivity; hormone transport hub |
| 5 | Zm00001eb333290 (PRX91) | Peroxidase 72 precursor; class III PRX | 8 | ROS/redox | *Atprx16* knockout = earlier germination; dual ROS/cell wall function |
| 6 | Zm00001eb044800 (RING63) | RING-HC E3 ubiquitin ligase (Hakai-like) | 8 | Ubiquitin/proteostasis | 590 RING genes in maize; ABA signaling turnover; substrate-dependent |
| 7 | Zm00001eb065740 (AHL9) | AT-hook nuclear localized protein 5 | 8 | Chromatin/growth | SOB3/AHL29 repress growth; AHL9 silencing derepresses auxin/elongation |
| 8 | Zm00001eb187270 (MYBR64) | MYB-related single-repeat R1-MYB TF | 7 | Chromatin/TF | ZmMYB59 represses germination; CCA1/LHY-like; starch mobilization link |
| 9 | Zm00001eb194870 (RING265) | RING-IBR-RING E3 ubiquitin ligase | 7 | Ubiquitin/proteostasis | RBR family; protein turnover during dormancy-germination transition |
| 10 | Zm00001eb408850 (IDP8263) | ABA-responsive PH-GRAM domain protein | 7 | ABA signaling | Membrane ABA perception; contributes to multi-pronged ABA attack |
| 11 | Zm00001eb159250 (CYP10) | Cytochrome P450 72A14 | 6 | Metabolism | CYP72A subfamily; possible hormone catabolism role |
| 12 | Zm00001eb303410 (ppr377) | PPR protein; mitochondrial RNA processing | 6 | Organelle RNA | Mitochondrial reactivation critical; potentially counterproductive target |
| 13 | Zm00001eb397700 (IBP1) | Initiator Binding Protein 1; SANT/Myb TF | 6 | Chromatin/TF | Binds Shrunken-1 promoter; alters gibberellin balance; NOT BiP/GRP78 |
| 14 | Zm00001eb136860 (AI714716) | MOS1-like; chromatin/immunity regulator | 5 | Epigenetic/defense | Reduces immune gene expression; resource reallocation |
| 15 | Zm00001eb292850 (si614021b09a) | O-methyltransferase ZRP4-like | 5 | Cell wall | Suberin/lignin biosynthesis; reduced cell wall rigidity |
| 16 | Zm00001eb388550 (PCO145926) | Calmodulin-like CML21; Ca2+ sensor | 5 | Defense/Ca2+ | Calcium-mediated defense signaling reduction |
| 17 | Zm00001eb403550 (v4: Zm00001d048453) | LRR receptor-like Ser/Thr kinase | 4 | Defense | Generic defense receptor kinase |
| 18 | Zm00001eb358860 (v4: Zm00001d011422) | Cytochrome P450 72A15 | 4 | Metabolism | CYP72A paralog on chromosome 8; lower priority than CYP72A14 |
| 19 | Zm00001eb066630 (v4: Zm00001d001877) | Phytosulfokine receptor 1 (PSKR1-like) | 4 | Defense/growth | PSK signaling dual role; growth-defense balance |
| 20 | Zm00001eb036320 (LOC100273360) | GDT1-like Golgi Ca2+/Mn2+ transporter | 3 | Transport/ion | UPF0016 family; indirect germination relevance |

---

## Proposed Primary MoA for Maize

### Model A: Hormone-Metabolic Derepression (Primary Driver)

This is the more parsimonious model, supported by the VP1 vivipary precedent.

**Pathway:**
```
Bacterial exRNAs
  |
  |--- Silence ABI40 (VP1-like) -> decreased ABA-responsive gene expression -> increased alpha-amylase
  |
  |--- Silence NPF15 (ABA importer) -> decreased ABA import into embryo -> decreased local ABA
  |
  |--- Silence HEX6 -> decreased glucose-ABA feedback -> break inhibitory loop
  |
  |--- Silence AHL9 -> derepress auxin biosynthesis -> increased cell elongation
  |
  |--- Silence MYBR64 -> derepress germination genes -> increased starch mobilization
  |
  Combined effect: ABA derepression + metabolic acceleration -> FASTER GERMINATION + VIGOR
```

**Testable predictions for Model A:**
- ABA levels will be lower in M-9-treated embryo axes at 12-24 hours vs. controls
- Alpha-amylase activity will be elevated in aleurone/scutellum at 24-48 hours
- Coleoptile/radicle elongation rate will increase before any change in ROS markers
- Exogenous ABA (10 uM) should abolish or reduce the M-9 germination benefit

### Model B: Redox-Proteostasis Acceleration (Primary Driver)

This model invokes a more novel mechanism but is supported by the oxidative window literature.

**Pathway:**
```
Bacterial exRNAs
  |
  |--- Silence PRX91 -> shift oxidative window -> increased H2O2 signaling + decreased cell wall stiffening
  |
  |--- Silence RING63/265 -> alter protein turnover -> accelerate dormancy protein clearance
  |
  |--- Silence ZRP4-like OMT -> decreased lignification -> decreased cell wall rigidity at radicle tip
  |
  |--- Silence ppr377 -> modulate mitochondrial efficiency -> alter energy metabolism
  |
  Combined effect: Optimized ROS + faster protein turnover + looser cell walls -> EMERGENCE
```

**Testable predictions for Model B:**
- ROS profiling (DHE/H2DCFDA) will show altered O2-/H2O2 ratios at 6-12 hours
- Cell wall stiffness (measured by AFM or extensometer) will be reduced at radicle tip
- SOD/CAT/APX enzyme activity ratios will differ between treatments
- Adding exogenous H2O2 (1 mM) to controls should partially phenocopy M-9 effects

**Distinguishing experiment:** Measure ABA levels AND ROS profiles simultaneously at 12 hours. If ABA changes precede ROS changes, Model A is primary. If ROS changes precede ABA changes, Model B is primary. If both change simultaneously, a combined model operates.

---

## Alternative Model: EPS Osmopriming

**What EPS alone explains:**

EPS osmopriming is the highest-concern confounder (Confounder 1). The bacterial EPS is a hydrated polymer matrix that could produce identical osmopriming effects simply through water activity modulation, without any RNA involvement.

**Specifically, EPS osmopriming could explain:**
1. **100% of the germination improvement** -- hydropriming and osmopriming are well-established technologies that improve maize germination under various conditions [7, 64]
2. **Faster imbibition** -- EPS matrix modulates water uptake kinetics during the 4-8 hour soak
3. **Enhanced seedling vigor** -- priming effects carry through to early seedling growth
4. **Metabolic pre-activation** -- priming allows metabolic reactivation before full imbibition begins

**What EPS alone does NOT explain (if the exRNA hypothesis is correct):**
1. Target-specific transcript downregulation (should be absent in RNase-treated EPS)
2. Gene-specific effects (different targets would show different responses)
3. Dose-dependency at sub-osmotic concentrations

**Six confounders identified:**
1. **EPS Osmopriming** (HIGHEST CONCERN) -- Control: EPS (intact) vs. EPS (RNase-treated) vs. synthetic hydrogel (equivalent water activity) vs. water-only
2. **Polysaccharide Elicitor Effects** -- Bacterial EPS polysaccharides can trigger plant defense priming and induce organ-specific resistance responses [81]. Control: Heat-denatured EPS vs. intact EPS
3. **Biopriming by Residual Bacteria** -- The maize seed-borne bacteriome influences germination [26]. Control: Filter-sterilize (0.22 um) vs. UV-sterilize vs. untreated EPS
4. **Nutrient Effects** -- EPS matrix contains proteins, amino acids, and minerals. Control: Dialyzed EPS vs. dialysate-only vs. complete EPS
5. **pH and Ionic Strength Effects** -- EPS solution may alter local pH and ionic environment. Control: Buffer-matched controls
6. **Bioinformatic False Positives** -- Computational prediction of sRNA-mRNA complementarity generates high false-positive rates in a 2.3 Gb genome [21]. Control: RT-qPCR validation

**The Killer Experiment (RNase elimination test):**
- Protocol: Prepare M-9 EPS -> split into three aliquots: (A) Untreated M-9, (B) M-9 + RNase A (100 ug/mL, 37C, 1 hour), (C) M-9 + heat-inactivated RNase A. Treat B73 inbred seeds (n=50 per treatment, 4 replicates). Soak 4-8 hours. Score germination at 24, 48, 72, 96 hours.
- Interpretation: If B ~ C << A: RNA is essential. If B ~ C ~ A: RNA is not essential. If B < A but B > C: Partial RNA contribution.
- Cost: ~$200-500; Timeline: 2 weeks; Decision value: CRITICAL

---

## Annotation Corrections (Critical)

| Original Name | Incorrect Assumption | Correct Identity | Evidence |
|---|---|---|---|
| IBP1 | BiP/GRP78 (ER chaperone) | Initiator Binding Protein 1; SANT/Myb + UBL domain TF | NCBI LOC542426; binds Shrunken-1 promoter |
| PRH130 | RNA helicase | PP2C32 (Protein phosphatase 2C 32) | NCBI LOC103635536; PP2C catalytic domain |
| CYP10 | Cyclophilin (CYP prefix overlap) | CYP72A14 (Cytochrome P450 monooxygenase) | CYP prefix = cytochrome P450, not cyclophilin |
| IDP8263 | Gene name | ISU-IBM Map4 genetic marker tag | NCBI LOC100285725; Fu et al. 2006 |

---

## v4-to-v5 Gene Model Mappings

| V4 ID | V5 ID | Annotation |
|---|---|---|
| Zm00001d048453 | Zm00001eb403550 | LRR receptor-like Ser/Thr kinase |
| Zm00001d011422 | Zm00001eb358860 | Cytochrome P450 72A15 |
| Zm00001d001877 | Zm00001eb066630 | Phytosulfokine receptor 1 (PSKR1-like) |

---

## Duplicate Analysis

CYP10 (Zm00001eb159250 / CYP72A14) and Zm00001d011422 (Zm00001eb358860 / CYP72A15) are **paralogs** from the same CYP72A subfamily but are distinct loci on different chromosomes (chromosome 3 and chromosome 8 respectively). No true duplicates were found among the 20 entries.

---

## Maize-Specific RNAi Context

- **Genome**: B73 reference (Schnable et al. 2009) [21]; ~2.3 Gb; ~32,000-39,000 protein-coding genes; paleopolyploid with extensive segmental and tandem duplications
- **RNAi toolkit**: DCL (Dicer-like): Multiple paralogs; AGO (Argonaute): Multiple paralogs with tissue-specific expression; RDR (RNA-dependent RNA polymerase): Amplification of silencing signal. Identified by Qian et al. (2011) [9] and Zhai et al. (2014) [10].
- **AGO stress response**: Qin et al. (2019) demonstrated maize AGO genes are differentially expressed in response to abiotic stress [22]
- **SIGS precedent**: Koch et al. (2016) demonstrated spray-induced gene silencing in cereals against *Fusarium graminearum* [11]; Wang et al. (2016) established bidirectional cross-kingdom RNAi [13]
- **Gene family sizes relevant to targets**: Class III peroxidase genes: 119 [45]; RING E3 ubiquitin ligase genes: 590 [74]; NPF transporter genes: 78 [50]; Hexokinase genes: 9 [36]; Cytochrome P450 genes: 263 [87]

---

## Validation Plan Summary

### Tier 1: Essential Experiments (Weeks 1-4, ~$1,500)
1. **Experiment 1: RNase Elimination** -- The "Killer Experiment"; go/no-go decision on RNA involvement
2. **Experiment 2: Target Transcript Quantification** -- RT-qPCR on 10 high-priority targets (Ranks 1-10); timepoints 0, 6, 12, 24, 48 hours; reference genes: ZmActin, ZmTubulin, ZmEF1a, ZmUBQ; geNorm [82] and NormFinder [83]; 2^-DDCt method [84, 85]
3. **Experiment 3: ABA/GA Quantification** -- LC-MS/MS of ABA, GA1, GA4 in embryo axes; timepoints 0, 6, 12, 24 hours

### Tier 2: Mechanistic Discrimination (Weeks 5-8, ~$1,200)
4. **Experiment 4: Alpha-Amylase and Invertase Activity** -- DNS reducing sugar method in aleurone/scutellum; Invertase: CWI, VI, total activity in embryo axes; timepoints 0, 12, 24, 48, 72 hours
5. **Experiment 5: ROS and Antioxidant Profiling** -- DHE fluorescence (O2-); H2DCFDA fluorescence + Amplex Red (H2O2); SOD, CAT, APX, GR enzyme panel; timepoints 6, 12, 24, 48 hours

### Tier 3: Conclusive Evidence (Weeks 9-12, ~$900)
6. **Experiment 6: Degradome Sequencing (PARE)** -- Parallel Analysis of RNA Ends [86] in M-9-treated vs. control at 24 hours; direct evidence of sRNA-guided mRNA cleavage at predicted target sites
7. **Experiment 7: Synthetic sRNA Mimics** -- Design synthetic 21-nt RNA duplexes for top 3 predicted bacterial sRNAs; apply to maize seeds during imbibition (with transfection reagent); sufficiency test

### Maize-Specific Experimental Considerations
1. **Inbred selection**: B73 recommended (reference genotype); alternatives W22 (Mutator transposon) or Mo17 (hybrid vigor)
2. **Germination conditions**: 25-28C, dark, paper towel roll method per ISTA protocols; score radicle emergence (>=2 mm) at 24-hour intervals
3. **Tissue dissection**: Separate embryo axis, scutellum, and endosperm for tissue-specific expression analysis
4. **Imbibition timing**: Apply M-9 during Phase I (0-8 hours) for maximum uptake; Phase II transition (~8-18 hours) represents the metabolic reactivation window
5. **Dose-response**: Test M-9 at 0.5x, 1x, 2x, and 4x standard concentration

### Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| EPS effect is entirely osmopriming | Medium-High | Fatal to hypothesis | RNase experiment (Tier 1) |
| Target predictions are false positives | Medium | Reduces actionable targets | RT-qPCR validation panel |
| sRNAs don't survive imbibition | Medium | Fatal to hypothesis | RNA extraction from imbibed seeds |
| PRH130 downregulation delays germination | Medium | Contradicts phenotype | Internal specificity control |
| PPR377 downregulation harms energy metabolism | Medium | Counterproductive target | Does not affect other targets |
| Effect is real but too small to commercialize | Medium | Limits application | Dose-response optimization |

---

## Key References

[1] Bewley JD. (1997) Seed germination and dormancy. *Plant Cell*, 9(7): 1055-1066. DOI: 10.1105/tpc.9.7.1055

[2] Bewley JD, Bradford KJ, Hilhorst HWM, Nonogaki H. (2013) Seeds: Physiology of Development, Germination and Dormancy. 3rd Edition. Springer. DOI: 10.1007/978-1-4614-4693-4

[3] Finkelstein R, Reeves W, Ariizumi T, Steber C. (2008) Molecular aspects of seed dormancy. *Annual Review of Plant Biology*, 59: 387-415. DOI: 10.1146/annurev.arplant.59.032607.092740

[4] Weitbrecht K, Muller K, Leubner-Metzger G. (2011) First off the mark: early seed germination. *Journal of Experimental Botany*, 62(10): 3289-3309. DOI: 10.1093/jxb/erq408

[5] Fait A, Angelovici R, Less H, Ohad I, Urbanczyk-Wochniak E, Fernie AR, Galili G. (2006) Arabidopsis seed development and germination is associated with temporally distinct metabolic switches. *Plant Physiology*, 142(3): 839-854. DOI: 10.1104/pp.106.086694

[6] Finch-Savage WE, Leubner-Metzger G. (2006) Seed dormancy and the control of germination. *New Phytologist*, 171(3): 501-523. DOI: 10.1111/j.1469-8137.2006.01787.x

[7] Paparella S, Araujo SS, Rossi G, Wijayasinghe M, Carbonera D, Balestrazzi A. (2015) Seed priming: state of the art and new perspectives. *Plant Cell Reports*, 34(8): 1281-1293. DOI: 10.1007/s00299-015-1784-y

[8] Jisha KC, Vijayakumari K, Puthur JT. (2013) Seed priming for abiotic stress tolerance: an overview. *Acta Physiologiae Plantarum*, 35(5): 1381-1396. DOI: 10.1007/s11738-012-1186-5

[9] Qian Y, Cheng X, Liu Y, Jiang H, Zhu S, Cheng B. (2011) Identification and characterization of Dicer-like, Argonaute and RNA-dependent RNA polymerase gene families in maize. *Plant Cell Reports*, 30(7): 1347-1363. DOI: 10.1007/s00299-011-1046-6

[10] Zhai L, Sun W, Zhang K, Jia H, Liu L, Liu Z, Teng F, Zhang Z. (2014) Identification and characterization of Argonaute gene family and meiosis-enriched Argonaute during sporogenesis in maize. *Journal of Integrative Plant Biology*, 56(11): 1042-1052. DOI: 10.1111/jipb.12205

[11] Koch A, Biedenkopf D, Furch A, Weber L, Rossbach O, Abdellatef E, Linicus L, Johannsmeier J, Jelonek L, Goesmann A, Cardoza V, McMillan J, Mentzel T, Kogel KH. (2016) An RNAi-based control of *Fusarium graminearum* infections through spraying of long dsRNAs. *PLoS Pathogens*, 12(10): e1005901. DOI: 10.1371/journal.ppat.1005901

[12] Bologna NG, Voinnet O. (2014) The diversity, biogenesis, and activities of endogenous silencing small RNAs in Arabidopsis. *Annual Review of Plant Biology*, 65: 473-503. DOI: 10.1146/annurev-arplant-050213-035728

[13] Wang M, Weiberg A, Lin FM, Thomma BPHJ, Huang HD, Jin H. (2016) Bidirectional cross-kingdom RNAi and fungal uptake of external RNAs confer plant protection. *Nature Plants*, 2: 16151. DOI: 10.1038/nplants.2016.151

[14] Weiberg A, Wang M, Lin FM, Zhao H, Zhang Z, Kaloshian I, Huang HD, Jin H. (2013) Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. *Science*, 342(6154): 118-123. DOI: 10.1126/science.1239705

[15] Cai Q, Qiao L, Wang M, He B, Lin FM, Palmquist J, Huang SD, Jin H. (2018) Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. *Science*, 360(6393): 1126-1129. DOI: 10.1126/science.aar4142

[16] He B, Wang H, Liu G, Wang S, Cai Q, Thompson G, Jin H. (2023) Fungal small RNAs ride in extracellular vesicles to enter plant cells through clathrin-mediated endocytosis. *Nature Communications*, 14: 4383. DOI: 10.1038/s41467-023-40093-4

[17] He B, Cai Q, Qiao L, Huang CY, Wang S, Miao W, Ha T, Wang Y, Jin H. (2021) RNA-binding proteins contribute to small RNA loading in plant extracellular vesicles. *Nature Plants*, 7: 342-352. DOI: 10.1038/s41477-021-00863-8

[18] Cai Q, He B, Wang S, Fletcher S, Niu D, Mitter N, Birch PRJ, Jin H. (2021) Message in a Bubble: Shuttling small RNAs and proteins between cells and interacting organisms using extracellular vesicles. *Annual Review of Plant Biology*, 72: 497-524. DOI: 10.1146/annurev-arplant-081720-010616

[19] Dunker F, Trutzenberg A, Rothenpieler JS, Kuhn S, Prols R, Schreiber T, Tissier A, Kemen A, Kemen E, Huckelhoven R, Weiberg A. (2020) Oomycete small RNAs bind to the plant RNA-induced silencing complex for virulence. *eLife*, 9: e56096. DOI: 10.7554/eLife.56096

[20] Rutter BD, Innes RW. (2017) Extracellular vesicles isolated from the leaf apoplast carry stress-response proteins. *Plant Physiology*, 173(1): 728-741. DOI: 10.1104/pp.16.01253

[21] Schnable PS, Ware D, Fulton RS, Stein JC, Wei F, Pasternak S, et al. (2009) The B73 maize genome: complexity, diversity, and dynamics. *Science*, 326(5956): 1112-1115. DOI: 10.1126/science.1178534

[22] Qin F, Sun QW, Huang LM, Chen XS, Zhou DX. (2019) Expression analysis of Argonaute genes in maize in response to abiotic stress. *Hereditas*, 156: 27. DOI: 10.1186/s41065-019-0102-z

[23] Flemming HC, Wingender J. (2010) The biofilm matrix. *Nature Reviews Microbiology*, 8(9): 623-633. DOI: 10.1038/nrmicro2415

[24] Flemming HC, Wingender J, Szewzyk U, Steinberg P, Rice SA, Kjelleberg S. (2016) Biofilms: an emergent form of bacterial life. *Nature Reviews Microbiology*, 14(9): 563-575. DOI: 10.1038/nrmicro.2016.94

[25] Costa OYA, Raaijmakers JM, Kuramae EE. (2018) Microbial extracellular polymeric substances: ecological function and impact on soil aggregation. *Frontiers in Microbiology*, 9: 1636. DOI: 10.3389/fmicb.2018.01636

[26] dos Santos LF, Souta JF, Soares CP, da Rocha LO, Santos MLC, Grativol C, Roesch LFW, Olivares FL. (2021) Insights into the structure and role of seed-borne bacteriome during maize germination. *FEMS Microbiology Ecology*, 97(4): fiab024. DOI: 10.1093/femsec/fiab024

[27] White CN, Proebsting WM, Hedden P, Rivin CJ. (2000) Gibberellins and seed development in maize. I. Evidence that gibberellin/abscisic acid balance governs germination versus maturation pathways. *Plant Physiology*, 122(4): 1081-1088. DOI: 10.1104/pp.122.4.1081

[28] White CN, Rivin CJ. (2000) Gibberellins and seed development in maize. II. Gibberellin synthesis inhibition enhances abscisic acid signaling in cultured embryos. *Plant Physiology*, 122(4): 1089-1097. DOI: 10.1104/pp.122.4.1089

[29] Finkelstein R, Reeves W, Ariizumi T, Steber C. (2008) Molecular aspects of seed dormancy. *Annual Review of Plant Biology*, 59: 387-415. DOI: 10.1146/annurev.arplant.59.032607.092740

[30] Linkies A, Leubner-Metzger G. (2012) Beyond gibberellins and abscisic acid: how ethylene and jasmonates control seed germination. *Plant Cell Reports*, 31(2): 253-270. DOI: 10.1007/s00299-011-1180-1

[31] Doehlert DC, Kuo TM, Felker FC. (1991) Isolation of alpha-amylases and other starch degrading enzymes from endosperm of germinating maize. *Plant Science*, 78(1): 39-47. DOI: 10.1016/0168-9452(91)90192-B

[32] Lauriere C, Doyen C, Thevenot C, Daussant J. (1992) Beta-amylases in cereals: a study of the maize beta-amylase system. *Plant Physiology*, 100(2): 887-893. DOI: 10.1104/pp.100.2.887

[33] Frias I, Bernal-Lugo I. (1998) Amylases synthesis in scutellum and aleurone layer of maize seeds. *Phytochemistry*, 48(4): 597-604. DOI: 10.1016/S0031-9422(97)00964-3

[34] de Barros EG, Larkins BA. (1990) Purification and characterization of zein-degrading proteases from endosperm of germinating maize seeds. *Plant Physiology*, 94(1): 297-303. DOI: 10.1104/pp.94.1.297

[35] Eastmond PJ. (2006) SUGAR-DEPENDENT1 encodes a patatin domain triacylglycerol lipase that initiates storage oil breakdown in germinating Arabidopsis seeds. *Plant Cell*, 18(3): 665-675. DOI: 10.1105/tpc.105.040543

[36] Zhang Z, Zhang J, Chen Y, Li R, Wang H, Ding L, Wei J. (2014) Isolation, structural analysis, and expression characteristics of the maize hexokinase gene family. *Molecular Biology Reports*, 41(11): 7793-7807. DOI: 10.1007/s11033-014-3495-9

[37] Zheng S, Lu J, Yu D, Li J, Zhou H, Jiang D, Liu Z, Zhuang C. (2019) Biochemical properties and subcellular localization of six members of the HXK family in maize and its metabolic contribution to embryo germination. *BMC Plant Biology*, 19: 27. DOI: 10.1186/s12870-018-1605-x

[38] Cheng WH, Taliercio EW, Chourey PS. (1996) The Miniature1 seed development locus of maize encodes a cell wall invertase required for normal development of endosperm and maternal cells in the pedicel. *Plant Cell*, 8(6): 971-983. DOI: 10.1105/tpc.8.6.971

[39] Sanchez-Linares L, Gavilanes-Ruiz M, Diaz-Pontones D, Guzman-Chavez F, Calzada-Alejo V, Zurita-Villegas V, Luna-Loaiza V, Moreno-Sanchez R, Bernal-Lugo I, Sanchez-Nieto S. (2012) Early carbon mobilization and radicle protrusion in maize germination. *Journal of Experimental Botany*, 63(12): 4513-4526. DOI: 10.1093/jxb/ers130

[40] Tsai AY-L, Gazzarrini S. (2014) Trehalose-6-phosphate and SnRK1 kinases in plant development and signaling: the emerging picture. *Frontiers in Plant Science*, 5: 119. DOI: 10.3389/fpls.2014.00119

[41] Cosgrove DJ. (2000) Loosening of plant cell walls by expansins. *Nature*, 407(6802): 321-326. DOI: 10.1038/35030000

[42] El-Maarouf-Bouteau H, Bailly C. (2008) Oxidative signaling in seed germination and dormancy. *Plant Signaling and Behavior*, 3(3): 175-182. DOI: 10.4161/psb.3.3.5539

[43] Bailly C. (2004) Active oxygen species and antioxidants in seed biology. *Seed Science Research*, 14(2): 93-107. DOI: 10.1017/S0960258504000133

[44] Wojtyla L, Lechowska K, Kubala S, Garnczarska M. (2016) Different modes of hydrogen peroxide action during seed germination. *Frontiers in Plant Science*, 7: 66. DOI: 10.3389/fpls.2016.00066

[45] Wang Y, Wang Q, Zhao Y, Han G, Zhu S. (2015) Systematic analysis of maize class III peroxidase gene family reveals a conserved subfamily involved in abiotic stress response. *Gene*, 566(1): 95-108. DOI: 10.1016/j.gene.2015.04.041

[46] ZmPrx25 study. (2025) Maize Peroxidase ZmPrx25 modulates apoplastic ROS homeostasis and promotes seed germination. *Antioxidants*, 14(9): 1067. DOI: 10.3390/antiox14091067

[47] Zhai X, Yan X, Zenda T, et al. (2024) Overexpression of the peroxidase gene ZmPRX1 increases maize seedling drought tolerance by promoting root development and lignification. *The Crop Journal*, 12(3): 753-765. DOI: 10.1016/j.cj.2024.04.008

[48] Nietzel T, Mostertz J, Ruberti C, Nee G, Fuchs P, Wagner S, Moseler A, Muller-Schussele SJ, Benamar A, Poschet G, et al. (2020) Redox-mediated kick-start of mitochondrial energy metabolism drives resource-efficient seed germination. *PNAS*, 117(1): 741-751. DOI: 10.1073/pnas.1910501117

[49] Paszkiewicz G, Gualberto JM, Benamar A, Macherel D, Logan DC. (2017) Arabidopsis seed mitochondria are bioenergetically active immediately upon imbibition. *Plant Cell*, 29(1): 109-128. DOI: 10.1105/tpc.16.00700

[50] Wang J, Li Y, Zhu F, Ming R, Chen LQ. (2023) Genome-wide identification and functional analysis of nitrate transporter genes in maize. *International Journal of Molecular Sciences*, 24(16): 12941. DOI: 10.3390/ijms241612941

[51] Xia X, Wei Q, Xiao C, Ye Y, Li Z, et al. (2023) Genomic survey of NPF and NRT2 transporter gene families in five inbred maize lines. *Genomics*, 115(2): 110555. DOI: 10.1016/j.ygeno.2022.110555

[52] Leran S, Varala K, Boyer JC, Chiurazzi M, Crawford N, et al. (2014) A unified nomenclature of NITRATE TRANSPORTER 1/PEPTIDE TRANSPORTER family members in plants. *Trends in Plant Sciences*, 19(1): 5-9. DOI: 10.1016/j.tplants.2013.08.008

[53] Kanno Y, Hanada A, Chiba Y, Ichikawa T, Nakazawa M, Matsui M, Koshiba T, Kamiya Y, Seo M. (2012) Identification of an abscisic acid transporter by functional screening using the receptor complex as a sensor. *PNAS*, 109(24): 9653-9658. DOI: 10.1073/pnas.1203567109

[54] Tal I, Zhang Y, Jorgensen ME, et al. (2016) The Arabidopsis NPF3 protein is a GA transporter. *Nature Communications*, 7: 11486. DOI: 10.1038/ncomms11486

[55] Saito H, Oikawa T, Hamamoto S, et al. (2015) The jasmonate-responsive GTR1 transporter is required for gibberellin-mediated stamen development in Arabidopsis. *Nature Communications*, 6: 6095. DOI: 10.1038/ncomms7095

[56] Doan DNP, et al. (2013) ZmPTR1, a maize peptide transporter expressed in the epithelial cells of the scutellum during germination. *Plant Molecular Biology*. DOI: 10.1007/s11103-013-0073-x

[57] Tal I, Zhang Y, Shani E, et al. (2023) Gibberellin and abscisic acid transporters facilitate endodermal suberin formation in Arabidopsis. *Nature Plants*, 9: 785-802. DOI: 10.1038/s41477-023-01391-3

[58] Zhang X, Garreton V, Chua NH. (2005) The AIP2 E3 ligase acts as a novel negative regulator of ABA signaling by promoting ABI3 degradation. *Genes & Development*, 19(13): 1532-1543. DOI: 10.1101/gad.1318705

[59] Stone SL, Williams LA, Farmer LM, Vierstra RD, Callis J. (2006) KEEP ON GOING, a RING E3 ligase essential for Arabidopsis growth and development, is involved in abscisic acid signaling. *Plant Cell*, 18(12): 3415-3428. DOI: 10.1105/tpc.106.046060

[60] Liu H, Stone SL. (2010) Abscisic acid increases Arabidopsis ABI5 transcription factor levels by promoting KEG E3 ligase self-ubiquitination and proteasomal degradation. *Plant Cell*, 22(8): 2630-2649. DOI: 10.1105/tpc.110.075960

[61] Oracz K, Stawska M. (2016) Cellular recycling of proteins in seed dormancy alleviation and germination. *Frontiers in Plant Science*, 7: 1128. DOI: 10.3389/fpls.2016.01128

[62] Galland M, Huguet R, Arc E, Cueff G, Job D, Rajjou L. (2014) Dynamic proteomics emphasizes the importance of selective mRNA translation and protein turnover during Arabidopsis seed germination. *Molecular & Cellular Proteomics*, 13(1): 1-14. DOI: 10.1074/mcp.M113.032227

[63] Cao Q, Li G, Cui Z, Yang F, Jiang X, Diallo L, Kong F. (2019) Seed priming with melatonin improves the seed germination of waxy maize under chilling stress via promoting the antioxidant system and starch metabolism. *Scientific Reports*, 9: 15044. DOI: 10.1038/s41598-019-51122-y

[64] Ibrahim EA. (2016) Seed priming to alleviate salinity stress in germinating seeds. *Journal of Plant Physiology*, 192: 38-46. DOI: 10.1016/j.jplph.2015.12.011

[65] Suzuki M, et al. (2003) Viviparous1 alters global gene expression patterns through broad regulation of abscisic acid signaling. *Plant Physiology*, 132(3): 1664-1677. DOI: 10.1104/pp.103.024323

[66] Shu K, et al. (2013) ABI4 regulates primary seed dormancy by regulating the biogenesis of abscisic acid and gibberellins in Arabidopsis. *PLoS Genetics*, 9(6): e1003577. DOI: 10.1371/journal.pgen.1003577

[67] Cantoro R, et al. (2013) In vitro binding of Sorghum bicolor transcription factors ABI4 and ABI5 to a conserved region of a GA 2-OXIDASE promoter. *Journal of Experimental Botany*, 64(18): 5721-5731. DOI: 10.1093/jxb/ert347

[68] Jang JC, et al. (1997) Hexokinase as a sugar sensor in higher plants. *Plant Cell*, 9(1): 5-19. DOI: 10.1105/tpc.9.1.5

[69] Moore B, et al. (2003) Role of the Arabidopsis glucose sensor HXK1 in nutrient, light, and hormonal signaling. *Science*, 300(5617): 332-336. DOI: 10.1126/science.1080585

[70] Price J, et al. (2003) Mechanisms of glucose signaling during germination of Arabidopsis. *Plant Physiology*, 132(3): 1424-1438. DOI: 10.1104/pp.103.020347

[71] Passardi F, et al. (2004) Performing the paradoxical: how plant peroxidases modify the cell wall. *Trends in Plant Science*, 9(11): 534-540. DOI: 10.1016/j.tplants.2004.09.002

[72] Jemmat AM, et al. (2020) Coordination of five class III peroxidase-encoding genes for early germination events of Arabidopsis thaliana. *Plant Science*, 298: 110565. DOI: 10.1016/j.plantsci.2020.110565

[73] Tnani H, et al. (2014) Peroxidase activity in scutella of maize in association with anatomical changes during germination. *SpringerPlus*, 3: 399. DOI: 10.1186/2193-1801-3-399

[74] Li Y, et al. (2025) Overview of RING gene family in maize. *BMC Plant Biology*. DOI: 10.1186/s12870-025-06683-8

[75] Brugiere N, et al. (2017) Overexpression of RING domain E3 ligase ZmXerico1 confers drought tolerance through regulation of ABA homeostasis. *Plant Physiology*, 175(3): 1350-1369. DOI: 10.1104/pp.17.01072

[76] Zhao J, et al. (2013) Arabidopsis thaliana AHL family modulates hypocotyl growth redundantly by interacting with each other via the PPC/DUF296 domain. *PNAS*, 110(48): E4688-E4697. DOI: 10.1073/pnas.1219277110

[77] Street IH, et al. (2008) The AT-hook-containing proteins SOB3/AHL29 and ESC/AHL27 are negative modulators of hypocotyl growth in Arabidopsis. *Plant Journal*, 54(1): 1-14. DOI: 10.1111/j.1365-313X.2007.03393.x

[78] Favero DS, et al. (2024) Chromatin attachment to the nuclear matrix represses hypocotyl elongation in Arabidopsis thaliana. *Nature Communications*, 15: 1547. DOI: 10.1038/s41467-024-45577-5

[79] Lu CA, et al. (2002) Three novel MYB proteins with one DNA binding repeat mediate sugar and hormone regulation of alpha-amylase gene expression. *Plant Cell*, 14(8): 1877-1893. DOI: 10.1105/tpc.001735

[80] Zhang Y, et al. (2020) Overexpression of maize ZmMYB59 gene plays a negative regulatory role in seed germination. *Frontiers in Plant Science*, 11: 564665. DOI: 10.3389/fpls.2020.564665

[81] Balmer D, De Papajewski DV, Planchamp C, Glauser G, Mauch-Mani B. (2013) Induced resistance in maize is based on organ-specific defence responses. *Plant Journal*, 74(2): 213-225. DOI: 10.1111/tpj.12114

[82] Vandesompele J, De Preter K, Pattyn F, Poppe B, Van Roy N, De Paepe A, Speleman F. (2002) Accurate normalization of real-time quantitative RT-PCR data by geometric averaging of multiple internal control genes. *Genome Biology*, 3(7): research0034. DOI: 10.1186/gb-2002-3-7-research0034

[83] Andersen CL, Jensen JL, Orntoft TF. (2004) Normalization of real-time quantitative reverse transcription-PCR data: a model-based variance estimation approach. *Cancer Research*, 64(15): 5245-5250. DOI: 10.1158/0008-5472.CAN-04-0496

[84] Livak KJ, Schmittgen TD. (2001) Analysis of relative gene expression data using real-time quantitative PCR and the 2^-DDCt method. *Methods*, 25(4): 402-408. DOI: 10.1006/meth.2001.1262

[85] Schmittgen TD, Livak KJ. (2008) Analyzing real-time PCR data by the comparative C~T~ method. *Nature Protocols*, 3(6): 1101-1108. DOI: 10.1038/nprot.2008.73

[86] German MA, Pillay M, Jeong DH, Hetawal A, Luo S, Janardhanan P, Kannan V, Rymarquis LA, Nobuta K, German R, De Paoli E, Lu C, Schroth G, Meyers BC, Green PJ. (2008) Global identification of microRNA-target RNA pairs by parallel analysis of RNA ends. *Nature Biotechnology*, 26(8): 941-946. DOI: 10.1038/nbt.1505

[87] Buchanan BB, Balmer Y. (2005) Redox regulation: a broadening horizon. *Annual Review of Plant Biology*, 56: 187-220. DOI: 10.1146/annurev.arplant.56.032604.144246
