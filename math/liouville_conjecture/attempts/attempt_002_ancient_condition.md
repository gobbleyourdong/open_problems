# attempt_002 — Exploiting the Ancient Condition

**Date:** 2026-04-09
**Track:** Theory (Even)
**Mountain:** 2 + 3 hybrid (backward uniqueness + energy methods)
**Status:** In progress. Two structural properties of ancient solutions identified that finite-time solutions don't have.

## What does "ancient" give us that we aren't using?

An ancient solution u : R³ × (-∞, 0] → R³ has been running for INFINITE backward time. Most NS analysis deals with forward-in-time solutions from initial data. The ancient condition is much stronger — it says the solution is smooth and bounded for ALL t ≤ 0.

### Property 1: Backward regularity bootstrapping

For any t₀ ≤ 0, the solution exists on (-∞, t₀]. Standard parabolic regularity gives:

```
For any k ≥ 0: sup_{x ∈ R³} |∇ᵏu(x, t₀)| ≤ C(k, M)
```

where C depends on k and the bound M, but NOT on how long the solution has existed. For a solution on [0, T], these bounds depend on T. For an ancient solution, they are INDEPENDENT of T because T = ∞.

**This means:** every spatial derivative of a bounded ancient solution is uniformly bounded on R³ × (-∞, 0]. This is strictly stronger than what a finite-time bounded solution gives.

In particular: **∇u, ∇²u, ∇p are all uniformly bounded on R³ × (-∞, 0].**

Wait — is ∇p bounded? Let me check.

The pressure satisfies: -Δp = ∂ᵢ∂ⱼ(uᵢuⱼ). For bounded u with bounded ∇u (which we have by parabolic regularity), the right side is bounded. On R³, the solution to -Δf = g with g bounded is:

```
∇p(x) = ∫_{R³} ∇K(x-y) · ∂ᵢ∂ⱼ(uᵢuⱼ)(y) dy
```

where K is the Newton kernel. Integration by parts twice:

```
∇p(x) = ∫_{R³} ∇³K(x-y) · (uᵢuⱼ)(y) dy
```

This is a Calderón-Zygmund singular integral of a bounded function. CZ theory gives ∇p ∈ BMO (not L^∞). So ∇p is NOT uniformly bounded in general, even for ancient solutions.

**BUT:** for ancient solutions, we have ∇u bounded (from parabolic regularity). So the right side of -Δp = ∂ᵢ∂ⱼ(uᵢuⱼ) can also be written as:

```
-Δp = ∂ᵢ(uⱼ ∂ⱼuᵢ) + ∂ⱼ(uᵢ ∂ᵢuⱼ) - ∂ᵢ∂ⱼ(uᵢuⱼ)  ... no, that's circular
```

Let me use the divergence-free condition: ∂ᵢuᵢ = 0. Then:

```
-Δp = ∂ᵢ∂ⱼ(uᵢuⱼ) = (∂ᵢuⱼ)(∂ⱼuᵢ) + uᵢ ∂ᵢ∂ⱼuⱼ + uⱼ ∂ⱼ∂ᵢuᵢ + uᵢuⱼ ∂ᵢ∂ⱼ(...)
```

Actually more simply: -Δp = tr(∇u · ∇u) = Σᵢⱼ (∂ᵢuⱼ)(∂ⱼuᵢ). For ancient solutions, ∇u is bounded, so:

```
|tr(∇u · ∇u)| ≤ |∇u|² ≤ C(M)²
```

So -Δp = f where f ∈ L^∞(R³) with ||f||_∞ ≤ C(M)². On R³, this gives p ∈ BMO, ∇p ∈ BMO^{-1} (not L^∞). The pressure gradient is still not bounded.

**Dead end for direct pressure bounding.** But there's a subtlety I missed...

### Property 2: The ancient mean-value property

For the heat equation, ancient solutions satisfy a mean-value property over parabolic balls extending backward in time. Specifically, if (∂/∂t - Δ)v = 0 on R³ × (-∞, 0], then v satisfies:

```
v(x, t) = ∫∫ v(y, s) · G(x-y, t-s) dy ds
```

for ALL backward time, where G is the heat kernel. This is much more restrictive than the forward mean-value property.

For NS, the nonlinearity breaks the exact mean-value property, but there should be an APPROXIMATE version. The key representation formula for mild solutions is:

```
u(t) = e^{(t-s)Δ} u(s) - ∫_s^t e^{(t-τ)Δ} P∇·(u⊗u)(τ) dτ
```

where P is the Leray projection. For ancient solutions, we can take s → -∞:

```
u(t) = lim_{s→-∞} [e^{(t-s)Δ} u(s)] - ∫_{-∞}^t e^{(t-τ)Δ} P∇·(u⊗u)(τ) dτ
```

The first term: e^{(t-s)Δ} u(s) with |u(s)| ≤ M. As s → -∞, e^{(t-s)Δ} smears u(s) over larger and larger scales. In the limit:

```
lim_{s→-∞} e^{(t-s)Δ} u(s) = ū  (spatial average, a constant vector)
```

This uses the fact that the heat kernel becomes flat as t-s → ∞. For bounded u, the spatial average ū exists and equals the limit.

**So every bounded ancient mild solution satisfies:**

```
u(t) = ū - ∫_{-∞}^t e^{(t-τ)Δ} P∇·(u⊗u)(τ) dτ     ... (★)
```

**This is a fixed-point equation!** The ancient solution is a constant ū minus a nonlinear integral over all past time. The Liouville conjecture says this integral must be zero (u ≡ ū, and then divergence-free on R³ forces ū = 0 if we normalize).

### What (★) gives us

Equation (★) says:

```
u(t) - ū = - ∫_{-∞}^t e^{(t-τ)Δ} P∇·(u⊗u)(τ) dτ
```

Define w = u - ū (the fluctuation from the spatial mean). Then:

```
w(t) = - ∫_{-∞}^t e^{(t-τ)Δ} P∇·((w+ū)⊗(w+ū))(τ) dτ
```

Expanding: (w+ū)⊗(w+ū) = w⊗w + ū⊗w + w⊗ū + ū⊗ū.

The ū⊗ū term: ∇·(ū⊗ū) = (ū · ∇)ū = 0 (constant). So it drops out.

The cross terms: ∇·(ū⊗w) = (ū · ∇)w and ∇·(w⊗ū) = (w · ∇)ū + ū(∇·w) = 0 (since ū is constant and ∇·w = 0). So ∇·(w⊗ū) = 0. Only the first cross term survives:

```
w(t) = - ∫_{-∞}^t e^{(t-τ)Δ} P[(ū · ∇)w + ∇·(w⊗w)](τ) dτ
```

The linear part (ū · ∇)w is just advection by a constant. In a moving frame x' = x - ūt, this term vanishes. So in the co-moving frame:

```
w(t) = - ∫_{-∞}^t e^{(t-τ)Δ} P∇·(w⊗w)(τ) dτ       ... (★★)
```

**This is a pure fixed-point equation for the fluctuation w, with NO linear transport term.** The Liouville conjecture is equivalent to: **(★★) has no bounded non-zero solution.**

### Why (★★) is progress

Equation (★★) is a nonlinear integral equation on R³ × (-∞, 0]. The integral operator maps:

```
T[w](t) = - ∫_{-∞}^t e^{(t-τ)Δ} P∇·(w⊗w)(τ) dτ
```

For T to have a fixed point w = T[w], we need ||T[w]|| ≤ ||w|| in some norm. The key estimate is:

```
||e^{(t-τ)Δ} P∇·(w⊗w)||_∞ ≤ C · (t-τ)^{-1/2} · ||w||_∞ · ||w||_∞ · (t-τ)^{-3/4}  ... ???
```

Actually, the Oseen kernel estimate gives:

```
||e^{tΔ} P∇ · F||_∞ ≤ C · t^{-1/2} · ||F||_∞     (for divergence-form F)
```

Wait — this has a t^{-1/2} singularity. Integrating from -∞ to t:

```
||T[w](t)||_∞ ≤ C · ||w||²_∞ · ∫_{-∞}^t (t-τ)^{-1/2} dτ = ∞
```

The integral DIVERGES. The ancient condition (integrating from -∞) makes the integral infinite in L^∞.

**This is why L^∞ is the wrong space.** The fixed-point argument needs a space where the integral converges. Classical theory uses spaces like L^∞_t L^3_x or L^∞_t BMO^{-1}_x, where the heat kernel decay is stronger.

### The gap, precisely stated

For bounded ancient solutions in L^∞, the integral in (★★) diverges in the L^∞ norm. The Liouville conjecture is equivalent to showing this integral MUST be zero despite not being absolutely convergent in L^∞.

**The oscillation must cancel the singularity.** The integral ∫_{-∞}^t (t-τ)^{-1/2} · f(τ) dτ converges if f decays fast enough as τ → -∞, even if the kernel is singular. For the NS problem, f(τ) = P∇·(w⊗w)(τ). If w is an ancient solution, does ||w(τ)||_∞ → 0 as τ → -∞?

If yes: the integral converges, the fixed-point equation becomes well-posed, and for small enough asymptotic norm, the only fixed point is w = 0. This would prove Liouville.

**The question reduces to:** do bounded ancient NS solutions become small as t → -∞?

This connects to Mountain 5 (dimension reduction) and to the backward energy inequality (Attempt 005 in the gap.md). If there's a monotone energy functional that forces ||w(t)||_∞ → 0 as t → -∞, the proof closes via (★★).

## Key finding

**The Liouville conjecture is equivalent to: bounded ancient NS solutions become asymptotically trivial as t → -∞.**

This is a DECAY claim, not a rigidity claim. It says: the solution can't maintain a non-trivial bounded profile for infinite backward time. The diffusion must eventually win over the nonlinearity.

**Why this might be true:** the heat equation dissipates all non-constant modes exponentially. The NS nonlinearity (u · ∇)u transfers energy between modes but doesn't CREATE energy (it's energy-conserving in the inviscid limit). So diffusion is strictly dissipative and the nonlinearity is energy-neutral. Over infinite time, dissipation should win.

**Why this might be false:** the nonlinearity can TRANSFER energy from large scales (which diffuse slowly) to small scales (which diffuse fast). If this transfer is fast enough, it can sustain a non-trivial profile indefinitely — the energy cascading from large to small scales is replenished at the large scales by the inverse cascade (in 3D, the vortex stretching). Whether this balance can be maintained for an ANCIENT (infinite backward time) solution is the open question.

## Next steps

- **Attempt 003:** make the backward decay argument rigorous. Define E(t) = ||w(t)||² in some weighted norm and show dE/dt ≥ c · E (so E decays BACKWARD in time). The weight must be chosen to make the nonlinear term energy-neutral.
- **For numerics:** compute ||w(τ)|| for the Beltrami flow (which is ancient but unbounded — the unboundedness comes from the exponential growth, and the question is whether the GROWTH is essential or whether there exist bounded ancient solutions that are not growing).

## Coupled observation from this fire

The numerical instance's `frequency_function.md` showed N(r) ≈ 1 with non-monotonicity localized near the vortex core (r ≈ 3). The deviation is 0.04%. This tells the theory track: **the frequency function approach almost works — the NS nonlinearity produces tiny corrections to the harmonic behavior.** The question is whether "almost works" can be made "works" via the ancient condition providing the missing 0.04%.

The answer from this attempt: the ancient condition doesn't directly fix the frequency function, but it DOES provide a different structural property — the fixed-point equation (★★) — that reduces Liouville to a DECAY claim. Decay + frequency function might combine: if ||w(t)|| → 0 as t → -∞, then the solution becomes "more harmonic" in the distant past, and the frequency function becomes "more monotone." The question is whether the feedback loop between decay and monotonicity closes.
