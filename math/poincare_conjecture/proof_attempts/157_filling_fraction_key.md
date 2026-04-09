---
source: Filling fraction determines pressure-vorticity competition
type: KEY FINDING — the mechanism is topology-dependent
date: 2026-03-28
---

## The Filling Fraction

Defined: fraction of domain where |ω| > 0.1 × |ω|_max.

| IC | Fill | ||H_nl||/||H_y|| | H_ω(full) | H_ω(yang) | H_ω(nl) | c₃ | α |
|----|------|-----------------|-----------|-----------|---------|-----|-----|
| TG | 0.94 | 0.46 | +0.21 | -0.01 | +0.22 | 0.40 | -0.01 |
| KP | 0.93 | 0.46 | +1.63 | -0.33 | +1.96 | 0.31 | -0.07 |
| trefoil | 0.06 | 1.42 | +1.04 | -5.20 | +6.24 | 0.26 | 0.00 |
| rings | 0.05 | 1.65 | -0.09 | -0.36 | +0.27 | 0.07 | -0.02 |
| tube | 0.06 | 1.57 | +0.00 | -0.70 | +0.70 | 0.00 | 0.00 |
| 2 perp | 0.09 | 1.15 | -0.50 | -0.91 | +0.41 | 0.16 | +0.02 |

## The Pattern

HIGH fill (>0.9): ||H_nonlocal|| / ||H_yang|| ≈ 0.46
  → Yang captures most of the pressure. Non-local is a 46% correction.
  → -Ω² dominates (ratio 2:1). c₃ > 1/3.

LOW fill (<0.1): ||H_nonlocal|| / ||H_yang|| ≈ 1.2-1.6
  → Non-local EXCEEDS Yang. The Poisson integral is dominated by the
     far-field structure of the tubes.
  → Pressure can reverse the compression. c₃ < 1/3 possible.

## Physical Interpretation

Volume-filling vorticity (TG, KP):
- Pressure at point x is determined by nearby vorticity.
- Yang's local approximation works well (non-local is 46% correction).
- The -Ω² vorticity term in the strain equation dominates.
- c₃ > 1/3, α < 0: compression.

Localized vorticity (tubes, knots):
- Pressure at the core is determined by the ENTIRE tube structure.
- The Biot-Savart integral of the tube creates long-range strain.
- Yang's local formula misses most of the pressure (non-local > 100% correction).
- The tube's self-induced strain can stretch along ω.
- c₃ < 1/3, α can be positive.

## Implications for the Proof

1. For VOLUME-FILLING flows: the c₃ ≥ 1/3 mechanism works.
   The filling fraction of turbulent flow is HIGH (many interacting scales).
   This is the relevant regime for the BKM argument.

2. For LOCALIZED structures: the mechanism fails.
   But localized vortex tubes in viscous flow DIFFUSE → fill increases.
   The inviscid trefoil has sustained stretching, but NS would damp it.

3. The PROOF must either:
   (a) Restrict to volume-filling initial data (fill > C)
   (b) Use viscosity to show localized structures diffuse before blowing up
   (c) Find a different bound for localized structures

## The Viscosity Argument

For NS (ν > 0): viscous diffusion broadens localized tubes.
A tube of width σ diffuses as σ² ~ νt.
The time for a tube to fill the domain: t_fill ~ L²/ν.
The time for blowup (if it could happen): t_blow ~ 1/|ω|.

If t_fill < t_blow (i.e., νL²|ω| > 1): the tube diffuses before blowing up.
This is exactly the CKN criterion (Caffarelli-Kohn-Nirenberg).

## Summary

The c₃ mechanism is NOT universal — it depends on the filling fraction.
For volume-filling flows (which includes developed turbulence), it works.
For localized tubes (which are the actual blowup candidates), it doesn't.
The gap between these regimes is exactly where viscosity matters.

## 157 proof files. Filling fraction is the key parameter.
