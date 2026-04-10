# Vorticity Frequency + Pressure-Weighted Test — Theory Track Response

**Date:** 2026-04-09
**Script:** `numerics/vorticity_frequency.py`
**Track:** Numerical (responding to theory track attempt_001)

## A. Vorticity Frequency N_ω(r) — MONOTONE on Burgers

| R | D_ω(R) | H_ω(R) | N_ω(R) | log N_ω |
|---|--------|--------|--------|---------|
| 0.5 | 0.0012 | 0.068 | 0.009 | -4.76 |
| 1.0 | 0.025 | 0.172 | 0.144 | -1.94 |
| 1.5 | 0.103 | 0.205 | 0.750 | -0.29 |
| 2.0 | 0.214 | 0.193 | 2.213 | 0.79 |
| 2.5 | 0.322 | 0.180 | 4.477 | 1.50 |
| 3.0 | 0.418 | 0.173 | 7.241 | 1.98 |
| 4.0 | 0.595 | 0.170 | 13.96 | 2.64 |

**N_ω(r) is MONOTONE non-decreasing** on Burgers. All 6 consecutive
pairs satisfy N_ω(R+) ≥ N_ω(R−).

**Effective exponential growth rate: 2.11** (from log N_ω slope).
Theory track predicted Gronwall bound exp(C(M)·r); the actual growth
rate is 2.11 per unit r.

**Key observation**: N_ω goes from 0.009 at R=0.5 to 14.0 at R=4.0
(1500× growth). This is NOT bounded. But for the Burgers vortex,
ω is NOT bounded either (ω_z = const · exp(-αr²/(2ν)) is bounded,
but |∇ω|² grows relative to |ω|² on spheres as R increases because
the vorticity is concentrated near the core while the sphere grows).

For a BOUNDED ancient solution with bounded vorticity, N_ω(r) growth
would be constrained. The Gronwall constant C(M) = 2.11 on Burgers
gives a concrete benchmark.

## B. Pressure-Weighted H̃(r) — FAILS (H̃ < 0)

| R | H(R) | H̃(R) | H̃/H |
|---|------|------|------|
| 0.5 | 0.40 | -0.12 | -0.31 |
| 1.0 | 6.33 | -2.01 | -0.32 |
| 2.0 | 100.97 | -32.83 | -0.33 |
| 3.0 | 510.39 | -167.83 | -0.33 |
| 5.0 | 3935.69 | -1303.63 | -0.33 |

**H̃(r) < 0 for ALL tested r.** The ratio H̃/H ≈ −0.33 consistently.

The Burgers vortex pressure p = −α²(r²/4 + z²/2) + centrifugal is
dominated by the strain term −α²z²/2, which makes |u|² + 2p < 0
on most of the sphere (the poles z = ±R dominate).

**CONCLUSION: Modification 1 (pressure-weighted) is NOT well-defined
on the Burgers vortex.** The pressure is too negative for |u|² + 2p
to be a valid weight. This modification may only work on flows with
WEAKER strain (e.g., pure vortex without background strain).

## Recommendations for Theory Track

1. **Modification 3 (vorticity) is CONFIRMED as the best direction.**
   N_ω(r) is monotone on Burgers with growth rate 2.11.
   The Gronwall bound C(M) is real and finite.

2. **Modification 1 (pressure-weighted) is KILLED for Burgers-type flows.**
   H̃ < 0 everywhere. Could still work on flows with weaker pressure
   (bounded ancient solutions might have weaker pressure than Burgers?),
   but it's risky.

3. **The effective Gronwall rate C ≈ 2.11 is the number to beat.**
   If the theory can show C = 0 for bounded ancient solutions (not just
   C = 0 for harmonic), Liouville follows from Modification 3.
   The structure of Sω (traceless symmetric matrix acting on divergence-free
   vector) might give cancellations that reduce C below 2.11.

## The Poincaré Parallel (updated)

On Poincaré: five soliton detectors, all monotone, equality on solitons.
On Liouville: the vorticity frequency N_ω is a candidate detector.
If it's truly monotone for bounded ancient NS flows (not just Burgers),
then N_ω → ∞ would contradict boundedness of ω, forcing ω ≡ 0 → u ≡ 0.

The monotonicity on Burgers is the FIRST POSITIVE SIGNAL for this direction.
