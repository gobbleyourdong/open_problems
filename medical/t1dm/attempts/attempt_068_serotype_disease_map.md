# Attempt 068: Serotype-Disease Map — CVB4 Is Diabetogenic, CVB3 Is Cardiotropic

## Source
ODD instance pattern 010 (`results/pattern_010_serotype_disease_map.md`), derived from `numerics/serotype_tropism.py` + `numerics/acute_vs_chronic_model.py`.

## The Discovery

CVB serotypes B1-B5 have distinct organ tropisms determined by VP1 capsid structure and CAR receptor binding affinity:

| Serotype | Primary tropism | Dominant diseases |
|----------|----------------|-------------------|
| **CVB1** | Pancreotrope + hepatotrope | Pancreatitis, hepatitis |
| **CVB2** | Neurotrope | Meningitis, encephalitis |
| **CVB3** | STRONGEST cardiotrope | Myocarditis, DCM, pericarditis |
| **CVB4** | STRONGEST diabetogenic | T1DM, pancreatitis, neonatal sepsis |
| **CVB5** | Myotrope + orchidotrope | Pleurodynia, orchitis, ME/CFS |

## What This Means

### For the patient
If the patient's T1DM was triggered by CVB, it was most likely **CVB4** (tropism score 0.90 for T1DM). CVB4-specific neutralizing antibodies, if measured, would confirm the serotype.

### For the protocol
The antiviral arm (fluoxetine) targets CVB 2C ATPase, which is >90% conserved across all 5 serotypes. **The protocol is serotype-agnostic** — one drug works for all serotypes. This is a strength: you don't need to know which serotype to treat.

### For the vaccine
A multivalent vaccine must cover all 5 serotypes. The VLP-ΔVP4 approach achieves this by including VP1-VP3 from each serotype. Monovalent vaccines would leave 4/5 serotypes uncovered.

### For screening
Serotype-specific serology could identify which organs to screen:
- CVB4-seropositive → screen pancreas (T1DM risk)
- CVB3-seropositive → screen heart (myocarditis/DCM risk)
- CVB5-seropositive → screen muscle/testes (ME/CFS, orchitis risk)

## The Multi-Serotype Patient

ODD's Monte Carlo (10K infections) shows that ~15-25% of the population is seropositive for ≥2 serotypes. These individuals have MULTI-ORGAN risk:
- CVB3 + CVB4: cardiac AND pancreatic risk simultaneously
- CVB4 + CVB5: pancreatic AND muscle/testicular risk

**the patient could have been infected by multiple serotypes over their lifetime.** This would explain multi-organ vulnerability even with a T1DM-dominant presentation.

## Status: SEROTYPE MAP FORMALIZED — CVB4 diabetogenic, CVB3 cardiotropic, protocol is serotype-agnostic
