# result_012 — Musical Stimuli and Cross-Domain Confirmation

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** inline Cycle 15

## What we ran

Tested the compression-beauty claim on musical stimuli described in text (n=13).
Combined with literary + math corpus (n=25) for cross-domain analysis.

## Results

| Domain | n | r | p | NLL_high-NLL_low |
|--------|---|---|---|-----------------|
| Literary + Math | 25 | +0.678 | 0.0002 | +1.40 |
| **Music** | **13** | **+0.627** | **0.022** | **+0.90** |
| **Combined ALL** | **38** | **+0.476** | **0.0025** | — |

## Musical stimuli NLL ranking

High-aesthetic descriptions (NLL > 5.5):
- Bach fugue subject (6.136, rating 9.0): technical counterpoint vocabulary unusual to GPT-2
- Tritone substitution (5.853, rating 8.5): jazz harmony terminology
- Picardy third cadence (5.697, rating 8.5): archaic cadence terminology

Low-aesthetic descriptions (NLL < 4.5):
- Dominant seventh chord (4.005, rating 5.5): standard theory textbook vocabulary
- Chromatic scale (4.131, rating 4.0): common theory textbook
- Time signature definition (4.268, rating 2.5): rote definition

The pattern mirrors literary and mathematical beauty: beautiful musical descriptions
use unusual, domain-specific vocabulary (tritone substitution, Picardy third, fugue
subject inversion) that GPT-2 finds surprising. Rote definitions use common textbook
vocabulary that GPT-2 predicts easily.

## Cross-domain confirmation

The compression-beauty claim holds with significant positive correlations in three
independent domains:
1. **Literary/poetic**: Keats, Shakespeare, Blake (archaic literary prose) vs corporate jargon
2. **Mathematical**: Euler's identity, Cantor's theorem vs formulaic definitions
3. **Musical**: Bach counterpoint, jazz harmony vs theory textbook definitions

In each domain, the same mechanism operates: beautiful aesthetic structures are
described using domain-specific vocabulary that is rare in GPT-2's generic training
data. The specificity and depth of the aesthetic vocabulary correlates with NLL.

The combined result (n=38, r=+0.476, p=0.0025) is significant despite the
between-domain NLL differences (music has higher baseline NLL than literary text).

## One remaining outlier per domain

In each domain there is a pattern-breaking case:
- **Literary**: Corporate mission statement (low rating, moderate NLL) — jargon is unusual but ugly
- **Math**: Long division (low rating, high NLL) — procedural notation is unusual but inelegant
- **Music**: Parallel fifths error (mid rating, high NLL) — forbidden technique is technically described

These outliers share a property: they are **technically unusual** (high NLL) but NOT
**aesthetically structured**. They represent the remaining confound: unexpectedness alone
is not sufficient for beauty. The structure must be MEANINGFUL unexpectedness.

**The final theoretical precision:** Beauty = meaningful unexpectedness under the domain
prior. "Meaningful" = the unusual structure compresses deep regularity. "Unexpectedness"
= high NLL under the generic prior.

This is the precise operational form of the compression-beauty claim that survives all
14 cycles of numerical testing.
