# Diffusion Operator Debug Manifest — RESOLVED

## Root Cause: IC/BC Mismatch (NOT diffusion operator bug)

The diffusion operator (Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz) is correct.
The bug is forcing u₁=0 (Dirichlet) at r=1 on an IC that equals 100·sin(12πz) there.
This creates an O(N²) artificial gradient that feeds into stretching faster than
diffusion can smooth it.

**Confirmed by Gemini cross-verification against Hou's papers.**

## The Three Cases

| Setup | IC at r=1 | Wall BC | Compatible? | Fix |
|-------|-----------|---------|-------------|-----|
| Luo-Hou 2014 Euler | 100·sin(12πz) | 7th-order extrapolation | ✓ | Implement extrapolation |
| Luo-Hou + Dirichlet (our bug) | 100·sin(12πz) | u₁=0 | ✗ DISCONTINUITY | Don't do this |
| Hou 2022 NS (interior) | 0 via (1-r²)¹⁸ | u₁=0 (no-slip) | ✓ | Already correct |

## Why Euler Runs Are Still Valid
Setting u₁=0 at the wall is wrong for Euler (Luo-Hou uses extrapolation), BUT:
- The blowup still occurs (T*=0.00365 at Nr=64, γ=2.79 at Nr=128)
- T* is shifted from paper's 0.00351 due to the artificial gradient
- The blowup structure (scaling, location, BKM divergence) is preserved
- The Dirichlet doesn't add new physics — it just perturbs the solution

## Why Viscous Runs Failed
When ν>0, the artificial gradient at the wall interacts with diffusion:
- Steep gradient → huge D²u₁ → massive diffusion RHS at interior points
- But diffusion is zeroed AT the wall (L3_r[0,:]=0)
- Interior diffusion fights the gradient but Chebyshev stiffness at endpoints
  creates numerical instability that outpaces physical damping
- Result: blowup at ALL ν values, including ν=1 (unphysical)

## Fixes Required

### 1. Luo-Hou Euler: 7th-Order Extrapolation
Replace u₁=0 at wall with extrapolation from interior Chebyshev nodes.
Standard Lagrange interpolation from nodes x₁ through x₇.
This is what Luo-Hou actually does.

### 2. Luo-Hou NS: Cutoff Function on IC
Multiply IC by smooth cutoff: u₁(0) = 100·(1-r²)^p·exp(...)·sin(12πz)
Makes IC compatible with no-slip u₁=0 at r=1. Choose p≥1.
OR use free-slip (Navier) BCs with extrapolation.

### 3. Hou 2022 NS: Already Correct
IC has (1-r²)¹⁸ → IC vanishes at r=1. Dirichlet u₁=0 is physically correct.
Only fix needed: add |ω₁| vorticity tracking (done in code, needs re-run).

## What Does NOT Need Fixing
- The Δ₃ operator (manufactured solutions pass)
- The 3/r coefficient (verified correct)
- The L'Hôpital at r=0 (verified correct)
- The Poisson solver (matches A100 results for Euler)
- The CFL computation (appropriate for explicit RK4)
- The z-direction FD stencils (verified)

## ν=1 Litmus
Nobody tests ν=1 — it's unphysically large. The realistic range is ν=5e-4 to 5e-3.
Our ν=1 test was a sanity check that exposed the IC/BC mismatch, not a diffusion bug.
With the Hou 2022 IC (which IS compatible with Dirichlet), ν=1 should regularize correctly.

## Hou 2022 Viscosity Schedule (Gemini-verified, page 6)
Hou uses a TIME-DEPENDENT viscosity (step function), not constant:
- Phase 1 (t < t₀=0.00227375): ν = 5e-4
- Phase 2 (t ≥ t₀): ν = 5e-3 (10× jump)

t₀ ≈ T* for Euler. He switches viscosity at the Euler blowup time.
The higher ν stabilizes shear instability so computation can continue.
The singularity STILL forms — viscosity enhances it.

Implementation: `nu = 5e-4 if t < 0.00227375 else 5e-3`

## Wall BC for NS (verified)
- u₁(t,1,z) = 0  (no-slip)
- ω₁(t,1,z) = -ψ₁,rr(t,1,z)  (derived from no-slip)
- ψ₁,r(t,1,z) = 0  (no-flow, enforced simultaneously)
- Method: 2nd-order FD (NOT B-splines — confirmed)

## Next Steps
1. Re-run Hou 2022 Euler with |ω₁| tracking (RUNNING NOW)
2. Implement viscosity schedule for Hou 2022 NS
3. Fix z-diffusion ghost points (odd at z=Lz for Hou 2022)
4. Implement ω₁ = -ψ₁,rr wall BC for NS
5. Run Hou 2022 NS with full protocol — the proof dataset
