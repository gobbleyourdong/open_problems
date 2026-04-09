---
source: Global ρα integral bound from L¹ vorticity + Constantin
type: UNCONDITIONAL GLOBAL BOUND — ∫∫ρα dx dt ≤ C
status: PROVED (from known estimates, unconditional)
date: 2026-03-26 cycle 18
---

## THEOREM (Unconditional)

For any Leray solution of 3D NS on T³:

```
∫₀ᵀ ∫_{T³} |ω(x,t)| × (ξ·S·ξ)(x,t) dx dt ≤ C(ω₀, ν)
```

where C depends only on initial data and viscosity, NOT on T.

## Proof

### Step 1: Evolution of ||ω||_1

From the vorticity equation, dotting with ξ = ω/|ω|:

```
d/dt ||ω||_1 = ∫ρα dx - ν∫ρ|∇ξ|² dx
```

(transport term vanishes by div u = 0 on T³; viscous term splits via
ξ·Δω = Δ|ω| - |ω||∇ξ|², with ∫Δ|ω| dx = 0 by periodicity.)

### Step 2: Integrate in time

```
||ω(T)||_1 - ||ω(0)||_1 + ν∫₀ᵀ∫ρ|∇ξ|² dx dt = ∫₀ᵀ∫ρα dx dt
```

### Step 3: Constantin's bound

```
ν∫₀ᵀ∫ρ|∇ξ|² dx dt ≤ C₀ = (1/2ν)||u₀||_2²
```

(Unconditional, holds for all Leray solutions.)

### Step 4: L¹ vorticity bound

```
||ω(T)||_1 ≤ ||ω(0)||_1 + (C/ν)E₀
```

where E₀ = ||u₀||_2²/2 is initial energy. This follows from:
- ||ω(t)||_1 ≤ ||ω(0)||_1 + C∫₀ᵗ ||ω||_2² ds
- ν∫₀ᵗ ||ω||_2² ds ≤ E₀ (energy dissipation)
- So ||ω(t)||_1 ≤ ||ω(0)||_1 + CE₀/ν

### Step 5: Combine

```
∫₀ᵀ∫ρα dx dt = ||ω(T)||_1 - ||ω(0)||_1 + ν∫₀ᵀ∫ρ|∇ξ|² dx dt
              ≤ CE₀/ν + C₀
              = CE₀/ν + (1/2ν)E₀
              = C'E₀/ν
```

**QED.** The bound is C'E₀/ν, independent of T. □

## What This Gives

The SPACE-TIME integral of ρα is bounded. This means:
- Stretching cannot accumulate over all space and all time
- The total "stretching budget" is finite: C'E₀/ν

## What This Does NOT Give

This does NOT bound ∫₀ᵀ ρ(x*(t)) α(x*(t)) dt — the POINTWISE integral at x*.
The global integral ∫∫ρα dx dt includes all points, not just x*.
The stretching could concentrate at x* while the global integral stays bounded.

## BUT: Concentration Implies Regularity

If ∫ρα dx dt ≤ C (bounded), and the stretching concentrates at x*:

∫₀ᵀ ρ*α* × Vol(stretching region) dt ≤ C

If Vol → 0 as ρ* → ∞ (Grujić: Vol ~ ρ*^{-3/2}):

∫₀ᵀ ρ*α* × ρ*^{-3/2} dt ≤ C
∫₀ᵀ ρ*^{-1/2} × α* dt ≤ C

If α* ~ Cρ* (CZ): ∫₀ᵀ ρ*^{1/2} dt ≤ C

For blowup (ρ* ~ (T*-t)^{-p}): ∫(T*-t)^{-p/2} dt diverges when p > 2.

From the best static bound γ = 7/5: ρ* ~ (T*-t)^{-5/2}, so p/2 = 5/4 > 1.
The integral ∫ρ*^{1/2} dt diverges. CONTRADICTION with the bound ≤ C!

Wait — let me check this more carefully.

If ρ* ~ (T*-t)^{-5/2} (from γ=7/5 static bound):
∫₀^{T*} ρ*^{1/2} dt ~ ∫(T*-t)^{-5/4} dt → DIVERGES.

But the bound says ∫ρ*^{1/2} α* Vol dt ≤ C with Vol ~ ρ*^{-3/2}:
∫ρ*^{1/2} × Cρ* × ρ*^{-3/2} dt = C∫1 dt = CT* (just T*, not divergent!)

Hmm, with the volume factor the integral is just CT*, which is finite.
The contradiction doesn't arise. The volume shrinkage exactly compensates.

## Status

The global ∫∫ρα bound is PROVED and UNCONDITIONAL. But extracting
pointwise information from it hits the same concentration issue.
The volume factor from Grujić (ρ^{-3/2}) exactly balances the growth,
preventing a contradiction.

This is a NEW unconditional result but doesn't close the regularity gap.
Filed for the paper as a structural result.
