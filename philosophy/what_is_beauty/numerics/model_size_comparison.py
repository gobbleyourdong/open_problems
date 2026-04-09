"""
model_size_comparison.py — Cycle 7
Numerical Track: what_is_beauty

Theory test: if CE4-aesthetics correlation is a genuine compression signal
(not just register prestige), then a richer prior (larger model) should
give BETTER within-register correlation. Specifically:
  - GPT-2-xl (1.5B) has richer priors than GPT-2-small (117M)
  - If the signal is "aesthetic texts are unusual under a rich prior," then
    larger model should rank them more aesthetically relative to their register

Two predictions:
  P1. Full correlation: GPT-2-xl r ≥ GPT-2-small r  (both register prestige + some signal)
  P2. Within-register: GPT-2-xl within-math r ≥ GPT-2-small within-math r
      And: within-literary partial r(xl) > partial r(small)  (more signal, less prestige)

Counter-hypothesis: the correlation is PURELY register prestige and larger model
doesn't change within-register signal (partial r stays ~0 regardless of model size).
"""

import math, json
from scipy.stats import spearmanr, pearsonr
import numpy as np


DATA = [
    ("Euler identity",           None, 9.5, "math"),
    ("Keats (truth/beauty)",     None, 9.0, "literary"),
    ("Dirac beauty quote",       None, 9.0, "literary"),
    ("Shakespeare (Sonnet 18)",  None, 8.5, "literary"),
    ("Cantor diagonal",          None, 8.5, "math"),
    ("Blake (Tyger)",            None, 8.5, "literary"),
    ("Donne (No man is island)", None, 8.5, "literary"),
    ("Pythagoras proof sketch",  None, 8.5, "math"),
    ("Euclid on Beauty bare",    None, 8.0, "literary"),
    ("Basho frog haiku",         None, 8.0, "literary"),
    ("Ramanujan infinite series",None, 8.0, "math"),
    ("Feynman (pleasure of find)",None,7.5, "literary"),
    ("Science journalism",       None, 5.0, "expository"),
    ("Wikipedia (Pythagoras)",   None, 4.0, "expository"),
    ("Encyclopedia definition",  None, 4.0, "expository"),
    ("Sports match report",      None, 3.5, "expository"),
    ("Weather forecast",         None, 3.0, "expository"),
    ("Lorem ipsum",              None, 2.5, "jargon"),
    ("Repetitive but wordy",     None, 2.0, "jargon"),
    ("Bureaucratic prose",       None, 1.5, "jargon"),
    ("Corporate mission stmt",   None, 1.5, "jargon"),
    ("Form letter",              None, 1.5, "jargon"),
    ("Repetitive text (aaaa)",   None, 1.0, "noise"),
    ("Comma-separated numbers",  None, 1.0, "noise"),
    ("Random ASCII",             None, 1.0, "noise"),
]

TEXTS = {
    "Euler identity":            "e^(i*pi) + 1 = 0. Five constants, one equation, zero mystery.",
    "Keats (truth/beauty)":      "Beauty is truth, truth beauty — that is all ye know on earth, and all ye need to know.",
    "Dirac beauty quote":        "It is more important to have beauty in one's equations than to have them fit experiment.",
    "Shakespeare (Sonnet 18)":   "Shall I compare thee to a summer's day? Thou art more lovely and more temperate.",
    "Cantor diagonal":           "Assume a bijection f: N -> R. Build x: x_n != f(n)_n for all n. Then x not in range(f). Contradiction. Therefore |R| > |N|.",
    "Blake (Tyger)":             "Tyger Tyger, burning bright, in the forests of the night; what immortal hand or eye could frame thy fearful symmetry?",
    "Donne (No man is island)":  "No man is an island entire of itself; every man is a piece of the continent, a part of the main.",
    "Pythagoras proof sketch":   "Draw squares on each side of a right triangle. The square on the hypotenuse equals the sum of the other two. The areas prove the theorem without algebra.",
    "Euclid on Beauty bare":     "Euclid alone has looked on Beauty bare. Let all who prate of Beauty hold their peace.",
    "Basho frog haiku":          "An old silent pond. A frog jumps into the pond. Splash! Silence again.",
    "Ramanujan infinite series": "1 + 2 + 3 + 4 + ... = -1/12. The zeta function at -1 assigns a finite value to a divergent sum.",
    "Feynman (pleasure of find)":"Physics is like sex: sure, it may give some practical results, but that is not why we do it.",
    "Science journalism":        "Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape once it crosses the event horizon.",
    "Wikipedia (Pythagoras)":    "The Pythagorean theorem states that the square of the hypotenuse of a right triangle equals the sum of the squares of the other two sides.",
    "Encyclopedia definition":   "Democracy is a system of government in which power is vested in the people, who rule either directly or through freely elected representatives.",
    "Sports match report":       "The home team won 3-1 after a dominant second half performance. Two goals from the striker and one from the midfielder secured the three points.",
    "Weather forecast":          "Partly cloudy skies with a chance of afternoon thunderstorms. Highs near 28 degrees. Winds from the southwest at 15 to 20 kilometres per hour.",
    "Lorem ipsum":               "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Repetitive but wordy":      "The cat sat on the mat. The mat was sat on by the cat. A cat was sitting on a mat. On the mat sat a cat.",
    "Bureaucratic prose":        "Pursuant to the provisions of the aforementioned regulation, the committee shall, not later than thirty (30) business days following the date hereof, convene a duly constituted meeting.",
    "Corporate mission stmt":    "We leverage synergistic core competencies to deliver best-in-class value-added solutions that empower our stakeholders to achieve transformative outcomes.",
    "Form letter":               "Dear valued customer, we have received your inquiry and will process it within 5-7 business days. Thank you for your patience.",
    "Repetitive text (aaaa)":    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "Comma-separated numbers":   "17, 4, 92, 3, 81, 56, 29, 74, 11, 63, 48, 35, 89, 2, 57, 44, 68, 13, 77, 31",
    "Random ASCII":              "q7!kRp#2mXv&9LnYw$sB^tFjQ@0dHcU%eAzOiGN",
}

REGISTERS = ["math", "literary", "expository", "jargon", "noise"]


def compute_nll(text, model, tok):
    import torch
    inputs = tok(text, return_tensors="pt")
    with torch.no_grad():
        out = model(**inputs, labels=inputs["input_ids"])
    return round(out.loss.item(), 4)


def partial_r(nll_vals, ratings, registers):
    reg_nll_mean = {}
    reg_rat_mean = {}
    for reg in REGISTERS:
        idxs = [i for i, r in enumerate(registers) if r == reg]
        if idxs:
            reg_nll_mean[reg] = sum(nll_vals[i] for i in idxs) / len(idxs)
            reg_rat_mean[reg] = sum(ratings[i] for i in idxs) / len(idxs)
    nll_resid = [nll_vals[i] - reg_nll_mean.get(registers[i], 0) for i in range(len(nll_vals))]
    rat_resid = [ratings[i] - reg_rat_mean.get(registers[i], 0) for i in range(len(ratings))]
    rho, p = spearmanr(nll_resid, rat_resid)
    return rho, p


def run():
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    models_to_test = [
        ("gpt2",    "GPT-2-small (117M)"),
        ("gpt2-xl", "GPT-2-xl (1.5B)"),
    ]

    labels   = [d[0] for d in DATA]
    ratings  = [d[2] for d in DATA]
    registers= [d[3] for d in DATA]
    texts    = [TEXTS[lbl] for lbl in labels]

    print("=" * 72)
    print("MODEL SIZE vs CORRELATION — what_is_beauty Cycle 7")
    print("=" * 72)

    all_nll = {}
    for model_name, model_label in models_to_test:
        print(f"\nComputing NLL with {model_label}...")
        tok   = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        nlls  = [compute_nll(t, model, tok) for t in texts]
        all_nll[model_name] = nlls

        rho_full, p_full = spearmanr(nlls, ratings)

        # Between-register
        reg_means = {}
        for reg in REGISTERS:
            idxs = [i for i,r in enumerate(registers) if r == reg]
            if idxs:
                reg_means[reg] = sum(nlls[i] for i in idxs) / len(idxs)
        reg_nll  = [reg_means[r] for r in REGISTERS]
        reg_rats = []
        for reg in REGISTERS:
            idxs = [i for i,r in enumerate(registers) if r == reg]
            if idxs:
                reg_rats.append(sum(ratings[i] for i in idxs) / len(idxs))
        rho_between, _ = spearmanr(reg_nll, reg_rats)

        # Partial (within-register)
        rho_partial, p_partial = partial_r(nlls, ratings, registers)

        # Within-math
        math_idxs = [i for i, r in enumerate(registers) if r == "math"]
        math_nlls = [nlls[i] for i in math_idxs]
        math_rats = [ratings[i] for i in math_idxs]
        rho_math, p_math = spearmanr(math_nlls, math_rats) if len(math_idxs) >= 3 else (float('nan'), 1)

        print(f"\n  {model_label}:")
        print(f"    Full r(NLL, rating):            {rho_full:+.3f}  p={p_full:.3f}")
        print(f"    Between-register r:             {rho_between:+.3f}")
        print(f"    Within-register partial r:      {rho_partial:+.3f}  p={p_partial:.3f}")
        print(f"    Within-math r (n={len(math_idxs)}):           {rho_math:+.3f}  p={p_math:.3f}")

    # Comparison: do larger models show more within-register signal?
    print("\n  NLL comparison (small vs xl), sorted by rating:")
    print(f"  {'Label':<35} {'rating':>6} {'nll_sm':>8} {'nll_xl':>8} {'diff':>7}")
    print("-" * 65)
    combined = sorted(zip(labels, ratings, registers, all_nll["gpt2"], all_nll["gpt2-xl"]),
                      key=lambda x: -x[1])
    for lbl, rat, reg, nll_sm, nll_xl in combined:
        diff = nll_xl - nll_sm
        print(f"  {lbl[:35]:<35} {rat:6.1f} {nll_sm:8.3f} {nll_xl:8.3f} {diff:+7.3f}")


if __name__ == "__main__":
    run()
