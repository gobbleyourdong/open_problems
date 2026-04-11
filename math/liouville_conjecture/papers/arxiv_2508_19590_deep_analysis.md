# arxiv 2508.19590 — Deep Technical Analysis of the Sparse Log-Weight Technique

> Author: Myong-Hwan Ri (DPRK Academy of Sciences, August 2025)
> Purpose: analyzing whether the X₁ norm technique applies to our Liouville campaign

## The X₁ Norm Construction

The weight a(j) on Littlewood-Paley block j:
- a(j) = 1 for j ≤ 0 and most j > 0
- a(j) = log₂(j) ONLY at doubly-exponential positions j ≈ 2^{2^k}
- The set of weighted positions is INCREDIBLY sparse

X₁ norm: ||v||_{X₁} = ||{2^{j/2} a⁻¹(j) ||Δⱼv||₂}||_{ℓ²}

This is H^{1/2} with inverse-log weights at sparse frequencies. Since a(j) ≥ 1,
X₁ is WEAKER than H^{1/2} (H^{1/2} ↪ X₁). "Barely supercritical."

## The Rescaling Trick (the clever part)

For λ = 2^{2^l}: rescaling v → λv(λ·) shifts Fourier support by 2^{2^l} positions.
The doubly-exponential spacing means this shift MISALIGNS almost every weighted
frequency with the sparse weight positions. The ratio a(j)/a(j + 2^{2^l}) → 0
as l → ∞.

Result: ||v_λ||_{X₁} → 0 as λ → ∞, while ||v_λ||_{H^{1/2}} stays fixed.

This makes the Gronwall coefficient small, closing the energy estimate.

## Why We CANNOT Use X₁ for Liouville

Three fatal incompatibilities:

1. **Ancient solutions on R³ are NOT in H^{1/2}(R³).** They're bounded (L^∞) but
   the H^{1/2} norm may be infinite. X₁ requires H^{1/2} finiteness.

2. **The rescaling trick needs a "zoom out."** It makes X₁ small by zooming out
   (λ → ∞). Ancient solutions already live on all of R³ — no compact domain
   to zoom out from.

3. **No initial time.** Ri's argument works forward from t=0 with energy inequality.
   Ancient solutions have no initial time — they extend to -∞.

## What We CAN Steal (the philosophy)

The idea: weaken a critical norm by sparse log weights, then use structural
properties (rescaling, sparsity) to make the weakened norm small.

**Speculative application to Liouville:**
- Define a "barely supercritical L³" norm on R³ (L³ is critical for NS)
- Show the Leray profile φ (from Type II blowup rescaling) satisfies this norm
- The drift term (1/2)y·∇φ in the Leray equation might force the profile's
  contribution at sparse frequencies to decay
- If φ ∈ weakened-L³, the Albritton-Barker argument might close

This is speculative but it's a CONCRETE LEAD for the next Liouville session.

## Assessment of the Paper Itself

The paper is NOT definitively wrong in any obvious step. The most likely failure:
- The summation (3.12)-(3.13) requires Σb(j₀(2k)) ≤ 3n for large n
- This relies on delicate combinatorial counting of the sparse set S(n)
- The Bernstein estimates on page 11 use ||u_k||_∞ ≤ C·b(j₀(k))·k·||u||_{X₁}
  which grows linearly in k — the sum converges only if b is controlled

The X₁ construction is genuinely clever. The paper deserves careful peer review
rather than dismissal. But it claims a millennium prize in 17 pages from a single
author — extreme skepticism is warranted.

## Action Items for Next Liouville Session

1. Define a "barely supercritical L³" analog of X₁ for the Leray profile
2. Check whether the drift (1/2)y·∇φ interacts with sparse frequency weights
3. If the Leray profile satisfies weakened-L³, test whether Albritton-Barker closes
4. This would be attempt_011 — a new route inspired by external literature
