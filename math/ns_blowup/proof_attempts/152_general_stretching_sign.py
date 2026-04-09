"""
Can we prove that (ω·∇)u creates compression along ω GENERICALLY?

The vorticity stretching term (ω·∇)u_i = ω_j ∂u_i/∂x_j = (ω·∇)u.
This is the rate of change of u along the vorticity direction.

For incompressible flow: ∇·u = 0 → ∂u_i/∂x_i = 0.
The velocity gradient tensor A_ij = ∂u_i/∂x_j has trace zero.

The stretching rate α = ê·S·ê where ê = ω/|ω| and S = (A+A^T)/2.

KEY QUESTION: Does (ω·∇)u systematically compress along ω?

Let's compute: α = ê·S·ê = Σ_ij ê_i S_ij ê_j = Σ_ij ê_i (A_ij+A_ji)/2 ê_j
            = Σ_ij ê_i A_ij ê_j  (since A_ij ê_i ê_j = A_ji ê_j ê_i by relabeling)

So α = ê^T A ê = ê_i A_ij ê_j = ê_i (∂u_i/∂x_j) ê_j.

In the vorticity direction: ê = ω/|ω|.
So α = (1/|ω|²) ω_i (∂u_i/∂x_j) ω_j.

The vorticity equation: dω_i/dt = (ω·∇)u_i - (u·∇)ω_i + ν∇²ω_i
                       = ω_j ∂u_i/∂x_j - u_j ∂ω_i/∂x_j + ν∇²ω_i

The stretching of |ω|:
d|ω|/dt = (ω/|ω|) · dω/dt = ê · [(ω·∇)u - (u·∇)ω + ν∇²ω]

The ê·(ω·∇)u term = (1/|ω|) ω_i ω_j ∂u_i/∂x_j = |ω| α.

So: d(ln|ω|)/dt = α - ê·(u·∇ê) + ν·ê·(∇²ω)/|ω|

The α term is the stretching rate. For regularity, we need α bounded.

Now: is there a GENERAL reason why α < 0 at high |ω|?

FROM THE DATA:
- TG: α = -0.08 at top 10% |ω| (compression)
- KP: α ≈ 0 (marginally compressive)
- The α sign is controlled by c₁, c₂, c₃ alignment

ANALYTICAL ARGUMENT:

Consider the velocity gradient tensor decomposition:
A = S + Ω where S is symmetric (strain) and Ω is antisymmetric (rotation).

The antisymmetric part: Ω_ij = ε_ijk ω_k / 2 (related to vorticity).

At a point where ω is large, ω determines Ω. The strain S is determined by
the Poisson equation for pressure: ∂²p/∂x_i∂x_j = -(A_ij A_ji) terms.

The question: does the PRESSURE force S to be compressive along ω?

Yang et al. (2024): The deviatoric pressure Hessian H_dev has eigenvalues
proportional to |ω|² in the ⊥ω plane, creating symmetric alignment c₂ ≈ c₃.

If c₂ = c₃ and c₁ < 1/3 (Ashurst): c₃ = (1-c₁)/2 > (1-1/3)/2 = 1/3.
→ α = λ₁c₁ + λ₂c₂ + λ₃c₃

With trace-free: λ₂ = -(λ₁+λ₃). If λ₁ > 0, λ₃ < 0:
α = λ₁c₁ - (λ₁+λ₃)(1-c₁-c₃)/2 + λ₃c₃... this gets messy.

Let me try a different approach: what's the SIGN of (ω·∇)u · ω at a vorticity max?

At a maximum of |ω|²: ∇(|ω|²) = 0.
So: 2ω_i ∂ω_i/∂x_j = 0 for all j.
This means: ω_i ∂ω_i/∂x_j = 0, i.e., ω ⊥ ∂ω/∂x_j.

The gradient of ω in ANY direction is perpendicular to ω.
Equivalently: ê·(∂ω/∂x_j) = 0 for all j.

Since ω = |ω| ê: ∂ω_i/∂x_j = (∂|ω|/∂x_j) ê_i + |ω| ∂ê_i/∂x_j.
At a max of |ω|: ∂|ω|/∂x_j = 0 (gradient of |ω| is zero too by chain rule).
So: ∂ω_i/∂x_j = |ω| ∂ê_i/∂x_j.

Now: ω_i ∂ω_i/∂x_j = |ω|² ê_i ∂ê_i/∂x_j = 0 (since |ê|=1 → ê⊥∂ê/∂x_j). ✓

Now the stretching: (ω·∇)u_i = ω_j ∂u_i/∂x_j = ω_j (S_ij + Ω_ij).

The component along ω: ê · [(ω·∇)u] = ω_j S_ij ê_i + ω_j Ω_ij ê_i.

The Ω term: ω_j Ω_ij ê_i = ω_j (ε_ijk ω_k/2) ê_i/1
           ... actually Ω_ij ê_i = (1/2)(ε_ijk ω_k) ê_i.
           Then ω_j (ε_ijk ω_k) ê_i = ε_ijk ω_j ω_k ê_i.
           Since ε is antisymmetric in jk and ω_j ω_k is symmetric: = 0.

So: ê · [(ω·∇)u] = ω_j S_ij ê_i = |ω| ê_j S_ij ê_i = |ω| α. ✓

(Just confirming: the stretching rate α = ê·S·ê controls the growth of |ω|.)

THE CONSTRAINT: At a spatial maximum of |ω|, the Laplacian Δ|ω|² ≤ 0.

Δ|ω|² = 2|∇ω|² + 2ω · Δω.

For NS: Δω = (1/ν)(dω/dt - (ω·∇)u + (u·∇)ω).
At the max: (u·∇)|ω|² = 0 iff the max moves with the fluid.

This is getting complicated. Let me try a more direct approach using
the IDENTITY for α at a vorticity maximum.
"""
import torch
import numpy as np
import math

# Symbolic computation of the generic mechanism
print("=" * 70)
print("GENERIC MECHANISM: Why does (ω·∇)u create compression along ω?")
print("=" * 70)

# The key identity (from the vorticity equation at a max of |ω|):
#
# At x* where |ω| is maximal:
#   α = ê·S·ê = Σ_i λ_i c_i
#
# where λ_i are strain eigenvalues (trace-free: Σλ_i = 0)
# and c_i = cos²(ω, e_i) (alignment: Σc_i = 1).
#
# From the evolution: d|ω|²/dt = 2|ω| d|ω|/dt = 2ω·dω/dt
#   = 2ω·[(ω·∇)u - (u·∇)ω + νΔω]
#   = 2|ω|²α + 2ω·[-(u·∇)ω + νΔω]
#
# At the spatial max of |ω|²: ∇(|ω|²) = 0, Δ(|ω|²) ≤ 0.
#
# Δ(|ω|²) = 2(∂ω_i/∂x_j)(∂ω_i/∂x_j) + 2ω_i Δω_i = 2|∇ω|² + 2ω·Δω ≤ 0
#
# → ω·Δω ≤ -|∇ω|² < 0 (AT A MAXIMUM)
#
# The viscous contribution: νω·Δω ≤ -ν|∇ω|² < 0 (ALWAYS compressive at a max)
#
# For the advection: ω·[(u·∇)ω] = u·∇(|ω|²/2) = 0 at a spatial max.
#
# So: d|ω|²/dt |_{max} = 2|ω|²α + 2νω·Δω ≤ 2|ω|²α
#
# But this just says d|ω|²/dt ≤ 2|ω|²α, which doesn't constrain α.
# We need the PRESSURE to constrain α.

# Let me think about this differently.
# The pressure enters through the STRAIN equation, not the vorticity equation.
# The strain evolves as:
#   dS/dt + u·∇S = -S² - (1/4)(ωω^T - |ω|²I/3) + H_dev + νΔS + ...
#
# where H_dev is the deviatoric pressure Hessian.
# The Yang formula: H_dev ≈ -(1/4)(ωω^T - |ω|²I/3)
# (This is the leading-order term when |ω| dominates.)
#
# With the Yang approximation:
#   dS/dt ≈ -S² - (1/2)(ωω^T - |ω|²I/3) + νΔS + ...
#
# The ωω^T term pushes S toward having eigenvalue -|ω|²/2 along ω
# and +|ω|²/4 in the ⊥ω plane (by trace-free).
#
# But file 148 showed Yang alone gives c₃ = 0.13, not 1/3.
# So the local approximation is not enough.

# The NON-LOCAL pressure is the key.
# Let me compute what the full Poisson pressure does.

print("\n--- The Pressure Poisson Equation ---")
print("Δp = -A_ij A_ji = -(S_ij + Ω_ij)(S_ji + Ω_ji)")
print("   = -S_ij S_ji - 2S_ij Ω_ji - Ω_ij Ω_ji")
print("   = -|S|² - 2S_ij Ω_ji - |Ω|²")
print()
print("Since Ω_ij = ε_ijk ω_k/2: |Ω|² = |ω|²/2")
print("And 2S_ij Ω_ji = S_ij ε_jik ω_k = (S × ω)_k ... (tensor product)")
print()
print("So: Δp = -|S|² + |ω|²/2 - (cross terms)")
print()
print("At high |ω|: Δp ≈ |ω|²/2 (positive pressure source)")
print("→ p is positive (high pressure) where |ω| is large")
print("→ ∂²p/∂z² > 0 along ω → COMPRESSION along ω")
print()
print("This is the GENERIC mechanism:")
print("  High |ω| → high pressure → compression along ω direction")
print("  It's not TG-specific, it's a consequence of the Poisson equation!")

# Quantify: what's the pressure Hessian along ω at a vorticity max?
# At x* where |ω| is max and ω = |ω|ê₃ (WLOG):
# Δp = |ω|²/2 - |S|² + cross terms
# The leading term is |ω|²/2 (from |Ω|² = |ω|²/2).
#
# If |ω| >> |S| at the max (which happens as |ω| grows):
# p ≈ |ω|² / (4|k|²) (Poisson solution)
# ∂²p/∂ê² ≈ |ω|² / 4 (second derivative along ω)
#
# Wait, the Poisson equation in Fourier: p_hat = source_hat / (-|k|²)
# So the pressure Hessian H_ij = -k_i k_j p_hat = k_i k_j source_hat / |k|²
#
# For the |ω|² source concentrated near x*:
# H_ij ≈ ∂²(|ω|²/2)/∂x_i∂x_j locally
#
# Hmm, this is getting circular. Let me think about it more carefully.

# Actually, the key observation is SIMPLER than I'm making it:
#
# The pressure field p satisfies Δp = (|ω|² - |S|²) / 2 (approximately).
# At a point where |ω| is maximal: Δp > 0 (since |ω|² ≥ |S|² for Beltrami-like structures).
#
# Δp > 0 means p has a LOCAL MINIMUM at that point.
# Wait no: Δp > 0 means the average of p on a sphere exceeds p at the center.
# So p is BELOW the surrounding average → it's a local minimum.
#
# But wait: pressure creates an ACCELERATING force -∇p.
# If p has a minimum at x*: -∇p points AWAY from x* in all directions.
# This is an EXPANSION (divergent) flow pattern.
# But the flow is incompressible! The expansion is in the ⊥ω plane,
# balanced by COMPRESSION along ω.
#
# Actually, the pressure Hessian H = ∇²p has Δp = tr(H) > 0.
# If the pressure field is approximately axisymmetric about ω:
# H = diag(h_⊥, h_⊥, h_ω) with 2h_⊥ + h_ω = Δp > 0.
#
# The pressure Hessian enters the strain evolution:
# dS/dt ~ ... + H + ...
# The H_ωω = h_ω component acts on the strain along ω.
# If h_ω < 0: pressure creates compression along ω. GOOD.
# If h_ω > 0: pressure creates stretching along ω. BAD.
#
# With axisymmetry: h_⊥ = (Δp - h_ω)/2.
# The incompressible acceleration: the pressure GRADIENT pushes fluid
# away from the low-p region (toward high |ω|).
#
# But the issue is: is h_ω < 0 or > 0?
#
# Yang's formula says: h_ω = -(1/4)|ω|² (deviatoric part)
# And the isotropic part: (Δp/3) = (|ω|²-|S|²)/6
# So H_ωω = h_ω + Δp/3 = -(1/4)|ω|² + (|ω|²-|S|²)/6
#         = |ω|²(-1/4 + 1/6) - |S|²/6
#         = -|ω|²/12 - |S|²/6
#         < 0 (ALWAYS!)
#
# H_ωω < 0 ALWAYS!

print("\n" + "=" * 70)
print("KEY IDENTITY: H_ωω < 0 ALWAYS")
print("=" * 70)
print()
print("Using Yang's pressure Hessian formula:")
print("  H_dev = -(1/4)(ωω^T - |ω|²I/3)")
print("  H_iso = (Δp/3)I = ((|ω|²/2 - |S|²)/3)I")
print()
print("Along ω: H_ωω = H_dev,ωω + H_iso")
print("  H_dev,ωω = -(1/4)(|ω|² - |ω|²/3) = -(1/4)(2|ω|²/3) = -|ω|²/6")
print()
print("Wait, let me redo this carefully.")
print()

# H_dev = -(1/4)(ω_i ω_j - |ω|²δ_ij/3)
# Along ω (i.e., ê·H_dev·ê where ê = ω/|ω|):
# ê_i H_dev_ij ê_j = -(1/4)(ê_i ω_i ω_j ê_j - |ω|² ê_i δ_ij ê_j/3)
#                   = -(1/4)(|ω|² - |ω|²/3)
#                   = -(1/4)(2|ω|²/3)
#                   = -|ω|²/6

print("H_dev along ω: ê·H_dev·ê = -(1/4)(|ω|² - |ω|²/3) = -|ω|²/6")
print()

# Now the isotropic part: H_iso = (1/3)(Δp)I = (1/3)((|ω|²-2|S|²)/2)I
# Wait: Δp = -A_ij A_ji. Let me compute this correctly.
# A_ij A_ji = (S_ij + Ω_ij)(S_ji + Ω_ji) = S_ij S_ji + S_ij Ω_ji + Ω_ij S_ji + Ω_ij Ω_ji
# = |S|² + 2 S_ij Ω_ji + |Ω|²
# Note: S_ij Ω_ji = S_ij (-Ω_ij) = -S_ij Ω_ij (since Ω is antisymmetric)
# Actually: Ω_ji = -Ω_ij, so S_ij Ω_ji = -S_ij Ω_ij
# And by the same token: Ω_ij S_ji = Ω_ij S_ij (since S is symmetric)
# So the cross terms cancel: S_ij Ω_ji + Ω_ij S_ji = 0.
# Therefore: A_ij A_ji = |S|² + |Ω|² = |S|² + |ω|²/2.
# And: Δp = -(|S|² + |ω|²/2)

# Wait, this gives Δp < 0 always! But I had Δp = |ω|²/2 - |S|² before.
# Let me recheck.
#
# The standard NS pressure: Δp = -∂u_i/∂x_j · ∂u_j/∂x_i = -A_ij A_ji
#   = -(|S|² + |ω|²/2)
# Actually no. Let me be very careful.
# Δp = -(∂²/∂x_i∂x_j)(u_i u_j) = ... no, this isn't right either.
#
# From NS: ∂u_i/∂t + u_j ∂u_i/∂x_j = -∂p/∂x_i + ν∇²u_i
# Taking divergence: ∂²p/∂x_i² = -∂u_i/∂x_j · ∂u_j/∂x_i (using ∇·u=0)
# Wait: ∂/∂x_i(∂u_i/∂t) = 0 (div-free). And:
# ∂/∂x_i(u_j ∂u_i/∂x_j) = (∂u_j/∂x_i)(∂u_i/∂x_j) + u_j ∂²u_i/∂x_i∂x_j
#                          = A_ji A_ij + 0 (div-free)
#                          = A_ij A_ji
#
# So: Δp = -A_ij A_ji = -(|S|² + |ω|²/2)?
# Wait, |Ω|² = Ω_ij Ω_ij. And Ω_ij = (ε_ijk ω_k)/2.
# |Ω|² = (1/4) ε_ijk ε_ijl ω_k ω_l = (1/4)(2δ_kl) ω_k ω_l = |ω|²/2.
# And A_ij A_ji = S_ij S_ji + Ω_ij Ω_ji = |S|² + |Ω|²= |S|² + |ω|²/2.
#
# But Ω_ij Ω_ji = Ω_ij (-Ω_ij) = -|Ω|² = -|ω|²/2.
# Wait: Ω_ji = -Ω_ij. So Ω_ij Ω_ji = -Ω_ij² = -|Ω|².
#
# Hmm, A_ij A_ji = S_ij S_ji + S_ij Ω_ji + Ω_ij S_ji + Ω_ij Ω_ji
# = |S|² + 0 + 0 + (-|Ω|²) = |S|² - |ω|²/2.
#
# So Δp = -(|S|² - |ω|²/2) = |ω|²/2 - |S|².
# CORRECT! Δp = |ω|²/2 - |S|².

print("CORRECTED: Δp = |ω|²/2 - |S|²")
print()
print("Derivation: A_ij A_ji = S² + SΩ + ΩS + Ω²")
print("  SΩ + ΩS terms cancel (S symmetric, Ω antisymmetric)")
print("  Ω_ij Ω_ji = -|Ω|² (since Ω_ji = -Ω_ij)")
print("  So A_ij A_ji = |S|² - |Ω|² = |S|² - |ω|²/2")
print("  Δp = -A_ij A_ji = |ω|²/2 - |S|²")
print()

# Now the pressure Hessian along ω:
# H_iso = (1/3)(Δp) = (1/3)(|ω|²/2 - |S|²)
# H_dev along ω = -|ω|²/6  (from Yang)
# Total H_ωω = H_dev + H_iso = -|ω|²/6 + (|ω|²/2 - |S|²)/3
#            = -|ω|²/6 + |ω|²/6 - |S|²/3
#            = -|S|²/3

print("Full H_ωω = H_dev_ωω + H_iso")
print("  = -|ω|²/6 + (|ω|²/2 - |S|²)/3")
print("  = -|ω|²/6 + |ω|²/6 - |S|²/3")
print("  = -|S|²/3")
print()
print("H_ωω = -|S|²/3 < 0 ALWAYS!")
print()
print("The pressure Hessian along ω is ALWAYS COMPRESSIVE,")
print("with magnitude proportional to the strain intensity |S|².")
print()
print("This is INDEPENDENT of:")
print("  - The specific IC")
print("  - The viscosity")
print("  - The flow geometry")
print("  - The relative magnitudes of |ω| and |S|")
print()
print("It depends ONLY on Yang's formula for H_dev being correct.")
print()

# BUT WAIT: File 148 showed Yang alone gives c₃ = 0.13.
# The Yang formula is a LOCAL approximation. The actual pressure is NON-LOCAL.
# So H_ωω = -|S|²/3 is only approximate.

print("CAVEAT: Yang's formula is a LOCAL approximation.")
print("The actual pressure Hessian includes non-local corrections.")
print("File 148 showed: Yang alone → c₃ = 0.13 (below 1/3).")
print("Full NS → c₃ = 0.33 (exactly 1/3 for KP).")
print()
print("So the non-local corrections are IMPORTANT and they HELP.")
print("The local Yang term gives compression, but not enough.")
print("The non-local pressure provides additional compression to reach c₃ = 1/3.")
print()

# The proof structure could be:
# 1. H_ωω = -|S|²/3 from Yang (local term, always compressive)
# 2. Non-local corrections make it MORE compressive
# 3. Combined: c₃ ≥ 1/3 at high |ω|

# But proving (2) is the hard part.
# What if instead we prove a WEAKER bound?

print("=" * 70)
print("WEAKER APPROACH: bound α directly using H_ωω")
print("=" * 70)
print()
print("The strain evolution along ω:")
print("  dα/dt = -ê·S²·ê + ê·H·ê + ... (viscous, advection)")
print()
print("The key terms:")
print("  -ê·S²·ê ≤ -α² (by Cauchy-Schwarz, since ê·S²·ê ≥ (ê·S·ê)²)")
print("  ê·H·ê = H_ωω ≤ -|S|²/3 (from Yang, approximately)")
print()
print("WAIT: -ê·S²·ê ≤ 0 (self-depletion, always non-positive)")
print("But the inequality ê·S²·ê ≥ α² is NOT always true.")
print("It's: ê·S²·ê ≥ α²/n where n is dimension... no, that's wrong.")
print()
print("Actually: ê·S²·ê = Σ λ_i² c_i ≥ (Σ λ_i c_i)² = α² iff ...")
print("  This is Cauchy-Schwarz: (Σ λ_i² c_i)(Σ c_i) ≥ (Σ λ_i c_i)²")
print("  Since Σ c_i = 1: ê·S²·ê ≥ α²  ✓")
print()
print("So: dα/dt ≤ -α² + H_ωω + ... ≤ -α² - |S|²/3 + ...")
print()
print("With |S|² ≥ 3α² (? not necessarily): dα/dt ≤ -α² - α² = -2α²")
print()
print("Hmm, |S|² = Σ λ_i² ≥ max(λ_i²). And α = Σ λ_i c_i.")
print("We need a relation between |S|² and α.")
print()
print("|S|² = λ₁² + λ₂² + λ₃² with λ₁+λ₂+λ₃=0.")
print("So |S|² ≥ 3α² iff λ₁²+λ₂²+λ₃² ≥ 3(λ₁c₁+λ₂c₂+λ₃c₃)²")
print("This is NOT true in general (consider c₁=1, c₂=c₃=0: |S|²≥3λ₁²? No.)")
print()
print("But we know c₁ < 1/3 at high |ω| (Ashurst).")
print("With c₁ < 1/3: α = λ₁c₁ + λ₂c₂ + λ₃c₃ < λ₁/3 + λ₂c₂ + λ₃c₃")
print("                < λ₁/3 + 0 + 0 = λ₁/3  (using c₂,c₃<1 and λ₂<λ₁, λ₃<0)")
print("Actually this isn't right either, since λ₂ can be positive.")
print()

# Let me just compute the Riccati structure numerically for several flows.
print("=" * 70)
print("NUMERICAL TEST: Is dα/dt ≤ -α² at high |ω|?")
print("(The Riccati bound from the self-depletion)")
print("=" * 70)

# For this we need to compute α and its time derivative from DNS data.
# This requires two consecutive timesteps.

DTYPE = torch.float64
pi = math.pi

class MiniSolver:
    def __init__(self, N=32, nu=0.0):
        self.N = N; self.nu = nu; self.Lx = 2*pi
        dx = self.Lx/N
        x = torch.linspace(0, self.Lx-dx, N, dtype=DTYPE)
        self.X, self.Y, self.Z = torch.meshgrid(x, x, x, indexing='ij')
        k = torch.fft.fftfreq(N, d=dx/(2*pi)).to(dtype=DTYPE)
        self.kx, self.ky, self.kz = torch.meshgrid(k, k, k, indexing='ij')
        self.ksq = self.kx**2 + self.ky**2 + self.kz**2; self.ksq[0,0,0]=1
        self.D = ((self.kx.abs()<N//3)&(self.ky.abs()<N//3)&(self.kz.abs()<N//3)).to(DTYPE)

    def fft(self, f): return torch.fft.fftn(f)
    def ifft(self, fh): return torch.fft.ifftn(fh).real
    def curl(self, ux_h, uy_h, uz_h):
        I=1j; return (I*self.ky*uz_h-I*self.kz*uy_h,I*self.kz*ux_h-I*self.kx*uz_h,I*self.kx*uy_h-I*self.ky*ux_h)
    def vel(self, wx_h, wy_h, wz_h):
        px=wx_h/self.ksq;py=wy_h/self.ksq;pz=wz_h/self.ksq
        px[0,0,0]=0;py[0,0,0]=0;pz[0,0,0]=0
        I=1j; return (I*self.ky*pz-I*self.kz*py,I*self.kz*px-I*self.kx*pz,I*self.kx*py-I*self.ky*px)
    def rhs(self, wh):
        D=self.D; uh=self.vel(*wh)
        f={}
        for n,h in [('ux',uh[0]),('uy',uh[1]),('uz',uh[2]),('wx',wh[0]),('wy',wh[1]),('wz',wh[2])]:
            f[n]=self.ifft(D*h)
            for d,kd in [('x',self.kx),('y',self.ky),('z',self.kz)]:
                f[f'd{n}_d{d}']=self.ifft(1j*kd*D*h)
        s=[];a=[]
        for c in ['x','y','z']:
            s.append(f['wx']*f[f'du{c}_dx']+f['wy']*f[f'du{c}_dy']+f['wz']*f[f'du{c}_dz'])
            a.append(f['ux']*f[f'dw{c}_dx']+f['uy']*f[f'dw{c}_dy']+f['uz']*f[f'dw{c}_dz'])
        return tuple(D*self.fft(s[i]-a[i])-self.nu*self.ksq*wh[i] for i in range(3))
    def step(self, wh, dt):
        def add(s,k,a): return tuple(s[i]+a*k[i] for i in range(3))
        k1=self.rhs(wh); k2=self.rhs(add(wh,k1,.5*dt)); k3=self.rhs(add(wh,k2,.5*dt)); k4=self.rhs(add(wh,k3,dt))
        return tuple(self.D*(wh[i]+dt/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])) for i in range(3))

def compute_alpha_at_max(solver, wh):
    """Compute α = ê·S·ê at the point of max |ω|."""
    D = solver.D; N = solver.N
    uh = solver.vel(*wh)
    k_dirs = [solver.kx, solver.ky, solver.kz]

    duidxj = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            duidxj[i,j] = solver.ifft(1j * k_dirs[j] * D * [uh[0],uh[1],uh[2]][i])
    S = 0.5 * (duidxj + duidxj.transpose(0,1))

    w = [solver.ifft(D*wh[i]) for i in range(3)]
    om = (w[0]**2 + w[1]**2 + w[2]**2).sqrt()

    # Max |ω| point
    flat = om.flatten()
    idx = flat.argmax().item()
    iz = idx % N; iy = (idx // N) % N; ix = idx // (N*N)

    wv = torch.tensor([w[i][ix,iy,iz].item() for i in range(3)], dtype=DTYPE)
    wn = wv.norm()
    if wn < 1e-12:
        return 0.0, 0.0, 0.0
    eh = wv / wn

    Sl = S[:,:,ix,iy,iz]
    alpha = (eh @ Sl @ eh).item()
    S2_ee = (eh @ Sl @ Sl @ eh).item()
    Snorm = Sl.norm().item()**2

    return alpha, S2_ee, Snorm

# Run for TG
solver = MiniSolver(N=32, nu=0.0)
X, Y, Z = solver.X, solver.Y, solver.Z
ux = torch.cos(X)*torch.sin(Y)*torch.cos(Z)
uy = -torch.sin(X)*torch.cos(Y)*torch.cos(Z)
uz = torch.zeros_like(X)
wh = solver.curl(solver.fft(ux), solver.fft(uy), solver.fft(uz))

dt = 2e-4
n_steps = 2000
print(f"\nTG Euler, N=32, dt={dt}, {n_steps} steps")
print(f"{'step':>6s}  {'t':>8s}  {'α':>10s}  {'ê·S²·ê':>10s}  {'|S|²':>10s}  {'α²':>10s}  dα/dt bound")

alpha_prev = None
for step in range(n_steps+1):
    if step % 200 == 0:
        alpha, S2ee, Snorm = compute_alpha_at_max(solver, wh)

        if alpha_prev is not None:
            dalpha = (alpha - alpha_prev) / (200 * dt)
            bound = -S2ee  # self-depletion bound
            yang_h = -Snorm / 3  # Yang pressure correction
            print(f"  {step:6d}  {step*dt:8.4f}  {alpha:10.6f}  {S2ee:10.6f}  {Snorm:10.4f}  "
                  f"{alpha**2:10.6f}  dα/dt={dalpha:.4f} bound={bound:.4f} +Yang={yang_h:.4f}")
        else:
            print(f"  {step:6d}  {step*dt:8.4f}  {alpha:10.6f}  {S2ee:10.6f}  {Snorm:10.4f}  "
                  f"{alpha**2:10.6f}")
        alpha_prev = alpha

    if step < n_steps:
        wh = solver.step(wh, dt)

print(f"\n{'='*70}")
print("SUMMARY OF PROOF-RELEVANT FINDINGS:")
print(f"{'='*70}")
print()
print("1. H_ωω = -|S|²/3 (Yang local approximation)")
print("   → Pressure Hessian along ω is ALWAYS compressive")
print("   → But the LOCAL approximation gives only c₃ ≈ 0.13 (insufficient)")
print()
print("2. The FIRST nonlinear products (TG) are analytically computable")
print("   → Exclusively at |k| = 2√2 (the (0,2,2) family)")
print("   → Create AXISYMMETRIC COMPRESSION along ω: cos²(ω,e₃) = 1.0")
print("   → Verified to machine precision")
print()
print("3. The self-depletion ê·S²·ê ≥ α² provides Riccati structure")
print("   → dα/dt ≤ -α² + H_ωω ≈ -α² - |S|²/3")
print("   → The Yang term REINFORCES the self-depletion")
print()
print("4. NON-LOCAL pressure corrections are NEEDED to get c₃ to 1/3")
print("   → Yang alone: c₃ = 0.13, full NS: c₃ = 0.33")
print("   → The gap is closed by advective mixing + multi-mode coupling")
print()
print("PROOF STRATEGY:")
print("  Step 1: Yang gives H_ωω ≤ 0 (compression along ω)")
print("  Step 2: Non-local corrections STRENGTHEN the compression")
print("  Step 3: Combined effect gives c₃ ≥ 1/3")
print("  Step 4: c₁ < 1/3 + c₃ ≥ 1/3 + trace-free → α ≤ 0 → BKM → regularity")
print()
print("The gap is in Step 2: proving the non-local pressure helps.")
