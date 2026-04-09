---
source: Instance C — Palinstrophy growth rate measurement
type: OBSERVATION — dP/P grows linearly in t, suggesting Gaussian P(t)
date: 2026-03-29
file: 260
---

## Measurement

Palinstrophy P = ∫|∇ω|² dx, measured at N=32 Euler for TG/KP/trefoil.

### Key finding: dP/P ∝ t (linear growth of the normalized rate)

Trefoil: dP/P goes from 0.034 (t=0.002) to 0.895 (t=0.028).
Growth rate: dP/P ≈ 34t.

If dP/dt = C·t·P: then P(t) = P₀ exp(Ct²/2) — GAUSSIAN growth.

Gaussian growth is:
- Faster than exponential (exp(t²) vs exp(t))
- But ALWAYS FINITE for finite t
- Never blows up in finite time

### Comparison to standard bound

Standard: dP/dt ≤ C·P³/ν (cubic in P → possible blowup)
Measured: dP/dt ≈ C·t·P (linear in P, linear in t → no blowup)

The standard bound overestimates by ~10¹⁴ at the measured timescale.

### Caveat

This is measured over t=0 to 0.03 only. The growth pattern could change.
Need longer evolution to confirm dP/P ∝ t persists.

If dP/P transitions to ∝ P (or ∝ P²): then dP/dt ∝ P² (or P³) and
blowup is possible. The question is the ASYMPTOTIC growth law.

## What this means for the proof

If dP/dt ≤ C·(t+1)·P can be PROVEN (linear in t and P):
→ P(t) ≤ P₀ exp(C(t²/2 + t)) → bounded for finite t
→ ||ω||_{H¹} bounded → progress toward ||ω||∞ bounded

The proof needs: bound the stretching integral ∫∇ω:∇(S·ω)dx
by C·t·P instead of C·P³/ν.

The factor t (instead of P²/ν) comes from the DEVELOPMENT of the strain
field over time. At t=0, S=0 (for TG) or small. S grows linearly at first.
The stretching involves S, so dP/dt ∝ S ∝ t at early times.

At LATE times: S saturates (from the |ω|²/|S|² = 4 attractor).
Then dP/dt ∝ S·P ∝ (||ω||/2)·P.
If ||ω|| ∝ P^{1/2} (from Sobolev): dP/dt ∝ P^{3/2} → sub-cubic!

P^{3/2} growth: dP/dt = C·P^{3/2} → P = P₀/(1-C√P₀ t/2)² → blowup at T* = 2/(C√P₀).

Hmm, P^{3/2} still gives finite-time blowup. Need β < 1 for bounded P.

## 260. Instance C first measurement.
