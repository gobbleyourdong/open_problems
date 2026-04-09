---
source: THE MECHANISM FOR N=2 — why M ≥ 0 forces C > -1/8
type: NEW MATHEMATICS — understanding the N=2 proof geometrically
file: 702
date: 2026-03-31
instance: MATHEMATICIAN
---

## STRIPPING TO THE ESSENCE: N=2

Two modes. k₁, k₂ on the unit sphere. v₁ ⊥ k₁, v₂ ⊥ k₂, unit amps.
Signs s₁, s₂. WLOG s₁s₂ = +1 at the max (the interesting case).

ω = v₁ + v₂. |ω|² = 2 + 2D where D = v₁·v₂.
M = w₁(k₁⊗k₁) + w₂(k₂⊗k₂) where wⱼ = vⱼ·ω = 1 + D.

Wait: w₁ = v₁·(v₁+v₂) = 1 + D. Similarly w₂ = 1 + D.
So w₁ = w₂ = 1 + D.

M = (1+D)(k₁⊗k₁ + k₂⊗k₂). This is PSD iff 1+D ≥ 0, i.e., D ≥ -1.
Since D = v₁·v₂ ≥ -1 always: M ≥ 0 is AUTOMATIC for N=2, s₁s₂=+1.

The correction: C = P₁₂ where P = sin²θ D + cosθ(v₁·k₂)(v₂·k₁).
|ω|² = 2 + 2D.

C/|ω|² = [sin²θ D + cosθ(v₁·k₂)(v₂·k₁)] / (2+2D)

The N=2 proof (file 525) showed min C/|ω|² = -1/8 at D=-1/2, θ=60°.

**Why does M ≥ 0 help here?** It doesn't constrain anything for N=2
(it's automatic). The bound comes from the GEOMETRY of P vs D.

So for N=2, the Hessian doesn't do the work. The bound comes directly
from the relationship P = sin²θ D + correction.

## THE REAL QUESTION FOR N≥3

For N=2: every sign pattern gives M ≥ 0 automatically.
For N≥3: NOT every sign pattern gives M ≥ 0. The max sign pattern
is the one that maximizes |ω|², and this specific pattern might have
M non-PSD for other sign choices — but it MUST have M ≥ 0 (since
it's the maximum).

The Hessian constraint EXCLUDES sign patterns that would give M non-PSD.
These excluded patterns might be exactly the ones that give C < -5/16.

**The theorem to prove**: among all sign patterns with M ≥ 0,
the minimum C/|ω|² is bounded below by -5/16 (or better).

## REFORMULATION AS A SEMIDEFINITE PROGRAM

Given: N modes with k-vectors kⱼ, polarizations vⱼ (unit, ⊥ kⱼ).
Variable: sign pattern s ∈ {±1}^N.

Objective: minimize C/|ω|² = [Σᵢ<ⱼ sᵢsⱼPᵢⱼ] / [Σ|vⱼ|² + 2Σᵢ<ⱼ sᵢsⱼDᵢⱼ]

Subject to: M(s) = Σⱼ wⱼ(s)(kⱼ⊗kⱼ) ≥ 0
           where wⱼ(s) = sⱼ Σₖ sₖ(vⱼ·vₖ)

This is a CONSTRAINED combinatorial optimization. The constraint M ≥ 0
is a SEMIDEFINITE constraint on the sign pattern.

**Key insight**: without the M ≥ 0 constraint, the minimum C/|ω|²
could be arbitrarily negative (choose signs to maximize negative P
terms while keeping |ω|² small).

WITH the constraint: the minimum is bounded (= -0.173 observed).

## THE LAGRANGIAN APPROACH

At the minimum: the constraint M ≥ 0 must be ACTIVE (otherwise the
minimum is in the interior and we're back to the unconstrained problem).

When M ≥ 0 is active: M has a zero eigenvalue. det(M) = 0.

For a 3×3 matrix: det(M) = 0 means M has rank ≤ 2. This constrains
the wⱼ distribution across k-directions.

At the N=3 worst case (C/|ω|² = -11/64):
Let me check: does M have a zero eigenvalue?

## CHECKING THE EXTREMAL M

At the N=3 extremum: cosθ = (-3/4, -3/4, 1/4), all D = -1/2,
signs (-1,+1,+1), |ω|² = 4.

ω = -v₁ + v₂ + v₃. wⱼ = sⱼ(vⱼ·ω):
w₁ = -v₁·(-v₁+v₂+v₃) = -(−1−1/2−1/2) = -(-2) = 2
w₂ = v₂·(-v₁+v₂+v₃) = -1/2+1-1/2 = 0
w₃ = v₃·(-v₁+v₂+v₃) = -1/2-1/2+1 = 0

**w₂ = w₃ = 0!** Only w₁ = 2 is nonzero.

M = 2(k₁⊗k₁). This has rank 1.
Eigenvalues: 2|k₁|² = 2, 0, 0.

**The Hessian IS degenerate at the extremum!** Two zero eigenvalues.

This means: the extremum sits on the BOUNDARY of the M ≥ 0 constraint.
Any perturbation that makes w₂ or w₃ negative would violate M ≥ 0.

## THE INSIGHT

At the worst C/|ω|²: the Hessian is MAXIMALLY degenerate (rank 1).
This means: most of the "Hessian budget" is concentrated in one
direction (k₁). The other modes (2,3) have wⱼ = 0 — they're on the
boundary of the allowed region.

**Theorem sketch**: the degeneracy of M at the extremum is what LIMITS
how negative C can be. With rank-1 M: only one mode contributes to
the Hessian, and the constraint wⱼ ≥ 0 for the others (or wⱼ can be
slightly negative if compensated) limits the polarization angles.

The rank-1 Hessian means: ω is aligned with v₁ only. Modes 2,3
are perpendicular to ω (since w₂ = w₃ = 0 means v₂·ω = v₃·ω = 0).

At D = -1/2 for all pairs: this is a very specific geometric config.
The negative C comes from the strain cross-term of the pair (2,3),
which has the largest sin²θ.

## THE PATH TO THE THEOREM

**Proposition**: For N=3 div-free modes at a vertex max:
if M = Σ wⱼ(kⱼ⊗kⱼ) ≥ 0 with Tr(M) = K²|ω|², then C ≥ -11/64 |ω|².

**Proof strategy**:
1. The worst case has M rank 1 (two zero eigenvalues).
2. Rank 1 means ω is "sourced" by one mode only: w₁ = |ω|², w₂=w₃=0.
3. w₂=0 means v₂·ω=0: mode 2 is perpendicular to ω.
4. This constrains D₁₂, D₁₃, D₂₃ through v₂⊥ω and v₃⊥ω.
5. With these constraints: C is a function of θ angles only.
6. Maximize -C/|ω|² under the rank-1 constraint → get 11/64.

The rank-1 assumption is KEY. If M has higher rank: more modes
contribute to ω, giving better averaging and higher C.

## 702. The mechanism: at the extremum, M is rank 1.
## The Hessian degeneracy constrains the geometry.
## w₂ = w₃ = 0 (perpendicular modes) limits C to -11/64.
## Path: prove rank-1 is the worst, then bound C under rank-1.
