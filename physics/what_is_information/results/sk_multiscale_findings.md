# results/sk_multiscale_findings.md — Multi-Scale S/K Analysis

**Date:** 2026-04-09
**Script:** `numerics/sk_multiscale.py`
**Setup:** 100KB synthetic English-like text (Markov chain), analyzed at byte / char-trigram / word / bigram levels

## Setup

Gap.md R3 asks: "Does the mind-as-compressor framing make a specific physical prediction once
translated into K-information terms? Candidate: the thermodynamic cost of cognition is dominated
by S-erasure (Landauer), while its cognitive value is measured in K-accumulation. The ratio should
be bounded."

This script tests whether the S/K ratio (Shannon entropy / gzip compression ratio) is constant
across scales of linguistic analysis.

## Results

| Level | Vocab | H (bits/token) | H_max | H/H_max | gzip | H/K |
|---|---|---|---|---|---|---|
| byte | 37 | 4.278 | 5.210 | 0.821 | 0.079 | **53.8×** |
| char_trigram | 906 | 9.198 | 9.823 | 0.936 | 0.038 | **241×** |
| word | 168 | 6.732 | 7.392 | 0.911 | 0.080 | **84.4×** |
| bigram | 320 | 8.059 | 8.322 | 0.969 | 0.048 | **166×** |

Note: gzip ratios are very low (0.04–0.08) because synthetic Markov text repeats
frequently from a small vocabulary (~168 words). Real English text has gzip ≈ 0.35–0.45.
The RELATIVE patterns across scales are reliable; absolute H/K values would be ~5× larger
for real English text.

## Finding 1: H/K ratio is NOT constant across scales

The S-cost per K-unit grows by a factor of ~3× from byte to bigram level:
- Byte: H/K = 53.8
- Char trigram: 241 (peak — trigrams are poorly matched by LZ77)
- Word: 84.4
- Bigram: 166

**This breaks the naive scale-independence prediction.** The S-cost per K-bit extracted
depends on the granularity of analysis. Coarser-scale analysis (words, bigrams) extracts
more K-structure per unit of alphabet but requires processing more S-information per token.

**Interpretation:** the H/K ratio at each scale measures "how much semantic compression
happens at that level." Byte-level compression is cheapest (H/K≈54 for this text); bigram
compression is most expensive (H/K≈166). If a cognitive system processes text at the bigram
level, it spends ~3× more S-erasure work per K-bit gained than a byte-level processor.

## Finding 2: H × K ≈ constant for byte-level and trigram (but not word/bigram)

| Level | H×K |
|---|---|
| byte | 0.340 |
| char_trigram | 0.351 |
| word | 0.537 |
| bigram | 0.391 |

Byte and char-trigram give H×K ≈ 0.34–0.35, suggesting a near-constant product at these
subword levels. Word and bigram diverge. This suggests a possible scale invariance within
the character-level analysis that breaks at the morphological boundary.

**Physical interpretation:** if H is S-information flow and gzip-K is K-content flow, then
H×K ≈ constant at character level says: the S-content and K-content of the text are
approximately anti-correlated at character scale. Not an exact conservation law — just a
scale-level symmetry in this corpus.

## Finding 3: H/H_max grows with scale — approaching max entropy at coarser granularities

| Level | H/H_max |
|---|---|
| byte | 0.821 |
| char_trigram | 0.936 |
| word | 0.911 |
| bigram | 0.969 |

At bigram level, the empirical entropy is 96.9% of maximum — bigrams are nearly maximally
unpredictable given the small vocabulary. This is a property of the synthetic text (only
168 unique words, limited Markov structure). Real English would show H/H_max < 0.5 at
the word level (due to Zipf's law and strong word co-occurrence constraints).

**Implication for R3:** a better test requires real text with a Zipfian word distribution.
The synthetic text's near-uniform word distribution inflates H/H_max and makes H/K larger
than it would be for real language. The next iteration should use a real text corpus.

## Finding 4: gzip ratios near constant at byte and word level (0.079 vs 0.080)

The byte-level and word-level gzip ratios are almost identical: 0.0795 vs 0.0798.
This means the text is equally compressible at byte level (character repetition) and at
word level (word repetition). For real natural language, word-level gzip ratio would be
much lower (~0.1) than byte-level (~0.35), because words repeat more than bytes.
The synthetic text's small vocabulary makes both equally repetitive.

## Limitations

1. **Synthetic text has too small vocabulary** (168 words). Real English has 50 000+
   common words and a Zipf distribution that makes H much lower relative to H_max.
   The H/K values are inflated by ~5× relative to what real text would show.

2. **gzip on word sequences** measures word-level repetition well but fails to find
   semantic regularity (related words in different word forms). A better K-proxy for word
   sequences would be a vocabulary-indexed compression (replacing each word with its rank
   in a frequency list, then compressing the rank sequence).

## Next steps (iteration 3)

The most important next step for R3 is computing the S/K ratio for a known-length natural
text and connecting it to the Landauer energy cost. For iteration 3 see `sk_bekenstein_bounds.py`.

## Status

Phase 2. Multi-scale analysis complete. H/K is scale-dependent (violates naive scale-independence).
The most useful extension: replace the synthetic corpus with real text (Gutenberg) and
rerun — this would validate whether scale-dependence of H/K is a property of language
or an artifact of the synthetic corpus.
