---
source: Bootstrap argument combining evolution equation + a priori bounds
type: PROOF ATTEMPT — the bootstrap
status: IN PROGRESS
date: 2026-03-26
---

## The Bootstrap Argument

### Setup

Consider a smooth solution of 3D NS on T³ with viscosity ν > 0.
Let ρ(t) = |ω(·,t)|_∞ = max_x |ω(x,t)| be the maximum vorticity.
Let x*(t) be the point where the max is achieved.

### The Exact Equation at x*

From Constantin (standard calculation):
```
dρ/dt = ρα + νΔρ − νρ|∇ξ|²                    (E1)
```
where all quantities evaluated at x*(t), and:
- α = ξ·Sξ (stretching rate)
- Δρ ≤ 0 (maximum principle)
- |∇ξ|² ≥ 0 (non-negative)

Therefore:
```
dρ/dt ≤ ρα − νρ|∇ξ|²                           (E2)
```

### Rearranging: The Stretching-Dissipation Balance

From (E1): νρ|∇ξ|² = ρα − dρ/dt + νΔρ

Since νΔρ ≤ 0:
```
νρ|∇ξ|² ≤ ρα − dρ/dt                           (E3)
```

And also (from E1 directly):
```
ρα = dρ/dt − νΔρ + νρ|∇ξ|²
   ≥ dρ/dt + νρ|∇ξ|²                            (E4)
```

### Key Identity: Integrate (E1) in Time

Integrate (E1) from 0 to T:
```
ρ(T) − ρ(0) = ∫₀ᵀ ρα dt + ν∫₀ᵀ Δρ dt − ν∫₀ᵀ ρ|∇ξ|² dt    (E5)
```

Rearrange:
```
∫₀ᵀ ρα dt = [ρ(T)−ρ(0)] − ν∫₀ᵀ Δρ dt + ν∫₀ᵀ ρ|∇ξ|² dt     (E6)
```

Now, each term on the right:

**Term 1:** ρ(T) − ρ(0) = |ω|_max(T) − |ω|_max(0).
Bounded if ρ doesn't blow up (which is what we want to prove).

**Term 2:** −ν∫₀ᵀ Δρ dt. Since Δρ ≤ 0 at x*, this is ≥ 0.
It equals ν∫₀ᵀ |Δρ| dt — the accumulated viscous smoothing at x*.

**Term 3:** ν∫₀ᵀ ρ|∇ξ|² dt — the accumulated direction-bending cost.

### The A Priori Bound (Constantin, Unconditional)

For ANY Leray solution:
```
∫₀ᵀ ∫_{T³} ρ|∇ξ|² dx dt ≤ C₀ := (1/2ν²)||u₀||²_{L²}     (AP)
```

This bounds the SPACE-TIME integral. At x*, ρ|∇ξ|² is one value
among all points. The integral over space is ≥ this one value
times... well, it's not directly extractable.

BUT: there's a subtlety. The a priori bound (AP) controls the
integral of ρ|∇ξ|² over ALL of T³. If ρ|∇ξ|² were concentrated
at x*, the pointwise value could be as large as the integral.
But if it's spread out, the pointwise value is small.

### The Connection: Maximum of ρ × Spread of |∇ξ|²

At x*, ρ = ρ_max (the global maximum). So:
```
ρ_max × |∇ξ(x*)|² ≤ ρ(x*)|∇ξ(x*)|²
```
is one term in the spatial integral. We can't bound the pointwise
value from the integral alone.

HOWEVER, we can use the EQUATION. From (E3):
```
νρ|∇ξ|² ≤ ρα − dρ/dt
```

And from BKM-type bounds: α ≤ C||ω||_∞ log(1 + ||∇ω||_{L²})
(the Beale-Kato-Majda logarithmic estimate).

### A Different Approach: Use (E6) Directly

From (E6):
```
∫₀ᵀ ρα dt = [ρ(T)−ρ(0)] − ν∫₀ᵀ Δρ dt + ν∫₀ᵀ ρ|∇ξ|² dt
```

The left side is what we want to control (time-integrated stretching
weighted by ρ).

The right side has three terms. Term 1 is bounded IF ρ is bounded.
Terms 2 and 3 are both non-negative (viscous contributions).

This looks circular: ∫ρα is bounded IF ρ is bounded.

### Breaking the Circularity

The BKM criterion: blowup iff ∫₀^{T*} ρ dt = ∞.

From (E2): dρ/dt ≤ ρα − νρ|∇ξ|² ≤ ρα.
So: d(log ρ)/dt ≤ α.
Integrating: log(ρ(T)/ρ(0)) ≤ ∫₀ᵀ α dt.

For BKM: if ∫₀^{T*} ρ dt = ∞, then ρ → ∞. For ρ → ∞,
we need ∫α dt → ∞. But from the evolution equation:

```
∫₀ᵀ α dt = log(ρ(T)/ρ(0)) + ν∫₀ᵀ |∇ξ|² dt − ν∫₀ᵀ Δρ/ρ dt
```

The second and third terms are NON-NEGATIVE (|∇ξ|² ≥ 0, Δρ/ρ ≤ 0).

So: **∫₀ᵀ α dt ≥ log(ρ(T)/ρ(0))**

If ρ → ∞ at T*, then ∫α dt → ∞. This is consistent — doesn't help.

But also: **∫₀ᵀ α dt = log(ρ(T)/ρ(0)) + (positive viscous terms)**

The viscous terms GROW as ρ grows (because |∇ξ|² and |Δρ|/ρ increase
with the complexity of the vorticity field). The question: do the
viscous terms grow FASTER than log ρ?

### The Critical Insight

From (E1) at x*:
```
α = dρ/(ρdt) − νΔρ/ρ + ν|∇ξ|²
  = d(log ρ)/dt + ν|Δρ|/ρ + ν|∇ξ|²
```

So: α − d(log ρ)/dt = ν(|Δρ|/ρ + |∇ξ|²) ≥ 0

The stretching EXCEEDS the growth rate by exactly the viscous terms.
The viscous terms represent the "tax" on stretching — the geometric
cost of maintaining the stretching configuration.

Integrating:
```
∫₀ᵀ α dt − log(ρ(T)/ρ(0)) = ν∫₀ᵀ (|Δρ|/ρ + |∇ξ|²) dt ≥ 0    (E7)
```

The viscous tax is always non-negative. The stretching must pay for
both the growth AND the tax.

### The Tax Grows Faster Than the Growth

If ρ → ∞, then by interpolation inequalities:
```
|Δρ| ≥ c × |∇ρ|² / ρ ≥ 0    (at the max, from Hessian)
```

And from elliptic regularity applied to the Biot-Savart relation:
```
|∇ξ|² = |∇ω|²/ρ² ≥ (something related to the spectral content)
```

The key question: as ρ → ∞ (approaching blowup), does the viscous
tax ν∫(|Δρ|/ρ + |∇ξ|²) dt grow faster than log ρ?

If YES: the stretching integral ∫α dt = log ρ + tax is dominated
by the tax, which is controlled by Constantin's a priori bound.
Then ∫α dt is bounded → log ρ is bounded → ρ is bounded → regularity.

### Using Constantin's Bound on the Tax

From (AP): ∫₀ᵀ ∫ ρ|∇ξ|² dx dt ≤ C₀

This is a SPACE-TIME integral, not just at x*. But at x*, ρ = ρ_max.
If the vorticity is concentrated near x* (as it must be near blowup —
Grujić showed the super-level sets shrink), then:

∫ ρ|∇ξ|² dx ≈ ρ_max × |∇ξ(x*)|² × Vol(blob)

where Vol(blob) ~ ρ_max^{-3/2} (from the L¹ bound on ω + concentration).

So: ρ_max × |∇ξ(x*)|² × ρ_max^{-3/2} ≤ C per unit time
→ |∇ξ(x*)|² ≤ C × ρ_max^{1/2}

Then: ν∫₀ᵀ |∇ξ(x*)|² dt ≤ νC ∫₀ᵀ ρ^{1/2} dt

And from BKM: if ρ ~ (T*−t)^{-p} near blowup, then:
∫ ρ^{1/2} dt ~ ∫ (T*−t)^{-p/2} dt

This converges if p/2 < 1, i.e., p < 2.

From the γ = 7/5 bound: dρ/dt ≤ Cρ^{7/5} gives p = 5/2.
Then p/2 = 5/4 > 1 — the integral DIVERGES. Tax grows to ∞.

### THE CONTRADICTION

Near a potential blowup (ρ → ∞ at T*):

From (E7):
```
∫₀ᵀ α dt = log(ρ(T)/ρ(0)) + ν∫₀ᵀ (|Δρ|/ρ + |∇ξ|²) dt
```

**Left side:** ∫α dt = ∫(d log ρ/dt + tax) dt → log ρ(T) + ∫tax dt

**The tax integral:** Using the volume concentration + Constantin's bound:
|∇ξ(x*)|² ≤ C ρ^{1/2}, so ∫|∇ξ|² dt ≤ C ∫ρ^{1/2} dt.

If ρ ~ (T*−t)^{-5/2} (from γ = 7/5): ∫ρ^{1/2} dt ~ ∫(T*−t)^{-5/4} dt
→ DIVERGES at T*.

But Constantin's bound says ∫∫ ρ|∇ξ|² dx dt ≤ C₀ (FINITE).

The spatial integral ∫ ρ|∇ξ|² dx ≥ ρ_max |∇ξ(x*)|² × Vol ≥ |∇ξ(x*)|² × Vol × ρ_max.

If Vol ~ ρ_max^{-3/2}:
∫ ρ|∇ξ|² dx ≥ |∇ξ(x*)|² × ρ_max^{-1/2}

So: ∫₀ᵀ |∇ξ(x*)|² × ρ_max^{-1/2} dt ≤ ∫₀ᵀ ∫ ρ|∇ξ|² dx dt ≤ C₀

Therefore: ∫₀ᵀ |∇ξ(x*)|² dt ≤ C₀ × max ρ_max^{1/2}

Hmm, this doesn't give what I need. The bound involves max ρ^{1/2}
on the right, which blows up.

## Where This Stands (Honest)

The bootstrap attempt reveals:
1. The stretching = growth + viscous tax (exact)
2. The viscous tax is non-negative (viscosity helps)
3. Near blowup, the tax SHOULD grow faster than the growth
4. Constantin's a priori bound constrains the tax
5. But extracting the POINTWISE tax at x* from the INTEGRAL bound
   still requires the volume concentration estimate
6. The volume concentration gives Vol ~ ρ^{-3/2}, which is not
   tight enough to close

## What's Missing

The volume concentration estimate Vol ~ ρ^{-3/2} comes from
||ω||_{L¹} ≤ C (bounded) + Chebyshev. This is CRUDE.

Grujić (2012) showed that near blowup, the super-level sets form
FILAMENTS with cross-section diameter ~ ρ^{-1/2}. If the filament
length is L (macro-scale), then:

Vol ~ L × ρ^{-1} (cross-section area × length)

This is BETTER than ρ^{-3/2}. With Vol ~ L × ρ^{-1}:
∫ ρ|∇ξ|² dx ≥ |∇ξ(x*)|² × ρ × L × ρ^{-1} = |∇ξ(x*)|² × L

So: ∫₀ᵀ |∇ξ(x*)|² × L dt ≤ C₀

If L stays macro-scale (≥ c > 0): ∫₀ᵀ |∇ξ(x*)|² dt ≤ C₀/c

Then from (E7):
∫₀ᵀ α dt = log ρ(T) + ν∫|∇ξ|² dt ≤ log ρ(T) + νC₀/c

For this to be consistent with log ρ(T) → ∞ (blowup):
νC₀/c must be ≥ 0 (always true) but this doesn't prevent log ρ → ∞.

THE REMAINING GAP: log ρ(T) → ∞ is consistent with ∫α dt → ∞
and the viscous tax being finite. The tax doesn't grow fast enough
to prevent blowup in this argument.

## Conclusion

The bootstrap doesn't close with the current ingredients.
The fundamental issue: the viscous tax at x* is bounded by
Constantin's integral, but dividing by the spatial concentration
factor introduces ρ_max dependence that eats the bound.

The approach that MIGHT work: show the tax grows SUPERLINEARLY
in log ρ. This would require the direction-bending |∇ξ|² to
increase faster than ρ near blowup — i.e., the vorticity field
becomes increasingly "twisted" as it concentrates. This is
exactly the Buaria anti-twist mechanism: concentration creates twist,
twist creates direction bending, direction bending kills stretching.

If |∇ξ|² ~ ρ^β for some β > 0 near blowup, then the tax
∫ρ^β dt diverges faster than log ρ, creating the contradiction.

Our DATA shows |Δω|/|ω|² is bounded (≈ 8-20) and |∇ξ| ~ O(1).
So |∇ξ|² ~ constant, not growing with ρ. The tax ∫|∇ξ|² dt ~ T,
while log ρ → ∞. The tax is LINEAR in T while the growth is
LOGARITHMIC... wait, that means the tax DOES dominate for large T!

∫₀ᵀ α dt = log ρ(T) + ν × (at least c × T)

If the tax is ≥ cT (direction bending persists for all time),
then ∫α dt ≥ cT, and log ρ(T) ≤ ∫α dt − cT + C.

From BKM: dρ/dt ≤ ρ × α ≤ ρ × (∫α accumulated rate).

Hmm, this isn't directly useful either. The log ρ and ∫α are
related but not in a way that creates a contradiction.

## True Status

Every path leads to the same wall: extracting pointwise info at x*
from integral bounds. The bridge is the VOLUME CONCENTRATION near
blowup + the STRUCTURE of the Biot-Savart operator.

Grujić's "filament length must be macro-scale" is the same gap.
We haven't closed it. But we've mapped it precisely.

The data says γ = 0. The best theory says γ = 7/5.
The proof needs γ ≤ 1. Gap: 2/5.

Every failure maps the space.
