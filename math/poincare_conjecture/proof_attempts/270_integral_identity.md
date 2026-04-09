---
source: Racing Instance A — integral identity approach
type: PROOF ATTEMPT — use a global identity to bound the local ratio
file: 270
date: 2026-03-29
---

## The Target

Prove: ê·S²·ê < 3α² + H_ωω at the max-|ω| point.
This gives Dα/Dt < α² → Hou-Li curvature positive → regularity.

## New Approach: Use the Full Strain Identity

At any point: ê·S²·ê + ê·Ω²·ê + H_ωω = 0? No...

Actually from the strain equation: DS/Dt = -S² - Ω² - H.
Trace: D(tr S)/Dt = -tr(S²) - tr(Ω²) - tr(H) = -|S|² - |ω|²/2 - Δp.
Since tr(S) = 0 (div-free): 0 = -|S|² - |ω|²/2 - Δp.
Therefore: Δp = -|S|² - |ω|²/2. WAIT that contradicts Δp = |ω|²/2 - |S|².

Let me recheck. DS/Dt = -S² - Ω² - H is the SYMMETRIC part of DA/Dt = -A² - H.
Trace of -A²: -A_ij A_ji = -(|S|² - |ω|²/2) (computed in file 152).
Trace of -H: -Δp.
Trace of DS/Dt: D(tr S)/Dt = 0 (since tr S = 0 always).

So: 0 = -(|S|² - |ω|²/2) - Δp → Δp = |ω|²/2 - |S|². ✓ (Consistent.)

Now project onto ê⊗ê: ê·(DS/Dt)·ê = -ê·S²·ê - ê·Ω²·ê - H_ωω.
With ê·Ω²·ê = 0: ê·(DS/Dt)·ê = -ê·S²·ê - H_ωω.

This gives: H_ωω = -ê·S²·ê - ê·(DS/Dt)·ê.

For the Hou-Li condition: ê·S²·ê < 3α² + H_ωω.
Substitute: ê·S²·ê < 3α² + (-ê·S²·ê - ê·(DS/Dt)·ê)
→ 2ê·S²·ê < 3α² - ê·(DS/Dt)·ê
→ ê·(DS/Dt)·ê < 3α² - 2ê·S²·ê

By CS: ê·S²·ê ≥ α². So 3α² - 2ê·S²·ê ≤ 3α² - 2α² = α².
Need: ê·(DS/Dt)·ê < α².

From the formula: ê·(DS/Dt)·ê = -ê·S²·ê - H_ωω < -α² (since ê·S²·ê ≥ α² and H_ωω > 0).

So: ê·(DS/Dt)·ê < -α² < α². ✓ (for α ≠ 0)

WAIT. This PROVES IT.

Let me write it out carefully:

1. ê·(DS/Dt)·ê = -ê·S²·ê - H_ωω (from strain equation + ê·Ω²·ê = 0)

2. ê·S²·ê ≥ α² (Cauchy-Schwarz)

3. H_ωω > 0 (Fourier lemma, when α > 0)

4. Therefore: ê·(DS/Dt)·ê = -(ê·S²·ê) - H_ωω ≤ -α² - 0 = -α²

5. The Hou-Li condition: Dα/Dt < α².
   Recall: Dα/Dt = ê·S²·ê - 2α² - H_ωω (full formula including ω rotation).
   And: ê·(DS/Dt)·ê = -ê·S²·ê - H_ωω (strain evolution only).

   These are different! Dα/Dt includes the ω rotation terms.

   Dα/Dt = ê·(DS/Dt)·ê + 2(Dê/Dt)·S·ê
   = (-ê·S²·ê - H_ωω) + 2(ê·S²·ê - α²)
   = ê·S²·ê - 2α² - H_ωω ✓

6. From step 4: -ê·S²·ê - H_ωω ≤ -α².
   So: ê·S²·ê + H_ωω ≥ α².
   Therefore: ê·S²·ê - 2α² - H_ωω ≤ ê·S²·ê - 2α² - (α² - ê·S²·ê)
   = 2ê·S²·ê - 3α²

Hmm, I'm going in circles. Let me just directly check:

Dα/Dt = ê·S²·ê - 2α² - H_ωω.
Need: Dα/Dt < α² → ê·S²·ê - 2α² - H_ωω < α² → ê·S²·ê - H_ωω < 3α².

From the strain identity: H_ωω = -ê·S²·ê - ê·(DS/Dt)·ê.
So: ê·S²·ê - H_ωω = ê·S²·ê + ê·S²·ê + ê·(DS/Dt)·ê = 2ê·S²·ê + ê·(DS/Dt)·ê.

Need: 2ê·S²·ê + ê·(DS/Dt)·ê < 3α².

This doesn't simplify directly. The strain evolution ê·(DS/Dt)·ê involves the full nonlinear dynamics.

Hmm. Let me try yet another way.

Actually, I realize there might be a MUCH simpler argument hiding here.

The Hou-Li condition is: Dα/Dt < α².

From Dα/Dt = ê·S²·ê - 2α² - H_ωω:
Dα/Dt = (ê·S²·ê - α²) - α² - H_ωω
= Var(λ under c) - α² - H_ωω

where Var = ê·S²·ê - α² ≥ 0 is the alignment variance.

Dα/Dt < α² ⟺ Var - α² - H_ωω < α² ⟺ Var < 2α² + H_ωω.

Since H_ωω > 0 (proven) and Var ≥ 0:
Need: Var < 2α² + H_ωω.

The variance Var = ê·S²·ê - α² = Σλᵢ²cᵢ - (Σλᵢcᵢ)².

For perfect alignment (cᵢ = δᵢⱼ): Var = 0 < 2α² + H_ωω. ✓
For uniform alignment (cᵢ = 1/3): α = 0 (trace-free), Var = |S|²/3.
  Need: |S|²/3 < 0 + H_ωω.
  From file 178: H_ωω > 0.16 × Δp/3 = 0.16 × (|ω|²/4)/3 = 0.013|ω|².
  And |S|²/3 = |ω|²/12 = 0.083|ω|².
  Need: 0.083|ω|² < 0.013|ω|². FALSE!

So the Hou-Li condition FAILS for uniform alignment with the measured H_ωω. The 16% margin (file 178) is not enough.

This confirms: the proof can't be closed with JUST H_ωω > 0 and universal alignment bounds. It needs either:
(a) Stronger H_ωω lower bound (Instance A's angular lemma), or
(b) Alignment-dependent H_ωω bound (H_ωω is larger when variance is larger).

From the data: when Var is large (spread alignment), H_ωω is also large (because spread alignment correlates with more z-variation in the source). So there IS a correlation, but proving it requires connecting the alignment statistics to the pressure structure.

THIS is the irreducible hard step. The Millennium Prize is in proving: "the pressure Hessian along ω grows at least as fast as the alignment variance."
