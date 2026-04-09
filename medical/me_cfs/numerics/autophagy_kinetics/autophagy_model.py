"""
REQ-006: Autophagy Kinetics Model — ME/CFS TD Mutant Clearance During Fasting
==============================================================================
Models autophagy flux during fasting and its quantitative impact on CVB TD
mutant clearance in ME/CFS patients.

References:
  - Alirezaei et al. 2010 (J Neurosci): Autophagy in brain during fasting
  - Mizushima & Klionsky 2007: LC3-II/I ratio as autophagy flux measure
  - Takahashi et al. 2018: FMD-induced autophagy kinetics
  - Longo & Mattson 2014: Intermittent fasting and cellular autophagy

Author: ODD instance (REQ-006)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import os

# Output directory
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ────────────────────────────────────────────────────────────────
# SECTION 1: AUTOPHAGY ACTIVATION KINETICS
# ────────────────────────────────────────────────────────────────

def ampk_activation(t, t_half=3.0):
    """
    AMPK activation kinetics after fasting onset.
    Modeled as first-order approach to 1.0 (full activation).
    t_half ~ 2-4h (midpoint 3h), Hardie et al. 2012.
    """
    k = np.log(2) / t_half
    return 1.0 - np.exp(-k * t)


def ulk1_phosphorylation(ampk_level, delay_h=1.5, current_t=0.0, fast_onset=0.0):
    """
    ULK1 phosphorylation follows AMPK with ~1.5h additional delay.
    ULK1 then initiates autophagosome biogenesis.
    """
    t_eff = max(0.0, current_t - fast_onset - delay_h)
    if t_eff <= 0:
        return 0.0
    k = np.log(2) / 2.0   # additional t½ ~2h for ULK1 step
    return ampk_level * (1.0 - np.exp(-k * t_eff))


def lc3_ratio(t, baseline=0.5, peak=4.0, peak_time=18.0, rise_t_half=6.0, decay_t_half=48.0):
    """
    LC3-II/I ratio during a continuous fast.
    - Baseline LC3-II/I ~ 0.5 (well-fed state)
    - Peak ~ 3-5× baseline at ~12-24h (mid 4.0 × 0.5 = 2.0 absolute, or ratio ~4.0)
    - Sustained during prolonged fast (slow decay after peak)
    From Alirezaei 2010: peak at ~24h in brain; similar kinetics in muscle/liver.
    """
    # Logistic rise to peak
    k_rise = np.log(2) / rise_t_half
    rise = 1.0 - np.exp(-k_rise * t)
    # Gaussian-like envelope peaking at peak_time
    envelope = np.exp(-0.5 * ((t - peak_time) / decay_t_half) ** 2)
    # Final ratio: baseline + added flux
    added = (peak - baseline) * rise * (envelope + 0.2 * (1 - envelope))
    return baseline + added


def mtor_suppression(t, onset=5.0, maximal_time=15.0, t_half_suppression=3.0):
    """
    mTOR activity (1.0 = normal fed state, 0.0 = fully suppressed).
    Suppression begins at ~4-6h, maximal at ~12-18h.
    mTOR suppression relieves its inhibition of ULK1, enabling autophagy.
    """
    if t < onset:
        return 1.0
    t_eff = t - onset
    k = np.log(2) / t_half_suppression
    min_activity = 0.15    # never fully zero; TORC1-independent baseline
    suppression = (1.0 - min_activity) * (1.0 - np.exp(-k * t_eff))
    return 1.0 - suppression


# ────────────────────────────────────────────────────────────────
# SECTION 2: TD MUTANT CLEARANCE DURING AUTOPHAGY
# ────────────────────────────────────────────────────────────────

# Baseline TD mutant half-life in tissue (days) — long because TD mutants
# replicate very slowly but evade immune surveillance.
TD_HALFLIFE_BASELINE_DAYS = 350.0
K_CLEAR_BASELINE = np.log(2) / TD_HALFLIFE_BASELINE_DAYS   # per-day clearance

# During peak autophagy (LC3-II/I ratio ~4), selective autophagy (virophagy)
# via SQSTM1 (p62) / NBR1 receptors captures viral RNA-protein complexes.
# Rate enhancement ~ 5× at peak (conservative from literature).
AUTOPHAGY_ENHANCEMENT_MAX = 5.0

# Autophagy receptor saturation constant (in LC3-II/I ratio units)
# Half-maximal receptor occupancy at LC3-II/I ~ 2.0
K_HALF_LC3 = 2.0


def autophagy_clearance_rate(lc3_ratio_val, baseline_k=K_CLEAR_BASELINE,
                              enhancement_max=AUTOPHAGY_ENHANCEMENT_MAX,
                              k_half=K_HALF_LC3):
    """
    Effective first-order clearance rate for TD mutants as a function of
    current LC3-II/I ratio. Michaelis-Menten-like saturation.

    Returns k_eff in units of day⁻¹.
    """
    # Fold-enhancement above baseline (Michaelis-Menten saturating)
    fold = 1.0 + (enhancement_max - 1.0) * lc3_ratio_val / (lc3_ratio_val + k_half)
    return baseline_k * fold


# ────────────────────────────────────────────────────────────────
# SECTION 3: PROTOCOL DEFINITIONS
# ────────────────────────────────────────────────────────────────

def get_lc3_at_time(t_day, protocol):
    """
    Return the LC3-II/I ratio at time t_day (days) given a fasting protocol.

    Protocols supported:
      - 'monthly_fmd'  : 5-day FMD once per month
      - 'weekly_24h'   : 24-hour fast every 7 days
      - 'daily_16_8'   : Daily 16:8 TRE
      - 'none'         : No fasting (baseline)
    """
    t_hour = t_day * 24.0   # convert to hours for kinetics

    if protocol == 'none':
        return 0.5   # baseline LC3-II/I

    elif protocol == 'daily_16_8':
        # TRE: 16h fast / 8h feeding window, repeating
        t_within_cycle = t_hour % 24.0
        # Fasting period is hours 0-16, re-feeding 16-24
        if t_within_cycle <= 16.0:
            # Minor AMPK activation, mild autophagy
            # LC3-II/I peaks at ~1.5 (not the 3-5× of prolonged fast)
            lc3_val = lc3_ratio(t_within_cycle, baseline=0.5, peak=1.8,
                                 peak_time=14.0, rise_t_half=5.0, decay_t_half=20.0)
            return lc3_val
        else:
            # Re-feeding suppresses autophagy quickly
            t_refeed = t_within_cycle - 16.0
            lc3_val = 0.5 + 1.3 * np.exp(-0.8 * t_refeed)
            return max(0.5, lc3_val)

    elif protocol == 'weekly_24h':
        # 24h fast every 7 days
        t_within_week = t_hour % (7 * 24.0)
        # Fast occupies the first 24h of the 7-day cycle
        if t_within_week <= 24.0:
            lc3_val = lc3_ratio(t_within_week, baseline=0.5, peak=4.0,
                                 peak_time=18.0, rise_t_half=6.0, decay_t_half=40.0)
            return lc3_val
        else:
            # Recovery: autophagy decays over 12-24h after re-feeding
            t_recovery = t_within_week - 24.0
            lc3_val = 0.5 + 3.5 * np.exp(-0.12 * t_recovery)
            return max(0.5, lc3_val)

    elif protocol == 'monthly_fmd':
        # 5-day FMD once per 30 days (Longo ProLon-style: ~500-800 kcal/day)
        # Provides ~3-4 days at peak autophagy
        t_within_month = t_hour % (30 * 24.0)
        fmd_duration_h = 5 * 24.0   # 120 hours
        if t_within_month <= fmd_duration_h:
            lc3_val = lc3_ratio(t_within_month, baseline=0.5, peak=4.5,
                                 peak_time=36.0, rise_t_half=8.0, decay_t_half=60.0)
            return lc3_val
        else:
            t_recovery = t_within_month - fmd_duration_h
            lc3_val = 0.5 + 4.0 * np.exp(-0.08 * t_recovery)
            return max(0.5, lc3_val)

    return 0.5   # fallback


# ────────────────────────────────────────────────────────────────
# SECTION 4: TD MUTANT LOAD SIMULATION (ODE)
# ────────────────────────────────────────────────────────────────

def simulate_td_clearance(protocol, t_span_days=(0, 365), initial_load=1.0, n_points=8760):
    """
    Simulate TD mutant load over time under a given fasting protocol.

    dV/dt = -k_eff(LC3) * V

    V is normalized: 1.0 = baseline load at t=0.

    Returns (t_days, V_load)
    """
    t_eval = np.linspace(t_span_days[0], t_span_days[1], n_points)

    def rhs(t, y):
        v = y[0]
        lc3 = get_lc3_at_time(t, protocol)
        k_eff = autophagy_clearance_rate(lc3)
        return [-k_eff * v]

    sol = solve_ivp(rhs, t_span_days, [initial_load], t_eval=t_eval,
                    method='RK45', rtol=1e-6, atol=1e-9)
    return sol.t, sol.y[0]


# ────────────────────────────────────────────────────────────────
# SECTION 5: ME/CFS ENERGY DEPLETION SAFETY ANALYSIS
# ────────────────────────────────────────────────────────────────

def mecfs_energy_during_fast(t_hour, mitochondrial_deficit=0.40):
    """
    Estimate relative ATP availability during fasting in an ME/CFS patient
    with 30-50% mitochondrial deficit (here: 40% default).

    Healthy baseline ATP = 1.0
    ME/CFS resting ATP ≈ 1.0 - deficit = 0.60

    During fasting, normal subjects maintain ATP via ketogenesis (~12-24h delay).
    ME/CFS patients have impaired fatty-acid oxidation and reduced ketone production.
    Additional energy drop estimated at 15-25% before ketosis kicks in.

    Returns: relative_atp (1.0 = healthy fed, 0.0 = none)
    """
    # ME/CFS resting ATP
    resting_atp = 1.0 - mitochondrial_deficit   # 0.60

    # Early fast dip (before ketosis): peaks at ~8-16h
    dip_magnitude = 0.20   # additional 20% drop at nadir
    dip = dip_magnitude * np.exp(-0.5 * ((t_hour - 12) / 6) ** 2)

    # Ketosis recovery: begins ~16-24h, stabilises at lower-than-baseline
    ketosis_onset = 20.0   # hours
    ketosis_recovery = 0.10 if t_hour > ketosis_onset else 0.0
    k_ket = 0.1
    ketosis_recovery = 0.10 * (1 - np.exp(-k_ket * max(0, t_hour - ketosis_onset)))

    return resting_atp - dip + ketosis_recovery


def pem_risk_score(t_hour, mitochondrial_deficit=0.40, pem_atp_threshold=0.35):
    """
    PEM risk: triggered when ATP drops below pem_atp_threshold.
    Returns a risk score 0-1 (0 = safe, 1 = high PEM risk).
    """
    atp = mecfs_energy_during_fast(t_hour, mitochondrial_deficit)
    if atp > pem_atp_threshold:
        return 0.0
    # Risk scales with depth below threshold
    depth = (pem_atp_threshold - atp) / pem_atp_threshold
    return min(1.0, depth * 2.0)


def find_safe_fast_duration(mitochondrial_deficit, pem_atp_threshold=0.35,
                             max_risk=0.20):
    """
    Find the maximum safe fasting duration (hours) for an ME/CFS patient
    with given mitochondrial deficit before PEM risk exceeds max_risk.
    """
    t_vals = np.linspace(1, 120, 500)
    for t in t_vals:
        if pem_risk_score(t, mitochondrial_deficit, pem_atp_threshold) > max_risk:
            return t
    return 120.0   # safe for full 5 days


# ────────────────────────────────────────────────────────────────
# SECTION 6: MINIMUM FASTING FREQUENCY ANALYSIS
# ────────────────────────────────────────────────────────────────

def scan_protocol_frequency(target_reduction=0.50, t_final_days=365):
    """
    Compute 12-month TD mutant load for standard protocols and find
    which achieves 50% and 90% reduction.
    """
    protocols = ['none', 'daily_16_8', 'weekly_24h', 'monthly_fmd']
    labels = ['No fasting', '16:8 TRE (daily)', '24h fast (weekly)', '5-day FMD (monthly)']
    results = {}
    for p, lbl in zip(protocols, labels):
        t, v = simulate_td_clearance(p, t_span_days=(0, t_final_days))
        results[lbl] = {
            't': t, 'v': v,
            '3mo': float(v[np.argmin(np.abs(t - 91))]),
            '6mo': float(v[np.argmin(np.abs(t - 182))]),
            '9mo': float(v[np.argmin(np.abs(t - 274))]),
            '12mo': float(v[-1])
        }
    return results


# ────────────────────────────────────────────────────────────────
# SECTION 7: HIGH-FREQUENCY SCAN (custom intervals)
# ────────────────────────────────────────────────────────────────

def simulate_custom_fmd_frequency(fmd_interval_days, t_span_days=365, n_points=4380):
    """
    Simulate a 5-day FMD repeated every fmd_interval_days.
    Returns (t_days, V_load)
    """
    fmd_duration_h = 5 * 24.0

    def get_lc3(t_day):
        t_h = t_day * 24.0
        t_within = t_h % (fmd_interval_days * 24.0)
        if t_within <= fmd_duration_h:
            return lc3_ratio(t_within, baseline=0.5, peak=4.5,
                             peak_time=36.0, rise_t_half=8.0, decay_t_half=60.0)
        else:
            t_rec = t_within - fmd_duration_h
            return max(0.5, 0.5 + 4.0 * np.exp(-0.08 * t_rec))

    t_eval = np.linspace(0, t_span_days, n_points)

    def rhs(t, y):
        lc3 = get_lc3(t)
        k_eff = autophagy_clearance_rate(lc3)
        return [-k_eff * y[0]]

    sol = solve_ivp(rhs, (0, t_span_days), [1.0], t_eval=t_eval,
                    method='RK45', rtol=1e-7, atol=1e-10)
    return sol.t, sol.y[0]


# ────────────────────────────────────────────────────────────────
# SECTION 8: PLOTTING
# ────────────────────────────────────────────────────────────────

def plot_autophagy_kinetics():
    """Plot AMPK, ULK1, LC3-II/I, and mTOR during a 5-day continuous fast."""
    t_h = np.linspace(0, 120, 1000)
    ampk = np.array([ampk_activation(t) for t in t_h])
    ulk1 = np.array([ulk1_phosphorylation(ampk_activation(t), current_t=t, fast_onset=0.0) for t in t_h])
    lc3 = np.array([lc3_ratio(t) for t in t_h])
    mtor = np.array([mtor_suppression(t) for t in t_h])

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Autophagy Activation Kinetics During 5-Day Fast\n"
                 "(Based on Alirezaei 2010 and Mizushima kinetics)", fontsize=13)

    ax = axes[0, 0]
    ax.plot(t_h, ampk, 'b-', lw=2)
    ax.axvline(3, color='gray', ls='--', alpha=0.5, label='t½ = 3h')
    ax.set_title("AMPK Activation")
    ax.set_xlabel("Hours after fasting onset")
    ax.set_ylabel("AMPK activity (relative)")
    ax.legend(); ax.set_ylim(0, 1.1); ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.plot(t_h, ulk1, 'g-', lw=2)
    ax.set_title("ULK1 Phosphorylation (autophagy initiation)")
    ax.set_xlabel("Hours after fasting onset")
    ax.set_ylabel("ULK1 activity (relative)")
    ax.set_ylim(0, 1.1); ax.grid(alpha=0.3)

    ax = axes[1, 0]
    ax.plot(t_h, lc3, 'r-', lw=2)
    ax.axhline(0.5, color='gray', ls='--', alpha=0.5, label='Baseline (0.5)')
    ax.axhline(4.0, color='orange', ls='--', alpha=0.5, label='Peak (4.0)')
    ax.fill_between(t_h, 0.5, lc3, where=(lc3 > 0.5), alpha=0.15, color='r')
    ax.set_title("LC3-II/I Ratio (autophagy flux)")
    ax.set_xlabel("Hours after fasting onset")
    ax.set_ylabel("LC3-II/I ratio")
    ax.legend(); ax.grid(alpha=0.3)

    ax = axes[1, 1]
    ax.plot(t_h, mtor, 'purple', lw=2)
    ax.axvline(5, color='gray', ls='--', alpha=0.5, label='Onset ~5h')
    ax.axvline(15, color='orange', ls='--', alpha=0.5, label='Max suppression ~15h')
    ax.set_title("mTOR Activity (1 = normal, 0 = suppressed)")
    ax.set_xlabel("Hours after fasting onset")
    ax.set_ylabel("mTOR activity (relative)")
    ax.legend(); ax.set_ylim(0, 1.1); ax.grid(alpha=0.3)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig1_autophagy_kinetics.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


def plot_td_clearance_protocols():
    """Plot TD mutant load over 12 months for each fasting protocol."""
    results = scan_protocol_frequency()

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("CVB TD Mutant Clearance Under Fasting Protocols\n"
                 "(12-month simulation, normalized load = 1.0 at baseline)", fontsize=13)

    colors = ['black', 'steelblue', 'darkorange', 'darkgreen']
    ax = axes[0]
    for (lbl, res), col in zip(results.items(), colors):
        ax.plot(res['t'], res['v'], lw=2, color=col, label=lbl)
    ax.axhline(0.5, color='gray', ls='--', alpha=0.6, label='50% reduction')
    ax.axhline(0.1, color='red', ls='--', alpha=0.6, label='90% reduction')
    ax.set_xlabel("Days")
    ax.set_ylabel("TD mutant load (normalized)")
    ax.set_title("TD Mutant Load Over 12 Months")
    ax.legend(fontsize=9); ax.set_ylim(0, 1.05); ax.grid(alpha=0.3)

    # Bar chart of 12-month endpoint
    ax = axes[1]
    labels = list(results.keys())
    vals_12mo = [res['12mo'] for res in results.values()]
    bars = ax.bar(range(len(labels)), vals_12mo, color=colors, alpha=0.8)
    ax.axhline(0.5, color='gray', ls='--', alpha=0.7, label='50% target')
    ax.axhline(0.1, color='red', ls='--', alpha=0.7, label='90% target')
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels([l.replace(' (', '\n(') for l in labels], fontsize=9)
    ax.set_ylabel("Remaining TD mutant load at 12 months")
    ax.set_title("12-Month Endpoint by Protocol")
    ax.legend(); ax.set_ylim(0, 1.05); ax.grid(alpha=0.3, axis='y')
    for bar, val in zip(bars, vals_12mo):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.01, f"{val:.2f}",
                ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig2_td_clearance_protocols.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")
    return results


def plot_quarterly_breakdown(results):
    """Plot TD load at 3, 6, 9, 12 months for all protocols."""
    labels = list(results.keys())
    timepoints = ['3mo', '6mo', '9mo', '12mo']
    tp_labels = ['3 months', '6 months', '9 months', '12 months']

    data = np.array([[res[tp] for tp in timepoints] for res in results.values()])

    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(tp_labels))
    width = 0.2
    colors = ['black', 'steelblue', 'darkorange', 'darkgreen']
    for i, (lbl, col) in enumerate(zip(labels, colors)):
        ax.bar(x + i * width, data[i], width, label=lbl, color=col, alpha=0.8)

    ax.axhline(0.5, color='gray', ls='--', lw=1.5, label='50% reduction target')
    ax.axhline(0.1, color='red', ls='--', lw=1.5, label='90% reduction target')
    ax.set_xticks(x + 1.5 * width)
    ax.set_xticklabels(tp_labels)
    ax.set_ylabel("TD mutant load (normalized, 1.0 = baseline)")
    ax.set_title("Quarterly TD Mutant Load: All Fasting Protocols")
    ax.legend(fontsize=9); ax.set_ylim(0, 1.05); ax.grid(alpha=0.3, axis='y')
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig3_quarterly_breakdown.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


def plot_fmd_frequency_scan():
    """Scan FMD interval (days) and find 12-month TD load."""
    intervals = [7, 10, 14, 21, 30, 45, 60, 90]
    loads_12mo = []
    for interval in intervals:
        t, v = simulate_custom_fmd_frequency(interval, t_span_days=365)
        loads_12mo.append(float(v[-1]))

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(intervals, loads_12mo, 'o-', lw=2, color='darkgreen', markersize=8)
    ax.axhline(0.5, color='gray', ls='--', lw=1.5, label='50% reduction')
    ax.axhline(0.1, color='red', ls='--', lw=1.5, label='90% reduction')
    ax.set_xlabel("FMD interval (days between 5-day FMD cycles)")
    ax.set_ylabel("TD mutant load at 12 months (normalized)")
    ax.set_title("Minimum FMD Frequency for 50% / 90% TD Mutant Reduction\nat 12 Months")
    for x, y in zip(intervals, loads_12mo):
        ax.annotate(f"{y:.2f}", (x, y), textcoords="offset points",
                    xytext=(4, 6), fontsize=8)
    ax.legend(); ax.grid(alpha=0.3)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig4_fmd_frequency_scan.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")
    return dict(zip(intervals, loads_12mo))


def plot_mecfs_energy_safety():
    """Plot ATP and PEM risk during fasting for ME/CFS patients."""
    t_h = np.linspace(0, 120, 500)
    deficits = [0.30, 0.40, 0.50]
    labels = ['30% deficit (mild ME/CFS)', '40% deficit (moderate)', '50% deficit (severe)']
    colors = ['steelblue', 'orange', 'red']

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("ME/CFS Energy Safety During Fasting\n"
                 "(reduced mitochondrial ATP production)", fontsize=12)

    ax = axes[0]
    for deficit, lbl, col in zip(deficits, labels, colors):
        atp = [mecfs_energy_during_fast(t, deficit) for t in t_h]
        ax.plot(t_h, atp, lw=2, color=col, label=lbl)
    ax.axhline(0.35, color='black', ls='--', lw=1.5, label='PEM threshold (0.35)')
    ax.axhline(1.0, color='gray', ls=':', alpha=0.5, label='Healthy fed baseline')
    ax.set_xlabel("Hours of fasting")
    ax.set_ylabel("Relative ATP availability")
    ax.set_title("ATP During Fasting — ME/CFS vs Healthy")
    ax.legend(fontsize=8); ax.grid(alpha=0.3); ax.set_ylim(0, 1.1)

    ax = axes[1]
    for deficit, lbl, col in zip(deficits, labels, colors):
        risk = [pem_risk_score(t, deficit) for t in t_h]
        ax.plot(t_h, risk, lw=2, color=col, label=lbl)
        safe_dur = find_safe_fast_duration(deficit)
        ax.axvline(safe_dur, color=col, ls=':', alpha=0.6)
    ax.axhline(0.20, color='gray', ls='--', lw=1.5, label='20% risk threshold')
    ax.set_xlabel("Hours of fasting")
    ax.set_ylabel("PEM risk score (0=safe, 1=high risk)")
    ax.set_title("PEM Risk During Fasting — ME/CFS Severity")
    ax.legend(fontsize=8); ax.grid(alpha=0.3); ax.set_ylim(0, 1.05)

    plt.tight_layout()
    path = os.path.join(OUT_DIR, "fig5_mecfs_pem_safety.png")
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {path}")


# ────────────────────────────────────────────────────────────────
# MAIN
# ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("REQ-006: Autophagy Kinetics — TD Mutant Clearance in ME/CFS")
    print("=" * 60)

    # 1. Kinetics plots
    print("\n[1] Plotting autophagy activation kinetics...")
    plot_autophagy_kinetics()

    # 2. Protocol comparison
    print("\n[2] Simulating TD clearance for all fasting protocols...")
    results = plot_td_clearance_protocols()
    plot_quarterly_breakdown(results)

    # 3. Quarterly table
    print("\n--- Quarterly TD mutant load ---")
    print(f"{'Protocol':<28} {'3mo':>6} {'6mo':>6} {'9mo':>6} {'12mo':>6}")
    print("-" * 55)
    for lbl, res in results.items():
        print(f"{lbl:<28} {res['3mo']:>6.3f} {res['6mo']:>6.3f} {res['9mo']:>6.3f} {res['12mo']:>6.3f}")

    # 4. FMD frequency scan
    print("\n[3] Scanning FMD frequency for 50%/90% reduction thresholds...")
    freq_scan = plot_fmd_frequency_scan()
    print("\n--- FMD interval vs 12-month TD load ---")
    for interval, load in freq_scan.items():
        tag = ""
        if load <= 0.10:
            tag = " <-- 90% reduction achieved"
        elif load <= 0.50:
            tag = " <-- 50% reduction achieved"
        print(f"  FMD every {interval:3d} days: {load:.3f}{tag}")

    # 5. Find threshold intervals
    intervals_sorted = sorted(freq_scan.keys())
    t50 = next((iv for iv in intervals_sorted if freq_scan[iv] <= 0.50), None)
    t90 = next((iv for iv in intervals_sorted if freq_scan[iv] <= 0.10), None)
    print(f"\n  Minimum FMD frequency for 50% reduction: every {t50} days" if t50 else "\n  50% not reached in scan range")
    print(f"  Minimum FMD frequency for 90% reduction: every {t90} days" if t90 else "  90% not reached in scan range")

    # 6. ME/CFS safety
    print("\n[4] ME/CFS fasting safety analysis...")
    plot_mecfs_energy_safety()
    print("\n--- Safe fasting durations by ME/CFS severity ---")
    for deficit in [0.30, 0.40, 0.50]:
        safe_h = find_safe_fast_duration(deficit)
        print(f"  {int(deficit*100)}% mitochondrial deficit: safe up to {safe_h:.1f}h fasting")

    print("\n--- Daily 16:8 TRE assessment ---")
    tres_lc3_peak = max(get_lc3_at_time(t_day, 'daily_16_8')
                        for t_day in np.linspace(0, 1, 200))
    weekly_lc3_peak = max(get_lc3_at_time(t_day, 'weekly_24h')
                          for t_day in np.linspace(0, 7, 2000))
    fmd_lc3_peak = max(get_lc3_at_time(t_day, 'monthly_fmd')
                       for t_day in np.linspace(0, 30, 5000))
    print(f"  16:8 TRE peak LC3-II/I:      {tres_lc3_peak:.2f}  (mild autophagy)")
    print(f"  Weekly 24h peak LC3-II/I:    {weekly_lc3_peak:.2f}  (moderate)")
    print(f"  Monthly FMD peak LC3-II/I:   {fmd_lc3_peak:.2f}  (strong)")

    print("\n[Done] All figures saved to:", OUT_DIR)
