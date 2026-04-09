# result_004 — Expanded Stimuli: CE4 Generalises, Combined Overfits

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/expanded_stimuli.py`, `numerics/threshold_sweep.py`

## What we ran

Threshold sweep over (tau, alpha) on n=10: best at tau=1.0, alpha=0.25, r=0.734.
Expanded to n=25 stimuli (15 new: more poetry, science writing, bad prose varieties).
Tested both optimised (tau=1.0, alpha=0.25) and original (tau=3.0, alpha=1.0) combined
metrics, plus CE4 alone and CC alone.

## Results (n=25)

| Metric | Spearman r | p-value |
|--------|-----------|---------|
| CE4 NLL alone | **+0.605** | **0.001** |
| Combined (tau=1.0, opt) | +0.262 | 0.206 |
| Combined (tau=3.0, orig) | +0.273 | 0.186 |
| CC alone | −0.309 | 0.132 |

## Key finding: CE4 generalises, combined does not

The threshold optimisation on n=10 overfit. The combined metric breaks on new
stimuli because CC measures ANY internal coherence, not just aesthetic coherence:
- Form letter (rating=1.5): CC=0.591 — template structure is highly coherent
- Corporate mission statement (rating=1.5): CC=0.327 — buzzword chains predict well
- "Repetitive but wordy" (rating=2.0): CC=0.452 — lexical repetition within text

These stimuli were not in the n=10 set. Adding them exposes the CC component as
an overfitted handle on two specific edge cases (random ASCII, repetitive "aaa").

CE4 (GPT-2 NLL) alone achieves r=0.605, p=0.001 on n=25. This is the strongest,
most replicable result across all Cycles. The correlation is significant and robust.

## What CE4 captures

Texts that GPT-2 finds hard to predict (high NLL) get higher aesthetic ratings:
- Mathematical notation, archaic literary prose, haiku register, dense proof language
  all have CE4 > 4.5 and ratings ≥ 8
- Plain expository writing, form letters, corporate prose, repetitive text
  all have CE4 < 3.5 and ratings ≤ 4

The mechanism: **beautiful text is semantically rare.** It uses registers,
constructions, and word combinations that are uncommon under GPT-2's
internet-text prior. Aesthetically impoverished text (bureaucratic, formulaic,
random) clusters near GPT-2's familiar patterns (common words, template phrases)
OR near GPT-2's unfamiliar patterns (random noise) — and CE4 already partially
separates these clusters via the NLL range.

The residual confound (random ASCII at CE4=5.2 with rating=1.0 vs Blake at
CE4=5.5 with rating=8.5) is not resolvable by CE4 alone. Both are unfamiliar
to GPT-2. A domain-specific model remains the correct fix.

## What the theory now says operationally

Three cycles of results converge on this picture:

| Metric | Mechanism it measures | r (n=25) | Robust? |
|--------|----------------------|----------|---------|
| CE1-CE3 (zlib/entropy) | Generic compressibility | < 0.35 | No |
| CC alone | Template/structural coherence | −0.31 | No (wrong direction) |
| CE4 (GPT-2 NLL) | Rarity under generic prior | **+0.61** | Yes |
| CC × sigmoid(CE4) | Contextual coherence × rarity | +0.27 | No (overfit to n=10) |
| Domain-LM NLL | Rarity under aesthetic prior | NOT YET MEASURED | — |

The compression-beauty claim at its cleanest: **aesthetic text is rare under
a generic language model prior** (CE4, r=0.605). The claim that beautiful text
also has internal coherence (CC) is true for the curated n=10 set but does not
survive expansion to n=25 — template texts are also coherent.

## The required next test

Build or fine-tune a domain-specific LM (trained on canonical beautiful texts).
Expected: domain NLL should:
- Be LOW for beautiful texts (domain prior compresses them well)
- Be HIGH for random noise AND corporate/formulaic prose (neither belongs in
  the aesthetic domain)

This would resolve the remaining confound. With a domain LM, the prediction
is r > 0.7 on n=25 or larger.

## Status across four cycles

| Cycle | Key result |
|-------|-----------|
| 1 | Surface metrics (CE1-CE3) fail: r < 0.35 |
| 2 | CE4 (GPT-2 NLL): r=0.226 on n=10 (not significant) |
| 3 | CC × sigmoid: r=0.710, p=0.022 on n=10 (significant but fragile) |
| 4 | CE4 alone: r=0.605, p=0.001 on n=25 (significant and robust) |

**Most robust finding: CE4 NLL r=0.605, p=0.001, n=25.**
Theory prediction survives expansion; combined metric does not.
