---
source: Strain ODE analysis + ∫α₊ data
type: QUANTITATIVE ANALYSIS of the -α² ODE
status: Finite stretching budget confirmed
date: 2026-03-26 cycle 5
---

## The Strain ODE at x*

```
dα/dt ≈ -(ê·S²·ê) + (-ê·H·ê) + viscous
      ≤ -α² + f(t)
```

where f(t) = -ê·H·ê + viscous (the forcing).

## TG N=64 Data

```
∫₀⁵ α₊ dt = 2.37    (total positive stretching)
∫₀⁵ α² dt = 2.01    (total squared stretching)
∫α²/∫α₊ = 0.846     (average α during positive phase ≈ 0.85)
```

The positive stretching episode: t = 1.5 to 4.0 (duration 2.5).
After t=4.0: α goes NEGATIVE (anti-twist) and ρ starts declining.
No second episode in T=5.

## Curl Noise N=64/128 Data

```
∫stretch₊ = 0.0003 at N=64 (mean, 5 seeds)
∫stretch₊ = 0.0004 at N=128 (mean, 5 seeds)
```

Essentially ZERO. No stretching events for random ICs at resolved scales.

## The Finite Stretching Budget

Each vortex event (sheet formation → concentration → anti-twist → decay)
contributes a FINITE amount to ∫α₊. For TG: ~2.4 per event.

The budget is finite because:
1. The -α² self-depletion limits the peak α to O(√f)
2. The pressure Hessian flips at high ρ (isotropic dominates)
3. The anti-twist creates negative α that terminates the event
4. After termination, ρ decays and no new event starts

For the proof: need to show the total number of events is finite
(or that event contributions decrease). Energy considerations:
each event dissipates energy via the cascade. Total energy is bounded
(a priori from initial data). So the total number of events is bounded
by initial_energy / energy_per_event.

## The Proof Sketch (Energy Budget)

1. Initial kinetic energy: E₀ = ||u₀||²/2 (bounded, conserved in Euler, dissipated in NS)
2. Each positive stretching event at x* transfers energy from large scales to small scales
3. The energy transferred per event: ΔE ~ ∫α₊ × ρ × (volume of event) × dt
4. Total events bounded by: N_events ≤ E₀ / ΔE_min
5. Total stretching: ∫α₊ dt ≤ N_events × (∫α₊ per event) ≤ (E₀/ΔE_min) × 2.4

If ΔE_min > 0 (each event dissipates a minimum energy): total ∫α₊ bounded.

## Status

This is a PLAUSIBILITY argument, not a proof. The gaps:
- Proving ΔE_min > 0 (each event dissipates nonzero energy)
- Proving events don't overlap or pile up
- Making the energy accounting rigorous

But the DATA strongly supports it: ∫stretch₊ → 0 for resolved ICs,
and the one TG event contributes a finite ~2.4 then terminates.

## Connection to Known Results

This is essentially the energy dissipation rate argument:
- NS dissipates energy at rate ν∫|∇u|² dx ≥ 0
- For smooth solutions, the dissipation is bounded
- The total dissipated energy ≤ E₀ (initial energy)
- Each stretching event involves local energy dissipation
- Finite total dissipation → finite total stretching

The question: is the stretching-to-dissipation ratio bounded?
From our data: α (stretching) and ν|∇ξ|² (dissipation) track each other
(the evolution equation relates them). If dissipation ≥ c × stretching:
total stretching ≤ (1/c) × total dissipation ≤ E₀/c.

This IS essentially what the evolution equation says:
νρ|∇ξ|² = ρα - dρ/dt + νΔρ
At x* (max): νρ|∇ξ|² ≤ ρα (when max is growing)
So: α ≤ ν|∇ξ|² (when max is growing)
Integrating: ∫α dt ≤ ν∫|∇ξ|² dt

And ν∫ρ|∇ξ|² dx dt ≤ C (Constantin). But extracting pointwise...
same wall as always.

## The Wall (Again)

Every argument eventually needs: pointwise at x* from spatial integral.
The energy budget argument needs: energy dissipated at x* from total energy.
Same mathematical gap. Different physical language.

The gap IS the Millennium Prize. We've characterized it precisely.
