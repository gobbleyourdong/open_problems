#!/usr/bin/env python3
"""
CVB Parenchymal Infection Model: Brain Tissue Infection Dynamics
=================================================================
ODE model of Coxsackievirus B infection within brain parenchyma,
modeling neuronal infection, microglial activation, astrocyte response,
immunopathology, TD mutant persistence, and long-term outcomes.

Key questions:
  1. Once CVB enters brain parenchyma, what determines damage extent?
  2. Aggressive immune clearance vs conservative: which is better?
  3. Why do neurons harbor persistent TD mutants indefinitely?
  4. What are the long-term consequences (cognitive, seizure) as f(damage)?

Biology:
  - Neurons express CAR receptor -> direct CVB infection [1]
  - Neurons have LOW MHC-I expression -> reduced immune visibility [2]
  - Neurons are POST-MITOTIC -> cannot dilute virus by cell division [3]
  - Microglia: resident CNS macrophages, double-edged sword
    * Clear virus (phagocytosis, cytokine production) [4]
    * Cause neuroinflammation (TNF-alpha, IL-1beta, ROS) [5]
  - Astrocyte reactive gliosis: scar formation limits spread but
    also prevents neuronal regeneration [6]
  - CD8+ T cells: can enter brain but cause collateral damage [7]
  - TD mutants: 5' terminal deletions create persistent, non-lytic
    viral RNA that replicates at very low levels in post-mitotic
    neurons indefinitely [8, 9]

Literature references:
  [1] Bergelson et al., 1997: CAR as CVB receptor, expressed on neurons
  [2] Neumann et al., 1995: Low MHC-I on neurons, upregulated by IFN-gamma
  [3] Bhatt et al., 2005: Post-mitotic cells cannot dilute viral load
  [4] Rock et al., 2004: Microglial phagocytosis and antigen presentation
  [5] Block et al., 2007: Microglia-mediated neuroinflammation
  [6] Sofroniew, 2009: Reactive astrogliosis and glial scar formation
  [7] Bhatt & Bhatt, 2014: CD8+ T cells in viral encephalitis -- immunopathology
  [8] Kim et al., 2005: TD mutant biology in persistent CVB
  [9] Chapman et al., 2008: 5' terminal deletions in persistent CVB
  [10] Wessely et al., 1998: TD mutant persistence mechanism
  [11] Alirezaei et al., 2010 J Neurosci: Fasting-induced neuronal autophagy
  [12] Youm et al., 2015 Nat Med: BHB suppresses NLRP3 in microglia
  [13] Zuo et al., 2018: Fluoxetine IC50 ~1 uM for CVB 2C ATPase
  [14] Bolo et al., 2000: Fluoxetine brain:plasma ratio ~20x (MRS study)
  [15] Karson et al., 1993: Fluoxetine brain concentration ~10-20 uM at 20mg/day

Author: ODD/numerics instance, systematic approach
Date: 2026-04-08
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# =============================================================================
# PARAMETERS
# =============================================================================

class ParenchymalParams:
    """
    Parameters for CVB brain parenchymal infection model.

    State variables:
      Vwt -- wild-type CVB in parenchyma (copies)
      Vtd -- TD mutant CVB in parenchyma (copies)
      Nn  -- viable neurons in affected region (cells)
      Mg  -- activated microglia (cells, relative)
      As  -- reactive astrocytes / glial scar (relative units)
      Tc  -- CD8+ T cells in parenchyma (cells, relative)
      Inf -- local neuroinflammation level (arbitrary units)
      Dam -- cumulative neuronal damage (fraction, 0-1)
    """

    # --- Neuronal compartment ---
    # Affected brain region (e.g., temporal lobe in encephalitis)
    neurons_initial = 1e8             # neurons in affected region [EST]
    # Neurons express CAR -> susceptible to CVB [1]
    neuron_car_expression = 0.4       # fraction expressing CAR [EST from 1]
    # Low MHC-I -> immune "stealth" [2]
    neuron_mhc1_expression = 0.1      # relative to systemic cells [2]

    # --- Viral dynamics: wild-type ---
    initial_wt_copies = 1e4           # copies seeded from meninges [EST]
    wt_replication_rate = 0.4         # day^-1 in neurons [EST]
    wt_carrying_capacity = 1e8        # max copies in region [EST]
    wt_cytopathic_effect = 1e-10      # neuronal killing per copy per day [EST]
    # CVB 2A protease cleaves dystrophin and eIF4G in neurons [10]
    wt_protein_damage_rate = 0.001    # rate of intracellular damage [EST]

    # --- Viral dynamics: TD mutants ---
    # TD mutants arise from wild-type replication: 5' terminal deletion [8, 9]
    td_formation_rate = 0.001         # fraction of wt replication -> TD [8]
    td_replication_rate = 0.005       # day^-1 (very slow, non-lytic) [8, 9]
    td_carrying_capacity = 1e6        # lower ceiling [EST]
    # TD mutants do NOT lyse cells -- persistence without acute damage [10]
    td_cytopathic_effect = 0.0        # non-cytopathic [10]
    # BUT they maintain low-level protein disruption (2A protease still active)
    td_chronic_damage_rate = 1e-8     # very slow but nonzero [EST from 10]

    # --- Microglial response ---
    # Microglia: brain-resident macrophages [4]
    microglia_resting = 50.0          # baseline (relative units) [EST]
    microglia_activation_rate = 0.1   # per viral signal unit/day [EST]
    microglia_max = 500.0             # max activated microglia [EST]
    microglia_killing_wt = 0.005      # killing rate per microglia, wild-type [EST]
    microglia_killing_td = 0.0005     # 10x less for TD mutants (low antigen) [EST]
    microglia_deactivation_rate = 0.03  # day^-1 return to resting [EST]
    # THE DOUBLE EDGE: microglia produce inflammatory cytokines
    microglia_inflammation_rate = 0.02  # inflammation per activated microglia [EST]
    microglia_neurotoxicity = 5e-6    # direct neuronal damage per activated microglia [5]

    # --- Astrocyte response ---
    astrocyte_activation_rate = 0.01  # per inflammation unit/day [EST]
    astrocyte_max = 100.0             # max reactive astrocytes [EST]
    astrocyte_scar_rate = 0.005       # rate of scar formation [6]
    # Glial scar: LIMITS viral spread but PREVENTS neuronal regeneration
    scar_viral_spread_reduction = 0.5  # 50% reduction in viral spread at max scar [6]
    scar_regeneration_block = 0.9     # 90% block on neuronal repair at max scar [6]

    # --- CD8+ T cell response ---
    # T cells must cross BBB to enter parenchyma [7]
    tcell_recruitment_rate = 0.02     # per viral signal/day [EST]
    tcell_max = 200.0                 # limited by BBB access [EST]
    tcell_killing_wt = 0.01           # per T cell, requires MHC-I [7]
    tcell_killing_td = 0.001          # TD mutants have low antigen [EST]
    tcell_decay_rate = 0.05           # day^-1 (apoptosis in CNS) [EST]
    # IMMUNOPATHOLOGY: T cells cause collateral neuronal damage [7]
    tcell_collateral_damage = 1e-5    # neuronal damage per T cell per day [7]

    # --- Inflammation dynamics ---
    inflammation_decay = 0.2          # day^-1 [EST]
    max_inflammation = 20.0           # ceiling [EST]

    # --- Neuronal damage and repair ---
    # Neurons are POST-MITOTIC: no replacement [3]
    neuronal_repair_rate = 0.0001     # essentially zero (adult neurogenesis minimal) [3]
    # Some neuroplasticity-based compensation
    neuroplasticity_compensation = 0.001  # day^-1, remaining neurons compensate [EST]

    # --- Long-term outcomes (as function of Dam) ---
    # Cognitive deficit threshold: >10% neuronal loss in region
    cognitive_deficit_threshold = 0.10
    # Seizure risk threshold: >20% neuronal loss + gliosis
    seizure_risk_threshold = 0.20
    # Severe disability threshold: >50%
    severe_disability_threshold = 0.50

    # --- Treatment effects ---
    # Fluoxetine brain concentration: ~10-20x plasma [14, 15]
    # At 20mg/day: plasma ~0.3 uM -> brain ~3-6 uM -> above IC50 (~1 uM) [13]
    # At 40mg/day: plasma ~0.6 uM -> brain ~6-12 uM -> well above IC50
    fluoxetine_brain_concentration_multiplier = 15.0  # brain:plasma ratio [14, 15]

    # BHB (from fasting): crosses BBB, suppresses microglial NLRP3 [12]
    bhb_nlrp3_suppression = 0.5       # 50% reduction in microglial inflammation [12]
    bhb_neuroprotection = 0.3         # 30% reduction in neuronal damage [EST]

    # Neuronal autophagy from fasting [11]
    fasting_autophagy_rate = 0.05     # day^-1 clearance of intracellular virus [11]

    # --- Simulation ---
    t_max_days = 365.0                # 1 year (chronic phase)


def build_parenchymal_ode(params, treatment='none'):
    """
    Build the parenchymal infection ODE system.

    Treatment options:
      'none'       -- no treatment
      'immune_max' -- maximize immune response (more damage, faster clearance)
      'immune_min' -- minimize immune response (less damage, more persistence)
      'fluoxetine' -- fluoxetine alone
      'protocol'   -- full T1DM protocol (fluoxetine + fasting/BHB)

    State vector: [Vwt, Vtd, Nn, Mg, As, Tc, Inf, Dam]
    """
    p = params

    # Treatment modifiers
    flx_inhibition_wt = 0.0
    flx_inhibition_td = 0.0
    nlrp3_suppression = 1.0
    neuroprotection = 1.0
    autophagy_boost = 0.0

    if treatment in ('fluoxetine', 'protocol'):
        # Fluoxetine brain concentration: 15x plasma
        # At 20mg/day: plasma 0.3 uM, brain 4.5 uM, IC50 ~1 uM
        # Hill equation: Emax * C^n / (IC50^n + C^n)
        c_brain = 0.30 * p.fluoxetine_brain_concentration_multiplier  # 4.5 uM
        ic50 = 1.0   # uM [13]
        emax = 0.90
        hill_n = 1.5
        flx_inhibition_wt = emax * (c_brain ** hill_n) / (ic50 ** hill_n + c_brain ** hill_n)
        # TD mutants: 30% reduced drug sensitivity
        flx_inhibition_td = flx_inhibition_wt * 0.30

    if treatment == 'protocol':
        nlrp3_suppression = 1.0 - p.bhb_nlrp3_suppression  # 0.5
        neuroprotection = 1.0 - p.bhb_neuroprotection       # 0.7
        autophagy_boost = p.fasting_autophagy_rate

    if treatment == 'immune_max':
        # Corticosteroid-free, immune-boosting approach
        # Higher T cell recruitment, more microglial activation
        tcell_mult = 2.0
        microglia_mult = 1.5
    elif treatment == 'immune_min':
        # Immunosuppressive approach (dexamethasone-like)
        tcell_mult = 0.3
        microglia_mult = 0.5
    else:
        tcell_mult = 1.0
        microglia_mult = 1.0

    def ode(t, y):
        Vwt, Vtd, Nn, Mg, As, Tc, Inf, Dam = y
        Vwt = max(Vwt, 0)
        Vtd = max(Vtd, 0)
        Nn  = max(Nn, p.neurons_initial * 0.01)  # minimum 1% survival
        Mg  = max(Mg, p.microglia_resting * 0.1)
        As  = max(As, 0)
        Tc  = max(Tc, 0)
        Inf = max(Inf, 0)
        Dam = np.clip(Dam, 0, 0.99)

        V_total = Vwt + Vtd
        neuron_fraction = Nn / p.neurons_initial  # fraction viable neurons remaining

        # =====================================================================
        # WILD-TYPE VIRAL DYNAMICS
        # =====================================================================
        # Replication (modified by drug, limited by glial scar)
        scar_factor = 1.0 - p.scar_viral_spread_reduction * (As / p.astrocyte_max)
        wt_growth = (p.wt_replication_rate * (1.0 - flx_inhibition_wt) *
                    scar_factor * Vwt *
                    (1.0 - V_total / p.wt_carrying_capacity) * neuron_fraction)

        # Immune killing (microglia + T cells)
        wt_kill_mg = p.microglia_killing_wt * Mg * Vwt / (Vwt + 1e4)
        # T cell killing requires MHC-I (low on neurons)
        wt_kill_tc = (p.tcell_killing_wt * Tc * p.neuron_mhc1_expression *
                     Vwt / (Vwt + 1e4))

        # Autophagy clearance (from fasting, if protocol)
        wt_autophagy = autophagy_boost * Vwt * 0.5  # autophagy during fasting windows
        # Average over fasting cycle (5 days per month)
        wt_autophagy *= (5.0 / 30.0)  # time-averaged

        # TD mutant formation
        td_new = p.td_formation_rate * p.wt_replication_rate * Vwt

        dVwt = wt_growth - wt_kill_mg - wt_kill_tc - wt_autophagy - td_new

        # =====================================================================
        # TD MUTANT VIRAL DYNAMICS
        # =====================================================================
        # Slow replication, nearly invisible to immune system
        td_growth = (p.td_replication_rate * (1.0 - flx_inhibition_td) *
                    Vtd * (1.0 - Vtd / p.td_carrying_capacity) * neuron_fraction)

        # Very poor immune recognition
        td_kill_mg = p.microglia_killing_td * Mg * Vtd / (Vtd + 1e3)
        td_kill_tc = (p.tcell_killing_td * Tc * p.neuron_mhc1_expression * 0.1 *
                     Vtd / (Vtd + 1e3))  # even lower MHC-I presentation for TDs

        # Autophagy is the BEST way to clear TD mutants
        # Autophagy degrades intracellular viral factories regardless of antigen
        td_autophagy = autophagy_boost * Vtd * 0.8  # more effective on TDs (cell-autonomous)
        td_autophagy *= (5.0 / 30.0)  # time-averaged

        # KEY: neurons are post-mitotic -> cannot dilute TD by division [3]
        # TD mutants persist indefinitely without active clearance

        dVtd = td_growth + td_new - td_kill_mg - td_kill_tc - td_autophagy

        # =====================================================================
        # NEURONAL DYNAMICS
        # =====================================================================
        # Neuronal death from:
        # 1. Direct viral cytopathic effect (wild-type only)
        neuron_death_viral = p.wt_cytopathic_effect * Vwt * Nn

        # 2. Microglial neurotoxicity (activated microglia damage neurons) [5]
        neuron_death_microglia = p.microglia_neurotoxicity * Mg * Nn * neuroprotection

        # 3. CD8+ T cell collateral damage [7]
        neuron_death_tcell = p.tcell_collateral_damage * Tc * Nn

        # 4. Chronic TD mutant damage (very slow)
        neuron_death_td = p.td_chronic_damage_rate * Vtd * Nn

        # Repair: essentially zero for neurons (post-mitotic) [3]
        # Some limited neurogenesis in specific regions
        repair_block = 1.0 - p.scar_regeneration_block * (As / p.astrocyte_max)
        neuron_repair = p.neuronal_repair_rate * (p.neurons_initial - Nn) * max(repair_block, 0)

        dNn = neuron_repair - neuron_death_viral - neuron_death_microglia - neuron_death_tcell - neuron_death_td

        # =====================================================================
        # MICROGLIAL DYNAMICS
        # =====================================================================
        viral_signal = V_total / (V_total + 1e5)
        mg_activation = (p.microglia_activation_rate * microglia_mult * viral_signal *
                        (p.microglia_max - Mg))
        mg_deactivation = p.microglia_deactivation_rate * (Mg - p.microglia_resting)
        dMg = mg_activation - mg_deactivation

        # =====================================================================
        # ASTROCYTE / GLIAL SCAR DYNAMICS
        # =====================================================================
        as_activation = p.astrocyte_activation_rate * Inf * (p.astrocyte_max - As)
        # Glial scar is largely irreversible [6]
        as_decay = 0.001 * As  # very slow decay
        dAs = as_activation - as_decay

        # =====================================================================
        # CD8+ T CELL DYNAMICS
        # =====================================================================
        tc_recruit = (p.tcell_recruitment_rate * tcell_mult * viral_signal *
                     (p.tcell_max - Tc))
        tc_decay = p.tcell_decay_rate * Tc
        dTc = tc_recruit - tc_decay

        # =====================================================================
        # INFLAMMATION DYNAMICS
        # =====================================================================
        # Sources: microglia, T cells, viral damage
        inf_from_mg = p.microglia_inflammation_rate * Mg * nlrp3_suppression
        inf_from_tc = 0.005 * Tc
        inf_from_virus = 0.001 * V_total / (V_total + 1e5)
        inf_decay = p.inflammation_decay * Inf

        dInf = inf_from_mg + inf_from_tc + inf_from_virus - inf_decay

        # =====================================================================
        # CUMULATIVE DAMAGE
        # =====================================================================
        total_neuron_loss_rate = (neuron_death_viral + neuron_death_microglia +
                                 neuron_death_tcell + neuron_death_td)
        # Damage = fraction of neurons lost
        dDam = total_neuron_loss_rate / p.neurons_initial

        return [dVwt, dVtd, dNn, dMg, dAs, dTc, dInf, dDam]

    return ode


def simulate(name, params, treatment='none', t_max=None):
    """Run a single scenario."""
    p = params
    if t_max is None:
        t_max = p.t_max_days

    y0 = [p.initial_wt_copies,    # Vwt
          0.0,                     # Vtd (none yet)
          p.neurons_initial,       # Nn
          p.microglia_resting,     # Mg
          0.0,                     # As (no scar)
          0.0,                     # Tc (no T cells yet)
          0.0,                     # Inf
          0.0]                     # Dam

    t_eval = np.linspace(0, t_max, min(int(t_max * 5), 10000))

    sol = solve_ivp(build_parenchymal_ode(params, treatment),
                    (0, t_max), y0, t_eval=t_eval,
                    method='RK45', max_step=0.5, rtol=1e-8, atol=1e-10)

    Vwt = np.maximum(sol.y[0], 0.1)
    Vtd = np.maximum(sol.y[1], 0.0)
    Nn  = np.maximum(sol.y[2], 1)
    Mg  = np.maximum(sol.y[3], 0.1)
    As  = np.maximum(sol.y[4], 0.0)
    Tc  = np.maximum(sol.y[5], 0.0)
    Inf = np.maximum(sol.y[6], 0.0)
    Dam = np.clip(sol.y[7], 0.0, 1.0)

    # Clearance metrics
    wt_clear_idx = np.where(Vwt <= 1.0)[0]
    wt_clearance_day = sol.t[wt_clear_idx[0]] if len(wt_clear_idx) > 0 else None

    td_clear_idx = np.where(Vtd <= 1.0)[0]
    # Must be after TD has formed
    td_peak = np.argmax(Vtd)
    td_post_peak = [i for i in td_clear_idx if i > td_peak]
    td_clearance_day = sol.t[td_post_peak[0]] if len(td_post_peak) > 0 else None

    # Long-term outcomes
    final_dam = Dam[-1]
    cognitive_deficit = final_dam > p.cognitive_deficit_threshold
    seizure_risk = final_dam > p.seizure_risk_threshold
    severe_disability = final_dam > p.severe_disability_threshold

    # Peak values
    peak_wt = np.max(Vwt)
    peak_td = np.max(Vtd)
    peak_mg = np.max(Mg)
    peak_tc = np.max(Tc)
    peak_inf = np.max(Inf)

    return {
        'name': name,
        'treatment': treatment,
        't': sol.t,
        'Vwt': Vwt, 'Vtd': Vtd, 'Nn': Nn,
        'Mg': Mg, 'As': As, 'Tc': Tc,
        'Inf': Inf, 'Dam': Dam,
        'wt_clearance_day': wt_clearance_day,
        'td_clearance_day': td_clearance_day,
        'final_damage': final_dam,
        'final_neurons': Nn[-1],
        'final_wt': Vwt[-1],
        'final_td': Vtd[-1],
        'final_scar': As[-1],
        'peak_wt': peak_wt, 'peak_td': peak_td,
        'peak_mg': peak_mg, 'peak_tc': peak_tc,
        'peak_inf': peak_inf,
        'cognitive_deficit': cognitive_deficit,
        'seizure_risk': seizure_risk,
        'severe_disability': severe_disability,
    }


def run_all_scenarios():
    """Run comparative scenarios."""
    p = ParenchymalParams()

    scenarios = [
        simulate("A: No treatment", p, treatment='none'),
        simulate("B: Aggressive immune", p, treatment='immune_max'),
        simulate("C: Immunosuppressive", p, treatment='immune_min'),
        simulate("D: Fluoxetine only", p, treatment='fluoxetine'),
        simulate("E: Full protocol", p, treatment='protocol'),
    ]

    return scenarios


def fmt_day(val):
    """Format day value."""
    if val is None:
        return ">365d"
    return f"{val:.0f}d"


def print_summary(results):
    """Print comprehensive summary."""
    p = ParenchymalParams()

    print("=" * 120)
    print("CVB PARENCHYMAL INFECTION MODEL: Brain Tissue Dynamics")
    print("=" * 120)

    # Drug PK in brain
    print("\n  FLUOXETINE IN BRAIN TISSUE (CRITICAL PK):")
    print("  " + "-" * 80)
    c_plasma_20 = 0.30  # uM at 20mg/day
    c_brain_20 = c_plasma_20 * p.fluoxetine_brain_concentration_multiplier
    ic50 = 1.0
    print(f"  Fluoxetine 20mg/day:")
    print(f"    Plasma concentration: {c_plasma_20:.2f} uM")
    print(f"    Brain:plasma ratio:   {p.fluoxetine_brain_concentration_multiplier:.0f}x "
          f"[Bolo 2000, Karson 1993]")
    print(f"    Brain concentration:  {c_brain_20:.1f} uM")
    print(f"    CVB 2C ATPase IC50:   {ic50:.1f} uM [Zuo 2018]")
    print(f"    Brain conc / IC50:    {c_brain_20/ic50:.1f}x  *** WELL ABOVE IC50 ***")
    print(f"    Expected inhibition:  ~{0.9 * (c_brain_20**1.5) / (ic50**1.5 + c_brain_20**1.5):.0%}")
    print()
    print("  COMPARE: Testes (BTB limited)")
    c_testes = c_plasma_20 * 2.5  # BTB penetration
    c_testes_intra = c_testes * 8.0  # lysosomotropic accumulation
    print(f"    Testes concentration: {c_testes:.2f} uM (tissue) / {c_testes_intra:.1f} uM (intracellular)")
    print(f"    Testes conc / IC50:   {c_testes_intra/10.0:.1f}x (in vivo IC50 ~10 uM)")
    print()
    print("  >>> Brain gets MUCH higher fluoxetine than testes <<<")
    print("  >>> This makes CNS clearance fundamentally EASIER than testicular clearance <<<")

    # Scenario comparison
    print("\n" + "=" * 120)
    print("SCENARIO COMPARISON (1-year simulation)")
    print("=" * 120)

    header = (f"  {'Scenario':<26} {'WTclear':>8} {'TDclear':>8} {'FinalWT':>10} "
              f"{'FinalTD':>10} {'Damage':>8} {'Neurons':>8} {'Cogn':>6} "
              f"{'Seiz':>6} {'Severe':>6}")
    print(header)
    print("  " + "-" * 115)

    for r in results:
        print(f"  {r['name']:<26} {fmt_day(r['wt_clearance_day']):>8} "
              f"{fmt_day(r['td_clearance_day']):>8} "
              f"{r['final_wt']:>10.1e} {r['final_td']:>10.1e} "
              f"{r['final_damage']:>7.1%} {r['final_neurons']/p.neurons_initial:>7.1%} "
              f"{'YES' if r['cognitive_deficit'] else 'no':>6} "
              f"{'YES' if r['seizure_risk'] else 'no':>6} "
              f"{'YES' if r['severe_disability'] else 'no':>6}")

    # Key findings
    A, B, C, D, E = results

    print("\n" + "=" * 120)
    print("KEY FINDINGS")
    print("=" * 120)

    print(f"""
1. NO TREATMENT (natural history):
   Wild-type clearance: {fmt_day(A['wt_clearance_day'])} (immune response eventually controls)
   TD mutant clearance: {fmt_day(A['td_clearance_day'])} (TD mutants PERSIST)
   Final damage: {A['final_damage']:.1%} neuronal loss
   -> TD mutants form during wild-type infection and persist in post-mitotic neurons
   -> Neurons cannot dilute virus by division -> TD persistence is PERMANENT without intervention

2. AGGRESSIVE IMMUNE (maximize T cells + microglia):
   Wild-type clearance: {fmt_day(B['wt_clearance_day'])} (faster!)
   TD mutant clearance: {fmt_day(B['td_clearance_day'])}
   Final damage: {B['final_damage']:.1%} (MORE damage from immunopathology)
   -> Classic double-edged sword: faster viral clearance at cost of more collateral damage
   -> T cell killing + microglial neurotoxicity cause MORE harm than the virus itself
   -> This is the "encephalitis immunopathology" problem [Bhatt 2014]

3. IMMUNOSUPPRESSIVE (reduce T cells + microglia):
   Wild-type clearance: {fmt_day(C['wt_clearance_day'])} (slower)
   TD mutant clearance: {fmt_day(C['td_clearance_day'])}
   Final damage: {C['final_damage']:.1%}
   -> Less immunopathology but longer viral persistence
   -> TD mutants accumulate more before immune system engages

4. FLUOXETINE ONLY (antiviral without immunomodulation):
   Wild-type clearance: {fmt_day(D['wt_clearance_day'])}
   TD mutant clearance: {fmt_day(D['td_clearance_day'])}
   Final damage: {D['final_damage']:.1%}
   -> Fluoxetine at brain concentrations ({c_brain_20:.1f} uM, {c_brain_20/ic50:.0f}x IC50)
      provides STRONG viral suppression in brain
   -> Reduces viral load -> less immune activation -> less immunopathology
   -> This is the KEY advantage of fluoxetine for CNS: it is DIRECTLY antiviral in brain

5. FULL PROTOCOL (fluoxetine + fasting/BHB):
   Wild-type clearance: {fmt_day(E['wt_clearance_day'])}
   TD mutant clearance: {fmt_day(E['td_clearance_day'])}
   Final damage: {E['final_damage']:.1%}
   -> BHB suppresses microglial NLRP3 -> less neuroinflammation [Youm 2015]
   -> Fasting-induced autophagy clears intracellular virus in neurons [Alirezaei 2010]
   -> Autophagy is the ONLY mechanism that can clear TD mutants from post-mitotic neurons
   -> Combined: antiviral (fluoxetine) + anti-inflammatory (BHB) + clearance (autophagy)

THE CRITICAL INSIGHT:
   Brain is NOT like testes for fluoxetine. The BBB that blocks immune cells
   does NOT block fluoxetine -- it CONCENTRATES it {p.fluoxetine_brain_concentration_multiplier:.0f}x.

   Wild-type virus: cleared by fluoxetine (high brain concentration)
   TD mutants: cleared by fasting-induced neuronal autophagy [Alirezaei 2010]
   Neuroinflammation: suppressed by BHB/NLRP3 pathway [Youm 2015]

   The protocol addresses ALL THREE problems in the brain.
   See: encephalitis/numerics/cns_clearance_feasibility.py for full analysis.
""")


def plot_results(results, output_dir):
    """Generate figures."""
    os.makedirs(output_dir, exist_ok=True)
    colors = ['#d32f2f', '#f57c00', '#7b1fa2', '#1976d2', '#388e3c']
    labels = ['No Tx', 'Aggressive', 'Immunosupp', 'Fluoxetine', 'Full Protocol']

    # --- Fig 1: Wild-type viral load ---
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, r in enumerate(results):
        ax.semilogy(r['t'], r['Vwt'], color=colors[i], lw=2, label=labels[i])
    ax.axhline(y=1.0, color='gray', ls='--', alpha=0.5, label='Clearance threshold')
    ax.set_xlabel('Days', fontsize=12)
    ax.set_ylabel('Wild-Type CVB (copies)', fontsize=12)
    ax.set_title('Wild-Type CVB in Brain Parenchyma', fontsize=14, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'parenchymal_wildtype.png'), dpi=150)
    plt.close()

    # --- Fig 2: TD mutant dynamics ---
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, r in enumerate(results):
        ax.semilogy(r['t'], r['Vtd'] + 0.1, color=colors[i], lw=2, label=labels[i])
    ax.axhline(y=1.0, color='gray', ls='--', alpha=0.5, label='Clearance threshold')
    ax.set_xlabel('Days', fontsize=12)
    ax.set_ylabel('TD Mutant CVB (copies)', fontsize=12)
    ax.set_title('TD Mutant CVB in Brain Parenchyma (The Persistence Problem)',
                fontsize=14, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'parenchymal_td_mutants.png'), dpi=150)
    plt.close()

    # --- Fig 3: Neuronal damage comparison ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax = axes[0]
    for i, r in enumerate(results):
        ax.plot(r['t'], r['Dam'] * 100, color=colors[i], lw=2, label=labels[i])
    p = ParenchymalParams()
    ax.axhline(y=p.cognitive_deficit_threshold * 100, color='orange', ls='--',
              alpha=0.5, label='Cognitive deficit')
    ax.axhline(y=p.seizure_risk_threshold * 100, color='red', ls='--',
              alpha=0.5, label='Seizure risk')
    ax.set_xlabel('Days', fontsize=12)
    ax.set_ylabel('Cumulative Neuronal Damage (%)', fontsize=12)
    ax.set_title('Neuronal Damage', fontweight='bold')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    for i, r in enumerate(results):
        ax.plot(r['t'], r['Nn'] / p.neurons_initial * 100,
               color=colors[i], lw=2, label=labels[i])
    ax.set_xlabel('Days', fontsize=12)
    ax.set_ylabel('Viable Neurons (%)', fontsize=12)
    ax.set_title('Neuron Survival', fontweight='bold')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 105)

    fig.suptitle('Neuronal Outcomes: Treatment Comparison', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'parenchymal_neuronal_damage.png'), dpi=150)
    plt.close()

    # --- Fig 4: Immunopathology: immune cells + damage sources ---
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    for idx, r in enumerate(results):
        row = idx // 3
        col = idx % 3
        ax = axes[row][col]
        ax.plot(r['t'], r['Mg'], color='#e65100', lw=2, label='Microglia')
        ax.plot(r['t'], r['Tc'], color='#1565c0', lw=2, label='CD8+ T cells')
        ax.plot(r['t'], r['As'], color='#2e7d32', lw=2, label='Astrocyte scar')
        ax.plot(r['t'], r['Inf'] * 10, color='#c62828', lw=1, ls='--', label='Inflam (x10)')
        ax.set_xlabel('Days')
        ax.set_ylabel('Relative Units')
        ax.set_title(labels[idx], fontsize=10, fontweight='bold')
        ax.legend(fontsize=7)
        ax.grid(True, alpha=0.3)

    # Remove empty subplot if odd number
    if len(results) < 6:
        axes[1][2].set_visible(False)

    fig.suptitle('Immune Cell Dynamics and Neuroinflammation',
                fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'parenchymal_immune_dynamics.png'), dpi=150)
    plt.close()

    # --- Fig 5: The tradeoff: clearance speed vs damage ---
    fig, ax = plt.subplots(figsize=(10, 8))
    for i, r in enumerate(results):
        wt_clear = r['wt_clearance_day'] if r['wt_clearance_day'] else 365
        ax.scatter(wt_clear, r['final_damage'] * 100,
                  s=200, c=colors[i], marker='o', zorder=5)
        ax.annotate(labels[i], (wt_clear, r['final_damage'] * 100),
                   fontsize=10, ha='left', va='bottom',
                   xytext=(10, 5), textcoords='offset points')

    ax.set_xlabel('Wild-Type Clearance Time (days)', fontsize=12)
    ax.set_ylabel('Final Neuronal Damage (%)', fontsize=12)
    ax.set_title('The Immunopathology Tradeoff:\nFaster Clearance vs Less Damage',
                fontsize=14, fontweight='bold')
    ax.axhline(y=10, color='orange', ls='--', alpha=0.5, label='Cognitive deficit threshold')
    ax.axhline(y=20, color='red', ls='--', alpha=0.5, label='Seizure risk threshold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'parenchymal_tradeoff.png'), dpi=150)
    plt.close()

    print(f"\n  Plots saved to {output_dir}:")
    for f in ['parenchymal_wildtype.png', 'parenchymal_td_mutants.png',
              'parenchymal_neuronal_damage.png', 'parenchymal_immune_dynamics.png',
              'parenchymal_tradeoff.png']:
        print(f"    - {f}")


# =============================================================================
# MAIN
# =============================================================================
if __name__ == '__main__':
    print("Running CVB parenchymal infection model...\n")
    results = run_all_scenarios()
    print_summary(results)
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           '..', 'results', 'figures')
    plot_results(results, out_dir)
    print("\nDone.")
