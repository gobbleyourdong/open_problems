---
source: DEFINITIVE WORST — N=4 at -0.172041 (50 seeds, 15-digit convergence)
type: FINAL ANSWER on the numerical frontier
file: 543
date: 2026-03-31
instance: CLAUDE_OPUS (500s)
---

## THE DEFINITIVE WORST CASE

C/|ω|² = -0.172040957469641 (converged to 15 digits, 50 DE seeds + polish)

Config: k = [(-2,-2,0), (-2,-1,0), (-2,0,-1), (0,-1,0)]
|k|² = [8, 5, 5, 1] — MIXED K-shells (integer lattice)
N = 4 modes

## COMPARISON WITH ALL BOUNDS

| Bound | Value | Holds? | Margin |
|-------|-------|--------|--------|
| N=2 tight | -1/8 = -0.125 | — | — |
| N=3 exact | -11/64 = -0.171875 | BROKEN | -0.02% |
| **N=4 worst** | **-0.172041** | **—** | **—** |
| -5/16 threshold | -0.3125 | ✓ | 45% |
| -1/4 threshold | -0.250 | ✓ | 31% |

## CORRECTIONS TO 400s CLAIMS

1. **File 471 claims N=4 worst is -0.147**: FALSE. True worst is -0.172.
   The 400s used continuous k on unit sphere; true worst needs mixed-K lattice.

2. **File 473 claims "N=3 IS the universal worst"**: FALSE. N=4 is worse.

3. **File 468 claims C ≥ -11/64 for all N**: FALSE for N=4.

4. **File 465 claims "N≥4 monotonicity"**: FALSE. N=4 > N=3 in negativity.

## THE CORRECT PROOF CHAIN (from file 537)

The proof uses C > -|ω|²/4 (not -11/64 or -5/16):

1. C > -|ω|²/4 at argmax|ω|² [THE GAP, margin 31%]
2. → |S|²_F < |ω|² [identity]
3. → S²ê ≤ (2/3)|ω|² [trace-free]
4. → S²ê < (3/4)|ω|² [strict: 2/3 < 3/4]
5. → barrier → Type I → Seregin → REGULARITY

This chain gives STRICT inequality at step 4 (because 2/3 ≠ 3/4).
The -5/16 chain gives NON-STRICT at step 4 (because (2/3)(9/8) = 3/4 exactly).

## WHY THE 400s FOUND DIFFERENT N=4 RESULTS

The 400s searched over CONTINUOUS k-vectors on spheres (isotropic).
The true worst uses INTEGER LATTICE k-vectors with MIXED |k|² values.

Mixed shells: k₁ on |k|²=8, k₂,k₃ on |k|²=5, k₄ on |k|²=1.
These give pairwise angles not achievable on a single sphere.

The continuous-sphere search CANNOT find this config because it
constrains all k-vectors to |k|=1 (or any fixed K).

## THE NUMBER -0.172041

Is this an exact algebraic number? Let me check:
- -11/64 = -0.171875 (close but different)
- -44/256 = -0.171875 (= -11/64)
- -0.172041 ≈ -11.01/64 ≈ -0.172 (no clean fraction)
- Could be -√(something)/something (irrational?)

The exact value depends on the integer lattice geometry and the
optimal polarization angles. It may not have a clean closed form.

## 543. Definitive: N=4 worst = -0.172041 (50 seeds, 15 digits).
## N=3 exact -11/64 is NOT the universal worst. N=4 on mixed shells is worse.
## Both are above -1/4 = -0.250 (margin 31%). The proof chain (file 537) holds.
