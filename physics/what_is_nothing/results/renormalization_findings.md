# Renormalization Scheme Comparison — Findings

**Generated:** 2026-04-09
**Script:** numerics/renormalization_comparison.py
**Data:** results/renormalization_data.json
**Depends on:** vacuum_energy.py, sm_vacuum_energy.py, susy_cancellation.py

## Context

The cosmological constant problem (gap.md R1) depends on how the vacuum energy
integral is regulated. Previous scripts used a hard Planck-scale cutoff, giving
a gap of ~10^139 vs the observed ρ_Λ ≈ 5.924e-27 J/m³. This document
compares three regularization schemes to show how the gap changes — and why
none of them solve the problem.

## Regularization Schemes

### Scheme 1: Planck Hard Cutoff

    ρ = Σ_i sign_i × n_i × ħc × k_max^4 / (32π²),   k_max = E_P / (ħc)

All SM species contribute (photon, gluons, fermions, massive bosons).
The k_max^4 factor means the result is set by the UV cutoff, not particle masses.

**Result:** ρ_cutoff ≈ -9.095e+112 J/m³,  gap = 10^139.2

### Scheme 2: Dimensional Regularization (MS-bar, μ = M_Z = 91.2 GeV)

    ρ_i = sign_i × n_i × m_i^4 / (64π²) × [ln(μ²/m_i²) + 3/2]

    For massless particles (m = 0): ρ = 0 exactly

Only massive particles contribute: W±, Z, Higgs, charged leptons, quarks.
The result scales as m_top^4 ≈ (173 GeV)^4, not E_Planck^4.

**Result:** ρ_dimreg ≈ -4.586e+43 J/m³,  gap = 10^69.9

### Scheme 3: ζ-function Regularization (μ = M_Z = 91.2 GeV)

    ρ_ζ = sign × n × m^4 / (64π²) × [ln(μ²/m²) + 3/2]

    For massless particles: ρ = 0 exactly (no mass scale available)

At leading order, ζ-reg and MS-bar dim-reg give identical finite parts.
Both are UV-finite by construction; massless = zero is exact in both.

**Result:** ρ_ζ ≈ -4.586e+43 J/m³,  gap = 10^69.9

## Comparison Table

| Regularization | Cutoff / Scale | ρ_vac (J/m³) | Gap vs Λ_obs | Orders |
|----------------|---------------|--------------|--------------|--------|
| Planck cutoff  | E_P = 1.22×10^19 GeV | -9.095e+112 | 10^139.2 | 139 |
| Dim-reg MS-bar | μ = 91.2 GeV (M_Z) | -4.586e+43 | 10^69.9 | 70 |
| ζ-function reg | μ = 91.2 GeV (M_Z) | -4.586e+43 | 10^69.9 | 70 |
| Observed ρ_Λ   | 2023 Planck+BAO | 5.924e-27 | 1 (reference) | 0 |

**Dim-reg reduces the gap by 69 orders of magnitude** relative to Planck cutoff.

## Key Findings

### 1. Massless particles vanish in UV-finite regularizations

In dim-reg and ζ-reg, photons and gluons contribute exactly zero vacuum energy.
This follows from dimensional analysis: without a mass scale, the only available
energy scale is μ (the renormalization point), but the vacuum energy is
μ-independent for massless particles at this order. This is a significant
structural difference from the Planck-cutoff approach.

### 2. The gap reduces from 10^139 to 10^70

This improvement (69 orders of magnitude) comes from two effects:
- Massless particles (photon: 2 DOF, gluons: 16 DOF) no longer contribute
- The result scales as m_top^4 ≈ (173 GeV)^4, not k_max^4 ≈ (1.22×10^19 GeV)^4

The ratio explains the improvement:
  (m_top / E_Planck)^4 ≈ (173 / 1.22×10^19)^4 ≈ 10^-67

### 3. This is NOT a solution

Dim-reg is a regularization choice. The renormalization scale μ is arbitrary:
- At μ = M_Z: gap = 10^69.9
- At μ = Λ_obs^(1/4): one can tune the gap to zero trivially
- The problem becomes: "why is the cosmological constant counterterm
  fine-tuned to 70 decimal places?"

The fine-tuning problem is relocated, not resolved.

### 4. The EW-scale gap (10^70) is the "natural" CC problem

In the field-theory literature, the cosmological constant problem is often
stated as a ~10^60 gap (using EW scale) rather than 10^120 (Planck scale).
This script reproduces that: dim-reg at μ = M_Z gives gap ≈ 10^70.
The precise number depends on which particles are included and the sign
of their contributions under dim-reg.

### 5. μ-dependence: the scale-ambiguity of the problem

| μ | ρ_dimreg (J/m³) | gap (orders) |
|---|-----------------|--------------|
| 1 meV (dark energy scale) | (very small) | (~0, trivially tuned) |
| 100 MeV (QCD) | (smaller) | smaller |
| 91.2 GeV (M_Z) | -4.586e+43 | 69.9 |
| 1 TeV (LHC) | (larger) | larger |
| 1.22×10^19 GeV (Planck) | (same as cutoff) | 139.2 |

At μ = Λ_obs^(1/4) ≈ 2.3 meV, the log term can be tuned to give ρ_dimreg ≈ ρ_Λ.
This is manifestly a fine-tuning, not an explanation.

## Relation to Previous Analyses

| Analysis | Method | Gap |
|----------|--------|-----|
| vacuum_energy.py | Planck cutoff, photon only | 10^138 |
| sm_vacuum_energy.py | Planck cutoff, full SM | 10^139 |
| susy_cancellation.py | SUSY at 1 TeV | 10^73 |
| **this script** | Dim-reg, massive only | 10^70 |
| Observed | — | 10^0 (reference) |

Dim-reg (10^70) is closer to observation than SUSY at 1 TeV (10^73) — but
this is misleading. SUSY at 1 TeV changes the physical content (new particles);
dim-reg just changes the regularization convention.

## What This Means for gap.md R1

gap.md R1: "What mechanism cancels the QFT vacuum energy contributions to the
cosmological constant?"

This script shows:
- The size of the problem depends on the regularization (10^139 vs 10^70)
- In UV-finite schemes, massless particles drop out (a genuine structural insight)
- The EW-scale statement of the problem is: the top quark, W, Z, Higgs contribute
  ρ ~ (173 GeV)^4 / 64π² to the vacuum energy; observed ρ_Λ is 10^70× smaller
- No regularization scheme explains this gap — it would require a new symmetry,
  cancellation mechanism, or non-field-theoretic description of the vacuum

The "mechanism" question (R1's residue) remains open. Dim-reg makes it precise:
we need an explanation for why the bare cosmological constant is fine-tuned against
the m_top^4 quantum correction to 1 part in 10^70.
