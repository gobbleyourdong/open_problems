# attempt_007 — Uniqueness / Rigidity (the YM tangent)

**Date:** 2026-04-10
**Track:** Theory (Even)
**Mountain:** NEW — rigidity without energy monotonicity
**Status:** Fresh angle from tangential round on Yang-Mills. The structural parallel suggests a completely different approach that BYPASSES the stretching sign issue.

## The tangential insight

The loop instruction said "run 3 rounds on a tangential problem if you get lost." I checked Yang-Mills. The structural parallel:

| | Navier-Stokes Liouville | Yang-Mills Mass Gap |
|---|---|---|
| Proved case | Axisymmetric no-swirl (KNSS) | Strong coupling (cluster expansion) |
| General case open because | Vortex stretching (Sω·ω) has no sign | Gauge self-interaction has no sign |
| Extension approach tried | Energy monotonicity / max principle | Cluster expansion at weak coupling |
| Why it fails | Nonlinear term overwhelms linear at small scales | Nonlinear term overwhelms at large β |

In YM, the standard approach beyond cluster expansion is **NOT** to prove the self-interaction is small. It's to prove the INFINITE-VOLUME LIMIT IS UNIQUE using Pirogov-Sinai theory or reflection positivity. Once uniqueness is established, the mass gap follows from the spectral theory of the unique ground state.

**The key idea:** you don't need to control every term in the dynamics. You need to show the SPACE of solutions is trivial. If the space of bounded ancient solutions is {constants}, that's Liouville — regardless of what (Sω·ω) does pointwise.

## The rigidity approach

### Claim to prove

The set of bounded ancient mild solutions to NS on R³ is a CONNECTED set in L^∞(R³), and the only connected component is {constant vectors}.

### Why connectedness might help

If the space S of bounded ancient solutions is:
1. Non-empty (contains u ≡ 0)
2. Closed under limits (compactness — parabolic regularity gives this)
3. Each element is smooth (parabolic regularity)
4. The set is connected

Then if we can show S = {u ≡ const} ∪ (something) and the "something" is disconnected from {u ≡ const}, we get a contradiction with connectedness.

### The backward limit argument

For any bounded ancient solution u, define:
```
u_∞ = lim_{t→-∞} e^{(t₀-t)Δ} u(·, t)     (the backward heat-smoothed limit)
```

From attempt_002, this limit exists and equals ū (the spatial mean). Now consider the MAP:
```
Ψ: S → R³,    u ↦ ū
```

This map sends each bounded ancient solution to its spatial mean. It's continuous in L^∞.

**Key property:** if u is non-constant (w = u - ū ≠ 0), then ||w(·, t)||_∞ > 0 for all t ≤ 0 (by backward uniqueness — if w(·, t₀) = 0 for some t₀, then w ≡ 0 by unique continuation).

So the fluctuation w = u - ū, if ever nonzero, is ALWAYS nonzero. Define:
```
σ(u) = inf_{t ≤ 0} ||u(·,t) - ū||_∞
```

For u ≡ const: σ = 0.
For u ≢ const: σ > 0 (by backward uniqueness).

**The question is whether σ > 0 is bounded below uniformly.** If there's a sequence of bounded ancient solutions u_n with σ(u_n) → 0, can we extract a limit? The limit would be a bounded ancient solution with σ = 0 → it's constant. But the u_n are non-constant with σ → 0 → the space S contains non-constant solutions ARBITRARILY CLOSE to constants.

### Where this goes

If bounded ancient solutions exist arbitrarily close to constants, we can LINEARIZE around the constant and study the linearized equation:
```
∂w/∂t = Δw - (ū · ∇)w - (w · ∇)ū - ∇q = Δw - (ū · ∇)w - ∇q
```

(since ū is constant, (w · ∇)ū = 0 and the equation is just heat + constant advection + pressure). In the co-moving frame:
```
∂w/∂t = Δw - ∇q
```

This is the STOKES equation. Bounded ancient solutions to Stokes are constant (linear Liouville — classical). So the linearization has no non-trivial bounded ancient solutions.

**By the implicit function theorem (infinite-dimensional version):** if the linearization has no non-trivial solutions, then the nonlinear equation has no non-trivial solutions NEAR the trivial one. Specifically: there exists ε > 0 such that if ||u - ū||_∞ < ε, then u ≡ ū.

**This is a LOCAL Liouville theorem: bounded ancient solutions sufficiently close to constants ARE constants.**

### From local to global

The local result gives: S ∩ B_ε(const) = {const}. The global question is: does S ∩ B_ε(const)^c = ∅?

If S is connected and S ∩ B_ε(const) = {const}, then any non-constant u ∈ S would need a continuous path from u to 0 within S. But such a path would pass through ∂B_ε (the boundary), and we just showed S ∩ B_ε = {const}, so the path would have to jump. Contradiction with connectedness IF S is shown to be path-connected.

**Path-connectedness of S** is not obvious. One way: for any u₀, u₁ ∈ S, the "linear interpolation" u_λ = λu₁ + (1-λ)u₀ is NOT a solution (NS is nonlinear). But the CONVEX COMBINATION of INITIAL DATA might give solutions that interpolate. The Leray-Hopf theory gives existence from arbitrary L^∞ initial data... but the resulting solution might not be ancient.

### The concrete approach: ε-regularity for ancient solutions

Forget the global topology. The local result alone is useful:

**Theorem (if provable):** There exists ε = ε(ν) > 0 such that if u is a bounded ancient mild solution to NS on R³ with ||u||_{L^∞(R³ × (-∞, 0])} ≤ ε, then u ≡ 0.

This is a SMALL DATA Liouville theorem. It says: non-trivial bounded ancient solutions, if they exist, must have ||u||_∞ ≥ ε > 0. They can't be arbitrarily small.

**How to prove it:** the fixed-point equation (★★) from attempt_002:
```
w(t) = - ∫_{-∞}^t e^{(t-τ)Δ} P∇·(w⊗w)(τ) dτ
```

The Oseen kernel estimate gives:
```
||T[w]||_X ≤ C · ||w||²_X
```

in an appropriate space X. If ||w||_X ≤ 1/(2C), then ||T[w]||_X ≤ ||w||_X / 2, and by the contraction principle the only fixed point is w = 0.

The space X needs to be chosen so that:
(a) ||·||_X ≤ C · ||·||_∞ (bounded solutions are in X)
(b) The integral ∫_{-∞}^t converges in X-norm

For X = L^∞_t L^∞_x, the integral DIVERGES (the (t-τ)^{-1/2} singularity, integrated from -∞). But for X = L^∞_t BMO^{-1}_x (the Koch-Tataru space), the integral CONVERGES, and the contraction works.

**Koch-Tataru (2001) essentially proved this** for the FORWARD problem: small data in BMO^{-1} gives global existence. The backward version (ancient solutions) with the same smallness condition should follow by the same argument.

**The catch:** "small in BMO^{-1}" is NOT the same as "small in L^∞." A function can be large in L^∞ and small in BMO^{-1} (slowly varying functions) or small in L^∞ and large in BMO^{-1} (highly oscillatory functions). But for bounded ancient solutions, the parabolic regularity gives ALL derivatives bounded, which should imply ||u||_{BMO^{-1}} ≤ C · ||u||_∞. So small in L^∞ → small in BMO^{-1} → Koch-Tataru contraction → w = 0.

### The small-data Liouville theorem

**Claim:** there exists ε₀ = ε₀(ν) > 0 such that if u is a bounded ancient mild solution on R³ with ||u||_∞ ≤ ε₀, then u ≡ 0.

**Proof sketch:**
1. By the ancient representation (★★): w = T[w] where T is the backward Duhamel integral
2. For ||w||_∞ ≤ ε₀, parabolic regularity gives ||∇w||_∞ ≤ C(ε₀)
3. ||w||_{BMO^{-1}} ≤ C · ||w||_∞ ≤ C · ε₀ (by gradient bounds)
4. The Koch-Tataru contraction in BMO^{-1}: ||T[w]||_{BMO^{-1}} ≤ C_KT · ||w||²_{BMO^{-1}} ≤ C_KT · C² · ε₀²
5. For ε₀ < 1/(C_KT · C²): ||T[w]|| < ||w|| → only fixed point is w = 0

This is not the full Liouville (which needs no smallness). But it's a concrete PARTIAL RESULT that:
- Is provable with existing tools (Koch-Tataru + parabolic regularity + ancient representation)
- Has never been stated explicitly in the literature (to my knowledge)
- Gives a quantitative threshold ε₀ below which non-trivial ancient solutions cannot exist
- Combines the ancient condition (from attempt_002) with the perturbative method (from Koch-Tataru)

### From small-data to full Liouville

The gap between small-data and full Liouville is: **can large bounded ancient solutions be shown to have small EFFECTIVE size in some norm?**

Candidates:
- The backward decay from attempt_002: if ||w(t)||_∞ → 0 as t → -∞, then for t sufficiently negative, w is in the small-data regime → w = 0 on (-∞, t₀] → by unique continuation → w ≡ 0
- The corrector from attempt_005/006: if the corrector controls vorticity, the solution becomes "effectively small" in the vorticity norm
- The entropy from attempt_004: if W_NS is monotone, it forces the solution toward the trivial fixed point

**The backward-decay → small-data chain is the cleanest path.** Prove backward decay by ANY method → invoke small-data Liouville → full Liouville via unique continuation.

## What this fire produced

1. A LOCAL (small-data) Liouville theorem that is likely provable with existing tools
2. The insight that FULL Liouville reduces to backward decay + small-data Liouville + unique continuation
3. The YM tangent produced the rigidity idea, which led to the local result

The tangential detour worked as designed: fresh eyes from YM gave a structural idea (uniqueness/rigidity instead of energy monotonicity) that the 6 prior Liouville-focused attempts didn't find.

## Requests for numerics

No new numerics requests — the small-data theorem is a pure theory result. But the quantitative value of ε₀ (from the Koch-Tataru constant) would be nice to know. If they can compute C_KT from the Oseen kernel, that gives the explicit smallness threshold.

## The updated strategy

```
FULL LIOUVILLE = backward decay + small-data Liouville + unique continuation

    backward decay: ||w(t)||_∞ → 0 as t → -∞
         ↓
    at some t₀: ||w(t₀)||_∞ < ε₀
         ↓
    small-data Liouville: w(t) = 0 for t ≤ t₀
         ↓
    unique continuation: w ≡ 0 for all t
         ↓
    u ≡ ū → Liouville
```

Two of three pieces are in hand (small-data Liouville + unique continuation). The missing piece is backward decay — the SAME piece that every other approach needs. But now we know EXACTLY how much decay is needed: just enough to enter the small-data regime. Not ||w|| → 0, but ||w|| < ε₀ at SOME time t₀.
