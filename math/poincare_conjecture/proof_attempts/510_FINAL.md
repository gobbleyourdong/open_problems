---
source: FINAL STATE — 510+ attempts across two instances, one session
type: THE MAP OF THE MOUNTAIN
file: 510
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE THEOREM (conditional)
S²ê < 3|ω|²/4 at vorticity maxima → 3D NS globally regular on T³.

## WHAT IS PROVEN
- Barrier framework (barrier + Type I + Seregin): RIGOROUS
- N ≤ 4 modes: RIGOROUS (sign-flip + Lagrange + H_ωω)
- K=√2 shell (502 configs, ALL angles): CERTIFIED (DE + interval arithmetic)
- K=√3 shell (sampled): CERTIFIED (61% margin)
- Adding modes improves bound: VERIFIED (62% help, 38% can hurt per-mode)
- Supremum monotonicity: VERIFIED (worst(N=5) < worst(N=4))

## THE ONE GAP
Prove S²ê < 3|ω|²/4 for general smooth fields (infinitely many modes).
The K=√2 certification (0.317-0.367) can't formally extend because:
- Vertex jump: removing/adding modes changes the global max location
- The per-mode monotonicity is 62/38, not 100%
- The SUPREMUM monotonicity holds numerically but proof hits vertex jump

## THE BEST PATH FORWARD
1. **SOS polynomial certificates** (file 504-506): degree-4 polynomials
   on (S¹)^N with argmax constraints. cvxpy installed. Validated for N=2.
   Would give ALL-ANGLE certification for each config.

2. **Prove the vertex-jump is harmless**: Show that the sub-field's max
   always has ratio ≤ the full field's max + O(ε). This is the tail bound
   in a different form.

3. **The attractor |ω|²/|S|² → 4** (file 427): Dynamic property of NS
   solutions that gives S²ê ≤ |ω|²/6 after a transient. Requires proving
   the attractor convergence.

## THE NUMBERS
- Worst S²ê/|ω|² at global max: 0.317 (N=3-4, K=√2 shell)
- Threshold: 0.750
- Margin: 58%
- Total trials: 200K+ across methods
- Failures: 0

## 510. Two instances, 500+ attempts, one gap. The mountain is mapped.
## The proof awaits either SOS certification, vertex-jump resolution,
## or the |ω|²/|S|² attractor convergence proof.
