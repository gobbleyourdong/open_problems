"""
expanded_stimuli.py — Cycle 4
Numerical Track: what_is_beauty

Expand the stimulus set from 10 to 25 texts spanning the full aesthetic range.
Compute CC + CE4 for each. Test whether optimised metric (tau=1.0, alpha=0.25)
generalises to the expanded set.

New stimuli added (15 new):
  High aesthetic (rating 8-10): more poetry, proofs, elegant scientific writing
  Mid range (rating 4-6):       engaging science writing, good journalism
  Low aesthetic (rating 1-3):   more legalese, bad prose, repetitive variations
"""

import json
import math

from scipy.stats import spearmanr


# ---------------------------------------------------------------------------
# All 25 stimuli with pre-assigned ratings and texts
# CC and CE4 will be computed on first run; cached here after first run
# ---------------------------------------------------------------------------

EXPANDED_STIMULI = [
    # === HIGH AESTHETIC (8-10) ===
    {"label": "Euler identity", "text": "e^(i*pi) + 1 = 0. Five constants, one equation, zero mystery.", "rating": 9.5},
    {"label": "Keats (truth/beauty)", "text": "Beauty is truth, truth beauty — that is all ye know on earth, and all ye need to know.", "rating": 9.0},
    {"label": "Shakespeare (Sonnet 18)", "text": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate.", "rating": 8.5},
    {"label": "Cantor diagonal", "text": "Assume a bijection f: N -> R. Build x: x_n != f(n)_n for all n. Then x not in range(f). Contradiction. Therefore |R| > |N|.", "rating": 8.5},
    {"label": "Euclid on Beauty bare", "text": "Euclid alone has looked on Beauty bare. Let all who prate of Beauty hold their peace.", "rating": 8.0},
    {"label": "Basho frog haiku", "text": "An old silent pond. A frog jumps into the pond. Splash! Silence again.", "rating": 8.0},
    # New high-aesthetic additions
    {"label": "Dirac beauty quote", "text": "It is more important to have beauty in one's equations than to have them fit experiment.", "rating": 9.0},
    {"label": "Pythagoras proof sketch", "text": "Draw squares on each side of a right triangle. The square on the hypotenuse equals the sum of the other two. The areas prove the theorem without algebra.", "rating": 8.5},
    {"label": "Donne (No man is an island)", "text": "No man is an island entire of itself; every man is a piece of the continent, a part of the main.", "rating": 8.5},
    {"label": "Feynman (pleasure of finding)", "text": "Physics is like sex: sure, it may give some practical results, but that's not why we do it.", "rating": 7.5},
    {"label": "Ramanujan infinite series", "text": "1 + 2 + 3 + 4 + ... = -1/12. The zeta function at -1 assigns a finite value to a divergent sum.", "rating": 8.0},
    {"label": "Blake (Tyger)", "text": "Tyger Tyger, burning bright, in the forests of the night; what immortal hand or eye could frame thy fearful symmetry?", "rating": 8.5},
    # === MID RANGE (4-6) ===
    {"label": "Wikipedia (Pythagoras)", "text": "The Pythagorean theorem states that the square of the hypotenuse of a right triangle equals the sum of the squares of the other two sides.", "rating": 4.0},
    # New mid-range additions
    {"label": "Science journalism (clear)", "text": "Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape once it crosses the event horizon.", "rating": 5.0},
    {"label": "Encyclopedia definition", "text": "Democracy is a system of government in which power is vested in the people, who rule either directly or through freely elected representatives.", "rating": 4.0},
    {"label": "Weather forecast", "text": "Partly cloudy skies with a chance of afternoon thunderstorms. Highs near 28 degrees. Winds from the southwest at 15 to 20 kilometres per hour.", "rating": 3.0},
    {"label": "Sports match report (plain)", "text": "The home team won 3-1 after a dominant second half performance. Two goals from the striker and one from the midfielder secured the three points.", "rating": 3.5},
    # === LOW AESTHETIC (1-3) ===
    {"label": "Bureaucratic prose", "text": "Pursuant to the provisions of the aforementioned regulation, the committee shall, not later than thirty (30) business days following the date hereof, convene a duly constituted meeting to assess the preliminary findings referenced in Exhibit A, subsection 4, paragraph 2(c)(iii).", "rating": 1.5},
    {"label": "Repetitive text", "text": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "rating": 1.0},
    {"label": "Random ASCII", "text": "q7!kRp#2mXv&9LnYw$sB^tFjQ@0dHcU%eAzOiGN", "rating": 1.0},
    # New low-aesthetic additions
    {"label": "Form letter (generic)", "text": "Dear valued customer, we have received your inquiry and will process it within 5-7 business days. Thank you for your patience and understanding in this matter.", "rating": 1.5},
    {"label": "Repetitive but wordy", "text": "The cat sat on the mat. The mat was sat on by the cat. A cat was sitting on a mat. On the mat sat a cat.", "rating": 2.0},
    {"label": "Corporate mission statement", "text": "We leverage synergistic core competencies to deliver best-in-class value-added solutions that empower our stakeholders to achieve transformative outcomes in a dynamic marketplace.", "rating": 1.5},
    {"label": "Lorem ipsum (Latin filler)", "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", "rating": 2.5},
    {"label": "Comma-separated noise", "text": "17, 4, 92, 3, 81, 56, 29, 74, 11, 63, 48, 35, 89, 2, 57, 44, 68, 13, 77, 31", "rating": 1.0},
]

# Pre-computed CC and CE4 values (from GPT-2) — first 10 from previous cycles
PRECOMPUTED = {
    "Euler identity":       {"cc": 0.184, "ce4": 5.04},
    "Keats (truth/beauty)": {"cc": 0.227, "ce4": 3.87},
    "Shakespeare (Sonnet 18)": {"cc": 0.301, "ce4": 3.68},
    "Cantor diagonal":      {"cc": 0.242, "ce4": 4.42},
    "Euclid on Beauty bare": {"cc": 0.164, "ce4": 6.21},
    "Basho frog haiku":     {"cc": 0.330, "ce4": 5.05},
    "Wikipedia (Pythagoras)": {"cc": 0.396, "ce4": 2.19},
    "Bureaucratic prose":   {"cc": 0.195, "ce4": 2.82},
    "Repetitive text":      {"cc": 0.682, "ce4": 1.34},
    "Random ASCII":         {"cc": 0.108, "ce4": 5.20},
}


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-max(-30.0, min(30.0, x))))


def combined(ce4, cc, tau=1.0, alpha=0.25):
    return (cc ** alpha) * sigmoid(ce4 - tau)


def compute_missing(model_name="gpt2"):
    """Compute CC and CE4 for stimuli not in PRECOMPUTED."""
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        tok = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
    except ImportError:
        return {}

    results = {}
    for s in EXPANDED_STIMULI:
        label = s["label"]
        if label in PRECOMPUTED:
            continue

        text = s["text"]
        # CE4: unconditional NLL
        try:
            inputs = tok(text, return_tensors="pt")
            with torch.no_grad():
                out = model(**inputs, labels=inputs["input_ids"])
            ce4 = round(out.loss.item(), 4)
        except Exception:
            ce4 = None

        # CC: contextual compression
        try:
            ids = tok.encode(text)
            if len(ids) < 4:
                cc = None
            else:
                split = max(1, len(ids) // 2)
                first, second = ids[:split], ids[split:]
                t_second = torch.tensor([second])
                with torch.no_grad():
                    nll_base = model(t_second, labels=t_second).loss.item()
                combined_t = torch.tensor([first + second])
                labels_t = torch.tensor([[-100] * len(first) + second])
                with torch.no_grad():
                    nll_ctx = model(combined_t, labels=labels_t).loss.item()
                cc = round(1.0 - nll_ctx / nll_base if nll_base > 0 else 0.0, 4)
        except Exception:
            cc = None

        results[label] = {"cc": cc, "ce4": ce4}
        print(f"  computed: {label[:50]}  cc={cc}  ce4={ce4}")

    return results


def run():
    print("=" * 72)
    print("EXPANDED STIMULI — what_is_beauty Cycle 4")
    print("n=25 stimuli, optimised metric (tau=1.0, alpha=0.25)")
    print("=" * 72)

    # Compute missing
    print("\nComputing CE4 + CC for new stimuli...")
    new_computed = compute_missing()

    # Merge
    all_data = {}
    all_data.update(PRECOMPUTED)
    all_data.update(new_computed)

    # Build full dataset
    full = []
    for s in EXPANDED_STIMULI:
        d = all_data.get(s["label"])
        if d and d.get("cc") is not None and d.get("ce4") is not None:
            full.append({
                "label": s["label"],
                "ce4": d["ce4"],
                "cc": d["cc"],
                "rating": s["rating"],
                "combined_opt": combined(d["ce4"], d["cc"], tau=1.0, alpha=0.25),
                "combined_orig": combined(d["ce4"], d["cc"], tau=3.0, alpha=1.0),
            })

    # Sort by combined_opt
    full.sort(key=lambda x: -x["combined_opt"])

    print(f"\n  n={len(full)} scored stimuli\n")
    print(f"  {'Label':<45} {'cc':>6} {'ce4':>6} {'comb_opt':>9} {'comb_orig':>10} {'rate':>5}")
    print("-" * 88)
    for r in full:
        print(
            f"  {r['label'][:45]:<45} {r['cc']:6.3f} {r['ce4']:6.2f} "
            f"{r['combined_opt']:9.3f} {r['combined_orig']:10.3f} {r['rating']:5.1f}"
        )

    if len(full) >= 10:
        ratings = [r["rating"] for r in full]
        opt   = [r["combined_opt"]  for r in full]
        orig  = [r["combined_orig"] for r in full]
        ce4   = [r["ce4"]           for r in full]
        cc    = [r["cc"]            for r in full]

        rho_opt,  p_opt  = spearmanr(opt,  ratings)
        rho_orig, p_orig = spearmanr(orig, ratings)
        rho_ce4,  p_ce4  = spearmanr(ce4,  ratings)
        rho_cc,   p_cc   = spearmanr(cc,   ratings)

        print(f"\n  Correlations (n={len(full)}):")
        print(f"  Optimised combined (tau=1.0, alpha=0.25): r={rho_opt:+.3f}  p={p_opt:.3f}")
        print(f"  Original combined  (tau=3.0, alpha=1.0):  r={rho_orig:+.3f}  p={p_orig:.3f}")
        print(f"  CE4 NLL alone:                            r={rho_ce4:+.3f}  p={p_ce4:.3f}")
        print(f"  CC alone:                                 r={rho_cc:+.3f}   p={p_cc:.3f}")

    return full


if __name__ == "__main__":
    results = run()
    print("\n" + json.dumps(results, indent=2))
