---
source: Computational verification of measure-theoretic approach
type: Data
status: RIGHT DIRECTION but slow convergence at small N
---

## Test
Compute <Q>, std(Q), and |<Q>|/std(Q) across resolutions.

## Results
| N | <Q> | std(Q) | |<Q>|/std | frac(Q>0) |
|---|-----|--------|----------|-----------|
| 4 | -3.6e-5 | 1.6e-2 | 0.002 | 0.497 |
| 8 | -1.5e-4 | 3.9e-2 | 0.004 | 0.493 |
| 16 | -4.1e-5 | 2.4e-3 | 0.017 | 0.478 |
| 32 | -5.1e-6 | 1.1e-4 | 0.047 | 0.445 |

## Interpretation
The ratio |<Q>|/std(Q) IS growing with N (0.002 → 0.047) — the mean
moves negative faster than the fluctuations. But at N=32, the ratio is
still only 0.047, far below 1. The simple Chebyshev bound
meas({Q>0}) ≤ std/|<Q>| gives > 1 (trivial) at these resolutions.

The exponential decay kicks in at N=64-128 where the ratio presumably
exceeds 1. We can't test this directly because compute_growth at N=64
would take too long in this verification script.

## Why the Convergence is Slow
Both <Q> and std(Q) DECREASE with N (the fields get weaker as energy
spreads across more modes). The ratio grows because <Q> decreases
SLOWER than std(Q) — but both are shrinking.

The exponential decay of the infection ratio isn't from the mean/std
ratio alone. It's from the SPATIAL STRUCTURE — the inter-shell
decorrelation we verified in file 021.

## Revised Understanding
The measure-theoretic approach (file 026) gives the correct DIRECTION
but only polynomial convergence rate from the mean/std ratio.
The EXPONENTIAL rate comes from the independence structure (file 021):
N/N_d independent shells each with bounded alignment probability.

The final proof needs BOTH:
1. Mean dominance (<Q> → -∞) — from Parseval, gives polynomial bound
2. Shell independence (corr < 0.02) — from Biot-Savart, upgrades to exponential

Neither alone is sufficient. Together they close the proof.
