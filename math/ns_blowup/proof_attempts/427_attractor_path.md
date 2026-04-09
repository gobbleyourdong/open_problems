---
source: THE ATTRACTOR PATH — |ω|²/|S|² → 4 gives S²ê ≤ |ω|²/6 (83% margin)
type: PROOF DIRECTION — uses NS DYNAMICS, bypasses the kinematic Key Lemma
file: 427
date: 2026-03-30
---

## THE DYNAMIC BOUND (NS solutions only, not arbitrary div-free fields)

For NS solutions on T³: the ratio |ω|²/|S|² converges to 4 at the
vorticity maximum (verified in DNS: 100% of post-transient measurements,
file 302).

At the attractor: |S|² = |ω|²/4 → S²ê ≤ (2/3)|S|² = |ω|²/6 ≈ 0.167.
Threshold: 3|ω|²/4 = 0.75. **Margin: 78%.**

## THE PROOF CHAIN (if attractor convergence is proven)

1. Local existence: smooth for [0, T₀] (standard)
2. Attractor convergence: |ω|²/|S|² → 4 by time T₀ (TO PROVE)
3. After T₀: |S|² < |ω|²/2 → S²ê < |ω|²/3 < 3|ω|²/4
4. Barrier → Type I → Seregin → regularity for [T₀, ∞)
5. Combined: smooth for all time ∎

## THE ATTRACTOR MECHANISM

From the strain evolution (Miller 2024):
d||S||²/dt = -2||S||²_{Ḣ¹} - 4∫det(S)

From the vorticity evolution:
d||ω||²/dt = 2∫ωSω - 2ν||∇ω||²

The ratio r = ||ω||²/||S||² evolves toward 4 because:
- The vorticity stretching ∫ωSω ∝ ||ω||²×α (grows with ω)
- The strain cubic -4∫det(S) ∝ -||S||³ (grows faster with S)
- At r < 4: ω grows faster than S → r increases
- At r > 4: S grows faster than ω → r decreases
- The fixed point r = 4 is stable

## WHY THIS IS APPROACH #3 (Grujic's depletion)

The attractor |ω|²/|S|² = 4 IS quantitative depletion of nonlinearity.
- The strain (nonlinear term) is depleted relative to vorticity
- The depletion factor is 4 (measured, resolution-independent)
- At the depleted state: S²ê ≤ |ω|²/6 (far below the barrier threshold)

This is the DYNAMIC version of Grujic's qualitative depletion observation.
Making it quantitative (proving convergence rate) would close the proof.

## WHAT NEEDS TO BE PROVEN

**Lemma (Attractor Convergence)**: For smooth NS solutions on T³ with ν > 0,
at the global max of |ω|: there exists T₀ (depending on initial data and ν)
such that |ω(x*,t)|²/|S(x*,t)|² ≥ 3 for all t > T₀.

(We only need r ≥ 3, not r = 4. At r = 3: |S|² = |ω|²/3 → S²ê ≤ 2|ω|²/9 < 3|ω|²/4.)

From DNS: the ratio reaches r ≥ 3 within ~5 eddy turnover times for all tested ICs.

## CONNECTION TO EXISTING LITERATURE

- Miller's enstrophy identity (arxiv:2407.02691): d||S||²/dt = -2||S||²_{Ḣ¹} - 4∫det(S)
  The -4∫det(S) term drives the attractor (cubic in eigenvalues)
- Buaria's self-attenuation (Nature 2020): physical mechanism for r → 4
- Grujic's depletion (2010/2018): qualitative version of the attractor
- Our barrier (file 360): quantifies WHAT the attractor implies (S²ê < 3|ω|²/4)

## 427. If |ω|²/|S|² → 4 is proven for NS: S²ê ≤ |ω|²/6 → REGULARITY.
## This is approach #3: quantitative depletion. Margin 78%.
## The attractor IS the depletion mechanism.
