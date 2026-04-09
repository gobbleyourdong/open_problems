---
source: Instance C — Shell enstrophy transfer is FORWARD (high shells gain)
type: NEGATIVE RESULT — inverse cascade route dead for localized ICs
file: 262
date: 2026-03-29
---

## Result

Trefoil: ALL shells k ≥ 5 have T(j) > 0 (gaining enstrophy).
Transfer rate T/E grows with k: from +2 at k=5 to +40 at k=15.
This is STRONG FORWARD CASCADE.

TG: Only k=2 has energy, it loses (T < 0). Trivial inverse cascade
because TG is single-scale.

## What this means

The approach "high shells self-deplete → ||ω||_{H^s} bounded" FAILS.
The trefoil's high-k modes gain enstrophy at 20-40× their content per
unit time. The forward cascade is vigorous.

## Why the palinstrophy still grows sub-cubically

The forward cascade feeds the high shells, but the RATE is controlled.
T(j)/E(j) ≈ const × k (grows linearly with k).
This means: dE_j/dt ≈ C × k × E_j.
Summing: dP/dt = Σ k² dE_j/dt ≈ C Σ k³ E_j.

If E_j ~ k^{-α} (power law spectrum): Σ k³ E_j ~ k_max^{4-α}.
For α > 4: the sum converges → dP/dt bounded.
For α < 4: the sum diverges → dP/dt grows with k_max.

Our data: E_j drops from 12666 (k=1) to 0.13 (k=15).
Fit: E_j ~ k^{-5.7}. α = 5.7 > 4 → the sum CONVERGES.

This means: despite forward cascade, the spectrum is steep enough
that the palinstrophy transfer rate is bounded.

## The proof route (revised)

Don't prove T(j) < 0 at high j (that's false).
Instead prove: the SPECTRUM E_j ~ k^{-α} with α > 4.
This gives dP/dt bounded → P bounded → regularity.

The spectrum exponent α > 4 is related to the SMOOTHNESS of the
vorticity field. For Euler: the spectrum should be at least as steep
as the initial condition's spectrum (by conservation properties?).

## 262. Forward cascade confirmed. New route: prove steep spectrum.
