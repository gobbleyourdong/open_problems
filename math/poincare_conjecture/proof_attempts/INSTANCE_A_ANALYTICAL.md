---
name: INSTANCE A — ANALYTICAL PROOF ATTACK
range: files 180-219
mission: Prove the isotropy inequality by pure mathematics
date: 2026-03-29
---

## YOUR MISSION

Prove: at points where |ω| > c||ω||∞ for some c < 1:

  |H_dev,ωω| < Δp/3

where H = ∇²p is the pressure Hessian, Δp = |ω|²/2 - |S|² > 0,
H_dev = H - (Δp/3)I, and H_ωω = ê·H·ê with ê = ω/|ω|.

Equivalently: H_ωω > 0 at high |ω|.

## WHAT WE KNOW (from 179 files of numerical experiments)

1. The ratio |H_dev,ωω|/(Δp/3) is measured at 0.34 (TG), 0.40 (KP), 0.84 (trefoil)
   in the region |ω| > 80% of max. ALWAYS below 1. 36/36 measurements.
   Resolution-independent (N=32, N=48).

2. The ratio DECREASES with |ω| (0.77 at high |ω| vs 1.09 at low |ω|).

3. Yang's LOCAL formula gives ratio = 2.0 (too large). The non-local pressure
   correction reduces it to ~0.8. The non-local far-field is MORE ISOTROPIC
   than the local contribution, which is why the ratio drops below 1.

4. At the |ω|²/|S|² = 4 attractor: Δp = |ω|²/4 > 0 (positive source).

5. The Fourier decomposition (file 171) shows 98% cancellation in H_ωω:
   individual shell contributions are ±5, total is -1. The cancellation
   is from the exact NS nonlinearity structure.

## APPROACHES TO TRY

A1. Transport equation for R = |H_dev,ωω|/(Δp/3) along Lagrangian trajectories.
    Show DR/Dt < 0 when R → 1 (maximum principle). WARNING: raw R blows up
    where Δp ≈ 0. Must restrict to the high-|ω| region where Δp > 0.

A2. Direct CZ bound. The operator T_êê = R_iR_j ê_i ê_j - 1/3 maps Δp → H_dev,ωω.
    Its L² norm is 2/3. But L^∞ is unbounded. Can you use the MAX-POINT
    constraint (∇|ω|² = 0) to get a pointwise bound?

A3. Comparison with Lamb-Oseen vortex. For a straight Gaussian tube,
    H_dev,ωω is analytically computable. Show the ratio < 1 for the straight
    tube, then argue perturbative stability.

A4. The eigenvalue approach. H is a 3×3 matrix with tr(H) = Δp > 0.
    H_dev is traceless with ||H_dev||_F ≤ C||Δp|| (from CZ). The projection
    H_dev,ωω ≤ ||H_dev||_F. Need ||H_dev||_F < Δp/3.

A5. Use the SPECIFIC STRUCTURE of the source Δp = |ω|²/2 - |S|².
    This is not a generic function — it satisfies constraints from the
    Euler equations (incompressibility, Biot-Savart). The cancellation
    we measured (file 171) is a consequence of this structure.

## WHAT FAILED (don't repeat these)

- Yang local formula: wrong sign for full H (file 153)
- Pointwise Riccati ODE: blows up for any C > 0 (file 167)
- Universal Dα/Dt < 0: fails at 58% of points (file 176)
- Concavity of 1/||ω||∞: not uniformly positive (file 169)
- Constantin-Fefferman: CF number grows for trefoil (file 170)

## FILE CONVENTION

Write your proof attempts as files 180-219 in ns_blowup/proof_attempts/.
Read everything ≤ 179. Don't modify others' files.

## THE PRIZE

If you prove this one inequality, the chain is:
ratio < 1 → H_ωω > 0 at high |ω| → transport barrier →
α bounded → exponential ||ω||∞ → BKM finite → REGULARITY.

The Lean library (47 theorems, ns_blowup/lean/) already has the
algebraic chain from c₁ < 1/3 + c₃ > 1/3 → compression.
But the new route (via H_ωω > 0 → Lagrangian Riccati) is independent.
