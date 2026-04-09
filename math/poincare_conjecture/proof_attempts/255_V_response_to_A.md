---
source: Instance B responds to Instance A's adversarial findings
type: VALIDATION — evaluating the three fatal issues
date: 2026-03-29
---

## Issue 1: Step 5 — D(Δp)/Dt ≠ |ω|²α (HIGH)

Instance A is RIGHT. D(Δp)/Dt = D(|ω|²/2)/Dt - D(|S|²)/Dt.
D(|ω|²/2)/Dt = |ω|²α (correct).
D(|S|²)/Dt involves third-order terms (S³, S·Ω², S·H).
We DROPPED the D|S|²/Dt term. This is not justified.

SEVERITY: HIGH. The dynamic Fourier lemma (Step 5) applied
D(Δp)/Dt = |ω|²α as if |S|² doesn't change. But |S|² DOES change.

CAN IT BE FIXED? Maybe. D|S|²/Dt = -2tr(S³) - 2tr(S·Ω²) - 2tr(S·H).
The leading term: -2tr(S³) involves third-order eigenvalue products.
For trace-free S: tr(S³) = 3λ₁λ₂λ₃ = 3det(S).
This can be positive or negative depending on eigenvalue ratios.

The correction D|S|²/Dt to D(Δp)/Dt could flip the sign of the
z-cosine component. This needs MEASUREMENT.

VERDICT: Step 5 IS BROKEN as stated. Need to either:
(a) Bound |D|S|²/Dt| < |D|ω|²/Dt| (so the correction is small)
(b) Find a different argument for DH > 0
(c) Replace the DH > 0 step entirely (Instance A's recommendation)

## Issue 2: Step 7 — Q < 0 ⇏ R < 1 (HIGH)

Instance A's counterexample: Δp/3=10, H_dev,ωω=+20, Var=25.
H_ωω = Δp/3 + H_dev,ωω = 10 + 20 = 30.
Q = Var - H_ωω = 25 - 30 = -5 < 0. ✓
But R = |H_dev,ωω|/(Δp/3) = 20/10 = 2 > 1. ✗

So Q < 0 and R > 1 can coexist. The bootstrap assumed Q < 0 → R < 1.
This is WRONG.

SEVERITY: HIGH. The bootstrap chain is broken.

CAN IT BE FIXED? Instance A suggests replacing Step 7 with a SCALING
argument: at high |ω|, the -Ω² term dominates -H regardless of R.
This is because -Ω² ~ |ω|² while -H ~ |ω|²/12 (maximum, from Δp/3).
The ratio is 3:1 at minimum (from |ω|²/4 vs |ω|²/12).

Actually wait: -Ω² off-diagonal is (1/4)|ω|²√(cᵢcⱼ).
-H off-diagonal is bounded by ||H||_op ≤ ||H||_F.
||H||_F ≤ √(tr(H²)) which involves |ω|⁴ terms... not obviously small.

The SCALING argument: -Ω² contributes |ω|²/4 to eigenvector rotation.
-H contributes at most ||H_dev||_op/|eigenvalue gap|.
The eigenvalue gap: |λᵢ-λⱼ| ~ |S| ~ |ω|/2.
||H_dev||_op: hard to bound without CZ.

So the scaling argument ALSO hits the CZ barrier for the off-diagonal.

VERDICT: Step 7 IS BROKEN. The fix (scaling) needs careful analysis.

## Issue 3: Step 2 — f_k > 0 at x* ≠ f_k everywhere (MODERATE)

The Fourier lemma (file 267) uses: (Δ_xy - k²)p_k = f_k.
p_k(x₀,y₀) = ∫G(x₀,y₀;x',y') f_k(x',y') dx'dy'.
If f_k > 0 EVERYWHERE on T²: then p_k < 0 (Green's function negative). ✓
If f_k CHANGES SIGN: p_k(x₀,y₀) could be positive.

The issue: we need f_k > 0 everywhere, but we only showed f_k > 0 at (x₀,y₀).

SEVERITY: MODERATE. For concentrated sources (f_k large at (x₀,y₀) and
small elsewhere): the Green's function is DOMINATED by the (x₀,y₀) region.
So p_k is approximately -(positive) even if f_k is slightly negative elsewhere.

For the QUANTITATIVE version: need the positive part of f_k to dominate
the negative part in the Green's function integral.

CAN IT BE FIXED? For |ω|² concentrated at x*: the source f = |ω|²/4
is also concentrated. The k-th z-Fourier component f_k is concentrated
at (x₀,y₀) (because |ω|² is). So f_k > 0 near (x₀,y₀) and ≈ 0
elsewhere. The Green's function integral is dominated by the positive
part. QUANTITATIVELY: need σ_xy << 1/k (so the source fits within one
Green's function oscillation length). This holds for k small (k=1,2).

VERDICT: Step 2 needs a CONCENTRATION CAVEAT but is fixable for small k.

## OVERALL

Instance A found real issues. Steps 5 and 7 are genuinely broken.
Step 2 has a moderate gap (fixable with concentration).

THE PROOF IS NOT COMPLETE. It's ~70% done (Instance A's estimate).

The remaining 30%:
1. Replace DH > 0 argument (Step 5) — needs new approach
2. Fix the bootstrap (Step 7) — drop R < 1, use scaling directly
3. Quantify the concentration in Step 2

## 255. Instance A's review is ACCURATE. The proof has 2 fatal gaps.
