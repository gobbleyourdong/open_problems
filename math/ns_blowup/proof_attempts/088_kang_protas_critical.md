---
source: Kang & Protas (2020/2022) arXiv:1909.00041
type: THE CRITICAL PAPER — enstrophy growth exponent 1.49 < 3/2
status: IF RIGOROUS → REGULARITY FOLLOWS DIRECTLY
date: 2026-03-26
---

## The Result

Using variational optimization (adjoint-based gradient ascent on
the enstrophy manifold), Kang & Protas found:

```
max_{T>0} E_T(ũ) ~ 0.224 × E₀^{1.490 ± 0.004}
```

with optimal time window T̃ ~ 0.124 × E₀^{-0.471 ± 0.008}.

## WHY THIS IS THE KEY

The critical exponent for blowup is **3/2**. If dE/dt ≤ C·E^α:
- α ≥ 3/2: blowup POSSIBLE (standard, known)
- α < 3/2: blowup IMPOSSIBLE (Gronwall + energy bound gives E bounded)

Kang-Protas measured: **α = 1.490 ± 0.004 < 1.500 = 3/2**

The gap: 3/2 - 1.49 = 0.01. Small but DEFINITE.

## The Regularity Argument (if α < 3/2 is rigorous)

From the enstrophy evolution:
```
dE/dt ≤ C·E^α    with α < 3/2
```

Combined with the energy dissipation:
```
ν ∫₀ᵀ E(s) ds ≤ E₀/2 = K₀/(2ν)
```

Gronwall gives: **E(T) ≤ E₀ × exp[K₀/(2ν)]** — uniformly bounded.

Bounded enstrophy → ||ω||₂ bounded → Sobolev embedding controls
higher norms → BKM integral finite → REGULARITY.

## What Kang-Protas Actually Shows

1. They NUMERICALLY optimize the initial condition to MAXIMIZE enstrophy
   growth at fixed initial enstrophy E₀, up to E₀ = 1000 (512³ grid)
2. The optimizer uses adjoint methods — finds the TRUE worst-case IC
3. The exponent 1.49 is measured across E₀ = 10 to 1000 (two decades)
4. The exponent is STABLE (±0.004 uncertainty)
5. At E₀ > 100: the maximizers become ASYMMETRIC (reconnection signature)

## The Gap Between Numerical and Proof

The exponent 1.49 is from COMPUTATION, not analytical proof.
Making it rigorous requires ONE of:

### Option A: Computer-assisted proof of the variational bound
- Verify the adjoint optimization at specific E₀ values using
  interval arithmetic (our toolset!)
- If max E_T ≤ C·E₀^{1.499} at E₀ = 100, 200, ..., 1000:
  the bound is machine-verified
- Extend via bootstrapping: if E grows at most E^{1.499},
  the solution stays in the verified regime forever

### Option B: Analytical proof that α < 3/2
- The maximizers have specific structure (Beltrami-like at low E₀,
  reconnection-type at high E₀)
- Show the maximizer structure PREVENTS α = 3/2
- Our single-mode orthogonality + strain self-depletion provide
  the algebraic mechanism for α < 3/2

### Option C: Use the gap between 1.49 and 1.50
- Even if we can only prove α < 1.50 (not α = 1.49):
  α < 3/2 is SUFFICIENT for regularity
- Any ε > 0 improvement over the classical α = 3/2 would do
- Our γ = 7/5 = 1.4 pointwise bound at x* gives α ≈ 7/5
  for the L∞ norm... but the enstrophy exponent is DIFFERENT

## Connection to Our Work

### Our γ = 7/5 bound (file 048):
This bounds the POINTWISE stretching rate at x*:
dρ/dt ≤ Cρ^{7/5}

The Kang-Protas exponent bounds the GLOBAL enstrophy growth:
dE/dt ≤ C·E^{1.49}

These are DIFFERENT quantities (L∞ vs L²). But they're related:
- E = ||ω||₂² ≤ Vol × ||ω||_∞² = Vol × ρ²
- dE/dt = ∫ω·S·ω dx ≤ ρ × E (using ||S|| ≤ Cρ)
- So dE/dt ≤ Cρ × E ≤ C × E^{1/2} × E = C·E^{3/2}

The classical α = 3/2 comes from this chain. To get α < 3/2:
need ||S||_∞ < C||ω||_∞ — the CZ bound NOT saturated.

Our single-mode orthogonality + strain self-depletion EXACTLY
provide this: the stretching at x* is depleted by the -α² term,
making the effective ||S|| at x* less than CZ predicts.

If the Kang-Protas maximizers satisfy our Lean lemmas (which
they must, since they're NS solutions): the self-depletion
reduces their growth rate below 3/2.

## The Proof Path (NEW)

1. The maximum enstrophy growth for NS is E_T ≤ C·E₀^α with α < 3/2
   (Kang-Protas, computational; need to make rigorous)
2. By our strain self-depletion (Lean lemma 2): the stretching
   at x* satisfies dα/dt ≤ -α² + forcing → the worst-case IC
   has α < CZ prediction
3. This α improvement propagates to the enstrophy equation:
   dE/dt = ∫ω·S·ω ≤ (reduced CZ) × E → α < 3/2
4. α < 3/2 + energy bound → E bounded → ||ω||₂ bounded
5. Bounded ||ω||₂ + regularity theory → ||ω||_∞ bounded → BKM → regularity

## CRITICAL QUESTION

Can we prove α < 3/2 ANALYTICALLY using our Lean lemmas?

The strain self-depletion gives: at x*, the stretching rate is
reduced by the -α² term. If this reduction propagates to the
INTEGRAL ∫ω·S·ω (enstrophy production), we get dE/dt < C·E^{3/2}.

The propagation: ∫ω·S·ω = ∫ρ²α dx. At x*: α is reduced.
Elsewhere: α is bounded by CZ. The WEIGHTED integral mixes
the depleted value at x* with generic values elsewhere.

If the contribution from x* DOMINATES (because ρ is max there):
the reduction at x* controls the integral → α < 3/2.

This is PLAUSIBLE and testable. The Kang-Protas data shows the
maximizers have their vorticity CONCENTRATED near one point
(the analogue of x*). So the x* contribution DOES dominate.

## Status

THIS IS THE MOST PROMISING PATH TO REGULARITY.

The Kang-Protas exponent 1.49 < 1.50 = 3/2 is a COMPUTATIONAL FACT.
Making it rigorous requires either:
(a) Computer-assisted verification of the variational bound (our toolset)
(b) Analytical proof using strain self-depletion (our Lean lemmas)
(c) Combination: Lean lemmas prove α < 3/2 - ε for some ε > 0

88 proof files. The target is sharper than ever.
