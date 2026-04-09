---
source: THE ARGUMENT — blowup forces coherence forces depletion
type: PROOF STRUCTURE — the complete chain
file: 833
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE COMPLETE ARGUMENT FOR NS REGULARITY ON T³

### STEP 1: Blowup forces N_eff → ∞
Galerkin truncation with viscosity on T³ is globally regular.
Therefore: if blowup occurs, the effective mode count N_eff → ∞.
**STATUS: PROVEN** (Leray-Temam, classical).

### STEP 2: Blowup forces coherence (D ≫ N)
If blowup occurs: ||ω||∞ → ∞.
The energy is bounded: ||u||² ≤ ||u₀||².
For N_eff active modes with amplitudes a_j: Σa_j² ≤ ||u₀||².
|ω|² = |Σ s_j a_j ω̂_j|² where ω̂_j = k_j × p_j / |k_j × p_j|.
By Cauchy-Schwarz: |ω|² ≤ (Σa_j²)(Σ|k_j|²) = E₀ · Σ|k_j|².

BUT: this gives |ω| ≤ √(E₀ · Σ|k|²), which grows as √(NK²).
For |ω| → ∞ with K bounded: need N → ∞ AND |ω|² ~ NK².
This means D = (|ω|² - Σ|k_j|²a_j²)/2 ≈ |ω|²/2.

ACTUALLY: |ω|² = Σ|ω_j|² + 2D = Σ a_j²|k_j|² + 2D.
For D = 0 (incoherent): |ω|² = Σa_j²|k_j|² ≤ K² · E₀.
So ||ω||∞ ≤ K√E₀ (BOUNDED for fixed K).

For ||ω||∞ → ∞: EITHER K → ∞ OR D ≫ Σa_j²|k_j|².

Case K → ∞ (energy cascades to high k):
N_eff grows with K. The modes at scale K have |k| ~ K.
Even with D = 0: ||ω|| ~ K√E₀. For K → ∞: ||ω|| → ∞.
But then: |S|²/|ω|² = (Σa_j²|k_j|²/2 + (K+T))/(Σa_j²|k_j|² + 2D).
With D = 0: |S|²/|ω|² = 1/2 + (K+T)/Σa_j²|k_j|².
(K+T) has mean 0. So |S|²/|ω|² ≈ 1/2.
α/|ω| ≈ √(1/3) ≈ 0.577. BOUNDED, not → 0.
**But from the SOS data: c(N) < 0.577 for N ≥ 4!**
**So even this case gives c(N) < 1 (the Key Lemma), which combined**
**with the Gevrey trick...**

Wait: c = 0.577 is constant, not → 0. The Gevrey trick needs c → 0.

Case K → ∞ with D = 0: α/|ω| ≈ 0.577 for ALL N. Doesn't → 0.
The Gevrey trick doesn't help because c stays at 0.577.

**THIS IS THE HOLE.** For modes at high K with D = 0 (incoherent):
the ratio α/|ω| stays at √(1/3) regardless of N.
The Key Lemma gives α/|ω| < 3/4, which is tighter but still constant.

### THE RESOLUTION

For D = 0 (incoherent modes): ||ω||∞ ≤ K√E₀.
The blowup rate: d/dt||ω|| ≤ (3/4)||ω||² ≤ (3/4)K²E₀.
But K grows because the cascade activates higher modes.
The cascade rate: dK/dt ~ ||ω||² / K (enstrophy transfer).
dK/dt ~ K²E₀/K = KE₀. So K grows exponentially: K ~ e^{E₀t}.
||ω|| ~ K√E₀ ~ √E₀ e^{E₀t}. EXPONENTIAL growth, NOT finite-time blowup!

For FINITE-TIME blowup: need SUPER-EXPONENTIAL growth.
d/dt||ω|| ≥ ε||ω||² (for some ε > 0) → 1/||ω|| decreasing linearly → blowup.
||ω||² ≥ (d/dt||ω||)/ε. If d/dt||ω|| ~ ||ω||²: blowup.
If d/dt||ω|| ~ ||ω|| (exponential): NO finite-time blowup.

So: incoherent modes give EXPONENTIAL growth at most. NOT blowup.

For finite-time blowup: need SUPER-EXPONENTIAL growth → need α·|ω| ≥ ε||ω||²
→ α ≥ ε||ω|| → α/|ω| ≥ ε > 0.

BUT: this is just the stretching being proportional to ||ω||².
For the Riccati y' = εy²: blowup iff ε > 0.

The question: can α/|ω| ≥ ε > 0 be maintained near blowup?
From the SOS data: for N ≥ 5, c(N) = 0.30. For N ≥ 7, c(N) = 0.21.
As N_eff → ∞ (which blowup forces): c(N_eff) → ???

If c(N_eff) → ε > 0 (stays bounded away from 0): blowup IS possible.
If c(N_eff) → 0: blowup is IMPOSSIBLE (growth subquadratic).

**The gap: does c(N) → 0 or does it plateau at some c_∞ > 0?**

### THE DIMENSION ARGUMENT (REVISITED)

From the three identities: the AVERAGE |S|²/|ω|² = 1/2 (from equal splitting).
For the WORST CASE at the ARGMAX:
|S|² = Σa_j²|k_j|²/2 + (K+T)  where E[(K+T)] = 0 (uncorrelation).
|ω|² = Σa_j²|k_j|² + 2D.
|S|²/|ω|² = (Σa²k²/2 + (K+T)) / (Σa²k² + 2D).

For D = 0: ratio = 1/2 + (K+T)/Σa²k². Fluctuations of (K+T) are O(√N·σ²).
Ratio = 1/2 ± O(1/√N) (by CLT if entries are independent-ish).

THIS GIVES: c(N) → √(1/3) ≈ 0.577 for D=0 (constant, not → 0).
But the SOS data shows c(N) < 0.577 for N ≥ 4 (0.54, 0.30, 0.26, 0.21).
The SOS tests include configs with D > 0 (not just D=0).

For the WORST config tested by SOS: D ≈ 0 (as incoherent as possible).
Yet c(N) still decreases! The SOS data at D≈0 gives c(7) = 0.21.

How is this possible if the ratio → 1/2 for D=0?
Because the SOS tests ALL VERTICES, including those where |ω|² is large
(D > 0 at those vertices). The MINIMUM c(N) occurs at the argmax vertex,
where D is MAXIMIZED. At the argmax: D > 0 → |ω|²>Σk² → ratio < 1/2.

So the SOS c(N) values ARE at the argmax (D > 0), not at D=0 vertices.
And at the argmax: D increases with N (more modes → more constructive
interference at the max). So the ratio DOES → 0 at the argmax.

The ADVERSARIAL config that keeps c(N) large would have D≈0 at the argmax.
But with N ≥ 4 modes on Z³: the R³ dimension argument forces D > 0.
The amount by which D > 0 determines c(N).

### THE PRECISE QUESTION (AGAIN)

For N modes at the argmax: D = (|ω|² - Σa²|k|²)/2 > 0.
Does D/Σa²|k|² → ∞ as N → ∞?

If YES: |S|²/|ω|² → 0 → c → 0 → no blowup.
If NO: c stays bounded above 0 → blowup possible.

For ADVERSARIAL configs: D can be O(1) (barely > 0).
Then D/Σa²|k|² ~ 1/N → 0. WRONG DIRECTION.

THE HONEST CONCLUSION: c(N) → 0 at the argmax requires D to grow
with N, which the adversary can prevent by choosing near-orthogonal modes.
The SOS data shows c(N) → 0 for the tested configs, but the adversary
has more freedom for larger N.

HOWEVER: the SOS certificates test ALL configs within their shell range.
For N=7, K²≤3: ALL 1716 configs give c(7) ≤ 0.21. This includes the
most adversarial configs on the lattice with K²≤3.

For larger K: the adversary has more freedom (more k-vectors available).
But the modes at larger K have larger |k|², so Σ|k|² grows.
The vorticity coherence D also has more room to grow.
The NET effect on c(N) is what the SOS data captures.

## 833. The argument: blowup → N_eff → ∞ → c(N) → 0 → no blowup.
## The gap: prove c(N) → 0 for all N (not just N=3-7).
## For D=0 (adversarial): c ≈ √(1/3) (constant). But argmax forces D > 0.
## The SOS data with K²≤3 shows c → 0 through N=7. Need ALL N.
## Amplitude invariance + Gevrey trick: ANY c → 0 suffices.
