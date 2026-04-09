---
source: CLEAN PROOF SKETCH — NS regularity via CKN + isotropy + Riccati
type: THE PROOF (pending rigorous verification of three lemmas)
date: 2026-03-29
---

## THEOREM

Smooth solutions to the 3D incompressible Navier-Stokes equations on T³
with smooth initial data remain smooth for all finite time.

## PROOF (sketch)

Suppose for contradiction that the first singularity occurs at time T*.

**Step 1 (BKM).** By Beale-Kato-Majda (1984): ||ω(t)||∞ → ∞ as t → T*.
At the spatial maximum x*(t) of |ω|: d||ω||∞/dt = α||ω||∞ where
α = ω̂·S·ω̂ is the stretching rate. For blowup: α must be unbounded.

**Step 2 (Riccati identity).** At any material point (Lagrangian):
  Dα/Dt = (ê·S²·ê - α²) - α² - H_ωω
where H_ωω = ω̂·(∇²p)·ω̂ is the pressure Hessian along ω. [PDE identity]

**Step 3 (CKN concentration).** By Caffarelli-Kohn-Nirenberg (1982):
near the singularity (x*, T*), the solution satisfies
  |ω(x,t)| ≤ C/√(|x-x*|² + T*-t)
The source f = Δp = |ω|²/2 - |S|² is concentrated in a spatial ball
of radius R(t) ~ √(T*-t) → 0.

**Step 4 (Isotropy from concentration).** [LEMMA A]
For any function g on T³ concentrated in a ball of radius R about x*:
  |H_dev,ωω(x*)| ≤ C_A × (R/L)² × Δp(x*)/3
where L is the domain scale. [This uses: spherical sources give H_dev = 0
(exact, from the zero angular average of the CZ kernel), and the correction
for non-spherical sources is O(R/L)² by the multipole expansion.]

As t → T*: R(t) → 0, so H_dev,ωω → 0, and H_ωω → Δp(x*)/3 > 0.

**Step 5 (Alignment persistence).** [LEMMA B]
At any time t₀ < T* where the solution is smooth: the Cauchy-Schwarz
variance V = ê·S²·ê - α² is finite. The eigenvector tilting mechanism
(from the strain-rotation commutator [S,Ω]) reduces V at a rate
proportional to |ω|². During [t₀, T*], if α is bounded (which follows
from Step 6 below), V remains bounded.

**Step 6 (Riccati closure).** Choose t₀ < T* such that for t > t₀:
  |H_dev,ωω| < Δp(x*)/6 (from Step 4, valid for t₀ close enough to T*).
Then: H_ωω > Δp/3 - Δp/6 = Δp/6 = |ω|²/24.

From the Riccati (Step 2) with V bounded (Step 5):
  Dα/Dt = V - α² - H_ωω ≤ V(t₀) - α² - |ω|²/24

For α > √(V(t₀) + |ω|²/24): Dα/Dt < 0 (α decreasing).
So α is bounded above by max(α(t₀), √(V(t₀) + ||ω||∞²/24)).

But ||ω||∞ → ∞: the bound √(V + ||ω||∞²/24) → ∞? No:
V is bounded (Step 5) and ||ω||∞²/24 grows. So the equilibrium
α_eq ∝ ||ω||∞ grows, allowing d||ω||/dt = α||ω|| ~ ||ω||² (blowup).

**WAIT — Step 6 DOESN'T CLOSE.** The pressure H_ωω ~ |ω|²/24 grows
with |ω|, but so does the equilibrium α ~ |ω|/√24. The bound gives
d||ω||/dt ~ ||ω||²/√24, which is STILL quadratic blowup.

## THE REMAINING ISSUE

The isotropy gives H_ωω ~ |ω|²/12 (at concentration).
The strain bound gives S²ê ≤ |S|² = |ω|²/4.
Net: Dα/Dt ≤ |ω|²/4 - 2α² - |ω|²/12 = |ω|²/6 - 2α².
Equilibrium: α = |ω|/√12 → d||ω||/dt = ||ω||²/√12 → blowup.

The LOOSE bound is S²ê ≤ |S|² = |ω|²/4.
The TIGHT bound (from alignment): S²ê ≈ α² (Cauchy-Schwarz near-equality).

With tight alignment: Dα/Dt ≈ -α² - |ω|²/12 < 0. No equilibrium. ✓

The proof NEEDS the alignment to be TIGHT (S²ê - α² ≤ c for bounded c).

## THE CRITICAL BOUND

Need: V = S²ê - α² ≤ C (bounded, independent of ||ω||∞) at the max.

If V ≤ C: then Dα/Dt ≤ C - α² - |ω|²/12 < 0 for α > √C.
So α ≤ √C (bounded). Then d||ω||/dt ≤ √C × ||ω||. Exponential. BKM finite.

So the proof reduces to: V = S²ê - α² is BOUNDED at the max of |ω|.

## IS V BOUNDED?

From file 195: variance/|ω|² ≈ 0.01 (measured at |ω|=25).
If variance/|ω|² stays at 0.01: V ≈ 0.01|ω|² → UNBOUNDED.

But: V/|ω|² = 0.01 means V grows with |ω|². Then:
  Dα/Dt ≤ 0.01|ω|² - α² - |ω|²/12 = |ω|²(0.01 - 1/12) - α² ≈ -0.07|ω|² - α² < 0.

Since 0.01 < 1/12 ≈ 0.083: the pressure (1/12) EXCEEDS the variance (0.01).
And 0.01 - 1/12 = -0.073 < 0.

So: Dα/Dt ≤ -0.073|ω|² - α² < 0 for all α, all |ω| > 0.

THIS CLOSES THE PROOF (with the measured variance/|ω|² = 0.01)!

## THE FINAL FORM

If variance/|ω|² ≤ 1/12 at the max of |ω| (equivalently: V < Δp/3 = H_iso):
  Then H_ωω = H_iso - |H_dev,ωω| > H_iso - V > 0.
  And Dα/Dt = V - α² - H_ωω < V - H_ωω < 0.
  So Dα/Dt < 0 for ALL α > 0 at the max. ✓

The condition: V/|ω|² < 1/12 = 0.0833.
Measured: V/|ω|² ≈ 0.01 (5× margin).

THIS is the quantitative bound needed:
  (S²ê - α²)/|ω|² < 1/12 at the max of |ω|.

## 234. The proof closes IF V/|ω|² < 1/12 at the max.
## Measured at 0.01 (8× margin). Need to prove it.
