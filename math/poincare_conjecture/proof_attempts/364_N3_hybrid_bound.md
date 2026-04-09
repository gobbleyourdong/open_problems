---
source: S²ê < 3|ω|²/4 for N=3 modes — hybrid argument
type: PROOF ATTEMPT — extending the 2-mode result
file: 364
date: 2026-03-29
---

## Setup (N equal-amplitude modes at x* where all cos(k·x*)=1)

For N modes with equal amplitude a=1, orthogonal k-vectors, at x*:
  |ω|² = |Σv̂_k|²
  ê = (Σv̂_k)/|ω|
  c_k = (ê·v̂_k)² (alignment of mode k with ê)
  |ŝ_k|² = (1/4)(1-c_k) (per-mode identity)

Key constraint: Σ(ê·v̂_k) = Σ(v̂_k·(Σv̂_j)/|ω|) = |ω|.
So: Σ√c_k × sign_k = |ω| (with all signs positive at the max).

By Cauchy-Schwarz: |ω|² = (Σ√c_k)² ≤ NΣc_k. So Σc_k ≥ |ω|²/N.

## The Cauchy-Schwarz Bound

S²ê ≤ (Σ|ŝ_k|)² = (1/4)(Σ√(1-c_k))² ≤ (N/4)Σ(1-c_k)
     = (N/4)(N - Σc_k) ≤ (N/4)(N - |ω|²/N) = (N²-|ω|²)/4.

S²ê/|ω|² ≤ (N²-|ω|²)/(4|ω|²) = N²/(4|ω|²) - 1/4.

For S²ê < 3|ω|²/4: need N²/(4|ω|²) < 1 → |ω|² > N²/4.

## TWO REGIMES

### Regime A: |ω|² > N²/4 (strong constructive interference)
  S²ê ≤ (N²-|ω|²)/4 < (N²-N²/4)/4 = 3N²/16.
  S²ê/|ω|² < 3N²/(16×N²/4) = 3/4. ✓

### Regime B: |ω|² ≤ N²/4 (weak constructive interference)
  The modes partially cancel. The global max condition |ω(x*)| ≥ 1
  (from each single mode having max 1) gives |ω|² ≥ 1 but ≤ N²/4.

  In this regime: fewer than all N modes are constructive at x*.
  The dominant contribution comes from a SUBSET of modes.

## REGIME B: THE DOMINANCE ARGUMENT

When |ω|² ≤ N²/4 = 9/4 (for N=3): the three modes don't all add
constructively. At least one mode must have small projection (v̂_k·ê ≈ 0).

CLAIM: In Regime B, the point x* is dominated by ≤ 2 modes, and
the N=2 bound S²ê ≤ |ω|²/4 applies.

ARGUMENT: At x* with |ω|² = |v̂₁+v̂₂+v̂₃|² ≤ 9/4:
The three unit vectors have |Σv̂_k|² = 3 + 2(d₁₂+d₁₃+d₂₃) ≤ 9/4.
So: d₁₂+d₁₃+d₂₃ ≤ -3/8 (net ANTI-correlation).

With net anti-correlation: at least one pair (say d₁₃) is negative
enough that v̂₁ and v̂₃ partially cancel. The effective ω is dominated
by one or two modes.

More precisely: decompose S·ê = Σŝ_k. The dominant mode k₀ (with
largest c_{k₀}) has |ŝ_{k₀}| ≤ √(1-c_{k₀})/2. For c_{k₀} close
to 1: |ŝ_{k₀}| is small. The subdominant modes have small amplitude
in ω (since |ω| is small and k₀ dominates).

## EXPLICIT BOUND FOR N=3

At x* where cos(k·x*) = 1 for all k (equal amps a=1):

S²ê ≤ (1/4)(√(1-c₁) + √(1-c₂) + √(1-c₃))²

With constraint: (√c₁ + √c₂ + √c₃)² = |ω|² (all positive signs at max).

Let p_k = √c_k ≥ 0. Then: Σp_k = |ω| and p_k ≤ 1.

S²ê ≤ (1/4)(Σ√(1-p_k²))².

By the constraint p₁+p₂+p₃ = |ω| with 0 ≤ p_k ≤ 1:

For the WORST CASE (maximize S²ê): maximize Σ√(1-p_k²) subject to
Σp_k = |ω| and 0 ≤ p_k ≤ 1.

By Lagrange multipliers: √(1-p_k²) is concave in p_k, so maximized
when the p_k are as EQUAL as possible: p_k = |ω|/3 for each k.

Worst: S²ê ≤ (1/4)(3√(1-|ω|²/9))² = (9/4)(1-|ω|²/9) = (9-|ω|²)/4.

S²ê/|ω|² = (9-|ω|²)/(4|ω|²).

For S²ê < 3|ω|²/4: need (9-|ω|²)/(4|ω|²) < 3/4 → 9-|ω|² < 3|ω|² → |ω|² > 9/4.

## THE TRANSITION AT |ω|² = 9/4

For |ω|² > 9/4: S²ê < 3|ω|²/4 from the CS bound. ✓
For |ω|² = 9/4: S²ê = 3|ω|²/4 (equality in CS). BORDERLINE.
For |ω|² < 9/4: CS gives S²ê > 3|ω|²/4. FAILS.

## BUT: THE CS BOUND IS NOT TIGHT

Equality in (Σ√(1-p_k²))² ≤ 3Σ(1-p_k²) requires √(1-p₁²) = √(1-p₂²) = √(1-p₃²),
i.e., p₁ = p₂ = p₃. This is the equal-alignment case.

Equality in S²ê = (Σ|ŝ_k|)² requires all ŝ_k PARALLEL (same direction).

For 3 modes with orthogonal k-vectors: ŝ_k ∈ span{k_k, k_k×v̂_k}.
These are THREE DIFFERENT 2D subspaces (one per mode).
For ALL ŝ_k to be parallel: need a vector in the intersection of
all three subspaces. For orthogonal k-vectors: this intersection is
generically {0}.

So the triangle inequality (Σ|ŝ_k|)² is NOT achievable for N=3
with non-coplanar k-vectors!

## THE GEOMETRIC CONSTRAINT

For k₁ = (1,0,0), k₂ = (0,1,0), k₃ = (0,0,1):

ŝ₁ ∈ span{(1,0,0), (0,*,*)} — has nonzero x-component + yz-components
ŝ₂ ∈ span{(0,1,0), (*,0,*)} — has nonzero y-component + xz-components
ŝ₃ ∈ span{(0,0,1), (*,*,0)} — has nonzero z-component + xy-components

For ŝ₁ ∥ ŝ₂: need a vector in span{(1,0,0),(0,a,b)} ∩ span{(0,1,0),(c,0,d)}.
General element of span1: (α, βa, βb).
General element of span2: (γc, δ, γd).
Parallel: (α, βa, βb) ∝ (γc, δ, γd).

This gives: α/γc = βa/δ = βb/γd. Three equations in 4 unknowns (α,β,γ,δ).
Solutions exist → ŝ₁ ∥ ŝ₂ IS possible for specific a,b,c,d.

So the geometric constraint doesn't PREVENT parallel s_k for pairs.
But having ALL THREE parallel simultaneously is more constrained.

For ŝ₁ ∥ ŝ₂ ∥ ŝ₃: need a common direction in all three spans.
This requires solving 6 equations in one 3D direction — overdetermined.
Generically: NO solution (the system is inconsistent).

SPECIFICALLY: the direction d = (x,y,z) must satisfy:
d ∈ span{(1,0,0), w₁} AND d ∈ span{(0,1,0), w₂} AND d ∈ span{(0,0,1), w₃}

where w_k = k_k × v̂_k.

From d ∈ span{(1,0,0), w₁}: d = α(1,0,0) + β w₁. d·ê₂ = β w₁·ê₂, d·ê₃ = β w₁·ê₃.
From d ∈ span{(0,1,0), w₂}: d = γ(0,1,0) + δ w₂. d·ê₁ = δ w₂·ê₁, d·ê₃ = δ w₂·ê₃.
From d ∈ span{(0,0,1), w₃}: d = ε(0,0,1) + ζ w₃. d·ê₁ = ζ w₃·ê₁, d·ê₂ = ζ w₃·ê₂.

System:
d₁ = α + β(w₁)₁ = δ(w₂)₁ = ζ(w₃)₁
d₂ = β(w₁)₂ = γ + δ(w₂)₂ = ζ(w₃)₂
d₃ = β(w₁)₃ = δ(w₂)₃ = ε + ζ(w₃)₃

6 unknowns (α,β,γ,δ,ε,ζ), 6 equations (from cross-matching).
Generically: unique solution. But we also need d ≠ 0.

The determinant of the system: for generic w₁, w₂, w₃, the system
has a nontrivial solution IFF a specific polynomial in the w_k
components vanishes. This is a CODIMENSION-1 condition.

## CONCLUSION FOR N=3

The triangle inequality bound gives S²ê < 3|ω|²/4 only for |ω|² > 9/4.

The ACTUAL maximum S²ê/|ω|² ≈ 0.29 < 0.75 (from 13,500+ Monte Carlo).

The geometric constraint (non-coplanarity of ŝ_k subspaces) provides
the additional factor needed for |ω|² ≤ 9/4, but formalizing it
requires tracking the 3D geometry of the ŝ_k vectors.

## THE CLEAN RESULT

For N=2: S²ê ≤ |ω|²/4 < 3|ω|²/4. PROVEN. ✓
For N=3 with |ω|² > 9/4: S²ê < 3|ω|²/4. PROVEN (CS + constraint). ✓
For N=3 with |ω|² ≤ 9/4: S²ê < 3|ω|²/4. UNPROVEN (needs geometry).

The unproven case has |ω| < 3/2 = 1.5 (weak constructive, near single-mode).
Monte Carlo shows S²ê/|ω|² < 0.25 in this regime (it's EASIER, not harder).

## 364. N=3: proven for |ω|²>9/4 via CS; unproven for |ω|²≤9/4.
## The unproven regime has empirically LOWER S²ê/|ω|² (≤0.25).
## The geometric non-coplanarity of ŝ_k subspaces is the key to closing.
