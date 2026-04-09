---
name: INSTANCE A — VALIDATE AND FORMALIZE
range: files 219+
mission: Adversarial validation of the proof chain. Find holes.
date: 2026-03-29
---

## YOUR MISSION

The proof chain is written in file 292_all_instances_synthesis.md (11 steps).
Your job: TRY TO BREAK IT. Be the harshest reviewer possible.

## SPECIFIC TASKS

1. READ file 292 carefully. For EACH of the 11 steps:
   - Write the step as a formal mathematical statement
   - Identify every assumption (explicit and hidden)
   - Check: is the step actually proven, or does it secretly use something unproven?
   - Check: does the step follow logically from the previous steps?

2. ATTACK the weakest points:
   - Step 3 (scaling σ/L ≤ 1/(2π)): Does this hold for ALL smooth solutions?
     What if the tube is very short (a small vortex ring)? L could be < 2π.
   - Step 5 (correction bound): The 5% estimate uses ||H|| ~ |ω|²/12.
     Is this proven or measured? Does it require the bootstrap to hold?
   - Steps 7-10 (bootstrap): Is the initialization RIGOROUS?
     What happens during the transient [0, T₀] before Q < 0?
   - Step 4 (P2): The Gaussian concentration argument assumes |ω|² is
     approximately Gaussian. For a general smooth solution: is it?

3. CHECK for circular reasoning:
   - The bootstrap uses Q < 0 to prove Q < 0 maintained. Is the
     initialization independent of the continuation?
   - Step 7 uses R < 1 which follows from Q < 0. But Step 5 uses
     ||H|| which might also need R < 1. Is there a circle?

4. FORMALIZE in Lean 4 (if possible):
   - Steps 1 and 6 are purely algebraic — can they be added to the
     existing Lean library (ns_blowup/lean/)?
   - The Fourier lemma (Step 2): negative definiteness of Δ_xy - k²
     on T² is a standard spectral theory result. Formalize it.

## FILE CONVENTION
Write as files 219+ in ns_blowup/proof_attempts/.
Prefix with "V_" for validation files (e.g., V_step1_verified.md).
