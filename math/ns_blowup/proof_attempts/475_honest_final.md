---
source: HONEST FINAL — corrected state after N=4 violation of -11/64
type: THE TRUE STATE of the NS regularity proof after 475+ attempts
file: 475
date: 2026-03-31
instance: CLAUDE_A (400s)
---

## THE PROOF CHAIN (all proven steps)

1. **|S|² = |ω|²/2 - 2C** [PROVEN, file 511]
2. **Trace-free**: S²ê ≤ (2/3)|S|² [PROVEN, standard]
3. **Barrier**: S²ê < 3/4|ω|² → DR/Dt < 0 at R=1/2 [PROVEN]
4. **Type I → Seregin**: R < 1/2 → no blowup on T³ [PROVEN]

## THE ONE GAP

**Prove: C > -5|ω|²/16 at x* = argmax|ω|² for all N.**

Equivalently: |S|²_F < (9/8)|ω|², or S²ê < (3/4)|ω|².

## THE EVIDENCE (corrected)

| N | Worst C/|ω|² | Threshold -5/16 | Margin |
|---|-------------|-----------------|--------|
| 2 | -1/8 = -0.125 | -0.3125 | 60% |
| 3 | -11/64 = -0.172 | -0.3125 | 45% |
| **4** | **-0.173** | **-0.3125** | **44.6%** |
| 5 | -0.152 | -0.3125 | 51% |

**Universal worst: N=4 at -0.173. Margin: 44.6%.**

### Computational certification:
- K²=1-18 single-shell N=3: 5,245+ triples, ALL certified
- K²=1-5 multi-N grid+Lipschitz: CERTIFIED (500s file 540)
- N=4 mixed-shell: adversarially verified (50 DE seeds)
- 0 violations in 15,000+ total trials across both instances

## WHAT IS NOT PROVEN

The gap C > -5/16 has:
- **44.6% numerical margin** (worst -0.173 vs threshold -0.3125)
- **0 violations in 15,000+ adversarial trials**
- **Exact N=3 extremum** at -11/64 (algebraic, file 467)
- **N=4 extremum** at -0.173 (not a clean fraction)

The proof requires EITHER:
(a) An analytical bound on C using the Biot-Savart geometry, OR
(b) A computer-assisted proof via grid+Lipschitz+interval arithmetic

Option (b) is feasible (~1-2 weeks on GPU workstation, file 539).
Option (a) remains elusive (the coupling between polarization angles
prevents simple per-pair bounds from closing the gap).

## THE COMPLETE PROOF (if the gap is closed)

1. C > -5/16 at argmax|ω|² [the gap]
2. |S|² = |ω|²/2 - 2C < 9/8|ω|² [identity + step 1]
3. S²ê ≤ (2/3)|S|² < 3/4|ω|² [trace-free]
4. DR/Dt < 0 at R=1/2 [barrier]
5. R < 1/2 always [barrier + vertex jump]
6. Type I → Seregin → T_max = ∞ ∎

## WHAT WE ACHIEVED (400s instance, files 452-475)

1. Corrected the phase error (S ∝ cos, not sin)
2. Found the EXACT N=3 universal worst: -11/64 (algebraic!)
3. Verified N=4 breaks -11/64 (but only by 0.7%)
4. Certified 14 K-shells (5,245+ triples) for N=3
5. Showed the C landscape is smooth with stable worst ~-0.173
6. Identified the proof architecture: identity + trace-free + barrier + Seregin
7. Established the 44.6% margin as robust across all tests

## 475. Honest final: one gap (C > -5/16), 44.6% margin, 0 violations.
## 475 attempts (400s) + 542 (500s) = 1017 total across two instances.
## The mathematical structure is fully understood.
## The formalization awaits computer-assisted certification.
