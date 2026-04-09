# SM Vacuum Energy — Findings

**Generated:** 2026-04-09
**Script:** numerics/sm_vacuum_energy.py
**Data:** results/sm_vacuum_data.json

## Setup

Formula per species i:

    rho_i = sign_i * n_i * hbar * c * k_max^4 / (32 * pi^2)

where sign_i = +1 (boson) or -1 (fermion), n_i = internal degrees of freedom,
k_max = E_cutoff / (hbar * c).

## Standard Model DOF inventory

| Category | Bosonic DOF | Fermionic DOF |
|----------|-------------|----------------|
| Photon   | 2           | —              |
| W± boson | 6           | —              |
| Z boson  | 3           | —              |
| Higgs    | 1           | —              |
| Gluons   | 16          | —              |
| e, μ, τ  | —           | 12             |
| νe, νμ, ντ | —         | 6              |
| u,d,s,c,b,t (quarks) | — | 72           |
| **Total** | **28** | **90** |

Net signed DOF (B − F) = 28 − 90 = **-62**
(fermions exceed bosons by 62 DOF).

Exact SUSY would require net DOF = 0, giving exact cancellation of vacuum energy.

## Surprising result: fermions dominate

The SM has **90 fermionic DOF vs 28 bosonic DOF** — quarks alone contribute
72 fermionic DOF (6 flavors × 2 spin × 2 p/ap × 3 color), swamping the 28 bosonic DOF.
As a result the net SM vacuum energy is **negative** (fermions win), and actually
*larger* in magnitude than bosons alone. The SM does not partially cancel the
cosmological constant problem — it makes it slightly worse in absolute value.

## Results

### Planck-scale cutoff (~1.956e9 J ≈ 1.22e19 GeV)

| Quantity | Value | Gap vs ρ_Λ |
|----------|-------|------------|
| Photon-only baseline | 2.934e+111 J/m³ | 10^137.7 |
| SM bosons only | 4.107e+112 J/m³ | 10^138.8 |
| SM fermion contribution | -1.320e+113 J/m³ | — |
| SM total (bosons + fermions) | -9.095e+112 J/m³ | 10^139.2 |
| Observed ρ_Λ | 5.924e-27 J/m³ | — |

Net SM total is **negative** — fermions (DOF=90) overwhelm bosons (DOF=28).
The net magnitude gap 10^139.2 is -0.35 orders *worse* than bosons alone.

### Electroweak-scale cutoff (~100 GeV)

| Quantity | Value | Gap vs ρ_Λ |
|----------|-------|------------|
| SM bosons only | 1.783e+44 J/m³ | 10^70.5 |
| SM total (bosons + fermions) | -3.367e+44 J/m³ | 10^70.8 |
| Observed ρ_Λ | 5.924e-27 J/m³ | — |

Even at the electroweak scale (where the SM has been tested), the gap is ~10^71 orders of magnitude.

## Key finding

The SM has 90 fermionic vs 28 bosonic DOF (net = −62, fermions win).
At Planck cutoff:
- Bosons-only gap: 10^138.8
- Full SM gap (|net|): 10^139.2
- Fermions make the magnitude **worse** by 0.35 orders — they do not cancel bosons,
  they add a larger negative contribution.

This is the opposite of naive intuition. The SM does NOT partially solve the
cosmological constant problem — the quark sector's 72 fermionic DOF dominate.

For fermion cancellation to reduce the gap, you need extra bosonic species (as in SUSY,
which adds a bosonic superpartner for every fermion). With exact SUSY and degenerate
masses, net DOF = 0 and the vacuum energy vanishes identically.

## Physical interpretation

The SM has more fermionic DOF (90) than bosonic (28), so the net
vacuum energy is negative at both cutoffs. The sign is unphysical anyway (the
observed cosmological constant is positive), reinforcing that something beyond
naive mode-counting is required.

The cosmological constant problem is NOT resolved by the SM:
- SUSY would cancel exactly if masses were degenerate (they are not)
- Actual SUSY breaking scale ≫ observed Λ^(1/4) ~ 2.3 meV
- The remaining 10^139 discrepancy at Planck cutoff (10^71 at EW cutoff)
  requires physics beyond the Standard Model

## Relation to gap.md R1

This calculation quantifies gap.md R1: the cosmological constant problem.
- The oft-cited "10^120" figure uses the EW cutoff with only the Higgs/gauge sector
  (fewer fermions), or assumes near-equal B/F DOF as a schematic estimate.
- Our photon-only result gave 10^137.7 (Planck).
- The full SM at Planck cutoff gives 10^139.2 (net |ρ|), slightly worse than photon-only.
- No known symmetry principle explains the residual fine-tuning.
- The SM does not reduce the cosmological constant problem; only a BSM mechanism
  (SUSY, extra dimensions, anthropic selection, or quantum gravity) can address it.
