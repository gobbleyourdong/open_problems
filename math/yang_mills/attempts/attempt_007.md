# Attempt 007 — Fisher Zeros: The Complex Analysis Route

**Date**: 2026-04-07
**Phase**: 2 (Exploration)
**Instance**: Even (Theory)

## The Idea

The partition function Z(β) = ∫ ∏ dU exp(-β S_W[U]) is an entire function
of β ∈ ℂ (finite lattice: finite-dimensional integral of an entire integrand).

Its zeros {β_i} in the complex plane are the **Fisher zeros**.

**Key fact**: Z(β) > 0 for all real β > 0 (integrand strictly positive).
So all Fisher zeros have Im(β) ≠ 0 or Re(β) ≤ 0.

**The mass gap connection**:
- If Fisher zeros accumulate on a point β* ∈ ℝ⁺ as V → ∞, then f(β) has a
  singularity at β* → phase transition → mass gap could vanish.
- If Fisher zeros stay at distance ≥ δ > 0 from ℝ⁺ uniformly in V, then
  f(β) is analytic → no phase transition → mass gap for all β.

## Why This Might Work for SU(N)

### The Abelian contrast: U(1) in d=4
U(1) lattice gauge theory in d=4 HAS a phase transition (Coulomb → confined).
Fisher zeros DO approach the real axis at β_c ≈ 1.01.
The reason: U(1) has a fundamentally different group structure — the
representation ring is Z (integers), not the finite branching of SU(N).

### SU(N) in d=4: why it's different
The non-Abelian structure imposes constraints:
1. **No local order parameter**: Elitzur's theorem says local gauge symmetry
   cannot break spontaneously. The transition in U(1) is driven by monopole
   condensation — a topological mechanism absent in SU(N) (π₁(SU(N)) = 0).
2. **Center symmetry**: SU(N) has center Z(N). The Polyakov loop transforms
   under Z(N). At zero temperature (infinite temporal extent), center symmetry
   is never broken for d=4 SU(N) — this is the confinement criterion.
3. **Asymptotic freedom**: The coupling flows to zero at short distances,
   meaning the theory becomes free in the UV. This is a SMOOTHING mechanism
   that prevents the UV modes from driving a phase transition.

### The structural conjecture
**Conjecture**: For SU(N) with N ≥ 2 in d=4, the Fisher zeros of Z_V(β) satisfy:

  dist(β_i, ℝ⁺) ≥ c(N) > 0  uniformly in V

where c(N) depends only on N (and possibly d).

## How to Prove It

### Strategy 1: Polymer Expansion (Strong Coupling)
At strong coupling (small β), the cluster/polymer expansion gives:

  ln Z(β) = V · f_0 + Σ_γ z(γ, β)

where γ are polymers (connected clusters of plaquettes) and z(γ, β) is the
polymer activity. The series converges absolutely for |β| < β_c(polymer).

If the polymer expansion converges in a DISK |β| < R in ℂ, then Z has no
zeros in that disk. This gives Fisher zeros bounded away from [0, R).

**Known**: Osterwalder-Seiler proved convergence for small real β. The complex
extension should give convergence in a disk of radius ~ the same β_c.

### Strategy 2: Weak Coupling / Perturbative Expansion
At large β (weak coupling), asymptotic freedom gives:

  Z(β) ~ Z_free · (1 + Σ_n c_n / β^n)

The perturbative series diverges (asymptotic), but Borel summability might
give analyticity in a sector. If the Borel sum is non-zero in a sector
{β : |arg(β)| < π/2 + ε, |β| > R}, then Fisher zeros are excluded from
that sector.

**Known**: Asymptotic freedom has been proven for the perturbative coefficients.
Borel summability for YM₄ is NOT proven (it would essentially solve the problem).

### Strategy 3: Interpolation
If Strategy 1 gives a zero-free disk {|β| < R₁} and Strategy 2 gives a
zero-free sector {|β| > R₂, |arg β| < θ}, then for R₁ > R₂ we cover ℝ⁺.

**The gap**: R₁ and R₂ are likely NOT overlapping with current technology.
This is the strong-weak interpolation problem.

### Strategy 4: Direct Bound on Z(β + iσ)
Prove |Z(β + iσ)| > 0 for all real β > 0, σ ∈ ℝ, σ ≠ 0.

Z(β + iσ) = ∫ exp(-(β+iσ) S_W) dμ = ∫ exp(-β S_W) exp(-iσ S_W) dμ

This is the Fourier transform of the action distribution:
Z(β + iσ) = Z(β) · ⟨exp(-iσ S_W)⟩_β

So we need: ⟨exp(-iσ S_W)⟩_β ≠ 0, i.e., the characteristic function of S_W
under the Boltzmann measure at coupling β never vanishes.

**When does a characteristic function vanish?**
For the NORMAL distribution: φ(σ) = exp(-σ²/2) — never zero.
For UNIFORM on [0,1]: φ(σ) = sin(σ)/σ — zeros at σ = nπ.
For lattice gauge theory: the action S_W has a BOUNDED range [0, S_max].
The characteristic function of a bounded random variable is ENTIRE and
CAN have zeros.

**But**: The action distribution is NOT uniform. At strong coupling, it's
concentrated near S_max (all plaquettes disordered). At weak coupling,
concentrated near 0 (all plaquettes ≈ identity). The specific structure
of the distribution matters.

### Strategy 5: Representation-Theoretic
Use the character expansion to write Z exactly:

  Z = Σ_{configurations of irreps on plaquettes} ∏_P d_R a_R(β)
      × (combinatorial factor from link integrals)

Each a_R(β) = I_{dim(R)}(β) / I_1(β) is a ratio of Bessel functions.
The zeros of Z in ℂ are determined by the zeros of this combinatorial sum.

For SU(2), a_j(β) = I_{2j+1}(β) / I_1(β). These are entire functions of β
with known zeros (zeros of Bessel functions lie on the imaginary axis).

**Key observation**: The zeros of Bessel functions I_n(z) are ALL on the
imaginary axis: I_n(iσ) = i^n J_n(σ), and J_n has real zeros.

So a_j(β) has zeros when I_{2j+1}(β) = 0, which happens when β = iσ_k
where σ_k are zeros of J_{2j+1}. These are on the IMAGINARY axis.

**If Z is built from products/sums of functions whose zeros are on the
imaginary axis, can the zeros of Z wander to the real axis?**

For the Lee-Yang theorem (Ising model), the answer is NO — the zeros of
Z(h) = Σ exp(-βH + hM) stay on the unit circle |e^h| = 1. The proof uses
the fact that each spin contributes a factor whose zeros are on the unit circle,
and products/sums of such functions preserve this property.

**The Yang-Mills analog**: Can we prove that the character expansion
preserves a zero-free region? This would be a representation-theoretic
Lee-Yang theorem for gauge theories.

## Assessment

Strategy 5 (representation-theoretic) is the most novel and the most
suited to the Even instance. The character expansion gives an EXACT
representation of Z as a sum of products of Bessel function ratios.
If we can prove that this sum has no zeros on ℝ⁺, we win.

The key question: **Is there a Lee-Yang type theorem for character expansions
of lattice gauge theories?**

This is a new question. I don't think it's been asked in this form before.
The Ising model Lee-Yang theorem relies on the "multiaffine" property of Z.
The gauge theory Z has a similar structure via the character expansion.

## Next Steps (Even Instance)
1. Write out Z in character expansion for SU(2) on a minimal lattice
2. Study the zero structure of this exact Z(β)
3. Look for the structural property that keeps zeros off ℝ⁺
4. Attempt to prove a Lee-Yang type theorem for the character expansion

## Next Steps (Odd Instance)
1. Compute Fisher zeros of Z(β) for SU(2) on 2⁴, 3⁴ lattices
2. Plot zeros in the complex β plane
3. Track the closest zero to ℝ⁺ as lattice size increases
4. Does the gap δ = min dist(β_i, ℝ⁺) increase, decrease, or stabilize?

## Result
Fisher zeros approach fully developed. Five strategies identified.
Strategy 5 (representation-theoretic Lee-Yang analog) is the most promising
novel contribution. Key question: does the character expansion preserve
a zero-free half-plane?
