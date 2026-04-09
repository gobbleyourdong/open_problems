# NS Blowup — Mathematical Manifest
# All constants, equations, and validated results in one place.
# For cross-referencing with LLM peer review crew.

## THE EQUATIONS (Hou-Li Transform, Axisymmetric)

### Variables
u₁ = uθ/r       (angular velocity / r)
ω₁ = ωθ/r       (angular vorticity / r)
ψ₁ = ψθ/r       (stream function / r)

### Velocity reconstruction
uʳ = -r·ψ₁,z
uᶻ = 2ψ₁ + r·ψ₁,r

### Evolution equations
u₁:  ∂ₜu₁ + uʳ∂ᵣu₁ + uᶻ∂zu₁ = 2u₁ψ₁,z + ν·Δ₃u₁
ω₁:  ∂ₜω₁ + uʳ∂ᵣω₁ + uᶻ∂zω₁ = 2u₁u₁,z + ν·Δ₃ω₁

### Poisson coupling
-(∂ᵣᵣ + 3/r·∂ᵣ + ∂zz)ψ₁ = ω₁

### Laplacian
Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz    (5D Laplacian radial part)
L'Hôpital at r=0: Δ₃ → 4∂ᵣᵣ + ∂zz

### Stretching terms (the nonlinearity)
u₁ equation: +2u₁ψ₁,z     (u₁ amplifies itself through ψ₁)
ω₁ equation: +2u₁u₁,z      (u₁ creates vorticity)
NOTE: NO 1/r⁴ factor. Hou-Li transform removes coordinate singularity.

### The feedback loop
ω₁ → [Poisson] → ψ₁ → [velocity] → uᶻ → [advection+stretching] → ω₁
Loop gain > 1 → blowup. Loop gain < 1 → regularity.

## INITIAL CONDITIONS

### Luo-Hou 2014 (boundary blowup at r=1)
u₁(0) = 100·exp(-30(1-r²)⁴)·sin(12πz)
ω₁(0) = 0
Domain: r∈[0,1], z∈[0,L/4], L=1/6
BC r=0: ∂ᵣu₁=∂ᵣω₁=∂ᵣψ₁=0 (Neumann/symmetry)
BC r=1: ψ₁=0 (no-flow), 7th-order extrapolation for u₁,ω₁
BC z=0: u₁=ω₁=ψ₁=0 (odd)
BC z=L/4: u₁ even, ω₁,ψ₁ odd

### Hou 2022 (interior blowup at r=0)
u₁(0) = 12000·(1-r²)¹⁸·sin(2πz)/(1+12.5sin²(πz))
ω₁(0) = 0
Domain: r∈[0,1], z∈[0,1/2], L=1
BC r=1: u₁=0 (no-slip, naturally satisfied by (1-r²)¹⁸)
BC z=0,z=1/2: all odd (=0)
NOTE: (1-r²)¹⁸ → 0 at r=1 with 17 zero derivatives. Wall is irrelevant.

## VALIDATED CONSTANTS (from our solver, cross-checked against A100 and papers)

### Euler blowup (ν=0, Luo-Hou IC)
T* = 0.00365 (Nr=64)     [Paper: 0.00351, A100: 0.00365 ✓]
γ = 1.846 (Nr=64)         [Paper: 2.5]
γ = 2.790 (Nr=128, R²=0.997) [A100: 2.79 ✓]

### Amplitude scaling
T*·A = 0.366 ± 0.004      (invariant across A=50,100,200,500)
Equivalently: T* = 0.366/A

### Critical viscosity (Luo-Hou IC)
ν=0:     BLOWUP  T*=0.00365  γ=1.846   [A100 ✓ EXACT]
ν=1e-4:  BLOWUP  T*=0.00675  γ=0.699   [A100 ✓ EXACT]
ν=2e-4:  BLOWUP  T*=0.01914  γ=0.449   [A100 ✓ EXACT]
ν=3e-4:  BLOWUP  T*=0.02214  γ=0.509   [A100: SURVIVED — solver bias]
ν=5e-4:  BLOWUP  T*=0.02500             [A100: SURVIVED — solver bias]
ν=1e-3:  SURVIVED                        [A100: SURVIVED ✓]
ν=1e-2:  SURVIVED                        [A100: SURVIVED ✓]

ν_c(Spark) ∈ (5e-4, 1e-3)
ν_c(A100) ∈ (2e-4, 3e-4)
ν_c EXISTS on both platforms.

### Blowup delay with viscosity
T*(ν=0)   = 0.00365   (1.0×)
T*(ν=1e-4) = 0.00675  (1.85×)
T*(ν=2e-4) = 0.01914  (5.24×)
T*(ν=3e-4) = 0.02214  (6.07×)
T*(ν=5e-4) = 0.02500  (6.85×)

### γ evolution through blowup (PySR, Nr=64 Euler)
τ ∈ [4e-4, 2e-3]:  γ ≈ 2.18  (early)
τ ∈ [1e-4, 4e-4]:  γ ≈ 1.37  (mid)
τ ∈ [4e-5, 1e-4]:  γ ≈ 0.99  (late — self-similar)
τ ∈ [1e-5, 4e-5]:  γ ≈ 0.75  (very late)
Best PySR fit: log(1/τ)/τ (log-corrected inverse)

### γ evolution (Nr=128 Euler)
Early:     γ = 1.80  R²=0.977
Mid-early: γ = 1.08  R²=1.000
Mid:       γ = 1.02  R²=1.000  ← self-similar regime
Mid-late:  γ = 1.04  R²=1.000
Late:      γ = 0.86  R²=0.992

### Chen-Hou constants (from their profile data, verified)
c_l = 3.00649898     (spatial collapse rate)
c_ω = -1.02942516   (vorticity growth rate)
-c_l/c_ω = 2.9205600 (blowup exponent μ)
u_x(0) = -2.532674

### Enstrophy identity
dE/dt = S - ν·P
S = vortex stretching (grows E)
P = palinstrophy (shrinks E)
|S| ≤ 2·Ω·E  (stretching bound)

### BKM criterion
T* < ∞  ⟺  ∫₀^{T*} ‖ω‖_∞ dt = ∞

### Field convergence (no solver needed)
du₁/dz converges to 0.2% by Nr=64.
du₁/dr diverges as Nr² — wall BC artifact, not physics.

## THE PROOF TARGET

Prove: for the Hou 2022 IC with (1-r²)¹⁸ and ANY ν > 0,
the feedback loop gain G(ν, Z) > 1 for all vortex scales Z < Z₀,
where Z is the shear layer width. This implies:
- Enstrophy grows without bound
- BKM integral diverges
- Finite-time blowup

The loop gain is embedded in the coupling:
u₁ → [stretching 2u₁ψ₁,z] → ω₁ → [Poisson -Δ₃ψ₁=ω₁] → ψ₁ → [velocity] → u₁

Viscosity adds ν·Δ₃ to both equations but CANNOT reduce G below 1
for the interior IC because:
- Diffusion broadens the vortex core at r=0
- Broader core feeds MORE into the Poisson coupling
- The Poisson-mediated stretching INCREASES with broadening
- Net effect: viscosity ENHANCES interior blowup

## OPEN QUESTIONS FOR THE MATH CREW

1. Can the loop gain G be expressed as a closed-form function of ν and Z?
2. Is there a simple inequality showing G > 1 for the (1-r²)¹⁸ IC?
3. The Poisson coupling ψ₁ = -Δ₃⁻¹(ω₁) — what properties of this
   inverse operator make the feedback self-amplifying?
4. Can the oscillation at ν_c (damped vs growing envelope) be
   characterized as a bifurcation? What type?
5. The γ evolution (2.2→1.0→0.75) — does this correspond to known
   asymptotic regimes in the self-similar blowup literature?
