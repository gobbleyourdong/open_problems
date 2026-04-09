---
source: ANALYTIC BOUND on α/|ω| for two-mode div-free fields
type: PROOF ATTEMPT — if α/|ω| < 1/2 for 2 modes, this closes the gap
file: 306
date: 2026-03-29
---

## Setup

Two real Fourier modes on T³:
  ω = a₁v̂₁cos(k₁·x) + a₂v̂₂cos(k₂·x)

with kᵢ ⊥ v̂ᵢ (divergence-free), |v̂ᵢ| = 1, aᵢ > 0.

Velocity (Biot-Savart):
  u = a₁(k₁×v̂₁)sin(k₁·x)/|k₁|² + a₂(k₂×v̂₂)sin(k₂·x)/|k₂|²

Strain:
  S(x) = S₁(x) + S₂(x)

where Sᵢ(x) = aᵢ sym(kᵢ ⊗ (kᵢ×v̂ᵢ)) cos(kᵢ·x) / |kᵢ|²

## Key Property: α = 0 for single mode at ITS max

For mode i alone at its max (cos(kᵢ·x) = 1):
  êᵢ = v̂ᵢ. α = v̂ᵢ · Sᵢ · v̂ᵢ = aᵢ v̂ᵢ·sym(kᵢ⊗(kᵢ×v̂ᵢ))·v̂ᵢ / |kᵢ|²
  = aᵢ(v̂ᵢ·kᵢ)(v̂ᵢ·(kᵢ×v̂ᵢ)) / |kᵢ|²
  = 0 (because v̂ᵢ ⊥ kᵢ×v̂ᵢ AND v̂ᵢ ⊥ kᵢ)

So EACH mode has zero self-contribution to α at the max.

## At the MIXTURE max

At x* where |ω|² is maximal: ê = ω(x*)/|ω(x*)|.

α(x*) = ê · S₁(x*) · ê + ê · S₂(x*) · ê

The key: ê ≠ v̂₁ and ê ≠ v̂₂ (it's a mixture direction). So each Sᵢ
contributes nonzero to α through the CROSS-alignment.

## Explicit computation of S₁ contribution

S₁(x) = (a₁cos(k₁·x)/(2|k₁|²)) [kᵢ⊗(k₁×v̂₁) + (k₁×v̂₁)⊗k₁]

Let w₁ = k₁×v̂₁ (perpendicular to both k₁ and v̂₁).

ê · S₁ · ê = (a₁cos(k₁·x)/(2|k₁|²)) [(ê·k₁)(ê·w₁) + (ê·w₁)(ê·k₁)]
           = a₁cos(k₁·x)(ê·k₁)(ê·w₁)/|k₁|²

Similarly for S₂ with w₂ = k₂×v̂₂:
ê · S₂ · ê = a₂cos(k₂·x)(ê·k₂)(ê·w₂)/|k₂|²

So: α = a₁c₁(ê·k₁)(ê·w₁)/|k₁|² + a₂c₂(ê·k₂)(ê·w₂)/|k₂|²

where cᵢ = cos(kᵢ·x*).

## At the max of |ω|

At x*: ω = a₁v̂₁c₁ + a₂v̂₂c₂. So ê = (a₁v̂₁c₁+a₂v̂₂c₂)/|ω|.

ê · k₁ = (a₁(v̂₁·k₁)c₁ + a₂(v̂₂·k₁)c₂)/|ω| = a₂c₂(v̂₂·k₁)/|ω|
(using v̂₁ ⊥ k₁).

ê · w₁ = (a₁(v̂₁·w₁)c₁ + a₂(v̂₂·w₁)c₂)/|ω| = a₂c₂(v̂₂·w₁)/|ω|
(using v̂₁ ⊥ w₁ = k₁×v̂₁).

So: ê·S₁·ê = a₁c₁ × [a₂c₂(v̂₂·k₁)/|ω|] × [a₂c₂(v̂₂·w₁)/|ω|] / |k₁|²
            = a₁a₂²c₁c₂² (v̂₂·k₁)(v̂₂·w₁) / (|k₁|²|ω|²)

Similarly:
ê · S₂ · ê = a₁²a₂c₁²c₂ (v̂₁·k₂)(v̂₁·w₂) / (|k₂|²|ω|²)

## The ratio α/|ω|

α = [a₁a₂²c₁c₂²(v̂₂·k₁)(v̂₂·w₁)/|k₁|² + a₁²a₂c₁²c₂(v̂₁·k₂)(v̂₁·w₂)/|k₂|²] / |ω|²

|ω|² = a₁²c₁² + a₂²c₂² + 2a₁a₂c₁c₂(v̂₁·v̂₂)

α/|ω| = α / √(|ω|²) = [a₁a₂²c₁c₂²P₁/|k₁|² + a₁²a₂c₁²c₂P₂/|k₂|²] / |ω|³

where P₁ = (v̂₂·k₁)(v̂₂·w₁) and P₂ = (v̂₁·k₂)(v̂₁·w₂).

## Bound on P₁

|P₁| = |(v̂₂·k₁)(v̂₂·(k₁×v̂₁))| ≤ |v̂₂·k₁| × |v̂₂·(k₁×v̂₁)|.

Since v̂₂ is a unit vector and k₁, k₁×v̂₁ are orthogonal to v̂₁:
The subspace ⊥ v̂₁ contains k₁ and k₁×v̂₁ (which are perpendicular to each other in this subspace).

v̂₂ projected onto ⊥ v̂₁: v̂₂⊥ = v̂₂ - (v̂₂·v̂₁)v̂₁. |v̂₂⊥|² = 1-(v̂₁·v̂₂)².

In ⊥ v̂₁: k₁/|k₁| and k₁×v̂₁/(|k₁|) are orthonormal. So:
v̂₂⊥ = (v̂₂·k̂₁)k̂₁ + (v̂₂·ŵ₁)ŵ₁ where k̂₁ = k₁/|k₁|, ŵ₁ = k₁×v̂₁/|k₁|.

Then: (v̂₂·k₁)(v̂₂·w₁) = |k₁|²(v̂₂·k̂₁)(v̂₂·ŵ₁).

By AM-GM: |(v̂₂·k̂₁)(v̂₂·ŵ₁)| ≤ [(v̂₂·k̂₁)² + (v̂₂·ŵ₁)²]/2 = |v̂₂⊥|²/2 = (1-(v̂₁·v̂₂)²)/2.

So: |P₁| ≤ |k₁|²(1-(v̂₁·v̂₂)²)/2.

Similarly: |P₂| ≤ |k₂|²(1-(v̂₁·v̂₂)²)/2.

## Substituting back

|α| ≤ [a₁a₂²|c₁|c₂²(1-d²)/2 + a₁²a₂c₁²|c₂|(1-d²)/2] / |ω|²

where d = v̂₁·v̂₂.

= (1-d²)a₁a₂(a₂|c₁|c₂² + a₁c₁²|c₂|) / (2|ω|²)

= (1-d²)a₁a₂|c₁c₂|(a₂|c₂| + a₁|c₁|) / (2|ω|²)

Now |ω|² ≥ (a₁|c₁| + a₂|c₂|)² × cos²(φ/2) where φ is the angle between
the vorticity components... actually let me be more careful.

|ω|² = |a₁v̂₁c₁ + a₂v̂₂c₂|² = a₁²c₁² + a₂²c₂² + 2a₁a₂c₁c₂d

At the max of |ω|: both c₁, c₂ have the same sign (to maximize addition).
Take c₁, c₂ > 0. Then |ω|² = a₁²c₁² + a₂²c₂² + 2a₁a₂c₁c₂d.

For d ≥ 0 (v̂₁·v̂₂ ≥ 0): |ω|² ≥ (a₁c₁ + a₂c₂)² × min(1, something...).
Actually: |ω|² ≥ (a₁c₁)² + (a₂c₂)² ≥ (a₁c₁ + a₂c₂)²/2 (Cauchy-Schwarz reverse).

For the bound:
|α/|ω|| ≤ (1-d²) a₁a₂c₁c₂(a₁c₁ + a₂c₂) / (2|ω|³)

≤ (1-d²) a₁a₂c₁c₂(a₁c₁+a₂c₂) / (2[(a₁c₁)²+(a₂c₂)²+2a₁a₂c₁c₂d]^{3/2})

Let t = a₁c₁/(a₁c₁+a₂c₂) ∈ [0,1] and S = a₁c₁+a₂c₂. Then:
a₁c₁ = tS, a₂c₂ = (1-t)S.

|ω|² = t²S² + (1-t)²S² + 2t(1-t)S²d = S²[t²+(1-t)²+2t(1-t)d]
     = S²[1-2t(1-t)(1-d)]

|α| ≤ (1-d²)t(1-t)S³ / (2 × S³[1-2t(1-t)(1-d)]^{3/2})
     = (1-d²)t(1-t) / (2[1-2t(1-t)(1-d)]^{3/2})

And |ω| = S√[1-2t(1-t)(1-d)].

So: |α/|ω|| ≤ (1-d²)t(1-t) / (2[1-2t(1-t)(1-d)]^{3/2}) / √[1-2t(1-t)(1-d)]

Wait, I need to be more careful:
|α/|ω|| = |α|/|ω| ≤ numerator / |ω|³ × |ω|² = numerator / |ω|

Hmm, let me redo.

|α| ≤ (1-d²)a₁a₂c₁c₂(a₁c₁+a₂c₂) / (2|ω|²)
= (1-d²)t(1-t)S² × S / (2|ω|²)
= (1-d²)t(1-t)S / (2[1-2t(1-t)(1-d)])

|ω| = S√[1-2t(1-t)(1-d)]

|α/|ω|| ≤ (1-d²)t(1-t) / (2[1-2t(1-t)(1-d)]^{3/2})

## Maximizing over t and d

Let u = t(1-t) ∈ [0, 1/4] and let g = 1-d ∈ [0, 2] (d = v̂₁·v̂₂ ∈ [-1,1]).

f(u,g) = (1-(1-g)²)u / (2(1-2ug)^{3/2}) = (2g-g²)u / (2(1-2ug)^{3/2})

Maximize over u ∈ [0, 1/4] and g ∈ [0, 2]:

∂f/∂u = (2g-g²)/2 × [(1-2ug)^{3/2} - u×(-3g)(1-2ug)^{1/2}] / (1-2ug)³
       = (2g-g²)/2 × (1-2ug+3ug) / (1-2ug)^{5/2}
       = (2g-g²)(1+ug) / (2(1-2ug)^{5/2})

This is POSITIVE for g > 0, u > 0, 1-2ug > 0. So f increases with u.

Maximum u = 1/4 (t = 1/2): equal amplitudes.

f(1/4, g) = (2g-g²)/4 / (2(1-g/2)^{3/2}) = (2g-g²) / (8(1-g/2)^{3/2})

Let h = g/2 ∈ [0, 1): f = (4h-4h²)/(8(1-h)^{3/2}) = h(1-h)/(2(1-h)^{3/2}) = h/(2√(1-h))×1/√(1-h)

Wait: f(1/4, g) = (2g-g²)/(8(1-g/2)^{3/2}).

With g = 2h: (4h-4h²)/(8(1-h)^{3/2}) = 4h(1-h)/(8(1-h)^{3/2}) = h/(2(1-h)^{1/2}).

So f = h/(2√(1-h)) where h = (1-d)/2 ∈ [0,1).

As h → 1 (d → -1): f → ∞. But d = -1 means v̂₁ = -v̂₂ (anti-parallel polarizations).
When d = -1: |ω|² = (a₁c₁-a₂c₂)². At t=1/2 (equal amps), |ω| = 0!
So f → ∞ but |ω| → 0. NOT at a max.

The constraint: we need to be at a MAX of |ω|, which requires |ω| to be large.

For d near -1 (anti-parallel v̂): |ω| ≈ |a₁c₁-a₂c₂| which is small if amplitudes
are equal. The max of |ω| shifts to where one mode dominates (c₁ near 1, c₂ near 0),
giving |ω| ≈ a₁ and α ≈ 0 (single-mode regime).

SO: the maximum of α/|ω| AT THE MAX OF |ω| is NOT at d → -1.

## The constrained problem

At the max of |ω|² over x (for fixed d, t, S): x* where both cos(kᵢ·x)
are optimal. For non-parallel k₁, k₂: the max has c₁ = c₂ = 1.

With c₁ = c₂ = 1:
|ω|² = a₁² + a₂² + 2a₁a₂d = (a₁+a₂)² - 2a₁a₂(1-d).

With t = 1/2 (a₁ = a₂ = a): |ω|² = 2a²(1+d). And S = 2a.

f = (1-d²)×(1/4)S / (2[1-1/2×(1-d)]×S) ... let me recompute with c₁=c₂=1.

|α| ≤ (1-d²)a₁a₂(a₁+a₂) / (2(a₁²+a₂²+2a₁a₂d))

With a₁=a₂=a:
|α| ≤ (1-d²)a²×2a / (2(2a²+2a²d)) = (1-d²)×2a³ / (4a²(1+d)) = (1-d)(1+d)×a / (2(1+d)) = (1-d)a/2.

|ω| = a√(2(1+d)).

|α/|ω|| ≤ (1-d)a / (2a√(2(1+d))) = (1-d) / (2√(2(1+d))).

## THE TWO-MODE BOUND (equal amplitude, at the max)

f(d) = (1-d) / (2√(2(1+d))) for d = v̂₁·v̂₂ ∈ (-1, 1].

Maximize over d: f'(d) = [-2√(2(1+d)) - (1-d)×2/(2√(2(1+d)))] / (8(1+d))
Numerator: -2√(2(1+d)) - (1-d)/√(2(1+d)) = [-2×2(1+d) - (1-d)] / √(2(1+d))
= [-4-4d-1+d] / √(2(1+d)) = [-5-3d] / √(2(1+d))

This is ALWAYS negative for d > -5/3 (which includes all of [-1,1]).

So f(d) is DECREASING in d. Maximum at d → -1.

But at d = -1: |ω| → 0 (cancellation). f(d) → ∞ but |ω| → 0.

The issue: we assumed c₁ = c₂ = 1. For anti-parallel v̂ with c₁=c₂=1:
|ω|² = 2a²(1+d) → 0 as d → -1. The max of |ω| is NOT at c₁=c₂=1 when d < 0!

For d < 0: the max might shift to where one cosine is 1 and the other is < 1.

## THE CONSTRAINT: TRUE MAX OF |ω|

For the TRUE max of |ω|² on T³:

|ω(x)|² = a₁²cos²(k₁·x) + a₂²cos²(k₂·x) + 2a₁a₂d cos(k₁·x)cos(k₂·x)

Setting ∂/∂x = 0 gives (for non-parallel k₁, k₂):
Either cos(kᵢ·x) = ±1 for both i, or a more complex critical point.

For k₁ ⊥ k₂ (e.g., k₁=(1,0,0), k₂=(0,1,0)):
|ω|² = a₁²cos²x + a₂²cos²y + 2a₁a₂d cos x cos y

Critical point: -2a₁²sin x cos x - 2a₁a₂d sin x cos y = 0 → sin x(a₁cos x + a₂d cos y) = 0
Similarly: sin y(a₂cos y + a₁d cos x) = 0.

Case sin x = sin y = 0 (i.e., x,y ∈ {0,π}): cos x, cos y ∈ {±1}.
Max: |ω|² = a₁² + a₂² + 2a₁a₂|d| (choosing signs to make d-term positive).
If d > 0: cos x = cos y = 1. |ω|² = (a₁+a₂)² - 2a₁a₂(1-d).
If d < 0: cos x = 1, cos y = -1 (or vice versa). |ω|² = a₁² + a₂² - 2a₁a₂d = a₁²+a₂²+2a₁a₂|d|.

So the max always has |ω|² = a₁² + a₂² + 2a₁a₂|d|. The EFFECTIVE d at the max is |d|!

## CORRECTED BOUND

At the max (effective d → |d|):
|α/|ω|| ≤ (1-|d|) / (2√(2(1+|d|))) where |d| = |v̂₁·v̂₂| ∈ [0, 1].

For |d| = 0 (perpendicular polarizations): f = 1/(2√2) ≈ 0.354.
For |d| → 1 (parallel): f → 0.
For |d| = 0.5: f = 0.5/(2√3) ≈ 0.144.

## THE MAXIMUM IS 1/(2√2) ≈ 0.354

Achieved at |d| = 0 (v̂₁ ⊥ v̂₂), equal amplitudes, at the lattice max.

## THIS IS STRICTLY LESS THAN 1/2!

For ANY two-mode div-free field on T³:
  α/|ω| ≤ 1/(2√2) ≈ 0.354 at the vorticity maximum.

The gap to 1/2: 0.146 (29% margin).

## CRITICAL CAVEAT

This bound used AM-GM on (v̂₂·k̂₁)(v̂₂·ŵ₁) ≤ |v̂₂⊥|²/2.
AM-GM is TIGHT only when v̂₂·k̂₁ = ±v̂₂·ŵ₁ (45° in the k₁-w₁ plane).
This might not be achievable simultaneously with the max condition.

Need to verify with the numerical computation.

## IF CONFIRMED: THE PROOF PATH

For N ≥ 2 modes: α/|ω| ≤ C_N < 1/2 at the max.
For N = 1: α = 0.
For N = 2: α/|ω| ≤ 1/(2√2) ≈ 0.354.
For N → ∞: α/|ω| → ??? (might approach 1/2 from below).

NS solutions (t > 0) have all modes active (analyticity).
If the N → ∞ limit stays < 1/2: REGULARITY FOLLOWS.

## 306. Two-mode bound: α/|ω| ≤ 1/(2√2) ≈ 0.354.
## Need to verify and extend to N modes.
