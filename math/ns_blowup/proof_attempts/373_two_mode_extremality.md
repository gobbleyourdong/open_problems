---
source: Proving 2-mode extremality for |∇u|²/|ω|² — marginal mode analysis
type: PROOF ATTEMPT — showing dF/da₃ ≤ 0 at the 2-mode boundary
file: 373
date: 2026-03-29
---

## SETUP

For N-mode div-free fields on T³ at the global max x* of |ω|:

  F(a₁,...,aN) = |∇u(x*)|² / |ω(x*)|²

The CLAIM: F achieves its maximum when at most 2 modes have nonzero amplitude.
Specifically: max F = 5/4 (achieved by the optimal 2-mode config from file 364).

## THE PAIRWISE STRUCTURE

At a vertex x* with signs s_k = ±1:

|∇u|² = Σ_k a_k² + 2Σ_{j<k} s_js_k a_ja_k G_{jk}
|ω|²  = Σ_k a_k² + 2Σ_{j<k} s_js_k a_ja_k D_{jk}

where:
- G_{jk} = (w_j·w_k)(k_j·k_k)/(|k_j|²|k_k|²) = gradient cross-term coefficient
- D_{jk} = v̂_j·v̂_k = vorticity cross-term coefficient

EXCESS = |∇u|² - |ω|² = 2Σ_{j<k} s_js_k a_ja_k (G_{jk} - D_{jk})

Define Δ_{jk} = G_{jk} - D_{jk} (the per-pair excess coefficient).

From file 364: Δ_{jk} = -sin²α_{jk} × sinβ_{jk}sinγ_{jk}

where α is the angle between k_j, k_k and β, γ are polarization cross-angles.

## MARGINAL MODE ANALYSIS

Consider a 2-mode field (a₁, a₂ > 0, a_k = 0 for k ≥ 3). The ratio:

F₀ = (a₁² + a₂² + 2s₁s₂a₁a₂G₁₂) / (a₁² + a₂² + 2s₁s₂a₁a₂D₁₂)

Now add a 3rd mode with small amplitude a₃ = ε → 0:

|∇u|² = a₁² + a₂² + ε² + 2s₁s₂a₁a₂G₁₂ + 2ε(s₁s₃a₁G₁₃ + s₂s₃a₂G₂₃)
|ω|²  = a₁² + a₂² + ε² + 2s₁s₂a₁a₂D₁₂ + 2ε(s₁s₃a₁D₁₃ + s₂s₃a₂D₂₃)

F(ε) = [F₀|ω|₀² + ε² + 2ε(s₁s₃a₁G₁₃+s₂s₃a₂G₂₃)] /
        [|ω|₀² + ε² + 2ε(s₁s₃a₁D₁₃+s₂s₃a₂D₂₃)]

At ε = 0:

dF/dε = [2(s₁s₃a₁G₁₃+s₂s₃a₂G₂₃)|ω|₀² - F₀×2(s₁s₃a₁D₁₃+s₂s₃a₂D₂₃)|ω|₀²] / |ω|₀⁴

= 2/|ω|₀² × [(s₁s₃a₁G₁₃+s₂s₃a₂G₂₃) - F₀(s₁s₃a₁D₁₃+s₂s₃a₂D₂₃)]

For F to DECREASE with the 3rd mode: need dF/dε ≤ 0, i.e.:

Σ_{j∈{1,2}} s_js₃a_j(G_{j3} - F₀D_{j3}) ≤ 0

Since the sign s₃ is chosen by the max condition (to maximize |ω|²),
the direction of the inequality depends on the geometry.

## THE KEY CONSTRAINT

At the OPTIMAL 2-mode config (F₀ = 5/4):
- a₁ = a₂ (equal amplitudes)
- α₁₂ = 60° (optimal angle)
- D₁₂ = specific dot product

F₀ = 5/4 means |∇u|² = (5/4)|ω|².

For ANY 3rd mode: need

  Σ s_js₃a_j(G_{j3} - (5/4)D_{j3}) ≤ 0

i.e.: the "effective excess" from the 3rd mode (G_{j3} - (5/4)D_{j3}) must be
non-positive when weighted by the existing amplitudes and signs.

## BOUND ON G_{j3} - (5/4)D_{j3}

G_{j3} = (w_j·w₃)(k_j·k₃)/(|k_j|²|k₃|²)
D_{j3} = v̂_j·v̂₃

G - (5/4)D = (w·w')(k·k')/(|k|²|k'|²) - (5/4)(v̂·v̂')

Using the BAC-CAB identity and |Δ| = G - D = -sin²α sinβ sinγ:

G - (5/4)D = D + Δ - (5/4)D = Δ - D/4 = -sin²α sinβ sinγ - D/4

For the 3rd mode to HELP (make dF/dε > 0): need G - (5/4)D > 0 for at
least one pair (j,3). This requires -sin²α sinβ sinγ > D/4.

For the optimal 2-mode config: D₁₂ ≈ 0 (orthogonal polarizations give max
excess). So D₁₃ and D₂₃ are constrained by the new mode's polarization.

THE QUESTION: can -sin²α_{j3} sinβ_{j3} sinγ_{j3} > D_{j3}/4?

Since |sin²α sinβ sinγ| ≤ sin²α ≤ 1 and D ∈ [-1,1]:
max of (-sin²α sinβ sinγ - D/4) = ... depends on the joint optimization.

At α = 90° (perpendicular new k): Δ = -sinβ sinγ. G - 5D/4 = -sinβsinγ - D/4.
With D = cosβ cosγ + sinβ sinγ cosΦ (general relation):

This gets complicated. Let me try a different approach.

## CONVEXITY ARGUMENT

CLAIM: F(a₁,...,aN) = |∇u|²/|ω|² is quasi-convex in the amplitudes on
the constraint set {a_k ≥ 0, Σa_k = const}.

If quasi-convex: the maximum is on the BOUNDARY (where some a_k = 0).
The boundary has fewer active modes. By induction: max is at N = 2.

Is F quasi-convex? F = (aᵀMa)/(aᵀNa) where M, N are symmetric matrices
(M for |∇u|² coefficients, N for |ω|² coefficients).

A ratio of quadratic forms is NOT quasi-convex in general.

But: the specific structure (M = N + excess matrix, with excess having
specific sign pattern) may give quasi-convexity.

## STATUS

The marginal mode analysis shows the 2-mode extremality reduces to a
finite-dimensional optimization (the sign of dF/dε). This can likely
be resolved by casework on the geometry of the 3rd mode.

The key insight: at the optimal 2-mode config (F = 5/4), adding any mode
must decrease F because the excess Δ_{j3} is bounded while D_{j3} contributes
to the denominator. The precise bound needs the pairwise formula.

## NEXT STEPS

1. Compute dF/dε explicitly for the optimal 2-mode config + arbitrary 3rd mode
2. Show it's always ≤ 0 (casework on α₃, β₃, γ₃)
3. Or: verify quasi-convexity numerically for the specific M, N matrices
4. Or: bound F directly via the pairwise excess structure

## 373. The 2-mode extremality reduces to dF/dε ≤ 0 at the boundary.
## Need: G_{j3} - (5/4)D_{j3} ≤ 0 on average. Likely provable via pairwise bounds.
