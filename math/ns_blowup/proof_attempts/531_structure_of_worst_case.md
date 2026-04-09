---
source: STRUCTURE OF THE WORST CASE — what drives C negative
type: ANALYSIS — the perpendicular component interaction is the bottleneck
file: 531
date: 2026-03-30
instance: CLAUDE_OPUS (500s)
---

## THE WORST N=4 CASE (C/|ω|² = -0.172)

Config: k = [(-2,-2,0), (-2,-1,0), (-2,0,-1), (0,-1,0)]

| Mode | a_j | |b_j| | |b_j|²/a_j(|ω|-a_j) | Role |
|------|-----|-------|---------------------|------|
| 0 (|k|²=8) | 0.90 | 0.43 | 12% | Strongly aligned |
| 1 (|k|²=5) | 0.92 | 0.38 | 10% | Strongly aligned |
| 2 (|k|²=5) | 0.39 | 0.92 | 100% (TIGHT) | Weakly aligned |
| 3 (|k|²=1) | 0.39 | 0.92 | 100% (TIGHT) | Weakly aligned |

**Modes 2 and 3 are at the MAX CONDITION BOUNDARY**: |b|² = a(|ω|-a).

## CORRECTION DECOMPOSITION

C = C_aligned + C_cross + C_perp

| Component | Value | C/|ω|² contribution |
|-----------|-------|---------------------|
| C_aligned | +0.105 | +0.016 (always ≥ 0) |
| C_cross | -0.396 | -0.059 |
| C_perp | -0.868 | -0.129 |
| **Total C** | **-1.159** | **-0.172** |

**The perpendicular-perpendicular interaction (C_perp) is 75% of the total.**

## THE DOMINANT PAIR (2,3): θ = 90°

P_{23} = -0.697 contributes 60% of the total C.

This pair has:
- θ = 90° (orthogonal k-vectors, sin²θ = 1)
- Both modes at the tight perpendicular bound
- b₂ ≈ -b₃ (from perpendicular cancellation, since b₀+b₁ is small)
- (b₂·n̂)(b₃·n̂) ≈ -(b₂·n̂)² < 0 (opposite projections onto the pair normal)

## WHY C CAN'T REACH -5/16

The perpendicular cancellation Σb_j = 0 constrains how many modes can
have large perpendicular components with the same projection pattern.

For two modes b₂ ≈ -b₃ to maximally contribute negative P:
  P_{23} ≈ -(b₂·n̂)² ≤ -|b₂|² ≤ -a₂(|ω|-a₂) ≤ -|ω|²/4

(Using AM-GM: a(|ω|-a) ≤ |ω|²/4 with equality at a=|ω|/2.)

So one pair contributes at most -|ω|²/4 = -0.25|ω|² to C.
And 0.25 < 5/16 = 0.3125. One pair alone CAN'T break the barrier!

For C to reach -5/16: need ADDITIONAL negative pairs.
But: the perpendicular cancellation limits how many modes can have
large perpendicular components. Adding more "b-heavy" modes requires
their perpendicular parts to cancel, limiting the total negative C.

From the data: worst total C/|ω|² = -0.172, well within the -1/4 limit
from a single pair + the limited additional contributions.

## THE BOUND

**Conjecture**: C ≥ -|ω|²/4 at the max, for all N.

Evidence: worst observed -0.172 > -0.250 (margin 31%).

If proven: |S|²_F ≤ |ω|² → S²ê ≤ (2/3)|ω|² < 3|ω|²/4. KEY LEMMA.

This is STRONGER than the -5/16 threshold (gives |S|² < |ω|² instead of < 9|ω|²/8).

## 531. Worst case driven by perp-perp interaction of boundary modes.
## One pair contributes at most -|ω|²/4. Perp cancellation limits the rest.
## Conjecture C ≥ -|ω|²/4 (margin 31%). Would give Key Lemma.
