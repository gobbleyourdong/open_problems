# NS Blowup — Proof Strategy Analysis
# Synthesized from LLM triangulation: Gemini, Grok, Manus (Mar 22, 2026)

## THE KEY FINDING: Euler ≠ NS Proof

Chen-Hou proved Euler blowup. The Euler proof CANNOT extend to NS.

### The Scaling Clash (Gemini, verified)
In Chen-Hou's Euler self-similar coordinates:
- C_l ~ (T-t)^3  (spatial collapse)
- C_ω ~ (T-t)^{-1}  (vorticity growth)

Effective viscosity in rescaled frame:
  ν_eff = ν / (C_l² · C_ω) ~ ν / ((T-t)^6 · (T-t)^{-1}) = ν · (T-t)^{-5}

ν_eff → ∞ as t → T*. Viscosity EXPLODES in the Euler rescaling.
The Euler self-similar profile cannot absorb this — the residual diverges.

### Manus's Error (corrected by Gemini)
Manus computed C_l ~ (T-t)^{-1/c_l} = (T-t)^{-1/3} → ∞.
This is WRONG: C_l is the physical length scale, must shrink to 0.
Correct: C_l ~ (T-t)^{c_l/(-c_ω)} ≈ (T-t)^{2.92} ≈ (T-t)^3 → 0.

### Grok's Error
Claimed "minimal modification" — just add ν·Δ₃ to damping coefficients.
Wrong because Δ₃ contains spatial derivatives (1/L²), not algebraic damping.
The 1/L² amplification from the Laplacian makes viscosity a singular perturbation.

## THE LERAY PROBLEM

To prove NS blowup, must use Leray scaling: L ~ (T-t)^{1/2}.

In Leray scaling, both stretching and viscosity scale as (T-t)^{-2}.
Permanent balance — no small parameter, no perturbation theory.

### Why Leray is Hard
1. NO self-similar solutions exist (Necas-Ruzicka-Sverak 1996).
   Blowup must be "nearly" self-similar or Type II.
2. Profile depends on ν — different ν = different balance = different profile.
3. Supercritical — energy doesn't control the solution in 3D.
4. Type I blowup partially ruled out by Seregin-Sverak results.
5. No perturbative parameter — need exact balance, not approximation.

### What Would Be Needed
- New approximate self-similar profile in Leray scaling
- New linearized operator L_NS (different from Chen-Hou's L)
- New function spaces (not the weighted L∞ ∩ C^{1/2} from Chen-Hou)
- New computer-assisted bounds
- Essentially: a new proof from scratch

## WHAT'S STILL VALID

### Our numerical data — ALL valid
- Euler blowup: T*=0.00365 (Nr=64), γ=2.79 (Nr=128) ✓
- Amplitude scaling: T*·A = 0.366 ✓
- ν_c exists: BLOWUP below, SURVIVED above ✓
- Three exact A100 matches (ν=0, 1e-4, 2e-4) ✓
- Field convergence table ✓
- PySR log(1/τ)/τ fit ✓

### Chen-Hou's Euler proof — valid
- 2D Boussinesq + 3D axisymmetric Euler: PROVEN
- Interior blowup with (1-r²)^18 IC: numerical evidence for NS

### The loop gain concept — valid as heuristic
- G ~ UR²/(νZ) captures the physics
- But proving G > 1 rigorously requires the full stability analysis
- In Leray scaling, G is O(1) permanently — can't prove it's >1 by scaling alone

## LLM TRIANGULATION SUMMARY

### Consensus (all three agree)
- The feedback loop u₁→ψ₁→ω₁→u₁ drives the blowup
- ν_c exists and represents a bifurcation
- γ=1.0 is the self-similar attractor
- Chen-Hou Euler proof is solid

### Gemini's contributions (confirmed)
- Loop gain proxy: G ~ UR²/(νZ)
- Hopf bifurcation at ν_c (2/3 agree, Grok says saddle-node)
- (T-t)^{-5} scaling clash — VERIFIED, kills Euler→NS extension
- log(1/τ)/τ from center-manifold reduction
- Leray scaling needed for NS proof

### Grok's contributions (partially corrected)
- Rigorous status check of all results
- Verified all constants match Chen-Hou
- Saddle-node bifurcation alternative (minority view)
- WRONG on "minimal modification" for NS extension
- WRONG on log being artifact (2/3 say it's real)

### Manus's contributions (partially corrected)
- Careful analysis of Poisson coupling properties
- Conservative assessment of proof difficulty
- Correctly identified need for new viscous profile
- WRONG on C_l exponent (inverted the scaling)
- Good on Q2: interval arithmetic IS needed for rigorous CAP

## OPEN QUESTIONS (post-triangulation)

1. Can the Hou 2022 interior blowup be proven in Leray scaling?
   Nobody has done this. No profile exists. This IS the prize.

2. The PySR log correction: Gemini derives it from center-manifold,
   Grok says pure power-law. Can this be settled from our data?
   Test: does the log correction improve fits at higher resolution (Nr=128)?

3. The bifurcation type: Hopf (Gemini, Manus) vs saddle-node (Grok).
   Testable: measure oscillation period vs ν. Constant period = Hopf,
   increasing period = saddle-node.

4. Can the Leray self-similar profile be computed numerically?
   If so, PySR + interval arithmetic might close the proof.
   But Necas-Ruzicka-Sverak says no EXACT self-similar solutions...
   Chen-Hou's "nearly" self-similar approach might work in Leray too.

5. Is there a SIMPLER proof strategy that avoids self-similar analysis entirely?
   E.g., direct energy methods, convex integration, or probabilistic arguments?
