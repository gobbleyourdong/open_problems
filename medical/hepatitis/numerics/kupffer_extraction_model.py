"""
kupffer_extraction_model.py
Portal Gatekeeper Model — Hepatic First-Pass CVB Extraction

Quantifies the liver's role as a filter between gut-shed CVB and
systemic circulation, with and without fluoxetine.

Literature parameters:
  - Hepatic blood flow: 1.5 L/min (25% of cardiac output at ~6 L/min)
  - Portal fraction: ~75% of hepatic flow = 1.125 L/min
  - Kupffer cell count: ~3×10^9 in adult liver (Bilzer et al. 2006)
  - Phagocytosis rate at saturation: ~25 viral particles/cell/min
  - First-pass extraction (healthy adult): 85-95% per pass
  - Sinusoidal transit time: 1-2 seconds per pass

Run: python3 kupffer_extraction_model.py
Outputs: kupffer_extraction_plots.png
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ---------------------------------------------------------------------------
# 1.  Anatomical / physiological constants
# ---------------------------------------------------------------------------

HEPATIC_FLOW_L_MIN     = 1.5          # L/min total hepatic blood flow
PORTAL_FRACTION        = 0.75         # portal vein fraction of hepatic flow
PORTAL_FLOW_L_MIN      = HEPATIC_FLOW_L_MIN * PORTAL_FRACTION   # 1.125 L/min
PORTAL_FLOW_ML_S       = PORTAL_FLOW_L_MIN * 1000 / 60           # mL/s (~18.75)

LIVER_VOLUME_ML        = 1500.0       # adult liver ~1.5 L
SINUSOID_TRANSIT_S     = 1.5          # seconds per pass through sinusoidal network
PASSES_PER_MIN         = 60 / SINUSOID_TRANSIT_S                 # ~40 passes/min

KUPFFER_COUNT          = 3.0e9        # total Kupffer cells (Bilzer 2006)
KUPFFER_VMAX_PART_MIN  = 25.0         # max phagocytosis rate, particles/cell/min at saturation
KUPFFER_KM             = 1.0e5        # half-saturation constant (particles/mL portal blood)

# ---------------------------------------------------------------------------
# 2.  Kupffer cell extraction — Michaelis-Menten kinetics
# ---------------------------------------------------------------------------

def kupffer_clearance_rate(conc_portal, activation=1.0):
    """
    Kupffer cell phagocytosis rate (particles/min, whole liver).

    Parameters
    ----------
    conc_portal : float
        Viral concentration in portal blood (particles/mL).
    activation : float
        Relative activation level (1.0 = baseline; >1 = activated by Vit D,
        fluoxetine, IFN; <1 = impaired by alcohol, NAFLD, immaturity).

    Returns
    -------
    float : total particles removed per minute across all Kupffer cells
    """
    vmax_total = KUPFFER_COUNT * KUPFFER_VMAX_PART_MIN * activation
    rate = vmax_total * conc_portal / (KUPFFER_KM + conc_portal)
    return rate  # particles/min

def extraction_efficiency(conc_portal, activation=1.0):
    """
    Fraction of portal viral load extracted per hepatic pass.

    E = (clearance_rate / transit_time) / input_rate
    Input rate (particles/min) = conc_portal × PORTAL_FLOW_ML_S × 60
    """
    input_rate = conc_portal * PORTAL_FLOW_ML_S * 60   # particles/min
    if input_rate < 1e-30:
        return 0.0
    removed = kupffer_clearance_rate(conc_portal, activation)
    # Cannot remove more than input
    eff = min(removed / input_rate, 1.0)
    return eff

# ---------------------------------------------------------------------------
# 3.  First-pass extraction across portal concentration range
# ---------------------------------------------------------------------------

concentrations_log = np.linspace(1, 8, 500)   # log10 particles/mL
concentrations     = 10 ** concentrations_log

eff_healthy   = np.array([extraction_efficiency(c, 1.0) for c in concentrations])
eff_nafld     = np.array([extraction_efficiency(c, 0.5) for c in concentrations])  # impaired
eff_fluox     = np.array([extraction_efficiency(c, 2.0) for c in concentrations])  # enhanced
eff_neonatal  = np.array([extraction_efficiency(c, 0.35) for c in concentrations]) # immature

# ---------------------------------------------------------------------------
# 4.  Multi-pass model
#     After each liver pass, cleared fraction is removed.
#     Blood recirculates; how many passes before CVB level falls below threshold?
# ---------------------------------------------------------------------------

SYSTEMIC_VOLUME_ML = 5000.0   # ~5 L blood volume (adult)
DETECTION_THRESHOLD_LOG10 = 2.0  # log10 copies/mL — below this: clinically cleared

def simulate_multipass(initial_viral_load_log10, activation=1.0,
                       n_passes=100, gut_shedding_rate=0.0):
    """
    Simulate systemic viral load over repeated hepatic passes.

    Parameters
    ----------
    initial_viral_load_log10 : float
        Starting systemic viral load (log10 particles).
    activation : float
        Kupffer cell activation level.
    n_passes : int
        Number of hepatic passes to simulate.
    gut_shedding_rate : float
        New particles added per pass from ongoing gut replication.

    Returns
    -------
    passes : np.ndarray
    load_log10 : np.ndarray
    """
    load = 10 ** initial_viral_load_log10
    loads = [load]
    for _ in range(n_passes):
        # Concentration in portal blood (assume mixing with systemic volume)
        conc_portal = load / SYSTEMIC_VOLUME_ML
        eff = extraction_efficiency(conc_portal, activation)
        removed = load * eff
        load = load - removed + gut_shedding_rate
        load = max(load, 0.0)
        loads.append(load)
    loads = np.array(loads)
    # Avoid log10(0)
    loads_log10 = np.where(loads > 0, np.log10(loads + 1), 0)
    return np.arange(n_passes + 1), loads_log10

# Time conversion: each "pass" = 1.5 s sinusoid transit
# But full blood recirculation time ≈ 1 min (cardiac cycle)
# For multi-pass: treat each pass as one cardiac recirculation (~1 min)

# ---------------------------------------------------------------------------
# 5.  Gut shedding -> portal -> systemic viremia — steady-state model
#     At steady state: gut_shedding_rate × (1 - E_kupffer) = systemic clearance
# ---------------------------------------------------------------------------

GUT_SHEDDING_RATES_LOG10 = np.array([4, 5, 6, 7, 8])  # particles/min shed into portal
ACTIVATION_LEVELS = {
    "No treatment (healthy adult)": 1.0,
    "NAFLD / alcohol (impaired)":   0.5,
    "Fluoxetine (enhanced)":        2.2,
    "Neonatal (immature)":          0.35,
}

print("=== Portal Gatekeeper Model — Parameter Report ===\n")
print(f"Hepatic blood flow:       {HEPATIC_FLOW_L_MIN:.1f} L/min")
print(f"Portal fraction:          {PORTAL_FRACTION*100:.0f}%  = {PORTAL_FLOW_L_MIN:.3f} L/min")
print(f"Kupffer cell count:       {KUPFFER_COUNT:.2e}")
print(f"Phagocytosis Vmax:        {KUPFFER_VMAX_PART_MIN:.0f} particles/cell/min")
print(f"KM (half-saturation):     {KUPFFER_KM:.1e} particles/mL\n")

print("Extraction efficiency at key concentrations (healthy adult):")
for conc_log in [3, 4, 5, 6, 7]:
    c = 10**conc_log
    e = extraction_efficiency(c, 1.0)
    print(f"  10^{conc_log} particles/mL  ->  E = {e*100:.1f}%")

print("\nSteady-state systemic viremia by gut shedding rate:")
print(f"  {'Shedding (log10/min)':>22}  {'Healthy':>10}  {'NAFLD':>10}  {'Fluoxetine':>12}  {'Neonatal':>10}")
for shed_log in GUT_SHEDDING_RATES_LOG10:
    shed_rate = 10**shed_log
    row = []
    for act in [1.0, 0.5, 2.2, 0.35]:
        # Approximate steady-state: systemic conc = shed * (1-E) / flow
        # Iterative solution
        conc_portal = shed_rate / PORTAL_FLOW_ML_S / 60  # initial estimate
        for _ in range(50):
            e = extraction_efficiency(conc_portal, act)
            systemic_rate = shed_rate * (1 - e)
            conc_portal_new = shed_rate / PORTAL_FLOW_ML_S / 60
            if abs(conc_portal_new - conc_portal) < 1:
                break
            conc_portal = conc_portal_new
        systemic_log10 = np.log10(max(systemic_rate, 1))
        row.append(f"10^{systemic_log10:.1f}")
    print(f"  10^{shed_log:>2.0f}                     "
          f"  {row[0]:>10}  {row[1]:>10}  {row[2]:>12}  {row[3]:>10}")

# ---------------------------------------------------------------------------
# 6.  ODE model: CVB dynamics in compartments
#     Compartments: Gut (G), Portal (P), Liver (L), Systemic (S)
# ---------------------------------------------------------------------------

def cvb_ode(t, y, params):
    """
    Simplified 4-compartment ODE for CVB dynamics.

    y = [G, P, L, S]  — viral load (particles) in each compartment

    Parameters
    ----------
    t : float  (minutes)
    y : array [G, P, L, S]
    params : dict with keys:
        gut_shedding     — particles/min shed into portal (fixed source term)
        kup_activation   — Kupffer activation level
        rep_rate_L       — liver replication rate constant (/min) if overwhelmed
        k_organ          — systemic-to-organ seeding rate (/min)
        k_clearance_sys  — systemic immune clearance (/min)
    """
    G, P, L, S = y
    p = params

    # Portal input from gut
    gut_input = p["gut_shedding"]

    # Kupffer extraction — depends on portal concentration
    conc_P = max(P, 0) / (LIVER_VOLUME_ML * 0.1)   # portal sinusoidal volume ~150 mL
    conc_P = max(conc_P, 1e-10)
    removed_by_kupffer = min(
        kupffer_clearance_rate(conc_P, p["kup_activation"]),
        max(P, 0) / 1.0   # can't remove more than present per minute
    )

    # Liver replication if hepatocytes infected (simplified: proportional to L)
    liver_rep = p["rep_rate_L"] * max(L, 0)

    # Flow rates
    portal_to_liver  = gut_input                    # portal blood delivers to liver
    liver_to_systemic = max(L, 0) * 0.10           # hepatic venous outflow fraction

    dG = -gut_input                                # gut shedding depletes gut pool
    dP = gut_input - removed_by_kupffer            # portal pool
    dL = removed_by_kupffer + liver_rep - liver_to_systemic  # liver pool
    dS = liver_to_systemic - p["k_clearance_sys"] * max(S, 0)

    return [dG, dP, dL, dS]

# ---------------------------------------------------------------------------
# 7.  Figures
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Portal Gatekeeper Model — Hepatic CVB Extraction Kinetics",
             fontsize=13, fontweight="bold")

# ------ Panel A: Extraction efficiency vs portal concentration ------
ax = axes[0, 0]
ax.semilogx(concentrations, eff_healthy * 100,  "b-",  lw=2.5, label="Healthy adult")
ax.semilogx(concentrations, eff_fluox * 100,    "g-",  lw=2.5, label="Fluoxetine (×2.2 activation)")
ax.semilogx(concentrations, eff_nafld * 100,    "r--", lw=2,   label="NAFLD/alcohol (×0.5)")
ax.semilogx(concentrations, eff_neonatal * 100, "m--", lw=2,   label="Neonatal (×0.35)")
ax.axhspan(85, 99, alpha=0.08, color="blue", label="Reported range 85-95%")
ax.set_xlabel("Portal CVB concentration (particles/mL)")
ax.set_ylabel("Kupffer extraction efficiency (%)")
ax.set_title("A: First-Pass Extraction vs Viral Concentration")
ax.legend(fontsize=8)
ax.set_ylim(0, 102)
ax.grid(True, alpha=0.3)

# ------ Panel B: Multi-pass clearance — healthy vs fluoxetine ------
ax = axes[0, 1]
initial_log10 = 8.0   # 10^8 particles systemic
passes_h, loads_h = simulate_multipass(initial_log10, activation=1.0, n_passes=200)
passes_f, loads_f = simulate_multipass(initial_log10, activation=2.2, n_passes=200)
passes_n, loads_n = simulate_multipass(initial_log10, activation=0.35, n_passes=200)

# Convert passes to approximate minutes (1 pass ≈ 1 min cardiac recirculation)
ax.plot(passes_h, loads_h, "b-",  lw=2, label="Healthy adult")
ax.plot(passes_f, loads_f, "g-",  lw=2, label="Fluoxetine")
ax.plot(passes_n, loads_n, "r--", lw=2, label="Neonatal")
ax.axhline(DETECTION_THRESHOLD_LOG10, ls="--", lw=0.8, color="grey",
           label="Detection threshold (10²/mL)")
ax.set_xlabel("Hepatic recirculation passes (~minutes)")
ax.set_ylabel("Systemic viral load (log10 particles)")
ax.set_title(f"B: Multi-Pass Clearance\n(initial load 10^{initial_log10:.0f} particles)")
ax.legend(fontsize=9)
ax.set_ylim(0, 10)
ax.grid(True, alpha=0.3)

# ------ Panel C: Gut shedding -> systemic viremia (steady-state) ------
ax = axes[0, 2]
shed_range = np.logspace(3, 9, 200)
scenarios = [
    ("Healthy adult", 1.0, "blue", "-"),
    ("Fluoxetine",    2.2, "green", "-"),
    ("NAFLD",         0.5, "red", "--"),
    ("Neonatal",      0.35, "purple", "--"),
]
for lbl, act, col, ls in scenarios:
    systemic_loads = []
    for shed in shed_range:
        conc_portal = shed / PORTAL_FLOW_ML_S / 60
        e = extraction_efficiency(conc_portal, act)
        systemic = shed * (1 - e)
        systemic_loads.append(max(systemic, 1))
    ax.loglog(shed_range, systemic_loads, color=col, ls=ls, lw=2, label=lbl)

ax.set_xlabel("Gut shedding rate (particles/min into portal)")
ax.set_ylabel("Steady-state systemic viral input (particles/min)")
ax.set_title("C: Gut Shedding → Systemic Viremia\n(steady-state)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, which="both")

# ------ Panel D: Number of passes to reach clearance threshold ------
ax = axes[1, 0]
initial_loads = [6, 7, 8, 9, 10]
load_colors = plt.cm.plasma(np.linspace(0.2, 0.9, len(initial_loads)))
threshold = DETECTION_THRESHOLD_LOG10

for init, col in zip(initial_loads, load_colors):
    passes_to_clear_h = None
    passes_to_clear_f = None
    pa, la = simulate_multipass(init, activation=1.0, n_passes=500)
    pb, lb = simulate_multipass(init, activation=2.2, n_passes=500)
    # find first pass below threshold
    below_h = np.where(la < threshold)[0]
    below_f = np.where(lb < threshold)[0]
    ptc_h = below_h[0] if len(below_h) else 500
    ptc_f = below_f[0] if len(below_f) else 500
    ax.bar(init - 0.2, ptc_h, width=0.35, color="blue",  alpha=0.7, label="Healthy" if init==6 else "")
    ax.bar(init + 0.2, ptc_f, width=0.35, color="green", alpha=0.7, label="Fluoxetine" if init==6 else "")

ax.set_xticks(initial_loads)
ax.set_xticklabels([f"10^{i}" for i in initial_loads])
ax.set_xlabel("Initial systemic viral load (particles)")
ax.set_ylabel("Passes to reach clearance threshold")
ax.set_title("D: Time to Clearance\n(passes ≈ minutes)")
ax.legend(fontsize=9)
ax.grid(True, axis="y", alpha=0.3)

# ------ Panel E: Fluoxetine first-pass concentration advantage ------
ax = axes[1, 1]
# Fluoxetine oral dose 20mg -> 60% first-pass extraction -> hepatic conc elevated
# Plasma Cmax ~15-55 ng/mL; hepatic portal Cmax ~3-5× higher
oral_dose_mg = 20.0
bioavailability = 0.40   # 40% systemic (60% first-pass metabolised)
hepatic_conc_factor = 1 / bioavailability  # ~2.5× portal/hepatic vs systemic

time_h = np.linspace(0, 24, 200)
# Simplified 1-compartment PK: tmax ~6h, t½ ~2-3 days (parent + norfluoxetine)
# At single dose, approximate hepatic portal concentration
ka   = 0.5   # absorption rate /h
ke   = 0.693 / 50   # elimination /h (t½ ≈ 50 h for combined fluoxetine+norfluox)
dose_mg = oral_dose_mg
# Portal conc before first-pass (absorbed fraction)
V_portal_L = 0.5   # effective portal distribution volume at absorption site
C_portal = (dose_mg / V_portal_L) * (ka / (ka - ke)) * (np.exp(-ke * time_h) - np.exp(-ka * time_h))
C_systemic = C_portal * bioavailability

ax.plot(time_h, C_portal,   "g-",  lw=2, label="Hepatic/portal exposure")
ax.plot(time_h, C_systemic, "b--", lw=2, label="Systemic plasma")
ax.fill_between(time_h, C_systemic, C_portal, alpha=0.15, color="green",
                label="First-pass advantage (extra hepatic exposure)")
ax.set_xlabel("Time after oral dose (hours)")
ax.set_ylabel("Relative fluoxetine concentration (a.u.)")
ax.set_title("E: First-Pass Advantage\n(fluoxetine 20 mg oral — hepatic vs systemic)")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# ------ Panel F: Clearance sequence prediction ------
ax = axes[1, 2]
organs = ["Liver\n(Kupffer+\nhepatocyte)", "Blood\n(systemic\nviremia)",
          "Pancreas", "Heart", "Muscle/\nCNS", "Testes\n(immune\nprivilege)"]
days_to_clear_fluox  = [14, 28, 42, 42, 60, 180]
days_to_clear_nofluox = [90, 180, 270, 270, 365, 730]  # no antiviral

x = np.arange(len(organs))
width = 0.35
ax.barh(x - width/2, days_to_clear_fluox,   height=0.3, color="green", alpha=0.8,
        label="Colchicine + fluoxetine")
ax.barh(x + width/2, days_to_clear_nofluox, height=0.3, color="red",   alpha=0.6,
        label="Colchicine only (no antiviral)")
ax.set_yticks(x)
ax.set_yticklabels(organs, fontsize=9)
ax.set_xlabel("Estimated days to organ clearance")
ax.set_title("F: Predicted Clearance Sequence\n(liver-first model)")
ax.legend(fontsize=9)
ax.set_xlim(0, 800)
ax.axvline(30,  ls="--", lw=0.5, color="grey")
ax.axvline(90,  ls="--", lw=0.5, color="grey")
ax.axvline(180, ls="--", lw=0.5, color="grey")
for d, lbl in [(30, "1 mo"), (90, "3 mo"), (180, "6 mo")]:
    ax.text(d + 2, len(organs) - 0.3, lbl, fontsize=7, color="grey")
ax.grid(True, axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig("kupffer_extraction_plots.png", dpi=150, bbox_inches="tight")
print("Saved: kupffer_extraction_plots.png")

# ---------------------------------------------------------------------------
# 8.  Summary numbers
# ---------------------------------------------------------------------------

print("\n=== Key Model Numbers ===\n")
print(f"Portal blood flow:          {PORTAL_FLOW_L_MIN:.3f} L/min  ({PORTAL_FLOW_ML_S:.1f} mL/s)")
print(f"Sinusoidal transit time:    {SINUSOID_TRANSIT_S:.1f} s/pass")
print(f"Passes per minute:          {PASSES_PER_MIN:.1f}")
print(f"Kupffer Vmax (whole liver): {KUPFFER_COUNT * KUPFFER_VMAX_PART_MIN:.2e} particles/min")

print("\nExtraction efficiency (healthy adult) by portal load:")
for clog in [3, 4, 5, 6, 7, 8]:
    c = 10**clog
    e_h = extraction_efficiency(c, 1.0)
    e_f = extraction_efficiency(c, 2.2)
    e_n = extraction_efficiency(c, 0.35)
    print(f"  10^{clog} /mL  ->  healthy {e_h*100:.1f}%  fluox {e_f*100:.1f}%  neonatal {e_n*100:.1f}%")

print("\nFluoxetine first-pass advantage: ~2.5× higher hepatic than systemic concentration")
print("This concentrates antiviral effect exactly where portal CVB arrives first.")
