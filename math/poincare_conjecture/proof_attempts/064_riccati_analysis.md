---
source: Analytical derivation of event duration from strain ODE
type: PROOF ATTEMPT — Riccati equation for α at x*
status: τ ~ 1/ρ from theory (data shows steeper, β ≈ 1-3)
date: 2026-03-26 cycle 10
---

## The Strain ODE at x* During a Stretching Event

At the vorticity max, above the pressure crossover ρ_c:

```
dα/dt = -α² - Kρ²    (K ≈ 1/6 from isotropic pressure dominance)
```

This is a Riccati equation with solution:

```
α(t) = c × tan(arctan(α₀/c) - c(t-t₀))    where c = √K × ρ
```

## Event Duration

Time for α to go from α₀ > 0 to 0:

- If α₀ << cρ: τ = α₀/(Kρ²) ~ α₀/ρ²
- If α₀ >> cρ: τ = π/(2√K × ρ) ~ 1/ρ
- If α₀ ~ cρ: τ ~ 1/ρ

**Prediction: τ ~ 1/ρ (linear decay with ρ)**

## Per-Event Stretching Budget

∫α dt over one event ≈ α₀ × τ / 2 (triangle approximation):

- If α₀ ~ Cρ (CZ bound): ∫α ~ Cρ × 1/ρ = C (bounded per event)
- If α₀ ~ C (bounded): ∫α ~ C/ρ² (decreasing per event)

**Result: per-event stretching is O(1) or O(1/ρ²)**

## Comparison with Data

Data (N=128 TG): τ ~ ρ^{-3.04}, which is STEEPER than the theory's ρ^{-1}.

Possible explanations:
1. The restoring force is stronger than Kρ² (e.g., grows as ρ⁴)
2. The -α² term provides additional damping beyond the Riccati model
3. The ρ^{-3} fit may be over multiple events with varying ρ

From single-point analysis (t=4.50, ρ=19): τ ~ 0.09, giving β ≈ 0.8.
The ρ^{-3} fit is across the full time series, mixing different ρ regimes.

## What This Proves (Partial)

Even with the conservative τ ~ 1/ρ:

```
∫α per event ~ α₀/ρ ~ C    (bounded by CZ × 1/ρ = constant)
```

The total ∫α₊ dt = Σ (per-event contributions) ~ Σ C.

Convergence requires: either finite events or decreasing contributions.

From energy dissipation: each event dissipates ΔE > 0.
Total events ≤ E₀/ΔE_min. So ∫α₊ ≤ (E₀/ΔE_min) × C.

**If ΔE_min > 0: total stretching is bounded. QED.**

## The Remaining Gap

Proving ΔE_min > 0 (each stretching event at x* dissipates a
minimum amount of energy). This connects to:

1. The viscous dissipation ν∫|∇ω|² dx during the event
2. The enstrophy production ∫ρα dt during the event (bounded above by C)
3. The energy cascade to small scales (irreversible)

This is essentially the energy dissipation rate problem —
a well-studied quantity in turbulence theory.

## Status

The Riccati analysis gives:
- τ ~ 1/ρ (event duration)
- ∫α per event ~ O(1) (bounded)
- Total ∫α₊ bounded IF events are finite (energy argument)

This is ALMOST a proof. The gap: ΔE_min > 0 per event.
Viscosity ensures ΔE > 0 for ν > 0. For Euler (ν=0):
the dealiasing (spectral truncation) acts as implicit dissipation,
but this is a numerical artifact, not physics.

For NS (ν > 0): the proof may actually close through this route.
