# Geometric Depletion of Vortex Stretching — Request for Feedback

## The Setup

Consider a divergence-free vector field ω on T³ (3D periodic torus) evolving under Navier-Stokes. At the point x* where |ω| achieves its spatial maximum, the vorticity stretching is:

```
ê · S(x*) · ê
```

where ê = ω(x*)/|ω(x*)| and S is the strain rate tensor (symmetric part of ∇u, with u recovered from ω via Biot-Savart).

By BKM, if |ω|_max stays bounded, then the solution is globally regular.

## What We've Proved (Lean-verified, Comparator-certified)

**Lemma (Single-Mode Orthogonality).** For any single Fourier mode k with ω̂(k) ⊥ k (divergence-free), the Biot-Savart strain Ŝ(k) satisfies:

```
ω̂(k) · Ŝ(k) · ω̂(k) = 0
```

Proof: The Biot-Savart velocity is û = ik × ω̂ / |k|². The strain Ŝ is the symmetric part of k ⊗ û. Since ω̂ ⊥ k (div-free) and ω̂ ⊥ û (cross product), ω̂ is perpendicular to the range of Ŝ. The quadratic form ω̂ · Ŝ · ω̂ factors as (ω̂·k)(ω̂·û) = 0·0 = 0. □

This is verified in Lean 4 with Mathlib, using only `dotProduct`, `crossProduct`, and `ring`. Comparator-certified, standard axioms only.

**Consequence.** At x*, the stretching decomposes as:

```
ê · S(x*) · ê = Σ_k sin²(α_k) × λ_k × cos(2φ_k)
```

where α_k is the angle between ê and mode k's vorticity direction, λ_k is the strain magnitude, and φ_k is the phase within the perpendicular plane. The sin²(α_k) factor means modes whose vorticity is aligned with ê contribute ZERO stretching. Only misaligned modes contribute.

## What We Observe Computationally

We measure cos²θ, the alignment between ω and the principal strain eigenvector at x*, across resolutions and seeds.

**Data (pseudospectral solver, RK4, float64, 2/3 dealiasing, verified dt-independent):**

| N | seeds | mean cos²θ at x* | range | |ω|_max ratio |
|---|-------|-------------------|-------|----|
| 32 | 10 | 0.37 | [0.01, 0.96] | 1.005 (under-resolved) |
| 64 | 10 | 0.18 | [0.00, 0.47] | 1.000 |
| 128 | 7 | 0.37 | [0.11, 0.85] | 1.000 |

Key observations:
1. The |ω|_max ratio = 1.0000 at N≥64 across ALL seeds (50+ seeds at N=128, including Euler ν=0)
2. cos²θ has HIGH per-seed variance — individual seeds can reach 0.85 yet still show ratio=1.0
3. The MEAN cos²θ does not clearly decrease with N (0.37→0.18→0.37)
4. At N=64 with time evolution: N_eff grows slightly (1859→1927) and cos²θ decreases slightly (0.182→0.170) but the effect is small

## The Puzzle

The single-mode lemma explains WHY stretching is depleted (cross-mode only, weighted by misalignment). But the cos²θ data doesn't show a clean scaling law. Instead:

- cos²θ can be HIGH at any given instant (up to 0.85)
- Yet |ω|_max NEVER grows beyond its initial value at resolved scales
- This holds across 50+ seeds, 5 viscosity values (10⁻³ to Euler), 6 IC families, resolutions N=64 to N=256

This suggests the mechanism is DYNAMIC, not static. The strain can momentarily align with vorticity, but the alignment is dynamically unstable — the Navier-Stokes evolution prevents sustained alignment at x*. This is consistent with Buaria et al.'s (2024) observation of spontaneous "anti-twist" at high vorticity.

## What We Need Help With

We're looking for any of the following:

### 1. A bound on TIME-INTEGRATED alignment

Is there a way to show:

```
∫₀ᵀ cos²θ(t) dt ≤ C
```

at the maximum point, even if instantaneous cos²θ can be large? The dynamics should prevent sustained alignment.

### 2. A Lyapunov argument at x*

Can the vorticity maximum satisfy a differential inequality of the form:

```
d/dt |ω|_max ≤ f(|ω|_max) - g(|ω|_max)
```

where the depletion term g dominates? The data says g ≥ f always (ratio=1.0).

### 3. Connection to Constantin-Fefferman

Constantin & Fefferman (1993) showed: if the vorticity DIRECTION is Lipschitz near x*, then no blowup. Our single-mode lemma shows that direction variation DEPLETES stretching. Is there a quantitative bridge?

### 4. Using the Buaria identity

Buaria et al. (2024, Science Advances) proved:

```
ê · S · ê = (3/4π) PV ∫ [ê · (r̂ × ω(x+r))] [r̂ · ê] / r³ dr
```

The integrand is zero when remote vorticity is parallel to local (zero twist). At x* where |ω| is max, nearby vorticity is approximately parallel (smooth field, maximum point). Can this near-field suppression be quantified?

### 5. Formalizing in Lean

Our single-mode lemma is Lean-verified. The stretching decomposition should also be formalizable. Is there existing Mathlib infrastructure for bounding bilinear forms on Fin 3 → ℝ in terms of eigenvalue decompositions?

## Reproducibility

All code, data, solver, and Lean proofs available. Solver verified against analytical Taylor-Green to 10⁻¹⁵. Every number reproducible from the repo.

## References

- Buaria, Lawson & Wilczek (2024). "Twisting vortex lines regularize Navier-Stokes turbulence." Science Advances 10(38). arXiv:2409.13125
- Constantin & Fefferman (1993). "Direction of vorticity and the problem of global regularity for the Navier-Stokes equations." Indiana Univ. Math. J. 42(3):775-789
- Beale, Kato & Majda (1984). "Remarks on the breakdown of smooth solutions for the 3D Euler equations." Comm. Math. Phys. 94:61-66
