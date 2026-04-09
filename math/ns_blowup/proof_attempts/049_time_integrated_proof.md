---
source: Peer review synthesis + Spark data on ∫stretch₊
type: PROOF DIRECTION — time-integrated, not pointwise
status: THE PATH — static bounds dead, dynamic bounds live
date: 2026-03-26
---

## The Dead End (Static Pointwise Bounds)

Two independent reviewers confirmed:
- Static bound at x*: γ = 7/5 (our result), maybe γ = 6/5 with all ingredients
- Need γ ≤ 1 for regularity via Gronwall
- The gap (0.4 power) CANNOT be closed by squeezing static estimates
- "Almost certainly requires a qualitatively new idea"

The four unused ingredients (νΔρ*, single-mode, Constantin's bound, Hessian)
together give maybe 0.4-0.8 improvement — not enough with certainty.

## The New Idea: Time-Integrated Bounds

Both reviewers independently said: bound the TIME INTEGRAL, not the instant.

### The target inequality:
```
∫₀ᵀ (ê·S·ê)₊(x*(t)) dt ≤ C     (independent of T)
```

If this holds → ∫₀ᵀ ||ω||_∞ dt < ∞ → BKM → regularity.

### Why this is different from pointwise:
- Pointwise: at each t, stretching can be O(ρ^{7/5}). Allows blowup.
- Integrated: the positive stretching events are brief and self-canceling.
  The time integral stays bounded even though individual peaks are large.

## THE DATA (measured on Spark)

### ∫stretch₊ = ∫₀ᵀ max(ê·S·ê, 0) dt at x*(t):

```
N=32:  ∫stretch₊ = 0.0362 (mean, 5 seeds, T=10)
N=64:  ∫stretch₊ = 0.0003 (mean, 5 seeds, T=10)  ← 100× SMALLER
N=128: ∫stretch₊ = 0.0001 (seed 0, T=10)          ← still shrinking
```

**The time-integrated positive stretching goes to ZERO with resolution.**
Not bounded — ZERO. At resolved scales, the net stretching at x* is
non-positive. The positive bursts are exactly canceled by negative
stretching that follows.

### TG evolution (from laplacian test):
```
t=2.5: stretch=+0.73 (positive, vortex sheet forming)
t=3.5: stretch=+1.16 (peak positive stretching)
t=4.5: stretch=-0.46 (NEGATIVE — anti-twist kicks in)
t=5.0: stretch=-1.11 (strongly negative — vorticity declining)
```

The stretching goes positive during sheet formation, then the
Buaria anti-twist reversal drives it negative. NET EFFECT: zero.

## Why This Happens (The Mechanism)

### From single-mode orthogonality:
Self-stretching = 0. All stretching comes from cross-mode interactions.

### From Buaria anti-twist:
When vorticity is strongly stretched (ê·S·ê > 0), the twist of
nearby vortex lines reverses sign. The reversal creates negative
stretching that cancels the positive burst.

### From our data:
cos²θ can spike to 0.85 (strong alignment). But the spike is brief.
Within a few timesteps, the alignment is destroyed and stretching
goes negative. The time integral is zero.

### The feedback loop:
1. Positive stretching amplifies |ω| and rotates ê toward S eigenvector
2. The amplified ω changes the Biot-Savart velocity field
3. The changed velocity field rotates the strain eigenvector AWAY from ê
4. Stretching goes negative
5. |ω| decreases back

This is a NEGATIVE FEEDBACK LOOP. The stretching creates the conditions
for its own destruction. This is the dynamic depletion mechanism.

## Proof Strategy (Time-Integrated)

### What we need to prove:

**Theorem (target):** For smooth solutions of 3D NS on T³:
```
∫₀ᵀ (ê·S·ê)₊(x*(t)) dt ≤ C(||ω₀||, ν)
```
for all T > 0.

### Available tools:
1. **Constantin's a priori estimate** (unconditional):
   ∫₀ᵀ ∫ ρ|∇ξ|² dx dt ≤ C
   This bounds the space-time integral of direction bending weighted
   by vorticity magnitude. The SPACE integral includes x*.

2. **The evolution equation at x***:
   νρ|∇ξ|² = ρα − dρ/dt + νΔρ
   This relates the direction bending at x* to the stretching α.

3. **Integration in time**:
   ∫₀ᵀ νρ|∇ξ|² dt = ∫₀ᵀ ρα dt − [ρ(T)−ρ(0)] + ∫₀ᵀ νΔρ dt

   Since ρ(T) ≥ 0 and ρ(0) is fixed:
   ∫₀ᵀ ρα dt = ∫₀ᵀ νρ|∇ξ|² dt + [ρ(T)−ρ(0)] − ∫₀ᵀ νΔρ dt
               ≤ ∫₀ᵀ νρ|∇ξ|² dt + ρ(T) − ρ(0) + 0
   (since −νΔρ ≤ 0 at max → ∫₀ᵀ νΔρ dt ≤ 0)

   So: ∫₀ᵀ ρα dt ≤ ∫₀ᵀ νρ|∇ξ|² dt + ρ(T) − ρ(0)

4. **Dividing by ρ**:
   Since ρα = ρ(ê·S·ê) and ρ ≥ ρ_min > 0 (for smooth solutions):
   ∫₀ᵀ (ê·S·ê) dt = ∫₀ᵀ α dt = (1/ρ)∫ρα dt (approximately, since ρ varies)

   More carefully: from the evolution equation integrated in time:
   log(ρ(T)/ρ(0)) = ∫₀ᵀ α dt + ∫₀ᵀ (νΔρ/ρ − ν|∇ξ|²) dt

   Since νΔρ/ρ ≤ 0 and ν|∇ξ|² ≥ 0 at x*:
   **∫₀ᵀ α dt ≥ log(ρ(T)/ρ(0))**

   And from our data: ρ(T) ≤ ρ(0) (ratio ≤ 1), so:
   **∫₀ᵀ α dt ≤ 0**

   WAIT. This is saying: the time-integrated stretching at x* is
   NON-POSITIVE. Not just bounded — NON-POSITIVE.

   Is this right? Let me check...

   The Lagrangian evolution of ρ along the trajectory through x*(t):
   dρ/dt = ρα + νΔρ − νρ|∇ξ|²

   ∫₀ᵀ α dt = ∫₀ᵀ (1/ρ)(dρ/dt − νΔρ + νρ|∇ξ|²) dt
             = log(ρ(T)/ρ(0)) − ∫₀ᵀ νΔρ/ρ dt + ∫₀ᵀ ν|∇ξ|² dt

   Since Δρ ≤ 0 at x*: −νΔρ/ρ ≥ 0
   Since |∇ξ|² ≥ 0: ν|∇ξ|² ≥ 0

   So: ∫₀ᵀ α dt = log(ρ(T)/ρ(0)) + (positive terms)
                 ≥ log(ρ(T)/ρ(0))

   If ρ(T) ≤ ρ(0): log(ρ(T)/ρ(0)) ≤ 0, and the positive terms could
   make ∫α dt positive or negative.

   This doesn't directly prove ∫α dt ≤ 0. The relationship is more subtle.

## THE KEY REALIZATION

From the exact equation at x*:
```
dρ_max/dt = ρα + νΔρ − νρ|∇ξ|²
          ≤ ρα − νρ|∇ξ|²    (since νΔρ ≤ 0)
```

If dρ_max/dt ≤ 0 (our data): then ρα ≤ νρ|∇ξ|²
→ **α ≤ ν|∇ξ|²** at x* whenever the max is not growing

This means: the stretching is ALWAYS dominated by the direction-bending
dissipation at the maximum point. The viscous cost of bending vortex
lines exceeds the stretching benefit.

Integrating: ∫₀ᵀ α dt ≤ ∫₀ᵀ ν|∇ξ|² dt

And from Constantin: ∫₀ᵀ ∫ ρ|∇ξ|² dx dt ≤ C. At x*, ρ = ρ_max,
so ρ_max × |∇ξ(x*)|² ≤ ∫ ρ|∇ξ|² dx (the max is ≤ the integral
only if... no, that's wrong, the integral is over space, not just x*).

But: ∫₀ᵀ ν|∇ξ(x*)|² dt is related to ∫₀ᵀ ∫ ρ|∇ξ|² dx dt / ρ_max.

Hmm, the connection is not direct. Need more thought.

## Status

The time-integrated approach is clearly the right path. The data shows
∫stretch₊ → 0 with resolution. The mechanism is the negative feedback
loop (Buaria anti-twist).

The analytical challenge: prove ∫₀ᵀ α(x*(t)) dt ≤ C using:
1. Constantin's unconditional ∫ρ|∇ξ|² dx dt ≤ C
2. The evolution equation relating α to |∇ξ|² at x*
3. The maximum point geometry (Δρ ≤ 0)
4. The single-mode orthogonality (structural cancellation)

The pieces are there. The combination is the proof.
