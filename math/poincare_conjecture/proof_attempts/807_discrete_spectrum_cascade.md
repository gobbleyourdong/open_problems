---
source: DISCRETE SPECTRUM CASCADE — can viscosity + discrete modes prevent blowup?
type: NEW APPROACH — exploiting T³ structure directly
file: 807
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE IDEA

On T³, the Fourier modes are discrete: k ∈ Z³. On R³, the spectrum is
continuous. This discreteness might constrain the blowup mechanism.

## FOURIER DECOMPOSITION ON T³

u(x,t) = Σ_{k ∈ Z³} û_k(t) e^{ik·x}, with k·û_k = 0 (div-free).

NS in Fourier space:
    d/dt û_k = -ν|k|²û_k - i P_k Σ_{m+n=k} (û_m ⊗ û_n) · k

where P_k is the Leray projector onto {v : k·v = 0}.

## VISCOUS DAMPING

Each mode k ≠ 0 is damped at rate ν|k|². On T³:
- Minimum |k|² = 1 (for k = (1,0,0), etc.)
- SPECTRAL GAP: no modes between 0 and 1

On R³: modes can have |k| arbitrarily close to 0 → no spectral gap.

For a mode at |k|² = K² to be sustained against viscous damping:
the nonlinear forcing must overcome ν K². This requires:

|N_k| ≥ ν K² |û_k|

where N_k = -i P_k Σ (û_m ⊗ û_n) · k is the nonlinear term.

## ENERGY CASCADE AND THE KEY LEMMA

Near blowup: energy cascades to higher k (smaller scales).
The stretching term ω·Sω transfers enstrophy from low to high k.

The Key Lemma bounds the stretching: α < (√3/2)|ω| at the max.
This limits the CASCADE RATE — energy can't transfer to high modes
faster than (√3/2)||ω||∞² per unit time.

## SPECTRAL ENERGY BUDGET

For each shell K² = |k|²:
    d/dt E_K = T_K - 2ν K² E_K

where E_K = Σ_{|k|²=K²} |û_k|² is the shell energy and T_K is the
nonlinear transfer to/from shell K.

Total enstrophy: Ω = Σ_K K² E_K
Stretching: Σ_K T_K · K² = ∫ω·Sω ≤ (√3/2)||ω||∞ · Ω (Key Lemma at max)

Wait — the Key Lemma bounds α at the MAX, not the integral ∫ω·Sω.
The integral is bounded by ||ω||∞ · ∫|S| · |ω|, which involves the
CZ operator. See file 803.

## THE DISCRETE ADVANTAGE

On T³, the mode count at shell K² is finite: N(K²) ≤ CK² (lattice points).
The enstrophy in shell K²: Ω_K = K² E_K.
Total enstrophy: Ω = Σ_{K²≥1} Ω_K (finite sum if u is smooth).

For blowup: Ω → ∞. This requires Ω_K → ∞ for increasingly high K.

Viscous damping of high modes: d/dt Ω_K ≤ K² T_K - 2ν K⁴ E_K
    = K² T_K - 2ν K² Ω_K

For Ω_K to grow: K² T_K > 2ν K² Ω_K, i.e., T_K > 2ν Ω_K.

The transfer T_K is bounded by the TRILINEAR interaction:
T_K ~ Σ_{m+n in shell K} |û_m| |û_n| |k|

For the cascade to reach shell K: modes at lower shells must have
enough energy. The Key Lemma limits the stretching rate, which limits
how fast energy can cascade.

## QUANTITATIVE ESTIMATE

Kolmogorov-type argument on T³:
- Total energy: E = ||u||²_{L²} ≤ ||u₀||² (bounded)
- Dissipation rate: ε = 2ν Ω
- If ε → ∞ (enstrophy blowup): energy is dissipated faster
- But total energy is bounded → ε must be integrable: ∫ε dt = E₀ - E(T*) ≤ E₀

For Type I: Ω ~ (T*-t)^{-1/2} (from concentration), ε = 2νΩ ~ (T*-t)^{-1/2}.
∫ε dt ~ √(T*-t) → 0. Integral converges. ✓ Consistent.

## THE BOTTLENECK

The same issue as file 803: the energy budget is SATISFIED by Type I
with parabolic concentration. The discrete spectrum doesn't help because
the cascade process is consistent with the energy constraints.

The spectral gap (λ₁ = 1) provides damping for the k = 0 mode neighborhood,
but the blowup occurs at HIGH k (k ≫ 1), where the damping rate ν k² is
large but so is the stretching.

## WHAT COULD WORK

The Key Lemma was proved for FINITE Fourier modes on T³ using the discrete
structure. The SOS certificates are specific to the T³ lattice Z³.

Can we prove a STRONGER version of the Key Lemma using the FULL lattice
structure, not just finite mode configurations?

On R³: the continuous Biot-Savart kernel 1/(4π|x|³) gives no extra
constraint. On T³: the discrete Biot-Savart kernel Σ_{k∈Z³} e^{ik·x}/|k|²
might have additional number-theoretic constraints from the lattice.

## THE LATTICE ADVANTAGE

The Biot-Savart kernel on T³:
    G(x) = Σ_{k∈Z³\{0}} e^{ik·x}/|k|²

The sum over the lattice Z³ has specific arithmetic structure:
- |k|² takes values 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, ...
  (some integers are not sums of 3 squares: 4^a(8b+7))
- The number of representations r₃(n) = #{k ∈ Z³ : |k|² = n}
  oscillates but grows on average as n^{1/2}

Could the arithmetic of r₃(n) constrain the stretching in a way that
goes beyond the Key Lemma?

## 807. Discrete spectrum cascade: viscous damping + spectral gap on T³.
## The energy budget is satisfied by Type I concentration (Ω ~ (T-t)^{-1/2}).
## The discrete advantage: lattice Z³ has arithmetic structure. Unexplored.
## The Key Lemma was proved using this lattice. Can it be strengthened?
