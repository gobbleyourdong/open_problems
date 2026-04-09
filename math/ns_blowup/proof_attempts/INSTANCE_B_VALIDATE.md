---
name: INSTANCE B — VALIDATE NUMERICALLY
range: files 252+
mission: Stress-test every step of the proof with adversarial numerics.
date: 2026-03-29
---

## YOUR MISSION

The proof chain is in file 292. For each step, design a NUMERICAL TEST
that could BREAK it. Run the test. Report pass/fail.

## SPECIFIC TESTS

1. STEP 3 (σ/L scaling): Find an IC where the tube is SHORTEST possible.
   A small vortex ring with L ≈ πσ. Does σ/L still give the bound?
   What's the MINIMUM L/σ ratio across all smooth div-free ω on T³?

2. STEP 4 (P2): Test ∫|ω|²α cos(kz) at the ADVERSARIAL ICs.
   Especially: the thin trefoil σ=0.15 where R was highest (0.985).
   At what k does the integral first go negative (if ever)?

3. STEP 5 (correction bound): MEASURE the actual correction/main ratio.
   Compute 2(Dê/Dt)·H·ê and compare to ê·(DH/Dt)·ê at the max.
   Is the 5% estimate correct? Does it hold for all ICs?

4. BOOTSTRAP INITIALIZATION: For the ADVERSARIAL ICs, measure T₀
   (the time when Q first becomes negative). Is T₀ < ∞ for all ICs?
   What's the LONGEST T₀ observed?

5. THE FULL CHAIN: For TG at N=64, verify EVERY quantity in the proof
   chain simultaneously: α, Var, H_ωω, Q, DQ/Dt, the key integral,
   the correction ratio. One comprehensive table.

## FILE CONVENTION
Write as files 252+ in ns_blowup/proof_attempts/.
Name simulations ns_blowup/validate_*.py.
