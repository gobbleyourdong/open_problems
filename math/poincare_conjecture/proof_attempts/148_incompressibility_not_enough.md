---
source: Incompressibility alone does NOT give c₂ ≈ c₃
type: NEGATIVE RESULT — the symmetry requires the full PDE
date: 2026-03-28
---

## Test: Does trace-free alone produce c₂ ≈ c₃?

### Restricted Euler (no pressure, just dA/dt = -A²):
- c₁ = 0.73 (ω aligns with stretching — BAD)
- c₂ = 0.26, c₃ = 0.006
- c₂ ≈ c₃? NO. c₃ is essentially zero.
- Without pressure, vorticity aligns with e₁ (Vieillefosse tail).

### Yang pressure added (dA/dt = -A² - H_yang):
- c₁ = 0.09 (pressure kills e₁ alignment — GOOD)
- c₂ = 0.77 (ω goes to e₂ — Ashurst alignment)
- c₃ = 0.13 (still below 1/3!)
- c₂ ≈ c₃? NO. c₂ >> c₃.

### Full NS PDE (from our DNS data):
- KP: c₂ = 0.333, c₃ = 0.333 (SYMMETRIC!)
- TG high |ω|: c₂ = 0.33, c₃ = 0.40

## Conclusion

The c₂ = c₃ symmetry is a FULL PDE phenomenon that emerges from:
1. Non-local pressure (the full Poisson equation, not just Yang's local term)
2. Advective mixing (u·∇A transports alignment between regions)
3. Multi-scale cascade (shell interactions homogenize alignment)

None of these are captured by the local ODE (restricted Euler + Yang).

## Impact on Proof Routes

Route B (symmetric alignment: c₂ = c₃ → c₃ ≥ 1/3):
- The symmetry IS real in full NS (KP data)
- But proving it requires PDE analysis, not just ODE/algebra
- The gap is: prove c₂ ≈ c₃ from the full NS dynamics

Route A (direct: prove c₁ < 1/3 AND c₃ > 1/3):
- Data supports both at high |ω| in TG
- But KP shows c₃ = 1/3 exactly (knife edge)
- The gap is: prove c₃ ≥ 1/3 from the full NS dynamics

Both routes need PDE-level arguments. The local ODE is insufficient.
The incompressibility-only proof does NOT work.

## What We Learned

1. Pressure is NECESSARY for c₁ < 1/3 (RE gives c₁ = 0.73 without it)
2. Pressure alone gives c₁ < 1/3 but NOT c₃ ≥ 1/3
3. The c₂ = c₃ symmetry is an EMERGENT property of the full PDE
4. The proof MUST use PDE structure beyond local dynamics

## 148 proof files. Incompressibility alone is not enough.
