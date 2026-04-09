"""
demarcation_compression.py — Cycle 17
Numerical Track: what_is_life

Test: can a compression-based life score correctly demarcate known edge cases?

The compression-life claim: life = persistent far-from-equilibrium compression
that produces copies of its own compressor.

Operationalised as 5 dimensions:
  C1 — Compression: does the system build compressed models of environment?
  C2 — Persistence: does it maintain a far-from-equilibrium state?
  C3 — Copying: does it produce copies of its compressor?
  C4 — Variation: do copies have heritable variation?
  C5 — Selection: do environmental pressures select among variants?

Score = mean(C1..C5), each rated 0-1.
The claim: score > 0.7 ↔ "clearly alive"; 0.4-0.7 = "edge case"; < 0.4 = "not alive"

Edge cases to test: viruses, prions, fire, crystals, computer viruses, RNA world,
autocatalytic sets, seeds, mules (sterile organisms), SARS-CoV-2.
"""

import numpy as np
from scipy.stats import spearmanr

# (name, C1_compress, C2_persist, C3_copy, C4_vary, C5_select, consensus_life_score, notes)
# consensus_life_score: expert consensus on whether this counts as life (0-1)
SYSTEMS = [
    {
        "name": "Bacterium (E. coli)",
        "C1": 0.9, "C2": 0.9, "C3": 1.0, "C4": 0.9, "C5": 1.0,
        "consensus": 1.0,
        "notes": "Paradigm case of life",
    },
    {
        "name": "Animal (mammal)",
        "C1": 1.0, "C2": 0.9, "C3": 0.9, "C4": 0.9, "C5": 1.0,
        "consensus": 1.0,
        "notes": "Paradigm case of life",
    },
    {
        "name": "Plant",
        "C1": 0.8, "C2": 0.9, "C3": 0.9, "C4": 0.9, "C5": 1.0,
        "consensus": 1.0,
        "notes": "Paradigm case",
    },
    {
        "name": "Virus (e.g. SARS-CoV-2)",
        "C1": 0.5, "C2": 0.1, "C3": 0.8, "C4": 0.9, "C5": 0.9,
        "consensus": 0.3,  # controversial — most biologists say not alive
        "notes": "No metabolism; needs host; but evolves",
    },
    {
        "name": "Prion (misfolded protein)",
        "C1": 0.0, "C2": 0.1, "C3": 0.5, "C4": 0.1, "C5": 0.1,
        "consensus": 0.0,
        "notes": "Self-propagating but no information storage or metabolism",
    },
    {
        "name": "Fire",
        "C1": 0.0, "C2": 0.6, "C3": 0.2, "C4": 0.0, "C5": 0.0,
        "consensus": 0.0,
        "notes": "Far-from-equilibrium but no information, no heritable variation",
    },
    {
        "name": "Crystal",
        "C1": 0.1, "C2": 0.3, "C3": 0.3, "C4": 0.1, "C5": 0.0,
        "consensus": 0.0,
        "notes": "Grows, nucleates, but no metabolism or information",
    },
    {
        "name": "Computer virus",
        "C1": 0.8, "C2": 0.3, "C3": 1.0, "C4": 0.6, "C5": 0.5,
        "consensus": 0.2,  # most say no (no metabolism, no physical far-from-eq)
        "notes": "Self-replicating, evolving, but not physical/chemical",
    },
    {
        "name": "RNA world (hypothetical)",
        "C1": 0.4, "C2": 0.5, "C3": 0.7, "C4": 0.8, "C5": 0.8,
        "consensus": 0.7,  # probably life in origin-of-life sense
        "notes": "Probably the origin of life; minimal metabolism",
    },
    {
        "name": "Seed (dormant)",
        "C1": 0.7, "C2": 0.2, "C3": 0.0, "C4": 0.8, "C5": 0.9,
        "consensus": 0.9,  # still classified as life even when dormant
        "notes": "Dormant life; potential for replication; classified as alive",
    },
    {
        "name": "Mule (sterile organism)",
        "C1": 0.9, "C2": 0.9, "C3": 0.0, "C4": 0.0, "C5": 0.9,
        "consensus": 1.0,  # alive despite sterility
        "notes": "Cannot reproduce but clearly alive; sterility is exception not rule",
    },
    {
        "name": "Autocatalytic chemical set",
        "C1": 0.3, "C2": 0.6, "C3": 0.6, "C4": 0.3, "C5": 0.4,
        "consensus": 0.4,
        "notes": "Catalyses its own formation; edge case for origin of life",
    },
    {
        "name": "Mitochondria (organelle)",
        "C1": 0.7, "C2": 0.8, "C3": 0.7, "C4": 0.5, "C5": 0.5,
        "consensus": 0.5,  # alive as part of cell; not independently alive
        "notes": "Reduced genome, only replicates within cell",
    },
    {
        "name": "Thermostat",
        "C1": 0.1, "C2": 0.0, "C3": 0.0, "C4": 0.0, "C5": 0.0,
        "consensus": 0.0,
        "notes": "Maintains temperature but no information copying, no compression",
    },
]


def run():
    print("=" * 72)
    print("DEMARCATION COMPRESSION TEST — what_is_life Cycle 17")
    print("Score = mean(C1_compress, C2_persist, C3_copy, C4_vary, C5_select)")
    print("=" * 72)

    scores = []
    for s in SYSTEMS:
        score = np.mean([s["C1"], s["C2"], s["C3"], s["C4"], s["C5"]])
        s["score"] = round(score, 3)
        scores.append(score)

    # Sort by score
    sorted_sys = sorted(SYSTEMS, key=lambda x: -x["score"])

    print(f"\n  {'System':<30} {'score':>6} {'C1':>4} {'C2':>4} {'C3':>4} {'C4':>4} {'C5':>4} {'consns':>7}")
    print("-" * 70)
    for s in sorted_sys:
        print(
            f"  {s['name'][:30]:<30} {s['score']:6.2f} "
            f"{s['C1']:4.1f} {s['C2']:4.1f} {s['C3']:4.1f} {s['C4']:4.1f} {s['C5']:4.1f} "
            f"{s['consensus']:7.1f}"
        )

    consensus = [s["consensus"] for s in SYSTEMS]
    rho, p = spearmanr(scores, consensus)
    print(f"\n  Spearman r(compression_score, consensus_alive) = {rho:+.3f}  p={p:.4f}  n={len(SYSTEMS)}")

    # Check demarcation thresholds
    correct_high  = sum(1 for s in SYSTEMS if s["score"] > 0.7 and s["consensus"] >= 0.8)
    correct_low   = sum(1 for s in SYSTEMS if s["score"] < 0.4 and s["consensus"] <= 0.2)
    n_high = sum(1 for s in SYSTEMS if s["score"] > 0.7)
    n_low  = sum(1 for s in SYSTEMS if s["score"] < 0.4)

    print(f"\n  Threshold accuracy:")
    print(f"  Score > 0.7 → 'alive': {correct_high}/{n_high} correctly classified")
    print(f"  Score < 0.4 → 'not alive': {correct_low}/{n_low} correctly classified")

    # Edge cases
    print(f"\n  Edge cases:")
    for s in sorted_sys:
        if 0.3 <= s["consensus"] <= 0.7 or (s["consensus"] != s["score"] > 0.5):
            print(f"  {s['name']:<30} score={s['score']:.2f}  consensus={s['consensus']:.1f}  {s['notes'][:45]}")


if __name__ == "__main__":
    run()
