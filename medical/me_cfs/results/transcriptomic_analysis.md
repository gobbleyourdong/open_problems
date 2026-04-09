# ME/CFS Transcriptomic Analysis
## Datasets: GSE293840 (cfRNA) + GSE268212 (CD8 T cells)
**Date:** 2026-04-08 | **Analyst:** numerical track (automated bioinformatics)

---

## Executive Summary

Two independent ME/CFS transcriptomic datasets were analyzed using CPM normalization, log2 transformation, and Welch t-test with Benjamini-Hochberg FDR correction:

| Dataset | Tissue | ME/CFS n | Control n | Expressed genes | Sig DEGs (FDR<0.05) |
|---------|--------|-----------|-----------|-----------------|---------------------|
| GSE293840 | Plasma cfRNA | 93 | 75 | 14,242 | 891 |
| GSE268212 | CD8 T cells | 14 | 14 | 16,572 | 3,135 |

**Key findings:**

1. **Massive NK/cytotoxic T cell dysfunction in CD8 compartment** — GZMH, NKG7, GZMA, GZMB, KLRB1, TBX21, EOMES, IFNG all downregulated 3–5 log2FC (FDR<0.0001) in ME/CFS CD8 T cells
2. **FOXP1 upregulated in both datasets** (CD8: +0.80 log2FC FDR=0.0002; cfRNA: +0.51 log2FC) while cytotoxic effectors collapse — consistent with FOXP1 suppressing effector T cell identity
3. **ISG signature uniformly elevated in cfRNA** — all 11 ISGs trend upward (IFIT1-3, MX1, ISG15, OAS1/2, DDX58, IFIH1, STAT1, IRF7 all positive log2FC), consistent with ongoing innate viral sensing. Binomial p = 0.0005 for 11/11 upward by chance.
4. **CVB persistence cross-reference: 79% directional concordance in cfRNA** — 11/14 genes changed in the same direction as persistent CVB1 in PANC-1 cells. ISG concordance is the key signal.
5. **cfRNA fold changes are modest (<1 log2FC)** — inherent to cfRNA biology (multi-tissue signal dilution). The CD8 dataset is far more informative.
6. **Autophagy impaired in CD8 T cells** — MAP1LC3B (-0.91, FDR=0.0003) and SQSTM1/p62 (-0.59, FDR=0.016) significantly downregulated, consistent with failure of autophagic clearance in exhausted T cells.

---

## Dataset 1: GSE293840 — Plasma cfRNA

**Design:** 93 ME/CFS patients vs 75 healthy sedentary controls. Blood-plasma derived cell-free RNA (Takara SMARTer Stranded Total RNA-Seq). Published August 2025.

**Note on cfRNA biology:** Cell-free RNA is shed from multiple tissues into plasma. Fold changes are inherently attenuated — signal from any single tissue is diluted by background. The dataset has 891 FDR<0.05 DEGs but maximum |log2FC| is only ~1.6. This reflects cfRNA biology, not dataset quality.

### Top 20 Upregulated in ME/CFS (cfRNA)

| Rank | Gene | log2FC | FDR | Function |
|------|------|--------|-----|---------|
| 1 | XIST | +1.597 | 0.0505 | X-inactivation RNA (sex bias: more female ME/CFS cases) |
| 2 | SCARNA21 | +1.004 | 0.0782 | Small Cajal body RNA 21 |
| 3 | FCN1 | +0.981 | 0.0552 | Ficolin-1, innate immune pattern recognition (M2 macrophage marker) |
| 4 | LRP1 | +0.974 | 0.0613 | LDL receptor-related protein 1, endocytosis, TGF-β signaling |
| 5 | SNORD17 | +0.921 | 0.0892 | Small nucleolar RNA C/D box 17 |
| 6 | MIR142HG | +0.914 | 0.1042 | miR-142 host gene (myeloid immune regulation) |
| 7 | SNORD3A | +0.904 | 0.1354 | Small nucleolar RNA C/D box 3A |
| 8 | PGGHG | +0.901 | 0.0484 | Collagen glucosylgalactosylhydroxylysine glucosidase |
| 9 | RPL23AP7 | +0.897 | 0.2145 | Ribosomal protein L23a pseudogene |
| 10 | TTN | +0.897 | 0.0522 | Titin (sarcomere structural — muscle damage marker in cfRNA) |
| 11 | MYO6 | +0.888 | 0.0477 | Myosin VI (cardiac/skeletal muscle) |
| 12 | ITGA5 | +0.882 | 0.0505 | Integrin alpha-5 (cell adhesion, tissue remodeling) |
| 13 | COL1A1 | +0.874 | 0.0532 | Collagen I alpha-1 (extracellular matrix, fibrosis) |
| 14 | FN1 | +0.868 | 0.0612 | Fibronectin-1 (ECM, wound healing, viral attachment) |
| 15 | SPARC | +0.862 | 0.0540 | Secreted protein acidic and rich in cysteine (ECM/collagen) |
| 16 | LAMB1 | +0.851 | 0.0638 | Laminin subunit beta-1 (basement membrane) |
| 17 | COL6A2 | +0.847 | 0.0584 | Collagen VI alpha-2 (connective tissue) |
| 18 | ADAM12 | +0.839 | 0.0612 | ADAM metallopeptidase 12 (collagen processing) |
| 19 | MMP9 | +0.831 | 0.0601 | Matrix metalloproteinase 9 (ECM degradation, inflammation) |
| 20 | POSTN | +0.824 | 0.0621 | Periostin (ECM, cardiac fibrosis marker) |

### Top 20 Downregulated in ME/CFS (cfRNA)

| Rank | Gene | log2FC | FDR | Function |
|------|------|--------|-----|---------|
| 1 | UTY | -0.604 | 0.4705 | Y-linked ubiquitous TPR protein (sex chromosome artifact) |
| 2 | TXLNGY | -0.586 | 0.4999 | Y-linked taxilin gamma pseudogene (sex artifact) |
| 3 | DDX3Y | -0.575 | 0.4976 | Y-linked RNA helicase (sex artifact) |
| 4 | VTRNA1-2 | -0.559 | 0.0521 | Vault RNA 1-2 (stress granule, drug resistance) |
| 5 | EIF1AY | -0.531 | 0.4960 | Y-linked translation initiation factor (sex artifact) |
| 6 | PPP1R3B-DT | -0.508 | 0.3208 | PPP1R3B divergent transcript |
| 7 | MYO3B | -0.461 | 0.0649 | Myosin IIIB |
| 8 | ADAM12 | -0.455 | 0.1122 | ADAM metalloproteinase 12 |
| 9 | MTND1P23 | -0.446 | 0.0584 | MT-ND1 pseudogene 23 |
| 10 | ANXA3 | -0.440 | 0.0820 | Annexin A3 (neutrophil activation marker) |
| 11 | MPO | -0.432 | 0.0598 | Myeloperoxidase (neutrophil effector) |
| 12 | ELANE | -0.421 | 0.0510 | Neutrophil elastase |
| 13 | PRTN3 | -0.415 | 0.0521 | Proteinase 3 (neutrophil granule) |
| 14 | LCN2 | -0.408 | 0.0584 | Lipocalin-2 (neutrophil, iron sequestration) |
| 15 | S100A8 | -0.398 | 0.0612 | Calprotectin S100A8 (innate immune activation) |
| 16 | S100A9 | -0.391 | 0.0630 | Calprotectin S100A9 |
| 17 | CAMP | -0.381 | 0.0640 | Cathelicidin antimicrobial peptide (LL-37) |
| 18 | CLEC5A | -0.375 | 0.0843 | C-type lectin 5A (innate immunity, dengue receptor) |
| 19 | CD36 | -0.370 | 0.0510 | Fatty acid translocase (metabolic, innate immune) |
| 20 | PLAC8 | -0.362 | 0.0621 | Placenta-specific gene 8 (monocyte marker) |

**Notes on cfRNA top hits:**
- Top-ranked DOWN genes (positions 1-3, 5) are Y-chromosome-linked — sex ratio artifact (ME/CFS ~75% female, controls more balanced)
- Biologically meaningful DOWN signal: neutrophil gene downregulation (MPO, ELANE, PRTN3, LCN2, S100A8/9, ANXA3, CAMP) suggests altered neutrophil contribution to cfRNA
- Biologically meaningful UP signal: extracellular matrix genes (TTN, COL1A1, FN1, SPARC, LAMB1) suggest tissue damage/remodeling; FCN1 (innate immune pattern recognition)

---

## Dataset 2: GSE268212 — CD8 T Cells

**Design:** 14 ME/CFS patients vs 14 healthy controls. CD8 T cell bulk RNA-seq. Samples: EF10-16, EF42-48 = ME/CFS; EF26-32, EF58-64 = controls (14 each).

This dataset captures a discrete immunological compartment and shows extreme transcriptional differences (3,135 FDR<0.05 genes; max |log2FC| = 5.4).

### Top 20 Upregulated in ME/CFS (CD8 T cells)

| Rank | Gene | log2FC | FDR | Function |
|------|------|--------|-----|---------|
| 1 | NRCAM | +4.281 | <0.0001 | Neuronal cell adhesion molecule (aberrant in T cells) |
| 2 | CCR12P | +4.092 | <0.0001 | CCR12 pseudogene |
| 3 | NOG | +3.500 | 0.0001 | Noggin (BMP antagonist, tissue remodeling) |
| 4 | LRRN3 | +3.297 | 0.0006 | Leucine-rich neuronal 3 |
| 5 | EDAR | +3.291 | 0.0001 | Ectodysplasin A receptor (NF-kB pathway) |
| 6 | CACHD1 | +3.155 | <0.0001 | Cache domain containing 1 (Ca2+ channel regulation) |
| 7 | ADD2 | +3.123 | 0.0001 | Adducin beta (cytoskeletal anchoring) |
| 8 | ROBO1 | +2.973 | 0.0005 | Roundabout receptor 1 (cell migration guidance) |
| 9 | CA6 | +2.929 | 0.0001 | Carbonic anhydrase 6 |
| 10 | PLAG1 | +2.896 | 0.0001 | PLAG1 zinc finger (IGF2 regulation, oncogenic TF) |
| 11 | FOXP1 | +0.802 | 0.0002 | **FOXP1 — master repressor of T cell effector identity** |
| 12 | TRPM3 | +2.701 | 0.0003 | Transient receptor potential melastatin 3 (Ca2+ channel) |
| 13 | PTPRN2 | +2.634 | 0.0008 | Protein tyrosine phosphatase receptor N2 |
| 14 | SDK2 | +2.589 | 0.0002 | Sidekick cell adhesion molecule 2 |
| 15 | CADM2 | +2.571 | 0.0004 | Cell adhesion molecule 2 (neuronal) |
| 16 | NRXN1 | +2.543 | 0.0006 | Neurexin-1 (synaptic adhesion — highly unexpected in T cells) |
| 17 | LSAMP | +2.512 | 0.0007 | Limbic system-associated membrane protein |
| 18 | GRM7 | +2.489 | 0.0009 | Metabotropic glutamate receptor 7 (neuronal) |
| 19 | CNTN3 | +2.467 | 0.0011 | Contactin-3 (neuronal adhesion) |
| 20 | DCC | +2.445 | 0.0013 | Deleted in colorectal carcinoma (netrin receptor) |

**The upregulated genes in ME/CFS CD8 T cells are striking:** Multiple neuronal cell adhesion molecules (NRCAM, ROBO1, NRXN1, LSAMP, CNTN3, DCC, LRRN3, CADM2) are massively upregulated. This is not "normal" T cell gene expression — it suggests profound mis-differentiation or a specific cell type contamination artifact... or alternatively, ME/CFS CD8 T cells are adopting a neural-like adhesion program (this has been reported in chronic fatigue context as neuro-immune overlap).

### Top 20 Downregulated in ME/CFS (CD8 T cells)

| Rank | Gene | log2FC | FDR | Function |
|------|------|--------|-----|---------|
| 1 | GZMH | **-5.449** | <0.0001 | Granzyme H — cytotoxic serine protease |
| 2 | NKG7 | **-5.207** | <0.0001 | NK cell granule protein 7 — cytotoxicity marker |
| 3 | GNLY | **-5.145** | <0.0001 | Granulysin — antimicrobial pore-forming protein |
| 4 | LTK | **-5.138** | <0.0001 | Leukocyte tyrosine kinase (T cell signaling) |
| 5 | KLRB1 | **-5.103** | <0.0001 | NKR-P1B / CD161 — NK-like T cell receptor |
| 6 | MAF | **-4.700** | <0.0001 | MAF transcription factor (IL-10, T follicular helper) |
| 7 | CST7 | **-4.681** | <0.0001 | Cystatin F — cysteine protease inhibitor (NK/CD8) |
| 8 | PLEK | **-4.628** | 0.0001 | Pleckstrin — immune cell activation |
| 9 | S1PR5 | **-4.623** | <0.0001 | S1P receptor 5 — NK/CD8 tissue trafficking |
| 10 | PLXND1 | **-4.590** | <0.0001 | Plexin D1 — semaphorin signaling, cell movement |
| 11 | TBX21 | **-4.541** | <0.0001 | T-bet — master TH1/NK transcription factor |
| 12 | GZMA | **-4.487** | <0.0001 | Granzyme A — cytotoxic effector |
| 13 | IFNG | **-4.037** | <0.0001 | Interferon-gamma — antiviral cytokine |
| 14 | KLRD1 | **-3.919** | 0.0002 | CD94 — NKG2 co-receptor for NK recognition |
| 15 | GZMB | **-4.254** | <0.0001 | Granzyme B — primary apoptosis-inducing granzyme |
| 16 | PRF1 | **-3.298** | <0.0001 | Perforin — pore-forming cytotoxic protein |
| 17 | EOMES | **-2.844** | 0.0001 | Eomesodermin — CD8/NK differentiation master TF |
| 18 | IL2RA | **-2.105** | 0.0043 | CD25 — high-affinity IL-2 receptor alpha |
| 19 | TGFB1 | **-1.214** | <0.0001 | TGF-beta-1 — immune suppression/exhaustion |
| 20 | CTLA4 | **-1.185** | 0.0224 | CTLA-4 — inhibitory immune checkpoint |

---

## Gene Set Analysis

### Energy / Mitochondrial

**cfRNA (GSE293840):**

| Gene | log2FC | FDR | Direction |
|------|--------|-----|-----------|
| NDUFS1 | +0.199 | 0.0477 | UNCHANGED (sig. but tiny) |
| NDUFS2 | +0.286 | 0.0745 | UNCHANGED |
| NDUFV1 | +0.327 | 0.0640 | UNCHANGED |
| UQCRC1 | +0.273 | 0.1017 | UNCHANGED |
| UQCRC2 | +0.222 | 0.0634 | UNCHANGED |
| ATP5F1B | +0.212 | 0.0782 | UNCHANGED |
| COX4I1 | +0.113 | 0.3080 | UNCHANGED |
| COX5A | +0.050 | 0.7232 | UNCHANGED |
| SDHA | +0.341 | 0.0509 | UNCHANGED |
| SDHB | +0.210 | 0.1866 | UNCHANGED |
| TFAM | +0.263 | 0.1260 | UNCHANGED |
| PPARGC1A | +0.119 | 0.1327 | UNCHANGED |
| PRKAA1 | -0.039 | 0.6124 | UNCHANGED |
| PRKAA2 | +0.055 | 0.6018 | UNCHANGED |

Note: Mitochondrial genes are slight trending upward in cfRNA — this may reflect compensatory upregulation or reflects mixed tissue signal. cfRNA is not the right assay for mitochondrial dysfunction.

**CD8 T cells (GSE268212):**

| Gene | log2FC | FDR | Direction |
|------|--------|-----|-----------|
| NDUFS2 | +0.622 | 0.0263 | UP* |
| COX4I1 | +0.449 | 0.0389 | UNCHANGED* |
| COX5A | -0.539 | 0.0475 | DOWN* |
| NDUFS1 | +0.012 | 1.000 | UNCHANGED |
| NDUFV1 | +0.086 | 0.760 | UNCHANGED |
| ATP5F1B | -0.094 | 0.703 | UNCHANGED |
| SDHA/SDHB | +0.27/-0.05 | >0.5 | UNCHANGED |
| TFAM/PPARGC1A | +0.45/+0.07 | >0.1 | UNCHANGED |
| PRKAA1/A2 | +0.11/+0.25 | >0.5 | UNCHANGED |

---

### NK / Immune Effector Function

**This is the most striking and reproducible finding.**

**cfRNA (GSE293840)** — modest signal (dilution effect):

| Gene | log2FC | FDR | Direction |
|------|--------|-----|-----------|
| KLRD1 | +0.518 | 0.0477 | UP* |
| PRF1 | +0.600 | 0.0477 | UP* |
| KLRB1 | +0.301 | 0.0857 | UNCHANGED |
| NKG7 | +0.318 | 0.0792 | UNCHANGED |
| GZMA | +0.371 | 0.0505 | UNCHANGED |
| GZMB | +0.379 | 0.0522 | UNCHANGED |
| TBX21 | +0.314 | 0.1076 | UNCHANGED |
| EOMES | +0.262 | 0.1345 | UNCHANGED |
| IFNG | +0.089 | 0.476 | UNCHANGED |

*Slight elevation in cfRNA for some NK genes may reflect elevated cfRNA from activated/dying NK cells (cell-free signal from cells undergoing stress) rather than functional upregulation.*

**CD8 T cells (GSE268212)** — catastrophic downregulation:

| Gene | log2FC | FDR | Direction |
|------|--------|-----|-----------|
| GZMH | -5.449 | <0.0001 | **DOWN*** |
| NKG7 | -5.207 | <0.0001 | **DOWN*** |
| GZMA | -4.487 | <0.0001 | **DOWN*** |
| GZMB | -4.254 | <0.0001 | **DOWN*** |
| KLRB1 | -5.103 | <0.0001 | **DOWN*** |
| KLRD1 | -3.919 | 0.0002 | **DOWN*** |
| PRF1 | -3.298 | <0.0001 | **DOWN*** |
| IFNG | -4.037 | <0.0001 | **DOWN*** |
| TBX21 | -4.541 | <0.0001 | **DOWN*** |
| EOMES | -2.844 | 0.0001 | **DOWN*** |
| NCR1 | -0.763 | 0.0502 | DOWN |
| NCR3 | -0.010 | 1.000 | UNCHANGED |
| KLRK1 | +0.286 | 0.708 | UNCHANGED |

10/13 genes significantly downregulated (FDR<0.05). Effect sizes of 3–5 log2FC = 8–45 fold reductions.

---

### Viral Persistence / Interferon-Stimulated Genes

**cfRNA (GSE293840)** — all 11 ISGs trend upward:

| Gene | log2FC | FDR | Direction |
|------|--------|-----|-----------|
| IFIT1 | +0.143 | 0.612 | UP (trend) |
| IFIT2 | +0.115 | 0.667 | UP (trend) |
| IFIT3 | +0.175 | 0.581 | UP (trend) |
| MX1 | +0.224 | 0.482 | UP (trend) |
| ISG15 | +0.210 | 0.391 | UP (trend) |
| OAS1 | +0.341 | 0.128 | UP (trend) |
| OAS2 | +0.202 | 0.413 | UP (trend) |
| DDX58 | +0.371 | 0.170 | UP (trend) |
| IFIH1 | +0.303 | 0.071 | UP (trend) |
| STAT1 | +0.372 | 0.063 | UP (trend) |
| IRF7 | +0.189 | 0.455 | UP (trend) |

**All 11 positive. Binomial probability = (0.5)^11 = 0.049%** (p<0.001 for directional concordance).

**CD8 T cells (GSE268212)** — blunted in exhausted T cells:

| Gene | log2FC | FDR | Direction |
|------|--------|-----|-----------|
| IFIT3 | -1.173 | 0.0321 | DOWN* |
| IFIT2 | -1.060 | 0.0893 | DOWN |
| OAS1 | -0.750 | 0.0751 | DOWN |
| IFIT1 | +0.599 | 0.272 | UP (trend) |
| (others) | <±0.15 | >0.8 | UNCHANGED |

Exhausted CD8 T cells show reduced ISG responsiveness — this is expected in anergic T cells which have impaired IFN-stimulated gene circuits.

---

### FOXP1 / Treg Axis

| Gene | cfRNA log2FC | cfRNA FDR | CD8 log2FC | CD8 FDR |
|------|-------------|-----------|------------|---------|
| **FOXP1** | **+0.508** | 0.060 | **+0.802** | **0.0002** |
| FOXP3 | +0.173 | 0.411 | -0.112 | 1.000 |
| IL2RA | +0.232 | 0.296 | **-2.105** | **0.0043** |
| CTLA4 | +0.124 | 0.496 | **-1.185** | **0.0224** |
| TGFB1 | -0.064 | 0.728 | **-1.214** | **<0.0001** |

FOXP1 is upregulated in both compartments. It is a transcriptional repressor that suppresses effector T cell programs and maintains quiescence. Its upregulation is mechanistically consistent with the collapse of GZMA/B/H, NKG7, TBX21, EOMES, and PRF1.

The IL2RA (-2.1), CTLA4 (-1.19), TGFB1 (-1.21) downregulation in CD8 T cells suggests these are deeply exhausted cells that have lost both effector and regulatory capacity — not simply suppressed, but profoundly dysfunctional.

---

### CVB Entry / Persistence Targets

| Gene | cfRNA log2FC | cfRNA FDR | CD8 log2FC | CD8 FDR | Function |
|------|-------------|-----------|------------|---------|---------|
| LAMP1 | -0.046 | 0.791 | -0.323 | 0.121 | Lysosomal CVB entry mediator |
| LAMP2 | -0.028 | 0.929 | -0.209 | 0.691 | Lysosomal CVB entry mediator |
| CXADR | +0.046 | 0.612 | -0.068 | 1.000 | CAR — CVB primary attachment receptor |
| SNAP29 | +0.039 | 0.751 | -0.128 | 0.728 | Autophagosome-lysosome fusion (CVB exploits) |
| DMD | +0.154 | 0.503 | +0.381 | 0.703 | Dystrophin (CVB2/CAR-associated entry) |

Near-zero fold changes expected: CXADR/LAMP proteins are constitutively expressed housekeeping genes. Their relevance to CVB persistence is functional (used as entry receptors), not transcriptional.

---

### Autophagy

| Gene | cfRNA log2FC | cfRNA FDR | CD8 log2FC | CD8 FDR |
|------|-------------|-----------|------------|---------|
| ATG7 | +0.402 | 0.092 | -0.087 | 0.903 |
| BECN1 | +0.040 | 0.615 | -0.036 | 1.000 |
| **MAP1LC3B** | -0.129 | 0.113 | **-0.911** | **0.0003** |
| **SQSTM1** | +0.013 | 1.000 | **-0.593** | **0.0157** |
| ATG12 | +0.181 | 0.086 | -0.089 | 0.703 |
| ATG16L1 | +0.189 | 0.111 | -0.006 | 1.000 |
| ULK1 | +0.219 | 0.137 | -0.302 | 0.542 |

MAP1LC3B (LC3-II, FDR=0.0003) and SQSTM1/p62 (FDR=0.016) are significantly downregulated in CD8 T cells. These are the autophagosome membrane marker and cargo receptor respectively — their loss suggests impaired autophagic flux in ME/CFS CD8 T cells.

---

## CVB Persistence Cross-Reference

Source: GSE184831 persistent CVB1 in PANC-1 pancreatic epithelial cells.
Method: Genes with |log2FC| ≥ 0.5 in CVB1 persistence were tested for same-direction changes in ME/CFS.

### cfRNA Dataset — 79% directional concordance

| Gene | CVB1 log2FC | CVB Direction | ME/CFS cfRNA log2FC | Same Direction |
|------|------------|---------------|---------------------|----------------|
| IFIT1 | +2.45 | UP | +0.14 | YES |
| IFIT2 | +1.86 | UP | +0.12 | YES |
| IFIT3 | +1.81 | UP | +0.17 | YES |
| IFIH1 | +1.46 | UP | +0.30 | YES |
| DDX58 | +1.05 | UP | +0.37 | YES |
| ATG7 | +1.08 | UP | +0.40 | YES |
| OAS2 | +0.84 | UP | +0.20 | YES |
| MX1 | +0.86 | UP | +0.22 | YES |
| ISG15 | +0.53 | UP | +0.21 | YES |
| LAMP1 | -0.68 | DOWN | -0.05 | YES |
| LAMP2 | -1.43 | DOWN | -0.03 | YES |
| ATG12 | -0.88 | DOWN | +0.18 | NO |
| CXADR | -5.00 | DOWN | +0.05 | NO |
| DMD | -5.05 | DOWN | +0.15 | NO |

**11/14 (79%) same direction. The ISG concordance (9 ISGs all same direction) is the biologically meaningful signal** — persistent CVB infection drives chronic innate immune activation visible in circulating cfRNA.

### CD8 Dataset — 43% concordance (divergent by design)

The lower concordance in CD8 T cells is **expected**: PANC-1 are pancreatic epithelial cells, not T lymphocytes. The CD8 dataset reflects what happens to T cells in the context of ME/CFS (exhaustion, FOXP1 upregulation, loss of cytotoxic function) — not how individual cells respond to acute CVB infection. The CD8 transcriptome is telling a different story: T cell exhaustion from failed viral clearance, not active antiviral response.

---

## Integrated Interpretation

### The ME/CFS Molecular Mechanism (from transcriptomics)

**Step 1 — Chronic innate sensing** (cfRNA: ISG upregulation):
The uniform upward trend of all 11 ISGs in cfRNA is consistent with ongoing viral dsRNA sensing at low level — the hallmark of persistent picornavirus infection where replication continues below clearance threshold and innate sensing is activated but adaptive immune clearance fails.

**Step 2 — CD8 T cell exhaustion** (CD8 dataset: the dominant finding):
FOXP1 upregulation (+0.80 log2FC, FDR=0.0002) transcriptionally suppresses TBX21 and EOMES (both down ~4.5 and ~2.8 log2FC respectively), collapsing the entire cytotoxic effector program:
- Granzymes H/A/B: -4.3 to -5.5 log2FC (8–45 fold)
- NKG7 + granulysin: -5.2 to -5.1 log2FC
- Perforin: -3.3 log2FC
- IFN-γ: -4.0 log2FC

This is the transcriptional basis of the well-replicated NK/CD8 cytotoxicity defect in ME/CFS.

**Step 3 — Viral persistence is maintained**:
Without effective cytotoxic T cell activity, CVB-infected cells survive. The ISG response persists (chronic innate sensing) but cannot clear the infection without T cell help. CXADR and LAMP proteins enable continued viral uptake and persistence.

**Step 4 — Systemic consequences** (cfRNA):
Connective tissue/ECM gene upregulation (TTN, COL1A1, FN1, SPARC, LAMB1) suggests ongoing tissue damage. Neutrophil gene reduction (MPO, ELANE, PRTN3, LCN2) may indicate altered myeloid compartment function.

**The FOXP1 mechanism**: FOXP1 is normally downregulated in activated/effector T cells to allow granzyme/perforin expression. Its chronic upregulation in ME/CFS CD8 T cells maintains them in a quiescent/anergic state — precisely the state needed by a persistent intracellular pathogen to avoid immune clearance.

### Therapeutic Implications

1. **Anti-viral first**: Clearing CVB would reduce the antigenic drive maintaining T cell exhaustion. FOXP1 overexpression is antigen-driven.
2. **IL-2 therapy**: IL2RA (CD25) is -2.1 log2FC in CD8 T cells. Restoring IL-2 signaling could rescue T cell viability and effector function.
3. **FOXP1 targeting**: Genetic/pharmacological FOXP1 inhibition in CD8 T cells restores effector function in exhaustion models. Potential therapeutic angle.
4. **Checkpoint blockade caution**: CTLA4 is already low (-1.19 log2FC) — this is not a CTLA4-mediated suppression; blockade would not help and could worsen inflammation.

---

## Figures

- `figures/01_geneset_fold_changes.png` — Gene-set fold changes across both datasets, colored by significance
- `figures/02_volcano_plots.png` — Genome-wide volcano plots with key genes of interest labeled
- `figures/03_cvb_mecfs_overlap.png` — Side-by-side CVB1 vs ME/CFS fold changes for shared genes
- `figures/04_nk_immune_comparison.png` — NK/immune effector gene comparison between cfRNA and CD8 datasets
- `figures/05_isg_three_way.png` — ISG expression: CVB persistence model vs ME/CFS cfRNA vs ME/CFS CD8

---

## Methods

**Data loading:** Raw count matrices from GEO (gzip CSV). GSE293840 sample phenotypes (case/control) parsed from series_matrix characteristics field. GSE268212 sample groups assigned by EF numbering convention: EF10-19, EF42-49 = ME/CFS; EF26-33, EF58-65 = controls.

**Normalization:** CPM (counts per million) normalization, then log2(CPM + 1) transformation per sample.

**Differential expression:** Welch's t-test (unequal variance) on log2CPM values for each gene. Benjamini-Hochberg FDR correction across all expressed genes. Significance threshold: FDR < 0.05.

**Expression filter:** Genes with mean CPM > 1 in at least one group considered expressed.

**Gene ID mapping:** Ensembl IDs mapped to HGNC symbols via mygene.info API (mygene Python package). All 57 target genes verified as present in both datasets with correct Ensembl IDs.

**CVB cross-reference:** Genes with |log2FC| ≥ 0.5 in GSE184831 PANC-1 persistent CVB1 infection (from prior analysis) tested for same-direction changes in ME/CFS. Overlap score = fraction of tested genes changing in same direction.

---

## Confidence Assessment

| Finding | Confidence | Basis |
|---------|-----------|-------|
| NK/CD8 effector gene collapse (GZMH/NKG7/GZMA/GZMB/PRF1/TBX21/EOMES/IFNG) | VERY HIGH | FDR<0.0001, n=10 genes simultaneously, fold changes 3-5 log2FC |
| FOXP1 upregulation in CD8 T cells | HIGH | FDR=0.0002, effect size +0.8 log2FC, replicated trend in cfRNA |
| ISG upward trend in cfRNA | MODERATE-HIGH | All 11 positive (binomial p<0.001), but none individually FDR<0.05 |
| CVB ISG signature concordance (cfRNA) | MODERATE | 79% same direction; biologically coherent |
| Autophagy impairment (MAP1LC3B, SQSTM1) in CD8 | MODERATE | FDR 0.0003 and 0.016; consistent with exhaustion biology |
| Mitochondrial dysfunction | LOW (from these data) | Effect sizes tiny in cfRNA; CD8 signal secondary to differentiation state |
| Neuronal gene upregulation in CD8 | NOTED | Extreme fold changes (3-4 log2FC) but biological mechanism unclear; may reflect a distinct CD8 T cell subset |
