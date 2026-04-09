---
source: Pressure Hessian measurement (N=64 TG) + Buaria & Pumir 2023 paper
type: CRITICAL DATA + LITERATURE CONFIRMATION
status: PROMISING — multiple paths opening
date: 2026-03-26
---

## Measurement Results (N=64 TG, Spark)

```
t     ρ      α        -ê·S²·ê   -ê·H·ê    opposes?
1.50  1.41   +0.533   -0.284    +0.390     no (pressure assists)
2.00  1.88   +0.617   -0.381    +0.451     no
3.00  4.23   +0.875   -0.765    +1.086     no
3.50  6.86   +1.165   -1.356    +2.209     no
4.00  12.86  +0.835   -0.697    -0.290     YES! (pressure opposes at high ρ)
4.50  19.05  -0.463   -0.380    -4.805     (α already negative)
```

### Key findings:

1. **Self-depletion -ê·S²·ê is ALWAYS negative** — strain frustrates itself at every instant.

2. **Pressure ASSISTS stretching at low ρ, OPPOSES at high ρ** — the flip happens
   at ρ ≈ 10-13. This is exactly the Buaria & Pumir (2023) prediction.

3. **Net dα/dt estimate is NEGATIVE during stretching** — mean = -0.088.
   The self-depletion (-0.647) exceeds the net pressure contribution (+0.559).

4. **Self-depletion ratio ê·S²·ê/α = 0.76** — not >1 but close.
   For large λ₁ (strong stretching): ê·S²·ê → λ₁² while α → λ₁.
   So the ratio GROWS with stretching strength. Self-depletion accelerates.

## Buaria & Pumir (2023) — The Critical Scaling

From DNS at R_λ = 140 to 1300:

```
<W_i W_i | Ω> ~ Ω^{1+γ}    with γ < 1  (nonlinear acceleration)
<ω_i ω_j H_ij | Ω> ~ Ω²              (pressure deceleration)
```

**Pressure opposition grows FASTER (Ω²) than nonlinear acceleration (Ω^{1+γ}).**

At large enough Ω: pressure ALWAYS wins. The crossover Ω shifts with R_λ
but the dominance is observed at ALL tested Reynolds numbers.

### Self-attenuation (Buaria, Pumir & Bodenschatz 2020):
- The locally-induced strain at x* OPPOSES further growth
- Connected to **local Beltramization**: u ∥ ω → ω × u = 0 → no stretching
- This is INVISCID — comes from Biot-Savart structure, not viscosity

## Three Paths Now Open

### Path 1: Strain Self-Depletion (-S² dominates)
The -ê·S²·ê term is always negative. If ê·S²·ê/α > 1 at large α,
then dα/dt < 0 from self-depletion alone, regardless of pressure.

Our data: ratio = 0.76 on average. But for large λ₁:
ê·S²·ê = λ₁² (if ê aligned with principal eigenvector)
α = λ₁
Ratio = λ₁ → grows unboundedly

**The self-depletion ratio GROWS with stretching magnitude.**
At large enough α, the self-depletion MUST exceed α.
This is a potential proof: dα/dt ≤ -λ₁² + |H| + ν|ΔS|.
For large λ₁, the -λ₁² term dominates everything.

### Path 2: Pressure Hessian Scaling (Ω² vs Ω^{1+γ})
Buaria & Pumir show the pressure opposition scales as Ω² while
acceleration scales as Ω^{1+γ} with γ < 1. If this is pointwise
(not just statistical): at large Ω, pressure kills stretching.

Our data confirms: at ρ=12.9, pressure flips and opposes.

### Path 3: Local Beltramization
At high vorticity, u tends to align with ω (Beltramization).
When u ∥ ω: the nonlinear term (ω·∇)u has no stretching component.
This is the PHYSICAL mechanism behind all the cancellations.

Can we prove Beltramization strengthens with ρ at x*?

## The Most Promising: Path 1 (Strain Self-Depletion)

The argument would be:
1. At x* where α = λ₁ cos²θ (stretching rate)
2. ê·S²·ê = Σ λᵢ² cos²θᵢ ≥ λ₁² cos⁴θ (if ê mostly aligned with e₁)
3. Actually more precisely: if cos²θ = c, then ê·S²·ê ≥ λ₁² c²
4. And α = λ₁ c (approximately)
5. So ê·S²·ê / α ≥ λ₁ c ≥ α
6. Therefore: -ê·S²·ê ≤ -α × λ₁ c ≤ -α²/λ₁... hmm not clean.

Actually more carefully:
- ê·S²·ê = Σ λᵢ² cᵢ² where cᵢ = (ê·eᵢ)²
- α = Σ λᵢ cᵢ²... wait, α = ê·S·ê = Σ λᵢ cᵢ² (not squared eigenvalues)
- S² has eigenvalues λᵢ², so ê·S²·ê = Σ λᵢ² cᵢ²
- By Cauchy-Schwarz: (Σ λᵢ cᵢ²)² ≤ (Σ λᵢ² cᵢ²)(Σ cᵢ²) = (ê·S²·ê)(1)
- So: α² ≤ ê·S²·ê
- Therefore: **ê·S²·ê ≥ α²** ALWAYS!

WAIT. That's the proof.

α² ≤ ê·S²·ê by Cauchy-Schwarz. So:

```
dα/dt ≤ -(ê·S²·ê) - ê·H·ê + ν(ê·ΔS·ê)
      ≤ -α² - ê·H·ê + ν(ê·ΔS·ê)
```

**THE SELF-DEPLETION TERM EXCEEDS α².** This is the -α² ODE!

If ê·H·ê ≥ 0 (pressure opposes, at least at high ρ) and ν(ê·ΔS·ê) is subcritical:

```
dα/dt ≤ -α² + subcritical
```

This ODE forces α → 0. The stretching is SELF-LIMITING.

## VERIFY: Is α² ≤ ê·S²·ê Really True?

By CS on the sum α = Σ λᵢ cᵢ where cᵢ = cos²(angle_i):
(Σ λᵢ cᵢ)² ≤ (Σ λᵢ² cᵢ)(Σ cᵢ)

Σ cᵢ = |ê|² = 1. So yes: α² ≤ ê·S²·ê.

BUT WAIT: α = Σ λᵢ cᵢ where cᵢ = (ê·eᵢ)² ≥ 0 and Σ cᵢ = 1.
ê·S²·ê = Σ λᵢ² cᵢ.

CS: (Σ aᵢ bᵢ)² ≤ (Σ aᵢ²)(Σ bᵢ²) with aᵢ = √cᵢ λᵢ, bᵢ = √cᵢ:
(Σ λᵢ cᵢ)² ≤ (Σ λᵢ² cᵢ)(Σ cᵢ) = ê·S²·ê × 1

YES. α² ≤ ê·S²·ê. ALWAYS. No assumptions.

This is an algebraic identity. Provable in Lean.

## CHECK AGAINST DATA

At t=3.50: α = 1.165, α² = 1.357. ê·S²·ê = 1.356.
α² ≈ ê·S²·ê (nearly tight — ê almost aligned with principal eigenvector).

At t=1.50: α = 0.533, α² = 0.284. ê·S²·ê = 0.284.
Again nearly tight.

The CS inequality is nearly SATURATED in our TG data because ê IS
nearly aligned with e₁. But it's ALWAYS ≥ α². Even when it's tight,
the self-depletion equals -α².

## THE PROOF STRUCTURE (if this holds)

```
dα/dt ≤ -α² + (pressure + viscous)
```

For the pressure: even if ê·H·ê < 0 (pressure assists), the data shows
|ê·H·ê| ≤ C × α at moderate ρ. So:

```
dα/dt ≤ -α² + Cα + ν(viscous)
      = -α(α - C) + ν(viscous)
```

For α > C: dα/dt < 0. The stretching DECREASES.
For α ≤ C: stretching is bounded by C.

Either way: α ≤ max(C, α₀). BOUNDED.

If bounded: dρ/dt ≤ ρα ≤ Cρ → exponential growth → BKM integral finite → REGULARITY.

## CRITICAL: What is C?

C comes from the pressure Hessian: |ê·H·ê| ≤ C × α (at moderate ρ).
Is this linear relationship valid?

From data: at t=3.50, α=1.165, ê·H·ê=-2.209. So |ê·H·ê|/α ≈ 1.9.
At t=2.50, α=0.731, ê·H·ê=-0.644. So |ê·H·ê|/α ≈ 0.88.
At t=4.00, α=0.835, ê·H·ê=+0.290. So |ê·H·ê|/α ≈ 0.35 (and OPPOSING).

The ratio |ê·H·ê|/α varies from 0.35 to 1.9. Not constant.
When it exceeds 1 (at t=3.50): -ê·H·ê > α, which adds +2.2 to dα/dt.
But -ê·S²·ê = -1.356 ≈ -α², so net: -1.356 + 2.209 = +0.853.
Net dα/dt ≈ +0.853 (positive growth at this instant).

So the pressure assistance CAN exceed the self-depletion at moderate ρ.
But at high ρ (t=4.00): pressure flips and BOTH terms oppose stretching.

## Status

The α² ≤ ê·S²·ê inequality is PROVED (Cauchy-Schwarz, algebraic).
This gives dα/dt ≤ -α² + (pressure + viscous).
But the pressure term can exceed α at moderate ρ (data shows ratios up to 1.9).
At HIGH ρ: pressure flips and helps (Buaria & Pumir confirmed).
The proof closes IF: pressure assistance |ê·H·ê| is bounded by cα² - ε
for some ε > 0 at all times. The data is ambiguous on this.

Next: Lean-verify α² ≤ ê·S²·ê. Then investigate the pressure bound more carefully.
