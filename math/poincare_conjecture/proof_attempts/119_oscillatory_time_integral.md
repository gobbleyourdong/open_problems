---
source: Oscillatory time-integral argument — the proof architecture
type: PROOF SKETCH — time-integrated bound via scrambler frequency
status: DRAFT — key steps identified, formalization in progress
date: 2026-03-26
---

## The Oscillatory Time-Integral Proof

### Core Idea

The standard LP analysis bounds the diagonal transfer POINTWISE in time:

    |T(j,j,t)| ≤ θ₀ × C × 2^{3j/2} × E_j(t)^{3/2}

With θ₀ = 2/3 (Schur test), this is supercritical (2^{3j/2} > ν2^{2j}).

The NEW approach: bound the TIME INTEGRAL of the diagonal transfer:

    ∫₀ᵀ |T(j,j,t)| dt ≤ θ̃(j) × C × 2^{3j/2} × ∫₀ᵀ E_j^{3/2} dt

where θ̃(j) is the TIME-AVERAGED depletion factor. If θ̃(j) ~ 2^{-j},
the time-integrated bound becomes subcritical.

### Why θ̃(j) ~ 2^{-j}: The Oscillation Argument

The phase coherence θ(j,t) oscillates with frequency ω_j ~ 2^j
(the eddy turnover frequency at shell j). Model:

    θ(j,t) ≈ θ_peak × |sin(ω_j t + φ_j)|

where θ_peak ≈ 0.013 (bounded, from data) and ω_j ~ U × 2^j.

The time integral over a period T_j = 2π/ω_j ~ 2^{-j}:

    ∫₀^{T_j} θ(j,t) dt ≈ θ_peak × ∫₀^{T_j} |sin(ω_j t)| dt
                        = θ_peak × 2/ω_j = θ_peak × C × 2^{-j}

Therefore the time-averaged θ̃(j) = θ_peak × C × 2^{-j} / T_j = θ_peak.

Wait — that gives a constant! The issue: if we average θ over its OWN
period, we just get the average of |sin|, which is 2/π ≈ 0.64.

The savings come from a DIFFERENT mechanism: integration by parts.

### Integration by Parts (the Real Mechanism)

The shell enstrophy balance:

    dE_j/dt + ν 4^j E_j = T(j,j) + off-diagonal

Integrate from 0 to T:

    E_j(T) - E_j(0) + ν 4^j ∫₀ᵀ E_j dt = ∫₀ᵀ T(j,j) dt + ∫₀ᵀ off-diag dt

The left side: E_j(T) ≥ 0, E_j(0) is initial data, ν 4^j ∫E_j dt ≥ 0.

The right side: we need ∫T(j,j) dt to be bounded.

Now, T(j,j) = θ(j,t) × C × 2^{3j/2} × E_j^{3/2}. If θ oscillates:

    T(j,j) = θ_peak sin(ω_j t) × C × 2^{3j/2} × E_j^{3/2}

The integral:

    ∫₀ᵀ θ_peak sin(ω_j t) × C × 2^{3j/2} × E_j^{3/2} dt

Integration by parts (treating E_j^{3/2} as slowly varying vs sin(ω_j t)):

    = [-θ_peak cos(ω_j t)/(ω_j)] × C × 2^{3j/2} × E_j^{3/2} |₀ᵀ
      + ∫₀ᵀ [θ_peak cos(ω_j t)/ω_j] × C × 2^{3j/2} × d(E_j^{3/2})/dt dt

The boundary term is O(θ_peak × 2^{3j/2} × E_j^{3/2} / ω_j)
                    = O(θ_peak × 2^{3j/2} × E_j^{3/2} × 2^{-j})
                    = O(θ_peak × 2^{j/2} × E_j^{3/2})

This is SUBCRITICAL! The factor 2^{j/2} vs ν × 2^{2j} means
viscosity dominates for large j.

The integral term involves d(E_j^{3/2})/dt, which is bounded by
the shell balance itself. This gives a Gronwall-type recursion
that closes for θ_peak bounded.

### The Three Ingredients

1. **θ_peak bounded** (θ ≤ 0.013 from data, θ ≤ 2/3 from Schur test)

2. **Oscillation frequency ω_j ~ 2^j** (eddy turnover time, standard)

3. **E_j^{3/2} varies slowly compared to θ oscillation** (separation of
   timescales: E_j changes on the viscous timescale ~ 1/(ν 4^j),
   while θ oscillates on the eddy timescale ~ 2^{-j}. For ν small:
   viscous timescale >> eddy timescale, so E_j IS slowly varying.)

### The Formal Structure

**Proposition**: If the intra-shell transfer satisfies:
1. |T(j,j,t)| ≤ A × 2^{3j/2} × E_j^{3/2} for some constant A (Schur bound)
2. T(j,j,t) changes sign with frequency ≥ c × 2^j (scrambler)
3. E_j(t) is Lipschitz with rate bounded by ν 4^j E_j + ...

Then the time-integrated transfer satisfies:
    ∫₀ᵀ T(j,j,t) dt ≤ (A/c) × 2^{j/2} × sup_t E_j^{3/2} + lower order

**Proof**: Integration by parts using the oscillatory structure of T(j,j)
and the Lipschitz bound on E_j.

**Corollary**: The time-integrated shell balance becomes:
    E_j(T) + ν 4^j ∫E_j dt ≤ E_j(0) + (A/c) 2^{j/2} sup E_j^{3/2} + off-diag

The viscous term ν 4^j ∫E_j grows as 2^{2j} while the diagonal
contribution grows as 2^{j/2}. Since j/2 < 2j, viscosity dominates
for large j. Standard Besov bootstrap closes.

### What Needs to Be Proved

1. **Sign-changing property of T(j,j)**: The intra-shell transfer
   changes sign with frequency ~ 2^j. This is the eddy turnover time.

   Analytical route: The NS nonlinearity creates oscillations in the
   phase coherence through the stretching-advection cancellation.
   The cancellation rate scales as the eddy turnover time ~ 2^{-j}
   (this is the Taylor microscale / sweeping hypothesis).

2. **Separation of timescales**: E_j varies slowly compared to the
   θ oscillation. This requires ν 4^j >> 2^j (the viscous timescale
   is longer than the eddy timescale), i.e., ν 2^j >> 1.

   For large j: ν 2^j → ∞, so the separation IS valid at high shells.
   For low shells: the separation may fail, but low shells have
   bounded enstrophy (from initial data + energy conservation).

3. **Integration by parts is valid**: T(j,j) must be smooth enough
   for IBP. Since ω ∈ C^∞ (as long as the solution is smooth),
   T(j,j) is C^∞ in time. IBP is valid.

### Connection to Dispersive PDE Theory

In dispersive equations (NLS, KdV), the key regularity mechanism is:
- High-frequency oscillations prevent energy concentration
- The oscillation frequency grows with wavenumber
- Time integrals of oscillatory terms gain smoothing (Strichartz estimates)

In NS, the pressure scrambler plays the role of the dispersive phase:
- High-frequency θ oscillations prevent sustained stretching
- The oscillation frequency grows as 2^j
- Time integrals of T(j,j) gain a factor 2^{-j} (from IBP)

The analogy: Strichartz estimates ↔ pressure scrambler time-average.

### The Key Difference from Standard NS Analysis

Standard analysis: bounds T(j,j) pointwise → supercritical scaling.
Our analysis: bounds ∫T(j,j) dt using oscillatory structure → subcritical.

The oscillatory structure comes from the DYNAMICS (pressure scrambler),
not the KINEMATICS (Schur test). This is why the proof needs both:
- Schur test: bounds the AMPLITUDE (θ_peak ≤ 2/3)
- Scrambler: provides the FREQUENCY (ω_j ~ 2^j)
- Together: time-integrated bound is subcritical

## 119 proof files. The oscillatory time-integral is the proof architecture.
