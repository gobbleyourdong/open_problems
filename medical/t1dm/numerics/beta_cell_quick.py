#!/usr/bin/env python3
"""
Beta Cell Quick — Lightweight Verification Wrapper
====================================================

Quick-run version of beta_cell_dynamics.py for verification purposes.

What this does:
  1. Runs 4 base scenarios (no intervention, Phase 1, full protocol, full+tepl)
     with 24-month horizon (fast: ~10s total)
  2. Runs a quick 100-patient Monte Carlo with 12-month horizon (~30s)
  3. Generates comparison plots and prints key numbers
  4. Total target runtime: <60 seconds

Why:
  The full beta_cell_dynamics.py MC (2000 patients x 3yr) times out at >2 min.
  This wrapper proves the ODE system works, generates the key plots, and runs
  a reduced MC for quick verification of outcome distributions.

systematic approach — T1DM Core Model — ODD Instance (numerics)
"""

import numpy as np
import time
import os
import sys
import json

# Import everything from the full model
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from beta_cell_dynamics import (
    BetaCellParams, ProtocolParams,
    patient_zero_params, simulate,
    fmd_state, intervention_active, beta_cell_ode,
    plot_scenario_comparison, plot_monte_carlo,
)
from copy import deepcopy

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
os.makedirs(OUTPUT_DIR, exist_ok=True)

RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(RESULTS_DIR, exist_ok=True)


# =============================================================================
# SCENARIO RUNNERS (24-month horizon, reduced output)
# =============================================================================

def run_scenario_no_intervention(t_years=2.0):
    """No intervention baseline."""
    params = patient_zero_params()
    protocol = ProtocolParams(
        fluoxetine_start_day=1e6,
        vitamin_d_start_day=1e6,
        butyrate_start_day=1e6,
        fmd_start_day=1e6,
        gaba_start_day=1e6,
        semaglutide_start_day=1e6,
        bhb_start_day=1e6,
        teplizumab_enabled=False,
    )
    return simulate(params, protocol, t_years=t_years, label="no_intervention")


def run_scenario_phase1(t_years=2.0):
    """Phase 1 only: fluoxetine + vitamin D + butyrate."""
    params = patient_zero_params()
    protocol = ProtocolParams(
        fmd_start_day=1e6,
        gaba_start_day=1e6,
        semaglutide_start_day=1e6,
        teplizumab_enabled=False,
    )
    return simulate(params, protocol, t_years=t_years, label="phase1_only")


def run_scenario_full(t_years=2.0):
    """Full protocol (Phases 1-3, no teplizumab)."""
    params = patient_zero_params()
    protocol = ProtocolParams()
    return simulate(params, protocol, t_years=t_years, label="full_protocol")


def run_scenario_tepl(t_years=2.0):
    """Full protocol + teplizumab."""
    params = patient_zero_params()
    protocol = ProtocolParams(teplizumab_enabled=True)
    return simulate(params, protocol, t_years=t_years, label="full_plus_tepl")


# =============================================================================
# KEY NUMBERS EXTRACTION
# =============================================================================

def extract_key_numbers(result, label):
    """Extract beta cell mass at 6, 12, 24 months."""
    t_days = result['t_days']
    B = result['B']
    Cp = result['Cp_ss']

    milestones = {}
    for months, days in [(6, 182.625), (12, 365.25), (24, 730.5)]:
        idx = np.argmin(np.abs(t_days - days))
        if idx < len(B):
            milestones[f"B_{months}mo"] = float(B[idx])
            milestones[f"Cp_{months}mo"] = float(Cp[idx])
        else:
            milestones[f"B_{months}mo"] = None
            milestones[f"Cp_{months}mo"] = None

    milestones['final_B'] = result['final_B']
    milestones['final_Cp'] = result['final_Cp']
    milestones['virus_cleared'] = result['virus_cleared']
    milestones['permanent_remission'] = result['permanent_remission']

    return milestones


def print_key_numbers(all_milestones):
    """Print a formatted table of key numbers across scenarios."""
    print("\n" + "=" * 90)
    print("KEY NUMBERS: Beta Cell Mass (% normal) at 6, 12, 24 months")
    print("=" * 90)

    header = f"{'Scenario':<25} {'B@6mo':>8} {'B@12mo':>8} {'B@24mo':>8} {'Cp@12mo':>9} {'Cp@24mo':>9} {'Remission':>10}"
    print(header)
    print("-" * 90)

    for label, m in all_milestones.items():
        b6 = f"{m['B_6mo']*100:.2f}%" if m['B_6mo'] is not None else "N/A"
        b12 = f"{m['B_12mo']*100:.2f}%" if m['B_12mo'] is not None else "N/A"
        b24 = f"{m['B_24mo']*100:.2f}%" if m['B_24mo'] is not None else "N/A"
        cp12 = f"{m['Cp_12mo']:.3f}" if m['Cp_12mo'] is not None else "N/A"
        cp24 = f"{m['Cp_24mo']:.3f}" if m['Cp_24mo'] is not None else "N/A"
        rem = "YES" if m['permanent_remission'] else "NO"
        print(f"{label:<25} {b6:>8} {b12:>8} {b24:>8} {cp12:>9} {cp24:>9} {rem:>10}")


# =============================================================================
# QUICK MONTE CARLO (100 patients, 12 months)
# =============================================================================

def quick_monte_carlo(n_samples=100, t_years=1.0, seed=42):
    """
    Reduced Monte Carlo for quick verification.
    100 patients x 1yr instead of 2000 x 3yr.
    """
    print(f"\n  Quick MC: {n_samples} patients x {t_years:.0f}yr ...")

    rng = np.random.default_rng(seed)

    final_B_list = []
    final_Cp_list = []
    time_to_cp_list = []
    time_to_b20_list = []
    time_to_indep_list = []
    virus_cleared_list = []
    permanent_remission_list = []
    trajectories_B = []

    baseline_params = patient_zero_params()
    protocol = ProtocolParams()

    for i in range(n_samples):
        if (i + 1) % 25 == 0:
            print(f"    ... sample {i+1}/{n_samples}")

        p = deepcopy(baseline_params)

        # Same distributions as full MC
        p.B_initial = np.clip(rng.lognormal(np.log(0.08), 0.35), 0.02, 0.20)
        p.Bd_initial = np.clip(rng.lognormal(np.log(0.04), 0.40), 0.01, 0.12)
        p.TD_initial = np.clip(rng.normal(35.0, 12.0), 10.0, 80.0)
        p.V_initial = np.clip(rng.lognormal(np.log(5.0), 0.5), 0.5, 30.0)
        p.Teff_initial = np.clip(rng.normal(15.0, 5.0), 3.0, 35.0)
        p.Treg_initial = np.clip(rng.normal(10.0, 3.0), 3.0, 20.0)
        p.Teff_exhaustion_factor = np.clip(rng.normal(0.15, 0.05), 0.0, 0.35)
        p.hla_risk = np.clip(rng.normal(1.0, 0.2), 0.5, 1.8)
        p.Cp_secretion_efficiency = np.clip(rng.normal(0.6, 0.15), 0.25, 0.95)
        p.B_replication_rate = np.clip(rng.lognormal(np.log(0.003), 0.3), 0.001, 0.008)
        p.Ab_initial = np.clip(rng.normal(25.0, 10.0), 5.0, 60.0)

        try:
            result = simulate(p, protocol, t_years=t_years, label=f"mc_{i}")

            final_B_list.append(result['final_B'])
            final_Cp_list.append(result['final_Cp'])
            time_to_cp_list.append(result['time_to_cp_signal'])
            time_to_b20_list.append(result['time_to_b20'])
            time_to_indep_list.append(result['time_to_independence'])
            virus_cleared_list.append(result['virus_cleared'])
            permanent_remission_list.append(result['permanent_remission'])

            # Store trajectory at lower resolution
            if i < 100:
                idx = np.arange(0, len(result['B']), 7)
                trajectories_B.append(result['B'][idx])

        except Exception as e:
            print(f"    WARNING: sample {i} failed: {e}")
            continue

    # Aggregate
    final_B = np.array(final_B_list)
    final_Cp = np.array(final_Cp_list)
    n_success = len(final_B)

    n_cp_improved = sum(1 for cp in final_Cp if cp > 0.20)
    n_b15 = sum(1 for b in final_B if b > 0.15)
    n_indep = sum(1 for b in final_B if b > 0.30)
    n_remission = sum(1 for r in permanent_remission_list if r)
    n_virus_clear = sum(1 for v in virus_cleared_list if v)

    valid_cp_times = [t for t in time_to_cp_list if t is not None]
    valid_indep_times = [t for t in time_to_indep_list if t is not None]

    mc_results = {
        "n_samples": n_success,
        "final_B": final_B,
        "final_Cp": final_Cp,
        "time_to_cp": time_to_cp_list,
        "time_to_b20": time_to_b20_list,
        "time_to_independence": time_to_indep_list,
        "virus_cleared_frac": n_virus_clear / max(n_success, 1),
        "cp_improved_frac": n_cp_improved / max(n_success, 1),
        "b15_frac": n_b15 / max(n_success, 1),
        "independence_frac": n_indep / max(n_success, 1),
        "remission_frac": n_remission / max(n_success, 1),
        "trajectories_B": trajectories_B,
    }

    return mc_results


def print_mc_summary(mc):
    """Print Monte Carlo outcome probabilities."""
    n = mc['n_samples']
    print(f"\n" + "=" * 70)
    print(f"QUICK MC RESULTS ({n} patients, full protocol)")
    print("=" * 70)
    print(f"  Final beta cell mass:")
    print(f"    Mean:   {np.mean(mc['final_B'])*100:.1f}%")
    print(f"    Median: {np.median(mc['final_B'])*100:.1f}%")
    print(f"    5th:    {np.percentile(mc['final_B'], 5)*100:.1f}%")
    print(f"    95th:   {np.percentile(mc['final_B'], 95)*100:.1f}%")
    print(f"  Outcome probabilities:")
    print(f"    C-peptide improved (>0.2):  {mc['cp_improved_frac']*100:.0f}%")
    print(f"    Beta cells > 15%:           {mc['b15_frac']*100:.0f}%")
    print(f"    Insulin independence (>30%): {mc['independence_frac']*100:.0f}%")
    print(f"    Permanent remission:         {mc['remission_frac']*100:.0f}%")
    print(f"    Virus cleared:               {mc['virus_cleared_frac']*100:.0f}%")


# =============================================================================
# QUICK COMPARISON PLOT
# =============================================================================

def plot_quick_comparison(results, filename="beta_cell_quick_comparison.png"):
    """Generate a compact 2x3 comparison plot for the 4 scenarios."""
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    colors = ['#c0392b', '#2980b9', '#27ae60', '#8e44ad']
    labels_short = {
        'no_intervention': 'No intervention',
        'phase1_only': 'Phase 1 only',
        'full_protocol': 'Full protocol',
        'full_plus_tepl': 'Full + teplizumab',
    }

    # 1. Beta cell mass
    ax = axes[0, 0]
    for i, r in enumerate(results):
        ax.plot(r['t_years'], r['B'] * 100, color=colors[i], linewidth=2,
                label=labels_short.get(r['label'], r['label']))
    ax.axhline(y=30, color='gray', linestyle='--', alpha=0.5, label='Insulin indep.')
    ax.axhline(y=10, color='gray', linestyle=':', alpha=0.5)
    ax.set_ylabel('Beta cell mass (% normal)')
    ax.set_title('Functional Beta Cell Mass')
    ax.legend(fontsize=7)
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    # 2. C-peptide
    ax = axes[0, 1]
    for i, r in enumerate(results):
        ax.plot(r['t_years'], r['Cp_ss'], color=colors[i], linewidth=2,
                label=labels_short.get(r['label'], r['label']))
    ax.axhline(y=0.2, color='gray', linestyle='--', alpha=0.5)
    ax.axhline(y=0.6, color='gray', linestyle=':', alpha=0.5)
    ax.set_ylabel('C-peptide (nmol/L)')
    ax.set_title('C-peptide (Steady-State)')
    ax.legend(fontsize=7)
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    # 3. T effectors
    ax = axes[0, 2]
    for i, r in enumerate(results):
        ax.plot(r['t_years'], r['Teff'], color=colors[i], linewidth=2,
                label=labels_short.get(r['label'], r['label']))
    ax.set_ylabel('Teff activity')
    ax.set_title('Autoreactive CD8+ T Cells')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # 4. Tregs
    ax = axes[1, 0]
    for i, r in enumerate(results):
        ax.plot(r['t_years'], r['Treg'], color=colors[i], linewidth=2,
                label=labels_short.get(r['label'], r['label']))
    ax.axhline(y=22, color='gray', linestyle='--', alpha=0.5, label='Healthy')
    ax.set_ylabel('Treg activity')
    ax.set_title('Regulatory T Cells')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Years')

    # 5. Viral load
    ax = axes[1, 1]
    for i, r in enumerate(results):
        ax.plot(r['t_years'], r['V'], color=colors[i], linewidth=2,
                label=labels_short.get(r['label'], r['label']))
    ax.set_ylabel('Replicating virus')
    ax.set_title('CVB Viral Load')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Years')

    # 6. TD mutants
    ax = axes[1, 2]
    for i, r in enumerate(results):
        ax.plot(r['t_years'], r['TD'], color=colors[i], linewidth=2,
                label=labels_short.get(r['label'], r['label']))
    ax.set_ylabel('TD mutant population')
    ax.set_title("5'-Terminal Deleted Mutants")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Years')

    fig.suptitle('Beta Cell Dynamics Quick Verification (24-month horizon)',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: {path}")
    return path


def plot_quick_mc(mc, filename="beta_cell_quick_mc.png"):
    """Compact MC results plot."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # 1. Final beta cell mass distribution
    ax = axes[0]
    ax.hist(mc['final_B'] * 100, bins=25, color='#2980b9', edgecolor='white', alpha=0.8)
    ax.axvline(x=30, color='red', linestyle='--', label='Insulin indep.')
    ax.axvline(x=np.median(mc['final_B']) * 100, color='orange', linewidth=2,
               label=f"Median: {np.median(mc['final_B'])*100:.1f}%")
    ax.set_xlabel('Final beta cell mass (% normal)')
    ax.set_ylabel('Count')
    ax.set_title(f'Final B Distribution (n={mc["n_samples"]})')
    ax.legend(fontsize=8)

    # 2. Spaghetti plot
    ax = axes[1]
    for traj in mc['trajectories_B'][:80]:
        t_weeks = np.arange(len(traj)) * 7 / 365.25
        ax.plot(t_weeks, traj * 100, color='#2980b9', alpha=0.08, linewidth=0.5)

    if mc['trajectories_B']:
        min_len = min(len(t) for t in mc['trajectories_B'][:80])
        trimmed = np.array([t[:min_len] for t in mc['trajectories_B'][:80]])
        median_traj = np.median(trimmed, axis=0)
        p5_traj = np.percentile(trimmed, 5, axis=0)
        p95_traj = np.percentile(trimmed, 95, axis=0)
        t_wk = np.arange(min_len) * 7 / 365.25
        ax.plot(t_wk, median_traj * 100, color='#e74c3c', linewidth=2, label='Median')
        ax.fill_between(t_wk, p5_traj * 100, p95_traj * 100, alpha=0.15, color='#2980b9',
                        label='5-95th pct')
    ax.axhline(y=30, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Years')
    ax.set_ylabel('Beta cell mass (% normal)')
    ax.set_title('Beta Cell Trajectories')
    ax.legend(fontsize=8)
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)

    # 3. Outcome pie
    ax = axes[2]
    outcomes = {
        'Insulin indep.': mc['independence_frac'],
        'C-peptide improved': max(mc['cp_improved_frac'] - mc['independence_frac'], 0),
        'No improvement': max(1.0 - mc['cp_improved_frac'], 0),
    }
    if sum(outcomes.values()) > 0:
        ax.pie(outcomes.values(), labels=outcomes.keys(),
               colors=['#27ae60', '#f39c12', '#c0392b'],
               autopct='%1.0f%%', startangle=90)
    ax.set_title(f'Outcomes at 1yr (n={mc["n_samples"]})')

    fig.suptitle('Quick Monte Carlo: 100 Patients x 1yr (Full Protocol)',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()

    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: {path}")
    return path


# =============================================================================
# MAIN
# =============================================================================

def main():
    t_start = time.time()

    print("=" * 72)
    print("BETA CELL DYNAMICS — QUICK VERIFICATION")
    print("Reduced MC (100 patients, 1yr) + 4 scenarios (24-month)")
    print("Target runtime: <60 seconds")
    print("=" * 72)

    # ---- Step 1: Run 4 base scenarios (24-month) ----
    print("\n--- STEP 1: Base scenarios (24-month horizon) ---")

    t1 = time.time()
    r_none = run_scenario_no_intervention(t_years=2.0)
    print(f"  No intervention:    B_final={r_none['final_B']*100:.2f}%  ({time.time()-t1:.1f}s)")

    t1 = time.time()
    r_p1 = run_scenario_phase1(t_years=2.0)
    print(f"  Phase 1 only:       B_final={r_p1['final_B']*100:.2f}%  ({time.time()-t1:.1f}s)")

    t1 = time.time()
    r_full = run_scenario_full(t_years=2.0)
    print(f"  Full protocol:      B_final={r_full['final_B']*100:.2f}%  ({time.time()-t1:.1f}s)")

    t1 = time.time()
    r_tepl = run_scenario_tepl(t_years=2.0)
    print(f"  Full + teplizumab:  B_final={r_tepl['final_B']*100:.2f}%  ({time.time()-t1:.1f}s)")

    all_results = [r_none, r_p1, r_full, r_tepl]

    # ---- Step 2: Extract and print key numbers ----
    print("\n--- STEP 2: Key numbers ---")

    all_milestones = {}
    for r in all_results:
        m = extract_key_numbers(r, r['label'])
        all_milestones[r['label']] = m

    print_key_numbers(all_milestones)

    # ---- Step 3: Generate comparison plots ----
    print("\n--- STEP 3: Comparison plots ---")
    fig_path = plot_quick_comparison(all_results)

    # ---- Step 4: Quick Monte Carlo ----
    print("\n--- STEP 4: Quick Monte Carlo (100 patients, 1yr) ---")
    t_mc = time.time()
    mc = quick_monte_carlo(n_samples=100, t_years=1.0, seed=42)
    mc_time = time.time() - t_mc
    print(f"  MC completed in {mc_time:.1f}s")

    print_mc_summary(mc)

    mc_fig = plot_quick_mc(mc)

    # ---- Step 5: Save JSON summary ----
    print("\n--- STEP 5: Save results ---")

    # Convert numpy types for JSON
    def to_serializable(obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (np.float64, np.float32)):
            return float(obj)
        if isinstance(obj, (np.int64, np.int32)):
            return int(obj)
        if isinstance(obj, np.bool_):
            return bool(obj)
        return obj

    summary = {
        "run_type": "quick_verification",
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "scenarios": {},
        "monte_carlo": {
            "n_samples": mc['n_samples'],
            "horizon_years": 1.0,
            "final_B_mean": to_serializable(np.mean(mc['final_B'])),
            "final_B_median": to_serializable(np.median(mc['final_B'])),
            "final_B_p5": to_serializable(np.percentile(mc['final_B'], 5)),
            "final_B_p95": to_serializable(np.percentile(mc['final_B'], 95)),
            "cp_improved_frac": to_serializable(mc['cp_improved_frac']),
            "b15_frac": to_serializable(mc['b15_frac']),
            "independence_frac": to_serializable(mc['independence_frac']),
            "remission_frac": to_serializable(mc['remission_frac']),
            "virus_cleared_frac": to_serializable(mc['virus_cleared_frac']),
        },
        "runtime_seconds": round(time.time() - t_start, 1),
    }

    for label, m in all_milestones.items():
        summary["scenarios"][label] = {k: to_serializable(v) for k, v in m.items()}

    json_path = os.path.join(RESULTS_DIR, "beta_cell_quick_results.json")
    with open(json_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"  JSON saved: {json_path}")

    # ---- Final report ----
    total_time = time.time() - t_start
    print(f"\n{'=' * 72}")
    print(f"QUICK VERIFICATION COMPLETE")
    print(f"  Total runtime: {total_time:.1f}s (target: <60s)")
    print(f"  4 scenarios: OK")
    print(f"  MC ({mc['n_samples']} patients): OK")
    print(f"  Figures: {fig_path}")
    print(f"           {mc_fig}")
    print(f"  JSON:    {json_path}")
    print(f"{'=' * 72}")

    return summary


if __name__ == "__main__":
    main()
