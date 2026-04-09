# Attempt 014 — Proving Tomboulis (5.15): The Information-Theoretic Route

**Date**: 2026-04-07
**Phase**: 3 (Proof Attempts)
**Track**: theory (Theory)

## Setup

We want to prove: for SU(2) lattice gauge theory with character expansion
coefficients c_j ∈ [0, 1],

  (∂/∂α) ln Z({c̃(α)}) ≥ (∂/∂α) ln Z⁺({c̃(α)})     ... (*)

where:
- c̃_j(α) = (1-w(α)) c_j^L + w(α) c_j^U is the interpolation
- Z = full partition function (periodic BC)
- Z⁺ = (Z + Z⁻)/2 where Z⁻ has center-twisted BC on one surface
- α parametrizes the coupling strength (larger α = stronger coupling)

## Rewriting (*)

Let S = Σ_P Σ_j d_j c_j χ_j(U_P) be the character expansion part of the action.
Then Z = ∫ ∏ dU · exp(S) and:

  (∂/∂α) ln Z = ⟨∂S/∂α⟩_Z

Similarly: (∂/∂α) ln Z⁺ = ⟨∂S/∂α⟩_{Z⁺}

where ⟨·⟩_Z means expectation under the Z measure and ⟨·⟩_{Z⁺} means
expectation under the Z⁺ = (Z + Z⁻)/2 measure.

Since ∂S/∂α = Σ_P Σ_j d_j (∂c_j/∂α) χ_j(U_P) and ∂c_j/∂α ≥ 0
(interpolation goes from weaker to stronger coupling), we have ∂S/∂α ≥ 0
(a positive operator — the sum of positive characters with positive coefficients).

So (*) becomes:

  ⟨∂S/∂α⟩_Z ≥ ⟨∂S/∂α⟩_{Z⁺}     ... (**)

## What (**) Says

The expectation of a POSITIVE observable (∂S/∂α ≥ 0) is LARGER under the
pure measure than under the mixed measure Z⁺ = (Z + Z⁻)/2.

Since Z⁺ = (Z + Z⁻)/2, we have:

  ⟨∂S/∂α⟩_{Z⁺} = [Z · ⟨∂S/∂α⟩_Z + Z⁻ · ⟨∂S/∂α⟩_{Z⁻}] / (Z + Z⁻)

So (**) becomes:

  ⟨∂S/∂α⟩_Z ≥ [Z⟨∂S/∂α⟩_Z + Z⁻⟨∂S/∂α⟩_{Z⁻}] / (Z + Z⁻)

Multiply both sides by (Z + Z⁻):

  ⟨∂S/∂α⟩_Z · (Z + Z⁻) ≥ Z⟨∂S/∂α⟩_Z + Z⁻⟨∂S/∂α⟩_{Z⁻}

Simplify:

  ⟨∂S/∂α⟩_Z · Z⁻ ≥ Z⁻ · ⟨∂S/∂α⟩_{Z⁻}

Since Z⁻ > 0, divide:

  ⟨∂S/∂α⟩_Z ≥ ⟨∂S/∂α⟩_{Z⁻}     ... (***)

## The Reduced Statement

Inequality (5.15) is equivalent to:

  ⟨∂S/∂α⟩_periodic ≥ ⟨∂S/∂α⟩_anti-periodic     ... (***)

The expectation of the coupling derivative is LARGER with periodic BC
than with anti-periodic (center-twisted) BC.

## Physical Interpretation

∂S/∂α is a positive observable that measures "how much the configuration
benefits from stronger coupling." It's like the "energy" in statistical mechanics.

(***) says: the average energy is higher with periodic BC than anti-periodic BC.

This is intuitively CORRECT for a confining theory:
- Periodic BC: the ground state is the vacuum (maximum plaquette ordering)
- Anti-periodic BC: the ground state contains a center vortex sheet (disorder on Σ)
- The disordered configurations (vortex) have LOWER energy (plaquettes less ordered)
- Therefore ⟨energy⟩_periodic > ⟨energy⟩_anti-periodic ✓

Wait — is this backwards? Let me think more carefully.

∂S/∂α = Σ d_j (∂c_j/∂α) ⟨χ_j(U_P)⟩. This is larger when plaquettes
are more ORDERED (higher character values). Periodic BC allows maximum ordering.
Anti-periodic BC forces a vortex sheet → less ordering → lower ∂S/∂α. YES, correct.

## Can We Prove (***)?

### Attempt A: Convexity Argument

The partition function Z(β) = ∫ exp(β·X) dμ where X = Σ ⟨plaquette terms⟩.
By Jensen's inequality: ⟨X⟩_β = (∂/∂β) ln Z(β).

For two measures μ_per and μ_anti with μ_per dominating μ_anti in the
convex order... but I don't know if this ordering holds.

### Attempt B: Correlation Inequality

If the Wilson lattice measure satisfies FKG-type inequalities (positive
correlations of increasing observables), then:

- ∂S/∂α is an increasing function of the link variables (larger link → larger plaquette)
- The periodic BC measure "dominates" the anti-periodic measure in some sense

For the Ising model, this works: ⟨σ_i⟩_+ ≥ ⟨σ_i⟩_- (plus BC dominates minus BC)
by GKS inequalities.

For gauge theories: the analog would be ⟨χ_j(U_P)⟩_per ≥ ⟨χ_j(U_P)⟩_anti.

**This is a plaquette expectation inequality.** Does periodic BC give higher
plaquette expectations than anti-periodic BC?

YES — this should follow from the MONOTONICITY of Z in the c_j coefficients
(Tomboulis Proposition II.1) combined with the fact that anti-periodic BC
effectively reduces some c_j (the plaquettes on the twisted surface have
reversed characters).

### Attempt C: Direct Proof via Character Expansion

In the character expansion:

  Z_per = Σ_configs ∏_P (d_{j_P} a_{j_P}) · (link integral factors)
  Z_anti = Σ_configs ∏_P (d_{j_P} a_{j_P}') · (link integral factors)

where a_{j_P}' = a_{j_P} for plaquettes not on Σ, and a_{j_P}' = a_{j_P} · (-1)^{2j}
for plaquettes on Σ (the center twist flips the character by (-1)^{2j} for SU(2)).

For SU(2): χ_j(-U) = (-1)^{2j} χ_j(U). So the center twist changes
a_j → (-1)^{2j} a_j for plaquettes on Σ.

For integer j (j = 0, 1, 2, ...): (-1)^{2j} = 1. No change.
For half-integer j (j = 1/2, 3/2, ...): (-1)^{2j} = -1. Sign flip!

**The center twist flips the sign of half-integer representations on Σ.**

So Z_anti has NEGATIVE coefficients for half-integer j on the twisted surface.
This means Z_anti < Z_per (some terms subtracted instead of added).

And ⟨∂S/∂α⟩_anti < ⟨∂S/∂α⟩_per because the negative terms reduce the
plaquette expectation.

## WAIT — Can We Prove This Directly?

Let me write Z_per and Z_anti more carefully.

Let S_Σ = Σ_{P ∈ Σ} Σ_{j half-int} d_j c_j χ_j(U_P) be the half-integer
character part of the action on the twisted surface.

Then:
  Z_per ∝ ∫ exp(S_total) dμ
  Z_anti ∝ ∫ exp(S_total - 2S_Σ) dμ

(The center twist flips sign of half-integer terms on Σ, which is subtracting 2S_Σ.)

Since S_Σ ≥ 0 (positive coefficients times characters, with c_j ≥ 0),
we have S_total - 2S_Σ ≤ S_total, so:

  exp(S_total - 2S_Σ) ≤ exp(S_total)  pointwise

Therefore: Z_anti ≤ Z_per. ✓ (This is trivial — the twisted partition function
is smaller because some positive terms become negative.)

But we need MORE: we need the DERIVATIVE ⟨∂S/∂α⟩_per ≥ ⟨∂S/∂α⟩_anti.

Since ∂S/∂α = Σ_P Σ_j d_j (∂c_j/∂α) χ_j(U_P) and this is a POSITIVE observable
(all terms positive), and the periodic measure gives HIGHER weight to ordered
configurations (where χ_j is larger)...

**Hmm, this is a correlation inequality.** We need:

  ⟨positive observable⟩ is larger under the measure with more positive weight

This is exactly the statement that the measure μ_per STOCHASTICALLY DOMINATES μ_anti
for positive observables.

## The FKG Connection

If the lattice gauge theory measure satisfies the FKG inequality, then
any two increasing events are positively correlated. The periodic BC measure
"adds" positive weight (S_Σ) compared to anti-periodic, making it a "higher"
measure in the FKG lattice.

For the Ising model: GKS gives ⟨f⟩_+ ≥ ⟨f⟩_free ≥ ⟨f⟩_- for any increasing f.

For gauge theories with c_j ≥ 0: the analog should be
⟨f⟩_per ≥ ⟨f⟩_anti for any gauge-invariant increasing observable f.

**This IS Tomboulis Proposition II.1 applied to the comparison of BC!**

## The Proof Structure

1. Z is monotone increasing in each c_j (Tomboulis Prop II.1) ✓ PROVEN
2. Periodic BC corresponds to c_j ≥ 0 on all plaquettes ✓ BY DEFINITION
3. Anti-periodic BC corresponds to c_j → (-1)^{2j} c_j on Σ plaquettes
   → half-integer c_j become NEGATIVE on Σ
4. But wait — Prop II.1 requires c_j ≥ 0 for ALL j. The anti-periodic BC
   introduces NEGATIVE c_j for half-integer j on Σ.
5. The monotonicity argument doesn't directly apply because we're OUTSIDE
   the domain of Prop II.1.

**THIS IS THE GAP.** Prop II.1 gives monotonicity for c_j ≥ 0. The anti-periodic
BC has c_j < 0 for some j on some plaquettes. The comparison Z_per vs Z_anti
goes outside the regime where the proposition is proved.

## Result

The proof of (5.15) reduces to:
**Does the monotonicity Z(c_j) ≤ Z(c_j') for c_j ≤ c_j' extend to the
regime where some c_j are negative?**

Specifically: is Z(c_j ≥ 0) ≥ Z(some c_j < 0, specifically c_{half-int} → -c_{half-int})?

This is NOT covered by reflection positivity (which requires all c_j ≥ 0).
It's a question about the ANALYTIC CONTINUATION of Z outside the RP regime.

This is the EXACT same issue Ito-Seiler identified: the inequality lives
outside the domain where the standard tools (RP, cluster expansion) work.

## Dead End?

Not necessarily. The specific structure (only half-integer j flipped, and only
on a specific surface Σ) is very constrained. The question might be answerable
by representation-theoretic methods specific to SU(2).

For U(1): ALL representations flip (since all are "half-integer" in a sense).
This makes the negative terms dominant at weak coupling → Z_anti can exceed Z_per
in the "energy" comparison → inequality fails → phase transition. ✓ Consistent.

For SU(2): only HALF the representations flip. The integer representations
(j = 0, 1, 2, ...) are unaffected. At weak coupling, the dominant configurations
have large plaquettes (j = 0 dominant), so the flipped half-integer terms are
small → the inequality should hold marginally.

**The margin might be provable from the dominance of j=0 over j=1/2 at weak coupling.**

At weak coupling: a_0(β) = 1, a_{1/2}(β) ≈ 1 - 3/(2β). The difference
1 - a_{1/2} ≈ 3/(2β) → 0 as β → ∞. So the flipped terms contribute O(1/β)
relative to the unflipped terms. This should give (***) with a margin of O(1/β).

**THIS MIGHT BE PROVABLE.** The character expansion at weak coupling is
dominated by j=0, and the flipped half-integer terms are perturbatively small.

## Next Step

Write out the weak-coupling expansion explicitly and verify that (***) holds
to leading order in 1/β. If yes, combine with strong-coupling proof to get
(***) at both extremes. The intermediate region then follows from... something
(continuity? monotonicity in β? a separate argument?)
