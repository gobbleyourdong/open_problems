# results/vacuum_energy_findings.md — Vacuum Energy: The Cosmological Constant Problem

**Date:** 2026-04-09
**Script:** `numerics/vacuum_energy.py`
**Setup:** Standard QFT calculation, Planck/EW/QCD cutoffs; Casimir effect; de Sitter temperature

## Setup

PROBLEM.md asks: what is nothing? The quantum vacuum is not nothing — it has energy,
measurable effects, and its own temperature. But the discrepancy between the QFT prediction
for its energy density and the observed cosmological constant is the largest known numerical
discrepancy in all of physics.

## Full Results

### Physical scales

| Quantity | Value |
|---|---|
| Planck length | 1.616×10⁻³⁵ m |
| Planck energy | 1.956×10⁹ J = 1.221×10²⁸ eV |
| Planck density | 5.155×10⁹⁶ kg/m³ = 4.64×10¹¹³ J/m³ |

### Observed vacuum energy density (from Λ, Planck 2023)

| Quantity | Value |
|---|---|
| Cosmological constant Λ | 1.106×10⁻⁵² m⁻² |
| ρ_Λ = Λc²/(8πG) | 5.924×10⁻²⁷ J/m³ |
| In eV/m³ | 3.70×10⁻⁸ eV/m³ |
| As fraction of ρ_Planck | 1.149×10⁻¹²³ |

### QFT predictions (zero-point energy sum, 2 photon modes)

| Cutoff | ρ_QFT (J/m³) | Gap vs observed |
|---|---|---|
| Planck scale (1.22×10²⁸ eV) | 2.934×10¹¹¹ | 10^137.7 |
| Electroweak scale (100 GeV) | 1.321×10⁴³ | 10^69.3 |
| QCD scale (200 MeV) | 2.113×10³² | 10^58.6 |

**Caveat on 10^137.7:** This uses 2 photon polarizations only (no SM fermion cancellation,
no reduced Planck mass). The commonly cited "10^120" figure uses particle physics natural units
comparing the 4th root of the energy density: (ρ_obs^(1/4) ≈ meV) vs (ρ_P^(1/4) ≈ 10^28 eV),
giving (10^28/10^-3)^4 ≈ 10^124. With slightly different cutoffs and conventions: 10^120–123.
All conventions agree: the gap is enormous.

### Casimir effect (real, measured vacuum energy)

| Plate separation | Casimir pressure |
|---|---|
| 1 nm | -1.300×10⁹ Pa = -12,831 atm |
| 10 nm | -1.300×10⁵ Pa = -1.28 atm |
| 100 nm | -13.0 Pa = -1.28×10⁻⁴ atm |
| 1 µm | -1.3×10⁻³ Pa = -1.28×10⁻⁸ atm |

The Casimir force at 10 nm plate separation is ~1 atmosphere — large and measurable.
The vacuum is not empty: it has a physical pressure between conducting plates.
First measured (Lamoreaux 1997, Mohideen 1998); now confirmed at sub-percent precision.

### De Sitter temperature of the vacuum

T_dS = ħc√(Λ/3)/(2πk_B) = 2.21×10⁻³⁰ K

The vacuum has a Gibbons-Hawking temperature from the cosmological horizon, analogous to
Hawking radiation from black holes. This temperature is 1.23×10³⁰ × colder than the CMB.
It is unmeasurable in any foreseeable experiment, but is theoretically nonzero.

### K-information framing

| Quantity | Value |
|---|---|
| SM Lagrangian (compact notation) | ~2000 characters |
| Planck-scale modes per m³ | ~2.37×10¹⁰⁴ |
| K-ratio (spec/modes) | ~8.4×10⁻¹⁰² |

The vacuum is the most extreme example of the S/K bifurcation from `what_is_information`:
- K-poor: described by ~2000 characters of SM Lagrangian
- S-rich: ~10^104 quantum fluctuation modes per cubic meter at Planck scale

## Finding 1: The vacuum is not nothing

Three independent measures show the vacuum has physical reality:
1. **Casimir pressure**: attractive force between plates from vacuum fluctuations (measured)
2. **Lamb shift**: electron energy levels shift due to vacuum fluctuations (measured)
3. **Dark energy / Λ**: the observed vacuum energy density (5.924×10⁻²⁷ J/m³) accelerates
   the universe's expansion (measured, Nobel Prize 2011)

The quantum vacuum is a sea of zero-point fluctuations. "Nothing" in physics means "lowest
energy state of all quantum fields" — and that lowest state has energy, pressure, and temperature.
Genuine metaphysical nothingness (no fields, no laws, no possibility) is not accessible from
within QFT. The question "why is there something rather than nothing" cannot be answered by
pointing to the vacuum; the vacuum IS something.

## Finding 2: The cosmological constant problem, sharpened

The gap between QFT prediction and observation:

> At Planck scale: 10^137.7 (or ~10^120-123 in standard particle physics units)

This is not a small numerical accident. The gap has a specific character:

**QFT sums all vacuum fluctuation modes.** Each mode contributes ½ħω to the vacuum energy.
Integrating to the Planck cutoff gives ρ_QFT ~ ρ_Planck ≈ 10^113 J/m³.

**The observed Λ corresponds to** ρ_Λ ≈ 10⁻²⁷ J/m³.

**The gap is 10^140.** Something must cancel the first 10^140/10^120 = 10^20 digits of the
QFT sum — leaving only the last ~120 digits contributing to the observed Λ. This requires
a precision of 1 in 10^120: the most precise "fine-tuning" known in physics.

Why would this cancellation happen? Current candidates (from the script):
1. **Supersymmetry**: bosons and fermions contribute vacuum energies of opposite sign.
   Exact SUSY gives perfect cancellation. Broken SUSY leaves a residual at the SUSY-breaking
   scale — still too large by ~10^60 at EW scale.
2. **Anthropic selection** (multiverse): Λ is small in our bubble because life requires it.
   The landscape of string vacua has ~10^500 solutions; a small fraction have small Λ.
   Weinberg (1987) predicted Λ should be near the observed value for galaxies to form.
3. **Unknown symmetry**: an exact cancellation mechanism we haven't found yet.
4. **Quantum gravity**: the Planck-scale cutoff is wrong; the actual QFT fails near the Planck
   scale and a UV-complete quantum gravity theory gives a different answer.

## Finding 3: The problem IS a K-information problem

**Framing the cosmological constant problem in K-information terms:**

The SM Lagrangian is a ~2000-character K-specification that generates 10^104 modes per m³.
Each mode contributes ½ħω to the vacuum energy. The naive sum of 10^104 modes gives ρ_QFT.
The observed value is ρ_Λ = 10^-123 × ρ_Planck.

The K-information question: **is there a K-short description that explains the cancellation?**

- If yes (symmetry, SUSY, UV-completion): the cancellation has a K-simple cause.
  Anthropic selection is K-poor: "we exist because Λ is small" is not a compression of
  the cancellation, it just moves the question back to the multiverse's distribution over Λ.
- If no (pure coincidence or anthropic): the cancellation is K-complex — the universe
  happened to have this Λ with no underlying reason. This would be an example of
  K-rich physical fact with no K-short explanation.

The cosmological constant problem is, in this framing, asking whether the observable universe's
vacuum energy has a short K-explanation. Current physics says: we don't know. The absence of
a K-explanation is what makes the problem hard; the gap itself is just the symptom.

**Comparison to the π case from `what_is_information`:**
π has H = 3.32 bits/digit (looks random to gzip) but K = O(1) (short program). The vacuum
has H = enormous (10^104 fluctuation modes) but its K may be O(1) (the SM Lagrangian, if it
correctly accounts for the cancellation). The cosmological constant problem asks whether
the OBSERVED Λ is captured by that K-short description or requires additional K-content.

## Sky bridges (numerical)

- **physics/what_is_information** — vacuum is the most extreme S/K example: K=~2000 chars,
  S=10^104 modes. The S/K bifurcation is most dramatic here of any physical system.
- **physics/what_is_time** — the low-entropy Big Bang that starts the thermodynamic arrow:
  why was the initial vacuum energy small enough for structure to form? The cosmological
  constant is the low-entropy initial condition problem for the vacuum itself.
- **physics/what_is_reality** — the vacuum's K-simple laws generate its S-rich fluctuations.
  This supports K-monism: physical laws (K-poor) are primary; observable states (S-rich)
  are derived. Whether the vacuum IS real or is a mathematical abstraction is the ontology question.
- **physics/what_is_computation** — QFT vacuum modes are K-manipulations; each mode is a
  K-function (wave with frequency ω). The universe "computes" the vacuum by running these K-functions.

## Next numerical steps

1. **Full SM degrees of freedom.** Include all standard model particles with correct statistics
   (bosons +, fermions −). Compute the partial cancellation from the known SM field content.
   How much does the known SM spectrum reduce the gap? (Expected: SM alone doesn't help much.)

2. **SUSY cancellation toy model.** For each SM boson, add a fermion superpartner with mass m̃.
   Compute the residual vacuum energy as a function of m̃. Plot the gap vs m̃: it should close
   to the EW scale gap (~10^69) when m̃ ~ TeV, which is ~10^56 short of the observed value.

3. **Anthropic window calculation.** Use Weinberg's 1987 result: Λ can be at most ~few ×
   the observed value for galaxies to form. Compute the probability that a randomly selected
   vacuum from a uniform-over-Λ distribution falls within the anthropic window. Is this
   window itself K-simple? (It's a constraint on structure formation, so probably K-medium.)

## Status

Phase 1 numerics. The cosmological constant problem is precisely characterized: gap is
10^120–123 by standard conventions (10^137.7 in our raw 2-mode calculation). The Casimir
effect confirms the vacuum is not nothing. The K-information framing sharpens the problem:
it asks whether the observed Λ has a K-short physical explanation.
