---
source: JB's insight — track coherent structures, not persistent tubes
type: NEW FRAMEWORK — finite-lifetime events consuming a bounded budget
status: Conceptually strong, needs rigorous definition of "coherent event"
date: 2026-03-26 cycle 30 (morning session)
---

## The Idea

Don't track tubes forever. Track them until they decohere (reconnect,
break up, spread out). Each coherent phase has a FINITE lifetime.
During that phase: the Lagrangian argument works. At decoherence:
ρ drops. Start fresh.

## The Framework

### Coherent vortex event: [t₁, t₂]
- Material region Ω(t) tracked by flow map
- |ω| ≥ ρ_max/2 inside Ω(t)
- ξ approximately constant (coherent direction)
- Ends when |∇ξ| spikes (reconnection/decoherence)

### During each event:
- det(∇Φ) = 1 → volume preserved
- Cauchy formula: ρ = σ₁|ω₀_event| where ω₀_event is the
  vorticity at the START of the event (not the global IC)
- The event consumes budget from Constantin:
  ΔC = ∫_{t₁}^{t₂} ∫_{Ω(t)} ρ|∇ξ|² dx dt

### At decoherence:
- ρ drops (concentration lost)
- The structure spreads, direction changes (|∇ξ| spikes)
- A new event may start from the new, LOWER base

### Total events bounded by budget:
Total ΔC = Σ ΔC_i ≤ C_total (Constantin)
Each event needs ΔC_i ≥ ΔC_min > 0 (minimum cost to sustain coherence)
Therefore: N_events ≤ C_total / ΔC_min

### Total stretching bounded:
∫α₊ dt = Σ (∫α₊ dt per event)
Each event: ∫α₊ ≤ A_max × τ_max (bounded peak × bounded duration)
Total: ≤ N_events × A_max × τ_max ≤ (C_total/ΔC_min) × A × τ

## Why ΔC_min > 0

Each coherent event must have |∇ξ| > 0 somewhere inside Ω(t)
(otherwise ξ is exactly constant → locally 2D → α=0 → no event).

The minimum cost: ΔC_min ~ ρ_event × |∇ξ|²_min × Vol_min × Δt_min.

For a genuine 3D stretching event: all these factors are > 0.
The incompressibility constraint forces |∇ξ| > 0 for genuine 3D flow
(from the codimension argument — fails only for 2D-type data,
which doesn't blow up anyway).

## Connection to Data

N=128 TG: 4 events, total ∫α₊ = 3.10
- Event 1: longest (dur=0.80), strongest
- Event 4: shortest, weakest
- Budget consumed: 3.10 out of C_total ~ E₀/ν

The events get weaker because:
1. Each consumes budget (finite C_total)
2. The remaining budget limits the next event's intensity
3. Eventually budget exhausted → no more events

## The Rigorous Gaps

1. Defining "coherent event" precisely (what threshold for |∇ξ|?)
2. Proving ΔC_min > 0 for genuine 3D events
3. Proving events don't OVERLAP (simultaneous events at different x)
4. Proving decoherence actually REDUCES ρ (not just changes topology)

## Why This Might Work

Unlike the Lagrangian tube argument (which failed because tubes
don't persist), this argument EMBRACES reconnection. The reconnection
is the MECHANISM: each reconnection consumes budget and resets ρ.
The finite budget prevents infinite repetition.

This is physically correct: turbulence IS a sequence of coherent
structure formations and destructions, consuming energy at each step.
The energy cascade is the budget being spent.

85 proof files. Fresh morning angle.
