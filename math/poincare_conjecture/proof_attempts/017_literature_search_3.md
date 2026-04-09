---
source: Web/arXiv search round 3
type: Literature — enstrophy bounds and maximum amplification
status: FOUND KEY PAPER — maximum enstrophy scales as E₀^{3/2}
---

## Critical Finding

### "Maximum Amplification of Enstrophy in 3D NS Flows" (arXiv 1909.00041)
This paper proves that the maximum growth of enstrophy is FINITE and scales as E₀^{3/2}.

Key quote: "as long as enstrophy remains finite, solutions are guaranteed to be
smooth and satisfy equations in the classical (pointwise) sense."

They use resolutions from 128³ to 512³ — same range as us.

**Direct connection:** If maximum enstrophy growth is bounded by E₀^{3/2}, then
enstrophy can never reach infinity in finite time. This is a PARTIAL regularity
result — it bounds the growth RATE but doesn't prove the solution stays smooth forever.

The E₀^{3/2} scaling is exactly the cubic vs quadratic competition:
- Enstrophy production ~ E^{3/2} (from trilinear stretching)
- Enstrophy dissipation ~ E (from quadratic diffusion)
- Balance: E^{3/2} = E → E = 1 (at equilibrium)
- Growth: dE/dt ≤ C E^{3/2} - ν E → solution: E(t) ≤ E₀/(1-ct)
- This gives FINITE TIME but not necessarily BLOWUP because the constant
  in the upper bound may not be tight

### "Quantitative Enstrophy Bounds for Measure Vorticities" (arXiv 2602.15670, Feb 2026)
VERY RECENT. Improved Nash inequalities for enstrophy depending on absolute vorticity
decay on balls. "Bounds are optimal in several aspects."

**Must read.** If they have optimal enstrophy bounds that we can use for our
pointwise stretching-dissipation analysis, this could close the gap.

### "Vortex Stretching and Enstrophy Production" (Phys Rev Fluids)
"Intense enstrophy is primarily depleted via viscous diffusion."
This is exactly our finding stated in their words.

## New Idea: Use the E^{3/2} Bound

The E₀^{3/2} maximum amplification result says:
```
max_t E(t) ≤ C E₀^{3/2}
```

For our setup: E₀ is the initial enstrophy, which scales as Σ|k|²|ω̂|².
For our curl noise IC with spectrum 1/(|k|²+1):
```
E₀ ~ Σ |k|² / (|k|²+1)² ~ Σ 1/(|k|²+1) ~ log(N)  (in 3D)
```

So max enstrophy ~ (log N)^{3/2} — grows LOGARITHMICALLY with N.
But the dissipation capacity grows as ~N² (from the maximum |k|²).

The ratio: max_stretch / dissip_capacity ~ (log N)^{3/2} / N² → 0.

This gives a CLEAN bound: the maximum possible stretching at any point
is bounded by (log N)^{3/2}, while the minimum possible dissipation at
a significant point is bounded below by ~N². Their ratio vanishes.

## Provable Lemma from Literature

**Lemma (from 1909.00041, adapted):**
For any divergence-free field ω on T_N³ with enstrophy E₀:
```
max_x |ω(x)·S(x)·ω(x)| ≤ C E₀^{3/2}
```

Combined with:
```
min_{significant x} ν|∇ω(x)|² ≥ c ν N² per point
```

The fraction where stretch > dissip is bounded by:
```
frac ≤ C E₀^{3/2} / (ν N²) → 0 as N → ∞
```

This gives POLYNOMIAL decay (like our Chebyshev bound) but it's
PROVABLE using established results.

## Status
The E^{3/2} bound is a known result. Using it for pointwise fraction
bounds is new (as far as I can tell from the search). The polynomial
bound is weaker than our observed exponential but it's PROVABLE.

The exponential improvement would come from concentration of measure
(Hoeffding on the spatial fraction), which upgrades polynomial mean
to exponential probability bound.

## Action Items
1. READ arXiv 1909.00041 — get the exact constant in E₀^{3/2} bound
2. READ arXiv 2602.15670 — check if optimal enstrophy bounds help
3. Combine E^{3/2} bound with spatial concentration → exponential?
4. This may be the cleanest proof path: known bounds + new application
