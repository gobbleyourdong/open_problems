# 2D Uniformization Certificate — Hamilton 1988

## Date: 2026-04-09
## Script: numerics/surface_uniformization.py

## CERTIFICATE

5 tests verifying the 2D analog of Poincaré (Hamilton 1988):

| Test | What | Result |
|------|------|--------|
| 1 | S² spectrum λ_k = k(k+1) | exact (7 modes) |
| 2 | Mode decay a_k(t) = a_k(0)·e^(-λ_k t) | 8 timepoints |
| 3 | L² convergence to round | 0.700 → 2.7e-5 over t∈[0,5] |
| 4 | 2D vs 3D comparison | documented |
| 5 | Cigar soliton (2D Type II) | K(0)=4, K(r)→1/r⁴ |

## Key Numbers

- λ_1 = 2 on unit S² (lowest non-trivial eigenvalue, multiplicity 3)
- Half-life of perturbations: log(2)/2 ≈ 0.347
- Cigar soliton K(0) = 4, K(r) ~ 4/r⁴ at infinity
- Convergence rate: pure exponential exp(-2t)

## Why It Matters

2D uniformization is the SIMPLEST version of Poincaré. Hamilton proved
it in 1988 using the same Ricci flow techniques he applied to 3D
positive Ricci in 1982. Perelman 2003 generalized to all of 3D.

The cigar soliton is the simplest example of a Type II singularity.
It exists in 2D (this script) but is FORBIDDEN in 3D by the
Hamilton-Ivey pinching estimate (verified in hamilton_ivey.py).
This explains why Perelman's surgery procedure works in 3D but the
4D smooth Poincaré conjecture remains open.

## Reproducibility

Dependencies: numpy. Runtime: < 1 second.
