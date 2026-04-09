---
source: c₃ rotation decomposition — e₃ moves toward ω, not the other way
type: MECHANISTIC BREAKTHROUGH — the strain rearranges around the vorticity
date: 2026-03-28
---

## The Experiment

At high-|ω| points, decompose dc₃/dt = d[cos²(ω̂, e₃)]/dt into:
1. ω rotation contribution: (ω̂ rotates, e₃ fixed)
2. e₃ rotation contribution: (e₃ rotates, ω̂ fixed)

## Results

### TG (Euler, N=32):
- e₃ rotation: 85-90% of dc₃/dt (POSITIVE: e₃ rotates TOWARD ω)
- ω rotation: 10-15% of dc₃/dt (NEGATIVE: ω moves slightly AWAY from e₃)
- e₃ rotation helps c₃: 80-85% of points
- ω rotation helps c₃: only 4-5% of points

### KP (Euler, N=32):
- e₃ rotation: 65-90% of dc₃/dt (POSITIVE)
- ω rotation: 10-35% of dc₃/dt (NEGATIVE)
- Pattern is the same: e₃ rotates toward ω

## Physical Mechanism

The vorticity direction ω̂ barely moves. Instead, the STRAIN FIELD
rearranges around the vorticity, with its compressive axis (e₃)
rotating toward ω̂.

This is driven by the STRAIN-ROTATION COMMUTATOR [S, Ω] = SΩ - ΩS
in the strain evolution equation:

  dS/dt = -S² + [S, Ω] + H + ν·ΔS + advection

The [S, Ω] term is a TORQUE on the strain eigenvectors. It rotates
them toward alignment with ω. This is a well-known mechanism in
turbulence theory (responsible for Ashurst alignment ω → e₂).

But why does e₃ (not e₂) align with ω at high |ω|?

### The (0,2,2) mode mechanism (from file 151):
1. TG vorticity creates stretching via (ω·∇)u
2. The stretching generates new strain patterns at |k|=2√2
3. These new patterns have their compression aligned WITH ω
4. As the new strain grows, e₃ increasingly points toward ω
5. The [S, Ω] commutator maintains this alignment

### Why e₃ and not e₂:
At Ashurst equilibrium: ω ∝ e₂, [S, Ω] = 0 (no torque).
The nonlinear (0,2,2) modes break this equilibrium by creating
strain with e₃ ∝ ω. This is NOT the Ashurst equilibrium — it's
a new attractor created by the specific geometry of vortex stretching.

The Ashurst alignment ω → e₂ is for WEAK vorticity.
At HIGH |ω|, the self-generated strain dominates, and the
new equilibrium has ω → e₃ (compression). This is the phase
transition at |ω| ≈ 12 identified in file 145.

## Connection to Previous Findings

1. File 150: c₃ ≥ 1/3 at k ≤ 4 → low-mode, from first nonlinear products
2. File 151: (0,2,2) modes create axisymmetric compression along ω
3. File 153: H_ωω > 0 (full pressure), so pressure OPPOSES compression
4. THIS FILE: e₃ rotates toward ω (85-90%), not ω toward e₃

The story: The nonlinear stretching creates strain patterns (0,2,2 modes)
whose compressive axis aligns with ω. The pressure opposes this alignment
but is overwhelmed. The result: c₃ > 1/3, α < 0, compression.

## Proof Strategy (updated again)

The [S, Ω] commutator rotates e₃ toward ω. This is algebraically
computable from the strain and vorticity fields.

Key observation: if the INITIAL nonlinear product already has e₃ ∝ ω
(which we proved analytically for TG), and [S, Ω] PRESERVES this
alignment, then c₃ ≥ 1/3 is maintained.

The proof reduces to:
1. Show the first nonlinear products create e₃ ∝ ω (done for TG)
2. Show [S, Ω] maintains this once established
3. Show the pressure opposition is weaker than the commutator torque

## 154 proof files. The strain rearranges around the vorticity.
