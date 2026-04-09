# Hou 2022 FoCM — Adaptive Mesh Parameters (Gemini extraction, verified)

## Vorticity Quantities Tracked
- ‖ω₁‖_∞ where ω₁ = ωθ/r  (PRIMARY — this is what we need to track)
- ‖ω‖_∞ (full 3D vorticity magnitude)
- Relative growth: ‖ω(t)‖_∞ / ‖ω(0)‖_∞

## Grid Tracking Indices
- J: grid index where u₁ achieves max along r
- J_r: grid index where u₁,r achieves max along r
- I_w: grid index where ω₁ achieves max along z
- I_wz: grid index where ω₁,z achieves max along z

## Time Period 1: t=0 to T₁=0.002191729
r(ρ) map (4-phase, static):
  r₁=0.001, r₂=0.05, r₃=0.2
  s_ρ₁=0.001, s_ρ₂=0.5, s_ρ₃=0.85
  No shift during this period.

z(η) map (3-phase, adaptive):
  z₁=0.1, z₂=0.25
  s_η₁=0.5, s_η₂=0.85
  Shift when I < 0.2·n₁:
    z₁ = 2·z(I_w), z₂ = 10·z(I_w)
    s_η₁ = 0.6, s_η₂ = 0.9

## Time Period 2: T₁ to T₂=0.002261605
z(η): same as Period 1

r(ρ) map (dynamic):
  s_ρ₁=0.05, s_ρ₂=0.6, s_ρ₃=0.9
  dr = r(J) - r(J_r)
  r₂ = r(J) + 2·dr
  r₁ = max((s_ρ₁/s_ρ₂)·r₂, r(J_r) - 5·dr)
  r₃ = max(3·r(J), (r₂-r₁)·(s_ρ₃-s_ρ₂)/(s_ρ₂-s_ρ₁) + r₂)
  Shift when J_r < 0.2·n₂

## Time Period 3: t ≥ T₂ (late stage)
r(ρ) map:
  s_ρ₁=0.05, s_ρ₂=0.5, s_ρ₃=0.9
  dr = r(J) - r(J_r)
  r₂ = r(J) + 8·dr
  r₁ = max((s_ρ₁/s_ρ₂)·r₂, r(J_r) - 3·dr)
  r₃ = max(4.5·r(J), (r₂-r₁)·(s_ρ₃-s_ρ₂)/(s_ρ₂-s_ρ₁) + r₂)
  Shift when J_r < 0.2·n₂

z(η) map:
  s_η₁=0.05, s_η₂=0.5, s_η₃=0.85
  dz = z(I_w) - z(I_wz)
  z₂ = z(I_w) + 2·dz
  z₁ = max((s_η₁/s_η₂)·z₂, z(I_wz) - 6·dz)
  z₃ = max(4.3·z(I_w), (z₂-z₁)·(s_η₃-s_η₂)/(s_η₂-s_η₁) + z₂)
  Shift when I_z < 0.2·n₁

## Key Implementation Notes
- Computation on UNIFORM grid in (ρ,η) space
- Maps r=r(ρ) and z=z(η) create adaptive physical grid
- Phase 0: covers r≈0 region specifically
- Phase 1: highest density, covers inner profile of sharp front
- Phase 2-3: outer profile and far-field
- Mesh tracks the singularity dynamically as it travels to (0,0)
