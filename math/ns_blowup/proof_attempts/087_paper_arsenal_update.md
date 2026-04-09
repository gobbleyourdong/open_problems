---
source: 13 new papers (morning session)
type: ARSENAL UPDATE — new tools for the proof
date: 2026-03-26
---

## New Tools from Papers (First Batch)

### 1. Moffatt-Kimura (2019): Reconnection Averts Singularity
- PROVED: Even in optimal blowup geometry (pyramid vortices), viscous
  reconnection prevents mathematical singularity for ALL ν > 0
- Circulation transfer: dΓ/dτ = -ε·s·Γ/(2√π·δ³)·exp(-s²/4δ²)
- Peak amplification: ω_max/ω₀ ~ exp[1 + 220(log[R_Γ/2000])²]
  (enormous but FINITE for any Re)
- δ²_min > 0 always (core never reaches zero thickness)
- **FOR US**: Each reconnection event has a QUANTIFIED endpoint
  (Γ → 0). The surviving circulation formula is our ΔC_min.

### 2. Enciso-Lucà-Peralta-Salas (2017): Reconnection is Rigorous
- PROVED: Vortex reconnection occurs in smooth NS solutions on T³
- Can engineer n reconnection events for any n
- Based on perturbation near Beltrami flows
- **FOR US**: Reconnection is a PROVEN feature of NS, not just observed

### 3. Kauffman (2022): Topology Bounds Reconnection Count
- R(K) = c(K) - s(K) + 1 (reconnection number of a knot)
- For trefoil T(2,3): R = 2 (exactly 2 reconnections to unknot)
- |σ(K)| ≤ R(K) (signature bounds reconnection from below)
- **FOR US**: FINITE upper bound on topology-changing reconnections.
  Each consumes budget → finite total budget → bounded stretching.

### 4. Yao-Hussain (2022 Annual Review): THE KEY PAPER
- Three phases of reconnection: advection → bridging → threading
- Duration τ_r ~ Re^{-1/2} (SHRINKS with Reynolds)
- Separation: δ(t) ~ (Γ|t-t₀|)^{1/2} (universal)
- Peak |ω| increases with Re but enstrophy integral appears bounded
- Core flattening LIMITS stretching efficiency
- **HELICITY IDENTITY**: |u·ω|² + |ω×u|² = |u|²|ω|²
  - At x* where u⊥ω: |ω×u| = |u||ω| (MAXIMUM Lamb vector)
  - Maximum Lamb = maximum nonlinearity = fastest reconnection
  - High helicity regions: Lamb suppressed → stretching weak
  - **THE DICHOTOMY**: either fast reconnection or weak stretching

## New Tools Summary

| Tool | What it gives | Source |
|------|--------------|--------|
| Γ transfer equation | Event endpoint (Γ→0) | Moffatt-Kimura |
| R(K) bound | Finite reconnection count | Kauffman |
| τ_r ~ Re^{-1/2} | Event duration scaling | Yao-Hussain |
| |u·ω|²+|ω×u|²=|u|²|ω|² | Helicity-Lamb dichotomy | Yao-Hussain |
| u⊥ω at x* | Max Lamb at max vorticity | Our measurement |
| Core flattening | Natural stretching limiter | Yao-Hussain |

## The Emerging Proof Path

1. At x*: u⊥ω → h=0 → |ω×u| maximal → strongest nonlinear interaction
2. Strongest nonlinearity → fastest reconnection (τ_r ~ Re^{-1/2})
3. Reconnection transfers circulation (Moffatt-Kimura eq 2.9)
4. Circulation → 0 ends the event (Γ drops to near-zero)
5. Each event consumes ΔC from Constantin budget
6. Number of topological events ≤ R(K) (Kauffman)
7. Non-topological events bounded by energy budget
8. Total ∫α₊ ≤ (# events) × (per-event bound) ≤ finite

## Waiting on Second Batch (7 more papers)
- 1909.00041: Maximum enstrophy amplification (key bound)
- 2405.11875: Most recent (2024)
- Others: TBD
