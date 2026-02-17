# QUINOA (Chenopodium quinoa) -- Mechanistic Claims Extraction

## Overview
- **Organism**: Chenopodium quinoa Willd. (quinoa)
- **Ploidy**: Allotetraploid (2n = 4x = 36; AABB genome; ~1.45 Gb; ~54,499 protein-coding genes)
- **Parentage**: C. pallidicaule (A genome) x C. suecicum (B genome); divergence 3.3-6.3 MYA
- **Family**: Amaranthaceae (Caryophyllales)
- **Treatment**: M-9 bacterial EPS (extracellular polysaccharide) solution; seed soaking
- **Phenotype**: Improved germination rate, improved seedling vigor relative to water controls
- **Total predicted exRNA targets**: 31 transcripts (AUR-series IDs, Jarvis 2017 genome assembly)
- **Evidence level**: Gene-level resolution for 4 fully resolved targets (12.9%); partially resolved for 24 (77.4%); completely unresolved for 3 (9.7%)
- **Unique species features**:
  - Allotetraploid halophyte (germinates at 300-400 mM NaCl)
  - Perisperm (not endosperm) as primary seed reserve tissue (maternally derived, diploid 2n)
  - Betalain antioxidant pigment system (replaces anthocyanins; Caryophyllales synapomorphy)
  - Triterpenoid saponin-coated seed coat (testa), regulated by TSARL1
  - Epidermal bladder cells (EBCs) for salt sequestration (unique to Chenopodioideae)
  - 100% seed-borne Bacillus spp. endophyte colonization with vertical transmission (Pankievicz et al. 2016)
  - Expanded gene families: 30 CqHAK, 34 CqCNGC, 21 CqAGO, 8 CqDCL, 11 CqRDR, 17+ CqCYP76AD, 8 CqDODA

---

## Theme 1: Ion Homeostasis -- K+ and Ca2+ Transport Coordination

### Claims:

- **Claim 1.1**: CqHAK5 (AUR62010943) is a high-affinity K+ transporter of the HAK/KUP/KT superfamily that drives K+ influx under low-K+ conditions; its silencing by bacterial esRNAs would directly affect the turgor-driven radicle cell expansion required for germination.
  - **Gene**: AUR62010943-RA (CqHAK5); 640 aa; Chromosome 2 (Chr02: 54,650,085-54,654,440)
  - **Arabidopsis ortholog**: AT4G13420 (AtHAK5)
  - **UniProt**: Family data in PMC10650088
  - **Direction**: Predicted downregulated by bacterial esRNA
  - **Mechanism**: CqHAK5 is a K+:H+ symporter (Cluster I, Clade IB) that mediates high-affinity K+ uptake at micromolar external K+ concentrations. K+ is the dominant inorganic osmolyte in plant cells (100-200 mM cytoplasmic) and the primary driver of turgor pressure during radicle cell expansion. HAK5-type transporters are activated via the CIPK23/CBL1/9 signaling complex.
  - **Evidence**: HIGH confidence. Confirmed by Ren et al. 2023 (PMC10650088 -- Table 1 mapping). 30 CqHAK family members identified in quinoa (vs ~13 in Arabidopsis), reflecting halophytic adaptation. AtHAK5 is essential for seedling establishment below ~20 uM external K+ (Rubio et al. 2010; Nieves-Cordones et al. 2010).
  - **Germination link**: K+ accumulation in radicle cells lowers water potential, driving osmotic water influx required for cell expansion and mechanical breakthrough of the micropylar endosperm cap -- the rate-limiting step for germination.
  - **HAK/KUP Paradox**: Silencing a K+ importer should impair germination, yet this is the highest-confidence target. Resolution requires context-dependent analysis (see dedicated section below).
  - **References**: Ren et al. 2023 (PMC10650088); Rubio et al. 2008 (Physiol Plant 134:598); Rubio et al. 2010 (Plant Physiol 153:863, PMC2879780); Nieves-Cordones et al. 2010 (Mol Plant 3:326); Rigas et al. 2001 (Plant Cell 13:139)

- **Claim 1.2**: CqCNGC14 (AUR62044372) is a cyclic nucleotide-gated Ca2+ channel that mediates auxin-induced Ca2+ influx; its silencing could reduce ABA-reinforcing Ca2+ signals, thereby accelerating dormancy release and promoting germination.
  - **Gene**: AUR62044372-RA (CqCNGC14); 710 aa; protein-coding
  - **Arabidopsis ortholog**: AT2G24610 (AtCNGC14)
  - **UniProt**: A0A803NE25
  - **Direction**: Predicted downregulated by bacterial esRNA
  - **Mechanism**: CNGC14 is a non-selective cation channel (6 TM domains per subunit, CNBD, CaMBD) permeable to Ca2+, K+, and Na+. Activated by cAMP/cGMP and inhibited by calmodulin (CaM7 specifically inhibits CNGC14). Mediates rapid cytosolic Ca2+ elevation in response to auxin, driving root gravitropism and root hair tip growth. Ca2+ signals through CDPKs phosphorylate and activate SnRK2 kinases, reinforcing ABA signaling. Silencing CNGC14 would dampen Ca2+-dependent ABA reinforcement, facilitating the ABA-to-GA hormonal transition required for dormancy release.
  - **Evidence**: HIGH confidence. Direct Arabidopsis ortholog projection confirmed by EnsemblPlants. Zhang et al. 2024/2025 (SSRN 5070311) identified 34 CqCNGC genes in quinoa (vs 20 in Arabidopsis) with stress-responsive expression. Shih et al. 2015 (PMID:26752079) established CNGC14 role in gravitropism. cngc14 mutants show complete loss of rapid auxin-induced Ca2+ and pH signals (Brost et al. 2019).
  - **Germination link**: Ca2+ is a ubiquitous second messenger during germination. ABA-induced Ca2+ increases maintain dormancy via CDPK-SnRK2-ABI5 signaling. Suppressing CNGC14-mediated Ca2+ influx reduces this ABA-reinforcing loop, potentially accelerating GA-mediated dormancy relief. In the quinoa halophyte context where ABA hyperresponsiveness is pre-adapted, silencing CNGC14 could have a disproportionately large effect on dormancy release compared to glycophytes.
  - **References**: Shih et al. 2015 (Current Biology 25:3119, PMID:26752079); Zhang et al. 2024/2025 (SSRN 5070311); Brost et al. 2019 (Plant Journal 99:910); Brost et al. 2016 (Current Biology 26:67)

- **Claim 1.3**: The co-targeting of K+ (CqHAK5) and Ca2+ (CqCNGC14) transport systems by bacterial esRNAs represents coordinated modulation of the seed ionic environment -- a pattern consistent with deliberate manipulation of the germination-relevant ion signaling network.
  - **Evidence**: [Inferred]. Two of four confirmed targets (50%) belong to ion transport. This overrepresentation relative to genome-wide expectation is statistically notable and biologically coherent: K+ drives radicle turgor pressure while Ca2+ serves as second messenger for ABA/auxin signaling.
  - **Germination link**: Synergistic effect -- K+ modulation affects osmotic/mechanical aspects of radicle emergence while Ca2+ modulation affects hormonal signaling balance.
  - **References**: Inferred from target list enrichment analysis

---

## Theme 2: Defense-Growth Tradeoff -- BAK1 Co-Receptor Competition

### Claims:

- **Claim 2.1**: CqBRL2/VH1-like (AUR62003502) is a BRI1-family LRR receptor-like kinase involved in vascular development and brassinosteroid/auxin signaling, NOT a defense receptor as the generic "LRR-RLK" annotation implies. Its downregulation may shift BAK1 co-receptor availability from immune (PTI) to growth (brassinosteroid/BRI1) signaling.
  - **Gene**: AUR62003502-RA (CqBRL2/VH1-like); 1,071 aa; Scaffold C_Quinoa_Scaffold_2370: 1,521,273-1,524,626 (forward strand)
  - **Arabidopsis ortholog**: AT2G01950 (BRL2/VH1 -- BRI1 Leucine-rich Receptor-Like Kinase 2 / Vascular Highway 1)
  - **UniProt**: A0A803KWU4
  - **Direction**: Predicted downregulated by bacterial esRNA
  - **Mechanism**: BRL2/VH1 is a member of the BRI1 superfamily with 22-25 LRRs and island domain, single-pass TM, and cytoplasmic Ser/Thr kinase domain. Unlike BRI1 itself, BRL2/VH1 does NOT function as a brassinosteroid receptor. It regulates vascular (provascular/procambial) differentiation and phloem transport continuity. Loss-of-function causes discontinuous phloem and premature leaf senescence (Clay and Nelson 2005; Ceserani et al. 2009, PMC2793540). The "Fragment" designation in quinoa annotation suggests partial gene model assembly in v1.0 reference.
  - **CRITICAL ANNOTATION CORRECTION**: Original study labels this as "LRR-RLK" implying defense function. Corrected to BRI1-family vascular/brassinosteroid signaling. This is the most consequential annotation correction in the dataset (Severity: CRITICAL).
  - **Evidence**: HIGH confidence. AT2G01950 confirmed via EnsemblPlants and BioGRID. 171 orthologs across angiosperms indicate high conservation.
  - **Germination link**: In the BAK1 co-receptor competition model, BAK1 is shared between FLS2-BAK1 (immune) and BRI1-BAK1 (growth) complexes (Chinchilla et al. 2007; Lozano-Duran and Zipfel 2015). Downregulation of CqBRL2/VH1 reduces BRI1-family receptor pool competing for BAK1, potentially shifting BAK1 availability toward remaining BRI1 complexes or releasing it from the BRL2 competitive sink. Brassinosteroids promote germination by promoting ABA catabolism and GA synthesis, accelerating dormancy release. The indirect impact on vascular patterning during embryonic axis establishment is a secondary consideration.
  - **References**: Clay and Nelson 2005 (Plant Physiol 138:1527); Ceserani et al. 2009 (PMC2793540); Chinchilla et al. 2007 (Nature 448:497); Lozano-Duran and Zipfel 2015 (Trends Plant Sci 20:12)

- **Claim 2.2**: AUR62021543 (candidate NBS-LRR/NLR resistance gene) represents a direct immune receptor target. If confirmed, bacterial esRNA silencing of an NLR gene would suppress Effector-Triggered Immunity (ETI) and enable deeper bacterial colonization during germination.
  - **Gene**: AUR62021543-RA; 603 aa; protein-coding
  - **UniProt**: A0A803M0R1
  - **Paralogs**: 678 (diagnostic for NBS-LRR tandem array expansion)
  - **Orthologs**: 45 (consistent with fast-evolving NLR genes)
  - **Direction**: Predicted downregulated by bacterial esRNA
  - **Mechanism**: 603 aa + 678 paralogs is the hallmark signature of the NBS-LRR disease resistance gene superfamily. CC-NBS-LRR class (lacks TIR domain based on size). NLR proteins mediate ETI upon detection of pathogen effectors. Quinoa encodes 183 NBS-LRR proteins (Bhatt/Ge et al. 2024, PMID:39100881), reflecting allotetraploid genome and active Andean pathogen pressure. Silencing an NLR would prevent ETI activation against seed-borne bacteria, enabling colonization without triggering the hypersensitive response.
  - **Evidence**: MEDIUM confidence. Paralogue count and size strongly suggestive of NLR family. Listed as "Unknown" in original study -- corrected to NBS-LRR candidate. Requires NLR-parser confirmation.
  - **Germination link**: NLR genes are not germination-specific but mediate seed-borne pathogen defense during imbibition. This represents a sophisticated immune evasion strategy if the sRNA-producing bacteria are the same Bacillus endophytes that colonize quinoa seeds with 100% frequency (Pankievicz et al. 2016).
  - **References**: Ge et al. 2024 (PMID:39100881); Jones and Dangl 2006 (Nature 444:323)

- **Claim 2.3**: Two candidate small antimicrobial peptides (AUR62040122 and AUR62035900) may represent seed defense proteins (defensins or LTPs) whose silencing would reduce antimicrobial concentrations in the germination zone.
  - **Gene AUR62040122**: 117 aa; 1 ortholog, 18 paralogs; Amaranthaceae-specific expansion. Size fits defensin precursor (~100-130 aa).
  - **Gene AUR62035900**: 105 aa; 38 paralogs. Size and family expansion consistent with LTP (Lipid Transfer Protein) family or cysteine-rich peptide (CRP) family.
  - **Direction**: Predicted downregulated
  - **Mechanism**: Seed antimicrobial peptides (defensins, LTPs, thionins) are first-line defenders against soil pathogens during germination. LTPs (~100 aa, cysteine-rich) are among the most abundant seed proteins. Bacterial esRNA silencing of multiple paralogs simultaneously would reduce antimicrobial peptide concentrations, creating a more permissive environment for bacterial colonization.
  - **Evidence**: LOW-MEDIUM. Protein size and paralogue patterns are consistent but not confirmatory. Requires mass spectrometry validation in seed extracts.
  - **Germination link**: This immune suppression theme (NLR + antimicrobial peptides) parallels the defense downshift observed in broccoli (CRK26, CRK29) and represents an asymmetric cost-benefit: reduced pathogen defense in exchange for resource reallocation to growth and accommodation of mutualistic Bacillus endophytes.
  - **References**: Inferred from structural data; parallels documented in Weiberg et al. 2013 (Science 342:118)

---

## Theme 3: Betalain/Antioxidant Pathway -- ROS Buffering and Resource Reallocation

### Claims:

- **Claim 3.1**: CqCYP76AD-like (AUR62012347) is a nontranslating CDS adjacent to functional CqCYP76AD1 (AUR62012346) on Scaffold 1995; its targeting by bacterial esRNAs could affect betalain biosynthesis through cis-regulatory lncRNA function or represent direct suppression of a cultivar-specific functional copy.
  - **Gene**: AUR62012347-RA; 1,306 bp transcript; Nontranslating CDS; Scaffold C_Quinoa_Scaffold_1995: 3,507,903-3,511,700 (reverse strand)
  - **Closest Arabidopsis structural homolog**: AT4G25360 (CYP76AD1-like, not present functionally in Arabidopsis as Arabidopsis lacks betalains)
  - **Direction**: Predicted downregulated
  - **Mechanism -- Possibility 1 (lncRNA function)**: If AUR62012347 functions as a lncRNA in cis-regulation of the adjacent CqCYP76AD1 locus (AUR62012346), bacterial sRNA targeting of this noncoding transcript could indirectly suppress CqCYP76AD1 expression. This would be a novel form of cross-kingdom regulation -- bacterial sRNA silencing of a plant regulatory non-coding RNA to suppress a biosynthetic enzyme.
  - **Mechanism -- Possibility 2 (cultivar-specific translation)**: Cai et al. (2025, Stress Biology) documented that a structurally similar quinoa locus (Cqu0091301) was restored to full protein-coding function by a ~4-kb genomic insertion absent in the reference genome. If AUR62012347 is translatable in specific cultivars but annotated as nontranslating in the reference, bacterial sRNA targeting could directly suppress a functional CYP76AD enzyme.
  - **Resource reallocation hypothesis**: If betalain biosynthesis is reduced by esRNA targeting, nitrogen atoms from betalamic acid (nitrogen-containing chromophore) and tyrosine/L-DOPA intermediates could be redirected toward protein synthesis during the narrow germination window when amino acid demand for cell division is high. The betalain pathway is metabolically expensive (requires NADPH, O2, tyrosine).
  - **Evidence**: MEDIUM confidence for gene identity (locus context from literature; direct function unconfirmed). Betalain pathway genes are expressed during germination at 64h, with cold stress responsiveness (Nagatoshi/Lv et al. 2023, PMC10453985).
  - **Germination link**: Betalains are the primary non-enzymatic antioxidants during imbibition ROS burst. Reduced betalain capacity is a cost, but partially compensated by enzymatic antioxidants (SOD, CAT, APX) that are independently inducible. The resource reallocation benefit may outweigh the antioxidant cost.
  - **Amaranthaceae-specific**: This pathway is UNIQUE to Caryophyllales. No Arabidopsis functional model exists. No chalcone synthase (CHS), no flavonoid pathway. DODA enzyme is unique to Caryophyllales. CYP76AD is biochemically distinct from all Arabidopsis CYP450s. Must be validated in quinoa or closely related Amaranthaceae (spinach, amaranth, beet).
  - **References**: Nagatoshi et al. 2023 (PMC10453985); Ge et al. 2025 (ScienceDirect); Cai et al. 2025 (Stress Biology); Hatlestad et al. 2012 (Nat Genet 44:816); Timoneda et al. 2019 (New Phytol 224:71); Brockington et al. 2015 (New Phytol 207:1170)

---

## Theme 4: Chloroplast Retrograde Signaling -- GUN4 and ABA Crosstalk

### Claims:

- **Claim 4.1**: CqGUN4 (AUR62015391) regulates Mg-chelatase activity and plastid-to-nucleus retrograde signaling via tetrapyrrole metabolites. Its downregulation could modulate ABA sensitivity through the PAP/SAL1/XRN retrograde pathway, indirectly promoting dormancy release.
  - **Gene**: AUR62015391-RA (CqGUN4); 491 aa; Scaffold C_Quinoa_Scaffold_2751: 6,125,623-6,136,839 (reverse strand)
  - **Arabidopsis ortholog**: AT3G59400 (GUN4; UniProtKB/Swiss-Prot Q9LX31)
  - **UniProt**: A0A803LM80
  - **Direction**: Predicted downregulated
  - **Mechanism -- Pathway 1 (Tetrapyrrole-retrograde/ABA interaction)**: GUN4 binds protoporphyrin IX (Proto IX) and Mg-protoporphyrin IX (Mg-Proto IX), stimulating Mg-chelatase (CHLD-CHLH-CHLI complex) activity 5-10x. GUN4-PPIX complex generates singlet oxygen (1O2) for retrograde signaling (Kim/Brzezowski et al. 2016, PMC4861466). The chloroplast retrograde signal metabolite PAP (3'-phosphoadenosine 5'-phosphate) inhibits nuclear XRN exoribonucleases, stabilizing specific mRNAs and enhancing ABA sensitivity, thereby inhibiting germination (Pornsiriwong et al. 2017, eLife 6:e23361). GUN4 downregulation would reduce chlorophyll biosynthesis flux, potentially altering the retrograde signal pool and indirectly modulating ABA sensitivity.
  - **Mechanism -- Pathway 2 (De-etiolation and seedling establishment)**: GUN4 is essential for the dark-to-light transition (etioplast-to-chloroplast) during seedling emergence. Downregulation transiently delays chlorophyll biosynthesis and photosynthetic capacity acquisition. This is a cost -- seedlings depend longer on seed reserves -- but acceptable if germination rate itself is accelerated.
  - **CHLH/GUN5 alternative**: The annotation "tetrapyrrole-binding protein, chloroplastic" could also describe CHLH/GUN5, the Mg-chelatase H subunit identified as an ABA receptor (Shen et al. 2006, Nature 443:823). If AUR62015391 encodes CHLH/GUN5 rather than GUN4, its downregulation would directly reduce ABA receptor capacity -- a much more proximal mechanism for germination promotion. Sequence confirmation to distinguish GUN4 from GUN5/CHLH is required.
  - **Evidence**: HIGH confidence for gene identity (direct Swiss-Prot projection AT3G59400). GUN4 also regulates plasmodesmata trafficking via tetrapyrrole retrograde signals (Azim et al. 2025, New Phytologist). 93 orthologs in EnsemblPlants.
  - **Germination link**: Retrograde signaling from immature plastids gates ABA-mediated dormancy maintenance. GUN4 silencing weakens this gate, facilitating germination. The greening delay is a tolerable secondary cost.
  - **References**: Larkin et al. 2003 (Science 299:902); Kim/Brzezowski et al. 2016 (JBC, PMC4861466); Shen et al. 2006 (Nature 443:823); Mochizuki et al. 2001 (PNAS 98:2053); Azim et al. 2025 (New Phytologist)

---

## Theme 5: Immune Suppression -- NBS-LRR and Defense Peptide Targeting

### Claims:

- **Claim 5.1**: The combined targeting of an NLR candidate (AUR62021543), two antimicrobial peptide candidates (AUR62040122, AUR62035900), and a BRI1-family LRR-RLK (AUR62003502) constitutes a multi-layered immune suppression strategy that would reduce both ETI and basal antimicrobial defense during the germination window.
  - **Genes**: AUR62021543 (NLR candidate, 603 aa, 678 paralogs), AUR62040122 (defensin candidate, 117 aa, 18 paralogs), AUR62035900 (LTP candidate, 105 aa, 38 paralogs), AUR62003502 (BRL2/VH1-like LRR-RLK)
  - **Direction**: All predicted downregulated
  - **Mechanism**: Three-layer defense suppression: (1) NLR silencing prevents ETI activation against seed-borne bacterial effectors; (2) antimicrobial peptide silencing reduces chemical defense in the germination zone; (3) LRR-RLK modulation alters the BAK1-mediated immune/growth balance. Net effect: a more permissive environment for bacterial colonization.
  - **Evidence**: [Speculative for NLR and peptide identities; requires NLR-parser and mass spectrometry confirmation]. The pattern parallels defense downshift observed in broccoli (CRK26, CRK29 targeting) and is consistent with the Botrytis cinerea model where fungal sRNAs silence plant immunity genes (Weiberg et al. 2013).
  - **Evolutionary framing**: The 100% Bacillus endophyte colonization rate with vertical transmission (Pankievicz et al. 2016, PMC4722091) suggests co-evolution rather than parasitism. This reframes immune suppression as "mutualistic microbial optimization of host germination" -- where the 100% colonization rate indicates quinoa immune suppression toward seed-borne Bacillus has been permanently or constitutively relaxed during seed maturation.
  - **References**: Ge et al. 2024 (PMID:39100881); Pankievicz et al. 2016 (PMC4722091); Jones and Dangl 2006 (Nature 444:323); Weiberg et al. 2013 (Science 342:118)

---

## Theme 6: Halophyte Adaptation -- EBCs, K+/Na+ Discrimination, and Expanded Gene Families

### Claims:

- **Claim 6.1**: Quinoa's halophyte biology creates a germination context fundamentally different from glycophyte crops, making the esRNA targeting of ion transport genes (CqHAK5, CqCNGC14) uniquely consequential in this species.
  - **Mechanism**: Epidermal bladder cells (EBCs), unique to quinoa and related Chenopodioideae, require coordinated K+/Na+ transport (CqHKT1.2 for Na+ loading, CqClc-c for vacuolar Cl-) and are not yet functional in germinating seeds or very young seedlings (Bohm et al. 2018). During this pre-EBC developmental window, K+/Na+ homeostasis depends entirely on root-level transport systems. Bacterial esRNA targeting of CqHAK5 during this window could have disproportionate effects on salinity management compared to later vegetative stages when EBCs provide a dedicated salt-sequestration mechanism.
  - **Evidence**: [Known for EBC biology; Inferred for esRNA vulnerability window]. Bohm et al. 2018 (Current Biology 28:3075); Bohm et al. 2020 (bioRxiv)
  - **Germination link**: The pre-EBC germination window is the most vulnerable period for K+/Na+ imbalance. HAK5 targeting could produce delayed effects on seedling vigor even if germination rate itself is not dramatically affected, because the plant cannot sequester excess Na+ until EBCs differentiate.

- **Claim 6.2**: ABA hypersensitivity in the halophyte context means that CqCNGC14 silencing (reducing ABA-reinforcing Ca2+ signals) could have a larger effect on dormancy release in quinoa than in glycophytes.
  - **Mechanism**: The quinoa genome contains expanded ABA biosynthesis, transport, and signaling genes (Jarvis et al. 2017). Quinoa shows ABA hyperresponsiveness that pre-adapts ABA-responsive genes for stress. This hypersensitivity means even modest reductions in ABA-reinforcing signals (via CqCNGC14 silencing) could shift the hormonal balance significantly toward GA dominance and dormancy release.
  - **Evidence**: [Inferred from quinoa ABA system characterization].
  - **References**: Jarvis et al. 2017 (Nature 542:307); Zhao et al. 2022 (Frontiers Plant Sci 13:853326)

- **Claim 6.3**: The expanded quinoa small RNA machinery (21 CqAGO, 8 CqDCL, 11 CqRDR) enhances the plant's capacity to process exogenous bacterial sRNAs, potentially amplifying the cross-kingdom silencing effect.
  - **Mechanism**: The quinoa RNAi machinery is expanded relative to Arabidopsis (10 AGO, 4 DCL, 6 RDR). This expanded repertoire means bacterial esRNAs could be loaded into multiple AGO complexes with different silencing specificities, processed into secondary siRNAs by RDR6, or trigger RNA-directed DNA methylation via 24-nt siRNAs and AGO4/RDR2/DCL3 pathway.
  - **Evidence**: [Known for gene family sizes; Speculative for functional consequences]. Xu et al. 2023 (Scientific Reports 13:3669)

---

## Theme 7: Nontranslating Transcripts and lncRNA Targeting

### Claims:

- **Claim 7.1**: Three of 31 targets (9.7%) are annotated as nontranslating CDS (AUR62012347, AUR62039771, AUR62034256), an above-chance representation suggesting that bacterial esRNAs may target non-coding or pseudogene transcripts through mechanisms distinct from canonical mRNA silencing.
  - **Genes**: AUR62012347 (1,306 bp, CYP76AD-like pseudogene), AUR62039771 (2,096 bp), AUR62034256 (714 bp)
  - **Mechanism**: If these transcripts do not produce functional proteins, the mechanism of esRNA action would involve post-transcriptional destabilization of lncRNAs or pseudogene transcripts rather than translational repression. Possible regulatory roles: (a) lncRNA-mediated chromatin silencing in cis; (b) natural antisense transcription affecting neighboring gene expression; (c) competitive endogenous RNA (ceRNA) sponge activity sequestering endogenous miRNAs; (d) smORF-encoded peptides below annotation detection thresholds.
  - **Evidence**: [Inferred from annotation analysis]. Three nontranslating targets at 9.7% exceeds the expected proportion from genome-wide nontranslating annotation frequency.
  - **Recommended validation**: RibORF, CPAT, or ribosome profiling to determine coding potential; FISH/smRNA-FISH to determine transcript localization.

---

## Theme 8: Allotetraploid Genome Complexity and Homeolog Buffering

### Claims:

- **Claim 8.1**: Quinoa's AABB allotetraploid genome provides functional buffering through homeolog compensation; if bacterial esRNAs target a sequence conserved between A and B homeologs, both copies are silenced, but if the esRNA targets a subgenome-specific sequence, only one homeolog is silenced and the other compensates. This creates a spectrum of silencing effects from partial to complete.
  - **Mechanism**: A and B subgenomes diverged 3.3-6.3 MYA, sufficient time for significant sequence divergence at sRNA-binding sites. The B subgenome is more structurally dynamic (71.7% pericentromeric inversion on Cq3B; Rey et al. 2023). Subgenome-specific expression dominance, transposable element distribution, and 24-nt siRNA-mediated methylation patterns all differ between A and B (Rey et al. 2023; Pikaard and Mittelsten Scheid 2014).
  - **Evidence**: [Known for subgenome divergence; Inferred for esRNA targeting specificity]
  - **Implications**: For CqHAK5 specifically, even if one targeted isoform is silenced, 29 other CqHAK family members maintain K+ transport. The unique contribution of the targeted CqHAK5 to germination-stage K+ uptake needs empirical determination. Subgenome-specific RT-qPCR using SNP-containing primer pairs at homeolog-distinguishing regions would determine whether one or both homeologs are downregulated.
  - **References**: Rey et al. 2023 (Commun Biol 6:1263); Kolano et al. 2016 (Mol Phylogenet Evol 100:109)

---

## HAK/KUP K+ Transporter Paradox

This is the central paradox of the quinoa target list: **CqHAK5 is the highest-confidence target with the most mechanistically clear annotation, yet silencing a canonical high-affinity K+ importer should impair radicle turgor and DELAY germination -- the opposite of the observed phenotype**.

### Resolution Hypotheses:

**(a) Context-dependent efflux roles**: Some HAK/KUP members mediate K+ efflux under specific conditions, particularly under high-Na+ environments where maintaining K+/Na+ ratio requires controlled K+ redistribution. If the targeted CqHAK5 isoform functions as a K+ efflux conduit under the saline conditions typical of quinoa germination, silencing it would INCREASE net K+ retention. [Inferred; requires electrophysiological characterization]

**(b) Na+ competition at HAK transporter sites**: Under saline conditions, Na+ competes with K+ at HAK transporter active sites, and some HAK isoforms have measurable Na+ co-transport activity. Silencing a HAK isoform with significant Na+ permeability could improve the K+/Na+ ratio without reducing total K+ accumulation. [Speculative]

**(c) Allotetraploid buffering**: With 30 CqHAK family members, silencing one isoform may be functionally compensated by others. The unique contribution of the targeted CqHAK5 to germination-stage K+ uptake needs empirical determination. 29 other family members maintain transport capacity. [Known for family size; Inferred for compensation]

**(d) Subgenome-specific targeting**: If the bacterial esRNA targets only the A-subgenome homeolog of CqHAK5, the B-subgenome copy maintains function, producing a partial reduction in K+ flux rather than complete loss. [Inferred]

**(e) K+/Na+ ratio matters more than K+ flux**: In a halophyte seedling where the pre-EBC developmental window creates vulnerability to Na+ toxicity, the K+/Na+ ratio may be more important than absolute K+ accumulation. Modifying HAK5 transport characteristics could improve this ratio. [Inferred]

**Experimental test**: Compare germination phenotypes of EPS-treated quinoa seeds under (i) standard K+ (1 mM KCl), (ii) low K+ (0.01 mM), (iii) high Na+ (100 mM NaCl), and (iv) high Na+ + low K+. If the paradox resolves via mechanism (a) or (b), the germination enhancement should be strongest under saline conditions.

---

## Top Targets (ranked)

| Rank | Gene ID | Annotation | Priority | Pathway | Why Top |
|------|---------|------------|----------|---------|---------|
| 1 | AUR62010943 | CqHAK5 (K+ high-affinity transporter) | CRITICAL | Ion transport / K+ homeostasis | Direct turgor driver for radicle emergence; K+/Na+ discrimination in halophyte context; activated by CIPK23/CBL1/9 complex |
| 2 | AUR62003502 | CqBRL2/VH1-like (LRR-RLK, BRI1 family) | HIGH | Hormone signaling / Vascular development | BAK1 co-receptor competition between immune and growth signaling; BR/auxin crosstalk; annotation correction from defense to vascular function |
| 3 | AUR62044372 | CqCNGC14 (Ca2+ channel) | HIGH | Ca2+ signaling / Auxin response | Ca2+ influx for gravitropism and auxin response; ABA-reinforcing Ca2+ signaling; Ca2+ oscillations for root hair growth |
| 4 | AUR62012347 | CqCYP76AD-like (betalain locus, nontranslating CDS) | HIGH | Betalain / Secondary metabolism | Antioxidant capacity during imbibition; resource reallocation from pigment to growth; Amaranthaceae-specific; possible lncRNA cis-regulation |
| 5 | AUR62015391 | CqGUN4 (tetrapyrrole-binding, chloroplastic) | MEDIUM-HIGH | Chloroplast retrograde signaling | Mg-chelatase regulation; ABA crosstalk via PAP pathway; de-etiolation during seedling establishment; possible GUN5/CHLH ABA receptor alternative |
| 6 | AUR62021543 | Candidate NBS-LRR resistance gene | MEDIUM | Disease resistance / Innate immunity | 678 paralogs diagnostic for NLR family; ETI suppression for bacterial colonization; 183 NBS-LRR in quinoa |
| 7 | AUR62040122 | Candidate antimicrobial CRP (defensin-type) | LOW-MEDIUM | Seed defense | 117 aa; 1 ortholog, 18 paralogs; Amaranthaceae-specific expansion; size fits defensin precursor |
| 8 | AUR62035900 | Candidate LTP or antimicrobial peptide | LOW-MEDIUM | Seed defense / Lipid transfer | 105 aa; 38 paralogs; consistent with LTP superfamily; seed-abundant pathogen defense |
| 9 | AUR62014700 | Possible transcription factor (WRKY/MYB/NAC) | LOW-MEDIUM | Transcription regulation | 361 aa; 185 orthologs; 88 paralogs; fits quinoa WRKY (92 members) or NAC (100+ members) family |
| 10 | AUR62011287 | Lineage-specific protein (Amaranthaceae-specific) | LOW | Unknown / Lineage-specific | 335 aa; only 4 orthologs; strong candidate for Amaranthaceae-specific function (saponin accessory? betalain accessory? halophyte adaptation?) |

Remaining 21 targets (AUR62043174, AUR62027225, AUR62031820, AUR62006498, AUR62039771, AUR62018498, AUR62025094, AUR62033668, AUR62037200, AUR62029415, AUR62042100, AUR62023678, AUR62016845, AUR62038512, AUR62020100, AUR62045001, AUR62007329, AUR62034256, AUR62041888, AUR62019623) have LOW or NO confidence function assignments. Several show distinctive conservation patterns: AUR62033668 (400 orthologs, 16 paralogs -- highly conserved multi-gene family); AUR62019623 (278 orthologs -- near-universal plant protein); AUR62007329 (263 orthologs -- universal plant protein). These may encode essential housekeeping or regulatory proteins whose downregulation could have broad physiological effects.

---

## Proposed Primary MoA for Quinoa

### Model A: Coordinated esRNA-Mediated Defense-Dormancy-Ion Knockdown

**Hypothesis**: Bacterial esRNAs function as authentic cross-kingdom regulatory molecules delivered into quinoa seed cells during imbibition, loaded into the plant AGO machinery (21 CqAGO), and simultaneously suppress multiple plant defense, dormancy, and ion transport pathways to shift the metabolic balance from immunity/quiescence toward growth/germination.

**Four-phase mechanistic sequence**:

**Phase 0 -- ABA-weakening via GUN4 + CNGC14 silencing (0-12 h post-imbibition)**:
- Bacterial esRNAs enter seed cells through EPS-mediated membrane interaction or imbibition-driven uptake
- CqCNGC14 silencing reduces Ca2+ influx, dampening Ca2+-dependent activation of CDPKs and SnRK2 kinases
- CqGUN4 silencing alters tetrapyrrole retrograde signals, potentially reducing PAP-mediated ABA amplification
- Net effect: ABA signal transduction chain weakened at two independent nodes before the hormonal peak at 12h

**Phase 1 -- Defense-growth tradeoff via BRL2/VH1-like silencing (6-24 h)**:
- CqBRL2/VH1-like silencing alters the BRI1-family/BAK1 receptor landscape
- Freed BAK1 is available for BRI1 brassinosteroid complexes
- Brassinosteroid signaling promotes CYP707A expression (ABA catabolism) and GA biosynthesis
- NBS-LRR silencing prevents ETI activation against Bacillus endophytes colonizing the germination zone
- Antimicrobial peptide candidates (if confirmed) are reduced, further facilitating colonization

**Phase 2 -- K+ accumulation for radicle emergence (12-48 h)**:
- CqHAK5 silencing paradox resolved by: (a) context-dependent K+ efflux role, (b) allotetraploid compensation by 29 other CqHAK members, and/or (c) improved K+/Na+ ratio under saline conditions
- CqCNGC14 silencing, having already reduced ABA reinforcement in Phase 0, now contributes to reduced root tip Ca2+ oscillation burden
- ABA/GA ratio shifts toward GA dominance; DELLA protein degradation proceeds faster
- Radicle cell expansion driven by osmotic turgor supported by K+ accumulation via non-targeted CqHAK family members

**Phase 3 -- Resource reallocation and seedling establishment (24-72 h)**:
- CqCYP76AD-like locus silencing reduces betalain pathway flux
- Tyrosine, L-DOPA, and nitrogen intermediates redirected toward protein synthesis for rapid cell division
- CqGUN4 silencing transiently delays greening but the cost is acceptable given accelerated germination timing
- Enzymatic antioxidants (SOD, CAT, APX) compensate for reduced betalain ROS buffering

**Model A predictions**:
- RNase treatment of the bacterial preparation should abolish germination improvement (critical discriminating test)
- Target gene mRNAs (CqHAK5, CqCNGC14, CqGUN4, CqBRL2/VH1) should be 2-5-fold downregulated at 12-24h post-imbibition
- Bacterial-origin sRNAs should be detectable inside plant cells and enriched in AGO co-immunoprecipitation
- ABA levels should be lower and GA levels higher in treated seeds at 12-24h
- AGO1 and/or AGO4 pathway mutants in Arabidopsis should show reduced response to the bacterial preparation

---

## Alternative Model: EPS Osmopriming

### Model B: EPS-Mediated Osmopriming with RNA as Bystander

**Hypothesis**: The bacterial EPS (extracellular polysaccharide) matrix provides the mechanistic basis for germination improvement through classical osmopriming -- controlled hydration kinetics, nutrient provision, and microenvironmental optimization -- while the esRNAs are transcriptionally inactive bystanders whose presence in the preparation is coincidental.

**Mechanistic sequence**:
- EPS polysaccharides form a hydrogel matrix around the seed with a specific water potential
- Controlled, gradual imbibition prevents sudden hydration damage (imbibition injury)
- EPS-derived oligosaccharides and amino acids serve as early metabolic substrates
- The controlled osmotic environment extends the "oxidative window" for germination signaling
- Any RNA molecules in the preparation are degraded by apoplastic RNases before reaching seed cells

**Model B predictions**:
- RNase-treated EPS should perform identically to intact EPS in germination assays
- Non-biological osmopriming agents (methylcellulose, PEG gel at matched water potential) should produce equivalent germination improvement
- Gene expression changes in treated seeds should reflect hydration status, not specific target knockdown
- Purified RNA without EPS should have no effect on germination

**Relevance to halophyte**: Osmopriming is especially relevant for quinoa because its halophyte physiology is adapted to respond to controlled water potential gradients. The EPS gel may precisely modulate the rate of water uptake in a way that mimics optimal soil moisture conditions, activating salt tolerance mechanisms optimally.

### Model C: Microbiome-mediated phytohormone production (confound)

If live bacteria in the preparation produce IAA, cytokinins, ACC deaminase, or other phytohormones (Bacillus subtilis, B. amyloliquefaciens are documented PGPR producing these compounds), these could directly stimulate germination independent of RNA content.

**Control**: Filter-sterilize (0.2 um) the EPS preparation; compare sterile vs. non-sterile preparations on nutrient agar; measure phytohormone content by LC-MS.

---

## Halophyte-Specific Considerations

### Perisperm Biology and the Seed Reserve Mobilization Axis

- Quinoa stores primary carbohydrate reserves in the **perisperm** (maternally derived nucellus tissue, diploid 2n), NOT an endosperm (triploid 3n from double fertilization). This is the only major food crop with this architecture. The perisperm consists of non-living, thin-walled cells filled with starch grains (Prego et al. 1998).
- The functional analog of the classic endosperm is retained only as a small **micropylar endosperm cap** (two cell layers) at the radicle tip. This cap is the primary mechanical and physiological barrier to radicle emergence, analogous to the Brassicaceae micropylar endosperm cap.
- Weakening of this cap by GA-induced cell wall-loosening enzymes (expansins, XTHs, pectinases) is the rate-limiting step for germination.
- **Implication for Ca2+ signaling**: Ca2+ signaling via CqCNGC14 at the embryo-micropylar endosperm interface may have different spatial constraints than in endosperm-based systems.
- **Implication for K+ transport**: CqHAK5's role in germination may relate primarily to radicle cell expansion AFTER cap rupture, rather than reserve mobilization (which is driven by amylases and proteases in the perisperm).
- **Betalain context**: The perisperm is a dead tissue at seed maturity; betalain antioxidant protection during imbibition operates primarily in the embryo, where CYP76AD enzyme activity would be most consequential.

### Saponin Seed Coat as Physical Barrier to sRNA Uptake

- Quinoa seeds accumulate triterpenoid saponins (up to 86% of total saponin in seed coat; Fiallos-Jurado et al. 2016) regulated by the master transcription factor TSARL1 (bHLH TF; Trinh et al. 2024).
- Saponins are amphipathic molecules (hydrophilic sugar chains + hydrophobic triterpenoid cores) that disrupt cell membranes.
- **As barrier**: Saponins could reduce bacterial EV (OMV) survival and impair membrane fusion with seed coat cells.
- **As facilitator (paradox)**: Saponin detergent-like properties could promote membrane fusion between bacterial OMVs and seed coat membranes during imbibition-driven hydration, analogous to artificial transfection reagents.
- **Experimental variable**: Sweet (low-saponin) vs. bitter (high-saponin) varieties provide a natural genetic tool for testing saponin barrier effects. Near-isogenic lines differing only at TSARL1 (G2078C SNP) could directly test whether saponin content affects esRNA-mediated germination improvement.

### Epidermal Bladder Cells (EBCs) and Developmental K+/Na+ Homeostasis

- EBCs are trichome-derived salt-sequestering organs unique to quinoa and related Chenopodioideae. They require CqHKT1.2 (Na+ channel), CqClc-c (vacuolar Cl-), and coordinated K+/Na+ transport (Bohm et al. 2018).
- **EBCs are NOT functional during seed germination and early seedling establishment**. The newly germinated seedling must manage K+/Na+ homeostasis without its most powerful salt-sequestration tool.
- This makes the pre-EBC developmental window (germination through first days of seedling establishment) particularly vulnerable to K+/Na+ imbalance, and CqHAK5 targeting during this window has consequences extending beyond germination rate into seedling vigor and salt stress resilience.

### 100% Bacillus Endophyte Colonization -- Evolutionary Context

- Quinoa is 100% colonized by Bacillus spp. endophytes with vertical transmission (seed-to-seed; Pankievicz et al. 2016, PMC4722091).
- This is NOT environmental bacteria encountering naive seeds -- these are co-evolved bacteria that have persisted with quinoa for millions of years.
- **Evolutionary implications**:
  - Co-evolution creates opportunity for **mutualistic RNA communication** -- bacteria promoting host germination to ensure their own propagation
  - The 100% colonization rate suggests quinoa immune system has been permanently or constitutively relaxed toward seed-borne Bacillus
  - This shifts interpretation from "pathogen manipulation of host plant" (Botrytis model) toward "mutualistic microbial optimization of host germination"
  - Whether bacterial sRNAs are pro-germination (mutualistic) or anti-defense (opportunistic) can be partially distinguished by testing whether germination improvement is maintained under pathogen-challenging conditions

---

## Annotation Corrections Summary

| # | AUR Gene ID | Original | Corrected | Severity |
|---|-------------|----------|-----------|----------|
| 1 | AUR62012347 | CYP76AD1-like or DODA-like (functional enzyme) | Nontranslating CDS -- likely CYP76AD-family pseudogene or tandem duplicate of CqCYP76AD1 (AUR62012346) | HIGH |
| 2 | AUR62039771 | Unknown | Nontranslating CDS (2,096 bp) -- possible lncRNA or pseudogene; no protein product | MEDIUM |
| 3 | AUR62034256 | Unknown | Nontranslating CDS (714 bp) -- putative smORF or pseudogene; no protein product | MEDIUM |
| 4 | AUR62045001 | Unknown | Not present in EnsemblPlants (Release 62, ChenopodiumDB import) -- gene model unverifiable from public databases | HIGH |
| 5 | AUR62021543 | Unknown | Candidate NBS-LRR resistance gene (CC-NBS-LRR class); 678 paralogs diagnostic for NLR family | HIGH |
| 6 | AUR62003502 | LRR-RLK (defense-implied) | CqBRL2/VH1-like (BRI1-family, vascular/brassinosteroid signaling) -- primary function is vascular differentiation and BR/auxin crosstalk, NOT immune defense | CRITICAL |

---

## Key References

### Quinoa Genome and Genomics
1. Jarvis DE et al. (2017) The genome of Chenopodium quinoa. *Nature* 542:307-312. DOI: 10.1038/nature21370. PMID: 28178233
2. Yasui Y et al. (2016) Draft genome sequence of an inbred line of Chenopodium quinoa. *DNA Research* 23:535-546. DOI: 10.1093/dnares/dsw037. PMID: 27458999
3. Zou C et al. (2017) High-quality genome assembly of quinoa provides insights into salt bladder-based salinity tolerance. *Cell Research* 27:1327-1340. DOI: 10.1038/cr.2017.124
4. Rey E et al. (2023) Chromosome-scale assembly of quinoa genome. *Communications Biology* 6:1263. DOI: 10.1038/s42003-023-05613-4
5. Kolano B et al. (2016) Molecular and cytogenetic evidence for allotetraploid origin. *Mol Phylogenet Evol* 100:109-123. DOI: 10.1016/j.ympev.2016.04.009

### HAK/KUP K+ Transport
6. Ren A et al. (2023) Genome-wide identification and characterization of HAK gene family in quinoa (CqHAK1-CqHAK30). *Plants* 12(21):3747. PMC: PMC10650088
7. Nieves-Cordones M et al. (2010) AtHAK5 required for plant growth and K+ acquisition under saline conditions. *Molecular Plant* 3:326-333
8. Rubio F et al. (2010) AtHAK5 and AKT1 vital for seedling establishment under low-K+. *Plant Physiology* 153:863-876. PMC: PMC2879780
9. Rubio F et al. (2008) Relative contribution of AtHAK5 and AtAKT1. *Physiologia Plantarum* 134:598-608
10. Rigas S et al. (2001) TRH1 encodes potassium transporter for root hair tip growth. *Plant Cell* 13:139-151

### CNGC Ca2+ Channels
11. Zhang Y et al. (2024/2025) CNGC gene family in quinoa. *SSRN Preprint* 5070311
12. Shih HW et al. (2015) CNGC14 regulates root gravitropism. *Current Biology* 25:3119-3125. PMID: 26752079
13. Brost C et al. (2019) Multiple CNGCs coordinate Ca2+ oscillations and polar growth of root hairs. *Plant Journal* 99:910-923
14. Brost C et al. (2016) CNGC14 regulates root gravitropism. *Current Biology* 26:67-71

### Tetrapyrrole/Retrograde Signaling
15. Larkin RM et al. (2003) GUN4, regulator of chlorophyll synthesis and intracellular signaling. *Science* 299:902-906
16. Kim C et al. (2016) GUN4-Protoporphyrin IX singlet oxygen generator. *JBC* PMC4861466
17. Shen YY et al. (2006) Mg-chelatase H subunit is ABA receptor. *Nature* 443:823-826
18. Mochizuki N et al. (2001) GUN5 mutant in plastid-to-nucleus signal transduction. *PNAS* 98:2053-2058
19. Azim MF et al. (2025) GUN4 regulates plasmodesmata trafficking via tetrapyrrole retrograde signals. *New Phytologist*

### BRL2/VH1 LRR-RLK
20. Clay NK, Nelson T (2005) Arabidopsis thickvein mutation. *Plant Physiology* 138:1527-1538
21. Ceserani T et al. (2009) VH1/BRL2 receptor-like kinase interacts with VIT and VIK. *Plant Journal* 57:1000-1014. PMC: PMC2793540

### Betalain Biosynthesis
22. Nagatoshi Y / Lv X et al. (2023) Quinoa betalain biosynthesis genes -- seed germination and cold stress. *Plant Signaling & Behavior* 18(1):2250891. PMC: PMC10453985
23. Ge F et al. (2025) CqCYP76AD and CqDODA families in quinoa. *ScienceDirect*. DOI: 10.1016/S0981-9428(25)00097X
24. Cai J et al. (2025) Genomic structural variation in betacyanin variegation in quinoa. *Stress Biology*. DOI: 10.1007/s44154-025-00284-z
25. Hatlestad GJ et al. (2012) Beet R locus encodes CYP450 for red betalain production. *Nature Genetics* 44:816-820
26. Timoneda A et al. (2019) Evolution of betalain biosynthesis in Caryophyllales. *New Phytologist* 224:71-85
27. Brockington SF et al. (2015) Lineage-specific gene radiations in betalain evolution. *New Phytologist* 207:1170-1180

### Defense/Immunity
28. Chinchilla D et al. (2007) FLS2-BAK1 complex initiates plant defence. *Nature* 448:497-500
29. Lozano-Duran R, Zipfel C (2015) Trade-off between growth and immunity via brassinosteroids. *Trends Plant Sci* 20:12-19
30. Jones JDG, Dangl JL (2006) The plant immune system. *Nature* 444:323-329
31. Ge F et al. (2024) NBS-LRR domain-containing R genes in quinoa. *Physiol Mol Biol Plants* 30:895-910. PMID: 39100881
32. Zipfel C et al. (2004) Bacterial disease resistance through flagellin perception. *Nature* 428:764-767

### Cross-Kingdom sRNA
33. Weiberg A et al. (2013) Fungal small RNAs suppress plant immunity. *Science* 342:118-123
34. Cai Q et al. (2018) Plants send small RNAs in EVs to fungal pathogen. *Science* 360:1126-1129
35. He B et al. (2021) RNA-binding proteins contribute to small RNA loading in plant EVs. *Nature Plants* 7:342-352
36. Cai Q et al. (2025) Vesicular and non-vesicular extracellular sRNAs direct gene silencing in plant-interacting bacterium. *Nature Communications* 16:2759
37. Zand Karimi H et al. (2022) Arabidopsis apoplastic fluid contains sRNA and circular RNA-protein complexes. *Plant Cell* 34:1863-1881
38. Koch A et al. (2016) RNAi-based control of Fusarium through spraying long dsRNAs. *PLOS Pathogens* 12:e1005901
39. Betti F et al. (2021) Exogenous miRNAs induce post-transcriptional gene silencing in plants. *Nature Plants* 7:1379-1388

### Quinoa Germination Biology
40. Zhao Y et al. (2022) Transcriptome of quinoa seeds during germination and GA/ABA responses. *Frontiers Plant Sci* 13:853326
41. Prego I et al. (1998) Seed structure and localization of reserves in Chenopodium quinoa. *Annals of Botany* 82:481-488
42. Lopez-Fernandez MP, Maldonado S (2013) Programmed cell death during quinoa perisperm development. *J Exp Bot* 64:3313-3325
43. Bohm J et al. (2018) Salt sequestration in epidermal bladder cells of Chenopodium quinoa. *Current Biology* 28:3075-3085
44. Orsini F et al. (2011) Beyond ionic and osmotic response to salinity in quinoa. *Functional Plant Biology* 38:818-831
45. Pankievicz VCS et al. (2016) Robust biological nitrogen fixation in a model grass-bacterial association. *Plant Journal* 81:907-919. PMC: PMC4722091

### Saponins
46. Fiallos-Jurado J et al. (2016) Saponin determination and functional characterization in quinoa. *Plant Science* 250:188-197
47. Trinh HX et al. (2024) TSARL1 as master controller of seed saponin biosynthesis. *Plant Biotechnol J* 22:2216-2234

### Quinoa RNAi Machinery
48. Xu Z et al. (2023) Genome-wide identification of AGO, DCL, and RDR families in quinoa. *Scientific Reports* 13:3669

### ABA/GA/Hormone Signaling
49. Liang Y et al. (2020) Transcription factors and homologs in seed dormancy and germination of quinoa. *Plant Physiol Biochem* 151:350-363
50. Zhu T et al. (2022) CqSnRK2 gene family and CqSnRK2.12 function. *BMC Genomics* 23:422
51. Chen L et al. (2024) CqGAox gene family and seed germination. *Industrial Crops and Products* 221:119480
52. Sun L et al. (2025) CqGID1 homologs in quinoa. *Plant Cell Reports* 44:88

### Halophyte Biology
53. Shabala S (2013) Learning from halophytes. *Annals of Botany* 112:1209-1221
54. Munns R, Tester M (2008) Mechanisms of salinity tolerance. *Annu Rev Plant Biol* 59:651-681
55. Shabala S, Mackay A (2011) Ion transport in halophytes. *Advances in Botanical Research* 57:151-199

### Epigenetics
56. Pikaard CS, Mittelsten Scheid O (2014) Epigenetic regulation in plants. *Cold Spring Harbor Perspectives in Biology* 6:a019315
57. Cheng F et al. (2016) Epigenetic regulation of subgenome dominance following whole genome triplication. *New Phytologist* 211:288-299

### Defense-Growth Tradeoff
58. Huot B et al. (2014) Growth-defense tradeoffs in plants. *Molecular Plant* 7:1267-1287
59. Boller T, Felix G (2009) Renaissance of elicitors. *Annu Rev Plant Biol* 60:379-406

### General Germination/ROS
60. Graeber K et al. (2012) Molecular mechanisms of seed dormancy. *Plant Cell & Environment* 35:1769-1786
61. Bailly C (2019) Signalling role of ROS in regulation of seed germination and dormancy. *Biochem J* 476:3023-3041
62. Weitbrecht K et al. (2011) First off the mark: early seed germination. *J Exp Bot* 62:3289-3309
63. Leubner-Metzger G (2003) Functions of beta-1,3-glucanases during seed germination. *Seed Science Research* 13:17-34

---

*Report generated: 2026-02-17*
*Source documents: ExRNA_Ag_Final_Report_CONFIDENTIAL_Long_Quinoa.pdf (33 pages), quinoa_germination_biology_report.md, quinoa_exRNA_target_annotation_report.txt, quinoa_gene_function_report.txt*
*Analysis: Exhaustive mechanistic claims extraction with all gene IDs, pathways, evidence levels, and references*
