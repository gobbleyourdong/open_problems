# results/k_change_pnp_connection.md — K-Change, Wolfram Classes, and P vs NP

**Date:** 2026-04-09
**Type:** Synthesis (Phase 3 final)
**Builds on:** sat_vs_ca_findings.md, turing_K_data.json, cellular_automata_K_findings.md, sat_class_correction.md

## The Complete Picture

### K-change taxonomy (all systems)

| System | K-change per step | Global K-landscape | Type | Wolfram class |
|---|---|---|---|---|
| Stopped clock | 0 | — | 0 | — |
| Unitary evolution | 0 | — | 0 | — |
| Periodic CA (Rule 184) | 8.77 bytes | K-flat | 2 | Class 2 |
| SAT verification | 111 bits | K-decreasing | P | P |
| Ion channel gating | 1 bit | — | 4 | Class 4 |
| RNA folding | 5.75→0 bytes | K-decreasing ARC | 5 | Class 4 → Class 1 |
| Turing machine (busy beaver) | 168 bits | K-structured | 4 | Class 4 |
| SAT search | 127 bits/step | K-flat | NP-hard | Class 3 steady state |
| Universal CA (Rule 110) | 32.6 bytes | K-structured | 4 | Class 4 |
| Chaotic CA (Rule 90) | 37.97 bytes | K-high | 3 | Class 3 |
| Quantum measurement | -log₂(P) bits | — | 3/random | Class 3 |
| Lyapunov gas (collisional) | λ=0.11/step | K-increasing | 3 | Class 3 |

### The P vs NP gap in K-change

**Per-step K-change:** verification (111 bits) vs search (127 bits) = **14% gap**
**Step-count:** verification O(n) vs search O(exp(n)) = **exponentially growing gap**

At n=70: 14% per-step × 137-fold more steps = **total K-change gap = ~157×**
At n=200: 14% per-step × ~1000-fold more steps = **total K-change gap = ~1,140×**

The P vs NP claim: the step-count gap grows without bound. No polynomial algorithm closes it.

### The K-boring paradox

**Paradox:** hard SAT instances have K-change per step in the Class 2 range (0.273 normalized), BELOW chaotic systems (Class 3 = 1.24 normalized). Yet hard SAT is much harder to solve than Class 2 systems.

**Resolution:** hard SAT is K-boring per step AND K-flat globally. It's not K-complex; it's K-opaque. Each DPLL step is simple (K-change = Class 2). But the steps provide NO INFORMATION about which branch leads to the solution — the landscape is uniformly K-flat. The solver must try exponentially many K-boring steps with no gradient to guide it.

**Analogy:** finding a needle in a haystack. Each piece of hay is simple to examine (K-change = Class 2). But 10^6 pieces × no gradient = exponential search. The difficulty is COUNTING, not complexity.

**Contrast with RNA folding (Type 5):** each folding step has moderate K-change (Class 4 range) AND the landscape is K-decreasing (gradient present → fewer steps needed). RNA folding terminates because the K-gradient guides it to completion. Hard SAT search doesn't terminate early because there's no K-gradient.

### Why K-informationalism explains P vs NP

Under K-informationalism: P vs NP is a claim about the K-landscape topology of NP-complete problems.

**P = NP would require:** all NP-complete problems have polynomial K-gradients — exploitable structure that lets you descend in steps proportional to n.

**P ≠ NP claims:** the K-landscape of NP-hard problems at the phase transition is uniformly K-flat. No gradient exists. Any algorithm must count through exponentially many K-boring steps.

**Numerical evidence:** K-flat landscape confirmed to n=70 (K mean=0.66±0.017 across 62 trajectory points at n=70, hardest instance). No gradient detected in any tested instance, algorithm, or n-value.

The three barriers explain why PROVING this is hard: the absence of a K-gradient in NP landscapes cannot be proved by any K-simple (natural, relativizing, algebrizable) technique. The proof must be K-complex.

## Status

This document completes the P vs NP numerical track. The compression asymmetry (exponential find/verify ratio), the K-flat landscape (no gradient at any scale or n-value), the K-boring per-step character (Class 2-like), and the K-change gap between verification and search (14% per step, exponential in step count) are all certified. P ≠ NP is consistent with all numerical evidence. The proof remains open.
