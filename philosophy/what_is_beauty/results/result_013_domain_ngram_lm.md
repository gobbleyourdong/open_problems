# result_013 — Domain N-gram LM: Corpus Coverage is Required

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/domain_ngram_lm.py`

## What we ran

A word-level trigram model trained on a curated mathematical corpus (533 tokens,
244 vocabulary items) was tested on the n=14 compressed math stimuli.

## Result

**Domain n-gram LM: r=−0.133, p=0.651 (completely fails)**
**GPT-2 NLL: r=+0.723, p=0.003 (retains its signal)**

All domain NLL values are nearly identical (~5.50 ± 0.02) because:
1. The training corpus (533 tokens) is too small for trigram coverage
2. Mathematical notation (e^(ix), sqrt(pi), etc.) is all OOV
3. Laplace smoothing assigns near-uniform probability to all OOV n-grams
4. Result: maximum-entropy uniform NLL for every text

## What this tells us

### The domain structural prior requirement is specific

The compression-beauty claim requires a prior that has LEARNED THE DOMAIN'S STRUCTURE.
A tiny trigram model fails because it cannot encode mathematical structure from
533 tokens. The domain prior must:
1. Have sufficient vocabulary coverage (all notation types seen)
2. Have learned statistical patterns in the domain (which structures co-occur)
3. Be able to distinguish "elegant proof" from "procedural computation" patterns

**GPT-2's generic prior happens to satisfy (1) and partially (2)** because it
was trained on large amounts of internet text including Stack Exchange Mathematics,
arXiv preprints, and textbooks. This is why GPT-2 NLL (r=+0.723) outperforms
the tiny trigram (r=−0.133).

### Implications for the domain LM test

The decisive test of the compression-beauty claim requires a model trained on:
- Mathematical proof literature (not just definitions)
- Large enough to cover the domain vocabulary (>100K tokens at minimum)
- NOT the specific canonical texts being evaluated (avoid memorisation)

The correct approach: train a small LSTM or transformer on a corpus of
mathematical proofs from arXiv (math.HO, math.CO categories) excluding
the canonical famous theorems in the evaluation set. This is tractable
but requires a compute investment beyond this session's scope.

### GPT-2 as the default

Until a domain-specific model is available, GPT-2 remains the best proxy
because it has implicit mathematical training from internet text. The
r=+0.723, p=0.003 result on compressed math statements reflects this
implicit domain coverage.

## Update to cert_001

The "domain structural prior" requirement now has a more specific operational
form: the prior must have sufficient vocabulary coverage of the evaluation domain.
A minimum of ~10K tokens of in-domain text would be needed for a bigram model;
~100K for a trigram; a proper transformer LM requires millions.

GPT-2 satisfies this threshold for mathematical text and gives r=+0.723.
The compression-beauty claim is supported at this level. The further
refinement (removing memorisation while maintaining coverage) awaits
a dedicated math LM.
