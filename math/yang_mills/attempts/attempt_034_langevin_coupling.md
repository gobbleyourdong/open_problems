# Attempt 034 — Option D: Langevin Coupling for BC Comparison

**Date**: 2026-04-07
**Phase**: 4 (Beyond the Wall)
**Instance**: Even (Theory)

## The Idea

Use COUPLED stochastic dynamics to compare periodic and anti-periodic measures
directly, bypassing the MK decimation entirely.

The SZZ/Nissim program (arXiv:2204.12737) uses the Langevin dynamics:

  dU_e = ∇_e S(U) dt + c_G U_e dt + √2 dB_e U_e

where S is the Wilson action, B_e is Brownian motion on the Lie algebra,
and c_G is the scalar curvature term. The invariant measure is the Wilson
lattice measure.

**New idea**: Run TWO coupled Langevin processes simultaneously:
- Process 1: drift from S_per (periodic BC action)
- Process 2: drift from S_anti (anti-periodic BC action)
- SAME Brownian motion B_e for both processes

The coupling ensures the processes are "as close as possible."

## The Comparison Dynamics

The difference in drift:

  ∇S_per - ∇S_anti = 2 Σ_{P∈Σ} Σ_{j half-int} d_j c_j ∇χ_j(U_P)

This is localized to the twisted surface Σ and involves only half-integer
character gradients.

Under the coupled dynamics, define:

  Δ(t) = ⟨O⟩_{per}(t) - ⟨O⟩_{anti}(t)

where ⟨·⟩(t) denotes expectation under the process at time t.

At t = 0: start both processes from the SAME initial configuration.
  Δ(0) = 0.

As t → ∞: processes converge to their respective invariant measures.
  Δ(∞) = ⟨O⟩_per - ⟨O⟩_anti (the quantity we want to bound).

## The Evolution of Δ(t)

By the coupling construction:

  dΔ/dt = ⟨O · (∇S_per - ∇S_anti)⟩ + (second order terms from curvature)

The first term involves the covariance of O with the drift difference:

  ⟨O · ∇(S_per - S_anti)⟩ = ⟨O · 2 Σ_{P∈Σ} half-int terms⟩

At the INVARIANT measure level (t → ∞), this is related to the
connected correlator of O with the surface operator. By spectral
positivity (attempt_022, PROVED), this correlator is ≥ 0 for the
periodic measure.

## The Stochastic Domination Argument

If we can show: at EVERY time t ≥ 0, the periodic process has "larger"
character values than the anti-periodic process (in expectation), then:

  Δ(t) ≥ 0 for all t ≥ 0 → Δ(∞) = ⟨O⟩_per - ⟨O⟩_anti ≥ 0 ✓

This is a PATHWISE comparison — if the drift from S_per always pushes
the process to "more ordered" configurations than S_anti, the ordering
is maintained dynamically.

## Where This Approach Could Work

The SZZ framework already has:
- Well-posedness of the Langevin dynamics on SU(N)^|E|
- Exponential mixing (Bakry-Émery at strong coupling)
- Localization of the dynamics (distant links decouple exponentially)

What's NEW: comparing two processes with DIFFERENT drifts using the SAME noise.

This is standard in the theory of STOCHASTIC ORDERING:
- Kamae-Krengel-O'Brien (1977): coupled processes preserve stochastic order
  if the drift satisfies a monotonicity condition
- Lindvall (1992): coupling methods for comparison of Markov chains

The monotonicity condition: ∇S_per ≥ ∇S_anti in an appropriate sense.
Since S_per - S_anti = 2 Σ_{Σ} half-int character terms ≥ 0 in expectation
(spectral positivity), the drift of the periodic process is "larger."

## The Technical Challenge

SU(2) doesn't have a total order, so "stochastic domination" in the
classical sense (Strassen's theorem on partially ordered spaces) doesn't
directly apply.

However: the OBSERVABLE O is real-valued. We need:

  E[O(U^{per}(t))] ≥ E[O(U^{anti}(t))] for all t

This is a comparison of one-dimensional marginals, which is weaker than
full stochastic domination.

**Can we prove this marginal comparison?**

For the coupled dynamics with the same BM:

  d(O(U^{per}) - O(U^{anti})) = ⟨∇O, drift_per - drift_anti⟩ dt
                                 + (noise terms cancel — same BM!)

So: d/dt E[O(U^{per}) - O(U^{anti})] = E[⟨∇O, ∇(S_per - S_anti)⟩]

This expectation is: E[Σ_e (∂O/∂U_e) · (∂(S_per - S_anti)/∂U_e)]

For O = Σ_P w_P Tr(U_P) and S_per - S_anti = 2 Σ_{Σ} half-int terms:

The inner product ⟨∇O, ∇ΔS⟩ involves derivatives of traces of plaquettes
with respect to link variables. These are products of link variables around
plaquettes — gauge-covariant objects.

The SIGN of E[⟨∇O, ∇ΔS⟩] is the key question. If it's ≥ 0, then
Δ(t) is non-decreasing from Δ(0) = 0, giving Δ(∞) ≥ 0. ✓

## Connection to the Wall

E[⟨∇O, ∇ΔS⟩] is a GRADIENT correlation — the covariance of the gradient
of O with the gradient of ΔS.

By the integration-by-parts formula on SU(2)^|E| (Langevin dynamics):

  E[⟨∇O, ∇ΔS⟩]_μ = -E[O · ΔΔS]_μ + E[O · ⟨∇S, ∇ΔS⟩]_μ

where ΔΔS is the Laplacian of ΔS on the group.

The first term involves the Laplacian (Casimir operator) on SU(2), which
is well-understood. The second term involves the gradient-gradient correlation,
which is related to the Hessian of the free energy.

**This is a NEW approach** that uses the differential geometry of SU(2)
rather than the combinatorics of the character expansion. It might bypass
the local-vs-global disconnect that blocks the MK approach.

## Assessment

The Langevin coupling approach is:
- Theoretically motivated (SZZ framework exists)
- Uses different mathematics (stochastic calculus, not cluster expansion)
- Reduces to a SIGN QUESTION about gradient correlations
- Might work at ALL couplings (not limited to strong coupling)

The sign question E[⟨∇O, ∇ΔS⟩] ≥ 0 is a SPECTRAL GEOMETRY question
on SU(2)^|E|. It might be provable using the positive Ricci curvature
of SU(2) (the Bakry-Émery condition) extended to the comparison setting.

## Status: SPECULATIVE but worth pursuing

This is Option D from THEWALL — a genuinely new method that doesn't hit
the MK local-vs-global wall. The key question is whether the Langevin
coupling preserves the observable ordering.

**Rating: ★★★★ (high potential, needs development)**

## For the numerical track

Test numerically: couple two heat bath MC processes (periodic and anti-periodic
BC, same random seeds) and track ⟨O⟩^{per}(t) - ⟨O⟩^{anti}(t) over MC time.
Does the difference remain ≥ 0 at all times?
