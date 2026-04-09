#!/usr/bin/env python3
"""
sm_vacuum_energy.py — Standard Model vacuum energy with full particle content.

Context: vacuum_energy.py computed the QFT vacuum energy with ONLY 2 photon
polarizations, giving a gap of ~10^137.7 vs observed cosmological constant.
This script uses the complete Standard Model particle content, where fermions
contribute NEGATIVE zero-point energy (Grassmann statistics).

For exact SUSY, bosonic and fermionic DOF would cancel. The SM does not have
exact SUSY, but the partial cancellation is still significant.

Key formula (per species i):
  ρ_i = s_i × n_i × ħc × k_max^4 / (32π²)
  where s_i = +1 (boson) or -1 (fermion)
  k_max = E_cutoff / (ħc)

Two cutoff scenarios:
  1. Planck scale: E_cutoff = E_P ≈ 1.956e9 J
  2. Electroweak scale: E_cutoff = 100 GeV

Usage:
    cd ~/open_problems/physics/what_is_nothing
    python3 numerics/sm_vacuum_energy.py

Numerical track, what_is_nothing — 2026-04-09
"""

import math, json, os

# ── Physical constants (SI) ───────────────────────────────────────────────────

hbar = 1.054571817e-34   # J·s
c    = 2.99792458e8      # m/s
G    = 6.67430e-11       # m³/(kg·s²)
eV   = 1.602176634e-19   # J per eV
GeV  = 1e9 * eV
MeV  = 1e6 * eV

# Planck scale
l_P  = math.sqrt(hbar * G / c**3)   # ≈ 1.616e-35 m
m_P  = math.sqrt(hbar * c / G)       # ≈ 2.176e-8 kg
E_P  = m_P * c**2                    # ≈ 1.956e9 J  (Planck energy)

# Observed cosmological constant (2023 Planck satellite data)
Lambda_obs = 1.1056e-52              # m⁻²
rho_Lambda = Lambda_obs * c**2 / (8 * math.pi * G)   # J/m³  ≈ 5.924e-27

# ── Standard Model particle table ────────────────────────────────────────────
# Each entry: (name, spin_stat, n_dof, mass_GeV)
#   spin_stat: "boson" → +1, "fermion" → -1
#   n_dof: effective internal degrees of freedom
#   mass_GeV: rest mass (0 = massless, uses only k_max from cutoff)
#
# Degree-of-freedom accounting:
#   Photon:      2 transverse polarizations (gauge field, 2 physical DOF)
#   W± bosons:   3 massive vector DOF × 2 (W+ and W-) = 6  [longitudinal + 2 transverse]
#   Z boson:     3 massive vector DOF
#   Higgs:       1 real scalar (after EWSB, the physical Higgs)
#   Gluons:      8 color × 2 transverse = 16
#   Electron:    2 spin × 2 (particle + antiparticle) = 4 Dirac DOF
#   Muon:        4 (same as electron)
#   Tau:         4
#   Quarks (6):  2 spin × 2 p/ap × 3 color = 12 each
#   Neutrinos:   1 helicity × 2 (ν + ν̄) = 2 each (Weyl/Majorana approximation for massless)
#
# Note: Goldstone bosons eaten by W/Z are NOT counted separately (they become
# the longitudinal polarizations and are already included in n_dof for W/Z).

SM_PARTICLES = [
    # ── Gauge bosons ──────────────────────────────────────────────────────────
    # name,                    stat,      n_dof,  mass_GeV
    ("Photon (γ)",            "boson",   2,      0.0),
    ("W± boson",              "boson",   6,      80.4),     # W+ and W- combined
    ("Z boson",               "boson",   3,      91.2),
    ("Higgs (H)",             "boson",   1,      125.25),
    ("Gluons (g×8)",          "boson",   16,     0.0),
    # ── Charged leptons ───────────────────────────────────────────────────────
    ("Electron (e)",          "fermion", 4,      0.000511),
    ("Muon (μ)",              "fermion", 4,      0.1057),
    ("Tau (τ)",               "fermion", 4,      1.777),
    # ── Neutrinos (massless approximation) ───────────────────────────────────
    ("Neutrino νe",           "fermion", 2,      0.0),
    ("Neutrino νμ",           "fermion", 2,      0.0),
    ("Neutrino ντ",           "fermion", 2,      0.0),
    # ── Quarks (×3 color) ────────────────────────────────────────────────────
    ("Up quark (u)",          "fermion", 12,     0.0022),
    ("Down quark (d)",        "fermion", 12,     0.0047),
    ("Strange quark (s)",     "fermion", 12,     0.096),
    ("Charm quark (c)",       "fermion", 12,     1.27),
    ("Bottom quark (b)",      "fermion", 12,     4.18),
    ("Top quark (t)",         "fermion", 12,     173.1),
]

# ── Core computation ─────────────────────────────────────────────────────────

def rho_single_species(n_dof: int, sign: float, mass_GeV: float,
                       cutoff_J: float) -> float:
    """
    Zero-point energy density for a single species.

    ρ = sign × n_dof × ħc × k_max⁴ / (32π²)

    For massless particles k_max = cutoff_J / (ħc).
    For massive particles we still use Planck cutoff (mass << E_P always).
    The mass determines whether the species is relevant below a given cutoff:
    if cutoff_J < mass_GeV × GeV × c² we zero it out (particle not excited).
    """
    mass_J = mass_GeV * GeV    # mass × c² in Joules (natural units where c=1: E = mc²)
    # If cutoff is below particle mass threshold, this species is decoupled
    if cutoff_J < mass_J and mass_J > 0:
        return 0.0
    k_max = cutoff_J / (hbar * c)
    rho = sign * n_dof * hbar * c * k_max**4 / (32 * math.pi**2)
    return rho


def compute_sm_vacuum(cutoff_J: float, label: str):
    """
    Compute full SM vacuum energy at a given cutoff.
    Returns a dict with per-species breakdown and totals.
    """
    total_boson = 0.0
    total_fermion = 0.0
    total_dof_boson = 0
    total_dof_fermion = 0
    species_list = []

    for name, stat, n_dof, mass_GeV in SM_PARTICLES:
        sign = +1.0 if stat == "boson" else -1.0
        rho = rho_single_species(n_dof, sign, mass_GeV, cutoff_J)

        if stat == "boson":
            total_boson += rho
            total_dof_boson += n_dof
        else:
            total_fermion += rho
            total_dof_fermion += n_dof

        species_list.append({
            "name": name,
            "stat": stat,
            "sign": sign,
            "n_dof": n_dof,
            "mass_GeV": mass_GeV,
            "rho_J_per_m3": rho,
        })

    total_rho = total_boson + total_fermion
    net_dof = total_dof_boson - total_dof_fermion   # signed: positive → more boson DOF

    return {
        "cutoff_label": label,
        "cutoff_J": cutoff_J,
        "species": species_list,
        "rho_boson_J_per_m3": total_boson,
        "rho_fermion_J_per_m3": total_fermion,
        "rho_total_J_per_m3": total_rho,
        "dof_boson": total_dof_boson,
        "dof_fermion": total_dof_fermion,
        "net_signed_dof": net_dof,
    }


# ── Run both cutoffs ──────────────────────────────────────────────────────────

result_planck = compute_sm_vacuum(E_P, "Planck scale (~1.956e9 J)")
result_ew     = compute_sm_vacuum(100 * GeV, "Electroweak scale (~100 GeV)")

# Photon-only baseline (what vacuum_energy.py computed)
rho_photon_only = rho_single_species(2, +1.0, 0.0, E_P)


# ── Pretty-print ──────────────────────────────────────────────────────────────

def log10_safe(x):
    if x == 0.0:
        return float('-inf')
    return math.log10(abs(x))


def fmt_rho(rho):
    if rho == 0.0:
        return "     0.0 (decoupled)"
    exp = math.floor(math.log10(abs(rho)))
    mantissa = rho / 10**exp
    sign_str = "+" if rho >= 0 else "-"
    return f"{sign_str}{abs(mantissa):.3f} × 10^{exp:+d} J/m³"


def print_table(result):
    label = result["cutoff_label"]
    print(f"\n{'═'*72}")
    print(f"  CUTOFF: {label}")
    print(f"{'═'*72}")
    print(f"  {'Particle':<25} {'Stat':>7}  {'DOF':>4}  {'Contribution':>30}  {'Sign'}")
    print(f"  {'─'*70}")

    running = 0.0
    for sp in result["species"]:
        rho = sp["rho_J_per_m3"]
        running += rho
        stat_str = "boson " if sp["stat"] == "boson" else "fermion"
        sign_ch  = "+" if sp["sign"] > 0 else "−"
        if rho == 0.0:
            rho_str = "  (decoupled at this cutoff)"
        else:
            exp = math.floor(log10_safe(rho))
            m   = rho / 10**exp
            rho_str = f"  {m:+.3f} × 10^{exp:+d}"
        print(f"  {sp['name']:<25} {stat_str:>7}  {sp['n_dof']:>4}  {rho_str:<32}")

    print(f"  {'─'*70}")

    rb = result["rho_boson_J_per_m3"]
    rf = result["rho_fermion_J_per_m3"]
    rt = result["rho_total_J_per_m3"]

    def gap_str(rho_val):
        if rho_val == 0.0:
            return "exact cancellation"
        ratio = abs(rho_val) / rho_Lambda
        return f"10^{math.log10(ratio):.1f} × ρ_Λ"

    print(f"\n  Boson total   (n_dof={result['dof_boson']:>3}): {fmt_rho(rb)}")
    print(f"  Fermion total (n_dof={result['dof_fermion']:>3}): {fmt_rho(rf)}")
    print(f"  ─── NET SM total ────────────────────: {fmt_rho(rt)}")
    print(f"\n  Observed ρ_Λ:    {rho_Lambda:.4e} J/m³")
    print(f"  Boson-only gap:  {gap_str(rb)}")
    print(f"  SM-total gap:    {gap_str(rt)}")

    gap_bosons_only = log10_safe(rb / rho_Lambda)
    gap_sm_total    = log10_safe(abs(rt) / rho_Lambda)
    if rt > 0:
        sign_note = "(net positive — bosons dominate)"
    else:
        sign_note = "(net negative — fermions dominate)"
    print(f"\n  Gap (bosons only):  10^{gap_bosons_only:.2f} orders of magnitude")
    print(f"  Gap (SM total):     10^{gap_sm_total:.2f} orders of magnitude  {sign_note}")
    cancellation_orders = gap_bosons_only - gap_sm_total
    print(f"  Fermion cancellation reduces gap by: {cancellation_orders:.2f} orders of magnitude")


def run():
    print("=" * 72)
    print("  Standard Model Vacuum Energy — Full Particle Content")
    print("  Cosmological Constant Problem: SM fermion partial cancellation")
    print("=" * 72)

    print(f"\n  Physical constants:")
    print(f"    ħ         = {hbar:.6e} J·s")
    print(f"    c         = {c:.8e} m/s")
    print(f"    E_Planck  = {E_P:.4e} J = {E_P/GeV:.2e} GeV")
    print(f"    ρ_Λ (obs) = {rho_Lambda:.4e} J/m³")

    print(f"\n  Photon-only baseline (from vacuum_energy.py, Planck cutoff):")
    print(f"    ρ_photon  = {rho_photon_only:.4e} J/m³")
    print(f"    Gap       = 10^{log10_safe(rho_photon_only/rho_Lambda):.2f}")

    print(f"\n  SM degree-of-freedom inventory:")
    total_b = sum(n for _, s, n, _ in SM_PARTICLES if s == "boson")
    total_f = sum(n for _, s, n, _ in SM_PARTICLES if s == "fermion")
    print(f"    Bosonic DOF:   {total_b}")
    print(f"    Fermionic DOF: {total_f}")
    print(f"    Net DOF (B-F): {total_b - total_f}  "
          f"({'bosons win' if total_b > total_f else 'fermions win'})")
    print(f"    (Exact SUSY would require B = F = 0 net, giving exact cancellation)")

    # Print tables for both cutoffs
    print_table(result_planck)
    print_table(result_ew)

    # ── Summary comparison ──────────────────────────────────────────────────
    print(f"\n{'═'*72}")
    print(f"  SUMMARY: How much does SM fermion cancellation help?")
    print(f"{'═'*72}")

    for result in [result_planck, result_ew]:
        rb = result["rho_boson_J_per_m3"]
        rt = result["rho_total_J_per_m3"]
        g_b = log10_safe(rb / rho_Lambda)
        g_t = log10_safe(abs(rt) / rho_Lambda)
        saved = g_b - g_t
        print(f"\n  [{result['cutoff_label']}]")
        print(f"    Bosons-only gap:        10^{g_b:.1f}")
        print(f"    SM total (±) gap:       10^{g_t:.1f}")
        print(f"    Orders saved by fermion cancellation: {saved:.1f}")
        print(f"    Remaining gap:          10^{g_t:.1f} (still catastrophic)")

    print(f"\n  Conclusion:")
    g_b_p = log10_safe(result_planck["rho_boson_J_per_m3"] / rho_Lambda)
    g_t_p = log10_safe(abs(result_planck["rho_total_J_per_m3"]) / rho_Lambda)
    g_b_ew = log10_safe(result_ew["rho_boson_J_per_m3"] / rho_Lambda)
    g_t_ew = log10_safe(abs(result_ew["rho_total_J_per_m3"]) / rho_Lambda)
    net_dof = total_b - total_f   # negative: SM has more fermion DOF
    rt_p_sign = "positive" if result_planck["rho_total_J_per_m3"] > 0 else "negative"
    print(f"    Surprise: SM has {total_f} fermionic vs {total_b} bosonic DOF (net = {net_dof}).")
    print(f"    Fermions DOMINATE — net vacuum energy is {rt_p_sign}.")
    print(f"    Magnitude gap at Planck cutoff: 10^{g_t_p:.1f} ({g_t_p - g_b_p:+.2f} vs bosons-only).")
    print(f"    The SM makes the cosmological constant problem SLIGHTLY WORSE.")
    print(f"    Only BSM physics with extra bosonic DOF (e.g. SUSY) can cancel fermions.")
    print(f"    Even with EW cutoff: gap = 10^{g_t_ew:.1f} (vs observed ρ_Λ).")
    print(f"    The cosmological constant problem is NOT resolved by the SM alone.")

    # ── Save results ─────────────────────────────────────────────────────────
    os.makedirs("results", exist_ok=True)

    # Prepare JSON-serializable species lists
    def species_for_json(result):
        lst = []
        for sp in result["species"]:
            lst.append({
                "name": sp["name"],
                "stat": sp["stat"],
                "n_dof": sp["n_dof"],
                "mass_GeV": sp["mass_GeV"],
                "rho_J_per_m3": sp["rho_J_per_m3"],
            })
        return lst

    data = {
        "observed_rho_Lambda_J_per_m3": rho_Lambda,
        "photon_only_Planck_J_per_m3": rho_photon_only,
        "photon_only_gap_log10": log10_safe(rho_photon_only / rho_Lambda),
        "planck_cutoff": {
            "cutoff_J": E_P,
            "cutoff_label": result_planck["cutoff_label"],
            "rho_boson_J_per_m3": result_planck["rho_boson_J_per_m3"],
            "rho_fermion_J_per_m3": result_planck["rho_fermion_J_per_m3"],
            "rho_total_J_per_m3": result_planck["rho_total_J_per_m3"],
            "dof_boson": result_planck["dof_boson"],
            "dof_fermion": result_planck["dof_fermion"],
            "net_signed_dof": result_planck["net_signed_dof"],
            "gap_bosons_only_log10": log10_safe(result_planck["rho_boson_J_per_m3"] / rho_Lambda),
            "gap_sm_total_log10": log10_safe(abs(result_planck["rho_total_J_per_m3"]) / rho_Lambda),
            "orders_saved_by_fermions": (
                log10_safe(result_planck["rho_boson_J_per_m3"] / rho_Lambda) -
                log10_safe(abs(result_planck["rho_total_J_per_m3"]) / rho_Lambda)
            ),
            "species": species_for_json(result_planck),
        },
        "ew_cutoff": {
            "cutoff_J": 100 * GeV,
            "cutoff_label": result_ew["cutoff_label"],
            "rho_boson_J_per_m3": result_ew["rho_boson_J_per_m3"],
            "rho_fermion_J_per_m3": result_ew["rho_fermion_J_per_m3"],
            "rho_total_J_per_m3": result_ew["rho_total_J_per_m3"],
            "dof_boson": result_ew["dof_boson"],
            "dof_fermion": result_ew["dof_fermion"],
            "net_signed_dof": result_ew["net_signed_dof"],
            "gap_bosons_only_log10": log10_safe(result_ew["rho_boson_J_per_m3"] / rho_Lambda),
            "gap_sm_total_log10": log10_safe(abs(result_ew["rho_total_J_per_m3"]) / rho_Lambda),
            "orders_saved_by_fermions": (
                log10_safe(result_ew["rho_boson_J_per_m3"] / rho_Lambda) -
                log10_safe(abs(result_ew["rho_total_J_per_m3"]) / rho_Lambda)
            ),
            "species": species_for_json(result_ew),
        },
        "sm_dof_boson": total_b,
        "sm_dof_fermion": total_f,
        "sm_net_dof": total_b - total_f,
        "note": (
            "Formula: rho_i = sign_i * n_i * hbar*c * k_max^4 / (32*pi^2). "
            "All species use E_Planck as cutoff (massive particles decoupled if mass > cutoff). "
            "Exact SUSY would give net_dof=0 and exact cancellation."
        ),
    }

    with open("results/sm_vacuum_data.json", "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n  Data → results/sm_vacuum_data.json")

    # ── Write findings markdown ───────────────────────────────────────────────
    g_b_p_val  = log10_safe(result_planck["rho_boson_J_per_m3"] / rho_Lambda)
    g_t_p_val  = log10_safe(abs(result_planck["rho_total_J_per_m3"]) / rho_Lambda)
    g_b_ew_val = log10_safe(result_ew["rho_boson_J_per_m3"] / rho_Lambda)
    g_t_ew_val = log10_safe(abs(result_ew["rho_total_J_per_m3"]) / rho_Lambda)
    saved_p    = g_b_p_val - g_t_p_val
    net_sign   = "+" if result_planck["rho_total_J_per_m3"] > 0 else "-"

    findings_md = f"""# SM Vacuum Energy — Findings

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
| **Total** | **{total_b}** | **{total_f}** |

Net signed DOF (B − F) = {total_b} − {total_f} = **{total_b - total_f}**
({'bosons exceed fermions' if total_b > total_f else 'fermions exceed bosons by ' + str(total_f - total_b) + ' DOF'}).

Exact SUSY would require net DOF = 0, giving exact cancellation of vacuum energy.

## Surprising result: fermions dominate

The SM has **{total_f} fermionic DOF vs {total_b} bosonic DOF** — quarks alone contribute
72 fermionic DOF (6 flavors × 2 spin × 2 p/ap × 3 color), swamping the 28 bosonic DOF.
As a result the net SM vacuum energy is **negative** (fermions win), and actually
*larger* in magnitude than bosons alone. The SM does not partially cancel the
cosmological constant problem — it makes it slightly worse in absolute value.

## Results

### Planck-scale cutoff (~1.956e9 J ≈ 1.22e19 GeV)

| Quantity | Value | Gap vs ρ_Λ |
|----------|-------|------------|
| Photon-only baseline | {rho_photon_only:.3e} J/m³ | 10^{log10_safe(rho_photon_only/rho_Lambda):.1f} |
| SM bosons only | {result_planck['rho_boson_J_per_m3']:.3e} J/m³ | 10^{g_b_p_val:.1f} |
| SM fermion contribution | {result_planck['rho_fermion_J_per_m3']:.3e} J/m³ | — |
| SM total (bosons + fermions) | {result_planck['rho_total_J_per_m3']:.3e} J/m³ | 10^{g_t_p_val:.1f} |
| Observed ρ_Λ | {rho_Lambda:.3e} J/m³ | — |

Net SM total is **negative** — fermions (DOF={total_f}) overwhelm bosons (DOF={total_b}).
The net magnitude gap 10^{g_t_p_val:.1f} is {saved_p:.2f} orders *worse* than bosons alone.

### Electroweak-scale cutoff (~100 GeV)

| Quantity | Value | Gap vs ρ_Λ |
|----------|-------|------------|
| SM bosons only | {result_ew['rho_boson_J_per_m3']:.3e} J/m³ | 10^{g_b_ew_val:.1f} |
| SM total (bosons + fermions) | {result_ew['rho_total_J_per_m3']:.3e} J/m³ | 10^{g_t_ew_val:.1f} |
| Observed ρ_Λ | {rho_Lambda:.3e} J/m³ | — |

Even at the electroweak scale (where the SM has been tested), the gap is ~10^{g_t_ew_val:.0f} orders of magnitude.

## Key finding

The SM has 90 fermionic vs 28 bosonic DOF (net = −62, fermions win).
At Planck cutoff:
- Bosons-only gap: 10^{g_b_p_val:.1f}
- Full SM gap (|net|): 10^{g_t_p_val:.1f}
- Fermions make the magnitude **worse** by {abs(saved_p):.2f} orders — they do not cancel bosons,
  they add a larger negative contribution.

This is the opposite of naive intuition. The SM does NOT partially solve the
cosmological constant problem — the quark sector's 72 fermionic DOF dominate.

For fermion cancellation to reduce the gap, you need extra bosonic species (as in SUSY,
which adds a bosonic superpartner for every fermion). With exact SUSY and degenerate
masses, net DOF = 0 and the vacuum energy vanishes identically.

## Physical interpretation

The SM has more fermionic DOF ({total_f}) than bosonic ({total_b}), so the net
vacuum energy is negative at both cutoffs. The sign is unphysical anyway (the
observed cosmological constant is positive), reinforcing that something beyond
naive mode-counting is required.

The cosmological constant problem is NOT resolved by the SM:
- SUSY would cancel exactly if masses were degenerate (they are not)
- Actual SUSY breaking scale ≫ observed Λ^(1/4) ~ 2.3 meV
- The remaining 10^{g_t_p_val:.0f} discrepancy at Planck cutoff (10^{g_t_ew_val:.0f} at EW cutoff)
  requires physics beyond the Standard Model

## Relation to gap.md R1

This calculation quantifies gap.md R1: the cosmological constant problem.
- The oft-cited "10^120" figure uses the EW cutoff with only the Higgs/gauge sector
  (fewer fermions), or assumes near-equal B/F DOF as a schematic estimate.
- Our photon-only result gave 10^{log10_safe(rho_photon_only/rho_Lambda):.1f} (Planck).
- The full SM at Planck cutoff gives 10^{g_t_p_val:.1f} (net |ρ|), slightly worse than photon-only.
- No known symmetry principle explains the residual fine-tuning.
- The SM does not reduce the cosmological constant problem; only a BSM mechanism
  (SUSY, extra dimensions, anthropic selection, or quantum gravity) can address it.
"""

    with open("results/sm_vacuum_findings.md", "w") as f:
        f.write(findings_md)
    print(f"  Findings → results/sm_vacuum_findings.md")

    print(f"\n{'='*72}")
    print(f"  Done.")
    print(f"{'='*72}")


if __name__ == "__main__":
    run()
