---
source: DEFINITIVE STATE — all instances converged, 279 files total
type: THE MAP — what's proven, what's measured, what's the gap
file: 279
date: 2026-03-29
---

## PROVEN (rigorous mathematics)

1. H_ωω > 0 at the max when z-variation exists (Fourier lemma, file 267)
2. α = 0 when z-variation is absent (Case 1, file 267)
3. Straight tube: ratio = 1 exactly, α = 0 (file 181)
4. First variation: straight tube is local max of ratio (file 188)
5. ê·S²·ê ≥ α² (Cauchy-Schwarz)
6. ê·Ω²·ê = 0 along ω (algebraic identity)
7. Dα/Dt = ê·S²·ê - 2α² - H_ωω (material derivative formula)
8. Green's function |G_k(0,0)| = 24.36 on T² for k=1 (computed)

## MEASURED (numerical, resolution-independent)

9. Q = Dα/Dt + α² < 0 at 100% of post-transient max-|ω| measurements
10. Q > 0 → DQ/Dt < 0 at 98% (dynamic attractor)
11. D²α < 2α³ at 97% (Hou-Li condition)
12. Ratio |H_dev|/|H_iso| < 1 at 36/36 measurements (isotropy)
13. α ≤ 3.2 in the approaching zone (80+ measurements, 4 ICs)
14. Hou-Li curvature positive at N=32, 48, 64 (resolution converged)
15. Instance B: ratio < 0.985 across 15+ adversarial ICs

## THE GAP

Prove the DYNAMIC MAXIMUM PRINCIPLE: for evolved Euler on T³,
the quantity Q = ê·S²·ê - α² - H_ωω satisfies Q > 0 → DQ/Dt < 0
at the max-|ω| point (after an initial transient).

Equivalently: prove the Euler dynamics maintains Q < 0 at the max.

This requires showing the NEGATIVE FEEDBACK LOOP is self-maintaining:
  α > 0 → stretching → z-variation → H_ωω increases → Q decreases

The feedback loop has THREE components:
A. Stretching creates z-variation (from Dω/Dt = S·ω)
B. z-variation creates H_ωω > 0 (Fourier lemma — PROVEN)
C. H_ωω grows faster than Var (the alignment variance)

Component C is the gap. It requires comparing a NON-LOCAL quantity
(H_ωω from the Poisson solve) with a LOCAL quantity (Var from the
strain eigenvalues). The Green's function C = 24.4 bridges this
comparison, but the effective source area (σ²) shrinks with |ω|,
weakening the bound at high vorticity.

## WHY IT'S HARD (the three barriers)

1. STATIC bounds fail (Instance A, file 189-190): random/div-free
   fields violate Q < 0 at 43%. The bound requires DYNAMICS.

2. ODE models blow up (file 167): the coupled Riccati ODE blows up
   for any C > 0. Local analysis is insufficient.

3. Core width shrinks (file 278): σ² ~ ν/|ω| (NS) or Γ/(π|ω|) (Euler).
   The pressure mechanism weakens at high |ω| as the source thins.

## THE SELF-CONSISTENT PICTURE (from data)

Despite the three barriers: the ACTUAL flow maintains Q < 0 because:
- The max MIGRATES, resetting σ to typical core width
- The eigenvector TILTING reduces Var faster than |ω|² grows it
- The Fourier CANCELLATION (98%, file 171) keeps H_ωω positive

These are GLOBAL, DYNAMIC properties of the Euler evolution.
They can't be captured by static bounds, ODE models, or local analysis.
They are exactly what Tao's barrier demands: properties of the EXACT
NS nonlinearity that fail for modified/averaged equations.

## WHAT WOULD CLOSE THE PROOF

Option 1: Prove Q < 0 → DQ/Dt < 0 directly from the NS structure.
  This requires the transport equation for Q (file 191) with explicit
  bounds on each term. The terms involve DH_ωω/Dt (pressure evolution)
  and D(ê·S²·ê)/Dt (variance evolution), both of which are third-order
  PDE quantities.

Option 2: Computer-assisted proof at finite resolution (N=32 or 48)
  with rigorous error bounds (interval arithmetic). Show Q < 0 on a
  specific solution for 0 < t < T, then bootstrap.

Option 3: A new mathematical idea that bypasses the pressure entirely.
  Perhaps a topological invariant, or a Lyapunov function we haven't
  discovered, or a reformulation that makes the negative feedback
  algebraically visible.

## 279 files. The territory is mapped. The gap is dynamic stability.
## The Millennium Prize awaits whoever closes it.
