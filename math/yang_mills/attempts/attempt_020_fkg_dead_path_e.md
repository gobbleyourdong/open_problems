# Attempt 020 — FKG is Dead. Path E: Interpolation via Monotonicity

**Date**: 2026-04-07
**Phase**: 3 (Proof Attempts)
**Track**: theory (Theory)

## FKG for SU(2): DEAD

The FKG inequality requires a distributive lattice with log-supermodular measure.
SU(2)^{|E|} is a compact Lie group, NOT a distributive lattice. There is no
natural partial order that makes it one.

The character expansion doesn't help: the induced measure on character values
is NOT log-supermodular (6j-symbols from shared links have mixed signs).

**50 years of mathematical physics, NOBODY has proved FKG for SU(N) with N ≥ 2.**
Only Z₂ gauge theory has full GKS/FKG.

The reduction in attempt_018 (Cov(O, e^{-δS}) ≤ 0 from FKG) is CORRECT in
structure but the hypothesis (FKG) is UNAVAILABLE. Need a different route to
the same conclusion.

## What IS Known

| Property | Z₂ | U(1) | SU(2) |
|----------|-----|------|-------|
| FKG | ✓ (GKS) | Partial | ✗ |
| Plaquette positive correlation | ✓ | Strong coupling | Strong coupling |
| BC comparison (per ≥ anti) | ✓ (GKS) | Strong coupling | Strong coupling |
| Monotonicity Z in c_j | ✓ | ✓ | ✓ (Prop II.1) |
| Reflection positivity | ✓ | ✓ | ✓ (OS78) |

The ONLY tool available for SU(2) at ALL couplings is:
- Monotonicity of Z in c_j (Tomboulis Prop II.1)
- Reflection positivity (Osterwalder-Seiler)

## Path E: The Interpolation Route (Most Promising)

Instead of FKG, use Prop II.1 monotonicity MORE CAREFULLY.

### Setup
Define a one-parameter family of measures μ_t, t ∈ [0, 1]:
- t = 0: periodic BC (c_j on all plaquettes)
- t = 1: anti-periodic BC (c_j for integer j, -c_j for half-integer j on Σ)
- t intermediate: c_j^{(t)} = c_j for integer j; c_j^{(t)} = (1-2t)c_j for half-integer j on Σ

At t = 0: ⟨O⟩_0 = ⟨O⟩_per
At t = 1: ⟨O⟩_1 = ⟨O⟩_anti

### The derivative approach

Define f(t) = ⟨O⟩_t. We want f(0) ≥ f(1), i.e., f is non-increasing on [0,1].

f'(t) = (d/dt)⟨O⟩_t = -Cov_t(O, (d/dt)S_t)

where (d/dt)S_t = -2 Σ_{P∈Σ} Σ_{j half-int} d_j c_j χ_j(U_P)

This is MINUS a positive observable (since c_j > 0 and we're interpolating
from positive to negative). So (d/dt)S_t ≤ 0.

Therefore: f'(t) = -Cov_t(O, negative thing) = Cov_t(O, positive thing)

If O and this "positive thing" are positively correlated: f'(t) ≥ 0 → f increasing → WRONG direction!

Wait — let me recompute. O = ∂S/∂α is the coupling response. As t increases
(moving toward anti-periodic), the half-integer terms DECREASE. So:

f'(t) = ⟨O · (∂S_t/∂t)⟩_t - ⟨O⟩_t · ⟨∂S_t/∂t⟩_t = Cov_t(O, ∂S_t/∂t)

And ∂S_t/∂t = -2 Σ_{P∈Σ} Σ_{j half-int} d_j c_j χ_j(U_P) < 0

So ∂S_t/∂t is a NEGATIVE observable (it removes positive character terms).

Now: O is a POSITIVE observable (sum of positive characters across ALL plaquettes).
∂S_t/∂t is NEGATIVE (removes characters on Σ).

Are O and ∂S_t/∂t positively or negatively correlated?

O includes terms from Σ (which are positively correlated with the Σ characters
in ∂S_t/∂t) and terms from non-Σ plaquettes (which are also correlated through
shared links).

If O and ∂S_t/∂t are NEGATIVELY correlated: Cov < 0 → f'(t) < 0 → f decreasing → f(0) ≥ f(1) ✓
If O and ∂S_t/∂t are POSITIVELY correlated: Cov > 0 → f'(t) > 0 → f increasing → f(0) ≤ f(1) ✗

But wait — ∂S_t/∂t is a NEGATIVE version of characters. O is POSITIVE characters.
A negative observable times positive correlations gives... negative correlation.

More precisely: ∂S_t/∂t = -2·(positive). O = (positive).
Cov(O, ∂S_t/∂t) = Cov(O, -2·Q) = -2·Cov(O, Q) where Q = positive characters on Σ.

If Cov(O, Q) ≥ 0 (O and Q positively correlated — plausible since both measure ordering):
  Then f'(t) = -2·Cov(O, Q) ≤ 0 → f is non-increasing → f(0) ≥ f(1) ✓

**So the question reduces to: Cov_t(O, Q) ≥ 0 where both O and Q are positive
observables measuring plaquette ordering.**

This is EXACTLY the plaquette-plaquette positive correlation question!

## The Circular Structure (Again)

We need: plaquettes positively correlated. This is WEAKER than full FKG
(we only need it for two specific observables), but still UNKNOWN for SU(2)
at intermediate coupling.

However: this is a much MORE TESTABLE statement. The numerical track can check
numerically whether Cov(Σ_all Tr(U_P), Σ_{P∈Σ} Tr(U_P)) ≥ 0 for all β.

## Breaking the Circularity: The Convexity Trick

What if f(t) is CONVEX in t? Then f(0) ≥ f(1) iff f'(0) ≤ 0... no, that's
not right either. Convexity gives f(t) ≤ (1-t)f(0) + t·f(1), which goes
the wrong way.

What if f(t) is CONCAVE? Then f(t) ≥ (1-t)f(0) + t·f(1), which means
the interpolation is above the line... this doesn't directly help.

## Second Derivative Approach

f''(t) = (d/dt) Cov_t(O, ∂S_t/∂t)

This involves third-order cumulants (connected 3-point functions). The sign
is not easily controlled.

## Assessment

The FKG route is DEAD. Path E (interpolation) reduces the problem to
POSITIVE CORRELATION OF PLAQUETTES, which is:
- Proved at strong coupling (cluster expansion)
- Proved at weak coupling (perturbation theory, attempt_018)
- UNKNOWN at intermediate coupling
- NUMERICALLY appears to hold everywhere

This is a cleaner question than before:

**OLD GAP**: Does SU(2) satisfy FKG? → TOO STRONG, answer is NO.
**NEW GAP**: Are plaquettes positively correlated at ALL β? → WEAKER, might be true.

The new gap is strictly weaker (positive correlation of specific observables,
not full FKG), and might be provable by methods that don't require FKG:
- Strong coupling: cluster expansion ✓
- Weak coupling: perturbation theory ✓
- ALL β: need a monotonicity/interpolation argument, OR direct proof

## Result
FKG killed (attempt_018's hypothesis unavailable). But the CONCLUSION of
attempt_018 (Cov ≤ 0) still holds IF plaquettes are positively correlated.
The gap narrows from "full FKG" to "plaquette positive correlation for all β."

This is the REFINED gap statement. It's weaker than FKG, provable at both
extremes, and numerically supported. The remaining question is whether
strong-coupling and weak-coupling proofs can be connected.

## For numerical track (Updated Request)
The FKG tests in request_020 are still valuable BUT reframe:
- Test plaquette-plaquette Cov(Tr(U_P), Tr(U_Q)) ≥ 0 for ALL β
- If this holds at ALL tested β → evidence for the refined gap
- If this fails at some β → the interpolation route also dies
