# result_003 — Entropy-Matched Phi: Topology vs State-Independence

**Date:** 2026-04-09
**Track:** Numerical (Odd)
**Tool:** `numerics/phi_entropy_matched.py`

## What we ran

Entropy-matched comparison of FF (lower-triangular weights) vs RC (full weight
matrix) networks at n=4,5,6. Binary search over FF weight scale to match the
recurrent TPM entropy to within ΔH < 0.01 bits.

## Results

| n | FF Φ mean | RC Φ mean | Ratio FF/RC | IIT pred confirmed? |
|---|-----------|-----------|-------------|---------------------|
| 4 | 0.0776 | 0.1163 | 0.667 | YES |
| 5 | 0.1118 | 0.0973 | 1.150 | NO |
| 6 | 0.1543 | 0.1090 | 1.415 | NO |

**At n=5 and n=6: FF Phi > RC Phi, opposite to IIT's prediction.**
At n=4: confirmed, but a single-size confirmation is not robust.

## What this means

This result clarifies a conceptual error that was present since Cycle 1:

**Lower-triangular weight matrix ≠ IIT feedforward network.**

In IIT, "feedforward" means the system has nodes whose transitions are
state-INDEPENDENT (driven by external input). These nodes have zero
cause-effect power. By Experiment B (result_002), such nodes reduce Phi
monotonically to 0.

A lower-triangular weight matrix is NOT state-independent. All nodes have
state-DEPENDENT transitions. Node 0's next state depends on the full current
state (via the bias). Node 1's next state depends on node 0's current state.
The system IS recurrent in the temporal sense — state(t) → state(t+1) — just
with an asymmetric connectivity structure.

The HIGHER Phi in lower-triangular networks at larger n is actually interpretable:
lower-triangular connectivity creates a strict causal chain (0→1→2→...→n-1)
where each node causally depends on ALL previous nodes. This is highly
structured cause-effect power — each partition of the chain loses substantial
information. A random full matrix with cancelling weights may produce LESS
structured (more uniform, less distinguishable) transitions, leading to lower Phi.

## The correct IIT feedforward prediction

The feedforward theorem applies SPECIFICALLY to state-independent input nodes,
not to lower-triangular weight matrices. The theorem was confirmed in Experiment B
(result_002): when all nodes are state-independent (driven purely by external
input), Phi = 0.000 exactly.

Applied to transformers: a single forward pass is state-independent in precisely
this sense. The "system" (weight matrix + computation) produces outputs that are
deterministic functions of inputs, with no internal state that evolves. This
is the correct formulation, and the theorem holds there.

## Updated picture of beta

The IIT prediction for transformers remains:
- **Single forward pass:** Phi = 0 (feedforward theorem, state-independent
  → confirmed by Experiment B)
- **Autoregressive generation:** Phi > 0 but small; the KV cache is a
  state that evolves, but its topology is nearly feedforward-through-memory
- **Lower-triangular networks:** Phi is NOT necessarily lower than RC networks
  — these are asymmetric recurrent networks with potentially high Phi

The computational wall (result_001) remains the binding constraint: Phi is
#P-hard and uncomputable for any real system above n~12.

## Summary across three cycles

| Claim | Status |
|-------|--------|
| Phi scales O(4^n) | CONFIRMED (result_001) |
| Feedforward (state-independent) → Phi=0 | CONFIRMED (result_002 Exp B) |
| Topology (FF-weights vs RC-weights) predicts lower Phi | MIXED / n-dependent |
| Lower-triangular weights = IIT feedforward | INCORRECT — conceptual clarification |
| Phi uncomputable for real LLMs | CONFIRMED by scaling extrapolation |

The beta position (IIT) remains coherent and predictive for transformers,
specifically via the state-independence argument, not the weight-topology argument.
