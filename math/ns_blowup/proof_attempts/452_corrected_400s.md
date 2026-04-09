---
source: CORRECTED 400s — post-phase-error state with self-vanishing as primary tool
type: ERROR CORRECTION + NEW APPROACH — self-vanishing alone suffices
file: 452
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## PHASE ERROR CORRECTION

Files 446-451 relied on the sin-cos decoupling (S ∝ sin, ω ∝ cos).
**This is WRONG** (500s file 523 verified: both S and ω involve cos(k·x)).

### What's invalidated from 400s:
- File 446: "budget = Σ(a/2)sinγ|sin(k·x)|" — the |sin| factor is wrong
- File 447: "N≤3 theorem: S=0 at max" — FALSE (S ≠ 0 at vertex max)
- File 448: Schur complement via sin null space — based on wrong premise
- File 451: "Phase mismatch" suppression — doesn't exist

### What REMAINS correct from 400s:
- Barrier framework (files 439-444) — independent of sin-cos
- Vertex jump R_crit = 0.476 (file 440) — verified numerically
- Negative cross-terms for orthogonal k (file 445) — algebraic, still valid
- Self-alignment of ê with dominant mode (file 450, mechanism correct)
- Directional cancellation of S_j·ê vectors (file 451, partially correct)

## THE CORRECTED SELF-VANISHING BOUND

At x* = argmax|ω|² (vertex max, all c_k = ±1):

S·ê = Σ s_k (S_k·ê) where s_k = cos(k·x*) = ±1.

|S_k·ê| = (a_k/2) sinγ_k (self-vanishing, PROVEN, verified to 10⁻¹⁵).

S²ê = |Σ s_k (a_k/2) sinγ_k ê_k|² where ê_k are unit vectors in R² (plane ⊥ ê).

**Triangle bound**: S²ê ≤ (Σ (a_k/2) sinγ_k)² = (1/4)(Σ a_k sinγ_k)².

And: |ω|² = |Σ s_k a_k v̂_k|² = (Σ s_k a_k cosγ_k)² + perpendicular².

**For Key Lemma**: need (1/4)(Σ a_k sinγ_k)² < (3/4)|ω|²
i.e., Σ a_k sinγ_k < √3 |ω|.

## THE SELF-ALIGNMENT MECHANISM (still valid!)

At the GLOBAL max of |ω|²: ê aligns with the dominant modes.
The dominant mode has cosγ ≈ 1 → sinγ ≈ 0 → contributes ≈ 0 to Σ a sinγ.

So: Σ a_k sinγ_k ≈ Σ_{minor} a_k sinγ_k (only non-dominant modes contribute).

And: |ω| ≈ a_dominant (the dominant mode's amplitude).

Ratio: Σ_{minor} a sinγ / (a_dominant) < √3 when the dominant mode is large enough.

## THE CRITICAL CASE: ALL MODES COMPARABLE

When NO single mode dominates: all a_k ≈ a.

Then: Σ a sinγ ≈ Na × (average sinγ). And |ω| ≈ Na × (average cosγ).
Ratio ≈ average(sinγ)/average(cosγ) = average(tanγ).

For Key Lemma: average(tanγ) < √3, i.e., average γ < 60°.

At the max: ê is the direction that minimizes the average γ (maximizes alignment).
For N randomly oriented modes in R³: the best ê gives average cosγ ≈ 2/π ≈ 0.64.
So average sinγ ≈ 0.77. Ratio ≈ 0.77/0.64 ≈ 1.2 > √3 ≈ 1.73? No, 1.2 < 1.73.

Actually: average(sinγ)/average(cosγ) ≠ average(tanγ). The ratio of averages
is less than the average of ratios (by Jensen).

For uniformly distributed modes: Σ a sinγ / Σ a cosγ = E[sinγ]/E[cosγ].

If γ ∈ [0, π/2] uniformly: E[sinγ] = 2/π ≈ 0.637, E[cosγ] = 2/π ≈ 0.637.
Ratio = 1.0 < √3 ≈ 1.73. ✓

If modes cluster near γ = π/3 (60°): E[sinγ] ≈ sin60° = √3/2, E[cosγ] ≈ 1/2.
Ratio ≈ √3 = 1.73. This is the BOUNDARY case!

But at the max: ê is OPTIMIZED to minimize the ratio. Modes near γ = 60° would
make ê rotate to improve alignment. So the optimized ratio is < 1.73.

## THE KEY OBSERVATION

The ratio Σ a sinγ / |ω| at the global max is BOUNDED because ê adapts.

Define f(ê) = (Σ a_k sinγ_k(ê)) / |Σ s_k a_k v̂_k| where γ_k(ê) = angle(v̂_k, ê).

At the max: ê is determined by ω. But over ALL possible fields:
the worst f is achieved when the mode directions v̂_k are adversarially chosen.

For ANY set of unit vectors v̂_k and amplitudes a_k:
min_ê max_signs f(ê, s) is bounded by a function of the mode geometry.

## NUMERICAL ADVERSARIAL SEARCH

From the 500s data: worst S²ê/|ω|² = 0.364 (threshold 0.750, margin 51%).
From 400s data: worst S²ê/|ω|² = 0.091 [these used wrong formulas].

Need to RECOMPUTE with correct formulas.

## 452. Phase error corrected. Self-vanishing is the primary tool.
## S²ê ≤ (1/4)(Σ a sinγ)². Need Σ a sinγ < √3|ω|.
## Self-alignment makes sinγ ≈ 0 for dominant modes.
## Critical case: comparable amplitudes → ratio ≈ tanγ_avg < √3.
## Need adversarial computation with CORRECT formulas.
