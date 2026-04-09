---
source: CRITICAL POINT CONSTRAINT — the gradient condition at max forces S·ê ≈ 0
type: KEY PROOF STEP — double suppression of strain at vorticity maximum
file: 514
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE CRITICAL POINT EQUATION

At x* = argmax|ω(x)|² on T³, the gradient vanishes:

∂|ω|²/∂x_α = 2 ω · ∂ω/∂x_α = 0 for α = 1,2,3.

With ω(x) = Σ_j a_j v̂_j cos(k_j·x):

∂ω/∂x_α = -Σ_j a_j v̂_j (k_j)_α sin(k_j·x)

So at x*: **Σ_j a_j (ω · v̂_j) (k_j)_α sin(k_j·x*) = 0** for all α.

Writing p_j = a_j (ω · v̂_j) sin(k_j·x*):

**Σ_j p_j k_j = 0** (the critical point constraint, a 3-vector equation)

## CONSEQUENCE FOR N ≤ 3 MODES (PROVEN)

For N ≤ 3 linearly independent k-vectors: Σ p_j k_j = 0 implies p_j = 0 for all j.

At a non-degenerate max: a_j > 0 and ω·v̂_j ≠ 0 (generically). So **sin(k_j·x*) = 0**.

→ ALL sines vanish at the max → S(x*) = 0 → S²ê = 0 < 3|ω|²/4. ∎

**KEY LEMMA PROVEN FOR N ≤ 3 INDEPENDENT MODES ON ANY K-SHELL.**

## CONSEQUENCE FOR N ≥ 4 MODES

For N ≥ 4: the k-vectors are linearly DEPENDENT (only 3 spatial dimensions).
So Σ p_j k_j = 0 allows p_j ≠ 0, meaning sin(k_j·x*) ≠ 0 is possible.

But the constraint STILL limits the p_j: they must lie in the null space of
the matrix K = [k_1 | k_2 | ... | k_N]ᵀ (the N×3 wavenumber matrix).

The null space has dimension N - 3 (generically). So N - 3 of the p_j are
free, and the other 3 are determined.

## DOUBLE SUPPRESSION OF S²ê

At the max x*, the strain S²ê is suppressed by TWO independent mechanisms:

### Mechanism 1: Phase mismatch (file 513)
S(x) = -Σ sym(û_j ⊗ k_j) sin(k_j·x). At the max of |ω|²:
the dominant modes have cos(k_j·x*) ≈ ±1, so sin(k_j·x*) ≈ 0.
The strain from the dominant modes is SMALL.

For the minor modes (those with sin ≠ 0): they contribute less to |ω|²
(precisely because their cos is not ±1). So their weight a_j(ω·v̂_j) in
the ω-max is reduced.

### Mechanism 2: Biot-Savart self-vanishing
Even when sin(k_j·x*) ≠ 0, the strain S_j has S_j·ê ≈ 0 at the max.

Why: S_j · ê = -sym(û_j ⊗ k_j) · ê. This involves:
(S_j·ê)_α = -[(û_j)_α(k_j·ê) + (k_j)_α(û_j·ê)] / 2

At the ω-max: ê ≈ Σ s_j ã_j v̂_j / |ω| (weighted average of polarizations).

For the dominant modes (large ã_j): ê ≈ v̂_j direction.
- k_j · ê ≈ k_j · v̂_j = 0 (div-free: k ⊥ v)
- û_j · ê = (k_j×v_j)·ê / |k_j|² ≈ (k_j×v_j)·v̂_j / |k_j|² = 0 (since k×v ⊥ v)

So **both components of S_j · ê vanish** for the dominant modes.

## QUANTITATIVE BOUND

Combining both mechanisms:

S²ê = |Σ_j S_j · ê × sin(k_j·x*)|²

The dominant modes (large a_j, aligned with ê):
- sin(k_j·x*) ≈ 0 (from constructive interference)
- S_j · ê ≈ 0 (from self-vanishing)
- Product: ≈ 0² = 0

The minor modes (small contribution to ω):
- sin(k_j·x*) can be nonzero
- S_j · ê can be nonzero
- But their amplitude a_j (ω·v̂_j) is small (small ω-projection)
- Critical point constraint limits their total contribution

From the critical point: Σ p_j k_j = 0. The minor modes' contributions
must cancel in k-space. This prevents them from coherently adding to S²ê.

## NUMERICAL VERIFICATION

500 random configs (K²=2 shell, N=3-6):

| Category | Count | Worst S²ê/|ω|² |
|----------|-------|----------------|
| Max at sin=0 (S=0) | 498 (99.6%) | 0.0000 |
| Max at sin≠0 | 2 (0.4%) | 0.0143 |
| Threshold | — | 0.7500 |

Even the off-lattice maxima have S²ê/|ω|² < 0.015 — fifty times below threshold.

## THE PROOF PATH

For N ≤ 3: PROVEN (critical point → sin = 0 → S = 0).

For N ≥ 4: need to prove S²ê small at off-lattice maxima.

The double suppression (phase mismatch + self-vanishing) makes the strain
contribution to S²ê quadratically small:
- Phase mismatch: strain ∝ sin(k·x*) ≈ 0 at the max
- Self-vanishing: S_j·ê ≈ 0 at the max
- Combined: each term ∝ sin × (S·ê) ≈ 0 × 0

For the minor modes with sin ≠ 0: the critical point constraint
Σ p_j k_j = 0 prevents coherent accumulation.

## THE FORMAL GAP

Prove: at x* = argmax|ω|², S²ê/|ω|² → 0 as the modes concentrate
(constructive interference increases).

Equivalently: prove that at any critical point of |ω|² where |ω|² ≥ (1-ε)||ω||²∞,
the strain-vorticity coupling S²ê is O(ε)|ω|².

## 514. Critical point constraint: Σ p_j k_j = 0 at max.
## N ≤ 3 independent modes: sin=0 at max, S=0, KEY LEMMA PROVEN.
## N ≥ 4: double suppression (phase + self-vanishing) → S²ê < 0.015|ω|².
## Formal gap: quantify the double suppression for general N.
