---
source: 2D PERPENDICULAR ANALYSIS — bounding C in the perpendicular plane
type: PROOF ATTEMPT — exploit the 2D structure of the perpendicular components
file: 535
date: 2026-03-30
instance: CLAUDE_OPUS (500s)
---

## SETUP

At x* = argmax|ω|²: w_j = a_j ê + b_j where:
- a_j > 0, Σa_j = |ω|
- b_j ⊥ ê, Σb_j = 0
- |b_j|² ≤ a_j(|ω| - a_j) ≡ r_j² (the perpendicular radius)

The b_j live in the 2D plane perpendicular to ê. Choose orthonormal
basis {f₁, f₂} in this plane. Write b_j = (x_j, y_j) in this basis.

## THE CORRECTION IN TERMS OF b

C = C_aa + C_ab + C_bb

C_aa = Σ_{j<k} a_j a_k (ê·n̂)² sin²θ ≥ 0 [PROVEN, always positive]

C_ab + C_bb involves the b_j projections onto pair normals n̂_{jk}.

For each pair normal: n̂_{jk} = (k_j × k_k)/|k_j × k_k|.

Decompose n̂_{jk} = (ê·n̂)ê + n̂_{jk}^⊥ where n̂^⊥ is the 2D projection.

Then: w_j · n̂ = a_j(ê·n̂) + b_j · n̂^⊥

The C_bb term: Σ (b_j·n̂^⊥)(b_k·n̂^⊥) sin²θ

This is a BILINEAR FORM in the 2D vectors b_j.

## THE 2D OPTIMIZATION

For FIXED k-vectors and FIXED a_j:
Minimize C_ab + C_bb over the b_j subject to:
- Σb_j = 0 (2 constraints in 2D)
- |b_j|² ≤ r_j² = a_j(|ω|-a_j) (N inequality constraints)

This is a CONSTRAINED QUADRATIC PROGRAM in 2N variables (x_j, y_j)
with 2 equality constraints and N inequality constraints.

For N=4: 8 variables, 2 equality + 4 inequality = 6 constraints.
Degrees of freedom: 8 - 2 = 6 (from equality), further limited by
the inequality constraints.

## THE QUADRATIC FORM

C_ab + C_bb = Σ_{j<k} [(a_j(ê·n̂)(b_k·n̂^⊥) + a_k(ê·n̂)(b_j·n̂^⊥))
              + (b_j·n̂^⊥)(b_k·n̂^⊥)] sin²θ

Define for each pair the 2D direction d_{jk} = n̂_{jk}^⊥ / |n̂_{jk}^⊥|
and the factor α_{jk} = |n̂_{jk}^⊥| sin²θ_{jk}.

Then C_ab + C_bb ≈ Σ_{j<k} [linear in b + bilinear in b] × geometry

## THE KEY BOUND

For the MINIMUM of C_ab + C_bb over all feasible b_j:

The minimum is achieved when the b_j are at the boundary of their
constraints (|b_j| = r_j for the active modes, |b_j| < r_j for others)
and satisfy the KKT conditions.

From the numerical data: at the worst case, modes 2,3 are at the
boundary (|b|=r, 100%) while modes 0,1 are in the interior (|b|<r).

## BOUND VIA CAUCHY-SCHWARZ

|C_bb| = |Σ_{j<k} (b_j·d)(b_k·d) α sin²θ|

For the DOMINANT pair (j,k) with b_j ≈ -b_k:
  |contribution| ≈ |b_j|² α ≤ r_j² α ≤ (|ω|²/4) α

For α ≤ 1: this contribution ≤ |ω|²/4.

For OTHER pairs: their contributions are bounded by |b_j||b_l| α'
where at least one of j,l is not in the dominant pair.

The perpendicular cancellation: if b_1 ≈ -b_2 (dominant pair uses
r_1² + r_2² perpendicular energy), then b_3 + b_4 ≈ -(b_1+b_2) ≈ 0.
So b_3 ≈ -b_4 too, but with smaller amplitudes.

Total C_bb ≈ -|b_1|²α₁₂ - |b_3|²α₃₄ + cross terms

With |b_1|² ≤ |ω|²/4 and |b_3|² ≤ |ω|²/4:
Worst C_bb ≤ -|ω|²/4 × (α₁₂ + α₃₄ - cross)

For the cross terms to NOT cancel: they involve products
(b_1·d_{13})(b_3·d_{13}) etc. With b_1 and b_3 pointing in
potentially orthogonal 2D directions: the cross terms average
to smaller values.

## STATUS

The 2D analysis gives:
- C_bb from dominant pair: ≤ |ω|²/4 (from AM-GM + single pair)
- C_bb from other pairs: bounded by cross terms involving
  perpendicular vectors in 2D (geometrically constrained)
- C_ab: partially compensates (from file 533 data)
- C_aa: strictly positive for N ≥ 3 (PROVEN)

For a CLEAN proof: need to show that the total C_bb from all pairs
plus C_ab doesn't exceed |ω|²/4 (i.e., C_ab + C_bb ≥ -|ω|²/4).

From the data: worst C_ab + C_bb = -0.235|ω|² (margin 6% to -1/4).

The 6% margin suggests the bound is TIGHT — possibly achievable
in the limit of some specific geometry. But the C_aa ≥ 0 contribution
(PROVEN) rescues the total bound.

## 535. 2D analysis: b_j live in 2D with sum=0 and amplitude constraints.
## The optimization is a constrained QP with ~6 free parameters for N=4.
## The dominant pair contributes ≤ |ω|²/4 (AM-GM). Other pairs add less.
## C_aa > 0 (proven) provides the final margin.
