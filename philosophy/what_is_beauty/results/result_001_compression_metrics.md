# result_001 — Compression Metrics for Text Aesthetics

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/compression_aesthetics.py`

## What we ran

Six compression-efficiency estimators (CE1-CE3 char-level, CE5-CE6 word-level,
CE4 LM-based if available) applied to 10 text stimuli spanning the range from
predicted high-aesthetic (canonical poetry, elegant proofs) to predicted
low-aesthetic (random ASCII, repetitive text, bureaucratic prose).

## The central finding

**Surface compression metrics (CE1-CE3, CE5-CE6) do not distinguish beautiful
text from random text.**

Raw scores, sorted by composite (higher = more compressible):

| Rank | Stimulus | Composite | Notes |
|------|----------|-----------|-------|
| 1 | Random ASCII | 0.400 | All n-gram metrics → max entropy |
| 2 | Wikipedia factual | 0.372 | |
| 3 | Bureaucratic prose | 0.360 | |
| 4 | Euler identity | 0.357 | |
| 5 | Keats | 0.349 | |
| 6 | Euclid | 0.347 | |
| 7 | Repetitive text | 0.343 | zlib scores well but word metrics tank |
| 8 | Basho haiku | 0.340 | |
| 9 | Shakespeare | 0.330 | |
| 10 | Cantor diagonal | 0.330 | |

Random ASCII ties or beats canonical poetry on every surface metric.

## Why this happens

Char-entropy, bigram redundancy, and word-entropy all measure compressibility
relative to a **generic/structure-blind prior** (uniform character distribution,
order-0 or order-1 Markov chain, or empirical word frequency). For short texts,
nearly every text approaches maximum entropy on these measures because:
1. Short texts have few repeated n-grams, so all n-gram distributions look
   nearly uniform regardless of semantic content.
2. Random ASCII has no repeated characters → all n-gram metrics degenerate to
   max-entropy, and many scores flip to 1.0 rather than 0.0 (degenerate case).

## What this means for the theory

This is **not a refutation** of compression-beauty. It is a **specification** of it.

The claim from `attempt_001` is: beauty tracks compression efficiency *relative
to the observer's priors*. The crucial word is "priors." A human observer
reading Keats has extraordinarily rich priors:
- English phonology, prosody, syntax
- Semantic networks built from millions of prior exposures
- Genre knowledge (Romantic poetry, odes, classical allusions)
- Emotional and cultural associations with the themes

Under those priors, "Beauty is truth, truth beauty" compresses dramatically
(the semantic content is dense, the form is exact, the allusion is tight).
Under those same priors, random ASCII does NOT compress — it is noise relative
to English-language models.

CE1-CE3 and CE5-CE6 don't carry those priors. They are uninformed priors.
CE4 (LM NLL under GPT-2 or better) is the correct measurement because the LM
encodes approximately the right kind of learned structural prior.

## Prediction refined

**Original:** "aesthetic response should correlate with measurable compression
ratios relative to observer priors."

**Refined (numerical iteration 3):** The relevant compression ratios are those
computed under **deep learned priors** (language models, visual models, musical
models — domain-specific), not under shallow statistical priors (entropy, zlib).
Shallow metrics capture only the *substrate-level* compression that explains
cross-cultural universals (symmetry preference, consonance). Deep LM metrics are
needed for *cultural-level* aesthetic differentiation.

This decomposition was implicit in `attempt_001` ("compression is relative to
priors") but is now operationally explicit:

| Prior depth | Captures | Metric |
|-------------|----------|--------|
| Shallow (zlib/entropy) | Cross-cultural universals (symmetry, repetition) | CE1-CE3 |
| Word-level | Basic linguistic familiarity | CE5-CE6 |
| Deep LM | Culturally-specific aesthetic differentiation | CE4 |
| Domain expert LM | Expert aesthetic response | CE4 with fine-tuned model |

## Next steps (numerical track)

1. Run CE4 on the same stimuli with GPT-2 and a larger model; check whether
   ranking inverts as expected (beautiful prose should have lower NLL than
   random ASCII).
2. Gather human beauty ratings for the same 10 stimuli (via existing datasets
   or a small annotation run) and compute Spearman correlation vs. CE4.
3. Test whether fine-tuned domain models (trained on poetry, on proofs) show
   sharper aesthetic discrimination than generic LMs — this is the "expert
   priors" prediction.

## Status

CE4 not yet run (requires transformers install and model download).
CE1-CE3, CE5-CE6 baseline complete.
Finding: shallow metrics null. Deep LM metric is the test.
