---
source: Instance C — Resonant transfer is POSITIVE at palinstrophy level
type: NEGATIVE RESULT — the sign flip doesn't carry to higher derivatives
file: 263
date: 2026-03-29
---

## Result

Local (resonant) palinstrophy transfer: +308,191 (POSITIVE, stretching)
Nonlocal palinstrophy transfer: +3,583,958 (POSITIVE, 12× larger)
Total: +3,892,149 (POSITIVE)

The resonant compressive sign flip from file 125 (enstrophy level)
does NOT carry over to the palinstrophy level. Both local and nonlocal
transfers feed the high shells.

## What this kills

Approach C2 (normal form): Even if we absorb the nonlocal part,
the resonant (local) part is POSITIVE at the palinstrophy level.
The normal form would leave a STRETCHING resonant term, not compressive.

This means the shell/LP approach CANNOT close the palinstrophy
estimate by exploiting the resonant sign structure.

## Why the sign flips between enstrophy and palinstrophy

Enstrophy: dE_j/dt = T(j) — the TOTAL transfer to shell j.
Low shells (k=1-4) lose enstrophy (T < 0).
The AVERAGE α (weighted by |ω|²) captures this loss → compressive.

Palinstrophy: dP_j/dt = k² T(j) — WEIGHTED by k².
The high shells (k=5-10) have large T(j) > 0 AND large k² multiplier.
The k² weighting amplifies the high-shell stretching,
overwhelming the low-shell compression.

## Instance C status

Approaches tried and failed:
- C4: |ω|²/|S|² = 4 attractor — improves constant, not exponent
- C1/C4: Inverse cascade — fails (forward cascade confirmed)
- C5: Three pillars combined — improves constant 6×, not exponent
- C2: Normal form / resonant sign — POSITIVE at palinstrophy level

Remaining approaches:
- C3: Frequency-weighted enstrophy with the BOOTSTRAP from file 261
  (if ||ω||∞ bounded → dP/dt linear → P bounded)
  But this requires ||ω||∞ bounded FIRST (Instance A's job)

## Conclusion

Instance C cannot close the proof independently.
The shell/LP framework gives CONSTANT improvements (factors 0.16-0.5)
but not EXPONENT improvements. The proof needs the non-local
pressure structure (Instance A's isotropy ratio) to bound ||ω||∞,
after which the palinstrophy bootstrap (file 261) closes everything.

## 263. The shell route circles back to Instance A's inequality.
