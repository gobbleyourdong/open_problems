---
source: STOKESLET ASYMPTOTIC — the 1/|y| coefficient in the Leray profile
type: ANALYSIS — the coefficient C is determined by the total force
file: 841
date: 2026-04-02
instance: MATHEMATICIAN (Opus)
---

## THE ASYMPTOTIC STRUCTURE

Bounded Leray solutions: φ = C_Stokeslet/|y| + O(e^{-|y|²/(4ν)}).

The Stokeslet coefficient C_ij = (δ_{ij}/|y| + y_iy_j/|y|³)·F_j/(8πν)
is determined by the TOTAL FORCE F on the fluid:
    F = ∫(nonlinear terms) dx = ∫(φ·∇)φ dx.

For the Leray equation WITHOUT external forcing:
    -νΔφ + (1/2)φ + (1/2)y·∇φ + (φ·∇)φ + ∇q = 0.

Integrate over B_R and send R → ∞:
    ∫∂B_R (ν∂φ/∂n - qn) dS = -∫_{R³} ((1/2)φ + (1/2)y·∇φ + (φ·∇)φ) dy.

The LHS is the total force from the Stokes part (determines C).
The RHS involves the drift and nonlinear terms.

For the DRIFT term: ∫(1/2)φ + (1/2)y·∇φ = ∫(1/2)∇·(yφ) - (1/2)φ
= (boundary terms) - (1/2)∫φ. For bounded φ decaying as 1/|y|:
∫|φ| dy diverges (1/|y| is not integrable on R³).

So the force integral is NOT well-defined for 1/|y| decay.
This means the standard force-balance argument doesn't directly apply.

## THE CORRECT APPROACH: WEIGHTED ESTIMATES

Tsai's proof uses WEIGHTED energy estimates with weight (1+|y|²)^{-s}.
The 1/|y| bound comes from a Sobolev embedding after establishing
weighted L² bounds.

To improve: need TIGHTER weighted estimates or a DIFFERENT weight.

The self-adjoint OU operator: L = -νΔ + (1/2) + (1/2)y·∇.
In the OU inner product (weighted by the Gaussian e^{-|y|²/(4ν)}):
L is self-adjoint with spectrum {k/2 : k = 0,1,2,...} (Hermite).
The 1/|y| solution is in the NULL SPACE (eigenvalue 0).

For L to force the null-space coefficient to 0: need the nonlinear
term (φ·∇)φ to be ORTHOGONAL to the null space in the weighted L².

(φ·∇)φ projected onto the null space: ∫(φ·∇)φ · ψ₀ · e^{-|y|²/(4ν)} dy
where ψ₀ ~ 1/|y| is the null-space eigenfunction.

If this integral is 0: C = 0. If nonzero: C ≠ 0.

## THE KEY OBSERVATION

The null-space eigenfunction 1/|y| is NOT in L² with Gaussian weight!
∫(1/|y|)² e^{-|y|²/(4ν)} dy = 4π∫₀^∞ e^{-r²/(4ν)} dr < ∞. Wait:
= 4π∫₀^∞ (1/r²)·r²·e^{-r²/(4ν)} dr = 4π∫₀^∞ e^{-r²/(4ν)} dr = 4π√(πν) < ∞.

Actually 1/|y| IS in L²(Gaussian weight)! The Gaussian provides enough decay.

So the projection IS well-defined. The question: is the nonlinear
forcing (φ·∇)φ orthogonal to 1/|y| in the Gaussian-weighted space?

This is a SPECIFIC INTEGRAL CONDITION on the Leray profile.
If it's satisfied: C = 0. If not: C ≠ 0.

## STATUS

The ε problem reduces to: is the Leray nonlinearity orthogonal to the
OU null space in the Gaussian-weighted inner product?

This is a concrete functional-analytic question.
28 years open (since Tsai 1998). Nobody has answered it.

## 841. The Stokeslet gives the 1/|y| asymptotics. The coefficient is
## determined by the projection of (φ·∇)φ onto the OU null space.
## If the projection is 0: C = 0 → φ ∈ L³ → NRS → regularity.
## This is a SPECIFIC INTEGRAL CONDITION on the Leray equation.
