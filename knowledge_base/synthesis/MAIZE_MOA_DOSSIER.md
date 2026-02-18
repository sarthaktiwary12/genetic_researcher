# MAIZE (Zea mays) -- Comprehensive Mechanism of Action Dossier
# Bacterial-Derived Extracellular tRF RNA Drug: From Seed to Harvest

**Date:** 2026-02-18
**Classification:** Internal MoA Dossier -- Regulatory & Scientific Decision Support
**Evidence Labeling:** [KNOWN] = published peer-reviewed literature; [INFERRED] = logical deduction from conserved biology and target annotations; [SPECULATIVE] = hypothesis requiring experimental validation
**Target Organism:** Zea mays (B73 reference genome v5)
**Drug:** G-rich 16-22 nt tRNA-derived fragments (tRFs), glyco-protected, G-quadruplex structured
**Delivery:** M-9 bacterial EPS seed soak (4-8h)
**Uptake:** Nucleolin-mediated endocytosis, 25-30% endosomal escape
**Confirmed regulation:** RT-qPCR validated for 5 of 20 targets

---

# TASK A: STRICT MECHANISTIC MoA MODEL

## A.1 Drug Properties and Entry Mechanism

### A.1.1 tRF Drug Characteristics

[KNOWN] Transfer RNA-derived fragments (tRFs) are a class of small non-coding RNAs generated from precursor or mature tRNAs, typically 14-30 nt in length. G-rich tRFs can fold into G-quadruplex (G4) structures, four-stranded nucleic acid secondary structures stabilized by Hoogsteen hydrogen bonding of guanine quartets stacked upon one another and coordinated by monovalent cations (K+ > Na+). G4 structures confer exceptional nuclease resistance (half-life in serum: hours vs. minutes for linear ssRNA) and serve as high-affinity ligands for nucleolin (NCL), a multifunctional nucleolar phosphoprotein that shuttles between the cell surface, cytoplasm, and nucleus (Abdelmohsen et al., 2011, RNA).

[KNOWN] Glycosylation of RNA (glyco-protection) further enhances stability against RNase degradation. The combination of G4 structure + glyco-protection creates a doubly stabilized molecular entity with pharmacokinetic properties far superior to unmodified ssRNA.

### A.1.2 Uptake: Nucleolin-Mediated Endocytosis

```
EXTRACELLULAR SPACE (apoplast / seed coat surface)
    |
    G4-tRF binds cell-surface nucleolin (NCL)
    |
    NCL-tRF complex triggers clathrin-mediated endocytosis
    |  [KNOWN: He et al. 2023 demonstrated clathrin-mediated
    |   endocytosis for cross-kingdom sRNA uptake in plants]
    |
    Early endosome (pH ~6.5)
    |
    ├── 70-75% --> Late endosome/lysosome --> DEGRADATION
    |
    └── 25-30% --> ENDOSOMAL ESCAPE
                   |
                   ├── Cytoplasmic release
                   |   |
                   |   └── RISC loading (AGO1/AGO2)
                   |       --> Post-transcriptional gene silencing (PTGS)
                   |
                   └── Nuclear import (NCL shuttling)
                       |
                       └── AGO4 loading
                           --> RNA-directed DNA methylation (RdDM)
```

[INFERRED] Nucleolin is conserved in plants (including maize) and functions as an RNA-binding protein at the nucleolar level. Plant nucleolin homologs (NUC-L1 in Arabidopsis) are involved in rRNA processing and ribosome biogenesis. The cell-surface localization of NCL that enables receptor-mediated uptake has been documented primarily in mammalian systems; in plants, the analogous uptake may involve nucleolin-like proteins at the plasma membrane or, alternatively, apoplastic RNA-binding proteins that facilitate endocytosis through clathrin-coated pits.

[KNOWN] Maize encodes a comprehensive RNAi toolkit: multiple DCL paralogs, tissue-specific AGO expression (AGO1, AGO2, AGO4, and others), and RDR amplification components (Qian et al. 2011; Zhai et al. 2014). AGO1 is the primary effector for PTGS via mRNA cleavage. AGO4 mediates RdDM at complementary DNA loci. Both pathways are available for exogenous tRF-mediated silencing.

### A.1.3 tRF --> RISC Loading Kinetics

[INFERRED] Based on cross-kingdom RNAi kinetics (Weiberg et al. 2013; Cai et al. 2018):

```
0h:    Seed imbibition begins; tRFs in EPS matrix contact seed surface
0-2h:  Imbibition Phase I -- rapid water uptake carries tRFs through seed coat
2-4h:  NCL-mediated endocytosis in embryo cells; endosomal processing begins
4-6h:  25-30% endosomal escape; cytoplasmic tRFs encounter AGO1/AGO2
6-8h:  RISC loading complete for early-uptake tRFs; initial target cleavage begins
       Seed removed from soak solution
8-12h: Maximal RISC-loaded tRF concentration; target silencing underway
       RDR-mediated amplification may extend silencing signal
12-24h: tRF levels decline as exogenous supply ceases; silencing persists
        via RISC-bound fraction and RDR-amplified secondary siRNAs
24-72h: Residual silencing; transitional effects persist through mRNA turnover
72h+:  Silencing wanes; developmental programs take over
```

---

## A.2 Strict Phase-by-Phase MoA

### PHASE 1 (0-8h): Drug Uptake and Initial Target Engagement

**Molecular events in temporal order:**

**Step 1.1: tRF delivery and seed penetration (0-4h)**

```
G4-tRFs in EPS glyco-matrix
    |
    Seed imbibition Phase I (rapid water uptake)
    |
    tRFs traverse: seed coat --> pericarp --> aleurone --> scutellum --> embryo axis
    |
    [KNOWN: Maize seed coat becomes permeable within minutes of imbibition;
     water uptake follows triphasic kinetics (Bewley 1997)]
    |
    tRFs reach embryo axis cells within 2-4h of imbibition
```

**Step 1.2: Cellular uptake and RISC loading (4-8h)**

```
Cell surface:
    G4-tRF + NCL --> clathrin-coated pit --> early endosome

Endosome:
    75% degraded in late endosome/lysosome
    25% escape to cytoplasm

Cytoplasm:
    tRF + AGO1 --> RISC assembly
    |
    Guide strand selection (thermodynamic asymmetry rule)
    |
    Active RISC (tRF-AGO1) scans cytoplasmic mRNAs

    Parallel pathway:
    tRF + NCL --> nuclear import
    tRF + AGO4 --> RdDM complex
```

**Step 1.3: First-wave target silencing initiation (6-8h)**

The earliest targets to show measurable downregulation are those with:
(a) high basal transcript abundance in the imbibing embryo
(b) short mRNA half-lives (rapid turnover amplifies silencing effect)
(c) high complementarity to the most abundant tRF species

[INFERRED] Based on seed expression data and ABA signaling dynamics, the likely first-wave targets are:

```
FIRST WAVE (6-8h):
    ABI40 (Zm00001eb197370) --> VP1-like TF, highly expressed in dry seed embryo
    NPF15 (Zm00001eb385450) --> ABA transporter, active during imbibition
    HEX6 (Zm00001eb154520)  --> Hexokinase, constitutively expressed
```

---

### PHASE 2 (8-24h): Germination Reprogramming

This is the critical decision window where the ABA/GA balance shifts toward germination. The drug's primary mechanistic effects are concentrated here.

**Step 2.1: ABA Signaling Network Collapse (8-16h)**

Three simultaneous hits on the ABA pathway create a coordinated reduction in ABA sensitivity:

```
NODE 1: TRANSCRIPTIONAL OUTPUT
    ABI40 (VP1-like B3 TF) mRNA --> tRF-AGO1 cleavage --> ABI40 protein ↓↓
    |
    [KNOWN: VP1 activates LEA, Em, dehydrin genes; represses alpha-amylase
     VP1 null = vivipary (precocious germination on ear)
     Suzuki et al. 2003, Plant Physiol 132:1664]
    |
    Consequences of ABI40↓:
    ├── ABA-responsive element (ABRE)-driven genes ↓
    │   ├── LEA proteins ↓ (maturation program off)
    │   ├── Em1/Em2 ↓ (late embryogenesis program off)
    │   └── Dehydrins ↓
    ├── Alpha-amylase gene DEREPRESSED ↑
    │   [KNOWN: VP1 represses alpha-amylase in maize aleurone;
    │    Hoecker et al. 1995, Genes Dev 9:2459]
    └── GA3ox (GA biosynthetic enzyme) DEREPRESSED ↑
        [KNOWN: ABI4/ABI5 bind GA 2-oxidase promoters in sorghum,
         linking ABA to GA catabolism; Cantoro et al. 2013]
        Reduced ABI40 --> reduced GA catabolism --> GA accumulates

NODE 2: HORMONE TRANSPORT
    NPF15 (PTR2/NPF4.6 ABA importer) mRNA --> tRF-AGO1 cleavage --> NPF15 protein ↓↓
    |
    [KNOWN: NPF4.6/AIT1 is an ABA importer in Arabidopsis;
     ait1 mutants show reduced ABA sensitivity during germination
     Kanno et al. 2012, PNAS 109:9653]
    |
    Consequences of NPF15↓:
    ├── Reduced ABA import: endosperm --> embryo axis
    │   [KNOWN: ABA moves from maternal tissues to embryo
    │    during maturation; reduced import = lower embryo ABA]
    ├── Local ABA concentration in embryo axis ↓
    └── ABA-to-GA ratio shifts toward germination

NODE 3: GLUCOSE-ABA FEEDBACK LOOP BREAK
    HEX6 (hexokinase-2-like) mRNA --> tRF-AGO1 cleavage --> HEX6 protein ↓↓
    |
    [KNOWN: HXK1 is a glucose sensor; glucose triggers ABA biosynthesis
     via NCED upregulation; gin2 mutants insensitive to glucose-mediated
     germination delay. Jang et al. 1997; Moore et al. 2003; Price et al. 2003]
    |
    Consequences of HEX6↓:
    ├── Glucose sensing capacity ↓
    │   (but not glucose phosphorylation -- family redundancy from
    │    ZmHXK4, ZmHXK7, ZmHXK8, ZmHXK9; Zheng et al. 2019)
    ├── Glucose-triggered ABA biosynthesis ↓
    │   (starch mobilization proceeds without ABA counter-response)
    └── gin2-like metabolic state:
        "Full throttle" starch mobilization without hormone brake

SYNERGY NODE: Triple ABA suppression
    ABI40↓ + NPF15↓ + HEX6↓
    |
    = Transcription (ABI40) + Transport (NPF15) + Feedback (HEX6)
    |
    [INFERRED: Three orthogonal attack vectors on ABA pathway
     are more robust than single-gene intervention because
     compensatory mechanisms cannot restore signaling through
     alternative routes when all three nodes are suppressed]
    |
    Net effect: ABA sensitivity reduced by estimated 60-80%
    [SPECULATIVE: magnitude estimate based on VP1 heterozygote
     phenotypes showing intermediate dormancy]
```

**Step 2.2: Ancillary ABA Pathway Modulation (8-16h)**

```
IDP8263 (Zm00001eb408850) --> PH-GRAM domain protein ↓
    |
    [INFERRED: Reduces ABA perception at membranes;
     PH-GRAM domains bind phosphoinositides and may
     participate in ABA receptor complex membrane anchoring]
    |
    Contribution: reinforces ABA desensitization
    (lower confidence; annotation quality limited)

PRH130/PP2C32 (Zm00001eb018090) --> Protein phosphatase 2C ↓
    |
    [KNOWN: Group A PP2Cs are NEGATIVE regulators of ABA signaling;
     they dephosphorylate/inactivate SnRK2 kinases.
     PP2C↓ --> SnRK2 remains active --> INCREASED ABA response]
    |
    *** PARADOXICAL TARGET ***
    Expected effect: DELAY germination (increases ABA sensitivity)
    |
    Possible resolutions:
    ├── (a) False positive -- tRF does not actually silence PP2C32
    ├── (b) Non-canonical function -- PP2C32 may dephosphorylate
    │       growth-promoting substrates beyond SnRK2
    ├── (c) Dose effect -- partial PP2C32 reduction may fine-tune
    │       rather than eliminate ABA responsiveness, preventing
    │       overshoot of ABA insensitivity that would cause vivipary
    └── (d) Temporal resolution -- PP2C32 silencing may occur later,
            after germination commitment, serving to restore some
            ABA sensitivity during seedling establishment
    |
    [CRITICAL: This target must be validated by RT-qPCR.
     If NOT downregulated, it supports RNA specificity.
     If downregulated with no germination delay, resolution (b) or (c).]
```

**Step 2.3: Metabolic Reprogramming (12-24h)**

```
STARCH MOBILIZATION ACCELERATION:

    ABI40↓ --> alpha-amylase DEREPRESSED in scutellum and aleurone
    |
    [KNOWN: Alpha-amylase is the rate-limiting enzyme for starch
     degradation in cereal endosperm; four isozymes in maize
     Doehlert et al. 1991; Frias & Bernal-Lugo 1998]
    |
    Alpha-amylase ↑ + Beta-amylase + Pullulanase
    |
    Starch --> Maltose --> Glucose
    |
    Glucose enters glycolysis
    |
    BUT: HEX6↓ means glucose does NOT trigger ABA synthesis
    |
    Result: "Full throttle" reserve mobilization
    (starch broken down rapidly; glucose flows to glycolysis/TCA
     without triggering the normal ABA brake)

MYBR64 (Zm00001eb187270) --> MYB-related TF ↓
    |
    [KNOWN: ZmMYB59 overexpression negatively regulates germination
     by reducing GA and increasing ABA; Zhang et al. 2020, Front Plant Sci]
    |
    [INFERRED: If MYBR64 functions like ZmMYB59,
     its downregulation DEREPRESSES germination genes
     and shifts GA/ABA balance toward germination]
    |
    Consequences of MYBR64↓:
    ├── Germination gene cluster DEREPRESSED
    ├── GA biosynthesis ↑ (if MYB59-like function confirmed)
    └── Synergy with ABI40↓: removes two independent brakes
        on alpha-amylase expression

IBP1 (Zm00001eb397700) --> Initiator Binding Protein 1 ↓
    |
    [KNOWN: IBP1 binds the Shrunken-1 (Sh1) initiator element;
     Sh1 encodes sucrose synthase (SuSy); IBP1 overexpression
     reduces internode elongation and alters GA balance]
    |
    [INFERRED: IBP1↓ may alter Sh1/SuSy expression, modifying
     sucrose-to-hexose conversion during reserve mobilization.
     If IBP1 represses Sh1, its downregulation could enhance
     SuSy activity, improving sucrose cleavage for growth]
```

**Step 2.4: Energy Metabolism Summary at 24h**

```
Treated seed at 24h vs. control:

RESERVE MOBILIZATION:
    Alpha-amylase activity: ↑↑ (ABI40↓ + MYBR64↓ derepression)
    Sucrose synthase (SuSy): ↑ (IBP1↓ modulation)
    Glucose flux to glycolysis: ↑ (starch mobilization accelerated)
    Glucose-ABA feedback: BROKEN (HEX6↓)

HORMONE STATUS:
    ABA in embryo axis: ↓↓ (NPF15↓ reduced import + ABI40↓ reduced signaling)
    GA: ↑ (reduced GA catabolism via ABI40↓/MYBR64↓)
    GA/ABA ratio: ↑↑↑ (strongly shifted toward germination)

NET METABOLIC STATE:
    Energy: abundant (accelerated starch breakdown)
    Hormone: pro-germination (low ABA, high GA)
    Signal: "GERMINATE NOW"
```

---

### PHASE 3 (24-72h): Radicle Emergence and Seedling Establishment

**Step 3.1: Cell Wall Loosening at Radicle Tip (24-36h)**

```
PRX91 (Zm00001eb333290) --> Class III peroxidase ↓
    |
    [KNOWN: Class III peroxidases operate in two cycles:
     (a) Peroxidative cycle: H2O2 + phenolics --> cross-linked
         cell wall (lignin, suberin) = STIFFENING
     (b) Hydroxylic cycle: O2 + NADH --> O2•- + OH• = LOOSENING
     Passardi et al. 2004, Trends Plant Sci]
    |
    [KNOWN: Atprx16 knockout shows earlier testa and endosperm
     rupture -- peroxidase restricts germination timing
     Jemmat et al. 2020, Plant Sci 298:110565]
    |
    [KNOWN: In maize, peroxidase activity increases in the scutellar
     apoplast 24h after imbibition; Tnani et al. 2014]
    |
    Consequences of PRX91↓:
    ├── Peroxidative cycle activity ↓ at radicle tip
    │   --> Reduced phenolic cross-linking
    │   --> Cell wall remains extensible
    ├── Local H2O2 ↑ (less scavenging)
    │   --> Pro-germination signaling
    │   --> Oxidative window shifted toward signaling range
    └── Physical barrier to radicle protrusion REDUCED

si614021b09a/ZRP4-like (Zm00001eb292850) --> O-methyltransferase ↓
    |
    [KNOWN: ZRP4 is a caffeoyl-CoA 3-O-methyltransferase
     involved in suberin and lignin monolignol biosynthesis;
     NCBI LOC100272885]
    |
    [INFERRED: ZRP4↓ reduces suberin deposition and lignin
     biosynthesis at the radicle tip and coleorhiza,
     reducing mechanical resistance to protrusion]
    |
    Consequences of ZRP4↓:
    ├── Suberin deposition at radicle tip ↓
    ├── Lignification of surrounding tissues ↓
    └── Synergy with PRX91↓: dual reduction of cell wall
        fortification at the radicle emergence point

COMBINED CELL WALL EFFECT:
    PRX91↓ (reduced cross-linking) + ZRP4↓ (reduced lignin/suberin)
    |
    = SOFTER cell wall at radicle tip
    + ELEVATED H2O2 for signaling
    |
    --> Earlier radicle protrusion (estimated 6-12h faster)
    [SPECULATIVE: timing estimate based on Atprx16 data]
```

**Step 3.2: Chromatin Remodeling and Auxin Derepression (24-48h)**

```
AHL9 (Zm00001eb065740) --> AT-hook nuclear localized protein ↓
    |
    [KNOWN: AHL proteins bind AT-rich DNA via the AT-hook motif
     and remodel chromatin through scaffold/matrix attachment
     region (S/MAR) interactions; Zhao et al. 2013, PNAS]
    |
    [KNOWN: SOB3/AHL29 and ESC/AHL27 are GROWTH-SUPPRESSIVE
     in Arabidopsis: overexpression represses hypocotyl growth;
     Street et al. 2008, Plant J 54:1-14]
    |
    [KNOWN: AHL proteins bind YUCCA9 promoter S/MAR regions,
     recruit SWR1 chromatin remodeling complex to deposit H2A.Z,
     REPRESSING auxin biosynthesis; Favero et al. 2024, Nat Commun]
    |
    Consequences of AHL9↓:
    ├── AHL9 binding to growth gene S/MARs ↓
    │   --> SWR1/H2A.Z deposition at target loci ↓
    │   --> Chromatin becomes PERMISSIVE (open)
    ├── YUCCA (auxin biosynthesis) genes DEREPRESSED ↑
    │   --> Local IAA production ↑
    │   --> Cell elongation ↑ in:
    │       ├── Radicle (primary root elongation)
    │       ├── Mesocotyl (soil emergence)
    │       └── Coleoptile (shoot growth)
    └── Growth gene program broadly DEREPRESSED
        --> Seedling vigor ↑ (directly addresses observed phenotype)

MOS1-like/AI714716 (Zm00001eb136860) --> Chromatin/immunity regulator ↓
    |
    [KNOWN: MOS1 in Arabidopsis modulates SNC1 (TIR-NB-LRR)
     expression through chromatin remodeling; At homolog AT4G24680]
    |
    [INFERRED: MOS1↓ reduces constitutive immune gene expression
     at the chromatin level, freeing transcriptional and metabolic
     resources for growth. Synergizes with AHL9↓ in creating a
     broadly growth-permissive chromatin landscape]
```

**Step 3.3: Redox-Proteostasis Optimization (24-48h)**

```
OXIDATIVE WINDOW TUNING:

    PRX91↓ --> H2O2 accumulates in apoplast
    |
    [KNOWN: The "oxidative window" model:
     germination requires ROS within a critical signaling range
     El-Maarouf-Bouteau & Bailly 2008; Bailly 2004]
    |
    H2O2 in signaling range:
    ├── Activates Ca2+ channels --> signal transduction
    ├── Oxidizes protein thiols --> activates germination enzymes
    │   [KNOWN: 412 redox-switched cysteines identified during
    │    seed germination; Nietzel et al. 2020, PNAS]
    ├── Promotes cell wall loosening (Fenton reaction at low levels)
    └── Does NOT reach damage threshold (other PRX family members
        maintain scavenging capacity -- 119 class III PRX genes in maize)

PROTEIN TURNOVER MODULATION:

    RING63 (Zm00001eb044800) --> RING-HC E3 ubiquitin ligase ↓
    |
    [KNOWN: 590 RING proteins in maize (Li et al. 2025);
     RING E3 ligases control ABA signaling component turnover:
     KEG targets ABI5 for degradation (Stone et al. 2006)
     AIP2 targets ABI3 for degradation (Zhang et al. 2005)]
    |
    [INFERRED: RING63↓ effect depends on substrate specificity:
     If RING63 targets growth-promoting proteins for degradation:
       RING63↓ --> growth proteins STABILIZED --> pro-growth
     If RING63 targets ABI3/ABI5 for degradation (like KEG/AIP2):
       RING63↓ --> ABI3/5 STABILIZED --> pro-dormancy (COUNTERPRODUCTIVE)
     The germination-promoting phenotype suggests the former]

    RING265 (Zm00001eb194870) --> RING-IBR-RING E3 ligase ↓
    |
    [INFERRED: RBR family E3 ligases involved in protein quality
     control and selective autophagy. RING265↓ may alter the
     clearance rate of dormancy-associated storage proteins
     and ABA signaling components during the dormancy-to-
     germination transition]

    Combined RING63↓ + RING265↓:
    |
    [INFERRED: Altered ubiquitin-proteasome flux during germination.
     The net effect is a shift in the proteome toward growth-
     associated proteins. Specific substrates must be identified
     experimentally (Co-IP + mass spectrometry)]
```

**Step 3.4: Organellar and Metabolic Modulation (24-48h)**

```
ppr377 (Zm00001eb303410) --> PPR protein (mitochondrial) ↓
    |
    [KNOWN: PPR proteins are essential for organellar RNA processing
     (editing, splicing, stabilization). Mitochondrial reactivation
     during germination is rapid -- ATP accumulation within minutes
     Nietzel et al. 2020; Paszkiewicz et al. 2017]
    |
    *** POTENTIALLY COUNTERPRODUCTIVE ***
    [INFERRED: ppr377↓ could impair mitochondrial transcript processing,
     reducing electron transport chain efficiency. However:
     (a) PPR family is large (>450 members in maize) -- redundancy likely
     (b) Partial knockdown may fine-tune rather than abolish
         mitochondrial function
     (c) Slightly reduced respiration may paradoxically reduce
         ROS overproduction during the imbibition burst]

CYP10/CYP72A14 (Zm00001eb159250) --> Cytochrome P450 ↓
CYP72A15 (Zm00001eb358860) --> Cytochrome P450 (paralog) ↓
    |
    [KNOWN: CYP72A subfamily involved in diverse oxidative metabolism.
     263 CYP genes in maize. CYP72A enzymes in other species
     metabolize brassinolide (BL) and other hormones]
    |
    [INFERRED: CYP72A14/15↓ may reduce:
     (a) Brassinolide catabolism --> BL accumulates --> cell elongation ↑
         [SPECULATIVE: requires demonstration of BL substrate specificity]
     (b) Xenobiotic detoxification capacity (minor during germination)
     (c) Secondary metabolite production (terpenoid/phenylpropanoid)]
    |
    [SPECULATIVE: If CYP72A14/15 catabolize brassinolide:
     CYP72A14↓ + CYP72A15↓ --> BL accumulates
     BL --> BRI1/BAK1 signaling --> cell elongation ↑
     This would synergize with AHL9↓ --> auxin ↑
     for combined auxin + BL growth promotion]
```

---

### PHASE 4 (72h+): Sustained Growth Advantage

**Step 4.1: Growth-Defense Reallocation**

```
DEFENSE DOWNSHIFT (cumulative effect of multiple defense targets):

    CML21/PCO145926 (Zm00001eb388550) --> Calmodulin-like Ca2+ sensor ↓
    |
    [INFERRED: Reduced Ca2+-mediated defense signaling;
     CML proteins transduce pathogen-triggered Ca2+ spikes
     into defense responses. CML21↓ attenuates this transduction.]

    LRR-RLK (Zm00001eb403550) --> Leucine-rich repeat receptor kinase ↓
    |
    [INFERRED: Reduced surface defense receptor density;
     fewer MAMP/DAMP perception events translated into
     downstream defense signaling]

    PSKR1-like (Zm00001eb066630) --> Phytosulfokine receptor ↓
    |
    [KNOWN: Phytosulfokine (PSK) is a secreted peptide that promotes
     cell proliferation and modulates growth-defense balance.
     PSKR1 perception typically promotes growth]
    |
    *** NOTE: PSKR1↓ could REDUCE growth-promoting PSK signaling ***
    [INFERRED: This target may serve bacterial self-interest
     (immune suppression) rather than plant growth promotion.
     PSK signaling also enhances wound healing and defense
     against necrotrophic pathogens, so PSKR1↓ may reduce
     these defenses while having ambiguous effects on growth]

    GDT1-like/LOC100273360 (Zm00001eb036320) --> Golgi Ca2+/Mn2+ transporter ↓
    |
    [INFERRED: Altered Golgi Ca2+ homeostasis may modify
     protein glycosylation (Ca2+-dependent) and secretory
     pathway function. Indirect effects on cell wall
     secretion and defense protein processing]

RESOURCE REALLOCATION BUDGET:
    [SPECULATIVE: In a germinating maize seedling, constitutive
     defense may consume 5-15% of total metabolic flux (ATP, NADPH,
     amino acids, carbon skeletons). Suppressing defense targets
     (CML21, LRR-RLK, PSKR1, MOS1) redirects this fraction
     toward growth processes during the critical 72h-7d window]

    Defense investment ↓ (~5-15% metabolic savings)
    |
    Redirected to:
    ├── Cell division (meristematic zones of root and shoot)
    ├── Cell elongation (radicle, mesocotyl, coleoptile)
    ├── Photosynthetic machinery assembly (chloroplast biogenesis)
    └── Root hair development (nutrient acquisition)
```

**Step 4.2: Integrated Seedling Growth Advantage (72h-7d)**

```
CONVERGING GROWTH SIGNALS:

    Auxin ↑ (AHL9↓ --> YUCCA derepression)
    +
    GA ↑ (ABI40↓/MYBR64↓ --> reduced GA catabolism)
    +
    ABA ↓↓ (triple ABA suppression)
    +
    BL ↑ (CYP72A14/15↓ --> reduced BL catabolism) [SPECULATIVE]
    +
    Cell wall flexibility ↑ (PRX91↓ + ZRP4↓)
    +
    Energy ↑ (HEX6↓ -- glucose-ABA feedback broken)
    +
    Defense cost ↓ (defense targets downregulated)
    |
    = SEEDLING VIGOR PHENOTYPE
    |
    Manifestation:
    ├── Faster radicle emergence (estimated 6-12h earlier)
    ├── Greater radicle elongation rate (cell wall loosening + auxin)
    ├── Faster coleoptile emergence through soil surface
    ├── Greater mesocotyl elongation (soil emergence under deep planting)
    ├── Earlier transition to photoautotrophy
    └── Larger seedling biomass at V1-V3 stages
```

**Step 4.3: Transition from tRF-Mediated Effects to Endogenous Programs (7d+)**

```
tRF SIGNAL DECAY:
    Exogenous tRFs: degraded by 48-72h post-imbibition
    RISC-bound tRFs: active for ~72-120h (AGO protein half-life)
    RDR-amplified siRNAs: may persist 5-7 days (secondary amplification)
    |
    After ~7 days: no residual drug effect
    All subsequent growth advantage is INDIRECT:
    |
    ├── Larger root system (established during drug window)
    │   --> More water and nutrients captured
    │   --> Sustained growth advantage
    ├── Earlier canopy closure
    │   --> Better light interception
    │   --> Competitive advantage over weeds
    ├── Greater photosynthetic capacity (more leaf area)
    │   --> More carbon fixation
    │   --> More biomass partitioning to ears
    └── Epigenetic memory (if AGO4/RdDM pathway engaged)
        [SPECULATIVE: DNA methylation changes at target loci
         could persist through mitotic cell divisions,
         maintaining some gene regulation effects beyond
         tRF degradation. This would extend the drug's
         effective window.]
```

---

## A.3 Strict MoA Summary Diagram

```
TIME ──────────────────────────────────────────────────────────────────>

0h        4h        8h       16h       24h       48h       72h      7d+
|         |         |         |         |         |         |         |
PHASE 1   |         |         PHASE 2   |         PHASE 3   |  PHASE 4
UPTAKE    |         |       REPROGRAM   |         EMERGE    |  GROWTH
|         |         |         |         |         |         |         |
tRF in    NCL       RISC     ABI40↓    Alpha-    Radicle   Seedling  Vegetative
EPS       binding   loaded   NPF15↓    amylase↑  emerges   vigor     advantage
matrix    endo-     target   HEX6↓     Glucose↑  Cell      visible   persists
          cytosis   scan     ABA↓↓     GA↑       wall               via root
          begins    begins   |         |         loose              system
                             MYBR64↓   IBP1↓     PRX91↓
                             IDP8263↓             ZRP4↓
                                                  AHL9↓
                                                  RING63/265↓
                                                  |
                                                  Auxin↑
                                                  BL↑[SPEC]
                                                  Defense↓

KEY MOLECULAR OUTPUTS BY PHASE:

Phase 1: Drug delivery and RISC engagement
Phase 2: ABA↓, GA↑, glucose sensing↓, starch mobilization↑
Phase 3: Cell wall loosening, auxin↑, ROS optimization, radicle emergence
Phase 4: Defense-growth reallocation, sustained vigor, root development
```

---

## A.4 Paradoxical Targets and Honest Uncertainties

| Target | Expected Effect if Downregulated | Problem | Resolution Needed |
|--------|----------------------------------|---------|-------------------|
| PRH130/PP2C32 | INCREASED ABA sensitivity (delays germination) | Contradicts germination-promoting phenotype | RT-qPCR: is it actually silenced? If so, substrate specificity analysis needed |
| ppr377 | Impaired mitochondrial function | Could reduce energy availability during germination | PPR family redundancy may compensate; partial knockdown may be tolerable |
| PSKR1-like | Reduced growth-promoting PSK signaling | Could impair cell proliferation | May serve bacterial self-interest (immune suppression) at minor growth cost |
| RING63 | Depends on substrate: could stabilize ABA signaling | Ambiguous without substrate identification | Co-IP/mass spec to identify ubiquitination substrates |

---

# TASK B: ROOT SYSTEM ARCHITECTURE AND NUTRIENT CAPTURE

## B.1 Overview: Maize Root System Architecture

[KNOWN] The maize root system is composed of multiple root types that develop sequentially:
- **Primary root (radicle)**: Emerges first during germination (0-3 DAP); provides initial anchorage and water uptake
- **Seminal roots**: 3-7 roots emerging from the scutellar node within 1-3 days of germination; early-season explorers
- **Crown (nodal) roots**: Emerge from above-ground stem nodes starting at V2-V3; become the dominant root system by V6
- **Lateral roots**: Branch from all root types; primary surface for nutrient and water uptake
- **Root hairs**: Unicellular extensions from epidermal cells; massively increase absorptive surface area

The early seed treatment (0-8h soak) directly affects the radicle and seminal root developmental programs. Crown roots and later structures are affected indirectly through the seedling vigor advantage established during germination.

## B.2 Target-by-Target Root Architecture Connections

### B.2.1 Primary Root (Radicle) Elongation Rate

**Direct connections from the 20 targets:**

```
AHL9↓ --> YUCCA derepression --> local auxin ↑ in radicle tip
    |
    [KNOWN: Auxin is THE master hormone for root elongation.
     In roots, LOW auxin concentrations at the elongation zone
     promote cell elongation, while HIGH concentrations at
     the root tip maintain the meristem.
     AHL proteins in Arabidopsis repress YUCCA9 expression
     via chromatin remodeling (Favero et al. 2024)]
    |
    [INFERRED: AHL9↓ increases auxin biosynthesis.
     In the radicle elongation zone, increased local auxin
     production may be redistributed by PIN efflux carriers
     to maintain the correct auxin gradient:
     High at tip (meristem maintenance) -->
     Low at elongation zone (cell elongation) -->
     Very low at differentiation zone]
    |
    Net effect: Faster radicle elongation rate
    Estimated magnitude: +15-30% elongation rate
    [SPECULATIVE: based on SOB3/AHL29 mutant phenotypes
     in Arabidopsis showing enhanced hypocotyl growth]

PRX91↓ --> Reduced cell wall stiffening at radicle tip
    |
    [KNOWN: Atprx16 knockout = earlier radicle emergence
     (Jemmat et al. 2020)]
    |
    [INFERRED: PRX91↓ reduces phenolic cross-linking in
     the radicle cell wall, maintaining wall extensibility
     and allowing turgor-driven cell expansion.
     Combined with expansin activity, this accelerates
     radicle elongation]

ZRP4↓ --> Reduced suberin/lignin at radicle tip
    |
    [INFERRED: Suberin deposition at the root tip/endodermis
     is normally a protective barrier. Reduced suberin allows
     greater cell expansion and water uptake but may increase
     pathogen susceptibility. During the critical first 72h,
     the growth benefit likely outweighs the defense cost]

ABI40↓ --> ABA↓ --> Reduced ABA-mediated growth inhibition
    |
    [KNOWN: ABA inhibits primary root elongation at high
     concentrations (>1 uM). Reduced ABA sensitivity
     relieves this growth constraint.
     ABA also promotes root growth at very low concentrations
     (<0.1 uM), but the net effect of ABI40↓ is pro-elongation
     given the high ABA levels in newly imbibed seeds]
```

**Quantitative estimate:** [SPECULATIVE] Combined AHL9↓ + PRX91↓ + ZRP4↓ + ABI40↓ may accelerate primary root elongation by 20-40% during the first 72h.

### B.2.2 Lateral Root Initiation and Density

```
AHL9↓ --> Auxin ↑ --> Lateral root initiation ↑
    |
    [KNOWN: Lateral root initiation requires local auxin
     maxima in pericycle founder cells adjacent to xylem poles.
     Auxin activates the ARF7/ARF19 --> LBD16/LBD29 transcriptional
     cascade that specifies lateral root founder cell identity
     (Okushima et al. 2007, Plant Cell)]
    |
    [KNOWN: In Arabidopsis, AHL mutants (sob3-D, esc-D loss-of-
     function suppressors) show enhanced auxin-mediated responses
     including increased lateral root formation]
    |
    [INFERRED: AHL9↓ in maize would increase endogenous auxin
     production via YUCCA derepression, creating more frequent
     auxin maxima in the pericycle, thereby increasing the
     number of lateral root primordia initiated per unit
     root length = higher lateral root density]

ABI40↓ --> ABA↓ --> Lateral root emergence facilitated
    |
    [KNOWN: ABA inhibits lateral root emergence (the step
     after primordium initiation where the lateral root
     penetrates the endodermis, cortex, and epidermis).
     ABA-insensitive mutants show more emerged lateral roots.
     Signorelli & Considine 2018, J Exp Bot]
    |
    [INFERRED: ABI40↓ reduces ABA sensitivity, facilitating
     the emergence of lateral root primordia that have been
     initiated by the auxin-mediated pathway]

PRX91↓ --> Reduced cell wall barriers to lateral root emergence
    |
    [INFERRED: Lateral root emergence requires cell wall
     degradation in overlying cortical and epidermal cells.
     Reduced peroxidase-mediated cross-linking in these
     cell walls facilitates lateral root penetration]
```

**Net effect on lateral roots:** [INFERRED] Higher lateral root density (more initiations per unit primary root length) + faster emergence (reduced ABA + reduced cell wall barrier). Estimated +25-50% more lateral roots by V3 stage [SPECULATIVE].

### B.2.3 Seminal Root Development

```
ABI40↓ + HEX6↓ + NPF15↓ --> Accelerated hormonal transition at scutellar node
    |
    [KNOWN: Seminal roots emerge from the scutellar node within
     1-3 days of germination. Their initiation requires the
     same ABA/GA balance shift as radicle emergence]
    |
    [INFERRED: The triple ABA suppression (ABI40↓, HEX6↓, NPF15↓)
     accelerates hormonal conditions favorable for seminal root
     emergence, potentially yielding:
     (a) Earlier seminal root emergence (1-2 days earlier)
     (b) More seminal roots (3-7 per seedling; number partly
         genetically determined but hormones influence it)]

AHL9↓ --> Auxin ↑ in scutellar node --> seminal root primordia activation
    |
    [INFERRED: Auxin accumulation at the scutellar node
     promotes seminal root primordium activation and outgrowth]
```

### B.2.4 Crown Root Number and Spread

```
AHL9↓ --> Sustained auxin production in later-developing nodes
    |
    [KNOWN: Crown (nodal) roots emerge from stem nodes at V2+.
     Their initiation is auxin-dependent (RTCS/RTCL pathway
     in maize). RTCS (rootless concerning crown and seminal roots)
     encodes a LOB-domain TF activated by auxin]
    |
    [INFERRED: If AHL9↓ effects persist through epigenetic memory
     (RdDM at AHL9 locus) or if the initial auxin surge programs
     more crown root primordia, then crown root number may be
     enhanced at V2-V6. However, by V2-V6, the exogenous tRFs
     are likely degraded, so the effect would be INDIRECT:
     larger seedling with more stem nodes available for crown
     root formation]

    Indirect pathway:
    Early vigor ↑ --> more stem nodes developed earlier
    --> more crown root sites available at V3-V6
    --> potentially +1-3 additional crown roots per plant
    [SPECULATIVE]
```

### B.2.5 Root Hair Density and Length

```
PRX91↓ --> Cell wall flexibility ↑ in root epidermal cells
    |
    [INFERRED: Root hairs form by tip growth of trichoblast
     (root-hair-forming epidermal) cells. Cell wall extensibility
     at the root hair tip determines elongation rate.
     PRX91↓ reduces peroxidase-mediated cell wall stiffening,
     potentially allowing longer root hairs]

AHL9↓ --> Auxin ↑ --> Root hair initiation ↑
    |
    [KNOWN: Auxin promotes root hair initiation through
     the WER/GL2/CPC transcription factor network.
     Higher auxin levels increase the proportion of
     trichoblasts that actually form root hairs]

ABI40↓ --> ABA↓ --> Root hair elongation facilitated
    |
    [KNOWN: ABA promotes root hair growth at moderate
     concentrations (0.1-1 uM) but inhibits at high
     concentrations. Reduced ABA sensitivity in the
     context of moderate ABA levels could facilitate
     root hair elongation]
```

**Net effect:** [INFERRED] Modest increase in root hair density (+10-20%) and length (+15-25%) due to cell wall flexibility and auxin enhancement. Root hairs account for up to 77% of root surface area, so even modest improvements significantly increase absorptive capacity.

### B.2.6 Water Capture Efficiency

```
Root architecture improvement summary:
    Primary root: longer, faster-growing
    Lateral roots: more numerous, earlier emergence
    Seminal roots: earlier emergence, potentially more
    Crown roots: indirectly enhanced via seedling vigor
    Root hairs: longer, more numerous
    |
    Combined: LARGER ROOT SYSTEM EARLIER
    |
    [KNOWN: Water uptake = root surface area x soil-root contact
     x hydraulic conductivity x water potential gradient]
    |
    Larger root system --> more soil-root contact
    More lateral roots --> better exploration of soil volume
    Longer root hairs --> access water in finer pore spaces
    Reduced suberin (ZRP4↓) --> higher radial hydraulic conductivity
    |
    [INFERRED: Net improvement in water capture:
     +15-30% water uptake efficiency during V1-V6
     (critical seedling establishment period)]
    [SPECULATIVE: magnitude estimate]

    CAUTION: Reduced suberin (ZRP4↓) is a double-edged sword:
    Less suberin = more water uptake but also more vulnerability
    to soil-borne pathogens and potential water loss under drought.
    The benefit is greatest in well-watered conditions during
    seedling establishment.
```

### B.2.7 Nitrogen Uptake Efficiency (NUE)

```
NPF15↓ --> NRT1/PTR family transporter ↓
    |
    [KNOWN: NPF4.6/AIT1 primarily transports ABA, but NPF
     family members are also nitrate and peptide transporters.
     The NPF family in maize: 78 members (Wang et al. 2023)]
    |
    [INFERRED: NPF15↓ REDUCES nitrate/peptide transport capacity
     of this specific transporter. However:
     (a) 78 NPF family members provide massive redundancy
     (b) The primary function of NPF15 is likely ABA transport
         (based on NPF4.6 homology)
     (c) Other NRT1/NRT2 transporters compensate for nitrate uptake
     Therefore: net effect on nitrate uptake is likely NEUTRAL]

    ROOT ARCHITECTURE effects on N uptake:
    More lateral roots (AHL9↓-mediated) --> more surface area
    for nitrate absorption --> improved NUE
    |
    [KNOWN: Nitrogen uptake efficiency is strongly correlated
     with root length density in the top 30 cm of soil,
     where most nitrate is concentrated after fertilization]
    |
    [INFERRED: The root architecture improvements (more laterals,
     earlier crown roots) improve NUE by 10-20% through increased
     soil volume exploration, even without changes to individual
     transporter expression]
    [SPECULATIVE: magnitude]
```

### B.2.8 Phosphorus Acquisition

```
ROOT HAIR EFFECTS:
    Longer root hairs (PRX91↓, AHL9↓) --> dramatically improved P uptake
    |
    [KNOWN: Phosphorus is highly immobile in soil (diffusion
     coefficient ~10^-13 m2/s). Root hairs are the PRIMARY
     mechanism for P acquisition because they extend into
     soil pore spaces beyond the P depletion zone.
     Root hair length is the single strongest predictor
     of plant P uptake efficiency (Gahoonia et al. 1997)]
    |
    [INFERRED: Even a 15-25% increase in root hair length
     translates to a ~30-50% increase in the soil volume
     from which P can be extracted (cylindrical geometry:
     volume scales with radius squared)]

LATERAL ROOT DENSITY:
    More laterals (AHL9↓) --> more P acquisition zones
    |
    [KNOWN: Shallow lateral roots are most effective for P
     uptake because topsoil has highest P concentration.
     More lateral roots in the top 15 cm = more P capture]

CYP72A14/15↓ --> possible effect on organic acid exudation
    |
    [SPECULATIVE: Some CYP enzymes participate in organic
     acid metabolism. Organic acid exudation (citrate, malate)
     from roots solubilizes otherwise-unavailable P. If
     CYP72A14/15 catabolize organic acid precursors, their
     downregulation could enhance organic acid exudation.
     This is highly speculative and requires metabolomic
     validation]
```

### B.2.9 Stress Resilience at Seedling Stage

```
ABI40↓ --> Modulated ABA response under drought
    |
    [KNOWN: ABA is the master drought-response hormone.
     ABI40↓ reduces ABA sensitivity, which is BENEFICIAL
     during germination but potentially HARMFUL under
     post-germination drought stress]
    |
    [INFERRED: The tRF effect is TRANSIENT (wanes by ~72h).
     By the time seedlings encounter field drought stress
     (typically V3-V6), ABI40 expression has recovered to
     normal levels. Therefore:
     BENEFIT: Faster establishment under non-stress conditions
     RISK: If drought occurs during 0-72h window,
           reduced ABA sensitivity could impair the
           seedling's drought response
     MITIGATION: Larger root system (from vigor advantage)
           provides better water access even with temporarily
           reduced ABA response]

RING63↓/RING265↓ --> Altered protein turnover under stress
    |
    [INFERRED: E3 ligases play roles in ubiquitin-mediated
     stress protein turnover. Transient reduction during
     germination may delay the clearance of stress-damage
     proteins, but this effect is minor given family redundancy
     (590 RING genes in maize)]

DEFENSE TARGET REDUCTION (CML21↓, LRR-RLK↓, MOS1↓):
    |
    [INFERRED: Transient defense suppression during 0-72h
     creates a window of increased pathogen susceptibility.
     For seedling-stage soil-borne pathogens (Pythium,
     Fusarium, Rhizoctonia), this is a legitimate concern:
     faster germination reduces time in vulnerable soil
     contact, but reduced defense during that time could
     partially offset this advantage.
     NET ASSESSMENT: The speed advantage (faster emergence
     out of the pathogen-rich soil zone) likely outweighs
     the defense cost for most field conditions]
```

## B.3 Root Architecture to Harvest Yield Translation

### B.3.1 Water Use Efficiency (WUE)

```
EARLY ROOT ADVANTAGE --> SUSTAINED WUE:

    Seedling stage (V1-V6):
    ├── Larger root system established during tRF window
    ├── More lateral roots exploring soil volume
    ├── Better soil-root contact for water absorption
    └── Earlier crown root development
    |
    |   [KNOWN: The root system at V6 determines the plant's
    |    water capture capacity for the rest of the season.
    |    Root architecture established by V6 is largely fixed
    |    for the deep root profile]
    |
    Vegetative growth (V6-VT):
    ├── Deeper root penetration (established early advantage persists)
    ├── More crown roots accessing deeper soil horizons
    └── Greater total root length density in soil profile
    |
    Reproductive growth (VT-R6):
    ├── [KNOWN: The critical period for maize yield is
    │    2 weeks before to 2 weeks after silking (VT/R1).
    │    Water deficit during this window causes:
    │    - Poor pollination (ASI increase)
    │    - Kernel abortion
    │    - Yield losses of 3-8% per day of stress
    │    (Claassen & Shaw 1970; NeSmith & Ritchie 1992)]
    │
    ├── Better root system from early advantage:
    │   --> More water available during critical VT/R1 period
    │   --> Reduced ASI (anthesis-silking interval)
    │   --> Better pollination
    │   --> More kernels per ear
    │   --> Higher yield under moderate drought
    │
    └── [INFERRED: Plants with 20-30% larger root systems
         at V6 maintain 10-15% higher leaf water potential
         during the VT/R1 critical period under moderate
         drought. This translates to:
         - 1-2 day shorter ASI
         - 5-15% more kernels set per ear
         - 5-10% higher grain yield under drought
         [SPECULATIVE: magnitude estimates based on
          published root trait QTL effects on yield;
          e.g., Gao & Lynch 2016, J Exp Bot]]
```

### B.3.2 Nutrient Capture and Grain Filling

```
NITROGEN:
    Early root advantage --> more N captured during vegetative growth
    |
    [KNOWN: Maize requires ~1.2 kg N per 100 kg grain.
     60-70% of grain N comes from vegetative tissue
     remobilization; 30-40% from post-silking uptake]
    |
    More root surface area --> more N acquisition
    --> More vegetative N stored in leaves/stalks
    --> More N available for remobilization to grain
    --> Higher grain protein content AND/OR
        Higher total grain yield (N-limited conditions)

PHOSPHORUS:
    Longer root hairs + more laterals --> better P capture
    |
    [KNOWN: P deficiency limits maize yield on ~70% of
     tropical soils and ~30% of temperate soils.
     Root hair traits explain up to 80% of variation
     in P uptake among maize genotypes
     (Zhu et al. 2010, Plant Physiol)]
    |
    Better P capture --> improved energy metabolism (ATP)
    --> Better starch synthesis in kernels
    --> Higher 100-kernel weight

POTASSIUM, MICRONUTRIENTS:
    Larger root system --> improved K, Zn, Fe, Mn uptake
    [INFERRED: General improvement in mineral nutrition
     proportional to increased root surface area]
```

### B.3.3 Drought Resilience During Flowering

```
CRITICAL PERIOD ANALYSIS:

    VT/R1 (flowering) is the yield-determining period for maize.
    |
    Drug applied at seed soak (0h) --> effects on VT/R1 are INDIRECT:
    |
    ├── ROOT ARCHITECTURE LEGACY EFFECT:
    │   Roots established during V1-V6 determine water access at VT/R1
    │   Deeper roots (from early vigor) --> access subsoil water
    │   More crown roots --> greater total absorptive capacity
    │   = "INSURANCE POLICY" against flowering-stage drought
    │
    ├── BIOMASS ACCUMULATION ADVANTAGE:
    │   Larger plant at V6 --> more leaf area --> more photosynthesis
    │   --> More carbohydrate reserves in stalk at VT/R1
    │   --> Greater buffer against photosynthetic decline during stress
    │
    └── EARLIER PHENOLOGY:
        [INFERRED: Faster germination + early vigor may advance
         the entire phenological calendar by 1-3 days.
         In environments where terminal drought is the primary
         stress, advancing flowering by even 1-2 days can
         escape the worst drought severity]
        |
        This "escape" mechanism is particularly valuable in:
        - Short-season environments
        - Semi-arid regions with predictable late-season drought
        - Heat-stressed tropical environments

YIELD IMPACT MODEL:
    Under well-watered conditions:
        Yield advantage from early vigor: +3-8% [SPECULATIVE]
        (mainly through more kernels/ear and slightly higher kernel weight)

    Under moderate drought at flowering:
        Yield advantage from root system + biomass: +8-15% [SPECULATIVE]
        (mainly through better pollination, reduced kernel abortion)

    Under severe drought at flowering:
        Yield advantage: +5-20% [SPECULATIVE]
        (larger variation because root depth advantage is most
         valuable when subsoil water is available)
```

---

# TASK C: PRODUCTIVITY VALIDATION PLAN

## C1. Field Trial Design

### C1.1 Plot Configuration

```
Plot size:        4 rows x 5.3 m length = 10.1 m2 (minimum)
                  Preferred: 6 rows x 8 m = ~36 m2
Row spacing:      76 cm (standard US Corn Belt) or 75 cm (metric)
Within-row plant spacing: 17.5 cm (target ~76,000 plants/ha)
                         Adjust for local recommendations
Harvest area:     Center 2 rows x interior 4 m = 6.1 m2
                  (discard border rows and 0.5 m end-of-row)
Alley spacing:    1.0 m between plots (combine access)
Border rows:      Minimum 4 guard rows surrounding entire trial
```

### C1.2 Experimental Design

```
Design:           Alpha-lattice incomplete block design
                  (preferred over RCBD for >6 treatments or
                   variable field conditions)
                  OR: Randomized Complete Block Design (RCBD)
                  if only 3 treatments

Treatments (3):
    T1: M-9 tRF seed soak (4h, standard concentration)
    T2: Water soak control (4h, distilled water)
    T3: RNase-treated M-9 soak (4h, M-9 + RNase A 100 ug/mL)

Replications:     n = 6 blocks per location (minimum)
                  n = 8 blocks preferred for <10% CV on yield
Total plots:      3 treatments x 6 reps = 18 plots per location
                  3 treatments x 8 reps = 24 plots per location

Planting density: 76,000 plants/ha (standard high-yield management)
                  Record actual stand count for covariate adjustment
```

### C1.3 Multi-Environment Trials (METs)

```
Locations (minimum 4, preferred 6-8):

Location 1: US Corn Belt -- Iowa or Illinois
    Soil: Mollisol (deep, fertile, high OM)
    Climate: temperate, well-watered
    Purpose: high-yield potential environment
    Hybrid: commercial B73-related single cross

Location 2: US Corn Belt -- Western Nebraska or Kansas
    Soil: Aridisol/Mollisol (variable moisture)
    Climate: temperate, drought-prone
    Purpose: moderate drought stress environment
    Irrigation: rainfed only

Location 3: Southern US -- Texas or Georgia
    Soil: Ultisol/Alfisol
    Climate: subtropical, heat stress + humidity
    Purpose: heat/humidity stress environment
    Hybrid: southern-adapted commercial

Location 4: Tropical -- Mexico (Bajio) or Brazil (Parana)
    Soil: Variable (Oxisol/Alfisol)
    Climate: tropical
    Purpose: tropical adaptation
    Hybrid: tropical-adapted commercial

Location 5 (optional): Northern US -- Minnesota or Wisconsin
    Soil: Mollisol
    Climate: cold stress during planting
    Purpose: cold germination stress environment

Location 6 (optional): Sub-Saharan Africa -- Kenya or South Africa
    Soil: Variable (often low P, low N)
    Climate: semi-arid to sub-humid
    Purpose: smallholder relevance; nutrient-limited environment

Seasons: 2 consecutive years minimum (Year 1 = preliminary; Year 2 = confirmatory)
Total field plots: 3 treatments x 8 reps x 6 locations x 2 years = 288 plots
```

### C1.4 Seed Treatment Protocol

```
Seed source:      Certified seed, single commercial hybrid per location
                  (hybrid choice site-adapted; document genotype)
Seed lot:         Single seed lot per hybrid (eliminate lot variation)
Seed treatment:   Apply M-9 (T1), water (T2), or RNase-M-9 (T3)
                  by seed soaking in 50-mL Falcon tubes
                  Seeds:solution ratio = 1:3 (v/v)
                  Duration: 4 hours at 25C in dark
                  Drain and surface-dry on blotting paper (1 hour)
                  Plant within 2 hours of drying
Fungicide:        Apply standard commercial seed-treatment fungicide
                  (e.g., fludioxonil + mefenoxam) AFTER M-9 treatment
                  to all treatments equally
Insecticide:      Standard seed-treatment neonicotinoid if local practice
```

---

## C2. Phenotyping Schedule by Growth Stage

### C2.1 Emergence and Early Vegetative (VE-V3)

```
STAGE   DAP*   MEASUREMENT                           METHOD
VE      4-7    Days to 50% emergence                 Daily plot census
VE      5-8    Final stand count                     Count all plants in harvest rows
VE      5-8    Emergence speed index (ESI)           ESI = sum(Ni/Di) where Ni = newly
                                                      emerged on day Di
V1      7-10   Seedling vigor score (1-9 scale)      Visual: 1=poor, 9=excellent
                                                      Score uniformity + size
V2      10-14  Plant height (soil to tip of tallest  Ruler, n=10 plants/plot
               leaf, pulled vertical)
V3      14-21  Stem diameter (1st internode)          Digital caliper, n=10 plants/plot
V3      14-21  Leaf number (fully expanded + visible) Count, n=10 plants/plot
V3      14-21  Root excavation subsample              Shovelomics on n=3 plants/plot
               (primary root length, lateral root     (destructive sampling from
               count, seminal root count)             non-harvest rows only)

*DAP = days after planting; timing varies by temperature
```

### C2.2 Mid-Vegetative (V6-V12)

```
STAGE   DAP     MEASUREMENT                          METHOD
V6      28-35   Plant height (soil to collar of      Measuring stick, n=10/plot
                newest fully expanded leaf)
V6      28-35   SPAD chlorophyll index                Konica Minolta SPAD-502
                (ear leaf or newest fully expanded)   n=10 plants/plot, mean of 3
                                                      readings per leaf (tip, mid, base)
V8      35-42   Stem diameter (3rd internode)          Digital caliper, n=10/plot
V10     42-49   Plant height                          n=10/plot
V10     42-49   Leaf area index (LAI)                 AccuPAR LP-80 ceptometer
                                                      (or LI-COR LAI-2200)
                                                      4 above + 4 below canopy readings
V12     49-56   Plant height (final pre-tassel)       n=10/plot
V12     49-56   SPAD chlorophyll (ear leaf)            n=10/plot
V12     49-56   Drone-based NDVI (optional)            Multispectral camera (RedEdge-MX)
                                                       Plot-level NDVI extraction
```

### C2.3 Flowering (VT/R1)

```
STAGE   DAP     MEASUREMENT                          METHOD
VT      56-70   Anthesis date (50% pollen shed)       Daily census: date when 50% of
                                                      plants in plot are shedding pollen
R1      58-75   Silking date (50% silk emergence)     Daily census: date when 50% of
                                                      plants in plot show visible silks
VT/R1   56-75   ASI (anthesis-silking interval)       ASI = silking date - anthesis date
                                                      Smaller ASI = better synchrony
                                                      ASI > 3 days indicates stress
VT      56-70   Ear height                            Soil to ear node, n=10/plot
VT      56-70   Tassel branch number                  Count primary branches, n=10/plot
VT      56-70   Final plant height                    Soil to tassel tip, n=10/plot
R1      60-75   Ear shoot number                      Count ears with visible silks per
                                                      plant, n=all plants in harvest rows
```

### C2.4 Grain Fill (R3 -- Milk Stage)

```
STAGE   DAP     MEASUREMENT                          METHOD
R3      80-90   Ear length (husked)                   Ruler on n=5 ears/plot
                                                      (non-harvest-row destructive sample)
R3      80-90   Kernel rows per ear                   Count at mid-ear, n=5 ears
R3      80-90   Kernels per row                       Count longest row, n=5 ears
R3      80-90   Ear diameter (mid-ear)                 Digital caliper, n=5 ears
R3      80-90   Kernel moisture content                Handheld grain moisture meter
R3      80-90   Collect kernels for metabolomics      Flash-freeze in liquid N2
                (separate protocol -- see C5)          Store at -80C
```

### C2.5 Maturity and Harvest (R6)

```
STAGE   DAP      MEASUREMENT                         METHOD
R6      120-140  Final stand count                    Count all plants in harvest rows
R6      120-140  Stalk lodging (%)                    Count stalks broken below ear node
R6      120-140  Root lodging (%)                     Count plants leaning >30 degrees
R6      120-140  Ear height (final)                   Soil to ear node, n=10/plot
R6      120-140  Barren plant count                   Plants with no ear or <10 kernels

HARVEST (R6 + 2-4 weeks, or at 20-25% kernel moisture):

Machine harvest:    Combine (Wintersteiger or Almaco plot combine)
                    with onboard weighing and moisture measurement
                    Harvest center 2 rows x interior length

Hand harvest (if needed for quality measurements):
    Harvest all ears from center 2 rows
    Count ears; weigh total ear mass
    Shell a subsample for grain moisture + grain weight
    Dry remaining ears for yield calculation
```

---

## C3. Yield Components (at R6)

### C3.1 Yield Component Measurements

```
COMPONENT                    METHOD                              UNIT
Ears per plant               Total ears harvested / stand count  ears/plant
Ear length                   Ruler, n=20 ears/plot               cm
Ear diameter                 Caliper at mid-ear, n=20 ears       mm
Kernel rows per ear          Count at mid-ear, n=20 ears         rows
Kernels per row              Count longest row, n=20 ears        kernels
Total kernels per ear        Rows x kernels/row (or image        kernels
                             analysis with KernelFinder)
100-kernel weight            Count 3 x 100 kernels per plot;     g (at 15.5%
                             weigh; adjust to 15.5% moisture      moisture)
Grain yield per plot         Total shelled grain weight per      kg/plot
                             harvest area, adjusted to 15.5%
                             moisture
Grain yield (t/ha)           (Plot yield / harvest area) x       t/ha
                             10,000; adjusted to 15.5% moisture
Harvest index (HI)           Grain yield / total above-ground    ratio
                             biomass (subsample for stover)
Test weight                  Shopper test weight apparatus       kg/hL
                             (or USDA-approved method)
```

### C3.2 Moisture Adjustment

```
All grain weights adjusted to 15.5% moisture (US standard):

Adjusted weight = Measured weight x (100 - measured moisture%) / (100 - 15.5)

Moisture measurement:
    Primary: Dickey-john GAC 2100 or Perten AM 5200 (NIRS)
    Confirmation: Oven-dry method (103C +/- 2C, 72 hours)
    on 50-g subsample per plot
```

### C3.3 Statistical Analysis

```
Linear mixed model:
    Yield_ij = mu + Treatment_i + Location_j + Treatment*Location_ij
               + Block(Location)_k(j) + error_ijk

    Treatment: FIXED effect (3 levels: M-9, Water, RNase-M-9)
    Location: RANDOM effect
    Block nested within Location: RANDOM effect
    Treatment x Location: RANDOM effect (for GxE estimation)

Software: R (lme4 package) or SAS PROC MIXED
Pairwise comparisons: Tukey HSD at alpha = 0.05
ANOVA assumptions: Check residual normality (Shapiro-Wilk)
                   and homoscedasticity (Levene's test)
Effect size: Report treatment means +/- SE, 95% CI, and
             percent change vs. water control
```

---

## C4. Grain Quality Assays

### C4.1 Sweetness / Sugar Content

```
ASSAY 1: Brix Refractometer (fresh sweet corn only)
    Sample: Fresh kernels at R3-R4 (milk-dough stage)
    Method: Press kernel juice onto digital refractometer
            (Atago PAL-1 or equivalent)
    n = 10 kernels per ear, 5 ears per plot
    Report: degrees Brix (+/- 0.1)
    Interpretation: Higher Brix = sweeter
    [NOTE: Only relevant for sweet corn varieties; for field
     corn, skip Brix and proceed directly to HPLC]

ASSAY 2: HPLC Sugar Quantification
    Sample: Lyophilized kernels ground to powder; 100 mg extracted in
            80% ethanol (3 x 1 mL, 80C, 30 min)
    Column: Aminex HPX-87H (Bio-Rad) or NH2-bonded HPLC column
    Mobile phase: 5 mM H2SO4 at 0.6 mL/min (Aminex)
                  or 75:25 acetonitrile:water (NH2)
    Detection: Refractive index (RI)
    Standards: Sucrose, glucose, fructose, maltose (0.1-10 mg/mL)
    Quantification: External calibration curve (R2 > 0.999)
    Report: mg/g DW for each sugar; total soluble sugars
```

### C4.2 Starch Content and Composition

```
ASSAY 3: Total Starch (Megazyme Kit K-TSTA-100A)
    Principle: Enzymatic hydrolysis of starch to glucose
               (thermostable alpha-amylase + amyloglucosidase)
               followed by glucose oxidase/peroxidase colorimetric assay
    Sample: 100 mg finely ground kernel flour (< 0.5 mm)
    Protocol: AOAC Method 996.11 / AACC Method 76-13.01
    Steps:
        1. Disperse starch in DMSO (if resistant starch present)
        2. Hydrolysis: alpha-amylase (100C, 6 min) + amyloglucosidase (50C, 30 min)
        3. Glucose assay: GOPOD reagent, read A510 nm
    Report: % starch w/w (DW basis); expected range 65-75% for dent corn

ASSAY 4: Amylose/Amylopectin Ratio
    Method: Iodine-binding assay (Megazyme K-AMYL or ConA method)
    OR: DSC (differential scanning calorimetry) for gelatinization
    Sample: Purified starch from defatted kernel flour
    Report: % amylose (expected: 25-28% for normal dent; <5% for waxy)
    Interpretation: M-9 treatment is not expected to change amylose ratio
                    (genetically determined); changes would suggest
                    unexpected effects on starch biosynthesis
```

### C4.3 Protein Content and Composition

```
ASSAY 5: Total Protein (Dumas/Kjeldahl)
    Primary method: Dumas combustion (Leco FP-528 or equivalent)
        Sample: 200 mg kernel flour
        Principle: Combustion at 900C; N2 detection by thermal conductivity
        Conversion factor: total N x 6.25 = crude protein
    Secondary method: Kjeldahl (AOAC 979.09)
        Sample: 1 g kernel flour
        Digestion: H2SO4 + catalyst; distillation; titration
    Report: % crude protein (DW basis); expected 8-12% for dent corn

ASSAY 6: Zein Protein Extraction and SDS-PAGE
    Purpose: Determine if M-9 affects zein accumulation (storage proteins)
    Extraction: 70% ethanol + 2% beta-mercaptoethanol
                (sequential extraction of alpha-zein, gamma-zein,
                 beta-zein, delta-zein)
    SDS-PAGE: 12% gel; Coomassie staining or PVDF for immunoblot
    Quantification: Densitometry (ImageJ) of zein bands
                    (19 kDa alpha, 22 kDa alpha, 27 kDa gamma, etc.)
    Report: Relative band intensity normalized to total lane protein
    Interpretation: Elevated zein = more nitrogen storage (higher protein corn)
                    Reduced zein = potentially better amino acid quality
                    (less zein = more non-zein protein with better lysine/tryptophan)
```

### C4.4 Oil Content

```
ASSAY 7: Crude Fat (Soxhlet or NIT/NIRS)
    Soxhlet method:
        Sample: 5 g finely ground kernel flour, dried at 103C
        Solvent: Petroleum ether or diethyl ether
        Extraction: 8 hours reflux
        Report: % crude fat (DW basis); expected 3.5-5% for dent corn

    NIT/NIRS method (rapid screening):
        Instrument: FOSS Infratec 1241 or Perten DA 7250
        Calibration: Validated against Soxhlet with local samples
        Report: % crude fat (DW basis)

    Interpretation: M-9 is not expected to significantly alter oil content
                    (embryo oil is determined during seed development,
                     not affected by seed soak treatment). However,
                     if grain-filling quality is improved, kernel size
                     increase could dilute embryo oil percentage.
```

### C4.5 Moisture Content

```
ASSAY 8: Grain Moisture
    Standard: Oven-dry method (ASABE S352.2)
    Sample: 50 g whole kernels per plot
    Protocol: 103C +/- 2C for 72 hours in forced-air oven
    Calculation: Moisture% = ((wet weight - dry weight) / wet weight) x 100
    Report: % moisture (wet basis)
    Use: All yield and quality measurements adjusted to 15.5% moisture basis
```

---

## C5. Molecular Validation

### C5.1 RT-qPCR Sampling Schedule

```
STAGE    DAP     TISSUE              TARGETS              n
VE       5-7     Embryo axis +       20 target genes +    3 biol reps x
                 scutellum           3 reference genes     3 treatment
                 (dissected seed)                          = 9 samples

V3       14-21   Root tip (0-2 cm)   20 target genes +    3 biol reps x
                 + leaf 3 (mid-      3 reference genes     3 treatment
                 lamina, 5 cm)                             = 9 x 2 tissues

V6       28-35   Root tip + ear      20 target genes +    3 biol reps x
                 primordium          3 reference genes     3 treatment
                 (if visible)                              = 9 x 2 tissues

R1       60-75   Developing ear      20 target genes +    3 biol reps x
                 (kernels 0-7 DAP)   25 biomarker genes    3 treatment
                 + silks + leaf      + 3 reference genes   = 9 x 3 tissues

R3       80-90   Developing kernels  25 biomarker genes    3 biol reps x
                 (14-21 DAP)         + 3 reference genes   3 treatment
                                                           = 9 samples

Total RNA samples: ~90 (across stages, tissues, treatments)
Total qPCR assays: ~90 samples x 48 genes x 3 tech reps = ~12,960 reactions
                   Use 384-well format: ~34 plates
```

### C5.2 Reference Gene Selection

```
Candidate reference genes (select best 3 by geNorm/NormFinder):
    1. ZmActin1 (Zm00001eb404170) -- cytoskeletal
    2. ZmEF1-alpha (Zm00001eb148440) -- translation elongation
    3. ZmGAPDH (Zm00001eb367050) -- glycolysis
    4. ZmUBQ (Zm00001eb264340) -- ubiquitin
    5. ZmTubulin (Zm00001eb403910) -- cytoskeletal
    6. ZmCYP (Zm00001eb110520) -- cyclophilin (peptidyl-prolyl isomerase)

Selection protocol:
    1. Run all 6 candidates on 18 representative samples
       (3 stages x 3 treatments x 2 biol reps)
    2. Analyze with geNorm (Vandesompele et al. 2002) for pairwise variation
    3. Analyze with NormFinder (Andersen et al. 2004) for stability
    4. Select top 3 by consensus ranking
    5. Use geometric mean of 3 reference genes for normalization
```

### C5.3 RNA-seq on Developing Ears

```
Timepoints: R1 (0-7 DAP kernels) and R3 (14-21 DAP kernels)
Treatments: M-9 vs. Water control (T1 vs. T2)
Biological replicates: 3 per treatment per timepoint = 12 libraries
Library prep: Poly(A) enrichment (TruSeq Stranded mRNA)
Sequencing: Illumina NovaSeq 6000, PE150, 30M read pairs per sample
Analysis pipeline:
    1. QC: FastQC + MultiQC
    2. Trim: Trimmomatic or fastp
    3. Align: STAR or HISAT2 to B73 v5 genome
    4. Quantify: featureCounts (Subread)
    5. DE analysis: DESeq2 (Love et al. 2014)
    6. Pathway enrichment: KEGG, GO, MapMan
    7. Focus on: starch biosynthesis, protein storage, hormones

Key genes to examine in RNA-seq:
    All 20 drug targets (residual silencing at R1?)
    All 25 biomarker genes (see C6)
    Starch biosynthesis cluster
    Zein gene cluster (chr 4, chr 7, chr 10)
    Hormone biosynthesis/catabolism genes
```

### C5.4 Metabolomics: ABA/GA in Kernels at R1

```
Sample: Developing kernels at R1 (0-7 DAP), flash-frozen
Analytes: ABA, GA1, GA3, GA4, IAA, JA, JA-Ile, SA, Z (zeatin), ZR
Method: LC-MS/MS (triple quadrupole)
    Extraction: 10 mg lyophilized kernel powder in 1 mL
                methanol:water:formic acid (15:4:1) with
                deuterium-labeled internal standards
                (d6-ABA, d2-GA1, d5-IAA, d5-JA, d4-SA)
    Cleanup: C18 SPE or Oasis HLB cartridge
    LC: UPLC C18 column, 0.3 mL/min, water/acetonitrile + 0.1% FA
    MS: MRM mode, ESI negative (ABA, JA, SA) and positive (GA, IAA, CK)
    Quantification: Isotope dilution with calibration curves

Interpretation:
    ABA lower in M-9 kernels --> residual ABA suppression during grain fill
    GA higher --> accelerated developmental programs
    IAA higher --> enhanced cell division in endosperm
    CK higher --> enhanced grain sink strength
```

---

## C6. Biomarker Panel for Grain Filling Enhancement

### C6.1 Sucrose/Starch Pathway Biomarkers (8 genes)

| # | Gene Name | Gene Model ID | Pathway | Function | Up = | Down = |
|---|-----------|--------------|---------|----------|------|--------|
| 1 | **Sh2** (Shrunken2) | Zm00001eb050730 | Starch biosynthesis | AGPase large subunit; commits glucose-1-P to starch synthesis; rate-limiting step | [KNOWN] Enhanced starch biosynthetic capacity; more amylopectin precursor (ADP-glucose) produced; larger kernels expected | [KNOWN] Reduced starch synthesis; shrunken kernel phenotype (sh2 mutant); sweet corn trait |
| 2 | **Bt2** (Brittle2) | Zm00001eb233830 | Starch biosynthesis | AGPase small (catalytic) subunit; heterotetrameric complex with Sh2 | [KNOWN] Enhanced AGPase activity; more ADP-glucose; improved starch deposition rate | [KNOWN] Reduced starch synthesis; brittle endosperm (bt2 mutant) |
| 3 | **Wx1** (Waxy1) | Zm00001eb304560 | Starch biosynthesis | Granule-bound starch synthase I (GBSSI); synthesizes amylose within starch granules | [KNOWN] More amylose relative to amylopectin; higher apparent amylose content | [KNOWN] Waxy (amylose-free) starch; wx1 null = waxy corn; reduced amylose |
| 4 | **Ae1** (Amylose Extender1) | Zm00001eb116530 | Starch biosynthesis | Starch branching enzyme IIb (SBEIIb); creates alpha-1,6 branch points in amylopectin | [KNOWN] Normal amylopectin branching pattern; standard starch structure | [KNOWN] Increased apparent amylose (resistant starch); ae1 mutant = amylose extender |
| 5 | **Su1** (Sugary1) | Zm00001eb174490 | Starch biosynthesis | Isoamylase-type starch debranching enzyme (ISA1); required for proper starch granule crystallization | [KNOWN] Normal starch granule formation; proper crystalline structure | [KNOWN] Phytoglycogen accumulation instead of starch; sugary endosperm (su1 mutant) |
| 6 | **Sh1** (Shrunken1) | Zm00001eb363690 | Sucrose metabolism | Sucrose synthase (SuSy); cleaves sucrose to UDP-glucose + fructose; channeling to starch synthesis | [KNOWN] Enhanced sucrose conversion to UDP-glucose for starch and cellulose biosynthesis; key for grain filling rate | [KNOWN] Shrunken kernels (sh1 mutant); impaired sucrose-to-starch conversion; reduced grain filling |
| 7 | **INCW2/Mn1** (Miniature1) | Zm00001eb072440 | Sucrose metabolism | Cell wall invertase; irreversibly cleaves sucrose to glucose + fructose at the pedicel/basal endosperm transfer layer | [KNOWN] Enhanced hexose production for endosperm cell division and expansion; critical for sink strength establishment | [KNOWN] Miniature kernel (mn1 mutant); reduced seed size; impaired endosperm development; reduced basal endosperm transfer layer function |
| 8 | **ZmSWEET4c** | Zm00001eb366400 | Sugar transport | Bidirectional hexose transporter; moves glucose/fructose from basal endosperm transfer layer into developing endosperm | [KNOWN] Enhanced hexose delivery to endosperm; improved sink strength; larger kernels | [KNOWN] Reduced kernel filling; impaired sugar transport across BETL; smaller kernels |

### C6.2 Nitrogen Assimilation / Storage Protein Biomarkers (4 genes)

| # | Gene Name | Gene Model ID | Pathway | Function | Up = | Down = |
|---|-----------|--------------|---------|----------|------|--------|
| 9 | **GS1-3** (Gln1-3) | Zm00001eb248430 | N assimilation | Cytosolic glutamine synthetase; assimilates NH4+ into glutamine; major enzyme for N remobilization to grain | [KNOWN] Enhanced N assimilation efficiency; more glutamine for grain protein synthesis; associated with NUE QTL on chr 5 | [KNOWN] Reduced N assimilation; lower grain protein; impaired N remobilization from leaves to grain |
| 10 | **GOGAT** (Fd-GOGAT) | Zm00001eb256160 | N assimilation | Ferredoxin-dependent glutamate synthase; converts glutamine + 2-oxoglutarate to 2 glutamate in plastids | [KNOWN] Enhanced glutamate production; more amino acid precursors for protein synthesis | [KNOWN] Reduced amino acid biosynthesis; impaired N metabolism |
| 11 | **O2** (Opaque2) | Zm00001eb413540 | Storage protein regulation | bZIP transcription factor; master regulator of 22-kDa alpha-zein gene expression; controls ~60% of endosperm protein | [KNOWN] High zein expression; vitreous endosperm; normal kernel hardness | [KNOWN] Reduced zein; opaque/floury endosperm (o2 mutant); higher lysine/tryptophan but soft kernel (QPM breeding target) |
| 12 | **22-kDa alpha-zein cluster** | Multiple loci (chr 4, 7, 10) | Storage protein | Prolamin storage proteins; 50-70% of endosperm protein; packaged in protein bodies | [KNOWN] High storage protein deposition; vitreous endosperm; adequate grain protein | [KNOWN] Reduced protein bodies; opaque endosperm; less total grain protein but better amino acid quality |

### C6.3 Hormone Marker Biomarkers (4 genes)

| # | Gene Name | Gene Model ID | Pathway | Function | Up = | Down = |
|---|-----------|--------------|---------|----------|------|--------|
| 13 | **VP1** (Viviparous1) | Zm00001eb197370 | ABA signaling | B3-domain TF; master regulator of seed maturation and dormancy; activates LEA/Em genes | [KNOWN] Active maturation program; ABA-responsive gene expression; proper desiccation tolerance | [KNOWN] Vivipary (precocious germination); reduced dormancy; reduced desiccation tolerance. NOTE: This IS ABI40, the drug target. Expression at R1/R3 indicates whether drug effects persist to grain fill |
| 14 | **GA20ox** | Zm00001eb380080 | GA biosynthesis | GA 20-oxidase; catalyzes penultimate step in bioactive GA biosynthesis (GA12 --> GA9 --> GA20) | [KNOWN] Enhanced GA biosynthesis; cell elongation; internode extension; can increase grain length | [KNOWN] Reduced GA; dwarf stature; potential grain size reduction |
| 15 | **GA3ox** | Zm00001eb219550 | GA biosynthesis | GA 3-oxidase; catalyzes final step producing bioactive GA1 and GA4 | [KNOWN] Enhanced bioactive GA; promotes cell division in endosperm; larger grain sink | [KNOWN] Reduced bioactive GA; limited cell expansion; smaller kernels |
| 16 | **ABI5** | Zm00001eb290340 | ABA signaling | bZIP TF; downstream effector of ABA signaling in seeds; activates LEA and maturation genes | [KNOWN] Active ABA signaling in developing kernels; proper maturation program | [KNOWN] Reduced ABA response; potentially premature termination of grain fill; accelerated dry-down |

### C6.4 Defense/Stress Biomarkers (3 genes)

| # | Gene Name | Gene Model ID | Pathway | Function | Up = | Down = |
|---|-----------|--------------|---------|----------|------|--------|
| 17 | **PR1** (Pathogenesis-related 1) | Zm00001eb362000 | Defense | SA-inducible defense marker; classic indicator of systemic acquired resistance (SAR) | [KNOWN] Active defense response; SA pathway engaged; potential grain defense against ear pathogens | [KNOWN] Reduced basal defense; potential susceptibility to ear rot (Fusarium, Aspergillus) |
| 18 | **Chitinase (PR3)** | Zm00001eb075570 | Defense | Endochitinase; degrades chitin in fungal cell walls; antimicrobial defense protein | [KNOWN] Active antifungal defense in kernels; protection against Fusarium ear rot and aflatoxin | [KNOWN] Reduced antifungal capacity; increased ear rot susceptibility |
| 19 | **HSP70** | Zm00001eb158050 | Stress response | Heat shock protein 70; molecular chaperone; protects proteins from denaturation under heat stress | [KNOWN] Active heat stress response; protein protection during grain fill under hot conditions; may indicate stress | [KNOWN] Reduced protein protection; higher susceptibility to heat-induced grain fill disruption |

### C6.5 Housekeeping/Reference Genes (3 genes)

| # | Gene Name | Gene Model ID | Pathway | Function | Use |
|---|-----------|--------------|---------|----------|-----|
| 20 | **Actin1** | Zm00001eb404170 | Cytoskeleton | Structural protein; constitutive expression | RT-qPCR normalization reference |
| 21 | **EF1-alpha** | Zm00001eb148440 | Translation | Translation elongation factor; constitutive | RT-qPCR normalization reference |
| 22 | **GAPDH** | Zm00001eb367050 | Glycolysis | Glyceraldehyde-3-phosphate dehydrogenase; constitutive | RT-qPCR normalization reference |

### C6.6 Additional Grain Quality Biomarkers (3 genes)

| # | Gene Name | Gene Model ID | Pathway | Function | Up = | Down = |
|---|-----------|--------------|---------|----------|------|--------|
| 23 | **ZmSSIIa** (Starch synthase IIa) | Zm00001eb386520 | Starch biosynthesis | Soluble starch synthase II; extends amylopectin chains to intermediate length; determines starch gelatinization temperature | [KNOWN] Normal amylopectin chain length distribution; standard gelatinization properties | [KNOWN] Altered amylopectin structure; modified starch functionality; lower gelatinization temperature |
| 24 | **ZmISA2** (Isoamylase 2) | Zm00001eb063770 | Starch biosynthesis | Isoamylase-type DBE; regulatory subunit of ISA1-ISA2 heteromeric complex; required for starch granule formation | [KNOWN] Proper starch granule crystallization; normal starch structure | [KNOWN] Impaired starch granule formation; phytoglycogen accumulation |
| 25 | **ZmCKX1** (Cytokinin oxidase 1) | Zm00001eb310310 | Cytokinin catabolism | Degrades active cytokinins (zeatin, iP); controls local CK levels in developing kernels | [KNOWN] Active CK degradation; limits kernel cell division; smaller kernels | [KNOWN] CK accumulates; MORE cell division in endosperm; LARGER kernels; higher grain yield (CKX downregulation is a breeding target for yield improvement) |

---

### C6.7 Biomarker Panel Summary

**Total panel: 25 genes (22 biomarkers + 3 references)**

**Expected profile if M-9 enhances grain filling:**

| Pathway | Gene | Expected Direction in M-9 vs. Control | Confidence |
|---------|------|--------------------------------------|------------|
| Starch | Sh2 | UP (more AGPase for starch synthesis) | [INFERRED] |
| Starch | Bt2 | UP (more AGPase catalytic subunit) | [INFERRED] |
| Starch | Wx1 | UNCHANGED (amylose ratio genetically fixed) | [INFERRED] |
| Starch | Ae1 | UNCHANGED (branching pattern genetically fixed) | [INFERRED] |
| Starch | Su1 | UP or UNCHANGED | [SPECULATIVE] |
| Sucrose | Sh1 | UP (more SuSy for sucrose conversion) | [INFERRED] |
| Sucrose | INCW2/Mn1 | UP (more CWI for sink strength) | [INFERRED] |
| Sugar transport | ZmSWEET4c | UP (more hexose delivery to endosperm) | [INFERRED] |
| N assimilation | GS1-3 | UP (more N remobilization to grain) | [SPECULATIVE] |
| N assimilation | GOGAT | UP (more glutamate for protein) | [SPECULATIVE] |
| Storage protein | O2 | UNCHANGED (TF activity, not transcript) | [INFERRED] |
| Storage protein | alpha-zein | UP (more storage protein deposition) | [SPECULATIVE] |
| ABA | VP1/ABI40 | DOWN (if residual drug effect) or RECOVERED | [SPECULATIVE] |
| GA | GA20ox | UP (more GA for cell expansion) | [SPECULATIVE] |
| GA | GA3ox | UP (more bioactive GA in kernels) | [SPECULATIVE] |
| ABA | ABI5 | DOWN (if residual ABA suppression) or RECOVERED | [SPECULATIVE] |
| Defense | PR1 | DOWN (growth-defense reallocation) or RECOVERED | [SPECULATIVE] |
| Defense | Chitinase | UNCHANGED or DOWN | [SPECULATIVE] |
| Stress | HSP70 | UNCHANGED (constitutive under non-stress) | [INFERRED] |
| Starch | SSIIa | UNCHANGED (genetically determined) | [INFERRED] |
| Starch | ISA2 | UNCHANGED | [INFERRED] |
| CK catabolism | CKX1 | DOWN (more CK for grain filling) | [SPECULATIVE] |

**Critical interpretation guideline:** If VP1/ABI40 and ABI5 show persistent downregulation at R1/R3 (50+ days after seed soak treatment), this would indicate either: (a) RdDM-mediated epigenetic silencing persisting through mitotic divisions, or (b) a secondary developmental program triggered during germination that maintains different hormone homeostasis. If these targets have RECOVERED to control levels, the grain-filling effects are entirely indirect (larger root system --> more nutrients --> better grain fill).

---

## C7. Statistical Power and Sample Size Justification

```
YIELD POWER ANALYSIS:
    Target detectable difference: 5% yield increase (0.5 t/ha at 10 t/ha mean)
    Expected CV for grain yield: 8-12% (well-managed field trial)
    Alpha: 0.05 (two-sided)
    Power: 0.80

    Required replicates per treatment per location:
    CV = 8%:  n = 5 (RCBD)
    CV = 10%: n = 6 (RCBD)
    CV = 12%: n = 8 (RCBD)

    With 6 locations:
    n = 4-6 reps per treatment per location is sufficient for
    5% yield difference detection across environments

GENE EXPRESSION POWER ANALYSIS:
    Target detectable fold-change: 2-fold (log2FC = 1)
    Expected CV for qPCR: 20-30%
    Alpha: 0.05 (two-sided)
    Power: 0.80

    Required biological replicates: n = 3-4 per treatment per timepoint
    Technical replicates: n = 3 per biological replicate
```

---

## C8. Timeline and Budget Summary

```
PHASE 1: SEED TREATMENT VALIDATION (Month 1-2)
    Lab germination tests (3 treatments x 6 reps)
    RT-qPCR validation of 5 confirmed + 15 predicted targets at VE
    ABA/GA quantification at VE
    Cost: ~$5,000

PHASE 2: GREENHOUSE ROOT PHENOTYPING (Month 2-4)
    Root architecture comparison (rhizotron or WinRHIZO)
    3 treatments x 8 plants x 4 timepoints
    Cost: ~$3,000

PHASE 3: FIELD TRIALS YEAR 1 (Month 3-8)
    4 locations x 24 plots = 96 field plots
    Phenotyping at all growth stages
    Yield harvest and quality analysis
    Cost: ~$40,000-60,000 (includes land, labor, seed, equipment)

PHASE 4: MOLECULAR VALIDATION (Month 4-10)
    RT-qPCR panel (90 samples x 48 genes)
    RNA-seq (12 libraries)
    Metabolomics (18 samples)
    Cost: ~$25,000-35,000

PHASE 5: FIELD TRIALS YEAR 2 (Month 12-20)
    Expanded to 6 locations
    Refined treatments based on Year 1 results
    Cost: ~$60,000-80,000

PHASE 6: DATA ANALYSIS AND REPORTING (Month 20-24)
    Statistical analysis (GxE, mixed models)
    Biomarker correlation with yield components
    Publication preparation
    Cost: ~$5,000 (personnel time)

TOTAL ESTIMATED BUDGET: $138,000-188,000 (2-year program)
MINIMUM VIABLE EXPERIMENT: $15,000 (lab + 1 field location + qPCR)
```

---

## C9. Regulatory and IP Considerations

```
CLASSIFICATION:
    The tRF drug is a biological RNA-based agricultural input.
    Regulatory pathway depends on jurisdiction:
    - US: EPA (biopesticide exemption if no pesticidal claim)
          or USDA-APHIS (if plant-incorporated protectant, unlikely)
          or FDA (if grain quality claims)
    - EU: Novel biostimulant (Regulation EU 2019/1009)
    - Brazil: MAPA biological input registration

DATA REQUIREMENTS FOR REGISTRATION:
    1. Product characterization (tRF sequence, G4 structure, stability)
    2. Efficacy data (field trials, 2+ years, 4+ locations)
    3. Environmental fate (RNA degradation kinetics in soil)
    4. Non-target organism safety (aquatic, avian, mammalian)
    5. Residue analysis (tRF detection in harvested grain -- expected nil)
    6. Manufacturing consistency (batch-to-batch variation)

KEY ADVANTAGE: RNA-based products are generally considered low-risk
because RNA degrades rapidly in the environment (half-life in soil: hours).
No genomic modification of the plant occurs.
```

---

# APPENDIX: Evidence Classification Summary

| Evidence Level | Count | Description |
|----------------|-------|-------------|
| [KNOWN] | ~45 claims | Published peer-reviewed literature with direct experimental support |
| [INFERRED] | ~35 claims | Logical deduction from conserved biology, target annotations, and homolog data |
| [SPECULATIVE] | ~20 claims | Hypotheses requiring experimental validation; includes all quantitative magnitude estimates |

**Honest assessment:** The MoA model is well-supported for the germination phase (Phase 1-2) based on extensive literature on ABA signaling, sugar sensing, and cell wall biology. The root architecture effects (Task B) are largely [INFERRED] from the molecular mechanisms and require experimental validation. The yield translation (B.3) and grain quality predictions are [SPECULATIVE] and represent the highest-uncertainty component of this dossier. The field validation plan (Task C) is designed to systematically test these predictions.

---

*Report prepared: 2026-02-18*
*Dossier version: 1.0*
*Next review: Upon completion of Phase 1 (seed treatment validation)*
