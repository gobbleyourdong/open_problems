---
source: Synthesis of reviewer 1 + reviewer 2 + Grujić + Constantin + our data
type: PROOF ATTEMPT — the full chain
status: IN PROGRESS
date: 2026-03-26
---

## Theorem (Target)

For any smooth divergence-free initial data ω₀ on T³, the solution to the
3D incompressible Navier-Stokes equations remains smooth for all time.

## Proof Strategy

We show that |ω|_max(t) cannot blow up in finite time by proving the
Constantin-Fefferman regularity condition holds at the vorticity maximum.

## Step 1: The Evolution Equation at x*

Let ρ = |ω|, ξ = ω/|ω|. The vorticity equation yields (Constantin):

```
(∂_t + u·∇)ρ − νΔρ + νρ|∇ξ|² = ρα          (*)
```

where α = ξ·Sξ is the stretching rate (S = symmetric part of ∇u).

This is EXACT. The term νρ|∇ξ|² is dissipative for ρ — it represents
the cost of vorticity direction bending. This is why Constantin's
unconditional estimate ∫ρ|∇ξ|² dx dt ≤ C holds.

## Step 2: Evaluate at x*(t)

At x*(t) where ρ achieves its spatial maximum:
- ∇ρ(x*) = 0 (first-order condition)
- Δρ(x*) ≤ 0 (second-order condition, negative semidefinite Hessian)
- ∇ξ(x*) = ∇ω(x*)/|ω(x*)| (simplification: ∇|ω| = 0 at max)

From (*):
```
νρ*|∇ξ*|² = ρ*α* − (∂_t + u·∇)ρ* + νΔρ*
           ≤ ρ*α* − (∂_t + u·∇)ρ*           (since νΔρ* ≤ 0)
```

where * denotes evaluation at x*.

## Step 3: Control the Material Derivative

The material derivative (∂_t + u·∇)ρ at x* equals the rate of change
of the maximum (since ∇ρ = 0, transport doesn't contribute):

```
dρ_max/dt ≈ (∂_t + u·∇)ρ(x*)
```

(This is exact if x* is non-degenerate; technical corrections for
degenerate maxima are standard, see Droniou-Imbert 2006.)

From the same equation (*), evaluated at x*:
```
dρ_max/dt = ρ*α* + νΔρ* − νρ*|∇ξ*|²
          ≤ ρ*α*                              (**)
```

This is the standard BKM inequality: dρ_max/dt ≤ ρ_max × α(x*).

## Step 4: Bound the Stretching at x* (THE KEY STEP)

Standard CZ gives α(x*) ≤ C||ω||_∞ = Cρ_max. This leads to
dρ_max/dt ≤ Cρ_max², which gives at most finite-time blowup (Gronwall).

But at x*, we have BETTER than CZ. The stretching is given by
Constantin's representation:

```
α(x*) = (3/4π) PV ∫ D(ŷ, ξ(x*+y), ξ(x*)) |ω(x*+y)| dy/|y|³
```

where D(v₁,v₂,v₃) = (v₁·v₃) det(v₁,v₂,v₃).

### Near-field cancellation (|y| < δ):

At x*, ρ is at its maximum, so:
(a) |ω(x*+y)| ≤ |ω(x*)| = ρ* for all y
(b) ∇ρ(x*) = 0 → the density is "flat" at quadratic order
(c) ω(x*+y) ≈ ρ*ξ* + (∇ω)*·y + O(|y|²) near x*
(d) ξ(x*+y) ≈ ξ* + (∇ξ)*·y + O(|y|²)
(e) D(ŷ, ξ(x*+y), ξ*) ≈ D(ŷ, ξ* + (∇ξ)*·y, ξ*)
    = D(ŷ, (∇ξ)*·y, ξ*) (since D(ŷ, ξ*, ξ*) = 0)
    = O(|∇ξ*| × |y|)

Therefore the near-field integral contributes:
```
|α_near| ≤ C ρ* |∇ξ*| ∫₀^δ |y| × |y|² / |y|³ dy
         = C ρ* |∇ξ*| δ
```

(The |y|² comes from the volume element, and one factor of |y| from
the D kernel expansion.)

### Far-field contribution (|y| > δ):

The far-field is bounded by standard CZ:
```
|α_far| ≤ C ∫_{|y|>δ} |ω(x*+y)| / |y|³ dy
        ≤ C ||ω||_{L^{3/2}} / δ^{1/2}    (by HLS inequality)
```

### Combine:

```
|α(x*)| ≤ C ρ* |∇ξ*| δ + C ||ω||_{L^{3/2}} / δ^{1/2}
```

Optimize over δ: set δ = (||ω||_{L^{3/2}} / (ρ* |∇ξ*|))^{2/3}

```
|α(x*)| ≤ C ρ*^{1/3} |∇ξ*|^{1/3} ||ω||_{L^{3/2}}^{2/3}
```

### The Sobolev interpolation:

||ω||_{L^{3/2}} is controlled by initial data (energy bound gives
||ω||_{L^1} ≤ C, and ||ω||_{L^2} is bounded by enstrophy which is
finite for smooth solutions on any finite time interval).

So: α(x*) ≤ C ρ*^{1/3} |∇ξ*|^{1/3} × (bounded)

## Step 5: Substitute Back

From Step 2: νρ*|∇ξ*|² ≤ ρ*α* − dρ_max/dt

Using the bound on α*:
```
νρ*|∇ξ*|² ≤ C ρ*^{4/3} |∇ξ*|^{1/3} − dρ_max/dt
```

Let X = |∇ξ*|. We have:
```
νρ* X² ≤ C ρ*^{4/3} X^{1/3} − dρ_max/dt
```

If dρ_max/dt ≤ 0 (max not growing), then:
```
νρ* X² ≤ C ρ*^{4/3} X^{1/3}
X^{5/3} ≤ (C/ν) ρ*^{1/3}
X ≤ (C/ν)^{3/5} ρ*^{1/5}
|∇ξ*| ≤ C' ρ*^{1/5}
```

This gives: |∇ξ*|/ρ*^{1/2} ≤ C' ρ*^{-3/10} → 0 as ρ* → ∞.

THE CF RATIO GOES TO ZERO AS VORTICITY GROWS. Not just bounded — ZERO.

## Step 6: Close the Bootstrap

From (**): dρ_max/dt ≤ ρ*α* ≤ C ρ*^{4/3} |∇ξ*|^{1/3}
         ≤ C ρ*^{4/3} (C' ρ*^{1/5})^{1/3}
         = C ρ*^{4/3 + 1/15}
         = C ρ*^{7/5}

Since 7/5 < 2, this is SUBCRITICAL. Gronwall gives:
```
ρ_max(t) ≤ (ρ_max(0)^{-2/5} − C't)^{-5/2}
```

This blows up at T* = ρ_max(0)^{-2/5} / C' → ∞ as ρ_max(0) → 0.

Wait — this still allows finite-time blowup for large initial data.
The 7/5 exponent is better than 2 (the critical exponent) but not enough
to prevent blowup completely.

## Step 6 (Revised): Use the Full Structure

The issue: we assumed dρ_max/dt ≤ 0 to get the bound on X, then used
X to bound dρ_max/dt. This is a BOOTSTRAP: we assumed the conclusion
to derive a weaker version of it.

To close properly: we need the bound on α* to hold WITHOUT assuming
dρ_max/dt ≤ 0.

From Step 2 (exact, no sign assumption):
```
νρ*|∇ξ*|² = ρ*α* − dρ_max/dt + νΔρ*
```

From Step 4: α* ≤ C ρ*^{1/3} |∇ξ*|^{1/3}

Substituting:
```
νρ* X² = ρ* × C ρ*^{1/3} X^{1/3} − dρ_max/dt + νΔρ*
```

Since νΔρ* ≤ 0 and dρ_max/dt = ρ*α* + νΔρ* − νρ*X² (from (*)):
```
dρ_max/dt = ρ*α* + νΔρ* − νρ*X²
          ≤ ρ*α* − νρ*X²
          ≤ C ρ*^{4/3} X^{1/3} − νρ*X²
```

For this to be positive (max growing): need C ρ*^{4/3} X^{1/3} > νρ*X²
→ X^{5/3} < (C/ν) ρ*^{1/3}
→ X < (C/ν)^{3/5} ρ*^{1/5}

So IF the max is growing, |∇ξ*| < C ρ*^{1/5}. Substituting back:
```
dρ_max/dt ≤ C ρ*^{4/3} (C ρ*^{1/5})^{1/3} − 0
          = C ρ*^{4/3 + 1/15}
          = C ρ*^{7/5}
```

So growth rate ≤ C ρ*^{7/5}. By Gronwall with exponent 7/5 < 2:
```
ρ_max(t) ≤ C / (T* − t)^{5/2}    (if blowup occurs)
```

BKM requires ∫₀^T* ||ω||_∞ dt = ∞. With ρ_max ~ (T*−t)^{-5/2}:
```
∫ (T*−t)^{-5/2} dt diverges at T*
```

So this growth rate IS still compatible with blowup in the BKM sense.

## WHERE IT STANDS

The near-field/far-field splitting gives α* ≤ C ρ*^{1/3} |∇ξ*|^{1/3}.
This is BETTER than CZ (which gives α* ≤ C ρ*) but NOT enough to
prevent blowup on its own. The exponent 7/5 is subcritical for
Gronwall (better than the critical 2) but still allows power-law blowup.

## WHAT'S NEEDED TO CLOSE

Need α* ≤ C ρ*^{1−ε} for some ε > 1/2 to make ∫ ρ*^{1−ε} dt finite
near a potential singularity.

Our bound gives α* ≤ C ρ*^{4/3+1/15} / ρ* = ... wait, let me redo.

Actually: from dρ_max/dt ≤ C ρ*^{7/5}, BKM requires ∫ ρ dt = ∞.
With ρ ~ (T*−t)^{-5/2}: ∫ (T*−t)^{-5/2} dt DOES diverge.

For regularity via BKM: need ρ ~ (T*−t)^{-p} with p ≤ 1 (so integral
converges). Our bound gives p = 5/2 > 1. Not enough.

The gap: need to improve α* ≤ C ρ*^{1/3} |∇ξ*|^{1/3} to
α* ≤ C ρ*^{β} with β < 1. Currently β = 4/3 + 1/15 divided by...

Actually let me reconsider. The bound was:
  dρ/dt ≤ C ρ^{7/5}
This gives ρ ~ (T*-t)^{-5/2}.
BKM: ∫ ρ dt ~ ∫ (T*-t)^{-5/2} dt — diverges. So blowup still possible.

Need: dρ/dt ≤ C ρ^γ with γ ≤ 1. Then ρ grows at most exponentially,
∫ ρ dt grows at most exponentially, always finite. Regularity.

Our γ = 7/5. Need γ ≤ 1. The gap: 7/5 → 1. Factor of 7/5.

## THE REMAINING GAP

The near-field/far-field bound with HLS gives a 1/3 + 1/3 = 2/3
power savings over CZ. We need a full power savings (γ from 2 to 1).
We achieved γ = 7/5 = 1.4. Need γ ≤ 1.0. Gap: 0.4.

HOWEVER: we haven't yet used:
1. The viscous term νΔρ* (dropped it as ≤ 0)
2. The single-mode orthogonality (structural Biot-Savart cancellation)
3. The fact that ∫ρ|∇ξ|² is bounded (Constantin's a priori estimate)
4. The Hessian constraint on the second derivatives at x*

Each of these could improve the bound. The question is by how much.

## COMPUTATIONAL CHECK

Our data shows γ < 1 (in fact γ appears to be 0 since ρ_max doesn't
grow at all — ratio = 1.0000). The analytical bound γ = 7/5 is
PESSIMISTIC. The real exponent is much better, we just haven't
captured it yet in the algebra.

This is the gap: 0.4 in the exponent. Every failure maps the space.
