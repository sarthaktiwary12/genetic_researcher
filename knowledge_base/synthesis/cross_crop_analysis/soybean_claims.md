# SOYBEAN (Glycine max) -- Mechanistic Claims Extraction

## Overview
- **Organism**: Glycine max (soybean)
- **Genome**: ~1.1 Gb, paleopolyploid (two whole-genome duplication events), ~75% genes in multiple copies
- **Reference assembly**: Williams 82 (Wm82.a2.v1 / Glyma 4.0); Schmutz et al. (2010) Nature 463:178-183
- **Treatment**: M-9 bacterial EPS (extracellular polymeric substance) solution, seed soaking during Phase I imbibition (0-6 hours)
- **Phenotype**: Germination rate increase, seedling vigor increase, early seedling growth improvement
- **Total predicted targets**: 23 original entries --> 18 unique GLYMA gene loci after deduplication and KRH-to-GLYMA resolution
- **Evidence level**: Gene-level (bioinformatic sRNA-mRNA complementarity prediction + literature-based functional annotation)
- **Unique features**: Paleopolyploid legume with duplicated RNAi machinery, nitrogen fixation capability, rhizobial symbiosis, experimentally validated bacteria-to-soybean sRNA transfer precedent (Ren et al. 2019, Science), 319 NBS-LRR disease resistance genes, 32 invertase genes, isoflavonoid defense pathway, unique sorbitol pathway in germinating axes

---

## Theme 1: Hormone-Sugar Metabolic Priming

**Central thesis**: The bacterial exRNAs simultaneously shift the ABA/GA ratio toward germination AND flood the embryonic axis with hexose sugars, creating a metabolically primed state that accelerates germination.

### Claims:

- **Claim 1.1**: Downregulation of the invertase/PME inhibitor (GLYMA_05G068700) derepresses cell wall invertase (CWI) activity, increasing hexose availability in germinating embryonic axes
  - **Genes**: GLYMA_05G068700 (KRH57561) -- Invertase/pectin methylesterase inhibitor superfamily protein
  - **Arabidopsis homolog**: AT5G46940
  - **Key domains**: Inv/PME inhibitor (PF04043)
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: The invertase inhibitor post-translationally suppresses CWI activity. Silencing the inhibitor derepresses CWI, which cleaves sucrose into glucose and fructose in the apoplast. In soybean, RNAi suppression of the orthologous GmCIF1 produced marked elevation of CWI activity, increased seed weight, and higher accumulations of hexoses, starch, and protein (Tang et al. 2017). In Arabidopsis, loss-of-function of AtCIF1 accelerated seed germination independently of exogenous ABA, with drastically increased CWI activity and boosted hexose levels by 24 hours post-imbibition (Su et al. 2016). In tomato, silencing INVINH1 increased seed weight and fruit hexose levels (Jin et al. 2009). Sugar metabolism in germinating soybean axes involves a unique sorbitol pathway where hexose accumulation correlates with invertase activity (Kuo et al. 1990). The soybean genome contains 32 putative invertase genes across three classes: cell wall invertases, vacuolar invertases, and cytoplasmic/alkaline/neutral invertases (Ni et al. 2018).
  - **Evidence**: [KNOWN] -- Score 10/10 -- Strongest cross-species validation of any target. Direct experimental support from soybean (Tang et al. 2017), Arabidopsis (Su et al. 2016), and tomato (Jin et al. 2009) loss-of-function studies.
  - **Germination link**: Increased hexose sugars fuel metabolic activation of the embryonic axis during Phase II; elevated CWI activity directly correlates with germination acceleration; hexose signaling via HXK-dependent pathways promotes growth programs
  - **Predicted molecular signature**: Elevated CWI activity in treated vs. control seeds at 12-24 hours post-imbibition; increased hexose (glucose + fructose) in embryonic axes
  - **References**: Tang et al. (2017) J Exp Bot 68:469-482 [DOI: 10.1093/jxb/erw425]; Su et al. (2016) Plant Mol Biol 90:137-155 [DOI: 10.1007/s11103-015-0402-2]; Jin et al. (2009) Plant Cell 21:2072-2089 [DOI: 10.1105/tpc.108.063719]; Kuo et al. (1990) Plant Physiol 93:1514-1520 [DOI: 10.1104/pp.93.4.1514]; Ni et al. (2018) Int J Mol Sci 19:2395 [DOI: 10.3390/ijms19082395]

- **Claim 1.2**: Downregulation of Phospholipase D beta 1 (GLYMA_01G215100) reduces phosphatidic acid-mediated ABA signal amplification, lowering the ABA/GA ratio
  - **Genes**: GLYMA_01G215100 -- Phospholipase D beta 1 (PLDbeta1)
  - **Arabidopsis homolog**: AT2G42010
  - **Key domains**: C2 domain; PLD active site; PLD C-terminal domain
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: PLDbeta1 generates phosphatidic acid (PA), a key lipid second messenger in ABA signaling and stress responses. In Arabidopsis, PA produced by PLDbeta1 promotes ABA-mediated stomatal closure and enhances drought tolerance. PA also activates NADPH oxidase, so reduced PA could modulate the ROS burst during imbibition. Downregulating PLDbeta1 would reduce PA-mediated ABA signal amplification, effectively lowering the ABA/GA ratio and favoring germination. Quantitative measurements in soybean show dry seeds contain ~32 ng/g ABA with undetectably low GA; after 6 hours imbibition, GA1 and GA4 increase to 0.6 and 0.4 ng/g while ABA drops to ~14 ng/g (Shuai et al. 2017; Gazara et al. 2019). Any reduction in ABA signaling amplification would accelerate this transition.
  - **Evidence**: [KNOWN for PA-ABA link] [INFERRED for germination effect] -- Score 10/10
  - **Germination link**: Lower ABA/GA ratio is the master hormonal switch for germination; reduced PA decreases ABA signal amplification; reduced NADPH oxidase activation modulates ROS burst
  - **Predicted molecular signature**: Reduced PA levels; decreased ABA/GA ratio relative to controls
  - **References**: Shuai et al. (2017) Sci Rep 7:12620 [DOI: 10.1038/s41598-017-13093-w]; Gazara et al. (2019) Sci Rep 9:9601 [DOI: 10.1038/s41598-019-45898-2]

- **Claim 1.3**: Downregulation of Cytokinin oxidase 3 (GLYMA_09G063900) elevates endogenous cytokinin levels, promoting cell division and providing antioxidant protection
  - **Genes**: GLYMA_09G063900 -- Cytokinin oxidase 3 (CKX3)
  - **Arabidopsis homolog**: AT5G56970
  - **Key domains**: FAD binding domain; CKX dehydrogenase domain
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: Cytokinin oxidases (CKX) irreversibly degrade cytokinins via oxidative side-chain cleavage. Cytokinins promote cell division and interact with the ABA/GA balance during germination. Downregulating CKX3 would elevate endogenous cytokinin levels, promoting cell division in the embryonic axis and radicle meristem. Critically, elevated cytokinins may also enhance zeatin riboside levels, which Gidrol et al. (1994) showed acts as a superoxide scavenger in soybean seeds -- providing an unexpected dual role: cell division promotion plus antioxidant protection within the "oxidative window."
  - **Evidence**: [KNOWN for CKX function] [INFERRED for germination acceleration] -- Score 9/10
  - **Germination link**: Elevated cytokinins promote cell division in embryonic axis; zeatin riboside acts as superoxide anion scavenger in soybean seeds (Gidrol et al. 1994); cytokinin-ABA crosstalk shifts hormonal balance toward germination
  - **Predicted molecular signature**: Elevated cytokinin (zeatin, zeatin riboside) levels in treated seeds
  - **References**: Gidrol et al. (1994) Eur J Biochem 224:21-28 [DOI: 10.1111/j.1432-1033.1994.tb19990.x]; Gazara et al. (2019) Sci Rep 9:9601 [DOI: 10.1038/s41598-019-45898-2]

- **Claim 1.4**: Downregulation of ROP GTPase (GLYMA_09G192700) modulates ABA signal transduction, potentially desensitizing ABA response
  - **Genes**: GLYMA_09G192700 (corrected from GLYMA_09G19270) -- ROP GTPase (RHO-related protein from plants 9)
  - **Arabidopsis homolog**: AT4G28950
  - **Key domains**: Ras GTPase domain
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: ROP (RHO of Plants) GTPases act as molecular switches in ABA signal transduction. In Arabidopsis, ROP10 negatively regulates ABA signaling; rop10 mutants are hypersensitive to ABA in germination assays. ROP GTPases also regulate ROS production through NADPH oxidase activation and polar auxin transport. The effect of downregulation depends on which specific ROP signaling module GLYMA_09G192700 participates in. If it functions analogously to AtROP10 (negative regulator of ABA), downregulation would enhance ABA sensitivity and potentially inhibit germination. If it functions in a positive ABA signaling arm, downregulation would reduce ABA sensitivity. This is a complex target requiring experimental validation.
  - **Evidence**: [KNOWN for ROP-ABA link] [INFERRED/UNCERTAIN for direction of effect] -- Score 9/10
  - **Germination link**: ABA signal transduction directly controls germination; ROS production via NADPH oxidase affects the oxidative window
  - **Risk**: Medium probability that downregulation could be counterproductive if this ROP is a negative ABA regulator
  - **References**: Shuai et al. (2017) Sci Rep 7:12620; Gazara et al. (2019) Sci Rep 9:9601

- **Claim 1.5 (Convergent model)**: The coordinated downregulation of the invertase inhibitor (derepress CWI --> more hexoses), PLDbeta1 (reduce PA --> weaken ABA signaling), and CKX3 (elevate cytokinins --> promote cell division) creates a convergent metabolic-hormonal signal: "sugar is abundant, ABA is low, divide and grow"
  - **Genes**: GLYMA_05G068700, GLYMA_01G215100, GLYMA_09G063900 acting in concert
  - **Direction**: All downregulated
  - **Mechanism**: Three-pronged attack on germination-limiting pathways operating simultaneously. This multi-target approach may explain why the seed treatment produces effects beyond what any single target downregulation would achieve.
  - **Evidence**: [INFERRED] -- Model A (Hormone-Sugar Metabolic Priming) is described as more parsimonious and better supported by existing soybean data than the alternative Defense-Redox model
  - **Testable prediction**: Exogenous glucose (10 mM) application to untreated seeds should partially phenocopy the germination acceleration; ABA/GA measurements will show altered ratios in treated seeds by 12 hours; invertase activity assays will show elevated CWI in treated vs. control by 24 hours

---

## Theme 2: Defense-Redox Reallocation

**Central thesis**: The bacterial exRNAs selectively suppress constitutive defense gene expression, liberating metabolic resources (carbon, nitrogen, energy) that are reallocated to germination processes, while simultaneously fine-tuning the ROS landscape to optimize the "oxidative window."

### Claims:

- **Claim 2.1**: Downregulation of TIR-NBS-LRR disease resistance protein (GLYMA_06G259700) reduces constitutive defense metabolic burden, freeing carbon and nitrogen for germination
  - **Genes**: GLYMA_06G259700 (KRH55503) -- TIR-NBS-LRR disease resistance protein
  - **Arabidopsis homolog**: AT5G45250
  - **Key domains**: TIR (Toll/interleukin-1 receptor); NBS (nucleotide-binding site); LRR (leucine-rich repeat)
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: Soybean contains 319 putative NBS-LRR disease resistance genes (Kang et al. 2012), and constitutive immune activation is metabolically costly with documented growth-defense tradeoffs (Gao et al. 2024). Isoflavonoid biosynthesis -- a legume-specific metabolic investment -- produces phytoalexins (glyceollins) from daidzein, representing a significant carbon and nitrogen cost. Downregulating a single TIR-NBS-LRR gene during germination reduces the constitutive defense metabolic burden, redirecting carbon and nitrogen from isoflavonoid biosynthesis and defense protein synthesis toward reserve mobilization and axis elongation. Metabolic profiling of soybean seed resistance to Fusarium fujikuroi showed metabolites rerouted between defense (isoflavone/flavone biosynthesis) and primary metabolism (glycine-serine-threonine, tryptophan) (Chang et al. 2022).
  - **Evidence**: [KNOWN for defense cost] [INFERRED for germination benefit of downregulation] -- Score 8/10
  - **Germination link**: Freed carbon and nitrogen redirected to storage protein mobilization and cell wall expansion; reduced isoflavonoid pathway flux; faster reserve mobilization (earlier beta-conglycinin degradation)
  - **Predicted molecular signature**: Reduced TIR-NBS-LRR transcript levels in treated seeds; decreased isoflavonoid (daidzein, genistein) accumulation in embryonic axes during first 48 hours
  - **References**: Kang et al. (2012) BMC Plant Biol 12:139 [DOI: 10.1186/1471-2229-12-139]; Gao et al. (2024) Plant Biotechnol J 22:1198-1205 [DOI: 10.1111/pbi.14258]; Chang et al. (2022) Front Plant Sci 13:993519 [DOI: 10.3389/fpls.2022.993519]; Lin et al. (2022) Theor Appl Genet 135:3773-3872 [DOI: 10.1007/s00122-022-04101-3]

- **Claim 2.2**: Downregulation of ERECTA-like LRR-RLK (GLYMA_10G242300) shifts the growth-defense balance toward growth during the germination window
  - **Genes**: GLYMA_10G242300 (KRH35424) -- Leucine-rich repeat receptor-like protein kinase (ERECTA-like)
  - **Arabidopsis homologs**: AT5G07180 (ERL2), AT5G62230 (ERL1)
  - **Key domains**: Protein kinase domain; LRR domain; LRR N-terminal domain
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: ERECTA-family receptor-like kinases regulate both developmental processes (organ shape, stomatal patterning) and pathogen defense. The Arabidopsis ERECTA pathway integrates growth and immunity signals. Downregulating the soybean ERECTA-like RLK could shift the growth-defense balance toward growth during the germination window, while potentially affecting organ morphology in later development.
  - **Evidence**: [KNOWN for ERECTA dual role] [INFERRED for germination effect] -- Score 7/10
  - **Germination link**: Reduced immune surveillance lowers metabolic cost; growth pathway derepression
  - **References**: Gao et al. (2024) Plant Biotechnol J 22:1198-1205

- **Claim 2.3**: Modulation of glutaredoxin (GLYMA_03G196400) fine-tunes the thiol-disulfide redox state, potentially widening the oxidative window for pro-germination ROS signaling
  - **Genes**: GLYMA_03G196400 -- Glutaredoxin family protein
  - **Arabidopsis homolog**: AT5G03870
  - **Key domains**: Glutaredoxin domain (PF00462)
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: The soybean genome encodes 12 Grx genes involved in thiol-disulfide redox homeostasis, with evidence of translational regulation under stress (Sainz et al. 2022). Glutaredoxins regulate the "redox kick-start" of mitochondrial energy metabolism during seed germination; seeds lacking thiol redox machinery use resources less efficiently (Nietzel et al. 2020). In rice, CRISPR knockout of OsGRX3/PHS9 produced delayed germination phenotypes, suggesting the wild-type protein facilitates rather than inhibits germination. The effect is context-dependent: if GLYMA_03G196400 functions as a dormancy-associated Grx (maintaining disulfide bridges on storage proteins during desiccation), its downregulation during imbibition could accelerate reductive activation of metabolic enzymes. However, if it functions as a pro-germination Grx (like OsGRX3), downregulation could be counterproductive. The ROS "oxidative window" concept posits a critical ROS concentration range that promotes germination signaling without causing oxidative damage (Bailly 2004; El-Maarouf-Bouteau & Bailly 2008).
  - **Evidence**: [KNOWN for Grx-redox role] [INFERRED/CONTEXT-DEPENDENT for direction] -- Score 9/10
  - **Germination link**: Altered thiol-disulfide balance affects storage protein mobilization, mitochondrial reactivation, and ROS signaling; soybean embryonic axes produce both superoxide and H2O2 with dynamic changes in SOD, catalase, and ascorbate-glutathione cycle enzymes during imbibition (Puntarulo et al. 1988, 1991)
  - **Risk**: Low-Medium probability that downregulation worsens redox state
  - **References**: Sainz et al. (2022) Antioxidants 11:1622 [DOI: 10.3390/antiox11081622]; Nietzel et al. (2020) PNAS 117:741-751 [DOI: 10.1073/pnas.1910501117]; Bailly (2004) Seed Sci Res 14:93-107 [DOI: 10.1079/SSR2004159]; El-Maarouf-Bouteau & Bailly (2008) Plant Signal Behav 3:175-182 [DOI: 10.4161/psb.3.3.5539]; Puntarulo et al. (1991) BBA 1074:277-283 [DOI: 10.1016/0304-4165(91)90164-c]; Puntarulo et al. (1988) Plant Physiol 86:626-630 [DOI: 10.1104/pp.86.2.626]

- **Claim 2.4**: Downregulation of LrgB-like membrane protein (GLYMA_01G009900) alters programmed cell death regulation during germination
  - **Genes**: GLYMA_01G009900 -- LrgB-like membrane protein
  - **Arabidopsis homolog**: AT1G32080
  - **Key domains**: LrgB domain (PF04172)
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: LrgB-family proteins are involved in programmed cell death (PCD) regulation, originally characterized in bacterial systems. In the plant context, modulating PCD pathways during germination could affect the controlled cell death processes that occur during endosperm weakening and radicle emergence.
  - **Evidence**: [INFERRED] -- Score 6/10
  - **Germination link**: PCD regulation during seed coat weakening and radicle protrusion
  - **References**: No soybean-specific references for LrgB in germination

- **Claim 2.5 (Defense-Redox Convergent Model)**: Downregulating TIR-NBS-LRR and ERECTA-like RLK reduces constitutive defense protein synthesis and isoflavonoid pathway flux; the freed carbon and nitrogen are redirected to storage protein mobilization and cell wall expansion; simultaneously, glutaredoxin modulation fine-tunes the redox state, potentially widening the oxidative window to allow stronger pro-germination ROS signaling without crossing into oxidative damage territory
  - **Genes**: GLYMA_06G259700, GLYMA_10G242300, GLYMA_03G196400, GLYMA_01G009900 acting in concert
  - **Direction**: All downregulated
  - **Evidence**: [INFERRED] -- Model B (Defense-Redox Reallocation) invokes a more novel mechanism but is consistent with the defense-growth tradeoff literature
  - **Predicted molecular signature**: Reduced TIR-NBS-LRR transcript levels; decreased isoflavonoid accumulation in embryonic axes during first 48 hours; altered SOD/catalase activity ratios; modified glutathione/glutaredoxin redox state; faster reserve protein mobilization (earlier beta-conglycinin degradation)
  - **Testable prediction**: Treated seeds will show reduced isoflavonoid levels compared to controls; adding exogenous salicylic acid (which activates defense) should abolish the germination benefit; ROS profiling (DHE/H2DCFDA staining) will show altered superoxide/H2O2 ratios in treated seeds; amino acid profiling will show increased free amino acids from reduced defense protein synthesis

---

## Theme 3: Cell Wall Remodeling

### Claims:

- **Claim 3.1**: Downregulation of Cellulose synthase A4 (GLYMA_09G051100) transiently reduces cell wall rigidity, facilitating radicle protrusion
  - **Genes**: GLYMA_09G051100 (KRH37200) -- Cellulose synthase A4 (CesA4)
  - **Arabidopsis homolog**: AT5G44030
  - **Key domains**: Cellulose synthase domain (PF03552)
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: CesA4 is a secondary cell wall cellulose synthase. Transient downregulation during imbibition could reduce cell wall rigidity, facilitating radicle protrusion through the seed coat -- consistent with the established role of cell wall loosening in germination. Soybean genome analysis identified 2,143 genes involved in cell wall biosynthesis and assembly, with key genes (expansins, cellulose synthases, glycosyltransferases) highly expressed at specific germination stages (Sangi et al. 2019). Embryonic axes grow through cell expansion rather than cell production during radicle emergence. However, sustained downregulation could compromise seedling structural integrity.
  - **Evidence**: [KNOWN for CesA function] [INFERRED for germination benefit] -- Score 7/10
  - **Germination link**: Cell wall loosening is essential for radicle protrusion; reduced cellulose deposition in secondary walls could facilitate embryo expansion
  - **Caveat**: Sustained downregulation could compromise seedling structural integrity post-emergence
  - **References**: Sangi et al. (2019) Planta 250:1325-1337 [DOI: 10.1007/s00425-019-03231-1]; Hernandez-Nistal et al. (2006) Plant Physiol Biochem 44:684-692 [DOI: 10.1016/j.plaphy.2006.10.017]

- **Claim 3.2**: The invertase/PME inhibitor (GLYMA_05G068700) has a dual cell wall role: its downregulation may also affect pectin methylesterase regulation
  - **Genes**: GLYMA_05G068700 (KRH57561) -- Invertase/pectin methylesterase inhibitor superfamily protein
  - **Direction**: Downregulated
  - **Mechanism**: This protein belongs to a superfamily that inhibits both invertases and pectin methylesterases. In addition to the invertase derepression described in Claim 1.1, downregulation may also affect pectin methylesterase (PME) activity. PMEs demethylesterify homogalacturonan in the cell wall, which can either stiffen or loosen walls depending on context. During germination, PME activity contributes to cell wall remodeling necessary for radicle emergence.
  - **Evidence**: [INFERRED] -- Dual function is speculative; the invertase inhibition function is better characterized
  - **Germination link**: Cell wall pectin remodeling during radicle protrusion

---

## Theme 4: RNA Processing and Translational Control

### Claims:

- **Claim 4.1**: Downregulation of exosome subunit Rrp46-like (GLYMA_09G261100) may alter mRNA turnover dynamics during germination
  - **Genes**: GLYMA_09G261100 -- Exosome subunit Rrp46-like
  - **Arabidopsis homolog**: AT3G46210
  - **Key domains**: 3' exoribonuclease; RNase PH domain
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: The exosome complex is a major 3'-to-5' RNA degradation machine. Modulating exosome subunit levels could alter the stability and turnover of germination-related mRNAs, potentially extending the half-life of pro-germination transcripts or altering the decay kinetics of stored maternal mRNAs.
  - **Evidence**: [SPECULATIVE] -- Score 5/10 -- No direct germination link established
  - **Germination link**: Indirect; altered mRNA turnover could shift transcript availability during imbibition
  - **References**: None specific to soybean germination

- **Claim 4.2**: Downregulation of Urb2/Npa2 ribosome biogenesis factor (GLYMA_08G231200) may modulate translational capacity
  - **Genes**: GLYMA_08G231200 -- Urb2/Npa2 ribosome biogenesis factor
  - **Arabidopsis homolog**: AT4G30150
  - **Key domains**: Urb2/Npa2 domain
  - **Direction**: Downregulated by exRNA-mediated silencing
  - **Mechanism**: Ribosome biogenesis is a major energy investment. Transient reduction in ribosome production could redirect nucleotide and energy resources toward other metabolic priorities during early imbibition.
  - **Evidence**: [SPECULATIVE] -- Score 4/10
  - **Germination link**: Indirect; resource reallocation from ribosome biogenesis
  - **References**: None specific

---

## Theme 5: Uncharacterized / Low-Confidence Targets

### Claims:

- **Claim 5.1**: UFM1-specific peptidase (GLYMA_02G220600) may modulate protein quality control during imbibition
  - **Genes**: GLYMA_02G220600 -- UFM1-specific peptidase (Peptidase C78)
  - **Arabidopsis homolog**: AT5G24680
  - **Key domains**: Peptidase C78 (PF07910)
  - **Direction**: Downregulated
  - **Evidence**: [SPECULATIVE] -- Score 5/10
  - **Mechanism**: UFM1 (ubiquitin-fold modifier 1) conjugation pathway is involved in ER protein quality control. Modulating this pathway could affect protein homeostasis during the metabolic reactivation of imbibition.

- **Claim 5.2**: hAT transposon superfamily protein (GLYMA_01G091700) -- function unclear
  - **Genes**: GLYMA_01G091700 -- hAT transposon superfamily protein
  - **Arabidopsis homolog**: AT4G15020
  - **Key domains**: DUF659 (PF04937)
  - **Direction**: Downregulated
  - **Evidence**: [SPECULATIVE] -- Score 4/10
  - **Mechanism**: Transposable element-related; may represent a transposon-derived gene with co-opted regulatory function or may be a bioinformatic false positive

- **Claim 5.3**: CURT1-like thylakoid membrane protein (GLYMA_07G060700) -- annotation conflict
  - **Genes**: GLYMA_07G060700 (KRH47986) -- CURT1-like thylakoid membrane protein (SoyBase annotation) vs. "cation transport regulator-like protein 2-like" (original annotation)
  - **Arabidopsis homolog**: AT4G01150 (CURT1A)
  - **Direction**: Downregulated
  - **Evidence**: [UNCERTAIN] -- Score 3/10
  - **FLAG**: Major annotation conflict. The original target list described this as "cation transport regulator-like protein 2-like" but SoyBase annotation for GLYMA_07G060700 indicates a CURT1-like thylakoid membrane protein. CURT1 proteins are NOT cation transporters. The KRH47986 NCBI record was removed, so the original annotation may have differed from current SoyBase entries. The discrepancy may reflect different annotation pipeline versions across genome assemblies.
  - **Germination link**: If truly CURT1-like, minimal relevance to germination (photosynthesis-related); if truly a cation transport regulator, potentially relevant to ion homeostasis during imbibition

- **Claim 5.4**: Four completely or poorly characterized targets have no predictable germination mechanism
  - **Genes**:
    - GLYMA_10G097500 (KRH33075) -- Hypothetical protein (uncharacterized); AT3G57440; NCBI record REMOVED
    - GLYMA_10G268800 (KRH35861) -- Hypothetical protein (very short, 61 aa); no Arabidopsis homolog
    - GLYMA_06G057500 (KRH5227*) -- DUF1677 protein; AT1G72510; truncated accession
    - GLYMA_12G091900 (KRH25272) -- Hypothetical integral membrane protein; AT5G22340; NCBI record REMOVED
  - **Evidence**: Scores 1-3/10
  - **Recommendation**: These would benefit from domain prediction via InterProScan or AlphaFold structure analysis

---

## Cross-Kingdom sRNA Precedent

### The Ren et al. (2019) Bradyrhizobium japonicum Evidence -- THE CRITICAL PRECEDENT

**Full citation**: Ren B, Wang X, Duan J, Ma J. (2019) Rhizobial tRNA-derived small RNAs are signal molecules regulating plant nodulation. *Science*, 365(6456): 919-922. DOI: 10.1126/science.aav8907

**Key findings**:
1. *Bradyrhizobium japonicum* (the nitrogen-fixing rhizobial symbiont of soybean) produces tRNA-derived small RNA fragments (tRFs) that are transferred to soybean host cells during the symbiotic interaction
2. These bacterial tRFs silence soybean target genes to regulate nodulation
3. The silencing mechanism operates through an AGO1-dependent pathway -- the canonical plant RNAi machinery
4. This establishes that bacterial small RNAs CAN enter soybean cells AND direct gene silencing via the host RNAi pathway

**Why this is critical for the exRNA hypothesis**:
- This is the most directly relevant precedent in the literature: a bacterium transferring functional sRNAs into soybean cells
- It was published in *Science*, the highest-impact venue, providing strong credibility
- It demonstrates that the biological phenomenon (bacteria-to-soybean sRNA transfer via RNAi) is not hypothetical -- it has been experimentally validated in a system involving the same host species (*Glycine max*)
- It distinguishes soybean from crop systems where such transfer has NOT been demonstrated, providing a biological plausibility advantage unique to soybean among the crops being studied
- The Ren et al. system uses rhizobial tRFs rather than exRNAs from EPS, but the downstream mechanism (AGO1-dependent silencing in soybean) would be identical

**Additional cross-kingdom RNAi precedents**:
- **Weiberg et al. (2013)** -- Fungal pathogen *Botrytis cinerea* transfers small RNAs into Arabidopsis and tomato cells to suppress plant immunity genes via AGO1-dependent RNAi. *Science* 342:118-123. [DOI: 10.1126/science.1239705]
- **Cai et al. (2018)** -- Plants reciprocally send small RNAs to fungal pathogens via extracellular vesicles (EVs) to silence virulence genes. *Science* 360:1126-1129. [DOI: 10.1126/science.aar4142]
- **He et al. (2023)** -- Fungal small RNAs ride in extracellular vesicles to enter plant cells through clathrin-mediated endocytosis. *Nature Communications* 14:4383. [DOI: 10.1038/s41467-023-40093-4]
- **Cai et al. (2021)** -- Comprehensive review of EV-mediated cross-kingdom RNA trafficking. *Annual Review of Plant Biology* 72:497-524. [DOI: 10.1146/annurev-arplant-081720-010616]
- **Ste-Croix et al. (2023)** -- Characterized microRNAs in the soybean cyst nematode (*Heterodera glycines*) and identified candidate effector sRNAs involved in cross-kingdom interactions with soybean. *RNA Biology* 20(1):614-628. [DOI: 10.1080/15476286.2023.2244790]
- **Subramanian et al. (2005)** -- Demonstrated that RNAi of soybean isoflavone synthase genes led to silencing in tissues distal to the transformation site, confirming soybean possesses functional systemic RNAi machinery. *Plant Physiology* 137(4):1345-1353. [DOI: 10.1104/pp.104.057257]

**Soybean RNAi toolkit**:
- Liu et al. (2014) conducted a systematic identification of RNA silencing components in soybean, identifying multiple copies of DCL (Dicer-like), AGO (Argonaute), RDR (RNA-dependent RNA polymerase), and HEN1 genes. The paleopolyploid nature of the soybean genome means many silencing components exist as duplicated paralogs, providing both redundancy and potential subfunctionalization. *BMC Bioinformatics* 15:4. [DOI: 10.1186/1471-2105-15-4]
- Host-induced gene silencing (HIGS) has been successfully demonstrated in soybean against the soybean cyst nematode (*Heterodera glycines*), with stable transgenic soybean lines expressing dsRNA against nematode fitness genes (HgY25, HgPrp17) showing effective silencing. Li et al. (2010, 2011, 2019). [DOIs: 10.1007/s00425-010-1209-7; 10.1111/j.1467-7652.2011.00601.x; 10.1007/s00122-019-03379-0]
- HEN1-mediated 2'-O-methylation protects small RNAs from 3'-end uridylation and degradation, relevant to understanding the stability of exogenous sRNAs within the soybean cellular environment. Li et al. (2005) *Current Biology* 15:1501-1507. [DOI: 10.1016/j.cub.2005.07.029]

---

## Top Targets (ranked)

| Rank | Gene ID | Annotation | Score | Pathway | Why Top |
|------|---------|------------|-------|---------|---------|
| 1 | GLYMA_05G068700 (KRH57561) | Invertase/PME inhibitor | 10 | Sugar sensing / Cell wall | Strongest cross-species experimental validation: RNAi of GmCIF1 elevates CWI, increases hexoses, starch, protein in soybean seeds (Tang et al. 2017); AtCIF1 loss accelerates germination in Arabidopsis (Su et al. 2016); INVINH1 silencing increases hexoses in tomato (Jin et al. 2009). Most directly actionable target. |
| 2 | GLYMA_01G215100 | Phospholipase D beta 1 | 10 | ABA/GA (lipid signaling) | PA is a validated ABA signaling amplifier; reducing PA directly lowers ABA/GA ratio, the master germination switch. Also modulates ROS burst via NADPH oxidase activation. |
| 3 | GLYMA_09G063900 | Cytokinin oxidase 3 (CKX3) | 9 | Hormone metabolism | CKX irreversibly degrades cytokinins; downregulation elevates cytokinins for cell division AND zeatin riboside acts as superoxide scavenger in soybean seeds (Gidrol et al. 1994) -- dual benefit. |
| 4 | GLYMA_03G196400 | Glutaredoxin family protein | 9 | ROS/redox | 12 Grx genes in soybean with evidence of translational regulation; regulates thiol-disulfide redox critical for "oxidative window"; but direction-dependent -- context matters. |
| 5 | GLYMA_09G192700 | ROP GTPase (ROP9) | 9 | ABA signal transduction | Molecular switch in ABA signaling; complex target because direction of effect depends on which ROP module it participates in. |
| 6 | GLYMA_06G259700 (KRH55503) | TIR-NBS-LRR disease resistance | 8 | Defense | Constitutive defense activation is metabolically costly (319 NBS-LRR genes in soybean); downregulation frees carbon/nitrogen for germination. Defense-growth tradeoff well documented. |
| 7 | GLYMA_09G051100 (KRH37200) | Cellulose synthase A4 (CesA4) | 7 | Cell wall | Transient reduction in secondary cell wall rigidity could facilitate radicle protrusion; 2,143 cell wall genes in soybean germination transcriptome. Risk: sustained downregulation compromises integrity. |
| 8 | GLYMA_10G242300 (KRH35424) | ERECTA-like LRR-RLK | 7 | Defense / Development | Dual-function RLK integrating growth and immunity; downregulation shifts balance toward growth during germination window. |
| 9 | GLYMA_01G009900 | LrgB-like membrane protein | 6 | Defense / Cell death | PCD regulation relevant to endosperm weakening; less well characterized in plant germination. |
| 10 | GLYMA_09G261100 | Exosome subunit Rrp46-like | 5 | RNA processing | Could alter mRNA turnover dynamics; indirect and speculative germination link. |
| 11 | GLYMA_02G220600 | UFM1-specific peptidase | 5 | Protein QC | ER protein quality control; speculative relevance. |
| 12 | GLYMA_08G231200 | Urb2/Npa2 ribosome biogenesis | 4 | Ribosome biogenesis | Resource reallocation from ribosome production; speculative. |
| 13 | GLYMA_01G091700 | hAT transposon protein | 4 | TE-related | May be bioinformatic false positive. |
| 14 | GLYMA_07G060700 (KRH47986) | CURT1-like thylakoid protein | 3 | Photosynthesis (UNCERTAIN) | Major annotation conflict; CURT1 is photosynthesis-related with minimal germination relevance. |
| 15 | GLYMA_06G057500 (KRH5227*) | DUF1677 protein | 3 | Unknown | Domain of unknown function; truncated accession. |
| 16 | GLYMA_12G091900 (KRH25272) | Hypothetical membrane protein | 2 | Unknown (membrane) | Uncharacterized; NCBI record removed. |
| 17 | GLYMA_10G097500 (KRH33075) | Hypothetical protein | 2 | Unknown | Completely uncharacterized; NCBI record removed. |
| 18 | GLYMA_10G268800 (KRH35861) | Hypothetical protein (61 aa) | 1 | Unknown | Very short protein; no known domains; no homologs. |

---

## Proposed Primary MoA for Soybean

**Model A: Hormone-Sugar Metabolic Priming (Favored -- more parsimonious)**

The bacterial exRNAs delivered via EPS during seed imbibition enter soybean cells and engage the host AGO1-dependent RNAi machinery (as precedented by Ren et al. 2019). The exRNAs simultaneously target three interconnected germination control nodes:

1. **Sugar flux derepression**: Silencing the invertase inhibitor (GLYMA_05G068700) elevates CWI activity, flooding embryonic axes with hexose sugars (glucose + fructose) that fuel metabolic activation and signal via HXK-dependent pathways.

2. **ABA signaling attenuation**: Silencing PLDbeta1 (GLYMA_01G215100) reduces phosphatidic acid production, attenuating ABA signal amplification and lowering the ABA/GA ratio below the germination threshold faster than untreated seeds. Silencing the ROP GTPase (GLYMA_09G192700) further modulates ABA signal transduction.

3. **Cytokinin elevation**: Silencing CKX3 (GLYMA_09G063900) prevents cytokinin degradation, elevating zeatin and zeatin riboside levels, promoting cell division in the embryonic axis while simultaneously providing antioxidant protection (zeatin riboside as superoxide scavenger).

The combined effect is a metabolically primed state: "sugar is abundant, ABA is low, divide and grow." This three-pronged attack on germination-limiting pathways produces effects beyond what any single target downregulation would achieve.

**Testable predictions for Model A**:
- Exogenous glucose (10 mM) to untreated seeds should partially phenocopy germination acceleration
- ABA/GA measurements will show altered ratios in treated seeds by 12 hours
- Invertase activity assays will show elevated CWI in treated vs. control by 24 hours
- Cytokinin profiling will show elevated zeatin/zeatin riboside

**Model B: Defense-Redox Reallocation (Alternative)**

The exRNAs primarily target defense genes (TIR-NBS-LRR, ERECTA-like RLK) and redox regulators (glutaredoxin), with the primary effect being resource liberation from constitutive defense pathways and optimization of the oxidative window. This model invokes a more novel mechanism but is consistent with the documented defense-growth tradeoff in soybean.

**Distinguishing experiment**: Apply exogenous glucose to untreated seeds AND measure isoflavonoid levels in treated seeds. If glucose phenocopies the effect but isoflavonoid levels are unchanged, Model A is primary. If isoflavonoid levels are reduced but glucose alone does not phenocopy, Model B is primary. If both effects are observed, a combined model operates.

---

## Alternative Model: EPS Osmopriming

**What EPS alone (without RNA) could explain**:

1. **EPS osmopriming (HIGHEST CONCERN confounder)**: [KNOWN] PEG-6000 osmopriming improves aged soybean seed vigor through carbon metabolism, ROS scavenging, hormone signaling, and lignin synthesis regulation (Wang et al. 2023). The bacterial EPS is a hydrated polymer matrix that could produce identical osmopriming effects simply through water activity modulation. This could explain 100% of the germination improvement without any RNA involvement. **Control**: Compare EPS (intact) vs. EPS (RNase-treated) vs. synthetic hydrogel (equivalent water activity) vs. water-only.

2. **Polysaccharide elicitor effects**: [KNOWN] Bacterial EPS polysaccharides can trigger plant innate immune responses and prime defense systems (Costa et al. 2018). Paradoxically, mild defense priming can enhance overall seedling vigor through "priming memory" that improves stress tolerance. **Control**: Heat-denatured EPS (destroys RNA secondary structure but preserves polysaccharides) vs. intact EPS.

3. **Biopriming by residual bacteria**: [KNOWN] Biopriming with *Bradyrhizobium japonicum* and *Bacillus megaterium* improves soybean germination and initial seedling growth (Miljakovic et al. 2022). If the EPS preparation contains viable bacteria, any germination enhancement could result from conventional biopriming rather than exRNA transfer. **Control**: Filter-sterilize (0.22 um) vs. UV-sterilize vs. untreated EPS.

4. **Nutrient effects**: [INFERRED] The EPS matrix contains proteins, amino acids, and minerals that may simply provide metabolic fuel for faster germination, particularly for aged or stressed seeds. **Control**: Dialyzed EPS (retain macromolecules, remove small molecules) vs. dialysate-only vs. complete EPS.

5. **pH and ionic strength effects**: [INFERRED] The EPS solution may alter the local pH and ionic environment of the seed coat during imbibition, affecting enzyme activities and ion channel kinetics independent of RNA content. **Control**: Buffer-matched controls at equivalent pH and ionic strength.

6. **Bioinformatic false positives in target prediction**: [KNOWN] Computational prediction of sRNA-mRNA complementarity generates high rates of false positives, especially with short sequences in a 1.1 Gb genome (Schmutz et al. 2010). Some or many of the 18 predicted targets may not be genuine biological targets. **Control**: Validate target downregulation by RT-qPCR (minimum 5 high-priority targets).

**The Killer Experiment -- RNase Elimination**:
- Prepare EPS seed treatment as standard
- Split into three aliquots: (A) Untreated EPS (positive control); (B) EPS + RNase A (100 ug/mL, 37C, 1 hour); (C) EPS + heat-inactivated RNase A (negative control for RNase buffer effects)
- Treat soybean seeds (var. Williams 82, n=50 per treatment, 4 replicates)
- Score germination (radicle emergence >= 2 mm) at 24, 48, 72, 96 hours
- Interpretation: If B ~ C << A: RNA is essential; If B ~ C ~ A: RNA is not essential; If B < A but B > C: partial RNA contribution
- Cost: ~$200-500; Timeline: 2 weeks; Decision value: CRITICAL

---

## Legume-Specific Considerations

### How soybean's legume biology intersects with exRNA effects:

1. **Nitrogen fixation and rhizobial symbiosis**: Soybean has a pre-existing biological infrastructure for receiving and responding to bacterial signals during symbiosis. The Ren et al. (2019) precedent shows that *Bradyrhizobium japonicum* already uses tRNA-derived small RNAs to regulate soybean gene expression during nodulation, via AGO1-dependent silencing. This means soybean may be especially receptive to bacterial sRNAs compared to non-legume crops, because the host RNAi pathway has been "trained" by millions of years of co-evolution with rhizobia. Additionally, GmCML5 and GmCML6 are involved in nodulation (Yadav et al. 2022), and the glutaredoxin network interacts with nitrogen metabolism enzymes (Sainz et al. 2022), suggesting potential crosstalk between exRNA targets and nitrogen fixation pathways.

2. **Storage protein composition**: Soybean seeds contain 70-80% globulin storage proteins (7S beta-conglycinin and 11S glycinin), which is substantially higher protein content than most non-legume crops. Storage protein mobilization is a critical germination checkpoint (Wei et al. 2020: mutants lacking abundant storage proteins show reduced germination). The exRNA-mediated defense downregulation could redirect nitrogen from isoflavonoid biosynthesis and defense protein synthesis specifically toward more efficient storage protein mobilization. The subtilisin-like protease C1 that initiates storage protein proteolysis requires PSV acidification at ~24 hours post-imbibition (He et al. 2007; Wilson et al. 2016) -- a timing window that coincides with when exRNA-mediated silencing effects would be expected to manifest.

3. **Isoflavonoid defense pathway**: Legumes invest heavily in isoflavonoid biosynthesis (daidzein --> glyceollins as phytoalexins), representing a significant carbon and nitrogen sink unique to legumes. The defense-reallocation model (Theme 2) predicts that exRNA-mediated downregulation of NBS-LRR genes would reduce isoflavonoid pathway flux, freeing these resources specifically for germination. This defense cost is legume-specific and would not be operative in non-legume crops like maize or wheat.

4. **Paleopolyploidy and duplicated RNAi machinery**: The soybean genome underwent two whole-genome duplication events (~59 and ~13 Mya), resulting in ~75% of genes existing in multiple copies (Schmutz et al. 2010). This means: (a) the RNAi toolkit (DCL, AGO, RDR, HEN1) has duplicated paralogs with potential subfunctionalization (Liu et al. 2014); (b) many target genes have paralogs that would not be silenced, providing functional redundancy; (c) the 1.1 Gb genome increases the rate of bioinformatic false positives in sRNA target prediction. The predicted 18 targets likely represent only a subset of actual targets, and some predictions may be spurious.

5. **Seed oil bodies and TAG mobilization**: Soybean seeds are rich in triacylglycerols (TAG) stored in oil bodies, mobilized by SDP1-family lipases during germination (Kanai et al. 2019). None of the 18 predicted targets directly affect TAG mobilization, but the metabolic priming model (increased hexose flux, altered hormonal balance) could indirectly accelerate oil body mobilization through hormonal crosstalk.

6. **Imbibition kinetics and exRNA uptake window**: Soybean seed imbibition follows a two-phase model: first coat-dominated, then cotyledon-dominated (Meyer et al. 2007). Water entry commences within 10 minutes. During Phase I imbibition (0-6 hours), the soybean seed coat becomes highly permeable, creating a temporal window during which exogenous molecules at the seed surface have maximal access to the embryo. Cell wall loosening begins early, with expansins, XTH, and cellulose synthases transcriptionally activated (Sangi et al. 2019). This cell wall remodeling may facilitate uptake of macromolecular complexes including EPS-bound sRNAs. EPS treatment should be applied during Phase I (0-6 hours) for maximum uptake.

---

## Key References

### Cross-Kingdom RNAi and Soybean RNAi Machinery
1. **Ren B, Wang X, Duan J, Ma J. (2019)** Rhizobial tRNA-derived small RNAs are signal molecules regulating plant nodulation. *Science* 365(6456):919-922. DOI: 10.1126/science.aav8907 **[CRITICAL PRECEDENT]**
2. Weiberg A, Wang M, Lin FM, Zhao H, Zhang Z, Kaloshian I, Huang HD, Jin H. (2013) Fungal small RNAs suppress plant immunity by hijacking host RNA interference pathways. *Science* 342(6154):118-123. DOI: 10.1126/science.1239705
3. Cai Q, Qiao L, Wang M, He B, Lin FM, Palmquist J, Huang SD, Jin H. (2018) Plants send small RNAs in extracellular vesicles to fungal pathogen to silence virulence genes. *Science* 360(6393):1126-1129. DOI: 10.1126/science.aar4142
4. He B, Wang H, Liu G, Chen A, Calvo A, Cai Q, Jin H. (2023) Fungal small RNAs ride in extracellular vesicles to enter plant cells through clathrin-mediated endocytosis. *Nature Communications* 14:4383. DOI: 10.1038/s41467-023-40093-4
5. Cai Q, He B, Wang S, Fletcher S, Niu D, Mitter N, Birch PRJ, Jin H. (2021) Message in a Bubble: Shuttling small RNAs and proteins between cells and interacting organisms using extracellular vesicles. *Annual Review of Plant Biology* 72:497-524. DOI: 10.1146/annurev-arplant-081720-010616
6. Ste-Croix DT, Belanger RR, Mimee B. (2023) Characterization of microRNAs in the cyst nematode *Heterodera glycines* identifies possible candidates involved in cross-kingdom interactions with its host *Glycine max*. *RNA Biology* 20(1):614-628. DOI: 10.1080/15476286.2023.2244790
7. Subramanian S, Graham MY, Yu O, Graham TL. (2005) RNA interference of soybean isoflavone synthase genes leads to silencing in tissues distal to the transformation site and to enhanced susceptibility to *Phytophthora sojae*. *Plant Physiology* 137(4):1345-1353. DOI: 10.1104/pp.104.057257
8. Liu X, Lu T, Dou Y, Yu B, Zhang C. (2014) Identification of RNA silencing components in soybean and sorghum. *BMC Bioinformatics* 15:4. DOI: 10.1186/1471-2105-15-4
9. Li J, Todd TC, Oakley TR, Lee J, Trick HN. (2010) Host-derived suppression of nematode reproductive and fitness genes decreases fecundity of *Heterodera glycines* Ichinohe. *Planta* 232(3):775-785. DOI: 10.1007/s00425-010-1209-7
10. Li J, Todd TC, Lee J, Trick HN. (2011) Biotechnological application of functional genomics towards plant-parasitic nematode control. *Plant Biotechnology Journal* 9(9):936-944. DOI: 10.1111/j.1467-7652.2011.00601.x
11. Li J, Todd TC, Trick HN. (2019) Host-derived gene silencing of parasite fitness genes improves resistance to soybean cyst nematodes in stable transgenic soybean. *Theoretical and Applied Genetics* 133(3):1187-1198. DOI: 10.1007/s00122-019-03379-0
12. Li J, Yang Z, Yu B, Liu J, Chen X. (2005) Methylation protects miRNAs and siRNAs from a 3'-end uridylation activity in Arabidopsis. *Current Biology* 15(16):1501-1507. DOI: 10.1016/j.cub.2005.07.029
13. Bologna NG, Voinnet O. (2014) The diversity, biogenesis, and activities of endogenous silencing small RNAs in Arabidopsis. *Annual Review of Plant Biology* 65:473-503. DOI: 10.1146/annurev-arplant-050213-035728
14. Vaucheret H. (2008) Plant ARGONAUTES. *Trends in Plant Science* 13(7):350-358. DOI: 10.1016/j.tplants.2008.04.007

### Soybean Germination Biology
15. Shuai H, Meng Y, Luo X, Chen F, Zhou W, Dai Y, Qi Y, Du J, Yang F, Liu J, Yang W, Shu K. (2017) Exogenous auxin represses soybean seed germination through decreasing the gibberellin/abscisic acid (GA/ABA) ratio. *Scientific Reports* 7:12620. DOI: 10.1038/s41598-017-13093-w
16. Gazara RK, de Oliveira EAG, Rodrigues BC, Nunes da Fonseca R, Oliveira AEA, Venancio TM. (2019) Transcriptional landscape of soybean (*Glycine max*) embryonic axes during germination in the presence of paclobutrazol, a gibberellin biosynthesis inhibitor. *Scientific Reports* 9:9601. DOI: 10.1038/s41598-019-45898-2
17. Bellieny-Rabelo D, De Oliveira EAG, Ribeiro ES, Costa EP, Oliveira AEA, Venancio TM. (2016) Transcriptome analysis uncovers key regulatory and metabolic aspects of soybean embryonic axes during germination. *Scientific Reports* 6:36009. DOI: 10.1038/srep36009
18. Ishibashi Y, Koda Y, Zheng S-H, Yuasa T, Iwaya-Inoue M. (2013) Regulation of soybean seed germination through ethylene production in response to reactive oxygen species. *Annals of Botany* 111(1):95-102. DOI: 10.1093/aob/mcs240
19. Meyer CJ, Steudle E, Peterson CA. (2007) Patterns and kinetics of water uptake by soybean seeds. *Journal of Experimental Botany* 58(3):717-732. DOI: 10.1093/jxb/erl244
20. Sangi S, Santos MLC, Alexandrino CR, Da Cunha M, Coelho FS, Ribeiro GP, Lenz D, Ballesteros H, Hemerly AS, Venancio TM, Oliveira AEA, Grativol C. (2019) Cell wall dynamics and gene expression on soybean embryonic axes during germination. *Planta* 250(4):1325-1337. DOI: 10.1007/s00425-019-03231-1
21. Hernandez-Nistal J, Labrador E, Martin I, Jimenez T, Dopico B. (2006) Transcriptional profiling of cell wall protein genes in chickpea embryonic axes during germination and growth. *Plant Physiology and Biochemistry* 44(11-12):684-692. DOI: 10.1016/j.plaphy.2006.10.017

### Storage Protein and Reserve Mobilization
22. He F, Huang F, Wilson KA, Tan-Wilson A. (2007) Protein storage vacuole acidification as a control of storage protein mobilization in soybeans. *Journal of Experimental Botany* 58(5):1059-1070. DOI: 10.1093/jxb/erl267
23. Wilson KA, Chavda BJ, Pierre-Louis G, Quinn A, Tan-Wilson A. (2016) Role of vacuolar membrane proton pumps in the acidification of protein storage vacuoles following germination. *Plant Physiology and Biochemistry* 104:242-249. DOI: 10.1016/j.plaphy.2016.03.031
24. Kim HT, Choi U-K, Ryu HS, Lee SJ, Kwon O-S. (2011) Mobilization of storage proteins in soybean seed (*Glycine max* L.) during germination and seedling growth. *Biochimica et Biophysica Acta -- Proteins and Proteomics* 1814(9):1178-1187. DOI: 10.1016/j.bbapap.2011.05.004
25. Wei X, Kim W-S, Song B, Oehrle NW, Liu S, Krishnan HB. (2020) Soybean mutants lacking abundant seed storage proteins are impaired in mobilization of storage reserves and germination. *ACS Omega* 5(14):8065-8075. DOI: 10.1021/acsomega.0c00128
26. Kanai M, Yamada T, Hayashi M, Mano S, Nishimura M. (2019) Soybean (*Glycine max* L.) triacylglycerol lipase GmSDP1 regulates the quality and quantity of seed oil. *Scientific Reports* 9:8924. DOI: 10.1038/s41598-019-45331-8

### Sugar Sensing and Invertase Biology
27. Tang X, Su T, Han M, Wei L, Wang W, Yu Z, Xue Y, Wei H, Du Y, Greiner S, Rausch T, Liu L. (2017) Suppression of extracellular invertase inhibitor gene expression improves seed weight in soybean (*Glycine max*). *Journal of Experimental Botany* 68(3):469-482. DOI: 10.1093/jxb/erw425
28. Su T, Wolf S, Han M, Zhao H, Wei H, Greiner S, Rausch T. (2016) Reassessment of an Arabidopsis cell wall invertase inhibitor AtCIF1 reveals its role in seed germination and early seedling growth. *Plant Molecular Biology* 90(1-2):137-155. DOI: 10.1007/s11103-015-0402-2
29. Jin Y, Ni DA, Ruan YL. (2009) Posttranslational elevation of cell wall invertase activity by silencing its inhibitor in tomato delays leaf senescence and increases seed weight and fruit hexose level. *The Plant Cell* 21(7):2072-2089. DOI: 10.1105/tpc.108.063719
30. Kuo TM, Doehlert DC, Crawford CG. (1990) Sugar metabolism in germinating soybean seeds: evidence for the sorbitol pathway in soybean axes. *Plant Physiology* 93(4):1514-1520. DOI: 10.1104/pp.93.4.1514
31. Ni DA, et al. (2018) Genome-wide survey of invertase encoding genes and functional characterization of an extracellular fungal pathogen-responsive invertase in *Glycine max*. *International Journal of Molecular Sciences* 19(8):2395. DOI: 10.3390/ijms19082395
32. Koch K. (2004) Sucrose metabolism: regulatory mechanisms and pivotal roles in sugar sensing and plant development. *Current Opinion in Plant Biology* 7(3):235-246. DOI: 10.1016/j.pbi.2004.03.014

### T6P/SnRK1 Pathway
33. Macovei A, Pagano A, Cappuccio M, Gallotti L, Dondi D, De Sousa Araujo S, Fevereiro P, Balestrazzi A. (2019) A snapshot of the trehalose pathway during seed imbibition in *Medicago truncatula* reveals temporal- and stress-dependent shifts in gene expression patterns associated with metabolite changes. *Frontiers in Plant Science* 10:1590. DOI: 10.3389/fpls.2019.01590

### Redox Biology
34. Sainz MM, Filippi CV, Eastman G, Sotelo-Silveira J, Borsani O, Sotelo-Silveira M. (2022) Analysis of thioredoxins and glutaredoxins in soybean: evidence of translational regulation under water restriction. *Antioxidants* 11(8):1622. DOI: 10.3390/antiox11081622
35. Nietzel T, Mostertz J, Ruberti C, Nee G, Fuchs P, Wagner S, Moseler A, Muller-Schussele SJ, Benamar A, Poschet G, et al. (2020) Redox-mediated kick-start of mitochondrial energy metabolism drives resource-efficient seed germination. *Proceedings of the National Academy of Sciences USA* 117(1):741-751. DOI: 10.1073/pnas.1910501117
36. Bailly C. (2004) Active oxygen species and antioxidants in seed biology. *Seed Science Research* 14(2):93-107. DOI: 10.1079/SSR2004159
37. El-Maarouf-Bouteau H, Bailly C. (2008) Oxidative signaling in seed germination and dormancy. *Plant Signaling and Behavior* 3(3):175-182. DOI: 10.4161/psb.3.3.5539
38. Gidrol X, Lin WS, Degousee N, Yip SF, Kush A. (1994) Accumulation of reactive oxygen species and oxidation of cytokinin in germinating soybean seeds. *European Journal of Biochemistry* 224(1):21-28. DOI: 10.1111/j.1432-1033.1994.tb19990.x
39. Puntarulo S, Galleano M, Sanchez RA, Boveris A. (1991) Superoxide anion and hydrogen peroxide metabolism in soybean embryonic axes during germination. *Biochimica et Biophysica Acta* 1074(2):277-283. DOI: 10.1016/0304-4165(91)90164-c
40. Puntarulo S, Sanchez RA, Boveris A. (1988) Hydrogen peroxide metabolism in soybean embryonic axes at the onset of germination. *Plant Physiology* 86(2):626-630. DOI: 10.1104/pp.86.2.626

### Ion Homeostasis and Calcium Signaling
41. Martinez-Ballesta MC, Egea-Gilabert C, Conesa E, Ochoa J, Vicente MJ, Franco JA, Banon S, Martinez JJ, Fernandez JA. (2020) The importance of ion homeostasis and nutrient status in seed development and germination. *Agronomy* 10(4):504. DOI: 10.3390/agronomy10040504
42. Hettenhausen C, Sun G, He Y, Zhuang H, Sun T, Qi J, Wu J. (2016) Genome-wide identification of calcium-dependent protein kinases in soybean and analyses of their transcriptional responses to insect herbivory and drought stress. *Scientific Reports* 6:18973. DOI: 10.1038/srep18973
43. Yadav M, Pandey J, Chakraborty A, Hassan MI, Kundu JK, Roy A, Singh IK, Singh A. (2022) A comprehensive analysis of calmodulin-like proteins of *Glycine max* indicates their role in calcium signaling and plant defense against insect attack. *Frontiers in Plant Science* 13:817950. DOI: 10.3389/fpls.2022.817950

### Defense-Growth Tradeoff
44. Gao M, Hao Z, Ning Y, He Z. (2024) Revisiting growth-defence trade-offs and breeding strategies in crops. *Plant Biotechnology Journal* 22(5):1198-1205. DOI: 10.1111/pbi.14258
45. Chang X, Li X, Meng H, Li H, Wu X, Gong G, Chen H, Yang C, Zhang M, Liu T, Chen W, Yang W. (2022) Physiological and metabolic analyses provide insight into soybean seed resistance to *Fusarium fujikuroi* causing seed decay. *Frontiers in Plant Science* 13:993519. DOI: 10.3389/fpls.2022.993519
46. Kang YJ, Kim KH, Shim S, Yoon MY, Sun S, Kim MY, Van K, Lee S-H. (2012) Genome-wide mapping of NBS-LRR genes and their association with disease resistance in soybean. *BMC Plant Biology* 12:139. DOI: 10.1186/1471-2229-12-139
47. Lin F, Chhapekar SS, Vieira CC, Da Silva MP, Rojas A, et al. (2022) Breeding for disease resistance in soybean: a global perspective. *Theoretical and Applied Genetics* 135(11):3773-3872. DOI: 10.1007/s00122-022-04101-3

### Seed Priming and EPS Context
48. Miljakovic D, Marinkovic J, Tamindzic G, Djordjevic V, Tintor B, Milosevic D, Ignjatov M, Nikolic Z. (2022) Bio-priming of soybean with *Bradyrhizobium japonicum* and *Bacillus megaterium*: strategy to improve seed germination and the initial seedling growth. *Plants* 11(15):1927. DOI: 10.3390/plants11151927
49. Wang Y, Zhou E, Yao M, Xue D, Zhao N, Zhou Y, Li B, Wang K, Miao Y, Gu C, et al. (2023) PEG-6000 priming improves aged soybean seed vigor via carbon metabolism, ROS scavenging, hormone signaling, and lignin synthesis regulation. *Agronomy* 13(12):3021. DOI: 10.3390/agronomy13123021
50. Flemming HC, Wingender J. (2010) The biofilm matrix. *Nature Reviews Microbiology* 8(9):623-633. DOI: 10.1038/nrmicro2415
51. Flemming HC, Wingender J, Szewzyk U, Steinberg P, Rice SA, Kjelleberg S. (2016) Biofilms: an emergent form of bacterial life. *Nature Reviews Microbiology* 14(9):563-575. DOI: 10.1038/nrmicro.2016.94
52. Costa OYA, Raaijmakers JM, Kuramae EE. (2018) Microbial extracellular polymeric substances: ecological function and impact on soil aggregation. *Frontiers in Microbiology* 9:1636. DOI: 10.3389/fmicb.2018.01636
53. Paparella S, Araujo SS, Rossi G, Wijayasinghe M, Carbonera D, Balestrazzi A. (2015) Seed priming: state of the art and new perspectives. *Plant Cell Reports* 34(8):1281-1293. DOI: 10.1007/s00299-015-1784-y

### Soybean Genome
54. Schmutz J, Cannon SB, Schlueter J, Ma J, Mitros T, Nelson W, et al. (2010) Genome sequence of the palaeopolyploid soybean. *Nature* 463(7278):178-183. DOI: 10.1038/nature08670

### General Germination Biology
55. Shu K, Liu XD, Xie Q, He ZH. (2016) Two faces of one seed: hormonal regulation of dormancy and germination. *Molecular Plant* 9(1):34-45. DOI: 10.1016/j.molp.2015.08.010
56. Rajjou L, Duval M, Gallardo K, Catusse J, Bally J, Job C, Job D. (2012) Seed germination and vigor. *Annual Review of Plant Biology* 63:507-533. DOI: 10.1146/annurev-arplant-042811-105550
57. Bewley JD, Bradford KJ, Hilhorst HWM, Nonogaki H. (2013) Seeds: Physiology of Development, Germination and Dormancy. 3rd Edition. Springer. ISBN: 978-1-4614-4692-7. DOI: 10.1007/978-1-4614-4693-4

### Experimental Methods References
58. Vandesompele J, De Preter K, Pattyn F, Poppe B, Van Roy N, De Paepe A, Speleman F. (2002) Accurate normalization of real-time quantitative RT-PCR data by geometric averaging of multiple internal control genes. *Genome Biology* 3(7):research0034. DOI: 10.1186/gb-2002-3-7-research0034
59. Andersen CL, Jensen JL, Orntoft TF. (2004) Normalization of real-time quantitative reverse transcription-PCR data: a model-based variance estimation approach. *Cancer Research* 64(15):5245-5250. DOI: 10.1158/0008-5472.CAN-04-0496
60. Livak KJ, Schmittgen TD. (2001) Analysis of relative gene expression data using real-time quantitative PCR and the 2^-DDCt method. *Methods* 25(4):402-408. DOI: 10.1006/meth.2001.1262
61. Schmittgen TD, Livak KJ. (2008) Analyzing real-time PCR data by the comparative C~T~ method. *Nature Protocols* 3(6):1101-1108. DOI: 10.1038/nprot.2008.73
62. German MA, Pillay M, Jeong DH, Hetawal A, Luo S, Janardhanan P, Kannan V, Rymarquis LA, Nobuta K, German R, De Paoli E, Lu C, Schroth G, Meyers BC, Green PJ. (2008) Global identification of microRNA-target RNA pairs by parallel analysis of RNA ends. *Nature Biotechnology* 26(8):941-946. DOI: 10.1038/nbt1417
63. Fehr WR, Caviness CE. (1977) Stages of soybean development. Special Report 80. Iowa State University. 11 pp.

---

## Annotation Flags and Data Quality Notes

1. **GLYMA_09G19270**: Truncated gene ID corrected to **GLYMA_09G192700** based on SoyBase validation (chromosome 9, positions 41,734,808-41,738,603). GLYMA_09G019270 is not a valid gene.

2. **KRH5227**: Truncated protein accession. Likely KRH52271 or KRH52270; both map to GLYMA_06G057500. Original source data should be verified.

3. **KRH47986 annotation conflict**: Original list says "cation transport regulator-like protein 2-like" but SoyBase/NCBI maps to GLYMA_07G060700 annotated as CURT1-like thylakoid membrane protein (AT4G01150 homolog). CURT1 proteins are NOT cation transporters. The KRH47986 NCBI record was removed. Possible explanations: annotation pipeline version differences, the removed record may have had a different annotation, or the original label came from automated BLAST annotation against a different database.

4. **GLYMA_06G259700v4**: The "v4" suffix is an annotation version marker (Wm82.a4.v1), not part of the canonical gene ID. Correct ID is GLYMA_06G259700.

5. **Three removed NCBI records**: KRH47986, KRH33075, and KRH25272 have been removed from NCBI, indicating these gene models may have been revised in newer genome assemblies.

6. **Six uncharacterized targets**: GLYMA_10G097500, GLYMA_10G268800, GLYMA_06G057500, GLYMA_12G091900, GLYMA_08G231200, and GLYMA_01G091700 remain poorly characterized with no experimentally validated function. Recommended for InterProScan domain prediction or AlphaFold structure analysis.

7. **Bioinformatic false positive rate**: Computational prediction of sRNA-mRNA complementarity in a 1.1 Gb paleopolyploid genome with ~75% gene duplication has inherently high false positive rates. Validation by RT-qPCR of at least 5-8 high-priority targets is essential before mechanistic claims can be considered supported.
