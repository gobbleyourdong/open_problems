"""
math_beauty_expanded.py — Cycle 8
Numerical Track: what_is_beauty

The within-math r=0.949 result (Cycle 5) was based on n=4 stimuli. Expand to
n=12 math stimuli spanning a range of aesthetic ratings to test whether the
result holds with more data.

Rating sources:
  - Wells 1988: mathematicians ranked theorems by beauty (1-10 scale)
  - Zeki et al. 2014: neuroaesthetics study of math beauty (brain activation)
  - Hardy 1940: "A Mathematician's Apology" — qualitative rankings
  - Survey of mathematicians (Rota 1997, "The Phenomenology of Mathematical Beauty")
  - Own assessment using the compression view as a guide
"""

import json
from scipy.stats import spearmanr, pearsonr
import numpy as np


MATH_STIMULI = [
    # ===  HIGH AESTHETIC (8-10) ===
    {
        "label": "Euler identity",
        "text": "e^(i*pi) + 1 = 0. Five constants, one equation, zero mystery.",
        "rating": 9.5,
        "source": "Wells 1988 #1; Zeki 2014 most beautiful"
    },
    {
        "label": "Euclid: infinitely many primes",
        "text": "Assume finitely many primes p1...pn. Let N = p1*p2*...*pn + 1. N is divisible by some prime not in the list. Contradiction.",
        "rating": 9.0,
        "source": "Hardy 1940; Aigner-Ziegler 'Proofs from THE BOOK'"
    },
    {
        "label": "Cantor diagonal argument",
        "text": "Assume a bijection f: N -> R. Build x: x_n != f(n)_n for all n. Then x not in range(f). Contradiction. Therefore |R| > |N|.",
        "rating": 8.5,
        "source": "Wells 1988 top-5; Proofs from THE BOOK"
    },
    {
        "label": "Pythagorean theorem (visual proof)",
        "text": "Draw four right triangles inside a square of side (a+b). The inner square has side c. Area: (a+b)^2 = 4*(ab/2) + c^2. Therefore a^2 + b^2 = c^2.",
        "rating": 8.5,
        "source": "Classic; visual proof most elegant"
    },
    {
        "label": "Fundamental theorem of calculus",
        "text": "If F'=f then the integral of f from a to b equals F(b) - F(a). Differentiation and integration are inverse operations.",
        "rating": 8.5,
        "source": "Mathematical canon; unifies two fundamental operations"
    },
    {
        "label": "Ramanujan 1+2+3+...=-1/12",
        "text": "1 + 2 + 3 + 4 + ... = -1/12. The zeta function at -1 assigns a finite value to a divergent sum.",
        "rating": 8.0,
        "source": "Surprising/provocative; Ramanujan's style"
    },
    # === MID AESTHETIC (5-7) ===
    {
        "label": "Pythagorean theorem (algebraic)",
        "text": "The Pythagorean theorem states that the square of the hypotenuse of a right triangle equals the sum of the squares of the other two sides.",
        "rating": 5.5,
        "source": "Informative but not elegant formulation"
    },
    {
        "label": "Binomial theorem",
        "text": "(a+b)^n = sum from k=0 to n of C(n,k)*a^(n-k)*b^k where C(n,k) = n!/(k!(n-k)!).",
        "rating": 6.0,
        "source": "Useful, moderately elegant"
    },
    {
        "label": "Definition of derivative",
        "text": "The derivative of f at x is the limit as h approaches 0 of (f(x+h)-f(x))/h, representing the instantaneous rate of change.",
        "rating": 5.0,
        "source": "Foundational but utilitarian definition"
    },
    # === LOW AESTHETIC (1-4) ===
    {
        "label": "Quadratic formula",
        "text": "The quadratic formula is x = (-b +/- sqrt(b^2 - 4ac)) / (2a). It gives the roots of any quadratic equation ax^2 + bx + c = 0.",
        "rating": 4.0,
        "source": "Useful but formulaic; most mathematicians rate it low"
    },
    {
        "label": "Long division algorithm",
        "text": "To divide 2847 by 13: 13 goes into 28 twice (26), remainder 2. Bring down 4 to get 24. 13 goes into 24 once (13), remainder 11. Bring down 7 to get 117. 13 goes into 117 nine times exactly. Answer: 219.",
        "rating": 2.0,
        "source": "Procedural; no aesthetic content"
    },
    {
        "label": "Trigonometric identities (rote list)",
        "text": "sin^2(x) + cos^2(x) = 1. tan(x) = sin(x)/cos(x). sin(a+b) = sin(a)cos(b) + cos(a)sin(b). cos(a+b) = cos(a)cos(b) - sin(a)sin(b).",
        "rating": 3.0,
        "source": "Necessary but aesthetically unmotivated rote list"
    },
]


def compute_ce4(text, model, tok):
    import torch
    inp = tok(text, return_tensors="pt")
    with torch.no_grad():
        out = model(**inp, labels=inp["input_ids"])
    return round(out.loss.item(), 4)


def run():
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    print("=" * 72)
    print("MATH BEAUTY EXPANDED — what_is_beauty Cycle 8")
    print(f"n={len(MATH_STIMULI)} math stimuli, testing within-math CE4 vs rating")
    print("=" * 72)

    tok   = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")

    results = []
    print(f"\n  {'Label':<45} {'NLL':>6} {'rating':>7}")
    print("-" * 60)
    for s in MATH_STIMULI:
        nll = compute_ce4(s["text"], model, tok)
        results.append({"label": s["label"], "nll": nll, "rating": s["rating"]})
        print(f"  {s['label'][:45]:<45} {nll:6.3f} {s['rating']:7.1f}")

    nlls    = [r["nll"]    for r in results]
    ratings = [r["rating"] for r in results]

    rho_full, p_full   = spearmanr(nlls, ratings)
    rho_pear, p_pear   = pearsonr(nlls, ratings)

    # Sort by NLL to show ranking
    ranked = sorted(results, key=lambda x: -x["nll"])
    print(f"\n  Ranked by NLL (most surprising first):")
    print(f"  {'rank':>4}  {'NLL':>6}  {'rating':>7}  label")
    for i, r in enumerate(ranked, 1):
        print(f"  {i:4d}  {r['nll']:6.3f}  {r['rating']:7.1f}  {r['label'][:50]}")

    print(f"\n  Correlations (n={len(results)}):")
    print(f"  Spearman r(NLL, rating) = {rho_full:+.3f}  p={p_full:.3f}")
    print(f"  Pearson  r(NLL, rating) = {rho_pear:+.3f}  p={p_pear:.3f}")

    # Compare to Cycle 5 result (n=4, r=0.949)
    n4_nlls    = [r["nll"]    for r in results if r["label"] in
                  ("Euler identity", "Cantor diagonal argument",
                   "Pythagorean theorem (visual proof)", "Ramanujan 1+2+3+...=-1/12")]
    n4_ratings = [r["rating"] for r in results if r["label"] in
                  ("Euler identity", "Cantor diagonal argument",
                   "Pythagorean theorem (visual proof)", "Ramanujan 1+2+3+...=-1/12")]
    if len(n4_nlls) >= 4:
        rho_n4, p_n4 = spearmanr(n4_nlls, n4_ratings)
        print(f"\n  n=4 subset (replication of Cycle 5): r={rho_n4:+.3f}  p={p_n4:.3f}")
        print(f"  (Cycle 5 reported: r=+0.949, p=0.051)")

    print(f"\n  Comparison: Cycle 5 (n=4) r=+0.949  →  Cycle 8 (n={len(results)}) r={rho_full:+.3f}")

    return results


if __name__ == "__main__":
    results = run()
    print(json.dumps(results, indent=2))
