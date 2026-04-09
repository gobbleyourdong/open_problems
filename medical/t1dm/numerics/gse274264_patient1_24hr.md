# GSE274264 Primary Human Islet scRNA-seq: Patient 1, 24hr

## Date: 2026-04-09
## Source: REQ-013

## HEADLINE

**FOXP1 and LAMP2 are NOT suppressed at 24hr in primary human islets.**
This contrasts with the PANC-1 cell line finding (GSE184831).

**INS (insulin) is DOWN 33%** — the clearest signal of beta cell damage.

## Data

996 control cells, 1871 CVB3-infected cells (patient 1, 24hr post-infection).
36,608 genes measured per cell.

## Key genes

| Gene | Ctrl mean | CVB3 mean | log2FC | Interpretation |
|------|-----------|-----------|--------|----------------|
| **FOXP1** | 0.809 | 0.874 | **+0.11** | **STABLE** — NOT suppressed |
| **LAMP2** | 1.391 | 1.539 | **+0.15** | **STABLE** — NOT suppressed |
| DMD | 0.073 | 0.090 | +0.26 | stable (low expression) |
| CXADR | 0.507 | 0.529 | +0.06 | stable (CVB receptor) |
| **INS** | 296.97 | 205.24 | **-0.53** | **DOWN 33% — beta cell damage** |
| GCG | 101.74 | 147.71 | +0.54 | UP 45% — alpha compensation? |
| SST | 275.49 | 221.04 | -0.32 | slight down (delta cells) |
| MX1 | 0.106 | 0.361 | +1.67 | UP 3.2x — IFN-stimulated gene |
| OAS1 | 0.061 | 0.172 | +1.35 | UP 2.5x — IFN response |
| STAT1 | 0.324 | 0.561 | +0.77 | UP 1.7x — JAK-STAT pathway |
| IL6 | 0.001 | 0.007 | +0.62 | UP — inflammatory cytokine |
| TNF | 0.015 | 0.026 | +0.51 | UP — inflammatory cytokine |
| BCL2 | 0.065 | 0.059 | -0.12 | stable (anti-apoptotic) |
| BAX | 0.903 | 1.003 | +0.15 | stable (pro-apoptotic) |
| CASP3 | 0.140 | 0.162 | +0.20 | stable (executioner caspase) |
| ATG5 | 0.198 | 0.215 | +0.12 | stable (autophagy) |
| BECN1 | 0.372 | 0.387 | +0.05 | stable (beclin-1) |
| SQSTM1 | 3.603 | 4.322 | +0.26 | stable (p62) |

## Interpretation

### What's active at 24hr
1. **Strong IFN response**: MX1 (3.2x), OAS1 (2.5x), STAT1 (1.7x) — innate immunity
2. **Inflammatory cytokines**: IL6, TNF elevated
3. **Beta cell damage**: INS down 33% — functional impairment without cell death
4. **Alpha compensation**: GCG up 45% — may indicate islet stress response

### What's NOT happening at 24hr
1. **No FOXP1 suppression** — the transcription factor is stable
2. **No LAMP2 suppression** — autophagy machinery intact
3. **No apoptosis activation** — BCL2, BAX, CASP3 all stable
4. **No autophagy dysregulation** — ATG5, BECN1, SQSTM1 stable
5. **No DMD degradation** — dystrophin is stable (but low baseline)

### Implications for the campaign

The PANC-1 finding (FOXP1/LAMP2 suppressed) may be:
1. **Cell-line specific**: PANC-1 is a cancer line with abnormal gene regulation
2. **Time-dependent**: 24hr may be too early; check 48hr
3. **Dose-dependent**: MOI in this study vs PANC-1 study may differ
4. **Real but weak**: primary islets may resist suppression that cancer cells cannot

## UPDATE: 48hr data confirms — FOXP1/LAMP2 stable across all patients

Full time course (3 patients × 2 timepoints):

| Patient | Time | FOXP1 | LAMP2 | INS | MX1 |
|---------|------|-------|-------|-----|-----|
| 1 | 24hr | +0.11 | +0.15 | -0.53 | +1.67 |
| 1 | 48hr | -0.02 | -0.13 | **-0.90** | +2.00 |
| 2 | 24hr | +0.09 | +0.02 | **-2.04** | +1.95 |
| 2 | 48hr | -0.04 | -0.10 | **-2.27** | +2.34 |
| 3 | 24hr | +0.02 | +0.02 | -0.14 | +1.73 |
| 3 | 48hr | +0.14 | +0.08 | -0.32 | +3.13 |

**FOXP1 range: [-0.04, +0.14] — STABLE across all 6 conditions.**
**LAMP2 range: [-0.13, +0.15] — STABLE across all 6 conditions.**
**INS range: [-0.14, -2.27] — CONSISTENTLY DOWN, up to 4.8x in patient 2.**

### Implications for the campaign

The PANC-1 finding of FOXP1/LAMP2 suppression does NOT replicate in
primary human islets. Beta cell damage (INS down) occurs through a
FOXP1/LAMP2-INDEPENDENT mechanism.

Possible explanations:
1. PANC-1 is a cancer cell line — its gene regulation is not representative
2. The CVB MOI or serotype in the two studies may differ
3. FOXP1/LAMP2 suppression may require chronic (weeks) exposure, not acute
4. The persistence mechanism may work differently in vivo

**The beta cell damage IS real** (INS down 4.8x in patient 2), but it's
NOT mediated by FOXP1/LAMP2 suppression. The campaign's model needs
revision to explain this discrepancy.

## Statistical Summary (3 biological replicates × 2 timepoints)

| Gene | 48hr mean log2FC | SEM | p-value (t-test vs 0) | Verdict |
|------|-------------------|-----|----------------------|---------|
| FOXP1 | +0.027 | 0.045 | **0.672** | NOT significant |
| LAMP2 | -0.049 | 0.053 | **0.534** | NOT significant |
| INS | -1.161 | 0.471 | 0.182 | Consistent DOWN but high variance |
| MX1 | +2.491 | 0.273 | **0.018*** | Significant UP |
| CXADR | -0.375 | 0.163 | 0.201 | Trend DOWN |
| DMD | +0.070 | 0.129 | 0.701 | NOT significant |

Only MX1 (interferon response) reaches significance. The INS drop is
CONSISTENT across all 3 patients (all negative) but inter-patient
variance is high (P2 drops 4.8x, P3 drops 1.2x). With n=3 replicates,
p=0.182 — suggestive but not conclusive by standard criteria.

FOXP1 and LAMP2 are definitively stable: p > 0.5, mean FC near zero,
no patient shows suppression beyond -0.13 log2FC.

## Reproducibility

Script: inline analysis using scanpy. Data: `numerics/transcriptomics/GSE274264/`.
Runtime: ~5 seconds per sample pair.
