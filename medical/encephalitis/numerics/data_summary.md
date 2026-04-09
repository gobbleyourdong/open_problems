# Viral Encephalitis (CVB) — Published Statistics Summary

**Disease:** Enteroviral / CVB Encephalitis
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `~/open_problems/medical/results/epidemiology_all_diseases.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| Enteroviral encephalitis incidence/100k/yr | 0.75 | Hosoya 2007 |
| CVB-specific encephalitis incidence/100k/yr | 0.15 | Hosoya 2007, GBD 2019 |
| Global annual enteroviral encephalitis cases | ~593,000 | GBD 2019 |
| CVB-attributable fraction | 20% | epidemiology_all_diseases.json |
| CVB-attributable annual cases | 118,600 | cross_disease_burden_results.json |
| Annual CVB-attributable deaths | 8,895 | cross_disease_burden_results.json |
| Case fatality rate | 7.5% | GBD 2019 |
| Total DALYs | 492,842 | cross_disease_burden_results.json |
| Disability weight | 0.223 | GBD 2019 |
| Economic burden/yr | $10.081 billion | cross_disease_burden_results.json |
| Average age at death | 30 years (predominantly young/neonatal) | cross_disease_burden_results.json |
| Neonatal mortality | Up to 30% | Hosoya 2007 |

## Serotype Data

| Serotype | Brain Parenchyma Tropism | Notes |
|----------|--------------------------|-------|
| CVB2 | 0.20 (PRIMARY) | Most neurotropic CVB serotype |
| CVB5 | 0.15 | Secondary |
| CVB3 | 0.10 | Occasional |
| CVB4 | 0.10 | Occasional |
| CVB1 | 0.05 | Rare |

Note: All scores are low compared to cardiac/pancreatic tropism, reflecting the BBB's protective role. But once breached, outcomes are severe due to low immune access in brain parenchyma.

## Persistence Modeling

| Parameter | Value | Source |
|-----------|-------|--------|
| Critical viral load for brain persistence | 378 infected cells (HIGHEST threshold) | pattern_010 |
| Brain parenchyma persistence probability | 36.0% | acute_chronic_transition_results.json |
| Immune access score (brain parenchyma) | 0.25 (LOWEST after testes) | pattern_010 |
| CAR density (neurons) | 0.35 | pattern_010 |

**The paradox:** The brain is hardest to infect (highest threshold) but once infected, has the worst immune access — making clearance very difficult.

## BBB Penetration Mechanism

CVB crosses the blood-brain barrier via:
1. **Trojan horse:** CVB infects circulating monocytes → monocytes migrate across BBB → release virus into parenchyma
2. **Direct endothelial infection:** CVB infects choroid plexus epithelium → transcytosis into CSF → parenchymal spread

GSE269413 (iPSC brain endothelial cells + CVB3) directly models mechanism 2.

## Treatment Data

| Treatment | Evidence |
|-----------|---------|
| Supportive care (ICU) | Standard |
| IVIG | Recommended in neonates/immunocompromised; limited adult RCT data |
| Acyclovir | Given empirically until HSV encephalitis excluded (acyclovir has no CVB activity) |
| Dexamethasone | Reduces edema; uncertain benefit in viral vs bacterial |
| Antiviral (CVB-specific) | None approved |

## GEO Datasets

| Accession | Samples | Organism | Relevance | Status |
|-----------|---------|----------|-----------|--------|
| GSE269413 | 12 | H. sapiens (iPSC) | HIGH — CVB3 BBB mechanism | [IDENTIFIED] |
| GSE146890 | 15 | H. sapiens | HIGH — blood-CSF barrier, Echovirus 30 | [IDENTIFIED] |
| GSE280993 | 8 | M. musculus | MODERATE — innate immunity vs CVB | [IDENTIFIED] |
| GSE273336 | 28 | M. musculus | MODERATE — multi-organ CVB | [IDENTIFIED] |
| GSE123550 | 6 | M. unguiculatus | MODERATE — EV71 brainstem | [DOWNLOADED] |
| GSE121971 | 6 | M. unguiculatus | MODERATE — CA16 brainstem | [DOWNLOADED] |
