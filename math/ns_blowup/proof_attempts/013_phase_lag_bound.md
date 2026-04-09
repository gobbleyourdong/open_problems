---
source: New idea from literature search (arXiv 2601.08862)
approach: Phase-lag geometric bound on strain-vorticity alignment
status: EXPLORING — most geometrically natural approach
---

## The Key Observation
The Lagrangian phase-lag paper shows that strain and vorticity alignment
is NOT instantaneous. There is a systematic temporal delay before ω aligns
with the principal strain direction. This delay is inherent to the NS dynamics.

## Why This Matters for Our Proof
Q(x) > 0 requires: ω·S·ω > ν|∇ω|²
This means: |ω|² |S| cos²θ > ν|∇ω|²
where θ is the angle between ω and the principal eigenvector of S.

If we can show cos²θ is bounded AWAY from 1 at high wavenumbers,
then the stretching can never exceed diffusion at those wavenumbers.

## The Geometric Argument

### Step 1: Decompose into scales
At wavenumber k, the vorticity mode ω̂_k has a direction in R³.
The strain S at that scale comes from the Biot-Savart coupling with
ALL other modes (triadic interactions).

### Step 2: The phase-lag mechanism
When ω̂_k points in direction ê, the Biot-Savart coupling generates
strain S whose principal direction is ROTATED from ê by the phase lag angle φ.

The rotation happens because:
- S is obtained from ω via a singular integral (Riesz transforms)
- The Riesz transform ROTATES the direction by π/2 in the plane
  perpendicular to k
- The resulting strain eigenframe is systematically offset from ω

### Step 3: Quantify the phase lag
For a single Fourier mode ω̂_k:
- The velocity is û = ik × ω̂_k / |k|²
- The strain is Ŝ_ij = i(k_i û_j + k_j û_i)/2
- The eigenvectors of Ŝ lie in the plane perpendicular to k
- ω̂_k also lies in this plane (div-free: k·ω̂ = 0)

Within the 2D plane ⊥ k:
- ω̂ points in some direction ê
- The strain eigenframe is rotated by 45° from ê
  (because the strain of a shear flow is at 45° to the flow direction)

So cos²θ = cos²(45°) = 1/2 for a SINGLE mode.
The stretching is at most HALF the maximum possible.

### Step 4: Multi-mode interaction
For multiple modes, the alignment depends on how the modes interact.
The strain at x is the SUM of strain contributions from all modes.
The alignment between ω(x) and the total S(x) is determined by
the VECTOR SUM of the rotated components.

For N modes with independent directions:
- Each mode contributes strain rotated by ~45° from ω
- The vector sum of N random-phase rotations has magnitude ~√N
- But the aligned component grows as ~N (coherent sum) only if
  ALL phases align, which has probability ~exp(-cN)

### Step 5: The bound
The effective cos²θ for the multi-mode interaction satisfies:
```
E[cos²θ] = 1/d = 1/3  (in 3D, by isotropy)
```

The probability of cos²θ > 1 - ε is:
```
P(cos²θ > 1-ε) ~ ε^{(d-2)/2} = ε^{1/2}  (in 3D)
```

For Q(x) > 0, we need cos²θ > ν|∇ω|² / (|ω|²|S|).
At high resolution: |∇ω|² ~ k² |ω|² and |S| ~ |ω| (Riesz bound).
So we need cos²θ > νk²/|ω|.

For this to be satisfiable: νk²/|ω| < 1, i.e., k < √(|ω|/ν).
Above this wavenumber, NO alignment can make stretching beat diffusion.

Below this wavenumber: the probability is ~(νk²/|ω|)^{1/2}.

### Step 6: The fraction bound
The fraction of points where Q > 0 is bounded by the probability that
the alignment is sufficient at the DOMINANT wavenumber k* where
stretching is strongest.

For the dominant mode k*:
```
P(Q > 0 at x) ≤ P(cos²θ > νk*²/|ω|) ~ (νk*²/|ω|)^{1/2}
```

The fraction over all x:
```
frac ≤ (ν k*² / ||ω||_∞)^{1/2}
```

As N increases, k* increases (more modes resolved), so the fraction decreases.
If k* ~ N^α for some α > 0, then frac ~ N^{-α}.

BUT this gives POLYNOMIAL decay, not exponential.

## The Gap: Polynomial vs Exponential
The single-mode phase lag argument gives polynomial decay (power law).
For exponential decay, we need the MULTI-MODE argument:
- Multiple independent alignment constraints at different k
- Joint probability is the PRODUCT
- Product of polynomials gives exponential

The number of independent constraints = number of resolved scales above k_c.
If there are ~log(N) independent scales (dyadic decomposition):
```
frac ≤ Π_{j=0}^{log N} (1 - p_j) ~ exp(-Σ p_j) ~ exp(-c log²N)
```

This gives INTERMEDIATE decay: exp(-c log²N), between polynomial and exponential.
Our data shows exp(-cN). The gap: log²N vs N.

## Where This Stands

The phase-lag argument gives:
- QUALITATIVE: correct direction (fraction decays)
- QUANTITATIVE: wrong rate (log²N or polynomial, not linear N)
- MECHANISM: correct (alignment rarity due to Riesz rotation)

The argument is too weak because it treats scales as independent
logarithmic intervals. In reality, the modes at scale k are O(k²)
in number (surface of a sphere in k-space), not O(1).

If we count MODES not SCALES:
```
frac ≤ exp(-c Σ_{|k|>k_c} log(1/p_k)) ~ exp(-c N^d)
```
where the sum is over all modes, not just dyadic scales.
This gives exp(-cN³) which is TOO FAST.

## Assessment
The phase-lag bound is geometrically correct but quantitatively
either too weak (scale-counting → log²N) or too strong (mode-counting → N³).

The truth (exp(-cN)) lies between these extremes, corresponding to
an effective number of independent constraints that grows LINEARLY with N.

This suggests ~N independent alignment constraints, which means
the constraints are independent per LINEAR dimension, not per mode
or per scale. In 3D on an N³ grid, there are N independent "slices"
in each direction. The alignment in one slice is independent of others
if the Riesz kernel decorrelates across slices.

The DECORRELATION LENGTH of the Riesz kernel ~1/|k|² is O(1) grid cells,
so slices separated by O(1) cells are independent.
Number of independent slices: ~N.
Each slice imposes one alignment constraint with failure probability p.
Joint: p^N = exp(N log p) = exp(-cN). ✓

THIS MATCHES THE DATA.

## The Partial Proof (Provable Lemma)

**Lemma (Phase-Lag Lower Bound):**
For a single Fourier mode ω̂_k of a divergence-free field on T³,
the angle θ between ω̂_k and the principal eigenvector of the
Biot-Savart strain at wavenumber k satisfies cos²θ = 1/2.

*Proof:* Direct computation. The velocity û = ik × ω̂/|k|².
The strain Ŝ_ij = i(k_i û_j + k_j û_i)/2. In the plane ⊥ k,
û is perpendicular to ω̂ (from the cross product). The strain
of a simple shear (velocity ⊥ to vorticity) has eigenvectors at
45° to both directions. Hence θ = 45°, cos²θ = 1/2. □

This is a PROVABLE LEMMA. It's a brick.
The full proof builds on it by handling multi-mode interactions.

## Next Steps
1. VERIFY the 45° phase lag computationally at N=4
2. PROVE the decorrelation across slices
3. If decorrelation holds → exp(-cN) follows from independence
4. Write up the Lemma as a standalone result
