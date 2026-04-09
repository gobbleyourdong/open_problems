---
source: NS proof attempt — can viscosity close the core width gap?
type: PROOF ATTEMPT for NS (ν > 0) specifically
file: 278
date: 2026-03-29
---

## The Chain (from file 277)

For NS with ν > 0: the proof needs σ_min > 0 at the max-|ω| point.

## The Viscous Core Width

For a vortex tube being compressed (rate λ_perp) and diffused (rate ν):
  dσ²/dt = -2λ_perp σ² + 2ν

Equilibrium: σ² = ν/λ_perp.

At the attractor: λ_perp ~ |S| ~ |ω|/2.
So: σ² ~ 2ν/|ω|. For large |ω|: σ → 0.

## The Problem

With σ² ~ ν/|ω|:
DH_ωω/Dt ~ C × σ² × |ω|³ ~ Cν|ω|²
2α³ ~ |ω|³/4

Ratio: Cν|ω|²/(|ω|³/4) = 4Cν/|ω| → 0. FAILS for large |ω|.

## Alternative: Direct H_ωω bound (not its derivative)

From the Fourier lemma: H_ωω ≥ C × ε × σ² × |ω|²
(where ε is the z-modulation amplitude of the source)

Need: H_ωω > Var = ê·S²·ê - α².

If ε ≥ cα (z-variation proportional to stretching):
H_ωω ≥ C × cα × σ² × |ω|²

And Var ≤ |S|² = |ω|²/4.

Need: Ccσ²α|ω|² > |ω|²/4 → α > 1/(4Ccσ²).

With σ² ~ ν/|ω|: α > |ω|/(4Ccν).

For large |ω|: this requires α ~ |ω|, which contradicts α ≤ |ω|/2.
So the condition α > |ω|/(4Ccν) is only satisfiable when |ω| < 2Ccν.
For ν small: this is a tiny range.

## The NS Regularity via a DIFFERENT Route

Forget the pressure Hessian. For NS, there's a classical approach:

The enstrophy equation: dE/dt = 2∫ω·Sω - 2ν∫|∇ω|².

By Poincaré: ∫|∇ω|² ≥ λ₁ ∫|ω|² = λ₁ E.

So: dE/dt ≤ 2||S||∞ E - 2νλ₁E = 2(||S||∞ - νλ₁)E.

If ||S||∞ < νλ₁: the enstrophy DECAYS. This gives regularity for
||ω||∞ < 2νλ₁ (since ||S||∞ ≤ C||ω||∞).

But for large ||ω||∞: ||S||∞ >> νλ₁ and this doesn't help.

## The Key NS Bound: Leray Energy Inequality

For NS: d/dt(||u||²/2) = -ν||ω||² (energy decays).
So: ν∫₀^T ||ω||² dt ≤ ||u₀||²/2 (total enstrophy integral bounded).

This is the LERAY BOUND. It gives ∫E dt < C/ν.

Combined with the palinstrophy equation:
dP/dt ≤ C||ω||∞ P - 2νQ

The viscous term -2νQ damps the palinstrophy at high wavenumbers.

From Agmon: ||ω||∞² ≤ C√(PQ).
So: dP/dt ≤ C(PQ)^{1/4} P - 2νQ.
By Young: C(PQ)^{1/4}P ≤ νQ + C₁P^{4/3}/ν^{1/3}.
So: dP/dt ≤ -νQ + C₁P^{4/3}/ν^{1/3}.

Hmm, this gives P^{4/3} growth which is sub-cubic (4/3 < 3) but
SUPER-LINEAR (4/3 > 1). Possible blowup at T* ~ ν^{1/3}/P₀^{1/3}.

## Actually: the classical NS regularity proof attempt

The best known conditional result for NS:

If ||ω||_{L^∞([0,T]; L^{3/2})} < ∞: regularity.
This is the Prodi-Serrin condition.

From our data: ||ω||_{L^{3/2}} ≤ ||ω||_{L²}^{...} × ||ω||∞^{...}

This is getting into classical NS theory. The point is: for NS,
regularity is OPEN even with viscosity. The Clay problem is
specifically about NS (ν > 0) on R³ or T³.

## Honest Assessment

The Green's function C = 24.4 is a genuine computational advance.
But the core width σ shrinks with |ω| (both for Euler and NS),
making the effective source area decrease. The conversion factor C
is large but the source area compensates.

The NET scaling: H_ωω ~ C × |ω|² × σ² ~ C × |ω| × ν (for NS).
This grows LINEARLY with |ω| (not quadratically). Meanwhile,
Var ~ |ω|² (quadratic). For large |ω|: Var >> H_ωω.

The proof via Green's function + Fourier lemma gives:
  H_ωω ~ |ω| (linear, from viscous core width)
  Var ~ |ω|² (quadratic, from strain eigenvalues)
  For large |ω|: Var dominates → Q > 0 → no attractor guarantee

## 278. NS proof via Green's function doesn't close either.
## The core width shrinks too fast for the pressure to keep up.
## The gap: prove σ stays finite independently of |ω|.
