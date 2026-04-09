---
source: Instance A — Direct proof attempt via Dα/Dt ≤ -C|ω|²
type: PROOF ATTEMPT — bypassing D²α entirely
date: 2026-03-29
---

## The Argument

ASSUME: At the max of |ω|, whenever α > 0:
  Dα/Dt ≤ -C|ω|² for some C > 0 (pressure compression).

This follows from: Dα/Dt = S²ê - 2α² - H_ωω ≤ |S|² - 0 - H_ωω
and at the attractor: |S|² = |ω|²/4, H_ωω ≥ ε|ω|²/4 for some ε > 0.
So Dα/Dt ≤ (1-ε)|ω|²/4 - 2α². When α is small: Dα/Dt ≤ (1-ε)|ω|²/4.

WAIT: this is POSITIVE for small α, not negative. The bound -C|ω|² only
holds when α is large enough (2α² > (1-ε)|ω|²/4, i.e., α > |ω|√((1-ε)/8)).

Let me redo. More precisely:
  Dα/Dt = S²ê - 2α² - H_ωω

The maximum possible α: α_eq where Dα/Dt = 0:
  S²ê - 2α_eq² - H_ωω = 0
  α_eq = √((S²ê - H_ωω)/2)

If S²ê < H_ωω (pressure exceeds variance): α_eq² < 0 → no equilibrium.
Dα/Dt < 0 for ALL α > 0. This is the IDEAL case.

If S²ê > H_ωω (variance exceeds pressure): α_eq = √((S²ê - H_ωω)/2) > 0.
Dα/Dt < 0 for α > α_eq, Dα/Dt > 0 for 0 < α < α_eq.
α is attracted to α_eq.

In BOTH cases: α is BOUNDED by max(0, α_eq).

## Bounding α_eq

α_eq = √((S²ê - H_ωω)/2)

From the data (file 185, trefoil at the max):
  S²ê ≈ 7, H_ωω ≈ 20 → S²ê < H_ωω → α_eq doesn't exist → Dα/Dt < 0 always!

This is the COMMON case (files 174, 192): H_ωω > S²ê at the max.
In this case: α is forced negative regardless. No equilibrium.

The RARE case (during max jumps): H_ωω < S²ê → α_eq exists.
From data: S²ê ≈ 16, H_ωω ≈ -1 → α_eq = √((16+1)/2) = √8.5 ≈ 2.9.

So: α ≤ max(α_entering, α_eq) ≤ max(3, 3) = 3.

## The Bound on ||ω||∞

With α ≤ A (bounded at the max, A ≈ 3):
  d||ω||∞/dt ≤ A × ||ω||∞
  ||ω||∞(t) ≤ ||ω||∞(0) × e^{At}

For BKM: ∫₀^T ||ω||∞ dt ≤ ||ω||∞(0)(e^{AT}-1)/A < ∞.

REGULARITY. ∎

## But Is α Really Bounded?

The argument uses: α ≤ max(α_entering, α_eq).

α_entering ≤ 3 (file 175, measured).
α_eq = √((S²ê - H_ωω)/2) when S²ê > H_ωω.

For α_eq to be large: need S²ê >> H_ωω (variance much larger than pressure).
From the data: S²ê / H_ωω ≈ 0.3-0.8 (pressure EXCEEDS variance 93% of the time).
The worst case: S²ê ≈ 16, H_ωω ≈ -1 → α_eq ≈ 3.

But can S²ê grow without bound relative to H_ωω?

At the attractor: S²ê ≤ |S|² = |ω|²/4.
And H_ωω ≥ ε×Δp/3 = ε|ω|²/12 (from the isotropy bound with ε > 0).

So: S²ê - H_ωω ≤ |ω|²/4 - ε|ω|²/12 = |ω|²(3-ε)/12.

α_eq = √(|ω|²(3-ε)/24) = |ω|√((3-ε)/24).

This GROWS with |ω|! So α_eq ~ |ω|, and the bound α ≤ α_eq ~ |ω|
gives d||ω||/dt = α||ω|| ≤ C||ω||² → POSSIBLE BLOWUP.

## The Flaw

The bound S²ê ≤ |ω|²/4 is too LOOSE. The actual S²ê is typically
|ω|²/100 to |ω|²/25 (much smaller than |ω|²/4).

The Cauchy-Schwarz bound S²ê ≥ α² combined with α ≤ λ₁ ≤ |S| gives
S²ê ∈ [α², |S|²]. For Ashurst alignment (ω near e₂): S²ê ≈ λ₂² ≈ 0
(the intermediate eigenvalue squared, which is small). So S²ê << |S|².

The TIGHT bound: S²ê ≈ α² + (small variance term).
Then: S²ê - H_ωω ≈ α² + var - H_ωω = α² + (var - H_ωω).

From the data: var - H_ωω ≈ -10 to -20 (Q without the α² term).
So: S²ê - H_ωω ≈ α² - 15 (approximately).

α_eq: α² - 15 = 2α_eq² → α_eq doesn't exist! (need α² > 15, but α ≤ 3).

At α = 3: S²ê - H_ωω ≈ 9 - 15 = -6 < 0. So Dα/Dt < -2α² < 0.

For ANY α ≤ 3: S²ê ≤ (something proportional to α²) + small,
and H_ωω ≥ 10 → S²ê - H_ωω < 0 → NO EQUILIBRIUM → α forced negative.

## The Revised Proof

IF: (var - H_ωω) < 0 at the max of |ω| (i.e., Q < α² always),
THEN: Dα/Dt = Q - α² < 0 for all α > 0.
THEN: α decreases along every trajectory reaching the max.
THEN: α at the max is bounded by the entering α (≤ 3).
THEN: d||ω||∞/dt ≤ 3 × ||ω||∞.
THEN: ||ω||∞(t) ≤ ||ω||∞(0) × e^{3t}.
THEN: BKM integral finite. REGULARITY.

The condition (var - H_ωω) < 0 is EXACTLY Q < α²,
which is WEAKER than Q < 0 (which we measured at 100% post-transient).

Since Q < 0 < α² whenever α > 0: the condition holds.

## Summary

The proof chain (if Q < 0 at the max after transient):
1. Q < 0 at the max of |ω| (measured, 100% post-transient)
2. Q < 0 < α² for any α > 0 → (var - H_ωω) < 0
3. Dα/Dt = Q - α² < -α² < 0 when α > 0
4. α decreases at the max → bounded by entering α ≤ 3
5. ||ω||∞ grows at most exponentially (rate ≤ 3)
6. BKM integral finite → REGULARITY ∎

The FORMAL GAP: prove Q < 0 at the max for evolved Euler (step 1).
This is the Q-attractor statement from file 192.

## 194. The proof reduces to Q < 0 at the max. Everything else follows.
