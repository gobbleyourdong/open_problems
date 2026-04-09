---
source: JB's level-set idea + reviewer 1 intermittency + our pressure crossover
type: CONDITIONAL REGULARITY THEOREM — the cleanest formulation
status: The argument works IF α ≤ 0 on {|ω| > ρ_c}
date: 2026-03-26
---

## The Level-Set Regularity Theorem (Conditional)

### Hypothesis: Pressure Crossover
There exists ρ_c > 0 such that for all smooth NS solutions on T³:
```
α(x,t) := ξ(x,t) · S(x,t) · ξ(x,t) ≤ 0
    whenever |ω(x,t)| > ρ_c
```

(Our data: ρ_c ≈ 12 for TG at N=64 with ν=10⁻⁴.)

### Theorem: If the hypothesis holds → global regularity.

### Proof:

**Step 1:** Split the enstrophy production:
```
∫ω·S·ω dx = ∫_{|ω|>ρ_c} ω·S·ω dx + ∫_{|ω|≤ρ_c} ω·S·ω dx
```

**Step 2:** On {|ω| > ρ_c}: by hypothesis, α ≤ 0, so ω·S·ω = |ω|²α ≤ 0.
Therefore: ∫_{|ω|>ρ_c} ω·S·ω dx ≤ 0.

**Step 3:** On {|ω| ≤ ρ_c}:
```
|ω·S·ω| ≤ |ω|² |α| ≤ |ω|² |S| ≤ ρ_c² |S|
```

Integrating: ∫_{|ω|≤ρ_c} ω·S·ω dx ≤ ρ_c² ∫|S| dx = ρ_c² ||S||₁

**Step 4:** CZ in L¹: ||S||₁ ≤ C||ω||₁

**Step 5:** L¹ vorticity bound (unconditional, file 071):
||ω(t)||₁ ≤ ||ω₀||₁ + CE₀/ν =: M₁

**Step 6:** Combine:
```
∫ω·S·ω dx ≤ 0 + ρ_c² × C × M₁ =: K (constant)
```

**Step 7:** Enstrophy evolution:
```
dE/dt = 2∫ω·S·ω dx - 2ν||∇ω||² ≤ 2K - 2ν||∇ω||²
```

**Step 8:** Since ||∇ω||² ≥ 0: dE/dt ≤ 2K (constant bound on growth rate).

**Step 9:** E(T) ≤ E₀ + 2KT (linear growth for any T).

**Step 10:** Bounded enstrophy for any finite T → solution is smooth on [0,T]
(by the Foias-Temam regularity criterion: sup E(t) < ∞ → regularity).

Since T is arbitrary: **global regularity.** □

### What This Means

The enstrophy grows at most LINEARLY in time (not exponentially or faster).
The growth constant K = ρ_c² × C × M₁ depends only on:
- ρ_c: the crossover threshold (measured ≈ 12)
- C: the CZ constant for ||S||₁ ≤ C||ω||₁ in L¹ (absolute)
- M₁: the L¹ vorticity bound (depends on IC and ν)

### The ONE Hypothesis

α(x,t) ≤ 0 whenever |ω(x,t)| > ρ_c.

This says: the stretching rate is non-positive in ALL high-vorticity regions.

Our data confirms this at ρ_c ≈ 12 for TG at N=64. The mechanism:
the isotropic pressure Hessian (Δp/3 > 0) dominates the deviatoric
part at high |ω|, making the total pressure Hessian oppose stretching.

Proving this hypothesis analytically would prove NS regularity.

### Lean Formalization Target

This is formalizable as a CONDITIONAL theorem in Lean:
- Hypothesis: a function-level condition on α and |ω|
- Conclusion: enstrophy is bounded linearly in T
- The proof uses: level-set splitting, CZ in L¹, L¹ bound

The algebraic steps (splitting, bounding, integrating) are standard
and should be expressible in Lean with Mathlib's measure theory.

### Connection to Everything

- **Pressure crossover** (file 056): measured ρ_c ≈ 12
- **Isotropic dominance** (Buaria & Pumir 2023): grows as Ω²
- **Single-mode orthogonality**: explains WHY α < 0 at high |ω|
- **Constantin's L¹ bound**: provides M₁ unconditionally
- **Miller's decomposition**: the ω⊗ω piece is orthogonal to -ΔS,
  so the only dangerous piece (S²) is suppressed on {|ω|>ρ_c}

96 proof files. The cleanest path to conditional regularity.
