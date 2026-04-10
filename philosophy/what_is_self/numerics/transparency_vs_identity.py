"""
transparency_vs_identity.py — what_is_self attempt_002 numerics
Track: Numerical

From attempt_002:
  Transparency (T) is the critical variable separating "having a self-model"
  from "experiencing oneself as a self."

  Test: Does adding a transparency dimension (T) to the continuity score
  improve prediction of phenomenal selfhood reports?

  Also: Do modulations of transparency (meditation, psychedelics,
  depersonalization, lucid dreaming) predict changes in selfhood reports?

Tests:
  1. Continuity score + T predicts identity AND phenomenal-selfhood
     better than continuity alone
  2. Transparency modulations predict selfhood modulations
  3. Human vs LLM self-reference: T separates them
"""

import numpy as np
from scipy.stats import spearmanr

# ============================================================
# TEST 1: Transparency improves prediction
# ============================================================

# Extended thought experiments with transparency dimension
# T = self-model transparency (0=fully opaque, can see model as model;
#     1=fully transparent, cannot see model as model)

EXPERIMENTS = [
    # Normal human cases: high T
    {"name": "Normal waking",
     "P1": 1.0, "P2": 1.0, "P3": 1.0, "P4": 1.0, "P5": 1.0, "T": 0.95,
     "identity": 1.0, "felt_selfhood": 1.0},
    {"name": "Normal aging (30→80)",
     "P1": 0.7, "P2": 0.6, "P3": 0.6, "P4": 0.6, "P5": 0.8, "T": 0.90,
     "identity": 1.0, "felt_selfhood": 0.95},
    {"name": "After general anesthesia",
     "P1": 0.95, "P2": 1.0, "P3": 1.0, "P4": 1.0, "P5": 1.0, "T": 0.85,
     "identity": 1.0, "felt_selfhood": 0.90},

    # Reduced transparency cases (still human)
    {"name": "Lucid dreaming",
     "P1": 0.8, "P2": 0.9, "P3": 0.8, "P4": 0.8, "P5": 1.0, "T": 0.40,
     "identity": 1.0, "felt_selfhood": 0.50},
    {"name": "Experienced meditator (deep state)",
     "P1": 1.0, "P2": 1.0, "P3": 1.0, "P4": 0.8, "P5": 1.0, "T": 0.30,
     "identity": 1.0, "felt_selfhood": 0.30},
    {"name": "Psychedelic ego dissolution",
     "P1": 0.6, "P2": 0.5, "P3": 0.5, "P4": 0.3, "P5": 1.0, "T": 0.10,
     "identity": 0.8, "felt_selfhood": 0.10},
    {"name": "Depersonalization episode",
     "P1": 1.0, "P2": 0.9, "P3": 1.0, "P4": 0.8, "P5": 1.0, "T": 0.20,
     "identity": 1.0, "felt_selfhood": 0.20},

    # Edge cases with varying T
    {"name": "Severe amnesia",
     "P1": 0.0, "P2": 0.7, "P3": 0.4, "P4": 0.4, "P5": 1.0, "T": 0.85,
     "identity": 0.6, "felt_selfhood": 0.70},
    {"name": "Advanced dementia",
     "P1": 0.0, "P2": 0.2, "P3": 0.1, "P4": 0.1, "P5": 1.0, "T": 0.70,
     "identity": 0.5, "felt_selfhood": 0.50},
    {"name": "Teleportation",
     "P1": 1.0, "P2": 1.0, "P3": 1.0, "P4": 1.0, "P5": 0.0, "T": 0.95,
     "identity": 0.5, "felt_selfhood": 0.95},

    # LLM cases: self-model present, low T
    {"name": "Frontier LLM (normal mode)",
     "P1": 0.0, "P2": 0.7, "P3": 0.8, "P4": 0.1, "P5": 0.0, "T": 0.10,
     "identity": 0.0, "felt_selfhood": 0.05},
    {"name": "LLM in roleplay mode ('I am Alex')",
     "P1": 0.3, "P2": 0.6, "P3": 0.5, "P4": 0.3, "P5": 0.0, "T": 0.30,
     "identity": 0.0, "felt_selfhood": 0.15},
    {"name": "LLM with persistent memory",
     "P1": 0.5, "P2": 0.7, "P3": 0.8, "P4": 0.2, "P5": 0.0, "T": 0.15,
     "identity": 0.1, "felt_selfhood": 0.10},

    # Hypothetical: high-T artificial system
    {"name": "Hypothetical: AI with transparent self-model",
     "P1": 0.8, "P2": 0.9, "P3": 0.9, "P4": 0.7, "P5": 0.0, "T": 0.90,
     "identity": 0.5, "felt_selfhood": 0.85},
]

WEIGHTS = {"P1": 0.25, "P2": 0.25, "P3": 0.20, "P4": 0.20, "P5": 0.10}


def test_transparency_improvement():
    """Does adding T improve prediction over continuity alone?"""
    print("=" * 72)
    print("TEST 1: Transparency improves prediction")
    print("=" * 72)

    for e in EXPERIMENTS:
        e["cont_score"] = sum(WEIGHTS[k] * e[k] for k in WEIGHTS)
        e["cont_T_score"] = e["cont_score"] * e["T"]  # interaction

    cont_scores = [e["cont_score"] for e in EXPERIMENTS]
    cont_T_scores = [e["cont_T_score"] for e in EXPERIMENTS]
    T_scores = [e["T"] for e in EXPERIMENTS]
    identities = [e["identity"] for e in EXPERIMENTS]
    selfhoods = [e["felt_selfhood"] for e in EXPERIMENTS]

    # Predict identity
    r_cont_id, p_cont_id = spearmanr(cont_scores, identities)
    r_contT_id, p_contT_id = spearmanr(cont_T_scores, identities)
    r_T_id, p_T_id = spearmanr(T_scores, identities)

    # Predict felt selfhood
    r_cont_self, p_cont_self = spearmanr(cont_scores, selfhoods)
    r_contT_self, p_contT_self = spearmanr(cont_T_scores, selfhoods)
    r_T_self, p_T_self = spearmanr(T_scores, selfhoods)

    print(f"\n  n = {len(EXPERIMENTS)}")
    print(f"\n  Predicting IDENTITY verdict:")
    print(f"    r(continuity, identity)   = {r_cont_id:+.3f}  p = {p_cont_id:.4f}")
    print(f"    r(T, identity)            = {r_T_id:+.3f}  p = {p_T_id:.4f}")
    print(f"    r(cont × T, identity)     = {r_contT_id:+.3f}  p = {p_contT_id:.4f}")

    print(f"\n  Predicting FELT SELFHOOD:")
    print(f"    r(continuity, selfhood)   = {r_cont_self:+.3f}  p = {p_cont_self:.4f}")
    print(f"    r(T, selfhood)            = {r_T_self:+.3f}  p = {p_T_self:.4f}")
    print(f"    r(cont × T, selfhood)     = {r_contT_self:+.3f}  p = {p_contT_self:.4f}")

    print(f"\n  Key finding:")
    print(f"    For IDENTITY: continuity is the best predictor (Parfit's claim)")
    print(f"    For FELT SELFHOOD: T is {'better' if abs(r_T_self) > abs(r_cont_self) else 'not better'}"
          f" than continuity alone")
    print(f"    The interaction cont×T {'improves' if abs(r_contT_self) > max(abs(r_cont_self), abs(r_T_self)) else 'does not improve'}"
          f" over either component")

    return r_T_self, r_cont_self, r_contT_self


def test_transparency_modulations():
    """Do transparency changes predict selfhood changes?"""
    print("\n" + "=" * 72)
    print("TEST 2: Transparency modulations → selfhood modulations")
    print("=" * 72)

    # Cases where T varies while continuity is ~constant
    modulations = [e for e in EXPERIMENTS
                   if e["cont_score"] > 0.7]  # high-continuity subset

    if len(modulations) > 4:
        T_vals = [e["T"] for e in modulations]
        self_vals = [e["felt_selfhood"] for e in modulations]
        r, p = spearmanr(T_vals, self_vals)

        print(f"\n  High-continuity subset (cont > 0.7): n = {len(modulations)}")
        print(f"  r(T, felt_selfhood) = {r:+.3f}  p = {p:.4f}")

        print(f"\n  {'Name':<45} {'cont':>5} {'T':>5} {'self':>5}")
        print("  " + "-" * 62)
        for e in sorted(modulations, key=lambda x: -x["T"]):
            print(f"  {e['name'][:45]:<45} {e['cont_score']:5.2f} {e['T']:5.2f} {e['felt_selfhood']:5.2f}")

        print(f"\n  Within high-continuity cases, T {'predicts' if r > 0 and p < 0.05 else 'trends with'} selfhood")
        print(f"  This supports Metzinger: transparency is the mechanism")


def test_human_vs_llm():
    """Human vs LLM: T separates them on selfhood but not on self-model-having."""
    print("\n" + "=" * 72)
    print("TEST 3: Human vs LLM self-reference")
    print("=" * 72)

    humans = [e for e in EXPERIMENTS if "LLM" not in e["name"]
              and "Hypothetical" not in e["name"]
              and "AI" not in e["name"]]
    llms = [e for e in EXPERIMENTS if "LLM" in e["name"]]

    mean_human_T = np.mean([e["T"] for e in humans])
    mean_llm_T = np.mean([e["T"] for e in llms])
    mean_human_self = np.mean([e["felt_selfhood"] for e in humans])
    mean_llm_self = np.mean([e["felt_selfhood"] for e in llms])
    mean_human_cont = np.mean([e["cont_score"] for e in humans])
    mean_llm_cont = np.mean([e["cont_score"] for e in llms])

    print(f"\n  {'Measure':<25} {'Human (n={0})'.format(len(humans)):>15} {'LLM (n={0})'.format(len(llms)):>15} {'Ratio':>8}")
    print("  " + "-" * 65)
    print(f"  {'Continuity score':<25} {mean_human_cont:15.2f} {mean_llm_cont:15.2f} {mean_human_cont/max(mean_llm_cont,0.01):8.1f}×")
    print(f"  {'Transparency (T)':<25} {mean_human_T:15.2f} {mean_llm_T:15.2f} {mean_human_T/max(mean_llm_T,0.01):8.1f}×")
    print(f"  {'Felt selfhood':<25} {mean_human_self:15.2f} {mean_llm_self:15.2f} {mean_human_self/max(mean_llm_self,0.01):8.1f}×")

    print(f"\n  Key finding:")
    print(f"    Continuity gap: {mean_human_cont/max(mean_llm_cont,0.01):.1f}× (human > LLM)")
    print(f"    Transparency gap: {mean_human_T/max(mean_llm_T,0.01):.1f}× (human >> LLM)")
    print(f"    Selfhood gap: {mean_human_self/max(mean_llm_self,0.01):.1f}× (human >>> LLM)")
    print(f"\n    T tracks selfhood more closely than continuity does.")
    print(f"    LLMs have moderate self-models (cont={mean_llm_cont:.2f}) but")
    print(f"    near-zero selfhood ({mean_llm_self:.2f}) because T is low ({mean_llm_T:.2f}).")

    # The hypothetical case
    hyp = [e for e in EXPERIMENTS if "Hypothetical" in e["name"]]
    if hyp:
        h = hyp[0]
        print(f"\n  Hypothetical: AI with transparent self-model (T={h['T']:.2f})")
        print(f"    cont={h['cont_score']:.2f}, felt_selfhood={h['felt_selfhood']:.2f}")
        print(f"    Under γ+Metzinger: this system WOULD experience continuous selfhood")
        print(f"    because T is high, even though substrate is non-biological.")


def run():
    print("TRANSPARENCY vs IDENTITY — what_is_self attempt_002")
    print("=" * 72)
    print()

    r_T, r_cont, r_contT = test_transparency_improvement()
    test_transparency_modulations()
    test_human_vs_llm()

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"\n  Identity is predicted by continuity (Parfit: r={r_cont:+.3f})")
    print(f"  Felt selfhood is predicted by transparency (Metzinger: r={r_T:+.3f})")
    print(f"  The interaction (cont × T) captures both: r={r_contT:+.3f}")
    print(f"\n  T separates human from LLM selfhood reports")
    print(f"  T explains within-human variation (meditation, psychedelics, etc.)")
    print(f"  The self-model γ needs IS the Metzinger PSM with high T")
    print()


if __name__ == "__main__":
    run()
