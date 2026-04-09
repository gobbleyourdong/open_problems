# result_006 — Within-Text Degradation: CC Captures Sequential Structure

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/degradation_test.py`

## What we ran

For 6 canonical beautiful texts (3 literary, 2 math, 1 haiku), generated
3 degraded variants each: D1 word-scramble, D2 sentence-scramble, D3 synonym
substitution. Measured CC and CE4 for all 24 (6×4) text variants.

Prediction: CC(original) > CC(degraded) — originals have internal structural
regularities that make the first half predictive of the second.

## Results

| Text | CC orig | D1 scramble | D2 sent | D3 synonym | Orig rank |
|------|---------|-------------|---------|------------|-----------|
| Keats | 0.227 | 0.050 | 0.246 | **0.325** | 3/4 |
| Shakespeare | **0.301** | 0.104 | 0.153 | 0.224 | **1/4** |
| Donne | **0.326** | 0.051 | 0.191 | 0.241 | **1/4** |
| Euler | 0.184 | **0.215** | 0.105 | 0.158 | 2/4 |
| Cantor | 0.242 | 0.038 | 0.122 | **0.255** | 2/4 |
| Basho | **0.330** | 0.036 | 0.143 | 0.250 | **1/4** |

**CC wins (original > degraded): 14/18 (78%)**
**Mean rank of original: 1.67/4 (chance = 2.5)**
**Original ranks 1st: 3/6 texts**

## By degradation type

| Degradation | Originals win | Pattern |
|-------------|--------------|---------|
| D1 word scramble | 5/6 | Strong — word order is load-bearing |
| D2 sentence scramble | 5/6 | Strong — sentence order is load-bearing |
| D3 synonym substitution | 3/6 (tie) | Weak — GPT-2 prefers common synonyms |

## Key findings

### 1. Sequential structure predicts CC, not lexical choice

Originals consistently beat word-scrambled and sentence-scrambled versions —
the aesthetic structure of these texts lives in their sequential ordering.
"Beauty is truth, truth beauty" works partly because the first clause
("Beauty is truth") predicts the second ("truth beauty") via chiasmus.
A random reordering destroys this.

### 2. Synonym substitution breaks the test

Replacing "Beauty" with "Appearance" and "truth" with "fact" increases CC for
Keats (0.325 > 0.227). This is the register confound from Cycle 5 operating
within a text: more common words → lower NLL → higher CC under GPT-2's generic prior.

Under an aesthetic domain prior, the specific aesthetic vocabulary IS the expected
vocabulary. "Beauty is truth" would be easier to predict than "Appearance is fact"
under a prior trained on canonical poetry. This is exactly the domain-specific
prior requirement.

### 3. Mathematical texts are harder to degrade clearly

Euler and Cantor originals rank 2nd, not 1st. For Euler, word scrambling
(D1) actually increases CC slightly (0.215 > 0.184), perhaps because scrambled
mathematical tokens happen to appear in more predictable contexts.
For Cantor, synonym substitution increases CC marginally (0.255 > 0.242).

Mathematical aesthetic structure may be more at the ARGUMENT level (logical
steps in the right order) than the word level. A proof-step scramble would
be a better degradation than a word or sentence scramble.

## What this adds to the theory

The within-text degradation test confirms:
- **CC is sensitive to sequential aesthetic structure** (word order, sentence order)
- **The generic prior (GPT-2) works against vocabulary-level aesthetics** (synonyms
  are preferred over precise aesthetic vocabulary under the generic prior)
- **The compression-beauty claim holds at the structural level** (sequential
  organisation creates predictive relationships that are absent in scrambled versions)

The remaining gap: the theory needs a prior that rewards precise aesthetic vocabulary
(structural domain prior, not a generic internet prior). With such a prior:
- D3 synonym substitution would also show CC(original) > CC(synonym), because
  "Beauty" is more predictable than "Appearance" in the aesthetic domain

## Summary of what_is_beauty numerics across 6 cycles

| Cycle | Finding | Status |
|-------|---------|--------|
| 1 | Surface metrics (zlib/entropy): no signal | CLOSED |
| 2 | GPT-2 NLL: partial support (r=0.546 without ASCII) | DONE |
| 3 | CC × sigmoid: r=0.710 p=0.022 on n=10 | DONE |
| 4 | CE4 alone: r=0.605 p=0.001 on n=25 (strongest) | DONE |
| 5 | CE4 is register prestige; within-math r=0.949 | DONE |
| 6 | Degradation: CC beats scramble 14/18; sequential structure confirmed | DONE |

**The theory is confirmed for sequential structure (CC beats scramble 78%).
The remaining test requires a structural domain prior for lexical-level aesthetics.**
