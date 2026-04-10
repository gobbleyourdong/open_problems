# landscape_k_coloring_v2 — Cycle 4 Odd (loop 2) findings

**Date:** 2026-04-09
**Driver:** `numerics/landscape_k_coloring_v2.py`
**Data:**   `results/landscape_k_coloring_v2_data.json`
**Prior:**  `results/landscape_k_coloring_findings.md` (Cycle 2 Odd, V1)

## Purpose

Cycle 2 Odd found that the V1 K-proxy on 3-coloring (gzip of
unresolved-edges bytes) produced a spurious "K increasing" signal
because the unresolved-edge blob shrank below the size at which gzip
is stable. Cycle 4 Odd applies the fix recommended in V1's findings:
encode the FULL coloring state as n bytes, with sentinel 255 for
unassigned nodes and 0/1/2 for assigned colors. Length is constant at n
for the entire search, so gzip overhead is a time-invariant bias.

## Raw results

| config           | instances | K_init | K_final | K_slope     | trend      | solved  |
|:-----------------|----------:|-------:|--------:|------------:|:-----------|:-------:|
| easy-30 (ρ=1.5)  |     3     | 0.833  |  1.322  | +0.001043   | increasing | 3/3     |
| hard-30 (ρ=2.35) |     3     | 0.833  |  1.356  | +0.000175   | flat-ish   | 3/3     |
| easy-50 (ρ=1.5)  |     3     | 0.500  |  0.927  | +0.000161   | flat-ish   | 3/3     |
| hard-50 (ρ=2.35) |     3     | 0.500  |  0.813  | +0.000019   | flat       | 0/3 (budget) |

## Headline: the V1 artifact is gone, but a new one has replaced it

The fixed-size encoding removes the gzip-overhead artifact — K_proxy
values are now in a plausible 0.5–1.4 band rather than drifting above
1.0 due to format bias. But the SAT fingerprint (easy → K decreasing,
hard → K flat) still does NOT appear. All four configurations show
small positive slopes, dominated by the fact that the initial
all-sentinel state is the most compressible the state will ever be
(a single repeated byte), and every subsequent assignment introduces
entropy.

Per-instance trajectories confirm the pattern:

```
easy-30 inst 0: 0.83 → 0.87 → 0.97 → 1.00 → 1.10 → 1.20 → 1.23 → 1.27 ...
hard-30 inst 0: 0.83 → 0.93 → 0.93 → 1.03 → 1.07 → 1.13 → 1.13 → 1.20 ...
```

Both trajectories rise from the constant-sentinel floor to a stable
mixed-value band within the first ~8 records, then fluctuate. Easy and
hard look essentially the same.

## Diagnosis: what the proxy is actually measuring

The V2 K-proxy measures **assignment progress** (how many bytes have
been converted from sentinel to 0/1/2), not **landscape opacity** (how
much structure remains in the constraint problem). Assignment progress
is a monotone increasing variable in backtracking, so the K-proxy's
initial trajectory is dominated by "state transitioning from
homogeneous (low K) to heterogeneous (higher K)." This swamps any
landscape-opacity signal.

For 3-SAT, `landscape_k.py` measures REMAINING CLAUSES (bytes encoding
the unresolved constraint set). When unit propagation works, clauses
collapse rapidly, the constraint set shrinks and becomes more
compressible (repeating patterns), K decreases. When propagation
stalls, clauses don't collapse, K stays flat. This is a LANDSCAPE
signal because the clauses ARE the constraint landscape.

For 3-coloring backtracking, the partial assignment IS the state
(there's no separate constraint list that collapses as search
progresses). The edges never go away; only the assigned nodes change.
Encoding the state directly captures "how much has been assigned," not
"how much constraint remains."

**Conclusion: the K-trajectory fingerprint as measured on SAT via
clause collapse does NOT port to 3-coloring backtracking without a
fundamentally different proxy design.** Not a gzip artifact (that's
fixed); a structural mismatch between what the proxy measures and
what the fingerprint captures.

## What would actually work (Cycle 5 Odd target)

Two candidates for a proxy that captures landscape opacity, not
assignment progress:

1. **Conflict-neighborhood entropy.** At each decision point, for each
   unassigned node, compute the count of "forbidden" colors (colors
   already used by assigned neighbors). Encode the histogram of forbidden-
   color-counts as bytes and gzip it. Compressibility measures how
   structured the remaining constraint is. For easy instances, the
   histogram becomes skewed quickly (unit-propagation analog); for hard
   instances, it stays uniform (no gradient).

2. **Solution-distance proxy.** Run the solver with a hidden oracle that
   knows the target coloring. At each step, encode the XOR-difference
   between current partial assignment and target. For easy instances,
   the difference should decrease monotonically via heuristic hints;
   for hard instances, it should fluctuate.

Option 1 is closer to SAT's measurement (both look at CURRENT
constraint structure, not FINAL answer) and is recommended.

## What this cycle produces as a positive result

- **Confirms** the V1 gzip-overhead artifact is real and fixable.
- **Refutes** the naive-fixed-size-encoding hypothesis.
- **Diagnoses** that the K-trajectory fingerprint measures constraint
  collapse, which needs a constraint-side proxy, not a state-side one.
- **Targets** a specific next-cycle experiment: conflict-neighborhood
  entropy on 3-coloring.

This is an honest Sigma "Map includes noise" Cycle-4-Odd output — the
dead-end is fully characterized and the next attack vector is named.

## Status

Cycle 4 Odd complete (as a second map feature — the V2 proxy is also
unsuitable, but now for a different and structurally-diagnosable
reason). Cycle 5 Odd will implement the conflict-neighborhood-entropy
proxy, or else pivot to a third NP family (Hamiltonian cycle) whose
state IS more constraint-like.
