"""
compression_aesthetics.py — Iteration 3
Numerical Track: what_is_beauty

Core claim under test: aesthetic response correlates with measurable compression
efficiency relative to the observer's priors.

FINDING FROM ITERATION 2:
  CE1-CE3 (zlib, char-entropy, bigram) measure raw/shallow compressibility.
  They do NOT track aesthetics: "aaaa..." scores highest by zlib+char metrics.
  The aesthetically relevant compression is relative to a RICH SEMANTIC PRIOR.
  CE4 (LM NLL) is the correct proxy — but requires a language model.

  Implication for the theory: the compression-beauty link is not about raw
  description length. It's about description length *under a prior that already
  encodes the relevant regularities* (linguistic, musical, mathematical, visual).
  This is a refinement of the claim, not a refutation.

WHAT WE BUILD HERE:
  CE5 — word-level entropy: H(word distribution) normalised by H(uniform over vocab).
         Better than char-entropy for natural language; still no model required.
  CE6 — word bigram redundancy: same as CE3 but at the word level.
  Fix: bigram_red degenerate case (short strings with all-unique chars).

  The CE4/CE5/CE6 tier requires words; CE1-CE3 work on any string.

Usage
-----
    python compression_aesthetics.py --demo
    python compression_aesthetics.py --text "Euclid alone has looked on Beauty bare"
    python compression_aesthetics.py --lm        # adds CE4 if transformers available
"""

import argparse
import json
import math
import re
import sys
import zlib
from collections import Counter


# ---------------------------------------------------------------------------
# CE1 — zlib compression ratio
# ---------------------------------------------------------------------------

def ce1_zlib(text: str) -> float:
    """zlib ratio = compressed_bytes / raw_bytes. Lower = more compressible."""
    raw = text.encode("utf-8")
    compressed = zlib.compress(raw, level=9)
    if len(raw) == 0:
        return 1.0
    return len(compressed) / len(raw)


# ---------------------------------------------------------------------------
# CE2 — character entropy (normalised)
# ---------------------------------------------------------------------------

def ce2_char_entropy(text: str) -> float:
    """Normalised Shannon entropy of char distribution. Lower = more predictable."""
    if not text:
        return 0.0
    counts = Counter(text)
    n = len(text)
    H = -sum((c / n) * math.log2(c / n) for c in counts.values() if c > 0)
    max_H = math.log2(max(len(counts), 2))
    return H / max_H


# ---------------------------------------------------------------------------
# CE3 — char bigram redundancy (fixed)
# ---------------------------------------------------------------------------

def ce3_bigram_redundancy(text: str) -> float:
    """
    Char-level bigram redundancy.  Higher = more consecutive-char structure.

    Fix: use conditional entropy H(c2|c1) = H(bigram_joint) - H(unigram),
    normalised by H(unigram).  When text is too short or all chars unique,
    the conditional entropy approaches H(unigram) → redundancy → 0.
    """
    if len(text) < 4:
        return 0.0

    unigrams = Counter(text)
    bigrams = Counter(zip(text, text[1:]))
    n1 = len(text)
    n2 = n1 - 1

    H1 = -sum((c / n1) * math.log2(c / n1) for c in unigrams.values())
    # Joint bigram entropy
    H_joint = -sum((c / n2) * math.log2(c / n2) for c in bigrams.values())
    # Conditional entropy H(c2|c1) = H(c1,c2) - H(c1)
    cond_H = H_joint - H1
    cond_H = max(0.0, cond_H)

    if H1 == 0:
        return 0.0

    # Redundancy: how much does knowing c1 reduce uncertainty about c2?
    redundancy = 1.0 - (cond_H / H1)
    return max(0.0, min(1.0, redundancy))


# ---------------------------------------------------------------------------
# CE5 — word entropy (normalised)
# ---------------------------------------------------------------------------

def _words(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z']+", text.lower())


def ce5_word_entropy(text: str) -> float:
    """
    Normalised Shannon entropy of word distribution.
    Lower = more lexical repetition = more predictable under a word-distribution prior.
    A text like "the the the the" has H=0; random word salad has H near 1.
    """
    ws = _words(text)
    if len(ws) < 2:
        return 1.0
    counts = Counter(ws)
    n = len(ws)
    H = -sum((c / n) * math.log2(c / n) for c in counts.values() if c > 0)
    max_H = math.log2(len(counts))
    if max_H == 0:
        return 0.0
    return H / max_H


# ---------------------------------------------------------------------------
# CE6 — word bigram redundancy
# ---------------------------------------------------------------------------

def ce6_word_bigram_redundancy(text: str) -> float:
    """
    Word-level bigram redundancy.  Higher = more sequential word structure.
    A sonnet with tight grammatical/poetic structure scores higher than a
    random sequence of words.
    """
    ws = _words(text)
    if len(ws) < 4:
        return 0.0

    unigrams = Counter(ws)
    bigrams = Counter(zip(ws, ws[1:]))
    n1 = len(ws)
    n2 = n1 - 1

    H1 = -sum((c / n1) * math.log2(c / n1) for c in unigrams.values())
    H_joint = -sum((c / n2) * math.log2(c / n2) for c in bigrams.values())
    cond_H = max(0.0, H_joint - H1)

    if H1 == 0:
        return 0.0

    redundancy = 1.0 - (cond_H / H1)
    return max(0.0, min(1.0, redundancy))


# ---------------------------------------------------------------------------
# CE4 — LM per-token NLL (optional)
# ---------------------------------------------------------------------------

def ce4_lm_nll(text: str, model_name: str = "gpt2") -> float | None:
    """
    Mean NLL per token under a causal LM.  Lower = more predictable under LM prior.
    Returns None if transformers not available.
    """
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
    except ImportError:
        return None

    try:
        tok = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        inputs = tok(text, return_tensors="pt")
        with torch.no_grad():
            out = model(**inputs, labels=inputs["input_ids"])
        return out.loss.item()
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Composite scorer
# ---------------------------------------------------------------------------

def score(text: str, use_lm: bool = False, lm_model: str = "gpt2") -> dict:
    """
    Compute all compression-efficiency scores.
    Composite oriented HIGHER = more compressible = higher predicted aesthetic response.

    Tier A (any string):    CE1, CE2, CE3 — shallow prior
    Tier B (word-bearing):  CE5, CE6      — word-distribution prior
    Tier C (optional):      CE4           — deep LM prior

    The compression-beauty claim is strongest for Tier C.  Tier A/B provide
    weaker but model-free baselines.
    """
    c1 = ce1_zlib(text)
    c2 = ce2_char_entropy(text)
    c3 = ce3_bigram_redundancy(text)
    c5 = ce5_word_entropy(text)
    c6 = ce6_word_bigram_redundancy(text)
    c4 = ce4_lm_nll(text) if use_lm else None

    # Orient: higher = more compressible
    s1 = max(0.0, 1.0 - c1)   # zlib: invert ratio; cap at 0 for ratio>1
    s2 = 1.0 - c2              # char entropy: invert
    s3 = c3                    # bigram redundancy: already higher=better
    s5 = 1.0 - c5              # word entropy: invert
    s6 = c6                    # word bigram: already higher=better

    tier_ab = [s1, s2, s3, s5, s6]

    if c4 is not None:
        s4 = max(0.0, 1.0 - c4 / 10.0)
        composite = sum(tier_ab + [s4]) / (len(tier_ab) + 1)
    else:
        s4 = None
        composite = sum(tier_ab) / len(tier_ab)

    return {
        "text": text[:120] + ("..." if len(text) > 120 else ""),
        "ce1_zlib_ratio": round(c1, 4),
        "ce2_char_H_norm": round(c2, 4),
        "ce3_bigram_red": round(c3, 4),
        "ce5_word_H_norm": round(c5, 4),
        "ce6_word_bigram_red": round(c6, 4),
        "ce4_lm_nll": round(c4, 4) if c4 is not None else None,
        "s1_zlib": round(s1, 4),
        "s2_char": round(s2, 4),
        "s3_bigram": round(s3, 4),
        "s5_word_H": round(s5, 4),
        "s6_word_bigram": round(s6, 4),
        "s4_lm": round(s4, 4) if s4 is not None else None,
        "composite": round(composite, 4),
    }


# ---------------------------------------------------------------------------
# Demo stimuli
# ---------------------------------------------------------------------------

DEMO_STIMULI = [
    # Predicted high aesthetic
    {
        "label": "Euclid (beautiful, elegant)",
        "text": "Euclid alone has looked on Beauty bare. Let all who prate of Beauty hold their peace.",
    },
    {
        "label": "Euler identity",
        "text": "e^(i*pi) + 1 = 0. Five constants, one equation, zero mystery.",
    },
    {
        "label": "Keats (Ode on a Grecian Urn)",
        "text": (
            "Beauty is truth, truth beauty — that is all ye know on earth, "
            "and all ye need to know."
        ),
    },
    {
        "label": "Cantor diagonal",
        "text": (
            "Assume a bijection f: N -> R. Build x: x_n != f(n)_n for all n. "
            "Then x not in range(f). Contradiction. Therefore |R| > |N|."
        ),
    },
    {
        "label": "Basho haiku",
        "text": "An old silent pond. A frog jumps into the pond. Splash! Silence again.",
    },
    {
        "label": "Shakespeare Sonnet 18 opening",
        "text": (
            "Shall I compare thee to a summer's day? "
            "Thou art more lovely and more temperate."
        ),
    },
    # Predicted low aesthetic
    {
        "label": "Bureaucratic prose",
        "text": (
            "Pursuant to the provisions of the aforementioned regulation, the committee "
            "shall, not later than thirty (30) business days following the date hereof, "
            "convene a duly constituted meeting to assess the preliminary findings "
            "referenced in Exhibit A, subsection 4, paragraph 2(c)(iii)."
        ),
    },
    {
        "label": "Random ASCII",
        "text": "q7!kRp#2mXv&9LnYw$sB^tFjQ@0dHcU%eAzOiGN",
    },
    {
        "label": "Repetitive text",
        "text": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    },
    # Mid-range
    {
        "label": "Wikipedia factual sentence",
        "text": (
            "The Pythagorean theorem states that the square of the hypotenuse of a "
            "right triangle equals the sum of the squares of the other two sides."
        ),
    },
]


def run_demo(use_lm: bool = False) -> None:
    results = []
    for s in DEMO_STIMULI:
        r = score(s["text"], use_lm=use_lm)
        r["label"] = s["label"]
        results.append(r)

    results.sort(key=lambda x: x["composite"], reverse=True)

    print("=" * 72)
    print("BEAUTY / COMPRESSION-EFFICIENCY DEMO")
    print("Higher composite = more compressible = higher predicted beauty")
    print("Tier A/B only (no LM)" + (" + CE4 LM prior" if use_lm else ""))
    print("=" * 72)
    for r in results:
        lm_str = f"  lm={r['ce4_lm_nll']:.2f}" if r["ce4_lm_nll"] is not None else ""
        print(
            f"  [{r['composite']:.3f}] {r['label']}\n"
            f"         zlib={r['ce1_zlib_ratio']:.3f} "
            f"H_c={r['ce2_char_H_norm']:.3f} "
            f"bg_c={r['ce3_bigram_red']:.3f} "
            f"H_w={r['ce5_word_H_norm']:.3f} "
            f"bg_w={r['ce6_word_bigram_red']:.3f}"
            + lm_str
        )
    print()
    print(json.dumps(results, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Compression-efficiency aesthetic scorer (Odd track, what_is_beauty)"
    )
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--text", type=str)
    parser.add_argument("--file", type=str)
    parser.add_argument("--lm", action="store_true")
    args = parser.parse_args()

    if args.demo:
        run_demo(use_lm=args.lm)
    elif args.text:
        print(json.dumps(score(args.text, use_lm=args.lm), indent=2))
    elif args.file:
        with open(args.file) as f:
            stimuli = json.load(f)
        results = [score(s["text"], use_lm=args.lm) | {"label": s.get("label", "")}
                   for s in stimuli]
        results.sort(key=lambda x: x["composite"], reverse=True)
        print(json.dumps(results, indent=2))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
