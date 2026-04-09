# Dilated Cardiomyopathy (CVB-induced) — Published Statistics Summary

**Disease:** Dilated Cardiomyopathy (DCM, CVB-induced chronic sequela)
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `/home/jb/medical_problems/results/cross_disease_burden_results.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| CVB-attributable new cases/yr | 174,000 | cross_disease_burden_results.json |
| CVB-attributable prevalent cases | 870,000 | cross_disease_burden_results.json |
| Annual CVB-attributable deaths | 87,000 | cross_disease_burden_results.json |
| Total DALYs | 4,487,808 | cross_disease_burden_results.json |
| YLL | 1,131,000 | cross_disease_burden_results.json |
| YLD | 3,356,808 | cross_disease_burden_results.json |
| Disability weight | 0.212 | GBD 2019 |
| Annual economic burden | $261 billion | cross_disease_burden_results.json |
| CVB-attributable fraction of all acquired DCM | 30% | Literature |
| Average age at death | 62 years | cross_disease_burden_results.json |
| Myocarditis-to-DCM transition probability | 30% | GBD 2019 |

## The DCM Rate Problem

DCM is mechanistically a **rate** problem, not an acute disease:

- TD mutants replicate 100,000x slower than wild-type CVB
- 2A protease production is LOW but CONTINUOUS
- Each contraction cycle tears sarcolemma where dystrophin is cleaved
- Fibrosis accumulates over years → chamber dilation → systolic failure
- Heart has near-zero regenerative capacity (cardiomyocyte turnover ~1%/year)

The protocol stops the rate (reduces TD mutant-driven 2A production) but cannot reverse existing fibrosis.

## Dystrophin Cleavage Mechanics

| Component | Normal | After CVB 2A Cleavage |
|-----------|--------|----------------------|
| Dystrophin status | Intact (427 kDa) | Cleaved at hinge 3 |
| DGC assembly | Complete | Disrupted |
| Sarcolemma integrity | Maintained | Tears at Z-discs during contraction |
| Cardiomyocyte fate | Survives | Progressive apoptosis |
| Downstream | Normal pump function | Fibrosis → DCM |

## Treatment Data

| Treatment | Effect | Evidence Level |
|-----------|--------|----------------|
| ACE inhibitors/ARBs | Reduce afterload, slow progression | RCT data (heart failure trials) |
| Beta-blockers | Reduce remodeling, improve survival | RCT data (MERIT-HF, COPERNICUS) |
| ICD/CRT devices | Prevent sudden death, resynchronize | RCT data |
| Heart transplant | Definitive (for end-stage) | Registry data |
| Fluoxetine + FMD | Stop TD mutant-driven 2A production | Model only; no human trial |
| Anti-fibrotics (pirfenidone) | Theoretical adjunct | No CVB-DCM data |

## HLA Risk

| HLA Genotype | DCM Odds Ratio | Notes |
|-------------|----------------|-------|
| DQ5 | ~2.8 | Cardiac autoimmunity predisposition |
| DR4 | ~0.5 | Protective |

The HLA paradox is identical to myocarditis (same mechanism).

## GEO Datasets

Overlap with myocarditis datasets:
- GSE35182 — includes 90 dpi chronic/DCM timepoint (n=12 chronic samples)
- GDS4436 — chronic CVB3-induced myocarditis/DCM (heart)
- No human DCM/CVB transcriptomic datasets

**Research gap:** No human DCM tissue transcriptomics with CVB status known.
