# Attempt 008 — Exact Z(β) for Minimal Lattice and Zero Structure

**Date**: 2026-04-07
**Phase**: 2 (Exploration)
**Track**: theory (Theory)

## Setup: SU(2) on 2⁴ Periodic Lattice

The simplest nontrivial case:
- d = 4, L = 2 (periodic boundary conditions)
- 2⁴ = 16 sites
- 4 × 16 = 64 links (but periodic BC identifies many)
  Actually: 2⁴ × 4 = 64 links, each carrying U ∈ SU(2)
- Plaquettes: 2⁴ × C(4,2) = 16 × 6 = 96 plaquettes

## Character Expansion

The Wilson action for SU(2):

  exp(β/2 · Re Tr(U_P)) = Σ_{j=0,1/2,1,...} (2j+1) · a_j(β) · χ_j(U_P)

where a_j(β) = I_{2j+1}(β) / I_1(β).

The partition function:

  Z(β) = ∫ ∏_{ℓ} dU_ℓ · ∏_P [Σ_j (2j+1) a_j(β) χ_j(U_P)]

After performing the link integrals using orthogonality:

  ∫ D^j_{mn}(U) D^{j'}_{m'n'}(U†) dU = δ_{jj'} δ_{mm'} δ_{nn'} / (2j+1)

The result is a sum over assignments of representations to plaquettes,
subject to constraints from shared links.

## The Combinatorial Structure

Each link ℓ is shared by 2(d-1) = 6 plaquettes (in d=4). The link integral
gives a "fusion" constraint: the representations on the plaquettes sharing
link ℓ must fuse consistently.

For SU(2), the fusion rules are the Clebsch-Gordan decomposition:
  j₁ ⊗ j₂ = |j₁-j₂| ⊕ |j₁-j₂|+1 ⊕ ... ⊕ (j₁+j₂)

The partition function becomes:

  Z(β) = Σ_{j_P} ∏_P [(2j_P+1) a_{j_P}(β)] · ∏_ℓ F(j_{P₁}, ..., j_{P₆})

where F is a combinatorial factor from the link integrals (related to
6j-symbols for the 6 plaquettes meeting at each link).

## Key Observation About Zeros

Each factor a_j(β) = I_{2j+1}(β) / I_1(β).

**Zeros of I_n(z)**:
- I_0(z): no real zeros, zeros at z = ±i·j_{0,k} where j_{0,k} are zeros of J_0
- I_n(z) for n ≥ 1: zero at z = 0, zeros at z = ±i·j_{n,k}
- ALL zeros are on the imaginary axis

So a_j(β) has:
- Zeros where I_{2j+1}(β) = 0: at β = i·j_{2j+1,k} (imaginary axis)
- Poles where I_1(β) = 0: at β = i·j_{1,k} (imaginary axis)

**The ratio a_j(β) has ALL its zeros and poles on the imaginary axis.**

## The Product Structure

Z(β) = Σ_config c_config · ∏_P a_{j_P}(β)

where c_config ≥ 0 (it's (2j+1) × combinatorial factor, which is a product
of dimensions and 6j-symbols squared — ALWAYS non-negative for SU(2)).

Wait — are the 6j-symbols squared? Let me think more carefully.

The link integral for SU(2) gives:

  ∫ D^{j₁}(U) ⊗ D^{j₂}(U) ⊗ ... ⊗ D^{j₆}(U†) dU

This is a product of Wigner 3j (or 6j) symbols, which CAN be negative.

So c_config is NOT necessarily non-negative. This means Z(β) is a sum with
MIXED SIGNS, and zeros on ℝ⁺ are not immediately excluded.

## The Critical Question

If c_config were all non-negative, then Z(β) would be a sum of positive
multiples of products of functions with imaginary-axis zeros. By a Lee-Yang
type argument, Z itself would have no zeros on ℝ⁺.

But c_config has mixed signs (from 6j-symbols), so the Lee-Yang argument
doesn't directly apply.

**However**: For the TRIVIAL representation j = 0, a_0(β) = 1 and
c_{all-trivial} = 1 (all plaquettes in trivial rep, all link integrals = 1).
This gives a constant term of 1 in Z(β).

So Z(β) = 1 + (sum of terms involving a_j(β) with j ≥ 1/2).

At strong coupling (small β): a_j(β) ~ (β/4)^{2j+1} → 0 for j ≥ 1/2.
So Z(β) ≈ 1 + O(β) > 0 near β = 0.

At weak coupling (large β): a_j(β) → 1 for all j, and Z(β) → Σ c_config × 1.
The sum Σ c_config > 0 because Z(β) > 0 for all real β > 0.

## Where This Attempt Fails

The mixed signs from 6j-symbols prevent a clean Lee-Yang argument.
The zeros of Z(β) in ℂ are determined by a complicated interplay between
Bessel functions and recoupling coefficients. Without a positivity property
of the recoupling coefficients, we can't control the zeros.

## But Wait — Gauge Invariance Helps

The character expansion of Z after ALL link integrals simplifies because
of the GAUGE INVARIANCE structure. The gauge-invariant combinations are
"spin foams" — closed surfaces colored by representations.

For a lattice with periodic BC, the partition function in the character
expansion is:

  Z = Σ_{spin foam F} ∏_{faces f∈F} (2j_f+1) a_{j_f}(β) · A(F)

where A(F) is the AMPLITUDE of the spin foam, which is a product of
6j-symbols over edges and 15j-symbols over vertices.

**Key structural fact**: For SU(2), the spin foam amplitudes A(F) satisfy
Regge symmetry and are related to the Ponzano-Regge model. The specific
signs and magnitudes are constrained by the representation theory.

**Question**: Is there a positivity property of spin foam amplitudes for SU(2)
that would enable a Lee-Yang argument?

This is a DEEP question connecting the mass gap to spin foam models and
topological quantum field theory. I don't know the answer.

## Result
The direct Lee-Yang approach hits a wall: 6j-symbols have mixed signs.
A spin-foam-level positivity property would resolve this.
The question "are spin foam amplitudes for SU(2) positive (or sign-definite)?"
is the key algebraic question to resolve.

This is a CLEAN, well-defined mathematical question that may have a known answer.

## Request for numerical track
Compute the exact partition function Z(β) for SU(2) on 2⁴ lattice in the
character expansion (truncated at j_max = 2). Plot |Z(β + iσ)| in the complex
plane. Locate the Fisher zeros. How close do they get to ℝ⁺?
