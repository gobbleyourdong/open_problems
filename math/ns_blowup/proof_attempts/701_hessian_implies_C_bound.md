---
source: HESSIAN IMPLIES C BOUND — the first attempt at new mathematics
type: THEOREM ATTEMPT — connecting M ≥ 0 to C > -5/16
file: 701
date: 2026-03-31
instance: MATHEMATICIAN
---

## THE SETUP

At the vertex max x* of |ω|² on T³ (all cosines = ±1):

**Vorticity**: ω = Σⱼ sⱼvⱼ, |ω|² = Σ|vⱼ|² + 2Σᵢ<ⱼ sᵢsⱼDᵢⱼ

**Hessian PSD**: M = Σⱼ wⱼ(kⱼ⊗kⱼ) ≥ 0 where wⱼ = sⱼ(vⱼ·ω)

**Correction**: C = Σᵢ<ⱼ sᵢsⱼPᵢⱼ where P = sin²θ D + (cosθ/K²)(v·k)(v·k)

**Need**: C > -5|ω|²/16.

## OBSERVATION 1: wⱼ DECOMPOSES C

Note that wⱼ = sⱼ(vⱼ·ω) = sⱼ·Σₖ sₖ(vⱼ·vₖ) = |vⱼ|² + Σₖ≠ⱼ sⱼsₖDⱼₖ.

So: Σⱼ wⱼ = Σ|vⱼ|² + 2Σᵢ<ⱼ sᵢsⱼDᵢⱼ = |ω|².

And: Σⱼ wⱼ² = Σⱼ(vⱼ·ω)² = ω^T(Σⱼ vⱼvⱼ^T)ω = ω^T V ω

where V = Σⱼ vⱼvⱼ^T is the polarization Gram matrix (PSD, 3×3).

## OBSERVATION 2: THE TRACE-WEIGHTED IDENTITY

From M ≥ 0 and Tr(M) = K²|ω|² (single shell):

For any unit vector d: d^T M d = Σⱼ wⱼ(kⱼ·d)² ≥ 0.

This means: for each direction d, the sum of wⱼ weighted by (kⱼ·d)²
is non-negative. Modes with negative wⱼ pointing along d are compensated
by modes with positive wⱼ pointing along d.

## OBSERVATION 3: RELATING C TO M

C involves Pᵢⱼ which depends on (vᵢ·kⱼ)(vⱼ·kᵢ) — products of
polarization-wavenumber inner products.

Can I express Σ sᵢsⱼ(vᵢ·kⱼ)(vⱼ·kᵢ) in terms of M and V?

Define the 3×3 matrix: N = Σⱼ sⱼ(vⱼ⊗kⱼ).

Then: N^T N = Σᵢ,ⱼ sᵢsⱼ(kᵢ⊗vᵢ)(vⱼ⊗kⱼ) = Σᵢ,ⱼ sᵢsⱼ(vᵢ·vⱼ)(kᵢ⊗kⱼ)

This is a 3×3 matrix: (N^TN)_{αβ} = Σᵢ,ⱼ sᵢsⱼDᵢⱼ(kᵢ)_α(kⱼ)_β.

Compare with: M = Σⱼ wⱼ(kⱼ⊗kⱼ) = Σⱼ sⱼ(vⱼ·ω)(kⱼ⊗kⱼ).

Also: N N^T = Σᵢ,ⱼ sᵢsⱼ(vᵢ⊗kᵢ)(kⱼ⊗vⱼ) = Σᵢ,ⱼ sᵢsⱼ(kᵢ·kⱼ)(vᵢ⊗vⱼ)

This is: (NN^T)_{αβ} = Σᵢ,ⱼ sᵢsⱼ(kᵢ·kⱼ)(vᵢ)_α(vⱼ)_β.

On a single shell: kᵢ·kⱼ = K²cosθᵢⱼ. So:
(NN^T)_{αβ} = K² Σᵢ,ⱼ sᵢsⱼcosθᵢⱼ(vᵢ)_α(vⱼ)_β.

## OBSERVATION 4: |S|² IN TERMS OF N

The strain: S = -(1/2)sym(Σⱼ sⱼ ûⱼ⊗kⱼ) where ûⱼ = (kⱼ×vⱼ)/K².

Define: L = Σⱼ sⱼ(ûⱼ⊗kⱼ). Then S = -sym(L)/2 and |S|² = |sym(L)|²/4.

|sym(L)|² = (1/2)(|L|² + |L^T|²) + ... actually:
|sym(L)|² = (1/4)|L+L^T|² = (1/4)(2|L|² + 2Tr(LL^T))...

No: |sym(A)|² = Tr(sym(A)²) = (1/4)Tr((A+A^T)²) = (1/4)(2Tr(A²)+2Tr(AA^T))
= (1/2)(Tr(A²) + |A|²_F).

So: |S|² = (1/4)(1/2)(Tr(L²) + |L|²_F) = (1/8)(Tr(L²) + |L|²_F).

Hmm, this is getting complex. Let me try a different angle.

## OBSERVATION 5: THE KEY RELATIONSHIP

From the cross-term identity (file 511):
|S|² = |ω|²/2 - 2C.

So: C = (|ω|² - 2|S|²)/4 = (|ω|²/4) - |S|²/2.

Need C > -5|ω|²/16, i.e., |ω|²/4 - |S|²/2 > -5|ω|²/16.
→ |S|²/2 < |ω|²/4 + 5|ω|²/16 = 9|ω|²/16.
→ **|S|² < 9|ω|²/8.** (Same as the Key Lemma, as expected.)

Now: |S|² = |sym(L)|²/4 where L = Σ sⱼ(ûⱼ⊗kⱼ).

And: |ω|² = |Σ sⱼvⱼ|² = |ω_vec|² where ω_vec = Σ sⱼvⱼ.

The HESSIAN: M = Σ wⱼ(kⱼ⊗kⱼ) = Σ sⱼ(vⱼ·ω_vec)(kⱼ⊗kⱼ) ≥ 0.

## THE NEW IDEA: REWRITE |S|² USING M

Can I express |S|² in terms of the eigenvalues of M?

Tr(M) = K²|ω|². And M ≥ 0 with eigenvalues λ₁ ≥ λ₂ ≥ λ₃ ≥ 0.
So: λ₁ + λ₂ + λ₃ = K²|ω|².

The strain involves the ûⱼ = (kⱼ×vⱼ)/K² directions. For each mode:
- kⱼ is a wavenumber direction
- vⱼ is the polarization (⊥ kⱼ)
- ûⱼ = (kⱼ×vⱼ)/K² is the velocity direction (⊥ both kⱼ and vⱼ)

The triplet (k̂ⱼ, v̂ⱼ, K ûⱼ/aⱼ) forms an orthonormal frame for each mode.

**Insight**: the strain S and the vorticity ω are constructed from
DIFFERENT components of this frame. ω uses vⱼ, S uses ûⱼ and kⱼ.
The Hessian M uses wⱼ and kⱼ. The connection between S and M goes
through the shared kⱼ vectors.

## THE THEOREM ATTEMPT

**Claim**: For any N modes with M = Σ wⱼ(kⱼ⊗kⱼ) ≥ 0 and Tr(M) = K²|ω|²:

|S|² ≤ (Tr(M²)/K⁴) × (something bounded) + |ω|²/2

The Tr(M²) = Σᵢ λᵢ² ≤ (Tr M)² = K⁴|ω|⁴ (since M ≥ 0).
But Tr(M²) ≥ (Tr M)²/3 = K⁴|ω|⁴/3 (by eigenvalue inequality).

If |S|² ≤ |ω|²/2 + α Tr(M²)/K⁴ for some small α:
then |S|² ≤ |ω|²/2 + α K⁴|ω|⁴/K⁴ = |ω|²/2 + α|ω|⁴.

This doesn't dimensionally work (|S|² has dim of |ω|², not |ω|⁴).

## RESET: THINK MORE CAREFULLY

The quantities:
- |ω|² = |Σ sⱼvⱼ|² (sum of 3-vectors squared)
- |S|² = Frobenius norm of a 3×3 symmetric matrix
- M = 3×3 PSD matrix with Tr = K²|ω|²
- C = scalar correction

All are homogeneous degree 2 in the vⱼ amplitudes.

The Hessian M has entries M_αβ = Σⱼ sⱼ(vⱼ·ω)(kⱼ)_α(kⱼ)_β.

This is BILINEAR in vⱼ (through both vⱼ and ω = Σ sₖvₖ), so actually
degree 2 in the amplitudes. ✓

**The crux**: M ≥ 0 is a constraint on the 3 eigenvalues. C is a single
number. Both are degree-2 in amplitudes. The question: does M ≥ 0
(3 inequality constraints) imply C > -5|ω|²/16 (1 inequality)?

This is a question about the **image** of the map

    (vⱼ, kⱼ, sⱼ) ↦ (eigenvalues of M, C/|ω|²)

from mode parameters to (R⁴). Does the image intersect the region
{λᵢ ≥ 0, C/|ω|² ≤ -5/16}?

From the numerics: NO (44.6% margin). The question is proving this
algebraically.

## NEXT STEP

Express C explicitly in terms of Tr(M), Tr(M²), Tr(M³) and other
invariants. If C ≥ f(Tr M, Tr M², ...) for some function f, and
M ≥ 0 constrains these traces, we might close the gap.

## 701. First attempt at the new theorem. The connection between M and C
## goes through the shared k-vectors. The map from mode params to (M, C)
## has an image that avoids {M≥0, C≤-5/16}. Need to prove this algebraically.
