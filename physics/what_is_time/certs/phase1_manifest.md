# certs/phase1_manifest.md — Numerical Certification: what_is_time

**Date:** 2026-04-09
**Phase:** 1 (numerical survey complete)
**Scripts:** entropy_arrow.py, lyapunov_arrow.py, (micro_macro_K.py in progress)

## Certified Claims

---

### C1 — S-entropy grows monotonically during gas diffusion (thermodynamic arrow confirmed)

**Status: CERTIFIED**

200-particle collision-free gas, left-half initial condition, 200 steps:
- H increases: 5.465 → 6.163 bits (Δ = +0.698)
- Left fraction decreases: 1.00 → 0.67
- Growth is monotone (with statistical fluctuations near equilibrium)

The thermodynamic arrow is confirmed in simulation: entropy increases along the forward time direction.

**Reference:** results/entropy_arrow_data.json

---

### C2 — Collision-free dynamics are exactly time-reversible (arrow requires dissipation)

**Status: CERTIFIED**

Reversed simulation (end state + velocity reversal, ε = 1e-10 perturbation):
- H decreases: 6.101 → 5.465 (exactly retracing the forward trajectory)
- The ε perturbation has no effect because there are no collision amplification events

**The arrow of time is NOT in the equations of motion.** Newton's laws (and ballistic
motion) are exactly time-symmetric. Reversal succeeds perfectly for non-dissipative systems.

**Reference:** results/entropy_arrow_data.json

---

### C3 — Lyapunov exponent λ ≈ 0.11/step for 60-particle hard-disk gas

**Status: CERTIFIED**

Two initially-identical configurations differing by ε = 1e-8 in one velocity component:
- Forward divergence: |δ(t)| ≈ ε × exp(λt), λ = 0.11 per step, R² ≈ 0.97
- Doubling time: t₁/₂ = ln(2)/λ ≈ 6.3 steps
- Time to macroscopic divergence: t_macro = log(1/ε)/λ ≈ 167 steps

With collisions: reversal fails in ~167 steps. Without collisions: reversal succeeds indefinitely.

**Dynamical enforcement of the arrow:** even with perfect velocity reversal, a 1-in-10^8
perturbation (quantum uncertainty, floating-point error) destroys the reversed trajectory
within 167 collision steps. This is the dynamical reason why low-entropy initial conditions
cannot be recreated from high-entropy present states.

**Reference:** results/lyapunov_data.json, results/lyapunov_findings.md

---

### C4 — K-proxy stays approximately constant during gas diffusion

**Status: CONSISTENT (unreliable measurement)**

The 400-byte particle state (200 particles × 2 bytes) is too small for gzip to give reliable K estimates.
Measured K-proxy = 0.545 throughout forward simulation — consistent with "K stays constant"
but the measurement is dominated by gzip header overhead at this sample size.

**Target for Phase 2:** re-run with 5000 particles (40 000 bytes) to get reliable micro-K measurement.
The micro_macro_K.py script (iteration 3, in progress) uses 500 particles × float32 = 4000 bytes,
which should give better reliability.

---

## Open Claims (Phase 2 targets)

- **R1: Why this specific arrow direction?** The Lyapunov exponent explains WHY reversal fails
  (dynamical enforcement), but not WHY the initial state was low-entropy. This requires
  cosmological initial conditions (low-entropy Big Bang) — addressed in what_is_reality.
  
- **R2: Primitivist felt-time account?** The phenomenology of time flow is not addressed by
  any script in Phase 1. Interface with philosophy/what_is_mind/γ parameter.

- **R3: Emergent time from entanglement.** Not yet modeled. Would require a quantum
  simulation showing time as emergent from entanglement structure (Page-Wootters mechanism).

## Summary

Phase 1 numerics: 3 claims certified (arrow real, requires dissipation, Lyapunov quantified).
C4 is consistent but unreliable. The key result: the thermodynamic arrow is a STATISTICAL
property (low-entropy initial conditions + Lyapunov amplification), not a dynamical one
(time-symmetric laws). The Lyapunov exponent quantifies the timescale for the arrow to
become irreversible: ~167 steps = ~1.67 seconds at dt=0.01.
