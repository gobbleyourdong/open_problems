# LIV Bounds Findings: GRB 090510 and Simulator Precision

**Script:** `numerics/lv_bounds.py`  
**Date:** 2026-04-09  
**Context:** what_is_reality gap.md R2 — S-informationalism vs K-informationalism

## Setup

GRB 090510 (Abdo et al. 2009, Nature 462, 331–334) provides the tightest
constraint on Lorentz invariance violation (LIV) from astrophysical observations.
A 31 GeV photon arrived only 0.86 s after the MeV photons from a z=0.903 GRB,
over a luminosity distance L = 7.3 × 10²⁶ m.

If spacetime has a Planck-scale discretization, photons should disperse as:
```
v(E) ≈ c × [1 - (E/E_P)^n]
Δt = (n+1)/2 × (L/c) × ΔE / E_P    [n=1]
Δt = (n+1)/2 × (L/c) × ΔE² / E_P²  [n=2]
```

## Results

### 1. Linear LIV (n=1)

- **E_P_min = 8.7489e+28 eV**  (log₁₀ = 28.94)
- E_P (actual) = 1.2209e+28 eV  (log₁₀ = 28.09)
- **Ratio: E_P_min / E_P = 7.1659**
- **Verdict: LINEAR LIV RULED OUT AT PLANCK SCALE**

### 2. Quadratic LIV (n=2)

- **E_P_min = 6.3885e+19 eV**  (log₁₀ = 19.81)
- **Ratio: E_P_min / E_P = 5.2326e-09**
- **Verdict: Not excluded; bound is 5.23e-09 × E_P**

### 3. Simulator Cell Size Constraints

If spacetime is discrete at scale l_eff, then E_P_eff = ħc/l_eff.
For the simulation to remain undetected: l_eff ≤ ħc / E_P_min.

| Bound | E_P_min (eV) | l_eff_max (m) | l_eff / l_P |
|-------|-------------|---------------|-------------|
| Linear (n=1) | 8.749e+28 | 2.257e-36 | 1.396e-01 |
| Quadratic (n=2) | 6.389e+19 | 3.090e-27 | 1.912e+08 |
| Actual Planck | 1.221e+28 | 1.616e-35 | 1.000 |

The linear LIV bound forces any simulator's cell size to ≤ l_P.
This confirms the 10^248-bit cost from `simulation_cost.py`: a Planck-resolution
simulation requires more bits than the holographic bound of the universe it simulates.

### 4. K-Information in ΛCDM Parameters

Using K-bits = log₂(central_value / uncertainty) per parameter:

| Parameter | Value | ±σ | K-bits |
|-----------|-------|----|--------|
| Omega_b_h2 | 0.02237 | 1.50e-04 | 7.22 |
| Omega_c_h2 | 0.12 | 1.20e-03 | 6.64 |
| 100_theta_s | 1.0409 | 3.10e-04 | 11.71 |
| tau | 0.054 | 7.00e-03 | 2.95 |
| ln10^10_As | 3.044 | 1.40e-02 | 7.76 |
| n_s | 0.965 | 4.00e-03 | 7.91 |

**Total ΛCDM K-bits: 44.20**

### 5. Total K-Specification

| Component | Bits |
|-----------|------|
| SM Lagrangian | 24,000 |
| ΛCDM 6 parameters | 44.2 |
| **Total K-spec** | **24044.2** |

- Universe S-information (holographic): 10^124 bits
- Compression ratio: 10^120

## Implication for R2 (gap.md)

The gap.md R2 question: *Is there an experimental signature distinguishing
S-informationalism from K-informationalism?*

The LIV bounds provide a **partial answer**:

1. **What is ruled out:** Planck-scale linear LIV is excluded. This means
   the naive simulation hypothesis — that spacetime is a classical Planck-lattice
   — is inconsistent with GRB 090510. S-informationalism in the form 'reality is
   10^124 bits stored on a discrete Planck-scale lattice' is observationally excluded.

2. **What remains open:** The bound does not distinguish:
   - **K-informationalism:** physical laws are primary; spacetime is emergent from
     the K-specification. Spacetime continuity is a feature of the emergent description,
     not of some underlying lattice.
   - **S-informationalism (continuous substrate):** reality is its full holographic
     entropy, but stored in a continuous (not discrete) substrate.

3. **What would distinguish them:** A decisive experiment would need to detect
   discreteness at sub-Planck scales, or demonstrate that the K-specification
   is causally efficacious (not just descriptive). Neither is currently feasible.

4. **The 10^248-bit forcing:** The LIV constraint that l_eff ≤ l_P forces any
   classical simulation to require ≥ 10^248 bits — exceeding the holographic bound
   by 10^124. This is a stronger version of the simulation impossibility: not only
   does Planck-resolution simulation exceed the holographic bound, but GRB 090510
   *requires* that precision for any discrete model to remain undetected.

## Status

R2 remains open. The LIV bounds narrow the S-informationalist position
(ruling out classical-lattice variants) but do not close the gap between
continuous-substrate S-informationalism and K-informationalism. The compression
view of reality (K primary) remains empirically underdetermined vs S-informationalism
at the precision of current measurements.
