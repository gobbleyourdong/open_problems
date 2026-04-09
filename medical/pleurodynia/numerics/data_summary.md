# Pleurodynia (Bornholm Disease) — Published Statistics Summary

**Disease:** Epidemic Pleurodynia / Bornholm Disease / Devil's Grip
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `~/open_problems/medical/results/epidemiology_all_diseases.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| CVB-attributable annual cases | 38,500 | epidemiology_all_diseases.json |
| Annual deaths | 4 (extremely rare) | epidemiology_all_diseases.json |
| Total DALYs | 75 | cross_disease_burden_results.json |
| Disability weight | 0.018 | GBD 2019 |
| Economic burden/yr | $57.75 million | cross_disease_burden_results.json |
| Outbreak periodicity | ~4 years (range 3-5) | Epidemic records 1888-2019 |
| Attack rate during epidemics | 10% (range 5-20%) | epidemiology_all_diseases.json |
| Duration (acute episode) | 2-14 days | Clinical series |
| Recurrence risk | ~30% | Case series |

## T1DM Temporal Association — Critical Epidemiological Data

**Gamble DR (1980) BMJ:** Pleurodynia epidemics in families of T1DM patients. Sibling of a child with pleurodynia had elevated T1DM risk.

**Richardson SJ (2009) Diabetologia:** Pleurodynia precedes T1DM incidence peaks by 1-3 years in population-level data. CVB3/CVB5 (primary pleurodynia serotypes) circulate in the community → CVB4 (T1DM serotype) often co-circulates → the same epidemic seeding event causes pleurodynia in some and T1DM in others, depending on HLA.

This makes pleurodynia epidemics **natural experiments** for CVB community circulation, with T1DM as the lagged outcome.

## Serotype Data

| Serotype | Muscle Tropism | Notes |
|----------|---------------|-------|
| CVB5 | 0.75 (PRIMARY) | Strongest myotropic CVB serotype |
| CVB3 | 0.50 | Secondary |
| CVB1 | 0.30 | Tertiary |
| CVB2 | 0.20 | Occasional |
| CVB4 | 0.15 | Rare |

## Persistence Modeling

| Parameter | Value | Source |
|-----------|-------|--------|
| Critical viral load for skeletal muscle persistence | 105 cells | pattern_010 |
| Skeletal muscle persistence probability | 51.2% | acute_chronic_transition_results.json |
| Satellite cell regenerative capacity | 0.65 | pattern_010 |
| Immune access score (skeletal muscle) | 0.30 | pattern_010 |

Note: skeletal muscle has significant regenerative capacity (satellite cells), which helps clear acute pleurodynia. But TD mutants in muscle can persist and seed systemic ME/CFS in ~20% of cases.

## Disease Network Role

Despite having the **lowest DALY burden** of any CVB disease (75 DALYs), pleurodynia is the **#2 intervention target** by network analysis:
- Treating pleurodynia prevents 20% progression to ME/CFS
- ME/CFS has the highest DALY burden (17.8M) of any CVB disease
- Network intervention value: 0.0525 (second only to treating CVB infection itself)

Source: `pattern_008_disease_network.md`

## Clinical Data

| Feature | Value |
|---------|-------|
| Presenting symptom | Sudden paroxysmal chest/upper abdominal pain, worse with breathing |
| Physical exam | Pleural friction rub occasionally; tenderness of intercostal muscles |
| Distinguish from | Pleuritis, pericarditis, pulmonary embolism, MI — workup usually needed |
| ECG | Normal |
| Chest X-ray | Normal |
| CVB serology | Positive in acute/convalescent pairs — rarely ordered |
| Treatment | NSAIDs, heat, rest |

## GEO Datasets

**None found.** Pleurodynia is clinically self-limiting and has not attracted transcriptomic study. No animal models for CVB pleurodynia in GEO.

The value of pleurodynia data would be in its role as a community indicator of CVB circulation — linking epidemic curve data to subsequent T1DM incidence in the same communities.
