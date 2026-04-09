---
source: Q ≥ 0 + viscosity → can we force Type I → Seregin → regularity?
type: PROOF ATTEMPT using existing Type I regularity results
date: 2026-03-29
file: 214
---

## Known Results

SEREGIN (2012): Type I blowup for NS on R³ is impossible.
Type I: ||ω(t)||∞ ≤ C/√(T*-t) for all t < T*.
If this holds: the rescaled solution converges to a self-similar
profile, backward uniqueness forces it to zero → contradiction.

KOCH-TATARU (2009): Mild solutions in L³ are smooth.
If ||u||_{L³} stays bounded: regularity.

## Our Situation

Q ≥ 0 gives: α' ≥ -α² → α ≥ C/(1+Ct) (Riccati lower bound).
d||ω||/dt = α||ω|| → ||ω|| grows at most quadratically (||ω||' ≤ C||ω||²).

For EULER (ν=0): ||ω||' ≤ C||ω||² → ||ω|| ≤ C/(T*-t) (blowup possible).
This is WORSE than Type I (C/√(T*-t)).

For NS (ν>0): ||ω||' ≤ α||ω|| - ν|∇ω|²/||ω||.

## The Gradient Term

At the max of |ω|: ω·Δω ≤ -|∇ω|² (from Δ|ω|² ≤ 0).

CKN partial regularity implies: near blowup, the solution concentrates
in a parabolic cylinder of radius √(T*-t). Inside this cylinder:
|ω| ~ ||ω||∞ and the gradient |∇ω| ~ ||ω||∞/√(T*-t) (parabolic scaling).

So: |∇ω|² ~ ||ω||∞²/(T*-t).

Viscous term: -ν|∇ω|²/||ω|| ~ -ν||ω||∞/(T*-t).

Total: ||ω||' ≤ C||ω||² - ν||ω||/(T*-t).

For ||ω|| ~ A/(T*-t) (the Q ≥ 0 bound):
||ω||' ≈ A/(T*-t)² (from the blowup) and
-ν||ω||/(T*-t) = -νA/(T*-t)².

So: ||ω||' ≈ A(1-ν)/(T*-t)² ... this doesn't quite work dimensionally.

Let me be more careful. If ||ω|| = A/(T*-t):
d||ω||/dt = A/(T*-t)² = α × A/(T*-t) → α = 1/(T*-t).

The viscous term: -ν|∇ω|²/||ω||.
|∇ω| at the max: from the concentration scale σ ~ √(ν(T*-t)) (viscous diffusion):
|∇ω| ~ ||ω||/σ ~ A/(T*-t) / √(ν(T*-t)) = A/(√ν (T*-t)^{3/2}).
|∇ω|² ~ A²/(ν(T*-t)³).
-ν|∇ω|²/||ω|| = -νA²/(ν(T*-t)³) × (T*-t)/A = -A/(T*-t)².

So: viscous term ≈ -A/(T*-t)² = -||ω||'.

The viscous term EXACTLY CANCELS the stretching at the BKM rate!

More precisely: ||ω||' ≈ α||ω|| - ν|∇ω|²/||ω|| ≈ A/(T*-t)² - A/(T*-t)² ≈ 0.

This is the CRITICAL BALANCE for NS blowup: stretching and viscosity
cancel at the BKM rate. Blowup requires stretching to EXCEED viscosity.

## The Implication

For Q ≥ 0: α ≤ C/(T*-t) (the BKM rate). The stretching rate is
at most C/(T*-t). The viscous term is ~ Cν/(T*-t)² × (T*-t) = Cν/(T*-t).

Wait, I need the viscous term more carefully. The NS vorticity at max:
d||ω||/dt = α||ω|| + ν(ω·Δω)/|ω| at the max.

ω·Δω at the max: from the NS equation, ω·Δω = (ω·Dω/Dt - ω·Sω)/ν
= (D|ω|²/2/Dt - |ω|²α)/ν = (||ω||d||ω||/dt - ||ω||²α)/ν.

This is circular (involves d||ω||/dt).

Let me use: at the max, Δ|ω|² = 2|∇ω|² + 2ω·Δω ≤ 0.
So: ω·Δω ≤ -|∇ω|².

d||ω||/dt = α||ω|| + ν(ω·Δω)/||ω|| ≤ α||ω|| - ν|∇ω|²/||ω||.

## The Lower Bound on |∇ω|²

At the max: we need |∇ω|² ≥ (something useful).

From the UNCERTAINTY PRINCIPLE / interpolation:
||ω||∞ ≤ C ||ω||_{L²}^{a} ||∇²ω||_{L²}^{1-a} (Gagliardo-Nirenberg).

This doesn't directly give |∇ω|² at the max.

From the concentration near blowup: if ω is concentrated in a ball
of radius R near x*: |∇ω| ~ ||ω||/R. And |∇ω|² ~ ||ω||²/R².

For NS: the minimum possible R is the VISCOUS SCALE R ~ √(ν/||S||).
With ||S|| ~ ||ω||/2: R ~ √(2ν/||ω||).
|∇ω|² ~ ||ω||²/(2ν/||ω||) = ||ω||³/(2ν).

Viscous term: -ν × ||ω||³/(2ν) / ||ω|| = -||ω||²/2.

So: d||ω||/dt ≤ α||ω|| - ||ω||²/2 ≤ (||ω||/2)||ω|| - ||ω||²/2 = 0.

d||ω||/dt ≤ 0 → ||ω|| DECREASING! REGULARITY!

## Wait — Is |∇ω|² ≥ ||ω||³/(2ν) Correct?

This assumes: ω is concentrated in a ball of radius R ~ √(2ν/||ω||).

WHY would ω concentrate at THIS scale? Because the viscous diffusion
smooths ω on scales smaller than the Kolmogorov scale ~ √(ν/||S||).

If the vorticity core has width σ > √(ν/||S||): the gradient is weaker.
If σ < √(ν/||S||): viscosity would smooth it to σ ~ √(ν/||S||).

So: σ ≥ √(ν/||S||) ~ √(2ν/||ω||). This gives the UPPER bound
on the gradient: |∇ω| ≤ ||ω||/σ_min = ||ω||/√(2ν/||ω||) = ||ω||^{3/2}/√(2ν).

But I need a LOWER bound! The estimate above is an UPPER bound.

The LOWER bound: |∇ω|² at the max could be ZERO (if ||ω|| is achieved
on a broad plateau). We can't bound it below without more information.

## The Flaw

The gradient estimate |∇ω|² ≥ ||ω||³/(2ν) is NOT proven. It's a
heuristic based on concentration scaling, but the actual |∇ω|² at
the max depends on the spatial profile of ω.

For a BROAD maximum (thick tube): |∇ω|² is small → viscous term small
→ doesn't help. The Q ≥ 0 stretching dominates.

For a NARROW maximum (thin tube): |∇ω|² is large → viscous term large
→ helps. But proving the max is narrow requires... the alignment /
pressure bounds we can't prove.

## 214. Type I + Seregin doesn't close because Q ≥ 0 allows worse rates.
## Viscosity at the max cancels stretching IF |∇ω|² ≥ C||ω||³/ν.
## But this gradient bound is NOT proven (it needs thin tube structure).
