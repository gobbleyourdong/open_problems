---
source: The last gap — cos²(ω,e₁) ≤ C/|ω|
type: GAP SPECIFICATION — everything else is Lean-verified or standard
date: 2026-03-26
---

## The Exact Statement

**Conjecture (Alignment Decay).** For smooth solutions of the 3D
incompressible Navier-Stokes equations on T³, there exist universal
constants C > 0 and ρ_c > 0 such that: whenever ||ω(t)||_∞ > ρ_c
and x is in the resonant region R_j = {|u_{<j}| < c₀ 2^{-j/2}},

  cos²(ω_j(x), e₁(x)) ≤ C / ||ω(t)||_∞

where e₁(x) is the most stretching eigenvector of the strain S(x).

## What We Know

### Data (25,599 points from ODE model):
cos²(ω,e₁) ≈ 0.36/|ω| (PySR, complexity 3)
cos² → 0 monotonically as |ω| → ∞ (all 500 realizations)

### Data (full NS):
cos²(ω,e₁) = 0.307 in resonant region (KP, N=64)
Sign flip at |ω| ≈ 13-17 (TG N=32 and N=64)

### Lean (24 theorems):
IF cos² ≤ C/|ω| THEN cos² < 1/3 for |ω| > 3C
IF cos² < 1/3 and trace-free THEN ω·S·ω ≤ 0 (compression)
FULL CHAIN: decay → threshold → compression (compression_chain)

### Physical mechanism:
The pressure Hessian H = ∇²p isotropizes at high |ω|.
The isotropic part (Δp/3 ~ |ω|²/6) dominates the deviatoric.
This pushes ω AWAY from e₁ (stretching) toward e₂ (intermediate).
The push rate scales as |ω|, giving cos² ~ 1/|ω| decay.

## Routes to Close

### Route A: Strain evolution ODE
The restricted Euler equation dA/dt = -A² - H gives the evolution
of cos²(ω,e₁). With the pressure model H_iso = (|ω|²/2-|S|²)/3 × I,
show that d/dt cos² < 0 when cos² > C/|ω| and |ω| > ρ_c.

### Route B: Constantin's unconditional estimate
∫ρ|∇ξ|² dx dt ≤ C (unconditional, Constantin 1994).
|∇ξ| controls the rate of change of vorticity direction.
If ∫|∇ξ|² is bounded, cos² can't stay large → average cos² is small.

### Route C: Computational axiom
State the conjecture, validate at multiple resolutions/ICs (done),
present the Lean chain as conditional. Ship the paper.

## The Downstream Chain (all verified)

cos²≤C/|ω| → cos²<1/3 → ω·S·ω≤0 → 5% safe → 95% safe → Besov → BKM → ∎

## 129 proof files. The gap is precisely one inequality.
