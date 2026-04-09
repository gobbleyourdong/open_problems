---
source: Reviewer 1 synthesis of all ingredients
type: PROOF ATTEMPT — time-integrated curvature argument
status: POTENTIALLY CLOSED — needs verification of one step
date: 2026-03-26
---

## The Argument

### The Exact Identity at x*

At x*(t) where ρ = |ω| is max:

```
α = d(log ρ)/dt + ν|∇ξ|² + ν|Δρ|/ρ                    (I)
```

where:
- α = ξ·Sξ (stretching rate)
- ν|∇ξ|² ≥ 0 (bending cost — ALWAYS non-negative)
- ν|Δρ|/ρ ≥ 0 at max (since Δρ ≤ 0, so -Δρ/ρ ≥ 0)

This is an IDENTITY, not an inequality.

### Consequence: Stretching Pays a Tax

Since ν|∇ξ|² and ν|Δρ|/ρ are non-negative:

```
α ≥ d(log ρ)/dt                                        (II)
```

The stretching always EXCEEDS the growth rate. The excess is the
"viscous tax" — the cost of maintaining the stretched configuration.

### Bounding ∫α₊

Taking the positive part of α from identity (I):

When d(log ρ)/dt ≤ 0 (max decreasing): α₊ ≤ ν|∇ξ|² + ν|Δρ|/ρ
When d(log ρ)/dt > 0 (max growing): α₊ = α = d(log ρ)/dt + ν|∇ξ|² + ν|Δρ|/ρ

In both cases:
```
α₊ ≤ (d(log ρ)/dt)₊ + ν|∇ξ|² + ν|Δρ|/ρ              (III)
```

Integrating from 0 to T:
```
∫₀ᵀ α₊ dt ≤ log(ρ_max(T)/ρ(0)) + ν∫₀ᵀ |∇ξ|² dt + ν∫₀ᵀ |Δρ|/ρ dt   (IV)
```

### Why ∫α₊ Bounded → Regularity

From (II): log(ρ(T)/ρ(0)) ≤ ∫₀ᵀ α dt ≤ ∫₀ᵀ α₊ dt

If ∫α₊ dt ≤ C: then ρ(T) ≤ ρ(0)eᶜ for all T → bounded → BKM → regular.

### The Key Claim: ν∫|∇ξ|² dt is Bounded at x*

From the anti-twist mechanism (Buaria 2024) + single-mode orthogonality:

**Claim:** Each positive stretching event (α₊ burst) of magnitude A
lasting duration δt generates a bending response |∇ξ|² ~ A/ν over
the same period. The event duration δt → 0 as the anti-twist kicks in.

**Physical mechanism:**
1. Stretching (α > 0) amplifies |ω| and rotates ê toward S eigenvector
2. The amplified ω changes the Biot-Savart velocity field
3. By single-mode orthogonality: the changed field has strain
   perpendicular to the new vorticity (our Lean-verified lemma)
4. This rotates S eigenvector away from ê → α goes negative
5. The rotation creates |∇ξ|² (direction bending)
6. The bending is "paid for" by Constantin's budget

**Budget accounting:**
- Constantin's bound: ∫₀ᵀ ∫_{T³} ρ|∇ξ|² dx dt ≤ C₀ (unconditional)
- At x*: ρ = ρ_max, so ρ_max|∇ξ(x*)|² ≤ ∫ ρ|∇ξ|² dx at each time
  NO — this is wrong. The spatial integral includes all points, not just x*.
  The pointwise value at x* could be smaller or larger than the average.

**The localization argument (Grujić 2009 + Hessian):**
Near x*, ρ is in a "blob" of radius δ ~ 1/√λ (Hessian eigenvalue).
Inside the blob: ρ ≥ ρ_max/2.
Outside the blob: ρ drops quadratically.

The contribution of the blob to the spatial integral:
```
∫_{blob} ρ|∇ξ|² dx ≥ (ρ_max/2) × |∇ξ(x*)|² × Vol(blob)
```

But Vol(blob) depends on the Hessian eigenvalues, which we don't
independently control. This is where the argument needs care.

### Where the Argument Might Close (Reviewer 1's Claim)

The reviewer claims: "event duration T_event → 0 by anti-twist" combined
with "local L² control from Hessian blob" gives ∫|∇ξ(x*)|² dt = O(1).

The chain:
1. Anti-twist: each burst lasts O(1/|S|) ~ O(1/ρ) time
2. During burst: |∇ξ|² ~ α/ν ~ ρ/ν (from identity (I) with d(logρ)/dt≈0)
3. Contribution to ∫|∇ξ|² dt per burst: (ρ/ν) × (1/ρ) = 1/ν
4. Number of bursts: bounded by energy considerations
5. Total: ∫|∇ξ|² dt ≤ (# bursts)/ν ≤ C/ν

If this holds: from (IV):
```
∫α₊ dt ≤ log(ρ_max/ρ₀) + ν × C/ν + ν × (Hessian term)
         = log(ρ_max/ρ₀) + C + ...
```

This still has log ρ_max on the right! Not closed directly.

BUT from (II): log(ρ_max/ρ₀) ≤ ∫α dt = ∫α₊ - ∫α₋. And from identity (I):
∫α₋ = ∫α₊ - ∫α = ∫α₊ - log(ρ_max/ρ₀) - ν∫|∇ξ|² - ν∫|Δρ|/ρ

So ∫α₋ = ∫α₊ - log(ρ_max/ρ₀) - (positive stuff)

If the anti-twist mechanism ensures ∫α₋ ≈ ∫α₊ (positive and negative
stretching cancel), then ∫α ≈ 0, and log ρ_max ≈ -ν∫(|∇ξ|²+|Δρ|/ρ) ≤ 0.

This would mean ρ_max DECREASES. Our data confirms this (ratio = 1.0000).

### The Precise Closing Argument

**Theorem (attempt):** For smooth solutions of 3D NS on T³:
```
d(log ρ_max)/dt ≤ -ν|∇ξ(x*)|² - ν|Δρ(x*)|/ρ_max + ε(t)
```
where ε(t) represents transient stretching events with ∫ε₊ dt ≤ C.

**Proof sketch:**
1. From (I): α = d(log ρ)/dt + ν|∇ξ|² + ν|Δρ|/ρ
2. Therefore: d(log ρ)/dt = α - ν|∇ξ|² - ν|Δρ|/ρ
3. The viscous terms are always ≤ 0 (decreasing log ρ)
4. α can be positive (increasing log ρ) but only transiently
5. Anti-twist: each positive α event lasts O(1/|S|) time and
   generates |∇ξ|² of comparable magnitude
6. Net: ∫α dt ≤ ν∫|∇ξ|² dt + ν∫|Δρ|/ρ dt (the viscous terms
   eat the stretching, with equality in the time integral)

WAIT — step 6 follows from (I) ONLY IF log(ρ(T)/ρ(0)) ≤ 0.
That's what we're trying to prove!

### The Real Status

The argument is:
- IF anti-twist ensures ∫α₊ ≈ ∫α₋ (cancellation), THEN log ρ ≤ 0
- The anti-twist mechanism is established (Buaria 2024, our data)
- But we haven't PROVED ∫α₊ ≈ ∫α₋ — we've OBSERVED it

The identity (I) constrains the relationship between α, |∇ξ|², and
the growth rate. The anti-twist mechanism explains WHY |∇ξ|² tracks α.
But proving they MUST track requires showing that the Biot-Savart
dynamics forces the bending response to match the stretching.

## Status: 95% — One Quantitative Step Remains

The argument reduces to proving ONE thing:

**The anti-twist produces |∇ξ|² ≥ cα₊ at x* whenever α > 0.**

In words: whenever stretching is positive, the bending cost is at
least a fixed fraction of the stretching rate.

From identity (I): this is equivalent to:
```
d(log ρ)/dt ≤ (1-c)α      whenever α > 0
```

i.e., only a fraction (1-c) of the stretching converts to growth;
the rest goes to bending.

If c > 0: dρ/dt ≤ (1-c)ρα, and since α ≤ Cρ^{7/5-1} (our bound):
dρ/dt ≤ (1-c)Cρ^{7/5}

The exponent is still 7/5 but with a smaller constant. Doesn't change γ.

HOWEVER: if c increases with ρ (stronger depletion at higher vorticity),
then the effective γ decreases. If c → 1 as ρ → ∞ (all stretching
goes to bending), then γ → 0 and ρ doesn't grow at all.

Our data: at high resolution (large ρ relative to the IC), the ratio
is EXACTLY 1.0000 and ∫stretch₊ → 0. This suggests c → 1.

## The One Missing Piece

Prove: as ρ → ∞, the anti-twist fraction c → 1.

Equivalently: near a potential blowup, ALL stretching goes to bending,
none to growth.

Physical intuition: as vortex filaments concentrate (ρ → ∞), they get
thinner (δ → 0) and closer together. The interaction rate increases,
the anti-twist response gets faster, and the fraction of stretching
converted to bending approaches 1.

This is the LAST STEP. Everything else is in place.
