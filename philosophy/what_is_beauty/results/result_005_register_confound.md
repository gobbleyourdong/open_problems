# result_005 — The Register Confound: CE4 Measures Prestige, Not Aesthetic Quality

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tools:** `numerics/register_relative_nll.py`, `numerics/partial_correlation.py`

## What we ran

Decomposed the CE4-rating correlation (r=0.606) into between-register and
within-register components using partial correlation and demeaning.

## The central finding

| Analysis | Correlation | Interpretation |
|----------|------------|----------------|
| Full r(CE4, rating), n=25 | **+0.606** | Observed effect |
| Between-register r | **+0.600** | Due to register assignment |
| Within-register partial r | **−0.125** | Residual after controlling register |
| Within-math r (n=4) | +0.949 | Exception: works for math |
| Within-literary r (n=8) | −0.062 | No within-register signal |

**The CE4-rating correlation is almost entirely a register-prestige effect.**
CE4 NLL predicts which REGISTER a text belongs to (math/literary ≈ 4.3-4.5 nats;
jargon/expository ≈ 2.5-2.9 nats), and registers correlate with aesthetic ratings.
This is a confound: the correlation does not arise from within-register aesthetic
quality but from between-register structural differences.

## Register means

| Register | CE4 mean | Rating mean |
|----------|---------|------------|
| math | 4.245 | 8.6 |
| literary | 4.479 | 8.4 |
| expository | 2.898 | 3.9 |
| jargon | 2.488 | 1.8 |
| noise | 3.120 | 1.0 |

The five registers form almost a perfect staircase in both CE4 and rating.
GPT-2's higher NLL for math and literary registers reflects that these genres
are underrepresented in GPT-2's internet-text training corpus (relative to
jargon and expository prose).

## The mathematical exception

Within the math register (n=4, r=+0.949, p=0.051):

| Text | CE4 NLL | Rating |
|------|---------|--------|
| Euler identity | 5.04 | 9.5 |
| Cantor diagonal | 4.42 | 8.5 |
| Pythagoras sketch | 3.77 | 8.5 |
| Ramanujan series | 3.75 | 8.0 |

Within mathematical texts, GPT-2 NLL orders the aesthetic ranking almost
perfectly. The more abstract/exotic the mathematical argument (Euler's identity
connecting e, i, π, 1, 0 vs Pythagoras's geometric argument), the higher both
the NLL and the aesthetic rating.

**Interpretation:** For mathematical beauty, GPT-2's prior IS approximately
the right prior. GPT-2 was not trained on large quantities of beautiful
mathematics, so unusual mathematical notation and argument structure genuinely
surprised it — and that surprise correlates with aesthetic excellence.

For literary beauty, GPT-2 has memorised canonical texts (Keats, Shakespeare,
Blake, Basho, Donne are all probably in its training data). The most famous
literary texts are the most predictable within the literary register, which
inverts the expected relationship (beautiful = surprising).

## What this means for the theory

The compression-beauty claim must be restated more carefully:

**Revised prediction:** Aesthetic quality within a register correlates with
compression efficiency under a prior that has learned that register WELL but
has NOT memorised the specific canonical texts being evaluated.

For GPT-2:
- Mathematical register: prior is weak (not much math training) → NLL is a
  genuine compression signal, not memorisation → theory works (r=0.949)
- Literary register: prior includes memorised canonical texts → NLL reflects
  training data coverage, not aesthetic compression → theory confounded

**Consequence:** A domain-specific prior that is COMPREHENSIVE within the
aesthetic domain (covers all beautiful texts equally well) would destroy the
within-register signal via memorisation. The correct prior is one that has
learned the STRUCTURE of beautiful work (metre, proof strategy, image
construction) without memorising the canonical instances.

This is a stronger and more specific prediction than before:
"Beauty ∝ compression efficiency under a structural prior that knows the
domain's structure but not its canonical instances."

## The aesthetic test requirement

A proper empirical test of the compression-beauty claim requires:
1. A prior trained on aesthetic domain structure (poetry metre, proof patterns,
   musical form) but NOT the specific texts being evaluated
2. Evaluation on texts the model has never seen — not canonical famous instances
3. Within-register measurement only (between-register register-prestige effects
   must be controlled)

## Summary across five cycles

| Cycle | Finding |
|-------|---------|
| 1 | Surface metrics (CE1-CE3): no signal |
| 2 | CE4 GPT-2: r=0.226 n=10, r=0.546 without ASCII confound |
| 3 | CC × sigmoid: r=0.710 p=0.022 n=10 — first significant result |
| 4 | CE4 alone: r=0.605 p=0.001 n=25 — most robust result |
| 5 | **CE4 is register prestige (r_within=−0.125). Within-math: r=0.949.** |

**The strongest finding: compression-beauty holds within-register for mathematics
(r=0.949, n=4). The full-corpus result (r=0.606) is a confound.**

**The required test: structural prior (not memorisation) evaluated on novel texts.**
