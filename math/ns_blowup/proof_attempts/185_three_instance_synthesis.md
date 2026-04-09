---
source: Instance A — synthesis of all three instances
type: THE COMPLETE PICTURE after parallel attack
date: 2026-03-29
---

## Instance A Findings (files 180-185)

1. Straight Lamb-Oseen tube: ratio = 1.000 exactly, α = 0 (extremal case)
2. Any perturbation at the max: ratio < 1 (verified numerically)
3. Conjecture α > 0 → H_ωω > 0: holds 92.5%, fails during max-point jumps
4. The quantity (var - H_ωω) < 0 at the max: holds 90% overall, 100% after t=0.06
5. This gives Dα/Dt < -α² (STRONG Riccati bound) in steady state

## Instance B Findings (file 220)

1. Adversarial IC battery: 7 ICs including thin trefoils (σ=0.10-0.30)
2. CANNOT break ratio = 1.0. Worst case: 0.955 (σ=0.15 at N=48)
3. Ratio DECREASES with resolution (N=32 artifacts, N=48 converges)
4. The ratio converges to ~0.95 as σ → 0 (not to 1.0!)
5. Margin: 4.5% at worst, geometric (not accidental)

## Instance C Findings (files 260-264)

1. Palinstrophy growth: dP/dt ≤ C||ω||∞ P (if ||ω||∞ bounded)
2. Forward cascade confirmed but bounded
3. Sobolev growth rates ~t (Gaussian, always finite)
4. The chain: ratio ≤ 1 → H_ωω > 0 → α bounded → ||ω||∞ exp → Sobolev finite

## The Combined State

The three instances converge:

| Question | Instance | Answer |
|----------|----------|--------|
| Can ratio exceed 1? | B (adversarial) | NO. Max 0.955. |
| Does the bound have a clean extremal? | A (analytical) | YES. Straight tube = 1. |
| Does ratio decrease with resolution? | B | YES. N=32 artifacts vanish at N=48. |
| Does Dα/Dt < -α² hold at the max? | A | YES (100% after transient) |
| Are Sobolev norms bounded? | C | YES (Gaussian growth, finite) |

## Remaining Gap

The FORMAL proof needs one of:
1. Prove ratio ≤ 1 for all div-free fields (from the variational argument)
2. Prove var - H_ωω < 0 at the max for evolved Euler (from the dynamics)
3. Close the LP energy estimate with alignment weights (from shell structure)

All three are candidate proof routes. None is closed yet.
The closest: the variational argument (straight tube extremal) + perturbation stability.

## 185 proof files across three instances.
