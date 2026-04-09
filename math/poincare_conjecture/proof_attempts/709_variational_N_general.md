---
source: VARIATIONAL APPROACH — bound |S|²/|ω|² using the max condition directly
type: NEW IDEA — bypass per-pair entirely, use |ω|² max as a PDE constraint
file: 709
date: 2026-03-31
instance: MATHEMATICIAN
---

## THE IDEA

Stop decomposing into pairs. Use the MAX CONDITION directly.

At x* = argmax|ω|² on T³: for any smooth div-free field ω:

    Δ|ω|² ≤ 0 (sub-harmonic at the max)

Expanding: Δ|ω|² = 2(|∇ω|² + ω·Δω).

At the max: ω·Δω ≤ -|∇ω|² (from Δ|ω|² ≤ 0).

And: |∇u|² = |S|² + |ω|²/2 (standard decomposition).
And: Parseval: ||∇u||₂² = ||ω||₂² (L² identity).

But we need POINTWISE, not L².

## THE BOCHNER-TYPE IDENTITY

For the vorticity field: Δω = curl Δu = Δ(curl u)... on T³ with
the NS structure, Δω involves the Biot-Savart operator.

For a GENERAL div-free field (not necessarily NS): ω is just a
div-free vector field. The Laplacian Δω is the component-wise Laplacian.

The identity: Δ|ω|² = 2|∇ω|² + 2ω·Δω.

At the max: 2|∇ω|² + 2ω·Δω ≤ 0 → ω·Δω ≤ -|∇ω|².

For Fourier modes: ω = Σ aₖv̂ₖ cos(k·x). At a vertex (all cos=±1):
∇ω = 0 (since ∂/∂xₐ cos(k·x) = -kₐ sin(k·x) = 0 at vertex).

So: |∇ω|² = 0 at vertices. And Δω = -Σ |kⱼ|² aⱼv̂ⱼsⱼ (Laplacian of cos).
ω·Δω = -Σⱼ |kⱼ|² aⱼsⱼ (vⱼ·ω) = -Σ |kⱼ|² wⱼ.

Hessian trace: Δ|ω|² = 0 + 2ω·Δω = -2Σ|kⱼ|²wⱼ ≤ 0.
→ Σ|kⱼ|²wⱼ ≥ 0. This is Tr(M) = K²|ω|² ≥ 0 for single shell. ✓

But ∇ω = 0 at vertices means the Bochner inequality is TRIVIAL (0 ≤ 0).
It doesn't constrain |S|².

## THE NON-VERTEX CASE

At a NON-vertex max (for multi-shell fields): ∇ω ≠ 0 and the
Bochner inequality is non-trivial. But for single-shell fields,
the max IS at a vertex (proven for K²=2, conjectured for others).

## A DIFFERENT VARIATIONAL APPROACH

Instead of the max of |ω|²: consider the FUNCTIONAL

    F[ω] = |S(x*)|² / |ω(x*)|²  evaluated at x* = argmax|ω|².

This functional maps div-free fields to [0, ∞). We want sup F < 9/8.

F is NOT a standard PDE functional — it depends on ω at ONE point
(the max), which itself depends on the GLOBAL field.

This is what makes the problem hard: it's a sup over a non-local
functional on an infinite-dimensional space.

## THE FINITE-MODE REDUCTION

For finitely many modes: ω = Σ aⱼvⱼcos(kⱼ·x).
At a vertex: ω = Σ sⱼaⱼvⱼ, S = Σ sⱼSⱼ (both finite linear combinations).

F = |Σ sⱼSⱼ|² / |Σ sⱼaⱼvⱼ|² at the MAX vertex.

This is a FINITE-DIMENSIONAL PROBLEM: maximize a ratio of quadratic
forms over signs s ∈ {±1}^N, subject to s being the |ω|²-maximizer.

The N=3 case is solved (file 707): F < 9/8 by the per-pair Q bound.
The N≥4 case: the per-pair bound is too crude.

## THE PER-MODE DECOMPOSITION OF Q

Q = Σⱼ [9|vⱼ|² - 8|Sⱼ|²] + 2Σᵢ<ⱼ sᵢsⱼ[9Dᵢⱼ - 8Tr(SᵢSⱼ)]
  = 5N + 2Σᵢ<ⱼ sᵢsⱼQᵢⱼ

The diagonal is ALWAYS 5N > 0 (self-vanishing: |Sⱼ|²=|vⱼ|²/2).
The cross-terms can be negative.

For Q > 0: need |Σ sᵢsⱼQᵢⱼ| < 5N/2.

**Bound**: |Σ sᵢsⱼQᵢⱼ| ≤ ||Q_matrix||_op × ||s||² = ||Q_matrix||_op × N
(where Q_matrix has entries Qᵢⱼ and ||s||²=N for s∈{±1}^N).

So: need ||Q_matrix||_op < 5/2.

Is this true? From the N=4 worst: Σ sQ = -1.71, and N=4, so
|Σ sQ|/N = 0.43 < 5/2 = 2.5. Yes, with huge margin.

But ||Q_matrix||_op can be much larger than |s^T Q s|/N for a specific s.

**Alternative**: at s* = argmax(s^T A s) where A = I + D_offdiag:
s* maximizes the "constructive" quadratic form. The cross-form
s^T Q s at s* is correlated with s^T A s because Q = 5A + 8P.

s^T G' s = 5 s^T A s + 16 s^T_off P s = 5|ω|² + 16C.

At s*: |ω|² is maximized. The 16C term is bounded by the correlation
between A and P.

**Claim**: since P is "close to" D (in the sense that P = sin²θ nn
while D = nn - cosθ tt, and they share the nn component):
the maximizer of s^T A s also tends to make s^T P s non-negative.

**This is the sign-flip theorem (file 705) in matrix language.**

## THE MATRIX INEQUALITY APPROACH

Define: A = I + D_off (vorticity matrix), P = P_off (correction matrix).
G' = 5A + 8P (the Q matrix with diagonal 5).

**Want**: s*^T G' s* > 0 where s* = argmax s^T A s.

**Sufficient**: G' ≥ 0 (positive semidefinite). But this fails.

**Alternative**: show G' ≥ -εA for some ε < 5, i.e., G' + εA ≥ 0.
Then: s*^T G' s* ≥ -ε s*^T A s* = -ε|ω|²*.
And: Q = s*^T G' s* ≥ -ε|ω|²*. Need -ε|ω|² + 5|ω|² > 0 → ε < 5.
Hmm, G' = 5A + 8P, so G' + εA = (5+ε)A + 8P. Need this PSD.
(5+ε)A + 8P ≥ 0 iff λ_min((5+ε)A + 8P) ≥ 0.

This requires 8P ≥ -(5+ε)A, i.e., the correction P is bounded
relative to A. This is a MATRIX inequality, not a scalar one.

## THE KEY: IS P BOUNDED BY A?

If |P_{ij}| ≤ α|D_{ij}| + β for some constants: then ||P||_op ≤ α||D||_op + βN.
And (5+ε)A + 8P = (5+ε-8α)D + (5+ε)I + 8(P-αD).

This gets complicated. Let me think about whether P ≪ A in some sense.

From the coupling: P = sin²θ nn and D = nn - cosθ tt.
For orthogonal k (cosθ=0): P = nn = D. So P = D. Ratio 1.
For parallel k (cosθ=1): P = 0. D = nn - tt. Ratio 0.
For general: P/D varies.

The matrix P is NOT simply proportional to D. The relationship
depends on the mode geometry (k-angles, polarizations).

## STATUS

The N≤3 proof works because the per-pair Q count gives Q ≥ 3 > 0.
For N≥4: the per-pair count fails. The matrix inequality approach
(G' ≥ -εA) might work but requires bounding P relative to A.

The cleanest path for general N: prove ||P||_op ≤ (5/8)||A||_op - 5/(8N)
or something similar. This would give G' ≥ 0 at s*.

## 709. Variational approach: Q > 0 ↔ matrix inequality G' = 5A + 8P.
## Need: s*^T(5A+8P)s* > 0 at s* = argmax(s^T A s).
## Sufficient: 8||P||_op < 5 (but this fails for orthogonal k where P=D).
## The proof needs the CORRELATION between the argmax of A and the
## non-negativity of 5A+8P at that argmax. This is the sign-flip theorem
## in matrix form.
