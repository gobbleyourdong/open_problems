---
source: Web/arXiv search round 2
type: Literature — geometric alignment approaches
status: FOUND KEY CONNECTIONS
---

## New Findings

### 1. "Lagrangian Phase-Lag" (arXiv 2601.08862, Jan 2026)
KEY FINDING: There is a systematic PHASE LAG between strain and vorticity alignment.
Classical theories assume instantaneous alignment — this paper shows alignment
is PRECEDED by pressure field topology acting as a geometric precursor.

**Connection to us:** The phase lag means ω and S are NEVER perfectly aligned
instantaneously. There's always a delay. This is the MECHANISM behind our
observation that the growing fraction decays — perfect alignment (which Q > 0 requires)
is prevented by the phase lag dynamics.

If we can bound the phase lag angle → we can bound P(Q > 0) directly.

### 2. "Geometric Characterization of Potential NS Singularities" (arXiv 2501.08976, Jan 2025)
Studies vorticity contained in cones with opening angle π.
Geometric constraints on how vorticity direction can vary near singularities.

**Connection to us:** If a singularity requires vorticity to be in a narrow cone,
and our data shows the cone angle (alignment fraction) goes to zero with resolution,
the singularity can't form.

### 3. "Microlocal Regularity" (arXiv 2601.08854, Jan 2026)
Introduces "microlocal amplitudes" and "directional energy functionals."
Monotone volume invariants that quantify directional concentration.

**Connection to us:** Our infection ratio IS a directional energy functional.
The fraction of points where stretching direction dominates is exactly a
measure of directional concentration. If their monotone invariants apply,
our decay might follow from their framework.

### 4. Retracted paper warning
"A Geometric Constraint Framework for Global Regularity" was RETRACTED.
This used geometric arguments similar to ours. Must understand WHY it was
retracted to avoid the same pitfall.

## New Proof Idea: Phase-Lag Bound

From the Lagrangian phase-lag paper:
- The angle between ω and the principal strain direction has a MINIMUM value
  determined by the pressure topology
- This minimum angle θ_min > 0 means cos²θ < 1 always
- The stretching ω·S·ω = |ω|²|S|cos²θ < |ω|²|S|(1-θ_min²)
- If θ_min grows with resolution (more modes = more phase lag)
  → stretching is bounded below dissipation at high k

This is a GEOMETRIC bound that uses the specific structure of NS,
not generic norm estimates. It's exactly what the Latala approach was missing.

## Action Items
1. READ arXiv 2601.08862 in detail — the phase lag mechanism
2. READ arXiv 2501.08976 — the cone constraint
3. Check if the phase lag angle θ_min is computable from the kernel
4. If θ_min ~ 1/k (grows with wavenumber) → proof closes
5. This would be the tightest possible geometric bound

## Updated Proof Ranking
1. **Phase-lag bound** (new, from literature) — geometric, uses NS structure
2. **ChatGPT alignment-rarity** — counting constraints, general
3. **Grok spectral convergence** — fallback
4. **Manus Latala** — failed (σ₃ grows too fast)
5. **Nemotron diagonalization** — failed (Q doesn't diagonalize)
