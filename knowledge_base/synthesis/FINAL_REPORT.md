# ExRNA-Mediated Reprogramming of Spinach Seed Germination

**Sarthak Tiwary | ExRNA-Ag | February 2026**
**Evidence:** [KNOWN] = peer-reviewed; [INFERRED] = deduced from homolog data; [SPECULATIVE] = untested hypothesis

---

## Bottom Line Up Front

M-9 (bacterial EPS seed treatment) improves spinach germination. sRNA sequencing identified ~109 spinach gene targets with complementarity to bacterial exRNAs. We asked: **Are these real targets? What's the mechanism? Can we prove it?**

**Answers:**

1. **21 high-priority targets** hit three regulatory levers: epigenetic brakes, ABA/GA hormone balance, and defense cost [1, 2, 3]. The target list is coherent -- not random.

2. **The mechanism is testable.** Two causal models make opposite predictions distinguishable by time-course qRT-PCR [4, 5].

3. **Six confounders threaten the hypothesis.** The simplest explanation -- osmopriming -- requires no novel biology [6, 7]. One target (cry8Ba) is bacterial contamination, not a spinach gene.

4. **One experiment decides everything.** RNase treatment of M-9: 2 weeks, <$500. If the phenotype survives RNase, RNA is irrelevant. If it doesn't, proceed.

5. **Minimum viable validation:** 5 experiments, 10-12 weeks, ~$3,600.

**Caveat:** "Zhu et al. (2022, *Nature Plants*)" -- cited in source documents as precedent for bacteria-to-plant sRNA transfer during imbibition -- **could not be verified** in PubMed, Google Scholar, or Nature Plants. Cross-kingdom RNAi is established in fungal-plant systems [8, 9, 10, 11, 12], but this specific bacterial-seed precedent may not exist. If confirmed, our finding would be genuinely novel.

---

## 1. Top 21 Targets

Scored by annotation quality, *Arabidopsis* homolog relevance [13], pathway membership, and mechanistic plausibility of downregulation promoting germination.

| Rank | Gene ID | Annotation | Theme | Score |
|------|---------|------------|-------|-------|
| 1 | SOV3g000150.1 | Ethylene receptor | Hormone | 10 |
| 2 | SOV1g033340.1 | DNA methyltransferase | Epigenetic | 10 |
| 3 | SOV3g043450.1 | EDR2 | Defense | 9 |
| 4 | SOV6g048760.1 | EDR2 (paralog) | Defense | 9 |
| 5 | SOV4g015450.1 | SUVR5 histone methyltransferase | Epigenetic | 9 |
| 6 | SOV3g035520.1 | Lipoxygenase (LOX) | Hormone | 9 |
| 7 | SOV6g036290.1 | HIRA histone chaperone | Epigenetic | 8 |
| 8 | SOV5g005530.1 | MOS1-like (NLR regulator) | Defense | 8 |
| 9 | SOV4g032870.1 | AHP (cytokinin relay) | Hormone | 8 |
| 10 | SOV1g020340.1 | MYB transcription factor | Signaling | 8 |
| 11 | SOV2g014810.1 | NAC domain protein | Signaling | 8 |
| 12 | SOV3g040200.1 | Glutathione S-transferase | ROS | 7 |
| 13 | SOV3g038840.1 | Peroxidase | ROS | 7 |
| 14 | SOV6g029280.1 | 6-PGDH (NADPH source) | Metabolic | 7 |
| 15 | SOV4g038060.1 | GIS2 zinc finger | Epigenetic | 7 |
| 16 | SOV3g033920.1 | PP2A regulatory subunit | Signaling | 7 |
| 17 | SOV1g018480.1 | CNGC (Ca2+ channel) | Transport | 7 |
| 18 | SOV1g021960.1 | Cation-Cl cotransporter | Transport | 7 |
| 19 | SOV2g025380.1 | Cation-Cl cotransporter | Transport | 6 |
| 20 | SOV2g009230.1 | Trehalose-P synthase | Metabolic | 5 |
| 21 | SOV4g030590.1 | PHD-domain protein | Epigenetic | 6 |

+49 medium-priority, +39 low-priority (Appendix A).

### Why These Matter

- **Ethylene receptor (#1):** Negative regulator. *etr1* mutants show reduced dormancy [1, 14]. Downregulation = ethylene hypersensitivity = pro-germination.
- **DNA methyltransferase (#2):** Maintains dormancy via promoter silencing. *met1* mutants show altered dormancy [15]. Downregulation = passive demethylation of GA biosynthesis genes.
- **EDR2 (#3-4, two paralogs):** SA-defense regulator [16]. Dual knockdown = defense cost eliminated.
- **SUVR5 (#5):** Writes repressive H3K9me2/3. Downregulation = chromatin opening at germination loci.
- **LOX (#6):** First step of JA biosynthesis [17]. Downregulation = less JA + less ABA cross-talk + less lipid peroxidation. Triple benefit from one target.

### Red Flags

- **cry8Ba (SOV2g038830.1):** *B. thuringiensis* crystal protein. **Bacterial contamination, not a spinach gene.** Remove from all analyses.
- **RT-domain proteins (4 targets):** Transposon alignment artifacts. Already low-priority.

---

## 2. Mechanism: Six Themes, Two Models

The 109 targets cluster into six functional themes that reinforce each other:

| Theme | Key Targets | What Downregulation Does |
|-------|-------------|------------------------|
| **Defense downshift** | EDR2 x2, MOS1, RLKs | Dismantles costly immunity [18, 19, 16]. Frees ATP/NADPH/carbon for growth. |
| **Epigenetic remodeling** | DNA-MTase, SUVR5, HIRA [20], GIS2 | Removes repressive marks on pro-germination promoters [15, 21]. Opens GA3ox, CYP707A loci. |
| **ROS optimization** | Peroxidase, GST, 6-PGDH | Reduces antioxidant capacity --> controlled ROS burst into the "oxidative window" [22, 23]. Breaks ABA-ROS dormancy loop [22, 24]. |
| **Hormone rebalancing** | Ethylene receptor, LOX, AHP, MYB, NAC | Targets regulatory nodes, not enzymes. Shifts ABA/GA ratio [1, 4, 5]. LOX + ethylene receptor = "brakes off + accelerator on." |
| **Transport** | CNGC [25], Cl-cotransporters, ABC | Blunts defense Ca2+ signaling. Adjusts osmotic potential for radicle emergence. |
| **Metabolic priming** | TPS [26], aspartokinase, CTP synthase | [SPECULATIVE] TPS down --> SnRK1 activated --> reserve mobilization. Contradicts simple model -- needs validation. |

### Two Testable Models

**Model 1: Defense-Epigenetic Reprogramming**
- Primary targets: DNA-MTase, SUVR5, EDR2, MOS1
- Pathway: Epigenetic derepression --> GA gene activation --> ABA/GA shift
- Test: Paclobutrazol (GA inhibitor) blocks the effect
- Temporal: Epigenetic/defense targets down first (3-6h), ROS changes follow (12-24h)

**Model 2: Metabolic-Hormonal Priming**
- Primary targets: Peroxidase, LOX, GST, CNGC, TPS
- Pathway: ROS attenuation --> ABA-ROS loop broken --> passive hormone shift
- Test: Ascorbic acid partially mimics the effect in untreated seeds
- Temporal: ROS/metabolic targets down first (1-3h), epigenetic changes follow

Time-course qRT-PCR distinguishes them.

### Minimal Effective Cocktail (6 genes from 109)

If mechanism validates, these 6 genes are the synthetic exRNA design targets:
1. DNA methyltransferase + SUVR5 (epigenetic)
2. Ethylene receptor + LOX (hormone)
3. EDR2 + MOS1 (defense)

---

## 3. Confounders: What Could Kill This Hypothesis

| # | Confounder | Threat | Control | Kill Condition |
|---|-----------|--------|---------|---------------|
| 1 | **EPS osmopriming** | CRITICAL | Iso-osmotic PEG 8000 vs M-9 [6] | PEG replicates phenotype = RNA irrelevant |
| 2 | **Polysaccharide MAMP elicitation** | HIGH | RNase treatment of M-9 [19, 27] | RNase has no effect = RNA irrelevant |
| 3 | **Live bacteria (PGPR)** | CONDITIONAL | Was M-9 filter-sterilized (0.22um)? [28, 29] | If no, serious threat |
| 4 | **Contamination / misannotation** | CRITICAL | Re-map to bacterial genome; BLAST all targets | Filtered list is empty = all artifacts |
| 5 | **RNA instability** | HIGH | Spike synthetic RNA, measure half-life [30, 31] | Degrades in minutes = mechanism implausible |
| 6 | **Non-specific RNA (PAMP)** | MEDIUM | Scrambled RNA control (same length/GC) [27] | Scrambled works = not sequence-specific |

### The Killer Experiment

**RNase A/T1 treatment of M-9 + heat-inactivated RNase control.**

This one experiment addresses confounders #1, #2, and #3 simultaneously because the treated solution retains identical EPS, osmolality, and polysaccharides -- only RNA is destroyed.

- **RNase kills phenotype:** Confounders #1-3 ruled out. exRNA hypothesis lives. Proceed.
- **RNase has no effect:** exRNA hypothesis is dead. Redirect to EPS/polysaccharide mechanism.

**Cost: <$500. Time: 2 weeks. Do this first.**

---

## 4. Validation Plan

### Gate 1: Go/No-Go (Weeks 1-3, ~$400)

| Exp | What | Cost | Decides |
|-----|------|------|---------|
| 1.1 | RNase treatment | $200 | Is RNA the active molecule? |
| 1.4 | PEG iso-osmotic control | $200 | Is it just osmopriming? |
| 1.5 | Bioinformatic cleanup | $0 | Does target list survive filtering? |

**If any fails: STOP. Redirect program.**

### Gate 2: Target Validation (Weeks 4-8, ~$3,200)

| Exp | What | Cost | Decides |
|-----|------|------|---------|
| 1.2 | EPS fractionation | $700 | RNA fraction vs polysaccharide fraction? |
| 1.3 | Dose-response | $150 | Quantitative RNA-phenotype link? |
| 2.1 | qRT-PCR time-course (15 genes) | $2,500 | Are targets actually silenced? |

**qRT-PCR panel:** 10 high-priority + 3 secondary + 2 negative controls (RT-domain artifact + cry8Ba). Timepoints: 0, 4, 8, 12, 24, 48h. Reference genes validated by geNorm [32] / NormFinder [33].

**GO:** >=6/10 targets downregulated (FC <0.5, p<0.05) at 8-24h. Controls unchanged.
**NO-GO:** <3 targets downregulated.

### Gate 3+: Mechanistic & Publication-Grade (If Gates 1-2 pass)

| Exp | What | Cost | Timeline |
|-----|------|------|----------|
| 3.1 | ROS assays | $1,000 | 3-4 weeks |
| 3.2 | sRNA uptake imaging | $4,000 | 8-12 weeks |
| 4.1 | Degradome/PARE-seq [34, 35] | $6,500 | 12-16 weeks |
| 4.2 | Synthetic RNA mimics | $4,000 | 8-10 weeks |
| 4.3 | *Arabidopsis* mutant validation | $750 | 6-8 weeks |

### Timeline

```
Week:  1   2   3   4   5   6   7   8   9  10  11  12
       |---|---|---|---|---|---|---|---|---|---|---|---|
RNase + PEG        [===]
Bioinformatics      [==]
       GATE 1 ---------*
Dose-Response       [===]
EPS Fractionation       [=======]
       GATE 2 -----------------*
qRT-PCR (15 genes)             [===============]
Hormone Markers                         [======]
       DATA COMPLETE --------------------------*
```

### Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| RNase doesn't kill phenotype | Program-ending | Redirect to polysaccharide/osmotic mechanism |
| PEG replicates phenotype | Program-ending | Accept: it's osmopriming, not RNAi |
| Unstable reference genes | Invalidates qRT-PCR | Validate 3 references with geNorm [32] |
| Poor seed RNA quality | Delays Tier 2 | TRIzol + PVP-40 protocol |

---

## 5. Recommendation

**Spend $400 and 2 weeks on Gate 1 (RNase + PEG + bioinformatics).** This decides everything.

- **Pass:** High-value, high-novelty territory. One of the first bacteria-to-plant sRNA demonstrations during seed imbibition. Commercially and scientifically significant.
- **Fail:** Stop immediately. Save $5,000-20,000 on downstream experiments. The EPS itself may still be commercially valuable as a priming agent.

**What we don't know yet:**
- Whether sRNAs enter spinach embryo cells
- Whether any target is actually downregulated
- Whether the phenotype depends on RNA at all
- Whether the cited "Zhu et al. 2022" precedent is a real paper

The confounders analysis is a strength. It protects against investing in an uncontrolled hypothesis.

---

## Appendix A: Medium Priority Targets (49)

| Gene ID | Annotation | Pathway | Score |
|---------|------------|---------|-------|
| SOV4g000330.1 | Phytoene synthase | Metabolic | 6 |
| SOV1g021670.1 | Disease resistance protein | Defense | 5 |
| SOV3g021300.1 | Stress response NST1 | Defense | 5 |
| SOV1g027650.1 | Receptor-like kinase | Signaling | 5 |
| SOV4g000660.1 | Ser/Thr kinase (RLK) | Signaling | 5 |
| SOV1g043000.1 | RING E3 ubiquitin transferase | Turnover | 5 |
| SOV1g002960.1 | F-box protein | Turnover | 5 |
| SOV4g010600.1 | Glycosyltransferase | Cell wall | 5 |
| SOV1g032780.1 | ABC transporter | Transport | 5 |
| SOV4g055600.1 | Cytochrome P450 | Metabolic | 5 |
| SOV5g006110.1 | F-box protein-like | Turnover | 4 |
| SOV2g038280.1 | F-box protein | Turnover | 4 |
| SOV2g028550.1 | E3 ubiquitin ligase | Turnover | 4 |
| SOV2g021870.1 | RING-type domain | Turnover | 4 |
| SOV1g033840.1 | Glyco_transf_64 | Cell wall | 4 |
| SOV4g051070.1 | Beta-galactosidase | Cell wall | 4 |
| SOV4g041000.1 | ABC transporter | Transport | 4 |
| SOV5g008400.1 | Cation/H+ antiporter | Transport | 4 |
| SOV2g038560.1 | DETOXIFICATION protein | Transport | 4 |
| SOV5g032210.1 | NRT1/PTR transporter | Transport | 4 |
| SOV6g014710.1 | Cd resistance-like | Transport | 4 |
| SOV3g000640.1 | G3P transporter | Transport | 4 |
| SOV1g004930.1 | GDSL esterase/lipase | Metabolic | 4 |
| SOV4g008190.1 | GDSL esterase/lipase | Metabolic | 4 |
| SOV6g042250.1 | GDSL esterase/lipase | Metabolic | 4 |
| SOV1g048270.1 | Aspartokinase | Metabolic | 4 |
| SOV5g001320.1 | CTP synthase | Metabolic | 4 |
| SOV6g037220.1 | PPR protein | RNA proc. | 4 |
| SOV6g035270.1 | PPR protein | RNA proc. | 4 |
| SOV5g000510.1 | RNA helicase | RNA proc. | 4 |
| SOV1g048290.1 | Glutamate receptor | Signaling | 4 |
| SOV2g039720.1 | Ca-binding protein | Signaling | 4 |
| SOV5g030510.1 | Protein kinase | Signaling | 4 |
| SOV1g019270.1 | DNA topoisomerase 2 | DNA repair | 4 |
| SOV4g051610.1 | ATR kinase | DNA repair | 4 |
| SOV1g034720.1 | Mito. morphology 35 | Organelle | 4 |
| SOV2g013310.1 | Folate transporter | Transport | 3 |
| SOV4g006140.1 | Choline phosphotransferase | Metabolic | 3 |
| SOV6g042110.1 | Glyoxylate reductase | Metabolic | 3 |
| SOV4g005210.1 | PPR protein | RNA proc. | 3 |
| SOV4g023530.1 | LUC7 (splicing) | RNA proc. | 3 |
| SOV4g046320.1 | Ser/Thr kinase | Signaling | 3 |
| SOV6g037890.1 | Patellin-6 | Signaling | 3 |
| SOV4g011580.1 | DNA polymerase | DNA repair | 3 |
| SOV5g013920.1 | CRM factor CFM3 | Organelle | 3 |
| SOV2g025780.1 | TIM50-like import | Organelle | 3 |
| SOV5g034290.1 | Cyt c biogenesis | Organelle | 3 |
| SOV3g020770.1 | TIC214 (chloroplast) | Organelle | 3 |
| SOV4g054740.1 | RETICULATA | Organelle | 3 |

Low-priority (39 targets): chaperones, unknowns, transposon elements, housekeeping, contamination artifacts. Full list available in knowledge base.

---

## Bibliography

[1] Finch-Savage, W.E. & Leubner-Metzger, G. (2006). *New Phytologist*, 171(3), 501-523. DOI: 10.1111/j.1469-8137.2006.01787.x

[2] Bewley, J.D. (1997). *The Plant Cell*, 9(7), 1055-1066. DOI: 10.1105/tpc.9.7.1055

[3] Weitbrecht, K. et al. (2011). *J. Exp. Bot.*, 62(10), 3289-3309. DOI: 10.1093/jxb/err030

[4] Shu, K. et al. (2018). *Front. Plant Sci.*, 9, 416. DOI: 10.3389/fpls.2018.00416

[5] Tuan, P.A. et al. (2018). *Front. Plant Sci.*, 9, 668. DOI: 10.3389/fpls.2018.00668

[6] Paparella, S. et al. (2015). *Plant Cell Rep.*, 34(8), 1281-1293. DOI: 10.1007/s00299-015-1784-y

[7] Upadhyay, S.K. et al. (2011). *Pedosphere*, 21(2), 214-222. DOI: 10.1016/S1002-0160(11)60120-3

[8] Weiberg, A. et al. (2013). *Science*, 342(6154), 118-123. DOI: 10.1126/science.1239705

[9] Cai, Q. et al. (2018). *Science*, 360(6393), 1126-1129. DOI: 10.1126/science.aar4142

[10] He, B. et al. (2023). *Nat. Commun.*, 14, 4552. DOI: 10.1038/s41467-023-40093-4

[11] Ravet, A. et al. (2025). *Nat. Commun.*, 16, 3533. DOI: 10.1038/s41467-025-57908-1

[12] Cai, Q. et al. (2021). *Annu. Rev. Plant Biol.*, 72, 497-524. DOI: 10.1146/annurev-arplant-081720-010616

[13] The Arabidopsis Genome Initiative (2000). *Nature*, 408, 796-815. DOI: 10.1038/35048692

[14] Bleecker, A.B. & Kende, H. (2000). *Annu. Rev. Cell Dev. Biol.*, 16, 1-18. DOI: 10.1146/annurev.cellbio.16.1.1

[15] Kawakatsu, T. et al. (2017). *Genome Biol.*, 18, 171. DOI: 10.1186/s13059-017-1251-x

[16] Tang, D. et al. (2005). *Plant J.*, 44(2), 245-257. DOI: 10.1111/j.1365-313X.2005.02523.x

[17] Wasternack, C. & Hause, B. (2013). *Ann. Bot.*, 111(6), 1021-1058. DOI: 10.1093/aob/mct067

[18] Huot, B. et al. (2014). *Mol. Plant*, 7(8), 1267-1287. DOI: 10.1093/mp/ssu049

[19] Boller, T. & Felix, G. (2009). *Annu. Rev. Plant Biol.*, 60, 379-406. DOI: 10.1146/annurev.arplant.57.032905.105346

[20] Nie, X. et al. (2014). *Biol. Open*, 3(9), 794-802. DOI: 10.1242/bio.20148680

[21] Narsai, R. et al. (2017). *Genome Biol.*, 18, 172. DOI: 10.1186/s13059-017-1302-3

[22] Li, S. et al. (2022). *Front. Plant Sci.*, 13, 1050132. DOI: 10.3389/fpls.2022.1050132

[23] Ishibashi, Y. et al. (2017). *Front. Plant Sci.*, 8, 275. DOI: 10.3389/fpls.2017.00275

[24] Bailly, C. (2004). *Seed Sci. Res.*, 14(2), 93-107. DOI: 10.1079/SSR2004159

[25] Moeder, W. et al. (2011). *Mol. Plant*, 4(3), 442-452. DOI: 10.1093/mp/ssr018

[26] Tsai, A.Y. & Gazzarrini, S. (2014). *Front. Plant Sci.*, 5, 119. DOI: 10.3389/fpls.2014.00119

[27] Zipfel, C. (2014). *Trends Immunol.*, 35(7), 345-351. DOI: 10.1016/j.it.2014.05.004

[28] Lugtenberg, B. & Kamilova, F. (2009). *Annu. Rev. Microbiol.*, 63, 541-556. DOI: 10.1146/annurev.micro.62.081307.162918

[29] Naseem, H. & Bano, A. (2014). *J. Plant Interact.*, 9(1), 689-701. DOI: 10.1080/17429145.2014.902125

[30] Flemming, H.C. & Wingender, J. (2010). *Nat. Rev. Microbiol.*, 8(9), 623-633. DOI: 10.1038/nrmicro2415

[31] Flemming, H.C. et al. (2016). *Nat. Rev. Microbiol.*, 14(9), 563-575. DOI: 10.1038/nrmicro.2016.94

[32] Vandesompele, J. et al. (2002). *Genome Biol.*, 3(7), RESEARCH0034. DOI: 10.1186/gb-2002-3-7-research0034

[33] Andersen, C.L. et al. (2004). *Cancer Res.*, 64(15), 5245-5250. DOI: 10.1158/0008-5472.CAN-04-0496

[34] Addo-Quaye, C. et al. (2008). *Curr. Biol.*, 18(10), 758-762. DOI: 10.1016/j.cub.2008.04.042

[35] German, M.A. et al. (2008). *Nat. Biotechnol.*, 26(8), 941-946. DOI: 10.1038/nbt1417
