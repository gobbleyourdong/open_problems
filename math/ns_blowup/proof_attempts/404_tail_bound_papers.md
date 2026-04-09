---
source: TAIL BOUND PAPERS — three paths to close the proof
type: RESEARCH — specific papers for the Fourier tail bound
file: 404
date: 2026-03-30
---

## THE GAP

Prove: modes with |k|² > K₀² contribute negligibly to |∇u|²/|ω|² at
the vorticity maximum. K₀² = 2 (K-shell certification gives R ≤ 1.236).
Need: R_total ≤ 1.236 + ε < 13/8 where ε accounts for the tail.
From numerics: ε ≤ 0.04 (massive margin of 0.35).


## PATH A: ANALYTICITY + GEVREY DECAY (cleanest)

NS solutions are spatially analytic (Foias-Temam, Gevrey class).
Fourier coefficients: |ω̂_k(t)| ≤ C(t) exp(-ρ(t)|k|) for ρ(t) > 0.

Tail bound: ||∇u_tail||² = Σ_{|k|>K₀} |k|²|û_k|² ≤ C² Σ_{|k|>K₀} exp(-2ρ|k|)
                          ≤ C' exp(-2ρK₀)

For ρ > 0 (guaranteed while solution is smooth): tail → 0 exponentially.

**Papers:**
- Spatial analyticity: arXiv:2209.14862 (stochastic NS, but technique applies)
- Gevrey regularity: arXiv:2310.14273
- Foias-Temam original: Remarks on the Navier-Stokes equations (1989)

**Gap in this path:** Near blowup, ρ(t) → 0. The tail grows. Need: the tail
perturbation to R stays within the 0.35 margin even as ρ shrinks.


## PATH B: DETERMINING MODES (most physical)

High-|k| modes are "enslaved" to low modes. The determining wavenumber
K_d: if two solutions agree on |k| ≤ K_d, they converge globally.

For our problem: the R-ratio at the max is determined by modes |k| ≤ K_d.
Modes beyond K_d are "slaved" and can't independently increase R.

**Papers:**
- Determining wavenumber for 3D NS: arXiv:2407.06474
- High-low frequency slaving: arXiv:1506.03060
- Determining modes: ResearchGate/280330205

**Gap:** K_d depends on the Reynolds number Re. For Re → ∞: K_d → ∞.
Near blowup: Re → ∞, so K_d → ∞ (same issue as Path A).


## PATH C: RADII POLYNOMIALS (most rigorous, computer-assisted)

Lessard's method for CAP proofs of PDEs:
1. Formulate as fixed-point: F(u) = 0 in weighted ℓ¹ Fourier space
2. Compute approximate solution ū on |k| ≤ K₀
3. Construct radii polynomial p(r) bounding the defect
4. If p(r₀) > 0 for some r₀: the true solution is within r₀ of ū

For our problem: the "solution" is the vorticity field at the max.
The radii polynomial bounds how much the tail changes R.

**Papers:**
- Radii polynomial approach: ScienceDirect/S0167278916000294 (Lessard)
- Computer-assisted proofs in PDE survey: arXiv:1810.00745 (Gómez-Serrano)
- Rigorous numerics for orbits: Springer/s00205-017-1186-0

**Gap:** Requires implementation of interval arithmetic framework.


## PATH D: CHEN-HOU TAIL METHODOLOGY (most directly relevant)

Chen-Hou (2023) proved 3D Euler blowup using computer-assisted proof.
Their tail methodology (arXiv:2305.05660):
1. Compute approximate solution on finite modes
2. Bound tail via energy dissipation + Sobolev embedding
3. Verify with interval arithmetic

Their specific technique for ||u_tail||:
- Bootstrap: initial data smooth → Fourier decay → tail bounded
- Energy estimate: high modes dissipate faster than low modes excite them
- Interval bounds: rigorous constants throughout

**Application to our problem:**
- Replace "blowup profile" with "vorticity maximum"
- Replace "stability of profile" with "barrier R < 13/8"
- Adapt their tail estimates from Euler to NS (add viscous dissipation)

**Papers:**
- arXiv:2305.05660 (Chen-Hou Part II: rigorous numerics)
- arXiv:2210.07191 (Chen-Hou Part I: analysis)


## RECOMMENDED PATH: A + D hybrid

1. Use Gevrey analyticity for the QUALITATIVE argument (tail → 0)
2. Use Chen-Hou's QUANTITATIVE method for explicit bounds
3. Implement in Python/MPMath with interval arithmetic
4. The 0.35 margin (from 1.236 + 0.04 = 1.28 vs 1.625) is HUGE

The margin is so large (22%) that even crude tail bounds will suffice.


## 404. Three paths to close the tail bound. Papers identified.
## Recommended: Gevrey + Chen-Hou hybrid. Margin 22% is very comfortable.
