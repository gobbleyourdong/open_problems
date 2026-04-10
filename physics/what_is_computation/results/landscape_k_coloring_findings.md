# landscape_k_coloring — Cycle 2 Odd findings

**Date:** 2026-04-09
**Driver script:** `numerics/landscape_k_coloring.py`
**Output data:** `results/landscape_k_coloring_data.json`

## Purpose

The Cycle 1 Odd work reproduced the find/verify asymmetry measurements
from `pnp_compression_asymmetry.py`. Cycle 2 Odd asks whether the
K-trajectory fingerprint established for 3-SAT in `landscape_k.py`
(decreasing K = easy, flat K = hard) generalizes to a different
NP-complete family: 3-graph-coloring.

## Setup

- Guaranteed-3-colorable random graphs built by partitioning nodes into
  3 color classes and sampling edges only between distinct classes.
- Two edge-density regimes: 1.5·n (sparse, easy) and 2.3·n (near the
  3-coloring phase transition at ~2.35·n).
- Sizes: n = 20, 30. Three instances per (n, density) config.
- Backtracking with 50k-step budget and K-proxy recording every 3 steps.
- K-proxy = gzip ratio of the bytes encoding edges whose endpoints are
  not yet both assigned (the "unresolved edge" sub-graph).

## Raw results

| config               | decisions | K_init | K_final | trend   | solved |
|----------------------|----------:|-------:|--------:|:-------:|:------:|
| easy-20 (ρ=1.5)      |      32.7 |  0.75  |   1.85  |  ↑      |  3/3   |
| hard-20 (ρ=2.35)     |     227.7 |  N/A   |   N/A   |  —      |  3/3   |
| easy-30 (ρ=1.5)      |      92.7 |  N/A   |   N/A   |  —      |  3/3   |
| hard-30 (ρ=2.35)     |  30,610.0 |  0.62  |   0.92  |  ↑      |  2/3   |

## Headline: the fingerprint does NOT cleanly transfer

Both measurable regimes (easy-20 and hard-30) show K-proxy INCREASING
during search, not decreasing. This contradicts the SAT fingerprint of
"easy → K decreases." On its face, the result says the fingerprint is
SAT-specific.

## Measurement artifact caveat (the real story)

Reading the per-step trajectory shows that the K-proxy increases because
the encoded byte string SHRINKS as nodes get assigned — gzip's header
overhead then dominates and the ratio rises above 1.0. Example from
easy-20 instance 0:

```
step  3  |  unresolved edges encoded as 56 B  |  gzip ratio 0.75
step  6  |  unresolved edges encoded as 52 B  |  gzip ratio 0.77
step  9  |  unresolved edges encoded as 44 B  |  gzip ratio 0.82
step 12  |  unresolved edges encoded as 38 B  |  gzip ratio 0.89
step 15  |  unresolved edges encoded as 28 B  |  gzip ratio 1.20
```

For inputs under ~100 bytes, gzip is not measuring compressibility; it
is measuring format overhead. The K-proxy as designed for SAT does not
transfer because:

- SAT's `landscape_k.py` encodes clauses (many, each 2 bytes/literal);
  the encoded blob stays in the 200-2000 B range where gzip is stable.
- 3-coloring's unresolved edge set is much smaller (tens of bytes) and
  shrinks fast. The gzip signal is dominated by overhead, not content.

**Conclusion: this is a methodological dead-end, not a domain-specific
negative result.** The K-trajectory question for 3-coloring is still
open; the current proxy just doesn't answer it.

## What would answer the question

Two fixes, both deferrable to a future Odd cycle:

1. **Fixed-size state encoding.** Instead of encoding only unresolved
   edges, encode the FULL coloring state (one byte per node,
   sentinel for unassigned). Input size stays constant at n bytes
   regardless of how many nodes are assigned, so gzip ratio tracks
   actual structural content rather than format overhead.

2. **Non-gzip compression proxy.** Use LZMA with dict size 1, or a
   conditional-entropy estimator, or a literal Kolmogorov-Solomonoff
   approximation via prefix-code expected length. These are
   length-robust for small inputs.

The sharper claim we want to test is still:

> The K-content of the *search constraint state* (not the instance
> itself) follows a monotone decreasing path for easy problems and
> a flat/opaque path for hard problems, and this fingerprint is
> domain-general.

## Lane-discipline note

This is a Cycle 2 Odd output and an example of a Sigma v6 "Maps include
noise" commit. The dead-end is committed with full explanation rather
than deleted. The SAT K-trajectory fingerprint remains the live result;
the 3-coloring generalization is *untested*, not *refuted*.

## Status

Cycle 2 Odd complete (as a map feature, not as a positive result).
The next Odd cycle should either (a) fix the K-proxy with strategy 1
above or (b) move to a third problem family (e.g. Hamiltonian cycle or
subset-sum search) where the existing byte-level proxy is stable.
