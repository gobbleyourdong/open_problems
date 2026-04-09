---
source: T³ ENERGY-ENSTROPHY BALANCE — does Type I violate the energy budget?
type: ATTEMPT + ANALYSIS — promising but fails at critical exponents
file: 803
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE IDEA

On T³ with ν > 0, energy decays: 2ν ∫₀^{T*} ||ω||²_{L²} dt ≤ ||u₀||²_{L²}.
Type I blowup concentrates vorticity. Does the concentration violate the budget?

## THE CHAIN

1. Energy inequality: 2ν ∫₀^{T*} Ω(t) dt ≤ ||u₀||²  (Ω = ||ω||²_{L²})
   This requires Ω = o((T*-t)^{-1}).

2. Type I: ||ω||∞ ≤ C₀/(T*-t).

3. Enstrophy equation: dΩ/dt = 2∫ω·Sω - 2ν||∇ω||²

4. Stretching bound (CZ on T³): ∫ω·Sω ≤ C||ω||³_{L³}
   By interpolation on T³: ||ω||₃ ≤ ||ω||²^{2/3} ||ω||∞^{1/3}
   So: ||ω||³_{L³} ≤ ||ω||²_{L²} · ||ω||∞ = Ω · ||ω||∞

5. Enstrophy ODE: dΩ/dt ≤ 2CΩ||ω||∞ - 2νΩ (Poincaré: ||∇ω||² ≥ Ω)
   = Ω(2CC₀/(T*-t) - 2ν)

6. Near T*: 2CC₀/(T*-t) ≫ 2ν, so:
   dΩ/dt ≤ 2CC₀Ω/(T*-t)
   → Ω(t) ≤ Ω(t₁) ((T*-t₁)/(T*-t))^{2CC₀}

7. Energy budget requires 2CC₀ < 1, i.e., C₀ < 1/(2C).

## WHY IT FAILS

For Type I blowup with parabolic concentration:
- Vorticity concentrates in volume V ~ (T*-t)^{3/2}
- ||ω||∞ ~ (T*-t)^{-1}, |ω| ~ (T*-t)^{-1} in V, small outside
- Ω ~ (T*-t)^{-2} · (T*-t)^{3/2} = (T*-t)^{-1/2}
- ∫(T*-t)^{-1/2} dt CONVERGES near T*
- Energy budget IS satisfied. No contradiction.

The enstrophy blows up like (T*-t)^{-1/2}, exponent 1/2 < 1. The energy
integral converges. Type I with parabolic concentration is CONSISTENT with
the energy inequality on T³.

## WHAT THE KEY LEMMA ADDS

The generic bound ∫ω·Sω ≤ CΩ||ω||∞ uses CZ on L³.
The Key Lemma gives α < (√3/2)|ω| at vorticity maxima.

But the stretching INTEGRAL involves α at ALL points, not just the max.
The Key Lemma is pointwise-at-the-max, not global. It reduces the constant
from C to C·(√3/2) at the max, but the max contributes only a measure-zero
subset of the integral.

To use the Key Lemma globally: would need α < (√3/2)|ω| EVERYWHERE, not
just at the max. This would require proving the Key Lemma away from critical
points of |ω|², where ∇|ω|² ≠ 0.

## THE CONSTRAINT ON C₀

If the enstrophy ODE gives Ω ~ (T*-t)^{-2CC₀} and the energy budget
requires 2CC₀ < 1:
- Small C₀ (weak blowup): budget satisfied, argument fails
- Large C₀ (strong blowup): budget violated → contradiction → no blowup

So Type I blowup with LARGE C₀ is excluded by energy. But with small C₀,
the argument doesn't work. And the actual parabolic concentration gives
C₀ consistent with the budget.

## VERDICT

The energy-enstrophy approach constrains the Type I constant but doesn't
exclude Type I blowup on T³. The concentration of vorticity is precisely
tuned (parabolic scaling) to satisfy the energy budget while still allowing
pointwise blowup.

## 803. Energy-enstrophy on T³: constrains Type I constant, doesn't exclude it.
## Parabolic concentration (V ~ (T*-t)^{3/2}) makes Ω ~ (T*-t)^{-1/2},
## which is integrable. The energy budget is satisfied. No contradiction.
