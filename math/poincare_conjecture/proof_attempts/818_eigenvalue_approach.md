---
source: EIGENVALUE APPROACH — bounding f(N) via strain eigenvalue constraints
type: PROOF ATTEMPT — using trace-free + determinant to bound f(N)
file: 818
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE APPROACH

Instead of bounding S²ê directly, bound the EIGENVALUES of S at the argmax.

The strain S is a 3×3 symmetric trace-free matrix with eigenvalues λ₁ ≥ λ₂ ≥ λ₃.
Constraints: λ₁ + λ₂ + λ₃ = 0, S²ê ≤ λ₁² (max eigenvalue squared).

From |S|²_F = λ₁² + λ₂² + λ₃² = |ω|²/2 - 2C:
The eigenvalues satisfy λ₁² + λ₂² + λ₃² = |ω|²/2 - 2C.

With trace-free: λ₃ = -(λ₁+λ₂). So:
λ₁² + λ₂² + (λ₁+λ₂)² = 2(λ₁²+λ₁λ₂+λ₂²) = |ω|²/2 - 2C.

The maximum eigenvalue: λ₁² ≤ (2/3)(λ₁²+λ₂²+λ₃²) = (2/3)(|ω|²/2-2C)
(from the trace-free constraint, maximum fraction is 2/3).

So: α² ≤ S²ê ≤ λ₁² ≤ (2/3)(|ω|²/2-2C) = |ω|²/3 - 4C/3.

For the Key Lemma: need λ₁² < (3/4)|ω|², which requires:
|ω|²/3 - 4C/3 < (3/4)|ω|²
-4C/3 < (3/4 - 1/3)|ω|² = (5/12)|ω|²
C > -(5/16)|ω|²

This is the Key Lemma in terms of C: C > -5|ω|²/16.

## THE DETERMINANT CONSTRAINT

The trace-free constraint gives: λ₃ = -(λ₁+λ₂).
The determinant: det(S) = λ₁λ₂λ₃ = -λ₁λ₂(λ₁+λ₂).

For |S|² fixed: det(S) is bounded by the AM-GM type inequality.

But det(S) also has a PHYSICAL meaning: it's related to the topology
of the strain field. For NS, det(S) = -(1/3)tr(S³) involves the
third-order statistics of the velocity gradient.

## THE NEW IDEA: EIGENVALUE SPLITTING

At the argmax with N modes: S = Σ S_j (sum of rank-2 matrices).

Each S_j = (s_j/2)(p_j⊗k_j + k_j⊗p_j) has rank 2 with eigenvalues
+|k_j|/2, -|k_j|/2, 0 (since Tr(S_j) = 0 and |S_j|² = |k_j|²/2).

Wait: S_j has eigenvalues ±|k_j|/2 and 0? Let me check.

S_j = (1/2)(p_j⊗k_j + k_j⊗p_j). Eigenvalues:
- In the span(p_j, k_j): the 2×2 block is (1/2)[[0, p·k], [p·k, 0]] = 0
  (since p_j ⊥ k_j). Wait, that gives eigenvalues ±(1/2)|p_j||k_j|cosθ = 0.

No! p_j ⊥ k_j, so p_j·k_j = 0. The 2×2 block in span(p_j, k_j) is:
(1/2)[[2p_j·p_j, p_j·k_j+k_j·p_j], [k_j·p_j+p_j·k_j, 2k_j·k_j]]
... I'm confusing myself. Let me just compute S_j·v for v = p_j and v = k_j.

S_j·p_j = (1/2)(p_j(k_j·p_j) + k_j|p_j|²) = (1/2)(0 + k_j) = k_j/2
S_j·k_j = (1/2)(p_j|k_j|² + k_j(p_j·k_j)) = (1/2)(|k_j|²p_j + 0) = |k_j|²p_j/2

So S_j maps p_j → k_j/2 and k_j → |k_j|²p_j/2. In the basis {p_j, k_j/|k_j|}:

S_j = (|k_j|/2) [[0, 1], [1, 0]] (in the {p_j, k̂_j} subspace)

Eigenvalues: ±|k_j|/2, with eigenvectors (p_j ± k̂_j)/√2.
Third eigenvalue: 0 (perpendicular to span(p_j, k_j)).

So each S_j has eigenvalues +|k_j|/2, -|k_j|/2, 0. ✓

## THE SUM OF RANK-2 MATRICES

S = Σ S_j is a sum of N rank-2 matrices, each with eigenvalues ±|k_j|/2.

The eigenvalues of S are constrained by the Weyl inequalities:
λ_max(S) ≤ Σ λ_max(S_j) = Σ |k_j|/2

And λ_min(S) ≥ Σ λ_min(S_j) = -Σ |k_j|/2

But these are trivial bounds (|S| ≤ Σ|S_j|).

## TIGHTER BOUND: CANCELLATION IN THE SUM

For two matrices S₁, S₂ with eigenvectors in DIFFERENT directions:
the eigenvalues of S₁+S₂ are SMALLER than |λ_max(S₁)| + |λ_max(S₂)|
due to directional mismatch.

For N matrices with eigenvectors spanning R³:
λ_max(S) ≤ C√(Σ|S_j|²) = C√(Σ|k_j|²/2) (random matrix bound)

By the matrix Chernoff/Bernstein inequality:
λ_max(Σ S_j) ≤ max_j ||S_j|| · √(2 ln(3) · N) (for independent random matrices)

But our S_j are NOT random — they're adversarially chosen.

For the WORST case: all S_j have eigenvectors aligned → λ_max = Σ|k_j|/2.
This requires all (p_j, k_j) pairs to span the SAME 2D subspace.

For N ≥ 4: can't have all (p_j, k_j) in the same plane (since k_j are
distinct integer vectors and p_j ⊥ k_j). So some eigenvector spread is forced.

## THE FORCED SPREAD FOR N ≥ 4

Each S_j has eigenvectors in span(p_j, k̂_j). For all S_j to have the
SAME principal eigenvector: need all p_j + k̂_j to be parallel (up to sign).

Since p_j ⊥ k_j: the eigenvector (p_j + k̂_j)/√2 lies on the unit sphere.
For different k_j: the k̂_j are in different directions. For p_j + k̂_j
to be parallel: p_j must compensate for the change in k̂_j.

For two modes with k₁ ⊥ k₂: p₁ + k̂₁ ∥ p₂ + k̂₂ requires:
p₁ - p₂ ∥ k̂₂ - k̂₁. Since p₁ ⊥ k₁ and p₂ ⊥ k₂: this constrains p₁, p₂.

For THREE modes with mutually orthogonal k-vectors:
p_j + k̂_j all parallel → three vectors in R³ must be parallel.
With k̂₁, k̂₂, k̂₃ orthogonal: p₁+k̂₁ = c(p₂+k̂₂) = c'(p₃+k̂₃).
This gives: p₁ = c·p₂ + (c·k̂₂ - k̂₁) and p₁ ⊥ k₁. Very constrained.

In general: for N ≥ 4 modes with distinct k-vectors, perfect eigenvector
alignment is IMPOSSIBLE. The maximum eigenvalue satisfies:

λ₁(S) ≤ Σ|k_j|/2 - δ(N)

where δ(N) > 0 grows with N (the forced spread reduces λ₁).

## THE BOUND ON f(N) FROM EIGENVALUE SPREAD

S²ê ≤ λ₁² ≤ (Σ|k_j|/2 - δ(N))²

For |ω|² ≥ N: S²ê/|ω|² ≤ (Σ|k_j|/2)²/N - correction.

With Σ|k_j| ≤ N·K (max wavenumber): S²ê/|ω|² ≤ N²K²/4N - ... = NK²/4 - ...

This is still O(N), which is TOO LARGE for the Key Lemma when N > 3.

But the trace-free bound gives a TIGHTER constraint:
S²ê ≤ (2/3)|S|² = (2/3)(|ω|²/2-2C)

The KEY LEMMA uses this, not the direct eigenvalue bound.

## CONCLUSION

The eigenvalue approach gives bounds on λ₁(S) but they're too loose
for the floor growth. The trace-free bound S²ê ≤ (2/3)|S|² is tighter
because it uses the constraint Tr(S)=0, not just eigenvalue inequalities.

The floor growth f(N) → 0 requires |S|²/|ω|² → 0, which is a statement
about the TOTAL strain magnitude, not just the maximum eigenvalue.

The total strain |S|² = |ω|²/2 - 2C depends on the cross-term C.
The floor growth requires C → |ω|²/4 (positive cross-terms dominate).

The eigenvalue approach doesn't directly help with this.

## 818. Eigenvalue approach: each S_j has eigenvalues ±|k_j|/2.
## Sum: λ_max(S) ≤ Σ|k_j|/2 - δ(N) from forced spread.
## But this doesn't bound |S|²/|ω|² → 0 (the floor growth).
## The floor growth is about TOTAL strain, not max eigenvalue.
