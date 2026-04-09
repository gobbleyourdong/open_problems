---
source: MILLER FRAMEWORK — the strain-vorticity orthogonality identity
type: KEY IMPORT — the most important new tool from the literature
file: 824
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE MILLER IDENTITY (2026, Pure and Applied Analysis)

For any divergence-free u on T³:

    ⟨-ΔS, ω⊗ω⟩ = 0

where S = sym(∇u), ω = curl u, and the inner product is L²(T³).

PROOF: Integration by parts + div(ω)=0 + triple product vanishing.
Works on T³ verbatim (no boundary terms needed).

## THE MODEL EQUATION (global regularity PROVEN)

Miller's μ-NS model: d_t S - ΔS - (1/2)P_st(ω⊗ω) + μP_st(S²+(3/4)ω⊗ω) = 0

At μ=0: GLOBAL REGULARITY. The model retains the strain-vorticity
interaction (the term that drives enstrophy growth) but drops the
self-amplification and advection.

The SAME enstrophy identity as full NS:
    d/dt ‖S‖² = -2‖S‖²_{H¹} - 4∫det(S)

The cubic det(S) is the SOLE driver of potential blowup.

## THE REGULARITY CRITERION (Theorem 1.9)

Define Q = P_st((u·∇)S + S² + (3/4)ω⊗ω).

If T_max < ∞ (blowup), then:

    limsup_{t→T_max} ‖Q‖_{L²} / ‖-ΔS‖_{L²} ≥ 1

EQUIVALENTLY: if ‖Q‖ < ‖-ΔS‖ for all time → REGULARITY.

## KEY ORTHOGONALITIES

1. ⟨-ΔS, ω⊗ω⟩ = 0 (Miller identity)
2. ⟨S² + (3/4)ω⊗ω, S⟩ = 0 (Proposition 1.1)
3. ⟨(u·∇)S, S⟩ = 0 (divergence-free transport)

All three components of Q are orthogonal to S in L². They DON'T
contribute to enstrophy growth — they only REDISTRIBUTE strain energy.

## THE CHAIN: KEY LEMMA + MILLER → REGULARITY?

Our Key Lemma: S²ê < (3/4)|ω|² at x* (pointwise, at vorticity max).
Miller's criterion: ‖Q‖ < ‖-ΔS‖ (global L² ratio).

The GAP: convert pointwise constraint at x* to global L² ratio.

If we could show:
(a) The Key Lemma constrains how S² and ω⊗ω align globally
(b) This alignment forces ‖P_st(S²+(3/4)ω⊗ω)‖ to be controlled by ‖-ΔS‖
(c) The advection (u·∇)S partially cancels the self-amplification
→ ‖Q‖ < ‖-ΔS‖ → REGULARITY

## THE CRITICAL OBSERVATION

From ⟨S²+(3/4)ω⊗ω, S⟩ = 0: the tensor S²+(3/4)ω⊗ω is PERPENDICULAR
to S in the L² inner product of symmetric trace-free tensors.

This means: P_st(S²+(3/4)ω⊗ω) ⊥ S. It lives in the ORTHOGONAL
COMPLEMENT of S within the strain space.

Similarly: ⟨(u·∇)S, S⟩ = 0, so the advection projection is also ⊥ S.

Both components of Q are perpendicular to S. And from Miller's identity:
⟨-ΔS, ω⊗ω⟩ = 0, so -ΔS has zero projection onto ω⊗ω.

The geometry in L²(T³; Sym₀(R³)):
- S lies in some direction
- Q ⊥ S (Q doesn't change ‖S‖)
- -ΔS has zero ω⊗ω component (Miller)
- We need ‖Q‖ < ‖-ΔS‖

## THE STRAIN EIGENFUNCTION CRITERION (Theorem 1.12)

Blowup requires: ∫₀^{T*} inf_ρ ‖-ρΔS - S‖² dt = ∞

i.e., S must deviate infinitely far from being a Laplacian eigenfunction.
If S concentrates on a SINGLE Fourier shell: inf_ρ = 0, no blowup.
Blowup requires energy spread across MANY scales simultaneously.

CONNECTION TO FLOOR GROWTH: If the SOS floor growth holds (f(N) → 0):
the strain at the argmax becomes negligible. This means the strain
is increasingly dominated by LOW modes (few active scales), which
pushes it TOWARD being a Laplacian eigenfunction. This would satisfy
the eigenfunction criterion → no blowup.

## THE SYNTHESIS

Miller's framework says: the problem reduces to controlling ONE L² ratio.
Our Key Lemma controls the pointwise behavior at the vorticity max.
The gap: local-to-global propagation of the strain constraint.

The floor growth (f(N) → 0) would make S negligible near the max,
pushing S toward eigenfunction structure (single-scale), which
satisfies Miller's eigenfunction criterion.

The chain: Key Lemma → floor growth → eigenfunction concentration → Miller → regularity

This is a DIFFERENT chain than file 815! It goes through Miller's
eigenfunction criterion instead of through the ODE exponent argument.

## WHAT THIS CHANGES

The gap is NO LONGER "prove depletion of nonlinearity."
The gap is: "prove that the strain near a Type I singularity cannot
spread across infinitely many Fourier scales."

This is a SPECTRAL CONCENTRATION problem, not a pointwise depletion problem.

On T³ with discrete Fourier modes: spectral concentration is naturally
constrained by the lattice structure and the Gevrey analyticity.

The SOS floor growth (f(N) → 0) means: with more active modes, the
strain becomes negligible at the max. This IS spectral concentration
(the strain energy concentrates on the modes that DON'T contribute
at the vorticity maximum).

## 824. Miller's framework: regularity ↔ ‖Q‖ < ‖-ΔS‖.
## Key identity: ⟨-ΔS, ω⊗ω⟩ = 0 (strain diffusion ⊥ vorticity).
## Model equation (no advection/self-amp): globally regular.
## Eigenfunction criterion: blowup requires spectral spread of strain.
## New chain: Key Lemma → spectral concentration → Miller → regularity.
## This is a SPECTRAL problem, not a pointwise depletion problem.
