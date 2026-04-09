# Attempt 013 — Why SU(2) Confines and U(1) Doesn't: The Algebraic Core

**Date**: 2026-04-07
**Phase**: 2 (Exploration — deep theory)
**Track**: theory (Theory)

## The Question

Tomboulis inequality (5.15) should hold for SU(2) but fail for U(1).
WHY? What algebraic property of SU(2) makes vortices always cost energy?

## The Vortex Free Energy

For a lattice with a non-contractible surface Σ, the vortex partition function
Z⁻ is the partition function with anti-periodic BC for the center element:

  Z⁻ = ∫ ∏ dU · exp(-β S_W) · ∏_{ℓ crossing Σ} (-1)

For SU(2): center = Z₂ = {I, -I}. The twist is multiplication by -I on links
crossing Σ. This changes U_P → -U_P for plaquettes with one link on Σ.

The vortex free energy: F_v = -ln(Z⁻/Z)

- F_v > 0: vortex costs energy → confinement
- F_v = 0: vortex is free → deconfinement
- F_v ~ Area(Σ): area law → string tension σ > 0

## For U(1)

Center of U(1) = U(1) itself (abelian). A "vortex" is a twist by e^{iθ}.
The Boltzmann weight for a plaquette: exp(β cos(θ_P + θ_twist))

At strong coupling (small β): cos(θ_P) ≈ 1 - θ_P²/2. The twist θ_twist
costs energy ~ β θ_twist². Vortices are suppressed → confinement.

At weak coupling (large β): the partition function is dominated by
configurations where θ_P ≈ 0 mod 2π. A twist by 2π costs NOTHING
because cos is periodic. The vortex can be "absorbed" by a smooth
gauge transformation → vortex is free → deconfinement.

**The key**: U(1) admits smooth deformations that absorb the vortex.
The periodicity of the cosine means large gauge transformations are free.

## For SU(2)

Center = Z₂ = {I, -I}. A center vortex twists by -I.

At strong coupling: vortex costs energy (same as U(1)). Confinement.

At weak coupling: the plaquettes are nearly I. A twist by -I on a link
changes the plaquette from ≈ I to ≈ -I. The action cost is:
  β(1 - Re Tr(U_P)/2) → β(1 - Re Tr(-I)/2) = β(1 - (-1)) = 2β

This is a LARGE cost, proportional to β. The twist CANNOT be absorbed
by a smooth gauge transformation because -I ≠ I in SU(2)/Z₂ = SO(3),
and the vortex represents a non-trivial element of π₁(SO(3)) = Z₂.

**The key**: SU(2) does NOT have the periodicity that U(1) has. The
center element -I is topologically distinct from I. There is no smooth
deformation that absorbs the center twist.

## The Topological Obstruction

For U(1): π₁(U(1)) = Z. Vortices can have arbitrary winding number.
At weak coupling, integer windings are free (lattice artifact disappears
in continuum). The deconfinement transition is driven by the delocalization
of these vortices.

For SU(2): π₁(SU(2)) = 0 (simply connected!). But π₁(SU(2)/Z₂) = Z₂.
Center vortices represent the non-trivial element of Z₂. They carry a
Z₂ charge that CANNOT be screened or delocalized. Each vortex costs
energy proportional to its area.

**This is why SU(2) confines**: center vortices always cost energy because
the Z₂ topological charge cannot be smoothly removed.

## Translating to Tomboulis's Framework

In the MK decimation, the coefficients c_j map the theory toward strong
coupling at each step. The question is whether the decimation preserves
Z > Z⁺ (= (Z + Z⁻)/2).

For SU(2): At each decimation step, the vortex cost F_v > 0 should be
preserved because:
1. The decimation is a coarse-graining that averages over UV modes
2. The center vortex is an IR property (lives on non-contractible surfaces)
3. Coarse-graining removes UV fluctuations but preserves IR topology
4. The Z₂ charge of the vortex is topological → survives coarse-graining

For U(1): The decimation might destroy the vortex cost because:
1. U(1) vortices with winding number n can decay to n=0 via smooth deformations
2. The decimation's coarse-graining can smooth out the vortex
3. At weak coupling, the decimation-renormalized theory can be in the Coulomb phase

## The Conjecture, Refined

**Conjecture (refined Tomboulis 5.15)**: For SU(N) lattice gauge theory with
N ≥ 2, the center vortex free energy F_v = -ln(Z⁻/Z) satisfies:

  F_v({c̃_j(n)}) ≥ F_v({c̃_j(n-1)}) · (some positive function of the decimation)

That is: the vortex cost is PRESERVED (or even enhanced) under MK decimation.

This should hold because:
1. The MK decimation flows toward strong coupling
2. At strong coupling, F_v ~ Area(Σ) · (-ln(β/4)) grows
3. The vortex cost in the original theory is a LOWER bound on the vortex cost
   in the decimated theory (stronger coupling = more confinement)

**Wait — is this obvious?**

If the exact coefficients c̃_j are sandwiched between bounds that both flow
to strong coupling, and F_v is monotone increasing as coupling strengthens...
then F_v should increase under decimation!

The question is: **is F_v monotone in the character expansion coefficients?**

## Is F_v Monotone?

F_v = -ln(Z⁻/Z) = ln Z - ln Z⁻

If BOTH Z and Z⁻ are increasing in each c_j (Tomboulis Proposition II.1),
but Z increases FASTER than Z⁻, then F_v = ln Z - ln Z⁻ increases too.

This requires: (∂/∂c_j) ln Z ≥ (∂/∂c_j) ln Z⁻ for all j.

In words: the pure theory's free energy responds MORE to coupling changes
than the vortex theory's free energy. This IS inequality (5.15)!

So the question is: is the response of Z to c_j always larger than the
response of Z⁻? And the answer relates to whether the center vortex
REDUCES the number of accessible configurations (constrains the phase space).

## Physical Argument

The vortex insertion forces one link per column to carry the center element -I.
This is a CONSTRAINT. A constrained system has FEWER configurations and is
LESS responsive to parameter changes. Therefore:

  (∂/∂c_j) ln Z⁻ ≤ (∂/∂c_j) ln Z

because the unconstrained system (Z) has more room to respond.

This is essentially a convexity / information-theoretic argument:
more constraints → less entropy → less sensitivity to coupling.

**Can this be made rigorous?**

For the Ising model: the constrained partition function (fixed boundary spins)
is indeed less sensitive to coupling changes than the free partition function.
This follows from the GKS inequalities.

For gauge theories: the analog would need the gauge-theory GKS inequalities
(Tomboulis Proposition II.1 + something more). The "something more" is the
key step that Ito-Seiler says is missing.

## Result
The algebraic reason for SU(2) confinement: π₁(SU(2)) = 0 prevents vortex
absorption by smooth deformations. The Z₂ center charge is topological.

The monotonicity question (is F_v increasing with coupling?) reduces to:
constrained systems are less responsive than unconstrained systems.

This is a NATURAL property that should follow from information-theoretic /
convexity arguments, but the rigorous proof for gauge theories is the
open problem.

## Next Steps
1. Formalize the argument: Z constrained ≤ Z free in response to c_j
2. Check if Tomboulis's Proposition II.1 (Z monotone in c_j) extends to
   a COMPARISON between Z and Z⁻
3. Study the information-theoretic formulation: relative entropy, Fisher
   information, Cramér-Rao type bounds
