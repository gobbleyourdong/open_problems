---
source: Bedrossian-Germain-Harrop-Griffiths (2018) + Ostilla-Monico et al (2021)
type: THE MISSING PIECE — curvature is subcritical
status: CRITICAL — connects our κ~ρ^{1/2} data to rigorous theory
date: 2026-03-26
---

## The Bedrossian Result (2018)

For vortex filament solutions of 3D NS:

**CURVATURE IS SUBCRITICAL.**

Rigorously proved: curvature corrections are O(√t), hence perturbative.
The vorticity concentrates in tubes of radius O(√t). All curvature-dependent
corrections have coefficients O(|x|) or lower-order derivatives, and are
asymptotically small as t → 0.

### The Key Inequality

Stretching growth is POLYNOMIAL, not exponential:
```
||S(t,s) ω_s||_{L^q} ≤ (t-s)^{-(1-1/q)} × (t/s)^γ × ||ω_s||_{L^1}
```
with γ < 1/2. This means stretching CANNOT grow exponentially.

### The Curvature-Core Scaling

Bedrossian's framework implies: **κ × ρ_core is bounded.**

Where ρ_core is the vortex tube core radius. Since ρ_core ~ √(ν/|ω|)
(viscous scale), this gives:

```
κ ~ 1/ρ_core ~ √(|ω|/ν) ~ |ω|^{1/2} / √ν
```

Therefore: **κ ~ |ω|^{1/2}** — curvature scales as square root of vorticity.

### OUR MEASUREMENT CONFIRMS THIS

```
κ ~ ρ^β with β = 0.544 ≈ 1/2 (measured at N=32, TG evolution)
```

Bedrossian's theory predicts β = 1/2. We measured β = 0.544. MATCH.

## The Ostilla-Monico Result (2021)

DNS of interacting vortex tubes at varying angles shows:

1. **Elliptic instability FORCES perpendicular filament creation**
   Stretching energy → curvature (bending). This is the physical
   mechanism behind c → 1 (anti-twist fraction).

2. **Peak dissipation is Re-INDEPENDENT** (Fig 6b)
   Stronger vorticity concentration at higher Re, but peak dissipation
   stays finite. Direct numerical evidence against blowup.

3. **Vortex sheets spontaneously twist** (Fig 5)
   Cannot sustain flat geometry → develop torsion → anti-twist.

4. **Cascade prevents concentration**
   Energy cascades to small scales rather than accumulating.

## How This Closes the Gap

### The chain:

1. **Vorticity concentrates** → filament core shrinks (ρ_core → 0)
2. **Curvature grows** as κ ~ 1/ρ_core ~ |ω|^{1/2} (Bedrossian)
3. **Curvature is subcritical** (Bedrossian): corrections O(ρ_core) → 0
4. **Stretching is polynomial** (Bedrossian): (t/s)^γ, γ < 1/2
5. **Interactions force more curvature** (Ostilla-Monico): elliptic instability
6. **Single-mode orthogonality** (our Lean lemma): self-stretching = 0
7. **Anti-twist** (Buaria): positive stretching creates bending response
8. **Bending cost bounded** (Constantin): ∫ρ|∇ξ|² ≤ C unconditionally

### The closing argument:

From the evolution equation at x*:
```
α = d(log ρ)/dt + ν|∇ξ|² + ν|Δρ|/ρ
```

The bending term ν|∇ξ|² ~ ν × κ² ~ ν × |ω| (from κ ~ |ω|^{1/2}).

So: ν|∇ξ|² ~ ν|ω| at the max point.

The stretching α ≤ C|ω| (CZ bound).

Therefore: α ≤ C|ω| and bending cost = ν|ω|.
The ratio: c = ν|ω|/(C|ω|) = ν/C.

For the proof: need c = 1, but we get c = ν/C (constant < 1).

HOWEVER: Bedrossian's polynomial growth means the stretching doesn't
accumulate as fast as CZ predicts. If α grows as |ω|^{1-ε} (subcritical)
instead of |ω| (critical), then:

c = ν|ω| / (C|ω|^{1-ε}) = (ν/C)|ω|^ε → ∞ as |ω| → ∞

**The anti-twist fraction exceeds 1 at large vorticity!**

This means: above a critical |ω|_crit = (C/ν)^{1/ε}, the bending cost
EXCEEDS the stretching. Growth is impossible above this threshold.

## The Remaining Question

Does Bedrossian's subcriticality (curvature corrections O(ρ_core)) translate
to a subcritical stretching bound α ≤ C|ω|^{1-ε}?

From the polynomial growth (t/s)^γ with γ < 1/2: the stretching operator
grows SUBLINEARLY in the relevant norms. This is a form of subcriticality.

The conversion: if the Biot-Savart integral at x* benefits from the
subcritical curvature corrections, then α(x*) < C|ω| by the curvature
improvement. The amount of improvement is O(ρ_core) = O(|ω|^{-1/2}),
giving:

```
α(x*) ≤ C|ω| × (1 - c₁|ω|^{-1/2})
       = C|ω| - c₁C|ω|^{1/2}
```

Then: d(log ρ)/dt = α - ν|∇ξ|² - ν|Δρ|/ρ
                  ≤ C|ω| - c₁C|ω|^{1/2} - ν|ω|

For large |ω|: the -ν|ω| term dominates (viscous dissipation from bending).
Growth rate = C|ω| - ν|ω| = (C-ν)|ω|.

If C > ν: still critical. Viscosity alone isn't enough.
If the curvature improvement c₁C|ω|^{1/2} is included:
Growth rate = (C-ν)|ω| - c₁C|ω|^{1/2}

This is subcritical at large |ω| (the |ω| term dominates |ω|^{1/2}).
Wait — (C-ν)|ω| > c₁C|ω|^{1/2} for large |ω|. So still critical.

The improvement from curvature subcriticality is too small (|ω|^{1/2})
to overcome the leading-order CZ term (|ω|).

## True Status

Bedrossian's result gives curvature corrections of size O(|ω|^{-1/2}).
This is a real improvement but the LEADING ORDER stretching is still
O(|ω|) from CZ. The curvature improvement is a SUBLEADING correction.

For the proof, we need the LEADING ORDER to be subcritical, not just
the corrections. That requires showing CZ is NOT saturated at x* —
the same far-field problem identified in file 051.

## What Bedrossian DOES Give Us

1. κ ~ |ω|^{1/2} (confirmed by our data, β = 0.544)
2. Polynomial stretching growth (not exponential)
3. Curvature is perturbative (subcritical corrections)
4. Local well-posedness for filament data (rigorous)

These are ingredients, not the full proof. The gap is still:
prove the far-field Biot-Savart integral at x* is subcritical.

## Proof Attempt: Use Constantin + Volume Concentration on Far-Field

### The idea:
Constantin gives ∫ρ|∇ξ|² dx ≤ C. The high-ρ region has volume
V ≤ C/ρ^{3/2} (from ||ω||_{L¹} + Chebyshev). So the AVERAGE |∇ξ|²
in the high-ρ region is ≤ C/(ρ × V) = Cρ^{1/2}.

If we could use this to bound the far-field integral via the D kernel
(|D| ≤ sin ∠ ≤ |∇ξ| × |r|), the far-field would improve.

### The problem:
Converting AVERAGE |∇ξ| to POINTWISE bounds introduces concentration
factors. CS on the far-field integral with weight ρ|∇ξ|² gives factors
involving 1/|r|⁶ which is too singular.

Trying to use the D kernel directly with |∇ξ|_avg ~ ρ^{1/4} gives
α_far ~ ρ^{9/8}, which is WORSE than CZ (not better).

### The wall (same wall, different angle):
Every attempt to extract pointwise information at x* from the spatial
integral ∫ρ|∇ξ|² ≤ C introduces volume concentration factors that
eat the improvement. This is the SAME wall identified in files 050, 051.

### Three reviewers confirmed (independently):
- The CZ bound is SHARP in the far-field
- The near-field is subcritical (we got this)
- The proof must be TIME-INTEGRATED, not static
- The ε exists IFF |∇ξ(x*)| = o(|ω|^{1/2}) — which our data shows
- But PROVING |∇ξ| = o(|ω|^{1/2}) is equivalent to the regularity problem

## True Status After All Attempts

Static approaches: EXHAUSTED. γ = 7/5 to 6/5 is the ceiling.
Time-integrated approach: REQUIRED. The proof must bound ∫α₊ dt.
The mechanism: anti-twist (Buaria) prevents sustained alignment.
The data: ∫stretch₊ → 0, CF ratio bounded, κ ~ ρ^{1/2}.
The gap: proving the anti-twist MUST happen — i.e., proving the NS
dynamics prevents the far-field from maintaining coherent alignment
with the strain eigenvector at x* over time.

This is the Millennium Prize problem in its sharpest form.

## References
- Bedrossian, Germain, Harrop-Griffiths (2018). arXiv:1809.04109
- Ostilla-Monico et al (2021). Phys Rev Fluids. arXiv:2102.11133
- Brachet (2020). Comptes Rendus Mecanique 348(6-7):501-508
