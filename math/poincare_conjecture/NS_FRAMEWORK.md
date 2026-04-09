Sources: Luo-Hou 2014 MMS, Hou 2022 FoCM, Hou 2026 JFoCM, Chen-Hou 2022 Part I, Chen-Hou 2025 PNAS

=== SHARED VARIABLES (all papers) ===
u₁=uθ/r  ω₁=ωθ/r  ψ₁=ψθ/r  (Hou-Li transform)
uʳ=−r·ψ₁,z  uᶻ=2ψ₁+r·ψ₁,r

=== EQUATIONS ===
u₁: ∂ₜu₁+uʳ∂ᵣu₁+uᶻ∂ᵤu₁ = 2u₁ψ₁,z + ν·Δ₃u₁
ω₁: ∂ₜω₁+uʳ∂ᵣω₁+uᶻ∂ᵤω₁ = 2u₁u₁,z + ν·Δ₃ω₁
Poisson: −(∂ᵣᵣ+3/r·∂ᵣ+∂ᵤᵤ)ψ₁ = ω₁
Δ₃ = ∂ᵣᵣ+(3/r)∂ᵣ+∂ᵤᵤ (5D Laplacian radial part)
Stretching: u₁→+2u₁ψ₁,z  ω₁→2u₁u₁,z (NO 1/r⁴)

========================================
PAPER 1: Luo-Hou 2014 (BOUNDARY blowup)
========================================
IC: u₁(0)=100·exp(−30(1−r²)⁴)·sin(12πz)  ω₁(0)=0
Domain: r∈[0,1] z∈[0,1/6] computed on [0,1/24] (quarter-period)
L=1/6  *CRITICAL*
BC r=0: ∂ᵣu₁=∂ᵣω₁=∂ᵣψ₁=0 (even)
BC r=1: ψ₁=0 (no-flow) + 7th-order extrapolation for u₁,ω₁
BC z=0: u₁=ω₁=ψ₁=0 (odd)
BC z=L/4: u₁ even (∂ᵤu₁=0), ω₁,ψ₁ odd (=0) *CRITICAL*
Diffusion: NONE (ν=0, inviscid Euler)
Blowup: T*=0.0035056 at (r,z)=(1,0) BOUNDARY
Scaling: ‖ω‖∞~(T−t)⁻⁵ᐟ² (γ=5/2)
Method: 6th-order B-spline Galerkin + 6th-order FD, RK4, adaptive mesh, up to 2048²

========================================
PAPER 2: Hou 2022 FoCM (INTERIOR blowup)
========================================
IC: u₁(0)=12000(1−r²)¹⁸sin(2πz)/(1+12.5sin²(πz))  ω₁(0)=0  *CRITICAL*
Amplitude: 12000 (120× Luo-Hou)
Radial: (1−r²)¹⁸ concentrated at r=0 (interior)
z-profile: sin(2πz)/(1+12.5sin²(πz)) biased toward z=0 *CRITICAL*
Domain: r∈[0,1] z∈[0,1] computed on [0,1/2] (half-period)
L=1  *CRITICAL*
BC r=0: ∂ᵣ=0 (Neumann pole)
BC r=1 Euler: uθ=uᶻ=0, ψ₁=0 (no-flow)
BC r=1 NS: u₁=0, ω₁=−ψ₁,rr *CRITICAL*
BC z=0,z=1/2: u₁=ω₁=ψ₁=0 (odd)
ν tested: 5×10⁻³ → viscosity ENHANCES singularity
Blowup: T*=0.00227648 at (r,z)=(0,0) INTERIOR
Scaling: ‖ω‖∞~(T−t)⁻¹ (γ=1) ‖u₁‖∞~(T−t)⁻¹ᐟ² Z(t)~(T−t)¹ᐟ²
Method: 2nd-order FD, RK2, B-spline Poisson, adaptive mesh, up to 1536²
Numerical diffusion: ν_num=1/n₁² *CRITICAL*

========================================
PAPER 3: Hou 2026 JFoCM (generalized dim)
========================================
IC: SAME as Hou 2022 FoCM
Variables: uses Γ=r·uθ instead of u₁
Generalized dimension: n(τ)=1+2R(τ)/Z(τ) → 3.188 as ν₀→0 *CRITICAL*
Γ eqn: Γₜ+uʳΓᵣ+uᶻΓᵤ = ν(Γᵣᵣ+(n−4)/r·Γᵣ+(6−2n)/r²·Γ+Γᵤᵤ)
ω₁ eqn: ω₁,ₜ+uʳω₁,ᵣ+uᶻω₁,ᵤ = (Γ²/r⁴)ᵤ−(n−3)ψ₁,ᵤω₁+ν(ω₁,ᵣᵣ+n/r·ω₁,ᵣ+ω₁,ᵤᵤ)
Poisson: −(∂ᵣᵣ+n/r·∂ᵣ+∂ᵤᵤ)ψ₁=ω₁ (n/r not 3/r) *CRITICAL*
Solution-dependent viscosity: ν(t)=ν₀·‖u₁‖∞·Z(t)² *CRITICAL*
ν₀=0.006 *CRITICAL*
Key constants: λ₀≈0.914 c_l≈0.5233 R(T₁)=1.2312e-4 Z(T₁)=3.3302e-5 R₀=3.6927
Max vorticity growth: 9×10²¹ (τ=185)
BKM: VIOLATED — ∫‖ω‖∞ds diverges linearly *CRITICAL*
Blowup: (0,0) interior, ‖ω‖∞~(T−t)⁻¹
Method: 2nd-order FD, RK2, 2nd-order FEM Poisson, 768²–1024²

========================================
PAPER 4: Chen-Hou 2022 Part I (self-similar)
========================================
Rescaled eqns:
  ωₜ+(c_l·x+u)·∇ω = θₓ+c_ω·ω
  θₜ+(c_l·x+u)·∇θ = c_θ·θ
Key constants: c_l=3.00649898 c_ω=−1.02942516 uₓ(0)=−2.532674 *CRITICAL*
−c_l/c_ω=2.9205600 (determines blowup exponent μ)

========================================
PAPER 5: Chen-Hou 2025 PNAS (rigorous proof)
========================================
Boussinesq: ωₜ+u·∇ω=θₓ  θₜ+u·∇θ=0
Rescaled: ω̃τ+(c_l·x+ũ)·∇ω̃=θ̃ₓ+c_ω·ω̃  θ̃τ+(c_l·x+ũ)·∇θ̃=(c_l+2c_ω)·θ̃
Normalizations: c_l(t)=2θₓₓ(t,0)/ωₓ(t,0)  c_ω(t)=½c_l(t)+uₓ(t,0)
μ≈2.92 (spatial scaling exponent) *CRITICAL*
Domain 3D: cylinder r∈[0,1] z∈𝕋  Domain 2D: ℝ²₊ (upper half-plane)
Blowup: 1/(T−t) amplitude, BOUNDARY, PROVEN (computer-assisted)

=== IC COMPARISON ===
            Luo-Hou 2014          Hou 2022 FoCM
Amplitude   100                   12000
Radial      exp(−30(1−r²)⁴)      (1−r²)¹⁸
            peaked at r=1         peaked at r=0
L           1/6                   1
z-profile   sin(12πz)             sin(2πz)/(1+12.5sin²(πz))
Blowup at   (1,0) BOUNDARY       (0,0) INTERIOR
γ           5/2                   1
T*          0.0035056             0.00227648
Wall BC     no-flow+extrap        no-slip (NS)
