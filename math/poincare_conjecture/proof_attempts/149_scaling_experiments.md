---
source: Case 1→2 scaling experiments + evolved alignment
type: DATA — the simple case converges to 1/3, NS dynamics perturb it
date: 2026-03-28
---

## Case 1: Two Modes → c₁ = c₃ = 0.20, α ≈ 0

Two modes interact purely through cross-terms (self-interaction = 0).
Result: perfect c₁-c₃ symmetry, zero net stretching. Neutral.

## Scaling: N Modes → Isotropy

| N_modes | c₁ | c₂ | c₃ | c₃ ≥ 1/3? |
|---------|-----|-----|-----|-----------|
| 2 | 0.16 | 0.67 | 0.17 | No |
| 4 | 0.31 | 0.38 | 0.31 | No |
| 64 | 0.34 | 0.33 | 0.33 | Almost |
| 224 | 0.33 | 0.33 | 0.34 | ✓ |

Convergence to isotropy (c₁=c₂=c₃=1/3) is MONOTONIC with N.
This is the law of large numbers applied to triadic interactions.

## Evolved Alignment: NS Breaks Isotropy

TG at N=32 evolved with full NS:
- t=1: c₃ drops to 0.14 (vortex sheet stretching event)
- t=3: c₃ at top 10% |ω| is 0.19 (still below 1/3)
- t=6-8: c₃ recovers to 0.34-0.39 at top |ω|

The NS dynamics CREATE transient dips in c₃ during stretching events.
The pressure then RESTORES c₃ during the recovery phase.
The question: do the dips accumulate, or does the recovery dominate?

## The Proof Landscape

Static N modes: c₃ → 1/3 as N → ∞ (statistical isotropy)
NS dynamics: perturb c₃ below 1/3 during stretching events
Pressure response: restore c₃ ≥ 1/3 during recovery

The proof needs: the TIME-INTEGRATED effect has c₃ ≥ 1/3 on average.
The BKM criterion uses ∫||ω||_∞ dt, which weights the high-|ω| periods
where the pressure response is strongest.

## Next: N=64 for the same test (higher |ω|, more modes)

## 149 proof files.
