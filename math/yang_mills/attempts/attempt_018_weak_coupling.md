# Attempt 018 — Weak Coupling Expansion of (5.15)

**Date**: 2026-04-07
**Phase**: 3 (Proof Attempts)
**Instance**: Even (Theory)

## Goal

Prove ⟨∂S/∂α⟩_per ≥ ⟨∂S/∂α⟩_anti at WEAK coupling (large β).

From attempt_016: the center twist flips half-integer j on surface Σ.
At weak coupling, the character expansion is dominated by j=0 (trivial rep).
The flipped terms should be perturbatively small.

## Setup

SU(2) character expansion on a lattice with P plaquettes, of which P_Σ
lie on the twisted surface Σ. The action is:

  S = Σ_{P not on Σ} Σ_j d_j c_j χ_j(U_P) + Σ_{P on Σ} Σ_j d_j c_j^{(σ)} χ_j(U_P)

where:
- Periodic BC: c_j^{(σ)} = c_j for all j
- Anti-periodic BC: c_j^{(σ)} = (-1)^{2j} c_j = c_j for integer j, -c_j for half-integer j

## The Observable

∂S/∂α = Σ_P Σ_j d_j (dc_j/dα) χ_j(U_P) ≥ 0

(since dc_j/dα ≥ 0 for the interpolation from weak to strong coupling).

## Weak Coupling Regime (β → ∞)

At large β, the dominant contributions come from j = 0:
  c_0(β) = 1 (always)
  c_{1/2}(β) = 1 - 3/(2β) + O(1/β²)
  c_1(β) = 1 - 5/β + O(1/β²)

All c_j → 1 as β → ∞. The partition function is dominated by ordered
configurations where all U_P ≈ I.

## Perturbative Expansion

Write c_{1/2} = 1 - ε where ε = 3/(2β) (small at large β).

**Periodic BC**: All plaquettes use c_{1/2}.
  S_per = Σ_P [1·χ_0 + 2(1-ε)χ_{1/2} + 3(1-5ε/3)χ_1 + ...]

**Anti-periodic BC**: Plaquettes on Σ use -c_{1/2} = -(1-ε).
  S_anti = S_per - 2·Σ_{P∈Σ} [2(1-ε)χ_{1/2} + 2·...] (subtracting twice the half-int part)

Wait, let me be more precise. The anti-periodic BC changes
c_{1/2} → -c_{1/2} on Σ. The DIFFERENCE in action is:

  δS = S_per - S_anti = 2·Σ_{P∈Σ} Σ_{j half-int} d_j c_j χ_j(U_P)

At leading order (j = 1/2 only):
  δS ≈ 2·Σ_{P∈Σ} 2·c_{1/2}·χ_{1/2}(U_P) = 4(1-ε)·Σ_{P∈Σ} χ_{1/2}(U_P)

## The Key Comparison

⟨∂S/∂α⟩_per - ⟨∂S/∂α⟩_anti = ?

Let O = ∂S/∂α (the positive observable). We need ⟨O⟩_per ≥ ⟨O⟩_anti.

  ⟨O⟩_per = ∫ O·exp(S_per)dμ / ∫ exp(S_per)dμ
  ⟨O⟩_anti = ∫ O·exp(S_per - δS)dμ / ∫ exp(S_per - δS)dμ

Let p(U) = exp(S_per)/Z_per be the periodic measure. Then:

  ⟨O⟩_anti = ⟨O·exp(-δS)⟩_per / ⟨exp(-δS)⟩_per

So:
  ⟨O⟩_per - ⟨O⟩_anti = ⟨O⟩_per - ⟨O·e^{-δS}⟩/⟨e^{-δS}⟩

  = [⟨O⟩⟨e^{-δS}⟩ - ⟨O·e^{-δS}⟩] / ⟨e^{-δS}⟩

  = -Cov_per(O, e^{-δS}) / ⟨e^{-δS}⟩

Now, δS ≥ 0 (it's a sum of positive character terms with c_j ≥ 0 times
positive characters evaluated on ordered plaquettes). So e^{-δS} ≤ 1.

**The sign of the covariance**: We need Cov(O, e^{-δS}) ≤ 0, i.e.,
O and e^{-δS} are NEGATIVELY correlated.

O = ∂S/∂α is large when plaquettes are ordered (high character values).
δS is large when plaquettes ON Σ are ordered (high character values).
So e^{-δS} is SMALL when plaquettes on Σ are ordered.

Since O includes contributions from plaquettes on Σ (which are positively
correlated with the rest), O and e^{-δS} should be negatively correlated:
when O is large (ordered), e^{-δS} is small (also because of ordering on Σ).

**Negative correlation → Cov(O, e^{-δS}) ≤ 0 → ⟨O⟩_per ≥ ⟨O⟩_anti. ✓**

## Is This a Proof?

The argument requires: Cov_per(O, e^{-δS}) ≤ 0.

This is a statement that O and e^{-δS} are negatively correlated.
Since O is an INCREASING function of the plaquette ordering and e^{-δS}
is a DECREASING function (of the plaquette ordering on Σ), this is
exactly the FKG inequality IF the periodic measure satisfies FKG.

**Does the SU(2) lattice gauge theory measure satisfy FKG?**

For ABELIAN theories (Z₂, U(1)): YES, the FKG inequality holds.
The lattice is a distributive lattice and the Boltzmann weight is
log-supermodular.

For NON-ABELIAN theories (SU(2)): The FKG framework requires a partial
order on configurations. For group-valued variables, there is no natural
partial order. FKG does NOT directly apply.

**However**: In the character expansion, the relevant variables are the
character values {χ_j(U_P)}, not the group elements. The characters
ARE real-valued and can be ordered. If we can show:

1. The character values {χ_j(U_P)} are positively correlated under the
   periodic measure (plaquettes that are ordered tend to be near
   plaquettes that are also ordered), AND

2. O is an increasing function of the characters, AND

3. e^{-δS} is a decreasing function of the characters on Σ

Then Cov(O, e^{-δS}) ≤ 0 follows from (1).

**Positive correlation of characters** (item 1) is the LATTICE GAUGE THEORY
GKS INEQUALITY. This is KNOWN for the Wilson action with c_j ≥ 0
(Tomboulis Proposition II.1, Brydges-Fröhlich-Seiler).

So the argument IS:
1. Characters are positively correlated (Prop II.1 / RP) ✓
2. O is increasing in characters ✓ (it's a sum of positive character terms)
3. e^{-δS} is decreasing in characters on Σ ✓ (δS is increasing → e^{-δS} decreasing)
4. Therefore Cov(O, e^{-δS}) ≤ 0 ✓ (positive correlation of characters)
5. Therefore ⟨O⟩_per ≥ ⟨O⟩_anti ✓ (from the covariance formula)
6. Therefore inequality (5.15) holds ✓

## WAIT — Is Step 4 Valid?

Step 4 says: if X and Y are such that X is increasing in a set of
positively correlated variables, and Y is decreasing in those variables,
then Cov(X, Y) ≤ 0.

This is exactly the FKG inequality: for a measure with positive correlations,
increasing functions are positively correlated with increasing functions,
and increasing functions are negatively correlated with decreasing functions.

**BUT**: FKG requires the measure itself to satisfy a lattice condition
(log-supermodularity). The question is whether the character-expansion-
based reformulation of the gauge theory measure satisfies this.

For the Wilson lattice measure in terms of CHARACTER VALUES (not group
elements): the measure is

  dμ ∝ exp(Σ_P Σ_j d_j c_j χ_j(U_P)) · ∏_P dU_P · (link constraint)

The link constraint (from integrating out shared links) couples different
plaquettes. This coupling is what makes the FKG condition non-trivial.

**The character expansion decouples the measure IF we treat the link
integrals as independent.** But they're NOT independent — links are shared
between plaquettes.

This is where Tomboulis's Proposition II.1 comes in: it proves
monotonicity (which is related to but not identical to FKG) for the
specific structure of the gauge theory measure.

## Assessment

The argument is ALMOST a proof. The gap is:

**Does Tomboulis's Proposition II.1 (monotonicity of Z in c_j) imply
the FKG property needed for Cov(O, e^{-δS}) ≤ 0?**

Monotonicity of Z says: increasing all c_j increases Z.
FKG says: expectations of increasing functions are positively correlated.

These are DIFFERENT properties. Monotonicity is a GLOBAL property (Z goes up).
FKG is a LOCAL property (expectations of products factorize with the right sign).

In general: monotonicity does NOT imply FKG. But for measures with the
specific structure of lattice gauge theories, it MIGHT.

## The Remaining Gap (Refined)

Tomboulis inequality (5.15) would follow from the FKG property of the
lattice gauge theory measure in the character expansion basis.

**Is the SU(2) Wilson lattice measure FKG in the character basis?**

This is a cleaner, more specific question than before. It might have a
known answer in the lattice gauge theory literature.

## Result
Reduced (5.15) to:
  Cov_per(O, e^{-δS}) ≤ 0
which follows from FKG in the character basis.
FKG for gauge theories is STRONGER than monotonicity (Prop II.1) but
related. The question is precise and may have a known answer.

## For numerical track
Verify numerically: Cov(O, e^{-δS}) < 0 for SU(2) on 2⁴ lattice at
various β. This is a single MC measurement.
