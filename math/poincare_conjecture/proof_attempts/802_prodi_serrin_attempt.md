---
source: PRODI-SERRIN ATTEMPT — concentration + Biot-Savart at non-obvious exponents
type: PARTIAL PROGRESS — the idea works IF concentration estimates hold
file: 802
date: 2026-04-01
instance: MATHEMATICIAN
---

## THE IDEA

Prodi-Serrin: u ∈ L^p_t L^q_x with 2/p + 3/q ≤ 1 → regularity.

Type I gives ||ω||∞ ~ 1/(T*-t). On T³: ||u||_{L^q} ~ ||ω||∞ for all q.
So ||u||_{L^q} ~ 1/(T*-t) → ∫||u||^p ~ ∫1/(T*-t)^p = ∞ for p ≥ 2.
Dead end with L^∞ bounds.

BUT: near blowup, the vorticity concentrates spatially. The L^r norms
for r < ∞ grow SLOWER than ||ω||∞ because the blowup region shrinks.

If ||ω||_{L^r} ~ (T*-t)^{-1+2/r} (from CKN-type concentration):
  For r=3: ||ω||_{L³} ~ (T*-t)^{-1/3}. Much slower than (T*-t)^{-1}.
  ||u||_{L^∞} ~ ||ω||_{L³}^{...}... the Biot-Savart mapping.

## THE TABLE

| r | q=3r/(3-r) | ||ω||_r exponent | p_max | p_PS | Works? |
|---|-----------|-----------------|-------|------|--------|
| 2 | 6 | 0 (bounded) | ∞ | 4 | YES |
| 5/2 | 15 | -1/5 | 5 | 5/2 | YES |
| 3 | ∞ | -1/3 | 3 | 2 | YES |
| 4 | ∞ | -1/2 | 2 | 2 | BOUNDARY |

For r ≤ 3: the Prodi-Serrin criterion IS satisfied IF the CKN
concentration estimate ||ω||_{L^r} ~ (T*-t)^{-1+2/r} holds.

## THE GAP

The CKN concentration estimate ||ω||_{L^r} ~ (T*-t)^{-1+2/r}
is NOT proven for Type I blowup. CKN partial regularity gives
dimension bounds on the singular set, not L^r norm bounds.

For the L^r norm: need to show that the blowup region has
measure ~ (T*-t)^2 (parabolic scaling). This is consistent with
Type I but not proven.

What IS known: for Type I blowup, the rescaled solution at the
blowup point converges to an ancient solution (Koch-Nadirashvili-
Seregin-Sverak). The Liouville conjecture says this ancient solution
is trivial → no blowup. But that's equivalent to Type I exclusion.

## STATUS

The Prodi-Serrin approach WOULD work if we could prove
||ω||_{L^r} = o(||ω||∞) for any r < ∞ near a Type I blowup.
This is a concentration/profile decomposition problem.
Not proven, but not obviously impossible.

## 802. PS approach: works IF ||ω||_{L^r} grows slower than ||ω||∞.
## The r=3 case would give regularity via PS(2,∞).
## The gap: proving the concentration estimate rigorously.
