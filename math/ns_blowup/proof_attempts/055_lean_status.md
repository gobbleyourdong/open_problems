---
source: Lean compilation results
type: VERIFIED LEMMAS — two theorems, zero sorries
status: COMPLETE
date: 2026-03-26
---

## Lean-Verified Theorems (Comparator-ready)

### 1. Single-Mode Orthogonality (SingleMode.lean)
```
For k, ω ∈ R³ with k ⬝ᵥ ω = 0:
  twiceStrainForm ω k (k ⨯₃ ω) = 0
```
Self-stretching is zero for each Fourier mode.
Axioms: [propext, Classical.choice, Quot.sound] ✅

### 2. Strain Self-Depletion (StrainSelfDepletion.lean)
```
For any symmetric B and vector a:
  (quadForm a B)² ≤ (a⬝ᵥa) × quadFormSq a B
```
i.e., α² ≤ |ê|² × (ê·S²·ê). For unit ê: α² ≤ ê·S²·ê.
Axioms: [propext, Classical.choice, Quot.sound] ✅

### Combined Implication
From the strain evolution at x*:
```
dα/dt = -(ê·S²·ê) - ê·H·ê + ν(ê·ΔS·ê) + (frame terms)
      ≤ -α² - ê·H·ê + ν(ê·ΔS·ê)
```
The -α² self-depletion is ALWAYS present and ALWAYS ≥ α².

### Build Info
- Lean 4.28.0 (toolchain 4.29.0-rc8 via Mathlib)
- Mathlib master (8200 cached oleans)
- `lake build` → 1428/1428 success
- `lake env lean Test/AxiomCheck.lean` → all clean
- Comparator: `lake env comparator comparator_config.json` → "Your solution is okay!"
  (for SingleMode; StrainSelfDepletion not yet in Challenge file)
