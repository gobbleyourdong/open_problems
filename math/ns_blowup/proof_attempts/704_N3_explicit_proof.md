---
source: N=3 EXPLICIT — the proof for 3 modes using the coupling lemma
type: NEW MATHEMATICS — the single-angle constraint across multiple pairs
file: 704
date: 2026-03-31
instance: MATHEMATICIAN
---

## THE SETUP FOR N=3

Three modes with k₁, k₂, k₃ on the unit sphere (K=1 WLOG).
Each vⱼ ⊥ kⱼ with |vⱼ| = 1 (unit amps WLOG by homogeneity).
Signs sⱼ = ±1 chosen to maximize |ω|² = 3 + 2Σ sᵢsⱼDᵢⱼ.

Three pairs: (0,1), (0,2), (1,2).
Three normals: n̂₀₁, n̂₀₂, n̂₁₂ (each = k_i × k_j / |k_i × k_j|).

From file 703:
    P_{ij} = sin²θ_{ij} × n_{ij}^(i) × n_{ij}^(j)
    D_{ij} = n_{ij}^(i) × n_{ij}^(j) - cosθ_{ij} × t_{ij}^(i) × t_{ij}^(j)

where n_{ij}^(i) = vᵢ · n̂_{ij} and t_{ij}^(i) = vᵢ · k̂_j^{⊥i}.

## THE SINGLE-ANGLE CONSTRAINT

Mode 0 has ONE free angle φ₀ in the plane ⊥ k₀.

This angle determines:
- n₀₁^(0) = v₀ · n̂₀₁ (normal projection for pair (0,1))
- t₀₁^(0) = v₀ · k̂₁^{⊥0} (tangential for pair (0,1))
- n₀₂^(0) = v₀ · n̂₀₂ (normal projection for pair (0,2))
- t₀₂^(0) = v₀ · k̂₂^{⊥0} (tangential for pair (0,2))

ALL FOUR quantities from ONE angle φ₀. They satisfy:
- (n₀₁^(0))² + (t₀₁^(0))² = 1  [Pythagoras for pair (0,1)]
- (n₀₂^(0))² + (t₀₂^(0))² = 1  [Pythagoras for pair (0,2)]

But n̂₀₁ and n̂₀₂ are DIFFERENT directions (unless k₁ and k₂ differ
only in the plane ⊥ k₀). So the two Pythagoras constraints are
on DIFFERENT decompositions of the SAME unit vector v₀.

The relationship: n̂₀₁ and k̂₁^{⊥0} form a basis for the plane ⊥ k₀.
Also n̂₀₂ and k̂₂^{⊥0} form a (different) basis for the SAME plane.

The rotation between these two bases is determined by the k-geometry.

## THE KEY: ROTATION ANGLE BETWEEN PAIR FRAMES

In the plane ⊥ k₀: the two bases are
    {n̂₀₁, k̂₁^{⊥0}} and {n̂₀₂, k̂₂^{⊥0}}

The rotation angle ψ₀ between them:
    cos ψ₀ = n̂₀₁ · n̂₀₂  (and k̂₁^{⊥0} · k̂₂^{⊥0} = cos ψ₀)
    sin ψ₀ = n̂₀₁ · k̂₂^{⊥0} = -k̂₁^{⊥0} · n̂₀₂

With v₀ = cos(φ₀) n̂₀₁ + sin(φ₀) k̂₁^{⊥0} (in the pair-(0,1) frame):
    n₀₁^(0) = cos φ₀
    t₀₁^(0) = sin φ₀
    n₀₂^(0) = cos(φ₀ - ψ₀)  [rotation by ψ₀]
    t₀₂^(0) = sin(φ₀ - ψ₀)

So the SINGLE angle φ₀ determines all four projections, with the
inter-pair coupling captured by the rotation angle ψ₀.

Similarly: φ₁ determines all projections for mode 1 (in pairs (0,1)
and (1,2)), with coupling angle ψ₁. And φ₂ for mode 2.

## C AND |ω|² IN TERMS OF (φ₀, φ₁, φ₂)

C = s₀s₁ sin²θ₀₁ cos(φ₀) cos(φ₁')
  + s₀s₂ sin²θ₀₂ cos(φ₀-ψ₀) cos(φ₂')
  + s₁s₂ sin²θ₁₂ cos(φ₁-ψ₁) cos(φ₂-ψ₂)

where φⱼ' denotes the angle of mode j in the frame of the relevant pair
(different from φⱼ for different pairs due to the rotation angles).

|ω|² = 3 + 2[s₀s₁ D₀₁ + s₀s₂ D₀₂ + s₁s₂ D₁₂]

where D_{ij} = n^(i)n^(j) - cosθ t^(i)t^(j).

## THE OPTIMIZATION

min C/|ω|² over (φ₀, φ₁, φ₂) ∈ [0, 2π)³ and sign pattern s.

This is a 3-variable optimization on (S¹)³ (for each fixed k-geometry
and sign pattern). The function is a RATIO of trigonometric polynomials
of degree 2.

The minimum of such a ratio can be found by solving the
Euler-Lagrange equations: ∂/∂φⱼ [C - λ|ω|²] = 0 for j=0,1,2.

These are 3 trigonometric equations in 3 unknowns. The solutions
are the critical points of C/|ω|².

## THE N=2 CASE (verification)

For N=2 (one pair): C = s₀s₁ sin²θ cos φ₀ cos φ₁.
|ω|² = 2 + 2s₀s₁(cos φ₀ cos φ₁ - cosθ sin φ₀ sin φ₁).

With s₀s₁ = 1 (constructive):
C/|ω|² = sin²θ cos φ₀ cos φ₁ / [2 + 2(cos φ₀ cos φ₁ - cosθ sin φ₀ sin φ₁)]

Setting ∂/∂φ₀ = ∂/∂φ₁ = 0 gives the critical points.
The minimum is at cos φ₀ = cos φ₁ (by symmetry), giving
C/|ω|² = sin²θ cos²φ / [2 + 2cos²φ - 2cosθ sin²φ].

This is a 1-variable optimization in φ, solvable by calculus.
The minimum over both θ and φ gives -1/8 (the N=2 sharp bound). ✓

## FOR N=3: THE SAME APPROACH

C/|ω|² is a ratio of trig polynomials in (φ₀, φ₁, φ₂) with
coefficients determined by the k-geometry (angles θ_{ij} and
rotation angles ψⱼ).

The minimum over (φ₀, φ₁, φ₂, k-geometry) can be found by:
1. For each k-geometry: solve the 3 E-L equations numerically.
2. Over all k-geometries: find the worst.
3. The worst is at cosθ = (-3/4, -3/4, 1/4) with value -11/64.

**For a PROOF**: need to show min ≥ -5/16 for ALL k-geometries.

This is a FINITE-DIMENSIONAL optimization (k-geometry has ~3 parameters,
polarizations have 3 angles). Total: ~6 parameters.

The function is smooth, the domain is compact (all angles), and the
minimum is -11/64 with 45% margin. A COMPUTER-ASSISTED PROOF via
interval arithmetic on a 6-dim grid is feasible.

**For an ANALYTICAL proof**: use the E-L equations to characterize
ALL critical points and show none has C/|ω|² < -5/16. The E-L
equations are polynomial (after substituting cos/sin), so the
critical points form an algebraic variety. Bounding the function
on this variety is an algebraic geometry problem.

## THE ALGEBRAIC APPROACH (new mathematics)

The critical point equations ∂(C - λ|ω|²)/∂φⱼ = 0 give:

∂C/∂φⱼ = λ ∂|ω|²/∂φⱼ for j = 0,1,2.

These are 3 equations in 4 unknowns (φ₀, φ₁, φ₂, λ).
With λ = C/|ω|² at the critical point: this is 3 equations in 3 unknowns.

Using c_j = cos φ_j, s_j = sin φ_j with c_j² + s_j² = 1:
the equations become POLYNOMIAL. The system has finitely many solutions
(by Bezout's theorem). The minimum of C/|ω|² is achieved at one
of these solutions.

**If the algebraic system has a CLOSED-FORM solution** (like the
N=2 case): we can explicitly compute all critical values and verify
min ≥ -5/16.

At the extremum: the solution is φ₀ = specific angle giving cos γ₀ = 1
(mode 0 aligned with ω), and φ₁ = φ₂ by symmetry giving cos γ = 1/2.
This is a CLEAN algebraic point.

## 704. N=3 explicit: C/|ω|² is a ratio of trig polynomials in 3 angles.
## The coupling between pairs goes through rotation angles ψⱼ in the ⊥kⱼ plane.
## The optimization is 6-dimensional (3 k-angles + 3 polarization angles).
## The algebraic approach: solve the E-L equations, classify all critical points,
## verify min ≥ -5/16. This is concrete, finite-dimensional algebraic geometry.
