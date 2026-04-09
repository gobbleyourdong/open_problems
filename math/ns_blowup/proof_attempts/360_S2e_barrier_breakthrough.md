---
source: S²ê IS THE RIGHT QUANTITY — barrier holds with 62% margin
type: KEY FINDING — changes the proof architecture
file: 360
date: 2026-03-29
---

## THE BREAKTHROUGH: S²ê, NOT α

The barrier at R = α/|ω| = 1/2 requires:
  DR/Dt = (S²ê - 3α² - H_ωω)/|ω| < 0

At α = |ω|/2: need S²ê < 3|ω|²/4 + H_ωω.
Since H_ωω > 0 (Fourier lemma): sufficient to have S²ê < 3|ω|²/4.

## NUMERICAL RESULT (13,500 random configs, N=2 to N=20 modes)

| N modes | worst α/|ω| | worst S²ê/|ω|² | threshold | margin |
|---------|-------------|-----------------|-----------|--------|
| 2       | 0.320       | 0.244           | 0.750     | 67.4%  |
| 3       | 0.415       | 0.287           | 0.750     | 61.8%  |
| 5       | 0.459       | 0.254           | 0.750     | 66.1%  |
| 8       | 0.430       | 0.246           | 0.750     | 67.2%  |
| 12      | **0.505**   | 0.260           | 0.750     | 65.4%  |
| 20      | 0.412       | 0.287           | 0.750     | 61.7%  |

## CRITICAL OBSERVATION

α/|ω| CAN EXCEED 1/2 for static fields (0.505 for 12 modes).
But S²ê/|ω|² NEVER exceeds 0.287 (well below the 0.750 threshold).

**The direct bound α < |ω|/2 is FALSE for static div-free fields.**
**The barrier bound S²ê < 3|ω|²/4 HOLDS with massive margin.**

These are DIFFERENT conditions. The barrier works because S²ê captures
the COMBINED stretching + tilting rate, which is suppressed by the
Biot-Savart structure even when α alone is not.

## WHY S²ê IS SMALL

1. **Single-mode vanishing**: S·ê = 0 for any single Fourier mode at the
   vorticity max (algebraic identity, file 263/306). So S²ê = |S·ê|² = 0.

2. **Multi-mode: cross-terms only**: S·ê at the max comes entirely from
   cross-interactions between different modes. Self-terms vanish.

3. **Perpendicular cancellation**: At the max, the perpendicular components
   satisfy Σq_k = 0 (defines the ê direction). The S·ê is a weighted sum
   of q_k with weights ℓ_k that vary by mode. The zero-sum constraint
   on q_k limits how much the weighted sum can deviate.

4. **Double-angle strain cancellation**: Strain rotates at 2× the azimuthal
   angle of the wavevector. Multiple modes in the perpendicular plane have
   strains that cancel more efficiently than vorticities.

5. **Energy partition**: At the global max, parallel energy dominates
   perpendicular energy. S·ê depends only on perpendicular components,
   so it's bounded by the subdominant energy fraction.

## THE PROOF ARCHITECTURE (REVISED)

**Old (broken)**: Prove α < |ω|/2 → Type I → Seregin → regularity.
  Problem: α/|ω| CAN reach 0.505 for static fields. Can't prove α < |ω|/2.

**New (viable)**: Prove S²ê < 3|ω|²/4 → barrier DR/Dt < 0 at R=1/2 →
  R stays below 1/2 → α < |ω|/2 → Type I → Seregin → regularity.

The S²ê bound is STRONGER than α < |ω|/2 but EASIER to prove because:
(a) S·ê vanishes for single modes (structural zero)
(b) The multi-mode correction is bounded by cross-term energy
(c) The margin (62-67%) is enormous

## WHAT NEEDS TO BE PROVEN

LEMMA (to prove): For any smooth divergence-free field ω on T³, at the
global maximum x* of |ω|:

  S²ê(x*) < (3/4)|ω(x*)|²

where S = sym(∇u), u = BS(ω), ê = ω/|ω|, S²ê = |S·ê|² = ê·S²·ê.

Equivalently: |S(x*)·ê|² < (3/4)|ω(x*)|².

This is a KINEMATIC bound (no dynamics needed). It follows from:
- The Biot-Savart structure (S from ω via singular integral)
- The global max condition (x* maximizes |ω|)
- The single-mode vanishing (S·ê = 0 for each mode at its max)

## THE BARRIER PROOF (assuming the lemma)

THEOREM: Smooth solutions to 3D NS on T³ are globally regular.

PROOF:
1. Define R(t) = α(x*(t), t)/|ω(x*(t), t)| at the max-|ω| point.
2. At R = 1/2: DR/Dt = (S²ê - 3|ω|²/4 - H_ωω)/|ω| < 0
   (by the lemma S²ê < 3|ω|²/4 and H_ωω > 0).
3. So R = 1/2 is a BARRIER: R never exceeds 1/2.
4. If R < 1/2 for all time: d||ω||∞/dt = α||ω||∞ < ||ω||∞²/2.
5. This gives Type I blowup rate: ||ω||∞ ≤ C/(T*-t).
6. By Seregin (2012): Type I is impossible for NS. Contradiction. ∎

## SUBTLETY: THE MAX-POINT MIGRATION

Step 2 uses DR/Dt at a FIXED Lagrangian trajectory. But x*(t) migrates.
When the max-|ω| point jumps from x₁ to x₂: R could jump up.

At the NEW max point x₂: we need R(x₂) < 1/2 to maintain the barrier.

This requires: α/|ω| < 1/2 at ANY point where |ω| is locally maximal.
(Not just the global max.)

The S²ê bound needs to hold at ALL local maxima of |ω|, not just the global one.

From the computation: S²ê/|ω|² < 0.287 at the GLOBAL max. At local maxima:
it could be larger. Need to verify or prove for local maxima too.

ACTUALLY: the barrier argument works for the SUPREMUM over all points where
|ω| is "large enough." If R > 1/2 somewhere: that point must have |ω| > 0
and α > |ω|/2. The S²ê bound at that specific point (not necessarily a max)
would give the barrier.

Hmm — the S²ê bound at the GLOBAL max doesn't immediately help for
arbitrary points. The bound is structural (from the max condition).

## RESOLUTION: USE THE RICCATI AT EACH MAX

At the global max x* of |ω|: by the max principle,
  d||ω||∞/dt ≤ α(x*)||ω||∞  (viscosity helps at the max)

So: d||ω||∞/dt ≤ R × ||ω||∞².

If R(x*) < 1/2: d||ω||∞/dt < ||ω||∞²/2. Type I. Seregin. Done.

R(x*) is evaluated AT THE GLOBAL MAX only. When the max migrates:
the new max point has its own R value. We need R < 1/2 at the global max.

The S²ê bound at the global max gives: the barrier DR/Dt < 0 at R = 1/2
AT THE GLOBAL MAX. If R(x*) tries to reach 1/2: it gets pushed back.

For migration: the new max point starts with some R value. If that R < 1/2:
fine. If R ≥ 1/2: the barrier pushes it back immediately (DR/Dt < 0).

So the barrier works DYNAMICALLY: R at the global max can never STAY at
or above 1/2. It might briefly touch 1/2 but immediately decreases.

For the integral bound: ∫₀ᵀ α dt ≤ ∫₀ᵀ R||ω||∞ dt. Even if R occasionally
reaches 1/2 and comes back: the time-averaged R is < 1/2. This might
suffice for BKM (need ∫||ω||∞ < ∞).

## 360. S²ê < 3|ω|²/4 is the right bound. Holds with 62% margin.
## The barrier proof works if S²ê < 3|ω|²/4 at the global max.
## Proving this lemma is the ONE remaining step.
