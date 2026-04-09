---
source: Spatial disjointness fails for Kida-Pelz — NOT universal
type: NEGATIVE RESULT — Lemma 3 needs reformulation
status: IMPORTANT — disjointness is IC-dependent
date: 2026-03-26
---

## Multi-IC Disjointness Results

### TG (ν=10⁻⁴): DISJOINT at j≥3
| j | ratio | verdict |
|---|-------|---------|
| 3 | 0.68 | neutral→disjoint |
| 4 | 0.39 | YES |

### JB Vortex (ν=10⁻²): DISJOINT at j=4
| j | ratio | verdict |
|---|-------|---------|
| 3 | 0.83 | neutral |
| 4 | 0.27 | YES |

### Kida-Pelz (ν=10⁻⁴): NO DISJOINTNESS
| j | ratio | verdict |
|---|-------|---------|
| 1 | 0.89 | neutral |
| 2 | 1.01 | neutral |
| 3 | 1.00 | neutral |
| 4 | 1.00 | neutral |

## Why KP is Different

KP has octahedral symmetry — no fixed stagnation points in the
classical TG sense. The enstrophy is uniformly distributed relative
to the velocity field. The resonant/non-resonant split doesn't
correlate with vorticity concentration.

TG and JB vortex have LATTICE stagnation points where vortex sheets
form. The fine-scale structures get advected away from these points.
KP doesn't have this structure.

## Implications

Lemma 3 (spatial depletion) CANNOT be stated as:
"ω_j is depleted in {|u_{<j}| < threshold}"

This is true for TG-type flows but NOT for general flows.

## What Still Works

1. Normal form absorbs 95% of transfer (IC-independent)
2. The 5% resonant residual exists at stagnation regions
3. For KP: the resonant region has ratio 1.00 (neutral, not concentrated)
4. Neutral means the resonant transfer scales as 5% × total
5. The question: is 5% of the total transfer subcritical?

## The Revised Question

Instead of proving ω_j AVOIDS stagnation points, we need to prove
that the TRANSFER itself is subcritical in the resonant region.

The resonant region has |u_{<j}| < threshold, which means the
strain ∇u_{<j} is bounded by the strain at the diffusion scale.
The stretching ω_j · ∇u_{<j} in the resonant region is bounded by:
||ω_j||_∞ × ||∇u_{<j}||_∞ × volume(R_j)

If volume(R_j) ~ 5% (constant) and ||∇u_{<j}||_∞ is bounded
(by the Sobolev norm of u_{<j}), then the resonant transfer is:
T_res ~ 0.05 × ||ω_j||_∞ × ||∇u_{<j}||_∞ × ||ω_j||_2

This is STILL the same scaling as the full transfer, just with
a factor 0.05. The 5% doesn't change the exponent.

## Status

The spatial disjointness approach is dead for general ICs.
We need a DIFFERENT argument for the resonant residual.

Options:
A. The resonant fraction might decrease with j (data: 25%→6%→5%)
   → plateau at 5%, probably not helpful
B. The strain in the resonant region might be weaker
   (stagnation points have |u|≈0 but |∇u| can be large)
C. The quasi-2D argument (k⊥u constraint)
   → reviewer 1's suggestion, not validated for KP
D. Accept 5% and show it's still subcritical somehow
E. Find a different decomposition entirely

## 124 proof files. Spatial disjointness is IC-dependent. Need new approach.
