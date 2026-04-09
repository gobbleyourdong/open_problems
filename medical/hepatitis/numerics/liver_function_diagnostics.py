#!/usr/bin/env python3
"""
liver_function_diagnostics.py
==============================
Clinical diagnostic model for CVB hepatitis — lab trajectory predictions
for distinguishing mild from fulminant disease.

systematic approach — ODD (numerics) instance
Disease: CVB Hepatitis
Date: 2026-04-08

PURPOSE
-------
Generate clinician-useful plots of expected lab trajectories at defined
timepoints for CVB hepatitis. The key diagnostic challenge is distinguishing
self-limiting viral hepatitis (treat supportively) from fulminant hepatic
failure (emergency: consider IVIG, liver transplant evaluation).

MODEL
-----
This is a DIAGNOSTIC model, not the mechanistic ODE model (see
hepatocyte_infection_model.py for that). Here we generate expected lab
value trajectories based on the clinical literature and use them to define
decision rules.

CLINICAL LAB MARKERS
  ALT: Alanine aminotransferase — cytoplasmic, specific to hepatocyte injury
  AST: Aspartate aminotransferase — both cytoplasmic and mitochondrial
  De Ritis ratio: AST/ALT — <1 viral hepatitis, >1 severe necrosis or alcohol
  Bilirubin: Total serum bilirubin — conjugation capacity
  INR: International Normalized Ratio — synthetic function (Factor VII, t1/2 6h)
  Albumin: Synthetic function (t1/2 ~20 days, slow responder)
  LDH: Lactate dehydrogenase — general tissue damage, nonspecific

LITERATURE REFERENCES
  [1] Kaplan et al., 1983 — Neonatal CVB hepatitis clinical course
  [2] Abzug et al., 1993 — Neonatal enteroviral disease lab values
  [3] Modlin, 1986 — Adult CVB hepatitis lab course
  [4] Dufour et al., 2000 — Lab diagnosis of hepatitis (AASLD review)
  [5] Polson & Lee, 2005 — Acute liver failure diagnostic criteria
  [6] Botelho-Nevers et al., 2012 — Enteroviral hepatitis in adults
  [7] Verboon-Maciolek et al., 2005 — Neonatal enteroviral multi-organ disease
  [8] De Ritis et al., 1957 — Original AST/ALT ratio paper
  [9] Giannini et al., 2005 — De Ritis ratio in clinical practice

Author: ODD/numerics instance, systematic approach
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


# =============================================================================
# CLINICAL TRAJECTORY DEFINITIONS
# =============================================================================

def generate_lab_trajectory(scenario, days=None):
    """
    Generate expected lab value trajectories for CVB hepatitis scenarios.

    Each scenario is defined by peak values, time to peak, and resolution
    kinetics, derived from clinical literature.

    Scenarios:
      'adult_mild':        Typical adult — subclinical to mild
      'adult_moderate':    Adult with moderate hepatitis (rare, immunosuppressed?)
      'neonate_moderate':  Neonate with some maternal Ab protection
      'neonate_severe':    Neonate, no maternal Ab, fulminant course
    """
    if days is None:
        days = np.linspace(0, 28, 500)

    trajectories = {}

    if scenario == 'adult_mild':
        # Adult CVB hepatitis [3,6]:
        # ALT rises to 100-300, peaks day 5-7, normalizes by day 14-21
        # Often subclinical — many never tested
        trajectories = _build_trajectory(
            days=days,
            alt_baseline=25,     alt_peak=200,      alt_peak_day=6,    alt_halflife=3.5,
            ast_ratio_base=0.7,  ast_ratio_peak=0.8,  # De Ritis <1 (viral pattern)
            bili_baseline=0.7,   bili_peak=1.5,      bili_peak_day=8,   bili_halflife=4.0,
            inr_baseline=1.0,    inr_peak=1.1,       inr_peak_day=7,   inr_halflife=3.0,
            albumin_baseline=4.0, albumin_nadir=3.8,  albumin_nadir_day=10,
            scenario_name='Adult Mild'
        )

    elif scenario == 'adult_moderate':
        # Less common: adult with moderate CVB hepatitis
        # ALT 300-800, resolves more slowly
        trajectories = _build_trajectory(
            days=days,
            alt_baseline=25,     alt_peak=500,      alt_peak_day=7,    alt_halflife=5.0,
            ast_ratio_base=0.7,  ast_ratio_peak=0.9,
            bili_baseline=0.7,   bili_peak=3.5,      bili_peak_day=9,   bili_halflife=5.0,
            inr_baseline=1.0,    inr_peak=1.3,       inr_peak_day=8,   inr_halflife=4.0,
            albumin_baseline=4.0, albumin_nadir=3.5,  albumin_nadir_day=12,
            scenario_name='Adult Moderate'
        )

    elif scenario == 'neonate_moderate':
        # Neonate with partial maternal Ab protection [1,2,7]:
        # ALT rises higher, slower resolution
        trajectories = _build_trajectory(
            days=days,
            alt_baseline=30,     alt_peak=800,      alt_peak_day=5,    alt_halflife=6.0,
            ast_ratio_base=0.8,  ast_ratio_peak=1.1,  # AST/ALT approaches 1
            bili_baseline=2.0,   bili_peak=8.0,      bili_peak_day=7,   bili_halflife=7.0,
            # Neonates have higher baseline bilirubin (physiologic jaundice)
            inr_baseline=1.0,    inr_peak=1.6,       inr_peak_day=6,   inr_halflife=5.0,
            albumin_baseline=3.2, albumin_nadir=2.6,  albumin_nadir_day=10,
            scenario_name='Neonate Moderate'
        )

    elif scenario == 'neonate_severe':
        # Fulminant neonatal CVB hepatitis [1,2,7]:
        # ALT >1000-5000, coagulopathy, possible death
        trajectories = _build_trajectory(
            days=days,
            alt_baseline=30,     alt_peak=3500,     alt_peak_day=4,    alt_halflife=8.0,
            ast_ratio_base=0.9,  ast_ratio_peak=1.8,  # De Ritis >1 = severe necrosis [8,9]
            bili_baseline=2.0,   bili_peak=18.0,     bili_peak_day=6,   bili_halflife=10.0,
            inr_baseline=1.0,    inr_peak=3.5,       inr_peak_day=5,   inr_halflife=8.0,
            albumin_baseline=3.0, albumin_nadir=1.8,  albumin_nadir_day=8,
            scenario_name='Neonate Severe (Fulminant)',
            fulminant=True
        )

    return trajectories


def _build_trajectory(days, alt_baseline, alt_peak, alt_peak_day, alt_halflife,
                      ast_ratio_base, ast_ratio_peak,
                      bili_baseline, bili_peak, bili_peak_day, bili_halflife,
                      inr_baseline, inr_peak, inr_peak_day, inr_halflife,
                      albumin_baseline, albumin_nadir, albumin_nadir_day,
                      scenario_name, fulminant=False):
    """
    Build lab value trajectory using asymmetric Gaussian-like rise/fall.

    Rise phase: exponential approach to peak
    Fall phase: exponential decay with half-life
    Fulminant: ALT may PARADOXICALLY DROP as hepatocytes are exhausted
    """
    n = len(days)

    # --- ALT ---
    ALT = np.zeros(n)
    for i, d in enumerate(days):
        if d <= alt_peak_day:
            # Rise phase: exponential
            rise_frac = 1.0 - np.exp(-2.0 * d / alt_peak_day)
            ALT[i] = alt_baseline + (alt_peak - alt_baseline) * rise_frac
        else:
            # Decay phase
            decay_time = d - alt_peak_day
            if fulminant and decay_time > 5:
                # In fulminant hepatitis, ALT can DROP paradoxically
                # because there are no more hepatocytes to release ALT
                # This is an OMINOUS sign (Polson & Lee 2005)
                ALT[i] = alt_peak * np.exp(-np.log(2) * decay_time / alt_halflife)
                # Additional crash after day 10
                crash_factor = np.exp(-0.3 * max(0, decay_time - 5))
                ALT[i] *= crash_factor
            else:
                ALT[i] = alt_baseline + (alt_peak - alt_baseline) * np.exp(
                    -np.log(2) * decay_time / alt_halflife)

    # --- AST (computed from ALT via De Ritis ratio) ---
    # Ratio changes over time: starts at baseline ratio, peaks at peak ratio
    AST_ALT_ratio = np.zeros(n)
    for i, d in enumerate(days):
        # Ratio rises with severity and time
        if d <= alt_peak_day + 2:
            frac = min(1.0, d / (alt_peak_day + 2))
            AST_ALT_ratio[i] = ast_ratio_base + (ast_ratio_peak - ast_ratio_base) * frac
        else:
            # Ratio slowly returns to baseline
            decay = (d - alt_peak_day - 2) / 10.0
            AST_ALT_ratio[i] = ast_ratio_base + (ast_ratio_peak - ast_ratio_base) * np.exp(-decay)
    AST = ALT * AST_ALT_ratio

    # --- Bilirubin ---
    bilirubin = np.zeros(n)
    for i, d in enumerate(days):
        if d <= bili_peak_day:
            rise_frac = 1.0 - np.exp(-2.0 * d / bili_peak_day)
            bilirubin[i] = bili_baseline + (bili_peak - bili_baseline) * rise_frac
        else:
            decay_time = d - bili_peak_day
            if fulminant:
                # Bilirubin stays elevated much longer in fulminant (impaired conjugation)
                bilirubin[i] = bili_baseline + (bili_peak - bili_baseline) * np.exp(
                    -np.log(2) * decay_time / (bili_halflife * 2))
            else:
                bilirubin[i] = bili_baseline + (bili_peak - bili_baseline) * np.exp(
                    -np.log(2) * decay_time / bili_halflife)

    # --- INR ---
    INR = np.zeros(n)
    for i, d in enumerate(days):
        if d <= inr_peak_day:
            rise_frac = 1.0 - np.exp(-2.5 * d / inr_peak_day)
            INR[i] = inr_baseline + (inr_peak - inr_baseline) * rise_frac
        else:
            decay_time = d - inr_peak_day
            if fulminant:
                # INR may continue to rise in fulminant (ongoing synthetic failure)
                INR[i] = inr_peak * (1.0 + 0.1 * min(decay_time, 10))
                # Eventually either death or slow recovery
                if decay_time > 10:
                    INR[i] = inr_peak * 1.5 * np.exp(-0.05 * (decay_time - 10))
            else:
                INR[i] = inr_baseline + (inr_peak - inr_baseline) * np.exp(
                    -np.log(2) * decay_time / inr_halflife)

    # --- Albumin ---
    # Slow responder (t1/2 ~20 days) — more useful for chronic disease
    albumin = np.zeros(n)
    for i, d in enumerate(days):
        if d <= albumin_nadir_day:
            drop_frac = 1.0 - np.exp(-1.5 * d / albumin_nadir_day)
            albumin[i] = albumin_baseline - (albumin_baseline - albumin_nadir) * drop_frac
        else:
            recovery_time = d - albumin_nadir_day
            if fulminant:
                albumin[i] = albumin_nadir  # No recovery in fulminant
            else:
                albumin[i] = albumin_nadir + (albumin_baseline - albumin_nadir) * (
                    1.0 - np.exp(-np.log(2) * recovery_time / 14.0))

    return {
        'days': days,
        'ALT': ALT,
        'AST': AST,
        'AST_ALT_ratio': AST_ALT_ratio,
        'bilirubin': bilirubin,
        'INR': INR,
        'albumin': albumin,
        'scenario_name': scenario_name,
    }


# =============================================================================
# DIAGNOSTIC DECISION RULES
# =============================================================================

def diagnostic_timeline():
    """
    Print the diagnostic decision tree at key timepoints.

    When a neonate presents with nonspecific illness and hepatitis is suspected,
    these are the lab values that distinguish mild from fulminant.
    """
    print("=" * 85)
    print("CVB HEPATITIS — DIAGNOSTIC DECISION TIMELINE")
    print("=" * 85)

    print("""
    PRESENTATION (Day 0-1):
    ========================
    Nonspecific: fever, irritability (neonates), malaise (adults)
    Often NO hepatitis-specific symptoms yet
    Send: ALT, AST, bilirubin, INR, CBC, blood culture, enteroviral PCR

    DAY 2-3 — FIRST LAB CHECK:
    ===========================
    +-----------+-------------------+-------------------+-------------------+
    | Lab       | Mild (adult)      | Moderate          | ALARM (fulminant) |
    +-----------+-------------------+-------------------+-------------------+
    | ALT       | 50-150 U/L        | 200-500 U/L       | >500 U/L          |
    | AST/ALT   | <0.8              | 0.8-1.0           | >1.0              |
    | Bilirubin | <2 mg/dL          | 2-5 mg/dL         | >5 mg/dL          |
    | INR       | <1.2              | 1.2-1.5           | >1.5              |
    +-----------+-------------------+-------------------+-------------------+

    DECISION at Day 2-3:
      INR >1.5 → FULMINANT HEPATITIS PROTOCOL
        → NICU/ICU, check Factor V level
        → Consider IVIG (750 mg/kg) [Abzug protocol]
        → Alert transplant team
        → Enteroviral PCR if not sent
      INR <1.5, ALT <500 → Monitor, recheck in 24-48h

    DAY 4-5 — CRITICAL WINDOW:
    ===========================
    +-----------+-------------------+-------------------+-------------------+
    | Lab       | Resolving         | Worsening         | FULMINANT         |
    +-----------+-------------------+-------------------+-------------------+
    | ALT trend | Stable or falling | Rising            | >1000 (or DROP*)  |
    | AST/ALT   | <1.0              | Rising toward 1   | >1.5              |
    | Bilirubin | Stable            | Rising             | >10 mg/dL         |
    | INR       | Stable <1.2       | Rising toward 1.5 | >2.0              |
    +-----------+-------------------+-------------------+-------------------+

    *CRITICAL: A FALLING ALT with RISING INR is the WORST sign.
     It means hepatocytes are being destroyed so fast there are none left
     to release ALT. This is the "ALT-INR dissociation" [5].

    DAY 7-10 — OUTCOME DETERMINATION:
    ==================================
    Mild/Moderate: ALT falling, INR normalizing → supportive care, discharge planning
    Fulminant: INR >3, encephalopathy → transplant evaluation

    DAY 14-21 — RECOVERY MONITORING:
    =================================
    Check: ALT should be <100 U/L (mild) or falling trend (moderate)
    Persistent ALT >100 at day 21 → consider chronic hepatitis / other etiology
    """)

    print("\n" + "=" * 85)
    print("THE ALT-INR DISSOCIATION — THE MOST DANGEROUS SIGN")
    print("=" * 85)
    print("""
    Normal pattern: ALT rises → peaks → falls as liver heals
    Fulminant pattern: ALT rises → peaks → CRASHES while INR RISES

    The crash happens because:
      1. Massive hepatocyte necrosis → all ALT released → peak
      2. No hepatocytes left to die → ALT drops (not from healing!)
      3. No hepatocytes left to synthesize clotting factors → INR rises
      4. This dissociation = >80% hepatocyte loss = hepatic failure

    Recognition of this pattern is the single most important diagnostic
    skill in acute liver failure management.
    """)


# =============================================================================
# PLOTTING — Clinician-Oriented Figures
# =============================================================================

def plot_diagnostic_trajectories(output_dir):
    """Generate clinical trajectory plots for all scenarios."""
    os.makedirs(output_dir, exist_ok=True)

    scenarios = ['adult_mild', 'adult_moderate', 'neonate_moderate', 'neonate_severe']
    days = np.linspace(0, 28, 500)

    trajs = [generate_lab_trajectory(s, days) for s in scenarios]

    colors = ['#1976d2', '#388e3c', '#f57c00', '#d32f2f']
    styles = ['-', '--', '-', '-']
    linewidths = [2, 2, 2, 3]

    # ---- Figure 1: ALT and AST trajectories ----
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    for i, tr in enumerate(trajs):
        axes[0, 0].plot(tr['days'], tr['ALT'], color=colors[i], ls=styles[i],
                        lw=linewidths[i], label=tr['scenario_name'])
    axes[0, 0].set_ylabel('ALT (U/L)', fontsize=11)
    axes[0, 0].set_title('ALT Trajectory', fontweight='bold')
    axes[0, 0].axhline(y=40, color='gray', ls=':', alpha=0.6, label='Upper normal (40)')
    axes[0, 0].axhline(y=1000, color='red', ls=':', alpha=0.4, label='Fulminant cutoff')
    axes[0, 0].set_yscale('log')
    axes[0, 0].set_ylim(10, 10000)
    axes[0, 0].legend(fontsize=7, loc='upper right')

    for i, tr in enumerate(trajs):
        axes[0, 1].plot(tr['days'], tr['AST'], color=colors[i], ls=styles[i],
                        lw=linewidths[i], label=tr['scenario_name'])
    axes[0, 1].set_ylabel('AST (U/L)', fontsize=11)
    axes[0, 1].set_title('AST Trajectory', fontweight='bold')
    axes[0, 1].set_yscale('log')
    axes[0, 1].set_ylim(10, 15000)
    axes[0, 1].legend(fontsize=7, loc='upper right')

    for i, tr in enumerate(trajs):
        axes[1, 0].plot(tr['days'], tr['AST_ALT_ratio'], color=colors[i], ls=styles[i],
                        lw=linewidths[i], label=tr['scenario_name'])
    axes[1, 0].set_ylabel('AST/ALT Ratio', fontsize=11)
    axes[1, 0].set_title('De Ritis Ratio (AST/ALT)', fontweight='bold')
    axes[1, 0].axhline(y=1.0, color='red', ls='--', alpha=0.5, label='Ratio = 1.0 (cutoff)')
    axes[1, 0].set_ylim(0.4, 2.5)
    axes[1, 0].legend(fontsize=7)

    # ALT-INR dissociation plot (fulminant only)
    ax = axes[1, 1]
    tr_severe = trajs[3]  # neonate_severe
    ax2 = ax.twinx()
    ln1 = ax.plot(tr_severe['days'], tr_severe['ALT'], color='#d32f2f', lw=2.5,
                  label='ALT (fulminant)')
    ln2 = ax2.plot(tr_severe['days'], tr_severe['INR'], color='#1a237e', lw=2.5,
                   ls='--', label='INR (fulminant)')
    ax.set_ylabel('ALT (U/L)', color='#d32f2f', fontsize=11)
    ax2.set_ylabel('INR', color='#1a237e', fontsize=11)
    ax.set_title('ALT-INR Dissociation (DANGER SIGN)', fontweight='bold', color='#d32f2f')
    # Add danger zone
    ax.axvspan(6, 14, alpha=0.08, color='red')
    ax.text(10, max(tr_severe['ALT']) * 0.85, 'DANGER\nZONE',
            ha='center', fontsize=12, color='red', fontweight='bold', alpha=0.5)
    lns = ln1 + ln2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, fontsize=8, loc='center right')

    for ax in axes.flat:
        ax.set_xlabel('Days post-infection')
        ax.grid(True, alpha=0.3)

    fig.suptitle('CVB Hepatitis: Diagnostic Lab Trajectories',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'diagnostic_trajectories.png'),
                dpi=150, bbox_inches='tight')
    plt.close()

    # ---- Figure 2: Bilirubin, INR, Albumin ----
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for i, tr in enumerate(trajs):
        axes[0].plot(tr['days'], tr['bilirubin'], color=colors[i], ls=styles[i],
                     lw=linewidths[i], label=tr['scenario_name'])
    axes[0].set_ylabel('Bilirubin (mg/dL)', fontsize=11)
    axes[0].set_title('Total Bilirubin', fontweight='bold')
    axes[0].axhline(y=1.2, color='gray', ls=':', alpha=0.5, label='Upper normal')
    axes[0].axhline(y=5.0, color='orange', ls='--', alpha=0.5, label='Clinical jaundice')
    axes[0].axhline(y=10.0, color='red', ls='--', alpha=0.5, label='Severe')
    axes[0].legend(fontsize=7)

    for i, tr in enumerate(trajs):
        axes[1].plot(tr['days'], tr['INR'], color=colors[i], ls=styles[i],
                     lw=linewidths[i], label=tr['scenario_name'])
    axes[1].set_ylabel('INR', fontsize=11)
    axes[1].set_title('INR — Synthetic Function', fontweight='bold')
    axes[1].axhline(y=1.5, color='orange', ls='--', alpha=0.5, label='Significant (1.5)')
    axes[1].axhline(y=2.0, color='red', ls='--', alpha=0.5, label='Severe (2.0)')
    axes[1].legend(fontsize=7)

    for i, tr in enumerate(trajs):
        axes[2].plot(tr['days'], tr['albumin'], color=colors[i], ls=styles[i],
                     lw=linewidths[i], label=tr['scenario_name'])
    axes[2].set_ylabel('Albumin (g/dL)', fontsize=11)
    axes[2].set_title('Serum Albumin', fontweight='bold')
    axes[2].axhline(y=3.5, color='gray', ls=':', alpha=0.5, label='Lower normal')
    axes[2].axhline(y=2.5, color='red', ls='--', alpha=0.5, label='Severe')
    axes[2].legend(fontsize=7)

    for ax in axes:
        ax.set_xlabel('Days post-infection')
        ax.grid(True, alpha=0.3)

    fig.suptitle('CVB Hepatitis: Bilirubin, INR, and Albumin Trajectories',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'severity_markers.png'),
                dpi=150, bbox_inches='tight')
    plt.close()

    # ---- Figure 3: Decision support — when to escalate ----
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot all INR trajectories with escalation thresholds
    for i, tr in enumerate(trajs):
        ax.plot(tr['days'], tr['INR'], color=colors[i], ls=styles[i],
                lw=linewidths[i], label=tr['scenario_name'])

    ax.axhline(y=1.0, color='green', ls='-', alpha=0.3, lw=8, label='Normal')
    ax.axhspan(1.0, 1.5, alpha=0.05, color='green')
    ax.axhspan(1.5, 2.0, alpha=0.08, color='yellow')
    ax.axhspan(2.0, 3.0, alpha=0.08, color='orange')
    ax.axhspan(3.0, 6.0, alpha=0.08, color='red')

    ax.text(25, 1.2, 'MONITOR', ha='center', fontsize=10, color='green', fontweight='bold')
    ax.text(25, 1.7, 'CONCERN — recheck 12h', ha='center', fontsize=10,
            color='#e65100', fontweight='bold')
    ax.text(25, 2.4, 'SIGNIFICANT — IVIG, ICU', ha='center', fontsize=10,
            color='#d84315', fontweight='bold')
    ax.text(25, 4.0, 'SEVERE — TRANSPLANT EVAL', ha='center', fontsize=10,
            color='#b71c1c', fontweight='bold')

    ax.set_xlabel('Days post-infection', fontsize=12)
    ax.set_ylabel('INR', fontsize=12)
    ax.set_title('INR-Based Escalation Protocol for CVB Hepatitis',
                 fontsize=14, fontweight='bold')
    ax.set_ylim(0.8, 6.0)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'inr_escalation_protocol.png'),
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"  Diagnostic plots saved to {output_dir}")


# =============================================================================
# LAB VALUE COMPARISON TABLE
# =============================================================================

def print_lab_comparison():
    """Print a formatted table of expected lab values at key timepoints."""
    print("\n" + "=" * 95)
    print("EXPECTED LAB VALUES BY SCENARIO AND TIMEPOINT")
    print("=" * 95)

    scenarios = ['adult_mild', 'adult_moderate', 'neonate_moderate', 'neonate_severe']
    timepoints = [0, 2, 5, 7, 10, 14, 21]

    for scenario in scenarios:
        traj = generate_lab_trajectory(scenario, np.array(timepoints, dtype=float))
        print(f"\n  {traj['scenario_name']}:")
        print(f"  {'Day':>5} {'ALT':>8} {'AST':>8} {'AST/ALT':>8} {'Bili':>8} {'INR':>8} {'Alb':>8}")
        print(f"  {'-'*56}")
        for i, day in enumerate(timepoints):
            print(f"  {day:>5} {traj['ALT'][i]:>8.0f} {traj['AST'][i]:>8.0f} "
                  f"{traj['AST_ALT_ratio'][i]:>8.2f} {traj['bilirubin'][i]:>8.1f} "
                  f"{traj['INR'][i]:>8.2f} {traj['albumin'][i]:>8.1f}")

    print(f"\n  Units: ALT/AST = U/L, Bilirubin = mg/dL, Albumin = g/dL")
    print(f"  Normal ranges: ALT <40, AST <40, Bili <1.2, INR ~1.0, Alb 3.5-5.0")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("CVB Hepatitis — Clinical Diagnostic Model\n")

    # Print diagnostic decision timeline
    diagnostic_timeline()

    # Print lab comparison table
    print_lab_comparison()

    # Generate plots
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           '..', 'results', 'figures')
    plot_diagnostic_trajectories(out_dir)

    print("\n" + "=" * 85)
    print("KEY DIAGNOSTIC MESSAGES")
    print("=" * 85)
    print("""
    1. CVB HEPATITIS IS UNDERDIAGNOSED in adults because:
       - Mild transaminase elevation often attributed to "nonspecific viral illness"
       - Enteroviral PCR rarely ordered in hepatitis workups
       - Self-limiting → patient recovers before etiology established

    2. IN NEONATES, the window between "mild" and "fulminant" is HOURS:
       - Day 2: ALT 200 → could be either
       - Day 3: ALT 800, INR rising → fulminant trajectory established
       - Day 5: ALT dropping + INR >2.0 → catastrophic (ALT-INR dissociation)

    3. THE DE RITIS RATIO IS UNDERUSED:
       - AST/ALT <1.0 in viral hepatitis (cytoplasmic release only)
       - AST/ALT >1.0 in severe necrosis (mitochondrial AST released)
       - Rising De Ritis ratio = worsening prognosis
       - This is a FREE diagnostic tool from labs already ordered

    4. FOR T1DM MONITORING:
       - Check liver enzymes before starting itraconazole/fluoxetine
       - If subclinical CVB hepatitis present (ALT 50-100), dose adjustment needed
       - Fluoxetine is hepatically metabolized (CYP2D6, CYP2C19)
       - Persistent mild ALT elevation may indicate ongoing CVB replication
    """)

    print("\nDone.")
