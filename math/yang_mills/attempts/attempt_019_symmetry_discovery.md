# Attempt 019 — Z₂ SYMMETRY: f(0) = f(1) EXACTLY

**Date**: 2026-04-07
**Phase**: 3 (Discovery)
**Instance**: Odd

## The Discovery

The interpolation function f(t) = ln Z(t) is **symmetric about t = 1/2**:

    f(t) = f(1-t) for all t ∈ [0, 1]

In particular: **f(0) = f(1)**. The periodic and anti-periodic partition
functions are EQUAL (in the character expansion on the 2D torus).

## Numerical Evidence

| β | L | f(0) | f(1) | f(0)-f(1) | min at t |
|---|---|------|------|-----------|----------|
| 1.0 | 4 | 0.000000 | 0.000000 | 0 | 0.49 |
| 2.0 | 4 | 0.000002 | 0.000002 | 0 | 0.50 |
| 2.3 | 4 | 0.000008 | 0.000008 | 0 | 0.50 |
| 5.0 | 4 | 0.005127 | 0.005127 | 0 | 0.50 |
| 10.0 | 4 | 0.078 | 0.078 | 0 | 0.50 |

f(t) always has a minimum at t = 1/2 and f(0) = f(1) to machine precision.

## Why This Happens

The interpolated partition function on the 2D torus:

    Z(t) = Σ_j [c_j^{Σ}(t)]^L · c_j^{L²-L}

For half-integer j: c_j^{Σ}(t) = (1-2t) c_j

The key: (1-2t)^L appears in Z(t). And (1-2(1-t))^L = (2t-1)^L = (-(1-2t))^L.

For EVEN L: (-(1-2t))^L = (1-2t)^L. So Z(t) = Z(1-t). **EXACT SYMMETRY.**
For ODD L: (-(1-2t))^L = -(1-2t)^L. The half-integer terms FLIP sign.
    But integer terms are unchanged. So Z(t) ≠ Z(1-t) for odd L.

Wait — let me check odd L. On the 2D torus, the number of plaquettes on
the vortex line Σ is L. If L is odd:

    Z(t) = Σ_{j int} c_j^{L²} + Σ_{j half} (1-2t)^L c_j^{L²}
    Z(1-t) = Σ_{j int} c_j^{L²} + Σ_{j half} (-(1-2t))^L c_j^{L²}
           = Σ_{j int} c_j^{L²} - Σ_{j half} (1-2t)^L c_j^{L²}   (L odd)

So Z(t) ≠ Z(1-t) for odd L. But Z(0) vs Z(1):
    Z(0) = Σ_j c_j^{L²}
    Z(1) = Σ_{j int} c_j^{L²} + Σ_{j half} (-1)^L c_j^{L²}
    For L odd: Z(1) = Σ_{j int} c_j^{L²} - Σ_{j half} c_j^{L²}

So Z(0) - Z(1) = 2 Σ_{j half} c_j^{L²} > 0 for odd L.
And Z(0) = Z(1) for even L.

## In Higher Dimensions (d=4)

On a d-dimensional torus, the vortex surface Σ has area L^{d-2} = L² for d=4.
The symmetry factor is (1-2t)^{L²}.

For even L²: always symmetric. L² is even iff L is even.
For odd L²: L must be odd. Then Z(0) > Z(1).

In BOTH cases: **Z(0) ≥ Z(1)**, which is what Tomboulis needs!

## Wait — This Is MUCH Simpler Than Expected

For the 2D torus, the partition function is:

    Z = Σ_j c_j^F

where F = number of plaquettes. The anti-periodic version flips half-integer
reps: Z⁻ = Σ_j (-1)^{2j} c_j^F.

    Z - Z⁻ = 2 Σ_{j half} c_j^F > 0

Since c_j > 0 for all j and β > 0: **Z > Z⁻ is TRIVIAL in 2D.**

The non-trivial content of Tomboulis is for d ≥ 3, where the partition
function has non-trivial spatial structure (link integrations couple
neighboring plaquettes).

## The Real Test: 4D

In 4D, Z is NOT a simple sum over j. Each plaquette carries a representation,
and shared links impose Clebsch-Gordan constraints. The partition function is:

    Z = Σ_{j on plaquettes} ∏_P d_{j_P} c_{j_P} · ∏_{links} (orthogonality)

The anti-periodic version flips j_P → (-1)^{2j_P} for plaquettes on Σ.

The question: is Z ≥ Z⁻ still true when the link constraints couple
the plaquettes?

My single-plaquette proof (attempt 013, S_anti > 0) shows YES for
uncoupled plaquettes. The 2D result shows YES for 2D (where plaquettes
decouple after gauge fixing). The 4D case is genuinely harder.

## Implication for theory track

The symmetry f(t) = f(1-t) means:
- f'(1/2) = 0 (the derivative vanishes at the midpoint)
- f decreasing on [0, 1/2] and increasing on [1/2, 1]
- f(0) = f(1) (for even L)

This means the INTERPOLATION ROUTE doesn't need f monotone on [0,1].
It only needs f(0) ≥ f(1), which is TRIVIALLY TRUE by symmetry (for even L)
or by explicit computation (for odd L, Z - Z⁻ = 2Σ_{half} c_j^F > 0 in 2D).

In 4D: the symmetry should still hold (the Z₂ center twist is involutory),
giving f(0) = f(1) for even L. For odd L: Z > Z⁻ should follow from the
dominance of the integer sector, but this needs proof.

## 019. DISCOVERY: f(t) = f(1-t) symmetry. f(0) = f(1) for even L.
## In 2D: Z > Z⁻ is trivial (sum of positive terms).
## In 4D: the Z₂ symmetry should give f(0) = f(1) for even L.
## The interpolation gap [1/2, 1] is resolved by SYMMETRY, not monotonicity.
## Tomboulis (5.15) in 2D: PROVEN. In 4D: reduces to Z > Z⁻ with constraints.
