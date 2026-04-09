# NS Regularity — Lean Formalization

249+ theorems across 17 files. 0 sorry in proved theorems.

## The Proof Chain (ProofChain.lean)

```
S²ê ≤ ||S||²_F         [DirectionalBound.lean — Cauchy-Schwarz, PROVEN]
||S||²_F < (3/4)|ω|²   [KeyLemma.lean — 31M+ evals, N=3,4 PROVEN]
→ α < (√3/2)|ω|        [ODE comparison]
→ Type I excluded       [Seregin 2012]
→ NS REGULAR on T³      [ESŠ 2003]
```

**Gap**: Step 2 for all N. c(N) ≈ 1.21/N^{0.98} observed but not proven analytically.

## File Index

### Core Algebra (self-contained, no Mathlib)
| File | Theorems | What |
|------|----------|------|
| StrainVorticity.lean | 7 | Cross products, Lagrange identity, Frobenius expansion |
| SingleModeTheorem.lean | 4 | ||S||²_F = (1/2)|ω|² per mode |
| EqualSplitting.lean | 4 | ∫||S||² = (1/2)∫|ω|² |
| ThreeIdentities.lean | 16 | Trace identities, symmetry decomposition |
| FrobeniusIdentity.lean | 11 | Frobenius expansion, single-mode theorem, cross-terms (7 PROVEN) |

### Proof Chain
| File | Theorems | What |
|------|----------|------|
| DirectionalBound.lean | 3 | S²ê ≤ ||S||²_F (Cauchy-Schwarz) — KEY |
| KeyLemma.lean | 3 | N=3,4 computational certificates |
| ProofChain.lean | 7 | 6-step conditional chain to regularity |
| SignConjecture.lean | 4 | Sign conjecture REFUTED; chain formalized |
| TraceFreeAlignment.lean | 5 | Tr(S)=0 → λ₃² ≤ (2/3)||S||²_F — KEY THEOREM |
| RouteAnalysis.lean | 19 | 5 proof routes, gap analysis |

### Depletion Proof
| File | Theorems | What |
|------|----------|------|
| SingleModeOrthogonality.lean | 117 | Exhaustive single-mode algebra |
| DepletionProof/Compression.lean | 28 | Multi-mode compression bounds |
| DepletionProof/AngularProfile.lean | 14 | Angular distribution analysis |
| DepletionProof/SingleMode.lean | 3 | Single-mode unconditional bound |
| DepletionProof/StrainSelfDepletion.lean | 1 | Self-depletion mechanism |
| DepletionProof/DirectionRotation.lean | 1 | Rotation invariance |
| AveragingBound.lean | 4 | |ω|² ≥ N averaging bound |

### Statements Only
| File | What |
|------|------|
| Challenge.lean | 3 challenge statements (sorry by design) |
| Blowup.lean | 6 deep mathematical statements (the open problem) |
