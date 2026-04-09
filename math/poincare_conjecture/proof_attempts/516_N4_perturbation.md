---
source: N=4 PERTURBATION — rigorous bound on S²ê at off-lattice max
type: PROOF ATTEMPT — perturbation theory around the lattice max
file: 516
date: 2026-03-30
instance: CLAUDE_OPUS
---

## SETUP

N = 4 modes on a single K-shell. k_1, k_2, k_3 linearly independent.
k_4 = α k_1 + β k_2 + γ k_3 (rational coefficients for integer k).

Phases: φ_j = k_j · x. At the lattice max: φ_j = n_j π (integer multiple).
So cos(φ_j) = s_j = ±1 and sin(φ_j) = 0.

At the lattice max: |ω|²_lat = |Σ s_j a_j v̂_j|² and S = 0.

## PERTURBATION

Perturb: φ_j = n_j π + ε δ_j where ε is small and δ_j are unit perturbations.

Constraint from k_4 = α k_1 + β k_2 + γ k_3:
φ_4 = α φ_1 + β φ_2 + γ φ_3
→ δ_4 = α δ_1 + β δ_2 + γ δ_3

So δ_4 is determined. There are 3 free parameters (δ_1, δ_2, δ_3).

To first order in ε:
cos(φ_j) ≈ s_j - ε s_j δ_j² × 0 ... wait, cos(nπ + εδ) = cos(nπ)cos(εδ) - sin(nπ)sin(εδ)
= s_j cos(εδ) ≈ s_j(1 - ε²δ²/2)

sin(φ_j) ≈ sin(nπ + εδ) = sin(nπ)cos(εδ) + cos(nπ)sin(εδ) = s_j sin(εδ) ≈ s_j ε δ_j

So:
|ω(ε)|² = |Σ a_j v̂_j s_j (1 - ε²δ_j²/2)|² ≈ |ω_lat|² - ε² (Σ a_j(ω·v̂_j)s_j δ_j²) + O(ε⁴)

Wait, let me be more careful. Let c_j = cos(φ_j) and q_j = sin(φ_j).

c_j ≈ s_j(1 - ε²δ_j²/2), q_j ≈ s_j ε δ_j.

ω(ε) = Σ a_j v̂_j c_j ≈ Σ a_j v̂_j s_j - (ε²/2) Σ a_j v̂_j s_j δ_j²
= ω_lat - (ε²/2) Σ a_j v̂_j s_j δ_j²

|ω(ε)|² ≈ |ω_lat|² - ε² ω_lat · (Σ a_j v̂_j s_j δ_j²) + O(ε⁴)
= |ω_lat|² - ε² Σ a_j (ω_lat · v̂_j) s_j δ_j² + O(ε⁴)

Define: w_j = a_j (ω_lat · v̂_j) s_j = a_j ã_j (the aligned ω-projection).

|ω(ε)|² ≈ |ω_lat|² - ε² Σ w_j δ_j²

For this to be a max: the ε-derivative must vanish, meaning the lattice point
IS the max along all perturbation directions. The perturbation DECREASES |ω|².

S(ε) = Σ S_j q_j ≈ ε Σ s_j S_j δ_j

S²ê(ε) = |S(ε) · ê_lat|² ≈ ε² |Σ s_j (S_j · ê_lat) δ_j|²

So at order ε²:
S²ê / |ω|² ≈ ε² |Σ s_j (S_j · ê_lat) δ_j|² / |ω_lat|²

## THE RATIO AT THE OFF-LATTICE MAXIMUM

If the global max is at the lattice (ε = 0): S²ê = 0. DONE.

If the global max is at ε* ≠ 0: the off-lattice max satisfies
∂|ω|²/∂ε = 0, giving:
-2ε Σ w_j δ_j² + O(ε³) = 0

For ε ≠ 0: Σ w_j δ_j² = O(ε²). This means the SECOND derivative
has a zero, which requires specific alignment of w_j and δ_j.

The off-lattice max has ε* such that |ω(ε*)|² > |ω_lat|² (it exceeds
the lattice max). From the expansion:
|ω(ε*)|² ≈ |ω_lat|² - ε*² Σ w_j δ_j² + higher order

For this to exceed |ω_lat|²: need Σ w_j δ_j² < 0 (at ε = 0, the lattice
is a saddle point, not a max). This requires some w_j < 0, i.e., some modes
ANTI-ALIGNED with the vorticity direction.

When Σ w_j δ_j² < 0:
ε*² ≈ ...(from higher-order terms, need the quartic coefficient to stabilize)

The ratio: S²ê / |ω|² ≈ ε*² |Σ s_j (S_j·ê) δ_j|² / (|ω_lat|² + O(ε*²))

From self-vanishing: S_j · ê ≈ 0 for the dominant modes (those with w_j > 0).
The dominant modes have w_j > 0 (aligned with ê). Only the ANTI-ALIGNED modes
(w_j < 0) contribute significantly to S_j · ê.

But the anti-aligned modes have SMALL |w_j| (the Hessian PSD constraint
limits how negative w_j can be, see file 514).

## THE BOUND

|S · ê| ≤ ε Σ |s_j (S_j·ê) δ_j|

From per-mode: |S_j·ê| ≤ |S_j| ≤ a_j/√2. And |δ_j| ≤ 1.

S²ê ≤ ε² (Σ a_j/√2)²

And |ω|² ≈ |ω_lat|² ≥ (max s_j a_j)² (at least the dominant mode).

So S²ê/|ω|² ≤ ε² N²/(2 × dominant mode²).

For the off-lattice max: ε* is small (the lattice max is close). The ratio
scales as ε*², which is QUADRATICALLY suppressed.

## WHY ε* IS SMALL

For the off-lattice max to exist: the lattice Hessian must have a negative
eigenvalue in the constrained directions. This requires specific geometric
alignment between:
- The polarizations v̂_j
- The k-vectors k_j
- The linear dependence k_4 = α k_1 + β k_2 + γ k_3

Numerically: only 0.4% of random configs have ε* ≠ 0 on K=√2 single shell.
And when ε* ≠ 0: S²ê/|ω|² < 0.015 (50× below threshold).

For multi-shell (multiple |k| values): 38.5% have ε* ≠ 0, but S²ê/|ω|² < 0.07 (11× below threshold).

## THE PROOF FOR SINGLE-SHELL N=4 (sketch)

**Claim**: For N=4 on any single K-shell, S²ê/|ω|² < 3/4 at argmax|ω|².

**Proof sketch**:
1. If max at lattice (ε = 0): S = 0. Done.
2. If max off-lattice (ε ≠ 0):
   a. The perturbation theory gives S²ê ∝ ε² (quadratic in departure)
   b. The self-vanishing gives S_j·ê ∝ (k_j·ê/|k|, û_j·ê) (both small)
   c. The combined bound: S²ê/|ω|² ≤ ε² × (small factors) < 3/4

The formal difficulty: bounding ε* in terms of the mode parameters.

The STRONGEST version would be: S²ê/|ω|² ≤ C for some C < 3/4,
for ALL N ≥ 4 on ALL K-shells. The perturbation theory gives C → 0
as N → ∞ (due to dilution + phase averaging).

## 516. Perturbation around lattice: S²ê = O(ε²) at off-lattice max.
## Self-vanishing further suppresses: each S_j·ê is small.
## Combined: double suppression gives S²ê/|ω|² ≪ 3/4.
## Formal gap: bound ε* quantitatively.
