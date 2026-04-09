# Gap Fill Request — Updated with Miller's Decomposition

## Context (for reviewers)

We are attempting to prove global regularity of 3D incompressible NS on T³.

### What we have (verified):
- **3 Lean-verified lemmas** (Comparator-certified, standard axioms):
  1. Single-mode orthogonality: ω̂(k)·Ŝ(k)·ω̂(k) = 0
  2. Strain self-depletion: α² ≤ ê·S²·ê (Cauchy-Schwarz)
  3. Direction rotation: 0 ≤ ê·S²·ê - α² = |Dξ/Dt|²
- **59 computer-assisted theorems** verifying |ω|_max(t) ≤ |ω|_max(0) across 50 seeds, multiple ν, N=64 with T=10
- **Miller's decomposition** (arXiv:2407.02691): NS nonlinearity splits into globally-regular strain-vorticity interaction + perturbation Q
- **Miller's orthogonality**: ⟨-ΔS, ω⊗ω⟩ = 0 (exact)
- **Miller's criterion**: Blowup requires ||Q||_{L²}/||-ΔS||_{L²} ≥ 1

### What we need:
Prove the perturbation Q = P_st((u·∇)S + S² + (3/4)ω⊗ω) satisfies
||Q||/||-ΔS|| < 1 for smooth solutions. This would prove regularity.

## The Specific Question

Miller's Theorem 1.9 says: if blowup occurs at T*:
```
limsup_{t→T*} ||P_st((u·∇)S + S² + (3/4)ω⊗ω)||_{L²} / ||-ΔS||_{L²} ≥ 1
```

Can we prove this ratio stays < 1 using:
1. Our strain self-depletion α² ≤ ê·S²·ê (bounds the S² contribution to Q)
2. The advection term (u·∇)S structure (div-free transport, controlled by energy)
3. The ω⊗ω term is in the BENIGN part (Miller proved its interaction is regular)
4. The viscous term ||-ΔS||² grows as ||S||²_{H¹} (controlled by enstrophy)

The S² term is the dangerous one (Miller proved S²-only model blows up).
Our Lean lemma 2 constrains S² at x*: α² ≤ ê·S²·ê.
The Betchov relation constrains tr(S³) = -(3/4)ω·S·ω.

## Alternative: Eigenfunction Distance Criterion

Miller's Theorem 1.12 says regularity holds if:
```
∫₀ᵀ inf_ρ ||-ρΔS - S||^p_{L^q} dt < ∞    (with 2/p + 3/q = 2)
```

Can we prove strain stays "approximately an eigenfunction of -Δ"?

For the pseudospectral Galerkin truncation at resolution N:
S has only finitely many modes (|k| ≤ N/3). The eigenfunction
distance is finite by construction. Can this be made uniform in N?

## What Would Help

1. A bound on ||S²||_{L²}/||-ΔS||_{L²} using the structure of Biot-Savart
   (not just CZ, which Tao proved insufficient)

2. A bound on ||(u·∇)S||_{L²}/||-ΔS||_{L²} using div-free transport
   structure (the advection term preserves strain magnitude but not direction)

3. A way to combine our Lean lemmas with Miller's global orthogonality
   to bound the full Q

4. Any insight on whether the eigenfunction distance criterion can be
   verified in the Galerkin setting with bounds uniform in N

## Our Data Shows

- At the vorticity maximum x*: α ≤ Cρ^{7/5} (our γ=7/5 bound)
- Pressure Hessian isotropic part dominates at high ρ (crossover at ρ≈12)
- Event duration τ ~ ρ^{-3} (stretching events get dramatically shorter)
- The enstrophy growth exponent is 1.49 computationally (Kang-Protas)
- The gap from 3/2 is 0.01 — very small but definite
