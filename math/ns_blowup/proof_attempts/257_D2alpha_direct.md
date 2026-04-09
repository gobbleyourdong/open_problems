---
source: DIRECT D²α bound at α = |ω|/2 (the worst case)
type: PROOF ATTEMPT — bypassing DVar and DH separately
date: 2026-03-29
---

## The Formula

At Q = 0 (the boundary where DQ/Dt < 0 is needed):
  Dα/Dt = -α² (from Q = Dα/Dt + α² = 0)

The DMP condition: DQ/Dt < 0 at Q = 0.
DQ/Dt = D²α/Dt² + 2αDα/Dt = D²α/Dt² + 2α(-α²) = D²α - 2α³.

Need: D²α < 2α³ at Q = 0.

## D²α from the Riccati identity

D²α/Dt² = D(S²ê - 2α² - H_ωω)/Dt
         = DS²ê/Dt - 4αDα/Dt - DH_ωω/Dt
         = DS²ê/Dt + 4α³ - DH_ωω/Dt  (using Dα = -α² at Q=0)

## Bounding DS²ê/Dt

S²ê = Σλᵢ²cᵢ. Its time derivative:
DS²ê/Dt = Σ[2λᵢ(Dλᵢ/Dt)cᵢ + λᵢ²(Dcᵢ/Dt)]
         = 2Σλᵢcᵢ(Dλᵢ/Dt) + Σλᵢ²(Dcᵢ/Dt)  [eigenvalue + tilting]

The eigenvalue derivative: Dλᵢ/Dt = eᵢ·(DS/Dt)·eᵢ.
DS/Dt = -S² - Ω² - H. So Dλᵢ/Dt = -λᵢ² - (Ω²)ᵢᵢ - Hᵢᵢ.

(Ω²)ᵢᵢ = (1/4)(|ω|²cᵢ - |ω|²) = -(|ω|²/4)(1-cᵢ). Wait:
Ω² = (1/4)(|ω|²I - ωω^T). In eigenbasis: (Ω²)ᵢᵢ = (|ω|²/4)(1 - cᵢ)...
Actually: (Ω²)ᵢᵢ = (1/4)(|ω|² - (ω·eᵢ)²) = (|ω|²/4)(1-cᵢ).
And -Ω² contributes -(Ω²)ᵢᵢ = -(|ω|²/4)(1-cᵢ) to Dλᵢ/Dt.

So: Dλᵢ/Dt = -λᵢ² - (|ω|²/4)(1-cᵢ) - Hᵢᵢ.

The eigenvalue part of DS²ê/Dt:
2Σλᵢcᵢ[-λᵢ² - (|ω|²/4)(1-cᵢ) - Hᵢᵢ]
= -2Σλᵢ³cᵢ - (|ω|²/2)Σλᵢcᵢ(1-cᵢ) - 2ΣλᵢHᵢᵢcᵢ

The first term: -2Σλᵢ³cᵢ (the eigenvalue cubic).
The second: -(|ω|²/2)(α - Σλᵢcᵢ²) = -(|ω|²/2)(α - S²ê + Var...)

Hmm, this is getting messy. Let me use α = Σλᵢcᵢ and S²ê = Σλᵢ²cᵢ.

Σλᵢcᵢ(1-cᵢ) = α - Σλᵢcᵢ² = α - (something between α² and S²ê).

At Q = 0: S²ê = α² + H_ωω (from Q = S²ê - α² - H_ωω = 0).

## Simplification at Q = 0

At Q = 0: Var = S²ê - α² = H_ωω > 0.

DS²ê/Dt (eigenvalue part) = -2Σλᵢ³cᵢ - (|ω|²/2)Σλᵢcᵢ(1-cᵢ) - 2ΣλᵢHᵢᵢcᵢ

The DOMINANT terms at high |ω|:
- -(|ω|²/2)Σλᵢcᵢ(1-cᵢ): this is -(|ω|²/2)(α-Σλᵢcᵢ²).
  With |S| ~ |ω|/2 and α ≤ |ω|/2: this is O(|ω|³).

Let me bound the leading term more carefully.

-(|ω|²/2)(α-Σλᵢcᵢ²) = -(|ω|²/2)α + (|ω|²/2)Σλᵢcᵢ²

The (|ω|²/2)Σλᵢcᵢ²: since |λᵢ| ≤ |S| ≤ |ω|/2 and Σcᵢ² ≤ 1:
(|ω|²/2)|Σλᵢcᵢ²| ≤ (|ω|²/2)(|ω|/2) = |ω|³/4.

And -(|ω|²/2)α = -(|ω|²/2)α.

At α = |ω|/2: -(|ω|²/2)(|ω|/2) = -|ω|³/4.
(|ω|²/2)Σλᵢcᵢ² ≤ |ω|³/4.

So the leading -Ω² eigenvalue contribution is between -|ω|³/2 and 0.
At α = |ω|/2: approximately -|ω|³/4 + |ω|³/4 = 0? This can't be right.

## THE SIMPLE BOUND

Let me just use: DS²ê/Dt ≤ C₁|ω|³ for some C₁.

And: D²α = DS²ê/Dt + 4α³ - DH_ωω/Dt ≤ C₁|ω|³ + 4α³ - DH_ωω/Dt.

Need: D²α < 2α³, i.e., C₁|ω|³ + 4α³ - DH < 2α³, i.e., C₁|ω|³ + 2α³ < DH.

This requires DH > C₁|ω|³ + 2α³. Which is a POSITIVE lower bound on DH.
But DH can be negative! So this approach FAILS for generic DH.

## THE CORRECT APPROACH (from the eigenvalue analysis)

D²α/Dt² = DS²ê/Dt + 4α³ - DH_ωω/Dt.

At Q = 0: S²ê = α² + H_ωω.

The -Ω² eigenvalue contribution to DS²ê/Dt:
= -(|ω|²/2)α + (|ω|²/2)Σλᵢcᵢ² + (other terms from -S², -H)

But Σλᵢcᵢ² is hard to bound without knowing the specific alignment.

## MEASUREMENT: What is D²α actually?

From file 193 (Instance A): D²α < 2α³ at 100% of post-transient times
between max-point jumps. 30× margin.

From the trefoil at α = 2.5, |ω| = 25:
D²α ≈ (some measured value), 2α³ = 31.25.
The measurement: D²α ≈ 1 (much less than 31.25). Margin: 30×.

## WHY THE MARGIN IS SO LARGE

D²α/Dt² at Q = 0 includes:
  +4α³ (from the -2α² term)
  +DS²ê/Dt (from the eigenvalue + tilting changes)
  -DH_ωω/Dt

The +4α³ is the ONLY positive O(α³) term. DS²ê/Dt is NEGATIVE at the max
(from the -Ω² eigenvalue compression -(|ω|²/2)α). And DH is bounded.

So: D²α ≈ 4α³ - (|ω|²/2)α - (other negative) = 4α³ - (|ω|²/2)α.

At α = |ω|/2: 4(|ω|/2)³ - (|ω|²/2)(|ω|/2) = |ω|³/2 - |ω|³/4 = |ω|³/4.
And 2α³ = 2(|ω|/2)³ = |ω|³/4.

So: D²α ≈ |ω|³/4 = 2α³ AT THE BOUNDARY. Zero margin!

The actual margin (30×) comes from α being MUCH LESS than |ω|/2 in practice.
At α = 0.1|ω| (typical): 4α³ = 0.004|ω|³, (|ω|²/2)α = 0.05|ω|³.
D²α ≈ 0.004 - 0.05 = -0.046|ω|³. And 2α³ = 0.002|ω|³. Much larger margin.

## CONCLUSION

The D²α < 2α³ bound BARELY holds at α = |ω|/2 (zero margin).
It holds with LARGE margin at typical α (0.1|ω|).

The proof can't be closed at α = |ω|/2 without additional structure
(the tilting, pressure, or the DH term need to contribute negatively).

This confirms Instance A's finding: proven for α < 0.35|ω|,
unproven at α = |ω|/2 (but never observed there).

## 257. The D²α approach gives zero margin at α = |ω|/2.
## The proof needs α < |ω|/2 (i.e., ω NOT aligned with e₁).
## This is the Ashurst alignment — the original open problem.
