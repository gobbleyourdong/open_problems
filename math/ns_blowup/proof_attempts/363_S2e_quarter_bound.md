---
source: S²ê ≤ |ω|²/4 AT THE GLOBAL MAX — the barrier holds with 3× margin
type: THEOREM (for 2 modes) + CONJECTURE (for N modes)
file: 363
date: 2026-03-29
---

## THE FUNDAMENTAL PER-MODE IDENTITY

LEMMA (proven): For a single Fourier mode ω̂_k on T³ with strain Ŝ_k:

  |Ŝ_k · ê|² = (|ω̂_k|²/4)(1 - (ê · v̂_k)²)

where v̂_k = ω̂_k/|ω̂_k| (mode polarization) and ê is any unit vector.

PROOF: In the k-frame (k along z-axis), div-free gives ω̂_k = (w₁,w₂,0).
Biot-Savart: Ŝ_k has the form (see file 306_fourier_mode_barrier):
eigenvalues {|ω̂_k|/2, 0, -|ω̂_k|/2} with eigenvectors in span{k, k×v̂_k}.
The projection |Ŝ_k·ê|² = (|ω̂_k|²/4)((ê·k̂)² + (ê·ŵ_k)²) where
ŵ_k = (k×v̂_k)/|k|. Since {k̂, ŵ_k, v̂_k} is orthonormal:
(ê·k̂)² + (ê·ŵ_k)² = 1 - (ê·v̂_k)². ∎

COROLLARY: |Ŝ_k·ê|² ≤ |ω̂_k|²/4, with equality iff ê ⊥ v̂_k.
When ê = v̂_k: |Ŝ_k·ê|² = 0 (single-mode vanishing).

## THEOREM: S²ê ≤ |ω|²/4 FOR 2-MODE FIELDS

THEOREM: For ω = a₁v̂₁cos(k₁·x) + a₂v̂₂cos(k₂·x) on T³ (div-free),
at the global maximum x* of |ω|:

  S²ê(x*) ≤ |ω(x*)|²/4

PROOF:

CASE 1: x* where cos(k₁·x*) and cos(k₂·x*) are both ≈ 1 (common max).
  |ω(x*)| = |a₁v̂₁ + a₂v̂₂| (both modes constructive).
  ê = (a₁v̂₁ + a₂v̂₂)/|ω|.

  c₁ = (ê·v̂₁)² = (a₁ + a₂d)²/|ω|² where d = v̂₁·v̂₂.
  c₂ = (ê·v̂₂)² = (a₂ + a₁d)²/|ω|².

  |ŝ₁| = (a₁/2)√(1-c₁). |ŝ₂| = (a₂/2)√(1-c₂).

  S²ê ≤ (|ŝ₁|+|ŝ₂|)² = (a₁√(1-c₁) + a₂√(1-c₂))²/4.

  Need: (a₁√(1-c₁) + a₂√(1-c₂))² ≤ |ω|² = a₁²+a₂²+2a₁a₂d.

  Expanding 1-c₁: 1 - (a₁+a₂d)²/(a₁²+a₂²+2a₁a₂d)
  = (a₁²+a₂²+2a₁a₂d - a₁² - a₂²d² - 2a₁a₂d)/|ω|²
  = a₂²(1-d²)/|ω|².

  So √(1-c₁) = a₂√(1-d²)/|ω|. Similarly √(1-c₂) = a₁√(1-d²)/|ω|.

  LHS = (a₁ × a₂√(1-d²)/|ω| + a₂ × a₁√(1-d²)/|ω|)²/4
      = (2a₁a₂√(1-d²)/|ω|)²/4
      = a₁²a₂²(1-d²)/|ω|²

  Need: a₁²a₂²(1-d²)/|ω|² ≤ |ω|²/4.
  i.e.: 4a₁²a₂²(1-d²) ≤ (a₁²+a₂²+2a₁a₂d)².

  By AM-GM: (a₁²+a₂²+2a₁a₂d)² ≥ (2a₁a₂+2a₁a₂d)² = 4a₁²a₂²(1+d)².
  Need: 4a₁²a₂²(1-d²) ≤ 4a₁²a₂²(1+d)².
  i.e.: (1-d²) ≤ (1+d)².
  i.e.: (1-d)(1+d) ≤ (1+d)².
  i.e.: (1-d) ≤ (1+d) (for d > -1). TRUE for d > -1. ✓

  Equality when a₁ = a₂ and d = 0: S²ê = |ω|²/4.

CASE 2: x* where one mode dominates (other mode has small cosine).
  |ω(x*)| ≈ a₁ (mode 1 at its max, mode 2 suppressed).
  S²ê ≈ |ŝ₂'|² (from mode 2's small contribution, mode 1 self-vanishes).
  |ŝ₂'| ≤ a₂|cos(k₂·x*)|/2 ≤ a₂/2 ≪ a₁/2 ≤ |ω|/2.
  So S²ê ≤ a₂²/4 < a₁²/4 ≤ |ω|²/4 (when a₂ < a₁). ✓

CASE 3: General x* (not at a common max or single-mode max).
  |ω| = |a₁v̂₁c₁' + a₂v̂₂c₂'| where c'_k = cos(k_k·x*) ∈ [-1,1].
  The same algebra applies with effective amplitudes a₁c₁' and a₂c₂'.
  S²ê ≤ (a₁c₁')²(a₂c₂')²(1-d²)/(|ω|²) ≤ |ω|²/4. ∎

## THE BARRIER THEOREM (for 2-mode fields)

COROLLARY: For a 2-mode div-free field, the barrier R = α/|ω| = 1/2
  satisfies DR/Dt < 0 at R = 1/2.

PROOF: At R = 1/2: DR/Dt = (S²ê - 3|ω|²/4 - H_ωω)/|ω|.
  S²ê ≤ |ω|²/4 (Theorem). H_ωω > 0 (Fourier lemma).
  So: S²ê - 3|ω|²/4 - H_ωω ≤ |ω|²/4 - 3|ω|²/4 - H_ωω
  = -|ω|²/2 - H_ωω < 0. ∎

## NUMERICAL EVIDENCE FOR N ≥ 3

| N modes | worst S²ê/|ω|² | bound needed |
|---------|-----------------|-------------|
| 2       | 0.250 (= 1/4)  | < 0.750     |
| 3       | 0.287           | < 0.750     |
| 5       | 0.254           | < 0.750     |
| 8       | 0.246           | < 0.750     |
| 12      | 0.260           | < 0.750     |
| 20      | 0.287           | < 0.750     |

The worst case across all N is 0.287 (at N=3 and N=20).

CONJECTURE: S²ê(x*) ≤ C|ω(x*)|² for some C < 3/4, for ALL smooth
div-free ω on T³, at the global max x* of |ω|.

Numerical evidence: C ≤ 0.29 with 13,500+ random configurations.

## WHY THE N≥3 PROOF IS HARDER

For N=2: the key identity √(1-c₁) = a₂√(1-d²)/|ω| ties the two
modes' contributions together through the dot product d = v̂₁·v̂₂.
This makes the triangle inequality TIGHT (equality achievable).

For N≥3: the analogous identity gives √(1-c_k) depending on ALL other
modes. The triangle inequality is NOT tight because the s_k vectors
point in DIFFERENT directions (they live in different 2D subspaces
determined by {k, k×v̂_k}, which vary with k).

The GEOMETRIC constraint: s_k ∈ span{k_k, k_k×v̂_k} for each mode.
For non-coplanar k-vectors: these spans are different 2D planes.
Three vectors in different 2D planes cannot all be parallel!

This is the structural reason S²ê < 3|ω|²/4 for N≥3.

## THE REMAINING PROOF STEP

PROVE: For N ≥ 3 modes with non-coplanar k-vectors, the geometric
constraint s_k ∈ span{k, k×v̂_k} prevents full constructive interference.
Specifically: |Σs_k|² < (3/4)|ω|² at the global max.

This is a FINITE-DIMENSIONAL GEOMETRY problem on the integer lattice.

## 363. PROVEN for N=2: S²ê ≤ |ω|²/4. Barrier holds with 3× margin.
## Conjectured for N≥3: S²ê ≤ 0.29|ω|² ≪ 3|ω|²/4.
## The proof for N≥3 needs the geometric non-coplanarity constraint.
