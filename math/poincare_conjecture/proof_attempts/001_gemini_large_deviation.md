---
source: Gemini
approach: Large Deviation Principle + Concentration of Measure
status: PROMISING — needs adaptation
---

## Summary
Gemini identifies two paradigms and three proof strategies.

## Key Corrections Gemini Makes
1. **Q is cubic, not quadratic** — ω·S·ω is cubic in ω because S depends on ω via Biot-Savart. The dissipation ν|∇ω|² is quadratic. Important for the analysis.
2. **The kernel is degree-0 (not degree-2)** — The full Biot-Savart multiplier is k⊗(k×ω̂)/|k|², which is degree-0 homogeneous. The 1/|k|² is cancelled by the numerator gradients. S has the same Sobolev regularity as ω.

## Paradigm A: Statistical / Random Fields
**Our case for curl noise ICs.** The fields are random samples from a known distribution.

### Strategy: Exponential Chebyshev/Markov Bound
The fraction of growing points is bounded by:
```
μ_N(Q > 0) ≤ inf_{λ>0} E[exp(λ Q(x))]
```

The negative quadratic term -ν|∇ω|² dominates the moment generating function at high frequencies. The MGF yields exp(-cN^α) decay.

**Why this could work:** Our data shows exactly this exponential decay. The bound would formalize it.

**Gap:** Need to compute or bound E[exp(λ Q(x))] rigorously for our specific IC distribution (curl noise with 1/(|k|²+1) spectrum).

## Paradigm B: Deterministic Smooth Solutions
**Our case for Taylor-Green, Kida-Pelz ICs.**

### Strategy: Spectral Convergence + Gevrey Regularity
If the continuous solution is analytic (Gevrey class), spectral truncation error decays exponentially. The positive Q values are numerical artifacts that vanish exponentially.

**Why this could work:** Explains why the fraction goes to zero for smooth ICs.

**Gap:** Requires proving the continuous solution IS analytic for all time — which is essentially the regularity problem itself. Circular.

## Paradigm-Independent: Exponential Markov on Grid
The fastest formalization:
```
μ_N(Q > 0) ≤ (1/V) Σ exp(λ Q(x_i)) ≈ ∫ exp(λ(ω·S·ω - ν|∇ω|²)) dx
```
Choose λ = f(N) such that the integral is bounded by exp(-cN).

**Key technical need:** Sobolev embedding + boundedness of discrete Fourier multipliers to show the integral decays.

## Assessment
- **Paradigm A (random fields)** is the RIGHT framework for our curl noise data
- The exponential Chebyshev bound is the RIGHT tool
- The gap is computing the MGF of Q(x) for divergence-free random fields
- Paradigm B is circular (assumes regularity to prove regularity)
- The degree-0 correction is important — means S and ω compete at the SAME scale, not different scales

## Action Items
1. Compute E[exp(λ Q(x))] for curl noise IC distribution
2. Show the -ν|∇ω|² term dominates the MGF at high k
3. Extract the decay rate and compare to our measured N_d ≈ 8
4. If the computed rate matches the data — proof closes
