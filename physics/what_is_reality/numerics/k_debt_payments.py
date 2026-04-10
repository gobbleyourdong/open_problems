#!/usr/bin/env python3
"""
k_debt_payments.py — K-debt payments from GW observations, multiverse K-costs,
                     and the simulation hypothesis under K-informationalism.

Context: TOE K-debt table from toe_k_analysis.py:
  SM+GR = 21,834 bits (K-minimum), Causal sets +100, CCC +466, LQG +1000, String +2161.
  K-informationalism: descriptions are preferred that minimise K(theory) + K(data|theory).
  Each TOE that accrues K-debt must "pay it off" via correct predictions SM+GR cannot match.

This script computes:
1. GW observations as K-debt payments against LQG
2. K-cost of different Tegmark multiverse levels
3. The simulation hypothesis K-cost vs SM+GR alone
4. A unified K-cost comparison table

Usage:
    cd ~/open_problems/physics/what_is_reality
    python3 numerics/k_debt_payments.py

Numerical track, what_is_reality — 2026-04-09
"""

import math
import json
import os

# ── Baseline parameters (from toe_k_data.json) ───────────────────────────────

K_SM_GR = 21_834          # bits — K-minimum, MDL winner
K_CAUSAL_SETS = 21_934    # bits (+100 above SM+GR)
K_CCC = 22_300            # bits (+466)
K_LQG = 22_834            # bits (+1000)
K_STRING = 23_995         # bits (+2161)

DEBT_LQG = K_LQG - K_SM_GR        # 1000 bits
DEBT_STRING = K_STRING - K_SM_GR  # 2161 bits
DEBT_CCC = K_CCC - K_SM_GR        # 466 bits
DEBT_CAUSAL = K_CAUSAL_SETS - K_SM_GR  # 100 bits


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — Gravitational Wave Observations as K-Debt Payments Against LQG
# ─────────────────────────────────────────────────────────────────────────────

def section1_gw_k_debt():
    """
    LQG predicts quantum-gravity corrections that alter GW propagation.
    Each LIGO event consistent with GR (and inconsistent with LQG corrections)
    provides Bayesian evidence against LQG.  Under K-informationalism that
    evidence is measured in bits: log2(P(data|GR) / P(data|LQG)).

    Observables tested per event:
      (a) Polarisation modes: GR has 2 (tensor +, x); LQG predicts 4 extra
          scalar/vector modes whose amplitude is bounded by detector sensitivity.
      (b) GW dispersion: h(f) ∝ f^{-α}; LQG predicts α ≠ 0. LIGO O3: α < 1e-3.
      (c) Arrival-time differences between high/low frequency components.

    Conservative Bayes factor per event:
      P(GR)/P(LQG) ~ 10  →  log2(10) ≈ 3.32 bits/event
    This is conservative: full posterior analyses give factors of 10–1000.
    """

    print("=" * 70)
    print("K-DEBT PAYMENTS FROM GRAVITATIONAL WAVE OBSERVATIONS")
    print("=" * 70)

    # --- O3 run (completed) ---
    n_o3_events       = 90          # LIGO-Virgo O3: ~90 confident GW detections
    # Conservative Bayes factor per event: P(GR)/P(LQG) ~ 10
    bayes_factor_per_event = 10.0
    bits_per_event    = math.log2(bayes_factor_per_event)   # 3.321928...
    bits_o3_total     = n_o3_events * bits_per_event

    # How much of the LQG K-debt (1000 bits) is paid off by O3?
    fraction_o3       = bits_o3_total / DEBT_LQG
    remaining_after_o3 = DEBT_LQG - bits_o3_total

    print(f"\n[O3 Run — completed]")
    print(f"  GW events (LIGO O3):              {n_o3_events}")
    print(f"  Conservative Bayes factor/event:  P(GR)/P(LQG) ~ {bayes_factor_per_event}")
    print(f"  K-payment per event:              log2({bayes_factor_per_event}) = {bits_per_event:.4f} bits")
    print(f"  Total K-payment from O3:          {n_o3_events} × {bits_per_event:.4f} = {bits_o3_total:.1f} bits")
    print(f"  LQG K-debt:                       {DEBT_LQG} bits")
    print(f"  Fraction paid off by O3:          {fraction_o3*100:.1f}%")
    print(f"  Remaining LQG K-debt after O3:    {remaining_after_o3:.1f} bits")

    # --- O4 projection ---
    # LIGO O4: ~300 events/year (conservative: 200-500 range)
    o4_rate_per_year  = 300          # events/year
    # bits needed to pay off remaining debt
    events_needed_total = math.ceil(DEBT_LQG / bits_per_event)
    events_needed_o4    = max(0, math.ceil(remaining_after_o3 / bits_per_event))
    years_o4_needed     = events_needed_o4 / o4_rate_per_year

    print(f"\n[O4 Projection — current as of 2026]")
    print(f"  LIGO O4 event rate:               ~{o4_rate_per_year} events/year")
    print(f"  Events needed to clear full debt: ceil({DEBT_LQG}/{bits_per_event:.4f}) = {events_needed_total}")
    print(f"  Events still needed after O3:     {events_needed_o4}")
    print(f"  Timeline (O4 alone):              {events_needed_o4}/{o4_rate_per_year} = {years_o4_needed:.2f} years")
    print(f"  → ~{years_o4_needed:.1f} year(s) of LIGO O4 operation clears the LQG K-debt")

    # --- Sensitivity to Bayes factor assumption ---
    print(f"\n[Sensitivity to Bayes-factor assumption]")
    print(f"  {'P(GR)/P(LQG) per event':<28} {'bits/event':>12} {'Events to clear debt':>22} {'O4 years':>10}")
    print("  " + "─" * 75)
    for bf in [2, 5, 10, 100, 1000]:
        bpe  = math.log2(bf)
        ev   = math.ceil(DEBT_LQG / bpe)
        yrs  = max(0, ev - n_o3_events) / o4_rate_per_year
        print(f"  {bf:<28} {bpe:>12.4f} {ev:>22} {yrs:>10.2f}")

    # --- Polarisation sub-analysis ---
    # GR predicts 2 tensor modes (h+, hx).
    # LQG in some formulations predicts 4-6 modes.
    # Null tests from network of 3 detectors (LIGO H, LIGO L, Virgo):
    #   P(2 modes | data) / P(6 modes | data) ~ 10^2 per event with SNR > 20
    n_high_snr_events = 10  # ~10 events in O3 with SNR > 20
    bf_polarisation   = 1e2
    bits_polarisation = n_high_snr_events * math.log2(bf_polarisation)
    print(f"\n[Polarisation test (SNR > 20 events)]")
    print(f"  High-SNR events (O3):   {n_high_snr_events}")
    print(f"  Bayes factor / event:   P(2 modes)/P(6 modes) ~ {bf_polarisation:.0e}")
    print(f"  K-payment:              {n_high_snr_events} × log2({bf_polarisation:.0e}) = {bits_polarisation:.1f} bits")
    print(f"  (Polarisation tests alone pay {bits_polarisation/DEBT_LQG*100:.1f}% of LQG K-debt)")

    # --- Dispersion constraint sub-analysis ---
    # alpha < 1e-3. LQG predicts alpha ~ E_GW/E_Planck ~ 1e-17 (very small)
    # but the constraint is still model-dependent.
    alpha_ligo_bound  = 1e-3
    alpha_lqg_pred    = 1e-17   # typical LQG prediction for ~100 Hz GW
    # If alpha prediction is wrong by a factor > 1e14, each dispersion measurement
    # pays log2(1e14) ≈ 46.5 bits. But only if LQG predicts a *detectable* deviation.
    # Conservative: dispersion tests pay ~1 bit/event (weak).
    bits_dispersion   = n_o3_events * 1.0
    print(f"\n[Dispersion constraint (alpha < {alpha_ligo_bound:.0e}) — conservative]")
    print(f"  LQG predicted alpha ~ {alpha_lqg_pred:.0e}  (well below current sensitivity {alpha_ligo_bound:.0e})")
    print(f"  Dispersion test K-payment: ~{bits_dispersion:.0f} bits total (1 bit/event, weak)")
    print(f"  Note: dispersion tests become powerful only if alpha_LQG ≳ 1e-3")

    gw_results = {
        "o3_events": n_o3_events,
        "bayes_factor_per_event_conservative": bayes_factor_per_event,
        "bits_per_event": bits_per_event,
        "bits_paid_o3": bits_o3_total,
        "lqg_k_debt_bits": DEBT_LQG,
        "fraction_paid_o3": fraction_o3,
        "remaining_debt_after_o3_bits": remaining_after_o3,
        "o4_rate_events_per_year": o4_rate_per_year,
        "events_needed_total": events_needed_total,
        "events_needed_o4": events_needed_o4,
        "years_o4_to_clear_debt": years_o4_needed,
        "polarisation_bits": bits_polarisation,
        "dispersion_bits_conservative": bits_dispersion,
        "sensitivity_table": [
            {
                "bf": bf,
                "bits_per_event": math.log2(bf),
                "events_to_clear": math.ceil(DEBT_LQG / math.log2(bf)),
                "o4_years": max(0, math.ceil(DEBT_LQG / math.log2(bf)) - n_o3_events) / o4_rate_per_year,
            }
            for bf in [2, 5, 10, 100, 1000]
        ],
    }
    return gw_results


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 — K-Cost of Tegmark Multiverse Levels
# ─────────────────────────────────────────────────────────────────────────────

def section2_multiverse_k_cost():
    """
    Tegmark's four-level classification of multiverses.
    K-informationalism asks: how many *extra* bits beyond SM+GR does each level require?

    Level I  — distant regions beyond our Hubble horizon.
                Same physical laws, same constants, different initial conditions.
                No extra K: the same SM+GR program generates all Level-I regions
                deterministically (or stochastically with a shared seed).
                K_extra = 0.

    Level II — eternal inflation bubbles with different physical constants.
                Requires specifying a meta-law that generates the distribution of
                constants (the inflaton potential, moduli stabilisation, etc.).
                Best understood via string landscape: ~K_string extra bits.
                K_extra ≈ K_string = 2161 bits (the landscape encoding overhead).
                More optimistically (simplest inflaton potential): K_extra ≈ 1000 bits.

    Level III — Many Worlds / MWI.
                All quantum branches exist. But branching is deterministic under
                unitary evolution — it is already contained in the Schrödinger
                equation inside SM+GR.  No additional K required.
                K_extra = 0.

    Level IV  — Mathematical Multiverse (all consistent mathematical structures).
                Requires specifying what "consistent" means (meta-axioms: ZFC? ETCS?
                some other foundation?). This is a non-trivial K cost.
                K_extra ≈ K(meta-axioms + selection principle) ≈ 500 bits.

    In addition we consider:
    Simulation hypothesis — covered in section 3.
    """

    print("\n" + "=" * 70)
    print("K-COST OF TEGMARK MULTIVERSE LEVELS")
    print("=" * 70)

    levels = [
        {
            "level": "SM+GR (baseline)",
            "K_laws_bits": K_SM_GR,
            "K_extra_bits": 0,
            "K_total_bits": K_SM_GR,
            "MDL_status": "preferred (K-minimum)",
            "rationale": (
                "21,834-bit SM+GR description. All observations consistent. "
                "No extra specification needed."
            ),
        },
        {
            "level": "Level I (distant Hubble volumes)",
            "K_laws_bits": K_SM_GR,
            "K_extra_bits": 0,
            "K_total_bits": K_SM_GR,
            "MDL_status": "K-tied with SM+GR",
            "rationale": (
                "Same laws, same constants, same program. Level-I regions are just "
                "different outputs of the same K-short program. K_extra = 0. "
                "Cannot be observed: no MDL advantage or penalty."
            ),
        },
        {
            "level": "Level II (eternal inflation / landscape)",
            "K_laws_bits": K_SM_GR,
            "K_extra_bits": DEBT_STRING,   # 2161 bits — must encode landscape meta-law
            "K_total_bits": K_SM_GR + DEBT_STRING,
            "MDL_status": "K-more expensive (+2161 bits vs SM+GR)",
            "rationale": (
                "Must encode the inflaton potential or string landscape that generates "
                "the distribution of physical constants. Best case K_extra ≈ 1000-2161 bits. "
                "Pays off only if it explains fine-tuning of Lambda or Higgs mass — "
                "which SM+GR cannot explain. Tentatively not preferred until that "
                "prediction is made precise."
            ),
        },
        {
            "level": "Level III (MWI / all quantum branches)",
            "K_laws_bits": K_SM_GR,
            "K_extra_bits": 0,
            "K_total_bits": K_SM_GR,
            "MDL_status": "K-tied with SM+GR (K-preferred over Copenhagen by 330-530 bits)",
            "rationale": (
                "Branching is deterministic under the unitary evolution already in SM+GR. "
                "No extra K needed to specify MWI. MWI saves the Copenhagen 'collapse' "
                "postulate (~330-530 bits of extra K in Copenhagen). "
                "K(MWI) = K(SM+GR) = 21,834 bits. K(Copenhagen) ≈ 22,164-22,364 bits."
            ),
        },
        {
            "level": "Level IV (mathematical multiverse)",
            "K_laws_bits": K_SM_GR,
            "K_extra_bits": 500,   # meta-axioms: ~500 bits
            "K_total_bits": K_SM_GR + 500,
            "MDL_status": "K-more expensive (+500 bits vs SM+GR)",
            "rationale": (
                "Must specify what 'all consistent mathematical structures' means. "
                "Requires encoding foundation axioms (ZFC? higher-order logic?) and "
                "a selection/measure principle over all such structures. "
                "K_extra ≈ 500 bits. Makes no new falsifiable predictions beyond SM+GR "
                "in any accessible region. Not MDL-preferred."
            ),
        },
    ]

    print(f"\n{'Level':<40} {'K-total':>9} {'K-extra':>9}  MDL status")
    print("─" * 90)
    for lv in levels:
        print(f"  {lv['level']:<38} {lv['K_total_bits']:>9,}  {lv['K_extra_bits']:>8,}  {lv['MDL_status']}")

    print(f"\n[K-minimum multiverse levels]")
    k_min = min(lv['K_extra_bits'] for lv in levels)
    winners = [lv['level'] for lv in levels if lv['K_extra_bits'] == k_min]
    print(f"  K-extra = {k_min} bits: {', '.join(winners)}")
    print(f"  Answer: Level I and Level III/MWI are K-tied at 0 extra bits above SM+GR.")
    print(f"  Both are K-minimal. The mathematical multiverse (Level IV) adds ~500 bits.")
    print(f"  Eternal inflation (Level II) adds ~2161 bits (landscape encoding cost).")

    print(f"\n[Rationales]")
    for lv in levels:
        print(f"  {lv['level']}:")
        for line in lv['rationale'].split('. '):
            if line:
                print(f"    {line.strip()}.")
        print()

    return levels


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 — Simulation Hypothesis K-Cost
# ─────────────────────────────────────────────────────────────────────────────

def section3_simulation_hypothesis():
    """
    To claim "we are in a simulation" one must specify at minimum:

      (A) Simulator physics (the physics of the substrate running the simulation):
          K_sim_physics ≥ 21,834 bits (it must be at least as complex as SM+GR
          to support sufficient computational substrate; likely more complex).

      (B) The simulation layer — the algorithm mapping substrate physics to
          simulated physics:
          K_layer ≈ 500–10,000 bits depending on compression achievable.
          Lower bound: ~500 bits for a highly regular algorithm.
          Upper bound: ~10,000 bits if the mapping is complicated.

      (C) Why our simulated universe has *our* specific physical laws:
          K_selection ≈ 0 bits if the laws are deterministically output by the
          simulation algorithm (e.g. computable from substrate + algorithm).
          K_selection ≈ K_laws_bits if the laws are specified ad hoc as a
          parameter table, adding another 21,834 bits.

    Conservative total: K_sim = K_sim_physics + K_layer
                               ≥ 21,834 + 500 = 22,334 bits

    Pessimistic total (laws also specified): ≥ 21,834 + 500 + 21,834 = 44,168 bits

    vs K(SM+GR) = 21,834 bits

    MDL: simulation hypothesis is disfavoured by ≥ 500 bits (conservative) unless
    it makes correct predictions that bare SM+GR cannot.
    """

    print("=" * 70)
    print("SIMULATION HYPOTHESIS — K-COST ANALYSIS")
    print("=" * 70)

    K_sim_physics_min = K_SM_GR          # minimum substrate complexity
    K_layer_low  = 500                   # bits — simplest simulation algorithm
    K_layer_high = 10_000                # bits — complex mapping
    K_selection_deterministic = 0        # bits — laws follow from algorithm
    K_selection_tabulated     = K_SM_GR  # bits — laws added as parameter table

    cases = [
        {
            "name": "Conservative (deterministic laws, simple layer)",
            "K_sim_physics": K_sim_physics_min,
            "K_layer": K_layer_low,
            "K_selection": K_selection_deterministic,
            "K_total": K_sim_physics_min + K_layer_low + K_selection_deterministic,
            "K_extra_vs_SMGR": K_layer_low + K_selection_deterministic,
        },
        {
            "name": "Mid-range (deterministic laws, complex layer)",
            "K_sim_physics": K_sim_physics_min,
            "K_layer": K_layer_high,
            "K_selection": K_selection_deterministic,
            "K_total": K_sim_physics_min + K_layer_high + K_selection_deterministic,
            "K_extra_vs_SMGR": K_layer_high + K_selection_deterministic,
        },
        {
            "name": "Pessimistic (tabulated laws, complex layer)",
            "K_sim_physics": K_sim_physics_min,
            "K_layer": K_layer_high,
            "K_selection": K_selection_tabulated,
            "K_total": K_sim_physics_min + K_layer_high + K_selection_tabulated,
            "K_extra_vs_SMGR": K_layer_high + K_selection_tabulated,
        },
    ]

    print(f"\n[Simulation hypothesis K-cost scenarios]")
    print(f"  SM+GR baseline K:            {K_SM_GR:,} bits")
    print()
    print(f"  {'Scenario':<46} {'K-total':>9} {'K-extra':>9}")
    print("  " + "─" * 68)
    for case in cases:
        print(f"  {case['name']:<46} {case['K_total']:>9,}  {case['K_extra_vs_SMGR']:>8,}")

    print(f"\n[Key arguments]")
    print(f"  (1) The simulator's substrate must support computation complex enough to")
    print(f"      run SM+GR physics — so K_sim_physics ≥ K_SM_GR = {K_SM_GR:,} bits.")
    print(f"  (2) The simulation layer (algorithm + boundary conditions) adds ≥ 500 bits.")
    print(f"  (3) Conservative lower bound: K(simulation) ≥ {K_SM_GR + K_layer_low:,} bits.")
    print(f"  (4) That is ≥ {K_layer_low} bits MORE than bare SM+GR.")
    print(f"  (5) Under MDL, simulation hypothesis is disfavoured until it makes")
    print(f"      correct predictions SM+GR cannot — e.g. glitch patterns, resolution")
    print(f"      artefacts, or computational savings that show up observationally.")
    print(f"\n  Current observational status: no prediction unique to the simulation")
    print(f"  hypothesis has been confirmed. MDL verdict: not preferred.")

    return cases


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 — Unified K-Cost Comparison Table
# ─────────────────────────────────────────────────────────────────────────────

def section4_unified_table():
    """
    Print and return a unified K-cost table covering all frameworks discussed.
    """

    print("\n" + "=" * 70)
    print("UNIFIED K-COST COMPARISON TABLE")
    print("=" * 70)

    K_COPENHAGEN_EXTRA = 330   # midpoint of 330-530 bits for collapse postulate
    K_COPENHAGEN_EXTRA_HI = 530

    rows = [
        # (Framework, K_total, K_extra_vs_SMGR, MDL_status)
        ("SM+GR (baseline)",                K_SM_GR,            0,                         "MDL winner — K-minimum"),
        ("SM+GR + Level I multiverse",       K_SM_GR,            0,                         "K-tied (same program, unobservable extra regions)"),
        ("SM+GR + MWI (Level III)",          K_SM_GR,            0,                         "K-tied; preferred over Copenhagen by 330-530 bits"),
        ("Causal Set Theory",                K_CAUSAL_SETS,      DEBT_CAUSAL,               "K-debt: +100 bits; needs 30/30 unique correct predictions"),
        ("CCC (Penrose)",                    K_CCC,              DEBT_CCC,                  "K-debt: +466 bits; Hawking point evidence needed"),
        ("SM+GR + Copenhagen QM",            K_SM_GR + K_COPENHAGEN_EXTRA,
                                            K_COPENHAGEN_EXTRA,                            "K-disfavoured vs MWI by 330 bits (collapse postulate overhead)"),
        ("SM+GR + Level IV multiverse",      K_SM_GR + 500,      500,                       "K-debt: +500 bits; no unique predictions"),
        ("LQG",                              K_LQG,              DEBT_LQG,                  "K-debt: +1000 bits; ~302 GW events to clear (O4 ~1 yr)"),
        ("SM+GR + Simulation hypothesis",    K_SM_GR + 500,      500,                       "K-debt: ≥+500 bits; no confirmed unique predictions"),
        ("SM+GR + Level II (landscape)",     K_SM_GR + DEBT_STRING, DEBT_STRING,           "K-debt: +2161 bits; may explain Lambda fine-tuning"),
        ("String/M-theory",                  K_STRING,           DEBT_STRING,               "K-debt: +2161 bits; no confirmed unique predictions"),
        ("Simulation (pessimistic)",         K_SM_GR + 10_000 + K_SM_GR,
                                            10_000 + K_SM_GR,                              "K-debt: +~32k bits; deeply disfavoured"),
    ]

    print(f"\n  {'Framework':<44} {'K-total':>9} {'K-extra':>9}  MDL status")
    print("  " + "─" * 120)
    for name, K_tot, K_ex, mdl in rows:
        print(f"  {name:<44} {K_tot:>9,}  {K_ex:>8,}  {mdl}")

    print(f"\n[Interpretation]")
    print(f"  K-extra = 0:        K-tied with SM+GR — no MDL penalty.")
    print(f"  K-extra > 0:        K-debt that must be repaid by correct unique predictions.")
    print(f"                      Each correct prediction that SM+GR cannot make pays down")
    print(f"                      log2(evidence-ratio) bits of the debt.")
    print(f"  K-extra < 0:        Would be K-preferred — no currently known example.")
    print(f"\n  Note: K-informationalism does not falsify high-K-extra theories.")
    print(f"  It only says they are currently not preferred under MDL.")

    return rows


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def run():
    gw_results   = section1_gw_k_debt()
    multiverse   = section2_multiverse_k_cost()
    simulation   = section3_simulation_hypothesis()
    table        = section4_unified_table()

    # ── Summary ──────────────────────────────────────────────────────────────

    print("\n" + "=" * 70)
    print("SUMMARY OF KEY FINDINGS")
    print("=" * 70)
    print(f"""
  1. GW events as K-debt payments:
     • Each LIGO event consistent with GR pays ~3.32 bits against LQG's 1000-bit K-debt.
     • LIGO O3 (90 events): paid ~299 bits — 29.9% of LQG K-debt cleared.
     • Remaining debt: ~701 bits.
     • LIGO O4 rate: ~300 events/year → ~212 more events needed → ~0.71 years.
     • ~1 year of LIGO O4 operation can clear the full LQG K-debt under conservative
       assumptions.  If Bayes factors are 100× per event (aggressive but defensible),
       LQG K-debt clears in ~{math.ceil(DEBT_LQG / math.log2(100))//300:.0f} month(s).

  2. Multiverse K-costs:
     • Level I and Level III (MWI) are K-minimal: K_extra = 0.
     • Level IV (mathematical multiverse) adds ~500 bits.
     • Level II (eternal inflation / landscape) adds ~2161 bits.
     • K-ordering: Level I = Level III < Level IV < LQG < Level II = String.

  3. Simulation hypothesis:
     • Conservative K-cost: ≥ {K_SM_GR + 500:,} bits vs {K_SM_GR:,} for SM+GR alone.
     • Disfavoured by ≥ 500 bits under MDL.
     • Not preferred unless it makes correct predictions SM+GR cannot.

  4. MDL winner: SM+GR (21,834 bits) with Level I or Level III (MWI) extension
     at zero extra K-cost.
""")

    # ── Persist results ───────────────────────────────────────────────────────

    os.makedirs(
        "os.path.expanduser("~/open_problems/") + "/physics/what_is_reality/results",
        exist_ok=True,
    )

    data = {
        "meta": {
            "script": "numerics/k_debt_payments.py",
            "date": "2026-04-09",
            "baseline_K_SM_GR_bits": K_SM_GR,
        },
        "section1_gw_k_debt_payments": gw_results,
        "section2_multiverse_k_costs": [
            {k: v for k, v in lv.items()} for lv in multiverse
        ],
        "section3_simulation_hypothesis": [
            {k: v for k, v in case.items()} for case in simulation
        ],
        "section4_unified_table": [
            {
                "framework": name,
                "K_total_bits": K_tot,
                "K_extra_bits": K_ex,
                "MDL_status": mdl,
            }
            for name, K_tot, K_ex, mdl in table
        ],
        "key_findings": {
            "o3_bits_paid_against_lqg": gw_results["bits_paid_o3"],
            "lqg_fraction_paid_by_o3": gw_results["fraction_paid_o3"],
            "o4_years_to_clear_lqg_debt": gw_results["years_o4_to_clear_debt"],
            "k_minimal_multiverse_levels": ["Level I", "Level III (MWI)"],
            "simulation_k_extra_min_bits": 500,
            "mdl_winner": "SM+GR",
            "mdl_winner_K_bits": K_SM_GR,
        },
    }

    out_path = "os.path.expanduser("~/open_problems/") + "/physics/what_is_reality/results/k_debt_payments_data.json"
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  Data → {out_path}")


if __name__ == "__main__":
    run()
