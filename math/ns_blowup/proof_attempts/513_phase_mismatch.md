---
source: PHASE MISMATCH — S is sine-driven, ω is cosine-driven, structurally opposed
type: KEY STRUCTURAL INSIGHT — could close the gap if max is at lattice point
file: 513
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE OBSERVATION

For a single K-shell field on T³ (all modes with |k| = K):

**Vorticity**: ω(x) = Σ_j a_j v̂_j cos(k_j · x)    ← COSINE driven
**Velocity**:  u(x) = Σ_j û_j cos(k_j · x)           ← COSINE driven
**Vel. grad**: ∇u(x) = -Σ_j (û_j ⊗ k_j) sin(k_j · x) ← SINE driven
**Strain**:    S(x) = -Σ_j sym(û_j ⊗ k_j) sin(k_j · x) ← SINE driven

where û_j = (k_j × v_j)/|k_j|² (Biot-Savart on T³).

## THE CONSEQUENCE AT LATTICE POINTS

At lattice points x ∈ {0, π}³ (for integer k-vectors):
- cos(k_j · x) = ±1 for all j (since k_j · x ∈ πZ)
- sin(k_j · x) = 0 for all j

Therefore: **S(x) = 0** and **|∇u(x)| = 0** at ALL lattice points.
→ S²ê = 0 < 3|ω|²/4 trivially. KEY LEMMA HOLDS AT LATTICE POINTS.

## THE QUESTION: IS THE MAX OF |ω|² AT A LATTICE POINT?

|ω(x)|² = Σ a_j² cos²(k_j·x) + 2Σ_{j<k} D_{jk} cos(k_j·x) cos(k_k·x)

This is a pure cosine trigonometric polynomial (even function of x).
For integer k-vectors: it has Fourier frequencies with integer components.

### N ≤ 3 independent modes (PROVEN)
The map x ↦ (cos(k_1·x), cos(k_2·x), cos(k_3·x)) is surjective onto [-1,1]³
(when k_1, k_2, k_3 are linearly independent over R, which they are for
any 3 non-coplanar K-shell vectors).

|ω|² is a PSD quadratic form in (c_1, c_2, c_3). Each c_j² coefficient
is a_j² > 0, so |ω|² is CONVEX in each variable separately.
→ Max on [-1,1]³ is at a VERTEX (all c_j = ±1).
→ This IS a lattice point x ∈ {0,π}³.
→ S = 0 at the max. KEY LEMMA HOLDS. ∎

### N ≥ 4 modes (OPEN)
The cosines are constrained: c_4 = cos(α·φ) where φ = (k_1·x, k_2·x, k_3·x).
The 4th cosine is NOT independent — determined by the first 3 phases.

The max of |ω|² might NOT be at a lattice point.

## COUNTEREXAMPLE TO "MAX AT LATTICE"

f(x) = cos(x_1) + cos(x_2) - cos(x_1+x_2)

Lattice max: f(0,0) = 1+1-1 = 1, f(0,π) = 1-1+1 = 1, etc. Max = 1.
Interior max: at x_1 = x_2 = π/3: f = 1/2 + 1/2 - (-1/2) = 3/2 > 1.

**The max of a pure cosine function is NOT always at a lattice point.**

However: this is for a NON-PSD quadratic form (the -cos(x_1+x_2) term makes
the effective matrix indefinite). For |ω|² which IS PSD: the situation is different.

## PSD STRUCTURE OF |ω|²

|ω|² = |V(x)|² where V(x) = Σ a_j v̂_j cos(k_j·x) ∈ R³.

This is the square of the L² norm of a vector. The "Gram matrix" is:
M_{jk} = a_j a_k (v̂_j · v̂_k) = D_{jk} (PSD, rank ≤ 3)

|ω|² = Σ M_{jk} c_j c_k where c_j = cos(k_j·x).

If the c_j were independent on [-1,1]^N: the max of a PSD form on a box
is at a vertex (each c_j² coefficient = a_j² > 0, convex in each variable).

But the c_j are constrained to a 3-dimensional manifold in [-1,1]^N.
On a constrained manifold: the max of a PSD form might NOT be at a vertex.

## THE PHASE MISMATCH BOUND (for general max)

Even when the max is NOT at a lattice point: the PHASE MISMATCH helps.

At x*: let c_j = cos(k_j·x*), s_j = sin(k_j·x*). Then c_j² + s_j² = 1.

|ω(x*)|² = |Σ a_j v̂_j c_j|² (cosine contributions)
|S(x*)|² = |Σ S_j s_j|²_F (sine contributions)

where |S_j|²_F = a_j²/2 (per-mode).

At the max of |ω|²: the cosines conspire CONSTRUCTIVELY. This means
the c_j are "large" (close to ±1). Therefore the s_j are "small"
(s_j² = 1 - c_j²).

Quantitatively: at the max, the effective "cosine energy"
E_c = Σ a_j² c_j² is large and the "sine energy"
E_s = Σ a_j² s_j² = Σ a_j² - E_c is small.

|S|² ≤ Σ |S_j|² + cross terms ≈ E_s/2 + cross terms

The phase mismatch means: when E_c is maximized (at the ω-max),
E_s is minimized. The strain can't be large when vorticity is large.

## THE FORMAL BOUND (attempt)

|S|² = |ω|²/2 - 2C (Frobenius identity, file 511)

Need: C > -5|ω|²/16 at the max.

Alternative route: prove |S|² < (9/8)|ω|² directly.

|S|² = Σ (a_j²/2) s_j² + 2Σ_{j<k} Tr(S_j S_k) s_j s_k

Using s_j² = 1 - c_j²:
= Σ (a_j²/2)(1-c_j²) + cross terms
= Σ a_j²/2 - Σ a_j² c_j²/2 + cross terms

And |ω|² = Σ a_j² c_j² + 2Σ D_{jk} c_j c_k

So: |S|² + |ω|²/2 = Σ a_j²/2 + cross terms (in sines) + Σ a_j² c_j²/2 + Σ D c·c

Hmm this gets messy. The cross terms in the strain involve s_j s_k
and the identity from 511 handles this exactly.

## STATUS

- N ≤ 3 on single shell: KEY LEMMA PROVEN (max at lattice, S = 0)
- N ≥ 4: max might not be at lattice, need bound on |S|²/|ω|² at max
- The phase mismatch provides the MECHANISM but not yet a proof
- The Frobenius identity (511) is the right tool: need C > -5|ω|²/16

## 513. Phase mismatch: S ~ sin, ω ~ cos. At lattice points: S = 0.
## For N ≤ 3 independent modes on single shell: KEY LEMMA PROVEN.
## For N ≥ 4: max might leave lattice. Phase mismatch helps but doesn't close.
