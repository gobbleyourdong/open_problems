# result_007 — Math Beauty Expanded: n=4 Signal Was Sampling Artefact

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/math_beauty_expanded.py`

## What we ran

Expanded the math stimuli set from n=4 (Cycle 5) to n=12 by adding:
- More high-aesthetic proofs (Euclid infinite primes, Fundamental Theorem of Calculus)
- Mid-range formulations (binomial theorem, definition of derivative)
- Low-aesthetic procedural content (long division, quadratic formula, trig list)

## Results

| Stimuli | Spearman r | p | Comment |
|---------|-----------|---|---------|
| Cycle 5 (n=4, high-aesthetic only) | +0.949 | 0.051 | All beautiful content |
| Cycle 8 n=4 subset replication | +0.632 | 0.368 | Different composition |
| Cycle 8 full (n=12) | **+0.423** | **0.171** | Not significant |

The r=0.949 from Cycle 5 was **not replicated** and does not hold at n=12.

## The main outlier

**Long division algorithm:** NLL=4.548 (second highest in dataset), rating=2.0

GPT-2 finds the step-by-step long division description highly surprising (NLL=4.55)
because it contains specific numbers (2847, 13, 219) and procedural steps that are
unusual in GPT-2's internet training corpus. But the long division algorithm has
essentially zero aesthetic content.

This is the same structural failure as random ASCII at the full-corpus level:
GPT-2 NLL marks "unusual relative to internet text," not "aesthetically excellent."
Within the math register, there is a sub-distinction between:
- **Elegant proofs** (unusual because they demonstrate non-obvious ideas)
- **Procedural algorithms** (unusual because they describe mechanical steps)

GPT-2 gives similar high NLL to both. A model trained specifically on
mathematical proof literature would distinguish them: elegant proofs follow
recognisable proof structures (assume→build→contradict→conclude) that the
model would learn to predict well, while procedural algorithms with specific
numbers would remain high NLL.

## Why n=4 gave r=0.949

The n=4 set (Euler, Cantor, Pythagorean visual proof, Ramanujan) consisted
entirely of high-aesthetic elegant proofs. Within that restricted range:
- All texts are in the same sub-register (elegant mathematical argument)
- NLL varies from 3.4 to 5.0, roughly tracking proof abstractness
- Ratings vary from 8.0 to 9.5

This created a spurious monotone relationship because the n=4 sample was
cherry-picked from the same aesthetic sub-class. Expanding to include
procedural math (long division NLL=4.55, rating=2.0) breaks the pattern.

## What the data does show at n=12

The correlation is positive (r=+0.423) and in the right direction, but not
significant. More importantly, examining the NLL ranking reveals a partial
structure:

- **Bottom of ranking** (lowest NLL, most predictable): trig identities (1.59),
  Pythagorean theorem algebraic (2.19), Binomial theorem (3.24)
  — all have ratings 3.0–6.0 (mid to low-aesthetic)
- **Top of ranking** (highest NLL, most surprising): Euler (5.04),
  Long division (4.55), Cantor (4.42), Euclid (4.31), FTC (4.23)
  — mixed aesthetic (9.5, 2.0, 8.5, 9.0, 8.5)

The long division outlier prevents the top of the NLL ranking from being
aesthetically excellent. Without it, the top-4 would all be highly-rated proofs.

## Revised assessment of the within-math claim

**The n=4 result was real in a limited sense:** within the sub-class of elegant
mathematical proofs, GPT-2 NLL does track aesthetic quality (r≈0.6–0.9). But
this sub-class selection is doing the work, not GPT-2's prior itself.

**The genuine within-math claim that survives:** among texts that are ALREADY
identified as belonging to the "elegant proof" sub-register (not "procedural
computation"), NLL may correlate with aesthetic depth. Testing this requires
cleaner sub-register labelling.

**Required test:** Split math stimuli into {elegant proofs} vs {procedural algorithms}
first, then compute within-elegant-proof r(NLL, rating).

## Theoretical implication

The compression-beauty signal is sensitive to within-register sub-structure.
Even the "math" register contains sub-registers (proofs vs algorithms vs
formulas vs definitions) with very different NLL profiles under GPT-2.
The right prior needs to learn at the sub-register level, not just the domain level.

## Update to cert_001

The cert_001 finding "within-math r=0.949 (n=4)" should be qualified:
**"Within-math r=0.949 (n=4, high-aesthetic proofs only); does not replicate
at n=12 when procedural math is included (r=0.423, p=0.171)."**
The signal is sub-register dependent, not domain-level.
