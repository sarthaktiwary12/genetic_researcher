# Bacterial Extracellular RNA-Mediated Reprogramming of Broccoli (*Brassica oleracea*) Seed Germination: Target Analysis, Mechanistic Models, and Validation Strategy

**Classification:** CONFIDENTIAL | **Prepared by:** Sarthak Tiwary | **Date:** February 2026 | **Version:** 1.0

**Evidence framework:** [Known] = published peer-reviewed data; [Inferred] = logical extrapolation from related systems; [Speculative] = hypothesis requiring validation.

---

## Executive Summary

This report presents a comprehensive analysis of 89 broccoli (*Brassica oleracea* var. *italica*) gene targets predicted to be downregulated by antisense-aligned bacterial extracellular small RNAs (esRNAs) extracted from the EPS preparation "M-9." Broccoli seeds treated with M-9 EPS solution exhibited improved germination rate and seedling vigor compared to water-soaked controls in Petri dish germination assays. Small RNA sequencing of the M-9 preparation identified esRNA fragments that align antisense to *B. oleracea* gene models (TO1000/JZS v1.0 genome), suggesting potential downregulation of 89 transcripts, of which 9 are targeted by multiple independent bacterial sRNAs.

Rigorous annotation enrichment — cross-referencing all 89 Bo-gene identifiers against EnsemblPlants (Release 62), BRAD v3.0, UniProtKB, InterPro, TAIR, and NCBI Gene — yielded **54 annotated targets** (60.7%) and **35 uncharacterized proteins** (39.3%). One critical annotation correction was identified: Bo8g068060.1 was annotated as "MEF2-like TF" but plants do not possess canonical MEF2 transcription factors; this gene encodes a **MADS-box transcription factor** (MIKC-type), with the structural similarity to the animal MEF2 MADS domain being an artifact of automated domain annotation. A minor correction flagged the chitinase (Bo3g036650.1/AT2G43580) as likely catalytically inactive due to missing essential residues. No contamination was detected; all 89 gene IDs conform to the standard *B. oleracea* nomenclature.

The target list is enriched for **defense/immunity components** (7.9%): two cysteine-rich receptor-like kinases (CRK26, CRK29), an RNA-dependent RNA polymerase (RDR), a chitinase, a GH17 beta-1,3-glucanase, a RING/U-box E3 ligase, and a pectinesterase. This pattern is consistent with bacterial esRNA-mediated suppression of host immune surveillance, a strategy documented in *Botrytis cinerea* (Weiberg et al., Science 2013) and *Hyaloperonospora arabidopsidis* (Dunker et al., eLife 2020). Additionally, **epigenetic/RNA regulation** targets (MBD10, RDR, CCCH zinc finger, tRNA dimethyltransferase) and **signal transduction** components (CAK1AT, CDPK15, PP2A-A subunit) suggest a coordinated reprogramming of the defense-dormancy-growth axis.

Among the annotated targets, the highest-priority candidates for explaining improved germination and vigor include: **(1) RDR** (Bo8g102500.1) — RNA-dependent RNA polymerase required for siRNA amplification and RNA-directed DNA methylation (RdDM); **(2) CRK26 + CRK29** (Bo7g119590.1, Bo7g107400.1) — immune receptor kinases mediating pattern-triggered immunity; **(3) MBD10** (Bo8g066360.1) — methyl-CpG-binding domain protein that reads DNA methylation to enforce gene silencing; **(4) ARF** (Bo7g114200.1) — likely a repressor-type auxin response factor maintaining seed dormancy; and **(5) ABCG37/PDR9** (Bo6g067490.1) — ABC transporter for defense compound export and auxin precursor transport. Two competing causal models are presented: (a) esRNA-mediated coordinated knockdown of defense brakes and dormancy gates, and (b) EPS-mediated osmopriming with RNA as a passive bystander. Seven discriminating experiments are proposed.

A distinctive feature of this *B. oleracea* analysis is the species' close evolutionary relationship to *Arabidopsis thaliana* (both Brassicaceae, ~15–20 Mya divergence), enabling strong functional inference from the extensively characterized Arabidopsis gene regulatory network. However, the *B. oleracea* lineage underwent a whole-genome triplication (WGT) event, creating three subgenomes (LF, MF1, MF2) with differential gene fractionation. This WGT must be considered when interpreting esRNA target specificity and functional redundancy.

---

## 1. Introduction and Experimental Context

### 1.1 The Cross-Kingdom RNA Interference Paradigm

Cross-kingdom RNA interference (RNAi) — the transfer of small regulatory RNAs between organisms from different taxonomic kingdoms to modulate gene expression — has emerged as a widespread mechanism in plant-microbe interactions. Weiberg et al. (2013) demonstrated that *Botrytis cinerea* delivers small RNAs into plant cells to hijack the Argonaute/DICER machinery and silence immunity genes [Known]. Cai et al. (2018) showed that *Arabidopsis* reciprocates by exporting sRNAs in extracellular vesicles to silence *Botrytis* virulence genes [Known]. Shahid et al. (2018) extended the paradigm to parasitic plants (*Cuscuta campestris* miRNAs silence host mRNAs), and Buck et al. (2014) demonstrated nematode-to-mammalian cross-kingdom exosomal RNA transfer. He et al. (2021) elucidated the RNA-binding protein machinery that loads sRNAs into plant extracellular vesicles. Zand Karimi et al. (2022) showed that both vesicular and non-vesicular RNA complexes exist in the plant apoplast, expanding the repertoire of extracellular RNA forms. Wang et al. (2016) and Zhang et al. (2016) established bidirectional cross-kingdom RNAi between plants and fungi in multiple crop systems.

### 1.2 Broccoli Seed Germination Biology

Broccoli (*Brassica oleracea* var. *italica*) belongs to the Brassicaceae, sharing conserved germination mechanisms with the model species *Arabidopsis thaliana* and *Lepidium sativum*. Brassicaceae seeds undergo a characteristic **two-step germination process**: testa (seed coat) rupture followed by endosperm rupture (Müller et al., Plant and Cell Physiology 2006) [Known]. The micropylar endosperm cap overlying the radicle tip presents the primary mechanical barrier; its enzymatic weakening is the rate-limiting step for radicle protrusion.

The ABA/GA hormonal axis governs germination timing: ABA maintains dormancy through ABI3/ABI4/ABI5 transcription factors, while GA promotes germination by triggering DELLA protein degradation via the GID1-SLEEPY1 pathway (Piskurewicz et al., Plant Cell 2008) [Known]. During imbibition, ABA is catabolized by CYP707A hydroxylases while GA levels rise, shifting the balance toward germination. Ethylene interacts with ABA to regulate endosperm rupture (Linkies et al., Plant Cell 2009) [Known].

The "oxidative window" model (Bailly et al., C. R. Biologies 2008) posits that germination proceeds only within a critical ROS range — below which insufficient signaling prevents dormancy release, above which oxidative damage impairs viability [Known]. In *Lepidium*, apoplastic ROS produced by NADPH oxidases in the endosperm cap contribute directly to cell wall loosening (Müller et al., J. Exp. Bot. 2009).

*B. oleracea* underwent a whole-genome triplication (WGT) event after diverging from *Arabidopsis*, generating three subgenomes: LF (Least Fractionated), MF1 (Medium Fractionated), and MF2 (Most Fractionated) (Liu et al., Nature Communications 2014) [Known]. This WGT created extensive gene redundancy — most Arabidopsis genes have 2–3 *B. oleracea* paralogs, with average CDS conservation of ~71%. The functional redundancy provides a buffer against esRNA-mediated silencing: partial knockdown of one paralog may be compensated by retained copies.

### 1.3 Experimental Design

Broccoli seeds were soaked in bacterial-derived EPS solution "M-9" for 4–8 hours until full imbibition. Control seeds were soaked in water for the same duration. Petri dish germination tests demonstrated improved germination rate and seedling vigor in M-9-treated seeds. Small extracellular RNA was extracted from M-9, sequenced, and antisense-aligned against the *B. oleracea* transcriptome, yielding 89 predicted target transcripts.

---

## 2. Annotation Enrichment, Corrections, and Genomic Context

### 2.1 Annotation Correction

Cross-referencing all 89 Bo-gene identifiers revealed one critical annotation error:

| # | Bo Gene ID | Original Annotation | Corrected Annotation | Severity | Evidence |
|---|-----------|---------------------|----------------------|----------|----------|
| 1 | Bo8g068060.1 | MEF2-like TF | **MADS-box transcription factor (MIKC-type)** | CRITICAL | Plants do NOT have canonical MEF2 TFs. The MADS domain shares structural homology with animal MEF2 but diverged extensively. B. oleracea has 91 MADS-box TFs (Shu et al., BMC Plant Biol 2019). |
| 2 | Bo3g036650.1 | Chitinase | **Putative chitinase (possibly catalytically inactive)** | MINOR | AT2G43580 may lack essential catalytic residues for active chitinase function. |

### 2.2 Contamination Assessment

All 89 gene IDs conform to the standard *B. oleracea* nomenclature (Bo[Chr]g[ID].1) from the TO1000 genome assembly (Liu et al., Nature Communications 2014). Gene ID Bo01182s010.1 uses scaffold nomenclature, which is expected for unplaced contigs. No bacterial, fungal, or animal gene IDs were detected. The tRNA dimethyltransferase (Bo8g090760.1) is a conserved eukaryotic TRM1 homolog, not of bacterial origin.

### 2.3 Multi-sRNA Target Genes

Nine genes are targeted by multiple independent bacterial sRNAs, suggesting convergent selection pressure on these loci:

| Gene ID | Annotation | Significance |
|---------|-----------|-------------|
| Bo6g067490.1 | PDR9/ABCG37 transporter | Auxin precursor + defense compound export |
| Bo4g061330.1 | THIC thiamine biosynthesis | Essential vitamin B1 pathway; riboswitch-regulated |
| Bo9g135400.1 | CCCH zinc finger protein | mRNA metabolism regulator; could amplify silencing |
| Bo4g076880.1 | PPR superfamily protein | Organellar RNA processing |
| Bo1g079000.1 | TFIIIC subunit 5 | RNA Pol III transcription (tRNA, 5S rRNA) |
| Bo2g047480.1 | DNA primase/PrimPol | DNA replication machinery |
| Bo7g089050.1 | C2/CaLB/MCTP protein | Ca2+-dependent membrane dynamics |
| Bo9g169690.1 | Uncharacterized | Unknown |
| Bo8g050640.1 | Uncharacterized | Unknown |

### 2.4 Whole-Genome Triplication Considerations

Potential WGT-derived paralog pairs in the target list include:
- **Bo7g119590.1 (CRK26) and Bo7g107400.1 (CRK29):** Both cysteine-rich RLKs on Chr C7, corresponding to different Arabidopsis CRK cluster members on At Chr 4.
- **Bo6g039950.1 and Bo6g039960.1:** Adjacent uncharacterized genes on Chr C6, likely tandem duplicates.
- **Bo9g173960.1 (GDI) and Bo9g173970.1 (DnaJ):** Adjacent on Chr C9 but encode different protein families — co-targeted by chromosomal proximity rather than functional relatedness.

---

## 3. Functional Category Distribution

### 3.1 Overview

| Category | Count | % | Key Members |
|---------|-------|---|-------------|
| Unknown/Uncharacterized | 35 | 39.3% | — |
| Defense/Immunity | 7 | 7.9% | CRK26, CRK29, Chitinase, GH17, PME, RING/U-box E3, RDR |
| Signal Transduction/Kinases | 7 | 7.9% | CAK1AT, CDPK15, 3× protein kinases, PP2A-A, C2/CaLB |
| Transport | 7 | 7.9% | PDR9/ABCG37, COPT5, ABC protein 1, UMAMIT, GDI, 2× vesicle transport |
| Transcription/Gene Regulation | 5 | 5.6% | ARF, MADS-box TF, HD-ZIP IV, TFIIIC5, TRFL7 |
| Cell Wall Modification | 4 | 4.5% | BGAL10, Pectinesterase, Glycosyltransferase, GH17 glucanase |
| Epigenetics/RNA Regulation | 4 | 4.5% | MBD10, RDR, CCCH ZnF, tRNA dimethyltransferase |
| Cell Cycle/Division | 3 | 3.4% | FZR3/CCS52B, EXO84B, CAK1AT |
| DNA Replication/Repair | 3 | 3.4% | DNA primase, Timeless, Alkyl transferase |
| Metabolism | 4 | 4.5% | THIC, BCKDH E1-beta, CTP synthase, CYP703A2 |
| Protein Homeostasis | 3 | 3.4% | DnaJ, RING E3, SBI1 |
| Chloroplast/Organelle | 3 | 3.4% | PPR, WCRKC thioredoxin, DnaJ |
| Membrane/Vesicle Trafficking | 4 | 4.5% | DUF789, PATL1, EXO84B, ARM repeat |

### 3.2 Pathway Enrichment Analysis

**Defense/Immunity (overrepresented):** Seven defense-related targets among 89 genes (7.9%) exceeds the genome-wide expectation for defense genes in *B. oleracea*. The defense enrichment includes two CRKs that associate with the FLS2 immune receptor complex, an RDR that amplifies antiviral siRNAs, a chitinase-like PR protein, and a GH17 beta-1,3-glucanase (PR-2 family). This overrepresentation parallels findings in *Botrytis cinerea*, where fungal sRNAs preferentially target plant immunity genes (Weiberg et al., 2013) [Known].

**Epigenetic/RNA Regulation (notable):** MBD10 reads DNA methylation marks; RDR produces siRNAs for RNA-directed DNA methylation; CCCH zinc finger proteins regulate mRNA metabolism; tRNA dimethyltransferase modifies tRNA stability. Collectively, these targets could broadly disrupt gene regulatory networks.

**Transport (notable):** PDR9/ABCG37 exports auxin precursors and coumarins; COPT5 mobilizes copper for photosynthetic electron transport; UMAMIT mediates amino acid allocation. Targeting transporters could reshape nutrient partitioning during germination.

---

## 4. Ranked Target Table

### Tier 1: Highest Priority (Mechanistically Sound, Well-Supported)

| Rank | Gene ID | Annotation | At Ortholog | Mechanism | Priority |
|------|---------|-----------|------------|-----------|----------|
| 1 | Bo8g102500.1 | **RDR** (RNA-Dependent RNA Polymerase) | RDR2/RDR6 | Downregulation reduces siRNA production and RdDM-mediated gene silencing, derepressing germination-promoting genes | HIGH |
| 2 | Bo7g119590.1 + Bo7g107400.1 | **CRK26 + CRK29** | AT4G38830, AT4G21410 | Defense receptor suppression; CRK29 induced 18-fold by flg22; associates with FLS2; downregulation frees resources for growth | HIGH |
| 3 | Bo8g066360.1 | **MBD10** (Methyl-CpG-Binding Domain 10) | AT1G15340 | Reduced reading of DNA methylation marks derepresses germination genes; accelerates dry-seed-to-germination epigenetic transition | HIGH |
| 4 | Bo7g114200.1 | **ARF** (Auxin Response Factor, repressor-type) | One of 23 AtARFs | If repressor-type (ARF10/16/17), reduces ABI3-mediated dormancy maintenance; releases ABA suppression of germination | HIGH |
| 5 | Bo3g036650.1 | **Chitinase** (putative) | AT2G43580 | Defense protein synthesis reduction; energy/nitrogen conservation during resource-limited germination | HIGH |

### Tier 2: High Priority (Strong Mechanistic Basis)

| Rank | Gene ID | Annotation | At Ortholog | Mechanism | Priority |
|------|---------|-----------|------------|-----------|----------|
| 6 | Bo6g067490.1 | **ABCG37/PDR9** | AT3G53480 | Reduced defense compound export + energy savings from reduced ATP-dependent transport; multiply targeted by sRNAs | MED-HIGH |
| 7 | Bo9g151660.1 | **COPT5** (Copper Transporter 5) | AT5G20650 | Reduced Cu-mediated ROS; optimizes oxidative window; crosstalk with iron homeostasis | MED-HIGH |
| 8 | Bo5g063050.1 | **HD-ZIP TF** (Class I/IV) | AT1G30490 | If stress-responsive HD-ZIP I: reduced ABA sensitivity and stress gene activation; energy reallocation | MED-HIGH |

### Tier 3: Moderate Priority (Plausible, Limited Direct Evidence)

| Rank | Gene ID | Annotation | At Ortholog | Mechanism | Priority |
|------|---------|-----------|------------|-----------|----------|
| 9 | Bo1g025790.1 | **CDPK15** | AT4G21940 | Reduced Ca2+-mediated ABA/defense signaling; family members CPK4/11 are positive ABA regulators | MEDIUM |
| 10 | Bo7g098960.1 | **PME** (Pectin Methylesterase) | PME family | Complex tissue-specific effects on cell wall; dual stiffening/loosening function | MEDIUM |
| 11 | Bo9g181290.1 | **TrxL2.2** (WCRKC Thioredoxin) | AT5G04260 | Atypical oxidizing thioredoxin; downregulation dampens oxidative signaling cascades | MEDIUM |
| 12 | Bo3g009380.1 | **FZR3/CCS52B** | AT3G57860 | APC/C activator; downregulation could accelerate G1→S cell cycle transition in radicle meristem | MEDIUM |

### Tier 4: Lower Priority (Paradoxical or Uncertain)

| Rank | Gene ID | Annotation | At Ortholog | Mechanism | Priority |
|------|---------|-----------|------------|-----------|----------|
| 13 | Bo3g185500.1 | **SBI1** (Seed Imbibition 1) | AT1G55740 | RFO mobilization paradox — downregulation should impair galactose release; likely compensated by redundant α-galactosidases | LOW-MED |
| 14 | Bo3g103050.1 | **BGAL10** | AT5G63810 | Xyloglucan beta-galactosidase; growth-promoting function makes downregulation counterintuitive | LOW-MED |
| 15 | Bo9g126160.1 | **GH17 β-1,3-glucanase** | AT5G56590 | Endosperm weakening enzyme; downregulation should delay germination but may be compensated by other hydrolases | LOW-MED |

---

## 5. Mechanistic Theme Analysis

### 5.1 Theme 1: Defense Downshift — The Growth-Immunity Tradeoff

**Targets involved:** CRK26, CRK29, Chitinase, GH17 glucanase, ABCG37/PDR9, RDR, RING/U-box E3

The most compelling mechanistic explanation for esRNA-mediated germination improvement is the **transient suppression of constitutive defense gene expression** during the narrow germination window. Plants face a fundamental resource allocation conflict between growth and defense (Huot et al., Molecular Plant 2014; Karasov et al., Plant Cell 2017) [Known]. Young seedlings must strategically allocate finite seed reserves between: (i) immune surveillance (CRK-mediated PTI, chitinase/glucanase synthesis, ABC transporter-dependent antimicrobial export), and (ii) germination-essential processes (radicle cell expansion, endosperm weakening, reserve mobilization).

CRK26 possesses a unique four-DUF26 extracellular domain architecture, and CRK29 is strongly induced (~18-fold) by bacterial flagellin (flg22), associating with the FLS2 immune receptor complex (Chou et al., Plant Physiology 2017) [Known]. Their downregulation would reduce PTI signaling, including ROS bursts, MAPK activation, and callose deposition — all energy-intensive processes. Chitinase accumulation can reach 1–2% of total soluble protein during pathogen attack; its constitutive expression diverts amino acids from growth-critical proteins [Known]. PDR9/ABCG37 consumes ATP for every transport cycle; reduced transporter activity frees energy for biosynthesis.

The defense downshift is particularly advantageous in the bacterial EPS environment, which presumably lacks fungal and oomycete pathogens. The transient nature of sRNA-mediated silencing means defense capacity would be restored post-germination as sRNA effects wane [Inferred].

### 5.2 Theme 2: Epigenetic Derepression — Unlocking Germination Competence

**Targets involved:** MBD10, RDR, TRFL7, tRNA dimethyltransferase, CCCH zinc finger

Germination involves massive epigenetic reprogramming. During seed development, extensive CHH-context methylation accumulates at transposable elements via the RdDM pathway (RDR2→DCL3→AGO4→DRM2). Upon germination, this hypermethylation is passively diluted through DNA replication (Kawakatsu et al., Cell 2017; Lin et al., Genome Biology 2017) [Known].

MBD10 reads methylation marks and recruits chromatin-modifying complexes to enforce gene silencing [Known]. Its downregulation would reduce the "reading" of methylation marks, allowing germination-promoting genes to escape silencing more rapidly. MBD6 and MBD10 are required for nucleolar dominance in allotetraploid Arabidopsis hybrids (Groszmann et al., Plant Cell 2011) [Known].

RDR downregulation directly reduces siRNA production — the raw material for RdDM. Whether RDR2 (24-nt siRNAs for RdDM) or RDR6 (21-nt siRNAs for PTGS), reduced RDR activity creates a more permissive chromatin state. RDR6-dependent methylation mediates maternal environmental control of seed dormancy by silencing the ALLANTOINASE gene via ATHPOGON1 transposon methylation (Iwasaki et al., eLife 2019) [Known]. In Brassica specifically, maternal RdDM components are required for seed development (Grover et al., Plant Journal 2018) [Known], highlighting the pathway's importance in Brassicaceae reproductive biology.

TRFL7 recruits PRC2 (Polycomb Repressive Complex 2) for H3K27me3 deposition at telobox-containing promoters [Known]. Its downregulation could derepress PRC2-silenced germination genes.

The synergy between MBD10 and RDR downregulation creates a two-pronged epigenetic derepression: reduced siRNA-directed methylation establishment (RDR) plus reduced methylation-mediated silencing enforcement (MBD10) [Inferred].

### 5.3 Theme 3: Hormone Rebalancing — Shifting from ABA Dominance to GA/Auxin Promotion

**Targets involved:** ARF (repressor-type), HD-ZIP TF, CDPK15, PP2A-A subunit, SBI1

The ABA/GA balance is the master switch for Brassicaceae germination. ARF10/ARF16/ARF17 promote dormancy by activating ABI3 transcription — a key amplifier of ABA signaling (Liu et al., PNAS 2013) [Known]. If Bo7g114200.1 encodes a repressor-type ARF, its downregulation would release ABI3-mediated ABA amplification, shifting the hormonal balance toward germination [Inferred]. Critically, miR160-mediated repression of ARF10 is essential for normal seed germination in Arabidopsis (Liu et al., Plant Journal 2007) [Known], establishing precedent for ARF silencing as a germination-promoting mechanism.

HD-ZIP class I transcription factors (ATHB5, ATHB6, ATHB7, ATHB12) modulate ABA sensitivity (Valdés et al., Plant Molecular Biology 2012) [Known]. If Bo5g063050.1 encodes a stress-responsive HD-ZIP I member, downregulation would reduce ABA-mediated growth inhibition. Alternatively, if HD-ZIP IV (ATML1-related), effects on germination would be minimal as these primarily regulate post-germinative epidermal differentiation.

CDPK15 (CPK15) is a calcium-dependent protein kinase. Family members CPK4 and CPK11 are positive ABA signaling regulators — their loss-of-function mutants show ABA-insensitive germination (Zhu et al., Plant Cell 2007) [Known]. CDPK15 downregulation could similarly reduce ABA signal transduction. PP2A-A subunit (RCN1) regulates auxin transport, ethylene signaling, and ABA response; its modulation could shift hormone crosstalk toward growth-promoting configurations [Inferred].

### 5.4 Theme 4: ROS Optimization — Tuning the Oxidative Window

**Targets involved:** COPT5, TrxL2.2 (WCRKC thioredoxin), CRK26/29

Copper transporter COPT5 mobilizes Cu from vacuolar stores (Garcia-Molina et al., Scientific Reports 2019) [Known]. Cu is a cofactor for Cu/Zn-superoxide dismutase (ROS scavenging) and cytochrome c oxidase (mitochondrial respiration). Reduced Cu mobilization via COPT5 downregulation could lower Cu-dependent ROS production while allowing ROS to remain within the optimal "oxidative window" for germination signaling [Inferred].

TrxL2.2 is an atypical chloroplast thioredoxin that functions as an **oxidation factor** — it drains reducing power from target proteins via the 2-Cys peroxiredoxin pathway (Serrato et al., Molecular Plant 2013) [Known]. Its downregulation would alter redox signaling cascades, potentially dampening stress-responsive gene activation.

CRK-mediated NADPH oxidase activation produces defense-associated ROS bursts. Reduced CRK signaling prevents excessive oxidative stress during germination [Inferred].

### 5.5 Theme 5: Cell Cycle Acceleration — Faster Radicle Cell Division

**Targets involved:** FZR3/CCS52B, CAK1AT, EXO84B

FZR3/CCS52B activates the APC/C (anaphase-promoting complex/cyclosome), an E3 ubiquitin ligase that degrades mitotic cyclins and enforces cell cycle checkpoints (Heyman and De Veylder, Molecular Plant 2012) [Known]. APC/C^FZR maintains G1 arrest by keeping cyclin levels low. Downregulation of FZR3 could allow cyclin accumulation and faster G1→S transition in radicle meristem cells, accelerating post-germinative cell division [Inferred]. Additionally, if FZR3 promotes endoreduplication in endosperm cells, its downregulation could reduce endosperm mechanical resistance to radicle emergence.

CAK1AT (CDK-Activating Kinase) phosphorylates CDKDs and RNA Pol II CTD, regulating both cell cycle progression and basal transcription [Known]. EXO84B is an exocyst complex component essential for secretory vesicle tethering and cell plate maturation during cytokinesis (Fendrych et al., Plant Cell 2010) [Known].

### 5.6 Theme 6: Cell Wall Remodeling — Complex and Context-Dependent

**Targets involved:** PME (pectinesterase), BGAL10, GH17 beta-1,3-glucanase, glycosyltransferase

PME activity exhibits a paradox: it can either stiffen cell walls (Ca2+ cross-linking of demethylesterified pectin) or loosen them (generating substrates for polygalacturonases) depending on the de-methylation pattern (Scheler et al., Plant Physiology 2015) [Known]. PME31 downregulation increases ABA-mediated germination inhibition, while overexpression attenuates it [Known], suggesting that the specific PME isoform and tissue context determine germination effects.

BGAL10 is the main xyloglucan beta-galactosidase in Arabidopsis; its downregulation should impair cell wall extension — paradoxical for germination improvement [Known]. GH17 beta-1,3-glucanase is a GA-induced endosperm weakening enzyme (Leubner-Metzger, Seed Science Research 2003) [Known]; its downregulation should delay germination. These paradoxical targets likely reflect functional compensation by redundant paralogs from WGT.

---

## 6. Causal Models

### 6.1 Model A: Coordinated esRNA-Mediated Defense-Dormancy Knockdown

**Hypothesis:** Bacterial esRNAs function as cross-kingdom regulatory signals that simultaneously suppress multiple plant defense and dormancy pathways, shifting the metabolic balance from immunity/quiescence toward growth/germination.

**Mechanism:**
1. Bacterial esRNAs are delivered to seed tissues during EPS imbibition, possibly via EPS-mediated protection from extracellular RNases
2. esRNAs are loaded into plant AGO1/AGO4 complexes
3. Defense receptors (CRK26/29) and effectors (chitinase, glucanase, ABCG37) are simultaneously silenced → energy reallocation from defense to growth
4. Epigenetic regulators (MBD10, RDR) are silenced → derepression of germination-promoting gene programs
5. Dormancy maintainers (ARF repressor, HD-ZIP) are silenced → release of ABA-mediated dormancy
6. Net effect: coordinated shift from defense/dormancy to growth/germination

**Predictions:**
- esRNA-specific: removal of RNA from EPS (RNase treatment) should abolish germination improvement
- Target-specific: individual gene knockdowns should partially recapitulate the phenotype
- AGO-dependent: *ago1* or *ago4* mutants should be resistant to esRNA effects
- Dose-dependent: esRNA concentration should correlate with germination improvement

### 6.2 Model B: EPS-Mediated Osmopriming with RNA as Bystander

**Hypothesis:** The EPS matrix provides optimal osmopriming conditions (controlled water potential, nutrient release, protective microenvironment) that improve germination, while esRNAs are transcriptionally active but functionally irrelevant to the germination phenotype.

**Mechanism:**
1. EPS polysaccharides create a hydrogel matrix around the seed
2. Controlled water release enables optimal imbibition kinetics
3. EPS-derived sugars and nutrients enhance metabolic activation
4. esRNAs are present but do not contribute to germination improvement
5. Gene expression changes observed are secondary consequences of improved hydration/nutrition

**Predictions:**
- EPS without RNA (RNase-treated EPS) should still improve germination
- Purified RNA without EPS should have no effect
- Non-specific polysaccharide gels should produce similar improvement
- Gene expression changes should correlate with hydration status, not specific target knockdown

### 6.3 Model Discrimination

The critical experiment is **RNase treatment of EPS before seed application**: if Model A is correct, RNase treatment abolishes improvement; if Model B is correct, RNase has no effect. Additional discriminating approaches include: (i) synthetic sRNA mimics targeting specific genes (e.g., anti-CRK26 dsRNA), (ii) AGO-pathway mutant analysis in Arabidopsis (a tractable proxy for *B. oleracea*), and (iii) RT-qPCR validation of predicted target downregulation in treated seeds.

---

## 7. Confounders and Alternative Explanations

### 7.1 Osmopriming Confound

EPS is a complex polysaccharide matrix that could function as an osmopriming agent independent of RNA content. Controlled water potential during imbibition is a well-established method for improving germination uniformity (Weitbrecht et al., J. Exp. Bot. 2011) [Known]. **Control:** Compare RNA-intact EPS vs. RNase-treated EPS vs. methylcellulose gel (non-biological osmoprimer) vs. water.

### 7.2 Nutrient Supplementation

EPS may contain minerals, amino acids, or vitamins that enhance seed metabolism during imbibition. **Control:** Chemical analysis of EPS composition; compare with defined nutrient solutions matching EPS mineral/amino acid content.

### 7.3 Microbial Contamination

Live bacteria in the EPS preparation could produce IAA, cytokinins, or other phytohormones that directly stimulate germination. PGPR effects on broccoli growth are documented (Griesbach et al., Acta Physiol. Plant. 2024) [Known]. **Control:** Filter-sterilize EPS; compare sterile vs. non-sterile; plate EPS to quantify viable bacteria.

### 7.4 Off-Target RNA Effects

esRNA fragments may trigger innate immune responses (dsRNA-activated pathways) rather than specific gene silencing, creating a hormetic stress response that improves germination. **Control:** Compare sequence-specific esRNA with scrambled dsRNA of similar size distribution.

### 7.5 Brassicaceae-Specific WGT Buffering

The whole-genome triplication in *B. oleracea* means most genes have 2–3 paralogs. esRNA-mediated silencing of one paralog may have minimal phenotypic effect due to compensation by retained copies. This could explain the paradoxical targets (BGAL10, GH17 glucanase, SBI1) where downregulation should theoretically impair germination but doesn't. **Approach:** Identify which subgenome copy (LF, MF1, or MF2) is targeted and whether paralog expression is sufficient for compensation.

### 7.6 Temporal Window of sRNA Activity

The germination window is narrow (typically 24–72 hours in broccoli). esRNA effects may be limited to early imbibition phases before endogenous RNase activity degrades exogenous RNAs. The transient nature of silencing could explain why defense genes can be safely downregulated — defense capacity is restored before seedlings encounter pathogens [Inferred].

---

## 8. Validation Plan

### 8.1 Experiment 1: RNase Treatment Test (Discriminates Models A vs. B)

**Objective:** Determine whether RNA content of EPS is required for germination improvement.
**Design:** Four treatments × 4 replicates × 50 seeds each:
1. Intact EPS (positive control)
2. RNase A/T1-treated EPS (RNA depleted)
3. Heat-inactivated RNase + EPS (RNA intact, control for RNase protein effects)
4. Water (negative control)

**Readouts:** Germination rate (T50), final germination %, seedling fresh weight at 7 days, radicle length.
**Expected (Model A):** Treatment 2 significantly worse than Treatment 1.
**Expected (Model B):** Treatments 1 and 2 equivalent.

### 8.2 Experiment 2: RT-qPCR Validation of Target Downregulation

**Objective:** Confirm that predicted target genes are actually downregulated in EPS-treated seeds.
**Design:** Sample RNA from EPS-treated and water-treated seeds at 6h, 12h, 24h, 48h post-imbibition. RT-qPCR for top 10 targets:
- Defense: *BoCRK26*, *BoCRK29*, *BoChitinase*, *BoABCG37*
- Epigenetic: *BoMBD10*, *BoRDR*
- Hormone: *BoARF*, *BoCDPK15*
- Cell cycle: *BoFZR3*
- Housekeeping: *BoActin*, *BoUBQ*

**Expected (Model A):** 2–5-fold downregulation of targets in EPS-treated seeds, peaking at 12–24h.

### 8.3 Experiment 3: Synthetic dsRNA Spray Test

**Objective:** Test whether specific gene silencing recapitulates germination improvement.
**Design:** Apply synthetic dsRNA targeting top 3 candidates (CRK26/29, MBD10, RDR) individually and in combination during seed imbibition.
**Readouts:** Germination rate, seedling vigor, target gene expression.
**Expected:** Partial recapitulation with individual dsRNAs; greater effect with combinations.

### 8.4 Experiment 4: Arabidopsis Proxy Validation

**Objective:** Use Arabidopsis mutant lines to test whether loss-of-function in orthologous genes improves germination.
**Design:** Test germination of T-DNA insertion mutants for:
- *crk26* (SALK lines), *crk29*
- *mbd10* (SALK_019428)
- *rdr2*, *rdr6*
- *arf10*, *arf16*

**Readouts:** Germination rate under standard and ABA-supplemented conditions.
**Expected:** Mutants in defense/dormancy genes show improved germination; epigenetic mutants show faster dormancy release.

### 8.5 Experiment 5: Hormone Profiling

**Objective:** Test whether EPS treatment alters ABA/GA/auxin balance.
**Design:** LC-MS/MS quantification of ABA, GA4, GA1, IAA, JA, SA in EPS-treated and control seeds at 0h, 6h, 12h, 24h, 48h.
**Expected (Model A):** Lower ABA, higher GA, lower SA/JA in EPS-treated seeds.

### 8.6 Experiment 6: sRNA Sequencing of Treated Seeds

**Objective:** Detect bacterial esRNAs inside plant cells and map their association with AGO complexes.
**Design:** sRNA-seq of EPS-treated seeds at 12h and 24h. AGO1 immunoprecipitation followed by sRNA-seq (AGO-RIP-seq) if antibodies available.
**Expected (Model A):** Bacterial-origin sRNAs detected in plant sRNA libraries; enrichment in AGO complexes.

### 8.7 Experiment 7: VIGS Validation in *B. oleracea*

**Objective:** Validate top targets using the recently developed CaLCuV-based VIGS system for *Brassica oleracea* (Lv et al., Planta 2020).
**Design:** VIGS constructs targeting *BoCRK26*, *BoMBD10*, *BoRDR*. Assess germination and seedling establishment.
**Expected:** VIGS-mediated silencing of defense/epigenetic targets improves seedling vigor.

---

## 9. Brassicaceae-Specific Considerations

### 9.1 Proximity to Arabidopsis

*B. oleracea* and *A. thaliana* are both Brassicaceae, diverging approximately 15–20 Mya. This close relationship enables exceptionally strong functional inference: ~71% average CDS conservation means most Arabidopsis gene functional data can be directly transferred to *B. oleracea* orthologs. The extensive TAIR, SALK T-DNA, and published Arabidopsis mutant resources provide an immediate proxy system for validating *B. oleracea* esRNA targets.

### 9.2 The Two-Step Germination Advantage

The Brassicaceae two-step germination (testa rupture → endosperm weakening → endosperm rupture) creates distinct temporal windows for intervention. esRNA effects on defense genes (CRK, chitinase) would primarily benefit the overall resource budget, while effects on cell wall genes (PME, BGAL10) and cell cycle genes (FZR3) could specifically modulate the endosperm weakening step or radicle cell division.

### 9.3 Glucosinolate-Defense Nexus

*B. oleracea* is rich in glucosinolates — defense metabolites unique to Brassicaceae. ABCG37/PDR9 exports oxygenated coumarins but may also participate in glucosinolate-derived metabolite transport. Downregulation of defense export pathways could specifically benefit broccoli by redirecting glucosinolate pathway precursors toward primary metabolism. Notably, PGPR enhance broccoli sulforaphane content (Griesbach et al., 2024) [Known], suggesting complex interactions between defense metabolism and microbial signals.

### 9.4 WGT-Mediated Functional Buffering

The whole-genome triplication provides a unique safety net for esRNA-mediated gene silencing. If bacterial esRNAs target only one of 2–3 WGT-derived paralogs, the retained copies maintain essential function while allowing partial knockdown of defense/dormancy pathways. This "buffered knockdown" could explain why broad targeting of multiple gene categories does not cause developmental defects — the WGT ensures functional compensation [Inferred].

---

## 10. Integration and Conclusions

### 10.1 Overarching Model

The *B. oleracea* esRNA target profile reveals a coherent biological narrative: bacterial extracellular small RNAs coordinately downregulate multiple nodes in the plant defense-dormancy-growth regulatory network, creating a transient physiological state optimized for germination and seedling establishment. Six mechanistic themes converge on a common outcome:

1. **Defense Downshift** (CRK26/29, Chitinase, GH17, ABCG37, RING/U-box E3): Reduces energy expenditure on immune surveillance in a pathogen-free EPS environment
2. **Epigenetic Derepression** (MBD10, RDR, TRFL7): Unlocks germination-promoting gene programs by disrupting methylation-mediated silencing
3. **Hormone Rebalancing** (ARF, HD-ZIP, CDPK15, PP2A-A): Shifts the ABA→GA balance toward germination by suppressing dormancy maintainers
4. **ROS Optimization** (COPT5, TrxL2.2): Fine-tunes the oxidative window for optimal germination signaling
5. **Cell Cycle Acceleration** (FZR3, CAK1AT, EXO84B): Expedites post-germinative cell division
6. **Cell Wall Remodeling** (PME, BGAL10, GH17): Context-dependent modulation of endosperm mechanical properties

The cumulative energy savings from reduced defense protein synthesis (CRKs, chitinase, glucanase), reduced ABC transporter activity (ABCG37), reduced siRNA biogenesis (RDR), and reduced epigenetic maintenance (MBD10) — redirected toward reserve mobilization, cell wall expansion, and metabolic activation — could quantitatively explain the observed germination improvement.

### 10.2 Comparison with Other Crop Species

The broccoli esRNA target profile shares key features with tomato/spinach, soybean, maize, and wheat analyses but exhibits distinctive characteristics:
- **Defense downshift** is present but less dominant than in wheat (24% of targets), consistent with the Brassicaceae's reliance on glucosinolate-based chemical defense rather than immune receptor-mediated resistance
- **Epigenetic derepression** is more prominent than in monocot crops, reflecting the documented importance of RdDM in Brassicaceae seed development (Grover et al., 2018)
- **The high proportion of uncharacterized targets (39.3%)** is notably greater than in maize or wheat, likely reflecting the smaller research community focused on *B. oleracea* genomics compared to major cereals
- **WGT-mediated buffering** is a unique feature not shared with diploid crops, providing both challenges (paralog specificity) and opportunities (safe partial knockdown)

### 10.3 Limitations and Caveats

1. **39.3% of targets remain uncharacterized** — these could include additional high-impact regulators
2. **Arabidopsis functional inference** assumes conserved function, which may not hold for all WGT paralogs
3. **Specific ARF identity** (activator vs. repressor) remains unconfirmed and is critical for interpretation
4. **Paradoxical targets** (BGAL10, GH17, SBI1) require experimental validation of compensatory mechanisms
5. **The B. oleracea TO1000 genome (v1.0)** has known assembly gaps; some gene models may be incomplete
6. **sRNA uptake mechanism** into seed cells remains uncharacterized in any system

---

## Bibliography

1. Bailly C, El-Maarouf-Bouteau H, Corbineau F (2008) From intracellular signaling networks to cell death: the dual role of reactive oxygen species in seed physiology. *C. R. Biologies* 331: 806–814.

2. Buck AH, Coakley G, Simbari F, McSorley HJ, et al. (2014) Exosomes secreted by nematode parasites transfer small RNAs to mammalian cells and modulate innate immunity. *Nature Communications* 5: 5488.

3. Cai Q, Qiao L, Wang M, He B, et al. (2018) Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. *Science* 360: 1126–1129.

4. Cao X, Jacobsen SE (2002) Role of the Arabidopsis DRM methyltransferases in de novo DNA methylation and gene silencing. *Current Biology* 12: 1138–1144.

5. Chen K, Du L, Chen Z (2003) Sensitization of defense responses and activation of programmed cell death by a pathogen-induced receptor-like protein kinase in Arabidopsis. *Plant Molecular Biology* 53: 61–74.

6. Chen K, Fan B, Du L, Chen Z (2004) Activation of hypersensitive cell death by pathogen-induced receptor-like protein kinases from Arabidopsis. *Plant Molecular Biology* 56: 271–283.

7. Acharya BR, Raina S, Maqbool SB, et al. (2007) Overexpression of CRK13, an Arabidopsis cysteine-rich receptor-like kinase, results in enhanced resistance to *Pseudomonas syringae*. *Plant Journal* 50: 488–499.

8. Couto D, Zipfel C (2016) Regulation of pattern recognition receptor signalling in plants. *Nature Reviews Immunology* 16: 537–552.

9. Deng Y, Zhai K, Xie Z, et al. (2017) Epigenetic regulation of antagonistic receptors confers rice blast resistance with yield balance. *Science* 355: 962–965.

10. Dunker F, Trutzenberg A, Rothenpieler JS, et al. (2020) Oomycete small RNAs bind to the plant RNA-induced silencing complex for virulence. *eLife* 9: e56096.

11. Fendrych M, Hala M, Zarsky V (2010) The Arabidopsis exocyst complex is involved in cytokinesis and cell plate maturation. *Plant Cell* 22: 3053–3065.

12. Griesbach E, Lattanzio G, Balmer A, et al. (2024) Plant growth-promoting rhizobacteria affect growth and sulforaphane content in broccoli seedlings. *Acta Physiologiae Plantarum* 46: 125.

13. Groszmann M, Gonzalez-Bayon R, Lyons RL, et al. (2011) Intrageneric incompatibilities as a tool to identify genes involved in nucleolar dominance. *Plant Cell* 23: 4221–4237.

14. Grover JW, Kendall T, Baten A, et al. (2018) Maternal components of RNA-directed DNA methylation are required for seed development in *Brassica rapa*. *Plant Journal* 94: 575–582.

15. He B, Cai Q, Qiao L, et al. (2021) RNA-binding proteins contribute to small RNA loading in plant extracellular vesicles. *Nature Plants* 7: 342–352.

16. Heyman J, De Veylder L (2012) The anaphase-promoting complex/cyclosome in control of plant development. *Molecular Plant* 5: 1182–1194.

17. Hou Y, Zhai Y, Feng L, et al. (2019) A *Phytophthora* effector suppresses trans-kingdom RNAi to promote disease susceptibility. *Cell Host & Microbe* 25: 153–165.

18. Huot B, Yao J, Montgomery BL, He SY (2014) Growth-defense tradeoffs in plants: a balancing act to optimize fitness. *Molecular Plant* 7: 1267–1287.

19. Iwasaki M, Hyvarinen L, Piskurewicz U, Lopez-Molina L (2019) Non-canonical RNA-directed DNA methylation participates in maternal and environmental control of seed dormancy. *eLife* 8: e37434.

20. Karasov TL, Chae E, Herman JJ, Bergelson J (2017) Mechanisms to mitigate the trade-off between growth and defense. *Plant Cell* 29: 666–680.

21. Kawakatsu T, Nery JR, Castanon R, Ecker JR (2017) Dynamic DNA methylation reconfiguration during seed development and germination. *Genome Biology* 18: 171.

22. Koch A, Biedenkopf D, Furch A, et al. (2016) An RNAi-based control of *Fusarium graminearum* infections through spraying of long dsRNAs. *PLOS Pathogens* 12: e1005901.

23. Leubner-Metzger G (2003) Functions and regulation of β-1,3-glucanases during seed germination, dormancy release and after-ripening. *Seed Science Research* 13: 17–34.

24. Linkies A, Müller K, Morris K, et al. (2009) Ethylene interacts with abscisic acid to regulate endosperm rupture during germination. *Plant Cell* 21: 3803–3822.

25. Liu PP, Montgomery TA, Fahlgren N, et al. (2007) Repression of AUXIN RESPONSE FACTOR10 by microRNA160 is critical for seed germination. *Plant Journal* 52: 133–146.

26. Liu S, Liu Y, Yang X, et al. (2014) The *Brassica oleracea* genome reveals the asymmetrical evolution of polyploid genomes. *Nature Communications* 5: 3930.

27. Lv H, Zheng J, Wang T, et al. (2020) An efficient virus-induced gene silencing (VIGS) system for functional genomics in Brassicas using a cabbage leaf curl virus (CaLCuV)-based vector. *Planta* 252: 45.

28. Marin E, Jouannet V, Herz A, et al. (2010) miR390, Arabidopsis TAS3 tasiRNAs, and their AUXIN RESPONSE FACTOR targets define an autoregulatory network. *Plant Cell* 22: 1104–1117.

29. Matzke MA, Mosher RA (2014) RNA-directed DNA methylation: an epigenetic pathway of increasing complexity. *Nature Reviews Genetics* 15: 394–408.

30. Müller K, Tintelnot S, Leubner-Metzger G (2006) Endosperm-limited Brassicaceae seed germination: abscisic acid inhibits embryo-induced endosperm weakening. *Plant and Cell Physiology* 47: 864–877.

31. Müller K, Linkies A, Vreeburg RA, et al. (2009) In vivo cell wall loosening by hydroxyl radicals during cress seed germination. *Plant Physiology* 150: 1855–1865.

32. Ning Y, Liu W, Wang GL (2017) Balancing immunity and yield in crop plants. *Trends in Plant Science* 22: 1069–1079.

33. Nowara D, Gay A, Lacomme C, et al. (2010) HIGS: host-induced gene silencing in the obligate biotrophic fungal pathogen *Blumeria graminis*. *Plant Cell* 22: 3130–3141.

34. Piskurewicz U, Jikumaru Y, Kinoshita N, et al. (2008) The gibberellic acid signaling repressor RGL2 inhibits Arabidopsis seed germination by stimulating abscisic acid synthesis and ABI5 activity. *Plant Cell* 20: 2729–2745.

35. Scheler C, Weitbrecht K, Pearce SP, et al. (2015) Promotion of testa rupture during garden cress germination involves seed compartment-specific expression and activity of pectin methylesterases. *Plant Physiology* 167: 200–215.

36. Serrato AJ, Fernandez-Trijueque J, Barajas-Lopez JD, et al. (2013) Plastid thioredoxins: a "one-for-all" redox-signaling system in plants. *Molecular Plant* 6: 266–268.

37. Shahid S, Kim G, Johnson NR, et al. (2018) MicroRNAs from the parasitic plant *Cuscuta campestris* target host messenger RNAs. *Nature* 553: 82–85.

38. Shu J, Liu Y, Li Z, et al. (2019) Genome wide analysis of MADS-box gene family in *Brassica oleracea* reveals conservation and variation in flower development. *BMC Plant Biology* 19: 106.

39. Tian D, Traw MB, Chen JQ, et al. (2003) Fitness costs of R-gene-mediated resistance in *Arabidopsis thaliana*. *Nature* 423: 74–77.

40. Vos IA, Moritz L, Pieterse CM, Van Wees SC (2015) Impact of hormonal crosstalk on plant resistance and fitness under multi-attacker conditions. *Frontiers in Plant Science* 6: 639.

41. Wang M, Weiberg A, Lin FM, et al. (2016) Bidirectional cross-kingdom RNAi and fungal uptake of external RNAs confer plant protection. *Nature Plants* 2: 16151.

42. Weiberg A, Wang M, Lin FM, et al. (2013) Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. *Science* 342: 118–123.

43. Weitbrecht K, Müller K, Leubner-Metzger G (2011) First off the mark: early seed germination. *Journal of Experimental Botany* 62: 3289–3309.

44. Zand Karimi H, Baldrich P, Rutter BD, et al. (2022) Arabidopsis apoplastic fluid contains sRNA- and circular RNA-protein complexes located outside extracellular vesicles. *Plant Cell* 34: 1863–1881.

45. Zhang T, Zhao YL, Zhao JH, et al. (2016) Cotton plants export microRNAs to inhibit virulence gene expression in a fungal pathogen. *Nature Plants* 2: 16153.

46. Zhu SY, Yu XC, Wang XJ, et al. (2007) Two calcium-dependent protein kinases, CPK4 and CPK11, regulate abscisic acid signal transduction in Arabidopsis. *Plant Cell* 19: 3019–3036.

47. Valdés AE, Overnas E, Johansson H, et al. (2012) The homeodomain-leucine zipper (HD-Zip) class I transcription factors ATHB7 and ATHB12 modulate abscisic acid signalling. *Plant Molecular Biology* 80: 425–442.

48. Gao M, He Y, Yin X, et al. (2021) Ca2+ sensor-mediated ROS scavenging suppresses rice immunity and is exploited by a fungal effector. *Cell* 184: 5391–5404.

49. Garcia-Molina A, Andrés-Colás N, Perea-García A, et al. (2019) The intracellular Arabidopsis COPT5 transport protein is required for photosynthetic electron transport under severe copper deficiency. *Scientific Reports* 9: 1–14.

50. Chou C, Ohkubo Y, Wu T, et al. (2017) Cysteine-rich receptor-like kinase CRK28 and CRK29 associate with the FLS2 receptor complex. *Plant Physiology* 173: 771–787.

51. Graeber K, Nakabayashi K, Miatton E, et al. (2012) Molecular mechanisms of seed dormancy. *Plant, Cell & Environment* 35: 1769–1786.

52. Erdmann RM, Picard CL (2020) RNA-directed DNA methylation. *PLOS Genetics* 16: e1009034.

53. Zemach A, Grafi G (2003) Characterization of Arabidopsis thaliana methyl-CpG-binding domain (MBD) proteins. *Plant Journal* 34: 565–572.

---

*End of Report*
