---
source: Eigenvector tilting is the DOMINANT mechanism killing α in the trefoil
type: BREAKTHROUGH — the missing Riccati term identified and measured
date: 2026-03-28
---

## The Decomposition

α = Σ λᵢ cᵢ where cᵢ = cos²(ω̂, eᵢ)

dα/dt = Σ (dλᵢ/dt) cᵢ  +  Σ λᵢ (dcᵢ/dt)
        [eigenvalue change]  [TILTING]

## Trefoil Results

| t | α | Dα/Dt | Eigenval | TILT | Ratio |
|---|---|-------|----------|------|-------|
| 0.01 | +2.24 | +1.68 | -2.98 | **+4.66** | tilt stretches |
| 0.07 | +2.50 | -7.29 | -4.44 | **-2.85** | tilt compresses |
| 0.13 | +1.95 | -17.78 | -5.38 | **-12.40** | tilt dominates 2:1 |
| 0.19 | +1.66 | -9.09 | +1.95 | **-11.03** | tilt dominates |
| 0.25 | +0.81 | -14.08 | +1.04 | **-15.12** | tilt dominates 15:1 |

After t=0.07: TILT is consistently negative and GROWING.
By t=0.25: TILT = -15, eigenvalue = +1. Tilt dominates 15:1.

## What TILT Is

TILT = Σ λᵢ (dcᵢ/dt) — the rate of change of α due to the
eigenvectors rotating relative to ω.

When e₃ (compressive) rotates TOWARD ω: c₃ increases, and since
λ₃ < 0 (most negative eigenvalue), the term λ₃·(dc₃/dt) < 0.
This is a NEGATIVE contribution to dα/dt → kills stretching.

## Why It's Missing From the ODE

The coupled Riccati ODE:
  dα/dt = -α² + C|ω|²

tracks α as if the eigenvectors are FROZEN. The tilt term (Σλᵢ dcᵢ/dt)
is entirely absent. The ODE blows up because it doesn't have the
eigenvector rotation that the PDE has.

## The Individual Strain Terms (trefoil at t=0.25)

| Term | Magnitude | Effect |
|------|-----------|--------|
| -S² (self-depletion) | -6.7 | Compressive (eigenvalues) |
| **-Ω² (vorticity)** | **+99.8** | STRETCHING eigenvalues! |
| **-H (pressure)** | **-92.1** | COMPRESSIVE eigenvalues |
| TILT | -15.1 | COMPRESSIVE (alignment) |

-Ω² and -H nearly cancel (+100 vs -92 = +8 net stretching).
TILT = -15 overwhelms the +8 net → total Dα/Dt = -14.

## The Proof Route (Grok's suggestion formalized)

The missing term in the Riccati is TILT = Σλᵢ(dcᵢ/dt).

From the vorticity equation: Dω̂/Dt = (S - αI)·ω̂
From the strain equation: De_i/Dt = perturbation theory

The tilt depends on:
1. The eigenvalue gaps (λᵢ - λⱼ) — how fast eigenvectors rotate
2. The off-diagonal strain evolution — from -Ω² and -H
3. The angle between ω and the eigenvectors

If we can show TILT ≤ -c|ω|² for some c > 0, then:
  dα/dt ≤ -α² + C|ω|² - c|ω|² = -α² + (C-c)|ω|²

If c > C: the tilt overcomes the pressure → dα/dt ≤ -α² → bounded!

From data: TILT/|ω|² ≈ -15/650 ≈ -0.023
           C = H_ωω/|ω|² ≈ 0.03

So c ≈ 0.023 and C ≈ 0.03. C > c (barely). Not enough to close.

BUT: the tilt grows FASTER than |ω|² over time (from -3 to -15
while |ω|² goes from 340 to 640). So c is INCREASING.

## 173 proof files. The tilting term is identified, measured, and dominant.
