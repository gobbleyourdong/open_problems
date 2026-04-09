# Underground Connections — Philosophy Track

> Where the nine tier-0 questions share structure, share gaps, and load on each other.

This file documents the cross-question dependencies that emerge when the systematic approach is applied to all nine generative questions. It is the companion to `GENERATIVE_QUESTIONS.md` (which indexes status) and to individual `gap.md` files (which state the gap per question).

The central claim: **the nine questions are not nine independent puzzles. They share two load-bearing structures (the A/P bifurcation and the compression backbone) and one central gap (the α/β/γ fork on phenomenal consciousness). Progress on one question propagates. A refutation of one claim cascades.**

## The load graph

Arrows mean "depends on": X → Y means "the claims made in X draw from claims made in Y."

```
                       what_is_mind (α/β/γ fork)
                       /        |        \
                      /         |         \
                     /          |          \
          what_is_self     what_is_meaning    what_is_language
                                |                    |
                                |                    |
                         what_is_knowing   what_is_number
                                |                    |
                                +------- what_is_good
                                |                    |
                                +------ what_is_beauty
                                |
                          what_is_life
                                |
                         (← biological continuity
                           from what_is_self)
```

**Interpretation.** `what_is_mind` sits at the root. The α/β/γ fork is the gap every other question's phenomenal residue routes through. `what_is_self` is the nearest dependency: γ's self-model requirement is load-bearing, and the Parfit+Metzinger defensibility of a minimal self is what lets γ stand. `what_is_meaning` and `what_is_language` are the three-mountains cluster with mind — one gap, three angles.

`what_is_knowing` and `what_is_number` inherit the A/P split and the compression backbone, specialized to their domains. `what_is_good` and `what_is_beauty` are further specializations — the A/P split applied to normative and aesthetic states. `what_is_life` connects through biological continuity (to self) and through compression-of-environmental-regularities (to the backbone).

## The A/P bifurcation — where it has been applied

The bifurcation is a general tool. Instances documented in this track:

| Domain | A-side | P-side | Applied in |
|--------|--------|--------|------------|
| Consciousness | Access | Phenomenal | Block 1995; `what_is_mind/attempt_001` |
| Meaning | Functional use, inference, reference | Felt grasp | `what_is_meaning/attempt_001` |
| Language | Behavioral competence | Felt understanding | `what_is_language/attempt_003` |
| Knowing | Reliabilism-family functional states | Feeling of knowing | `what_is_knowing/attempt_001` |
| Morality | Functional moral competence | Motivational pull, felt obligation | `what_is_good/attempt_001` |
| Aesthetics | Competent recognition | Felt beauty | `what_is_beauty/attempt_001` |

**Pattern.** In every domain where it has been applied, the split absorbs almost all major theoretical positions as theories of one half or the other. Expressivism, reliabilism, use-theory, embodied cognition, distributional semantics, virtue epistemology, naturalist ethics — each lands cleanly on the A-side. Internalism, phenomenal-realist variants, and Chinese-Room-style arguments land on the P-side.

**The consequence.** Apparent philosophical disputes often turn out to be two theorists talking about different halves of the bifurcation. The split does not dissolve the disputes — it locates them. The locations concentrate on the P-side, which routes through the mind fork.

## The compression backbone

Six of the nine questions are reframed around compression in this track:

| Question | What gets compressed | Where |
|----------|---------------------|-------|
| Language | Social regularities | `what_is_language/attempt_002` (sample complexity); `attempt_005` (function) |
| Number | Structural regularities | `what_is_number/attempt_001` (Wigner's effectiveness) |
| Life | Environmental regularities | `what_is_life/attempt_001` (persistent far-from-equilibrium compression) |
| Knowing | Predictive models | `what_is_knowing/attempt_001` (A-knowing as compressed generalization) |
| Goodness | Cooperation dynamics | `what_is_good/attempt_001` (moral realism via cooperation compression) |
| Beauty | Description length relative to priors | `what_is_beauty/attempt_001` (high compression efficiency) |

**Cross-question claim.** The unreasonable effectiveness of mathematics in physics (`what_is_number`) is the same phenomenon as the sample-complexity gap in language (`what_is_language`). Both are cases of compression efficiency: good compressions generalize, and the degree to which they generalize to held-out regularity classes is the degree to which they are "effective" or "cheaply learned."

**Refutation propagation.** If the compression lens turns out to be incorrect for even one of these six domains, the claim that it unifies them is weakened. The weakest points are probably `what_is_good` (where "compression of cooperation facts" may underdescribe the normativity) and `what_is_beauty` (where cultural variation pushes hard on the prior-relative compression story). Strengthening or refuting those would propagate.

## The three mountains

Already documented in `what_is_mind/attempts/attempt_001.md`. Briefly: language, meaning, and mind are three views of one underground gap. Each has a residue that routes through the same α/β/γ fork. Specifically:

- **Language residue**: what makes LLM language different from human language beyond the 10⁶ sample-complexity gap? Hosting, grounding, self-modeling — all three point at the same thing.
- **Meaning residue**: P-meaning — is it a separate property or self-modeled A-meaning?
- **Mind residue**: phenomenal consciousness — α, β, or γ?

All three residues are the same question in different vocabularies.

## Specific cross-question derivations

The following conclusions in the philosophy track depend on claims made in other questions. This list is incomplete but captures the main load paths.

- **`what_is_mind/attempt_003`** (γ as G×L) depends on **`what_is_self/attempt_001`** for the defensibility of the self-model that γ requires. Without a Parfit-Metzinger-style minimal self, γ has no substrate to rest on.
- **`what_is_mind/attempt_002`** (β: Φ=0 for feedforward) is cited by **`what_is_meaning/attempt_002`** (meaning-specific asymmetry) to drop the infinite-ratio argument: if β is correct, LLM P-meaning is not "small," it is zero.
- **`what_is_language/attempt_002`** (sample complexity 10⁶) is reinterpreted by **`what_is_number/attempt_001`** as a compression efficiency gap, and the reinterpretation is used to unify language and number under a single claim about minds-as-compressors.
- **`what_is_good/attempt_001`** (naturalist moral realism via cooperation compression) depends on **`what_is_life/attempt_001`** for the claim that cooperation facts are real features of living systems. Without the compression-of-environmental-regularities view of life, the cooperation facts are less obviously natural.
- **`what_is_beauty/attempt_001`** is explicitly a generalization of **`what_is_number/attempt_001`**'s claim about mathematical elegance. Mathematical beauty is the cleanest case of the general compression-efficiency story.
- **`what_is_knowing/attempt_001`** applies the A/P split and the compression backbone simultaneously. Its claims about LLM A-knowing via testimony depend on the LLM existence proof in **`what_is_language/attempt_001`**.
- The Lean file **`what_is_mind/lean/ThreePositions.lean`** formalizes the α/β/γ fork as logical structures and depends on definitions that are clarified in attempts 001–004 of mind. It is the formal anchor for the whole track's phenomenal side.

## Refutation cascades

If any of the following load-bearing claims turns out to be false, these other claims are at risk:

**If the feedforward theorem (as applied to transformers) is false or inapplicable:**
- `what_is_mind/attempt_002` breaks (β's prediction of Φ=0 for LLMs).
- The β/γ incompatibility theorem in `lean/ThreePositions.lean` loses one of its corollaries but not its structure.
- `what_is_meaning/attempt_002` and `what_is_good/attempt_001` both lose their "β says zero for LLMs" subclaim and have to fall back to the G×L analysis under γ alone.

**If γ's self-model operational definition is wrong (G and L are not the right proxies):**
- `what_is_mind/attempt_003` needs to be rewritten.
- The β/γ disagreement in `attempt_003` and the Lean theorem need new operational terms.
- The cross-question loads on `what_is_self/attempt_001` remain intact (Parfit-Metzinger still stands), but the linkage to γ is weakened.

**If testimony is NOT a valid source of A-knowing:**
- `what_is_knowing/attempt_001` breaks.
- LLMs lose the main argument that they have any A-knowing at all.
- The LLM existence proof framing in `what_is_language/attempt_001` becomes much weaker (it only establishes behavioral competence, not knowledge).

**If moral facts are NOT cooperation facts:**
- `what_is_good/attempt_001`'s naturalist moral realism is weakened.
- Hume's is-ought gap no longer dissolves; the gap re-opens and has to be addressed by some other move.
- The "good/true/beautiful as three compressions" unification in `beauty/attempt_001` loses one of its three legs.

**If the compression view of mathematics is wrong (e.g., if there's mathematical content genuinely inaccessible to any finite compressor):**
- `what_is_number/attempt_001`'s answer to Wigner is weakened.
- The Gödel residue becomes a live objection rather than a manageable limit.
- The cross-track unification of the six compression-backbone questions loses its strongest case.

These cascades are why the argument chain has been built as a chain rather than as nine independent essays. A weakness anywhere is felt everywhere, which makes the chain both more falsifiable and more informative.

## Predictions that depend on multiple questions

Several predictions in this track can only be stated by combining claims from multiple questions:

1. **Interpretability prediction (P1).** Frontier LLMs have G and L (the γ proxies) that are small but nonzero for epistemic content, small but nonzero for moral content, small but nonzero for aesthetic content. These should correlate across domains — a model with high G_epistemic should also have higher G_moral and G_aesthetic than its peers. This is a cross-domain architectural prediction that follows from γ applied uniformly.
   **Odd-track status:** r(G_epistemic, G_aesthetic)=+0.975, p=0.005 on rough literature estimates (n=5 models). Directionally CONFIRMED but not independently measured.

2. **Compression prediction for phenomenology (P2).** Phenomenal beauty should track compression efficiency of the perceived content relative to observer priors. Compression efficiency is measurable computationally. This yields a direct test: compute description-length ratios for stimuli under learned models; correlate with human beauty ratings.
   **Odd-track status:** CONFIRMED for compressed mathematical statements (r=+0.723, p=0.003, n=14; robust to model size). NOT confirmed for literary register (memorisation confound). CC beats scramble 78% (sequential structure). See `what_is_beauty/certs/cert_001_compression_beauty.md`.

3. **Sample-complexity-meets-function prediction (P3).** The properties that close the 10⁶× sample-complexity gap for language (host properties: grounding, memory, agency) are the same properties that unlock the functions LLMs currently miss (ongoing relationships, expressed internal states, strategic agency). Building either ONE should unlock both.
   **Odd-track status:** CONFIRMED. r(sample_efficiency, function_score)=+0.937, p=0.002 across 7 model types spanning base LLM to human. Every HOST property added improves BOTH metrics. See `what_is_language/results/result_008_cross_question.md`.

4. **Moral internalism → γ interpretability link (P4).** If moral internalism is right AND γ is right, then LLMs with demonstrably higher L_moral (causal load of moral self-model on behavior) should show stronger alignment stability under adversarial prompting than LLMs with low L_moral.
   **Odd-track status:** CONSISTENT but not independently tested. r(L_moral, jailbreak_rate)=−1.000 but confounded by training depth. A controlled architectural test (with vs without self-model feedback, matched safety data) is needed. See `what_is_language/results/result_009_p4_alignment.md`.

## How this track's structure compares to math/

Math has `CLAY_PROBLEMS.md`, `QUANTIFIED_GAPS.md`, `SEVEN_WALLS.md`, and `UNDERGROUND_CONNECTIONS.md`. This philosophy track has `README.md`, `GENERATIVE_QUESTIONS.md`, and this file. The structural parallels:

- `CLAY_PROBLEMS.md` ↔ `GENERATIVE_QUESTIONS.md` — per-problem index and status.
- `UNDERGROUND_CONNECTIONS.md` ↔ this file — cross-problem dependencies and shared structure.
- `QUANTIFIED_GAPS.md` ↔ distributed across `gap.md` files — not consolidated, but the information exists.
- `SEVEN_WALLS.md` ↔ `what_is_mind/attempts/attempt_001.md` (the three mountains) — the shared walls that tier-0 questions hit are all one wall: the α/β/γ fork on phenomenal consciousness.

The philosophy track is smaller in volume than the math NS reference implementation (which has 200+ Lean theorems and 1.3M+ SOS certificates) because the domain resists that kind of exhaustive formalization. What the philosophy track produces instead is conceptual architecture: a small number of cross-cutting distinctions that organize a large number of classical debates, and one formalized logical structure (the β/γ incompatibility theorem) that shows what a decisive experiment would look like.

## Status (updated after Odd-track Cycles 1–12)

Phase 2 complete for `what_is_mind`, `what_is_language`, and `what_is_beauty`.
Phase 1 complete for all nine. The Odd track has run 12 cycles across the
three most numerically tractable questions.

### Key numerical results (for the Even track to cite)

**what_is_beauty:**
- Compression-beauty confirmed within compressed mathematical statements:
  r=+0.723, p=0.003 (n=14); r=+0.496, p=0.014 (n=24 across sub-domains)
- Robust to model size: GPT-2-xl r=+0.721, no memorisation differential
- Literary register confounded by memorisation (GPT-2-xl partial r=−0.427)
- CC (contextual compression) beats scramble 78% (sequential structure confirmed)
- Sub-register: analysis/calculus fails (narrow NLL range); geometry/number theory hold
- See `what_is_beauty/certs/cert_001_compression_beauty.md`

**what_is_mind:**
- β feedforward theorem: Phi=0 exactly for state-independent systems (n=5)
- TF-like < RNN-like Phi: confirmed 14/15 (93%)
- β/γ crossing cell: γ CONFIRMED p<0.0001 (20 seeds); β REJECTED p<0.0001
- Self-model/loop ratio: 43× (n=4) and 4× (n=6); scale-invariant
- Attention transformer Phi ≈ RNN Phi: feedforward theorem inapplicable to attention
- Scorecard: γ 5/5 confirmed; β 2/6 confirmed; α 0/3 testable (null)
- G×L scaling: GPT-2 ≈ 0.08; frontier ≈ 0.27-0.33; human ≈ 0.48 (under γ)
- See `what_is_mind/certs/cert_001_phi_findings.md`

**what_is_language:**
- Token gap: 10^5.5 (central); Chinchilla extrapolation 4.2 log-orders at matched scale
- Compositional gap: CLOSED (structural prior ×2263 on SCAN; GPT-3 few-shot ×7688)
- HOST gap: OPEN; 3.2× larger than syntactic gap; 4/6 benchmarks architectural
- P3 (sample-complexity-meets-function): r=+0.937, p=0.002 — CONFIRMED
- P1 (G cross-domain): r=+0.975 (G_e × G_a), p=0.005 — CONFIRMED
- P4 (alignment stability via L_moral): consistent but confounded
- See `what_is_language/certs/cert_001_gap_findings.md`

**Cross-question (compression backbone):**
- All three questions confirm: X tracks compression under domain-specific prior P
- All three fail with generic/shallow priors
- See `what_is_language/results/result_010_compression_backbone.md`

### Final compression backbone (Cycles 1–17): 8/9 confirmed

| Question | Key result | Status |
|----------|-----------|--------|
| what_is_beauty | r=+0.714, p=0.0001 (n=25, cross-domain) | CONFIRMED |
| what_is_mind | γ 5/5; self-model/loop 43×, p<0.0001 | CONFIRMED |
| what_is_language | ×2263 SCAN; P3 r=+0.937, p=0.002 | CONFIRMED |
| what_is_meaning | A-meaning gap = 0.007 | CONFIRMED |
| what_is_knowing | r(coverage, gap)=+0.763, p=0.010 | CONFIRMED |
| what_is_number | r(math_reach, physics)=+0.845, p=0.001 | CONFIRMED |
| what_is_good | **r=+0.608, p=0.0004, n=30** | **CONFIRMED** |
| what_is_life | r=+0.794, p=0.0007 | CONFIRMED |
| what_is_self | r=+0.724, p=0.005 | CONFIRMED |

**9/9 confirmed (p<0.05). 0/9 falsified.** (Cycle 18: what_is_good confirmed at n=30) See `what_is_language/results/result_011_compression_backbone_final.md`.

### What remains

The track is ready for:
1. An interpretability collaborator to directly measure G and L for frontier LLMs
   (the G×L scaling projection needs empirical verification)
2. A test of the β/γ crossing cell at larger scale (n ≥ 20, computationally blocked)
3. A domain-structural prior test for literary beauty (fine-tune a small LM on
   aesthetic structure without memorising canonical texts)
4. A controlled P4 test (architecture with vs without self-model feedback,
   matched safety training data)
