# Viral Orchitis (CVB) — Published Statistics Summary

**Disease:** Viral Orchitis (CVB-attributable)
**Numerics instance:** ODD
**Generated:** 2026-04-08
**Full analysis cross-reference:** `/home/jb/medical_problems/results/cross_disease_burden_results.json`

---

## Epidemiology

| Statistic | Value | Source |
|-----------|-------|--------|
| CVB-attributable annual new cases | 20,000 | cross_disease_burden_results.json |
| CVB-attributable prevalent cases | 60,000 | cross_disease_burden_results.json |
| Annual deaths | 0 (not directly fatal) | cross_disease_burden_results.json |
| Total DALYs | 3,240 | cross_disease_burden_results.json |
| Disability weight | 0.036 | GBD 2019 |
| Economic burden/yr | $720 million | cross_disease_burden_results.json |
| CVB fraction of all viral orchitis | 25% | cross_disease_burden_results.json |

Note: Mumps is the primary cause of viral orchitis. CVB is the second most common.

## The Blood-Testis Barrier — Critical Pharmacokinetic Data

| Parameter | Value | Source |
|-----------|-------|--------|
| Immune access score (testes) | 0.15 (LOWEST of any CVB organ) | pattern_010 |
| Persistence probability per infection | 48.0% | acute_chronic_transition_results.json |
| Critical infection threshold | 134 cells (moderate) | pattern_010 |
| CAR density (testicular tissue) | 0.45 | pattern_010 |

**The BTB paradox:** The testes require a moderate number of infected cells (134) to establish persistence — but once persistence is established, the BTB blocks:
- T cells
- Antibodies (IgG crosses poorly)
- Most hydrophilic antivirals
- The adaptive immune response generally

Result: natural clearance is nearly impossible. The testes become a **permanent CVB reservoir**.

## The Reservoir Theory

Orchitis is the least studied CVB disease but may be disproportionately important as a **reseeding reservoir**:

1. CVB establishes in testicular tissue (TD mutants, BTB-protected)
2. Periodic viremic episodes reseed other organs: heart, CNS, skeletal muscle
3. This explains why some patients have recurring myocarditis episodes without reinfection
4. Clearing testicular CVB breaks the reseeding loop

Disease network analysis: removing orchitis disrupts **51.1%** of all disease cascade paths — second only to myocarditis (57.4%).

## Serotype Data

| Serotype | Testicular Tropism | Notes |
|----------|-------------------|-------|
| CVB5 | 0.60 (PRIMARY) | Myotrope — testicular tissue similar to skeletal muscle |
| CVB4 | 0.15 | Occasional |
| CVB3 | 0.10 | Occasional |
| CVB2 | 0.10 | Occasional |
| CVB1 | 0.05 | Rare |

## Drug Penetration Through the Blood-Testis Barrier

| Drug | BTB Penetration | Notes |
|------|----------------|-------|
| Standard antivirals (pleconaril) | POOR — hydrophilic | BTB blocks most hydrophilic drugs |
| Fluoxetine | POTENTIALLY BETTER — lipophilic, base | Lysosomotropic; basic compounds concentrate in cells |
| Hydroxychloroquine | MODERATE | Also lysosomotropic |
| FMD-induced AMPK | Unknown | AMPK is an intracellular signal — systemic FMD may reach testicular cells |

No human data on fluoxetine testicular concentration exists. This is a critical experimental gap.

## Fertility Impact

| Impact | Data |
|--------|------|
| Testicular atrophy (severe orchitis) | ~30-50% of cases with severe disease |
| Oligospermia | ~30% with bilateral orchitis |
| Azoospermia | ~5-10% with bilateral severe orchitis |
| Infertility (male factor) | CVB orchitis contributes to ~5% of male infertility |

## GEO Datasets

**None found.** No transcriptomic data for CVB orchitis exists in GEO. This is the most understudied CVB disease relative to its potential importance as a viral reservoir.
