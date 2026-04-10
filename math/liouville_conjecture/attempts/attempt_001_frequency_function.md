# attempt_001 — Frequency Function with NS-Adapted Weight

**Date:** 2026-04-09
**Track:** Theory (Even)
**Mountain:** 1 (Frequency function / Almgren monotonicity)
**Status:** In progress. The standard Almgren frequency fails. Three modifications proposed; the pressure-weighted variant is the most promising.

## The standard Almgren frequency function

For a function u on R^n, define:
```
D(r) = ∫_{B_r} |∇u|² dV
H(r) = ∫_{∂B_r} |u|² dS
N(r) = r · D(r) / H(r)
```

**Almgren's theorem (1979):** if u is harmonic (Δu = 0), then N(r) is monotone non-decreasing in r. This immediately implies the Liouville theorem for harmonic functions: if u is bounded and harmonic on R^n, then N(r) is bounded, monotonicity forces N(r) → const, and the only possibility is N ≡ 0 (u is constant).

The frequency function works because the equation Δu = 0 creates a precise cancellation in the derivative dN/dr. All error terms vanish for harmonic functions.

## Why it fails for Navier-Stokes

For NS, u satisfies ∂u/∂t + (u · ∇)u = Δu - ∇p. The frequency function at a fixed time t (treating u(·, t) as an elliptic object) gives:

```
dN/dr = (good terms from Δu) + (error from (u · ∇)u) + (error from ∇p) + (error from ∂u/∂t)
```

### Error term 1: the nonlinear transport (u · ∇)u

This contributes to D'(r) a term:
```
∫_{B_r} ∇u : ∇((u · ∇)u) dV
```

By integration by parts and the Cauchy-Schwarz inequality:
```
|error₁| ≤ C · M · r · ∫_{B_r} |∇²u|² dV + C · M · ∫_{∂B_r} |∇u|² dS
```

where M = sup |u|. The first term involves second derivatives (which we don't control independently of r), and the second contributes to dD/dr with the WRONG sign.

### Error term 2: the pressure ∇p

The pressure satisfies -Δp = ∂ᵢ∂ⱼ(uᵢuⱼ), so ∇p is determined by u but NOT pointwise bounded by u. For bounded u, ∇p ∈ BMO(R³), which means:

```
∫_{B_r} |∇p|² dV ≤ C(M) · r³ · (1 + log r)²  (at best)
```

This logarithmic growth is too slow to absorb but too fast to ignore.

### Error term 3: the time derivative ∂u/∂t

For ancient solutions, u is smooth for all t ≤ 0, so ∂u/∂t is bounded. But it contributes an additional term to dN/dr that has no sign.

### Net effect

The errors make dN/dr have NO definite sign. N(r) can increase or decrease, and there is no monotonicity theorem for the standard Almgren frequency on NS solutions.

## Modification 1: Pressure-weighted frequency

**Idea:** absorb the pressure error by modifying H(r) to include the pressure.

Define:
```
H̃(r) = ∫_{∂B_r} (|u|² + 2p) dS
Ñ(r) = r · D(r) / H̃(r)
```

**Why this might work:** the NS equations can be written as:
```
∂u/∂t = Δu - ∇(|u|²/2 + p) + ω × u
```

The term |u|²/2 + p is the Bernoulli function. It satisfies its own elliptic equation:
```
-Δ(|u|²/2 + p) = |ω|² - |S|²  (where S is the strain rate)
```

By including p in H̃, the pressure gradient in the frequency derivative cancels with the transport term's gradient part:
```
(u · ∇)u = ∇(|u|²/2) + ω × u
```

The gradient part ∇(|u|²/2) combines with ∇p to give ∇(|u|²/2 + p), and the Bernoulli function's elliptic equation might give the right sign.

**The remaining error after this modification:** the ω × u term (the rotational part of the nonlinearity). This term is orthogonal to u in pointwise sense (since (ω × u) · u = 0), which gives:

```
∫_{∂B_r} (ω × u) · u dS = 0  for all r
```

This is promising — the rotational nonlinearity might not contribute to H̃'(r) at all!

**What needs to be checked:**
1. Is H̃(r) > 0? (The pressure p can be negative, so |u|² + 2p might be negative somewhere.) If H̃ changes sign, the frequency function is undefined.
2. Does the Bernoulli function's equation (-Δ(|u|²/2 + p) = |ω|² - |S|²) give the right sign? The term |ω|² - |S|² has no definite sign in general (for irrotational flow, ω = 0 and it's negative; for solid-body rotation, |ω|² > |S|² and it's positive).
3. Does the time derivative ∂u/∂t contribute a controllable error to dÑ/dr?

**Prediction for the numerical instance:** compute H̃(r) = ∫_{∂B_r} (|u|² + 2p) dS on the Burgers vortex. If H̃(r) > 0 for all r, the modification is at least well-defined. Report the sign profile and the ratio H̃(r)/H(r).

## Modification 2: Strain-weighted Dirichlet integral

**Idea:** instead of ∫|∇u|², use the strain integral ∫|S|² where Sᵢⱼ = (∂ᵢuⱼ + ∂ⱼuᵢ)/2.

Define:
```
D_S(r) = ∫_{B_r} |S|² dV
N_S(r) = r · D_S(r) / H(r)
```

**Why this might work:** the energy dissipation in NS is 2ν ∫|S|² (not ∫|∇u|²). The strain tensor is the mechanically relevant quantity. For divergence-free fields, |∇u|² = |S|² + |ω|²/2 (Korn-type identity), so switching from ∇u to S changes the frequency function by a term involving enstrophy.

The vortex stretching term in the vorticity equation involves the STRAIN applied to vorticity: (ω · ∇)u = Sω (the antisymmetric part of ∇u acting on ω vanishes). So the strain is the object that couples to vorticity.

**The hope:** the strain-based frequency might have a monotonicity property because the strain is the "right" gradient for the NS energy structure.

**What needs to be checked:** compute dN_S/dr and see whether the error terms from the nonlinearity have a better structure than in the standard case.

## Modification 3: Vorticity frequency function

**Idea:** work with ω = curl u instead of u. Define:
```
D_ω(r) = ∫_{B_r} |∇ω|² dV
H_ω(r) = ∫_{∂B_r} |ω|² dS
N_ω(r) = r · D_ω(r) / H_ω(r)
```

**Why this might work:** the pressure disappears entirely from the vorticity equation:
```
∂ω/∂t + (u · ∇)ω = Δω + (ω · ∇)u
```

No ∇p term. This eliminates error term 2 completely. The remaining error is from the stretching term (ω · ∇)u = Sω.

**The remaining error after this modification:**
```
∫_{B_r} ∇ω : ∇(Sω) dV
```

This involves ∇S · ω (which is ∇²u · ω) and S · ∇ω. The S · ∇ω term has a chance of having a sign, because S is symmetric and the bilinear form ⟨Sξ, ξ⟩ is bounded by |S| · |ξ|². For bounded ancient solutions, |S| is bounded (by parabolic regularity), so:

```
|error₃| ≤ C(M) · ∫_{B_r} |∇ω|² dV = C(M) · D_ω(r)
```

This error is proportional to D_ω itself! That means:
```
dN_ω/dr ≥ (good terms) - C(M) · N_ω(r)
```

This is a GRONWALL-type inequality, not a monotonicity, but it gives:
```
N_ω(r) ≤ N_ω(r₀) · e^{C(M)(r-r₀)}
```

For bounded solutions, this means N_ω grows at most exponentially in r. Combined with the boundedness of ω (which gives H_ω(r) ≤ C · r²), this constrains D_ω(r) ≤ C · r³ · e^{C·r}. This is NOT enough for Liouville (we'd need polynomial growth, not exponential), but it's a STARTING POINT.

**The question:** can the Gronwall constant C(M) be improved? For the specific structure of Sω (traceless symmetric matrix times a divergence-free vector), the constant might be smaller than the generic bound. If C(M) = 0 for some special class, we get monotonicity.

**Prediction for the numerical instance:** compute N_ω(r) on the Burgers vortex. Plot log N_ω(r) vs r. If the growth is sub-exponential in practice, the Gronwall bound is not tight and there may be room for improvement.

## Observation from the numerical instance (coupled observation)

The numerics instance already found (in `results/known_ancient_solutions.md`):

> "Every known non-trivial ancient NS solution is UNBOUNDED... Any proof must be indirect — via monotone invariants, contradictions, or exclusion arguments... The Poincaré parallel is exact: Perelman didn't find ancient Ricci flows by construction; he proved they must be solitons via five monotone detectors."

This confirms the frequency-function direction: **we need a monotone (or almost-monotone) invariant that detects the trivial solution as its unique fixed point.** The frequency function is the classical tool for this. The question is which modification makes it work for NS.

## Ranking of the three modifications

1. **Modification 3 (vorticity)** — most promising. Eliminates pressure entirely. Error is Gronwall-type, which is a real bound. The question is whether the Gronwall constant can be driven to zero.
2. **Modification 1 (pressure-weighted)** — elegant but risky. Requires H̃ > 0, which is not guaranteed. The ω × u orthogonality is genuinely helpful.
3. **Modification 2 (strain-weighted)** — mechanically motivated but hasn't been worked out. The strain-vorticity coupling might produce cancellations or might make things worse.

## Next steps

- **For the numerics instance:** compute N_ω(r) on Burgers vortex. Plot log N_ω vs r. Also compute H̃(r) = ∫(|u|² + 2p) on spheres for Burgers — check sign.
- **For me (theory):** work out the full dN_ω/dr calculation rigorously. Identify exactly where the Gronwall constant comes from and whether the (ω · ∇)u = Sω structure gives a tighter bound than |S| · |ω|.
- **Attempt 002:** if the vorticity frequency function gives a tight enough bound, try to combine it with the ancient condition (which should give additional structure as t → -∞).

## Sky bridges

- **Poincaré reconstruction:** the numerical instance's observation that Perelman used five monotone detectors for solitons parallels exactly what we need — a monotone detector for the trivial solution.
- **NS certifier:** the certifier proves c(N) < 3/4, which excludes Type I. The frequency function approach, if successful, would prove Liouville, which excludes Type II. The two proofs are complementary halves.
- **Yang-Mills:** the Faddeev-Niemi topological mass gap approach in YM also uses energy monotonicity arguments. If the NS frequency function works, the same structure might apply to the YM mass gap.
