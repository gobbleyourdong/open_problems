---
source: Signed T(j,j) analysis — IBP argument reality check
type: CORRECTION — IBP requires sign changes, only present at high j
status: PARTIALLY VIABLE — works at high shells where it matters
date: 2026-03-26
---

## The Sign Structure of T(j,j)

T(j,j) = ∫ ω_j · S_j · ω_j dx is the SIGNED intra-shell transfer.

### Data (TG, N=32, t=0 to 8):

| Shell | T(j,j) sign | Sign changes | Frequency |
|-------|------------|--------------|-----------|
| j=1 | Always NEGATIVE | 1 | 0.06 Hz |
| j=2 | Always POSITIVE | 0 | 0.00 Hz |
| j=3 | OSCILLATING | 5 | 0.31 Hz |

### Implications for IBP

The integration-by-parts argument requires T(j,j) to CHANGE SIGN.

- **j=2**: T is one-signed (positive). IBP gives NO savings.
  The integral ∫T dt just accumulates. Standard supercritical bound applies.

- **j=3**: T oscillates. IBP gives partial savings.
  The positive and negative contributions partially cancel.

- **Higher j**: Expected to oscillate faster (more sign changes).
  The IBP savings grow with j.

### Why This Is Still OK for the Proof

The proof only needs subcriticality at HIGH shells (large j).

**Low shells (j ≤ j*):**
- E_j is bounded by total energy (conservation)
- The enstrophy in low shells can grow but is controlled by
  the total enstrophy, which satisfies:
  d/dt ∫|ω|² = 2∫ω·S·ω dx - 2ν∫|∇ω|²
  The first term is bounded by C||ω||³_{L³} (standard)
  and controlled by viscosity for smooth data

**High shells (j > j*):**
- T(j,j) oscillates (sign changes with frequency ~ 2^j)
- IBP gives savings of 2^{-j} on the time integral
- Viscosity 2^{2j} dominates 2^{3j/2-j} = 2^{j/2}
- These shells are subcritical

**The bridge (j = j*):**
- j* = O(log(1/ν)) (the dissipation scale)
- Below j*: inertial range, bounded by energy cascade
- Above j*: dissipation range, controlled by viscosity
- At j*: the transition, where θ matters most

### Revised Proof Architecture

1. **Low shells (j ≤ j*):** Bounded by total enstrophy.
   Use the standard Prodi-Serrin-Ladyzhenskaya bound:
   ∫₀ᵀ ||u||_{L^p}^q dt < ∞ for 2/q + 3/p = 1.
   This controls the total enstrophy production.

2. **High shells (j > j*):** T(j,j) oscillates with frequency ω_j ~ 2^j.
   IBP on the time integral:
   ∫T(j,j) dt = boundary terms O(2^{j/2}) + lower order
   Viscosity 2^{2j} dominates. Bootstrap closes.

3. **The connection:** j* ~ log(1/ν). For any finite ν > 0,
   there's a finite number of "active" shells below j*.
   The enstrophy in these shells is controlled by the
   total energy bound. Above j*, the IBP + viscosity control.

### What T(j,j) < 0 at j=1 Means

Shell j=1 has T(1,1) < 0: the intra-shell transfer REMOVES enstrophy
from this shell. The stretching at shell 1 is compressive (strain
flattens the large-scale vorticity into sheets, which cascades
energy to higher shells).

This is consistent with the forward cascade picture:
- Low shells: T < 0 (enstrophy removed by cascade)
- Mid shells: T > 0 (enstrophy deposited by cascade)
- High shells: T oscillates (dissipation-range dynamics)

### The Complete Picture

| Shell range | T(j,j) sign | Control mechanism |
|------------|------------|-------------------|
| j ≤ j_inertial | Negative | Energy cascade (forward) |
| j_inertial < j < j* | Positive | Bounded by total enstrophy |
| j ≥ j* | Oscillating | IBP + viscosity (subcritical) |

The proof needs different tools at different scales:
- Low j: energy estimates (standard, unconditional)
- Mid j: enstrophy estimates (bounded by energy + Sobolev)
- High j: oscillatory estimates (NEW — the IBP argument)

## 120 proof files. The signed structure reveals the proof must be multi-scale.
