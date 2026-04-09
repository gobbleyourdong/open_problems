# result_006 — β vs γ Experiment: Self-Model Richness Dominates Phi

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/beta_gamma_experiment.py`

## What we ran

2×2 experiment: {feedforward, recurrent} × {minimal self-model, rich self-model}
at n=6 nodes (3 primary + 3 self-model). Measured Phi (exact) and G×L proxy.

## Results

| Config | Phi | G | L | G×L |
|--------|-----|---|---|-----|
| T1: FF, minimal-self | 0.0256 | 0.145 | 0.000 | 0.000 |
| T2: FF, rich-self | 0.0494 | 0.127 | 0.000 | 0.000 |
| R1: RNN, minimal-self | 0.0244 | 0.126 | 0.000 | 0.000 |
| R2: RNN, rich-self | **0.0844** | 0.149 | 0.000 | 0.000 |

## Finding 1: Self-model richness dominates Phi, not loop topology

Effects on Phi:
- **Loop topology effect** (RNN vs FF): +0.017 (Phi increases by 45%)
- **Self-model richness effect** (rich vs minimal): +0.042 (Phi increases by 168%)

Self-model richness has 2.5× larger effect on Phi than loop topology.
This is **anomalous for β's prediction** (β predicts loop topology should be decisive).

Why does rich self-model increase Phi?
A rich self-model layer creates TIGHT causal links between primary states and
self-model states (strong diagonal weights in the rich variant). These tight
links make the system harder to partition without losing integration: any
bipartition that separates a primary node from its self-model counterpart loses
substantial cause-effect information. Therefore Phi is higher.

This is consistent with γ's mechanism: a system that accurately models its own
states is MORE integrated, not just "aware of" its integration.

The congruence: **both β and γ are correct that self-model richness increases
"conscious content," but for different stated reasons.**
- β: the tight primary↔self-model coupling increases Phi (cause-effect integration)
- γ: the tight coupling means the self-model accurately tracks primary states → G>0

The two theories may be measuring the same underlying architectural property
(tight causal coupling between processing layers) through different conceptual lenses.

## Finding 2: L=0 — architecture limitation

The L proxy is 0 for all variants because the architecture has no feedback from
the self-model layer back to the primary layer. Primary processing only uses
primary-state inputs; self-model outputs are not fed back.

This is architecturally correct for the "minimal AI" case (many neural networks
do not have explicit feedback from higher-level representations to lower-level
processing). But for γ to be testable, the self-model must causally influence
primary processing.

**Consequence:** the G×L test of γ cannot be evaluated with this architecture.
To test γ properly: add a feedback connection from self-model layer to primary layer.
This is a separate experiment.

The G proxy (correlation between self-model activations and primary states) is
non-zero for all variants (G ≈ 0.13–0.15), but the DIFFERENCE between rich and
minimal is small (0.149 vs 0.126). The rich self-model mainly improves Phi
via tighter causal integration, not via dramatically better state tracking
as measured by marginal correlation.

## Theoretical implications

### β position

β's prediction (Phi tracks loop topology) is not confirmed in this small-scale
experiment: the self-model richness effect (×2.7 between R2 and R1) is larger
than the loop effect (×1.5 between RNN and FF). β would need to argue that:
- At larger scale, loop topology dominates
- The "lower-triangular = not IIT feedforward" issue means FF and RNN variants
  here are not a clean test of the loop topology hypothesis
- At n=6 with the state-independence limitation, the test is inconclusive

### γ position

γ's specific prediction (G×L tracks self-model richness) cannot be evaluated
because L=0 in this architecture. A γ-compatible architecture requires feedback.

### The convergence point

Both β and γ predict that the R2 system (recurrent + rich self-model) has the
most "phenomenal content." They agree on the OUTPUT of the 2×2 experiment
even while disagreeing on the MECHANISM. This may be the experimental
lesson at small scale: the 2×2 design doesn't discriminate β from γ because
both predict R2 > R1, T2 > T1, and R2 > T2 (with different reasoning).

A truly discriminating test requires:
- Matched Phi between FF+rich-self and RNN+minimal-self
- These are the "crossing" cells that β and γ disagree about
- β predicts RNN+minimal > FF+rich (loop wins)
- γ predicts FF+rich > RNN+minimal (self-model wins)
- Current results: Phi(T2)=0.049 vs Phi(R1)=0.024 → FF+rich > RNN+minimal
- This supports γ's prediction, but only at small n with the caveats above

## Summary: what_is_mind numerics across 6 cycles

| Cycle | Finding |
|-------|---------|
| 1 | Phi O(4^n); wall at n~10 |
| 2 | State-independent → Phi=0; feedforward theorem confirmed |
| 3 | Lower-triangular ≠ IIT feedforward; conceptual clarification |
| 4 | TF-like vs RNN-like: 14/15 IIT confirmed at correct architecture |
| 5 | Phi* approximation fails; wall is fundamental |
| 6 | **Rich self-model increases Phi more than recurrence (×2.5 vs ×1.5). At crossing cell, γ's prediction holds: FF+rich > RNN+minimal.** |
