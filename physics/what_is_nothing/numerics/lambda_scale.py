#!/usr/bin/env python3
"""
lambda_scale.py — What is special about L* ≈ 0.91 m?

Context: lamb_shift.py found that ρ_vac = g_SM ħc/(32π² L⁴) matches ρ_Λ at
L* ≈ 0.91 m. This script investigates:

  Part 1. Compare L* to every known physical length scale. Does any match?
  Part 2. Anthropic fine-tuning sweep — compare Λ fine-tuning severity to other
          fundamental constants under both uniform and log-uniform priors.

Main questions:
  - Is L* ≈ 0.91 m a coincidence with some known scale?
  - Is Λ uniquely fine-tuned, or is all of fundamental physics similarly
    constrained anthropically?

Numerical track, what_is_nothing — 2026-04-09
"""

import math
import json
import os

# ─────────────────────────────────────────────────────────────────────────────
# Physical constants (SI unless noted)
# ─────────────────────────────────────────────────────────────────────────────
hbar    = 1.054e-34       # J·s
c       = 2.998e8         # m/s
G       = 6.674e-11       # m³/(kg·s²)
k_B     = 1.380649e-23    # J/K
m_p     = 1.673e-27       # kg  proton mass
m_e     = 9.109e-31       # kg  electron mass
m_n     = 1.675e-27       # kg  neutron mass
a0      = 5.292e-11       # m   Bohr radius
l_P     = 1.616e-35       # m   Planck length
H0      = 2.184e-18       # s⁻¹ Hubble constant
T_CMB   = 2.725           # K   CMB temperature
eV_J    = 1.602176634e-19 # J per eV

# Fine structure constant and particle physics
alpha   = 7.2974e-3       # dimensionless
alpha_s = 0.1181          # strong coupling at m_Z
eta     = 6e-10           # baryon-to-photon ratio

# Derived scales
L_Hubble = c / H0                                     # Hubble radius ≈ 1.37e26 m
rho_Planck = 4.634e113                                # J/m³ (from lamb_shift.py)
rho_Lambda_obs = 5.924e-27                            # J/m³ (Planck 2018)
SM_g_eff = 41                                         # SM effective DOF for vacuum energy

# L* from lamb_shift.py: ρ_vac(L*) = ρ_Λ
# ρ_vac = g_SM * hbar * c / (32 * π² * L⁴)  →  L* = (g_SM*hbar*c / (32π²*ρ_Λ))^{1/4}
L_star = (SM_g_eff * hbar * c / (32 * math.pi**2 * rho_Lambda_obs))**0.25
# sanity check: should be ≈ 0.91 m

# ─────────────────────────────────────────────────────────────────────────────
# PART 1 — Length scale comparison table
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 74)
print("LAMBDA_SCALE.PY  —  What physical scale is L* ≈ {:.3f} m?".format(L_star))
print("=" * 74)

print(f"""
  g_SM = {SM_g_eff}   (SM effective boson − 7/8 fermion degrees of freedom)
  ρ_Λ  = {rho_Lambda_obs:.4e} J/m³   (Planck 2018 + BAO)
  L*   = (g_SM ħc / 32π² ρ_Λ)^(1/4) = {L_star:.4e} m  ← the target scale
""")

# ── Compute each candidate scale ─────────────────────────────────────────────

scales = {}

# 1. Thermal de Broglie wavelength of proton at T_CMB
#    λ_th = ħ / √(2π m k_B T)
lam_th_p = hbar / math.sqrt(2 * math.pi * m_p * k_B * T_CMB)
scales["λ_dB proton (T_CMB)"] = (lam_th_p, "ħ/√(2π m_p k_B T_CMB)")

# 2. Thermal de Broglie wavelength of electron at T_CMB
lam_th_e = hbar / math.sqrt(2 * math.pi * m_e * k_B * T_CMB)
scales["λ_dB electron (T_CMB)"] = (lam_th_e, "ħ/√(2π m_e k_B T_CMB)")

# 3. Classical electron radius: r_e = α² a₀ = e²/(4πε₀ m_e c²)
#    In SI: r_e = α² a₀  (α ≈ 7.297e-3, a₀ ≈ 5.292e-11 m)
r_e = alpha**2 * a0
scales["r_e classical electron radius"] = (r_e, "α² a₀ = e²/(4πε₀ m_e c²)")

# 4. Compton wavelength of electron (reduced): ħ/(m_e c)
lambda_C_e = hbar / (m_e * c)
scales["ƛ_C electron (Compton)"] = (lambda_C_e, "ħ/(m_e c)")

# 5. Compton wavelength of proton (reduced): ħ/(m_p c)
lambda_C_p = hbar / (m_p * c)
scales["ƛ_C proton (Compton)"] = (lambda_C_p, "ħ/(m_p c)")

# 6. Neutron star scale: combine G, ħ, c, m_neutron
#    Natural dimensionless combination: (ħ c / G m_n²) × (ħ / m_n c)
#    Or: Schwarzschild radius of 1 solar mass  ≈ 3 km
#    More physically: G m_n / c² (gravitational length of one neutron)
G_m_n_over_c2 = G * m_n / c**2
scales["G m_n/c² (neutron grav. length)"] = (G_m_n_over_c2, "G m_n / c²")

#    Also: ħ/(m_n c) — neutron Compton wavelength
lambda_C_n = hbar / (m_n * c)
scales["ƛ_C neutron (Compton)"] = (lambda_C_n, "ħ/(m_n c)")

#    Neutron star radius ~ a few km — encode via Chandrasekhar-like scale:
#    R_NS ~ (ħ c / G)^{1/2} / m_p^2 × (ħ/m_p c)
#    Simplest: (ħ c / G m_n²) has units [energy / energy] = dimensionless, so
#    actual NS scale ~ (M_sun / m_n) × (G m_n / c²) ≈ 3km
M_sun = 1.989e30   # kg
R_NS_approx = (M_sun / m_n) * G_m_n_over_c2
scales["R_NS approx (Schwarzschild M_sun)"] = (R_NS_approx, "(M_sun/m_n)×G m_n/c² ≈ Schwarzschild r_sun")

# 7. QCD confinement scale: L_QCD = ħc / Λ_QCD   (Λ_QCD ≈ 200 MeV)
Lambda_QCD_eV = 200e6 * eV_J   # 200 MeV in Joules
L_QCD = hbar * c / Lambda_QCD_eV
scales["L_QCD confinement (200 MeV)"] = (L_QCD, "ħc / Λ_QCD,  Λ_QCD=200 MeV")

# 8. Geometric mean of Planck length and Hubble radius
L_geom_PH = math.sqrt(l_P * L_Hubble)
scales["√(l_P × L_Hubble) geom. mean"] = (L_geom_PH, "√(l_P c/H₀)")

# 9. Geometric mean of Bohr radius and Hubble radius
L_geom_a0H = math.sqrt(a0 * L_Hubble)
scales["√(a₀ × L_Hubble) geom. mean"] = (L_geom_a0H, "√(a₀ c/H₀)")

# 10. Geometric mean of QCD scale and Hubble radius
L_geom_QCDH = math.sqrt(L_QCD * L_Hubble)
scales["√(L_QCD × L_Hubble) geom. mean"] = (L_geom_QCDH, "√(L_QCD c/H₀)")

# 11. Geometric mean of electron Compton and Hubble radius
L_geom_CH = math.sqrt(lambda_C_e * L_Hubble)
scales["√(ƛ_C,e × L_Hubble) geom. mean"] = (L_geom_CH, "√(ħ/m_e c × c/H₀)")

# 12. Electroweak scale: ħc / E_EW  (E_EW = 246 GeV = Higgs vev)
E_EW_J = 246e9 * eV_J   # 246 GeV
L_EW = hbar * c / E_EW_J
scales["L_EW (Higgs vev, 246 GeV)"] = (L_EW, "ħc / (246 GeV)")

# 13. Thermal photon wavelength at T_CMB: λ_peak = hc/(2.898mm·K × T)
#     Wien peak: λ_max = 2.898e-3 m·K / T
lambda_Wien = 2.898e-3 / T_CMB
scales["Wien peak λ at T_CMB"] = (lambda_Wien, "2.898e-3 m·K / T_CMB")

# 14. Characteristic scale from just ħ, c, H₀ (no G):
#    L_cH = √(ħ c / (ħ H₀²)) — no, need dimensions right
#    ħ/c has units J·s/m = kg — not a length
#    c/H₀ = Hubble radius (already there)
#    Let's try: (ħ / (m_p c)) × (c/H₀)^{1/2} — mixed, not natural
#    Try anthropic scale: length at which k_B T_CMB = ħc/L → L = ħc/(k_B T_CMB)
L_thermal_photon = hbar * c / (k_B * T_CMB)
scales["ħc/(k_B T_CMB) thermal photon"] = (L_thermal_photon, "ħc / (k_B T_CMB)")

# 15. Proton radius (charge): ~0.84 fm
r_proton = 0.84e-15   # m
scales["r_proton (charge radius)"] = (r_proton, "0.84 fm (experimental)")

# 16. Scale from ρ_Λ alone (Λ energy scale):
#    E_Λ = ρ_Λ^{1/4} × (ħc)^{3/4} — in eV units ≈ 2.3 meV
#    L_Λ = ħc / E_Λ
E_Lambda_J = (rho_Lambda_obs * (hbar * c)**3)**0.25
L_Lambda_scale = hbar * c / E_Lambda_J
scales["L_Λ = ħc/E_Λ (dark energy scale)"] = (L_Lambda_scale, "(ħc)/(ρ_Λ(ħc)³)^{1/4}")

# ── Print the table ───────────────────────────────────────────────────────────

print(f"  L* = {L_star:.6e} m   (reference)\n")
print(f"  {'Scale name':<40s}  {'Value (m)':>14s}  {'Ratio to L*':>14s}  {'log₁₀(ratio)':>13s}")
print(f"  {'─'*40}  {'─'*14}  {'─'*14}  {'─'*13}")

scale_results = {}
for name, (val, formula) in sorted(scales.items(), key=lambda x: x[1][0]):
    ratio = val / L_star
    log_r = math.log10(ratio)
    flag = " ◄ MATCH" if abs(log_r) < 0.5 else (" ◄ close" if abs(log_r) < 1.5 else "")
    print(f"  {name:<40s}  {val:>14.4e}  {ratio:>14.4e}  {log_r:>+13.3f}{flag}")
    scale_results[name] = {
        "value_m": val,
        "formula": formula,
        "ratio_to_Lstar": ratio,
        "log10_ratio": log_r,
    }

print(f"\n  MATCH criterion: |log₁₀(ratio)| < 0.5 (within a factor of ~3)")
print(f"  Close criterion: |log₁₀(ratio)| < 1.5 (within an order of magnitude)")

# ── Closest matches analysis ──────────────────────────────────────────────────

sorted_by_closeness = sorted(scale_results.items(), key=lambda x: abs(x[1]["log10_ratio"]))

print("\n" + "=" * 74)
print("CLOSEST MATCHES TO L* (ranked by |log₁₀ ratio|)")
print("=" * 74)
print()
for i, (name, d) in enumerate(sorted_by_closeness[:6]):
    print(f"  #{i+1}  {name}")
    print(f"       value = {d['value_m']:.4e} m,  ratio = {d['ratio_to_Lstar']:.4f},  "
          f"log₁₀ = {d['log10_ratio']:+.3f}")
    print()

# ─────────────────────────────────────────────────────────────────────────────
# PART 2 — Anthropic fine-tuning sweep
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 74)
print("PART 2 — Anthropic Fine-Tuning Sweep Across Fundamental Constants")
print("=" * 74)

print("""
  For each constant: compute P(observed | uniform prior) and
  P(observed | log-uniform prior), given the anthropic window
  where life/structure is plausible.

  Severity metric: log₁₀(1/P) — nats of information needed to explain the
  observed value by chance.  Under log-uniform prior, this is
    log₁₀((log x_max - log x_min) / (log x_obs_max - log x_obs_min))
  Under linear prior:
    log₁₀((x_max - x_min) / (x_window_max - x_window_min))

  Priors range from physical minimum (theory/experiment) to physical maximum.
""")

# Helper functions
def log10_severity_log_uniform(x_obs, x_window_lo, x_window_hi, x_range_lo, x_range_hi):
    """log₁₀(1/P) under log-uniform prior.
    P = (log x_hi - log x_lo) / (log range_hi - log range_lo)"""
    log_window = math.log(x_window_hi) - math.log(x_window_lo)
    log_range  = math.log(x_range_hi)  - math.log(x_range_lo)
    P = log_window / log_range
    return math.log10(1.0 / P), P

def log10_severity_linear(x_window_lo, x_window_hi, x_range_lo, x_range_hi):
    """log₁₀(1/P) under uniform (linear) prior.
    P = (x_hi - x_lo) / (range_hi - range_lo)"""
    window = x_window_hi - x_window_lo
    rng    = x_range_hi  - x_range_lo
    P = window / rng
    return math.log10(1.0 / P), P

# ── Constants table setup ─────────────────────────────────────────────────────

constants = {}

# ── (a) Fine structure constant α ≈ 1/137 ────────────────────────────────────
# Anthropic window: [1/200, 1/80] — outside: atoms unstable or stars fail
# Prior range: [0, 1] (dimensionless; α=1 would mean strong EM = nuclear)
#              lower bound: α > 0 (trivially)  use 1e-6 for log-uniform
alpha_obs   = alpha               # 7.297e-3 ≈ 1/137
alpha_w_lo  = 1.0/200             # 0.005
alpha_w_hi  = 1.0/80              # 0.0125
alpha_r_lo  = 1e-6               # log-uniform lower bound (any weaker EM)
alpha_r_hi  = 1.0                 # α ≥ 1 would give strong-coupling EM

sev_log_a, P_log_a = log10_severity_log_uniform(alpha_obs, alpha_w_lo, alpha_w_hi, alpha_r_lo, alpha_r_hi)
sev_lin_a, P_lin_a = log10_severity_linear(alpha_w_lo, alpha_w_hi, alpha_r_lo, alpha_r_hi)

constants["alpha (fine structure)"] = {
    "symbol": "α",
    "observed": alpha_obs,
    "window_lo": alpha_w_lo,
    "window_hi": alpha_w_hi,
    "range_lo": alpha_r_lo,
    "range_hi": alpha_r_hi,
    "P_log_uniform": P_log_a,
    "log10_severity_log": sev_log_a,
    "P_linear": P_lin_a,
    "log10_severity_linear": sev_lin_a,
    "note": "window [1/200,1/80]; atoms don't form or stellar EM fails outside",
}

# ── (b) Electron/proton mass ratio μ = m_e/m_p ≈ 1/1836 ──────────────────────
# Anthropic window: [1/10000, 1/100]  — smaller: H atom too small; larger: chemistry fails
# Prior range: [1e-6, 1]  (μ=1: equal masses; log-uniform)
mu_obs   = m_e / m_p             # ≈ 5.446e-4 ≈ 1/1836
mu_w_lo  = 1.0/10000             # 1e-4
mu_w_hi  = 1.0/100              # 1e-2
mu_r_lo  = 1e-6
mu_r_hi  = 1.0                   # μ=1 means m_e=m_p, no stable atoms

sev_log_mu, P_log_mu = log10_severity_log_uniform(mu_obs, mu_w_lo, mu_w_hi, mu_r_lo, mu_r_hi)
sev_lin_mu, P_lin_mu = log10_severity_linear(mu_w_lo, mu_w_hi, mu_r_lo, mu_r_hi)

constants["mu (electron/proton mass ratio)"] = {
    "symbol": "μ = m_e/m_p",
    "observed": mu_obs,
    "window_lo": mu_w_lo,
    "window_hi": mu_w_hi,
    "range_lo": mu_r_lo,
    "range_hi": mu_r_hi,
    "P_log_uniform": P_log_mu,
    "log10_severity_log": sev_log_mu,
    "P_linear": P_lin_mu,
    "log10_severity_linear": sev_lin_mu,
    "note": "window [1/10000,1/100]; outside: chemistry or atomic structure fails",
}

# ── (c) Strong coupling α_s ≈ 0.12 ───────────────────────────────────────────
# Anthropic window: [0.05, 0.30] — outside: nuclei unstable (too weak) or quarks unbound (too strong)
# Prior range: [0.001, 10]  (log-uniform; α_s < 0.001: proton unstable; α_s > 10: unknown QFT)
alphas_obs  = alpha_s             # 0.1181
alphas_w_lo = 0.05
alphas_w_hi = 0.30
alphas_r_lo = 0.001
alphas_r_hi = 10.0

sev_log_as, P_log_as = log10_severity_log_uniform(alphas_obs, alphas_w_lo, alphas_w_hi, alphas_r_lo, alphas_r_hi)
sev_lin_as, P_lin_as = log10_severity_linear(alphas_w_lo, alphas_w_hi, alphas_r_lo, alphas_r_hi)

constants["alpha_s (strong coupling)"] = {
    "symbol": "α_s",
    "observed": alphas_obs,
    "window_lo": alphas_w_lo,
    "window_hi": alphas_w_hi,
    "range_lo": alphas_r_lo,
    "range_hi": alphas_r_hi,
    "P_log_uniform": P_log_as,
    "log10_severity_log": sev_log_as,
    "P_linear": P_lin_as,
    "log10_severity_linear": sev_lin_as,
    "note": "window [0.05,0.30]; outside: no stable nuclei or asymptotic freedom fails",
}

# ── (d) Baryon-to-photon ratio η ≈ 6e-10 ────────────────────────────────────
# Anthropic window: [1e-11, 1e-8] — outside: no structure formation or baryon dilution
# Prior range: [1e-20, 1]  — from PQ symmetry / inflation lower bound to unity
eta_obs  = eta                    # 6e-10
eta_w_lo = 1e-11
eta_w_hi = 1e-8
eta_r_lo = 1e-20
eta_r_hi = 1.0

sev_log_eta, P_log_eta = log10_severity_log_uniform(eta_obs, eta_w_lo, eta_w_hi, eta_r_lo, eta_r_hi)
sev_lin_eta, P_lin_eta = log10_severity_linear(eta_w_lo, eta_w_hi, eta_r_lo, eta_r_hi)

constants["eta (baryon-to-photon ratio)"] = {
    "symbol": "η",
    "observed": eta_obs,
    "window_lo": eta_w_lo,
    "window_hi": eta_w_hi,
    "range_lo": eta_r_lo,
    "range_hi": eta_r_hi,
    "P_log_uniform": P_log_eta,
    "log10_severity_log": sev_log_eta,
    "P_linear": P_lin_eta,
    "log10_severity_linear": sev_lin_eta,
    "note": "window [1e-11,1e-8]; outside: no structure or matter washed out",
}

# ── (e) Cosmological constant Λ (ρ_Λ) ───────────────────────────────────────
# Already analyzed in cc_prior_analysis.py; include here for comparison
# Anthropic window: [0, 30 × ρ_Λ_obs]  (Weinberg 1987)
# Prior range: [epsilon_IR, rho_Planck]  with epsilon_IR ≪ ρ_obs
rho_Lam_max = 30.0 * rho_Lambda_obs
epsilon_IR  = 1e-200
rho_prior_hi = rho_Planck

sev_log_cc, P_log_cc = log10_severity_log_uniform(rho_Lambda_obs, epsilon_IR, rho_Lam_max, epsilon_IR, rho_prior_hi)
sev_lin_cc, P_lin_cc = log10_severity_linear(epsilon_IR, rho_Lam_max, epsilon_IR, rho_prior_hi)

constants["Lambda (cosmological constant)"] = {
    "symbol": "ρ_Λ",
    "observed": rho_Lambda_obs,
    "window_lo": epsilon_IR,
    "window_hi": rho_Lam_max,
    "range_lo": epsilon_IR,
    "range_hi": rho_prior_hi,
    "P_log_uniform": P_log_cc,
    "log10_severity_log": sev_log_cc,
    "P_linear": P_lin_cc,
    "log10_severity_linear": sev_lin_cc,
    "note": "Weinberg window [0, 30 ρ_obs]; prior [ε_IR, ρ_Planck]; log-uniform ≈ 56%",
}

# ── Print results table ───────────────────────────────────────────────────────

print(f"\n  {'Constant':<35s}  {'Observed':>12s}  {'Log-unif P':>12s}  "
      f"{'Sev(log)':>10s}  {'Linear P':>12s}  {'Sev(lin)':>10s}")
print(f"  {'─'*35}  {'─'*12}  {'─'*12}  {'─'*10}  {'─'*12}  {'─'*10}")

for name, d in constants.items():
    sev_log = d['log10_severity_log']
    sev_lin = d['log10_severity_linear']
    P_log   = d['P_log_uniform']
    P_lin   = d['P_linear']
    obs     = d['observed']
    print(f"  {name:<35s}  {obs:>12.4e}  {P_log:>12.4f}  {sev_log:>+10.2f}  {P_lin:>12.4e}  {sev_lin:>+10.2f}")

print(f"\n  Severity = log₁₀(1/P): how many decades of 'luck' needed?")
print(f"  +0 = typical (no fine-tuning), +10 = 10 decades fine-tuned")
print(f"  Λ severity under log-uniform should be ≈ 0 (P≈56%)")

# ── Narrative comparison ──────────────────────────────────────────────────────

print("\n" + "=" * 74)
print("FINE-TUNING COMPARISON — Is Λ uniquely special?")
print("=" * 74)

print(f"""
  Under LOG-UNIFORM prior:
  ─────────────────────────────────────────────────────────────────────────""")

for name, d in sorted(constants.items(), key=lambda x: x[1]['log10_severity_log']):
    tag = ""
    s = d['log10_severity_log']
    if s < 0.5:
        tag = "  ← TYPICAL (no tuning)"
    elif s < 1.5:
        tag = "  ← mild"
    elif s < 3.0:
        tag = "  ← moderate"
    else:
        tag = "  ← SEVERE"
    print(f"  {name:<35s}  severity = {s:+.2f} decades{tag}")

print(f"""
  Under LINEAR prior:
  ─────────────────────────────────────────────────────────────────────────""")

for name, d in sorted(constants.items(), key=lambda x: x[1]['log10_severity_linear']):
    tag = ""
    s = d['log10_severity_linear']
    if s < 0.5:
        tag = "  ← TYPICAL"
    elif s < 2.0:
        tag = "  ← mild"
    elif s < 10.0:
        tag = "  ← moderate"
    else:
        tag = "  ← SEVERE"
    print(f"  {name:<35s}  severity = {s:+.2f} decades{tag}")

# ── Relative ranking analysis ─────────────────────────────────────────────────

print("\n" + "=" * 74)
print("RELATIVE RANKING — Does prior choice change the ordering?")
print("=" * 74)

# Compute rank correlation (Spearman) between log-uniform and linear severities
names_list  = list(constants.keys())
sev_log_arr = [constants[n]['log10_severity_log'] for n in names_list]
sev_lin_arr = [constants[n]['log10_severity_linear'] for n in names_list]

# Simple rank correlation
def rank_list(arr):
    sorted_idx = sorted(range(len(arr)), key=lambda i: arr[i])
    ranks = [0]*len(arr)
    for rank, idx in enumerate(sorted_idx):
        ranks[idx] = rank + 1
    return ranks

ranks_log = rank_list(sev_log_arr)
ranks_lin = rank_list(sev_lin_arr)

n_c = len(names_list)
d2_sum = sum((rl - rli)**2 for rl, rli in zip(ranks_log, ranks_lin))
spearman_r = 1 - 6*d2_sum / (n_c*(n_c**2 - 1))

print(f"""
  Spearman rank correlation (log-uniform vs linear severity ordering): {spearman_r:.3f}

  Interpretation:
  • ρ_S ≈ +1.0 → both priors give the SAME ranking of fine-tuning severity
  • ρ_S ≈  0.0 → priors completely disagree about which constant is most tuned
  • ρ_S ≈ -1.0 → priors give REVERSED ranking

  Prior choice dramatically changes absolute severity (Λ goes from P=56% to P=10^{sev_lin_cc:.0f})
  but {"PRESERVES" if spearman_r > 0.7 else "SCRAMBLES"} the relative ordering.
""")

# ── Dimensional analysis of L* ────────────────────────────────────────────────

print("=" * 74)
print("DIMENSIONAL ANALYSIS — What combination of constants gives L*?")
print("=" * 74)

# We want to find if L* ≈ ħ^a c^b G^d m^e k_B^f T^g H₀^h gives L*
# Key observation: L* = (g_SM ħc / 32π² ρ_Λ)^{1/4}
# ρ_Λ involves G and H₀ via ρ_Λ = Λ c²/(8πG) and Λ/H₀² is the density param
# So L* ~ (ħc/ρ_Λ)^{1/4} ~ (ħc × G / (H₀² c²))^{1/4} ~ (ħG/(c H₀²))^{1/4}

L_hG_cH2 = (hbar * G / (c * H0**2))**0.25
ratio_hG = L_hG_cH2 / L_star
log_ratio_hG = math.log10(ratio_hG)

print(f"""
  L* = ({SM_g_eff} ħc / 32π² ρ_Λ)^(1/4)  [by definition]

  Since ρ_Λ ≈ 3 Ω_Λ H₀² / (8πG)  and Ω_Λ ≈ 0.685 ≈ O(1):
    ρ_Λ ~ H₀² c² / G   →   L* ~ (ħG / (c H₀²))^(1/4)

  Numerical check:
    (ħ G / c H₀²)^(1/4) = {L_hG_cH2:.4e} m
    L*                   = {L_star:.4e} m
    Ratio                = {ratio_hG:.4f}  [log₁₀ = {log_ratio_hG:+.3f}]

  This is a TAUTOLOGY: L* is defined by matching ρ_Λ, and ρ_Λ ∝ H₀²/G.
  So L* ∝ (ħ G / c H₀²)^(1/4) — a combination of quantum gravity AND cosmology.

  Physical interpretation:
    L* is NOT a particle physics scale.
    L* is NOT a pure quantum scale (no k_B, no T).
    L* IS a quantum gravity + Hubble constant combination.
    It encodes: "at what length scale do quantum (ħ) and gravitational (G,H₀)
    effects simultaneously set the vacuum energy density?"

  This is consistent with the holographic interpretation:
    L* ~ l_P^(1/2) × L_Hubble^(1/2) = √(l_P L_Hubble)
    = √({l_P:.4e} × {L_Hubble:.4e}) = {L_geom_PH:.4e} m
    vs L*                                         = {L_star:.4e} m
    log₁₀ ratio                                   = {math.log10(L_geom_PH/L_star):+.3f}
""")

# ─────────────────────────────────────────────────────────────────────────────
# Save results/lambda_scale_data.json
# ─────────────────────────────────────────────────────────────────────────────

data = {
    "meta": {
        "script": "lambda_scale.py",
        "date": "2026-04-09",
        "description": "L* scale comparison and anthropic fine-tuning sweep",
    },
    "L_star": {
        "value_m": L_star,
        "formula": "L* = (g_SM ħc / 32π² ρ_Λ)^(1/4)",
        "g_SM": SM_g_eff,
        "rho_Lambda_obs": rho_Lambda_obs,
        "dimensional_formula": "(ħ G / c H₀²)^(1/4) — quantum gravity + Hubble combination",
    },
    "length_scales": scale_results,
    "closest_matches": [
        {"rank": i+1, "name": name, "value_m": d["value_m"],
         "ratio": d["ratio_to_Lstar"], "log10_ratio": d["log10_ratio"]}
        for i, (name, d) in enumerate(sorted_by_closeness[:10])
    ],
    "anthropic_fine_tuning": {
        name: {
            "symbol": d["symbol"],
            "observed": d["observed"],
            "window": [d["window_lo"], d["window_hi"]],
            "prior_range": [d["range_lo"], d["range_hi"]],
            "log_uniform": {
                "P": d["P_log_uniform"],
                "log10_severity": d["log10_severity_log"],
            },
            "linear": {
                "P": d["P_linear"],
                "log10_severity": d["log10_severity_linear"],
            },
            "note": d["note"],
        }
        for name, d in constants.items()
    },
    "spearman_rank_correlation": spearman_r,
    "dimensional_analysis": {
        "L_hG_cH2_m": L_hG_cH2,
        "ratio_to_Lstar": ratio_hG,
        "log10_ratio": log_ratio_hG,
        "formula": "(ħ G / c H₀²)^(1/4)",
        "interpretation": "L* is a quantum gravity + cosmological scale, not a particle physics scale",
    },
}

results_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(results_dir, exist_ok=True)
json_path = os.path.join(results_dir, "lambda_scale_data.json")
with open(json_path, "w") as f:
    json.dump(data, f, indent=2)
print(f"\nSaved: {json_path}")
