# Pattern 007: Li Criterion Extended to n=60 — ALL POSITIVE

**Date**: 2026-04-07
**Track**: numerical

## Results (K=100 zeros, mpmath 40-digit precision)

| n | λ_n | Status |
|---|------|--------|
| 1 | 0.0200 | ✓ (smallest, most fragile) |
| 5 | 0.498 | ✓ |
| 10 | 1.968 | ✓ |
| 20 | 7.525 | ✓ |
| 30 | 15.755 | ✓ |
| 40 | 25.503 | ✓ |
| 50 | 35.762 | ✓ |
| 60 | 45.951 | ✓ |

ALL 60 values positive. Zero failures.

## Growth Rate
λ_n/n ≈ 0.32 log(n) - 0.54 (with K=100 zeros)
RH predicts: λ_n/n ≈ 0.5 log(n) - 1.42 (K→∞)
The slope underestimates because K=100 misses tail zeros.

## Key Observation
λ_1 is the SMALLEST coefficient (0.020). If RH were false, the first
sign change would likely occur at small n. The positivity of λ_1
is the most informative single check.

## Combined RH Certificates (numerical track)
| Criterion | Range | Violations | Status |
|-----------|-------|------------|--------|
| Li λ_n ≥ 0 | n = 1..60 | 0 | ✓ |
| Robin σ(n) < bound | n = 5041..100000 | 0 | ✓ |
| Zeros on Re=1/2 | t ∈ [10, 200] | 0 | ✓ |
