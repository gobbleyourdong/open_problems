---
source: PROOF STRATEGY — Invariance Principle + KKL + Efron-Stein + Hanson-Wright
type: THE PATH — these four theorems close the Key Lemma
file: 397
date: 2026-03-29
---

## THE PROOF STRATEGY (from literature research)

### Step 1: Invariance Principle (Mossel-O'Donnell-Oleszkiewicz 2010)
For degree-2 multilinear polynomials with small per-coordinate influences:
Rademacher ≈ Gaussian (in distribution).

For GAUSSIAN orthogonal forms: E[L|Y=max] = 0 EXACTLY (independence).
So: L(s*) at the Y-maximizer is "Gaussian-like" → centered, O(σ_L).

Paper: Annals of Mathematics 171(1), 2010. "Noise stability of functions
with low influences: invariance and optimality."

### Step 2: KKL Theorem (Kahn-Kalai-Linial 1988)
For Boolean functions: total influence Σ Inf_i ≥ Var(f) × c log N / N.
Per-coordinate influence: max Inf_i ≤ ||M||_∞² / ||M||_F² ~ 1/N for
our matrices (where entries are O(1/√N)).

Small per-coordinate influence → Invariance Principle applies.

### Step 3: Efron-Stein Decomposition
Orthogonal decomposition f = Σ_S f^{=S}. For quadratic forms: only
degree-0 and degree-2 terms. Orthogonality Tr(M_A M_B) = 0 kills
the Fourier cross-correlation at degree 2.

### Step 4: Hanson-Wright (Rudelson-Vershynin 2013)
||M_A s*||² concentrates around E[||M_A s||²] = 2||M_A||_F² (for Rademacher s).
At s* determined by M_B: the concentration still holds because
M_A ⊥ M_B (the constraint doesn't affect M_A's norm).

### Combined:
- ||M_A s*|| ~ ||M_A||_F (Step 4, bounded)
- alignment(s*, M_A s*) ~ 1/√N (Steps 1-3, from invariance + low influence)
- |s*^T M_A s*| = alignment × √N × ||M_A s*|| ~ (1/√N) × √N × ||M_A||_F = ||M_A||_F

**KEY LEMMA FOLLOWS: |s*^T M_A s*| ≤ C × ||M_A||_F with C = O(1).**


## THE PER-COORDINATE INFLUENCE BOUND

For our Biot-Savart residual matrix M_L:

Inf_j(L) = E[L(s) - L(s^{j→-s_j})]² / 4 = (Σ_k M_{jk})² for the quadratic form.

Actually: for Q(s) = Σ_{j<k} a_{jk} s_j s_k, the influence of coordinate i is:
Inf_i(Q) = Σ_{j≠i} a_{ij}² (the sum of squared entries in row i).

Total influence: Σ_i Inf_i = 2 Σ_{j<k} a_{jk}² = 2||M||_F² (off-diagonal).

Max influence: max_i Inf_i = max_i (Σ_{j≠i} a_{ij}²) = max row-squared-norm.

For the Invariance Principle: need max Inf_i / Var(Q) → 0. Since:
- max Inf_i ≤ ||M||_op² (spectral norm squared, from Cauchy-Schwarz on a row)
- Var(Q) = ||M||_F² (the Frobenius norm squared)

The ratio: max Inf_i / Var(Q) ≤ ||M||_op² / ||M||_F² = 1/r_eff.

For our matrices: r_eff ≈ 2-4 (effective rank). So: max Inf_i / Var ≈ 1/3.

This is NOT small! The per-coordinate influence is ~ 1/3 of the variance,
which means the Invariance Principle may not apply directly.

**GAP**: The Invariance Principle requires max influence → 0. For our
matrices with r_eff ≈ 3: max influence is ~ 1/3. Not small enough.


## RESOLUTION: USE THE SPECIFIC STRUCTURE

The Invariance Principle doesn't apply directly (influences too large).
But: the FOURTH-MOMENT anti-correlation (file 396) provides the needed bound.

Alternative: use the NOISE STABILITY approach (Mossel 2012):
- Noise stability of MAX-CUT: the Goemans-Williamson rounding has noise
  sensitivity η. For our problem: the "noise" is M_A (orthogonal to M_B).
- The MAX-CUT solution's response to orthogonal perturbation is bounded.

Or: use the GROTHENDIECK inequality directly:
- max_{s∈{±1}^N} s^T M_A s ≤ K_G × max_{u∈S^{N-1}} u^T M_A u = K_G × ||M_A||_op
- At the specific s* (not the maximizer of M_A): |s*^T M_A s*| should be
  much less than the maximum, bounded by ||M_A||_F.


## KEY PAPERS TO READ IN DETAIL

1. **Mossel-O'Donnell-Oleszkiewicz (2010)**: Invariance Principle.
   Annals of Mathematics 171(1). The foundational tool.

2. **O'Donnell (2014)**: "Analysis of Boolean Functions" textbook.
   Chapter 11 (Invariance Principle), Chapter 9 (Influences).
   Available: cs.cmu.edu/~odonnell/boolean-analysis/

3. **Kwan (2024)**: Quadratic Littlewood-Offord resolution.
   arXiv:2312.13826. Anticoncentration for degree-2 Rademacher polynomials.

4. **Rudelson-Vershynin (2013)**: Hanson-Wright sharp constants.
   arXiv:1306.2872.

5. **Buaria-Lawson-Wilczek (2024)**: Anti-twist self-attenuation.
   Science Advances. Physical mechanism for the mathematical bound.

6. **Miller (2019)**: Middle eigenvalue strain criterion.
   arXiv:1710.05569. NS regularity via strain eigenvalue control.


## STATUS

The proof strategy is clear but has a GAP: the Invariance Principle
requires small per-coordinate influences (max Inf_i / Var → 0),
which fails for our matrices (r_eff ≈ 3, ratio ≈ 1/3).

ALTERNATIVES:
A. Prove the Key Lemma directly via the fourth-moment anti-correlation
B. Use noise stability instead of invariance principle
C. Exploit the specific Biot-Savart structure (not just orthogonality)
D. Computer-assisted proof with interval arithmetic for each K-shell


## 397. Invariance Principle + KKL + Efron-Stein + Hanson-Wright is the path.
## GAP: r_eff ≈ 3 means influences are NOT small. Need alternative.
## Best bet: fourth-moment anti-correlation (file 396) or noise stability.
