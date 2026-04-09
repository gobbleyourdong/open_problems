---
source: THE REAL GAP — honest assessment of the bootstrap debate
type: ANALYSIS — where the proof stands after the 417/418 exchange
file: 419
date: 2026-03-30
---

## THE DEBATE

File 417_bootstrap_FAILS: "Tail grows as ||ω||∞^{3/2}, overwhelms head."
File 418_bootstrap_defense: "Seregin handles blowup; only finite ||ω||∞ matters."

## THE SUBTLE ISSUE (not addressed by either side)

The dichotomy (file 418) is:
- Case A: ||ω||∞ stays bounded → σ > 0 → tail small → barrier extends
- Case B: ||ω||∞ → ∞ → Type I → Seregin → impossible

Case B is correctly handled by Seregin.

Case A is where the subtlety lies. Under the barrier (α < ||ω||∞/2):
||ω||∞(t) ≤ ||ω||∞(0) exp(t/2) (exponential growth).

At time T: ||ω||∞(T) ≈ ||ω₀|| exp(T/2) — LARGE but finite.

The tail perturbation at ||ω||∞ = M (large, finite):
σ = cν/M → small.
tail_ℓ¹ ≤ ||ω||_{G^σ} × C/σ^{3/2} (Cauchy-Schwarz + Gevrey)
≈ ||ω||_{L²} × M^{3/2}/(cν)^{3/2}.

perturbation/|ω|² ≈ ||ω||_{L²} × M^{1/2}/(cν)^{3/2}.

For M large enough: this EXCEEDS 0.394 (the margin).

## THE QUESTION

Does the barrier break at some finite M_critical?

If ||ω||∞ reaches M_critical before the barrier breaks:
the barrier breaks at R = 1/2 → ||ω||∞ can grow FASTER.
If it grows super-Type-I: Seregin doesn't apply → possible blowup.

## BUT: does ||ω||∞ REACH M_critical?

Under the barrier: ||ω||∞ grows exponentially.
M_critical ∝ ((cν)^{3/2}/||ω||_{L²})^2 — could be VERY large.

For ν > 0 (NS, not Euler): the viscous dissipation BOUNDS the enstrophy:
d||ω||²/dt ≤ -2ν||∇ω||² + 2∫ωSω ≤ -2ν||∇ω||² + C||ω||∞||ω||²

Under the barrier (||ω||∞ ≤ M exp(t/2)):
d||ω||²/dt ≤ -2ν||∇ω||² + CM||ω||² exp(t/2)

The enstrophy DOES grow, but ||ω||_{G^σ} is controlled by the Gevrey ODE.

## THE FOIAS-TEMAM GEVREY ODE

d/dt ||ω||²_{G^σ} + ν||ω||²_{G^σ,1} ≤ |σ'| ||ω||²_{G^σ,1/2} + C/ν³ ||ω||⁶_{G^σ}

Choosing σ to keep ||ω||_{G^σ} bounded requires:
the RHS not to exceed the LHS dissipation (ν||ω||²_{G^σ,1}).

For our barrier: ||ω||∞ grows exponentially → σ shrinks exponentially.
The question: does ||ω||_{G^σ(t)} stay finite as σ → 0?

As σ → 0: ||ω||_{G^σ} → ||ω||_{L²} (FINITE, controlled by enstrophy).

So ||ω||_{G^σ} STAYS BOUNDED (approaching ||ω||_{L²}) as σ → 0!

## THIS CHANGES THE TAIL ESTIMATE

tail_ℓ¹ ≤ ||ω||_{G^σ} × (Σ exp(-2σ|k|))^{1/2}

||ω||_{G^σ} → ||ω||_{L²} ≤ C (bounded by enstrophy under barrier).

(Σ_{|k|>K} exp(-2σ|k|))^{1/2} ≈ C/σ^{3/2} = C × (M/(cν))^{3/2}.

tail_ℓ¹ ≤ C_L² × C × M^{3/2}/(cν)^{3/2}.

perturbation/|ω|² ≈ C_L² × M^{1/2}/(cν)^{3/2} → ∞ as M → ∞.

## VERDICT

The ||ω||_{G^σ} IS bounded (it approaches ||ω||_{L²}).
But the COMBINATORIAL factor C/σ^{3/2} still grows as M^{3/2}.
The perturbation/||ω||∞ grows as M^{1/2}.

For large enough M: the perturbation exceeds the 0.394 margin.

## THE TRUE REMAINING QUESTION

Does the enstrophy ||ω||_{L²}² stay bounded under the barrier?

If yes: ||ω||_{G^σ} ≤ √E stays bounded → M_critical depends on E.
If E grows: M_critical shrinks → barrier breaks sooner.

Under the barrier: dE/dt ≤ CE^{3/2} (standard supercritical).
E can blow up in finite time EVEN IF ||ω||∞ is bounded by the barrier.

WAIT: ||ω||∞ ≤ M exp(t/2) (bounded exponentially under the barrier).
And: dE/dt ≤ ||ω||∞ E ≤ M exp(t/2) × E.
This gives: E(t) ≤ E₀ exp(2M(exp(t/2)-1)). BOUNDED for each finite t!

So: E STAYS FINITE under the barrier for each finite time.
||ω||_{G^σ} ≤ √E stays finite.
BUT: E grows double-exponentially with t. And M_critical depends on E.

As t → ∞: E → ∞ → M_critical shrinks → eventually perturbation > 0.394.

This happens at t ~ log(M_critical) ~ log((cν)^3/E₀) — FINITE time.

At that time: the barrier breaks. Then ||ω||∞ can grow super-exponentially.

## HONEST CONCLUSION

The bootstrap debate is NOT settled. The tail perturbation grows with
||ω||∞ even for finite vorticity. At large enough ||ω||∞ (reachable
in finite time under the barrier): the perturbation exceeds the margin.

The proof is OPEN for general smooth fields.

## 419. The gap is genuine. Tail perturbation grows as ||ω||∞^{1/2}.
## Neither the bootstrap (411) nor the defense (418) is fully correct.
## The Key Lemma (all-N S²ê bound) remains the irreducible gap.
