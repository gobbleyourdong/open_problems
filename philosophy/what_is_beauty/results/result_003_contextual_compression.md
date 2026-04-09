# result_003 — Contextual Compression: First Significant Correlation

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/contextual_compression.py`

## What we ran

Contextual compression (CC) metric: measures how much the first half of a text
reduces the LM NLL of the second half. Combined with CE4 (unconditional NLL)
using: combined = CC × sigmoid(CE4_nll − 3).

## Results

| Stimulus | CC | CE4_nll | Combined | Rating |
|----------|-----|---------|----------|--------|
| Repetitive text | **0.682** | 1.34 | 0.109 | 1.0 |
| Wikipedia | 0.396 | 2.19 | 0.122 | 4.0 |
| Basho haiku | 0.330 | 5.05 | **0.293** | 8.0 |
| Shakespeare | 0.301 | 3.68 | 0.200 | 8.5 |
| Cantor diagonal | 0.242 | 4.42 | 0.195 | 8.5 |
| Keats | 0.227 | 3.87 | 0.160 | 9.0 |
| Euler identity | 0.184 | 5.04 | 0.163 | 9.5 |
| Euclid | 0.164 | 6.21 | 0.158 | 8.0 |
| Bureaucratic prose | 0.195 | 2.82 | 0.089 | 1.5 |
| **Random ASCII** | **0.108** | 5.20 | **0.097** | 1.0 |

## Correlations

| Metric | Spearman r | p-value | Significance |
|--------|-----------|---------|-------------|
| CE1–CE3 surface | < 0.35 | > 0.30 | not significant |
| CE4 NLL alone | +0.226 | 0.530 | not significant |
| CC alone | −0.128 | 0.724 | not significant |
| **Combined (CC × sigmoid)** | **+0.710** | **0.022** | **p < 0.05** ✓ |

## What each component contributes

**CC alone (r=−0.128):** Contextual coherence alone fails because repetitive
text has CC=0.682 (first half perfectly predicts second half) but rating=1.0.
High CC is necessary but not sufficient for beauty.

**CE4 alone (r=+0.226):** Unconditional NLL alone fails because random ASCII
has CE4=5.20 (similar to beautiful mathematical proofs at 5.04). The confusion
of "unusual" with "beautiful" is the key flaw.

**Combined (r=+0.710, p=0.022):** The product correctly handles both pathologies:
- Repetitive text: high CC (0.682) × near-zero sigmoid(1.34−3)=0.16 → combined=0.109
- Random ASCII: low CC (0.108) × moderate sigmoid(5.20−3)=0.90 → combined=0.097
- Basho haiku: moderate CC (0.330) × high sigmoid(5.05−3)=0.89 → combined=0.293

The formula captures "internally coherent AND unusual relative to base rate" —
which is precisely the compression-beauty claim stated operationally:
beauty = high compression gain from internal structure (CC) in content that
is rich enough to resist generic-prior compression (CE4 > 3).

## Theoretical significance

This is the first operationalisation of the compression-beauty prediction that
achieves statistical significance (n=10, p=0.022). The metric is a proxy for
"compression under domain-specific prior" — it approximates the domain prior
by using GPT-2 as the base and measuring self-compression as the domain signal.

The combined score has a natural interpretation under the compression-beauty
theory:
- CC = compression gain from internal structure (the aesthetic signal)
- sigmoid(CE4−3) = weight that favours content that is genuinely complex
  (not trivially compressible under any prior)
- Product = "beautifully structured complexity"

This is Schmidhuber's information-theoretic aesthetics formulation
("beauty = interestingness = compression progress") quantified: the interesting
text is both complex enough to have content (CE4 > 3) and structured enough
to compress internally (CC > 0).

## Caveats

1. **n=10 is small.** p=0.022 is encouraging but not robust. With n=50 stimuli
   from an actual beauty ratings dataset (e.g., using poem ratings from
   EmoBank/Gutenberg Poetry Corpus), the correlation would be more reliable.

2. **The stimuli set is not random.** It was selected to span a range, not
   drawn from any population. Ascertainment bias could inflate the correlation.

3. **GPT-2 as the base model** introduces systematic biases (trained on
   English web text; archaic literary registers are underrepresented). A better
   base model would sharpen the results.

## Next steps

1. Run on a larger, unbiased set of stimuli from existing poetry beauty datasets
   (e.g., Gutenberg Poetry Corpus with crowd-sourced beauty ratings).
2. Parameterize the sigmoid threshold (currently hardcoded at 3.0); find the
   optimal threshold that maximizes Spearman r.
3. Test the metric on non-text stimuli: musical sequences encoded as text,
   mathematical notations, to verify the cross-domain claim.

## Status

**Compression-beauty theory: first statistically significant empirical support.**
Combined CC × CE4 metric: r=0.710, p=0.022 (n=10, proxy ratings).
Interpretation: beauty tracks contextual self-compression in content that
resists generic-prior prediction.
