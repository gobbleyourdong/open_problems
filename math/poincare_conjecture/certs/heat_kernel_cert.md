# Heat Kernel on S³ Certificate

## Date: 2026-04-09
## Script: numerics/heat_kernel_s3.py

## CERTIFICATE

Heat kernel on round S³(1) computed via spherical harmonic expansion.
Eigenvalues λ_k = k(k+2), multiplicities m_k = (k+1)².

| Test | Quantity | Result |
|------|----------|--------|
| 1 | K(x,x,t) → 1/(2π²) | 0.05066 at t=10 (matches 1/vol = 0.0507) |
| 2 | Heat trace Z(t) → 1 | 1.000000 at t=10 |
| 3 | Weyl Z(t) ~ vol/(4πt)^(3/2) | ratio 1.0010 at t=10⁻³ (0.1% accuracy) |
| 4 | f(p,τ) → 0 as τ → 0 | f = 0.0003 at τ = 10⁻⁴ |

## Key Numbers

- vol(S³) = 2π² = 19.7392
- 1/vol = 0.0506606
- λ_1 = 3 (lowest non-trivial eigenvalue, multiplicity 4)
- Decay rate of K(x,x,t) - 1/vol matches e^(-λ_1·t) = e^(-3t)
- Weyl ratio at t=10⁻³: 1.0010 (Weyl is exact in this limit)

## Reproducibility

Dependencies: numpy. Runtime: < 1 second.
Eigenvalue cutoff: k_max = 50 for low t, k_max = 200-300 for tiny t.
