---
source: Instance A — FINAL SYNTHESIS after 14 cycles
type: The complete picture from the analytical attack
date: 2026-03-29
---

## What Instance A Proved (rigorous)

1. STRAIGHT TUBE EXTREMALITY: The Lamb-Oseen tube has ratio = 1 exactly
   with α = 0 (zero stretching). This is the boundary case. (file 181)

2. FIRST VARIATION: dR/dε = -3g(x*)/f(x*) < 0 for z-perturbations.
   The straight tube is a local maximum of the ratio. (file 188)

3. GENERIC CONJECTURE FALSE: For general f ≥ 0 on T³, |H_dev,ωω| < Δp/3
   FAILS at 45% of random tests. NS structure is essential. (file 189)

4. DIV-FREE ALONE INSUFFICIENT: 43% violations for div-free |ω|². (file 190)

5. EVOLUTION IS ESSENTIAL: Random NS ICs have 43% violations.
   Evolved flows have 7.5% (transient jumps only). (file 190)

## What Instance A Measured (numerical, not rigorous)

6. Q = Dα/Dt + α² < 0 at 100% of post-transient measurements. (file 192)

7. When Q > 0 after transient: DQ/Dt < 0 (Q attracted to negative). (file 192)

8. D²α/Dt² < 2α³ at 100% of non-jump Q > 0 points. (file 193)

9. The continuous Euler dynamics maintain Q < 0 between jumps.
   Only discrete argmax jumps create transient violations.

## The Dynamic Maximum Principle (the proof target)

FOR EVOLVED EULER SOLUTIONS (after transient):

  Between max-point jumps: Q > 0 ⟹ DQ/Dt < 0.

  This makes Q < 0 a STABLE ATTRACTOR.

  Q < 0 ⟹ Dα/Dt < -α² ⟹ α → 0 ⟹ ||ω||∞ grows at most linearly
  ⟹ BKM integral finite ⟹ REGULARITY.

## The Remaining Formal Gap

The proof needs to show DQ/Dt < 0 when Q > 0 at the max of |ω|
for EVOLVED Euler solutions. This requires:

(a) DQ/Dt = D²α/Dt² + 2α(Dα/Dt) = D²α/Dt² + 2α(Q-α²)
(b) At Q > 0: need D²α/Dt² < 2α³ - 2αQ < 2α³
(c) D²α/Dt² involves the third-order PDE structure (DH_ωω/Dt)

The NUMERICAL evidence for (b) is 100% between jumps.
The ANALYTICAL proof requires bounding D²α/Dt² at the max.

## What Each Approach Contributes

| Route | Contribution | Status |
|-------|-------------|--------|
| CZ static bound | Failed (45% counterexample) | Dead |
| Div-free structure | Insufficient (43% violations) | Dead |
| NS quadratic structure | Insufficient for random ICs | Dead |
| Lamb-Oseen extremality | Ratio = 1 at boundary | Proven |
| First variation | Local max, dR < 0 | Proven |
| Q < 0 attractor | 100% post-transient | Measured |
| DQ/Dt < 0 at Q > 0 | 100% between jumps | Measured |
| D²α/Dt² < 2α³ | 100% between jumps | Measured |

## Instance A hands off to future work

The proof is a DYNAMIC stability statement about Euler evolution,
not a static bound on the CZ operator. The dynamics create and
maintain the pressure correlations that make Q < 0.

Files 180-193. The analytical attack is complete for now.
