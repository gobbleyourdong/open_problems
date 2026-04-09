"""
correlation_analysis.py — Cycle 2
Numerical Track: what_is_beauty

Compute Spearman rank correlations between compression-efficiency metrics
(CE1-CE6, CE4 LM) and ground-truth aesthetic ratings.

Ground-truth ratings: consensus aesthetic quality from literature and citation
frequency, not a controlled human study. Rated 1-10 where:
  10 = universally cited as beautiful (Euler's identity in mathematics surveys)
   7 = widely recognised as aesthetically excellent
   4 = neutral/functional prose
   1 = aesthetically negative (bureaucratic, random, repetitive)

This is a PROXY ground truth — a proper study would use crowd-sourced ratings.
The point here is to check whether the metric ordering correlates with the
rough consensus ordering, not to claim experimental validity.

Usage:
    python correlation_analysis.py
"""

import json
from scipy.stats import spearmanr, kendalltau

# Ground-truth aesthetic ratings (consensus proxy, 1-10)
RATED_STIMULI = [
    {
        "label": "Euler identity",
        "text": "e^(i*pi) + 1 = 0. Five constants, one equation, zero mystery.",
        "rating": 9.5,   # Consistently ranked #1 in mathematical beauty surveys
        "source": "Wells 1988 survey; Zeki 2014 neuroaesthetics study",
    },
    {
        "label": "Keats (Ode on a Grecian Urn)",
        "text": (
            "Beauty is truth, truth beauty — that is all ye know on earth, "
            "and all ye need to know."
        ),
        "rating": 9.0,   # Canonical poetry; widely cited as pinnacle of Romantic verse
        "source": "Standard literary canon; poetic beauty surveys",
    },
    {
        "label": "Shakespeare Sonnet 18 opening",
        "text": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate.",
        "rating": 8.5,   # Among most recognised lines in English literature
        "source": "English poetry rankings; public surveys",
    },
    {
        "label": "Cantor diagonal",
        "text": (
            "Assume a bijection f: N -> R. Build x: x_n != f(n)_n for all n. "
            "Then x not in range(f). Contradiction. Therefore |R| > |N|."
        ),
        "rating": 8.5,   # Frequently cited as a beautiful proof; Proofs from THE BOOK
        "source": "Aigner & Ziegler 'Proofs from THE BOOK'",
    },
    {
        "label": "Euclid (beautiful, elegant)",
        "text": "Euclid alone has looked on Beauty bare. Let all who prate of Beauty hold their peace.",
        "rating": 8.0,   # Millay sonnet, famous meditation on mathematical beauty
        "source": "Millay 1923; literary canon",
    },
    {
        "label": "Basho haiku",
        "text": "An old silent pond. A frog jumps into the pond. Splash! Silence again.",
        "rating": 8.0,   # Most famous Japanese haiku; canonical aesthetic object
        "source": "Matsuo Basho c.1686; haiku canon",
    },
    {
        "label": "Wikipedia factual sentence",
        "text": (
            "The Pythagorean theorem states that the square of the hypotenuse of a "
            "right triangle equals the sum of the squares of the other two sides."
        ),
        "rating": 4.0,   # Informative, clear, not aesthetically distinguished
        "source": "Neutral informational prose (proxy)",
    },
    {
        "label": "Bureaucratic prose",
        "text": (
            "Pursuant to the provisions of the aforementioned regulation, the committee "
            "shall, not later than thirty (30) business days following the date hereof, "
            "convene a duly constituted meeting to assess the preliminary findings "
            "referenced in Exhibit A, subsection 4, paragraph 2(c)(iii)."
        ),
        "rating": 1.5,   # Aesthetically negative; intentionally ugly legalese
        "source": "Proxy: legalese antipattern",
    },
    {
        "label": "Repetitive text",
        "text": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "rating": 1.0,   # No aesthetic content
        "source": "Null stimulus",
    },
    {
        "label": "Random ASCII",
        "text": "q7!kRp#2mXv&9LnYw$sB^tFjQ@0dHcU%eAzOiGN",
        "rating": 1.0,   # No aesthetic content
        "source": "Null stimulus",
    },
]


def run_correlation():
    import sys
    sys.path.insert(0, "numerics")
    from compression_aesthetics import score

    results = []
    for s in RATED_STIMULI:
        r = score(s["text"], use_lm=True, lm_model="gpt2")
        r["label"] = s["label"]
        r["rating"] = s["rating"]
        results.append(r)

    ratings = [r["rating"] for r in results]

    metrics = {
        "CE1_zlib":      [1.0 - r["ce1_zlib_ratio"] for r in results],
        "CE2_char_H":    [1.0 - r["ce2_char_H_norm"] for r in results],
        "CE3_bigram":    [r["ce3_bigram_red"] for r in results],
        "CE5_word_H":    [1.0 - r["ce5_word_H_norm"] for r in results],
        "CE6_word_bgm":  [r["ce6_word_bigram_red"] for r in results],
        "CE4_LM_NLL":    [1.0 - r["ce4_lm_nll"] / 10.0 for r in results],
        "Composite_AB":  [
            (1.0 - r["ce1_zlib_ratio"] + 1.0 - r["ce2_char_H_norm"] +
             r["ce3_bigram_red"] + 1.0 - r["ce5_word_H_norm"] +
             r["ce6_word_bigram_red"]) / 5
            for r in results
        ],
        "Composite_ALL": [r["composite"] for r in results],
    }

    print("=" * 72)
    print("SPEARMAN CORRELATION — Compression Metrics vs. Aesthetic Ratings")
    print("n=10 stimuli; ratings = consensus proxy (not controlled human study)")
    print("=" * 72)
    print(f"\n  {'Metric':<20}  Spearman r  Kendall tau  p-value (Spearman)")
    print("-" * 72)

    for name, vals in metrics.items():
        rho, p = spearmanr(vals, ratings)
        tau, p_tau = kendalltau(vals, ratings)
        star = " *" if p < 0.05 else ("  " if p < 0.10 else "  ")
        print(f"  {name:<20}  {rho:+.3f}      {tau:+.3f}        {p:.3f}{star}")

    print()
    print("* p < 0.05")
    print()
    print("Ranked stimuli by CE4_LM_NLL (most predictable first):")
    print("-" * 72)
    ranked_lm = sorted(results, key=lambda x: x["ce4_lm_nll"])
    for r in ranked_lm:
        print(f"  lm_nll={r['ce4_lm_nll']:.2f}  rating={r['rating']:.1f}  {r['label']}")

    print()
    print("Ranked stimuli by human rating (best first):")
    print("-" * 72)
    ranked_hr = sorted(results, key=lambda x: -x["rating"])
    for r in ranked_hr:
        print(f"  rating={r['rating']:.1f}  lm_nll={r['ce4_lm_nll']:.2f}  {r['label']}")

    return results, metrics, ratings


if __name__ == "__main__":
    run_correlation()
