# F-Functional Certificate — Perelman's First Functional

## Date: 2026-04-09
## Script: numerics/f_functional.py

## CERTIFICATE

Perelman's F-functional verified on round S³:

| Test | What | Result |
|------|------|--------|
| 1 | F = R = 6/r² on round S³ (constant f) | exact at 5 radii |
| 2 | F monotone under (modified) RF | 8/8 timepoints |
| 3 | No steady soliton on closed S³ | ∫R > 0 (3 examples) |
| 4 | Round S³ IS shrinking soliton at τ = r²/4 | 2τ·Ric/g = 1.000000 EXACT |
| 5 | F vs λ vs W comparison | documented |

## Key Numbers

- Soliton parameter for round S³(r): τ = r²/4
- Matches extinction time T from extinction_time.py: T = r₀²/4
- 2τ · Ric/g = 1.000000 exact at r ∈ {0.5, 1.0, 1.5, 2.0}
- F(round S³(1)) = R = 6 (matches λ)

## Three Functionals Coverage

The numerical track has now verified ALL THREE of Perelman's monotone
functionals on the round sphere:

  F (this script): F = R, monotone, soliton equation verified
  λ (lambda_invariant.py): λ = R = 6/r², 33 timepoints
  W (w_entropy_verification.py): 16 timepoints, 4 sub-tests

All three form a hierarchy with critical points being respectively
steady solitons, Einstein metrics, and shrinking solitons.

## Reproducibility

Dependencies: numpy. Runtime: < 1 second.
