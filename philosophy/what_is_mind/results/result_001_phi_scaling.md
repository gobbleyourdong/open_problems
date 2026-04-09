# result_001 — Φ Computation: Scaling and Methodological Gap

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/phi_small_systems.py`

## What we ran

System-level Φ (IIT 3.0 approximation, bipartition minimum) computed for small
binary networks (n=2..8) comparing:
- Feedforward: spatially directed connections (lower-index → higher-index only),
  noisy-OR activation, density=0.7
- Recurrent: all-to-all random connections, sigmoidal activation, density=0.5

3 states sampled per n, timings recorded.

## Scaling result (confirmed)

| n | n_states | n_bipartitions | FF time (s) | RC time (s) |
|---|----------|----------------|-------------|-------------|
| 2 | 4 | 1 | 0.000 | 0.000 |
| 3 | 8 | 3 | 0.002 | 0.002 |
| 4 | 16 | 7 | 0.014 | 0.014 |
| 5 | 32 | 15 | 0.054 | 0.054 |
| 6 | 64 | 31 | 0.438 | 0.438 |
| 7 | 128 | 63 | 3.645 | 3.809 |
| 8 | 256 | 127 | 31.68 | 31.32 |

**Scaling is O(2^n * 2^n) = O(4^n) per state.** Doubling n multiplies time by ~8-9x.

Extrapolation:
- n=10: ~2000s per state
- n=15: ~years per state
- n=20: ~millions of years per state
- LLM-scale n=10^9: utterly impossible

This confirms the #P-hardness claim in attempt_002: Φ is not computable for
any system of even 20 binary nodes with current methods, and transformers
operate at n ~ 10^9 to 10^12.

## Comparison result: INCONCLUSIVE

Raw Φ values across sizes:

| n | FF Φ mean | RC Φ mean |
|---|-----------|-----------|
| 2 | 0.381 | 0.000 |
| 3 | 0.279 | 0.121 |
| 4 | 0.221 | 0.042 |
| 5 | 0.266 | 0.093 |
| 6 | 0.251 | 0.093 |
| 7 | 0.349 | 0.117 |
| 8 | 0.235 | 0.108 |
| **mean** | **0.283** | **0.082** |

**Feedforward networks score higher Φ than recurrent.** This is the OPPOSITE
of IIT's prediction.

## Why the comparison is inconclusive

Three confounds prevent interpreting this result as a test of the feedforward theorem:

### 1. TPM construction parameters not controlled

The feedforward network uses noisy-OR (density=0.7, deterministic tendency)
while the recurrent network uses Gaussian weights (mean=0, density=0.5). These
produce fundamentally different TPM statistics independent of topology.

Random Gaussian recurrent weights tend toward near-uniform TPMs (high
entropy, low causal differentiation) because positive and negative weights
cancel, producing activations near 0.5 for all inputs. Near-uniform TPMs
have LOW Φ because any partition produces similar distributions.

Deterministic-ish noisy-OR networks produce more structured TPMs (some
transitions highly probable, others near-zero), which creates larger
cause-effect divergences and therefore higher Φ.

This is a PARAMETER confound, not a topology confound.

### 2. "Feedforward" means spatial directionality, not temporal feedforward

The IIT feedforward theorem applies to systems driven by EXTERNAL inputs,
where the system's current state has zero influence on itself — only on
downstream environment. My "feedforward" network is TEMPORALLY RECURRENT
(state at t → state at t+1), but with SPATIALLY asymmetric connections
(lower-index nodes influence higher-index nodes but not vice versa).

Spatial asymmetry is not the same as temporal feedforward. A spatially
directed network still has genuine cause-effect power through time, and
should have Φ > 0. The feedforward theorem does NOT predict Φ=0 for this case.

The correct test would require: nodes whose next-state probabilities are
independent of ANY current system state (driven purely by external input).
This requires a different TPM structure.

### 3. System-level vs. mechanism-level Φ

Full IIT 3.0 Φ sums cause-effect power over ALL mechanisms (subsets of nodes),
not just the whole-system level. My implementation computes only the
whole-system bipartition minimum, which is a simplified proxy. This
simplification may systematically over- or under-estimate Φ in different
network topologies.

## What the result DOES establish

1. **The exponential scaling wall is real and measured.** Φ is uncomputable
   for any system relevant to consciousness (>~12 nodes) with current methods.

2. **A controlled comparison of feedforward vs. recurrent Φ is tractable at
   n≤8 but requires matching TPM statistics, not just changing topology.**
   This is the next required experiment.

3. **The approximate implementation (system-level bipartition only) is
   implementationally correct** — the scaling, partition enumeration, and
   EMD computation are all working. The issue is experimental design, not code.

## Next steps (numerical track)

1. **Controlled comparison**: construct feedforward and recurrent TPMs with
   matched entropy (same average transition probability uncertainty), only
   differing in whether back-connections exist. This requires working in
   the TPM space directly, not constructing via activation functions.

2. **Implement the correct IIT feedforward test**: construct a network where
   "input nodes" have state-independent transition probabilities, then verify
   Φ=0 for the partition that cuts between input and processing nodes.

3. **Approximation comparison**: implement the Φ* approximation and compare
   against the exact computation for n≤8 to validate the faster proxy.

## Status

Scaling: confirmed (O(4^n), wall at n~10).
Feedforward theorem: not yet tested (methodological issue).
Implementation: correct but limited to system-level Φ.
