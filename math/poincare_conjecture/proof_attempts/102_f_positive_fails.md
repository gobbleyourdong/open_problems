---
source: f = |ω|²/2 - |S|² > 0 check on {|ω| > threshold}
type: DEAD END — f < 0 at many high-ω points (strain dominates)
date: 2026-03-26
---

## Result: f = |ω|²/2 - |S|² is NOT universally positive on {|ω| > ρ_c}

```
t=3.00: min f = -3.81, min ratio |ω|²/(2|S|²) = 0.37
t=4.00: min f = -58.2, min ratio = 0.04 (strain 25× vorticity!)
```

## What This Kills

- Level-set theorem (file 096): relied on f > 0 → Δp > 0 → pressure opposes
- Harmonic shielding (file 098): relied on H_iso = Δp/3 > 0 inside Ω

At the MAXIMUM x*: f > 0 always (confirmed). But at other high-ω points:
strain from nearby structures makes |S|² >> |ω|²/2.

## What Survives

- Littlewood-Paley (files 100-101): works in L² shells, doesn't need f > 0
- Shell transfer data: tridiagonal + small diagonal — STILL VALID
- Miller's eigenfunction distance: independent of pressure sign
- The proof at x* specifically: f(x*) > 0 always

## Lesson

The vortex sheet has |ω| large AND |S| large along its entire extent.
Only at the PEAK of |ω| does |ω|² dominate |S|². Elsewhere on the
sheet: strain dominates. The level-set approach can't work because
the high-ω set includes the entire sheet, not just its peak.

102 proof files. Level-set path dead. Littlewood-Paley path lives.
