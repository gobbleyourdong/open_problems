# Attempt 046 — The Generator Route: Bypassing the Fierz Cancellation

**Date**: 2026-04-07
**Phase**: 4 (Beyond the Wall — new angle)
**Instance**: Even (Theory)

## The Problem (from attempt_044)

The Fierz identity gives:
  E[⟨∇O, ∇ΔS⟩] = (1/2)⟨chair⟩ - (1/4)⟨plaq·plaq⟩

The leading terms CANCEL. Sign depends on subleading corrections.

## Alternative: Use the Generator Directly

Instead of expanding the inner product, use integration by parts:

  E[⟨∇O, ∇ΔS⟩] = -E[O · L(ΔS)]

where L = Δ + ⟨∇S, ∇·⟩ is the Langevin generator.

## Computing L(ΔS)

ΔS = 2c_{1/2} Σ_{Q∈Σ} χ_{1/2}(U_Q) (truncating at j = 1/2)

### The Laplacian Part

Δ_e χ_{1/2}(U_Q) = -C_{1/2} · χ_{1/2}(U_Q) = -(3/4) χ_{1/2}(U_Q)

for each link e ∈ Q. Each plaquette has 4 links, so:

Δ(ΔS) = 2c_{1/2} · (-3) · Σ_{Q∈Σ} χ_{1/2}(U_Q) = -6c_{1/2} Σ_Σ χ_{1/2}

### The Drift Part

⟨∇S, ∇ΔS⟩ = Σ_e ⟨∇_e S, ∇_e ΔS⟩

This couples the FULL action S to the surface operator ΔS through shared links.
It involves the Hessian of the action and is more complex.

### Combining

L(ΔS) = -6c_{1/2} Σ_Σ χ_{1/2}(U_Q) + ⟨∇S, ∇ΔS⟩

So: E[⟨∇O, ∇ΔS⟩] = 6c_{1/2} E[O · Σ_Σ χ_{1/2}(U_Q)] - E[O · ⟨∇S, ∇ΔS⟩]

## The First Term: Casimir Contribution

6c_{1/2} E[O · Σ_Σ χ_{1/2}(U_Q)]
= 6c_{1/2} [⟨O⟩⟨Σ_Σ χ_{1/2}⟩ + Cov(O, Σ_Σ χ_{1/2})]

Both ⟨O⟩ and ⟨Σ_Σ χ_{1/2}⟩ are positive (character expansion).
Cov(O, Σ_Σ χ_{1/2}) ≥ 0 (spectral positivity, attempt_022).

**First term > 0.** ✓

## The Second Term: Drift Contribution

-E[O · ⟨∇S, ∇ΔS⟩] is the interaction between the full action gradient
and the surface operator gradient, weighted by O.

This is the DIFFICULT term. It involves the same Fierz-type inner products
that led to the cancellation in attempt_044.

## A Key Simplification

At the level of the GENERATOR, we can write:

L(ΔS) = -C_{eff} · ΔS + (interaction term)

where C_{eff} is an effective Casimir modified by the interaction.

For the FREE theory (β = 0): L = Δ, so L(ΔS) = -(3·4)·ΔS = -12·ΔS.
(Wait, I had -6 before. Let me recheck.)

For link e₁ in Q: Δ_{e₁} χ_{1/2}(U_Q) = Δ_{e₁} Tr(U_{e₁} · staple_Q(e₁))

The Laplacian on SU(2) of f(U) = Tr(U · M) is:
Δ f = Σ_a (∂²/∂θ_a²)|_{θ=0} Tr(e^{iθ_a T_a} U M) = -C_{1/2} Tr(U M)

where C_{1/2} = Σ_a (T_a)² = (3/4)I₂ (the quadratic Casimir in the fundamental).

So Δ_{e₁} χ_{1/2}(U_Q) = -(3/4) χ_{1/2}(U_Q). ✓

With 4 links per plaquette: Σ_{e∈Q} Δ_e χ_{1/2}(U_Q) = 4·(-3/4) = -3.
Times 2c_{1/2}: = -6c_{1/2} Σ_Σ χ_{1/2}. ✓ (matches above)

For the INTERACTING theory: the drift ⟨∇S, ∇ΔS⟩ adds a correction.
This correction involves the character expansion coefficients c_j and
the geometry of nearby plaquettes.

## The Net Effect

E[⟨∇O, ∇ΔS⟩] = (positive Casimir term) - (drift interaction term)

The Casimir term is 6c_{1/2} E[O · Σ_Σ χ_{1/2}] > 0 (proved).

The drift term is E[O · ⟨∇S, ∇ΔS⟩]. At strong coupling (small c_j):

⟨∇S, ∇ΔS⟩ = Σ_e Σ_{P∋e, Q∈Σ∩e} (Fierz terms involving c_j)

Each term is O(c_{1/2}) (one factor from ΔS, others from S).
The total drift term is O(c_{1/2}²) (two character expansion factors).

The Casimir term is O(c_{1/2}) × O(c_{1/2}) = O(c_{1/2}²) (from the
⟨O⟩⟨Σ χ⟩ part) plus Cov which is O(c_{1/2}^{dist+2}).

**At strong coupling**: Casimir term ~ 6c_{1/2} · O(c_{1/2}) = O(c_{1/2}²)
Drift term ~ O(c_{1/2}²) (same order)

The NET sign again depends on the COEFFICIENTS. No obvious dominance.

## The Bakry-Émery Connection

The SZZ approach uses Bakry-Émery: Ric - Hess(S) ≥ K > 0 at strong coupling.

For our comparison: we need a modified criterion for comparing TWO measures.
The "comparison Bakry-Émery" criterion:

If Ric - Hess(S) ≥ K > 0 and ΔS is "small" compared to K, then the
comparison E[⟨∇O, ∇ΔS⟩] ≥ 0 follows from spectral gap dominance.

Specifically: at strong coupling, K = (3/4)·4 - C_d·β ≈ 3 (the Ricci
curvature dominates for small β). The perturbation ΔS is O(c_{1/2}·|Σ|).

By the POINCARÉ INEQUALITY with gap K:

|Cov(f, g)| ≤ (1/K) · √(E[|∇f|²]) · √(E[|∇g|²])

The drift interaction term is bounded by (1/K) · ‖∇O‖ · ‖∇²S · ∇ΔS‖.

For K large (strong coupling): the drift term is SUPPRESSED by 1/K.
The Casimir term is NOT suppressed (it's independent of K).

**Therefore**: at strong coupling (K large), the Casimir term DOMINATES.

  E[⟨∇O, ∇ΔS⟩] = (Casimir > 0) - (drift = O(1/K) · small) > 0 ✓

## The Crucial Observation

The Casimir of SU(2) (C_{1/2} = 3/4) provides a POSITIVE MASS for the
gradient correlation. The interaction (drift) is a PERTURBATION that
is controlled by the Bakry-Émery spectral gap.

At strong coupling: spectral gap K is large → drift perturbation small
→ Casimir dominates → gradient correlation positive.

At weak coupling: K → 0 (spectral gap shrinks) → drift perturbation
grows → Casimir may not dominate → gradient correlation sign uncertain.

**This is EXACTLY the strong-coupling limitation of the SZZ approach!**
The Bakry-Émery criterion controls the comparison at strong coupling
but fails at weak coupling.

## Where Does This Leave Us?

The generator approach confirms:
1. At strong coupling: gradient correlation > 0 (Casimir dominates)
   ← This is the same regime as cluster expansion, nothing new.
2. At weak coupling: Casimir vs drift competition, sign unclear
   ← Same wall as before.

## Result

The generator approach provides a CLEAN derivation of why the gradient
correlation is positive at strong coupling (Casimir of SU(2) provides the
positive contribution, interaction is perturbatively small). But it does
NOT extend to weak coupling.

The mass gap at weak coupling remains the frontier. The Casimir contribution
is always positive, but the drift interaction grows relative to it as the
coupling weakens. Whether it ever overtakes the Casimir is the open question.

**The wall persists at weak coupling. The Casimir provides hope (a structural
positive term), but proving it dominates at all couplings requires new ideas.**

## For numerical track

Compute numerically:
1. The Casimir term: 6c_{1/2} · ⟨O · Σ_Σ χ_{1/2}⟩ (should be positive)
2. The drift term: ⟨O · ⟨∇S, ∇ΔS⟩⟩ (sign?)
3. The ratio: Casimir/drift as a function of β
4. Does the Casimir always dominate? Or does the drift overtake at some β?
