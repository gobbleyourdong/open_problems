---
source: DIRECT VARIATIONAL — min Q/|ω|² via Euler-Lagrange on the 6-dim space
type: NEW APPROACH — treat the entire optimization as a single variational problem
file: 711
date: 2026-03-31
instance: MATHEMATICIAN
---

## THE CLEAN FORMULATION

For N=3 modes with unit amps on a unit sphere (K=1 WLOG):

Minimize: f = Q/|ω|² = (9|ω|² - 8|S|²)/|ω|² = 9 - 8|S|²/|ω|²

Equivalently: maximize g = |S|²/|ω|² subject to the Biot-Savart constraint.

Variables: (θ₁₂, θ₁₃, θ₂₃, φ₁, φ₂, φ₃) ∈ [compact domain]
(3 k-angles constrained by Gram PSD, 3 polarization angles, and discrete sign choice)

The minimum f = 9/4 = 2.25 at the known extremum (file 467).
Need: f > 0, i.e., g < 9/8.

## THE STRUCTURE

From the identity |S|² = |ω|²/2 - 2C:
g = |S|²/|ω|² = 1/2 - 2C/|ω|².

So: max g ⟺ min C/|ω|².

The extremum of C/|ω|² satisfies:
∇(C/|ω|²) = (∇C × |ω|² - C × ∇|ω|²)/|ω|⁴ = 0
→ |ω|² ∇C = C ∇|ω|² (gradient proportionality).

At the extremum: ∇C = λ ∇|ω|² where λ = C/|ω|² (the Lagrange multiplier
IS the ratio being extremized).

## THE EULER-LAGRANGE EQUATIONS

For each parameter xₐ (a = 1,...,6):
∂C/∂xₐ = λ ∂|ω|²/∂xₐ

These are 6 equations in 7 unknowns (x₁,...,x₆,λ). With the constraint
that s* is the max-|ω|² sign (discrete), this gives 6 equations in
6 unknowns + the discrete sign choice.

The solutions are the CRITICAL POINTS of C/|ω|² on the 6-dim parameter space.
There are finitely many (by algebraic geometry, since C and |ω|² are
trigonometric polynomials).

## WHAT WE KNOW

The global minimum of C/|ω|² is -11/64 = -0.171875 (verified numerically
to 10⁻¹⁵ at the geometry cosθ = (-3/4, -3/4, 1/4), file 467).

At this extremum: λ = -11/64. The E-L equations are satisfied.
The Hessian of C/|ω|² (restricted to the 6-dim space) is positive semi-
definite (local minimum, file 472 landscape analysis).

## THE PROOF BY CLASSIFICATION OF CRITICAL POINTS

**Proof outline**:
1. The critical points of C/|ω|² form a finite algebraic set (Bezout).
2. At each critical point: verify C/|ω|² > -5/16.
3. The boundary of the parameter domain: verify C/|ω|² > -5/16.
4. Conclusion: C/|ω|² ≥ -11/64 > -5/16 everywhere.

Step 2 can be done NUMERICALLY (exhaustive search found only the -11/64
extremum) or ALGEBRAICALLY (solve the E-L system symbolically).

## THE SYMMETRY REDUCTION

At the extremum: the configuration has Z₂ symmetry (modes 1,2 symmetric).
This reduces the 6-dim space to effectively 3 dimensions:
- θ (the common k-angle for both pairs involving mode 0)
- ψ (the azimuthal angle of k₃ relative to k₂)
- φ₀ (mode 0's polarization angle)
- φ₁ = φ₂ by symmetry

The E-L equations reduce to 3 equations in 3 unknowns.
These can potentially be solved in CLOSED FORM.

## STATUS

The direct variational approach is the CLEANEST path to the N=3 proof.
It avoids the per-pair decomposition entirely and works with the
global optimization directly.

The extremum at -11/64 is fully characterized (algebraic geometry,
file 467). The E-L equations at this point can be verified.
The classification of ALL critical points proves the global bound.

For N≥4: the same approach applies but with more variables.
The dimension grows as 3(N-1) + N = 4N-3 (k-angles + polarizations).
For N=4: 13 parameters. The E-L system has more solutions,
but the global minimum is still bounded (observed -0.173).

## 711. Direct variational: classify all critical points of C/|ω|².
## The N=3 case has 6 parameters with Z₂ symmetry → 3 effective.
## The global min -11/64 is a clean algebraic point.
## The proof: verify Q > 0 at ALL critical points + boundary.
## This is the CORRECT framework for the proof.
