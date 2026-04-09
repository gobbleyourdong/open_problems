---
source: COMPREHENSIVE SHELL SURVEY — worst C/|ω|² for N=3 across 12 shells
type: DATA — the complete landscape of the correction bound
file: 459
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## THE DATA (N=3, optimized polarizations at vertex max)

| K² | Modes | Worst C/|ω|² | |S|²/|ω|² | Margin from -5/16 |
|----|-------|-------------|-----------|-------------------|
| 2 | 6 | -0.125 | 0.750 | 60% |
| 3 | 4 | -0.111 | 0.722 | 64% |
| 5 | 12 | **-0.165** | 0.830 | **47%** |
| 6 | 12 | -0.158 | 0.816 | 50% |
| 8 | 6 | -0.125 | 0.750 | 60% |
| 9 | 15 | -0.163 | 0.826 | 48% |
| 10 | 12 | -0.158 | 0.816 | 49% |
| 11 | 12 | -0.148 | 0.796 | 53% |
| 13 | 12 | -0.144 | 0.788 | 54% |
| 14 | 24 | -0.159 | 0.818 | 49% |
| 17 | 24 | -0.151 | 0.802 | 52% |
| 18 | 18 | -0.140 | 0.780 | 55% |

**Universal worst: K²=5, C/|ω|² = -0.165, |S|²/|ω|² = 0.830.**
**Threshold: -5/16 = -0.3125 (equivalently |S|²/|ω|² < 9/8 = 1.125).**
**Margin: 47%.**

## THE WORST CONFIGURATION (K²=5)

k-vectors: (-2,0,-1), (-2,1,0), (-1,0,-2)
Pairwise angles: 36.9°, 36.9°, 66.4°
cos(θ): 0.8, 0.8, 0.4
sin²(θ): 0.36, 0.36, 0.84

The 66.4° pair has sin²θ = 0.84 (near-orthogonal) which allows
a large negative correction. The two 36.9° pairs have sin²θ = 0.36.

## KEY OBSERVATIONS

1. **K²=5 is the worst shell** (not K²=2). Higher shells (K²≥8) are generally
   better, with worst C/|ω|² converging toward ~-0.15.

2. **The worst C/|ω|² stabilizes** across shells at approximately -0.165.
   It does NOT grow with K². The bound appears universal.

3. **The margin from -5/16 is at least 47%** across all shells tested.
   This is a ROBUST gap, not a tight bound.

4. **K²=2 and K²=8 are special**: their simpler geometry (all components
   from {0,±1,±2}) gives C/|ω|² = -1/8 exactly (the N=2 tight bound).

## THE PROOF TARGET

Prove: **C/|ω|² ≥ -5/16 at argmax|ω|² for any N ≥ 3 on any K-shell.**

Equivalently: **|S(x*)|²_F < (9/8)|ω(x*)|².**

The 47% margin suggests this is far from tight. A proof might show
C ≥ -1/6 or even C ≥ -1/5 (tighter than needed but more natural).

## THE GEOMETRIC MECHANISM

At the global max vertex, the sign pattern maximizes |ω|². This makes:
- D cross-terms POSITIVE (constructive interference)
- P cross-terms TEND POSITIVE (P ∝ sin²θ × D + correction)
- The correction (P - sin²θ D) can make P negative when in-plane
  projections override normal projections

The WORST case occurs when:
1. sin²θ is moderate (0.36-0.84) — enough for large correction
2. In-plane dot product v^∥·v^∥ exceeds D (making P < 0)
3. The constructive sign pattern at the max ALSO makes the negative P terms add

But the constructive interference that makes |ω|² large ALSO limits
how negative C can be (since C depends on the SAME sign pattern).

## 459. Complete shell survey: worst C/|ω|² = -0.165 (K²=5).
## Threshold -5/16. Margin 47%. Stable across 12 shells.
## The geometric mechanism is understood. Formal proof remains.
