# Molecular Biology of Wheat (Triticum aestivum) Seed Germination: A Comprehensive Review with Implications for sRNA-Mediated Gene Regulation

## Abstract

Wheat (*Triticum aestivum* L.) is a hexaploid cereal (AABBDD genome, 2n = 6x = 42) whose seed germination biology is governed by an intricate network of hormonal, redox, metabolic, and developmental signaling pathways. This review synthesizes current knowledge of the molecular mechanisms underpinning wheat germination and early seedling establishment, with emphasis on how targeted downregulation of specific gene classes -- as might be achieved through bacterial extracellular small RNA (esRNA)-mediated gene silencing -- could enhance germination vigor. We examine the ABA/GA hormonal axis, endosperm mobilization, reactive oxygen species (ROS) homeostasis, polyamine metabolism, auxin signaling, chloroplast membrane biogenesis, cytoskeletal dynamics, organelle gene expression, ribosome biogenesis, and magnesium transport. For each pathway, we evaluate whether transient downregulation of key genes would be predicted to promote or impair germination.

---

## 1. ABA/GA Balance in Wheat Germination

### 1.1 ABA in Dormancy Maintenance

Abscisic acid (ABA) is the central hormone maintaining seed dormancy in wheat. The transition from dormancy to germination requires a decline in both ABA content and ABA sensitivity (Barrero et al., *Plant Physiology*, 2009; Son et al., *Plant Cell & Environment*, 2016). Genetic variation in wheat seed dormancy is highly correlated with ABA content, which is closely associated with the expression levels of ABA biosynthesis genes *TaNCED1* and *TaNCED2*, as well as the downstream transcription factor *TaABI5* (Tuttle et al., *Plant Cell & Environment*, 2022). The wheat ortholog of *VIVIPAROUS1* (*TaVP1*), a B3-domain transcription factor homologous to Arabidopsis *ABI3*, modulates ABA responsiveness during seed maturation. Transgenic studies with *Avena fatua VP1* demonstrated that constitutive expression enhanced ABA sensitivity and suppressed germination, though natural variation in *TaVP1* expression levels alone does not fully account for dormancy differences among wheat cultivars (McKibbin et al., *Plant Molecular Biology*, 2002; Nakamura & Toyama, *Cereal Chemistry*, 2001).

The ABA signaling core -- comprising PYR/PYL receptors, group A PP2C phosphatases, and SnRK2 kinases -- is functionally conserved in wheat. Critically, TaPP2C-a10 interacts with subclass III TaSnRK2 kinases and, when overexpressed, promotes seed germination and decreases ABA sensitivity (Yu et al., *Plant Cell Reports*, 2020). The recently characterized TaPP2C-a5 undergoes alternative splicing to produce two isoforms that coordinately negatively regulate seed dormancy (Li et al., *Journal of Advanced Research*, 2025). After-ripening-mediated dormancy release involves transcriptional repression of *PP2C*, *SnRK2*, and *ABI5* genes (Barrero et al., *PLoS ONE*, 2013). These findings have direct implications for esRNA-mediated strategies: downregulation of ABA signaling components such as *ABI5* or *SnRK2* kinases would be predicted to phenocopy after-ripening and promote germination.

### 1.2 GA Signaling and DELLA Protein Degradation

Gibberellins (GA) antagonize ABA by promoting DELLA protein degradation via the 26S proteasome. In wheat, the DELLA proteins encoded by *Rht-B1* and *Rht-D1* (orthologs of barley *SLN1*) are GA signaling repressors. GA-mediated proteasome-dependent degradation of SLN1 is necessary for derepression of downstream responses including GAMYB transcription and alpha-amylase induction in the aleurone (Fu et al., *Plant Cell*, 2002; Gubler et al., *Plant Physiology*, 2002). In wheat aleurone cells, GA-dependent alpha-amylase expression is also mediated by TOR (target of rapamycin) signaling, where TaTOR-TaS6K1 signaling contributes to GA-dependent germination by mediating alpha-amylase synthesis and controlling proteasomal degradation of Rht-1 (Luo et al., *Plant Signaling & Behavior*, 2023). Mutations in the DELLA domain of *Rht* genes (e.g., *Rht-B1b*, *Rht-D1b*) confer GA insensitivity, producing semidwarf phenotypes that revolutionized wheat breeding during the Green Revolution but also reduce alpha-amylase activity in germinating seeds.

### 1.3 Pre-Harvest Sprouting and Dormancy QTLs

Pre-harvest sprouting (PHS) -- premature germination on the mother plant before harvest -- is a major wheat-specific problem linked to insufficient seed dormancy, causing annual losses exceeding USD 1 billion globally. The causal gene for the major PHS resistance QTL *Qphs.pseru-3AS* is *TaPHS1* (also designated *TaMFT-3A*), a MOTHER OF FLOWERING TIME-like gene that positively regulates ABA sensitivity and enhances dormancy (Liu et al., *Genetics*, 2013). Two causal mutations in *TaPHS1* jointly determine PHS resistance. Additional loci include *TaMKK3* on chromosome 4AL and *TaQsd1* on 5BL, the latter encoding an alanine aminotransferase expressed specifically in embryos. Gene pyramiding studies demonstrated that *TaPHS1* most consistently increases PHS resistance in wheat and triticale (Shorinola et al., *Molecular Breeding*, 2022). For esRNA-mediated improvement of germination, the target logic would be inverted relative to PHS resistance: transient downregulation of *TaPHS1/TaMFT* during imbibition could accelerate the dormancy-to-germination transition.

---

## 2. Endosperm Mobilization

### 2.1 Aleurone Layer Biology

The aleurone layer, typically 1-3 cells thick in wheat, is the metabolically active tissue responsible for synthesizing hydrolytic enzymes upon perception of embryo-derived GA. During germination, GA induces GAMYB transcription factor expression, which transactivates alpha-amylase gene promoters through binding to the GARE (GA-responsive element) motif TAACAAA (Gubler et al., *Plant Cell*, 1995). In rice, loss-of-function mutations of *OsGAMYB* abolish alpha-amylase expression in the endosperm in response to GA treatment (Kaneko et al., *Plant Cell*, 2004). In barley, SLN1 protein levels decline rapidly in response to GA before any increase in GAMYB levels, establishing the temporal order: GA perception, DELLA degradation, GAMYB expression, then alpha-amylase transcription (Gubler et al., *Plant Physiology*, 2002).

Upon programmed cell death (PCD), aleurone cells release alpha-amylases, proteases, cell wall-degrading enzymes, and other hydrolases into the starchy endosperm, providing carbohydrates, amino acids, and minerals to the growing embryo. The alpha-amylase gene family in wheat includes multiple isozymes with distinct biochemical properties, and their differential regulation contributes to both normal germination and to quality defects such as late maturity alpha-amylase (LMA) (Mares & Mrva, *Planta*, 2022).

### 2.2 Sugar Sensing and Hexokinase Signaling

Hexokinase (HXK) functions as both a glycolytic enzyme and a glucose sensor in plants (Smeekens, *Annual Review of Plant Biology*, 2000). In wheat embryos, glucose concentration acts as a bidirectional signal: low glucose stimulates germination by promoting ABA catabolism, whereas high glucose delays germination by inducing ABA biosynthesis and signaling (Cho et al., *Trends in Plant Science*, 2006; Granot et al., *BMC Plant Biology*, 2013). The HXK1-glycolytic pathway provides the ATP and metabolic intermediates necessary to fuel post-germinative cell division and expansion, a function particularly critical before the transition to photoautotrophic growth (Andriotis et al., *bioRxiv*, 2019). Sugar sensing integrates with TOR kinase and SnRK1 signaling to coordinate carbon availability with growth decisions, forming a metabolic checkpoint during germination.

---

## 3. ROS and Redox in Wheat Germination

### 3.1 The Oxidative Window Concept

Bailly et al. (2008) proposed the "oxidative window for germination," a foundational concept in cereal seed biology (*Comptes Rendus Biologies*; also *Plant Signaling & Behavior*, 2008). This model holds that seed germination is only possible when intracellular ROS levels fall within a defined range: below this window, insufficient ROS signaling prevents dormancy release; above it, oxidative damage impairs cellular function. ROS, particularly H2O2, act as signaling molecules that promote dormancy release by interfering with ABA signaling and promoting GA responsiveness (Bailly et al., *Plant Signaling & Behavior*, 2008; Ye et al., *Frontiers in Plant Science*, 2020). In barley, the interrelationship between ABA and ROS plays a key role in the dormancy-to-germination transition, with lower ABA levels associated with higher H2O2 and enhanced germination capacity (Ishibashi et al., *Frontiers in Plant Science*, 2017).

### 3.2 Class III Peroxidases

Wheat possesses an exceptionally large class III peroxidase (POD) gene family, with 374 members identified across the hexaploid genome (Wang et al., *BMC Genomics*, 2019). These enzymes perform dual functions: generating ROS (O2^.- via the oxidative cycle) and scavenging ROS (H2O2 via the peroxidative cycle). A specific member, TaPer12-3A, was recently shown to negatively regulate seed dormancy and positively mediate germination by maintaining H2O2 homeostasis through scavenging excess H2O2 (Han et al., *BMC Plant Biology*, 2024). TaPer12-3A expression was consistently higher in wheat genotypes with weak dormancy, and its heterologous overexpression in rice and Arabidopsis enhanced germination rates. This demonstrates that modulating the ROS-scavenging capacity of individual peroxidases can shift the oxidative window to favor germination. Downregulation of specific class III peroxidases that generate ROS in the apoplast could, in principle, help maintain the oxidative window in a germination-permissive range.

### 3.3 Alternative Oxidase (AOX) and Mitochondrial Respiration

The mitochondrial alternative oxidase (AOX) directly couples ubiquinol oxidation with O2 reduction to water, bypassing proton-pumping complexes III and IV, thereby dramatically reducing the ATP yield of respiration (Vanlerberghe, *International Journal of Molecular Sciences*, 2013). Under non-stress conditions, AOX promotes seed germination progression. In wheat seedlings, exposure to continuous light upregulated *AOX1a* expression, consistent with the increased alternative pathway capacity observed during the greening of etiolated wheat seedlings (Saha et al., *Journal of Plant Physiology*, 2015). AOX also modulates ABA signaling and ROS homeostasis: in Arabidopsis, AOX2 influences seed germination under salt stress by adjusting ROS levels (Zheng et al., *Environmental and Experimental Botany*, 2024). Paradoxically, while AOX reduces ATP production, its ROS-dampening role is critical during the metabolic burst of early germination, preventing excessive oxidative stress that could push ROS levels above the oxidative window.

### 3.4 PARP and NAD+ Depletion

Poly(ADP-ribose) polymerases (PARPs) catalyze poly(ADP-ribosyl)ation using NAD+ as a substrate, a process activated by DNA damage and oxidative stress. In plants, PARP activation under stress consumes NAD+ and depletes the ATP pool, creating an energy crisis (De Block et al., *Plant Journal*, 2005). Crucially, PARP downregulation or chemical inhibition has consistently been shown to improve plant growth, stress tolerance, and energy homeostasis. PARP-deficient plants maintain NAD+ levels, reduce mitochondrial ROS formation, and show enhanced biomass production (De Block et al., *Plant Journal*, 2005; Schulz et al., *PLoS ONE*, 2012). AtPARP3 is specifically expressed in seeds, and its promoter activity coincides with ROS accumulation in the embryo (Rissel et al., *BMC Plant Biology*, 2019). During seed germination, when DNA damage repair is active and ROS are generated, PARP activity could represent an energy drain. **Therefore, transient PARP downregulation via esRNA-mediated silencing represents a particularly compelling strategy for improving germination vigor**, as it would conserve NAD+ and ATP for biosynthetic processes while reducing oxidative stress.

---

## 4. Polyamine Metabolism

### 4.1 The ADC Pathway in Wheat

In wheat and other plants, putrescine biosynthesis occurs primarily via the arginine decarboxylase (ADC) pathway, where arginine is decarboxylated to agmatine and subsequently converted to putrescine (Alcazar et al., *Plant Physiology and Biochemistry*, 2010). Putrescine is then sequentially converted to spermidine and spermine by spermidine synthase and spermine synthase, respectively, using decarboxylated S-adenosylmethionine (dcSAM) as the aminopropyl donor. Transgenic wheat expressing an oat *ADC* cDNA constitutively exhibited 7-fold increases in putrescine, 2.5-fold increases in spermidine, and 1.8-fold increases in spermine in seeds (Bassie et al., *Molecular Breeding*, 2008). ADC activity is highest during germination of high-viability seeds and declines with loss of viability, correlating closely with agmatine content (Sinska & Lewandowska, *Plant Growth Regulation*, 1991).

### 4.2 Polyamine-ABA Crosstalk

The polyamine-hormone interaction network is nuanced and consequential for germination. Putrescine is positively linked to the expression of ABA biosynthesis genes but downregulates gibberellin biosynthesis genes, while spermidine exerts exactly the opposite effects (Alcazar et al., *Polyamines*, 2014). During seed germination, an increase in the (spermidine + spermine) : putrescine ratio is observed in embryos, suggesting a shift from ABA-promoting to GA-promoting polyamine profiles (Pieruzzi et al., *BMC Plant Biology*, 2011). This ratio shift implies that ADC downregulation -- which would reduce putrescine accumulation -- could potentially enhance germination by reducing ABA biosynthesis gene expression and alleviating dormancy. However, ADC activity is also critical for stress tolerance during imbibition; under osmotic stress, ADC activity increases dramatically and elevated putrescine is protective (Bouchereau et al., *Journal of Plant Physiology*, 1999). Thus, **the effect of ADC downregulation on germination is context-dependent**: beneficial under non-stress conditions by shifting the polyamine ratio, but potentially detrimental under abiotic stress.

---

## 5. Auxin Signaling and Seedling Emergence

### 5.1 The ARF Family in Wheat

Auxin response factors (ARFs) are plant-specific transcription factors that bind to auxin response elements (AuxREs) to activate or repress target gene expression. A genome-wide survey of hexaploid wheat identified 69 *TaARF* members organized into 24 homoeologous groups (Qiao et al., *Frontiers in Plant Science*, 2018; Bouzroud et al., *South African Journal of Botany*, 2020). Twenty *TaARF* members were expressed differentially across roots, stems, and leaves of wheat seedlings, with expression significantly altered by exogenous auxin treatment (Qiao et al., *Frontiers in Plant Science*, 2018).

### 5.2 Auxin in Radicle Emergence and Coleoptile Elongation

Auxin is critical for radicle emergence and the establishment of gravitropic growth in wheat seedlings. ARFs regulate root gravitropism, cell elongation, and vascular patterning. *TaARF4* determines root length and plant height in wheat, placing it at a key node in seedling establishment. The ARF-Aux/IAA interaction module provides combinatorial specificity: in the absence of auxin, Aux/IAA repressors heterodimerize with ARFs to block target gene transcription; auxin promotes Aux/IAA degradation via the SCF^TIR1 ubiquitin ligase, releasing ARFs (Vernoux et al., *Molecular Cell*, 2011). Downregulation of specific ARF repressors (those with Q-rich middle regions that function as transcriptional repressors) could constitutively activate auxin-responsive genes and promote radicle elongation, though excessive auxin signaling can also inhibit growth through feedback mechanisms.

---

## 6. Chloroplast Transition and Membrane Lipids

### 6.1 SQD1 and Sulfolipid Biosynthesis

UDP-sulfoquinovose synthase (SQD1) catalyzes the first committed step in sulfolipid (sulfoquinovosyldiacylglycerol, SQDG) biosynthesis, converting UDP-glucose and sulfite to UDP-sulfoquinovose (Mulichak et al., *PNAS*, 1999; Sanda et al., *Journal of Biological Chemistry*, 2001). SQDG is found predominantly in thylakoid membranes and constitutes one of the three non-phosphorous glycolipids of the photosynthetic membrane. SQD1 expression is dramatically upregulated (up to 15-fold) under phosphate limitation, when SQDG substitutes for phosphatidylglycerol to conserve phosphate (Essigmann et al., *PNAS*, 1998).

### 6.2 Relevance to Germination

During seed germination, the embryo grows heterotrophically in darkness before transitioning to photoautotrophic growth upon de-etiolation. Thylakoid membrane assembly and SQDG biosynthesis are not required during the dark, heterotrophic phase of germination. Arabidopsis *sqd2* mutants (deficient in sulfolipid synthase, downstream of SQD1) showed impaired growth only under phosphate-limited conditions (Yu et al., *PNAS*, 2002). **Therefore, transient downregulation of SQD1 during the pre-photosynthetic germination phase is predicted to be metabolically neutral or mildly beneficial**, as it would redirect UDP-glucose toward glycolysis and cell wall biosynthesis rather than sulfolipid production, potentially improving energy availability for the germinating seedling. Only upon greening would SQD1 expression become necessary for functional thylakoid membrane assembly.

---

## 7. Cytoskeletal Dynamics

### 7.1 Kinesin Motor Proteins

The wheat kinesin superfamily comprises 155 genes (*TaKIN*) that participate in cell division, intracellular transport, and cell elongation (Wang et al., *BMC Genomics*, 2024). Kinesins control microtubule dynamics during mitosis and cytokinesis, and specific members regulate root hair growth and cytoskeletal organization. Transcript profiling revealed that some *TaKIN* genes are downregulated in the radicle during early seedling development, suggesting developmental regulation of motor protein expression (Wang et al., *BMC Genomics*, 2024). The wheat homolog *TaMRH2a*, a kinesin-family gene, regulates cytoskeleton organization and root hair growth. Loss of function of specific kinesins results in randomly oriented microtubules and aberrant cell expansion, indicating that any esRNA-mediated downregulation of kinesin genes must be carefully targeted to non-essential family members.

### 7.2 Profilin and Actin Dynamics

Profilins are small (12-15 kDa) actin-binding proteins that regulate actin polymerization by catalyzing ADP/ATP exchange on actin monomers (Bao et al., *Frontiers in Plant Science*, 2015). The actin cytoskeleton drives cell expansion, vesicle trafficking, organelle movement, and polar growth during radicle emergence and coleoptile elongation. In Arabidopsis, overexpression of *Profilin 3* altered F-actin organization and affected cell elongation (Fan et al., *Plant Cell Reports*, 2013). In the context of germination, profilin levels must be finely tuned: too little profilin reduces the pool of polymerization-competent actin monomers, while excess profilin sequesters monomers and reduces filament density. **Downregulation of profilin during germination would likely impair the rapid cell elongation required for radicle protrusion and coleoptile growth, making it an unfavorable target for esRNA-mediated silencing.**

---

## 8. Organelle Gene Expression: PPR Proteins

Pentatricopeptide repeat (PPR) proteins constitute one of the largest protein families in land plants (over 450 members in wheat), are encoded by nuclear genes, and are imported into mitochondria or chloroplasts where they mediate virtually all post-transcriptional RNA processing events (Barkan & Small, *Annual Review of Plant Biology*, 2014; Ren et al., *Plant Communications*, 2025). PPR functions include RNA editing (C-to-U), intron splicing, transcript stabilization, and translational regulation. P-type PPR proteins predominantly participate in RNA splicing and translation, while PLS-type PPR proteins are primarily responsible for RNA editing (Chen et al., *Frontiers in Plant Science*, 2021).

During germination, mitochondrial biogenesis is critical for the resumption of aerobic respiration, and chloroplast gene expression must be activated for the eventual transition to photosynthesis. PPR protein function is therefore essential for organelle function at both stages. However, the large PPR family contains members with highly specific, sometimes redundant functions. Downregulation of individual PPR proteins that are dispensable during germination (e.g., those involved in chloroplast transcript maturation not required during the heterotrophic phase) could theoretically be tolerated without phenotypic consequence. Conversely, silencing PPR proteins involved in mitochondrial Complex I or Complex III assembly would impair respiration and be detrimental to germination.

---

## 9. Ribosome Biogenesis

### 9.1 The PeBoW Complex and BOP1

The PeBoW complex, comprising PES (Pescadillo), BOP1 (Block of Proliferation 1), and WDR12, localizes to the nucleolus and is essential for 60S ribosomal large subunit assembly and 25S rRNA maturation in plants (Cho et al., *Plant Journal*, 2013; Ahn et al., *Journal of Experimental Botany*, 2016). BOP1 is essential for seed viability, and its transient silencing in tobacco caused defective ribosome biogenesis, repressed global protein translation, altered nucleolar structure, and delayed cell growth (Ahn et al., *Journal of Experimental Botany*, 2016).

### 9.2 Translation During Germination

Wheat seeds store thousands of mRNAs in the dry state: approximately 38% of transcripts represented on the GeneChip Wheat Genome Array are found in mature dormant wheat seeds (Barrero et al., *PLoS ONE*, 2012; Bai et al., *Plants*, 2020). Upon imbibition, these stored mRNAs are selectively loaded onto polysomes and translated before de novo transcription commences, enabling rapid resumption of metabolic activity. The translational machinery stored in dry seeds is already effective within the first 0-8 hours after imbibition (Bai et al., *Plant Physiology*, 2020). **Downregulation of BOP1 or other ribosome biogenesis factors during germination would be highly detrimental**, as it would reduce the translational capacity needed to synthesize the proteome required for radicle emergence and seedling growth. Ribosome biogenesis represents a fundamental bottleneck during germination and should not be targeted.

---

## 10. Magnesium Transport

### 10.1 The MRS2/MGT Family in Wheat

Twenty-four *TaMGT* genes have been identified across 18 wheat chromosomes, with 20 members predicted to localize to chloroplasts and potentially also to mitochondria and the cytoplasm (Ma et al., *Frontiers in Plant Science*, 2023). These CorA-type transporters maintain Mg2+ homeostasis, which is essential for chlorophyll biosynthesis, photosynthetic enzyme activity (including RuBisCO), ribosome function (Mg2+ stabilizes ribosomal subunit association), and as a cofactor for hundreds of enzymes including kinases and phosphatases (Gebert et al., *New Phytologist*, 2009; Li et al., *Plant and Cell Physiology*, 2016).

### 10.2 Relevance to Germination

During the heterotrophic phase of germination, Mg2+ demand is primarily for ribosomal function (both cytoplasmic and mitochondrial), enzyme activation (particularly kinases involved in ABA/GA signaling), and ATP-Mg2+ complexes required for energy metabolism. Chloroplast-localized MGT transporters become critical only upon greening. Downregulation of chloroplast-targeted MGT transporters during early germination may be tolerable, as photosynthetic Mg2+ demand is minimal. However, silencing of cytoplasmic or mitochondrial Mg2+ transporters could impair translation and respiration. Expression profiling showed that *TaMGT* genes are differentially regulated across developmental stages and under abiotic stress (Ma et al., *Frontiers in Plant Science*, 2023), suggesting that some family members are functionally specialized for post-germination growth rather than germination per se.

---

## Integrative Discussion: Implications for esRNA-Mediated Gene Downregulation

Bacterial extracellular sRNAs offer a mechanism for transient, non-heritable gene silencing in the plant host during the germination window. Based on the molecular mechanisms reviewed above, we can categorize potential gene targets by their predicted effects on germination and seedling vigor:

### Targets Where Downregulation Is Predicted to Be Beneficial

1. **PARP genes**: Downregulation conserves NAD+ and ATP, reduces ROS-mediated cellular damage, and improves energy homeostasis -- one of the most robust growth-promoting effects documented in plant biology.
2. **ABA signaling components** (*ABI5*, *SnRK2*, *TaPHS1/TaMFT*): Transient reduction in ABA sensitivity would accelerate the dormancy-to-germination transition, mimicking the natural after-ripening program.
3. **PP2C phosphatases** (paradox note): While PP2Cs are negative regulators of ABA signaling in the canonical pathway, their downregulation in wheat specifically has complex effects depending on the family member; careful target selection is essential.
4. **SQD1**: During the dark, heterotrophic germination phase, sulfolipid biosynthesis is dispensable, and downregulation may redirect UDP-glucose toward energy-producing pathways.

### Targets Where Downregulation Is Context-Dependent

5. **ADC (arginine decarboxylase)**: Reduces putrescine accumulation and may shift the polyamine ratio to favor germination under non-stress conditions, but could compromise osmotic stress tolerance during imbibition.
6. **Specific class III peroxidases**: Depending on whether the targeted member generates or scavenges ROS, downregulation could fine-tune the oxidative window in either direction.
7. **Chloroplast-targeted PPR proteins and MGT transporters**: Dispensable during the pre-photosynthetic phase but essential after de-etiolation.

### Targets Where Downregulation Would Be Detrimental

8. **BOP1 and ribosome biogenesis factors**: Translation capacity is the rate-limiting step during early germination and must not be compromised.
9. **Kinesin and profilin**: Required for the cell division and elongation that drive radicle emergence.
10. **AOX**: Needed to manage ROS during the metabolic burst of germination; its loss would push ROS above the oxidative window.
11. **Mitochondrial PPR proteins**: Essential for respiratory complex assembly.

---

## Conclusions

Wheat germination biology is characterized by several features unique to or accentuated in hexaploid cereals: the large aleurone layer mediating endosperm mobilization, the PHS problem requiring carefully calibrated dormancy, the enormous class III peroxidase family managing ROS homeostasis, and the polyploid genome providing functional redundancy across homoeologs. The molecular mechanisms governing germination -- ABA/GA antagonism, ROS signaling within the oxidative window, stored mRNA translation, and metabolic reprogramming -- offer multiple nodes where bacterial esRNA-mediated gene silencing could theoretically improve germination vigor. The most promising targets are those involved in energy-consuming processes dispensable during germination (PARP, SQD1) or in maintaining dormancy that must be overcome (ABI5, SnRK2). Conversely, genes encoding fundamental machinery for translation (BOP1), cytoskeletal dynamics (kinesin, profilin), and mitochondrial respiration (AOX, mitochondrial PPR proteins) represent targets where downregulation would be counterproductive.

The hexaploid wheat genome provides an additional layer of complexity and opportunity: homoeologous gene copies on the A, B, and D sub-genomes may be differentially expressed during germination, and esRNA-mediated silencing may preferentially target one homoeolog while leaving others functional, providing a degree of built-in robustness against complete loss of function.

---

## References

Ahn CS, Cho HK, Lee DH, Sim HJ, Kim SG, Pai HS. Functional characterization of the ribosome biogenesis factors PES, BOP1, and WDR12 (PeBoW), and mechanisms of defective cell growth and proliferation caused by PeBoW deficiency in Arabidopsis. *Journal of Experimental Botany*. 2016;67(17):5217-5232.

Alcazar R, Altabella T, Marco F, Bortolotti C, Reymond M, Koncz C, Carrasco P, Tiburcio AF. Polyamines: molecules with regulatory functions in plant abiotic stress tolerance. *Planta*. 2010;231(6):1237-1249.

Bai B, Novak O, Ljung K, Hanson J, Bentsink L. Lost in Translation: Physiological Roles of Stored mRNAs in Seed Germination. *Plants*. 2020;9(3):347.

Bailly C, El-Maarouf-Bouteau H, Corbineau F. From intracellular signaling networks to cell death: the dual role of reactive oxygen species in seed physiology. *Comptes Rendus Biologies*. 2008;331(10):806-814.

Barkan A, Small I. Pentatricopeptide repeat proteins in plants. *Annual Review of Plant Biology*. 2014;65:415-442.

Barrero JM, Millar AA, Griffiths J, Czechowski T, Scheible WR, Udvardi M, Reid JB, Ross JJ, Jacobsen JV, Gubler F. Gene expression profiling identifies two regulatory genes controlling dormancy and ABA sensitivity in Arabidopsis seeds. *Plant Journal*. 2010;61(4):611-622.

Barrero JM, Cavanagh C, Verbyla KL, Tibbits JFG, Verbyla AP, Huang BE, Rosewarne GM, Stephen S, Wang P, Whan A, Rigault P, Hayden MJ, Gubler F. Transcriptomic analysis of wheat near-isogenic lines identifies PM19-A1 and A2 as candidates for a major dormancy QTL. *Genome Biology*. 2015;16:93.

Bassie L, Noury M, Lepri O, Lahaye T, Christou P, Capell T. Transgenic wheat plants expressing an oat arginine decarboxylase cDNA exhibit increases in polyamine content in vegetative tissue and seeds. *Molecular Breeding*. 2008;21:187-200.

Cho HK, Ahn CS, Lee HS, Kim JK, Pai HS. Pescadillo plays an essential role in plant cell growth and survival by modulating ribosome biogenesis. *Plant Journal*. 2013;76(4):609-621.

De Block M, Verduyn C, De Brouwer D, Cornelissen M. Poly(ADP-ribose) polymerase in plants affects energy homeostasis, cell death and stress tolerance. *Plant Journal*. 2005;41(1):95-106.

Essigmann B, Guler S, Narang RA, Linke D, Benning C. Phosphate availability affects the thylakoid lipid composition and the expression of SQD1, a gene required for sulfolipid biosynthesis in Arabidopsis thaliana. *PNAS*. 1998;95(4):1950-1955.

Fu X, Richards DE, Ait-Ali T, Hynes LW, Ougham H, Peng J, Harberd NP. Gibberellin-mediated proteasome-dependent degradation of the barley DELLA protein SLN1 repressor. *Plant Cell*. 2002;14(12):3191-3200.

Gubler F, Kalla R, Roberts JK, Jacobsen JV. Gibberellin-regulated expression of a myb gene in barley aleurone cells: evidence for Myb transactivation of a high-pI alpha-amylase gene promoter. *Plant Cell*. 1995;7(11):1879-1891.

Gubler F, Chandler PM, White RG, Llewellyn DJ, Jacobsen JV. Gibberellin signaling in barley aleurone cells. Control of SLN1 and GAMYB expression. *Plant Physiology*. 2002;129(1):191-200.

Han Y, Liu S, Wei Y, Zhang X, Wang Y, Shi G, Li J, Liu D, Zhang A. Functional analysis of a wheat class III peroxidase gene, TaPer12-3A, in seed dormancy and germination. *BMC Plant Biology*. 2024;24:41.

Ishibashi Y, Aoki N, Kasa S, Sakamoto M, Kai K, Tomokiyo R, Watabe G, Yuasa T, Iwaya-Inoue M. The interrelationship between abscisic acid and reactive oxygen species plays a key role in barley seed dormancy and germination. *Frontiers in Plant Science*. 2017;8:275.

Kaneko M, Inukai Y, Ueguchi-Tanaka M, Itoh H, Izawa T, Kobayashi Y, Hattori T, Miyao A, Hirochika H, Ashikari M, Matsuoka M. Loss-of-function mutations of the rice GAMYB gene impair alpha-amylase expression in aleurone and flower development. *Plant Cell*. 2004;16(1):33-44.

Liu S, Sehgal SK, Li J, Lin M, Trick HN, Yu J, Gill BS, Bai G. Cloning and characterization of a critical regulator for preharvest sprouting in wheat. *Genetics*. 2013;195(1):263-272.

Luo H, Wang Q, Guo Y, Li F, Li Z, Zhang Y. Gibberellic-acid-dependent expression of alpha-amylase in wheat aleurone cells is mediated by target of rapamycin (TOR) signaling. *Plant Signaling & Behavior*. 2023;18(1).

Ma W, Zhang Y, Li W, Du B, Liu J, Wang Z, Li J. Uncovering the role of wheat magnesium transporter family genes in abiotic responses. *Frontiers in Plant Science*. 2023;14:1078299.

Mulichak AM, Theisen MJ, Essigmann B, Benning C, Garavito RM. Crystal structure of SQD1, an enzyme involved in the biosynthesis of the plant sulfolipid headgroup donor UDP-sulfoquinovose. *PNAS*. 1999;96(23):13097-13102.

Qiao L, Zhang W, Li X, Zhang L, Zhang X, Li X, Guo H, Ren Y, Zheng J, Chang Z. Characterization and expression patterns of auxin response factors in wheat. *Frontiers in Plant Science*. 2018;9:1395.

Ren R, Yan X, Zhao Y, Wei Y. Pentatricopeptide repeat proteins in plants: Cellular functions, action mechanisms, and potential applications. *Plant Communications*. 2025;6(1).

Rissel D, Heym PP, Peiter E. A yeast growth assay to characterize plant poly(ADP-ribose) polymerase (PARP) proteins and inhibitors. *Analytical Biochemistry*. 2017;527:20-23.

Sanda S, Leustek T, Theisen MJ, Garavito RM, Benning C. Recombinant Arabidopsis SQD1 converts UDP-glucose and sulfite to the sulfolipid head group precursor UDP-sulfoquinovose in vitro. *Journal of Biological Chemistry*. 2001;276(6):3941-3946.

Schulz P, Neukermans J, Van der Kelen K, Muhlenbock P, Van Breusegem F, Noctor G, Teige M, Metzlaff M, Hannah MA. Chemical PARP inhibition enhances growth of Arabidopsis and reduces anthocyanin accumulation and the activation of stress protective mechanisms. *PLoS ONE*. 2012;7(5):e37287.

Tuttle KM, Martinez SA, Schramm EC, Takebayashi Y, Seo M, Steber CM. Genetic variation of seed dormancy in wheat (Triticum aestivum L.) is mediated by transcriptional regulation of abscisic acid metabolism and signaling. *Plant Cell & Environment*. 2022;45(12):3621-3635.

Vanlerberghe GC. Alternative oxidase: a mitochondrial respiratory pathway to maintain metabolic and signaling homeostasis during abiotic and biotic stress in plants. *International Journal of Molecular Sciences*. 2013;14(4):6805-6847.

Wang X, Wang H, Liu S, Ferjani A, Li J, Yan J, Yang X, Qin F. Genome-wide and evolutionary analysis of the class III peroxidase gene family in wheat and Aegilops tauschii reveals that some members are involved in stress responses. *BMC Genomics*. 2019;20:666.

Wang Y, Zhang H, Liu J, Hou X, Zhang Y, Fan S, Li X, Gao F, Li X. Genome-wide identification and expression analysis of the kinesin gene superfamily suggests roles in response to abiotic stress and fertility of wheat. *BMC Genomics*. 2024;25:1156.

Ye N, Li H, Zhu G, Liu Y, Liu R, Xu W, Jing Y, Peng X, Zhang J. Advances in the understanding of reactive oxygen species-dependent regulation on seed dormancy, germination, and deterioration in crops. *Frontiers in Plant Science*. 2020;13:826809.

Yu B, Xu C, Benning C. Arabidopsis disrupted in SQD2 encoding sulfolipid synthase is impaired in phosphate-limited growth. *PNAS*. 2002;99(8):5732-5737.

Yu W, Bhatt H, Li Y, Jha S, Rao S, Guo J. Wheat PP2C-a10 regulates seed germination and drought tolerance in transgenic Arabidopsis. *Plant Cell Reports*. 2020;39(5):635-651.
