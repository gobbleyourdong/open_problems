# T1DM — Published Statistics Summary

**Disease:** Type 1 Diabetes Mellitus
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `/home/jb/medical_problems/results/cross_disease_burden_results.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| Global T1DM prevalence (all ages) | ~9 million | IDF Diabetes Atlas 2022 |
| Annual new T1DM cases globally | ~540,000 | IDF 2022 |
| CVB-attributable fraction | 35% | Hyoty 2016, Richardson 2009 |
| CVB-attributable new cases/yr | 189,000 | Model (cross_disease_burden) |
| CVB-attributable prevalent cases | 2,940,000 | Model estimate |
| Annual CVB-attributable deaths | 17,500 | cross_disease_burden_results.json |
| Total DALYs (CVB-attributable) | 2,308,152 | cross_disease_burden_results.json |
| YLL (CVB-attributable) | 262,500 | cross_disease_burden_results.json |
| YLD (CVB-attributable) | 2,045,652 | cross_disease_burden_results.json |
| Disability weight | 0.049 | GBD 2019 |
| Annual economic burden (CVB fraction) | $23.5 billion | cross_disease_burden_results.json |
| Incidence/100k/yr (all-cause T1DM) | 15 | GBD 2019, US data |

## HLA Risk Data

| HLA Genotype | T1DM Odds Ratio | Source |
|-------------|-----------------|--------|
| DR3-DQ2 / DR4-DQ8 (compound het) | 15-20 (HIGHEST RISK) | Todd 2010 (Nat Rev Immunol) |
| DR3-DQ2 alone | 5 | Todd 2010 |
| DR4-DQ8 alone | 5-7 | Todd 2010 |
| DR15-DQ6 | 0.03 (strongly protective) | Todd 2010 |
| No risk alleles | ~0.3 | Todd 2010 |

Population at elevated T1DM risk (RR >= 1.5): ~10-15%
Population at high T1DM risk (RR >= 3.0): ~3-5%

Source: `pattern_009_genetic_risk_landscape.md`, `hla_risk_model_results.json`

## CVB Serotype Tropism

| Serotype | Beta Cell Tropism Score | Notes |
|----------|------------------------|-------|
| CVB4 | 0.90 | PRIMARY — first strain to cause diabetes in mice (Loria 1977), found in human islets (Dotta 2007) |
| CVB1 | 0.55 | SECONDARY — found in human islets (Oikarinen 2008) |
| CVB3 | 0.20 | Occasional |
| CVB2 | 0.15 | Rare |
| CVB5 | 0.10 | Rare |

## Persistence Modeling

| Parameter | Value | Source |
|-----------|-------|--------|
| Critical viral load for persistence (beta cells) | 74 infected cells | pattern_010 |
| Persistence probability per CVB4 infection | 54.7% | acute_chronic_transition_results.json |
| Phase diagram: % of parameter space leading to persistence | 54.7% | acute_vs_chronic_model.py |
| CAR receptor density score (beta cells) | 0.90 (highest of any organ) | pattern_010 |
| TD mutant autoimmune risk score | 0.80 (highest) | pattern_010 |

## Protocol Data

| Component | Mechanism | Evidence Level |
|-----------|-----------|----------------|
| Fluoxetine 20mg | Lysosomal disruption → CVB clearance; IC50 1.5-8 μM in vitro | IC50 reconciled (pattern_011) |
| FMD 5-day cycles | AMPK → ULK1 → autophagy → TD mutant clearance | ODE model (8/8 organs cleared) |
| Colchicine 0.5mg | NLRP3 block → IL-1beta → insulitis suppression | COPE trial mechanism |
| IVIG 0.4g/kg | CVB neutralization (acute phase) | Standard neonatal use |

**Protocol clearance time (unified model):**
- Female: ~7 months
- Male: ~9-18 months (testicular reservoir extends clearance)

Source: `unified_cvb_clearance_v3.py`

## Current Clinical Trial Status

| Therapy | Status | Key Data |
|---------|--------|---------|
| Teplizumab (anti-CD3) | FDA approved Stage 2 T1DM (2022) | Delays onset ~2 years, NNT ~2-3 in high-risk |
| Abatacept (CTLA-4-Ig) | Phase 2 complete | C-peptide preserved at 2yr, effect waned |
| GAD-alum vaccine | Phase 3 failed overall | Signal in HLA-DR3-DQ2 subgroup |
| VX-880 (stem cell beta cells) | Phase 1/2 ongoing | C-peptide restoration shown, needs immunosuppression |
| Fluoxetine + FMD (antiviral) | NOT IN TRIAL | No human trial registered |

## Key References

- Hyoty H (2016) Diabetologia — CVB etiology in T1DM
- Dotta F et al. (2007) NEJM — CVB4 in human islets at onset
- Todd JA (2010) Nat Rev Immunol — HLA genetic architecture
- Oikarinen S et al. (2008) Diabetologia — CVB1 in islets
- Gamble DR (1980) BMJ — pleurodynia epidemics and T1DM
- Richardson SJ (2009) Diabetologia — enteroviral protein in islets at onset
