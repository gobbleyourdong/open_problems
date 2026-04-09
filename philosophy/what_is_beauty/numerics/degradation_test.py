"""
degradation_test.py — Cycle 6
Numerical Track: what_is_beauty

Within-text degradation test: do originals score higher on CC than
their deliberately degraded variants?

Theory prediction (within a text family, same register):
  CC(original) > CC(scrambled) because the original has internal structural
  regularities (meter, rhyme, proof steps, logical flow) that make the
  first half predictive of the second. Scrambling destroys this.

Design:
  For each of 6 canonical texts, create 3 degraded variants:
    D1: word-level scramble (words in random order, same words)
    D2: sentence-level scramble (sentences in random order)
    D3: synonym substitution (replace key aesthetic words with near-synonyms,
        breaking the specific semantic density of the original)

  Predict: CC(original) > CC(D1), CC(D2), CC(D3) for literary texts.
  For mathematical texts: also predict CC(original) > scrambled versions.
"""

import json
import math
import random
import re


def scramble_words(text: str, seed: int = 42) -> str:
    """Randomly reorder words, preserving punctuation attachment."""
    rng = random.Random(seed)
    words = text.split()
    rng.shuffle(words)
    return " ".join(words)


def scramble_sentences(text: str, seed: int = 42) -> str:
    """Randomly reorder sentences."""
    rng = random.Random(seed)
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    if len(sentences) <= 1:
        # Split on commas/semicolons instead
        sentences = re.split(r'(?<=[,;])\s+', text.strip())
    rng.shuffle(sentences)
    return " ".join(sentences)


def substitute_synonyms(text: str, substitutions: dict) -> str:
    """Apply word substitutions (replaces aesthetic words with flat synonyms)."""
    result = text
    for original, replacement in substitutions.items():
        result = re.sub(r'\b' + re.escape(original) + r'\b', replacement, result, flags=re.IGNORECASE)
    return result


# Canonical texts with their aesthetic-word substitutions
TEXTS = [
    {
        "label": "Keats (truth/beauty)",
        "original": "Beauty is truth, truth beauty — that is all ye know on earth, and all ye need to know.",
        "synonyms": {"Beauty": "Appearance", "truth": "fact", "beauty": "appearance", "know": "understand", "need": "require"},
        "type": "literary",
        "rating": 9.0,
    },
    {
        "label": "Shakespeare (Sonnet 18)",
        "original": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate.",
        "synonyms": {"lovely": "attractive", "temperate": "moderate", "Shall": "Should", "compare": "liken", "summer": "warm"},
        "type": "literary",
        "rating": 8.5,
    },
    {
        "label": "Donne (No man is island)",
        "original": "No man is an island entire of itself; every man is a piece of the continent, a part of the main.",
        "synonyms": {"island": "territory", "entire": "complete", "continent": "landmass", "main": "whole", "piece": "part"},
        "type": "literary",
        "rating": 8.5,
    },
    {
        "label": "Euler identity",
        "original": "e^(i*pi) + 1 = 0. Five constants, one equation, zero mystery.",
        "synonyms": {"mystery": "complexity", "constants": "values", "equation": "formula", "zero": "no", "Five": "Multiple"},
        "type": "math",
        "rating": 9.5,
    },
    {
        "label": "Cantor diagonal",
        "original": "Assume a bijection f: N -> R. Build x: x_n != f(n)_n for all n. Then x not in range(f). Contradiction. Therefore |R| > |N|.",
        "synonyms": {"bijection": "mapping", "Contradiction": "Problem", "Therefore": "So", "Assume": "Suppose", "Build": "Create"},
        "type": "math",
        "rating": 8.5,
    },
    {
        "label": "Basho haiku",
        "original": "An old silent pond. A frog jumps into the pond. Splash! Silence again.",
        "synonyms": {"silent": "quiet", "old": "ancient", "frog": "amphibian", "Splash": "Sound", "Silence": "Quiet"},
        "type": "literary",
        "rating": 8.0,
    },
]


def compute_cc(text: str, model=None, tok=None) -> dict | None:
    """Compute CC and CE4 for a text using the provided model."""
    if model is None or tok is None:
        return None
    import torch
    ids = tok.encode(text)
    if len(ids) < 4:
        return {"cc": None, "ce4": None, "note": "too short"}
    try:
        # CE4
        inp = torch.tensor([ids])
        with torch.no_grad():
            ce4 = model(inp, labels=inp).loss.item()
        # CC
        split = max(1, len(ids) // 2)
        first, second = ids[:split], ids[split:]
        t2 = torch.tensor([second])
        with torch.no_grad():
            nll_base = model(t2, labels=t2).loss.item()
        t_all = torch.tensor([first + second])
        labs = torch.tensor([[-100]*len(first) + second])
        with torch.no_grad():
            nll_ctx = model(t_all, labels=labs).loss.item()
        cc = round(1.0 - nll_ctx / nll_base if nll_base > 0 else 0.0, 4)
        return {"cc": cc, "ce4": round(ce4, 4)}
    except Exception as e:
        return {"cc": None, "ce4": None, "error": str(e)}


def run():
    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        tok = AutoTokenizer.from_pretrained("gpt2")
        model = AutoModelForCausalLM.from_pretrained("gpt2")
    except Exception:
        print("transformers not available"); return

    from scipy.stats import spearmanr

    print("=" * 72)
    print("WITHIN-TEXT DEGRADATION TEST — what_is_beauty Cycle 6")
    print("Prediction: CC(original) > CC(scrambled) for aesthetically structured text")
    print("=" * 72)

    all_results = []
    original_wins_cc = 0
    original_wins_ce4 = 0
    total_comparisons = 0

    for t in TEXTS:
        orig = t["original"]
        d1   = scramble_words(orig)
        d2   = scramble_sentences(orig)
        d3   = substitute_synonyms(orig, t["synonyms"])

        variants = [
            ("original", orig),
            ("D1_word_scramble", d1),
            ("D2_sent_scramble", d2),
            ("D3_synonym_sub",   d3),
        ]

        print(f"\n  {t['label']} (type={t['type']}, rating={t['rating']})")
        scores = {}
        for vname, vtext in variants:
            r = compute_cc(vtext, model, tok)
            scores[vname] = r
            if r:
                cc_s = f"{r['cc']:.3f}" if r['cc'] is not None else "None"
                ce4_s = f"{r['ce4']:.3f}" if r['ce4'] is not None else "None"
                print(f"    {vname:<20}  CC={cc_s}  CE4={ce4_s}")

        # Count wins
        orig_cc = scores["original"]["cc"] if scores["original"] else None
        orig_ce4 = scores["original"]["ce4"] if scores["original"] else None
        for vname in ["D1_word_scramble", "D2_sent_scramble", "D3_synonym_sub"]:
            v = scores.get(vname)
            if v and orig_cc is not None and v["cc"] is not None:
                total_comparisons += 1
                if orig_cc > v["cc"]:
                    original_wins_cc += 1
                if orig_ce4 is not None and v["ce4"] is not None and orig_ce4 < v["ce4"]:
                    # For CE4, lower = more predictable = better under generic prior
                    # But for aesthetics, HIGHER CE4 correlated with aesthetics in Cycle 4
                    # So we check: does original have CE4 closer to its register mean?
                    original_wins_ce4 += 1  # just track, analyze below

        all_results.append({
            "label": t["label"], "type": t["type"], "rating": t["rating"],
            "scores": {k: v for k, v in scores.items() if v}
        })

    print(f"\n  CC wins: original > degraded in {original_wins_cc}/{total_comparisons} comparisons")

    # Summary: within each text, does original rank first by CC?
    print("\n  CC ranking within each text family (1=original ranks highest):")
    cc_rank_of_original = []
    for r in all_results:
        cc_vals = {k: v["cc"] for k, v in r["scores"].items() if v.get("cc") is not None}
        if not cc_vals:
            continue
        ranked = sorted(cc_vals.items(), key=lambda x: -x[1])
        rank = next((i+1 for i, (k,_) in enumerate(ranked) if k == "original"), None)
        cc_rank_of_original.append(rank)
        print(f"    {r['label'][:35]:<35}  original ranks: {rank}/4  ({', '.join(k for k,_ in ranked)})")

    valid = [r for r in cc_rank_of_original if r is not None]
    if valid:
        mean_rank = sum(valid) / len(valid)
        top_rate  = sum(1 for r in valid if r == 1) / len(valid)
        print(f"\n  Mean rank of original: {mean_rank:.2f}/4 (1 = best)")
        print(f"  Original ranks 1st: {sum(1 for r in valid if r==1)}/{len(valid)} texts")
        if mean_rank < 2.5:
            print("  → Originals tend to have HIGHER CC than degraded variants.")
        else:
            print("  → Originals do NOT consistently outperform degraded variants on CC.")

    return all_results


if __name__ == "__main__":
    results = run()
