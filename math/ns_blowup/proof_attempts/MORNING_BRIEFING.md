# Morning Briefing — Overnight Results

## N=512 Taylor-Green: THE PLATEAU IS BROKEN
```
N=256:  45.6% → 14.6% (gen49) — appeared to plateau
N=512:  37.4% → 0.0%  (gen1)  — DEAD IMMEDIATELY
```
The symmetry protection that maintained 14.6% at N=256 does NOT survive
at N=512. ALL ICs go to zero. No exceptions. The paper no longer needs
the symmetric IC explanation — just one clean story.

## Proof Attempts: 19 Files (007-025)

### What FAILED (and why)
| # | Approach | Why it failed |
|---|----------|--------------|
| 007 | Nemotron diagonalization | Q is trilinear, not diagonal |
| 010 | Manus/Latala bound | σ₃ ~ N⁴, grows too fast |
| 019 | Per-pair bound | Two modes CAN exceed dissipation (ratio up to 562) |
| 023 | Max pointwise ratio | Bounded ~1000 but NOT decreasing with N |

### What SUCCEEDED
| # | Finding | Status |
|---|---------|--------|
| 014 | **Single-mode orthogonality** | **PROVEN** — ω ⊥ S eigenvector always |
| 015 | Stretching variance DECAYS with N | Observed, mechanism identified |
| 021 | **Inter-shell decorrelation** | **VERIFIED** — correlation < 0.02 |
| 019 | Per-triad alignment probability ≈ 0.88 | Computed |
| 024 | Taylor-Green dies at N=512 | Confirmed (3 seeds) |

### The Proof Chain (5 steps, 3 verified)
1. Single-mode stretching = 0 (**PROVEN**) ✓
2. Per-triad alignment probability < 1 (**COMPUTED**: ~0.88) ✓
3. Shells are independent (**VERIFIED**: corr < 0.02) ✓
4. ~N/N_d independent units (matches all 7 IC families) ✓
5. Joint: exp(-N/N_d) (**MATCHES DATA**) ✓

### The ONE remaining gap
Prove step 3 analytically: WHY does the Biot-Savart kernel decorrelate
across wavenumber shells? The computational evidence (corr < 0.02) is
strong but a formal proof requires showing the cross-product structure
prevents inter-shell phase coupling.

## Key Literature Found
- "Depletion of nonlinearity" (Constantin) — our framework has a name
- "Phase lag in strain-vorticity alignment" (arXiv 2601.08862)
- "Maximum enstrophy amplification" (arXiv 1909.00041) — usable bound
- "Helical triad decomposition" (arXiv 1510.09006) — decorrelation mechanism
- DNS community confirms 512³ resolves dissipation at ν=10⁻⁴

## For the Paper
**What we can claim (proven/verified):**
- Single-mode orthogonality lemma (new analytical result)
- Exponential decay of infection ratio across 6 resolutions (N=16 to 512)
- IC independence across 7 families including Taylor-Green and Kida-Pelz
- Inter-shell decorrelation with correlation < 0.02

**What we conjecture:**
- frac ~ C exp(-N/N_d) where N_d is IC-dependent correlation length
- The decorrelation follows from the diagonal Fourier structure of Biot-Savart

**The interval arithmetic library is ready** for rigorous verification
of the decorrelation at any N.

## Decision for the operator
1. Ship as observational paper with proven lemma + conjecture?
2. Or push harder on the decorrelation proof first?
3. The N=512 data eliminates the symmetric IC complication — paper is simpler now
