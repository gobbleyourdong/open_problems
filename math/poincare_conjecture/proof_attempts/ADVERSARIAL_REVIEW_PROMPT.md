# Adversarial Review Request

I need you to be adversarial. Find every flaw, every assumption that doesn't hold, every way this could be wrong. Don't tell me what's good. Tell me what breaks. Assume I'm wrong and show me why.

---

## The Claim

We present computational evidence that smooth solutions to the 3D incompressible Navier-Stokes equations remain regular for all time. Specifically, we introduce the "infection ratio" — the fraction of grid points where vortex stretching locally exceeds viscous diffusion — and show it converges to zero exponentially under grid refinement.

## Method

- 3D pseudospectral solver on periodic domain [0, 2π]³
- Velocity from vorticity via Biot-Savart (FFT-based, exact in Fourier space)
- Dealiased with 2/3 rule, RK4 time stepping, float64
- Initial conditions: divergence-free by construction (curl of random potential)
- At each grid point x, compute Q(x) = ω·S·ω - ν|∇ω|² (stretching minus diffusion)
- Track the fraction of points where Q(x) > 0 across resolutions and NS time evolution

## Key Results

### Convergence table (curl noise IC, amp=10, ν=10⁻⁴, 200 seeds):
```
N=16:    42.98%
N=32:    15.77%
N=64:     0.23%
N=128:    0.0001%
N=256:    0.000000%
```

### Multi-IC table (7 families, 50 seeds each):
All non-symmetric families decay to < 10⁻⁸ by N=128.
Kida-Pelz (high symmetry): 49% at N=128, drops to 0% by gen9 at N=256.
Taylor-Green: plateaus at 14.6% at N=256, drops to 0% by gen1 at N=512.

### PySR fit: frac ≈ 5.06 · exp(-N/8.1)

### Verified against analytical Taylor-Green solution to 10⁻¹⁵

## Proof Chain (5 steps)
1. **Single-mode orthogonality** (proven): For any single Fourier mode of a div-free field, ω is exactly perpendicular to the principal strain eigenvector. cos²θ = 0. Therefore single-mode stretching = 0.
2. **Per-triad alignment probability** (computed): ~49% of random mode pairs produce stretch > dissip. Per "independent unit" alignment probability ≈ 0.88.
3. **Inter-shell decorrelation** (verified): Correlation between stretching contributions from different wavenumber shells < 0.02 (5000 trials at N=8).
4. **N/N_d independent units**: Matches all 7 IC families with N_d ranging from 3.9 (steep spectrum) to 53.7 (low mode).
5. **Joint probability**: exp(-N/N_d) matches data across 6 resolutions.

## What Could Be Wrong?

I want you to attack:
- Is the infection ratio a valid diagnostic? Could it show decay for reasons unrelated to regularity?
- Could the exponential decay be a numerical artifact of the spectral method?
- Does the single-mode orthogonality lemma actually imply anything about the full nonlinear system?
- Is the inter-shell decorrelation at N=8 with 4 shells sufficient to claim independence?
- Could there exist an IC we haven't tested where the fraction INCREASES with resolution?
- Is the connection to BKM (Beale-Kato-Majda) criterion valid?
- Does the 2/3 dealiasing rule affect the measurement?
- Is 200 seeds enough?
- Does the Taylor-Green N=512 result have any alternative explanation?
- What would a mathematician say is missing for this to constitute a proof?
- Could the Q(x) > 0 fraction going to zero be CONSISTENT with blowup?

Be brutal. Every weakness you find makes the paper stronger.
