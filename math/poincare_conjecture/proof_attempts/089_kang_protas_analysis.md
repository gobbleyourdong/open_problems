---
source: Careful analysis of Kang-Protas implications
type: ANALYSIS — what α=1.49 actually means for regularity
status: The result is about OPTIMAL GROWTH, need to interpret correctly
date: 2026-03-26 cycle 31
---

## What Kang-Protas ACTUALLY Found

max_{T>0, ||ω₀||₂²=E₀} E(T)/E₀ ~ C × E₀^{β-1}  with β = 1.49

This means: starting from enstrophy E₀, the MAXIMUM achievable
enstrophy at ANY later time T (optimized over BOTH T and initial
condition shape) is at most C × E₀^{1.49}.

The amplification ratio: E(T)/E₀ ~ E₀^{0.49}

## What This Means for Blowup

For blowup: need E(t) → ∞ in finite time.

Starting from E₀: after one optimal event:
  E₁ ≤ C E₀^{1.49}

After two optimal events:
  E₂ ≤ C (C E₀^{1.49})^{1.49} = C^{1+1.49} × E₀^{1.49²}

After n events:
  E_n ≤ C^{(1.49^n-1)/0.49} × E₀^{1.49^n}

Since 1.49 > 1: 1.49^n → ∞. So E_n → ∞ as n → ∞.

**THE KANG-PROTAS RESULT DOES NOT RULE OUT BLOWUP BY ITERATION.**

The amplification exponent β = 1.49 > 1 means each event AMPLIFIES
the enstrophy. Iterating gives unbounded growth (1.49^n → ∞).

For β ≤ 1: each event would NOT amplify → enstrophy stays bounded.
But β = 1.49 > 1: amplification occurs.

## Why I Was Confused

I initially thought the critical threshold was β < 3/2 for the
amplification ratio. But β is the GROWTH POWER, not the ODE exponent.

The ODE exponent α from dE/dt ≤ C E^α:
- Classical (CZ): α = 3 (from ||S||₃ ≤ C||ω||₃ and interpolation)
- Lu-Doering: instantaneous max dE/dt ~ E³ (α = 3)
- For α > 2: ∫E dt converges near blowup → no contradiction with energy
- For α ≤ 2: ∫E dt diverges → contradicts energy bound → regularity

The Kang-Protas amplification β = 1.49 is about the TOTAL growth
over an optimal time window, NOT the instantaneous rate.

## The Correct Interpretation

The Kang-Protas result constrains the VARIATIONAL problem:
  max_{u₀, T} E(T)/E₀ subject to ||ω₀||₂² = E₀

Result: max ~ E₀^{0.49} (growth is sublinear beyond power 1).

For blowup via the enstrophy ODE:
  dE/dt ≤ C E^α with α = 3 (Lu-Doering, sharp instantaneously)

But the TIME-AVERAGED growth rate is much lower:
  E(T_opt)/E₀ ~ E₀^{0.49} over T_opt ~ E₀^{-0.47}
  Average rate: (E₀^{1.49} - E₀) / E₀^{-0.47} ~ E₀^{1.96}
  Compare with E^3 instantaneous: E₀^{1.96} << E₀^3 for large E₀

The instantaneous rate is α=3 but the TIME-AVERAGED rate is ~E₀^{1.96}.
The energy constraint acts through the TIME INTEGRAL, not instantaneously.

## Does β = 1.49 Prove Regularity?

**NOT DIRECTLY.** β > 1 allows iteration to infinity.

**BUT:** the energy constraint limits the NUMBER of iterations.
Each optimal event costs energy ΔK ~ ν × E₀^{β} × T_opt ~ ν E₀^{β-γ}.
With β-γ = 1.02: the cost EXCEEDS E₀ (linearly) for large E₀.

The energy budget is K₀ ~ E₀/λ₁. Events continue while K available.
After n events: remaining K ≈ K₀ - n × ν E_n^{1.02}.

Since E_n grows as E₀^{1.49^n}: the cost grows SUPEREXPONENTIALLY.
The budget K₀ is exhausted after O(log log(K₀/(νE₀))) events.
E at exhaustion: E₀^{1.49^{O(log log)}} — a finite but ENORMOUS number.

This IS bounded (finite, not ∞). So blowup doesn't occur.
But the bound is an iterated exponential tower — practically useless.

## The Real Value of Kang-Protas

The result shows that the WORST-CASE NS dynamics:
1. Amplifies enstrophy by E₀^{0.49} per event (sublinear)
2. Takes time E₀^{-0.47} per event (shrinking window)
3. The amplification exponent β < 2γ + 1 (their data: 1.49 < 1.94)

If β < 2γ + 1: the iterated growth is DOUBLY EXPONENTIAL at worst.
If β ≤ 1: the growth is bounded by E₀ (no iteration).
The gap: β = 1.49, need β ≤ 1.

## Connection to Our Strain Self-Depletion

Our Lean lemma: α² ≤ ê·S²·ê at x*. This reduces the effective
stretching below CZ. If this reduction propagates to the GLOBAL
enstrophy production, it should reduce β below the CZ prediction.

The CZ prediction for β: from dE/dt ≤ C E³ and T ~ E^{-0.47}:
β_CZ ~ 3 - 0.47 = 2.53. But actual β = 1.49 << 2.53.

The strain self-depletion is ALREADY CAPTURED in the Kang-Protas
computation (they solve the actual NS equations). The β = 1.49
INCLUDES all depletion effects.

To improve β: need a depletion mechanism NOT captured by NS.
But NS IS the full equation — there's nothing to add.

## Conclusion

Kang-Protas β = 1.49 is the ACTUAL worst-case growth for NS.
It's better than CZ (β ~ 2.53) but worse than β ≤ 1 (regularity).
The iterated tower gives a FINITE but astronomical bound.
Practically: regularity holds. Rigorously: the bound is too weak.

89 proof files. The Kang-Protas exponent narrows the gap but
doesn't close it through simple iteration. Need a deeper argument.
