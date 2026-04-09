---
source: DEFINITIVE ROADMAP — exactly what's needed to close the proof
type: ROADMAP — concrete steps for the next session
file: 393
date: 2026-03-29
---

## THE PROOF CHAIN (complete except one step)

1. d||ω||∞/dt ≤ α||ω||∞ at the global max (PROVEN)
2. Barrier at R = 1/2: need S²ê < 3|ω|²/4 (PROVEN → regularity via Seregin)
3. Trace-free: S²ê ≤ (2/3)|S|² = (2/3)(|∇u|²-|ω|²/2) (PROVEN, from div u = 0)
4. Need: |∇u|²/|ω|² < 13/8 at the global max (EQUIVALENT to step 2)
5. Regression: R ≤ 1 + 2(max(L) + c×Y_max)/(N+2Y_max) where c < 0 (PROVEN)
6. **Need: max(L)/Y_max ≤ C < 5/4 + |c| ≈ 1.75** (THE ONE REMAINING STEP)

## WHAT WE KNOW ABOUT max(L)/Y_max

### Numerically (6000+ trials, N=5-9):
worst max(L)/Y_max = 0.92 (at N=5). Threshold = 1.75. Margin 52%.

### Asymptotically (CLT for Rademacher chaos):
max(L)/Y_max → σ_L/σ_Y ≈ 0.39 as N → ∞.

### The quantities:
- σ_L/σ_Y = (σ_X/σ_Y)√(1-ρ²) ≈ 0.63 × 0.62 ≈ 0.39 (STABLE across N)
- r_eff(M_L) ≈ 2 (BOUNDED, not growing with N)
- Both max(L) and Y_max scale as σ × √(2N ln2) for large N

## THE THREE APPROACHES TO PROVE STEP 6

### Approach A: Hypercontractivity for Rademacher chaos

For degree-2 polynomial Q(s) = s^T M s on {±1}^N:
max Q ≤ E[Q] + C_hyp × σ_Q × √(log(1/δ))   (for P(Q > max) < δ)

With δ = 2^{-N} (probability of the max):
max Q ≤ C_hyp × σ_Q × √(N ln 2)

The hypercontractivity constant for degree-2 chaos: C_hyp = (p-1) for
||Q||_p ≤ (p-1)||Q||_2. With p = log(2^N): C_hyp = N ln 2 - 1.

This gives max Q ≤ (N ln2) × σ_Q. TOO LOOSE (linear in N, not √N).

But: for LOW EFFECTIVE RANK (r_eff ≈ 2): the hypercontractivity constant
is √(r_eff), not N. This requires the KERNEL-SPECIFIC hypercontractivity.

**Read**: Latała's result on moments of chaos in Banach spaces.
**Key paper**: Latała, "Estimates of moments and tails of Gaussian chaoses" (2006).
The tail bound for low-rank chaos: max ~ √(r_eff × N) × ||M||_op.

### Approach B: Direct SDP certification

Formulate: max_{s ∈ {±1}^N} L(s)/Y_max(s) as a ratio optimization.

This can be relaxed to an SDP: max Tr(M_L X)/Tr(M_Y X) subject to
X ≽ 0, X_{ii} = 1.

Solve the SDP numerically with certified solver (DSDP, MOSEK) for
ALL mode configurations in the K-shell.

This is the computer-assisted route. Feasibility: for K=√2 (9 modes),
the SDP has dimension 9×9. Very small — certifiable in milliseconds.

### Approach C: Kernel-specific bound via Biot-Savart structure

Prove: r_eff(M_L) ≤ 3 (from the 3D Biot-Savart structure).

Then: max(L) ≤ √(3N) × ||M_L||_op (from the rank-constrained max).

And: Y_max ≥ √N × ||M_Y||_op / K_G (from Grothendieck lower bound).

Ratio: max(L)/Y_max ≤ K_G × √3 × ||M_L||_op / ||M_Y||_op.

If ||M_L||_op / ||M_Y||_op = σ_L/(σ_Y × √(r_L/r_Y)): bounded by the
ratio of Frobenius norms adjusted for rank.

With σ_L/σ_Y ≈ 0.39 and K_G ≈ 1.78 and √3 ≈ 1.73:
ratio ≤ 1.78 × 1.73 × 0.39 × (correction) ≈ 1.20 × correction.

If the correction is ≤ 1.46: ratio ≤ 1.75. CLOSES!

## RECOMMENDED READING

1. **Rudelson-Vershynin**: arxiv 1306.2872 — Hanson-Wright sharp constants
2. **Latała (2006)**: "Estimates of moments and tails of Gaussian chaoses" —
   low-rank tail bounds that transfer to Rademacher chaos
3. **Adamczak-Latała-Litvak-Pajor-Tomczak-Jaegermann (2014)**: arxiv 1309.7083 —
   Hanson-Wright for matrices with structure
4. **Pisier**: arxiv 1101.4195 — Grothendieck survey, kernel-specific bounds

## CONCRETE NEXT STEPS

1. Read Latała's paper on low-rank chaos tails — if the bound is
   max ~ √(r_eff × N) × ||M||_op with small constant: proof closes
2. Compute the SDP for the K=√2 shell as a backup (certified bound)
3. Prove r_eff(M_L) ≤ 3 from the Biot-Savart geometry (key lemma)
4. If constant too large: try kernel-specific tightening using the
   algebraic structure Δ = -(1-κ²)D - κAB

## 393. The proof reduces to: bound max(L)/Y_max ≤ 1.75 universally.
## Three approaches: hypercontractivity (read Latała), SDP, kernel-specific.
## The margin is 52% (numerically). The asymptotic is 0.39/1.75 = 22% of threshold.
