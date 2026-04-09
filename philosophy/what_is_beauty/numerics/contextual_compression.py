"""
contextual_compression.py — Cycle 3
Numerical Track: what_is_beauty

Contextual compression score (CC):
  CC = 1 - NLL(second_half | first_half) / NLL(second_half | no_context)

Interpretation:
  CC near 1  → the first half almost completely predicts the second half
               (maximally internally coherent, repetitive, or structured)
  CC near 0  → context provides no help; text has no internal structure
  CC < 0     → context makes the second half HARDER to predict (incoherent)

The compression-beauty claim predicts: beautiful text has CC > boring/random text,
because aesthetic structure creates internal predictability (the poem's form
constrains later lines; the proof's beginning constrains its steps; the
haiku's first image constrains its resolution).

This is a MODEL-FREE contextual metric in the sense that it measures
self-compression rather than compression-under-prior. It is different from CE4:
  CE4 measures: is this text predictable under GPT-2's general prior?
  CC measures: does this text predict itself better than GPT-2's base rate?

The expected separation:
  Random ASCII:  CC ≈ 0  (no internal structure; context doesn't help)
  Repetitive:    CC ≈ 1  (first half perfectly predicts second half)
  Poetry:        CC > 0  (rhyme, metre, theme create cross-sentence prediction)
  Plain prose:   CC ≈ 0..0.2  (some lexical coherence but loose structure)
  Mathematical:  CC > 0  (proof steps constrain next steps)

This metric CORRECTLY handles the random ASCII problem: random ASCII has
CC ≈ 0 because knowing the first half of "q7!kRp#..." gives zero information
about the second half "eAzOiGN". Beautiful poetry has CC > 0 because its
internal structure is predictively rich.

The tradeoff: repetitive text (CC ≈ 1) is still an outlier. We handle this by
using CC in COMBINATION with CE4 (unconditional NLL): a text is aesthetically
interesting when CC > 0 AND CE4 is not trivially low (i.e., not pure repetition).
"""

import json
import math
import sys
from typing import Optional


def compute_contextual_compression(
    text: str,
    model_name: str = "gpt2",
    split_frac: float = 0.5,
) -> dict:
    """
    Compute the contextual compression score for a text.

    Splits text into first_half / second_half at split_frac of tokens.
    Computes:
      nll_base      = NLL(second_half)           — no context (prepend BOS only)
      nll_ctx       = NLL(second_half | first_half)
      CC            = 1 - nll_ctx / nll_base
      delta_nll     = nll_base - nll_ctx          — how many nats context saves

    Returns dict with all intermediate values and the CC score.
    Returns None values if transformers not available.
    """
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError:
        return {"cc": None, "nll_base": None, "nll_ctx": None, "delta_nll": None}

    try:
        tok = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)

        full_ids = tok.encode(text)
        if len(full_ids) < 4:
            return {"cc": None, "nll_base": None, "nll_ctx": None,
                    "delta_nll": None, "note": "too short"}

        split = max(1, int(len(full_ids) * split_frac))
        first_ids = full_ids[:split]
        second_ids = full_ids[split:]

        if len(second_ids) < 2:
            return {"cc": None, "nll_base": None, "nll_ctx": None,
                    "delta_nll": None, "note": "second half too short"}

        import torch

        # NLL of second half without context
        second_tensor = torch.tensor([second_ids])
        with torch.no_grad():
            out_base = model(second_tensor, labels=second_tensor)
        nll_base = out_base.loss.item()

        # NLL of second half WITH first half as context
        combined = torch.tensor([first_ids + second_ids])
        # labels: -100 (ignore) for first half, actual ids for second half
        labels = torch.tensor([[-100] * len(first_ids) + second_ids])
        with torch.no_grad():
            out_ctx = model(combined, labels=labels)
        nll_ctx = out_ctx.loss.item()

        cc = 1.0 - nll_ctx / nll_base if nll_base > 0 else 0.0
        delta = nll_base - nll_ctx

        return {
            "cc": round(cc, 4),
            "nll_base": round(nll_base, 4),
            "nll_ctx": round(nll_ctx, 4),
            "delta_nll": round(delta, 4),
            "n_tokens_first": len(first_ids),
            "n_tokens_second": len(second_ids),
        }
    except Exception as e:
        return {"cc": None, "nll_base": None, "nll_ctx": None,
                "delta_nll": None, "error": str(e)}


def combined_score(ce4_nll: float, cc: float) -> float:
    """
    Combined aesthetic score using CE4 (unconditional NLL) and CC.

    Logic:
    - CE4_nll: higher = less predictable = more unusual. Not a good predictor alone.
    - CC: higher = more internally coherent. Also not a good predictor alone.
    - Combined: high CC AND medium CE4_nll = aesthetically interesting
      (structured, but not trivially repetitive)

    Score = CC * (1 - exp(-CE4_nll / 3))
    The second factor rises from 0 at nll=0 (trivially predictable) toward 1
    at nll >> 3, penalising trivially predictable texts (repetitive) less than
    completely unpredictable ones (random).

    Actually: we want HIGH CE4_nll to be good (interesting) but not confounded
    with random noise. CC solves the random noise problem.

    Final: combined = CC * sigmoid(CE4_nll - 3)
    where sigmoid pushes below-3 nll (boring/repetitive) toward 0.
    """
    sigmoid = 1.0 / (1.0 + math.exp(-(ce4_nll - 3.0)))
    return round(cc * sigmoid, 4)


DEMO_STIMULI = [
    {"label": "Euler identity",
     "text": "e^(i*pi) + 1 = 0. Five constants, one equation, zero mystery.",
     "rating": 9.5},
    {"label": "Keats",
     "text": "Beauty is truth, truth beauty — that is all ye know on earth, and all ye need to know.",
     "rating": 9.0},
    {"label": "Shakespeare",
     "text": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate.",
     "rating": 8.5},
    {"label": "Cantor diagonal",
     "text": ("Assume a bijection f: N -> R. Build x: x_n != f(n)_n for all n. "
              "Then x not in range(f). Contradiction. Therefore |R| > |N|."),
     "rating": 8.5},
    {"label": "Euclid",
     "text": "Euclid alone has looked on Beauty bare. Let all who prate of Beauty hold their peace.",
     "rating": 8.0},
    {"label": "Basho haiku",
     "text": "An old silent pond. A frog jumps into the pond. Splash! Silence again.",
     "rating": 8.0},
    {"label": "Wikipedia",
     "text": ("The Pythagorean theorem states that the square of the hypotenuse of a "
              "right triangle equals the sum of the squares of the other two sides."),
     "rating": 4.0},
    {"label": "Bureaucratic prose",
     "text": ("Pursuant to the provisions of the aforementioned regulation, the committee "
              "shall, not later than thirty (30) business days following the date hereof, "
              "convene a duly constituted meeting to assess the preliminary findings "
              "referenced in Exhibit A, subsection 4, paragraph 2(c)(iii)."),
     "rating": 1.5},
    {"label": "Repetitive text",
     "text": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
     "rating": 1.0},
    {"label": "Random ASCII",
     "text": "q7!kRp#2mXv&9LnYw$sB^tFjQ@0dHcU%eAzOiGN",
     "rating": 1.0},
]

# CE4 NLL values from Cycle 2
CE4_NLL = {
    "Euler identity": 5.04,
    "Keats": 3.87,
    "Shakespeare": 3.68,
    "Cantor diagonal": 4.42,
    "Euclid": 6.21,
    "Basho haiku": 5.05,
    "Wikipedia": 2.19,
    "Bureaucratic prose": 2.82,
    "Repetitive text": 1.34,
    "Random ASCII": 5.20,
}


def run_demo():
    from scipy.stats import spearmanr

    print("=" * 72)
    print("CONTEXTUAL COMPRESSION — what_is_beauty Cycle 3")
    print("=" * 72)

    results = []
    for s in DEMO_STIMULI:
        r = compute_contextual_compression(s["text"])
        r["label"] = s["label"]
        r["rating"] = s["rating"]
        r["ce4_nll"] = CE4_NLL.get(s["label"], None)
        if r["cc"] is not None and r["ce4_nll"] is not None:
            r["combined"] = combined_score(r["ce4_nll"], r["cc"])
        else:
            r["combined"] = None
        results.append(r)

    print(f"\n  {'Label':<25} {'CC':>6} {'NLL_base':>8} {'NLL_ctx':>8} {'delta':>6} {'CE4':>6} {'comb':>6} {'rate':>5}")
    print("-" * 80)
    for r in results:
        cc_s = f"{r['cc']:6.3f}" if r["cc"] is not None else "  None"
        nb_s = f"{r['nll_base']:8.3f}" if r["nll_base"] is not None else "    None"
        nc_s = f"{r['nll_ctx']:8.3f}" if r["nll_ctx"] is not None else "    None"
        dn_s = f"{r['delta_nll']:6.3f}" if r["delta_nll"] is not None else "  None"
        ce4_s = f"{r['ce4_nll']:6.2f}" if r["ce4_nll"] is not None else "  None"
        co_s = f"{r['combined']:6.3f}" if r["combined"] is not None else "  None"
        print(f"  {r['label']:<25} {cc_s} {nb_s} {nc_s} {dn_s} {ce4_s} {co_s} {r['rating']:5.1f}")

    # Correlations
    valid = [r for r in results if r["cc"] is not None]
    if len(valid) >= 5:
        ratings = [r["rating"] for r in valid]
        cc_vals = [r["cc"] for r in valid]
        comb_vals = [r["combined"] for r in valid if r["combined"] is not None]
        comb_ratings = [r["rating"] for r in valid if r["combined"] is not None]

        rho_cc, p_cc = spearmanr(cc_vals, ratings)
        rho_comb, p_comb = spearmanr(comb_vals, comb_ratings) if len(comb_vals) >= 5 else (None, None)

        print(f"\n  Spearman r(CC, rating)       = {rho_cc:+.3f}  p={p_cc:.3f}")
        if rho_comb is not None:
            print(f"  Spearman r(combined, rating) = {rho_comb:+.3f}  p={p_comb:.3f}")
        print()

        # Also compare to CE4 alone
        ce4_vals = [r["ce4_nll"] for r in valid]
        rho_ce4, p_ce4 = spearmanr(ce4_vals, ratings)
        print(f"  Spearman r(CE4_NLL, rating)  = {rho_ce4:+.3f}  p={p_ce4:.3f}  (Cycle 2 baseline)")

    return results


if __name__ == "__main__":
    results = run_demo()
    print(json.dumps(results, indent=2))
