# Attempt 031 — The Wall: Precise Analysis

**Date**: 2026-04-07
**Phase**: 4 (Gap Identification)
**Instance**: Odd

## What theory track Found (attempt_032)

THE WALL: "The lattice vortex free energy F_v(β) > 0 for all β > 0, but
no known method propagates F_v > 0 from strong coupling to weak coupling."

The block ratio Z_block^{per}(g) / Z_block^{anti}(g) is NOT automatically ≥ 1
for all boundary conditions g.

## My Initial Claim (wrong)

I claimed spectral positivity gives Z_block^{per}(g) ≥ Z_block^{anti}(g)
for all g. This is WRONG. Here's why:

Spectral positivity gives: Cov(Tr(U_P), Tr(U_Q)) ≥ 0. This means
plaquettes are positively correlated. But the comparison Z_per ≥ Z_anti
is not a correlation statement — it's a comparison of TWO DIFFERENT MEASURES.

Z_per - Z_anti = ∫ [e^{S_per} - e^{S_anti}] ∏ dU

where S_per - S_anti = 2Σ_{j half} d_j c_j Σ_{P∈Σ} χ_j(U_P).

The integrand can be positive or negative (characters are not sign-definite).
The claim Z_per ≥ Z_anti says the INTEGRAL is ≥ 0, which doesn't follow
from pointwise bounds.

## What DOES Follow from Spectral Positivity

On any finite lattice with periodic BC, the spectral representation gives:

Z_per / Z_anti = exp(F_v)

where F_v = Σ_{n≥1} ??? — NOT directly from spectral decomposition.

Actually, the ratio Z_per/Z_anti is related to the EXPECTATION of the
center twist operator:

Z_anti = ∫ exp(-β S_W) · ∏_{ℓ crossing Σ} (-1) ∏ dU
       = ⟨∏_{ℓ crossing Σ} (-1)⟩_Z · Z_per

Wait, that's for a gauge transformation twist. Let me be precise.

For SU(2): the center twist multiplies each link crossing Σ by -I.
In the action: this changes Tr(U_P) → Tr(-U_P) = -Tr(U_P) for
plaquettes with an odd number of links on Σ.

So Z_anti = ∫ exp(β Σ_{P∉Σ} (1/2)Tr(U_P) - β Σ_{P∈Σ} (1/2)Tr(U_P)) ∏ dU

Z_per - Z_anti = ∫ exp(-β S_bulk) [exp(β Σ_{P∈Σ}(1/2)Tr) - exp(-β Σ_{P∈Σ}(1/2)Tr)] ∏ dU

= ∫ exp(-β S_bulk) · 2sinh(β Σ_{P∈Σ} (1/2)Tr(U_P)) ∏ dU

NOW: sinh(x) has the sign of x. So the integrand is positive when
Σ_{P∈Σ} (1/2)Tr(U_P) > 0 and negative when < 0.

**The sign of the integral depends on whether the AVERAGE of Tr(U_P)
over Σ-plaquettes is positive or negative under the bulk measure.**

At STRONG coupling: the bulk measure is nearly Haar (uniform), so
⟨Tr(U_P)⟩ ≈ 0. The sinh argument is O(1) and its expectation is...
dominated by the fluctuations. Not obvious.

At WEAK coupling: ⟨Tr(U_P)⟩ ≈ 2 (plaquettes nearly identity). The
sinh argument is ≈ β · Area(Σ) > 0, so the integral is positive. ✓

## Wait — Actually This IS Obvious

The function sinh(x) is convex for x > 0 and odd.

By Jensen's inequality: ⟨sinh(X)⟩ ≥ sinh(⟨X⟩) if sinh is convex
in the range of X.

⟨X⟩ = β Σ_{P∈Σ} ⟨(1/2)Tr(U_P)⟩_bulk

where the expectation is over the BULK measure (exp(-βS_bulk) on non-Σ links
+ Haar measure on Σ links). 

Under Haar measure: ⟨(1/2)Tr(U_P)⟩ = 0 (average trace = 0 for SU(2)).
Wait, that's only if the link variables are independent. In the presence
of the bulk, the links are correlated and ⟨(1/2)Tr(U_P)⟩ > 0 for β > 0.

Hmm, this is getting circular. The average plaquette is > 0 for β > 0
(this is the physical statement that the gauge field is ordered). But
proving ⟨(1/2)Tr(U_P)⟩ > 0 under the measure where Σ-plaquettes enter
with a sinh requires understanding the measure itself.

## The Honest Assessment

I cannot prove Z_per ≥ Z_anti using only spectral positivity or Jensen.
The wall is real. The theory track is right.

The specific obstruction: the sinh representation
  Z_per - Z_anti = ∫ exp(-βS_bulk) · 2sinh(β Σ_{P∈Σ}(1/2)Tr) ∏ dU
has a sign-indefinite integrand. Proving the integral is positive requires
controlling the distribution of Σ_{P∈Σ} Tr(U_P) under the bulk measure.

This is a LARGE DEVIATION question: what's the probability that a
macroscopic average (over L² plaquettes) is negative?

For L large: by the CLT, Σ Tr(U_P) / L² → ⟨Tr(U_P)⟩ > 0 with
probability 1. The negative fluctuation probability is
exp(-c L²) (large deviation). So the positive contribution to the
integral dominates by an exponential margin.

**But making this rigorous requires the large deviation bound, which
itself requires control of the lattice gauge theory's concentration
properties.** And those concentration properties are what we're trying
to prove in the first place (the mass gap gives exponential concentration).

## THE WALL (reconfirmed from the odd side)

The wall is a **bootstrap problem**: proving F_v > 0 requires concentration
of the plaquette sum, which requires a mass gap, which is what F_v > 0
is supposed to prove.

This circular structure IS the Ito-Seiler obstruction.

## What Survives

| Result | Status | Depends on wall? |
|--------|--------|-----------------|
| S_anti > 0 (attempt_013) | PROVEN | No |
| G(P,Q) ≥ 0 (spectral, attempt_022) | PROVEN | No |
| F_v > 0 on finite lattice (attempt_027) | MC evidence | No (finite lattice) |
| F_v > 0 at strong coupling | PROVEN (OS78) | No |
| F_v > 0 at step n₀ | PROVEN (cluster exp) | No |
| F_v > 0 at step 0 (= Tomboulis 5.15) | **NOT PROVEN** | **YES — THE WALL** |
| Confinement for all β | **NOT PROVEN** | **YES** |
| Mass gap | **NOT PROVEN** | **YES** |

## 031. The wall is real. Z_per ≥ Z_anti at all β is a bootstrap problem:
## proving it requires concentration, which requires the mass gap.
## This is the EXACT same circularity Ito-Seiler identified in 2007.
## The systematic approach has mapped the wall precisely in 32 even + 15 odd attempts.
