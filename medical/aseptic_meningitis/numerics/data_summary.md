# Aseptic Meningitis — Published Statistics Summary

**Disease:** Aseptic Meningitis (Enteroviral/CVB)
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `/home/jb/medical_problems/results/epidemiology_all_diseases.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| Incidence/100k/yr (all aseptic meningitis) | 2.0 (range 1.0-3.0) | Khetsuriani 2006 (CDC), Jmor 2008 |
| Global annual cases (all aseptic meningitis) | 1,584,000 | CDC surveillance |
| Enterovirus fraction of all viral meningitis | 85% | GBD 2019 |
| CVB fraction of enteroviral meningitis | ~35% | epidemiology_all_diseases.json |
| CVB-attributable annual cases | 470,000 | cross_disease_burden_results.json |
| Annual deaths | 2,350 | cross_disease_burden_results.json |
| Total DALYs | 109,745 | cross_disease_burden_results.json |
| Disability weight | 0.134 | GBD 2019 |
| Economic burden/yr | $3.055 billion | cross_disease_burden_results.json |

## Serotype Data

| Serotype | Meningitis Tropism | Notes |
|----------|-------------------|-------|
| CVB2 | 0.70 (PRIMARY) | Most common CVB in meningitis |
| CVB5 | 0.60 | Second most common |
| CVB4 | 0.25 | Occasional |
| CVB3 | 0.30 | Occasional |
| CVB1 | 0.20 | Rare |

Note: Echovirus 30 (a different enterovirus) causes additional meningitis cases — see GSE146890.

## Persistence Modeling

| Parameter | Value | Source |
|-----------|-------|--------|
| Critical viral load for CNS persistence (meninges) | 324 infected cells | pattern_010 |
| Meningeal persistence probability | 39.2% | acute_chronic_transition_results.json |
| Immune access score (meninges) | 0.65 | pattern_010 |
| CAR density (meningeal cells) | 0.55 | pattern_010 |

The relatively high persistence threshold (324 cells) and good immune access explain why most aseptic meningitis resolves without chronic sequelae. But the ~39% that establish persistence can progress to encephalitis or chronic neurological symptoms.

## Clinical Data

| Feature | Data |
|---------|------|
| Time to resolution (typical) | 7-14 days | 
| CSF findings | Lymphocytic pleocytosis (50-500 cells/mm3), normal glucose, mildly elevated protein |
| CSF enteroviral PCR sensitivity | ~75% in acute phase | 
| Blood transcriptomic diagnosis (vs LP) | Validated in GSE133378 (n=476) |
| Hospitalization rate | ~30% |
| ICU admission rate | ~5% |
| Long-term neurological sequelae | ~5-10% |
| Neonatal mortality | Up to 10-15% |

## Key GEO Datasets

| Accession | Samples | Relevance | Status |
|-----------|---------|-----------|--------|
| GSE133378 | 476 | VERY HIGH — blood transcriptomics replaces lumbar puncture | [IDENTIFIED, priority download] |
| GSE269413 | 12 | HIGH — CVB3 BBB penetration mechanism | [IDENTIFIED] |
| GSE146890 | 15 | HIGH — blood-CSF barrier, Echovirus 30 | [IDENTIFIED] |
| GSE15323 | 9 | MODERATE — EV71 related enterovirus | [IDENTIFIED] |

GSE133378 is the largest human enteroviral dataset in GEO and directly addresses the clinical question of whether blood transcriptomics can replace the painful and risky lumbar puncture for diagnosis.

## Treatment Data

| Treatment | Evidence |
|-----------|---------|
| Supportive care (analgesia, hydration) | Standard |
| IVIG | Effective in immunocompromised, neonates; limited RCT data for immunocompetent |
| Antiviral | No approved drug for enteroviruses. Pleconaril showed activity (Phase 2) but development halted. |
| Fluoxetine | Theoretical — IC50 demonstrated for CVB, no meningitis-specific data |
