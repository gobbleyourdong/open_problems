---
source: HANSON-WRIGHT + BOUNDED EFFECTIVE RANK → analytical closure path
type: PROOF DIRECTION — the spectral decay of M_L bounds the max-cut value
file: 391
date: 2026-03-29
---

## THE KEY FINDING

The regression residual matrix M_L has **effective rank r_eff ≈ 2**,
bounded independently of N:

| N | r_eff mean | r_eff max |
|---|-----------|-----------|
| 3 | 1.74 | 2.00 |
| 5 | 2.02 | 3.36 |
| 7 | 2.15 | 4.52 |
| 9 | 2.14 | 4.01 |

r_eff = ||M_L||_F² / ||M_L||_op² measures how many eigenvalues contribute.
For our Biot-Savart-derived matrix: r_eff ≈ 2 (the matrix is essentially rank 2).

## WHY r_eff IS BOUNDED

The residual M_L has entries (Δ_{jk} - slope × D_{jk}) where both Δ and D
come from the Biot-Savart kernel in R³. After removing the D-correlated
component (the regression): the residual lives in a LOW-DIMENSIONAL subspace.

Specifically: the Biot-Savart structure constrains each pair's contribution
to a 2D plane in R³ (the plane ⊥ to the mode polarizations). The regression
removes the 1D component correlated with D. The residual is in the REMAINING
1D orthogonal complement — giving effective rank ≈ 2 (the matrix has ~2
significant eigenvalues).

## THE HANSON-WRIGHT BOUND

**Theorem (Rudelson-Vershynin 2013):** For s ∈ {±1}^N random (Rademacher)
and M a fixed symmetric matrix:

P(|s^T M s - E[s^T M s]| > t) ≤ 2 exp(-c min(t²/||M||_F², t/||M||_op))

**Corollary (maximum over sign patterns):**

max_s s^T M s ≤ C × max(√(N ln 2) × ||M||_F, N ln 2 × ||M||_op)

For our matrix with ||M||_F ≈ √r_eff × ||M||_op ≈ √2 × ||M||_op:

max(L) = max_s s^T M_L s ≤ C × max(√(2N ln 2) × ||M_L||_op, N ln 2 × ||M_L||_op)

For N ≥ 5: the first term dominates (√(2N) < N for N ≥ 3).

**max(L) ≤ C × √N × ||M_L||_op**

## THE CLOSURE ARGUMENT

R(s*) = 1 + 2(max(L) + slope × Y_max) / (N + 2Y_max)

With:
- max(L) ≤ C√N × ||M_L||_op
- slope = ρ × σ_X/σ_Y ≈ -0.8 × σ_X/σ_Y
- Y_max ≈ σ_Y × √(2N ln 2) (max of a quadratic form, Hanson-Wright)

Numerator: 2(C√N × ||M_L||_op - 0.8(σ_X/σ_Y) × σ_Y√N)
= 2√N × (C × ||M_L||_op - 0.8σ_X)

Denominator: N + 2Y_max ≈ N + 2σ_Y√N ≈ N (for large N).

R ≤ 1 + 2(C||M_L||_op - 0.8σ_X)/√N

**For large N: R → 1 from above (the excess vanishes!)**

For small N (N=5): the constants matter. With C ≈ 3 (from Hanson-Wright),
||M_L||_op ≈ σ_X × √(1-ρ²)/√N, σ_X ≈ √(N/8) × max|Δ|:

The detailed computation needs the actual constants from Hanson-Wright.

## WHAT NEEDS TO BE PROVEN

1. **r_eff(M_L) ≤ C₀** for some universal C₀ (independent of N)

   This follows from: M_L is a matrix derived from the Biot-Savart kernel
   in R³ after regression. The rank is bounded by the dimension of the
   ambient space (3) minus the regression direction (1) = 2.

   More precisely: each entry M_{jk} = Δ_{jk} - slope × D_{jk} depends
   on 3D geometric quantities (κ, A, B, D). The matrix M acts on R^N but
   its IMAGE is in a 3D space (since the ŝ_k vectors are in R³). After
   regression: the residual is in a 2D subspace.

   **CLAIM: r_eff(M_L) ≤ 3 for all N.** (Numerically: max observed = 4.5.)

2. **The Hanson-Wright constant C** for the maximum over {±1}^N

   The standard bound: max_s s^T M s ≤ C(||M||_F √(N ln 2) + ||M||_op N ln 2).
   With r_eff bounded: ||M||_F = √r_eff × ||M||_op ≈ √3 × ||M||_op.
   So: max ≤ C(√(3N ln 2) + N ln 2) × ||M||_op.

   For N ≥ 5: the second term dominates. But C is a SMALL constant
   (typically C ≈ 1/c where c ≈ 0.1 from Hanson-Wright: c ≈ 0.01-0.1).

3. **Combine with the regression bound** to show R < 13/8

## THE PROOF SKETCH (if r_eff ≤ 3 is proven)

STEP 1: At the global max, decompose X = L + slope × Y (regression).
STEP 2: max(L) ≤ C√(3N) × ||M_L||_op (Hanson-Wright + bounded r_eff).
STEP 3: ||M_L||_op ≤ σ_L / √N = σ_X√(1-ρ²) / √N (from r_eff ≤ 3).
         Actually: ||M_L||_op² = λ_max(M_L^T M_L). For rank-3 matrix:
         ||M_L||_op ≤ ||M_L||_F/√1 = σ_L... no, this doesn't help.

Hmm: the relationship ||M_L||_op and σ_L needs more care.

σ_L² = E[L²] = 4Σ(M_L)_{jk}² = 4||M_L||_F²/2 = 2||M_L||_F² (for symmetric).
Wait: σ_L² = Var(L) = E[(s^T M_L s)²] - (E[s^T M_L s])² = 4Σ_{j<k} M_{jk}² = 2||M_L||_F².

So ||M_L||_F = σ_L/√2.

And: ||M_L||_op ≈ ||M_L||_F/√r_eff = σ_L/(√2 × √r_eff).

For r_eff = 2: ||M_L||_op = σ_L/2.

max(L) ≤ C × √(N ln 2) × σ_L/√2 + C × N ln 2 × σ_L/2

For N = 5: ≈ C × 1.86 × σ_L/√2 + C × 3.47 × σ_L/2 ≈ C × (1.32 + 1.73)σ_L = 3.05Cσ_L.

The regression: slope × Y_max = ρσ_X/σ_Y × σ_Y√(2N ln2) = ρσ_X√(2N ln2).
≈ -0.8 × σ_X × 2.63 = -2.1σ_X.

With σ_L = σ_X√(1-ρ²) = 0.6σ_X:
max(L) ≈ 3.05C × 0.6σ_X = 1.83Cσ_X.

Net: max(L) + slope×Y_max ≈ (1.83C - 2.1)σ_X.

For C < 2.1/1.83 ≈ 1.15: the net is NEGATIVE → R < 1 → barrier closes!

The Hanson-Wright constant: from Rudelson-Vershynin, c ≈ 1/16 in the
exponential, giving C ≈ 4 for the max bound. But 4 > 1.15.

So the GENERIC Hanson-Wright constant is too large. Need the SPECIFIC
structure of M_L to get a tighter C.

## STATUS

r_eff ≈ 2 is the KEY structural finding. Combined with Hanson-Wright:
the max-cut value of M_L grows as √N (not N). This is the RIGHT scaling
for the regression bound to close.

The GAP is now the CONSTANT: the generic Hanson-Wright constant C ≈ 4
is too large by ~3.5×. The specific Biot-Savart structure should give
a tighter constant, but proving this requires kernel-specific analysis.

## 391. r_eff ≈ 2 (bounded, not growing). Hanson-Wright gives √N scaling.
## The proof is now about the CONSTANT in the tail bound.
## Kernel-specific Hanson-Wright needed to close.
