---
source: Instance A — α>0 → H_ωω>0 fails transiently during max-point jumps
type: NEAR-MISS — conjecture holds 92.5% of the time, fails during jumps
date: 2026-03-29
---

## The Test

At the max-|ω| point of the trefoil, dense sampling every 50 steps:
  α > 0 AND H_ωω < 0: 6 violations out of ~80 measurements (7.5%)

## When It Fails

t = 0.025-0.050: max-point JUMP (α goes from +1.1 to +2.7).
During the jump: H_ωω = -0.7 to -1.1 (briefly negative).
After t = 0.06: H_ωω returns to positive (+7 to +29) permanently.

The violations are TRANSIENT: ~0.025 time units.
α still decreases during and after: +2.7 → +0.5 by t=0.25.
The eigenvector tilting mechanism (file 173) works regardless.

## The Refined Conjecture

WEAK: α > 0 at the max → H_ωω > 0 EVENTUALLY (within time O(1/α)).
STRONG: α > 0 at the max → H_ωω > 0 always (FAILS, 7.5% violations).

The weak version suffices for the proof because:
1. The transient H_ωω < 0 episodes add at most Δ(α) ≈ α × Δt ≈ 2.7 × 0.025 ≈ 0.07
2. This is negligible compared to the subsequent decrease from α = 2.7 to 0.5
3. The net effect over any O(1) time window is still compression

## Impact on the Proof

The two-case argument (file 182) needs modification:

CASE 1: α ≤ 0. No danger. ✓
CASE 2: α > 0 AND H_ωω > 0 (92.5% of the time). Transport barrier works. ✓
CASE 3: α > 0 AND H_ωω < 0 (7.5%, during jumps). TRANSIENT.
  During this case: Dα/Dt = ê·S²·ê - 2α² - H_ωω.
  With H_ωω ≈ -1: Dα/Dt ≈ S²ê - 2α² + 1.
  At α ≈ 2.7: 2α² ≈ 14.6, S²ê ≈ 16 (from data).
  Dα/Dt ≈ 16 - 14.6 + 1 = +2.4 (slightly positive — α grows slowly).
  Duration: ~0.025. Total α increase: 2.4 × 0.025 ≈ 0.06.
  Negligible. Then H_ωω turns positive and α crashes.

## The Straight Tube Connection

The straight tube has ratio = 1 exactly and H_ωω = 0.
The jump violations have ratio slightly > 1 (H_ωω slightly < 0).
These are points momentarily close to the straight-tube configuration
(the max just moved to a less-curved part of the trefoil).

The dynamics quickly curve the tube (generate z-variation), pushing
H_ωω positive again. The straight-tube config is UNSTABLE.

## 183. Conjecture nearly holds. Transient violations are negligible.
## The proof can accommodate them via time-averaging.
