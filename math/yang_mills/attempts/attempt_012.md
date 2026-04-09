# Attempt 012 — Correction: The SZZ/Nissim Program

**Date**: 2026-04-07
**Phase**: 2 (Exploration)
**Instance**: Even (Theory)

## CORRECTION TO ATTEMPT 009

**The paper arXiv:2510.22788 is by Ron Nissim (MIT), NOT Adhikari-Butez-Chatterjee.**
And it proves mass gap at **STRONG COUPLING ONLY**, not all couplings.

My earlier assessment ("proved mass gap in 't Hooft limit — BREAKTHROUGH") was
misleading. The result is in the SAME regime as Osterwalder-Seiler (1978) — strong
coupling — just with sharper modern methods and for U(N) specifically.

## The Actual State of the Art

### Shen-Zhu-Zhu (SZZ23, arXiv:2204.12737)
- Proved mass gap for **SU(N) and SO(N)** at strong coupling (β < c_d)
- Method: Langevin dynamics + Bakry-Émery criterion
- Key: SU(N) has uniformly positive Ricci curvature → exponential mixing
- This modernizes Osterwalder-Seiler with stochastic analysis

### Nissim (2025, arXiv:2510.22788)
- Extended SZZ23 to **U(N)** at strong coupling
- Challenge: U(N) = U(1) × SU(N), and U(1) has ZERO Ricci curvature
- Solution: Decompose into three steps:
  1. Cluster expansion for U(1) conditional measure (à la OS78)
  2. Show conditional observables are almost local
  3. Bakry-Émery for SU(N) marginal (à la SZZ23)
- Result: mass gap for U(N), all d ≥ 2, N ≥ 26, β < 10^{-6d}

### What ALL these results share
**They are all STRONG COUPLING.** β must be small (g must be large).

### What remains open
Mass gap at **weak coupling** (large β, small g) or at **all couplings**.
This is the actual Clay Millennium Problem. NOBODY has proved it.

## Revised Route Assessment

**Route 1 (extend strong coupling to all couplings)**: The SZZ/Nissim methods
are clean but fundamentally limited to strong coupling. The Bakry-Émery criterion
requires β < c_d (the Hessian perturbation must be dominated by Ricci curvature).
At weak coupling, the perturbation EXCEEDS the curvature → criterion fails.

**There is no known way to extend Bakry-Émery-type arguments to weak coupling
for lattice gauge theories.** The positive Ricci curvature of SU(N) helps at
strong coupling but is overwhelmed by the interaction at weak coupling.

Route 1 rating: ★★★★★ → **★★★** (strong coupling only, no path to weak)

**Route 2 (Tomboulis)**: Remains the ONLY attempt at all couplings. The MK
decimation doesn't distinguish strong from weak coupling — it FLOWS from weak
to strong. This is its unique strength.

Route 2 rating: ★★★★ → **★★★★★** (promoted to top route)

## The Revised Picture

```
STRONG COUPLING MASS GAP:
  ✓ Osterwalder-Seiler (1978) — cluster expansion
  ✓ SZZ23 (2023) — Langevin + Bakry-Émery for SU(N), SO(N)
  ✓ Nissim (2025) — extended to U(N)
  ✓ Adhikari-Cao (2022) — finite groups at WEAK coupling (different!)

ALL COUPLINGS:
  ✗ NOBODY has proved this for any continuous non-abelian gauge group in d ≥ 3
  ~ Tomboulis (2007) — claimed but disputed (gap: inequality 5.15)
  ~ Chatterjee (2021) — mass gap ⟹ confinement (but doesn't prove mass gap)

THE GAP IS STILL: strong coupling → ALL couplings
```

## The Deep Reason the Gap Persists

At strong coupling: the gauge field fluctuations are LARGE and essentially
independent. The theory is like a disordered system → cluster expansion works.

At weak coupling: the gauge field is nearly ordered (close to a classical
vacuum). The mass gap arises from COLLECTIVE non-perturbative dynamics
(confinement, flux tubes, glueballs). These are not captured by any local
perturbative method.

The mass gap at weak coupling is a genuinely NON-PERTURBATIVE phenomenon.
It requires understanding the global structure of the gauge field configuration
space, not just local fluctuations.

## What the Even Instance Should Do

1. **Focus on Tomboulis (Route 2)** — the only path to all couplings
2. Investigate whether the MK decimation preserves the vortex cost (5.15)
3. Study the algebraic structure: WHY should SU(2) preserve Z > Z⁺ but U(1) not?
4. The answer should involve center symmetry / π₁ / non-abelian structure

## Result
Major correction applied. No one has proved mass gap beyond strong coupling
for continuous non-abelian groups. Tomboulis promoted to primary route.
The SZZ/Nissim program is excellent mathematics but doesn't reach the gap.
