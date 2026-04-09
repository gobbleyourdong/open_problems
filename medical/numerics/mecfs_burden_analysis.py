#!/usr/bin/env python3
"""
ME/CFS Disease Burden Analysis — CVB Attribution & Protocol Cost-Effectiveness
===============================================================================
Computes total ME/CFS disease burden attributable to coxsackievirus B (CVB),
models % of cases potentially responsive to antiviral protocol, and compares
cost-effectiveness vs status quo (no treatment).

Data sources:
- Jason 2008 (PMID 18277320): economic burden
- Gow 1991, Bowles 1993, Clements 1995, Chia 2008: enteroviral prevalence
- Brenu 2011, Maher 2005: NK cell dysfunction
- IOM 2015, CDC: prevalence and demographics
- NCBI GEO: transcriptomic datasets (downloaded to numerics/transcriptomics/mecfs/)
"""

import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

# ── Output directory ────────────────────────────────────────────────────────
RESULTS_DIR = Path(__file__).parent.parent / 'results'
FIGURES_DIR = RESULTS_DIR / 'figures'
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# ── Epidemiological constants ────────────────────────────────────────────────
MECFS_US_CASES_LOW    = 836_000
MECFS_US_CASES_HIGH   = 2_500_000
MECFS_US_CASES_MID    = 1_500_000

MECFS_GLOBAL_LOW      = 17_000_000
MECFS_GLOBAL_HIGH     = 24_000_000
MECFS_GLOBAL_MID      = 20_500_000

# Enterovirus detection rates in ME/CFS (from biopsy studies)
EV_DETECTION_LOW      = 0.20   # Gow 1991
EV_DETECTION_MID      = 0.35   # Central estimate
EV_DETECTION_HIGH     = 0.53   # Clements 1995

# % of EV-positive patients caused specifically by CVB
CVB_FRACTION_LOW      = 0.40
CVB_FRACTION_MID      = 0.60   # CVB most common genus in persistent EV
CVB_FRACTION_HIGH     = 0.80

# Economic burden (US)
ANNUAL_BURDEN_LOW_B   = 17e9   # USD/year
ANNUAL_BURDEN_MID_B   = 20e9
ANNUAL_BURDEN_HIGH_B  = 24e9

# Per-patient annual cost
COST_PER_PATIENT_LOW  = 8_675
COST_PER_PATIENT_MID  = 11_000
COST_PER_PATIENT_HIGH = 14_458

# Protocol parameters
PROTOCOL_EFFICACY_LOW   = 0.30  # % improvement in responders (conservative)
PROTOCOL_EFFICACY_MID   = 0.55  # moderate estimate
PROTOCOL_EFFICACY_HIGH  = 0.75  # optimistic (based on EV clearance data)

PROTOCOL_ANNUAL_COST_USD = 2_400  # ~$200/month (antivirals + supplements)
PROTOCOL_DURATION_YEARS  = 2.0   # treatment duration

# QALY parameters
QALY_LOSS_PER_PATIENT_YEAR = 0.47  # from Brouwers 2021 EQ-5D data
ICER_THRESHOLD_USD         = 50_000  # willingness-to-pay per QALY (US threshold)


# ── 1. CVB-Attributable ME/CFS Burden ────────────────────────────────────────
def compute_cvb_attributable_burden():
    """
    Estimate cases and economic cost attributable to CVB specifically.
    Uses cascade: total ME/CFS → EV-positive fraction → CVB fraction
    """
    scenarios = {}

    for label, total, ev_rate, cvb_frac, annual_cost in [
        ('conservative', MECFS_US_CASES_LOW,  EV_DETECTION_LOW,  CVB_FRACTION_LOW,  ANNUAL_BURDEN_LOW_B),
        ('central',      MECFS_US_CASES_MID,  EV_DETECTION_MID,  CVB_FRACTION_MID,  ANNUAL_BURDEN_MID_B),
        ('optimistic',   MECFS_US_CASES_HIGH, EV_DETECTION_HIGH, CVB_FRACTION_HIGH, ANNUAL_BURDEN_HIGH_B),
    ]:
        ev_positive    = total * ev_rate
        cvb_cases      = ev_positive * cvb_frac
        burden_fraction = (ev_rate * cvb_frac)
        cvb_burden_usd = annual_cost * burden_fraction

        scenarios[label] = {
            'total_mecfs_us': total,
            'ev_positive_cases': round(ev_positive),
            'cvb_cases': round(cvb_cases),
            'ev_detection_rate': ev_rate,
            'cvb_fraction': cvb_frac,
            'burden_fraction': round(burden_fraction, 3),
            'cvb_burden_usd_annual': round(cvb_burden_usd, 0),
            'annual_cost_input': annual_cost,
        }

    return scenarios


# ── 2. Protocol Responsiveness Model ─────────────────────────────────────────
def model_protocol_responsiveness(cvb_scenarios):
    """
    Models what % of ME/CFS patients are potentially responsive to
    antiviral/immunomodulatory protocol targeting CVB persistence.

    Responsive criteria:
    - EV RNA-positive on biopsy (20-53% of ME/CFS)
    - OR elevated anti-EV antibodies (30-50%)
    - OR NK cell dysfunction + clinical EV features (proxy)

    We use CVB-attributable cases as the denominator for responsiveness.
    """
    results = {}

    for scenario, data in cvb_scenarios.items():
        total = data['total_mecfs_us']
        cvb_cases = data['cvb_cases']

        # Additional proxy: patients with both EV markers + NK dysfunction
        nk_dysfunction_rate = 0.50  # ~50% of ME/CFS have significant NK reduction
        dual_marker_rate = data['ev_detection_rate'] * 0.70  # 70% of EV+ also have NK dysfunction
        dual_marker_cases = round(total * dual_marker_rate)

        # Conservative responsive = CVB cases only
        # Liberal responsive = any EV-positive
        responsive_conservative = cvb_cases
        responsive_liberal = round(total * data['ev_detection_rate'])
        responsive_mid = round((cvb_cases + responsive_liberal) / 2)

        results[scenario] = {
            **data,
            'dual_marker_cases': dual_marker_cases,
            'responsive_conservative': responsive_conservative,
            'responsive_liberal': responsive_liberal,
            'responsive_mid': responsive_mid,
            'pct_responsive_conservative': round(responsive_conservative / total * 100, 1),
            'pct_responsive_liberal': round(responsive_liberal / total * 100, 1),
            'pct_responsive_mid': round(responsive_mid / total * 100, 1),
        }

    return results


# ── 3. Cost-Effectiveness Analysis ────────────────────────────────────────────
def compute_cost_effectiveness(responsiveness_data):
    """
    Incremental cost-effectiveness ratio (ICER) of protocol vs no treatment.

    Status quo: no effective treatment, full disease burden continues
    Protocol:   antiviral + immunomodulatory intervention over 2 years

    QALY gain = (efficacy × QALY_loss_per_year × treatment_years + sustained benefit years)
    """
    cea_results = {}

    for scenario, data in responsiveness_data.items():
        for efficacy, eff_label in [
            (PROTOCOL_EFFICACY_LOW, 'efficacy_low'),
            (PROTOCOL_EFFICACY_MID, 'efficacy_mid'),
            (PROTOCOL_EFFICACY_HIGH, 'efficacy_high'),
        ]:
            # Cost per patient
            total_protocol_cost = PROTOCOL_ANNUAL_COST_USD * PROTOCOL_DURATION_YEARS

            # QALY gained per patient
            # During treatment: partial improvement
            qaly_during = efficacy * QALY_LOSS_PER_PATIENT_YEAR * PROTOCOL_DURATION_YEARS
            # Sustained benefit after clearance (5-year horizon)
            sustained_years = 5.0 - PROTOCOL_DURATION_YEARS
            qaly_after = efficacy * 0.70 * QALY_LOSS_PER_PATIENT_YEAR * sustained_years  # 70% maintenance
            total_qaly_gained = qaly_during + qaly_after

            # ICER = incremental cost / incremental effectiveness
            # Cost comparator (no treatment): patient still incurs ~$11k/year in healthcare costs
            saved_medical_costs = efficacy * COST_PER_PATIENT_MID * PROTOCOL_DURATION_YEARS * 0.35
            net_incremental_cost = total_protocol_cost - saved_medical_costs

            icer = net_incremental_cost / total_qaly_gained if total_qaly_gained > 0 else float('inf')

            key = f"{scenario}_{eff_label}"
            cea_results[key] = {
                'scenario': scenario,
                'efficacy': efficacy,
                'protocol_cost_per_patient': total_protocol_cost,
                'qaly_gained_per_patient': round(total_qaly_gained, 3),
                'saved_medical_costs_per_patient': round(saved_medical_costs, 0),
                'net_incremental_cost': round(net_incremental_cost, 0),
                'icer_per_qaly': round(icer, 0),
                'cost_effective': icer < ICER_THRESHOLD_USD,

                # Population-level
                'responsive_patients': data['responsive_mid'],
                'population_qaly_gained': round(data['responsive_mid'] * total_qaly_gained),
                'population_cost': round(data['responsive_mid'] * total_protocol_cost),
                'population_savings': round(data['responsive_mid'] * saved_medical_costs),
                'net_population_cost': round(data['responsive_mid'] * net_incremental_cost),
            }

    return cea_results


# ── 4. Generate Figures ───────────────────────────────────────────────────────
def generate_figures(cvb_scenarios, responsiveness_data, cea_results):
    """Generate 4 publication-quality figures."""

    # ── Figure 1: CVB-Attributable Burden Cascade ──────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(14, 6))
    fig.suptitle('CVB-Attributable ME/CFS Burden (US)', fontsize=14, fontweight='bold')

    for idx, (scenario, data) in enumerate(cvb_scenarios.items()):
        ax = axes[idx]
        categories = ['Total\nME/CFS', 'EV-positive\ncases', 'CVB-specific\ncases']
        values = [data['total_mecfs_us'], data['ev_positive_cases'], data['cvb_cases']]
        colors = ['#3b82f6', '#f59e0b', '#ef4444']
        bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=0.7)
        ax.set_title(f'{scenario.capitalize()} estimate', fontsize=11)
        ax.set_ylabel('Patients (US)')
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))
        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.02,
                   f'{val:,.0f}', ha='center', va='bottom', fontsize=9)
        ax.set_ylim(0, max(values) * 1.2)

    plt.tight_layout()
    fig.savefig(FIGURES_DIR / 'fig1_cvb_burden_cascade.png', dpi=150, bbox_inches='tight')
    plt.close()

    # ── Figure 2: Protocol Responsiveness ──────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 6))
    scenarios = list(responsiveness_data.keys())
    x = np.arange(len(scenarios))
    width = 0.25

    pct_cons = [responsiveness_data[s]['pct_responsive_conservative'] for s in scenarios]
    pct_mid  = [responsiveness_data[s]['pct_responsive_mid'] for s in scenarios]
    pct_lib  = [responsiveness_data[s]['pct_responsive_liberal'] for s in scenarios]

    b1 = ax.bar(x - width, pct_cons, width, label='Conservative\n(CVB-specific)', color='#6366f1', alpha=0.85)
    b2 = ax.bar(x, pct_mid, width, label='Central estimate', color='#06b6d4', alpha=0.85)
    b3 = ax.bar(x + width, pct_lib, width, label='Liberal\n(all EV-positive)', color='#10b981', alpha=0.85)

    ax.set_xticks(x)
    ax.set_xticklabels([s.capitalize() for s in scenarios])
    ax.set_ylabel('% of ME/CFS patients potentially responsive to protocol')
    ax.set_title('Protocol Responsiveness — % ME/CFS Patients with CVB/EV Biomarkers', fontweight='bold')
    ax.legend(loc='upper left')
    ax.set_ylim(0, 65)
    ax.axhline(y=25, color='gray', linestyle='--', linewidth=1, label='25% threshold')
    for bars in [b1, b2, b3]:
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                   f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=8)
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / 'fig2_protocol_responsiveness.png', dpi=150, bbox_inches='tight')
    plt.close()

    # ── Figure 3: ICER by Efficacy and Scenario ────────────────────────────
    fig, ax = plt.subplots(figsize=(11, 6))
    eff_labels  = ['efficacy_low', 'efficacy_mid', 'efficacy_high']
    eff_pcts    = ['30%', '55%', '75%']
    scenario_colors = {'conservative': '#f87171', 'central': '#fb923c', 'optimistic': '#4ade80'}

    for sc in ['conservative', 'central', 'optimistic']:
        icers = []
        for eff_l in eff_labels:
            key = f"{sc}_{eff_l}"
            icers.append(cea_results[key]['icer_per_qaly'])
        ax.plot(eff_pcts, icers, 'o-', color=scenario_colors[sc],
                label=sc.capitalize(), linewidth=2, markersize=8)

    ax.axhline(y=ICER_THRESHOLD_USD, color='red', linestyle='--', linewidth=2,
               label=f'WTP threshold (${ICER_THRESHOLD_USD:,}/QALY)')
    ax.fill_between(eff_pcts, [0]*3, [ICER_THRESHOLD_USD]*3, alpha=0.05, color='green')
    ax.text(0.02, 0.12, 'Cost-effective region', transform=ax.transAxes,
            color='green', fontsize=10, alpha=0.7)

    ax.set_xlabel('Protocol Efficacy (% improvement in responders)')
    ax.set_ylabel('ICER ($/QALY gained)')
    ax.set_title('Cost-Effectiveness: CVB Protocol vs No Treatment\n(5-year horizon, US willingness-to-pay)', fontweight='bold')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
    ax.legend()
    ax.set_ylim(0, max(ICER_THRESHOLD_USD * 2.5, 120_000))
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / 'fig3_icer_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()

    # ── Figure 4: Population-Level Economic Impact ──────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(13, 6))
    fig.suptitle('Population-Level Economic Impact of CVB Protocol (Central Scenario)', fontweight='bold')

    # Left: QALY gains
    ax = axes[0]
    central_keys = [k for k in cea_results if k.startswith('central_')]
    eff_names = ['Low efficacy\n(30%)', 'Mid efficacy\n(55%)', 'High efficacy\n(75%)']
    qaly_vals = [cea_results[k]['population_qaly_gained'] for k in sorted(central_keys)]
    colors = ['#fbbf24', '#34d399', '#60a5fa']
    bars = ax.bar(eff_names, qaly_vals, color=colors, edgecolor='black', linewidth=0.7)
    ax.set_ylabel('QALYs Gained (population, 5-yr horizon)')
    ax.set_title('Total QALYs Gained\n(responsive patients, central scenario)')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x/1e3:.0f}k'))
    for bar, val in zip(bars, qaly_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.02,
               f'{val:,.0f}', ha='center', va='bottom', fontsize=9)

    # Right: Net costs vs savings
    ax = axes[1]
    costs = [cea_results[k]['population_cost'] for k in sorted(central_keys)]
    savings = [cea_results[k]['population_savings'] for k in sorted(central_keys)]
    net = [cea_results[k]['net_population_cost'] for k in sorted(central_keys)]
    x = np.arange(len(eff_names))
    width = 0.28
    ax.bar(x - width, [c/1e9 for c in costs], width, label='Protocol cost', color='#f87171', alpha=0.85, edgecolor='black', lw=0.7)
    ax.bar(x, [s/1e9 for s in savings], width, label='Medical cost savings', color='#4ade80', alpha=0.85, edgecolor='black', lw=0.7)
    ax.bar(x + width, [n/1e9 for n in net], width, label='Net cost', color='#60a5fa', alpha=0.85, edgecolor='black', lw=0.7)
    ax.set_xticks(x)
    ax.set_xticklabels(eff_names, fontsize=9)
    ax.set_ylabel('USD (billions)')
    ax.set_title('Population Cost–Savings\n(central scenario, 2-year treatment)')
    ax.legend(fontsize=9)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:.1f}B'))

    plt.tight_layout()
    fig.savefig(FIGURES_DIR / 'fig4_population_economic_impact.png', dpi=150, bbox_inches='tight')
    plt.close()

    print(f"Figures saved to: {FIGURES_DIR}")


# ── 5. Main ───────────────────────────────────────────────────────────────────
def main():
    print("=" * 70)
    print("ME/CFS CVB BURDEN ANALYSIS")
    print("=" * 70)

    # Compute burden
    cvb_scenarios = compute_cvb_attributable_burden()
    print("\n[1] CVB-Attributable ME/CFS Burden (US)")
    print(f"{'Scenario':<15} {'Total ME/CFS':>14} {'EV+':>12} {'CVB cases':>12} {'CVB burden $B/yr':>16}")
    print("-" * 70)
    for sc, d in cvb_scenarios.items():
        print(f"{sc:<15} {d['total_mecfs_us']:>14,} {d['ev_positive_cases']:>12,} "
              f"{d['cvb_cases']:>12,} ${d['cvb_burden_usd_annual']/1e9:>14.1f}B")

    # Responsiveness model
    resp_data = model_protocol_responsiveness(cvb_scenarios)
    print("\n[2] Protocol Responsiveness (% ME/CFS patients)")
    print(f"{'Scenario':<15} {'Responsive (cons)':>18} {'Responsive (mid)':>17} {'Responsive (lib)':>17}")
    print("-" * 70)
    for sc, d in resp_data.items():
        print(f"{sc:<15} {d['responsive_conservative']:>10,} ({d['pct_responsive_conservative']:4.1f}%)"
              f"  {d['responsive_mid']:>9,} ({d['pct_responsive_mid']:4.1f}%)"
              f"  {d['responsive_liberal']:>8,} ({d['pct_responsive_liberal']:4.1f}%)")

    # Cost-effectiveness
    cea = compute_cost_effectiveness(resp_data)
    print("\n[3] ICER Analysis ($ per QALY, 5-year horizon)")
    print(f"{'Key':<35} {'ICER':>10} {'Cost-effective?':>16}")
    print("-" * 65)
    for key in sorted(cea.keys()):
        d = cea[key]
        flag = "YES" if d['cost_effective'] else "no"
        print(f"{key:<35} ${d['icer_per_qaly']:>9,}  {flag:>15}")

    # Central + mid-efficacy summary
    c = cea['central_efficacy_mid']
    print("\n[4] Central Scenario, Mid-Efficacy (55%) Summary:")
    print(f"    Protocol cost per patient:     ${c['protocol_cost_per_patient']:,.0f}")
    print(f"    QALY gained per patient:       {c['qaly_gained_per_patient']:.2f}")
    print(f"    Medical cost savings:          ${c['saved_medical_costs_per_patient']:,.0f}")
    print(f"    ICER:                         ${c['icer_per_qaly']:,.0f}/QALY")
    print(f"    Cost-effective (<$50k/QALY):   {'YES' if c['cost_effective'] else 'NO'}")
    print(f"    Responsive patients (US):      {c['responsive_patients']:,}")
    print(f"    Population QALYs gained:       {c['population_qaly_gained']:,}")
    print(f"    Net population cost:           ${c['net_population_cost']:,.0f}")

    # Figures
    generate_figures(cvb_scenarios, resp_data, cea)

    # Save JSON results
    output = {
        'analysis_date': '2026-04-08',
        'model_version': '1.0',
        'cvb_burden_scenarios': cvb_scenarios,
        'protocol_responsiveness': resp_data,
        'cost_effectiveness': cea,
        'parameters': {
            'us_cases_range': [MECFS_US_CASES_LOW, MECFS_US_CASES_HIGH],
            'ev_detection_range': [EV_DETECTION_LOW, EV_DETECTION_HIGH],
            'cvb_fraction_range': [CVB_FRACTION_LOW, CVB_FRACTION_HIGH],
            'protocol_cost_per_year_usd': PROTOCOL_ANNUAL_COST_USD,
            'treatment_duration_years': PROTOCOL_DURATION_YEARS,
            'qaly_loss_per_patient_year': QALY_LOSS_PER_PATIENT_YEAR,
            'wtp_threshold_usd': ICER_THRESHOLD_USD,
            'sources': {
                'prevalence': 'CDC 2015; IOM 2015',
                'ev_detection': 'Gow 1991 PMID 1653789; Clements 1995 PMID 7836862; Chia 2008 PMID 17898445',
                'economic_burden': 'Jason 2008 PMID 18277320',
                'qaly': 'Brouwers 2021 EQ-5D',
                'nk_dysfunction': 'Brenu 2011 PMID 21199756',
            }
        }
    }

    out_path = RESULTS_DIR / 'mecfs_cvb_burden_analysis.json'
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nJSON saved: {out_path}")
    print("Done.")


if __name__ == '__main__':
    main()
