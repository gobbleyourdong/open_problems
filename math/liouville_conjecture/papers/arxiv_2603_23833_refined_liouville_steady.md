# arxiv 2603.23833 — Refined Liouville-Type Theorems for Stationary NS

> Authors: Cho-Yang (March 25, 2026)
> Status: STEADY solutions only. Does NOT apply to ancient (time-dependent).

## Main result
Liouville for 3D stationary NS under refined L^p growth assumptions.
If ||u||_{L^p(annuli)} grows no faster than ρ^{2/p-1/3} · g(ρ)^{3/p-1}
where g is any slowly-growing function with divergent integral, then u ≡ 0.

Allows growth up to iterated logarithms (log, log log, etc.) — hence "refined."
Works for 3/2 < p < 3 without separate ∇u ∈ L² assumption.

## Improvement over prior work
- Galdi: needed u ∈ L^{9/2} globally
- Seregin-Wang 2019: liminf of ||u||/ρ^γ → 0
- Tsai 2021: sharp exponent ρ^{2/p-1/3}
- Cho et al 2024: liminf < ∞
- THIS paper: extra slowly-growing g(ρ) factor allowed. Strictly weaker assumption.

## Why it doesn't help our campaign
- **STEADY only.** No time derivative. The techniques are elliptic (energy equalities).
- Our gap is ANCIENT solutions (time-dependent, defined on (-∞, 0]).
- Extending to parabolic case requires controlling space-time flux terms — qualitatively harder.
- The backward entry decomposition (our gap) is about temporal decay, not spatial growth rates.

## One potentially useful ingredient
Lemma 3: K_θ(ρ) = ρ⁻¹||u||³_{L³} controls both ∇u ∈ L² and u ∈ L⁶.
Could inform spatial profile estimates for rescaled ancient solutions at large |x|,
but only AFTER establishing any spatial decay — which is itself an open problem
(attempt_009/010 explored this and it was killed by numerics).

## Bottom line
Elegant steady-state sharpening. Orthogonal to our time-dependent ancient campaign.
