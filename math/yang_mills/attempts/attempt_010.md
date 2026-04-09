# Attempt 010 — Convexity Interpolation Route

**Date**: 2026-04-07
**Phase**: 2 (Exploration)
**Instance**: Even (Theory)

## The Idea

The pressure p(β) = (1/V) ln Z(β) is CONVEX in β (standard: log of integral
of exponentials is convex). This is a PROVEN fact for any lattice gauge theory.

We also know:
- p(β) is ANALYTIC for β ∈ (0, β₁) for some β₁ > 0 (Osterwalder-Seiler)
- Mass gap Δ(β) > 0 for β ∈ (0, β₁) (same proof)
- p(β) is SMOOTH (C^∞) for any finite lattice (finite-dim integral of smooth function)

**Question**: Can convexity of p help extend analyticity to all β > 0?

## Analysis

### What convexity gives us
A convex function on an open interval is:
1. Continuous
2. Left and right differentiable everywhere
3. Differentiable except at countably many points
4. If differentiable at a point, C^∞ in a neighborhood? NO — convex ≠ analytic.

A convex function CAN have corners (first-order phase transitions = discontinuity
in p'(β) = ⟨S⟩/V). But it cannot have OSCILLATIONS or non-monotone behavior.

### What convexity does NOT give us
- Analyticity at a point (convex functions can have corners)
- Absence of phase transitions (first-order transitions are corners in convex functions)
- Any control over the mass gap (which relates to correlation functions, not the free energy)

### The interpolation theorem we'd WANT

**Desired theorem**: If a convex function f on (0,∞) is real-analytic on (0,a) and
real-analytic on (b,∞) for some 0 < a ≤ b, then f is real-analytic on (0,∞).

**This is FALSE.** Counterexample: f(x) = max(x, 2-x) is convex, analytic on
(0,1) and (1,∞), but has a corner at x = 1.

So convexity alone does NOT interpolate analyticity. The route needs more structure.

### What WOULD work

If we knew that p(β) has NO CORNERS (no first-order transitions) AND no
higher-order non-analyticities, then p would be analytic everywhere.

Rephrasing: we need to prove p is C^ω (real-analytic), not just convex.
Convexity is a nice property but doesn't close the gap.

### Can we combine convexity with something else?

**Idea A**: Convexity + uniform bound on all derivatives.
If |p^{(n)}(β)| ≤ C^n n! for all n (Cauchy estimate), then p is real-analytic.
The derivatives of p are moments of S_W:
  p'(β) = ⟨S_W⟩/V
  p''(β) = Var(S_W)/V
  p^{(n)}(β) = κ_n(S_W)/V  (cumulants)

If the cumulants satisfy |κ_n| ≤ C^n n! · V, then |p^{(n)}| ≤ C^n n! and
p is analytic. This is essentially the cluster expansion condition —
when cumulants factorize properly (clustering), the generating function is analytic.

So: analyticity of p ⟺ uniform clustering of all correlation functions.
This is CIRCULAR — clustering IS the mass gap.

**Idea B**: Convexity + monotonicity of the mass gap.
If Δ(β) is monotonically decreasing (numerical evidence: YES), then
Δ(β) ≥ lim_{β→∞} Δ(β). If the limit is > 0 (physical mass gap), we win.
But: we don't know the limit is > 0 (that's Gap B).

## Verdict

**Route 3 (convexity interpolation) is WEAKER than I thought.**
Convexity alone doesn't interpolate analyticity. You need clustering bounds
on cumulants, which is the mass gap itself. Circular.

The route survives only if combined with Route 1 (Chatterjee 't Hooft) or
Route 2 (Tomboulis): if either of those proves mass gap at ONE MORE coupling
β*, and we already have it at strong coupling, then the "no phase transition"
argument (attempt_006) kicks in.

## Downgrade

Route 3: ★★★ → ★★ (supporting role only, not standalone)

## A New Observation: The Pressure Is Actually KNOWN

For SU(2) on a finite lattice, the pressure p(β) can be computed exactly
via the character expansion:

  Z(β) = Σ_configs ∏_P (2j_P+1) a_{j_P}(β) · (combinatorial factors)

This is a known function of β. The Odd instance can compute p(β) for small
lattices and study its analyticity properties directly.

For the INFINITE lattice, p(β) = lim_{V→∞} (1/V) ln Z_V(β). The existence
of this limit for all β > 0 is itself a non-trivial result (proven at strong
coupling by OS, conjectured elsewhere).

## Result
Route 3 downgraded — convexity insufficient alone. The key insight is that
analyticity of p ⟺ clustering of correlations ⟺ mass gap. All routes
eventually reduce to the same core question.

The value of this attempt: proving that "shortcut" approaches via thermodynamic
functions don't avoid the hard problem. The mass gap must be proved directly
from the dynamics of the theory (correlation decay, spectral gap of transfer
matrix, or equivalent).
