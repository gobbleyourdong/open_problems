---
source: Instance B — the geometric constraint for N≥3 modes
type: PROOF SKETCH for S²ê ≤ C|ω|² with C < 3/4
file: 335
date: 2026-03-29
---

## The N=2 Result (file 363, PROVEN)

S²ê ≤ |ω|²/4 at the max for any 2-mode div-free field.
Equality when: a₁ = a₂, v̂₁ ⊥ v̂₂, common max (c₁ = c₂ = 1).

At equality: |ω|² = a₁² + a₂² = 2a². S²ê = a⁴(1-0)/a² × 1/4 ... wait.
From file 363: S²ê = a₁²a₂²(1-d²)/|ω|² (Case 1).
At a₁=a₂=a, d=0: S²ê = a⁴/(2a²) = a²/2 = |ω|²/4. ✓

## Why N≥3 Should Be Strictly Better

For N=2 at equality: s₁ ∥ s₂ (both in the same 2D plane in ⊥ê space).
For N=3: s₃ is in span{k₃, k₃×v̂₃}. If k₃ is NOT coplanar with k₁,k₂:
then span{k₃, w₃} ≠ span{k₁, w₁} ≠ span{k₂, w₂}.

The three s_k vectors live in different 2D subspaces of the 2D ⊥ê plane.
Wait — the ⊥ê plane IS 2D. So any vector in ⊥ê is in this 2D plane.
The constraint s_k ∈ span{k, k×v̂_k} projected onto ⊥ê gives a 1D
direction for each k (or 2D if both k and w have components in ⊥ê).

Hmm, let me reconsider.

## The ⊥ê plane structure

Each s_k = -(c_k/(2|k|²))[(ê·k)w_k + (ê·w_k)k] lives in R³.

But S·ê = Σs_k is a 3-vector. S²ê = |Σs_k|².

The s_k are NOT restricted to ⊥ê. They have components along ê too!
Actually: from the identity |S·ê|² = S²ê, the vector S·ê has:
(S·ê)·ê = α (along ê)
|(S·ê)_⊥|² = S²ê - α² = Var (perpendicular)

The full |S·ê|² = α² + Var = S²ê.

For the barrier: need S²ê < 3|ω|²/4.

## The Key for N≥3: Angular Diversity

For N=2 at the TIGHT configuration: both s_k project maximally into
the SAME direction in ⊥ê. They add constructively.

For N≥3: the k-vectors span 3D (generically). The projections of
different s_k onto the ⊥ê plane point in DIFFERENT directions.
They add with PARTIAL cancellation.

The cancellation factor: from the angular diversity of k on Z³.

For N modes with uniformly distributed k-directions:
|Σs_k|² ≈ N × |s_typ|² (no constructive interference).
vs (Σ|s_k|)² = N² × |s_typ|² (full constructive).

Ratio: 1/N (destructive) vs 1 (constructive). For large N: massive reduction.

## The Formal Argument (sketch)

CLAIM: For N ≥ 3 modes with non-coplanar k-vectors on Z³:
S²ê(x*) ≤ (1 - η)|ω(x*)|²/4 for some η > 0 depending on the
geometry of the k-configuration.

PROOF SKETCH: The N=2 tight bound uses s₁ ∥ s₂ (both in the same
direction in ⊥ê). For N=3 with non-coplanar k₃:

|Σs_k|² = |s₁+s₂+s₃|² = |s₁+s₂|² + |s₃|² + 2(s₁+s₂)·s₃

From N=2: |s₁+s₂| ≤ √(S²ê_{1,2}) ≤ |ω₁₂|/2 where ω₁₂ is the
two-mode vorticity. And |s₃| ≤ a₃/2 (per-mode bound).

The cross-term: 2(s₁+s₂)·s₃. This has DEFINITE SIGN only when
(s₁+s₂) and s₃ are aligned. For non-coplanar k₃: s₃ makes an
angle with (s₁+s₂) that depends on the geometry. The cross-term
is bounded by 2|s₁+s₂||s₃|cos(angle), which is < 2|s₁+s₂||s₃|
when angle ≠ 0.

For the TIGHT bound: need angle = 0 (full constructive). But for
non-coplanar k: this is IMPOSSIBLE because the 2D subspaces of
s₁+s₂ and s₃ are different.

## WHAT'S NEEDED TO FORMALIZE

The proof that angle ≠ 0 for non-coplanar k requires:

1. s₁+s₂ lies in span{k₁,w₁,k₂,w₂} (a 4D space generically).
   Projected onto ⊥ê: at most 2D.

2. s₃ lies in span{k₃,w₃} (a 2D space).
   Projected onto ⊥ê: at most 1D (a specific direction).

3. For the s₃-direction to coincide with the s₁+s₂ direction:
   span{k₃,w₃} must intersect the s₁+s₂ direction in ⊥ê.
   This is codimension ≥ 1 (a non-generic condition).

For GENERIC k₃ (on Z³, most k₃ choices): the angle is nonzero.
The reduction factor η depends on the MINIMUM angle over all k₃ ∈ Z³.

On Z³: the angles between different mode planes are QUANTIZED (discrete lattice).
The minimum nonzero angle is bounded below by ~ 1/max|k|.

For SMOOTH solutions (|ω̂_k| decaying as |k|^{-s}):
only finitely many modes with significant amplitude. The geometric
non-coplanarity gives η > 0.

## STATUS

The N≥3 geometric argument is PLAUSIBLE but not yet formal.
The key step: prove that on Z³, for 3+ non-coplanar k-vectors,
the mode strains s_k can't all be parallel in the ⊥ê plane.
This is a LATTICE GEOMETRY problem.

## 335.
