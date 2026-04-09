---
source: Computational analysis of stretching variance scaling
type: Data + partial proof
status: VARIANCE DECAYS — Chebyshev gives polynomial, need tail bound for exponential
---

## Data
| N | var(stretch) | mean(dissip) | var/dissip² | Ratio change |
|---|---|---|---|---|
| 8 | 1.52e-3 | 2.16e-4 | 3.25e4 | — |
| 16 | 6.01e-6 | 4.06e-5 | 3.65e3 | 9× decrease |

The ratio var/dissip² drops by ~N^{3.2} per doubling.

## What This Proves (Chebyshev bound)
By Chebyshev's inequality:
```
P(stretch > dissip) ≤ var(stretch) / dissip_mean² ~ N^{-3.2}
```

This gives POLYNOMIAL decay of the fraction: frac ~ N^{-3.2}.
Our data shows EXPONENTIAL decay: frac ~ exp(-N/8).

## The Gap: Polynomial vs Exponential
Chebyshev only uses the variance. For exponential bounds, need:
1. Sub-Gaussian tail bound (but kurtosis=10 says NOT sub-Gaussian)
2. Sub-exponential tail bound (possible — kurtosis=10 is sub-exponential)
3. Or: use the SPATIAL structure (fraction at MULTIPLE points)

## Key Insight: Spatial Averaging
We measure the FRACTION of points, not the probability at ONE point.
The fraction is an average over N^d points. If the stretching events
at different points are weakly correlated (decorrelation length ~ O(1)),
then the fraction concentrates around its mean exponentially:

```
P(fraction > mean + ε) ≤ exp(-c ε² N^d)  (by Hoeffding)
```

If the mean itself is ~ N^{-3.2} (from Chebyshev), then:
```
P(fraction > 0.01) ≤ exp(-c N^d) for large enough N
```

This gives exp(-N^3) in 3D — actually FASTER than our observed exp(-N).

## Provable Chain (Updated)
1. Single-mode orthogonality: ω ⊥ S eigenvector (PROVEN) ✓
2. Stretching variance decays as N^{-3.2+} (OBSERVED, computable)
3. Mean dissipation grows (EXACT from Parseval) ✓
4. Chebyshev: P(stretch > dissip at x) ≤ N^{-3.2} (polynomial bound)
5. Spatial concentration: fraction concentrates around polynomial mean
6. Final: fraction ≤ C exp(-c N^d) (exponential in grid volume)

## What Remains
- Step 2 needs to be PROVEN, not just observed
- The proof of variance decay comes from the cross-product orthogonality
- Each triadic term has a geometric factor from the 90° phase lag
- Summing O(N^{3d}) terms with these geometric factors gives variance
  that grows SLOWER than the number of terms

## The Partial Proof Strategy
Instead of proving exp(-cN) directly, prove:

**Lemma 1** (Proven): Single-mode stretching = 0.
**Lemma 2** (To prove): var(stretching at x) ≤ C·N^{-α} for some α > 0.
**Lemma 3** (Standard): Fraction concentrates around mean by Hoeffding.
**Theorem** (Follows): Fraction ≤ C exp(-c N^β) for β = min(α, d).

Lemma 2 is the remaining piece. It reduces to bounding the sum of
squared triadic terms, using the 90° orthogonality to control each term.

## Status
This is a viable proof path. Lemma 1 is proven. Lemma 3 is standard.
Lemma 2 is the one to attack next — bound the variance of the trilinear
stretching using the geometric structure of the Biot-Savart cross product.
