# attempt_010 — Spatial Decay for Bounded Ancient Solutions

**Date:** 2026-04-10
**Track:** Theory (Even)
**Mountain:** 9 (far-field / pressure gauge, from Agent 4)
**Status:** Pushing the far-field path. The question: do bounded ancient NS solutions on R³ have spatial decay of the gradient?

## The precise question

Let u be a bounded ancient mild solution to NS on R³ with |u| ≤ M. Does:

```
|∇u(x, t)| → 0   as |x| → ∞,   uniformly in t ≤ 0  ?
```

If yes: the far-field is linear, the pressure normalizes, and attempt_009's chain closes.
If no: bounded ancient solutions can have non-trivial far-field structure for infinite time.

## What parabolic regularity gives (and doesn't)

### Interior estimates (standard)

For any ball B_R(x₀) with R ≥ 1, the NS interior estimates give:

```
|∇u(x₀, t)| ≤ C(M, ν) / R^α    for some α > 0  ???
```

**Actually: NO.** Standard interior estimates for NS give:

```
|∇u(x₀, t)| ≤ C · (||u||_{L^∞(Q_R)} / R + ||u||_{L^∞(Q_R)}² / ν)
```

where Q_R = B_R(x₀) × [t-R², t] is a parabolic cylinder. For |u| ≤ M:

```
|∇u(x₀, t)| ≤ C · (M/R + M²/ν)
```

The first term M/R decays with R. The second term M²/ν does NOT. So:

```
|∇u(x₀, t)| ≤ C · M²/ν    (bounded, but no spatial decay)
```

**Standard parabolic regularity does not give spatial decay of ∇u.** The bound is uniform in x₀.

## A different approach: the ancient condition + mean value

For the HEAT equation, bounded ancient solutions are characterized by the mean value property. A bounded ancient caloric function u satisfies:

```
u(x, t) = ∫_{R³} G(x-y, τ) u(y, t-τ) dy    for all τ > 0
```

where G is the heat kernel. Taking τ → ∞ and using |u| ≤ M:

```
u(x, t) → ū    as τ → ∞    (convergence to spatial mean)
```

This gives u(x, t) ≡ ū (Liouville for the heat equation). The gradient vanishes identically.

For NS, the mild formulation gives:

```
u(x, t) = ∫ G(x-y, τ) u(y, t-τ) dy - ∫₀^τ ∫ K(x-y, s) (u⊗u)(y, t-s) dy ds
```

where K is the Oseen kernel. The first term → ū as τ → ∞ (same as heat). The gradient of the first term → 0 as τ → ∞.

The second term (the Duhamel integral) has gradient:

```
∇_x [∫₀^τ ∫ K(x-y, s) (u⊗u)(y, t-s) dy ds]
= ∫₀^τ ∫ ∇_x K(x-y, s) · (u⊗u)(y, t-s) dy ds
```

The Oseen kernel gradient satisfies:

```
|∇_x K(x-y, s)| ≤ C · s^{-2} · (1 + |x-y|/√s) · exp(-c|x-y|²/s)
```

For the integral over y: at fixed x with |x| large, the contributions from |y| near the origin are suppressed by exp(-c|x|²/s) (the kernel localizes around x, not around the origin). The contributions from |y| near x involve (u⊗u)(y, t-s) which is bounded by M².

**The key question:** does the Duhamel integral ∫₀^τ converge as τ → ∞, AND does its gradient at x depend on |x|?

The gradient at x involves:
```
∫₀^τ s^{-2} · exp(-c|x|²/s) · M² · s^{3/2} ds = M² ∫₀^τ s^{-1/2} · exp(-c|x|²/s) ds
```

Substitution σ = |x|²/s:
```
= M² · |x|² ∫_{|x|²/τ}^∞ σ^{-3/2} · exp(-cσ) · dσ/σ  ??? 
```

Let me be more careful. Setting σ = c|x|²/s (so s = c|x|²/σ, ds = -c|x|²/σ² dσ):

```
= M² ∫_{c|x|²/τ}^∞ (c|x|²/σ)^{-1/2} · exp(-σ) · c|x|²/σ² dσ
= M² · c^{1/2} · |x| ∫_{c|x|²/τ}^∞ σ^{-3/2} · exp(-σ) dσ
```

As τ → ∞, the lower limit → 0, and:
```
∫_0^∞ σ^{-3/2} · exp(-σ) dσ = Γ(-1/2) ... 
```

Wait, Γ(-1/2) diverges. The integral ∫_0^∞ σ^{-3/2} e^{-σ} dσ diverges at 0. This means the Duhamel gradient integral DIVERGES as τ → ∞.

**But this is the GLOBAL integral.** The ANCIENT solution's Duhamel integral starts from -∞, not from 0. Let me reconsider.

## The ancient Duhamel at large |x|

For an ancient solution, the representation is:

```
u(x, t) = ū - ∫_{-∞}^t ∫_{R³} K(x-y, t-s) · ∇·(w⊗w)(y, s) dy ds
```

The gradient at x:
```
∇u(x, t) = -∫_{-∞}^t ∫_{R³} ∇_x K(x-y, t-s) · ∇·(w⊗w)(y, s) dy ds
```

The Oseen kernel has the DIVERGENCE form built in: K acts on ∇·F, not on F. By integration by parts in y:

```
∇u(x, t) = -∫_{-∞}^t ∫_{R³} ∇_x ∇_y K(x-y, t-s) · (w⊗w)(y, s) dy ds
```

Now ∇_x ∇_y K = -∇_x² K (since K depends on x-y). So:

```
|∇u(x, t)| ≤ ∫_{-∞}^t ∫_{R³} |∇²K(x-y, t-s)| · |w|² dy ds
```

The second-derivative kernel:
```
|∇²K(z, s)| ≤ C · s^{-5/2} · exp(-c|z|²/s)
```

At large |x|, the dominant contribution to the y-integral comes from TWO regions:
- **Near the origin** (|y| ~ 0): |x-y| ≈ |x|, kernel ~ s^{-5/2} exp(-c|x|²/s). Suppressed exponentially.
- **Near x** (|y| ~ |x|): |x-y| ~ 0, kernel ~ s^{-5/2}. NOT suppressed.

The contribution from |y| near x:
```
∫_{B_1(x)} |∇²K(x-y, t-s)| · |w(y,s)|² dy ≤ C · s^{-5/2} · (2M)² · |B_1| = C' · M² · s^{-5/2}
```

Integrating over s from -∞ to t:
```
∫_{-∞}^t s^{-5/2} ds diverges at s = t (i.e., t - s → 0)
```

Wait — I should write τ = t - s > 0:
```
∫_0^∞ τ^{-5/2} dτ diverges at τ = 0
```

**The integral diverges near τ = 0 (short times).** This is a standard singularity of the Oseen kernel — resolved by the regularity of w (the integrand has better behavior than the kernel alone suggests because w is smooth).

For smooth w, integration by parts in time absorbs the singularity:
```
∫_0^∞ τ^{-5/2} · |w(x, t-τ)|² dτ = [time-IBP terms] + smoother integral
```

This is getting into technical regularity theory that's hard to resolve without a full functional-analytic setup.

## The honest assessment

The spatial decay question for bounded ancient NS solutions is:
1. **TRUE for the heat equation** (bounded ancient caloric → constant → ∇ ≡ 0)
2. **LIKELY TRUE for NS** based on physical reasoning (what bounded solution has non-trivial far-field structure for infinite time?)
3. **NOT PROVED by standard estimates** (parabolic regularity gives uniform bounds, not decay)
4. **REQUIRES either:**
   (a) A new estimate that uses the ANCIENT condition to force spatial decay, or
   (b) A way to handle the pressure gauge WITHOUT spatial decay, or
   (c) Working in a function space where spatial decay is built in (but then boundedness alone isn't enough as a hypothesis)

## The comparison: spatial decay vs backward temporal decay

| Question | Spatial decay at ∞ | Backward temporal decay |
|---|---|---|
| Statement | |∇u(x,t)| → 0 as |x| → ∞ | ||w(t)|| → 0 as t → -∞ |
| Blocks which approach? | Far-field / pressure gauge | Small-data contraction |
| Known for heat equation? | Yes (bounded ancient → constant) | Yes (bounded ancient → constant) |
| Known for NS? | No | No |
| Uses stretching? | Only indirectly (far field is approximately linear) | Directly ((Sω·ω) is the obstruction) |
| Which might be easier? | Maybe — the far field IS more linear | Maybe — more tools available (energy methods, Carleman) |

**These two questions might be EQUIVALENT.** If spatial decay holds, the solution becomes small at large |x|, and a localized version of the small-data argument might give temporal decay too. Conversely, if temporal backward decay holds, the solution was "born from nothing" and should also decay at infinity.

**The deep question:** are spatial decay and temporal backward decay for bounded ancient NS EQUIVALENT, or is one strictly easier? If they're equivalent, we haven't gained a new path — we've just reformulated the same gap. If spatial decay is strictly easier (because the far field is more linear), Agent 4's finding is a genuine advance.

## What would resolve this

A result of the form: "bounded ancient solutions with spatial decay have temporal decay" or vice versa would show the two paths converge. Neither direction is known.

**The most promising sub-question:** for bounded ancient NS on R³, does u(x,t) have a LIMIT as |x| → ∞? Not necessarily zero — just any limit. If lim_{|x|→∞} u(x,t) = L(t) exists for each t, then L(t) is a bounded ancient ODE solution (in the limit the PDE reduces to an ODE). Bounded ancient ODE solutions are constant: L(t) ≡ L. Then u(x,t) → L as |x| → ∞, uniformly in t. This is spatial decay to a constant, which is what Agent 4 needs.

**Does the limit at infinity exist?** For bounded functions on R³, the limit at infinity doesn't exist in general (oscillating functions). But for bounded ancient SOLUTIONS to NS — with all the regularity that entails — it might. The ancient condition + smoothness + boundedness is a very restrictive class.

## Next step

Investigate whether bounded ancient NS solutions on R³ have a well-defined spatial limit at infinity. This is a question about the far-field ASYMPTOTICS of solutions with infinite backward history. It should be accessible by:
1. Spatial averaging on large spheres: does (1/|∂B_R|) ∫_{∂B_R} u dS converge as R → ∞?
2. Comparing with the heat kernel representation (the linear part HAS a limit at infinity)
3. Using the divergence-free condition to constrain far-field oscillations (div u = 0 limits what oscillatory patterns are possible)
