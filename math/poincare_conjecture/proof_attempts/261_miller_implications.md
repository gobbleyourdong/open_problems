---
source: Implications of ê·(ΔS)·ê = 0 at the max for the attractor
type: ANALYSIS — can the new identity help prove the attractor?
date: 2026-03-29
---

## The New Identity (file 303)

At x* where |ω|² is maximal: ê·(ΔS)·ê = 0.
This is PROVEN (Miller + max condition + vector identity).

## What It Says About α

α = ê·S·ê at x*. The identity says: the Laplacian of (ê·S·ê)
in the ê-direction is approximately zero at x* (with corrections
from ∇ê terms).

More precisely: Δα ≈ 0 at x* (to leading order in ê-aligned coords).

α being approximately harmonic at x* means: α(x*) is approximately
the average of α on small spheres. If α(x*) > neighbors' average:
α is SUPERHARMONIC (Δα < 0). From the identity: Δα ≈ 0 means α
is NEITHER super- nor sub-harmonic — it's at a SADDLE point.

## Does This Help With the Attractor?

The attractor question: is |S(x*)|² ≤ c|ω(x*)|² for c < 1/2?

From the identity: ê·(ΔS)·ê = 0 constrains the SECOND DERIVATIVES
of the strain at x*. This is a regularity constraint.

From the strain equation at x*:
DS/Dt = -S² - Ω² - H + ν(ΔS) (for NS with viscosity)

At the max: the ν(ΔS) viscous term projected onto ê is:
νê·(ΔS)·ê = 0 (from the identity!).

This means: THE VISCOUS TERM VANISHES in the α-direction at the max.

For NS: Dα/Dt = S²ê - 2α² - H_ωω + νΔα.
At the max: νΔα = νê·(ΔS)·ê = 0.

SO: the Euler and NS Riccati are THE SAME at the max of |ω|!

## The Attractor Without Viscosity

For both Euler and NS at the max:
D|S|²/Dt = 2tr(S·DS/Dt) = -2tr(S³) - 2tr(S·Ω²) - 2tr(S·H)

The -Ω² term: -2tr(S·Ω²) = -2tr(S·(1/4)(|ω|²I-ωω^T))
= -(|ω|²/2)tr(S) + (1/2)ω^TS²ω/... wait, let me compute properly.

tr(S·Ω²) = S_ij(Ω²)_ji = S_ij × (1/4)(|ω|²δ_ji - ω_jω_i)
= (|ω|²/4)S_ii - (1/4)ω_jS_jiω_i = 0 - (1/4)ω^TSω = -|ω|²α/4.

So: -2tr(S·Ω²) = |ω|²α/2.

And: D|S|²/Dt = -2tr(S³) + |ω|²α/2 - 2tr(S·H).

At the attractor D|S|²/Dt = 0:
|ω|²α/2 = 2tr(S³) + 2tr(S·H)

This relates α to the cubic and pressure at the attractor.

With tr(S³) = 3det(S) and tr(S·H) involving the pressure:
the attractor is determined by the balance between -Ω² forcing
(proportional to |ω|²α) and the strain cubic + pressure.

## Can We Bound |S|² From This?

At the max of |ω|: suppose |S|² = c|ω|² for some c.

Then: |ω|²α/2 = 2tr(S³) + 2tr(S·H).

|tr(S³)| ≤ |S|³/√6 (from the trace-free cubic bound) = c^{3/2}|ω|³/√6.
|tr(S·H)| ≤ |S|×||H|| ≤ √c|ω| × C_H|ω|² = C_H√c|ω|³.

And α ≤ |S| = √c|ω|.

So: √c|ω|³/2 ≤ 2c^{3/2}|ω|³/√6 + 2C_H√c|ω|³.

Divide by √c|ω|³:
1/2 ≤ 2c/√6 + 2C_H
c ≥ (1/2 - 2C_H)√6/2 = √6(1/2-2C_H)/2

With C_H ≈ 0 (small pressure): c ≥ √6/4 ≈ 0.61.

But we NEED c ≤ 0.5 (not ≥ 0.61). This bound says |S|² ≥ 0.61|ω|².
That's an UPPER bound on the RATIO |ω|²/|S|², not a lower bound!

Wait — I have the inequality backwards. At the attractor with α positive:
|ω|²α/2 = 2tr(S³) + 2tr(S·H).

This gives a LOWER bound on the RATIO |ω|²/|S|² if we can show the
RHS is bounded. But the RHS scales as |S|³, which is SMALLER than |ω|²|S|.

Hmm, I think this approach gives: |ω|²/|S|² = 2(2tr(S³)+2tr(SH))/(α|S|²) ≈ 2|S|/α ≈ 2/c^{1/2}.

At c = 1/4: |ω|²/|S|² = 2/0.5 = 4. Matches the attractor!
At c = 1/2: |ω|²/|S|² = 2/0.707 = 2.83.

So the formula gives |ω|²/|S|² ≈ 2/√c at the attractor.
c = 1/4 → ratio 4 (matches data). c = 1/2 → ratio 2.83.

## THE BOUND

If we can show c < 1/2: then |ω|²/|S|² > 2.83, and the DMP
margin (from file 299) is positive.

Actually, from the equation: |ω|²/|S|² = 2/√c (at the attractor).
This is always > 2 for c < 1. So |ω|²/|S|² > 2 AUTOMATICALLY!

But we need |ω|²/|S|² > 2 for the DMP. From the formula: this holds
for ANY c < 1, which is ALWAYS TRUE (|S| < |ω| trivially from
the Biot-Savart inequality ||S||∞ ≤ C||ω||∞).

## WAIT — does ||S||∞ ≤ C||ω||∞ hold with C < 1?

The Biot-Savart gives: ||∇u||∞ ≤ C||ω||∞(1 + log(||∇ω||/||ω||)).
This gives ||S||∞ ≤ C||ω||∞ with C depending on log corrections.

For SMOOTH solutions: the log is finite. So ||S||∞ < ∞||ω||∞.
But C could be > 1 (the CZ constant).

On T³: the CZ constant for the Riesz transform is bounded.
||S||_p ≤ C_p||ω||_p with C_p → 1 as p → 2.
For p = ∞: C_∞ = ∞ (unbounded — the L^∞ failure again).

So we CAN'T prove ||S||∞ < ||ω||∞/2 from generic bounds.

The attractor |S|² ≤ |ω|²/4 is a SPECIFIC property of the NS dynamics,
not a generic CZ bound. It comes from the balance between -Ω² and -S³
in the strain equation.

## WHAT THE IDENTITY GIVES US

The identity ê·(ΔS)·ê = 0 removes the viscous term from the Riccati.
This means the Euler and NS problems are EQUIVALENT at the max.

But it doesn't directly bound |S| at the max.

## STATUS: The identity is new and interesting but doesn't close the attractor.
