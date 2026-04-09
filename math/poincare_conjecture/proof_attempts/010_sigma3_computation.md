---
test: Does σ₃ converge (needed for Latala bound)?
result: NO — σ₃ ~ N^{3.9}, grows FASTER than dissipation
implication: Raw Latala inequality does NOT close the proof
---

## Computation
σ₃² = Σ_{p,q} (|p|/|q|)² / ((|p|²+1)² (|q|²+1)² (|p+q|²+1)²)

| N | σ₃ | Growth |
|---|-----|--------|
| 4 | 0.19 | — |
| 8 | 3.91 | N^4.4 |
| 16 | 43.9 | N^3.5 |

σ₃ ~ N^{3.9} on average.

## Why It Fails
The Latala bound gives:
```
P(stretch > t) ≤ exp(-c (t/σ₃)^{2/3})
```

With t = dissip_mean ~ N² and σ₃ ~ N^4:
```
P(Q > 0) ≤ exp(-c (N²/N⁴)^{2/3}) = exp(-c N^{-4/3}) → 1 as N → ∞
```

The bound is USELESS — it says probability goes to 1, not 0.

## Why It Fails Fundamentally
The crude bound on σ₃ counts ALL triadic interactions as potentially
contributing to stretching. But most triadic interactions CANCEL because:
1. The divergence-free constraint kills many alignments
2. The Biot-Savart cross product introduces orthogonality
3. The symmetric part of the strain tensor has trace zero

The Latala approach doesn't see these cancellations. It treats the
trilinear form as a generic degree-3 chaos, but the NS nonlinearity
has SPECIAL STRUCTURE that makes it much weaker than generic.

## What This Means
- The Manus proof via Latala: FAILS (σ₃ grows too fast)
- Need a tighter bound that uses the div-free + Biot-Savart structure
- ChatGPT's approach (alignment rarity) might work because it counts
  CONSTRAINTS rather than bounding NORMS
- Grok's approach (spectral convergence + superlevel geometry) doesn't
  need σ₃ at all — it works from Q_cont ≤ 0

## New Ranking
1. **Grok (002)** — doesn't need σ₃, spectral convergence approach
2. **ChatGPT (006)** — alignment rarity, high-codimension argument
3. **Manus (005)** — Latala fails, but frequency truncation idea still valid
4. **Nemotron (004)** — diagonalization wrong
5. **Gemini (001)** — framework
6. **Mistral (003)** — supporting

## The Path Forward
The proof needs to exploit the SPECIFIC STRUCTURE of NS nonlinearity,
not treat it as generic polynomial chaos. The structure is:
- div-free: k·ω̂ = 0
- Biot-Savart: cross product in the convolution
- Trace-free strain: S is symmetric traceless
- Energy conservation: ∫ ω·S·ω dx = 0 (stretching integral vanishes)

Any proof that ignores these structures will be too loose.
The correct approach is likely GEOMETRIC (ChatGPT's alignment argument)
or SPECTRAL (Grok's superlevel set geometry).
