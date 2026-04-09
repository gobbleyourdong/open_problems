---
source: SDP RELAXATION FAILS — reduces to triangle inequality
type: DEAD END — the relaxation loses the Biot-Savart coupling
file: 428
date: 2026-03-30
---

## THE ATTEMPT

Formulate max S²ê/|ω|² as an SDP over the mode parameters.

## WHY IT FAILS

The SDP relaxation decouples each mode's amplitude and direction:
max |Σw_k|² subject to |w_k| ≤ r_k, w_k ⊥ v̂_k.

This is solved by the TRIANGLE INEQUALITY:
max |Σw_k| = Σr_k × max(ê direction) = Σ r_k √(1-(ê·v̂_k)²).

The SDP gives (N-1)/4 × |ω|² — the SAME bound as file 363.
For N ≥ 5: this exceeds 3/4. FAILS.

## THE ROOT CAUSE

The Biot-Savart structure couples each mode's amplitude r_k to its
direction d̂_k through a SINGLE angle θ_k (the polarization).

The SDP relaxation treats r_k and d̂_k as INDEPENDENT — losing the
coupling. The anti-correlation (high r_k ↔ diverse d̂_k) is invisible
to the relaxation.

No standard convex relaxation captures this coupling because the
constraint surface is a CURVED MANIFOLD (product of circles S¹×...×S¹).

## WHAT WOULD WORK

A relaxation that PRESERVES the θ_k coupling:
- Moment/SOS relaxation of degree ≥ 4 (captures the sin/cos coupling)
- Interval arithmetic over the θ_k parameter space (brute force)
- A NON-CONVEX bound that exploits the manifold curvature

## 428. SDP = triangle inequality. Doesn't capture Biot-Savart coupling.
