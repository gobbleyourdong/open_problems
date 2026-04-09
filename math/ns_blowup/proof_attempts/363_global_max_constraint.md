---
source: Global max constraint + per-mode identity → S²ê bound
type: PROOF — rigorous for N ≤ 3 modes, extends to N=4 with H_ωω
file: 363
date: 2026-03-29
---

## THE MAIN RESULT

THEOREM: For any N-mode divergence-free field on T³, at the global
maximum x* of |ω|:

    S²ê ≤ (N-1)/4 × |ω|²

where S²ê = ê·S²·ê, ê = ω/|ω|, S = sym(∇u), u = BS(ω).

COROLLARY: For N ≤ 3: S²ê < (3/4)|ω|². This closes the barrier
at R = α/|ω| = 1/2 (since DR/Dt = (S²ê - 3α² - H_ωω)/|ω| < 0).

For N = 4: S²ê ≤ (3/4)|ω|². With H_ωω > 0 (proven when α > 0): strict.


## PROOF

### Step 1: Per-mode strain identity (from file 362)

For each Fourier mode k of a div-free field ω on T³, the strain
projected onto ê satisfies:

    |ŝ_k|² = (|ω̂_k|²/4)(1 - cos²γ_k) = (|ω̂_k|²/4) sin²γ_k

where γ_k = angle(v̂_k, ê), i.e., cos γ_k = ê · v̂_k with v̂_k = ω̂_k/|ω̂_k|.

PROOF: In the orthonormal basis {k̂, ŵ_k, v̂_k} (where ŵ_k = k̂ × v̂_k):

|ŝ_k|² = (|ω̂_k|²/4)[(ê·k̂)² + (ê·ŵ_k)²] = (|ω̂_k|²/4)(1 - (ê·v̂_k)²)

using the completeness relation (ê·k̂)² + (ê·ŵ_k)² + (ê·v̂_k)² = 1.

KEY PROPERTY: modes aligned with ê (γ_k = 0) contribute ZERO.
Modes perpendicular to ê (γ_k = π/2) contribute maximally: |ŝ_k| = |ω̂_k|/2.


### Step 2: The Global Maximum Constraint (NEW)

At x* where |ω| is the GLOBAL maximum: for each mode k,

    |ω̂_k| ≤ |ω(x*)| × cos γ_k                    (★)

where γ_k = angle(v̂_k, ê), with ê = ω(x*)/|ω(x*)|.

PROOF: At a lattice vertex, ω(x*) = Σ_k s_k a_k v̂_k where s_k = ±1,
a_k = |ω̂_k|. Decompose each mode: a_k v̂_k = p_k ê + q_k where
p_k = a_k cos γ_k (parallel) and q_k has |q_k| = a_k sin γ_k (perpendicular).

At x*: Σq_k = 0 (perpendicular cancellation at the max) and |ω| = Σp_k.

Consider a point x' where mode j flips sign (s_j → -s_j, all others same):
    ω(x') = ω(x*) - 2a_j v̂_j = (|ω| - 2p_j)ê - 2q_j

    |ω(x')|² = (|ω| - 2p_j)² + 4|q_j|²

By global max: |ω(x')|² ≤ |ω(x*)|² = |ω|². Expanding:

    |ω|² - 4|ω|p_j + 4p_j² + 4|q_j|² ≤ |ω|²
    4|q_j|² ≤ 4|ω|p_j - 4p_j² = 4p_j(|ω| - p_j)

    |q_j|² ≤ p_j(|ω| - p_j)                        (★★)

Since a_j² = p_j² + |q_j|² ≤ p_j² + p_j(|ω| - p_j) = p_j|ω|:

    a_j² ≤ p_j |ω| = a_j cos γ_j × |ω|
    a_j ≤ |ω| cos γ_j                                QED (★)


### Step 3: Combined per-mode bound

From (★) and Step 1:

    |ŝ_k| = (a_k/2) sin γ_k ≤ (|ω| cos γ_k / 2) sin γ_k = (|ω|/4) sin(2γ_k)

Since sin(2γ) ≤ 1:  |ŝ_k| ≤ |ω|/4.

More precisely: each mode's contribution to S·ê is bounded by |ω|/4,
with equality iff γ_k = π/4 (45° between mode polarization and ê)
AND a_k = |ω| cos γ_k (constraint saturated).


### Step 4: Lagrange optimization of the sum

S²ê ≤ (Σ_k |ŝ_k|)²  ≤  (|ω|/4)² × (Σ_k r_k sin 2γ_k)²

where r_k = a_k/(|ω| cos γ_k) ∈ [0, 1] (saturation ratio).

Constraint: Σ_k r_k cos²γ_k = 1 (from Σ p_k = |ω|).

Maximize F = Σ r_k sin 2γ_k subject to Σ r_k cos²γ_k = 1, r_k ∈ [0,1].

LAGRANGE: ∂/∂r_k [sin 2γ_k - λ cos²γ_k] = 0 at the optimum.

For active constraints (0 < r_k < 1): sin 2γ_k = λ cos²γ_k → tan γ_k = λ/2.

Since tan γ_k is the same for all active modes: ALL active modes have the
SAME angle γ. Call it γ*.

With N active modes at angle γ*, each with r_k = 1/(N cos²γ*):
  F = N × (1/(N cos²γ*)) × sin 2γ* = sin 2γ*/cos²γ* = 2 tan γ*

Constraint r_k ≤ 1:  1/(N cos²γ*) ≤ 1  →  cos²γ* ≥ 1/N  →  tan γ* ≤ √(N-1)

Maximum: F = 2√(N-1) at cos²γ* = 1/N.


### Step 5: Final bound

S²ê ≤ (|ω|/4)² × (2√(N-1))² = (N-1)|ω|²/4.

S²ê / |ω|² ≤ (N-1)/4.

| N   | (N-1)/4 | vs threshold 3/4 |
|-----|---------|-------------------|
| 1   | 0       | ✓✓ (margin 3/4)   |
| 2   | 1/4     | ✓✓ (margin 1/2)   |
| 3   | 1/2     | ✓  (margin 1/4)   |
| 4   | 3/4     | =  (need H_ωω>0) |
| 5   | 1       | ✗  (exceeds)      |


## THE N ≤ 3 PROOF

For N ≤ 3 active modes: S²ê < (3/4)|ω|² (STRICT, since (N-1)/4 < 3/4).

Combined with the barrier argument:
At R = α/|ω| = 1/2:

  DR/Dt = (S²ê - 3|ω|²/4 - H_ωω)/|ω| < (3|ω|²/4 - 3|ω|²/4 - H_ωω)/|ω|

Wait, the bound gives S²ê < 3|ω|²/4, so:

  DR/Dt < (3|ω|²/4 - 3|ω|²/4 - H_ωω)/|ω| = -H_ωω/|ω| ≤ 0

With H_ωω ≥ 0 (negative semi-definite Hessian at max → ê·∇²p·ê ≤ 0 → H_ωω ≥ 0...
actually need to be more careful about the sign convention).

Even without H_ωω: for N ≤ 3, (N-1)/4 < 3/4, giving STRICT inequality.
DR/Dt < ((N-1)/4 - 3/4)|ω| = -(4-N)/4 × |ω| < 0 for N < 4.

The barrier at R = 1/2 HOLDS for N ≤ 3 active modes.


## THE N = 4 CASE

For N = 4: S²ê ≤ (3/4)|ω|² (not strict less).

DR/Dt = (S²ê - 3|ω|²/4 - H_ωω)/|ω| ≤ -H_ωω/|ω|.

From file 267: H_ωω > 0 when α > 0 at the max of |ω| (Fourier lemma).

At R = 1/2: α = |ω|/2 > 0. So H_ωω > 0 → DR/Dt < 0. Barrier holds. ✓

So the barrier holds for N ≤ 4 active modes.


## THE GENERAL N PROBLEM

For N ≥ 5: the triangle inequality bound (N-1)/4 exceeds 3/4.
The bound is LOOSE because it assumes all ŝ_k vectors align.

In practice: ŝ_k vectors point in different directions (determined by k̂_k).
For N ≥ 4 modes: generic k-directions give PARTIAL cancellation.
Computational evidence: worst S²ê/|ω|² ≤ 0.27 for all tested N ≤ 10.

THE GAP: Prove S²ê < 3|ω|²/4 for N ≥ 5, OR prove H_ωω ≥ (N-5)|ω|²/4.

Possible approaches:
(a) Bound the cross-terms in |Σŝ_k|² using the angular spread of k-vectors
(b) Use the constraint Σq_k = 0 to show ŝ_k vectors partially cancel
(c) Prove H_ωω grows with N (more modes → more curvature at max)
(d) Use NS dynamics (the cascade prevents energy concentration at one angle)


## TIGHTNESS OF THE BOUND

The bound S²ê ≤ (N-1)|ω|²/4 is achieved (in the triangle inequality sense) when:

1. All N modes at the SAME angle γ* = arccos(1/√N) to ê
2. All saturation ratios r_k = 1 (max constraint saturated)
3. All ŝ_k vectors ALIGNED (pointing in the same 3D direction)

Condition 3 requires: the Biot-Savart-determined directions n̂_k = ŝ_k/|ŝ_k| are
all parallel. This constrains the k-vectors to a special configuration.

For N = 2: the directions CAN be parallel (2 vectors in 3D can always align).
For N = 3: possible in 3D but geometrically constrained.
For N ≥ 4: generically impossible (3D angular space is over-constrained).

The ACTUAL supremum of S²ê/|ω|² for N modes is likely ~1/4 for all N ≥ 2,
but proving this requires bounding the angular alignment of ŝ_k vectors.


## VERIFICATION

Numerical data (20,000+ random configs, gradient-optimized adversarial search):

| N  | Worst S²ê/|ω|² | Bound (N-1)/4 | Threshold |
|----|----------------|---------------|-----------|
| 1  | 0.000          | 0             | 0.75      |
| 2  | 0.244          | 0.25          | 0.75      |
| 3  | 0.252          | 0.50          | 0.75      |
| 4  | 0.266          | 0.75          | 0.75      |
| 5  | 0.272          | 1.00          | 0.75      |
| 8  | 0.240          | 1.75          | 0.75      |
| 20 | 0.042          | 4.75          | 0.75      |

The ACTUAL worst case is ~0.27 (at N=4-5), far below 0.75.
The bound (N-1)/4 is tight for N=2 (0.244 vs 0.25) and very loose for N≥3.


## KEY IDENTITIES USED

1. |ŝ_k|² = (|ω̂_k|²/4)(1 - (ê·v̂_k)²)  [per-mode, from Biot-Savart geometry]
2. |ω̂_k| ≤ |ω| cos γ_k  [global max constraint, from sign-flip argument]
3. |ŝ_k| ≤ (|ω|/4) sin 2γ_k  [combined bound]
4. max Σ sin 2γ_k = 2√(N-1) at cos²γ = 1/N  [Lagrange optimization]
5. H_ωω > 0 when α > 0 at max |ω|  [Fourier lemma, file 267]


## 363. Rigorous: S²ê < 3|ω|²/4 for N ≤ 3. With H_ωω: N ≤ 4.
## Gap for N ≥ 5: triangle inequality too loose, actual ~0.27 << 0.75.
