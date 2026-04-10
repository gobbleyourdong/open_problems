# cross_species_SP_findings.md — Cross-Species Specious Present Predictions

**Date:** 2026-04-10
**Script:** numerics/cross_species_SP.py
**Addresses:** Universality theorem (attempt_005) — does the chain predict different SP for different species?

## Key Results

### 1. Q10 is conserved across species (robust prediction)

Since ΔE is conserved across Nav channel families (highly conserved protein):

| Species | T (K) | Q10 | Note |
|---------|-------|-----|------|
| Human | 310 | 1.679 | Baseline |
| Cat | 312 | 1.671 | |
| Elephant | 309 | 1.684 | |
| Hummingbird | 313 | 1.663 | |
| Fruit fly | 298 | 1.751 | Higher because colder |
| Iguana | 308 | 1.690 | |

Q10 ranges from 1.66 to 1.75 across the physiological range. The variation comes from Q10's mild temperature dependence (Q10 itself decreases with T). **This is the chain's most robust cross-species prediction** — it depends only on ΔE, not on compression ratio.

### 2. Threshold predictions (sensitive to compression ratio — Weakness 1)

| Species | N (ecological) | n_qubits | Phenomenal time? | Compression scale |
|---------|---------------|----------|-----------------|-------------------|
| Elephant | 464 | 8.9 | YES (richer than human) | 0.5× |
| Human | 141 | 7.1 | YES (baseline) | 1× |
| Cat | 88 | 6.5 | YES (moderate) | 1.5× |
| Iguana | 40 | 5.3 | MARGINAL | 5× |
| Hummingbird | 20 | 4.3 | MARGINAL | 3× |
| Mouse | 3.4 | 1.8 | NO | 10× |
| Fruit fly | 0.1 | — | NO | 100× |

**CRITICAL CAVEAT:** These predictions are dominated by the compression_scale parameter, which is CRUDELY estimated as proportional to brain-size ratio. The mouse prediction (N = 3.4 → no phenomenal time) is almost certainly too extreme — mice demonstrate temporal order discrimination in behavioral tasks, suggesting N >> 3.4.

The compression_scale is Weakness 1 from attempt_005. The cross-species predictions EXPOSE this weakness sharply: the qualitative ordering (elephant > human > cat > iguana > hummingbird > mouse > fly) is probably correct, but the quantitative N values depend on a poorly constrained parameter.

### 3. Bit-optimal constraint (trivially holds in the model)

The model computes t_order = 1/B, so t_order × B = 1 by construction. **This is NOT a test of the constraint.** The real test requires independently measuring t_order and B in non-human species and checking whether their product is 1.

### What is robust vs. fragile

| Prediction | Depends on | Robust? |
|-----------|-----------|---------|
| Q10 ≈ 1.68 across species | ΔE only | **VERY ROBUST** |
| Q10 varies mildly with T (1.66–1.75) | ΔE + T | **ROBUST** |
| SP ordering: elephant > human > cat | Brain size ordering | **LIKELY** |
| Specific N values | Compression ratio | **FRAGILE** |
| Mouse has no phenomenal time | Compression ratio | **PROBABLY WRONG** |
| t_order × B = 1 cross-species | Model assumption | **UNTESTED** |

### Honest assessment

The cross-species script succeeds at generating testable predictions but exposes the compression ratio as the chain's Achilles' heel. The Q10 prediction is the safe bet — it depends on conserved molecular biology. The threshold predictions require independent estimation of each species' effective compression ratio, which is currently beyond reach.

The most productive next step would be: find a species where BOTH t_order and B have been independently measured, and check whether t_order × B ≈ 1. Candidate: the cat (well-studied temporal discrimination in auditory cortex) or the macaque (well-studied visual temporal order).

## Status

Predictions generated. Q10 cross-species is the robust headline result. Threshold predictions are preliminary and dominated by the compression ratio uncertainty.
