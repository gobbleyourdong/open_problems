# SUSY Cancellation — Findings

**Generated:** 2026-04-09
**Script:** numerics/susy_cancellation.py
**Data:** results/susy_data.json
**Depends on:** results/sm_vacuum_data.json (from sm_vacuum_energy.py)

## Setup

The Standard Model has 28 bosonic and 90 fermionic DOF (net = −62, fermions dominate),
giving a vacuum energy of ~10^139.2 J/m³ in magnitude at Planck cutoff —
a gap of 10^139.2 orders of magnitude above observed ρ_Λ ≈ 5.924e-27 J/m³.

SUSY adds a superpartner for each SM particle (opposite statistics, same DOF count).
MSSM total: 236 DOF (118 bosonic + 118 fermionic — exactly balanced).

### Formula: exact SUSY cancellation

When all superpartner masses equal their SM counterparts:

    For each SM particle i with DOF nᵢ:
      SM contribution:      sᵢ × nᵢ × mᵢ⁴ / (32π²)
      Partner contribution: −sᵢ × nᵢ × mᵢ⁴ / (32π²)   [opposite stat, same mass]
      Net pair:             0

    Total: ρ = 0  (exact cancellation)

### Formula: broken SUSY at scale m̃

When all superpartners have mass m̃ > m_SM:

    Residual ρ_SUSY ≈ m̃⁴ / (16π²)   [GeV⁴, canonical 1-DOF form]
    Residual ρ_SUSY ≈ N_eff × m̃⁴ / (16π²)   [N_eff = 118 for full MSSM]

    SI conversion: ρ [J/m³] = ρ [GeV⁴] × (GeV_J)⁴ / (ħc)³
    where GeV_J = 1.602×10⁻¹⁰ J/GeV, ħc = 3.1615e-26 J·m

## Unit conversion cross-check

Photon-only at Planck cutoff:
  Computed: 2.933848e+111 J/m³
  Known (from sm_vacuum_energy.py): 2.933848e+111 J/m³
  Ratio: 1.00000000  (PASS)

## Results

### m̃ sweep — residual gap table (canonical, 1 DOF)

| m̃ (GeV) | Label | ρ_SUSY (J/m³) | log10(gap vs ρ_Λ) |
|----------|-------|---------------|-------------------|
| 1.00e+01 | 10 GeV | 1.320e+39 | 65.35 |
| 1.00e+02 | 100 GeV (EW scale) | 1.320e+43 | 69.35 |
| 1.00e+03 | 1 TeV (LHC-accessible SUSY) | 1.320e+47 | 73.35 |
| 1.00e+04 | 10 TeV | 1.320e+51 | 77.35 |
| 1.00e+05 | 100 TeV | 1.320e+55 | 81.35 |
| 1.00e+10 | 1e10 GeV (GUT-ish) | 1.320e+75 | 101.35 |
| 1.00e+15 | 1e15 GeV (near-GUT) | 1.320e+95 | 121.35 |
| 1.22e+19 | 1.221e+19 GeV (Planck) | 2.934e+111 | 137.69 |

SM alone (no SUSY): gap = 10^139.2 at Planck cutoff.
Exact SUSY (m̃ = 0): gap = 0 (ρ = 0 identically).

### Focus: m̃ = 1 TeV (LHC naturalness target)

- Canonical residual: ρ = 1.3205e+47 J/m³
- Gap vs observed: **10^73.35**
- Full MSSM (118 DOF): gap = 10^75.42

Even at 1 TeV, SUSY reduces the gap from 10^139.2 to ~10^73.
That is ~79 orders of magnitude of improvement — still 60 orders from observed.

### Gap milestone table

| Target log10(gap) | Required m̃ | Notes |
|-------------------|------------|-------|
| 139.2 | 2.904e+19 GeV | No improvement — SM level |
| 60    | 4.602e-01 GeV | EW-scale gap level |
| 20    | 4.602e-11 GeV | 20 orders from observed |
| 0     | 4.602e-16 GeV = 0.0005 meV | **Exact match to ρ_Λ** |

## The meV fine-tuning problem

For ρ_SUSY = ρ_Λ (exact match), one needs:

    m̃ ≈ 4.602e-16 GeV = **0.0005 meV**

This is the SUSY fine-tuning statement:
- SUSY with m̃ ≈ meV would naturally explain the cosmological constant.
- But LHC excludes sparticles below ~1 TeV, so m̃ ≥ 10³ GeV.
- The ratio is m̃_LHC / m̃_natural ≈ 2.17e+18 — a fine-tuning of ~2e+18.
- This is a restatement of the CCP: SUSY shifts the problem, not resolves it.

The meV scale is not physically motivated independently — it equals (ρ_Λ)^(1/4)
in natural units, which is a tautology (dark energy scale = dark energy scale).

## Key findings

1. **Exact SUSY**: vacuum energy vanishes identically. The MSSM has equal bosonic
   and fermionic DOF (118 each), giving perfect cancellation.

2. **1 TeV SUSY breaking**: gap reduced from 10^139.2 → 10^73.3.
   SUSY at the LHC scale reduces the CCP by ~79 orders of magnitude.
   The remaining gap of ~10^73 is still catastrophically large.

3. **meV requirement**: To match ρ_Λ, superpartner masses must be ~0.00 meV.
   The LHC excludes this by ~18 orders of magnitude in mass
   (~73 orders in energy density).

4. **The fine-tuning problem is not solved, only shifted**:
   Without SUSY: fine-tune ρ_vac by 1 part in 10^139.
   With TeV SUSY: fine-tune SUSY-breaking parameters by 1 part in 10^73.
   SUSY improves the situation dramatically but leaves a residual hierarchy problem.

5. **No physically-motivated stopping point**: There is no principle that sets
   m̃ ≈ meV. The TeV scale was motivated by electroweak naturalness (unrelated
   to the CCP), and even that fails to match observations.

## Relation to gap.md

This quantifies why SUSY does not close gap.md R1:
- SUSY does provide the right mechanism (exact cancellation at zero breaking).
- SUSY breaking necessarily reintroduces a vacuum energy residual.
- At the observed sparticle mass scale (≳ 1 TeV), the residual is 10^73× too large.
- The "SUSY solution to the CCP" requires m̃ at the meV scale, which is unmotivated.
- This is sometimes called the "second fine-tuning" or "μ-problem" in SUSY contexts.
