---
source: Instance A VALIDATION — Steps 4, 8, 9, 10 (dependent on broken steps)
type: ADVERSARIAL REVIEW
date: 2026-03-29
---

## Step 4: P2 — ∫|ω|²α cos(kz) > 0 [files 288 + 247]

DEPENDS ON: Step 3 (gradient suppression).

CLAIM: The integral I = ∫|ω(z)|² α(z) cos(kz) dz > 0 along the
z-line through x* when α(0) > 0.

The argument: I = α₀∫|ω|² cos dz + ∫|ω|²(α-α₀) cos dz.
First term > 0 (if |ω|² peaks at z=0 and α₀ > 0).
Correction: bounded by ||∂α/∂z|| × (something from Step 3).

REVIEW:
- First term: ∫|ω(z)|² cos(kz) dz with |ω|² peaked at z=0.
  For k=1: this is the first Fourier cosine coefficient of a peaked
  function. For a peaked function: this IS positive (the function's
  Fourier expansion has positive first mode). ✓ for small k.
  For large k: could be negative (oscillatory cancellation). ⚠️
- Correction bound: uses Step 3 (||∂α/∂z|| ≤ 0.16α/σ). DEPENDS ON
  Step 3 which has MODERATE hole (curvature assumption).

ADDITIONAL ISSUE: The integral is over ONE z-line at (x₀,y₀).
But the Fourier lemma (Step 2) needs f_k(x,y) > 0 for ALL (x,y),
not just (x₀,y₀). Step 4 only bounds the integral at (x₀,y₀).

VERDICT: **Step 4 is VALID at (x₀,y₀) for small k, conditional on
Step 3. But it doesn't give f_k > 0 everywhere (needed by Step 2).** ⚠️

---

## Step 8: DVar/Dt < 0 [file 286]

DEPENDS ON: Steps 6 + 7.

CLAIM: Since -S² doesn't rotate eigenvectors (Step 6) and -Ω²
dominates -H in rotation (Step 7): net rotation is toward ω → Var decreases.

REVIEW:
- From Step 6: -S² has no off-diagonal in eigenbasis. ✓
- From Step 7: -Ω² dominates -H. **BROKEN** (Step 7 has logical error).

Even without Step 7: the -Ω² contribution to eigenvector rotation
is ALGEBRAICALLY computable:
  De_i/Dt from -Ω² = (|ω|²/4)Σ_{j≠i} √(c_jc_i)/(λ_i-λ_j) × e_j

This rotates eigenvectors TOWARD ω (when λ_i < λ_j and c_j > 0).
The rotation rate from -Ω² is |ω|²/4 × O(1).

The -H contribution: De_i/Dt from -H = Σ_{j≠i} H_{ji}/(λ_i-λ_j) × e_j.
Magnitude: |H|/(Δλ) where Δλ is the eigenvalue gap.
|H| ~ |ω|² (from the Poisson equation). Δλ ~ |S| ~ |ω|/2.
So: -H rotation rate ~ |ω|²/(|ω|/2) = 2|ω|. WAIT: this doesn't
have the right dimensions. Let me redo.

H_{ji} is a component of the Hessian: |H_{ji}| ≤ ||H|| ~ C|ω|².
λ_i - λ_j ~ |S| ~ |ω|/2.
Rotation rate from -H: ~ |ω|²/(|ω|/2) = 2|ω|.

-Ω² rotation rate: ~ |ω|²/4.

Ratio: (|ω|²/4)/(2|ω|) = |ω|/8.

For |ω| >> 8: -Ω² dominates. For |ω| ~ 1: comparable. ⚠️

BUT: this analysis doesn't use the bootstrap or R < 1. It uses
the SCALING of each contribution. The -Ω² contribution SCALES
as |ω|² while -H scales as |ω|² × (1/eigenvalue gap ~ 1/|ω|)
= |ω|. So -Ω² ALWAYS dominates at high |ω|.

WAIT: I made an error. The -H off-diagonal in the eigenbasis:
H_{ji} for j≠i (the off-diagonal of H in the strain eigenbasis).
This is bounded by ||H_dev||_F ≤ C||Δp||_∞ ≤ C|ω|².
The eigenvalue gap: |λ_i - λ_j| ≥ gap (positive for non-degenerate S).

The rotation rate: H_{ji}/(λ_i-λ_j).
If gap ~ |S| ~ |ω|/2: rate ~ |ω|²/(|ω|/2) = 2|ω|.
But -Ω² rate is |ω|²/4.

Ratio: (|ω|²/4)/(2|ω|) = |ω|/8 → ∞ as |ω| → ∞.

So: at HIGH |ω|: -Ω² dominates -H WITHOUT needing the bootstrap.
This is a SCALING argument, not a bootstrap argument!

VERDICT: **Step 8 can potentially be rescued using SCALING (|ω| → ∞)
instead of the broken bootstrap (Step 7). At high |ω|: -Ω² dominates
-H by factor |ω|/8 → ∞. DVar/Dt < 0 for large enough |ω|.** ✓*

*Conditional on |ω| being large enough. Near blowup: |ω| → ∞, so this holds.

---

## Step 9: DQ/Dt < 0 [file 283]

DEPENDS ON: Steps 5 + 8.

CLAIM: DQ/Dt = DVar/Dt - DH_ωω/Dt < 0 (since DVar < 0 and DH_ωω > 0).

REVIEW:
- DQ/Dt = D(Var)/Dt - D(H_ωω)/Dt: this is CORRECT by linearity.
  Q = Var - H_ωω → DQ/Dt = DVar/Dt - DH_ωω/Dt. ✓
- DVar/Dt < 0: from Step 8. CONDITIONALLY valid at high |ω|. ✓*
- DH_ωω/Dt > 0: from Step 5. **BROKEN** (Step 5 drops D|S|²/Dt).

Even if Step 5 is wrong: DQ/Dt < 0 could still hold if DVar/Dt
is SUFFICIENTLY negative to overcome a potentially positive -DH_ωω/Dt.

From data: DVar/Dt ≈ -200 while DH_ωω/Dt ≈ +100 (rough).
Net DQ/Dt ≈ -300. So DVar/Dt dominates even if DH_ωω/Dt < 0. ⚠️

But without a proof of DH_ωω/Dt > 0: DQ/Dt < 0 is NOT proven.
It could be that DH_ωω/Dt is VERY negative (pressure rapidly decreasing)
and DQ/Dt > 0.

VERDICT: **Step 9 BROKEN (depends on broken Step 5).** ⚠️

---

## Step 10: Q < 0 maintained (bootstrap) [file 248]

DEPENDS ON: Steps 9 + initialization.

CLAIM: Q < 0 at T₀, DQ/Dt < 0 when Q ≥ 0 → Q stays negative.

REVIEW:
- The logic: if Q(T₀) < 0 and DQ/Dt < 0 whenever Q ≥ 0: Q can't cross
  zero (it would need DQ/Dt > 0 at Q = 0, which is denied). ✓ (valid logic)
- Initialization Q(T₀) < 0: NOT PROVEN (measured, see Attack 1 in V_step7_10).
- DQ/Dt < 0 when Q ≥ 0: from Step 9. **BROKEN.**

VERDICT: **Step 10 BROKEN (depends on broken Step 9 and unproven initialization).** ✗
