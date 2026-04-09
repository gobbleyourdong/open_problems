---
source: Attempt to prove isotropization analytically
type: PARTIAL — physical argument clear, rigorous proof not achieved
status: The wall persists — pointwise from integral
date: 2026-03-26 cycle 19
---

## Why |ω|² Peak is Sharper Than |S|² at x*

### |ω|² at x*:
- Maximum point: |ω(x*+r)|² = ρ² - r·Hess·r + O(|r|³)
- QUADRATIC decay from peak
- Width: δ_ω ~ ρ/√λ (Hessian eigenvalue)
- ∇|ω|² = 0 at x* (maximum condition)

### |S|² at x*:
- NOT a maximum (S depends on global ω via Biot-Savart)
- ∇|S|² ≠ 0 in general (LINEAR variation near x*)
- Width of variation: determined by Biot-Savart kernel, NOT by ω peak
- Smoother than |ω|² because convolution smooths

### The consequence:
f = |ω|²/2 - |S|² has a quadratic peak at x* (from |ω|²)
modified by a linear slope (from |S|²). As ρ grows, the
quadratic peak dominates → f becomes more isotropic.

## Why It Can't Be Proved (The Same Wall)

Proving |S|² varies linearly at x* requires bounding ∇(|S|²),
which involves second derivatives of the Biot-Savart integral.
This is a CZ-type estimate → pointwise bounds require knowing
the global distribution → same wall as before.

The statement "|S| is smoother than |ω|" is physically obvious
(convolution smooths) but analytically requires the same
pointwise-from-integral upgrade that blocks all other approaches.

## The Conjecture (Computationally Verified)

**Conjecture:** At the maximum point x* of |ω|, the pressure
source f = |ω|²/2 - |S|² has anisotropy that DECREASES with ρ:

```
anisotropy(f, x*) ~ C/ρ^β    for some β > 0
```

Computationally verified for TG at N=64:
- Peak anisotropy 1.49 at ρ=6.9
- Drops to 0.67 at ρ=12.9

This would imply |H^D| = o(ρ²) → pressure crossover → regularity.
