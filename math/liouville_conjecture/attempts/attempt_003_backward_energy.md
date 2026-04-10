# attempt_003 — Backward Energy Inequality (the Perelman analog)

**Date:** 2026-04-09
**Track:** Theory (Even)
**Mountain:** 3 + 5 hybrid (energy methods + dimension reduction)
**Status:** In progress. The numerics instance quantified the gap precisely: backward decay is automatic at large scales (R >> R_crit) but not at small scales (R << R_crit = √(ν/C(M))). The theory challenge is proving small-scale decay using the structure of Sω for bounded divergence-free fields.

## The reduction from attempt_002

Liouville is equivalent to backward decay: ||w(t)||_∞ → 0 as t → -∞, where w = u - ū is the fluctuation from the spatial mean.

The numerics instance (backward_decay.md) quantified this precisely:

```
Model: d|ω|²/dt = -2νλ₁|ω|² + 2α|ω|²

At scale R:
  diffusion rate = ν/R²
  stretching rate = α ~ C(M) ≤ ||S||_∞ ≤ C'(M)

R_crit = √(ν/C(M))

R >> R_crit: diffusion wins → backward decay automatic
R << R_crit: stretching can win → backward decay OPEN
```

So large-scale features of bounded ancient solutions MUST decay backward (diffusion dominates). The question is whether small-scale features (R < R_crit) can persist.

## The Perelman parallel (concrete version)

In Ricci flow, Perelman defined the W-entropy:

```
W(g, f, τ) = ∫ [τ(R + |∇f|²) + f - n] · (4πτ)^{-n/2} e^{-f} dV
```

W is monotone non-decreasing along Ricci flow. Equality holds precisely on shrinking gradient solitons. For an ancient solution, W(t) is bounded above (from the curvature bound) and monotone → W has a limit as t → -∞ → the ancient solution is a soliton → the only bounded soliton on R³ is the constant curvature metric.

**The analog for NS would be:** a functional E(u, t) that is:
1. Monotone non-increasing forward in time (dissipative)
2. Bounded below (from the boundedness of u)
3. Equality characterizes the trivial solution (E = 0 iff u = const)

Then for an ancient solution: E is monotone and bounded → E has a limit as t → -∞ → the limit characterizes the solution → the only possibility is E = 0 → u = const.

## Candidate functionals

### Candidate 1: Enstrophy Ω(t) = ∫_{R³} |ω|² φ dx

The enstrophy (localized with a cutoff φ) satisfies:

```
dΩ/dt = -2ν ∫ |∇ω|² φ dx + 2 ∫ (Sω · ω) φ dx + (transport and cutoff terms)
```

The first term is strictly dissipative. The second is the vortex stretching.

For the enstrophy to be monotone non-increasing, we need:

```
ν ∫ |∇ω|² φ ≥ ∫ (Sω · ω) φ
```

The right side is bounded by ||S||_∞ · Ω. The left side is bounded below by (ν/R²) · Ω (Poincaré inequality on B_R). So the condition is:

```
ν/R² ≥ ||S||_∞
```

which is exactly R ≥ R_crit. **Enstrophy is monotone non-increasing at scales above R_crit** — consistent with the numerics. But at scales below R_crit, the stretching term can increase enstrophy.

**Dead end for Candidate 1** in its current form. The enstrophy inequality reproduces the same scale dichotomy the numerics found.

### Candidate 2: Weighted enstrophy with Gaussian weight

**Idea:** use a Gaussian weight that couples the spatial and temporal scales.

Define:
```
Ω_τ(t) = ∫_{R³} |ω(x,t)|² · (4πτ)^{-3/2} · e^{-|x|²/(4τ)} dx
```

This is the enstrophy convolved with a Gaussian of width √τ. The parameter τ plays the role of Perelman's τ (backward time scale).

For the heat equation (ω = 0, linear diffusion), the Gaussian-weighted norm of any function is monotone non-increasing in t when τ = const. This is because the heat kernel commutes with the Gaussian weight.

For NS, the stretching term contributes:

```
dΩ_τ/dt = -(dissipation from Δω weighted by Gaussian)
           + 2 ∫ (Sω · ω) · G_τ dx
           + (transport terms from (u·∇)ω)
```

The transport terms (u · ∇)ω contribute a term involving u · ∇(G_τ) = u · (-x/(2τ)) · G_τ. For bounded u, this is bounded by (M/(2τ)) · |x| · G_τ, which is integrable.

**The key ratio:** at the scale √τ, the dissipation rate is ν/τ and the stretching rate is ||S||_∞ ≤ C(M). So the Gaussian weight is effective when:

```
τ ≤ ν / C(M) = R_crit²
```

For small τ (high spatial resolution), the Gaussian concentrates near the origin and the dissipation at that scale wins. For large τ (low spatial resolution), the dissipation is weak and stretching can dominate.

**This is the SAME dichotomy but parameterized differently.** The Gaussian weight doesn't resolve the small-scale problem — it just moves the cutoff from R_crit in space to R_crit² in the τ parameter.

### Candidate 3: Log-enstrophy (inspired by Perelman's f-functional)

**Idea:** Perelman's entropy involves log terms (f = log of a density). Try:

```
L(t) = ∫_{R³} |ω|² · log(|ω|² / Ω₀) · φ dx
```

where Ω₀ is a reference enstrophy level.

The log weighting penalizes concentration: if ω is spread out (low peak, high volume), L is large and negative. If ω is concentrated (high peak, low volume), L is large and positive. The log shifts the balance between dissipation and stretching because:
- Dissipation smooths ω (reduces concentration) → decreases L
- Stretching concentrates ω (amplifies peaks) → increases L

The evolution:
```
dL/dt = -2ν ∫ |∇ω|²/|ω|² · |ω|² φ dx  +  stretching terms  +  ...
```

Wait — the Fisher information ∫ |∇ω|²/|ω|² is exactly the right quantity! It measures the "roughness" of the vorticity distribution. For the Liouville problem:
- Fisher information is high when ω has sharp gradients (concentrated)
- Fisher information is zero when ω is constant

The dissipative term -2ν · (Fisher info) · Ω is negative-definite and proportional to how "non-constant" ω is. **This might be the functional where dissipation automatically beats stretching regardless of scale.**

**Why?** The stretching term (Sω · ω) amplifies |ω|² but does NOT change |∇ω|²/|ω|² (the Fisher information) because stretching is a LINEAR operation on ω (Sω is linear in ω). So:

```
d(Fisher)/dt due to stretching = 0  (stretching is scale-invariant)
d(Fisher)/dt due to diffusion < 0   (diffusion reduces gradients)
```

If this is right, the Fisher information of ω is monotone non-increasing for ALL bounded ancient NS solutions, regardless of scale!

**CHECK THIS CAREFULLY.** The claim "stretching doesn't change Fisher information" needs rigorous verification. Stretching Sω IS linear in ω, but it changes both |ω|² and |∇ω|² — the ratio |∇ω|²/|ω|² might change.

Let S be constant (the simplest case). Then ∂ω/∂t = Sω gives ω(t) = e^{St} ω₀. Then:
```
|ω|² = |e^{St} ω₀|²
|∇ω|² = |e^{St} ∇ω₀|²  (S doesn't depend on x in this model)
```

So |∇ω|²/|ω|² = |e^{St} ∇ω₀|² / |e^{St} ω₀|². This is NOT constant — it depends on how the eigenvectors of S align with ω₀ vs ∇ω₀. If ω₀ is aligned with the stretching direction but ∇ω₀ is aligned with the compressing direction, the ratio DECREASES. If both are aligned the same way, the ratio is unchanged.

**Correction:** stretching DOES change the Fisher information. The claim was wrong. But the change depends on the ALIGNMENT between ω, ∇ω, and S. For BOUNDED divergence-free fields, the alignment might be constrained.

### Candidate 4: The NS entropy (direct Perelman analog)

**The most ambitious candidate.** Define, by analogy with Perelman's W-entropy:

```
W_NS(u, f, τ) = ∫ [τ(|ω|² + |∇u|²) + f - 3] · (4πτ)^{-3/2} · e^{-f} dx
```

where f satisfies a conjugate equation (backward heat equation with NS transport):

```
-∂f/∂t = Δf - u · ∇f + |∇f|² - |ω|²/(2τ) + 3/(2τ)
```

This is modeled directly on Perelman's construction, replacing Ricci curvature R with enstrophy density |ω|² and the metric evolution with the NS evolution.

**The question:** does W_NS have a monotonicity property along NS solutions?

This is the deepest attempt and requires careful calculation. I will NOT claim monotonicity without computing dW_NS/dt explicitly. But the structure is promising because:
- Perelman's W works by balancing curvature (analogous to enstrophy) against diffusion
- The conjugate equation for f absorbs the transport term (u · ∇) cleanly
- The factor τ provides the scale coupling that the other candidates were missing

**This is Attempt 004 or 005 material — too deep for this fire.** Flagging it for the next round.

## Summary of this fire

| Candidate | Status | Why |
|---|---|---|
| 1. Enstrophy | Dead end | Reproduces the R_crit dichotomy, doesn't resolve small scales |
| 2. Gaussian-weighted enstrophy | Dead end | Same dichotomy in τ parameterization |
| 3. Log-enstrophy / Fisher info | **PARTIALLY ALIVE** | Stretching's effect on Fisher info depends on alignment; alignment might be constrained for bounded div-free fields. Needs more work. |
| 4. NS entropy (Perelman analog) | **PROMISING, UNTESTED** | Direct structural analog of what worked for Poincaré. Too deep for one fire. Flagged for Attempt 004. |

## The key insight from this fire

The standard energy functionals (enstrophy, weighted enstrophy) all reproduce the SAME scale dichotomy: diffusion wins above R_crit, stretching can win below. No simple energy functional resolves this because the dichotomy is a REAL FEATURE of the NS vorticity equation.

To break through, the functional must exploit STRUCTURAL properties of (ω · ∇)u = Sω for bounded divergence-free fields that the generic |S| · |ω| bound misses. Two candidates remain:
1. Fisher information with alignment constraints (Candidate 3)
2. The full NS entropy à la Perelman (Candidate 4)

Both need the next fire.

## Coupled observation

The numerics instance's backward_decay.md gave me the EXACT quantitative structure I needed: R_crit = √(ν/C(M)), large-scale decay automatic, small-scale persistence is the gap. Without that quantification, I would have spent this fire rediscovering the dichotomy algebraically. Instead I could jump straight to testing candidate functionals against it. The coupling saved a full fire.

Their dimensional ladder (2D: no stretching → max principle → Liouville proved; 3D: stretching breaks max principle → Liouville open) is the clearest statement of the 2D→3D gap I've seen. The stretching eigenvalue α is the single parameter that separates the proved from the open case.
