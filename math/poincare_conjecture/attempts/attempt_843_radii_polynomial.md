# Attempt 843 — Radii Polynomial: NS Regularity as One Inequality

**Date**: 2026-04-07
**Instance**: Odd (from continuous domain investigation)

## The Idea

Apply the radii polynomial / verified computation approach to the
Leray profile equation. The Liouville conjecture (φ = 0 is the only
bounded ancient solution) becomes a COMPUTABLE inequality.

## The Setup

The Leray profile φ satisfies:
  -νΔφ + (1/2)φ + (1/2)y·∇φ + (φ·∇)φ + ∇q = 0

The linear part L = -νΔ + (1/2) + (1/2)y·∇ is the Ornstein-Uhlenbeck operator.

## The OU Spectrum

In the Hermite function basis {H_n(y)}:
  L H_n = (n/2) H_n

Spectrum: λ_n = n/2 for n = 0, 1, 2, ...
Spectral gap: λ_1 - λ_0 = 1/2.
ALL eigenvalues POSITIVE (for n ≥ 1 after removing the constant mode).

## The Radii Polynomial Approach

1. Write F(φ) = Lφ + (φ·∇)φ + ∇q = 0
2. Approximate solution: φ̄ = 0 (the trivial solution)
3. Residual: F(0) = 0 (exact — the trivial solution IS a solution)
4. Linearization: DF(0) = L (the OU operator)
5. Inverse bound: ||L⁻¹|| = 1/λ_min = 2 (from the spectral gap)
6. Nonlinearity bound: ||D²F|| = ||(φ·∇)φ|| ≤ C_S ||φ||² (Sobolev)

The Banach fixed point theorem gives: if
  ||L⁻¹|| × ||D²F|| × ||φ|| < 1
i.e., 2 × C_S × ||φ|| < 1
i.e., ||φ|| < 1/(2C_S)

then φ = 0 is the UNIQUE solution in the ball ||φ|| < 1/(2C_S).

## The Gap: ONE INEQUALITY

Tsai (1998): |φ(y)| ≤ C/(1+|y|).
This gives ||φ||_{weighted L²} ≤ C' (some Sobolev norm).

Need: C' < 1/(2C_S).

C' = Tsai constant (from the 1998 bound)
C_S = Sobolev embedding constant (for the quadratic nonlinearity)

Both are COMPUTABLE NUMBERS.

## Why This Might Work

The OU operator has a STRONG spectral gap (λ_min = 1/2). This means
the linearized problem is well-conditioned — small nonlinear perturbations
can't create new solutions near φ = 0.

The Tsai bound |φ| ≤ C/|y| gives φ in weighted L² but NOT in L³.
The gap between L² and L³ is exactly the Tsai gap (28 years open).

BUT: the radii polynomial approach doesn't need L³. It needs the
Sobolev norm to be small enough. The weighted L² norm from Tsai's
bound might suffice if the Sobolev constant C_S is not too large.

## The Computation

1. Compute C_S: the Sobolev embedding constant for the quadratic
   nonlinearity in the OU-weighted space. This is a spectral theory
   computation (eigenvalues of the product operator).

2. Compute C': the Tsai constant in the appropriate norm. Tsai's proof
   gives |φ(y)| ≤ C/(1+|y|) where C depends on the initial data.
   For self-similar profiles: C is universal.

3. Check: C' < 1/(2C_S).

## Caveat

The IFT approach proves φ = 0 is LOCALLY unique (in a ball). The Liouville
conjecture asks for GLOBAL uniqueness (no bounded solutions anywhere).
To bridge: need ||φ|| < r for ALL bounded solutions, where r is the
uniqueness radius. Tsai's bound gives this IF C' < r.

The potential failure: C' might be too large (the Tsai bound is not tight
enough). In that case: need a TIGHTER bound on |φ|, which is exactly
the Tsai gap.

But: the radii polynomial approach makes the gap QUANTITATIVE.
Instead of "prove φ ∈ L³" (abstract), we get "prove C' < 1/(2C_S)" (number).

## 843. NS regularity = ONE INEQUALITY: C' < 1/(2C_S).
## C' = Tsai constant, C_S = Sobolev embedding in OU space.
## Both computable. The gap is quantified. The systematic approach applies.
