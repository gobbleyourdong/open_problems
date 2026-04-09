"""
continuity_quantification.py — Cycle 17
Numerical Track: what_is_self

From attempt_001: Parfit's claim is that psychological continuity (not strict
identity) is what matters. The numerical test:

Can a psychological continuity score predict "same person" intuitions in
thought experiments?

Dimensions of psychological continuity (from Parfit 1984):
  P1 — Memory: fraction of earlier memories carried forward
  P2 — Personality: cosine similarity of personality profiles
  P3 — Beliefs: cosine similarity of belief sets
  P4 — Desires: cosine similarity of desires/goals
  P5 — Bodily continuity: physical substrate continuity (0=none, 1=same)

Continuity score = weighted average (weights from Parfit's emphasis)
  Total = 0.25*P1 + 0.25*P2 + 0.2*P3 + 0.2*P4 + 0.1*P5

Test cases: classic personal identity thought experiments.
Ground truth: consensus verdict from philosophy of personal identity literature.
"""

import numpy as np
from scipy.stats import spearmanr

# Thought experiments: (name, P1, P2, P3, P4, P5, consensus_same_person, notes)
# consensus_same_person: 0=different person, 0.5=unclear/borderline, 1=same person
THOUGHT_EXPERIMENTS = [
    {
        "name": "Normal aging (30→80 years)",
        "P1": 0.7, "P2": 0.6, "P3": 0.6, "P4": 0.6, "P5": 0.8,
        "consensus": 1.0,
        "notes": "Clear case: same person despite change",
    },
    {
        "name": "Overnight sleep",
        "P1": 1.0, "P2": 1.0, "P3": 1.0, "P4": 1.0, "P5": 1.0,
        "consensus": 1.0,
        "notes": "Paradigm case of same person",
    },
    {
        "name": "General anesthesia",
        "P1": 0.95, "P2": 1.0, "P3": 1.0, "P4": 1.0, "P5": 1.0,
        "consensus": 1.0,
        "notes": "Consciousness gap but continuous person",
    },
    {
        "name": "Gradual cell replacement (normal biology)",
        "P1": 1.0, "P2": 1.0, "P3": 1.0, "P4": 1.0, "P5": 0.3,
        "consensus": 1.0,
        "notes": "Most cells replaced every 7-10 years; clearly same person",
    },
    {
        "name": "Severe amnesia (retrograde)",
        "P1": 0.0, "P2": 0.7, "P3": 0.4, "P4": 0.4, "P5": 1.0,
        "consensus": 0.6,  # legal/practical identity maintained but phenomenological gap
        "notes": "Physical continuity but memory lost; identity disputed",
    },
    {
        "name": "Teleportation (Parfit's case)",
        "P1": 1.0, "P2": 1.0, "P3": 1.0, "P4": 1.0, "P5": 0.0,
        "consensus": 0.5,  # Parfit: what matters is preserved; strict identity unclear
        "notes": "Perfect psychological continuity; original destroyed and recreated",
    },
    {
        "name": "Gradual neural replacement (neuron by neuron)",
        "P1": 0.9, "P2": 0.9, "P3": 0.9, "P4": 0.9, "P5": 0.5,
        "consensus": 0.7,
        "notes": "Ship of Theseus for neurons; most say same person",
    },
    {
        "name": "Brain in a vat (normal continuity, different body)",
        "P1": 1.0, "P2": 1.0, "P3": 1.0, "P4": 1.0, "P5": 0.1,
        "consensus": 0.9,
        "notes": "Most say same person if brain continues; body is incidental",
    },
    {
        "name": "Fission (brain split, each half in different body)",
        "P1": 0.9, "P2": 0.9, "P3": 0.9, "P4": 0.9, "P5": 0.5,
        "consensus": 0.3,  # each is like the original, neither IS the original
        "notes": "Parfit's hardest case: both successors have continuity",
    },
    {
        "name": "Radical personality change (religious conversion)",
        "P1": 0.8, "P2": 0.2, "P3": 0.3, "P4": 0.2, "P5": 1.0,
        "consensus": 0.8,  # still legally and socially the same person
        "notes": "Physical continuity preserved; personality radically changed",
    },
    {
        "name": "Advanced dementia",
        "P1": 0.0, "P2": 0.2, "P3": 0.1, "P4": 0.1, "P5": 1.0,
        "consensus": 0.5,  # legally same; psychologically nearly severed
        "notes": "Legal identity maintained; psychological continuity nearly broken",
    },
    {
        "name": "Hypothetical mindwipe (Star Trek style)",
        "P1": 0.0, "P2": 0.0, "P3": 0.0, "P4": 0.0, "P5": 0.8,
        "consensus": 0.1,  # most say different person
        "notes": "Complete psychological discontinuity; only body remains",
    },
    {
        "name": "Identical twin raised apart",
        "P1": 0.0, "P2": 0.4, "P3": 0.3, "P4": 0.3, "P5": 0.0,
        "consensus": 0.0,  # different people
        "notes": "Shared genetics but no psychological continuity = different person",
    },
]

WEIGHTS = {"P1": 0.25, "P2": 0.25, "P3": 0.20, "P4": 0.20, "P5": 0.10}


def run():
    print("=" * 72)
    print("PSYCHOLOGICAL CONTINUITY QUANTIFICATION — what_is_self Cycle 17")
    print("=" * 72)

    scores = []
    for exp in THOUGHT_EXPERIMENTS:
        score = sum(WEIGHTS[k] * exp[k] for k in WEIGHTS)
        exp["score"] = round(score, 3)
        scores.append(score)

    consensus = [e["consensus"] for e in THOUGHT_EXPERIMENTS]
    rho, p = spearmanr(scores, consensus)

    sorted_exp = sorted(THOUGHT_EXPERIMENTS, key=lambda x: -x["score"])
    print(f"\n  {'Experiment':<40} {'score':>6} {'consns':>7}")
    print("-" * 57)
    for e in sorted_exp:
        print(f"  {e['name'][:40]:<40} {e['score']:6.3f} {e['consensus']:7.2f}")

    print(f"\n  Spearman r(continuity_score, consensus_same) = {rho:+.3f}  p={p:.4f}  n={len(THOUGHT_EXPERIMENTS)}")

    # Group analysis
    import numpy as np
    high = [e["score"] for e in THOUGHT_EXPERIMENTS if e["consensus"] >= 0.8]
    mid  = [e["score"] for e in THOUGHT_EXPERIMENTS if 0.4 <= e["consensus"] < 0.8]
    low  = [e["score"] for e in THOUGHT_EXPERIMENTS if e["consensus"] < 0.4]

    print(f"\n  Mean continuity score by consensus group:")
    print(f"  Same person (consns≥0.8, n={len(high)}): {np.mean(high):.3f}")
    print(f"  Borderline  (0.4-0.8, n={len(mid)}):    {np.mean(mid):.3f}")
    print(f"  Diff person (consns<0.4, n={len(low)}):  {np.mean(low):.3f}")

    print(f"\n  The Parfit-Metzinger prediction: identity=what matters=continuity.")
    print(f"  If continuity score predicts 'same person' consensus: prediction confirmed.")


if __name__ == "__main__":
    run()
