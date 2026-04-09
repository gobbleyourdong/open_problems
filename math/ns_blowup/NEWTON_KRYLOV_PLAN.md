# Newton-Krylov Solver for Leray-Frame Periodic Orbits

## The Idea

Instead of running forward simulations from ICs and hoping to find blowup,
search directly for **periodic orbits** of the Leray-rescaled NS equations.

A periodic orbit in Leray frame = **discretely self-similar (DSS) blowup** in physical frame.
Bradshaw-Tsai (2019) proved DSS solutions EXIST for NS. Nobody has computed one.

## Why Leray Frame?

In Leray coordinates (ξ = x/√(T*-t), τ = -ln(T*-t)):
- Finite-time blowup t→T* maps to τ→∞
- A blowup profile becomes a **fixed point** (Type I) or **periodic orbit** (Type II/DSS)
- **ν stays constant** — no blowup of the viscous coefficient
- The spatial grid resolves the self-similar structure at O(1) scale
- NRS (1996) rules out fixed points (for finite-energy). So we hunt **periodic orbits**.

## Equations in Leray Frame

### Physical-frame equations (our current solver, Hou-Li variables):
```
∂u₁/∂t = -uʳ∂ᵣu₁ - uᶻ∂zu₁ + 2u₁ψ₁,z + ν·Δu₁
∂ω₁/∂t = -uʳ∂ᵣω₁ - uᶻ∂zω₁ + 2u₁·u₁,z + ν·Δω₁
```
where Δ = L3_r + ∂²z, L3_r = D²ᵣ + (3/r)Dᵣ

### Leray-rescaled Hou-Li variables:
```
U₁(ξ,τ) = λ(τ)·u₁(r,t),  W₁(ξ,τ) = λ²(τ)·ω₁(r,t)
ξ = r/λ,  λ = √(T*-t) = e^{-τ/2}
```

### Rescaled equations:
```
∂U₁/∂τ = ½ξ·∂U₁/∂ξ + ½U₁ - Uʳ∂ξU₁ - Uᶻ∂ξzU₁ + 2U₁Ψ₁,ξz + ν·ΔξU₁
∂W₁/∂τ = ½ξ·∂W₁/∂ξ + W₁ - Uʳ∂ξW₁ - Uᶻ∂ξzW₁ + 2U₁·U₁,ξz + ν·ΔξW₁
```

The new terms vs physical frame are:
- **½ξ·∇ξ** — Leray drift (advection toward origin)
- **½U₁** and **W₁** — amplitude scaling (different powers for u₁ vs ω₁)

These are LINEAR additions to the RHS. Everything else (nonlinear advection,
stretching, Poisson, diffusion) has the same structure.

## Algorithm: Periodic Orbit Search

### Step 1: Forward map
Given state X₀ = (U₁, W₁) at τ=0, integrate the Leray PDE forward by period T_p
to get X(T_p) = Φ(X₀, T_p).

### Step 2: Root finding
Find X₀ and T_p such that:
```
F(X₀, T_p) = Φ(X₀, T_p) - X₀ = 0
```

### Step 3: Newton iteration
```
X₀^{n+1} = X₀^n - J⁻¹·F(X₀^n, T_p)
```
where J = ∂F/∂X₀ is the monodromy matrix minus identity.

### Step 4: Krylov (GMRES) for the linear solve
J is Nr×Nz × Nr×Nz — too large to form explicitly.
Instead, use matrix-free GMRES with Jacobian-vector products:
```
J·v ≈ (Φ(X₀ + εv, T_p) - Φ(X₀, T_p)) / ε
```
Each J·v costs ONE forward PDE integration.

### Step 5: Period adaptation
Also solve for T_p. Add a phase condition (e.g., ∂τ‖W₁‖² = 0 at τ=0)
to pin the phase and make T_p well-defined.

## Implementation Plan

### Phase A: Leray forward solver (~200 lines)
File: `ns_blowup/leray_solver.py`

1. Subclass SweepSolver or build standalone
2. Modify `compute_rhs()` to add Leray drift terms:
   ```python
   # Leray drift: ½ξ·∂f/∂ξ (in r-direction, ξ maps to r in rescaled coords)
   drift_u1 = 0.5 * xi_r * (D_r @ U1) + 0.5 * xi_z * _ddz(U1)
   drift_w1 = 0.5 * xi_r * (D_r @ W1) + 0.5 * xi_z * _ddz(W1)

   # Amplitude scaling
   scale_u1 = 0.5 * U1
   scale_w1 = 1.0 * W1

   rhs_u1 += drift_u1 + scale_u1
   rhs_w1 += drift_w1 + scale_w1
   ```
3. Domain: ξ ∈ [0, ξ_max] instead of r ∈ [0,1]
   - ξ_max needs to be large enough to capture the profile
   - Wall BC at r=1 becomes a far-field condition at ξ_max
   - This is a CHANGE from bounded [0,1] to semi-infinite [0,∞)
   - Option: keep [0,1] but interpret as rescaled domain with damping layer near ξ=1

### Phase B: Validation (~50 lines)
1. Run Leray solver on known data (our Nr=256 Luo-Hou)
2. Verify Ω̃ ≈ 380 (constant) — should match our Leray analysis
3. Verify Γ trajectory matches physical-frame data

### Phase C: Newton-Krylov orbit finder (~300 lines)
File: `ns_blowup/orbit_finder.py`

1. Forward integration wrapper: `phi(X0, T_period) → X_final`
2. Residual: `F(X0, T_period) = phi(X0, T_period) - X0`
3. Jacobian-vector product via finite differences
4. GMRES inner solver (use scipy.sparse.linalg.gmres)
5. Newton outer loop with line search
6. Phase condition: pin phase by requiring ∂τ‖W₁‖²|_{τ=0} = 0

### Phase D: Initial guess strategies
The hardest part. Options:
1. **Warm start from physical data**: Take Nr=256 Leray-transformed data,
   use the late-time profile as initial guess. Even though it's regularizing,
   it's near the relevant region of phase space.
2. **Homotopy from Euler**: Start with ν=0 (where Chen-Hou have a steady state),
   gradually increase ν. Track how the fixed point moves. If it persists → blowup.
   If it vanishes at some ν_c → regularity.
3. **Random perturbation sweep**: Generate many random profiles, integrate
   forward a few periods, select those with smallest |F|.
4. **Symmetry reduction**: Exploit axisymmetry + z-reflection to reduce dimension.

## Computational Cost

Per Newton step:
- ~30 GMRES iterations × 1 forward integration each
- Forward integration: ~1000 RK4 steps per period
- Each step: Poisson solve + RHS = O(Nr² · Nz · log(Nz))

At Nr=64, Nz=128:
- Forward integration: ~1 minute on Spark
- Newton step: ~30 minutes
- Full convergence (~10 Newton steps): ~5 hours

At Nr=256, Nz=512:
- Forward integration: ~1 hour on Spark (based on validation timing)
- Newton step: ~30 hours
- Full convergence: 12+ days → need H200 or reduce grid

**Recommendation**: Develop and debug at Nr=64. Production runs at Nr=128 or Nr=256 on rented GPU.

## Key Risks

1. **No periodic orbit exists at ν=1e-4**: NRS rules out fixed points,
   and DSS existence (Bradshaw-Tsai) is for specific constructions,
   not arbitrary ν. The orbit might not exist at this ν.

2. **Basin of attraction**: Newton-Krylov only converges if initial guess
   is close enough. The orbit (if it exists) might be in a region of
   phase space we haven't explored.

3. **Domain truncation**: Leray frame is semi-infinite [0,∞).
   Truncating to [0, ξ_max] introduces artificial reflections.
   Need sponge layer or rational Chebyshev basis.

4. **Period unknown**: We're searching for T_p simultaneously.
   This adds a free parameter but also makes convergence harder.

## What Success Looks Like

- **Best case**: Newton-Krylov converges to a periodic orbit at some ν > 0.
  This IS a NS blowup solution. Validate spectrally, publish, claim prize.

- **Interesting case**: Orbit exists at ν=0 (Euler, consistent with Chen-Hou)
  but vanishes at some ν_c > 0. The value of ν_c and how the orbit
  disappears (saddle-node bifurcation?) is itself publishable.

- **Regularity evidence**: No orbit found at any ν > 0 despite thorough search.
  Combined with our Leray analysis showing Γ→0, this is evidence FOR regularity.
  Not a proof, but a clear numerical statement.

## Immediate Next Steps

1. Write `leray_solver.py` — add Leray drift to existing solver
2. Validate on Nr=64 against our Leray analysis data
3. Write `orbit_finder.py` — Newton-Krylov wrapper
4. Test with ν=0 first — should find Chen-Hou's steady state
5. Homotopy: increase ν, track the solution
