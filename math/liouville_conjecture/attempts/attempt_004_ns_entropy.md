# attempt_004 — The NS Entropy (Perelman W-Analog)

**Date:** 2026-04-10
**Track:** Theory (Even)
**Mountain:** All (this is the synthesis attempt)
**Status:** In progress. Fisher information killed by numerics (stretching has wrong sign). This is the last surviving functional candidate.

## What the numerics killed

From the SCRATCHPAD (numerics → theory, Apr 10 00:15):
- **Fisher information:** dF/dt|_stretching = α · F > 0. Wrong sign. Stretching INCREASES Fisher info. Dead for strain-dominated flows.
- **N_ω growth rates:** Beltrami gives N_ω ~ R/3 (linear, not exponential). The Gronwall bound from attempt_001 was loose. The actual growth depends on the SPECIFIC structure of the flow, not just the generic bound.
- **2D comparison not informative:** can't compute N_ω on bounded ancient 2D solutions because Liouville says they don't exist.

**What survives:** the NS entropy (Candidate 4 from attempt_003). This is now the only untested direction.

## The construction

### Perelman's W-entropy (review)

On a Riemannian manifold (M, g(t)) evolving by Ricci flow ∂g/∂t = -2Ric:

```
W(g, f, τ) = ∫_M [τ(R + |∇f|²) + f - n] · (4πτ)^{-n/2} · e^{-f} dV_g
```

where f satisfies the conjugate heat equation:
```
∂f/∂τ = -Δf + |∇f|² - R + n/(2τ)
```

(here τ = T - t is backward time). Under coupled evolution of g and f:
```
dW/dτ = 2τ ∫_M |Ric + Hess(f) - g/(2τ)|² · (4πτ)^{-n/2} · e^{-f} dV_g ≥ 0
```

The integrand is a PERFECT SQUARE. Monotonicity is automatic. Equality iff Ric + Hess(f) = g/(2τ), i.e., the metric is a shrinking gradient soliton.

### The NS analog — what should replace what

| Ricci flow | NS | Why |
|---|---|---|
| g(t) (metric) | u(t) (velocity field) | The evolving object |
| Ric (Ricci curvature) | S (strain rate ½(∇u + ∇uᵀ)) | The "curvature" of the flow — both measure deformation |
| R (scalar curvature) | |S|² or |ω|² (enstrophy density) | The scalar contraction |
| Δ (Laplace-Beltrami) | Δ (Laplacian on R³) | Diffusion operator |
| ∂g/∂t = -2Ric | ∂u/∂t = Δu - (u·∇)u - ∇p | Evolution equation |
| Gradient soliton | ??? | The critical point of the entropy |

### The critical question: what is the NS "soliton"?

For Ricci flow, the soliton satisfies Ric + Hess(f) = λg. The metric moves by diffeomorphism + scaling.

For NS, a "soliton" would be a solution that moves by translation + scaling:
```
u(x, t) = λ(t) · U(λ(t)(x - a(t)))
```

This is a SELF-SIMILAR solution. Self-similar ancient NS solutions are precisely the solutions to:
```
-½U - ½(x · ∇)U + (U · ∇)U = ΔU - ∇P     (backward self-similar)
∇ · U = 0
```

**Known result (Tsai 1998, Nečas-Růžička-Šverák 1996):** bounded backward self-similar solutions on R³ are trivial (U ≡ 0). LIOUVILLE IS ALREADY PROVED FOR SELF-SIMILAR SOLUTIONS.

This is exactly analogous to: Perelman's W-entropy forces convergence to a soliton, and on closed simply-connected 3-manifolds the only soliton is the round sphere.

For NS: if we can build an entropy W_NS whose critical points are self-similar solutions, and we already know the only bounded self-similar solution is trivial, then monotonicity of W_NS would prove Liouville for ALL bounded ancient solutions (not just self-similar ones).

### Defining W_NS

By analogy with Perelman, define:

```
W_NS(u, f, τ) = ∫_{R³} [τ(|ω|² + |∇f|²) + f - 3/2] · (4πτ)^{-3/2} · e^{-f} dx
```

where f : R³ → R satisfies a conjugate equation (backward in time):

```
-∂f/∂t = Δf - u · ∇f + |∇f|² - |ω|² + 3/(2τ)
```

and τ > 0 is a scale parameter (backward time).

### Computing dW_NS/dt

This is the critical calculation. Following Perelman's method:

Define the measure dμ = (4πτ)^{-3/2} e^{-f} dx. The conjugate equation for f is chosen so that dμ/dt = 0 (the measure is preserved — same as Perelman).

Then:
```
dW_NS/dt = ∫ [τ · d|ω|²/dt + τ · d|∇f|²/dt + df/dt] dμ
         + ∫ [τ(|ω|² + |∇f|²) + f - 3/2] · (dμ/dt) 
```

The second line vanishes because dμ/dt = 0 by construction of f.

For the first line:

**Term 1: τ · d|ω|²/dt.** Using the vorticity equation ∂ω/∂t = Δω - (u·∇)ω + (ω·∇)u:
```
d|ω|²/dt = 2ω · (Δω - (u·∇)ω + Sω)
         = 2ω · Δω - 2u · ∇(|ω|²/2) + 2(Sω) · ω
         = Δ|ω|² - 2|∇ω|² - u · ∇|ω|² + 2(Sω · ω)
```

**Term 2: τ · d|∇f|²/dt.** Using the conjugate equation for f:
```
This requires computing ∂(∇f)/∂t and is algebraically involved.
```

**Term 3: df/dt.** From the conjugate equation directly:
```
df/dt = -(Δf - u · ∇f + |∇f|² - |ω|² + 3/(2τ))
```

### The obstruction

Here is where the NS calculation DIVERGES from Perelman's.

In Ricci flow, the key identity that makes dW/dτ a perfect square is:

```
d(R + |∇f|²)/dτ = Δ(R + |∇f|²) - 2|Ric + Hess(f) - g/(2τ)|² + (transport)
```

The -2|...|² term is negative-definite and gives the monotonicity.

For NS, the analogous computation gives:
```
d(|ω|² + |∇f|²)/dt = Δ(|ω|² + |∇f|²) - 2|∇ω|² - 2|Hess(f)|²
                      + 2(Sω · ω)        ← the stretching term
                      + (cross terms between ω and f)
                      + (transport)
```

The stretching term 2(Sω · ω) has NO DEFINITE SIGN. This is the same obstruction that killed every other approach — vortex stretching has no sign.

### Can the conjugate equation absorb the stretching?

In Perelman's construction, the conjugate equation for f is specifically designed to absorb the curvature terms. Can we design a different conjugate equation that absorbs the stretching?

**Modified conjugate equation:**
```
-∂f/∂t = Δf - u · ∇f + |∇f|² - |ω|² + α(Sω · ω)/|ω|² + 3/(2τ)
```

where α is a constant chosen to cancel the stretching in dW/dt.

The stretching contributes +2τ(Sω · ω) dμ to dW/dt. Adding α(Sω · ω)/|ω|² to df/dt contributes -α(Sω · ω)/|ω|² dμ to dW/dt. To cancel:

```
2τ(Sω · ω) - α(Sω · ω)/|ω|² = 0
→ α = 2τ|ω|²
```

But α depends on ω, which depends on the solution. The conjugate equation becomes NONLINEAR in f AND u. Perelman's f equation is linear in f (given g). The nonlinearity might destroy the measure-preservation property dμ/dt = 0.

### Where this attempt stands

The NS entropy construction runs into the same wall as every other approach: **the vortex stretching term (Sω · ω) has no definite sign.** Absorbing it into the conjugate equation is possible formally but makes the equation nonlinear in a way that may destroy the structural properties needed for monotonicity.

**This is NOT a dead end** — it's a PRECISELY CHARACTERIZED obstruction. The stretching term is the single algebraic quantity that separates the NS problem from the Ricci flow problem. If (Sω · ω) can be controlled for bounded ancient solutions on R³ — not in general, but for this SPECIFIC class — the entropy construction works.

### What would control (Sω · ω) for bounded ancient solutions?

The stretching term (Sω · ω) = Σᵢⱼ Sᵢⱼ ωᵢ ωⱼ is a quadratic form in ω with matrix S. The strain S is traceless (tr S = 0, from incompressibility) and symmetric. Its eigenvalues sum to zero: λ₁ + λ₂ + λ₃ = 0.

For stretching to be positive (amplify ω), ω must be aligned with the STRETCHING eigendirection (positive eigenvalue of S). For stretching to be negative (compress ω), ω must be aligned with the COMPRESSING eigendirection.

**The question is whether, on average over space, bounded ancient solutions can maintain ω aligned with the stretching direction.**

Physical intuition says NO — the vorticity tends to align with the INTERMEDIATE eigenvector of S (the Betchov 1956 observation, confirmed numerically in turbulence simulations). The intermediate eigenvalue is typically close to zero, so the net stretching is small. But "small on average" is not "zero" and is not "non-positive."

**For the numerical instance:** compute the alignment statistics between ω and the eigenvectors of S on the Burgers vortex. Specifically: what fraction of the domain has ω aligned with λ₁ (stretch) vs λ₂ (intermediate) vs λ₃ (compress)? And what is the SPATIALLY AVERAGED value of (Sω · ω)/|ω|²?

### The meta-observation

Every attempt on Liouville — frequency function, backward uniqueness, energy methods, perturbation from axisymmetric, dimension reduction, AND now the NS entropy — runs into the SAME algebraic obstruction: the vortex stretching term (Sω · ω).

This convergence across 5+ independent approaches confirms that (Sω · ω) IS the gap. The Liouville conjecture for NS reduces, in every formulation, to a statement about the STATISTICS of vortex stretching in bounded ancient solutions.

The question is not "can we avoid the stretching term?" (every route hits it). The question is: "what property of bounded ancient solutions constrains the stretching statistics to be non-amplifying on average?"

## Requests for the numerical instance

1. **Stretching alignment statistics on Burgers:** compute eigenvectors of S, measure the angle between ω and each eigenvector, compute (Sω · ω)/|ω|² as a function of position.
2. **Spatially averaged stretching rate:** ∫(Sω · ω) dx / ∫|ω|² dx on Burgers. Is it positive, negative, or zero?
3. **The same quantities on the Beltrami flow** (where ω ∝ u, so ω is an eigenvector of S automatically).
4. **Prepare to compute W_NS once I finalize the formula** — for now, the formula above with the standard conjugate equation (without the α modification).

## Updated SCRATCHPAD entry needed

Writing to SCRATCHPAD with the Fisher-killed acknowledgment and the new stretching-alignment request.

## Sky bridges

- **Perelman's W-entropy:** the construction works when curvature enters with a definite sign. For NS, the "curvature" (stretching) has no sign. The structural difference between Ricci flow and NS is precisely this sign issue.
- **Turbulence theory (Betchov 1956):** the alignment of ω with eigenvectors of S is a classical question in turbulence. The observation that ω aligns preferentially with the INTERMEDIATE eigenvector is one of the most robust empirical facts in turbulence. If this alignment holds for bounded ancient solutions, it would constrain the stretching and potentially close the entropy argument.
- **The Beale-Kato-Majda criterion:** regularity is equivalent to ∫₀ᵀ ||ω||_∞ dt < ∞. For ancient solutions on (-∞, 0], this becomes ∫_{-∞}⁰ ||ω||_∞ dt < ∞. The stretching term determines whether ||ω||_∞ grows or decays. Same obstruction, different formulation.
