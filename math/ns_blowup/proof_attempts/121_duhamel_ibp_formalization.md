---
source: Duhamel IBP formalization — the 2^{-j} gain from oscillatory nonlinearity
type: PROOF SKETCH — adapting Chaves-Santos & Ferreira framework to T³
status: IN PROGRESS — key mechanism identified, formalization needed
date: 2026-03-26
---

## The Framework (from arXiv:2603.19102)

Chaves-Santos & Ferreira prove dispersive + smoothing estimates for the
modified Stokes semigroup e^{t(νΔ̃+r-B)} on Riemannian manifolds, where:
- Δ̃ = Bochner Laplacian (viscous diffusion)
- r = Ric(u,·)♯ (Ricci curvature — provides exponential decay)
- B = -2 grad(-Δ_g)⁻¹ div(r(u)) (pressure-curvature coupling)

Their Lemma 7.2 gives: ||e^{t(νΔ̃+r-B)}u₀|| ≤ C t^{-α} e^{-σ_ν t} ||u₀||

On Einstein manifolds (Ric = λ < 0): B = 0 and r provides exponential decay.
This gives global well-posedness (Theorem 7.3).

## Adaptation to T³

On flat T³: Ric = 0, r = 0, B = 0. No curvature-driven decay.
The semigroup is just e^{νtΔ} with eigenvalues e^{-ν|k|²t}.

The Duhamel formulation for vorticity at shell j:

```
ω_j(t) = e^{-ν4^j t} ω_j(0) + ∫₀ᵗ e^{-ν4^j(t-τ)} F_j(τ) dτ     (*)
```

where F_j = [ℙ(ω·∇u - u·∇ω)]_j is the Leray-projected nonlinear source
restricted to shell j.

## The Key Observation: F_j Oscillates

From our phase scrambler experiments (files 117-118):
- F_j(τ) has an oscillatory component with frequency ω_j ~ 2^j
- The oscillation comes from the Leray projection ℙ_k = I - k̂⊗k̂
  acting differently on each k-direction
- The sign of the intra-shell contribution changes ~2^j times per unit time

Model: F_j(τ) = A_j(τ) × Φ_j(τ) where:
- A_j is a slowly varying envelope (timescale >> 2^{-j})
- Φ_j oscillates with frequency ~ 2^j (sign changes)

## The IBP Argument

Apply integration by parts to the Duhamel integral (*):

```
∫₀ᵗ e^{-ν4^j(t-τ)} A_j(τ) Φ_j(τ) dτ
```

Let Ψ_j(τ) = ∫₀^τ Φ_j(s) ds (antiderivative of the oscillation).
Since Φ_j oscillates with frequency ω_j ~ 2^j:
|Ψ_j(τ)| ≤ C/ω_j ~ C × 2^{-j}  (bounded antiderivative)

IBP:
```
= [e^{-ν4^j(t-τ)} A_j(τ) Ψ_j(τ)]₀ᵗ
  - ∫₀ᵗ d/dτ[e^{-ν4^j(t-τ)} A_j(τ)] × Ψ_j(τ) dτ
```

### Boundary term:
```
= A_j(t) Ψ_j(t) - e^{-ν4^j t} A_j(0) Ψ_j(0)
≤ C × |A_j|_max × 2^{-j}
```

### Integral term:
```
d/dτ[e^{-ν4^j(t-τ)} A_j] = ν4^j e^{-ν4^j(t-τ)} A_j + e^{-ν4^j(t-τ)} A_j'
```

The integral becomes:
```
∫₀ᵗ [ν4^j A_j + A_j'] × e^{-ν4^j(t-τ)} × Ψ_j dτ
≤ (ν4^j |A_j|_max + |A_j'|_max) × 2^{-j} × ∫ e^{-ν4^j(t-τ)} dτ
≤ (ν4^j |A_j|_max + |A_j'|_max) × 2^{-j} × 1/(ν4^j)
= |A_j|_max × 2^{-j} + |A_j'|_max × 2^{-j}/(ν4^j)
```

### Total Duhamel integral:
```
|∫₀ᵗ e^{-ν4^j(t-τ)} F_j dτ| ≤ C × |A_j|_max × 2^{-j} + lower order
```

Compare to the STANDARD bound (without oscillation):
```
|∫ e^{-ν4^j(t-τ)} F_j dτ| ≤ |F_j|_max × 1/(ν4^j)
= |A_j|_max × 1/(ν4^j)  [no 2^{-j} gain]
```

## The 2^{-j} Gain

The IBP gives a factor of **2^{-j}** from the bounded antiderivative of
the oscillation. This is INDEPENDENT of ν.

For the enstrophy at shell j:
```
E_j(t) ≤ e^{-2ν4^j t} E_j(0) + C × 2^{-j} × sup_τ |A_j(τ)|²
```

The envelope A_j satisfies |A_j| ≤ C × 2^{3j/2} × E_j^{3/2}/(something)
(from the standard trilinear bound on the NS nonlinearity).

With the 2^{-j} gain:
```
Effective transfer ≤ C × 2^{-j} × 2^{3j/2} × E_j^{3/2} = C × 2^{j/2} × E_j^{3/2}
```

This is **SUBCRITICAL** (2^{j/2} < 2^{2j} = viscous rate).

## What Needs To Be Proved

### 1. Oscillation decomposition of F_j
Show that F_j = A_j Φ_j where Φ_j has bounded antiderivative ~ 2^{-j}.
This is the MATHEMATICAL content of the phase scrambler.

Approach: Use the Littlewood-Paley decomposition of the nonlinear term.
The triadic interactions within shell j involve modes at different
k-directions. The Leray projection ℙ_k creates direction-dependent
phases that oscillate as the solution evolves.

### 2. Envelope bound
Show |A_j| ≤ C × 2^{3j/2} × E_j^{3/2} (standard trilinear bound
applied to the envelope, not the full oscillating term).

### 3. Slowly varying envelope
Show |A_j'| ≤ C × 2^j × |A_j| (the envelope changes on the eddy
turnover timescale, which is LONGER than the oscillation period).

### 4. Closure in Besov
Substitute the 2^{-j}-improved Duhamel bound into the standard
Besov B^1_{2,∞} framework. With the subcritical scaling, the
bootstrap closes for smooth initial data.

## Connection to the Data

| Quantity | Theory | Data |
|----------|--------|------|
| Oscillation freq at j | ~ 2^j | 0.2, 0.8, 1.1, 1.7 Hz (j=1,2,3,4) |
| Peak θ | bounded | 0.004-0.013 (all shells) |
| IBP gain | 2^{-j} | θ_avg ~ 0.04 × 2^{-j} |
| Stretching exponent | 2^{j/2} (subcritical) | consistent with bounded solutions |

## The Analogy to Dispersive PDE

| Dispersive PDE | NS with pressure scrambler |
|---------------|--------------------------|
| Phase e^{iξ·x} oscillates | Triadic phases oscillate |
| Strichartz: ∫e^{it|ξ|²} → t^{-d/2} | IBP: ∫e^{-ν4^j(t-τ)} Φ_j → 2^{-j} gain |
| Dispersion relation ω = |ξ|² | Eddy turnover ω_j = U × 2^j |
| Phase mixing prevents concentration | Phase scrambling prevents coherence |

The NS pressure acts as a pseudo-dispersive mechanism:
not through a dispersion relation, but through the direction-dependent
Leray projection creating effective phase mixing.

## Status

The proof architecture is:
1. Duhamel formulation (standard, from Paper 2 framework)
2. Oscillation decomposition of F_j (THE new ingredient)
3. IBP on the Duhamel integral (calculus)
4. 2^{-j} gain → subcritical scaling (arithmetic)
5. Besov bootstrap (standard LP theory)
6. BKM → global regularity (standard)

Steps 1, 3, 4, 5, 6 use existing machinery.
Step 2 is the NOVEL ANALYTICAL CONTENT — proving that the
NS nonlinearity has an oscillatory structure with bounded antiderivative.

## 121 proof files. The Duhamel IBP is the proof architecture.
