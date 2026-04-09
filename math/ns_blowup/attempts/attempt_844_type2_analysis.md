# Attempt 844 — Type II Blowup: What Would It Look Like?

**Date**: 2026-04-08
**Instance**: Both (theory + numerics)

## The Anti-Problem for NS

The systematic approach says: frame the anti-problem. What would a COUNTEREXAMPLE
to NS regularity look like?

### Self-Similar (Type I): RULED OUT
|u(x,t)| ~ C/√(T-t). The rescaled solution is STATIONARY in self-similar
variables. The ODE balance forces the profile to be in L³ → trivial → no blowup.

### Type II: THE REMAINING THREAT
|u(x,t)| grows FASTER than C/√(T-t). Blowup rate (T-t)^{-α} with α > 1/2.

Properties a Type II blowup MUST have:
1. **Super-critical growth**: α > 1/2 (faster than self-similar)
2. **Non-stationary in self-similar variables**: the rescaled solution
   MOVES (oscillates, drifts, or cascades)
3. **Energy bounded**: ||u(t)||_{L²} ≤ ||u₀||_{L²} (energy inequality)
4. **BKM**: ∫₀ᵀ ||ω||_∞ dt = ∞ (vorticity integral diverges)

### What Constrains Type II?

**Constraint 1**: The blowup rate cannot exceed |u| ~ C/(T-t) (Type I bound).
For α > 1: Seregin (2012) shows this implies L³-regularity → contradiction.
So α ∈ (1/2, 1] for Type II.

Actually: Type II means the TYPE I RATE doesn't hold, i.e., 
sup_x |u(x,t)| × (T-t)^{1/2} → ∞ as t → T. But the pointwise rate
can be anything > 1/2.

**Constraint 2**: Cheskidov-Dai-Palasek (2025): Type I blowup requires
energy inequality VIOLATION. So Type I is excluded on T³ without even
the profile analysis. But Type II doesn't require energy violation.

**Constraint 3**: The critical ratio R = |∫ωSω|/∫|∇ω|² must approach or
exceed 1 for blowup. At all tested Re: R ≈ 0 (diffusion-dominated).
A Type II blowup would need R → 1 at an EXTREMELY concentrated vortex.

### The Concentration Scenario

A Type II blowup concentrates vorticity at a point while the total
enstrophy might remain bounded. The vorticity direction ξ = ω/|ω|
must align with the LARGEST eigenvector of S (for maximum stretching).

From the NS analysis (839 attempts): the dynamics PUSH ξ toward the
INTERMEDIATE eigenvector of S (Vieillefosse mechanism). This is the
ANTI-stretching direction. The Type II blowup must OVERCOME this
mechanism — it needs a NONLOCAL effect (pressure) to maintain alignment.

### The Pressure Hessian

The pressure p satisfies Δp = -Tr(S²) + |ω|²/2. Near a vorticity
concentration: p has a negative Laplacian (suction toward the vortex).
The pressure Hessian H_p acts on the vorticity direction equation.

The deviatoric part of H_p (the Calderon-Zygmund operator) can ROTATE
ξ toward the largest eigenvector. This is the ONLY mechanism that could
sustain Type II blowup against the Vieillefosse restoring force.

### The Number for Type II

Define: Ψ(t) = sup_x |ω(x,t)| × ||∇ξ(x,t)||⁻¹ (coherence length).

For Type II blowup: Ψ must DECREASE (the coherence length shrinks as
vorticity concentrates). The BKM criterion: ∫||ω||_∞ dt = ∞ means
||ω||_∞ grows faster than 1/(T-t).

The COMPUTABLE test: track Ψ(t) in DNS. If Ψ stays bounded below:
the vorticity direction stays coherent → anti-stretching mechanism active
→ no Type II.

If Ψ → 0: the direction DECOHERENCES rapidly → possible blowup.

### What the numerical track Should Compute

Track these diagnostics in the Taylor-Green simulation at high Re:
1. R(t) = |∫ωSω|/∫|∇ω|² (critical ratio)
2. Ψ(t) = max|ω| / max|∇ξ| (coherence length)
3. α(t) = ê·S·ê / |ω| (stretching ratio, from the 842 NS attempts)
4. The ALIGNMENT: angle between ω and e₁, e₂, e₃ of S

These diagnostics would show EARLY SIGNS of Type II if it exists.

## 844. Type II is the remaining threat. Must overcome Vieillefosse.
## Needs CZ pressure Hessian to maintain alignment. Track Ψ(t), R(t), α(t).
## GPU simulation at Re=5000+ needed for the interesting regime.
