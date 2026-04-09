---
source: Dynamic tube lattice with back-reaction
type: MODEL RESULT — amplification survives in symmetric configurations
date: 2026-03-26
---

## Results

### Static model (no back-reaction): AMPLIFICATION possible
### Dynamic model (with back-reaction):

- 2 tubes 85°: NaN (numerical instability from core thinning)
- 5 perpendicular cascade: AMPLIFICATION (ratio=499×, 0° direction change!)
- 10 optimal chain: NaN (same instability)

### Why the cascade survives:

The perpendicular (x,y,z) arrangement makes each tube an EIGENVECTOR
of the other tubes' strain. The direction rotation term (I-ê⊗ê)·S·ê = 0
because S·ê ∥ ê for this symmetric configuration.

This is the TG case: ε = 0, tight CS, no anti-twist.
The adversary uses SYMMETRY to avoid the anti-twist mechanism.

### What the model DOESN'T capture:

1. Tube bending (straight tubes in model, curved in NS)
2. Reconnection (topology preserved in model, changes in NS)
3. Nonlocal pressure (simplified BS in model, full Poisson in NS)
4. The ω⊗ω - |ω|²I term in strain equation (dropped in model)

### What this means for the proof:

Single-mode orthogonality + direction rotation are NECESSARY but
NOT SUFFICIENT. The symmetric adversary evades them.

The proof NEEDS at least one of:
- Tube bending (curvature prevents sustained straight geometry)
- Reconnection (topology change destroys the symmetric configuration)
- Pressure nonlocality (the full Poisson equation prevents local BS)
- Miller's ω⊗ω term (the vorticity-strain coupling the model drops)

### Connection to the real problem:

The perpendicular cascade IS Taylor-Green vortex (approximately).
TG has x,y,z-oriented vortex sheets. Our TG data shows ratio > 1
at low resolution (vortex sheet amplification = the cascade working).
But at sufficient resolution: ratio CONVERGES (sheet resolves, cascade terminates).

The termination mechanism: the sheet THINS until viscosity resolves it,
then the perpendicular forces CREATE bending (Shimizu-Yoneda), and
the bending destroys the symmetric configuration. Anti-twist kicks in
AFTER the symmetry breaks.

103 proof files. The model confirms the algebraic lemmas aren't enough.
The proof needs the geometric/dynamic mechanisms.
