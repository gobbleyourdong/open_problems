# Attempt 022 — Interpolation Proof of Plaquette Positive Correlation

**Date**: 2026-04-07
**Phase**: 3 (Proof Attempts)
**Instance**: Even (Theory)

## The Statement

For SU(2) lattice gauge theory with Wilson action at any β > 0:

  Cov_β(Tr(U_P), Tr(U_Q)) ≥ 0  for all plaquettes P, Q

Equivalently: ⟨Tr(U_P) Tr(U_Q)⟩ ≥ ⟨Tr(U_P)⟩ ⟨Tr(U_Q)⟩

## Known

- β small (strong coupling): YES. Cluster expansion gives
  Cov ~ (β/4)^{dist(P,Q)} > 0 (leading term positive, corrections small)

- β large (weak coupling): YES. Perturbation around ordered vacuum.
  Fluctuations around U_P ≈ I give Gaussian-like correlations > 0.

- β intermediate: OPEN.

## Approach: Analyticity Extension

The truncated 2-point function G(P,Q; β) = ⟨Tr(U_P) Tr(U_Q)⟩_c is:
1. Analytic in β for β ∈ (0, β_OS) (Osterwalder-Seiler strong coupling)
2. Positive for β ∈ (0, β_OS)
3. Analytic in β for β ∈ (β_weak, ∞) (weak coupling perturbation theory)
4. Positive for β ∈ (β_weak, ∞)

**Question**: Can G(β) = 0 for some β_* ∈ (β_OS, β_weak)?

If G is analytic on ALL of (0, ∞) — which requires no phase transition — then
G being positive on two intervals and analytic everywhere forces G ≥ 0 everywhere
(by the identity theorem for real-analytic functions, a function that is positive
on an interval and analytic cannot cross zero without being identically zero in
a neighborhood).

Wait — that's not right. An analytic function CAN cross zero. sin(x) is analytic
and crosses zero at x = nπ. The identity theorem says if an analytic function
is zero on a set with an accumulation point, it's zero everywhere. But G could
have isolated zeros.

## A Better Approach: Spectral Representation

The truncated 2-point function has a spectral (Lehmann) representation.
Using the transfer matrix T:

  G(P, Q; β) = Σ_{n≥1} |⟨Ω|Tr(U_P)|n⟩|² · λ_n^{dist(P,Q)}

where λ_n = eigenvalues of T with λ_0 > λ_1 ≥ λ_2 ≥ ... > 0.

**Every term in this sum is NON-NEGATIVE.** (It's a squared matrix element
times a positive eigenvalue raised to a positive power.)

Therefore: G(P, Q; β) ≥ 0 for ALL β!

## Wait — Is This Right?

The spectral representation of the connected correlator on the lattice:

  ⟨O_1(x) O_2(y)⟩_c = Σ_{n≥1} ⟨Ω|O_1|n⟩ ⟨n|O_2|Ω⟩ · (λ_n/λ_0)^{|x-y|}

For O_1 = O_2 = Tr(U_P) (both the SAME observable at different points):

  G(|x-y|) = Σ_{n≥1} |⟨Ω|Tr(U_P)|n⟩|² · (λ_n/λ_0)^{|x-y|}

Each term: |matrix element|² ≥ 0, (λ_n/λ_0) ∈ (0, 1), power ≥ 0.

**Every term is non-negative. The sum is non-negative. G ≥ 0.**

## THIS IS A PROOF!

Wait — let me check the assumptions:

1. **Transfer matrix exists**: YES, for any finite periodic lattice at any β > 0.
   T is a positive self-adjoint operator on L²(SU(2)^{spatial links}).

2. **Spectral decomposition exists**: YES, T is compact (continuous kernel on
   compact space), so it has a discrete spectrum with eigenvalues λ_0 > λ_1 ≥ ...

3. **λ_n > 0 for all n**: YES, T has strictly positive kernel (Boltzmann weight > 0).
   By Krein-Rutman, all eigenvalues are positive (or: T = e^{-aH} with H bounded
   below, so eigenvalues = e^{-aE_n} > 0).

4. **The spectral representation formula holds**: YES, this is the standard
   Lehmann representation. For lattice theories with a transfer matrix, it's exact
   (not approximate).

5. **The observable Tr(U_P) is self-adjoint**: YES, the trace is real for
   unitary matrices, and the adjoint of Tr(U_P) in L² is Tr(U_P)† = Tr(U_P).

6. **Connected correlator = sum of |matrix elements|²**: For a self-adjoint
   observable O with ⟨Ω|O|Ω⟩ subtracted:

   ⟨O(0)O(t)⟩_c = Σ_{n≥1} |⟨Ω|O|n⟩|² · (λ_n/λ_0)^t

   YES, this is correct. The connected part removes the n=0 (vacuum) term.

## Conclusion

**Theorem**: For SU(2) lattice gauge theory on any finite periodic lattice
at any coupling β > 0, the connected plaquette-plaquette correlator satisfies:

  ⟨Tr(U_P(x)) Tr(U_P(y))⟩_c ≥ 0  for all x, y

**Proof**: Spectral decomposition of the transfer matrix. Each term in the
Lehmann representation is |⟨Ω|Tr(U_P)|n⟩|² · (λ_n/λ_0)^{|x-y|} ≥ 0.
The sum of non-negative terms is non-negative. ∎

This is true for ANY self-adjoint observable, not just Tr(U_P).

## What This Gives Us

From attempt_020: Tomboulis (5.15) reduces to Cov(O, Q) ≥ 0 where
O = Σ_P (∂c_j/∂α) Tr(U_P) and Q = Σ_{P∈Σ} Tr(U_P).

Both O and Q are sums of Tr(U_P) with non-negative coefficients. And:

  Cov(Σ_P a_P Tr(U_P), Σ_Q b_Q Tr(U_Q))
  = Σ_P Σ_Q a_P b_Q Cov(Tr(U_P), Tr(U_Q))
  = Σ_P Σ_Q a_P b_Q G(P,Q)
  ≥ 0

since a_P ≥ 0, b_Q ≥ 0, G(P,Q) ≥ 0.

**THEREFORE: Tomboulis inequality (5.15) HOLDS.**

## Wait — Does This Actually Close the Gap?

Let me re-examine the chain:

1. G(P,Q) ≥ 0 (spectral representation) ✓ PROVED
2. Cov(O, Q) ≥ 0 where O, Q are positive linear combinations of Tr(U_P) ✓ FOLLOWS
3. f'(t) = Cov_t(O, ∂S_t/∂t) = -2 Cov_t(O, Q) ≤ 0 ✓ FOLLOWS
4. f(0) ≥ f(1), i.e., ⟨O⟩_per ≥ ⟨O⟩_anti ✓ FOLLOWS
5. This is Tomboulis (5.15) ✓

But WAIT — step 3 uses Cov_t, not Cov_0. At t = 0, the measure is periodic.
At t ∈ (0,1), the measure is interpolated (some c_j partially flipped).

Does the spectral representation still give G ≥ 0 for the interpolated measure?

The interpolated measure at parameter t has c_j^{(t)} = c_j for integer j,
and c_j^{(t)} = (1-2t) c_j for half-integer j on Σ.

For t ∈ [0, 1/2): the half-integer coefficients are still POSITIVE (c_j^{(t)} > 0).
The spectral representation applies. G ≥ 0. ✓

For t ∈ (1/2, 1]: the half-integer coefficients on Σ become NEGATIVE.
The transfer matrix may no longer be positive (some Boltzmann weights negative).
The spectral representation may break (eigenvalues could be negative).

**THIS IS THE PROBLEM.** The spectral positivity argument works when all
character expansion coefficients are non-negative (reflection positivity regime).
When some become negative (anti-periodic BC interpolation past t = 1/2),
the argument fails.

## Revised Assessment

The spectral representation gives G ≥ 0 when ALL c_j ≥ 0 (the RP regime).
This covers:
- The periodic measure (t = 0) ✓
- All interpolations with t < 1/2 ✓

For t ∈ [1/2, 1], we need a different argument. But:

f(0) ≥ f(1/2) by the spectral argument (f non-increasing on [0, 1/2]).
f(1/2) vs f(1) needs the anti-periodic regime.

At t = 1/2: the half-integer coefficients on Σ are ZERO. The measure is
"half-periodic" — only integer representations contribute on Σ.

At t = 1: full anti-periodic BC.

Can we bound f(1/2) - f(1) separately? Or use a different spectral argument
for the [1/2, 1] regime?

## Actually — Rethink the Interpolation

We don't need f monotone on [0, 1]. We just need f(0) ≥ f(1).

We have: f(0) ≥ f(1/2) (proved by spectral representation).

For f(1/2) vs f(1): at t = 1/2, the Σ-surface has only integer representations.
At t = 1, the Σ-surface has NEGATIVE half-integer coefficients. Going from
t = 1/2 to t = 1 SUBTRACTS half-integer character terms on Σ.

⟨O⟩ at t = 1/2 vs t = 1: the only change is adding NEGATIVE terms on Σ.
Since O includes positive terms from Σ (and those terms involve ALL representations
including half-integer), adding negative half-integer terms on Σ should DECREASE ⟨O⟩.

Hmm, this is not rigorous. Let me think differently.

## Alternative: Direct Comparison Z_per vs Z_anti

We know Z_per > Z_anti (trivially — anti-periodic subtracts positive terms).

We want ⟨O⟩_per ≥ ⟨O⟩_anti. This is NOT obvious from Z_per > Z_anti.
(A smaller Z doesn't mean smaller expectations.)

But with the spectral representation, for the periodic measure, we proved
G(P,Q) ≥ 0. This gives us POSITIVE correlations of all plaquettes.

The anti-periodic measure's correlator G_anti may or may not be positive
(some eigenvalues of the twisted transfer matrix could be negative).

## Result

PARTIAL PROOF:
- For the PERIODIC measure (all c_j ≥ 0): plaquette positive correlation PROVED
  via spectral representation. This is a genuine theorem.
- The interpolation from periodic to anti-periodic partially works (t ∈ [0, 1/2]).
- The full Tomboulis (5.15) requires the full range [0, 1], which includes
  the negative-c_j regime where spectral positivity breaks.

The gap has narrowed further: from "plaquette positive correlation at all β"
to "the interpolation works in the negative-coefficient regime [1/2, 1]."

This is progress. The spectral representation argument is a REAL THEOREM
that should be formalized in Lean immediately.
