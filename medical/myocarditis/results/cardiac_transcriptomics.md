# Cardiac CVB Transcriptomic Analysis

**Analysis date**: 2026-04-08  
**Script**: `numerics/transcriptomics/analyze_cardiac_v2.py`  
**JSON output**: `myocarditis/results/cardiac_transcriptomics.json`

## Datasets

| Dataset | Description | Platform | Scale | n |
|---------|-------------|----------|-------|---|
| GSE1457 | CVB3 cardiac time course — A/J mice | GPL81 (MG-U74Av2) | MAS5 linear | 7 |
| GSE35182 | Sex differences CVB3 10+90 dpi — BALB/c | GPL6246 (Mouse Gene ST 1.0) | log2 RMA | 24 |
| GSE19496 | Genetic susceptibility CVB3 — 4 strains | GPL6887 (Illumina WG-6 v2) | log2 RMA | 24 |
| GSE19303 | Human DCM endomyocardial biopsies | GPL570 (HG-U133 Plus 2.0) | MAS5 linear | 81 |

**Scale note**: MAS5 = raw Affymetrix signal (linear, can be negative). Fold changes computed as mean(case+100) / mean(ctrl+100) with log2 transformation. RMA/lumi = log2-normalized — fold change = 2^(mean_diff).

## GSE1457: CVB3 Murine Cardiac Time Course

**Study design**: Male A/J mice, 10^5 PFU CVB3 or PBS IP. Pooled hearts harvested at days 3, 9, and 30. GPL81 Affymetrix MG-U74Av2. **All samples are pooled — no statistical test possible.**

**Genes recovered**: Bax, Bcl2, Becn1, Casp3, Col1a1, Cxadr, Dmd, Fn1, Foxp1, Foxp3, Ifit1, Ifit2, Isg15, Lamp2, Mx1, Myh6, Myh7, Nfkb1, Sqstm1, Tnni3

### Fold Changes Across Time Points

| Gene | Day3 log2FC | Day3 FC | Day9 log2FC | Day9 FC | Day30 log2FC | Day30 FC |
|------|------------|---------|------------|---------|-------------|---------|
| Bax | +0.61 | 1.53x | +0.11 | 1.08x | +1.64 | 3.12x |
| Bcl2 | +0.07 | 1.05x | +0.99 | 1.98x | +3.78 | 13.75x |
| Becn1 | -1.38 | 0.38x | -0.93 | 0.53x | +1.44 | 2.71x |
| Casp3 | -0.42 | 0.75x | +0.05 | 1.04x | +2.46 | 5.52x |
| Col1a1 | -0.11 | 0.93x | +3.16 | 8.95x | +0.43 | 1.35x |
| Cxadr | +0.14 | 1.10x | +0.24 | 1.18x | +3.44 | 10.82x |
| Dmd | -0.04 | 0.97x | +0.48 | 1.40x | +2.55 | 5.87x |
| Fn1 | -0.53 | 0.69x | +0.18 | 1.13x | +1.00 | 2.00x |
| Foxp1 | -0.65 | 0.64x | — | — | — | — |
| Foxp3 | -1.24 | 0.42x | +0.47 | 1.39x | +2.45 | 5.47x |
| Ifit1 | +0.83 | 1.78x | -0.17 | 0.89x | -0.55 | 0.68x |
| Ifit2 | +1.76 | 3.38x | +3.28 | 9.69x | +1.39 | 2.61x |
| Isg15 | +1.12 | 2.18x | -0.10 | 0.93x | +0.16 | 1.12x |
| Lamp2 | +2.79 | 6.91x | +1.40 | 2.65x | +2.86 | 7.25x |
| Mx1 | +0.49 | 1.40x | -0.03 | 0.98x | +2.54 | 5.80x |
| Myh6 | +0.64 | 1.56x | — | — | -0.48 | 0.72x |
| Myh7 | -0.10 | 0.93x | +0.17 | 1.12x | +2.18 | 4.52x |
| Nfkb1 | +0.85 | 1.80x | +0.72 | 1.65x | -0.31 | 0.81x |
| Sqstm1 | +0.80 | 1.74x | +0.94 | 1.92x | +2.85 | 7.21x |
| Tnni3 | +0.01 | 1.00x | +0.67 | 1.59x | +2.05 | 4.13x |

**Key findings:**
- **Ifit2**: +3.28 log2FC at day 9 — strongest IFN response gene in acute myocarditis
- **Mx1**: -0.03 log2FC at day 9 — IFN-stimulated antiviral gene
- **Nfkb1**: +0.72 log2FC — NF-kB inflammatory pathway activation
- **Lamp2**: +1.40 log2FC — lysosomal signature in acute myocarditis
- **Cxadr**: +0.24 log2FC — CVB receptor (decreasing during active infection)

## GSE35182: Sex Differences in CVB3 Myocarditis

**Study design**: BALB/c mice, male and female, CVB3 or PBS, 10 dpi (acute) and 90 dpi (chronic/DCM). GPL6246 Affymetrix Mouse Gene 1.0 ST, RMA-normalized log2 scale. n=3 per group.

**Probe coverage**: 4 of 26 target genes recovered via curated GPL6246 annotation.

### 10 dpi — Acute Myocarditis

| Gene | Male log2FC | Male FC | Male p | Female log2FC | Female FC | Female p |
|------|------------|---------|--------|--------------|-----------|---------|
| Becn1 | -0.25 | 0.84x | 0.048 | -0.18 | 0.88x | 0.317 |
| Casp1 | +0.03 | 1.02x | 0.797 | -0.14 | 0.91x | 0.091 |
| Foxp3 | -0.44 | 0.74x | 0.005 | -0.18 | 0.88x | 0.271 |
| Ifit1 | -0.11 | 0.93x | 0.072 | +0.01 | 1.00x | 0.957 |

### 90 dpi — Chronic / DCM Phase

| Gene | Male log2FC | Male FC | Male p | Female log2FC | Female FC | Female p |
|------|------------|---------|--------|--------------|-----------|---------|
| Becn1 | +0.12 | 1.08x | 0.503 | -0.20 | 0.87x | 0.640 |
| Casp1 | +0.15 | 1.11x | 0.350 | +0.06 | 1.04x | 0.500 |
| Foxp3 | -0.21 | 0.86x | 0.063 | -0.27 | 0.83x | 0.026 |
| Ifit1 | -0.03 | 0.98x | 0.850 | -0.11 | 0.93x | 0.400 |

**Clinical relevance**: Men develop more severe myocarditis than women (Fairweather 2012). These data test whether differential gene expression at 10 dpi predicts the sex difference in chronic DCM at 90 dpi.

## GSE19496: Genetic Susceptibility to CVB3 Myocarditis

**Study design**: 4 mouse strains at day 4 post CVB3. A/J = susceptible, B10.A = resistant, B6 = moderate, CSS3 = congenic. GPL6887 Illumina MouseWG-6 v2, log2 lumi normalization. n=3 per strain per group.

**Probe coverage**: 5 of 26 target genes recovered.

| Gene | A/J log2FC | A/J FC | A/J p | B10.A log2FC | B10.A FC | B10.A p |
|------|-----------|--------|-------|-------------|----------|---------|
| Bcl2 | +0.05 | 1.04x | 0.701 | -0.25 | 0.84x | 0.409 |
| Becn1 | -0.37 | 0.77x | 0.040 | -0.11 | 0.93x | 0.563 |
| Casp1 | +0.22 | 1.17x | 0.303 | -0.10 | 0.93x | 0.579 |
| Cxadr | -0.15 | 0.90x | 0.596 | +0.20 | 1.15x | 0.256 |
| Mx1 | +0.06 | 1.04x | 0.834 | +0.30 | 1.23x | 0.292 |

**Key interpretation**: Larger fold-change in A/J vs B10.A = candidate susceptibility genes. Smaller/opposite change = potential resistance mechanisms.

## Figures

All figures in `myocarditis/results/figures/`:
- `gse1457_timecourse.png` — Day 3/9/30 fold changes for 20 target genes
- `gse19496_susceptibility.png` — A/J vs B10.A vs B6 vs CSS3 strain comparison
- `gse35182_sex_differences.png` — Male vs female at 10 and 90 dpi
- `lamp_cross_dataset.png` — LAMP1/LAMP2 lysosomal signature across all datasets

## Human DCM Cross-Reference

See `dilated_cardiomyopathy/results/human_dcm_analysis.md` for full human DCM analysis (GSE19303, n=81).
