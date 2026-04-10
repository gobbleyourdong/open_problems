# Liouville Conjecture — The Gap

> **Updated after 8 theory attempts + 11 numerics scripts (Apr 9-10, 2026)**
> Previous version focused on the 5 mountains. This version incorporates
> the decomposition discovered through the campaign.

## The single sentence (UPDATED)

**Full Liouville = backward entry into the small-data regime + small-data Liouville + unique continuation. Two of three pieces are in hand. The remaining gap is: does every bounded ancient solution ever become small enough to enter the perturbative regime?**

## The decomposition

```
FULL LIOUVILLE = (1) + (2) + (3)

(1) Backward entry: ∃ t₀ ≤ 0 such that ||u(t₀) - ū||_∞ < ε₀
    STATUS: ★★★ THE GAP ★★★

(2) Small-data Liouville: ||u||_∞ < ε₀ → u ≡ 0
    STATUS: PROOF SKETCH COMPLETE (attempt_008)
    ε₀ = ν / (8 · C_Oseen), explicit

(3) Unique continuation: if w(·, t₀) = 0 then w ≡ 0
    STATUS: KNOWN (Escauriaza-Seregin-Šverák framework)
```

The chain: if (1) holds at some t₀, then (2) gives w = 0 on (-∞, t₀], then (3) extends to w ≡ 0 on (-∞, 0], giving u ≡ ū (Liouville).

## The original gap (still true, now contextualized)

**We cannot control the vortex stretching term (ω · ∇)u for bounded ancient solutions on R³ without assuming symmetry, decay, integrability, or smallness.**

Every proved case of Liouville for NS works by either:
(a) Killing the stretching term structurally (axisymmetric no-swirl: it vanishes identically), or
(b) Working in a function space where the stretching term is subcritical (L³: the scaling makes it controllable), or
(c) Assuming self-similarity (reduces to an ODE where stretching is explicit)

The general case has stretching that is:
- Present (not killed by symmetry)
- Supercritical (L^∞ is above the critical scaling)
- Non-self-similar (no ODE reduction)

All three at once is what makes the problem open.

## What the gap looks like from each mountain

### Mountain 1 (Frequency function)

**Gap:** the frequency function N(r) for NS picks up nonlinear error terms:

```
dN/dr = (good terms) + ∫ (u · ∇)u · (something involving u and ∇u)
```

The error term has the wrong sign and the wrong scaling. For Almgren monotonicity to work, the error must be either:
- Absorbed into the good terms (requires smallness of u — fails for large M)
- Shown to have a sign (requires structure in the nonlinearity — not known)
- Transformed away (requires a clever change of variables)

**Specific obstruction:** if u is bounded by M, the error term is O(M · r² · D(r)), but the good term is only O(r · D'(r)). For large M, the error dominates.

**What would break through:** a frequency function adapted to the NS nonlinearity. Possible candidates:
- Weight the integrals by the pressure (absorbs part of the nonlinearity)
- Use the stream function formulation (reduces the order of the nonlinearity)
- Work with vorticity ω instead of velocity u (different error structure)

### Mountain 2 (Backward uniqueness)

**Gap:** the Carleman inequality used by ESŠ has the form:

```
∫ e^{2τφ} |Lv|² ≥ C ∫ e^{2τφ} (τ³|v|² + τ|∇v|²)
```

where L is the linearized operator and φ is a weight function. For L³ solutions, the weight φ can be chosen to match the NS scaling. For L^∞ solutions, no known weight works because:
- L^∞ is supercritical: the natural weight grows too fast
- The pressure term ∇p is not in L² when u ∈ L^∞ (it's in BMO)
- The bilinear form (u · ∇)v in the linearization has the wrong scaling for the Carleman weight

**Specific obstruction:** the inequality requires ∫ e^{2τφ} |∇p|² < ∞, but for bounded u, ∇p ∈ BMO and the exponential weight can make this integral diverge.

**What would break through:**
- A Carleman inequality that works with BMO data (not known to exist in the parabolic setting)
- Showing that bounded ancient solutions automatically have ∇p ∈ L²_loc with controlled growth (possible via the ancient condition — infinite backward time might give regularity of the pressure)
- An entirely different approach to backward uniqueness that avoids Carleman inequalities (e.g., logarithmic convexity)

### Mountain 3 (Energy methods)

**Gap:** need to show ∫_{R³} |∇u(x,t)|² dx < ∞ for bounded ancient solutions.

Local parabolic regularity gives:

```
∫_{B_R} |∇u|² ≤ C(M) · R³  for each ball B_R
```

This is a VOLUME growth bound, but it allows the total Dirichlet integral to be infinite as R → ∞. The question is whether the ancient condition forces better decay.

**Specific obstruction:** a bounded function on R³ can have gradient growing like R^{3/2} in the Dirichlet sense. The divergence-free condition constrains this (div u = 0 kills one degree of freedom), but not enough to force finite energy.

**What would break through:**
- An energy identity for ancient solutions that shows ∫|∇u|² is monotone in t → -∞ (and hence bounded)
- A Liouville theorem for the PRESSURE: if p is bounded and solves -Δp = ∂²(uᵢuⱼ)/∂xᵢ∂xⱼ with bounded uᵢuⱼ, is ∇p ∈ L²? (This is itself an open question in potential theory.)
- Using the structure of the NS nonlinearity: (u · ∇)u = ∇(|u|²/2) + ω × u. The gradient part is absorbed by pressure. The remaining ω × u might have better integrability than the full nonlinearity.

### Mountain 4 (Perturbation from axisymmetric)

**Gap:** the KNSS proof for axisymmetric no-swirl uses the SCALAR maximum principle for ω_θ/r (the angular vorticity divided by the radius). In full 3D, there is no scalar quantity with a maximum principle.

**Specific obstruction:** when swirl is added to an axisymmetric flow, the vorticity equation acquires a stretching term proportional to (u_θ)² / r. This term has a definite sign (positive) and drives vorticity amplification. The KNSS proof cannot absorb it.

**What would break through:**
- A maximum principle for a MODIFIED quantity that incorporates the swirl. Candidate: ω_θ/r - f(u_θ/r) for some function f that cancels the stretching.
- Showing that the swirl component u_θ of a bounded ancient solution must decay, even without assuming decay at infinity. (The swirl satisfies its own equation; the ancient condition might force it.)
- A perturbative argument: if ||u_θ||_∞ ≤ ε(M), then the KNSS proof goes through with controlled error. Then show that bounded ancient solutions cannot have large swirl. (This is two hard sub-problems, but each is simpler than the original.)

### Mountain 5 (Dimension reduction)

**Gap:** need to show bounded ancient solutions develop directional structure.

**Specific obstruction:** there is no known rigidity result that forces a bounded divergence-free vector field on R³ to have a preferred direction. The divergence-free condition ∂₁u₁ + ∂₂u₂ + ∂₃u₃ = 0 constrains ONE degree of freedom out of three velocity components. This is not enough for directional rigidity.

**What would break through:**
- A result from the ancient condition: as t → -∞, the solution has had infinite time to "organize." Does infinite backward time force spatial structure? (Analogy: ancient solutions to the heat equation ARE polynomials, which have directional structure.)
- Using the pressure: the pressure equation -Δp = tr(∇u ⊗ ∇u) might force directional correlations in ∇u.
- A spectral argument: the linearized NS operator around a bounded ancient solution might have a spectral gap that forces alignment.

## The Numerics Scaffold

### What the numerical instance should compute

**Priority 1 — Structure of known ancient solutions:**
- Compute all known explicit ancient solutions (Oseen vortex, Lamb-Oseen, Burgers vortex, Beltrami flows) and verify they satisfy Liouville (bounded ones are constant)
- For each, compute: vortex stretching magnitude, frequency function profile, Dirichlet integral growth, pressure gradient behavior
- **Goal:** build intuition for what the vortex stretching term "does" in specific cases

**Priority 2 — Frequency function numerics:**
- Implement the Almgren frequency function N(r) for known solutions
- Compute the error terms from the NS nonlinearity explicitly
- Plot N(r) vs r for Oseen vortex, Beltrami flow, Burgers vortex
- **Goal:** see whether N(r) is "almost monotone" in practice and what breaks the monotonicity

**Priority 3 — Swirl perturbation:**
- Start with the KNSS axisymmetric no-swirl proof setup
- Add small swirl component u_θ = ε · f(r, z)
- Compute how the maximum principle for ω_θ/r degrades as ε grows
- Find the critical ε where the proof breaks
- **Goal:** quantify the perturbation gap in Mountain 4

**Priority 4 — Ancient solution construction attempts:**
- Try to construct a bounded non-constant ancient solution numerically
- Use backward-in-time integration from various initial data
- If every attempt converges to a constant, that's numerical evidence FOR Liouville
- If any attempt stabilizes on a non-constant profile, that's a counterexample candidate
- **Goal:** empirical evidence on whether non-trivial bounded ancient solutions can exist

**Priority 5 — Dimensional ladder:**
- Compute the 2D analogs of all the above (where Liouville is proved)
- Identify exactly which step fails in 3D but works in 2D
- **Goal:** isolate the 3D-specific difficulty numerically, the way Poincaré's numerical instance found that Hamilton-Ivey is the 3D-specific inequality

### Key quantities to track across all numerics

| Quantity | Symbol | What it measures |
|---|---|---|
| Vortex stretching norm | ||ω · ∇u|| | The enemy — this is what makes 3D hard |
| Frequency function | N(r) = r · D(r) / H(r) | Growth rate detector — monotone implies Liouville |
| Dirichlet integral | ∫_{B_R} |∇u|² | Energy — finite implies Liouville (Galdi) |
| Pressure gradient | ||∇p||_{BMO} | The hidden difficulty — bounded u ↛ bounded ∇p |
| Stretching-to-diffusion ratio | ||(ω·∇)u|| / ||Δω|| | >1 means stretching wins; <1 means diffusion wins |
| Enstrophy growth | d/dt ∫|ω|² | If bounded for ancient solutions → Liouville |
| Swirl parameter | ||u_θ||_∞ / M | How far from the proved (no-swirl) case |

## The Theory Track Scaffold

### What the theory instance (me) should attempt

**Attempt 001:** Frequency function with NS-adapted weight. Try: weight by |u|^{-α} or by e^{-p} (exponential of the pressure). See if the nonlinear error terms cancel or have a sign.

**Attempt 002:** Ancient condition exploitation. What properties do ancient NS solutions have that finite-time solutions don't? Known: ancient solutions are smooth (parabolic regularity backward in time). What else? Is ∇p automatically better for ancient solutions? Does the Dirichlet integral have a monotonicity property for ancient solutions?

**Attempt 003:** Vorticity formulation of Liouville. Work with ω instead of u. The vorticity equation has a different structure: the stretching term (ω · ∇)u can be rewritten as Sω where S is the strain matrix. The strain matrix of a bounded flow has specific spectral properties (tr S = 0 by incompressibility). Use these properties.

**Attempt 004:** Pressure Liouville. Instead of proving Liouville for u directly, prove it for p first. If -Δp = ∂²(uᵢuⱼ)/∂xᵢ∂xⱼ with bounded u, what can be said about p? Classical Liouville for harmonic functions says bounded harmonic functions on R³ are constant. The NS pressure is not harmonic — it satisfies a Poisson equation with bounded right side. But the right side has DIVERGENCE STRUCTURE (it's a double divergence of a bounded tensor). This might give more than the generic Poisson theory.

**Attempt 005:** Backward energy inequality. For ancient solutions, define E(t) = ∫ |u(x,t)|² φ(x) dx with a suitable cutoff φ. Show E(t) is monotone as t → -∞. If E is monotone and bounded below, it has a limit, and the limit might force u to be constant. This is the energy analog of the entropy monotonicity that works for Ricci flow (Perelman's W-entropy, which the Poincaré instance just reconstructed).

## Campaign Summary (8 attempts, Apr 9-10 2026)

### What was tried and what happened

| # | Attempt | Mountain | Outcome |
|---|---------|----------|---------|
| 001 | Frequency function (3 modifications) | 1 | Mod 1 (pressure-weighted) KILLED by numerics (H̃ < 0). Mod 3 (vorticity) ALIVE — N_ω monotone on Burgers, C=2.11. |
| 002 | Ancient condition exploitation | 2+3 | **KEY REDUCTION:** Liouville ≡ backward decay. Fixed-point equation (★★). |
| 003 | Backward energy (4 candidates) | 3+5 | Enstrophy DEAD (R_crit dichotomy). Gaussian DEAD (same). Fisher KILLED by numerics (wrong sign). NS entropy ALIVE but hits (Sω·ω). |
| 004 | NS entropy (Perelman analog) | All | Built W_NS. dW/dt computation reveals (Sω·ω) as THE single obstruction across all approaches. |
| 005 | KNSS corrector | 4 | Found Φ̃ = ω_θ/r - u_θ²/r². Principal terms cancel via Young's. |
| 006 | Corrector verification | 4 | Lower-order terms DON'T cancel. Source positive. BUT Gronwall + ancient might still close. |
| 007 | Uniqueness/rigidity (YM tangent) | NEW | **DECOMPOSITION FOUND.** Small-data Liouville via Koch-Tataru contraction. Full Liouville = backward entry + small-data + unique continuation. |
| 008 | Small-data proof sketch | 7 | **FIRST PROVABLE RESULT.** 6-step proof, ε₀ = ν/(8C), confirmed sound by numerics instance. |

### What the numerics instance computed (11 scripts)

| Script | Key result |
|---|---|
| known_ancient_solutions | Every known non-trivial ancient solution is UNBOUNDED |
| frequency_function | N(r) ≈ 1 on Burgers, non-monotone by 0.04% |
| vorticity_frequency | N_ω MONOTONE on Burgers (C=2.11) — first positive signal |
| backward_decay | R_crit = √(ν/C(M)), dimensional ladder 2D→3D |
| theory_requests_batch1 | Fisher KILLED (dF/dt|_stretch > 0), H̃ < 0 confirmed, N_ω on Beltrami = R/3 |
| stretching_eigenvalues | Eigenvalue analysis of S |
| stretching_alignment | Alignment between ω and S eigenvectors |
| swirl_perturbation | KNSS extends to ε < 0.908 |
| knss_corrector_test | Testing Φ̃ = ω_θ/r - u_θ²/r² |
| w_ns_entropy | Computing W_NS on Burgers |
| koch_tataru_constant | Computing explicit ε₀ |
| backward_construction | Attempting to construct bounded ancient solutions numerically |

### What was killed (dead directions)

- Pressure-weighted frequency function (H̃ < 0 on strain-dominated flows)
- Fisher information (stretching increases it — wrong sign)
- Pure enstrophy monotonicity (reproduces R_crit dichotomy, doesn't resolve small scales)
- Gaussian-weighted enstrophy (same dichotomy in τ parameterization)
- KNSS corrector with pure max principle (lower-order terms have wrong sign)

### What survived

1. **Vorticity frequency N_ω** — monotone on Burgers. If monotone for bounded ancient → Liouville.
2. **NS entropy** — works IF (Sω·ω) is controlled. Betchov alignment might help.
3. **Small-data Liouville** — PROVABLE with existing tools. First concrete theorem.
4. **The decomposition** — Full Liouville = backward entry + small-data + unique continuation.
5. **KNSS corrector + Gronwall + ancient** — might give axisymmetric Liouville with swirl.

### The remaining gap (precisely stated)

**Does every bounded ancient NS solution on R³ satisfy ||u(·, t₀) - ū||_∞ < ε₀ for some t₀ ≤ 0?**

Where ε₀ = ν/(8C_Oseen) is the small-data threshold from attempt_008.

Equivalently: can a bounded ancient solution maintain ||w||_∞ ≥ ε₀ for ALL t ≤ 0?

If NO (all solutions eventually dip below ε₀): Liouville follows by the decomposition.
If YES (some solution stays above ε₀ forever): that solution would be a remarkable object — bounded, ancient, non-trivial, sustaining stretching against diffusion for infinite time. Understanding WHY it sustains would itself be a major result.

## Status

OPEN. The gap has been narrowed from "prove Liouville" (vague) to "prove backward entry into the small-data regime" (precise, quantitative, explicit threshold). One provable theorem produced (small-data Liouville). Multiple dead directions documented. The campaign continues.
