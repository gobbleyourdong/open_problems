---
source: Intermediate eigenvector alignment VERIFIED — self-attenuation mechanism
type: NUMERICAL RESULT + PHYSICAL INTERPRETATION
file: 389
date: 2026-03-29
---

## RESULT

At the global maximum of |ω| on T³, the vorticity direction ê = ω/|ω|
preferentially aligns with the INTERMEDIATE eigenvector e₂ of S:

| N modes | mean c₂ | ê closest to e₂ |
|---------|---------|-----------------|
| 3       | 0.563   | 63%             |
| 5       | 0.519   | 60%             |
| 8       | 0.410   | 43%             |

(Uniform random would give c₂ = 1/3 = 0.333, closest 33%.)

## MECHANISM: PER-MODE SELF-VANISHING

Each Fourier mode k has S_k·v̂_k = 0 (eigenvalue 0 along polarization).

At the global max: ê ≈ Σa_kv̂_k/|ω| (weighted average of polarizations).

S·ê = ΣS_k·ê. Since S_k·v̂_k = 0: S_k·ê only sees the PERPENDICULAR
part of ê relative to v̂_k. For dominant modes (ê ≈ v̂_k): |ê_⊥| is small.

The TOTAL S·ê is small because ê is close to the NULL DIRECTION of each
dominant mode's strain. The null direction of S ≈ the intermediate eigenvector.

## CONNECTION TO SELF-ATTENUATION (Nature 2020)

The alignment ê → e₂ IS the "self-attenuation of extreme events" observed
in DNS of turbulence. Our analysis provides the MECHANISM:
- Self-vanishing S_k·v̂_k = 0 (Biot-Savart geometry)
- Global max condition ê ≈ Σv̂_k (coherence of polarizations)
- Combined: ê → null of S → intermediate eigenvector

This is automatic for the Biot-Savart kernel — not a dynamical property
of NS, but a KINEMATIC property of any div-free field.

## QUANTITATIVE CONSEQUENCE

When c₂ > 1/3 (intermediate alignment above uniform):

S²ê = λ₁²c₁ + λ₂²c₂ + λ₃²c₃

With λ₂² ≤ min(λ₁², λ₃²) (middle eigenvalue is smallest in magnitude):

S²ê ≤ (1-c₂)|S|² + c₂ × 0 = (1-c₂)|S|² [approximate, when λ₂ ≈ 0]

For c₂ = 0.56 (N=3 average): S²ê ≤ 0.44|S|² (vs 0.667|S|² from trace-free).

## LIMITATION

The alignment provides a nicer INTERPRETATION but not a stronger BOUND
than the per-mode approach (file 363). Both give S²ê ≤ (N-1)|ω|²/4.

The alignment DOES explain why the numerical S²ê/|ω|² ≈ 0.05-0.28 is
much smaller than the (N-1)/4 bound: the intermediate alignment means
S²ê is dominated by λ₂² ≈ 0 (the null eigenvalue), not by λ₁² or λ₃².

## 389. Self-attenuation alignment VERIFIED: c₂ = 0.56 for N=3 (63% of time).
## Mechanism: per-mode self-vanishing S_k·v̂_k = 0 drives ê toward S's null.
## Matches the Nature 2020 turbulence observation. Same tool as file 363.
