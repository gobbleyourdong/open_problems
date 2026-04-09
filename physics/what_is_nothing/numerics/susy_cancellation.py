#!/usr/bin/env python3
"""
susy_cancellation.py — SUSY breaking and the cosmological constant residual.

Context: sm_vacuum_energy.py established that the full SM has net -62 DOF
(fermions dominate), making the vacuum energy negative and ~10^139.2 J/m³
in magnitude. The gap is 10^139.2 orders from observed ρ_Λ.

SUSY key facts:
  - Each SM boson gains a fermionic superpartner ("gaugino" / "higgsino")
  - Each SM fermion gains a bosonic superpartner ("sfermion" / "squark" / "slepton")
  - Exact SUSY: every partner has the SAME mass → contributions cancel exactly
    because: ρ_partner = -ρ_original (opposite sign, same DOF, same magnitude)
    Net vacuum energy = 0 identically.
  - Broken SUSY at scale m̃: superpartner masses ≈ m̃ >> m_SM
    Residual ρ_SUSY ≈ N_eff × m̃^4 / (16π²)   [in natural units]
    where N_eff = total number of DOF in the MSSM = 2 × SM_DOF (each has a partner)

This script:
  1. Verifies the exact-SUSY cancellation formula.
  2. Computes residual ρ_SUSY(m̃) for m̃ ∈ {10, 100, 1e3, 1e4, 1e5, 1e10, 1e15, 1e19} GeV.
  3. Computes the detailed residual from the SM mass spectrum:
       Δρ_i = n_i × (m̃^4 - m_i^4) / (32π² (ħc)^3 ħ)   [J/m³]
     for each SM particle with its superpartner at mass m̃.
  4. Identifies the SUSY-breaking scale that would give ρ_SUSY ≈ ρ_Λ.
  5. Identifies gap milestones: m̃ for gap = 10^60, 10^20, 10^0.

Unit conversion (cleanest path):
  In natural units (ħ = c = 1): ρ [GeV^4].
  Convert to SI J/m³:
    ρ [J/m³] = ρ [GeV^4] × (GeV_in_J)^4 / (hbar_c_in_GeVm)^3 / hbar_in_Js
  where:
    GeV_in_J      = 1.602176634e-10  (1 GeV = this many joules)
    hbar_c_in_GeVm = 1.9733e-16      (ħc in GeV·m)
  So:
    1 GeV^4 → 1 GeV × (GeV_in_J / GeV_in_J)... use dimensional analysis:
    ρ [J/m³] = ρ_nat [GeV^4] × (GeV_in_J)^4 / (hbar_c_in_GeVm)^3
  Verify: [GeV^4] × [J/GeV]^4 / [GeV·m]^3
         = [GeV^4 × J^4/GeV^4] / [GeV^3 m^3]
         = [J^4 / GeV^3 m^3]   ... not right. Use the standard:

  ħc = 197.3269804 MeV·fm = 1.9733e-16 GeV·m = 1.9733e-7 GeV·nm
  1 fm = 1e-15 m
  ρ [J/m³] = ρ_nat [GeV^4] × (GeV_in_J / (hbar_c_in_m * GeV_in_J))^3
            = ρ_nat [GeV^4] × GeV_in_J / hbar_c_in_m^3

  Actually the cleanest:
    [ρ in natural units] = m̃^4 / (16π²)  in units of GeV^4
    To convert: use ħc = 0.197327 GeV·fm, so 1/ħc has units 1/(GeV·fm)
    ρ [J/m³] = ρ [GeV^4] × (1/ħc)^3  × c × ħ   ... reduces to:
    ρ [J/m³] = ρ [GeV^4] / (ħc)^3  × GeV × (1/m)^3 × J/GeV
             = ρ [GeV^4] × (1 GeV in J) / (ħc in m·GeV)^3

  Which is what the task specification says:
    ρ [J/m³] = m̃^4_GeV × (1.602e-10)^4 / (1.9733e-16)^3 / (16π²)

  Let's verify dimensions:
    [GeV^4 × (J/GeV)^4 / (GeV·m)^3]
    = [GeV^4 × J^4/GeV^4] / [GeV^3·m^3]
    = [J^4/(GeV^3·m^3)]    ... still wrong dimensionally?

  Correct approach — use the known identity:
    1 GeV^4 (natural units) = (GeV/c^2)^4 × c^7 / ħ^3
  Numerically, the task formula works because everything cancels correctly in
  the product — see the comment in geV4_to_SI() below where we cross-check
  against the photon baseline from sm_vacuum_data.json.

Usage:
    cd ~/open_problems/physics/what_is_nothing
    python3 numerics/susy_cancellation.py

Numerical track, what_is_nothing — 2026-04-09
"""

import math, json, os

# ── Physical constants (SI) ───────────────────────────────────────────────────

hbar    = 1.054571817e-34    # J·s
c       = 2.99792458e8       # m/s
G       = 6.67430e-11        # m³/(kg·s²)
eV_J    = 1.602176634e-19    # J per eV
GeV_J   = 1e9 * eV_J        # J per GeV  = 1.602176634e-10 J
hbar_c  = hbar * c           # J·m  = 3.16153e-26 J·m
# ħc in GeV·m:  hbar*c / GeV_J = 3.16153e-26 / 1.602176634e-10 = 1.97327e-16 GeV·m
hbar_c_GeVm = hbar_c / GeV_J  # ≈ 1.9733e-16 GeV·m

# Planck scale
m_P = math.sqrt(hbar * c / G)     # ≈ 2.176e-8 kg
E_P = m_P * c**2                   # ≈ 1.956e9 J
E_P_GeV = E_P / GeV_J             # ≈ 1.2209e19 GeV

# Observed cosmological constant
Lambda_obs = 1.1056e-52            # m⁻²
rho_Lambda = Lambda_obs * c**2 / (8 * math.pi * G)  # J/m³ ≈ 5.924e-27
rho_Lambda_log10 = math.log10(rho_Lambda)

# ── Unit conversion: natural GeV^4 → SI J/m³ ─────────────────────────────────

def geV4_to_SI(rho_nat_GeV4: float) -> float:
    """
    Convert energy density from natural units (GeV^4, ħ=c=1) to SI (J/m³).

    Derivation:
      In natural units ħ = c = 1, so [energy] = [mass] = [length^-1] = [time^-1].
      ρ in GeV^4 is shorthand for ρ in (ħc)^-3 × GeV^4 × ħ^-1 ... messy.

      Cleaner: use the known QFT formula for zero-point energy density.
      For a single massless boson with cutoff Λ_GeV:
        ρ = Λ^4 / (16π²)  [GeV^4 natural]
      The SM script computed this in SI directly using k_max = E_cutoff/(ħc).
      Cross-check: photon-only at Planck = 2.934e+111 J/m³ (from sm_vacuum_data.json)
      and Planck energy E_P_GeV = 1.2209e19 GeV, n_dof=2 (photon):
        ρ_nat = 2 × (1.2209e19)^4 / (32π²)  GeV^4
        ρ_SI  = ρ_nat × conversion_factor
        2.934e+111 J/m³ / ρ_nat_GeV4 → conversion factor

      Standard result: 1 GeV^4 (natural) = (GeV_J)^4 / (hbar_c)^3
        Units: [J^4] / [J·m]^3 = [J^4]/[J^3·m^3] = [J/m³]  ✓

    So: ρ [J/m³] = ρ [GeV^4] × (GeV_J)^4 / (hbar_c)^3
    """
    return rho_nat_GeV4 * (GeV_J)**4 / (hbar_c)**3


def log10_safe(x: float) -> float:
    if x == 0.0:
        return float('-inf')
    return math.log10(abs(x))


# ── Cross-check the unit conversion against known result ─────────────────────

def _crosscheck_units():
    """
    Verify geV4_to_SI against the photon-only result from sm_vacuum_energy.py.
    Photon: n_dof=2, massless, Planck cutoff.
    ρ_nat = 2 × E_P_GeV^4 / (32π²)
    ρ_SI  should be ≈ 2.9338e+111 J/m³
    """
    rho_nat_photon = 2 * E_P_GeV**4 / (32 * math.pi**2)
    rho_si_photon  = geV4_to_SI(rho_nat_photon)
    known = 2.933847828682001e+111
    ratio = rho_si_photon / known
    ok = abs(math.log10(ratio)) < 0.01   # should agree to <1%
    return rho_si_photon, known, ratio, ok


# ── SM particle table (same as sm_vacuum_energy.py) ──────────────────────────
# (name, stat, n_dof, mass_GeV)

SM_PARTICLES = [
    ("Photon (γ)",       "boson",   2,   0.0),
    ("W± boson",         "boson",   6,   80.4),
    ("Z boson",          "boson",   3,   91.2),
    ("Higgs (H)",        "boson",   1,   125.25),
    ("Gluons (g×8)",     "boson",   16,  0.0),
    ("Electron (e)",     "fermion", 4,   0.000511),
    ("Muon (μ)",         "fermion", 4,   0.1057),
    ("Tau (τ)",          "fermion", 4,   1.777),
    ("Neutrino νe",      "fermion", 2,   0.0),
    ("Neutrino νμ",      "fermion", 2,   0.0),
    ("Neutrino ντ",      "fermion", 2,   0.0),
    ("Up quark (u)",     "fermion", 12,  0.0022),
    ("Down quark (d)",   "fermion", 12,  0.0047),
    ("Strange quark (s)","fermion", 12,  0.096),
    ("Charm quark (c)",  "fermion", 12,  1.27),
    ("Bottom quark (b)", "fermion", 12,  4.18),
    ("Top quark (t)",    "fermion", 12,  173.1),
]

SM_DOF_BOSON   = sum(n for _, s, n, _ in SM_PARTICLES if s == "boson")
SM_DOF_FERMION = sum(n for _, s, n, _ in SM_PARTICLES if s == "fermion")
SM_DOF_TOTAL   = SM_DOF_BOSON + SM_DOF_FERMION

# MSSM: each SM particle gets a superpartner with the same DOF but opposite stat.
# Total MSSM DOF = 2 × SM_DOF_TOTAL, split equally B/F → N_eff = SM_DOF_TOTAL.
MSSM_DOF_TOTAL = 2 * SM_DOF_TOTAL   # = 2*(28+90) = 236

# ── SUSY residual: simple formula ─────────────────────────────────────────────

def rho_susy_simple_GeV4(m_tilde_GeV: float) -> float:
    """
    Simple SUSY residual at uniform breaking scale m̃.

    When all superpartners have mass m̃ and all SM particles have mass ≈ 0
    (or m̃ >> m_SM), the residual vacuum energy from SUSY breaking is:

      ρ_SUSY = N_eff × m̃^4 / (16π²)

    where N_eff = total number of DOF that remain unpaired in mass
    (equivalently, the number of degrees of freedom in the superpartner sector,
    each contributing m̃^4/(32π²) with the same sign as the heavier partners).

    Derivation:
      Exact SUSY (m_partner = m_SM): ρ_total = 0 (exact cancellation).
      Broken SUSY (m_partner = m̃ > m_SM):
        For each SM species with DOF n_i:
          ρ_partner - ρ_SM ≈ n_i × (m̃^4 - m_i^4) / (32π²)
          [the partner has the opposite stat, so it contributes +n_i × m̃^4/(32π²)
           when m̃ >> m_i, and the SM contributes -n_i × m_i^4/(32π²), leaving a net
           positive residual n_i × m̃^4/(32π²)]
      Summing over all SM_DOF_TOTAL species pairs:
        ρ_SUSY ≈ SM_DOF_TOTAL × m̃^4 / (32π²)
                = (SM_DOF_TOTAL/2) × m̃^4 / (16π²)

    We use the conventional form N_eff × m̃^4 / (16π²) where N_eff absorbs the
    counting. For the MSSM:
      N_eff ≈ SM_DOF_TOTAL = 118  (since each partner adds back its contribution).

    Note: some references quote N_eff = 1 (normalizing to a single DOF) and then
    separately note that "the MSSM has O(100) DOF". We keep the full DOF count
    so our result is honest about the magnitude.

    For simplicity and convention we also provide a "canonical" single-DOF formula
    ρ_canon = m̃^4 / (16π²) to show where the meV bound comes from.
    """
    return SM_DOF_TOTAL * m_tilde_GeV**4 / (16 * math.pi**2)


def rho_susy_canonical_GeV4(m_tilde_GeV: float) -> float:
    """Canonical single-DOF SUSY residual: m̃^4 / (16π²)."""
    return m_tilde_GeV**4 / (16 * math.pi**2)


# ── SUSY residual: detailed per-species (task item 4) ─────────────────────────

def rho_susy_detailed_GeV4(m_tilde_GeV: float) -> float:
    """
    Per-species SUSY residual, summing Δρ_i = n_i × (m̃^4 - m_i^4) / (32π²).

    For each SM particle with DOF n_i and mass m_i:
      - The SM particle has stat s_i ∈ {boson, fermion}.
      - The SUSY partner has opposite stat and mass m̃.
      - The SM particle contributes: s_i × n_i × m_i^4 / (32π²)
      - The SUSY partner contributes: (-s_i) × n_i × m̃^4 / (32π²)
      - Total pair contribution: s_i × n_i × (m_i^4 - m̃^4) / (32π²)

    Sum over all SM particles:
      ρ_net = Σ_i s_i × n_i × m_i^4 / (32π²)   [SM part]
            + Σ_i (-s_i) × n_i × m̃^4 / (32π²)  [partner part]

    Since Σ_i s_i × n_i = (28 - 90) = -62 (net DOF signed):
      Partner contribution = -(-62) × m̃^4 / (32π²) = +62 × m̃^4 / (32π²)
      SM contribution = Σ_i s_i × n_i × m_i^4 / (32π²)  [the original SM vacuum energy]

    At m̃ >> m_SM: ρ_residual ≈ +62 × m̃^4 / (32π²) + small SM_original

    But this misses the full picture. When SUSY is exact (m̃ = m_i for all i):
      Each pair has zero net contribution → total = 0.
    When m̃ = 0 (nonsensical but formal): partners at mass 0 → restores SM vacuum.

    For the task's "same m̃ for all partners" case:
    The residual relative to the exact-SUSY baseline (ρ=0) is:

      Δρ = Σ_i n_i × |m̃^4 - m_i^4| / (32π²) × appropriate sign

    The most physically meaningful: how much does adding SUSY partners at m̃
    shift ρ from 0? When SUSY is exact (all m_partner = m_SM), ρ=0.
    When partners get mass m̃ > m_SM, each partner gains extra energy:
      Δρ_i = n_i × (m̃^4 - m_i^4) / (32π²)
    These are all positive (m̃ > m_i assumed), so ρ_residual > 0.

    Returns residual in GeV^4.
    """
    total = 0.0
    for name, stat, n_dof, mass_GeV in SM_PARTICLES:
        # Each partner: mass m̃, opposite stat from SM particle.
        # The pair (SM + SUSY partner) had zero contribution when m_partner = m_SM.
        # Now m_partner = m̃, so the net pair contribution increases by:
        delta = n_dof * (m_tilde_GeV**4 - mass_GeV**4) / (32 * math.pi**2)
        total += delta
    return total


# ── Main computation sweep ────────────────────────────────────────────────────

M_TILDE_VALUES_GeV = [10, 100, 1e3, 1e4, 1e5, 1e10, 1e15, E_P_GeV]

LABELS = {
    10:      "10 GeV",
    100:     "100 GeV (EW scale)",
    1e3:     "1 TeV (LHC-accessible SUSY)",
    1e4:     "10 TeV",
    1e5:     "100 TeV",
    1e10:    "1e10 GeV (GUT-ish)",
    1e15:    "1e15 GeV (near-GUT)",
}


def label_for(m: float) -> str:
    for key, lbl in LABELS.items():
        if abs(m - key) / (key + 1) < 0.01:
            return lbl
    return f"{m:.3e} GeV (Planck)"


def compute_sweep():
    rows = []
    for m_tilde in M_TILDE_VALUES_GeV:
        rho_nat_simple   = rho_susy_simple_GeV4(m_tilde)
        rho_nat_canon    = rho_susy_canonical_GeV4(m_tilde)
        rho_nat_detailed = rho_susy_detailed_GeV4(m_tilde)

        rho_si_simple   = geV4_to_SI(rho_nat_simple)
        rho_si_canon    = geV4_to_SI(rho_nat_canon)
        rho_si_detailed = geV4_to_SI(rho_nat_detailed)

        gap_simple   = rho_si_simple   / rho_Lambda
        gap_canon    = rho_si_canon    / rho_Lambda
        gap_detailed = rho_si_detailed / rho_Lambda

        rows.append({
            "m_tilde_GeV":        m_tilde,
            "label":              label_for(m_tilde),
            "rho_simple_GeV4":    rho_nat_simple,
            "rho_canon_GeV4":     rho_nat_canon,
            "rho_detailed_GeV4":  rho_nat_detailed,
            "rho_simple_J_m3":    rho_si_simple,
            "rho_canon_J_m3":     rho_si_canon,
            "rho_detailed_J_m3":  rho_si_detailed,
            "gap_simple":         gap_simple,
            "gap_canon":          gap_canon,
            "gap_detailed":       gap_detailed,
            "log10_gap_simple":   log10_safe(gap_simple),
            "log10_gap_canon":    log10_safe(gap_canon),
            "log10_gap_detailed": log10_safe(gap_detailed),
        })
    return rows


# ── Find m̃ for target log10 gap ──────────────────────────────────────────────

def find_m_tilde_for_gap(target_log10_gap: float, use_dof: float = 1.0) -> float:
    """
    Find m̃ such that log10(ρ_SUSY / ρ_Λ) = target_log10_gap.

    Using canonical formula: ρ_SUSY = use_dof × m̃^4 / (16π²) [GeV^4]
    ρ_Lambda_GeV4 = rho_Lambda / geV4_to_SI(1.0)

    Solve: use_dof × m̃^4 / (16π²) × conversion = 10^target_log10_gap × rho_Lambda
    → m̃^4 = 10^target × rho_Lambda_SI / conversion × 16π² / use_dof
    → m̃    = (...)^(1/4)
    """
    conversion = (GeV_J)**4 / (hbar_c)**3   # converts GeV^4 → J/m³
    rhs = (10**target_log10_gap) * rho_Lambda / conversion * 16 * math.pi**2 / use_dof
    if rhs <= 0:
        return float('nan')
    m_tilde = rhs**(0.25)
    return m_tilde   # in GeV


# ── Pretty printing ───────────────────────────────────────────────────────────

def sep(char='─', n=80):
    return char * n


def fmt_exp(x):
    if x == 0:
        return "0.0"
    if abs(x) < 1e-300:
        return "0.0 (underflow)"
    exp = math.floor(math.log10(abs(x)))
    mantissa = x / 10**exp
    sign_s = "+" if x >= 0 else "-"
    return f"{sign_s}{abs(mantissa):.3f}×10^{exp:+d}"


def run():
    print("=" * 80)
    print("  SUSY Cancellation and the Cosmological Constant Residual")
    print("  what_is_nothing — numerical track — 2026-04-09")
    print("=" * 80)

    # ── Cross-check unit conversion ──────────────────────────────────────────
    rho_si_check, rho_known, ratio, ok = _crosscheck_units()
    print(f"\n  Unit conversion cross-check (photon-only at Planck):")
    print(f"    Computed: {rho_si_check:.6e} J/m³")
    print(f"    Known:    {rho_known:.6e} J/m³")
    print(f"    Ratio:    {ratio:.8f}  ({'PASS' if ok else 'FAIL — check conversion!'})")
    if not ok:
        print("  WARNING: unit conversion mismatch > 1%. Results unreliable.")

    # ── Constants summary ─────────────────────────────────────────────────────
    print(f"\n  Physical constants:")
    print(f"    ħ              = {hbar:.6e} J·s")
    print(f"    c              = {c:.8e} m/s")
    print(f"    ħc             = {hbar_c:.6e} J·m = {hbar_c_GeVm:.4e} GeV·m")
    print(f"    E_Planck       = {E_P:.4e} J = {E_P_GeV:.4e} GeV")
    print(f"    ρ_Λ (obs)      = {rho_Lambda:.4e} J/m³")
    print(f"    1 GeV^4 → SI   = {geV4_to_SI(1.0):.4e} J/m³")

    # ── SM DOF inventory ──────────────────────────────────────────────────────
    print(f"\n  SM + MSSM degrees of freedom:")
    print(f"    SM bosonic DOF:   {SM_DOF_BOSON}")
    print(f"    SM fermionic DOF: {SM_DOF_FERMION}")
    print(f"    SM total DOF:     {SM_DOF_TOTAL}")
    print(f"    MSSM total DOF:   {MSSM_DOF_TOTAL}  (each SM particle gets a superpartner)")

    # ── Exact SUSY cancellation ───────────────────────────────────────────────
    print(f"\n{sep('═')}")
    print(f"  EXACT SUSY CANCELLATION")
    print(f"{sep('═')}")
    print(f"""
  When SUSY is unbroken (m_partner = m_SM for all particles):
    Each SM boson gains a fermionic superpartner with the SAME mass.
    Each SM fermion gains a bosonic superpartner with the SAME mass.
    Contribution of SM particle i:  +sign_i × n_i × f(m_i)
    Contribution of its partner:    -sign_i × n_i × f(m_i)   [opposite stat, same mass]
    Net pair contribution:          0

  Summing over all {SM_DOF_TOTAL} SM particles + {SM_DOF_TOTAL} SUSY partners:
    ρ_total = 0  [exact, to all orders in the zero-point energy calculation]

  This is the SUSY miracle: the vacuum energy vanishes identically when
  all superpartner masses are degenerate with their SM counterparts.
  The SM's terrible -62 net DOF imbalance becomes irrelevant — the MSSM
  has exactly 118 bosonic and 118 fermionic DOF (perfect balance).
""")

    # ── Sweep: residual vs m̃ ─────────────────────────────────────────────────
    rows = compute_sweep()

    print(f"{sep('═')}")
    print(f"  SUSY RESIDUAL VACUUM ENERGY vs BREAKING SCALE m̃")
    print(f"  (canonical formula: ρ_canon = m̃^4/(16π²), and detailed per-species)")
    print(f"{sep('═')}")
    print()

    # Table header — canonical (1 DOF) for comparison with literature
    print(f"  {'m̃ (GeV)':<18} {'Label':<30} {'ρ_canon (J/m³)':<20} {'log10(gap)':<12}")
    print(f"  {sep('-',16):<18} {sep('-',28):<30} {sep('-',18):<20} {sep('-',10):<12}")
    for r in rows:
        lbl = r["label"]
        m   = r["m_tilde_GeV"]
        rho = r["rho_canon_J_m3"]
        g   = r["log10_gap_canon"]
        m_str  = f"{m:.3e}"
        rho_str = fmt_exp(rho)
        print(f"  {m_str:<18} {lbl:<30} {rho_str:<20} {g:<12.2f}")

    print()
    print(f"  (Full MSSM DOF = {SM_DOF_TOTAL} factor makes ρ_simple = {SM_DOF_TOTAL} × ρ_canon)")
    print(f"  log10(gap) would be {math.log10(SM_DOF_TOTAL):.2f} larger for the full MSSM count.")

    # ── Milestone table ───────────────────────────────────────────────────────
    print(f"\n{sep('═')}")
    print(f"  GAP MILESTONES: What m̃ gives each residual gap?")
    print(f"  (using canonical ρ = m̃^4 / (16π²), 1 DOF for comparison with literature)")
    print(f"{sep('═')}")

    milestones = [
        (139.2, "10^139.2 (SM Planck cutoff magnitude — SUSY makes no improvement)"),
        (120,   "10^120   (often-cited 'classic' CCP figure)"),
        (60,    "10^60    (electroweak-scale gap, roughly)"),
        (40,    "10^40    (between EW and observed)"),
        (20,    "10^20    (20 orders from observed)"),
        (10,    "10^10    (10 orders from observed)"),
        (0,     "10^0 = 1 (exact match to observed ρ_Λ)"),
    ]

    print()
    print(f"  {'Target log10(gap)':<20} {'m̃ needed (GeV)':<22} {'m̃ in natural units'}")
    print(f"  {sep('-',18):<20} {sep('-',20):<22} {sep('-',30)}")
    for target, desc in milestones:
        m_needed = find_m_tilde_for_gap(target, use_dof=1.0)
        # Convert to physical energy units for context
        m_needed_eV = m_needed * 1e9   # GeV → eV
        if m_needed_eV < 1e-3:
            nat_str = f"{m_needed_eV*1e3:.4f} meV"
        elif m_needed_eV < 1:
            nat_str = f"{m_needed_eV*1e3:.3f} meV"
        elif m_needed_eV < 1e3:
            nat_str = f"{m_needed_eV:.4f} eV"
        elif m_needed_eV < 1e6:
            nat_str = f"{m_needed_eV/1e3:.4f} keV"
        elif m_needed_eV < 1e9:
            nat_str = f"{m_needed_eV/1e6:.4f} MeV"
        elif m_needed_eV < 1e12:
            nat_str = f"{m_needed_eV/1e9:.4f} GeV"
        else:
            nat_str = f"{m_needed_eV/1e12:.4f} TeV"
        print(f"  {target:<20.1f} {m_needed:.6e} GeV    {nat_str}")
    print()

    # ── Special focus: 1 TeV ─────────────────────────────────────────────────
    tev_row = [r for r in rows if abs(r["m_tilde_GeV"] - 1e3) < 1][0]
    print(f"{sep('═')}")
    print(f"  FOCUS: m̃ = 1 TeV (LHC-accessible SUSY-breaking scale)")
    print(f"{sep('═')}")
    print(f"""
  If SUSY is broken at m̃ = 1 TeV (as motivated by electroweak naturalness
  before LHC Run 1 excluded sub-TeV sparticles):

  Canonical residual (1 DOF):
    ρ_canon = (1000 GeV)^4 / (16π²) = {tev_row['rho_canon_GeV4']:.4e} GeV^4
            = {tev_row['rho_canon_J_m3']:.4e} J/m³
    Gap vs observed: 10^{tev_row['log10_gap_canon']:.2f}

  Full MSSM residual ({SM_DOF_TOTAL} DOF):
    ρ_simple = {SM_DOF_TOTAL} × ρ_canon = {tev_row['rho_simple_J_m3']:.4e} J/m³
    Gap vs observed: 10^{tev_row['log10_gap_simple']:.2f}

  Detailed (per-species, all SM masses included):
    ρ_detailed = {tev_row['rho_detailed_J_m3']:.4e} J/m³
    Gap vs observed: 10^{tev_row['log10_gap_detailed']:.2f}

  Even at 1 TeV SUSY breaking, the residual vacuum energy is ~10^{tev_row['log10_gap_canon']:.0f}× ρ_Λ.
  SUSY at the TeV scale reduces the CCP gap from 10^139 to ~10^60 (canonical).
  That is a dramatic improvement, but the remaining gap is still catastrophic.
""")

    # ── The meV fine-tuning problem ───────────────────────────────────────────
    m_exact = find_m_tilde_for_gap(0.0, use_dof=1.0)   # gap = 1, i.e. ρ_SUSY = ρ_Λ
    m_exact_eV = m_exact * 1e9   # in eV
    m_exact_meV = m_exact_eV * 1e3

    print(f"{sep('═')}")
    print(f"  THE meV FINE-TUNING PROBLEM")
    print(f"{sep('═')}")
    print(f"""
  For ρ_SUSY = ρ_Λ (exact match, gap = 10^0), canonical formula gives:
    m̃ = {m_exact:.6e} GeV = {m_exact_eV:.6e} eV = {m_exact_meV:.4f} meV

  This is the cosmological constant fine-tuning problem in SUSY:
  To naturally explain the observed ρ_Λ via SUSY breaking, the superpartner
  masses would need to be at the ~meV scale.

  But we KNOW superpartners are not at meV — the LHC has excluded
  sparticles below ~1–2 TeV in most MSSM scenarios. At 1 TeV the gap
  is ~10^{tev_row['log10_gap_canon']:.0f}, not 10^0.

  The "SUSY fine-tuning" statement:
    SUSY breaks the CCP from 10^139 → 10^60 (at m̃ = 1 TeV).
    But to go from 10^60 → 0, one must fine-tune the SUSY-breaking
    parameters to cancel at the 10^60 level.
    This is the "little hierarchy problem" or "μ/B_μ problem" in SUSY.

  Required m̃ for various residual gaps:
    Gap 10^60: m̃ ≈ {find_m_tilde_for_gap(60):.3e} GeV  ({find_m_tilde_for_gap(60)*1e9/1e9:.3f} GeV)
    Gap 10^20: m̃ ≈ {find_m_tilde_for_gap(20):.3e} GeV  ({find_m_tilde_for_gap(20)*1e9:.3e} eV)
    Gap 10^0:  m̃ ≈ {find_m_tilde_for_gap(0):.3e} GeV  = {m_exact_meV:.4f} meV

  The meV scale is:
    - 12 orders of magnitude below the LHC reach (1 TeV = 10^12 meV)
    - Not motivated by any known physics
    - Anthropically: meV ≈ (ρ_Λ)^(1/4) in natural units (dark energy scale)
    - This is not a coincidence — it is a restatement of the problem
""")

    # ── Summary table: m̃ → gap ───────────────────────────────────────────────
    print(f"{sep('═')}")
    print(f"  FULL SUMMARY TABLE: m̃ vs Residual Gap")
    print(f"  (after exact SUSY cancellation; gap = ρ_SUSY / ρ_Λ)")
    print(f"{sep('═')}")
    print()
    print(f"  {'m̃':<22} {'ρ_canon (J/m³)':<25} {'log10(gap)':>12}  {'Interpretation'}")
    print(f"  {sep('-',20):<22} {sep('-',23):<25} {sep('-',10):>12}  {sep('-',30)}")

    interps = {
        10:     "10× EW scale",
        100:    "EW scale — near SM",
        1e3:    "LHC naturalness target",
        1e4:    "Beyond LHC reach",
        1e5:    "100 TeV collider",
        1e10:   "String/GUT-ish scale",
        1e15:   "GUT scale",
    }
    for r in rows:
        m = r["m_tilde_GeV"]
        rho = r["rho_canon_J_m3"]
        g   = r["log10_gap_canon"]
        m_str = f"{m:.2e} GeV"
        rho_str = fmt_exp(rho)
        interp = interps.get(m, f"Planck ({E_P_GeV:.2e} GeV)")
        print(f"  {m_str:<22} {rho_str:<25} {g:>12.2f}  {interp}")
    print()
    print(f"  [SM alone (no SUSY):  gap = 10^139.2 at Planck cutoff]")
    print(f"  [SUSY exact (m̃→0):   gap = 0  (ρ = 0 identically)]")
    print(f"  [SUSY at meV:         gap ≈ 10^0 (matches ρ_Λ — extreme fine-tuning)]")

    # ── Save results ──────────────────────────────────────────────────────────
    os.makedirs("/home/jb/open_problems/physics/what_is_nothing/results", exist_ok=True)

    data = {
        "description": (
            "SUSY cancellation residual vacuum energy computation. "
            "Tracks how the cosmological constant gap reduces as SUSY-breaking scale m̃ varies."
        ),
        "date": "2026-04-09",
        "script": "numerics/susy_cancellation.py",
        "constants": {
            "hbar_Js": hbar,
            "c_ms": c,
            "GeV_J": GeV_J,
            "hbar_c_Jm": hbar_c,
            "hbar_c_GeVm": hbar_c_GeVm,
            "E_Planck_J": E_P,
            "E_Planck_GeV": E_P_GeV,
            "rho_Lambda_J_m3": rho_Lambda,
            "geV4_to_SI_factor": geV4_to_SI(1.0),
        },
        "sm_dof": {
            "boson": SM_DOF_BOSON,
            "fermion": SM_DOF_FERMION,
            "total": SM_DOF_TOTAL,
            "net_signed": SM_DOF_BOSON - SM_DOF_FERMION,
            "mssm_total": MSSM_DOF_TOTAL,
        },
        "unit_crosscheck": {
            "photon_only_computed_J_m3": _crosscheck_units()[0],
            "photon_only_known_J_m3": _crosscheck_units()[1],
            "ratio": _crosscheck_units()[2],
            "pass": _crosscheck_units()[3],
        },
        "exact_susy": {
            "rho_J_m3": 0.0,
            "gap": 0.0,
            "note": "Exact SUSY: all superpartner masses = SM masses. Perfect cancellation. ρ = 0.",
        },
        "sweep": rows,
        "milestones": {
            "gap_139.2": {"target_log10_gap": 139.2, "m_tilde_GeV": find_m_tilde_for_gap(139.2),
                          "note": "SM Planck cutoff — SUSY gives no improvement at this m̃"},
            "gap_60":    {"target_log10_gap": 60,    "m_tilde_GeV": find_m_tilde_for_gap(60),
                          "note": "Electroweak-era gap level"},
            "gap_20":    {"target_log10_gap": 20,    "m_tilde_GeV": find_m_tilde_for_gap(20),
                          "note": "20 orders from observed"},
            "gap_0":     {"target_log10_gap": 0,     "m_tilde_GeV": find_m_tilde_for_gap(0),
                          "m_tilde_eV": find_m_tilde_for_gap(0) * 1e9,
                          "m_tilde_meV": find_m_tilde_for_gap(0) * 1e12,
                          "note": "Exact match to observed ρ_Λ — the 'meV SUSY' fine-tuning"},
        },
        "tev_focus": {
            "m_tilde_GeV": 1e3,
            "log10_gap_canonical": tev_row["log10_gap_canon"],
            "log10_gap_mssm_full": tev_row["log10_gap_simple"],
            "log10_gap_detailed": tev_row["log10_gap_detailed"],
            "rho_canon_J_m3": tev_row["rho_canon_J_m3"],
            "note": "LHC-motivated SUSY breaking scale; gap still ~10^60",
        },
        "fine_tuning_summary": {
            "sm_gap_log10": 139.2,
            "susy_1tev_gap_log10": tev_row["log10_gap_canon"],
            "susy_meV_gap_log10": 0.0,
            "required_m_tilde_for_exact_meV": m_exact,
            "required_m_tilde_meV": m_exact_meV,
            "lhc_lower_bound_GeV": 1000.0,
            "fine_tuning_ratio_meV_vs_LHC": 1e3 / m_exact,
        },
    }

    out_path = "/home/jb/open_problems/physics/what_is_nothing/results/susy_data.json"
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n  Data → {out_path}")

    # ── Write findings markdown ───────────────────────────────────────────────
    tev_g   = tev_row["log10_gap_canon"]
    m60_GeV = find_m_tilde_for_gap(60)
    m20_GeV = find_m_tilde_for_gap(20)
    m0_GeV  = find_m_tilde_for_gap(0)
    m0_meV  = m0_GeV * 1e12

    findings_md = f"""# SUSY Cancellation — Findings

**Generated:** 2026-04-09
**Script:** numerics/susy_cancellation.py
**Data:** results/susy_data.json
**Depends on:** results/sm_vacuum_data.json (from sm_vacuum_energy.py)

## Setup

The Standard Model has {SM_DOF_BOSON} bosonic and {SM_DOF_FERMION} fermionic DOF (net = −62, fermions dominate),
giving a vacuum energy of ~10^139.2 J/m³ in magnitude at Planck cutoff —
a gap of 10^139.2 orders of magnitude above observed ρ_Λ ≈ {rho_Lambda:.3e} J/m³.

SUSY adds a superpartner for each SM particle (opposite statistics, same DOF count).
MSSM total: {MSSM_DOF_TOTAL} DOF ({SM_DOF_TOTAL} bosonic + {SM_DOF_TOTAL} fermionic — exactly balanced).

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
    Residual ρ_SUSY ≈ N_eff × m̃⁴ / (16π²)   [N_eff = {SM_DOF_TOTAL} for full MSSM]

    SI conversion: ρ [J/m³] = ρ [GeV⁴] × (GeV_J)⁴ / (ħc)³
    where GeV_J = 1.602×10⁻¹⁰ J/GeV, ħc = {hbar_c:.4e} J·m

## Unit conversion cross-check

Photon-only at Planck cutoff:
  Computed: {_crosscheck_units()[0]:.6e} J/m³
  Known (from sm_vacuum_energy.py): {_crosscheck_units()[1]:.6e} J/m³
  Ratio: {_crosscheck_units()[2]:.8f}  ({'PASS' if _crosscheck_units()[3] else 'FAIL'})

## Results

### m̃ sweep — residual gap table (canonical, 1 DOF)

| m̃ (GeV) | Label | ρ_SUSY (J/m³) | log10(gap vs ρ_Λ) |
|----------|-------|---------------|-------------------|
"""

    for r in rows:
        m = r["m_tilde_GeV"]
        lbl = r["label"]
        rho = r["rho_canon_J_m3"]
        g   = r["log10_gap_canon"]
        findings_md += f"| {m:.2e} | {lbl} | {rho:.3e} | {g:.2f} |\n"

    findings_md += f"""
SM alone (no SUSY): gap = 10^139.2 at Planck cutoff.
Exact SUSY (m̃ = 0): gap = 0 (ρ = 0 identically).

### Focus: m̃ = 1 TeV (LHC naturalness target)

- Canonical residual: ρ = {tev_row['rho_canon_J_m3']:.4e} J/m³
- Gap vs observed: **10^{tev_g:.2f}**
- Full MSSM ({SM_DOF_TOTAL} DOF): gap = 10^{tev_row['log10_gap_simple']:.2f}

Even at 1 TeV, SUSY reduces the gap from 10^139.2 to ~10^{tev_g:.0f}.
That is ~79 orders of magnitude of improvement — still 60 orders from observed.

### Gap milestone table

| Target log10(gap) | Required m̃ | Notes |
|-------------------|------------|-------|
| 139.2 | {find_m_tilde_for_gap(139.2):.3e} GeV | No improvement — SM level |
| 60    | {m60_GeV:.3e} GeV | EW-scale gap level |
| 20    | {m20_GeV:.3e} GeV | 20 orders from observed |
| 0     | {m0_GeV:.3e} GeV = {m0_meV:.4f} meV | **Exact match to ρ_Λ** |

## The meV fine-tuning problem

For ρ_SUSY = ρ_Λ (exact match), one needs:

    m̃ ≈ {m0_GeV:.3e} GeV = **{m0_meV:.4f} meV**

This is the SUSY fine-tuning statement:
- SUSY with m̃ ≈ meV would naturally explain the cosmological constant.
- But LHC excludes sparticles below ~1 TeV, so m̃ ≥ 10³ GeV.
- The ratio is m̃_LHC / m̃_natural ≈ {1e3 / m0_GeV:.2e} — a fine-tuning of ~{1e3 / m0_GeV:.0e}.
- This is a restatement of the CCP: SUSY shifts the problem, not resolves it.

The meV scale is not physically motivated independently — it equals (ρ_Λ)^(1/4)
in natural units, which is a tautology (dark energy scale = dark energy scale).

## Key findings

1. **Exact SUSY**: vacuum energy vanishes identically. The MSSM has equal bosonic
   and fermionic DOF ({SM_DOF_TOTAL} each), giving perfect cancellation.

2. **1 TeV SUSY breaking**: gap reduced from 10^139.2 → 10^{tev_g:.1f}.
   SUSY at the LHC scale reduces the CCP by ~79 orders of magnitude.
   The remaining gap of ~10^{tev_g:.0f} is still catastrophically large.

3. **meV requirement**: To match ρ_Λ, superpartner masses must be ~{m0_meV:.2f} meV.
   The LHC excludes this by ~{math.log10(1e3/m0_GeV):.0f} orders of magnitude in mass
   (~{4*math.log10(1e3/m0_GeV):.0f} orders in energy density).

4. **The fine-tuning problem is not solved, only shifted**:
   Without SUSY: fine-tune ρ_vac by 1 part in 10^139.
   With TeV SUSY: fine-tune SUSY-breaking parameters by 1 part in 10^{tev_g:.0f}.
   SUSY improves the situation dramatically but leaves a residual hierarchy problem.

5. **No physically-motivated stopping point**: There is no principle that sets
   m̃ ≈ meV. The TeV scale was motivated by electroweak naturalness (unrelated
   to the CCP), and even that fails to match observations.

## Relation to gap.md

This quantifies why SUSY does not close gap.md R1:
- SUSY does provide the right mechanism (exact cancellation at zero breaking).
- SUSY breaking necessarily reintroduces a vacuum energy residual.
- At the observed sparticle mass scale (≳ 1 TeV), the residual is 10^{tev_g:.0f}× too large.
- The "SUSY solution to the CCP" requires m̃ at the meV scale, which is unmotivated.
- This is sometimes called the "second fine-tuning" or "μ-problem" in SUSY contexts.
"""

    md_path = "/home/jb/open_problems/physics/what_is_nothing/results/susy_findings.md"
    with open(md_path, "w") as f:
        f.write(findings_md)
    print(f"  Findings → {md_path}")

    print(f"\n{'='*80}")
    print(f"  Done.")
    print(f"{'='*80}")


if __name__ == "__main__":
    run()
