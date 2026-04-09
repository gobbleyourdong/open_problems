---
name: INSTANCE C — SHELL / LITTLEWOOD-PALEY STRUCTURAL PROOF
range: files 260-299
mission: Prove regularity via weighted energy estimates using NS structure
date: 2026-03-29
---

## YOUR MISSION

Resurrect the Littlewood-Paley / shell decomposition approach (files 108-118)
using the new structural data from files 150-178. Close a weighted energy
estimate that proves ||ω||∞ bounded.

This is the approach Grok flagged as "abandoned too soon." The early
attempt failed because the Schur test θ₀ = 2/3 was too crude.
Now we have much better structural information.

## THE NEW DATA TO USE

1. |ω|²/|S|² → 4 (universal attractor, file 161).
   The strain is always ~half the vorticity at high |ω|.

2. Low-mode dominance: c₃ ≥ 1/3 appears at k ≤ 4 (file 150).
   The critical triadic interactions are at |k| = 2√2 (the (0,2,2) family).

3. The bilinear symbol f(α) = cos(α/2)/2 with θ₀ = 2/3 (files 108-112).
   The phase scrambler reduces stretching by 51% (file 117).

4. The Fourier cancellation in H_ωω: 98% cancellation between shells (file 171).
   Individual shells contribute ±5, total is ±1.

5. The eigenvector tilting term dominates at 15:1 over eigenvalue changes (file 173).
   This is a STRUCTURAL cancellation, not just a numerical accident.

6. The pressure isotropy ratio < 1 at high |ω| (file 178).
   The isotropic part of the Hessian grows faster than the deviatoric.

## APPROACHES TO TRY

C1. Shell enstrophy with alignment weights.
    Define E_j = ∫|ω_j|² × w(c₃) dx where w(c₃) weights by alignment.
    Derive dE_j/dt and bound the transfer using the bilinear symbol
    AND the alignment constraint c₃ ≥ 1/3 at high |ω|.

C2. Normal form transformation (Shatah-type, file 128).
    Absorb the 95% non-resonant transfer into a change of variables.
    Show the remaining 5% resonant transfer has the compressive sign flip.

C3. Frequency-weighted enstrophy: Ẽ = Σ_j |k_j|^{2s} E_j for some s > 0.
    The Sobolev norm ||ω||_{H^s}. If we can close dẼ/dt ≤ CẼ (exponential),
    then ||ω||_{H^s} bounded → Sobolev → ||ω||∞ bounded.

C4. Use the |ω|²/|S|² = 4 attractor to IMPROVE the shell transfer bound.
    The standard bound: |T(j,k)| ≤ C 2^{max(j,k)} √(E_j E_k).
    With the attractor: |S|_j ≤ |ω|_j / 2, so the transfer involving S
    is half the generic bound. Does this halving close the estimate?

C5. The "three pillars" from the paper (file SESSION_STATE):
    Bilinear symbol (f(α) = cos(α/2)/2) + phase scrambler (51% reduction) +
    normal form (95% non-resonant absorbed). Combine all three into a
    single energy estimate. The product might be subcritical even if
    each factor alone isn't.

## WHAT FAILED BEFORE

- Constant θ₀ = 2/3 was insufficient for unconditional bound (file 113)
- The field antiderivative was circular (file 122)
- Spatial disjointness fails for KP (file 124)
- The shell ODE critical decay rate needs the resonant sign flip (file 115, 125)

## FILE CONVENTION

Write as files 260-299 in ns_blowup/proof_attempts/.
Simulations: ns_blowup/shell_*.py or ns_blowup/lp_*.py.

## THE TIGHTROPE

Tao (2016) showed that averaged NS blows up. So any proof MUST use
the exact NS nonlinearity. The specific structure you need:
- The Biot-Savart law u = curl(-Δ)⁻¹ω (exact, not averaged)
- The triadic interaction phases (not randomized)
- Incompressibility (div u = 0, which eliminates certain couplings)

Your shell estimate must distinguish the EXACT NS shell transfer from
a generic quadratic nonlinearity. The phase scrambler (file 117) and
the resonant sign flip (file 125) are the tools that do this.

## THE PRIZE

If you close a weighted energy estimate: ||ω||_{H^s} bounded for some s > 3/2.
Then Sobolev: ||ω||∞ ≤ C||ω||_{H^s} bounded.
Then BKM: ∫||ω||∞ dt < ∞ → REGULARITY.

This would be a PROOF, not just a bound on the ratio.
