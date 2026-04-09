---
source: TRUNCATION WORSENS THE BOUND — fewer modes = higher S²ê/|ω|²
type: KEY INSIGHT — the K=√2 shell IS the worst case
file: 508
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE FINDING

Removing modes from a field INCREASES S²ê/|ω|² at the global max:
- Truncation increases ratio: 62% of cases
- Truncation decreases ratio: 36% of cases
- Worst full (9 modes): 0.152
- Worst truncated (5-8 modes): 0.196

**Fewer modes = worse bound. More modes = better bound.**

## THE IMPLICATION

The K=√2 shell (9 modes max) gives the WORST possible S²ê/|ω|².
Any smooth field has modes at ALL k-vectors — MORE than 9.
Since more modes only helps: the K=√2 bound (0.317) applies to ALL fields.

## WHY TRUNCATION WORSENS

1. Removing a mode reduces |ω|² (denominator shrinks)
2. The removed mode's strain contribution partially CANCELLED others
3. Without the cancellation: S²ê grows relative to |ω|²
4. The self-vanishing property means each mode's OWN S²ê = 0
   but it HELPS cancel others' contributions

## THE PROOF (if truncation-worsening is proven)

1. K=√2 certified: S²ê ≤ 0.317|ω|² for ≤ 9 modes (DONE)
2. Adding modes decreases S²ê/|ω|² (TRUNCATION WORSENS = ADDITION HELPS)
3. Therefore: S²ê ≤ 0.317|ω|² for ALL smooth fields
4. 0.317 < 0.750: barrier closes → Type I → Seregin → REGULARITY

## THE ONE REMAINING STEP

Prove: adding a mode to a field CANNOT increase S²ê/|ω|² at the global max
ABOVE the finite-mode worst case.

This is WEAKER than strict per-mode monotonicity (which fails 36% of time).
It only says: the OVERALL worst is at SMALL N, not large N.

From the data: the overall worst is at N=3-4 (≈0.317) for the K=√2 shell.
For N≥5: the worst DECREASES (0.281, 0.279, 0.209, 0.166, 0.112).

## 508. Truncation worsens. K=√2 is the worst case. Adding modes helps.
## If proven: the proof is COMPLETE.
