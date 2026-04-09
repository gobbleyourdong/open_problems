# Viral Myocarditis — Published Statistics Summary

**Disease:** Viral Myocarditis (CVB-induced)
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `~/open_problems/medical/results/cross_disease_burden_results.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| CVB-attributable new cases/yr | 900,000 | GBD 2019 |
| CVB-attributable prevalent cases | 1,050,000 | cross_disease_burden_results.json |
| Annual CVB-attributable deaths | 175,000 | cross_disease_burden_results.json |
| Total DALYs | 6,544,125 | cross_disease_burden_results.json |
| YLL | 5,250,000 | cross_disease_burden_results.json |
| YLD | 1,294,125 | cross_disease_burden_results.json |
| Disability weight | 0.145 | GBD 2019 |
| Annual economic burden | $45 billion | cross_disease_burden_results.json |
| CVB-attributable fraction of all myocarditis | 50% | GBD 2019 |
| Progression to DCM (without treatment) | 30% | GBD 2019 |
| Average age at death (CVB myocarditis) | 45 years | cross_disease_burden_results.json |

## Serotype Data

| Serotype | Cardiomyocyte Tropism | Notes |
|----------|----------------------|-------|
| CVB3 | 0.90 (PRIMARY) | #1 cardiotrope; 2A protease most active on cardiac dystrophin |
| CVB2 | 0.55 | Secondary cardiotrope; also meningitis |
| CVB4 | 0.20 | Pancreatic primary, occasional cardiac |
| CVB5 | 0.25 | Pleurodynia/muscle primary |
| CVB1 | 0.15 | Pancreatic primary |

## Persistence Modeling

| Parameter | Value | Source |
|-----------|-------|--------|
| Critical viral load for persistence (cardiomyocytes) | 83 infected cells | pattern_010 |
| Persistence probability per CVB3 infection | 54.1% | acute_chronic_transition_results.json |
| CAR receptor density score | 0.85 | pattern_010 |
| TD autoimmune risk score (cardiac myosin mimicry) | 0.65 | pattern_010 |
| Protocol cardiac clearance time | 4.5 months | unified_cvb_clearance_v3.py |
| LVEF recovery (pre-fibrotic, with protocol) | +10-23% | Model projection |
| LVEF recovery (post-fibrotic, with protocol) | ~0% (progression stopped) | Model projection |

## HLA Data

| HLA Genotype | Myocarditis OR | Notes |
|-------------|----------------|-------|
| DQ5 | ~2.5 | Cardiac antigen presentation |
| DR4 | ~0.5 | PROTECTIVE (HLA paradox — same allele that risks T1DM protects heart) |
| DR3-DQ2/DR4-DQ8 | ~0.5 | Protective |

Source: `pattern_009_genetic_risk_landscape.md`

## Disease Network Position

- **Keystone disease** — removing myocarditis from network disrupts 57.4% of all CVB disease cascade paths
- In-degree: 4 (receives from CVB infection, pericarditis, orchitis, neonatal sepsis)
- Out-degree: 3 (seeds DCM, pericarditis, orchitis)
- 30% of myocarditis progresses to DCM

Source: `pattern_008_disease_network.md`

## 2A Protease Cleavage Mechanism

- CVB 2A protease cleaves dystrophin at hinge 3 (aa 1699-1758 region)
- Disrupts dystrophin-glycoprotein complex (DGC) assembly
- Sarcolemma loses structural support → tears during each contraction cycle
- TD mutants produce 2A at low continuous rate → slow progressive damage

## Biomarker Data

| Biomarker | Sensitivity | Specificity | Notes |
|-----------|-------------|-------------|-------|
| Troponin I elevation | ~75% | ~85% | Acute phase; peaks days 3-5 |
| BNP/NT-proBNP | ~80% | Moderate | Severity marker |
| Cardiac MRI (LGE pattern) | ~85% | ~90% | Reference standard; shows viral myocarditis vs ischemic |
| LVEF <40% | ~50% | ~95% | Poor sensitivity (many have normal EF acutely) |

## Kühl Precedent

Kühl et al. 2003 (Circulation): IFN-beta treatment in patients with persistent enteroviral or adenoviral genomes in myocardium → viral clearance and LVEF improvement. This is the proof-of-concept for antiviral treatment of persistent cardiac CVB. Fluoxetine as oral antiviral is the protocol's analog.

## GEO Datasets

**Human:** GSE57781 (iPSC cardiomyocytes, n=4) — ONLY human CVB myocarditis transcriptomic dataset
**Mouse:** GSE261940, GSE248521, GSE174458, GSE35182, GDS4436, GDS4311, GSE19496, GSE26630, GSE1457, GDS1032
**None downloaded** — priority: GSE174458 (scRNA-seq cellular landscape), GSE57781 (human)
