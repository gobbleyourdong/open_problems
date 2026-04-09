---
source: Synthesis of Buaria et al. (2024) anti-twist + our single-mode orthogonality
approach: Physical-space stretching identity → Fourier-space depletion → bound at x*
status: IN PROGRESS — key identity found, gap identified
---

## The Buaria Identity (Science Advances, 2024)

For ANY 3D incompressible flow, the normalized vortex stretching at point x is:

```
ê·S·ê(x) = (3/4π) PV ∫ [ê(x)·(r̂ × ω(x+r))] [r̂·ê(x)] / r³ dr     (*)
```

where ê = ω/|ω| is the vorticity direction. This is EXACT (derived from Biot-Savart).

Key property: the local antisymmetric part of ∇u drops out because ε_{ijk}ω_iω_j = 0.

### Why this identity matters

The integrand factors into:
1. **Twist factor**: ê·(r̂ × ω(x+r)) — the azimuthal component of remote vorticity
2. **Axial weight**: r̂·ê — projection onto the vorticity axis
3. **Kernel**: 1/r³ — Biot-Savart decay

**If ω(x+r) ∥ ê**: twist factor = 0 → ZERO stretching contribution.
Stretching requires the remote vorticity to be MISALIGNED with the local direction.

## Connection to Single-Mode Orthogonality (Our Lemma 1)

### Fourier space
Lemma 1: For each mode k, ω̂(k) ⊥ Ŝ(k) eigenvectors.
Equivalently: mode k's vorticity CANNOT stretch itself. ω̂(k)·Ŝ(k)·ω̂(k) = 0.

### Physical space (Buaria)
Identity (*): stretching at x requires TWIST — directional misalignment of remote ω.
If all ω pointed in the same direction, stretching would be zero everywhere.

### The connection
Single-mode orthogonality IS the Fourier dual of the twist requirement.
- Fourier: self-stretching = 0 for each mode (ω̂ ⊥ strain eigenvectors)
- Physical: self-aligned stretching = 0 (parallel vorticity has zero twist)
- Both say: stretching is entirely a CROSS-mode / MISALIGNMENT phenomenon

## The Argument at x* (Maximum Point)

At x* where |ω| achieves its spatial maximum:

### 1. Near-field contribution is suppressed
- |ω(x*+r)| ≤ |ω(x*)| for all r (definition of maximum)
- For small |r|: ω(x*+r) ≈ |ω(x*+r)| ê + O(|r|) (smooth field)
- The twist of nearly-parallel vorticity is O(|r|·|∇ω̂|)
- Near-field stretching ≤ C |ω(x*)| |∇ω̂|_{x*} × (near-field volume)

### 2. Far-field contribution averages out
- For large |r|: ω(x*+r) is generically decorrelated from ê
- The twist factor ê·(r̂ × ω(x*+r)) has random sign
- By CLT / decorrelation: far-field integral ≤ C √(number of correlation volumes) × typical |ω|

### 3. The maximum condition constrains ∇ω̂
At x*: ∇|ω|² = 0 (stationary point)
This constrains the relationship between ω direction change and magnitude change.
The Hessian ∂²|ω|²/∂x_i∂x_j ≤ 0 (maximum → negative semidefinite).

## The Depletion Coefficient (from file 042)

In Fourier space, the stretching at x* decomposes as:
```
ê·S·ê = Σ_k sin²(ψ_k) × (ê_perp · S_k · ê_perp)
```
where ψ_k = angle between ê and the vorticity direction of mode k at x*.

From the constraint Σ_k a_k cos(ψ_k) = 1 (definition of ê), by Lagrange multipliers:

```
Depletion = Σ_k cos²(ψ_k) |S_k| ≥ 1 / Σ_k (a_k² / |S_k|)
```

where a_k = |ω_k(x*)|/|ω(x*)|.

This is TIGHT (achieved by the Lagrange solution cos(ψ_k) = λ a_k / (2|S_k|)).

### The depletion is strictly positive
Since Σ a_k cos(ψ_k) = 1 and ê is a unit vector, at least one cos(ψ_k) ≠ 0.
So Σ cos²(ψ_k) |S_k| > 0 for any nonzero field.

### But is it large enough?
The depletion bound 1/Σ(a_k²/|S_k|) can be small when many low-amplitude
modes collectively build up |ω(x*)|. This is where the Biot-Savart structure
must be used — generic div-free fields may have small depletion, but the
specific coupling through the Laplacian inverse constrains this.

## What Would Close the Proof

### Path A: Universal depletion bound
Show that for ANY div-free field on T³:
```
ê·S·ê at x* ≤ (1-δ) ||S||_∞  for some universal δ > 0
```
This seems too strong — the CZ bound is likely sharp in general.

### Path B: Dynamical depletion
Show that along NS trajectories, the depletion coefficient GROWS or
stays bounded away from zero. This uses the NS dynamics (not just kinematics).
The Buaria anti-twist observation supports this — the dynamics spontaneously
generate anti-twist at high vorticity — but hasn't been proven.

### Path C: Computer-assisted verification
At fixed N (e.g., N=64 or N=128):
1. Use interval arithmetic to rigorously bound all Fourier modes
2. At each timestep, verify ê·S·ê < ν|∇ω|²/|ω|² at x*
3. This proves regularity for the specific (N, ν, IC) configuration
4. Combined with convergence data: the bound holds at all tested N

This is feasible with our interval arithmetic library and follows the
Chen-Hou paradigm of computer-assisted proof.

### Path D: Maximum principle + Buaria identity
Use identity (*) directly at x*:
1. Split integral into |r| < δ and |r| > δ
2. Near field: bounded by C|ω|_max |∇ω̂| δ (twist is small near max)
3. Far field: bounded by C ||ω||_2 / δ (L² bound + kernel decay)
4. Optimize δ to get: stretching ≤ C |ω|_max^{1-α} for some α > 0
5. If α > 0: growth rate is sub-quadratic → no finite-time blowup

The challenge: making step 2 rigorous requires bounding |∇ω̂| at x*
independently of |ω|_max. This relates to the regularity of the
vorticity direction field — studied by Constantin & Fefferman (1993).

## The Constantin-Fefferman Connection

Constantin & Fefferman (1993): if the vorticity direction ω̂ is
Lipschitz in a neighborhood of the maximum, then no blowup.

Their condition: |ω̂(x) - ω̂(y)| ≤ C|x-y| near x*.

Combined with Buaria: if ω̂ is Lipschitz at x*, then the near-field
twist is O(|r|), the near-field contribution to stretching is bounded,
and the integral converges to something ≤ C|ω|_max (not |ω|_max²).

The question: does Biot-Savart + maximum point FORCE ω̂ to be Lipschitz?

For smooth solutions: yes (by regularity). But the question is whether
the Lipschitz constant of ω̂ can grow as |ω|_max grows.

If |∇ω̂| stays bounded as |ω|_max → ∞: then Path D works.
This is essentially equivalent to the regularity question itself.

## Summary of Gaps

| Approach | What it needs | Status |
|----------|--------------|--------|
| Depletion coefficient (042) | Universal lower bound on Σ cos²ψ |S| | Open |
| Anti-twist (Buaria) | Prove anti-twist is mandatory, not just typical | Open |
| Computer-assisted (Path C) | Interval arithmetic at specific N | Feasible |
| Near/far splitting (Path D) | Bound |∇ω̂| at x* | ≈ regularity itself |
| Constantin-Fefferman | ω̂ Lipschitz ⟹ regularity | Known, but condition unverified |

## The Honest Assessment

Every analytical path converges to the same gap: proving that the Biot-Savart
coupling prevents coherent alignment at the maximum point. The single-mode
orthogonality and the Buaria identity both EXPLAIN why this should happen,
but neither PROVES it must happen strongly enough to prevent blowup.

The computer-assisted path (C) is the most realistic route to a rigorous
result for specific configurations. Combined with our convergence data
showing the bound holds at N=64, 128, 256, this would be a publishable
computational proof analogous to Chen-Hou's Euler blowup proof.

## References
- Buaria, Lawson & Wilczek (2024). Science Advances 10(38). arXiv:2409.13125
- Constantin & Fefferman (1993). Indiana Univ. Math. J. 42(3):775-789
- Our file 014: Single-mode orthogonality lemma (PROVEN)
- Our file 042: Depletion coefficient approach (IN PROGRESS)
