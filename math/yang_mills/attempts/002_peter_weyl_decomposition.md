---
source: PETER-WEYL DECOMPOSITION — the "Fourier modes" of Yang-Mills
type: ANALYSIS — algebraic structure of lattice YM in representation basis
file: 002
date: 2026-04-07
instance: ODD (Opus)
---

## MOTIVATION

In NS on T³, the proof architecture depended on decomposing velocity/vorticity
into Fourier modes and finding algebraic identities (Frobenius cross-term,
K/D=1/2 regression) in the mode basis. The Key Lemma was a finite-dimensional
statement about N-mode configurations.

For Yang-Mills on the lattice, the analogous decomposition is PETER-WEYL:
expand functions on the gauge group G into matrix coefficients of irreducible
representations. This turns the infinite-dimensional path integral into a sum
over representation labels.

## PETER-WEYL THEOREM

For G compact (e.g., SU(2)):

    L²(G) = ⊕_j (2j+1) · V_j

where j = 0, 1/2, 1, 3/2, ... labels irreducible representations of SU(2),
V_j has dimension (2j+1), and the multiplicity is (2j+1).

Concretely: any f ∈ L²(SU(2)) can be expanded as

    f(U) = Σ_j (2j+1) Tr(f̂_j · D^j(U))

where D^j(U) is the (2j+1)×(2j+1) Wigner D-matrix and f̂_j is the
Fourier coefficient matrix.

## CHARACTERS

The character of representation j:

    χ_j(U) = Tr(D^j(U))

For SU(2) with U = exp(iθ n̂·σ/2):

    χ_j(U) = sin((2j+1)θ) / sin(θ)

Characters are class functions (depend only on conjugacy class = angle θ).
They satisfy orthogonality: ∫ χ_j(U) χ_k(U)* dU = δ_{jk}.

## WILSON ACTION IN REPRESENTATION BASIS

The Wilson plaquette operator:

    (1/2) Re Tr(U_p) = (1/2) Re χ_{1/2}(U_p)

This is a function of the plaquette holonomy U_p ∈ SU(2).

Using character expansion:

    exp(β · (1/2) Re Tr(U_p)) = Σ_j d_j · a_j(β) · χ_j(U_p)

where d_j = 2j+1 and a_j(β) are the expansion coefficients:

    a_j(β) = (1/d_j) ∫ exp(β · (1/2) Re Tr(U)) · χ_j(U) dU

For SU(2), these are modified Bessel functions:

    a_j(β) = I_{2j+1}(β) / I_1(β)

(up to normalization). Key properties:
- a_0(β) = 1 (trivial representation)
- a_j(β) ~ (β/(4j+2))^{2j+1} for β → 0 (strong coupling: higher reps suppressed)
- a_j(β) → 1 for β → ∞ (weak coupling: all reps contribute equally)

## THE REPRESENTATION-THEORETIC PARTITION FUNCTION

After expanding each plaquette Boltzmann weight in characters and integrating
over link variables using orthogonality:

    Z = Σ_{j_p} ∏_p d_{j_p} a_{j_p}(β) · (coupling coefficients)

The coupling coefficients come from integrating products of D-matrices over
shared links. For a single link shared by plaquettes p₁,...,p_k:

    ∫ D^{j_1}(U) ⊗ D^{j_2}(U) ⊗ ... ⊗ D^{j_k}(U) dU

This is a tensor product integral — it equals a product of Clebsch-Gordan
coefficients (3j, 6j, 9j, ... symbols depending on the lattice topology).

## THE KEY STRUCTURE

On a 4D hypercubic lattice, each link is shared by 6 plaquettes.
The link integral gives a 6j-symbol (or product of 3j-symbols).

The partition function becomes:

    Z = Σ_{j_p} ∏_p d_{j_p} a_{j_p}(β) · ∏_links {6j-symbol}

This is a STATE SUM MODEL (like Turaev-Viro in 3D topology).

## ANALOGY TO NS FOURIER DECOMPOSITION

| NS on T³ | YM on lattice |
|-----------|---------------|
| Fourier mode k ∈ Z³ | Representation label j ∈ {0,1/2,1,...} |
| Amplitude a_k | Plaquette rep weight a_j(β) |
| Mode count N | Max representation j_max |
| Polarization v_k ⊥ k_k | Clebsch-Gordan coupling (geometry) |
| Biot-Savart coupling | 6j-symbol (angular momentum recoupling) |
| Key Lemma: Q > 0 at argmax | Mass gap: spectral gap > 0 in transfer matrix |
| SOS certificates over modes | ? certificates over representations |

## THE TRANSFER MATRIX IN REP BASIS

For a lattice with one "time" direction (length T) and spatial volume L³:

The transfer matrix T acts on states ψ(j_{spatial links}).
In the strong-coupling expansion (β small):

    T ≈ I + β · Σ_{spatial plaquettes} (plaquette operator) + O(β²)

The plaquette operator in rep basis is a RAISING/LOWERING operator on j labels
(it changes j by ±1/2 via the fusion rules of SU(2)).

The ground state at β = 0: all j = 0 (trivial representation everywhere).
The first excited state: one plaquette with j = 1/2.
The gap: Δ(β=0) = -ln(a_{1/2}(β)) ≈ ln(1/β) → ∞ (infinite gap at β=0).

At β → ∞ (continuum limit): a_j(β) → 1 for all j. Gap → 0 in lattice units.
But in PHYSICAL units: Δ_phys = Δ_lattice / a, and a → 0 as β → ∞.
The question: does Δ_phys = Δ_lattice / a → finite positive limit?

## WHAT TO COMPUTE

### 1. Character expansion coefficients a_j(β) for SU(2)
These are known analytically (Bessel functions). Tabulate and verify.

### 2. 6j-symbols for SU(2)
The Racah-Wigner coefficients. Known closed form (Racah formula).
For small j (j ≤ 10): enumerate all and tabulate.

### 3. Transfer matrix in truncated rep basis
Truncate at j_max. The transfer matrix becomes a FINITE matrix.
For j_max = 2 on a 2³ spatial lattice:
  - Number of spatial links: 3 × 2³ = 24
  - Each link has j ∈ {0, 1/2, 1, 3/2, 2} = 5 values
  - Hilbert space dimension: 5^24 ≈ 6 × 10^16 (TOO LARGE)

Need to use gauge invariance to reduce: at each vertex, the representations
on the 6 adjacent links must satisfy coupling rules (the vertex is a
6j-symbol). This dramatically reduces the effective dimension.

For a 2³ lattice with gauge fixing:
  - Vertices: 8. Links: 24. Independent DOF after gauge fixing: 24 - 8 + 1 = 17.
  - With j_max = 1: 3^17 ≈ 1.3 × 10^8. FEASIBLE on GPU.
  - With j_max = 2: 5^17 ≈ 7.6 × 10^11. Marginal (sparse matrix).

### 4. Spectral gap of truncated transfer matrix
Lanczos algorithm on the sparse transfer matrix.
If gap > 0 at β_continuum: evidence for mass gap.
With interval arithmetic: CERTIFIED gap.

## THE systematic approach QUESTION

Can we find algebraic identities in the representation basis that constrain
the spectral gap?

The NS analogy: the Frobenius identity related |S|² to |ω|² through
cross-terms. What relates the transfer matrix eigenvalues to the
representation weights a_j(β)?

Candidate: the Schwinger-Dyson equations in rep basis become recursion
relations on representation labels. The Makeenko-Migdal loop equations
relate Wilson loops of different sizes through specific algebraic formulas.

These are the "cross-term identities" of Yang-Mills.

## 002. Peter-Weyl is the Fourier decomposition of YM.
## The lattice partition function = state sum over representations.
## Transfer matrix in rep basis is finite (truncated) and computable.
## The mass gap = spectral gap of this matrix in the β → ∞ limit.
## First computation: 2³ spatial lattice, j_max = 1, Lanczos for gap.
