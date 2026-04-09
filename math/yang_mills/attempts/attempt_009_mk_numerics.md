# Attempt 009 — MK Decimation Numerics: First Results

**Date**: 2026-04-07
**Phase**: 2 (Numerics)
**Instance**: Odd

## What I Computed

Ran MK decimation for SU(2) and U(1) in d=4 with the simple recursion
c_j → c_j^{2(d-1)} = c_j^6 per step.

## Key Findings

### 1. MK flow is EXTREMELY fast to strong coupling

After ONE step, c_{1/2} drops from 0.48 (at β=2.3) to 0.012.
After TWO steps, all non-trivial coefficients are < 10^{-10}.

This means: the MK approximation flows to INFINITE COUPLING in 2-3 steps
for any starting β. The flow is c_j → c_j^6, so:
  c_{1/2} = 0.48 → 0.48^6 = 0.012 → 0.012^6 ≈ 3×10^{-12}

### 2. Z/Z+ > 1 at every step for SU(2) — but converges to 1

Z/Z+ starts at 1.5-2.5 (depending on β) and drops to ~1.000 after step 1.
It NEVER goes below 1. The inequality Z > Z+ is PRESERVED.

But the convergence to 1 is so fast that the numerics can't distinguish
"Z/Z+ = 1.0000" from "Z/Z+ = 1 + 10^{-15}" after step 2.

### 3. The 1D transfer matrix model is too crude

My Z/Z+ computation uses a 1D effective transfer matrix, which is what
the MK decimation reduces to. But the 1D model loses the information about
the SURFACE Σ where the vortex lives. In 1D, after MK decimation reduces
to a single line, the vortex surface degenerates.

The CORRECT test needs to preserve the d-dimensional structure: compute
Z and Z- on a d-dimensional lattice, perform MK decimation IN ONE DIRECTION,
and check Z/Z+ at each step while maintaining the spatial structure.

### 4. U(1) shows identical behavior (unexpected!)

U(1) shows Z/Z+ > 1 at all steps too. This is WRONG — U(1) in d=4 has a
phase transition and should show Z/Z+ < 1 in the Coulomb phase.

The reason: the MK flow drives U(1) to strong coupling too (c_n → c_n^6 → 0).
In the MK approximation, U(1) ALSO confines at all β! This is a known
failure of MK in d=4: it predicts confinement for U(1), which is wrong.

## What This Means for Tomboulis

The MK approximation is NOT accurate enough to distinguish SU(2) (confining)
from U(1) (deconfining) in d=4. Both flow to strong coupling under MK.

Tomboulis's argument uses BOUNDS on the exact theory from above and below,
not the MK approximation itself. The inequality (5.15) must hold for the
EXACT partition function, not just the MK-approximated one.

## What I Need to Do Instead

1. **Exact Z and Z- on small lattices** (2^4, 3^4) via character expansion
   with full spatial structure (not 1D reduction)
2. **Monte Carlo measurement** of Z/Z- on larger lattices (8^4, 16^4)
   via the ratio trick: Z-/Z = ⟨(-1)^{vortex flux}⟩_Z
3. **Tomboulis's actual bounding scheme** uses UPPER and LOWER bounds
   from the MK recursion, not the MK flow itself. Need to implement
   the bounding, not just the recursion.

## The Corrected Diagnostic

The right question is NOT "does MK preserve Z > Z+?"
The right question is "does the EXACT Z/Z+ stay > 1 for all β?"

For the exact theory:
- β small: Z/Z+ >> 1 (strong coupling, vortex costs a lot)
- β large: Z/Z+ should still be > 1 (confinement) but by a small amount
- The margin Z/Z+ - 1 ~ exp(-σ Area(Σ)) where σ is the string tension
- At weak coupling: σ ~ Λ_QCD^2, Area(Σ) = L^2, so Z/Z+ ~ 1 + exp(-Λ^2 L^2)

The Monte Carlo measurement of σ(β) is the direct test.

## 009. MK decimation runs but is too crude — flows to strong coupling in 2 steps.
## Can't distinguish SU(2) from U(1) (both confine under MK in d=4).
## Need exact Z/Z- on small lattices and MC on larger ones.
## The right test is the string tension σ(β) > 0 for all β.
