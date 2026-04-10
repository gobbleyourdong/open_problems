# The Liouville Conjecture for 3D Navier-Stokes

## Formal Statement

**Conjecture (Liouville for NS):** Let u : R³ × (-∞, 0] → R³ be a bounded ancient mild solution to the incompressible Navier-Stokes equations:

```
∂u/∂t + (u · ∇)u = Δu - ∇p
∇ · u = 0
sup_{x ∈ R³, t ≤ 0} |u(x,t)| ≤ M < ∞
```

Then u ≡ const (and therefore u ≡ 0 by the divergence-free condition on R³).

Equivalently: the only bounded ancient solution to NS on R³ is the trivial one.

## Why This Problem Exists

This is the **quantum mountain** of Navier-Stokes regularity. Every proof route to the Clay Millennium Prize converges here:

| Proof route | Chain to regularity | Where Liouville enters |
|---|---|---|
| Key Lemma c(N) < 3/4 | c(N) certified → Type I excluded → Seregin → regularity | Seregin's theorem requires Liouville to close |
| Energy methods (CKN) | Partial regularity → extend to full | Extension uses blow-up limits = ancient solutions |
| Scaling / blow-up | Rescale near singularity → limit is ancient solution | Ancient solution must be trivial |
| Mild solutions (Fujita-Kato) | Local existence → global → control blowup rate | Blowup control → Type I → Seregin → Liouville |
| Profile decomposition | Concentrate profiles → classify | Profile classification needs Liouville for limits |

Proving Liouville would close NS regularity simultaneously from ALL five mountains. Disproving it would construct a singularity.

## What Is Known (the scaffold)

### Proved cases (Liouville holds)

| Case | Result | Authors | Year |
|---|---|---|---|
| **2D** | Liouville holds | Trivial (2D NS is globally regular) | — |
| **Linear Stokes** | Liouville holds | Classical (linear parabolic Liouville) | — |
| **Axisymmetric, no swirl** | Liouville holds | Koch, Nadirashvili, Seregin, Šverák | 2009 |
| **One component ≡ 0** | Liouville holds | Lei, Zhang | 2011 |
| **u ∈ L^∞_t L^3_x** | Regularity (implies Liouville for this class) | Escauriaza, Seregin, Šverák | 2003 |
| **Self-similar** | Liouville holds for self-similar ancient solutions | Nečas, Růžička, Šverák (forward); Tsai (backward) | 1996, 1998 |
| **Axisymmetric with decay** | Liouville holds if |u| → 0 at spatial infinity | Koch et al. (strengthened) | 2009+ |
| **Small solutions** | Liouville holds if M is small enough | Perturbative (contraction in critical spaces) | Various |
| **Finite energy** | Liouville holds if ∫|u|² < ∞ | Energy equality + backward uniqueness | Classical |

### What each proved case tells us

**Axisymmetric no-swirl (KNSS 2009):** This is the deepest result. The proof uses:
1. Ancient solution + axisymmetry → the vorticity ω = curl u satisfies a scalar equation
2. The scalar vorticity equation has a maximum principle (thanks to no-swirl: the stretching term vanishes)
3. Maximum principle + boundedness → |ω| is bounded → decay estimates → ω ≡ 0 → u ≡ 0

The key structural feature: **no swirl kills the vortex stretching term.** In full 3D, the stretching term (ω · ∇)u is what makes NS hard. It can amplify vorticity without bound. Removing it (axisymmetric no-swirl) makes the equation parabolic-scalar, and Liouville follows from classical PDE theory.

**ESŠ 2003 (L³ regularity):** Uses backward uniqueness for parabolic equations. If u ∈ L^∞_t L³_x, then a rescaling argument + compactness shows that any blowup limit is a bounded ancient solution in L³, and backward uniqueness forces it to be zero. This proves regularity for the L³ class WITHOUT proving Liouville for the general bounded class — it uses a stronger assumption.

**Self-similar (Tsai 1998):** Self-similar ancient solutions have the form u(x,t) = λ(t) U(λ(t) x) for some profile U. The self-similarity constrains the solution so tightly that Liouville follows from an ODE analysis of the profile.

### What is NOT known (the open case)

**General bounded ancient solutions in 3D with no symmetry, no decay assumption, no integrability condition, no self-similarity.**

The solution is only assumed to be:
- Smooth (mild solution)
- Divergence-free
- Bounded: |u(x,t)| ≤ M for all (x,t) ∈ R³ × (-∞, 0]
- Ancient: defined for all t ≤ 0

No other structure is assumed. THIS is what needs to be proved trivial.

## The Structural Difficulty

### Why the 3D case is hard (the vortex stretching term)

The vorticity equation in 3D:

```
∂ω/∂t + (u · ∇)ω = Δω + (ω · ∇)u
                              ^^^^^^^^
                              vortex stretching
```

In 2D, ω is a scalar and (ω · ∇)u ≡ 0 (vorticity is perpendicular to the flow plane). The equation becomes a scalar advection-diffusion equation with a maximum principle. Liouville is trivial.

In 3D, ω is a vector and (ω · ∇)u is the stretching term. It can amplify vorticity exponentially. There is no maximum principle for the vorticity magnitude. The equation is fundamentally different from its 2D counterpart.

### Why bounded is not enough (the pressure problem)

Boundedness of u does NOT imply boundedness of ∇p. The pressure satisfies:

```
-Δp = ∂²(u_i u_j)/∂x_i ∂x_j
```

For bounded u, the right side is bounded, but the Laplacian inverse on R³ maps L^∞ to BMO, not to L^∞. So ∇p can be unbounded even when u is bounded. This means the acceleration ∂u/∂t = Δu - (u·∇)u - ∇p is not obviously bounded.

### Why ancient is crucial

Ancient solutions are defined for all t ≤ 0. This is an INFINITE time condition. For finite-time existence, bounded solutions are easy (they're smooth by parabolic regularity). The difficulty is that an ancient solution has had infinite time to develop complex spatial structure.

The pressure non-locality + infinite time + 3D stretching together prevent the standard tools (maximum principle, energy estimates, backward uniqueness in L³) from reaching the general case.

## The Five Mountains for Liouville

### Mountain 1: Frequency Function / Almgren Monotonicity

**Idea:** Define a frequency function N(r) = r · D(r) / H(r) where D is a Dirichlet-type integral and H is an L²-type integral on spheres. If N(r) is monotone in r, then the growth rate of u is controlled, and bounded ancient solutions must be constant.

**What's known:** Almgren monotonicity works for:
- Harmonic functions (classical Liouville)
- Solutions to elliptic equations with Lipschitz coefficients
- Caloric functions (solutions to the heat equation)

**The gap:** For NS, the nonlinearity (u · ∇)u destroys the clean monotonicity. The frequency function picks up error terms proportional to |u|² · |∇u|, which cannot be absorbed without additional assumptions (like smallness or symmetry).

**What would close it:** a modified frequency function that accounts for the nonlinear transport, or a transformation that removes the transport term.

### Mountain 2: Backward Uniqueness Extension

**Idea:** ESŠ (2003) proved backward uniqueness for NS in L³. Extend this to L^∞.

**What's known:** Backward uniqueness says: if u(·, 0) = 0 and u is an ancient solution, then u ≡ 0. This is proved using Carleman inequalities. The L³ case works because L³ is a critical space for NS scaling.

**The gap:** L^∞ is supercritical. The Carleman inequality approach requires the solution to be in a critical or subcritical space. In L^∞, the Carleman weight functions don't produce the right decay.

**What would close it:** either a new Carleman inequality that works in L^∞, or a way to show bounded ancient solutions are automatically in L³ (which would reduce to the known case).

### Mountain 3: Energy Methods / Gallagher-Koch-Planchon

**Idea:** Show that bounded ancient solutions have additional integrability (e.g., finite Dirichlet integral ∫|∇u|² < ∞), which then implies Liouville via energy estimates.

**What's known:** Galdi (2011) showed that bounded solutions on R³ with finite Dirichlet integral are constant. The question is whether bounded ancient solutions AUTOMATICALLY have finite Dirichlet integral.

**The gap:** the parabolic regularity of NS gives local estimates on ∇u, but the global integral ∫_{R³} |∇u|² can be infinite even for bounded u. There's no known mechanism that forces finite energy from boundedness alone on R³.

**What would close it:** a global energy inequality for ancient solutions that shows the Dirichlet integral cannot grow without bound as t → -∞.

### Mountain 4: Symmetry Reduction + Perturbation

**Idea:** Start from the proved cases (axisymmetric no-swirl, self-similar) and perturb. Show that Liouville is stable under perturbation — if it holds for a nearby class, it holds for the general class.

**What's known:** KNSS proved Liouville for axisymmetric no-swirl. The swirl component satisfies its own equation. If the swirl is "small" in some sense, the perturbative approach should work.

**The gap:** "small swirl" has been studied (Lei-Navas-Zhang, Pan, etc.) but the results require the swirl to decay at infinity or satisfy integrability conditions. General bounded swirl is not covered.

**What would close it:** a stability estimate showing that the KNSS proof degrades gracefully as swirl is added, with the degradation controlled by the boundedness constant M.

### Mountain 5: Dimension Reduction / Slicing

**Idea:** Reduce the 3D problem to a family of 2D problems by slicing. If each slice satisfies a 2D Liouville theorem, the full solution is constant.

**What's known:** 2D Liouville is trivial. If a 3D solution has ANY direction of translation invariance (u(x₁, x₂, x₃, t) independent of x₃), then it reduces to a 2D solution and Liouville holds.

**The gap:** general 3D solutions have no translation invariance. The slicing approach requires showing that bounded ancient solutions develop approximate translation invariance in at least one direction, or that the variation in the "worst" direction is controlled.

**What would close it:** a rigidity result showing that bounded ancient solutions on R³ must have a direction of slow variation (possibly using the pressure equation and the divergence-free condition).

## Connection to the SOS Certifier

The NS certifier (currently at N=12, 9/13, floor ≥ 19.30) is building the numerical fortress that says:

```
c(N) = sup S²e / |ω|² < 3/4 for all N
```

This excludes Type I blowup. If a singularity forms, it must be Type II (blowup rate faster than (T-t)^{-1/2}). Type II blowup limits are bounded ancient solutions on R³. So:

```
c(N) < 3/4 for all N
    → Type I excluded (Seregin 2012)
    → any blowup is Type II
    → Type II blowup limit is a bounded ancient solution
    → IF Liouville holds: that solution is trivial → contradiction → no blowup
    → NS regularity
```

The certifier and this problem are two halves of the same proof. The certifier handles one side (Type I exclusion). Liouville handles the other (Type II impossibility). Both are needed.

## Status

OPEN. The quantum mountain of NS regularity. Five mountains identified but none yet climbed beyond base camp in the general case. The strongest partial result (KNSS 2009, axisymmetric no-swirl) gives a template for what a full proof might look like, but the extension to general 3D requires handling vortex stretching, which is the fundamental difficulty of 3D fluid mechanics.

See `gap.md` for the precise obstruction analysis.
