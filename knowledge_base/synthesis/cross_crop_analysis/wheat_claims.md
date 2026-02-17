# WHEAT (Triticum aestivum) -- Mechanistic Claims Extraction

## Overview
- Organism: Triticum aestivum L. (hexaploid bread wheat, AABBDD genome, 2n = 6x = 42)
- Treatment: M-9 bacterial EPS solution, seed soaking 4-8 hours until full imbibition
- Total predicted targets: 75 transcripts (71 protein-coding, 4 nontranslating CDS)
- Evidence level: Gene-level annotation with pathway-level inference; 5 critical annotation corrections applied
- Unique features: Hexaploid (AABBDD, ~17 Gb genome), 374 class III peroxidases, complex dormancy genetics linked to pre-harvest sprouting (PHS), massive aleurone-mediated endosperm mobilization, ~85% repetitive sequences, 155 kinesin genes, ~488 NAC TFs, 24 TaMGT genes, 69 TaARF members
- Reference genome: IWGSC RefSeq v1.1 (Chinese Spring)
- Unique loci after homeolog deduplication: ~72 (69 excluding nontranslating CDS)
- Annotation corrections required: 5 high/moderate severity
- Confirmed homeolog pairs in target list: 3 (chr 2 ABC transporters, chr 6 LRR-RLKs, chr 5 NB-LRRs)
- Dominant theme: 18/75 targets (24%) function in plant immunity/defense -- unprecedented among crops analyzed

---

## Theme 1: ABA/GA Balance and Dormancy Release

### Claims:

- **Claim 1.1**: Downregulation of an SnRK2-family serine/threonine kinase would directly reduce ABA signal transduction, phenocopying the after-ripening process that naturally releases wheat seed dormancy.
  - Genes: TraesCS7D02G384400 (Ser/Thr protein kinase, 891 aa; likely SnRK2-family ABA-activated kinase)
  - Direction: Downregulated by esRNA antisense targeting
  - Mechanism: SnRK2 kinases are the central positive regulators of ABA signaling. Upon ABA perception by PYR/PYL receptors and PP2C inhibition, SnRK2 kinases are released to phosphorylate downstream targets including ABI5/ABF/AREB transcription factors and ion channels. Downregulation would: (i) reduce phosphorylation of ABI5/ABF TFs, lowering expression of ABA-responsive germination-inhibitory genes; (ii) diminish SnRK2-mediated ion channel regulation, reducing stress-responsive stomatal closure; (iii) accelerate the dormancy-to-germination transition. The wheat-specific SnRK2 kinase PKABA1 was the first SnRK2 characterized, identified specifically in wheat embryos (Anderberg & Walker-Simmons, PNAS 1992).
  - Evidence: [Known/Inferred] -- SnRK2 function in ABA signaling is well-established (Fujii & Zhu, PNAS 2009; Yu et al., Plant Cell Reports 2020). The specific SnRK2 identity of TraesCS7D02G384400 requires confirmation but protein kinase domain and 891 aa size are consistent. Supporting evidence: AtPP2-B11, an E3 ubiquitin ligase that degrades SnRK2.3, promotes germination when overexpressed; its loss-of-function shows ABA hypersensitivity and impaired germination [Known].
  - Germination link: Accelerated dormancy-to-germination transition; mimics after-ripening
  - References: Fujii & Zhu, PNAS 2009; Yu et al., Plant Cell Reports 2020; Anderberg & Walker-Simmons, PNAS 1992; Barrero et al., PLoS ONE 2013

- **Claim 1.2**: The after-ripening-mediated dormancy release in wheat involves transcriptional repression of PP2C, SnRK2, and ABI5 genes, and esRNA-mediated downregulation of these same components would phenocopy this natural process.
  - Genes: TaPP2C-a10, TaPP2C-a5 (not directly in target list but contextually relevant), TraesCS7D02G384400 (likely SnRK2), TaABI5 (not in target list but downstream effect)
  - Direction: Downregulated
  - Mechanism: After-ripening in wheat naturally leads to transcriptional repression of ABA signaling cascade components. TaPP2C-a10 interacts with subclass III TaSnRK2 kinases and, when overexpressed, promotes seed germination and decreases ABA sensitivity. TaPP2C-a5 undergoes alternative splicing to produce two isoforms that coordinately negatively regulate seed dormancy. The esRNA system would achieve the same endpoint by directly silencing SnRK2.
  - Evidence: [Known] for after-ripening mechanism; [Inferred] for esRNA-mediated phenocopy
  - Germination link: Reduced ABA sensitivity; faster germination onset
  - References: Barrero et al., PLoS ONE 2013; Yu et al., Plant Cell Reports 2020; Li et al., Journal of Advanced Research 2025; Tuttle et al., Plant Cell & Environment 2022

- **Claim 1.3**: Downregulation of the BTB/POZ and TAZ domain-containing protein 3 could stabilize PP2C phosphatases by reducing CUL3-BTB-mediated degradation, thereby further dampening ABA signaling.
  - Genes: TraesCS3D02G394800 (BTB/POZ + TAZ domain protein 3, 250 aa)
  - Direction: Downregulated
  - Mechanism: BTB/POZ proteins function as substrate adaptors for CUL3-RING E3 ubiquitin ligase complexes. The CUL3-BTB complex targets PP2Cs and stress TFs for proteasomal degradation. Downregulation of the BTB adaptor would stabilize PP2Cs (which are negative regulators of ABA signaling in the canonical pathway), potentially reducing ABA sensitivity in a context-dependent manner.
  - Evidence: [Inferred] -- BTB-CUL3 targeting of ABA signaling components is established in Arabidopsis; specific wheat connection inferred
  - Germination link: Reduced ABA sensitivity through PP2C stabilization
  - References: Inferred from BTB/CUL3 biology literature

- **Claim 1.4**: Transient downregulation of TaPHS1/TaMFT during imbibition could accelerate the dormancy-to-germination transition by reducing ABA sensitivity.
  - Genes: TaPHS1/TaMFT-3A (not directly in the 75-target list but mechanistically central)
  - Direction: Would need downregulation for germination promotion
  - Mechanism: TaPHS1 (TaMFT-3A) is a MOTHER OF FLOWERING TIME-like gene that positively regulates ABA sensitivity and enhances dormancy. It is the causal gene for the major PHS resistance QTL Qphs.pseru-3AS. Two causal mutations in TaPHS1 jointly determine PHS resistance. For germination improvement, the target logic is inverted relative to PHS resistance.
  - Evidence: [Known] -- Liu et al., Genetics 2013; Shorinola et al., Molecular Breeding 2022
  - Germination link: Accelerated dormancy release; but note the PHS risk if applied during grain filling
  - References: Liu et al., Genetics 2013; Nakamura et al., Plant Cell 2011; Shorinola et al., Molecular Breeding 2022

- **Claim 1.5**: The ent-kaurenoic acid oxidase (KAO) target represents a paradoxical finding -- it is a GA biosynthesis enzyme, and its downregulation should impair rather than improve germination.
  - Genes: TraesCS7D02G101200 (Ent-kaurenoic acid oxidase, CYP450, 493 aa)
  - Direction: Downregulated
  - Mechanism: KAO catalyzes oxidation of ent-kaurenoic acid to ent-7alpha-hydroxykaurenoic acid in the GA biosynthesis pathway. GA promotes germination, so downregulating a GA biosynthesis enzyme is contradictory. Possible explanations: (i) KAO is not rate-limiting and other pathway enzymes compensate; (ii) the hexaploid genome provides homeologous copies that buffer the loss; (iii) the sRNA targets this transcript only weakly; or (iv) it is a false-positive antisense alignment.
  - Evidence: [Contradictory] -- This target warrants careful experimental validation
  - Germination link: Expected detrimental; paradoxical presence in target list
  - References: Fu et al., Plant Cell 2002; Gubler et al., Plant Physiology 2002

---

## Theme 2: Endosperm Mobilization

### Claims:

- **Claim 2.1**: Indirect promotion of aleurone activation through ABA/GA balance modulation -- no direct aleurone-specific targets are present in the top-ranked list, but SnRK2, ADC, and NAC38 downregulation would indirectly promote GA-responsive aleurone activation.
  - Genes: TraesCS7D02G384400 (SnRK2 kinase), TraesCS2A02G071200 (ADC), TraesCS5B02G275200 (NAC38) -- indirect effects
  - Direction: All downregulated
  - Mechanism: The aleurone layer (1-3 cells thick in wheat) produces hydrolytic enzymes upon GA perception. GA induces GAMYB transcription factor expression, which transactivates alpha-amylase gene promoters through GARE motifs (TAACAAA). Reducing ABA sensitivity via SnRK2 downregulation and shifting the ABA/GA balance via ADC downregulation would enhance GA-dependent aleurone responses. TOR (target of rapamycin) signaling via TaTOR-TaS6K1 contributes to GA-dependent alpha-amylase synthesis and DELLA protein degradation.
  - Evidence: [Inferred] -- The aleurone mechanism is [Known]; the connection to the esRNA targets is inferred
  - Germination link: Enhanced starch mobilization; faster provision of sugars to the growing embryo
  - References: Gubler et al., Plant Cell 1995; Gubler et al., Plant Physiology 2002; Kaneko et al., Plant Cell 2004; Luo et al., Plant Signaling & Behavior 2023

- **Claim 2.2**: Sugar sensing through hexokinase (HXK) and TOR/SnRK1 signaling represents a metabolic checkpoint during germination that intersects with the ABA/GA axis.
  - Genes: No direct HXK or TOR targets in the list
  - Direction: N/A for direct targeting; indirect modulation via metabolic flux changes
  - Mechanism: Low glucose stimulates germination by promoting ABA catabolism; high glucose delays germination by inducing ABA biosynthesis. The HXK1-glycolytic pathway provides ATP and metabolic intermediates for post-germinative growth. Sugar sensing integrates with TOR kinase and SnRK1 signaling. SQD1 downregulation could redirect UDP-glucose toward glycolysis, potentially affecting this checkpoint.
  - Evidence: [Inferred]
  - Germination link: Metabolic checkpoint coordination
  - References: Smeekens, Annual Review of Plant Biology 2000; Cho et al., Trends in Plant Science 2006; Granot et al., BMC Plant Biology 2013

- **Claim 2.3**: Beta-glucanase targets may facilitate endosperm cell wall degradation during reserve mobilization.
  - Genes: TraesCS2A02G439500 (GH17 beta-glucanase, 460 aa), TraesCS5A02G429600 (GH17 beta-glucanase, 490 aa)
  - Direction: Downregulated -- paradoxical for endosperm mobilization
  - Mechanism: GH17 family glucan endo-1,3-beta-D-glucosidases hydrolyze beta-glucans in cell walls and callose. Downregulation during germination would impair cell wall degradation, which is detrimental to mobilization. However, these enzymes also function in plant defense (callose degradation at plasmodesmata). Their targeting may relate to the defense downshift theme rather than endosperm mobilization.
  - Evidence: [Inferred] -- Likely defense-related rather than mobilization-related
  - Germination link: Ambiguous -- defense context more likely
  - References: General GH17 biology

---

## Theme 3: ROS/Oxidative Window

### Claims:

- **Claim 3.1**: PARP downregulation conserves NAD+ and ATP while simultaneously reducing ROS-mediated cellular damage, representing the single most robust target for improving germination vigor.
  - Genes: TraesCS1A02G328000 (Poly[ADP-ribose] polymerase, PARP, 824 aa; PARP catalytic domain + DNA-binding zinc finger domain)
  - Direction: Downregulated by esRNA antisense targeting
  - Mechanism: PARP catalyzes poly(ADP-ribosyl)ation using NAD+ as substrate, activated by DNA damage and oxidative stress during imbibition. During wheat seed germination, the embryo experiences oxidative stress from membrane lipid peroxidation, mitochondrial reactivation, and ROS generation. PARP activation consumes NAD+ critically needed for respiratory metabolism. Downregulation conserves the NAD+ pool, providing more ATP for reserve mobilization, cell division, and radicle emergence. De Block et al. (2005) demonstrated >10% biomass increase in PARP-deficient Arabidopsis and oilseed rape with broad-spectrum stress tolerance and maintained NAD+/ATP levels. Vanderauwera et al. (2007) and Schulz et al. (2012) confirmed these findings through both genetic and pharmacological (3-methoxybenzamide) PARP inhibition. AtPARP3 is specifically expressed in seeds, with promoter activity coinciding with ROS accumulation in the embryo (Rissel et al., BMC Plant Biology 2019).
  - Evidence: [Known] -- This is the most well-validated of all targets. PARP downregulation improving plant vigor is documented across multiple species and methods.
  - Germination link: Conserved NAD+ and ATP for biosynthetic processes; reduced oxidative damage; improved energy homeostasis during the metabolic burst of early germination
  - References: De Block et al., Plant Journal 2005; Vanderauwera et al., PNAS 2007; Schulz et al., PLoS ONE 2012; Rissel et al., BMC Plant Biology 2019

- **Claim 3.2**: The oxidative window concept defines a critical ROS concentration range for germination -- too little ROS prevents dormancy release, too much causes oxidative damage -- and multiple esRNA targets modulate this window.
  - Genes: TraesCS1A02G328000 (PARP -- indirectly modulates ROS via NAD+/mitochondrial effects), TraesCS6B02G296400 (AOX -- directly modulates ROS), class III peroxidases (374 members in wheat, none directly targeted but PARP-ROS connection intersects)
  - Direction: PARP downregulated (beneficial for ROS management); AOX downregulated (detrimental -- would increase ROS above the oxidative window)
  - Mechanism: Bailly et al. (2008) proposed that germination is only possible when intracellular ROS levels fall within a defined range. H2O2 acts as a signaling molecule promoting dormancy release by interfering with ABA signaling. Wheat's 374 class III peroxidases perform dual functions: generating ROS (oxidative cycle) and scavenging ROS (peroxidative cycle). TaPer12-3A specifically promotes germination by scavenging excess H2O2 (Han et al., BMC Plant Biology 2024). PARP downregulation reduces ROS formation indirectly by maintaining mitochondrial function. AOX downregulation would be detrimental by increasing mitochondrial ROS.
  - Evidence: [Known] for the oxidative window concept; [Inferred] for the PARP-ROS-germination connection in wheat specifically
  - Germination link: Maintenance of ROS within the germination-permissive oxidative window
  - References: Bailly et al., Comptes Rendus Biologies 2008; Han et al., BMC Plant Biology 2024; Wang et al., BMC Genomics 2019; Ishibashi et al., Frontiers in Plant Science 2017; Ye et al., Frontiers in Plant Science 2020

- **Claim 3.3**: AOX (ubiquinol oxidase) downregulation is paradoxical and likely detrimental -- it would push ROS above the oxidative window during the metabolic burst of early germination.
  - Genes: TraesCS6B02G296400 (Ubiquinol oxidase / Alternative oxidase, AOX, 340 aa)
  - Direction: Downregulated
  - Mechanism: AOX bypasses proton-pumping complexes III and IV of the electron transport chain, reducing ATP yield but managing ROS levels. AOX2 is specifically expressed during early seed germination and is essential for ROS homeostasis; AOX mutants show salt-hypersensitive germination. Downregulation would increase mitochondrial ROS to damaging levels and enhance ABA sensitivity.
  - Evidence: [Contradictory] -- Current evidence predicts detrimental effects from AOX downregulation
  - Germination link: Detrimental; possible explanations include (i) fine-tuning rather than elimination could optimize energy efficiency, (ii) temporal dispensability during very early imbibition (0-6h) when mitochondria are reorganizing, or (iii) false-positive antisense alignment
  - References: Vanlerberghe, International Journal of Molecular Sciences 2013; Saha et al., Plant Signaling & Behavior 2016; Zheng et al., Environmental and Experimental Botany 2024

---

## Theme 4: Polyamine Metabolism

### Claims:

- **Claim 4.1**: ADC downregulation would reduce putrescine accumulation, shifting the polyamine ratio from ABA-promoting to GA-promoting, while redirecting metabolic resources.
  - Genes: TraesCS2A02G071200 (Arginine decarboxylase, ADC, 625 aa; pyridoxal phosphate-dependent decarboxylase domain; UniProt A0A3B6AQP0)
  - Direction: Downregulated by esRNA antisense targeting
  - Mechanism: ADC catalyzes the first and rate-limiting step of the polyamine biosynthesis pathway: decarboxylation of L-arginine to agmatine, subsequently converted to putrescine, then spermidine and spermine. The polyamine-ABA crosstalk is bidirectional: putrescine positively regulates ABA biosynthesis gene expression (including NCED3), while spermidine and spermine promote GA biosynthesis and oppose ABA. During germination, an increase in the (spermidine + spermine) : putrescine ratio is observed in embryos. ADC downregulation would produce multiple convergent effects: (i) reduced putrescine accumulation leading to decreased NCED expression and lower ABA levels; (ii) shift in polyamine ratio toward GA-promoting forms; (iii) increased availability of SAM for ethylene biosynthesis (polyamines and ethylene compete for SAM), and ethylene generally promotes germination; (iv) redirection of arginine toward protein synthesis; (v) reduced energy expenditure on polyamine biosynthesis.
  - Evidence: [Known] for polyamine-ABA crosstalk; [Inferred] for the beneficial effect of ADC downregulation on wheat germination
  - Germination link: Reduced ABA signaling, enhanced GA response, increased ethylene availability, metabolic resource redirection
  - Caveat: ADC activity is also critical for stress tolerance during imbibition. Under osmotic stress, ADC activity increases dramatically and elevated putrescine is protective. Complete loss of polyamines is lethal. The benefit requires moderate, transient downregulation -- consistent with the sRNA-mediated mechanism during the 4-8 hour imbibition window.
  - References: Alcazar et al., Planta 2010; Pieruzzi et al., BMC Plant Biology 2011; Bassie et al., Molecular Breeding 2008; Sinska & Lewandowska, Plant Growth Regulation 1991; Bouchereau et al., Journal of Plant Physiology 1999; Ebeed et al., BMC Genomics 2022

---

## Theme 5: Auxin Signaling and Developmental Patterning

### Claims:

- **Claim 5.1**: Downregulation of a repressor-class ARF could constitutively activate auxin-responsive genes, promoting radicle elongation and coleoptile growth.
  - Genes: TraesCS6B02G167100 (Auxin response factor, ARF, 927 aa; B3 DNA-binding domain + Auxin_resp domain + AUX/IAA domain; 220 orthologues, 21 paralogues)
  - Direction: Downregulated
  - Mechanism: ARFs bind to auxin response elements (AuxREs) to activate or repress target gene expression. Hexaploid wheat contains 69 TaARF members in 24 homoeologous groups. Approximately 60% of ARFs are transcriptional repressors (Q-rich middle regions). If TraesCS6B02G167100 is a repressor-class ARF, its downregulation would constitutively activate auxin-responsive genes promoting radicle emergence and cell elongation. TaARF4 determines root length and plant height in wheat. The ARF-Aux/IAA interaction module provides combinatorial specificity.
  - Evidence: [Inferred] -- The repressor vs. activator identity of this specific ARF needs confirmation
  - Germination link: Enhanced radicle elongation and coleoptile growth; improved seedling establishment
  - Caveat: Excessive auxin signaling can inhibit growth through feedback mechanisms
  - References: Qiao et al., Frontiers in Plant Science 2018; Bouzroud et al., South African Journal of Botany 2020; Vernoux et al., Molecular Cell 2011

- **Claim 5.2**: YABBY transcription factor (TaYABBY3A) downregulation would delay leaf polarity establishment, conserving energy during the dark germination phase.
  - Genes: TraesCS2A02G386200 (TaYABBY3A, 262 aa; C2-C2 zinc finger + YABBY domain [HLH-like fold]; plant-specific TF family; confirmed by Zhao et al., PeerJ 2022)
  - Direction: Downregulated
  - Mechanism: YABBY transcription factors regulate abaxial-adaxial polarity in lateral organs and leaf development. During dark germination when leaf polarity establishment is premature, downregulation would save energy by delaying developmental programs not yet needed. YABBY TFs are stress-responsive in wheat; GmYABBY10 is involved in salt and drought stress responses in soybean.
  - Evidence: [Inferred] -- YABBY function is known; germination-specific benefit is inferred
  - Germination link: Energy conservation during dark heterotrophic growth by delaying premature developmental programs
  - References: Zhao et al., PeerJ 2022; Zhao SP et al., Plant Physiology and Biochemistry 2017

- **Claim 5.3**: CDC27/APC3 downregulation could moderate premature cell division, prioritizing reserve mobilization over proliferation.
  - Genes: TraesCS7A02G398600 (CDC27/APC3 -- Cell division cycle protein 27 homolog B, 718-758 aa; TPR repeats + ANAPC3 domain)
  - Direction: Downregulated
  - Mechanism: CDC27/APC3 is a core component of the anaphase-promoting complex (APC/C), essential for mitotic progression. Moderate downregulation could slow premature cell division during very early germination, prioritizing reserve mobilization over proliferation.
  - Evidence: [Speculative]
  - Germination link: Possible metabolic prioritization of mobilization over division
  - References: General APC/C biology

---

## Theme 6: Chloroplast Transition and Membrane Lipids

### Claims:

- **Claim 6.1**: SQD1 downregulation during the dark heterotrophic germination phase is predicted to be metabolically neutral or mildly beneficial by redirecting UDP-glucose toward energy-producing pathways.
  - Genes: TraesCS1D02G241800 (SQD1, UDP-sulfoquinovose synthase, chloroplastic, 478 aa; CORRECTED from original "Arginine decarboxylase" annotation; Arabidopsis ortholog AT4G33030), TraesCS3D02G228900 (SQD1-related, 809-1,048 aa; provisionally annotated as SQD1)
  - Direction: Downregulated
  - Mechanism: SQD1 catalyzes the first committed step in sulfolipid (SQDG) biosynthesis, converting UDP-glucose and sulfite to UDP-sulfoquinovose. SQDG is found predominantly in thylakoid membranes. During seed germination, the embryo grows heterotrophically in darkness -- thylakoid membrane assembly and SQDG biosynthesis are not required. Arabidopsis sqd2 mutants showed impaired growth only under phosphate-limited conditions. Transient SQD1 downregulation would redirect UDP-glucose toward glycolysis and cell wall biosynthesis, and sulfur toward amino acid synthesis -- both beneficial for germination energy and protein production. SQD1 expression is dramatically upregulated (up to 15-fold) under phosphate limitation; this response would be unnecessary during early germination from seed reserves.
  - Evidence: [Known] for SQD1 biochemistry and dispensability; [Inferred] for benefit during germination
  - Germination link: Metabolic resource redirection; improved energy availability for germinating seedling
  - Note: TraesCS5A02G365700 was originally annotated as SQD1 but is actually a nontranslating CDS with no protein product -- the SQD1 annotation was likely inherited from a neighboring gene.
  - References: Mulichak et al., PNAS 1999; Sanda et al., Journal of Biological Chemistry 2001; Essigmann et al., PNAS 1998; Yu et al., PNAS 2002

---

## Theme 7: Epigenetic/Chromatin Remodeling

### Claims:

- **Claim 7.1**: DDM1 downregulation could derepress germination-promoting genes silenced by DNA methylation during seed maturation and dormancy.
  - Genes: TraesCS7A02G074600 (DDM1 -- Decrease in DNA Methylation 1, 751 aa; helicase ATP-binding domain + helicase C-terminal domain; SNF2-like superfamily)
  - Direction: Downregulated
  - Mechanism: DDM1 is an SNF2-family chromatin remodeling ATPase that maintains DNA methylation patterns by remodeling nucleosomes to allow DNA methyltransferase access to hemimethylated DNA. In Arabidopsis, ddm1 mutants show progressive loss of DNA methylation across repetitive sequences and some genes, activation of transposable elements, and developmental abnormalities (Jeddeloh et al., Nature Genetics 1999). Transient DDM1 downregulation during germination could cause partial, stochastic demethylation that derepresses germination-promoting genes silenced during maturation. The hexaploid wheat genome, with ~85% repetitive sequences (IWGSC 2018), may be particularly sensitive to DDM1 modulation. Epigenetic reprogramming is a recognized component of the dormancy-to-germination transition in cereals.
  - Evidence: [Inferred] -- DDM1 function is [Known]; the specific germination-promoting consequence of transient downregulation in wheat is [Speculative]
  - Germination link: Epigenetic derepression of growth-promoting gene programs
  - References: Jeddeloh et al., Nature Genetics 1999; IWGSC, Science 2018

- **Claim 7.2**: Bromodomain TF (GTE8 family) downregulation may reduce transcription of defense or stress gene programs by decreasing acetylated histone reading capacity.
  - Genes: TraesCS3A02G122200 (Bromodomain-containing TF, GTE8 family, 519-713 aa; bromodomain + NET domain + coiled coil)
  - Direction: Downregulated
  - Mechanism: Bromodomains recognize and bind acetylated lysine residues on histones, recruiting transcriptional machinery to actively transcribed chromatin. Downregulation would reduce the cell's capacity to read histone acetylation marks, potentially reducing transcription of defense or stress gene programs.
  - Evidence: [Speculative]
  - Germination link: Possible reduction of stress/defense gene transcription, reallocating resources
  - References: General bromodomain/chromatin biology

- **Claim 7.3**: Homeobox-DDT domain protein downregulation may modulate chromatin remodeling and developmental gene expression.
  - Genes: TraesCS2A02G124800 (Homeobox-DDT domain protein, RLT-3 family, 1,090 aa; Homeobox domain + DDT domain)
  - Direction: Downregulated
  - Mechanism: DDT domain proteins are involved in chromatin remodeling. The homeobox domain provides DNA-binding specificity. Together with DDM1 and GTE8, this target suggests a coordinated modulation of the epigenetic landscape during germination.
  - Evidence: [Speculative]
  - Germination link: Epigenetic/transcriptional modulation
  - References: General homeobox/DDT biology

---

## Theme 8: Defense Pathway Downshift (THE DOMINANT THEME -- 24% of targets)

### Claims:

- **Claim 8.1**: Coordinated downregulation of 6 F-box proteins would broadly reduce immune-related protein turnover via the SCF (Skp1-Cullin-F-box) ubiquitin ligase complex, redirecting ATP from proteasomal degradation toward growth.
  - Genes:
    - TraesCS5A02G188400 (F-box with kelch beta-propeller, 370 aa; CORRECTED from "ARF")
    - TraesCSU02G067600 (F-box/LRR-repeat protein, 215 aa; CORRECTED from "Kinesin")
    - TraesCS5A02G170400 (Uncharacterized F-box, 431 aa; beta-propeller domain)
    - TraesCS6A02G040900 (F-box, 407-411 aa)
    - TraesCS2D02G520600 (F-box with kelch repeats, 430 aa)
    - TraesCS4D02G117200 (F-box/LRR with FBD domain, 511 aa)
  - Direction: All downregulated
  - Mechanism: F-box proteins serve as substrate recognition components of SCF E3 ubiquitin ligase complexes, targeting specific proteins for proteasomal degradation. In plant immunity, F-box proteins degrade suppressors of immune signaling, thereby activating defense responses. Coordinated downregulation of 6 F-box proteins would broadly reduce protein turnover in immune pathways, decreasing energy investment in defense and redirecting ATP, amino acids, and metabolic precursors toward germination processes.
  - Evidence: [Inferred] -- F-box role in immunity is [Known]; germination benefit from immune downshift is [Inferred]
  - Germination link: Energy reallocation from defense to growth; reduced metabolic cost of proteasomal turnover
  - References: Weiberg et al., Science 2013 (cross-kingdom RNAi precedent)

- **Claim 8.2**: Coordinated downregulation of 5 LRR receptor-like kinases would reduce PAMP-triggered immunity (PTI) at the cell surface, decreasing the energy cost of immune surveillance.
  - Genes:
    - TraesCS7D02G379600 (Lectin-RLK with lectin + apple domains, 596 aa)
    - TraesCS5D02G095300 (Malectin-LRR-RLK, 955 aa)
    - TraesCS6B02G152900 (LRR-RLK, 1,049 aa; probable homeolog with #57)
    - TraesCS6D02G116100 (LRR-RLK, 1,050 aa; probable homeolog with #59)
    - TraesCS5B02G502400 (L-type lectin-RLK, 731 aa)
  - Direction: All downregulated
  - Mechanism: LRR-RLKs are the first line of pathogen perception in PAMP-triggered immunity (PTI). They contain extracellular LRR, lectin, or malectin domains for pathogen molecule recognition, transmembrane domains, and intracellular kinase domains for signal transduction. Their downregulation would reduce immune surveillance at the cell surface. The coordinated targeting of both B- and D-subgenome homeologs of chr 6 LRR-RLKs is noteworthy.
  - Evidence: [Inferred] -- LRR-RLK immune function is [Known]; benefit from reduced surveillance during germination is [Inferred]
  - Germination link: Reduced energy expenditure on immune surveillance; facilitation of beneficial bacterial interaction
  - References: Weiberg et al., Science 2013; Shahid et al., Nature 2018

- **Claim 8.3**: Downregulation of 2 NB-LRR disease resistance proteins (probable homeologs on chr 5B and 5D) would reduce the energy-expensive effector-triggered immunity (ETI) pathway.
  - Genes:
    - TraesCS5D02G521900 (NB-LRR, 946 aa; NB-ARC + winged helix + LRR domains; 38 orthologues, 694 paralogues)
    - TraesCS5B02G559900 (NB-LRR, 1,136 aa; Rx_N + NB-ARC + winged helix + LRR domains; 157 orthologues, 822 paralogues)
  - Direction: Both downregulated (probable homeologs targeted coordinately)
  - Mechanism: NB-LRR proteins mediate effector-triggered immunity (ETI), the most energy-expensive defense response involving hypersensitive response and programmed cell death. The massive paralogy (694-822 paralogs each) indicates rapid birth-and-death evolution characteristic of plant immune receptors. Coordinated targeting of B- and D-subgenome copies would amplify the knockdown effect beyond hexaploid buffering.
  - Evidence: [Inferred]
  - Germination link: Reduced defense energy investment; resource reallocation to growth
  - References: General NLR biology; Weiberg et al., Science 2013

- **Claim 8.4**: ABC transporters involved in defense compound transport would be downregulated, reducing ATP expenditure on xenobiotic/defense compound efflux.
  - Genes:
    - TraesCS7B02G381000 (ABCG/PDR subfamily, 1,389 aa; 2 ABC transporter domains, 13 TM helices)
    - TraesCS2B02G069000 (ABCC13/MRP, LOW PHYTIC ACID 2, 1,531 aa; probable homeolog with #41)
    - TraesCS2A02G056800 (ABCC conjugate transporter, 992 aa; probable homeolog with #40)
  - Direction: All downregulated
  - Mechanism: ABC transporters actively export defense compounds and detoxification conjugates, consuming significant ATP. ABCG/PDR subfamily members transport defense-related secondary metabolites. ABCC/MRP transporters transport conjugated xenobiotics and phytic acid into vacuoles. The chr 2 A-B homeolog pair suggests coordinated targeting.
  - Evidence: [Inferred]
  - Germination link: ATP conservation by reducing active transport of defense compounds
  - References: General ABC transporter biology

- **Claim 8.5**: Additional defense targets (Gnk2 antifungal protein and LURP1-related protein) further support the defense downshift model.
  - Genes:
    - TraesCS2A02G393400 (Gnk2-homologous antifungal protein, 307 aa; 2 Gnk2-homologous domains + signal peptide + TM helix)
    - TraesCS1D02G303100 (LURP-one-related 8 / LOR family, 209 aa; LOR domain + Tubby-like C-terminal domain)
  - Direction: Both downregulated
  - Mechanism: Gnk2 proteins are stress-antifungal defense proteins. LURP1 (Lazarus1-Upregulated Protein 1) family members are involved in RPP5-mediated immune responses. Their downregulation reduces constitutive defense compound production.
  - Evidence: [Inferred]
  - Germination link: Defense-to-growth resource shift
  - References: General defense protein biology

- **Claim 8.6**: The defense downshift pattern parallels the immune suppression strategy used by pathogenic fungi (Botrytis cinerea), but in a mutualistic rather than parasitic context.
  - Genes: All 18 defense-related targets collectively
  - Direction: All downregulated
  - Mechanism: Weiberg et al. (2013) demonstrated that Botrytis cinerea delivers Bc-sRNAs into plant cells to silence MAPKKKs, WAKs, and oxidative burst regulators. Cai et al. (2018) showed plants reciprocate by exporting sRNAs to silence Botrytis virulence genes. The wheat esRNA target pattern -- coordinated suppression of F-box proteins, LRR-RLKs, NB-LRRs, ABC transporters, and defense proteins -- mirrors pathogenic immune suppression but in a context where the bacterial sRNAs are facilitating beneficial interaction rather than infection.
  - Evidence: [Speculative] -- The cross-kingdom RNAi precedent is [Known]; the mutualistic interpretation is [Speculative]
  - Germination link: Facilitated beneficial plant-microbe interaction; reduced immune-mediated energy drain
  - References: Weiberg et al., Science 2013; Cai et al., Science 2018; Shahid et al., Nature 2018; Buck et al., Nature Communications 2014

---

## Theme 9: Organelle Gene Expression and Respiration

### Claims:

- **Claim 9.1**: PPR protein downregulation could be tolerable if the targeted member is involved in chloroplast rather than mitochondrial RNA processing.
  - Genes: TraesCS3B02G123400 (PPR protein, projected from Arabidopsis At5g16860, 661 aa; multiple PPR repeats; 158 orthologues, 552 paralogues)
  - Direction: Downregulated
  - Mechanism: PPR proteins (>450 members in wheat) mediate post-transcriptional RNA processing in mitochondria and chloroplasts: RNA editing (C-to-U), intron splicing, transcript stabilization, translational regulation. During germination, mitochondrial biogenesis is critical for aerobic respiration resumption. Chloroplast-targeted PPR proteins that process transcripts needed only for photosynthesis would be dispensable during the dark heterotrophic phase. If At5g16860 is chloroplast-targeted, its downregulation during germination may be tolerated.
  - Evidence: [Inferred] -- Depends on the subcellular targeting of this specific PPR protein
  - Germination link: Potentially neutral if chloroplast-targeted; detrimental if mitochondrial
  - References: Barkan & Small, Annual Review of Plant Biology 2014; Ren et al., Plant Communications 2025

- **Claim 9.2**: mTERF domain protein downregulation may affect organellar transcription termination.
  - Genes: TraesCS6B02G109500 (mTERF domain protein, 125 aa; mitochondrial transcription termination factor family / PORR domain)
  - Direction: Downregulated
  - Mechanism: mTERF proteins regulate organellar transcription termination in mitochondria and chloroplasts. The small size (125 aa) and high paralogy (130 paralogues) suggest this may be a specialized, partially redundant family member.
  - Evidence: [Speculative]
  - Germination link: Uncertain; depends on organellar targeting and transcript specificity
  - References: General mTERF biology

---

## Theme 10: Ribosome Biogenesis and Translation (DETRIMENTAL if silenced)

### Claims:

- **Claim 10.1**: BOP1 downregulation would be highly detrimental to germination by reducing translational capacity during the critical period when stored mRNAs must be translated.
  - Genes: TraesCS5A02G360900 (BOP1 -- Ribosome biogenesis protein BOP1 homolog, 694 aa; WD40 repeats; CORRECTED from "BTB/POZ and TAZ domain protein 3")
  - Direction: Downregulated -- PARADOXICAL/DETRIMENTAL
  - Mechanism: BOP1 is part of the PeBoW complex (PES/BOP1/WDR12) essential for 60S ribosomal large subunit assembly and 25S rRNA maturation. Wheat seeds store ~38% of total transcripts in the dry state; upon imbibition, these stored mRNAs are selectively loaded onto polysomes and translated before de novo transcription commences (0-8 hours post-imbibition). BOP1 silencing in tobacco caused defective ribosome biogenesis, repressed global protein translation, altered nucleolar structure, and delayed cell growth.
  - Evidence: [Contradictory] -- Translation is the rate-limiting step during early germination
  - Germination link: DETRIMENTAL; however, stored ribosomes may buffer 0-24h, providing some tolerance; energy savings from reduced ribosome synthesis is speculative
  - References: Ahn et al., Journal of Experimental Botany 2016; Cho et al., Plant Journal 2013; Bai et al., Plants 2020; Barrero et al., PLoS ONE 2012

---

## Theme 11: Cytoskeletal Dynamics (DETRIMENTAL if silenced)

### Claims:

- **Claim 11.1**: Kinesin motor protein downregulation would impair cell division and intracellular transport essential for radicle emergence.
  - Genes: TraesCS2B02G505400 (Kinesin-like protein, 785 aa; kinesin motor domain + microtubule-binding; 283 orthologues, 44 paralogues)
  - Direction: Downregulated -- PARADOXICAL/DETRIMENTAL
  - Mechanism: Kinesins control microtubule dynamics during mitosis and cytokinesis. The wheat kinesin superfamily comprises 155 genes (TaKIN). Loss of function of specific kinesins results in randomly oriented microtubules and aberrant cell expansion. However, the 155-member family provides significant redundancy.
  - Evidence: [Contradictory] -- Cell division is essential for germination
  - Germination link: DETRIMENTAL; partially buffered by 155-member family redundancy
  - References: Wang et al., BMC Genomics 2024

- **Claim 11.2**: Profilin downregulation would impair rapid cell elongation required for radicle protrusion and coleoptile growth.
  - Genes: TraesCS1B02G356700 (Profilin, 131 aa; profilin domain; 268 orthologues)
  - Direction: Downregulated -- DETRIMENTAL
  - Mechanism: Profilins regulate actin polymerization by catalyzing ADP/ATP exchange on actin monomers. The actin cytoskeleton drives cell expansion, vesicle trafficking, organelle movement, and polar growth. Profilin levels are dose-sensitive: both over- and under-expression impair growth.
  - Evidence: [Contradictory] -- Cell elongation requires profilin
  - Germination link: DETRIMENTAL; unfavorable target for esRNA-mediated silencing
  - References: Bao et al., Frontiers in Plant Science 2015; Fan et al., Plant Cell Reports 2013

---

## Theme 12: Stress Response and Protein Quality Control

### Claims:

- **Claim 12.1**: NAC domain protein 38 (NAC38) downregulation would reduce stress-transcriptional braking on germination.
  - Genes: TraesCS5B02G275200 (NAC domain containing protein 38, projected from Arabidopsis AT2G24430/ANAC038, 368 aa; NAC domain + TAR region; 173 orthologues, 26 paralogues)
  - Direction: Downregulated
  - Mechanism: The wheat NAC TF family is massive (~488 members). Multiple wheat NAC genes are ABA-inducible and stress-responsive: TaNAC29 promotes senescence and salt/drought stress responses; TaSNAC11-4B promotes ROS accumulation and senescence; TaNAC2 enhances abiotic stress tolerance. If NAC38 follows the dominant pattern of being ABA-inducible and stress-responsive, its downregulation would: (i) reduce expression of dormancy-maintenance gene programs; (ii) decrease stress-responsive gene expression that inhibits growth; (iii) limit senescence-associated PCD beyond what is needed for aleurone function; (iv) redirect metabolic resources from stress compound synthesis toward germination processes.
  - Evidence: [Inferred] -- Contingent on NAC38 being stress/ABA-responsive rather than a dormancy inhibitor like ANAC060/040
  - Germination link: Reduced stress transcriptional braking; enhanced growth-promoting gene expression
  - References: Xia et al., PLoS ONE 2019; general NAC TF literature

- **Claim 12.2**: sHSP/alpha-crystallin chaperone downregulation may reduce energy expenditure on stress-responsive protein folding during non-stress germination.
  - Genes: TraesCS4B02G205800 (sHSP/alpha-crystallin domain protein, 536 aa; DUF8041 + HSP20-like alpha-crystallin domain)
  - Direction: Downregulated
  - Mechanism: Small heat shock proteins function as molecular chaperones, preventing irreversible aggregation of denatured proteins. During non-stress germination, reducing the constitutive expression of stress-responsive chaperones could conserve energy.
  - Evidence: [Inferred]
  - Germination link: Energy conservation during non-stress conditions
  - References: General sHSP biology

---

## Theme 13: One-Carbon Metabolism

### Claims:

- **Claim 13.1**: SHMT (serine hydroxymethyltransferase) downregulation would affect one-carbon metabolism with complex consequences for folate-dependent biosynthetic reactions.
  - Genes: TraesCS3D02G378700 (Glycine hydroxymethyltransferase / SHMT, 583 aa; SHMT-like domain + PLP-dependent transferase; cofactor pyridoxal 5'-phosphate)
  - Direction: Downregulated
  - Mechanism: SHMT catalyzes the reversible interconversion of serine and glycine, a central reaction in one-carbon metabolism providing methyl groups for nucleotide biosynthesis, amino acid metabolism, and methylation reactions via the folate cycle. Downregulation would reduce one-carbon flux, potentially impairing DNA synthesis and methylation -- but also potentially reducing SAM availability for ABA-related methylation.
  - Evidence: [Speculative] -- Complex metabolic consequences, difficult to predict net effect
  - Germination link: Uncertain; context-dependent effects on methylation and biosynthesis
  - References: General SHMT/one-carbon metabolism biology

---

## Theme 14: Membrane Transport and Ion Homeostasis

### Claims:

- **Claim 14.1**: Magnesium transporter downregulation may be tolerable if the target is chloroplast-localized, as photosynthetic Mg2+ demand is minimal during dark germination.
  - Genes: TraesCS3B02G440800 (Probable magnesium transporter, CorA-type, 364 aa; 60 orthologues, 10 paralogues)
  - Direction: Downregulated
  - Mechanism: TaMGT transporters maintain Mg2+ homeostasis essential for chlorophyll biosynthesis, photosynthetic enzyme activity, ribosome function (Mg2+ stabilizes ribosomal subunit association), and as cofactor for kinases and phosphatases. 24 TaMGT genes exist in wheat with 20 predicted to localize to chloroplasts. During heterotrophic germination, chloroplast Mg2+ demand is minimal. Silencing of cytoplasmic or mitochondrial Mg2+ transporters would impair translation and respiration.
  - Evidence: [Inferred] -- Depends on subcellular localization of this specific transporter
  - Germination link: Potentially neutral if chloroplast-targeted; detrimental if cytoplasmic/mitochondrial
  - References: Ma et al., Frontiers in Plant Science 2023; Gebert et al., New Phytologist 2009; Li et al., Plant and Cell Physiology 2016

- **Claim 14.2**: Mechanosensitive ion channels (MscS family) downregulation may affect osmotic stress sensing during imbibition.
  - Genes:
    - TraesCS7B02G381200 (MscS mechanosensitive channel, 1,416-1,423 aa; MscS TM domain + C-terminal domain; 4 TM helices)
    - TraesCS7B02G358900 (MscS mechanosensitive channel, 621-641 aa; MscS domain; plastid envelope localization; paralogs on 7B)
  - Direction: Both downregulated
  - Mechanism: MscS-family mechanosensitive channels release osmolytes in response to membrane tension during osmotic stress. During imbibition, seeds undergo rapid water uptake creating osmotic stress. Downregulation could impair osmotic adjustment but also reduce osmolyte loss.
  - Evidence: [Speculative]
  - Germination link: Uncertain; depends on temporal requirements during imbibition
  - References: General MscS channel biology

- **Claim 14.3**: MFS sugar transporter downregulation may modulate sugar sensing and myo-inositol uptake.
  - Genes:
    - TraesCS4D02G263000 (MFS sugar transporter / myo-inositol transporter, 521 aa; 12 TM helices; 359 orthologues)
    - TraesCS5D02G114300 (MFS sugar transporter, 450-514 aa; 10 TM helices; 375 orthologues)
  - Direction: Both downregulated
  - Mechanism: MFS sugar transporters mediate sugar and myo-inositol uptake across membranes. Myo-inositol is a precursor for phytic acid (IP6) and cell signaling molecules (IP3). Downregulation could reduce myo-inositol transport, potentially affecting phytic acid metabolism and phosphorus mobilization from seed reserves.
  - Evidence: [Speculative]
  - Germination link: Possible effects on phosphorus mobilization and sugar sensing
  - References: General MFS transporter biology

---

## Theme 15: RNA Metabolism and mRNA Turnover

### Claims:

- **Claim 15.1**: ASCH domain RNA-binding protein downregulation may affect RNA metabolism during germination.
  - Genes: TraesCS4A02G232100 (ASCH domain protein, 385 aa; ASCH domain + PUA-like superfamily; 163 orthologues)
  - Direction: Downregulated
  - Mechanism: ASCH (ASC-1 Homology) domains bind RNA. PUA-like domains are associated with pseudouridine synthases and other RNA modification enzymes. Downregulation could affect post-transcriptional RNA processing.
  - Evidence: [Speculative]
  - Germination link: Uncertain
  - References: General ASCH domain biology

- **Claim 15.2**: RCD1/CNOT9 downregulation may affect mRNA catabolism and translational repression in P-bodies.
  - Genes: TraesCS5A02G423100 (Cell differentiation protein rcd1 / CNOT9 family, 396-400 aa; ARM-like fold + CNOT9/Rcd1 domain; 351 orthologues)
  - Direction: Downregulated
  - Mechanism: CNOT9 is a component of the CCR4-NOT deadenylase complex involved in mRNA catabolism and translational repression in P-bodies. Downregulation could stabilize certain mRNA populations during germination, potentially including germination-promoting stored mRNAs.
  - Evidence: [Speculative]
  - Germination link: Possible stabilization of stored germination-promoting mRNAs
  - References: General CCR4-NOT complex biology

---

## Theme 16: Additional Specialized Targets

### Claims:

- **Claim 16.1**: Cutin biosynthesis-related alpha/beta hydrolase downregulation could affect cuticle formation on emerging radicle.
  - Genes: TraesCS1D02G190800 (Alpha/beta hydrolase-1 / Bodyguard 3-related, 466 aa; AB hydrolase-1 domain; 205 orthologues)
  - Direction: Downregulated
  - Mechanism: Bodyguard-related proteins participate in cutin biosynthesis and cuticle formation. Downregulation could impair cuticle deposition on the emerging radicle, potentially affecting water relations.
  - Evidence: [Speculative]
  - Germination link: Uncertain; cuticle dispensable during very early germination
  - References: General cutin biosynthesis biology

- **Claim 16.2**: Assimilatory sulfite reductase downregulation may affect sulfur amino acid biosynthesis during germination.
  - Genes: TraesCS1B02G336300 (Assimilatory sulfite reductase [ferredoxin], 636 aa; 2 nitrite/sulfite reductase ferredoxin-like domains + 2 [4Fe-4S] clusters + siroheme)
  - Direction: Downregulated
  - Mechanism: Assimilatory sulfite reductase catalyzes the reduction of sulfite to sulfide in the chloroplast, a key step in assimilatory sulfate reduction. During germination, sulfur amino acids (methionine, cysteine) are primarily mobilized from seed storage proteins rather than synthesized de novo. Downregulation during the heterotrophic phase may be tolerable.
  - Evidence: [Inferred]
  - Germination link: Potentially neutral if sulfur demands met by storage protein mobilization
  - References: General sulfur assimilation biology

- **Claim 16.3**: GPI anchor biosynthesis (PIGA) downregulation may affect protein anchoring to plasma membranes.
  - Genes: TraesCS3A02G336700 (PIGA domain protein, 415 aa; PIGA + glycosyltransferase domains; 206 orthologues)
  - Direction: Downregulated
  - Mechanism: PIGA catalyzes the first step of GPI anchor biosynthesis, which is required for anchoring certain proteins to the plasma membrane. Some GPI-anchored proteins function in cell wall remodeling and signaling during germination.
  - Evidence: [Speculative]
  - Germination link: Uncertain
  - References: General GPI anchor biosynthesis biology

- **Claim 16.4**: BURP domain protein downregulation may affect developmental processes and stress responses.
  - Genes: TraesCS4D02G095300 (BURP domain protein, 625 aa; BURP domain + signal peptide; 371 orthologues)
  - Direction: Downregulated
  - Mechanism: BURP domain proteins include polygalacturonase-associated proteins, dehydration-responsive proteins, and development-related proteins. Downregulation could affect cell wall modification or stress responsiveness.
  - Evidence: [Speculative]
  - Germination link: Context-dependent; may reduce stress-responsive gene programs
  - References: General BURP domain biology

- **Claim 16.5**: Trypsin-like serine protease may function in protein mobilization during germination.
  - Genes: TraesCS5B02G289200 (Trypsin-like serine protease, 550-583 aa; 2 Trypsin_2 domains + Peptidase S1_PA)
  - Direction: Downregulated -- potentially detrimental for reserve mobilization
  - Mechanism: Serine proteases participate in protein mobilization from the endosperm. Downregulation could impair proteolytic processing of storage proteins. However, this protease may also have defense-related functions.
  - Evidence: [Speculative]
  - Germination link: Potentially detrimental if involved in storage protein mobilization; neutral if defense-related
  - References: General serine protease biology

- **Claim 16.6**: CYP450 hormone biosynthesis-related enzyme downregulation may affect hormone balance.
  - Genes: TraesCS5A02G037600 (Cytochrome P450, 509 aa; CYP450 domain + TM helix + heme/iron binding; 150 orthologues)
  - Direction: Downregulated
  - Mechanism: CYP450 enzymes participate in diverse hormone biosynthesis and secondary metabolite pathways. Without knowing the specific substrate, the effect is unpredictable. If involved in ABA biosynthesis, downregulation would be beneficial; if in GA biosynthesis, detrimental.
  - Evidence: [Speculative]
  - Germination link: Depends on substrate specificity
  - References: General CYP450 biology

- **Claim 16.7**: Peptidase S49 (signal peptide peptidase) downregulation may affect chloroplast thylakoid membrane proteolysis.
  - Genes: TraesCS6B02G319000 (Peptidase S49, 660 aa; 2 Peptidase S49 domains)
  - Direction: Downregulated
  - Mechanism: Signal peptide peptidases cleave signal peptides within the thylakoid membrane. Dispensable during the pre-photosynthetic germination phase.
  - Evidence: [Inferred]
  - Germination link: Likely neutral during dark germination
  - References: General signal peptide peptidase biology

- **Claim 16.8**: Calcineurin-like phosphoesterase downregulation may affect phosphate signaling.
  - Genes: TraesCS5B02G369300 (Calcineurin-like phosphoesterase, 1,022 aa; phosphoesterase domain + 9 TM helices; 195 orthologues)
  - Direction: Downregulated
  - Mechanism: Metal-dependent phosphoesterases participate in phosphate metabolism and signal transduction. The large size and 9 TM helices suggest a complex membrane-integral enzyme.
  - Evidence: [Speculative]
  - Germination link: Uncertain
  - References: General phosphoesterase biology

---

## Nontranslating CDS Targets (4 targets)

- **TraesCS5B02G439630** (#1): Chr 5B, 1,794 bp; no protein product; possible regulatory RNA or pseudogene
- **TraesCS7D02G087400** (#2): Chr 7D, 2,176 bp; no protein product; possible regulatory RNA or pseudogene
- **TraesCS5D02G375418** (#3): Chr 5D, 3,028 bp; no protein product; possible regulatory element
- **TraesCS5A02G365700** (#4): Chr 5A; originally annotated as "UDP-sulfoquinovose synthase, chloroplastic" but is actually nontranslating CDS; SQD1 annotation likely inherited from a neighboring gene

These nontranslating CDS targets may represent: (i) regulatory long non-coding RNAs (lncRNAs) that modulate gene expression; (ii) pseudogenes with residual regulatory function; (iii) unannotated small ORFs; or (iv) artifacts of gene model prediction. Their functional significance is unknown.

---

## Uncharacterized/Unknown Targets (8 targets)

- **TraesCS5B02G389900** (#12): DUF1677 domain protein, 130 aa; plant-specific domain of unknown function
- **TraesCS3D02G469000** (#23): Uncharacterized, 260 aa; coiled coil + disordered regions; low conservation (4 orthologues)
- **TraesCS7D02G281500** (#27): Uncharacterized transmembrane protein, 291 aa; 1 TM helix
- **TraesCS7D02G253300** (#48): Uncharacterized small protein, 155 aa
- **TraesCS3D02G204700** (#49): Uncharacterized, 212 aa; no InterPro domains
- **TraesCS4A02G108000** (#53): Uncharacterized but highly conserved, 533-535 aa; 238 orthologues, 79 paralogues (high conservation implies essential function)
- **TraesCS4B02G159300** (#70): Very small protein, 82 aa; may be a gene fragment
- **TraesCS6D02G213500** (#73): Uncharacterized, 272-287 aa; 134 orthologues (moderate conservation)
- **TraesCS4D02G127100** (#21): Uncharacterized but highly conserved, 482-661 aa; 354 orthologues (very high conservation suggests essential function)
- **TraesCS4B02G385200** (#58): Rice ortholog poorly characterized (Os03g0109400), 839 aa

---

## Top Targets (ranked)

| Rank | Gene ID | Annotation | Score | Pathway | Why Top |
|------|---------|------------|-------|---------|---------|
| 1 | TraesCS1A02G328000 | PARP (Poly[ADP-ribose] polymerase) | HIGHEST | DNA damage/energy | Conserves NAD+ and ATP; prevents stress-induced energy depletion; >10% biomass increase documented in PARP-deficient plants (De Block et al. 2005); most well-validated target |
| 2 | TraesCS7D02G384400 | Ser/Thr protein kinase (likely SnRK2) | HIGH | ABA signaling | Reduces ABA sensitivity; phenocopies after-ripening; directly accelerates dormancy-to-germination transition; wheat PKABA1 precedent |
| 3 | TraesCS2A02G071200 | Arginine decarboxylase (ADC) | HIGH | Polyamine/ABA crosstalk | Reduces putrescine/ABA axis; shifts polyamine ratio toward GA; redirects arginine to protein synthesis; increases SAM for ethylene |
| 4 | TraesCS5B02G275200 | NAC domain protein 38 | HIGH | Stress TF/dormancy | ABA-inducible stress TF; downregulation reduces dormancy maintenance and stress-responsive gene braking |
| 5 | TraesCS7A02G074600 | DDM1 (Decrease in DNA Methylation 1) | HIGH | Chromatin remodeling | Transient downregulation derepresses methylation-silenced germination genes; hexaploid genome with ~85% repeats particularly sensitive |
| 6 | TraesCS5A02G188400 + 5 others | F-box proteins (6 targets) | HIGH | Ubiquitin-proteasome/defense | Coordinate defense proteolysis reduction; reduce immune investment; redirect energy to growth |
| 7 | TraesCS5D02G521900 + TraesCS5B02G559900 | NB-LRR disease resistance (2 homeologs) | MEDIUM-HIGH | ETI/defense | Reduce energy-expensive ETI; B+D subgenome homeologs targeted coordinately |
| 8 | TraesCS6B02G167100 | Auxin response factor (ARF) | MEDIUM-HIGH | Auxin signaling | If repressor-class ARF, enhances auxin-responsive gene expression; promotes root/coleoptile growth |
| 9 | TraesCS2A02G386200 | TaYABBY3A | MEDIUM-HIGH | Developmental TF | Delays leaf polarity establishment; saves energy during dark germination |
| 10 | TraesCS3D02G394800 | BTB/POZ + TAZ domain protein 3 | MEDIUM | E3 ligase/hormone | CUL3-BTB stabilizes PP2Cs; reduces ABA sensitivity |
| 11 | TraesCS1D02G241800 + TraesCS3D02G228900 | SQD1 (UDP-sulfoquinovose synthase) (2 paralogs) | MEDIUM | Chloroplast lipid | Dispensable during dark germination; redirects UDP-glucose to glycolysis and sulfur to amino acids |
| 12 | TraesCS7D02G379600 + 4 others | LRR receptor-like kinases (5 targets) | MEDIUM | Immune receptors/PTI | PAMP perception receptors; downregulation reduces immune surveillance; broad pathogen sensing reduction |
| 13 | TraesCS4B02G205800 | sHSP/alpha-crystallin | MEDIUM | Heat shock/chaperone | Reduces stress-responsive chaperone expression; energy conservation during non-stress germination |
| 14 | TraesCS2A02G393400 | Gnk2-homologous antifungal protein | MEDIUM | Defense | Reduces antifungal compound production; defense-to-growth resource shift |
| 15 | TraesCS3A02G122200 | Bromodomain TF (GTE8 family) | MEDIUM | Chromatin/transcription | Reduces acetylated histone reading; may reduce defense/stress gene transcription |
| 16 | TraesCS7A02G398600 | CDC27/APC3 | LOW-MEDIUM | Cell cycle | Moderates premature cell division; prioritizes mobilization over proliferation |
| 17 | TraesCS6B02G296400 | Ubiquinol oxidase (AOX) | LOW | Alternative respiration | PARADOXICAL: AOX essential for ROS management; expected detrimental; may reflect fine-tuning |
| 18 | TraesCS5A02G360900 | BOP1 (ribosome biogenesis) | LOW | Translation | PARADOXICAL: Translation required for germination; stored ribosomes may buffer 0-24h |
| 19 | TraesCS2B02G505400 | Kinesin motor protein | LOW | Cytoskeleton | PARADOXICAL: Cell division essential; 155-member family provides redundancy |
| 20 | TraesCS1B02G356700 | Profilin | LOW | Actin dynamics | PARADOXICAL: Cell elongation requires profilin; dose-sensitive; both over- and under-expression impair growth |

---

## Proposed Primary MoA for Wheat

The primary mechanism of action for M-9 bacterial EPS-mediated germination improvement in wheat is a **multi-node, coordinated transcriptional reprogramming** involving three convergent strategies:

**Strategy 1 -- Energy Conservation (PARP + SQD1 + defense downshift):** PARP downregulation conserves NAD+ and ATP by preventing stress-induced energy depletion. SQD1 downregulation redirects UDP-glucose from sulfolipid biosynthesis toward glycolysis. Coordinated downregulation of 18 defense pathway genes (F-box proteins, LRR-RLKs, NB-LRRs, ABC transporters, antifungal proteins) dramatically reduces the ATP cost of immune surveillance and defense compound production. The net effect is a higher-energy cellular state favoring biosynthesis over defense.

**Strategy 2 -- ABA/Dormancy Brake Release (SnRK2 + ADC + NAC38 + BTB/POZ):** SnRK2 kinase downregulation directly reduces ABA signal transduction. ADC downregulation shifts the polyamine ratio from ABA-promoting putrescine toward GA-promoting spermidine/spermine. NAC38 downregulation reduces stress-transcriptional braking. BTB/POZ downregulation stabilizes PP2C phosphatases. Together, these converge on reducing ABA sensitivity and accelerating the dormancy-to-germination transition, phenocopying the natural after-ripening process.

**Strategy 3 -- Epigenetic Derepression (DDM1 + GTE8 + Homeobox-DDT):** Transient DDM1 downregulation causes partial demethylation that derepresses germination-promoting genes silenced during seed maturation. Bromodomain TF and Homeobox-DDT modulation further reshape the chromatin landscape.

**Predicted network output:** A "low-stress, high-energy, growth-permissive" cellular state that accelerates the dormancy-to-germination transition, improves reserve mobilization efficiency, and enhances radicle/coleoptile growth. The 4-8 hour imbibition treatment window ensures transient, non-heritable effects that fade as bacterial sRNAs are degraded.

**The wheat target list is unique** among crops analyzed in the dominance of the defense downshift theme (24% of all targets). This suggests the bacterial esRNAs may specifically suppress wheat immune recognition of bacterial-derived molecules in the EPS, facilitating beneficial interaction. This parallels the immune suppression strategy used by pathogenic fungi (Botrytis cinerea; Weiberg et al., Science 2013) but in a mutualistic context.

---

## Alternative Model: EPS Osmopriming

**What EPS alone explains:**

The bacterial EPS is a hygroscopic polysaccharide matrix that modifies water uptake kinetics during seed imbibition. The EPS creates a controlled hydration microenvironment that:

1. **Prevents imbibition damage** from excessively rapid water uptake, reducing membrane damage and cellular leakage
2. **Provides osmotic priming** that pre-activates metabolic processes during soaking, giving seeds a "head start" on germination when transferred to optimal conditions
3. **Contains MAMPs** (microbial-associated molecular patterns) that trigger mild, transient defense priming (hormesis), which paradoxically enhances stress tolerance
4. **Supplies trace nutrients** (minerals, amino acids) from the bacterial culture medium

Under this model, the RNA in the EPS is a passive bystander -- bacterial nucleic acids co-extracted with polysaccharides but biologically inert in the cross-kingdom context. The antisense alignments are coincidental sequence complementarity with no functional significance.

**Discriminating predictions for osmopriming model:**
- RNase pre-treatment of EPS should NOT abolish the germination improvement
- Purified polysaccharide fraction (RNA-depleted) should reproduce the effect fully
- No target-specific mRNA changes would be detected by qRT-PCR
- Other hygroscopic polymers (PEG, methylcellulose) at equivalent water potential should partially reproduce the effect
- Dose-response should correlate with EPS concentration, not RNA concentration
- Heat-denatured EPS (destroying RNA secondary structure but preserving polysaccharide) should retain activity

**Combined model note:** The two models are not mutually exclusive. A combined model where EPS provides the delivery matrix and physical priming while esRNAs provide sequence-specific gene regulation is biologically plausible and may best explain the observed phenotype.

---

## Hexaploid Buffering Analysis

### How Hexaploidy Affects Target Redundancy

The hexaploid wheat genome (AABBDD, ~17 Gb; IWGSC 2018) contains three subgenomic copies (homeologs) of most genes. This has profound implications for esRNA-mediated silencing:

**1. Built-in Safety Margin:**
For most targets in the 75-gene list, only ONE homeolog appears. This means the remaining A, B, or D copies are NOT targeted and can fully compensate. Even aggressive esRNA-mediated silencing of one homeolog would produce only a ~33% reduction in total gene product, creating moderate, non-lethal phenotypic effects -- ideal for a germination enhancement strategy.

**2. Confirmed Homeolog Pairs in Target List (amplified knockdown):**

| Group | Subgenome A | Subgenome B | Subgenome D | Function | Buffering Status |
|-------|-------------|-------------|-------------|----------|-----------------|
| Chr 2 ABC transporters | TraesCS2A02G056800 | TraesCS2B02G069000 | -- | ABCC/phytic acid transport | A + B targeted; D copy may compensate |
| Chr 6 LRR-RLKs | -- | TraesCS6B02G152900 | TraesCS6D02G116100 | Immune receptor kinase | B + D targeted; A copy may compensate |
| Chr 5 NB-LRR | -- | TraesCS5B02G559900 | TraesCS5D02G521900 | Disease resistance | B + D targeted; A copy may compensate |

Targeting multiple homeologs of the same gene amplifies the knockdown effect, potentially overcoming polyploid buffering. The coordinated targeting of both B- and D-subgenome NB-LRR copies on chromosome 5 is particularly noteworthy.

**3. Homeolog Expression Bias:**
Ramirez-Gonzalez et al. (Science 2018) demonstrated that ~30% of wheat homeolog triads show non-balanced expression, meaning compensation is NOT universal. Homeologs may be expressed at different levels, in different tissues, or at different developmental stages. esRNAs targeting the dominantly expressed homeolog would have disproportionate effects.

**4. Subgenome D Over-representation:**
The target list contains an unusually high number of chromosome 7D loci (7 targets: #2, #9, #10, #27, #35, #48, #66), suggesting possible D-subgenome sequence bias in esRNA targeting. This could relate to sequence divergence patterns between the D genome (contributed by Aegilops tauschii) and the A/B genomes.

**5. Design qRT-PCR with Homeolog Specificity:**
For experimental validation, primers must exploit 3' UTR SNPs to distinguish A, B, and D homeolog expression independently.

---

## Beneficial vs Detrimental Targets

### Targets Where Downregulation Is Predicted to Be BENEFICIAL for Germination

| Gene ID | Annotation | Benefit | Confidence |
|---------|------------|---------|------------|
| TraesCS1A02G328000 | PARP | Conserves NAD+/ATP; reduces oxidative damage | [Known] -- Highest confidence |
| TraesCS7D02G384400 | Ser/Thr kinase (likely SnRK2) | Reduces ABA sensitivity; mimics after-ripening | [Known/Inferred] |
| TraesCS2A02G071200 | ADC (arginine decarboxylase) | Shifts polyamine ratio; reduces ABA biosynthesis | [Known] -- Context-dependent |
| TraesCS5B02G275200 | NAC38 | Reduces stress/dormancy transcription | [Inferred] |
| TraesCS7A02G074600 | DDM1 | Derepresses methylation-silenced germination genes | [Inferred] |
| TraesCS5A02G188400 + 5 others | F-box proteins (6 targets) | Reduces defense proteolysis; energy reallocation | [Inferred] |
| TraesCS5D02G521900 + TraesCS5B02G559900 | NB-LRR (2 homeologs) | Reduces ETI energy cost | [Inferred] |
| TraesCS7D02G379600 + 4 others | LRR-RLKs (5 targets) | Reduces PTI surveillance energy | [Inferred] |
| TraesCS7B02G381000 + 2 others | ABC transporters (3 targets) | Reduces defense transport ATP cost | [Inferred] |
| TraesCS1D02G241800 + TraesCS3D02G228900 | SQD1 (2 paralogs) | Redirects UDP-glucose to glycolysis; dispensable in dark | [Known] |
| TraesCS3D02G394800 | BTB/POZ + TAZ | Stabilizes PP2Cs; reduces ABA sensitivity | [Inferred] |
| TraesCS2A02G393400 | Gnk2 antifungal | Reduces defense compound production | [Inferred] |
| TraesCS1D02G303100 | LURP1-related | Reduces immune response investment | [Inferred] |
| TraesCS4B02G205800 | sHSP/alpha-crystallin | Energy conservation during non-stress | [Inferred] |
| TraesCS6B02G319000 | Peptidase S49 | Thylakoid peptidase dispensable in dark | [Inferred] |

### Targets Where Downregulation Is CONTEXT-DEPENDENT

| Gene ID | Annotation | Context | Risk |
|---------|------------|---------|------|
| TraesCS2A02G071200 | ADC | Beneficial under non-stress; detrimental under osmotic stress (putrescine is protective) | Moderate |
| TraesCS3B02G123400 | PPR protein | Beneficial if chloroplast-targeted; detrimental if mitochondrial | High |
| TraesCS3B02G440800 | Mg transporter | Beneficial if chloroplast-targeted; detrimental if cytoplasmic | High |
| TraesCS6B02G167100 | ARF | Beneficial if repressor-class; detrimental if activator-class | Moderate |
| TraesCS2A02G386200 | TaYABBY3A | Beneficial during dark phase; potentially detrimental during de-etiolation | Low |

### Targets Where Downregulation Is Predicted to Be DETRIMENTAL

| Gene ID | Annotation | Why Detrimental | Confidence |
|---------|------------|-----------------|------------|
| TraesCS5A02G360900 | BOP1 (ribosome biogenesis) | Translation is rate-limiting in early germination; BOP1 essential for 60S subunit assembly; its silencing in tobacco repressed global translation | [Known] -- High confidence detrimental |
| TraesCS1B02G356700 | Profilin | Required for actin dynamics driving radicle elongation; dose-sensitive; both over- and under-expression impair growth | [Known] -- High confidence detrimental |
| TraesCS2B02G505400 | Kinesin motor protein | Required for cell division driving radicle emergence; but 155-member family provides some redundancy | [Known] -- Moderate confidence detrimental |
| TraesCS6B02G296400 | AOX (ubiquinol oxidase) | Essential for ROS management during germination metabolic burst; AOX mutants salt-hypersensitive; loss pushes ROS above oxidative window | [Known] -- High confidence detrimental |
| TraesCS7D02G101200 | Ent-kaurenoic acid oxidase (KAO) | GA biosynthesis enzyme; downregulation should impair GA-mediated germination | [Contradictory] |
| TraesCS7A02G398600 | CDC27/APC3 | Cell cycle essential for cell division during germination; but moderate reduction may be tolerable | [Moderate] detrimental |

---

## Key References

### From the PDF Report (Bibliography, 53 references):

1. Alcazar R, Altabella T, Marco F, Bortolotti C, Reymond M, Koncz C, Carrasco P, Tiburcio AF. Polyamines: molecules with regulatory functions in plant abiotic stress tolerance. *Planta*. 2010;231(6):1237-1249.
2. Ahn CS, Cho HK, Lee DH, Sim HJ, Kim SG, Pai HS. Functional characterization of the ribosome biogenesis factors PES, BOP1, and WDR12 (PeBoW), and mechanisms of defective cell growth and proliferation caused by PeBoW deficiency in Arabidopsis. *Journal of Experimental Botany*. 2016;67(17):5217-5232.
3. Bai B, Novak O, Ljung K, Hanson J, Bentsink L. Lost in Translation: Physiological Roles of Stored mRNAs in Seed Germination. *Plants*. 2020;9(3):347.
4. Bailly C, El-Maarouf-Bouteau H, Corbineau F. From intracellular signaling networks to cell death: the dual role of reactive oxygen species in seed physiology. *Comptes Rendus Biologies*. 2008;331(10):806-814.
5. Barkan A, Small I. Pentatricopeptide repeat proteins in plants. *Annual Review of Plant Biology*. 2014;65:415-442.
6. Bassie L, Noury M, Lepri O, Lahaye T, Christou P, Capell T. Transgenic wheat plants expressing an oat arginine decarboxylase cDNA exhibit increases in polyamine content in vegetative tissue and seeds. *Molecular Breeding*. 2008;21:187-200.
7. Basu A, Prasad P, Das SN, Kalam S, Sayyed RZ, Reddy MS, El Enshasy H. Plant growth promoting rhizobacteria (PGPR) as green bioinoculants: recent developments, constraints, and prospects. *Sustainability*. 2021;13(3):1140.
8. Buck AH, Coakley G, Simbari F, McSorley HJ, Quintana JF, Le Bihan T, Kumar S, Abreu-Goodger C, Lear M, Harcus Y, Ceroni A, Babayan SA, Blaxter M, Ivens A, Maizels RM. Exosomes secreted by nematode parasites transfer small RNAs to mammalian cells and modulate innate immunity. *Nature Communications*. 2014;5:5488.
9. Cai Q, Qiao L, Wang M, He B, Lin FM, Palmquist J, Huang SD, Jin H. Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. *Science*. 2018;360(6393):1126-1129.
10. De Block M, Verduyn C, De Brouwer D, Cornelissen M. Poly(ADP-ribose) polymerase in plants affects energy homeostasis, cell death and stress tolerance. *Plant Journal*. 2005;41(1):95-106.
11. Ebeed HT, Hassan NM, Khodary SEA, Habib SA. Genome-wide analysis of polyamine biosynthesis genes in wheat reveals gene expression specificity and involvement of STRE and MYB-elements in regulating polyamines under drought. *BMC Genomics*. 2022;23:734.
12. Essigmann B, Guler S, Narang RA, Linke D, Benning C. Phosphate availability affects the thylakoid lipid composition and the expression of SQD1, a gene required for sulfolipid biosynthesis in Arabidopsis thaliana. *PNAS*. 1998;95(4):1950-1955.
13. Fu X, Richards DE, Ait-Ali T, Hynes LW, Ougham H, Peng J, Harberd NP. Gibberellin-mediated proteasome-dependent degradation of the barley DELLA protein SLN1 repressor. *Plant Cell*. 2002;14(12):3191-3200.
14. Gubler F, Kalla R, Roberts JK, Jacobsen JV. Gibberellin-regulated expression of a myb gene in barley aleurone cells: evidence for Myb transactivation of a high-pI alpha-amylase gene promoter. *Plant Cell*. 1995;7(11):1879-1891.
15. Gubler F, Chandler PM, White RG, Llewellyn DJ, Jacobsen JV. Gibberellin signaling in barley aleurone cells. Control of SLN1 and GAMYB expression. *Plant Physiology*. 2002;129(1):191-200.
16. Han Y, Liu S, Wei Y, Zhang X, Wang Y, Shi G, Li J, Liu D, Zhang A. Functional analysis of a wheat class III peroxidase gene, TaPer12-3A, in seed dormancy and germination. *BMC Plant Biology*. 2024;24:41.
17. Harris D, Joshi A, Khan PA, Gothkar P, Sodhi PS. On-farm seed priming in semi-arid agriculture: development and evaluation in maize, rice and chickpea in India using participatory methods. *Experimental Agriculture*. 1999;35(1):15-29.
18. He B, Cai Q, Qiao L, Huang CY, Wang S, Miao W, Ha T, Wang Y, Jin H. RNA-binding proteins contribute to small RNA loading in plant extracellular vesicles. *Nature Plants*. 2021;7(3):342-352.
19. Hu Z, Parekh U, Maruta N, Trusov Y, Botella JR. Cross-kingdom RNAi of pathogen effectors leads to quantitative adult plant resistance in wheat. *Frontiers in Plant Science*. 2020;11:253.
20. International Wheat Genome Sequencing Consortium (IWGSC). Shifting the limits in wheat research and breeding using a fully annotated reference genome. *Science*. 2018;361(6403):eaar7191.
21. Koch A, Biedenkopf D, Furch A, Weber L, Rossbach O, Abdellatef E, Linicus L, Johannsmeier J, Jelonek L, Goesmann A, Cardoza V, McMillan J, Mentzel T, Kogel KH. An RNAi-based control of Fusarium graminearum infections through spraying of long dsRNAs involves a plant passage and is controlled by the fungal silencing machinery. *PLoS Pathogens*. 2016;12(10):e1005901.
22. Liu S, Sehgal SK, Li J, Lin M, Trick HN, Yu J, Gill BS, Bai G. Cloning and characterization of a critical regulator for preharvest sprouting in wheat. *Genetics*. 2013;195(1):263-272.
23. Luo H, Wang Q, Guo Y, Li F, Li Z, Zhang Y. Gibberellic-acid-dependent expression of alpha-amylase in wheat aleurone cells is mediated by target of rapamycin (TOR) signaling. *Plant Signaling & Behavior*. 2023;18(1).
24. Ma W, Zhang Y, Li W, Du B, Liu J, Wang Z, Li J. Uncovering the role of wheat magnesium transporter family genes in abiotic responses. *Frontiers in Plant Science*. 2023;14:1078299.
25. Mahmood A, Turgay OC, Farooq M, Hayat R. Seed biopriming with plant growth promoting rhizobacteria: a review. *FEMS Microbiology Ecology*. 2016;92(8):fiw112.
26. Mulichak AM, Theisen MJ, Essigmann B, Benning C, Garavito RM. Crystal structure of SQD1, an enzyme involved in the biosynthesis of the plant sulfolipid headgroup donor UDP-sulfoquinovose. *PNAS*. 1999;96(23):13097-13102.
27. Nakamura S, Abe F, Kawahigashi H, Nakazono K, Tagiri A, Matsumoto T, Utsugi T, Ogawa T, Handa H, Ishida H, Mori M, Kawaura K, Ogihara Y, Miura H. A wheat homolog of MOTHER OF FT AND TFL1 acts in the regulation of germination. *Plant Cell*. 2011;23(9):3215-3229.
28. Nowara D, Gay A, Lacomme C, Shaw J, Ridout C, Douchkov D, Hensel G, Kumlehn J, Schweizer P. HIGS: host-induced gene silencing in the obligate biotrophic fungal pathogen Blumeria graminis. *Plant Cell*. 2010;22(9):3130-3141.
29. Pfeifer M, Kugler KG, Sandve SR, Zhan B, Rudi H, Hvidsten TR, Mayer KF, Olsen OA. Genome interplay in the grain transcriptome of hexaploid bread wheat. *Science*. 2014;345(6194):1250091.
30. Pieruzzi FP, Dias LLC, Balbuena TS, Santa-Catarina C, dos Santos ALW, Floh EIS. Polyamines, IAA and ABA during germination in two recalcitrant seeds: Araucaria angustifolia (Gymnosperm) and Ocotea odorifera (Angiosperm). *Annals of Botany*. 2011;108(4):693-701.
31. Qiao L, Zhang W, Li X, Zhang L, Zhang X, Li X, Guo H, Ren Y, Zheng J, Chang Z. Characterization and expression patterns of auxin response factors in wheat. *Frontiers in Plant Science*. 2018;9:1395.
32. Ramirez-Gonzalez RH, Borrill P, Lang D, Harrington SA, Brinton J, Venturini L, Davey M, Jacobs J, van Ex F, Pasha A, et al. The transcriptional landscape of polyploid wheat. *Science*. 2018;361(6403):eaar6089.
33. Rodriguez MV, Barrero JM, Corbineau F, Gubler F, Benech-Arnold RL. Dormancy in cereals (not too much, not so little): about the mechanisms behind this trait. *Seed Science Research*. 2015;25(2):99-119.
34. Saha B, Borovskii G, Panda SK. Alternative oxidase and plant stress tolerance. *Plant Signaling & Behavior*. 2016;11(12):e1256530.
35. Schulz P, Neukermans J, Van der Kelen K, Muhlenbock P, Van Breusegem F, Noctor G, Teige M, Metzlaff M, Hannah MA. Chemical PARP inhibition enhances growth of Arabidopsis and reduces anthocyanin accumulation and the activation of stress protective mechanisms. *PLoS ONE*. 2012;7(5):e37287.
36. Scofield SR, Huang L, Brandt AS, Gill BS. Development of a virus-induced gene silencing system for hexaploid wheat and its use in functional analysis: a new tool for wheat genomics. *Plant Physiology*. 2005;138(4):2165-2173.
37. Shahid S, Kim G, Johnson NR, Wafula E, Wang F, Coruh C, Bernal-Galeano V, Phifer T, dePamphilis CW, Westwood JH, Axtell MJ. MicroRNAs from the parasitic plant Cuscuta campestris target host messenger RNAs. *Nature*. 2018;553(7686):82-85.
38. Shorinola O, Bird N, Simmonds J, Berry S, Henriksson T, Jack P, Werner P, Cornille A, Haberer G, Mayer KFX, Uauy C. The wheat Phs-A1 pre-harvest sprouting resistance locus delays the rate of seed dormancy loss and maps 0.3 cM distal to the PM19 genes in UK germplasm. *Journal of Experimental Botany*. 2017;68(15):4424-4438.
39. Torada A, Koike M, Ogawa T, Takenouchi Y, Tadamura K, Wu J, Matsumoto T, Kawaura K, Ogihara Y. A causal gene for seed dormancy on wheat chromosome 4A encodes a MAP kinase kinase. *Current Biology*. 2016;26(6):782-787.
40. Tuttle KM, Martinez SA, Schramm EC, Takebayashi Y, Seo M, Steber CM. Genetic variation of seed dormancy in wheat (Triticum aestivum L.) is mediated by transcriptional regulation of abscisic acid metabolism and signaling. *Plant Cell & Environment*. 2022;45(12):3621-3635.
41. Vanderauwera S, De Block M, Van de Steene N, van de Cotte B, Metzlaff M, Van Breusegem F. Silencing of poly(ADP-ribose) polymerase in plants alters abiotic stress signal transduction. *PNAS*. 2007;104(38):15150-15155.
42. Vanlerberghe GC. Alternative oxidase: a mitochondrial respiratory pathway to maintain metabolic and signaling homeostasis during abiotic and biotic stress in plants. *International Journal of Molecular Sciences*. 2013;14(4):6805-6847.
43. Wang M, Weiberg A, Lin FM, Thomma BP, Huang HD, Jin H. Bidirectional cross-kingdom RNAi and fungal uptake of external RNAs confer plant protection. *Nature Plants*. 2016;2:16151.
44. Wang X, Wang H, Liu S, Ferjani A, Li J, Yan J, Yang X, Qin F. Genome-wide and evolutionary analysis of the class III peroxidase gene family in wheat and Aegilops tauschii reveals that some members are involved in stress responses. *BMC Genomics*. 2019;20:666.
45. Wang Y, Zhang H, Liu J, Hou X, Zhang Y, Fan S, Li X, Gao F, Li X. Genome-wide identification and expression analysis of the kinesin gene superfamily suggests roles in response to abiotic stress and fertility of wheat. *BMC Genomics*. 2024;25:1156.
46. Weiberg A, Wang M, Lin FM, Zhao H, Zhang Z, Kaloshian I, Huang HD, Jin H. Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. *Science*. 2013;342(6154):118-123.
47. Xia H, Chen L, Wang F, Li D. Genome-wide analysis, expansion and expression of the NAC family under drought and heat stresses in bread wheat (T. aestivum L.). *PLoS ONE*. 2019;14(2):e0213390.
48. Yu B, Xu C, Benning C. Arabidopsis disrupted in SQD2 encoding sulfolipid synthase is impaired in phosphate-limited growth. *PNAS*. 2002;99(8):5732-5737.
49. Yu W, Bhatt H, Li Y, Jha S, Rao S, Guo J. Wheat PP2C-a10 regulates seed germination and drought tolerance in transgenic Arabidopsis. *Plant Cell Reports*. 2020;39(5):635-651.
50. Yuan C, Li C, Yan L, Jackson AO, Liu Z, Han C, Yu J, Li D. A high throughput barley stripe mosaic virus vector for virus induced gene silencing in monocots and dicots. *PLoS ONE*. 2011;6(10):e26468.
51. Zhang T, Zhao YL, Zhao JH, Wang S, Jin Y, Chen ZQ, Fang YY, Hua CL, Ding SW, Guo HS. Cotton plants export microRNAs to inhibit virulence gene expression in a fungal pathogen. *Nature Plants*. 2016;2:16153.
52. Zhao SP, Lu D, Yu TF, Ji YJ, Zheng WJ, Zhang SX, Chai SC, Chen ZY, Cui XY. Genome-wide analysis of the YABBY family in soybean and functional identification of GmYABBY10 involvement in high salt and drought stresses. *Plant Physiology and Biochemistry*. 2017;119:132-146.
53. Zhao Y, Li J, Liu H, Xi Y, Xue M, Liu W, Zhuang Z. Identification and expression profiles of the YABBY transcription factors in wheat. *PeerJ*. 2022;10:e12855.

### From the Germination Biology Report (Additional References):

54. Barrero JM, Millar AA, Griffiths J, Czechowski T, Scheible WR, Udvardi M, Reid JB, Ross JJ, Jacobsen JV, Gubler F. Gene expression profiling identifies two regulatory genes controlling dormancy and ABA sensitivity in Arabidopsis seeds. *Plant Journal*. 2010;61(4):611-622.
55. Barrero JM, Cavanagh C, Verbyla KL, et al. Transcriptomic analysis of wheat near-isogenic lines identifies PM19-A1 and A2 as candidates for a major dormancy QTL. *Genome Biology*. 2015;16:93.
56. Bao CC, et al. Profilin review. *Frontiers in Plant Science*. 2015.
57. Bouchereau A, et al. ADC and osmotic stress. *Journal of Plant Physiology*. 1999.
58. Chen L, et al. PPR protein classification. *Frontiers in Plant Science*. 2021.
59. Cho JI, et al. Sugar sensing. *Trends in Plant Science*. 2006.
60. Fan T, et al. Profilin 3 overexpression. *Plant Cell Reports*. 2013.
61. Gebert M, et al. Mg2+ transport. *New Phytologist*. 2009.
62. Granot D, et al. Hexokinase signaling. *BMC Plant Biology*. 2013.
63. Ishibashi Y, et al. ABA-ROS interrelationship in barley dormancy. *Frontiers in Plant Science*. 2017.
64. Jeddeloh JA, et al. DDM1 and DNA methylation maintenance. *Nature Genetics*. 1999.
65. Kaneko M, et al. GAMYB loss-of-function in rice. *Plant Cell*. 2004.
66. Li L, et al. TaPP2C-a5 alternative splicing. *Journal of Advanced Research*. 2025.
67. Li LG, et al. Mg2+ transport. *Plant and Cell Physiology*. 2016.
68. Mares DJ, Mrva K. LMA in wheat. *Planta*. 2022.
69. McKibbin RS, et al. TaVP1 in wheat dormancy. *Plant Molecular Biology*. 2002.
70. Nakamura S, Toyama T. *Cereal Chemistry*. 2001.
71. Ren R, et al. PPR proteins in plants. *Plant Communications*. 2025.
72. Rissel D, Heym PP, Peiter E. PARP assay. *Analytical Biochemistry*. 2017.
73. Saha B, Borovskii G, Panda SK. AOX and stress tolerance. *Journal of Plant Physiology*. 2015.
74. Sanda S, et al. SQD1 biochemistry. *Journal of Biological Chemistry*. 2001.
75. Shorinola O, et al. Gene pyramiding for PHS. *Molecular Breeding*. 2022.
76. Sinska I, Lewandowska U. ADC and seed viability. *Plant Growth Regulation*. 1991.
77. Smeekens S. Sugar sensing. *Annual Review of Plant Biology*. 2000.
78. Son S, et al. ABA and wheat dormancy. *Plant Cell & Environment*. 2016.
79. Vernoux T, et al. ARF-Aux/IAA module. *Molecular Cell*. 2011.
80. Ye N, et al. ROS in seed dormancy and germination. *Frontiers in Plant Science*. 2020.
81. Zheng et al. AOX2 and germination under salt stress. *Environmental and Experimental Botany*. 2024.
82. Andriotis VM, et al. HXK and metabolic intermediates. *bioRxiv*. 2019.
83. Bouzroud S, et al. ARF family survey. *South African Journal of Botany*. 2020.

---

## Annotation Corrections Summary

| # | TraesCS ID | Original Annotation | Corrected Annotation | Severity | Evidence |
|---|-----------|---------------------|---------------------|----------|---------|
| 1 | TraesCS5A02G188400 | Auxin response factor (ARF) | F-box domain protein (kelch beta-propeller) | HIGH | UniProt A0A3B6KHS1; InterPro F-box + kelch domains |
| 2 | TraesCSU02G067600 | Kinesin-like protein | F-box/LRR-repeat protein | HIGH | UniProt A0A3B6UAE2; F-box + LRR domains |
| 3 | TraesCS1D02G241800 | Arginine decarboxylase | UDP-sulfoquinovose synthase (SQD1) | HIGH | Arabidopsis ortholog AT4G33030 = SQD1 |
| 4 | TraesCS5A02G360900 | BTB/POZ + TAZ domain protein 3 | Ribosome biogenesis protein BOP1 | MODERATE | UniProt A0A1D5YQ88; EnsemblPlants annotation |
| 5 | TraesCS7D02G219500 | BOP1 ribosome biogenesis | PGG domain transmembrane protein (17 TM helices) | MODERATE | UniProt A0A3B6THH2; 5 PGG domains |
| V | TraesCS2A02G386200 | YABBY TF (zinc finger + HLH) | VERIFIED CORRECT: TaYABBY3A | NONE | Zhao et al., PeerJ 2022 |
| 6 | TraesCS5A02G365700 | SQD1, chloroplastic | Nontranslating CDS (no protein product) | MODERATE | EnsemblPlants classification |

**Correct assignments:**
- Real ARF: TraesCS6B02G167100 (927 aa; B3 + Auxin_resp + AUX/IAA domains)
- Real kinesin: TraesCS2B02G505400 (785 aa; kinesin motor domain)
- Real ADC: TraesCS2A02G071200 (625 aa; pyridoxal phosphate-dependent decarboxylase)
- Real BOP1: TraesCS5A02G360900 (694 aa; WD40 repeats)
- Real BTB/POZ: TraesCS3D02G394800 (250 aa; BTB/POZ + TAZ domains)

---

## Complete Target Inventory (All 75 targets)

| # | TraesCS ID | Chr | Corrected Annotation | Category |
|---|-----------|-----|---------------------|----------|
| 1 | TraesCS5B02G439630 | 5B | Nontranslating CDS | Unknown |
| 2 | TraesCS7D02G087400 | 7D | Nontranslating CDS | Unknown |
| 3 | TraesCS5D02G375418 | 5D | Nontranslating CDS | Unknown |
| 4 | TraesCS5A02G365700 | 5A | Nontranslating CDS (NOT SQD1) | Unknown |
| 5 | TraesCS1D02G241800 | 1D | SQD1 (NOT Arginine decarboxylase) | Chloroplast lipid |
| 6 | TraesCS2A02G071200 | 2A | Arginine decarboxylase (ADC) | Polyamine metabolism |
| 7 | TraesCS4A02G232100 | 4A | ASCH domain RNA-binding protein | RNA metabolism |
| 8 | TraesCS3D02G228900 | 3D | SQD1-related enzyme | Chloroplast lipid |
| 9 | TraesCS7D02G384400 | 7D | Ser/Thr protein kinase (likely SnRK2) | ABA signaling |
| 10 | TraesCS7D02G379600 | 7D | Lectin receptor kinase | Immunity/PTI |
| 11 | TraesCS3D02G378700 | 3D | SHMT (serine hydroxymethyltransferase) | One-carbon metabolism |
| 12 | TraesCS5B02G389900 | 5B | DUF1677 domain protein | Unknown |
| 13 | TraesCS5A02G188400 | 5A | F-box protein (NOT ARF) | Ubiquitin-proteasome |
| 14 | TraesCS6B02G167100 | 6B | Auxin response factor (ARF) | Auxin signaling |
| 15 | TraesCS5D02G521900 | 5D | NB-LRR disease resistance | Immunity/ETI |
| 16 | TraesCS3B02G440800 | 3B | Magnesium transporter (CorA-type) | Ion transport |
| 17 | TraesCSU02G067600 | Un | F-box/LRR protein (NOT Kinesin) | Ubiquitin-proteasome |
| 18 | TraesCS2B02G505400 | 2B | Kinesin motor protein | Cytoskeleton |
| 19 | TraesCS5A02G170400 | 5A | Uncharacterized F-box protein | Ubiquitin-proteasome |
| 20 | TraesCS6A02G040900 | 6A | F-box protein | Ubiquitin-proteasome |
| 21 | TraesCS4D02G127100 | 4D | Uncharacterized (highly conserved) | Unknown |
| 22 | TraesCS4A02G289700 | 4A | Ankyrin/TPR Cul2-RING E3 ligase | Ubiquitin-proteasome |
| 23 | TraesCS3D02G469000 | 3D | Uncharacterized (coiled-coil) | Unknown |
| 24 | TraesCS3B02G123400 | 3B | PPR protein (organellar RNA) | Organelle gene expression |
| 25 | TraesCS2A02G124800 | 2A | Homeobox-DDT domain protein | Chromatin/transcription |
| 26 | TraesCS2A02G393400 | 2A | Gnk2-homologous antifungal protein | Defense |
| 27 | TraesCS7D02G281500 | 7D | Uncharacterized transmembrane protein | Unknown |
| 28 | TraesCS7A02G074600 | 7A | DDM1 (DNA methylation maintenance) | Chromatin remodeling |
| 29 | TraesCS3B02G587600 | 3B | Uncharacterized (large, TE-related?) | Unknown |
| 30 | TraesCS7A02G398600 | 7A | CDC27/APC3 (cell cycle) | Cell cycle |
| 31 | TraesCS7B02G381000 | 7B | ABC transporter ABCG/PDR (defense) | Defense transport |
| 32 | TraesCS3A02G336700 | 3A | PIGA (GPI anchor biosynthesis) | Membrane anchoring |
| 33 | TraesCS2D02G520600 | 2D | F-box with kelch repeats | Ubiquitin-proteasome |
| 34 | TraesCS2A02G439500 | 2A | GH17 beta-glucanase | Cell wall/defense |
| 35 | TraesCS7D02G101200 | 7D | Ent-kaurenoic acid oxidase (KAO) | GA biosynthesis |
| 36 | TraesCS7B02G381200 | 7B | Mechanosensitive ion channel (MscS) | Osmotic sensing |
| 37 | TraesCS5D02G095300 | 5D | Malectin-LRR receptor kinase | Immunity/PTI |
| 38 | TraesCS4D02G095300 | 4D | BURP domain protein | Development/stress |
| 39 | TraesCS5A02G037600 | 5A | Cytochrome P450 (hormone-related) | Hormone biosynthesis |
| 40 | TraesCS2B02G069000 | 2B | ABCC13/MRP (phytic acid transport) | Transport |
| 41 | TraesCS2A02G056800 | 2A | ABCC conjugate transporter | Transport/detox |
| 42 | TraesCS1D02G190800 | 1D | Alpha/beta hydrolase (cutin-related) | Cuticle biosynthesis |
| 43 | TraesCS5B02G289200 | 5B | Trypsin-like serine protease | Proteolysis |
| 44 | TraesCS3B02G442800 | 3B | DUF506/PDDEXK nuclease-like | Nuclease activity |
| 45 | TraesCS7B02G358900 | 7B | Mechanosensitive ion channel (MscS) | Osmotic sensing |
| 46 | TraesCS5A02G429600 | 5A | GH17 beta-glucanase | Cell wall/defense |
| 47 | TraesCS2A02G386200 | 2A | TaYABBY3A (VERIFIED) | Developmental TF |
| 48 | TraesCS7D02G253300 | 7D | Uncharacterized small protein | Unknown |
| 49 | TraesCS3D02G204700 | 3D | Uncharacterized protein | Unknown |
| 50 | TraesCS6B02G109500 | 6B | mTERF domain protein | Organelle transcription |
| 51 | TraesCS4D02G117200 | 4D | F-box/LRR with FBD domain | Ubiquitin-proteasome |
| 52 | TraesCS5A02G423100 | 5A | RCD1/CNOT9 (mRNA turnover) | RNA metabolism |
| 53 | TraesCS4A02G108000 | 4A | Uncharacterized (highly conserved) | Unknown |
| 54 | TraesCS1A02G328000 | 1A | PARP (Poly[ADP-ribose] polymerase) | DNA repair/energy |
| 55 | TraesCS4B02G205800 | 4B | sHSP/alpha-crystallin chaperone | Stress response |
| 56 | TraesCS1B02G356700 | 1B | Profilin | Actin dynamics |
| 57 | TraesCS6D02G116100 | 6D | LRR receptor-like kinase | Immunity/PTI |
| 58 | TraesCS4B02G385200 | 4B | Uncharacterized (rice Os03g0109400) | Unknown |
| 59 | TraesCS6B02G152900 | 6B | LRR receptor-like kinase | Immunity/PTI |
| 60 | TraesCS3A02G122200 | 3A | Bromodomain TF (GTE8 family) | Chromatin/transcription |
| 61 | TraesCS5B02G275200 | 5B | NAC domain protein 38 | Stress TF/dormancy |
| 62 | TraesCS6B02G296400 | 6B | Ubiquinol oxidase (AOX) | Alternative respiration |
| 63 | TraesCS5A02G360900 | 5A | BOP1 ribosome biogenesis (NOT BTB/POZ) | Translation |
| 64 | TraesCS3D02G394800 | 3D | BTB/POZ + TAZ domain protein 3 | E3 ligase/signaling |
| 65 | TraesCS4D02G263000 | 4D | MFS sugar/myo-inositol transporter | Sugar transport |
| 66 | TraesCS7D02G219500 | 7D | PGG domain transmembrane protein (NOT BOP1) | Unknown |
| 67 | TraesCS1D02G303100 | 1D | LURP-one-related 8 (defense) | Defense |
| 68 | TraesCS5B02G369300 | 5B | Calcineurin-like phosphoesterase | Phosphatase |
| 69 | TraesCS5D02G114300 | 5D | MFS sugar transporter | Sugar transport |
| 70 | TraesCS4B02G159300 | 4B | Uncharacterized small protein (82 aa) | Unknown |
| 71 | TraesCS1B02G336300 | 1B | Assimilatory sulfite reductase | Sulfur metabolism |
| 72 | TraesCS6B02G319000 | 6B | Peptidase S49 (signal peptide proc.) | Thylakoid proteolysis |
| 73 | TraesCS6D02G213500 | 6D | Uncharacterized protein | Unknown |
| 74 | TraesCS5B02G502400 | 5B | L-type lectin receptor kinase | Immunity |
| 75 | TraesCS5B02G559900 | 5B | NB-LRR disease resistance | Immunity/ETI |
