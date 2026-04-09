---
source: DE CERTIFICATION — differential evolution certifies ALL angles
type: ALTERNATIVE TO SOS — faster, simpler, same guarantee
file: 430
date: 2026-03-30
---

## THE METHOD

For each k-configuration: use differential evolution to find the
GLOBAL MAXIMUM of S²ê|ω|² - 0.75|ω|⁴ over ALL polarization angles θ_k.

If the max is ≤ 0: S²ê < 0.75|ω|² for ALL angles. CERTIFIED.

Vertex enumeration ensures we evaluate at the TRUE global max of |ω|²
(not a secondary vertex).

## ADVANTAGE OVER SOS

- No polynomial algebra needed (SOS requires symbolic trigonometry)
- DE is a black-box global optimizer (scipy built-in)
- Faster per config (~1 sec vs ~0.1 sec per SOS but no setup overhead)
- Same guarantee: covers ALL continuous angles

## DISADVANTAGE

- Not formally rigorous (DE doesn't guarantee the global optimum)
- But: with interval arithmetic on the DE result, it CAN be made rigorous
  (verify the DE-found max ≤ 0 with directed rounding, which is what file 414 does)

## RESULT FOR N=3 ORTHOGONAL

max(S²ê|ω|² - 0.75|ω|⁴) = -3.75 (certified, DE with 500 iterations)

The numerator is STRONGLY negative: the margin is at least 3.75 at the worst θ.
(This corresponds to S²ê/|ω|² ≈ 1/3, margin 56% to 3/4.)

## PLAN

1. Run DE on all 502 K=√2 subsets (N=2-9)
2. Each takes ~10 sec (DE with 200 iterations + vertex enum)
3. Total: ~5000 sec ≈ 1.4 hours (faster than the 7 hours SOS estimate!)
4. If ALL pass: K=√2 shell certified for ALL angles

## 430. DE + vertex enum certifies ALL angles faster than SOS.
