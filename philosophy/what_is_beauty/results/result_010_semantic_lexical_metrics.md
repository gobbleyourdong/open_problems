# result_010 — Semantic and Lexical Metrics: LM NLL Remains Best

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** inline Cycle 13

## What we ran

Two alternative aesthetic metrics tested on n=18 stimuli (literary + math):
1. Sentence-Transformers semantic metrics (embedding norm, scramble sensitivity, cross-sentence coherence)
2. Lexical compression metrics (TTR, content density, avg word length, chars-per-unique-content-token)

## Results

### Semantic metrics (sentence-transformers all-MiniLM-L6-v2)

| Metric | r | p | Notes |
|--------|---|---|-------|
| Embedding norm | +0.013 | 0.958 | All embeddings normalized to unit sphere |
| 1 - scramble_similarity | −0.081 | 0.751 | Wrong direction |
| Cross-sentence coherence | −0.305 | 0.218 | Negative — factual texts more coherent |

**All semantic metrics fail.** BERT embedding similarity captures topical
coherence (texts consistently about one topic), not predictive structure.
Haiku and Blake have LOW cross-sentence similarity (jumping between images)
despite high aesthetic ratings. Factual/definition texts have HIGH coherence
(all about the same topic) but low ratings.

### Lexical metrics

| Metric | r | p | Notes |
|--------|---|---|-------|
| TTR (vocabulary variety) | −0.106 | 0.677 | No signal |
| Content word density | −0.072 | 0.776 | No signal |
| Avg word length (negative) | −0.430 | 0.075 | Trending: shorter words = more beautiful |
| Chars per unique content token (CPT, inverted) | **+0.490** | **0.039** | Significant |

**CPT** (lower = more content per character) is the one metric that works
at n=18 (r=+0.490, p=0.039). But:
- Without repetitive text: r=+0.393, p=0.118 (not significant)
- Without two extreme outliers: r=+0.318, p=0.231 (not significant)
- Within math only (n=6): r=+0.812, p=0.050 (borderline)

**CPT fails robustness check.** The significance is driven by the extreme
outliers (repetitive text cpt=42, trig identities cpt=17.6) at the bottom.

## What the metrics tell us

Semantic metrics (BERT embeddings) fail because they capture TOPICAL similarity,
not predictive structural compression. Beautiful texts are not more topically
coherent; they are more structurally surprising.

Lexical metrics partially work within math (CPT r=+0.812 for math-only n=6)
because mathematical aesthetic compression is partly about economy of notation.
Euler's identity (cpt=7.6) uses few characters for many concepts. Trig identity
lists (cpt=17.6) use many characters for few unique concepts.

## Why LM NLL remains superior

The LM NLL metric (GPT-2 CE4) measures "surprise under a learned language
model prior." This captures:
1. Topical unusualness (the content is rare in the training distribution)
2. Structural complexity (the pattern requires more bits to encode)
3. Register specificity (the notation/register is uncommon)

None of the lexical or semantic metrics capture all three jointly. The LM NLL
(r=+0.723 for compressed math statements, n=14, p=0.003) remains the best
available proxy for aesthetic compression under a learned prior.

## For the theory

The failure of semantic and lexical metrics confirms: aesthetic compression
is NOT captured by simple statistics of the text. It requires a model that
has learned the structural patterns of the domain. The NLL under a language
model (which has learned domain structure) IS a proxy for "how much structure
does this text pack relative to what was expected."

This is the compression-beauty claim stated precisely: aesthetics tracks
not raw density or semantic similarity, but UNEXPECTEDNESS of structure
relative to a learned prior — exactly what NLL measures.
