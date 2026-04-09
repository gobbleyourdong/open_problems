# Attempt 011 — The Tomboulis Gap: Inequality (5.15)

**Date**: 2026-04-07
**Phase**: 2 (Exploration)
**Instance**: Even (Theory)

## The Exact Gap in Tomboulis (2007)

Tomboulis's proof of confinement for SU(2) in d ≤ 4 has ONE disputed step:

### The Inequality

**Eq. (5.15)**: A_{Λⁿ}(α, r) ≥ A⁺_{Λⁿ}(α, r)

where:
- A = (1/ln F₀ᵁ) · (1/|Λⁿ|) · (d/dα) ln Z_{Λⁿ}({c̃_j})  (pure partition function)
- A⁺ = (1/ln F₀ᵁ) · (1/|Λⁿ|) · (d/dα) ln Z⁺_{Λⁿ}({c̃_j})  (with vortex flux)
- Z⁺ = (Z + Z⁽⁻⁾)/2

**In words**: The free energy per site responds MORE to changes in the
interpolation parameter for the PURE theory than for the theory WITH vortex
flux inserted.

### Where It's Needed

This inequality is used to construct a common interpolation parameter t that
simultaneously reproduces both Z and Z⁽⁻⁾ at each decimation step. Without
it, the implicit function theorem fails: if A⁺ > A, the integrand F(s,t)
diverges before reaching λ = 1, and the construction breaks.

### The Dispute

**Tomboulis says**: After n decimation steps (n large enough), the upper bound
coefficients c_j^U(n) flow to the strong coupling regime (c_j → 0). The exact
coefficients c̃_j are sandwiched between upper and lower bounds, both near 0.
At strong coupling, the inequality is trivially verified by cluster expansion.
So (5.15) is only invoked at strong coupling.

**Ito-Seiler say**: It's not clear the argument correctly restricts to strong
coupling. The number of decimations needed depends on the initial β, and the
uniformity in lattice size (for the thermodynamic limit) is not established.

### The U(1) Test

Ito-Seiler's killer observation: The MK recursion treats U(1) and SU(2)
identically (same decimation formulas). But U(1) in d=4 HAS a phase transition.
So either:
(a) The inequality (5.15) fails for U(1) — which would mean it encodes the
    non-abelian structure, or
(b) The overall argument has a flaw that doesn't depend on (5.15)

If (a), then proving (5.15) for SU(2) but not U(1) would be the KEY step
that distinguishes confining from non-confining theories. This is actually
EXCITING — it means the inequality is the right thing to study.

## Analysis: Is (5.15) True?

### At strong coupling: YES (proven)
When all c_j are small (convergent cluster expansion), both Z and Z⁺ are
close to their free-field values, and the vortex insertion is a small
perturbation. The inequality follows from the expansion.

### At weak coupling: UNKNOWN
When c_j are near 1 (weak coupling), the cluster expansion diverges.
The partition function is dominated by nearly-ordered configurations.
The vortex insertion creates a topological defect that is energetically
costly in the ordered phase. The derivative A measures how sensitive the
free energy is to changing the coupling — this sensitivity should be
LARGER for the pure theory (more configurations available) than for
the vortex-constrained theory.

**Physical intuition says YES**: The pure theory has more "room" to respond
to coupling changes than the topologically constrained theory. But this
needs a proof.

### For U(1): Should FAIL at weak coupling
In the Coulomb phase of U(1), the vortex free energy goes to zero
(vortices are free, not confined). So Z⁽⁻⁾/Z → 1, meaning Z⁺ → Z, meaning
A⁺ → A. The inequality becomes an equality, and the implicit function
construction requires STRICT inequality. This is consistent with the
phase transition existing for U(1).

**Actually**: In the Coulomb phase, the vortex insertion has ZERO cost,
so the with-vortex partition function behaves identically to the without-vortex
one. The inequality A ≥ A⁺ becomes A = A⁺, and the construction fails
because you can't separate the two.

**For SU(2)**: Vortices always cost energy (string tension σ > 0 at all β),
so Z⁽⁻⁾ < Z, hence A > A⁺ (strict). This IS the confinement mechanism.

## The Circular Logic Problem

Wait — this is circular:
- To PROVE confinement, we need A > A⁺
- A > A⁺ essentially SAYS Z⁽⁻⁾ < Z (vortices have a cost)
- Z⁽⁻⁾ < Z IS confinement (area law for the vortex free energy)

So the inequality (5.15) is not an auxiliary technical lemma — it IS the
statement we're trying to prove, repackaged. Tomboulis's proof, at its core,
ASSUMES confinement (at strong coupling) and tries to bootstrap it to all
couplings. The bootstrap mechanism is the MK decimation flow.

The question is: does the MK decimation flow PRESERVE the inequality?
Specifically: if A > A⁺ holds at step n+1 (strong coupling), does it
also hold at step n (slightly weaker coupling)?

## A New Formulation

**Reformulated question**: Is the property "A > A⁺" (equivalently, "vortices
cost energy") preserved under one INVERSE MK decimation step?

If yes: start at strong coupling (where A > A⁺ is proven), and undo
decimation steps one at a time until reaching arbitrary initial β.
Each inverse step preserves A > A⁺.

If no: the Tomboulis approach fails, and we need a different method.

## Assessment

This is a clean, well-defined mathematical question:

**Does the MK decimation RG preserve the strict inequality Z > Z⁺?**

This should be checkable:
1. The MK decimation is explicit (character expansion + Clebsch-Gordan)
2. The inequality Z > Z⁺ is a specific comparison of partition functions
3. The preservation under one RG step is a finite calculation for any
   finite truncation of the character expansion

The Odd instance should:
- Implement the MK decimation for SU(2)
- Track Z and Z⁺ through multiple decimation steps
- Verify whether Z > Z⁺ is preserved or violated
- Test on U(1) (should fail) and SU(2) (should hold)

## Result
The Tomboulis gap is ONE inequality: A ≥ A⁺. It encodes the cost of
vortex insertion. It's true at strong coupling, unknown at weak coupling.
Physically it should hold for SU(2) (always confining) and fail for U(1)
(has Coulomb phase). The question reduces to: does MK decimation preserve
the vortex cost inequality?

This is checkable and well-defined. Upgrading Route 2.
