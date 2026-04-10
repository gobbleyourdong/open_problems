# attempt_009 — Pressure Gauge and Far-Field Decay (Agent 4's Finding)

**Date:** 2026-04-10
**Track:** Theory (Even)
**Mountain:** NEW — far-field linearization bypasses (Sω·ω)
**Status:** In progress. This is the first approach that potentially BYPASSES the stretching sign issue entirely by working at spatial infinity instead of in the vortex core.
**Source:** Agent 4 (Sonnet, pressure hint) in the agent-as-numerics experiment. The stall-point was different from the predicted cluster.

## What Agent 4 found

Agent 4 tried the Bernoulli function B = |u|²/2 + p. Key observations:

1. ∇B = -∂ₜu + ω×u + Δu is bounded (by parabolic regularity for bounded ancient solutions)
2. B itself is NOT bounded because p ∈ BMO, not L^∞
3. The obstruction: the spatially constant part of p (the gauge freedom c(t)) is undetermined
4. If u(x,t) → const as |x| → ∞ uniformly in t, the gauge normalizes and B becomes bounded

Agent 4's conclusion: "bounded ancient solutions must have spatial decay at infinity. If true, the Bernoulli argument closes."

## Why this is a different route

All 8 previous attempts hit the stretching term (Sω·ω) as the obstruction. This is a LOCAL problem — what happens inside the vortex core where ω is concentrated.

Agent 4's obstruction is a FAR-FIELD problem — what happens as |x| → ∞. This is a fundamentally different location in the solution, and the tools that apply are different:
- **Local (core):** stretching, energy methods, frequency function — all hit (Sω·ω)
- **Far-field (infinity):** heat kernel asymptotics, spatial decay estimates, potential theory

The far-field might be EASIER because:
- At large |x|, ∇u decays (parabolic regularity for bounded solutions)
- The nonlinear term (u·∇)u = O(M · |∇u|) = O(M · C(M) / |x|) → 0
- So at large |x|, the equation is APPROXIMATELY LINEAR (heat + Stokes)
- Bounded ancient solutions of linear equations are constant (classical Liouville)

## The far-field linearization argument

### Step 1: Spatial gradient decay

For bounded ancient solutions on R³ with |u| ≤ M, standard parabolic regularity gives:

```
|∇ᵏu(x, t)| ≤ Cₖ(M, ν)    for all x ∈ R³, t ≤ 0, k ≥ 0
```

This is a UNIFORM bound on all derivatives, independent of position and time. But it doesn't give DECAY at infinity — the bound is the same at |x| = 1 and |x| = 10⁶.

**Can we get spatial decay of ∇u for bounded ancient solutions?**

For the heat equation ∂v/∂t = Δv with |v| ≤ M on R³ × (-∞, 0]:
- v is a bounded ancient caloric function
- By the Liouville theorem for the heat equation: v is a polynomial in x of degree ≤ d for some d
- Bounded polynomial on R³ → d = 0 → v is constant → ∇v ≡ 0

For NS, the nonlinearity prevents this clean argument. But the FAR-FIELD behavior should be close to heat:

### Step 2: The nonlinear term at infinity

The nonlinear term is:
```
|(u · ∇)u(x, t)| ≤ |u(x,t)| · |∇u(x,t)| ≤ M · C₁(M, ν)
```

This is bounded but NOT decaying. The issue: both |u| and |∇u| are bounded uniformly, so their product is bounded uniformly. We don't get decay at infinity from this estimate.

**But wait — can we get spatial decay of ∇u WITHOUT assuming it?**

Consider the REPRESENTATION formula for bounded ancient solutions. From attempt_002:

```
u(x, t) = ū + w(x, t)
w(x, t) = -∫_{-∞}^t ∫_{R³} K(x-y, t-τ) · (w⊗w)(y,τ) dy dτ
```

where K is the Oseen kernel. The Oseen kernel decays exponentially in |x-y|/√(t-τ):

```
|K(x-y, t-τ)| ≤ C · (t-τ)^{-2} · exp(-c|x-y|²/(t-τ))
```

For fixed x with |x| → ∞, the integral over y is dominated by |y| near |x| (the kernel concentrates). But (w⊗w)(y,τ) is bounded by (2M)² for all y. So:

```
|w(x, t)| ≤ C · (2M)² · ∫_{-∞}^t (t-τ)^{-2} · ∫_{R³} exp(-c|x-y|²/(t-τ)) dy dτ
```

The spatial integral gives (π(t-τ)/c)^{3/2}. So:

```
|w(x, t)| ≤ C' · M² · ∫_{-∞}^t (t-τ)^{-1/2} dτ = ∞
```

The temporal integral DIVERGES. This is the same issue from attempt_002 — the L^∞ norm doesn't give convergence.

**The ancient representation doesn't directly give spatial decay.** The temporal divergence masks any spatial structure.

### Step 3: Spatial decay via a DIFFERENT mechanism

Let me try a different approach. Consider the PRESSURE equation:

```
-Δp = ∂ᵢ∂ⱼ(uᵢuⱼ) = tr(∇u · ∇u)
```

The right side is bounded: |tr(∇u · ∇u)| ≤ |∇u|² ≤ C₁². On R³, the Newton potential gives:

```
p(x) = -1/(4π) ∫_{R³} tr(∇u · ∇u)(y) / |x - y| dy + c(t)
```

The integral converges (the integrand is bounded and the kernel 1/|x-y| is locally integrable in 3D). For |x| → ∞:

```
|p(x) - c(t)| ≤ C₁²/(4π) · ∫_{R³} 1/|x-y| dy · χ_{|∇u(y)| > ε}  +  ε² · ∫ 1/|x-y| dy
```

Hmm, this doesn't simplify cleanly because ∇u doesn't decay.

### Step 4: The REAL question

The far-field linearization requires: |∇u(x,t)| → 0 as |x| → ∞.

For bounded ancient solutions, do we have spatial decay of the gradient?

**Known:** for the STATIONARY NS equations (Δu = (u·∇)u + ∇p on R³ with |u| ≤ M):
- Chae (2014): if u is a smooth bounded steady solution, then u is constant (Liouville for steady NS)
- The proof USES spatial decay of ∇u, which Chae derives from the steady equation structure

**For the ancient (non-steady) case:** the time derivative ∂u/∂t is bounded (parabolic regularity). So:

```
Δu = ∂u/∂t + (u·∇)u + ∇p
```

All terms on the right are bounded. The Laplacian of a bounded function with bounded Laplacian on R³ — does this give spatial decay of ∇u?

By elliptic regularity at each fixed time: Δu ∈ L^∞ → u ∈ W^{2,p}_{loc} for all p. But NO decay at infinity without additional assumptions.

**HOWEVER:** the ancient condition gives us more. At each time t, u(·, t) is a bounded function on R³ with bounded Laplacian. As t → -∞, the function has existed for longer and longer. The heat equation component of the NS evolution has been smoothing for infinite time.

**The key estimate:** for a function f on R³ with |f| ≤ M and |Δf| ≤ K, the gradient satisfies:

```
|∇f(x)| ≤ C · (M/R + K·R)    for all R > 0
```

Optimizing: R = √(M/K), giving |∇f(x)| ≤ C · √(MK). This is POSITION-INDEPENDENT — no spatial decay.

**Dead end for pure elliptic estimates.** The gradient bound doesn't decay in space without additional structure.

### Step 5: What would make the far-field work

The far-field linearization requires one of:
(a) Spatial decay of ∇u: |∇u(x,t)| → 0 as |x| → ∞ (not proved)
(b) Spatial decay of u - ū: |u(x,t) - ū| → 0 as |x| → ∞ (not proved)
(c) A way to normalize the pressure without spatial decay (unclear)
(d) A far-field energy estimate that avoids the stretching issue at infinity

**None of these are immediate.** The far-field approach is a genuinely different angle (Agent 4 found a new obstruction), but converting it to a proof requires either spatial decay results that don't currently exist, or a new way to handle the pressure gauge.

### Step 6: The spatial decay question AS the gap

**New formulation of the gap:** the Liouville conjecture may reduce to:

"Do bounded ancient NS solutions on R³ satisfy u(x,t) → const as |x| → ∞?"

If yes: pressure normalizes → Bernoulli bounds → far-field linearization → core estimates → Liouville.

If no: there exist bounded ancient solutions with non-trivial far-field behavior, which would be remarkable objects in their own right.

**This is a DIFFERENT question from backward decay** (attempt_002's formulation: ||w(t)|| → 0 as t → -∞). It's SPATIAL decay, not TEMPORAL decay. The two questions are independent — you could have spatial decay without temporal decay, or vice versa.

**Which is easier?**
- Temporal backward decay: requires controlling the stretching term over infinite time. HARD (every approach hits Sω·ω).
- Spatial far-field decay: requires showing bounded solutions can't sustain non-trivial far-field structure. POSSIBLY EASIER because the far field is more linear.

## The updated decomposition

```
FULL LIOUVILLE = (1a OR 1b) + (2) + (3)

(1a) Backward temporal decay: ||w(t₀)||_∞ < ε₀ at some t₀     [original gap]
(1b) Spatial far-field decay: u(x,t) → const as |x| → ∞        [NEW, from Agent 4]
(2) Small-data Liouville: ||w||_∞ < ε₀ → w ≡ 0                [PROVED, attempt_008]
(3) Unique continuation: w(·,t₀) = 0 → w ≡ 0                   [KNOWN, ESŠ]

Either (1a) or (1b) would close the full Liouville. They are different paths.
(1b) bypasses the stretching sign issue entirely by working at |x| → ∞.
```

## Status

Agent 4's finding is REAL — the pressure gauge is a genuinely different obstruction from (Sω·ω). The far-field approach is promising in principle (it bypasses the stretching sign issue) but requires spatial decay of bounded ancient solutions, which is itself an open question.

The spatial decay question might be easier than the temporal decay question because the far field is more linear. But "might be easier" is not "is easier" — the gradient estimates in Step 4 show that naive elliptic bounds don't give spatial decay.

**Next step:** investigate whether the ANCIENT condition (infinite backward time + heat semigroup smoothing) forces spatial decay. The heat equation forces spatial decay for ancient solutions (they're constant). The NS nonlinearity at large |x| is small relative to diffusion. Can we bootstrap from "small nonlinearity at infinity" to "spatial decay"?

## Requests for numerics

1. On a truncated or bounded modification of Burgers: compute |∇u(x)|/|Δu(x)| at large |x|. Does the gradient decay relative to the Laplacian?
2. Run Agent 4's Bernoulli argument to completion assuming spatial decay. What exactly does the argument prove? Does it give FULL Liouville or only partial?
