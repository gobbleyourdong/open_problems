# Attempt 024 — Center Symmetry Decomposition of (5.15)

**Date**: 2026-04-07
**Phase**: 3 (Proof Attempts)
**Track**: theory (Theory)

## Key Idea

The transfer matrix T commutes with the Z₂ center of SU(2). The Hilbert
space decomposes: H = H₊ ⊕ H₋ (center-even and center-odd sectors).

The periodic and anti-periodic partition functions are:

  Z_per = Tr(T^{N_t}) = Tr(T₊^{N_t}) + Tr(T₋^{N_t}) = Z₊ + Z₋
  Z_anti = Tr(T_twist · T^{N_t-1}) = Tr(T₊^{N_t}) - Tr(T₋^{N_t}) = Z₊ - Z₋

where T_twist inserts the center element -I on one temporal slice.

## The Comparison in Terms of Sectors

For a Z₂-EVEN observable O (like Tr(U_P) for a plaquette — center cancels
on closed loops), define:

  ⟨O⟩₊ = Tr(O · T₊^{N_t}) / Z₊   (expectation in even sector)
  ⟨O⟩₋ = Tr(O · T₋^{N_t}) / Z₋   (expectation in odd sector)

Then:
  ⟨O⟩_per = (⟨O⟩₊ Z₊ + ⟨O⟩₋ Z₋) / (Z₊ + Z₋)
  ⟨O⟩_anti = (⟨O⟩₊ Z₊ - ⟨O⟩₋ Z₋) / (Z₊ - Z₋)

## Computing the Difference

  ⟨O⟩_per - ⟨O⟩_anti
  = [(⟨O⟩₊Z₊ + ⟨O⟩₋Z₋)(Z₊ - Z₋) - (⟨O⟩₊Z₊ - ⟨O⟩₋Z₋)(Z₊ + Z₋)]
    / [(Z₊ + Z₋)(Z₊ - Z₋)]

Numerator:
  = ⟨O⟩₊Z₊Z₊ - ⟨O⟩₊Z₊Z₋ + ⟨O⟩₋Z₋Z₊ - ⟨O⟩₋Z₋Z₋
    - ⟨O⟩₊Z₊Z₊ - ⟨O⟩₊Z₊Z₋ + ⟨O⟩₋Z₋Z₊ + ⟨O⟩₋Z₋Z₋   -- WAIT, signs

Let me redo carefully:
  A = ⟨O⟩₊Z₊, B = ⟨O⟩₋Z₋
  S = Z₊ + Z₋, D = Z₊ - Z₋

  ⟨O⟩_per = (A + B)/S
  ⟨O⟩_anti = (A - B)/D

  ⟨O⟩_per - ⟨O⟩_anti = (A+B)/S - (A-B)/D
  = [(A+B)D - (A-B)S] / (SD)
  = [AD + BD - AS + BS] / (SD)
  = [A(D-S) + B(D+S)] / (SD)
  = [A(-2Z₋) + B(2Z₊)] / (SD)
  = 2[-AZ₋ + BZ₊] / (SD)
  = 2[-⟨O⟩₊Z₊Z₋ + ⟨O⟩₋Z₋Z₊] / (SD)
  = 2Z₊Z₋[⟨O⟩₋ - ⟨O⟩₊] / (SD)

Since Z₊ > 0, Z₋ > 0 (positive transfer matrix eigenvalues), and
S = Z_per > 0, D = Z_anti > 0 (both partition functions positive):

  **Sign(⟨O⟩_per - ⟨O⟩_anti) = Sign(⟨O⟩₋ - ⟨O⟩₊)**

## The Reformulation

**Tomboulis (5.15) is equivalent to:**

  ⟨O⟩₋ ≥ ⟨O⟩₊

The expectation of the coupling response O in the Z₂-ODD sector is ≥ the
expectation in the Z₂-EVEN sector.

## Physical Interpretation

H₊ = center-even states: vacuum, 0⁺⁺ glueball, 2⁺⁺ glueball, ...
H₋ = center-odd states: electric flux string, 0⁻⁺ glueball, ...

⟨O⟩₊ = average plaquette ordering in the center-even (vacuum-like) sector
⟨O⟩₋ = average plaquette ordering in the center-odd (string-like) sector

(5.15) says: the string sector has HIGHER average plaquette ordering than
the vacuum sector.

This is... counterintuitive? The vacuum should be the MOST ordered state.

Wait — let me reconsider. O is the COUPLING RESPONSE ∂S/∂α, not the
plaquette itself. This measures how much the free energy changes when the
coupling increases. The string sector might respond MORE to coupling changes
because it has more room to order (it starts less ordered and gains more
from increased coupling).

Actually, I think the sign might be WRONG. Let me recheck.

## Sanity Check at Strong Coupling

At strong coupling (β → 0): all plaquettes are disordered. ⟨Tr(U_P)⟩ ≈ 0.
The difference between sectors is exponentially small.

⟨O⟩₊ ≈ ⟨O⟩₋ ≈ 0. The difference is O(β^{P_Σ}) where P_Σ is the number of
plaquettes on the twisted surface. Both are positive. The sign of the
difference depends on the specific cluster expansion coefficients.

From the Osterwalder-Seiler proof: at strong coupling, (5.15) holds.
So ⟨O⟩₋ ≥ ⟨O⟩₊ at strong coupling. ✓

## Sanity Check at Weak Coupling

At weak coupling (β → ∞): plaquettes are nearly I.

In the vacuum sector (H₊): the ground state has all plaquettes ≈ I.
Small fluctuations. ⟨Tr(U_P)⟩₊ ≈ 2 - O(1/β).

In the string sector (H₋): there must be a center vortex somewhere.
This vortex forces some plaquettes away from I.
⟨Tr(U_P)⟩₋ ≈ 2 - O(1/β) for plaquettes far from the vortex,
but ≈ 2 - O(1) for plaquettes near the vortex.

Wait, but the AVERAGE over all plaquettes: the string sector has a
vortex sheet that costs energy. The average plaquette is LOWER in
the string sector: ⟨O⟩₋ < ⟨O⟩₊.

This would give ⟨O⟩_per - ⟨O⟩_anti < 0. That's the WRONG sign for (5.15)!

## ERROR CHECK

Did I get the algebra wrong? Let me recompute with explicit numbers.

At weak coupling, large β:
  Z₊ = e^{-E₀ N_t} (1 + ...) ≈ e^{-E₀ N_t}  (vacuum dominates)
  Z₋ = e^{-E₁ N_t} (1 + ...) ≈ e^{-E₁ N_t}  (lightest odd state)

where E₀ = 0 (vacuum energy) and E₁ = Δ (mass gap).

So Z₊ >> Z₋ at large N_t (mass gap suppresses odd sector).

  Z_per = Z₊ + Z₋ ≈ Z₊
  Z_anti = Z₊ - Z₋ ≈ Z₊

And:
  ⟨O⟩_per ≈ ⟨O⟩₊ (vacuum sector dominates)
  ⟨O⟩_anti ≈ ⟨O⟩₊ (also vacuum dominates, since Z₋/Z₊ → 0)

The difference is exponentially small: O(e^{-ΔN_t}).

So the question of SIGN is about the O(e^{-ΔN_t}) correction, not the
leading behavior. The leading term cancels.

## Corrected Analysis

⟨O⟩_per - ⟨O⟩_anti = 2Z₊Z₋(⟨O⟩₋ - ⟨O⟩₊) / (Z_per · Z_anti)

At large N_t: Z₊Z₋ / (Z_per Z_anti) ≈ Z₋/Z₊ = e^{-ΔN_t}

So: ⟨O⟩_per - ⟨O⟩_anti ≈ 2e^{-ΔN_t} · (⟨O⟩₋ - ⟨O⟩₊)

For (5.15): we need this to be ≥ 0, i.e., ⟨O⟩₋ ≥ ⟨O⟩₊.

BUT: what is O here? O = ∂S/∂α where α is the MK interpolation parameter.
This is NOT the same as the plaquette trace. It's the response of the
free energy to coupling changes.

Let me reconsider what O actually measures. In Tomboulis's framework:

O = Σ_P Σ_j d_j (∂c_j/∂α) χ_j(U_P)

where ∂c_j/∂α > 0 (interpolation from weak to strong). This IS a sum of
character traces with positive coefficients. So it's similar to the plaquette
but weighted by (∂c_j/∂α).

The question ⟨O⟩₋ ≥ ⟨O⟩₊ asks: does the odd sector have larger
character-weighted plaquette expectation?

At strong coupling: both sectors have similar expectations (disorder), and
the difference is calculable by cluster expansion. (5.15) holds. ✓

At weak coupling: the odd sector is dominated by the lightest Z₂-odd state
(a glueball with odd center charge, or a wrapped flux tube). This state
has a DIFFERENT spatial profile from the vacuum.

Whether ⟨O⟩₋ > ⟨O⟩₊ at weak coupling is a specific spectral question
about the transfer matrix.

## A Different Route: Large N_t Limit

In the large N_t limit (zero temperature):

  ⟨O⟩_per → ⟨O⟩₊ → ⟨0|O|0⟩  (vacuum expectation)
  ⟨O⟩_anti → ⟨O⟩₊  (also vacuum, since odd sector exponentially suppressed)

So ⟨O⟩_per - ⟨O⟩_anti → 0 exponentially fast. (5.15) is TRIVIALLY satisfied
(with ≥ 0 as the difference → 0⁺).

**At finite N_t**: the difference is O(e^{-ΔN_t}) and the sign depends on
⟨O⟩₋ vs ⟨O⟩₊. But the MASS GAP Δ > 0 ensures the difference vanishes
in the infinite-volume limit.

## THE REALIZATION

Tomboulis's argument operates at FINITE lattice volume. He takes the
thermodynamic limit AFTER establishing the inequality. At finite volume,
the mass gap is ALWAYS positive (Krein-Rutman). So Z₊ > Z₋ > 0.

The inequality (5.15) at finite volume, for the EXACT interpolated
coefficients (which are in the strong-coupling regime after enough
decimation steps), is verified by the strong-coupling cluster expansion.

**Tomboulis's own argument that (5.15) is only needed at strong coupling
is correct, PROVIDED the decimation correctly flows to strong coupling.**

The decimation flow is controlled by the sandwich theorem (MKDecimation.lean):
the exact coefficients are between upper and lower bounds that both → 0.

## Revised Assessment

The center decomposition doesn't directly prove (5.15), but it reveals:

1. At infinite volume (N_t → ∞): (5.15) is TRIVIALLY true (difference → 0⁺)
2. At finite volume: (5.15) depends on ⟨O⟩₋ vs ⟨O⟩₊, which is a spectral question
3. After MK decimation: the theory is at strong coupling where (5.15) is proven

The REAL question is whether Tomboulis's argument correctly handles the
order of limits (decimation → thermodynamic limit → continuum limit).

This is the Ito-Seiler critique in a nutshell: the order of limits matters,
and Tomboulis doesn't clearly establish uniformity.

## Result

The center decomposition reformulates (5.15) as ⟨O⟩₋ ≥ ⟨O⟩₊ (odd sector
has higher coupling response than even sector). This is:
- Trivially true at infinite N_t (both → vacuum value)
- True at strong coupling (cluster expansion)
- A finite-volume spectral question in general

The UNIFORMITY in volume is the remaining issue — the same one Ito-Seiler
flagged. The center decomposition doesn't solve it but clarifies what it is.

## Next: What Would Actually Close the Gap

The gap would close if we could prove:
(a) ⟨O⟩₋ ≥ ⟨O⟩₊ for the EXACT interpolated coefficients at FINITE volume, OR
(b) The MK decimation flow to strong coupling is UNIFORM in volume, OR
(c) A completely different proof of (5.15) that doesn't need the MK framework

Option (b) is what Tomboulis claims and Ito-Seiler disputes. The dispute is
about whether "the coefficients being sandwiched near zero" is sufficient for
the cluster expansion to work uniformly in volume.
