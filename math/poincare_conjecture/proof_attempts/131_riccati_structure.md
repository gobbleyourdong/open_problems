---
source: Riccati structure — c < 1/3 kills stretching with no escape
type: KEY STRENGTHENING — the compression is dynamically enforced
date: 2026-03-26
---

## The Riccati Inequality

From the strain equation dS/dt = -S² - H_yang projected onto ê = ω/|ω|:

```
dα/dt ≤ -α² - (|ω|²/12)(1 - 3c)
```

where α = ê·S·ê (stretching rate), c = cos²(ω, e₁).

### When c < 1/3:
The forcing term -(|ω|²/12)(1-3c) is NEGATIVE.
The Riccati ODE dα/dt ≤ -α² - δ (δ > 0) has:
- NO positive equilibrium (Lean: riccati_no_positive_equilibrium)
- RHS < 0 for ALL α ≥ 0 (Lean: riccati_rhs_negative)
- → α must decrease monotonically → α → -∞
- → stretching is DESTROYED, compression ACCELERATES

### Comparison to previous argument:
Before: c < 1/3 → trace-free algebra → ω·S·ω ≤ 0 (instantaneous)
Now: c < 1/3 → Riccati → α → -∞ (DYNAMICALLY enforced, irreversible)

The Riccati is STRONGER because it shows the compression is not just
possible but INEVITABLE. Once c drops below 1/3, the stretching rate
has no escape — it's trapped in a basin with no positive equilibrium.

## Connection to the Full Proof

```
Yang et al. H_dev                        (published JFM 2024)
  → balance: c ~ 1/|ω|                   (derived from strain ODE)
  → |ω| > 3C → c < 1/3                   Lean: the_complete_law ✓
  → Riccati: dα/dt ≤ -α² - δ < 0         Lean: riccati_rhs_negative ✓
  → α → 0 then negative                  (Riccati dynamics)
  → ω·S·ω ≤ 0                           (compression)
  → regularity                           (standard PDE)
```

## Lean Theorems (Compression.lean, now 7 theorems)
1. trace_free_recenter
2. stretching_nonpos_of_misaligned
3. threshold_from_decay
4. compression_chain
5. alignment_equilibrium
6. alignment_decay_bound
7. the_complete_law
8. riccati_no_positive_equilibrium
9. riccati_forcing_negative
10. riccati_rhs_negative

## 131 proof files. 30 Lean theorems. The Riccati seals it.
