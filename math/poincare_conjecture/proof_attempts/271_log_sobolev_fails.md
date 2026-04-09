---
source: Log Sobolev approach fails — Q/P grows exponentially
type: NEGATIVE — the spectral ratio isn't bounded
file: 271
date: 2026-03-29
---

## Q/P (super-palinstrophy / palinstrophy) grows as exp(3.72t)

ln(Q/P) ~ 3.72t (R² = 0.998). Exponential growth.

This means the vorticity spectrum is FLATTENING over time:
higher wavenumbers gain relative to lower ones (forward cascade).

## Log Sobolev doesn't close

||ω||∞ ≤ C√P √(log(Q/P)) = C√P √(3.72t).
dP/dt ≤ C||ω||∞ P ≤ C²P^{3/2} √(3.72t).

Integration: P blows up at T* = (3/(C√P₀))^{2/3}. FINITE TIME.

The √t correction from the log Sobolev is not enough to
make the P^{3/2} growth sub-critical.

## What would work

Need: dP/dt ≤ CP^β with β < 1 for P bounded, or β = 1 for
P exponential (regularity). The actual β from the data is ~1.5
(half-power, from P^{3/2}√t). This is ABOVE 1 → possible blowup of P.

But ||ω||∞ doesn't blow up (Hou-Li positive). The discrepancy:
P can blow up while ||ω||∞ stays bounded — the H^1 norm diverges
but the L^∞ norm doesn't. This is consistent with the solution
developing small-scale structure (high wavenumbers) without
concentrating into a point singularity.

For NS with ν > 0: the viscous term -2νQ in dP/dt provides
dissipation that can tame the P blowup. If ν > 0: P stays bounded.

## For Euler (ν=0): the log Sobolev approach FAILS.
## For NS (ν > 0): viscosity saves it.
## The proof route via palinstrophy only works for NS, not Euler.

## 271. Log Sobolev killed. Q/P grows exponentially.
