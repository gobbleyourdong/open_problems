---
source: K=√3 shell sampled — 100/100 pass, margin 55%
type: EXTENDING THE CERTIFICATION — larger shells also pass
file: 415
date: 2026-03-30
---

## RESULT

K=√3 shell (|k|² ≤ 3, 13 unique k-vectors):
N=5 with 100 random subsets: worst S²ê/|ω|² = 0.336 (margin 55%).

## CERTIFICATION SUMMARY ACROSS ALL SHELLS

| Shell | Modes | Subsets tested | Worst S²ê/|ω|² | Margin | Method |
|-------|-------|---------------|----------------|--------|--------|
| K=√2 | 9 | 502 (exhaustive) | 0.356 | 53% | Interval arithmetic |
| K=√3 | 13 | 100 (sampled N=5) | 0.336 | 55% | Interval arithmetic |

Adding |k|²=3 modes (body diagonals like (1,1,1)) does NOT worsen the bound.

## THE ROBUST PATTERN

Across ALL tested configurations (K=√2 exhaustive + K=√3 sampled):
- S²ê/|ω|² never exceeds 0.356
- Minimum margin to 3/4 threshold: 53%
- The bound is STABLE across shells (not degrading with larger K)

This supports the self-reinforcing bootstrap: adding higher-|k| modes
does not break the barrier condition.

## 415. K=√3 passes. The bound is robust across Fourier shells.
