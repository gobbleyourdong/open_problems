---
source: Two-sign verification — Claim 1 holds (90%), Claim 2 fails (14%)
type: PARTIAL — DVar/Dt < 0 but DH_ωω/Dt NOT > 0
date: 2026-03-29
---

## Results (trefoil, α > 0 at max)

DVar/Dt < 0: **90%** (26/29 measurements) — STRONG ✓
DH_ωω/Dt > 0: **14%** (4/29 measurements) — FAILS ✗
BOTH signs: **14%** (4/29) — the two-sign proof doesn't hold

## Why Claim 2 Fails

H_ωω depends on the GLOBAL pressure field. When the max point moves
(even slightly), H_ωω changes because the global Poisson integral
is evaluated at a new location. This creates large DH_ωω/Dt of
either sign, unrelated to the local stretching.

## The Corrected Argument

Don't need DH > 0. Need:
1. DVar/Dt < 0 persistently (measured: 90%) → V → 0 over time
2. H_ωω > 0 on average (measured: 76-100% of high-|ω| points)
3. Eventually V drops below H_ωω → Q = V - H_ωω < 0
4. Q < 0 → Dα/Dt < -α² → α bounded → regularity

The timescale: DVar/Dt ≈ -55 with V ≈ 8 → V hits 0 in ~0.15 time.
The transient Q > 0 lasts ~0.04 time. Consistent.

## What This Adds

The variance ROBUSTLY DECREASES (90% of the time when α > 0).
This is the TILTING MECHANISM in action.
Combined with H_ωω > 0 (from the Fourier lemma + evolution):
Q inevitably becomes negative.

## Formal Gap (unchanged)

Proving DVar/Dt < 0 requires: the -Ω² term dominates in the
variance evolution. This is the same CZ barrier dressed differently.

## 240 files. Claim 1 confirmed. Claim 2 failed. The variance decrease
## is the robust mechanism. The proof still needs the -Ω² dominance bound.
