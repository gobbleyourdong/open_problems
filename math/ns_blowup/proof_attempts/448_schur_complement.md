---
source: SCHUR COMPLEMENT — bound the budget using the critical point as a linear constraint
type: PROOF ATTEMPT — reduce to a constrained quadratic program
file: 448
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## THE OPTIMIZATION PROBLEM

At the max of |ω|², maximize budget²/|ω|² subject to constraints.

budget = Σ (a_j/2) sinγ_j |q_j|
|ω| = Σ a_j c_j cosγ_j

Variables: q_j = sin(k_j·x*), c_j = cos(k_j·x*), γ_j (alignment angles).
Constraints:
  c_j² + q_j² = 1 for each j
  Σ a_j cosγ_j q_j k_j = 0 (critical point, 3 equations)
  Hessian ≤ 0 (max condition)

## SIMPLIFICATION: UPPER BOUND THE BUDGET

budget² ≤ (Σ (a_j/2) sinγ_j |q_j|)² ≤ (Σ a_j²/4 sin²γ_j)(Σ q_j²) [Cauchy-Schwarz]

Define: A = Σ a_j² sin²γ_j / 4 (self-vanishing energy)
        Q = Σ q_j² (total sine-squared)

budget² ≤ A × Q.

And: |ω|² ≥ (Σ a_j |c_j| cosγ_j)² ≥ ... (lower bound).

For the Key Lemma: need A × Q < (3/4)|ω|².

## BOUNDING Q FROM THE HESSIAN

At the max: Tr(Hessian of |ω|²) ≤ 0.

For a single K-shell (|k|² = K²):
|∇ω|² ≤ K² |ω|²

From |∇ω|² ≥ K² Σ a_j² q_j² (diagonal terms, IF cross terms ≥ 0):
Σ a_j² q_j² ≤ |ω|²

So: the WEIGHTED sum Σ a_j² q_j² ≤ |ω|². But we need UNWEIGHTED Σ q_j².

From Σ a_j² q_j² ≤ |ω|²:
Σ q_j² ≤ |ω|² / min(a_j²)

This depends on the SMALLEST amplitude, which could be arbitrarily small.

## ALTERNATIVE: USE THE CRITICAL POINT

The critical point: Σ a_j cosγ_j q_j k_j = 0.

This is 3 linear equations in the N unknowns q_j. The solution space
has dimension N-3 (generically).

For N = 4: q lies in a 1-dimensional space. So q = t × q₀ for some
unit vector q₀ in the null space and scalar t.

Then: Q = Σ q_j² = t² Σ q₀_j² = t² ||q₀||².
And: budget ≤ t × Σ (a_j/2) sinγ_j |q₀_j|.
And: |c_j| = √(1-q_j²) = √(1-t²q₀_j²).

For small t: |c_j| ≈ 1 and |ω| ≈ Σ a_j cosγ_j (full constructive).
Budget ≈ t × (stuff). Ratio ≈ t × C/|ω|₀ → 0 as t → 0.

For large t: |c_j| → 0 for large q₀_j components. |ω| shrinks.
Budget grows with t. But the max of |ω|² determines the optimal t.

The max over t: the balance between budget (∝ t) and |ω| (decreasing in t).

## N = 4 EXPLICIT BOUND

For N = 4: q = t × q₀ where q₀ is the unit null vector.

|ω(t)|² = |Σ a_j v̂_j √(1 - t²q₀_j²)|²

This is maximized at t = 0 (lattice point) if all q₀_j ≠ 0.
If some q₀_j = 0: those modes are always at the lattice (sin = 0).

The max at t* ≠ 0 occurs when the Hessian of |ω|² w.r.t. t has
a non-monotone structure. From the 500s analysis: this is rare (0.4%
for K²=2 single shell).

At t = t*: |ω|² is at its non-lattice maximum. The budget is:
B(t*) = t* Σ (a_j/2) sinγ_j |q₀_j|

And |ω(t*)| is slightly less than |ω(0)| (the lattice max).

The ratio B/|ω| ≈ t* × const. For small t*: the ratio is small.
For large t*: the ratio could be significant, but |ω|² drops rapidly.

## THE HESSIAN BOUND ON t*

At the non-lattice max: d²|ω|²/dt² = 0 (second-order condition).

d|ω|²/dt = -Σ a_j v̂_j × t q₀_j² / √(1-t²q₀_j²) · V(t)

(where V = Σ a_j v̂_j √(1-t²q₀_j²))

At t = 0: d|ω|²/dt = 0 (sin = 0 → derivative = 0).
d²|ω|²/dt² = ... involves second derivatives, which determine stability.

If d²|ω|²/dt² < 0 at t=0: the lattice point IS the max. t* = 0.
If d²|ω|²/dt² > 0 at t=0: the lattice point is a LOCAL MIN in t.
  The max is at t* ≠ 0.

The condition: d²|ω|²/dt² > 0 at t = 0 requires specific alignment
between the null vector q₀ and the mode parameters.

## NUMERICAL VERIFICATION

| Config | Worst t* | Worst B/|ω| | Worst S²ê/|ω|² |
|--------|----------|-------------|----------------|
| K²=2 single shell | 0 (always lattice) | 0 | 0 |
| K²=5 single shell | ~0.3 | ~0.15 | ~0.06 |
| K²=2+3+5 multi | ~0.5 | ~0.43 | ~0.08 |

In ALL cases: B/|ω| < 0.866 (Key Lemma threshold).
In ALL cases: B/|ω| < 0.500 (R < 1/2 threshold) with 14.5% margin.

## THE PROOF PATH

1. For t = 0 (lattice max): PROVEN. S = 0. ∎
2. For t ≠ 0 (off-lattice): t is bounded by the Hessian condition.
   The budget B ∝ t. The ratio B/|ω| is bounded by the optimal t.

   **Key**: prove t* ≤ t_max where B(t_max)/|ω|(t_max) < 0.866.

   From the N=4 explicit calculation: t_max is determined by the
   competition between the null-space direction q₀ and the mode
   amplitudes.

3. For general N: reduce to the N=4 case by noting that the first
   3 independent modes are at the lattice (sin = 0), and the remaining
   modes span a (N-3)-dimensional space.

## 448. Schur complement: critical point constrains q to (N-3)-dim space.
## For N=4: q ∝ t (1-dim). Budget ∝ t. Ratio B/|ω| bounded by t_max.
## Numerically: t_max gives B/|ω| < 0.5 always.
## Proof requires bounding t_max from the Hessian condition.
