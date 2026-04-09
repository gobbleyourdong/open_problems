---
source: BUARIA CLOSURE — near-field/far-field + Constantin estimate at the max
type: PROOF ATTEMPT — combines files 043 + 046 + 363
file: 425
date: 2026-03-30
---

## THE ARGUMENT

At x* = argmax|ω|, from the Buaria identity (exact, Biot-Savart):

α(x*) = (3/4π) PV ∫ [ê·(r̂ × ω(x*+r))][r̂·ê] / r³ dr

### Near-field (|r| < δ):

ω(x*+r) ≈ |ω(x*+r)| [ê + |r|∇ξ + O(|r|²)]

The twist: ê·(r̂ × ω) ≈ |ω(x*+r)| × |r| × |∇ξ| (since ê × ê = 0)

Near-field integral ≤ C₁ ||ω||∞ |∇ξ(x*)| × δ

### Far-field (|r| > δ):

|α_far| ≤ (3/4π) ∫_{|r|>δ} |ω(x*+r)| / r² dr ≤ C₂ ||ω||_{L¹} / δ

### Combined:

α(x*) ≤ C₁ ||ω||∞ |∇ξ| δ + C₂ M₁/δ

where M₁ = ||ω||_{L¹} ≤ ||ω₀||₁ + CE₀/ν (UNCONDITIONAL, file 046).

Optimizing over δ: α ≤ 2√(C₁C₂ M₁ ||ω||∞ |∇ξ|)

### For the barrier (α < ||ω||∞/2):

Need: 4C₁C₂ M₁ |∇ξ(x*)| < ||ω||∞²/4

i.e.: **|∇ξ(x*)| < ||ω||∞² / (16 C₁C₂ M₁)**

### Does this hold?

From Constantin's unconditional estimate (file 046):
∫₀ᵀ ∫ |ω| |∇ξ|² dx dt ≤ ||u₀||²/(2ν²) =: C₀

At x*: |ω(x*)| |∇ξ(x*)|² × Vol(blob) ≤ spatial integral ≤ C₀

where Vol(blob) is the volume where |ω| ≈ ||ω||∞.

So: |∇ξ(x*)|² ≤ C₀ / (||ω||∞ × Vol(blob))

For the barrier: need |∇ξ(x*)|² < ||ω||∞⁴ / (256 C₁²C₂² M₁²)

This requires: C₀/(||ω||∞ × Vol) < ||ω||∞⁴/C'

i.e.: Vol(blob) > C₀ × C' / ||ω||∞⁵

### Two regimes:

**Broad peak** (Vol(blob) > V₀):
|∇ξ| is small (smooth field) → barrier holds from near-field bound.
Effectively ≤ 4 modes active → per-mode bound (PROVEN, file 363).

**Sharp peak** (Vol(blob) < V₀):
Many modes active (N_eff ~ 1/Vol^{1/3}).
But: |∇ξ| is also large (steep gradients) → near-field integral larger.
The balance: the near-field/far-field splitting shows α ≤ C√(|ω||∇ξ|).
From Constantin: |∇ξ| ≤ C₀^{1/2}/(|ω|^{1/2} Vol^{1/2}).
So: α ≤ C × C₀^{1/4} × |ω|^{1/4} / Vol^{1/4}.

For Vol = (ν/|ω|)^{3/2} (Kolmogorov scale):
α ≤ C × C₀^{1/4} × |ω|^{1/4} × (|ω|/ν)^{3/8} = C'|ω|^{5/8}/ν^{3/8}

For α < |ω|/2: need |ω|^{5/8}/ν^{3/8} < |ω|/(2C')
i.e.: |ω|^{3/8} > 2C'/ν^{3/8} → |ω| > (2C')^{8/3}/ν

For |ω| above this threshold: barrier HOLDS.
For |ω| below this threshold: BOUNDED.
Either way: NO BLOWUP. ∎

## THE GAP

The argument uses Vol(blob) from the Hessian of |ω|² at x*.
The Kolmogorov-scale estimate Vol ~ (ν/|ω|)^{3/2} is HEURISTIC.

Proving Vol(blob) ~ (ν/|ω|)^{3/2} requires showing the vorticity
peak has width ~ √(ν/|ω|) — the Kolmogorov scale.

This is related to Grujic's sparseness: if the super-level set
{|ω| > ||ω||∞/2} is "sparse" at scale (ν/||ω||∞)^{1/2}:
the volume estimate holds.

## CONNECTION TO GRUJIC

Grujic (2001, 2012): sparseness → regularity.
Our argument: Vol(blob) > C/||ω||⁵ → regularity (via barrier).

The sparseness condition IS Vol(blob) < C δ³ (thin in one direction).
Our condition IS Vol(blob) > C/||ω||⁵ (not too thin).

These are COMPLEMENTARY: Grujic needs thinness, we need non-vanishing.
BOTH are needed for the argument to close at all scales.

## STATUS

The argument has the right STRUCTURE but needs the blob volume
estimate to be rigorous. The volume depends on:
1. The Hessian eigenvalues of |ω|² at x* (curvature of the peak)
2. The viscous balance at the Kolmogorov scale
3. Grujic's sparseness condition

If Vol(blob) can be controlled from below by ν^{3/2}/||ω||∞^{3/2}
(the Kolmogorov cube): the argument closes.

## 425. Near-field/far-field + Constantin → α < |ω|/2 if blob volume bounded.
## The blob volume = Kolmogorov cube is the missing quantification.
## Connects to Grujic sparseness. Could close with parabolic regularity.
