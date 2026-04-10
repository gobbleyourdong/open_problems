# Bishop-Gromov Certificate

## Date: 2026-04-09
## Script: numerics/bishop_gromov.py

## CERTIFICATE

Bishop-Gromov volume comparison verified on three model spaces:

| Space | K | Ratio behavior | Result |
|-------|---|----------------|--------|
| S³(1) | +1 | monotone DECREASING | 0.9999 → 0.4775 |
| H³(1) | -1 | INCREASING (vs Euclidean) | 1.002 → 5.436 |
| Model = M | any | exactly 1.0 (sharp) | 1.000000 |

## Analytical Volume Formulas Verified

  vol_S³(B(p,ρ)) = 2π·ρ - π·sin(2ρ)
  vol_H³(B(p,ρ)) = π·sinh(2ρ) - 2π·ρ
  vol_R³(B(ρ)) = (4/3)π·ρ³

All three closed-form. No numerical integration. Machine precision.

## Key Numbers

  vol(S³(1)) = 2π² = 19.7392 (whole sphere)
  vol_R³(B(1)) = 4π/3 = 4.1888
  Bishop-Gromov constant for κ: depends on Perelman's W-monotonicity
  Sharpness: equality holds at every radius for the model space

## Reproducibility

Dependencies: numpy. Runtime: < 1 second.
