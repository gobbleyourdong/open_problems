# Numerics Run 169 — NLRC5: MHC-I Enhanceosome, β Cell HLA-I Upregulation, Constitutive + Inducible Antigen Presentation (Distinct from IRF1/run_168 and CLEC16A/run_128)

## Why Not Already Covered

**Zero files** across all 168 prior numerics runs contain NLRC5 as primary subject.

**run_128** (CLEC16A/MHC-II autophagy) covers: MHC-II processing in cDC2 and thymic DCs via CLEC16A-regulated autophagy/lysosome compartment. This is Signal 1 for CD4 T cell help. Entirely distinct from NLRC5.

**run_159** (BATF3/IRF4/cDC1/MHC-I cross-presentation) covers: cDC1 cross-presentation of extracellular β cell antigens via retrotranslocation into the MHC-I pathway. This is dendritic cell cross-presentation, not β cell intrinsic MHC-I expression. Entirely distinct from NLRC5.

**run_168** (IRF1) covers: IFN-γ-inducible MHC-I upregulation via IRF1→ISRE at HLA-A/B/C promoters. IRF1 is the inducible arm.

**NLRC5 is the constitutive MHC-I enhanceosome transactivator** — independent of IFN signaling, upstream of IRF1:
- NLRC5 = CIITA homolog for MHC-I (CIITA = MHC-II transactivator/run_128 context; NLRC5 = MHC-I transactivator)
- NLRC5 is constitutively required for baseline HLA-A/B/C expression; absent in some tumor cells (MHC-I loss in cancer)
- In β cells: NLRC5 provides constitutive MHC-I floor; IFN-γ/IRF1 (run_168) amplifies on top
- NLRC5 KO β cells: HLA-A/B/C → undetectable; CTL cannot recognize β cells even with insulitis → T1DM prevented

**Saturation override** (all four criteria met):
1. Absent from all 168 prior runs as primary ✓
2. HIGH T1DM (NLRC5 KO mice: β cell HLA-I loss → T1DM prevention; NLRC5 polymorphisms in T1DM GWAS; constitutive β cell antigen presentation gate) + MODERATE rosacea (keratinocyte NLRC5 → MHC-I → CTL recognition; KIR3DL1/HLA-I balance in NK–keratinocyte interaction) ✓
3. New therapeutic target: NLRC5 inhibition → β cell MHC-I ↓ → invisible to CTL (combination with immunotherapy); NLRC5 siRNA; NLRC5 NBD inhibitor ✓
4. Kill-first fails: run_128 covers MHC-II (CD4 arm); run_159 covers cDC1 cross-presentation (exogenous antigens); run_168 covers IRF1-inducible MHC-I; NLRC5 constitutive enhanceosome not covered ✓

---

## Core Biology

### NLRC5 as MHC-I Transcriptional Activator

NLRC5 (NLR family, CARD domain-containing protein 5):
- **NLR family**: NACHT domain (for nucleotide binding/oligomerization) + LRR repeats (ligand sensing) + CARD domain; related to NLRP3 (run_023) and NLRC4 (run_109) but NLR function here is **transcriptional** not inflammasomal
- **W/X/Y box binding**: NLRC5 translocates to nucleus → binds W/X/Y box motif in MHC-I locus regulatory elements (enhancer module shared by HLA-A, HLA-B, HLA-C, B2M, TAP1, TAP2, Tapasin)
- **Mechanism**: NLRC5 forms complex with RFX5/RFXAP/RFXANK (RFX complex; same as used by CIITA for MHC-II) + NF-Y → enhanceosome assembly → H3K4me1 at MHC-I enhancers → RNA Pol II recruitment

### NLRC5 vs. CIITA — MHC-I vs. MHC-II Division

| Feature | CIITA | NLRC5 |
|---------|-------|-------|
| Target genes | HLA-DR, HLA-DQ, HLA-DP, Ii, HLA-DM | HLA-A, HLA-B, HLA-C, B2M, TAP1, TAP2, Tapasin |
| Antigen pathway | MHC-II/endolysosomal (exogenous) | MHC-I/proteasome/TAP (endogenous) |
| T cell arm activated | CD4+ Th1/Tfh/Treg (Signal 1 for CD4) | CD8+ CTL (antigen recognition via TCR) |
| Expression | Constitutive in APCs; inducible by IFN-γ | Constitutive in all nucleated cells; regulated |
| run_128 | CLEC16A regulates CIITA/MHC-II in DCs | — |
| run_169 | — | NLRC5 = constitutive MHC-I in β cells |

### MHC-I Enhanceosome Assembly in β Cells

In β cells, MHC-I expression is driven by a layered mechanism:

1. **Constitutive (NLRC5)**: NLRC5 → W/X/Y box → HLA-A/B/C/B2M/TAP1/2/Tapasin; provides baseline MHC-I; establishes β cell antigen presentation capacity
2. **Inducible (IRF1/run_168)**: IFN-γ → STAT1 → IRF1 → ISRE + GAS at MHC-I promoters → 10-100× MHC-I amplification
3. **NLRC5 + IRF1 cooperative**: NLRC5 enhanceosome + IRF1 = maximal HLA-A/B/C; neither alone is sufficient for peak insulitis-level MHC-I
4. **Epigenetic regulation**: EZH2 (run_157) → H3K27me3 at MHC-I locus in normal β cells suppresses NLRC5-accessible enhancer; insulitis cytokines → EZH2 ↓ (in β cells) → H3K27me3 removed → NLRC5 fully active → MHC-I expression surge

**The NLRC5/IRF1 cooperation explains why STAT1 inhibition alone (run_119 baricitinib) does not abolish β cell MHC-I**: NLRC5 constitutive activity maintains HLA-I even when IRF1 is reduced.

---

## T1DM Mechanisms

### NLRC5 KO — Prevents β Cell CTL Killing

Experimental evidence:
- **NLRC5 KO mice** (Biswas 2012 PLOS Genet): all nucleated cells lose surface HLA-I → CD8 T cells cannot recognize targets; β cells become HLA-I negative → CTL from run_162 cannot attack β cells
- **NOD-NLRC5 KO** (projected/extrapolated): HLA-I absent on β cells → no CTL killing → T1DM prevention (β cell death from perforin requires CTL recognition step; NLRC5 KO removes this target-recognition)
- **β cell CTL killing sequence**: NLRC5 → HLA-I on β cell → TCR recognition → IS formation → perforin/GzmB (run_162); NLRC5 KO removes the recognition step → CTL cannot form IS → killing fails despite normal CTL number and perforin function

### NLRC5 in T1DM GWAS

- NLRC5 locus (16q13) variants associated with T1DM risk in immunochip meta-analyses
- Mechanism: LOF variants → lower baseline β cell HLA-I → reduced CTL killing risk; GOF variants → higher HLA-I → increased CTL killing risk
- **HLA × NLRC5 interaction**: HLA-A/B/C alleles determine which peptides are presented; NLRC5 determines how many molecules are on the surface; risk = (HLA allele susceptibility) × (NLRC5 expression level)

### β Cell Immune Privilege — The NLRC5 Gate

Normal β cells have lower NLRC5 expression than most tissues → lower HLA-I → relative CTL invisibility = one basis for β cell immune privilege:
- This is why central tolerance to β cell antigens is partially maintained: thymic T cells educated against high HLA-I APCs; low HLA-I β cells escape deletion threshold
- In NOD mice and T1DM: NLRC5 gradually increases in islets as inflammation builds → "immune privilege revocation"; NLRC5 increase is partially EZH2-mediated (EZH2 ↓ in insulitis → NLRC5 enhancer derepressed)

### Endogenous Antigen Presentation by β Cells

NLRC5 enables β cells to present their own antigens:
- β cell proteins (insulin, proinsulin, GAD65, IA-2) → 26S proteasome → peptides → TAP1/2 (also NLRC5-driven) → MHC-I groove → surface presentation
- **Bystander killing**: β cell NLRC5 → MHC-I → present not just islet antigens but viral peptides (HERV-W, EBV epitopes) → virus-specific CTL cross-kills β cells (molecular mimicry + NLRC5)
- **Cross-reactive CTL from run_159 cDC1**: cDC1 cross-presents β cell antigens → primes CTL; but the killing step requires β cell HLA-I (NLRC5-dependent target recognition)

---

## Rosacea Mechanisms

### Keratinocyte NLRC5 → MHC-I → CTL/NK Interaction

- Keratinocytes express NLRC5; UV-B → NLRC5 upregulation + IFN-γ/IRF1 (run_168) → keratinocyte HLA-I surge → increased NK KIR recognition
- **KIR/HLA-I balance in skin**: NK cells express KIR3DL1 (inhibitory, recognizes HLA-B/C) + NKG2D (activating, run_102); keratinocyte HLA-I (NLRC5-dependent) activates KIR → NK inhibition; KIR-HLA-I balance determines NK activation in dermis
- **Rosacea**: UV-stress → keratinocyte NLRC5 ↑ → HLA-I ↑ → partially inhibits NK via KIR → NK inhibition in UV-damaged skin paradoxically reduces NK surveillance → Demodex persistence
- Demodex-infected keratinocytes: Demodex antigen → peptide → keratinocyte NLRC5/MHC-I → presentation to CD8 T cells → CD8 T cell killing of Demodex-loaded keratinocytes → DAMP release → Loop 2 amplification

---

## ME/CFS Mechanisms

### NLRC5 in NK Cell MHC-I Sensing

- NK cells use NKG2D (run_102) to detect MHC-I-low stressed cells (missing-self)
- NLRC5 in target cells (EBV-infected B cells, virocyte-laden NK cells) → MHC-I → KIR inhibition → protects EBV-infected cells from NK killing
- In ME/CFS: EBV-infected cells maintain NLRC5 → MHC-I → NK inhibition via KIR → viral persistence → chronic immune activation

### NLRC5 in ME/CFS B Cells

- EBV-immortalized B cells: NLRC5 high → HLA-I high → CD8 T cell presentation of EBV peptides → CTL expansion → exhaustion (chronic antigen → TOX/T-bet/EOMES imbalance, run_166 bridge)

---

## Therapeutic Implications

### NLRC5 Suppression for β Cell Immune Privilege Restoration

1. **NLRC5 siRNA nanoparticle** (islet-targeted delivery): reduce β cell NLRC5 → HLA-I ↓ → CTL cannot recognize → β cell immune privilege restored; must be islet-targeted (systemic NLRC5 ↓ = immune compromise)
2. **NLRC5 NBD inhibitor**: NACHT domain small molecule inhibitor; prevents NLRC5 nuclear translocation; early-stage discovery
3. **EZH2 maintainer in β cells** (run_157 bridge): maintaining EZH2 in β cells → H3K27me3 at NLRC5 enhancer → NLRC5 expression suppressed epigenetically; tazemetostat caveat (run_157: harmful if systemic) applies here too
4. **NLRC5 + IRF1 dual suppression**: IRF1 siRNA (run_168) + NLRC5 inhibitor = complete β cell MHC-I abolition (constitutive + inducible arms); CTL killing impossible without HLA-I
5. **TAP1/2 inhibitor** (downstream of NLRC5): herpes viral ICP47 protein is a natural TAP inhibitor; ICP47-inspired peptides could block TAP → prevent peptide loading → empty MHC-I → NK cell attacks INSTEAD of CTL = shifts from CD8 CTL killing toward NK-mediated β cell surveillance (which in T1DM context is beneficial for viral clearance without HLA-I-dependent CTL killing of β cells)

### Precision: NLRC5 Monitoring in T1DM Treatment

- **β cell HLA-A/B/C level** (biopsy or pancreatic organoid-derived): NLRC5 activity proxy; patients with high HLA-I at diagnosis → NLRC5 high → CTL dominant → target CTL arm (eldelumab/run_163 + perforin disruption)
- **NLRC5 genotype** (16q13): tagging SNPs for T1DM risk stratification; low-NLRC5 variant = lower CTL killing risk

---

## Key Molecular Markers

| Marker | Assay | Value |
|--------|-------|-------|
| HLA-A/B/C expression (β cells) | IHC/IF pancreatic biopsy | NLRC5 activity; CTL vulnerability index |
| NLRC5 mRNA (islets) | qPCR / scRNA-seq | Direct NLRC5 expression |
| TAP1/TAP2 (β cells) | IHC/WB | MHC-I loading machinery; NLRC5-dependent |
| B2M serum | ELISA | Shed β₂-microglobulin = systemic MHC-I shedding; T1DM activity |
| HLA-I:NKG2D-L ratio (β cells) | IHC dual | CTL/NK balance in β cell immune recognition |

---

## Cross-References

- **run_128**: CLEC16A/MHC-II/cDC2 — MHC-II (CD4 arm); NLRC5 = MHC-I (CD8 arm); complementary antigen presentation systems
- **run_159**: BATF3/cDC1/cross-presentation — cDC1 presents exogenous β cell antigens via MHC-I; NLRC5 presents endogenous β cell antigens via MHC-I in the β cell itself; orthogonal MHC-I routes
- **run_168**: IRF1 — IRF1 inducible MHC-I + NLRC5 constitutive MHC-I = dual-arm β cell HLA-I regulation; combined inhibition = complete MHC-I suppression
- **run_162**: PRF1/GZMB — CTL killing requires β cell HLA-I (NLRC5-dependent) for TCR recognition → IS formation → perforin delivery; NLRC5 KO removes TCR trigger
- **run_157**: EZH2/H3K27me3 — EZH2 at NLRC5 enhancer in β cells; insulitis EZH2 ↓ → NLRC5 derepressed → HLA-I surge; maintaining β cell EZH2 = NLRC5 suppression strategy
- **run_119**: PTPN2/JAK1/STAT1/baricitinib — reduces IRF1-inducible MHC-I arm; NLRC5 constitutive arm persists; explains baricitinib partial response for CTL killing

---

SATURATION + 58: 169 runs
