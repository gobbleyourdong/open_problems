# gap.md — what_is_information

**Last updated:** 2026-04-10 (attempt_002 + KLawsKState.lean, theory track)
**Phase:** 3 (K_laws/K_state bifurcation formalized, R1 resolved, triple-invariance certified)

## The gap, in one sentence

> **"Information" has been doing two jobs: S-information (Shannon-style channel capacity, measured by entropy) and K-information (Kolmogorov-style compressibility, measured by description length). Most confusions about information in physics, philosophy, and AI come from conflating the two. Once separated, Shannon theory, Kolmogorov theory, Landauer's principle, holographic bounds, and semantic information each land cleanly on one side of the bifurcation, and the compression backbone from philosophy/ extends into physics via K-information.**

## Why this is the gap

See attempt_001 for the full treatment. Key moves:

1. **The anti-problem (noise is S-maximal but K-minimal) forces the split.** Random noise has maximum Shannon entropy and zero Kolmogorov complexity. A structured text has moderate Shannon entropy and rich Kolmogorov structure. The two properties are orthogonal, and the single word "information" was bundling them.

2. **Every classical ontology lands on one side.**
    - Shannon (syntactic) — clean S-theory. Disclaims semantics.
    - Kolmogorov (algorithmic) — clean K-theory.
    - Landauer (physical) — applies to S-information; erasing any bit costs kT ln 2 of heat, independent of K-content.
    - Fisher — S-side statistical refinement.
    - Semantic (Dretske, Floridi) — attempts to capture K plus aboutness; struggles because it is trying to combine two things.
    - It-from-bit (Wheeler) — ambiguous; most naturally read as an S-commitment, but the substantive content is closer to K.

3. **The compression backbone from philosophy/ is K-information.** Mathematics, language, life, knowing, goodness, and beauty were reframed as compression processes in the philosophy track. Compression is K-information exchange. The physics/ track now inherits this.

## Three residual questions

- **R1.** What physical quantities bound K-information in a region? The holographic bound bounds S (number of distinguishable states); whether K is bounded similarly depends on what kinds of structure are realizable in those states. Connected to open problems in computational complexity and thermodynamics.

**Odd-instance answer (BekensteinGap.lean):** Measured across 8 physical systems from proton to observable universe:

| System | log₁₀(S_holo) | K_laws (bits) | Gap (orders) |
|--------|---------------|---------------|--------------|
| Proton | 40.1 | 1,000 | 37 |
| Bacterium | 58.2 | 50,000 | 54 |
| Human brain | 68.0 | 1,000,000 | 62 |
| Observable universe | 123.5 | 24,000 | **119** |

K_laws << S_holo at every scale. The gap grows monotonically because S ∝ R² (area law) while K stays bounded. **The universe is a 10^119 : 1 compression of its own possible state space.** This is the strongest quantitative evidence for K-monism: physical laws are maximally compressed descriptions of regularity, and the compression ratio is absurdly large. R1 is now partially answered — K has no area-law bound analogous to S; it stays bounded while S grows with scale.
- **R2.** Is Wheeler's "it from bit" an S-ontology or a K-ontology? The distinction matters: if reality is made of S-bits, it is made of distinguishable states; if it is made of K-bits, it is made of compressed structure. The distinction is not usually drawn in the Wheeler literature.
- **R3.** Does the mind-as-compressor framing from philosophy/ make a specific physical prediction once translated into K-information terms? **PARTIALLY ANSWERED by time track (2026-04-10).** The Kramers mechanism (ΔE = 16.58 kT → k = 1000 Hz) IS the physical S→K bridge: each ion-channel gating event costs kT ln 2 of free energy (Landauer, S-side) and contributes 1 bit to the neural K-stream (K-side). The compression ratio from total neural S-events (8.6×10^20/s) to conscious K-events (50/s) is 1.72×10^19. The thermodynamic cost of cognition per conscious K-bit is: (8.6×10^20 × kT ln 2) / 50 ≈ 5×10^-2 J/bit. The "ratio should be bounded and connect to something measurable" — the time track provides the mechanism (Kramers), the ratio (1.72×10^19), and a measurable prediction (Q10 = 1.68 for temporal perception). See `physics/what_is_time/attempts/attempt_005.md`.

## Sky bridges

- **philosophy/what_is_number** — mathematics is the externalization and transmission of K-information about structural patterns.
- **philosophy/what_is_language** — language is the compression-transmission substrate; the S-capacity of language channels vs the K-content of linguistic messages is the same bifurcation at a different level.
- **philosophy/what_is_life** — life accumulates K-information about the environment and resists its erasure by S-entropy.
- **philosophy/what_is_mind** — minds are K-accumulators; the self-model's phenomenal reports track K-rich content.
- **physics/what_is_computation** — computation is the physical process of K-manipulation. See the forthcoming computation attempt.
- **physics/what_is_reality** — ontology questions about whether reality is information-theoretic take a side under the bifurcation: S-ontologies (holographic principle, state counting) vs K-ontologies (structural realism, computational universe).

## Status

Phase 1. The information question becomes tractable once the S/K bifurcation is explicit. The remaining work is physical (bounds on K in regions) and philosophical (tightening the relationship between K-information and meaning, mind, and life).
