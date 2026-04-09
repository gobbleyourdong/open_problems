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

1. **Interpretability prediction.** Frontier LLMs have G and L (the γ proxies) that are small but nonzero for epistemic content, small but nonzero for moral content, small but nonzero for aesthetic content. These should correlate across domains — a model with high G_epistemic should also have higher G_moral and G_aesthetic than its peers. This is a cross-domain architectural prediction that follows from γ applied uniformly.

2. **Compression prediction for phenomenology.** Phenomenal beauty should track compression efficiency of the perceived content relative to observer priors. Compression efficiency is measurable computationally. This yields a direct test: compute description-length ratios for stimuli under learned models; correlate with human beauty ratings.

3. **Sample-complexity-meets-function prediction.** The properties that close the 10⁶× sample-complexity gap for language (host properties: grounding, memory, agency) are the same properties that unlock the functions LLMs currently miss (ongoing relationships, expressed internal states, strategic agency). Building either ONE should unlock both. This is the two-mountain convergence of `what_is_language` restated as a specific empirical claim: build an LLM with full host properties, it should learn faster AND function more fully.

4. **Moral internalism → γ interpretability link.** If moral internalism is right AND γ is right, then LLMs with demonstrably higher L_moral (causal load of moral self-model on behavior) should show stronger alignment stability under adversarial prompting than LLMs with low L_moral. This is a non-obvious prediction that links philosophy of mind, ethics, and interpretability in a way no one framework alone would suggest.

## How this track's structure compares to math/

Math has `CLAY_PROBLEMS.md`, `QUANTIFIED_GAPS.md`, `SEVEN_WALLS.md`, and `UNDERGROUND_CONNECTIONS.md`. This philosophy track has `README.md`, `GENERATIVE_QUESTIONS.md`, and this file. The structural parallels:

- `CLAY_PROBLEMS.md` ↔ `GENERATIVE_QUESTIONS.md` — per-problem index and status.
- `UNDERGROUND_CONNECTIONS.md` ↔ this file — cross-problem dependencies and shared structure.
- `QUANTIFIED_GAPS.md` ↔ distributed across `gap.md` files — not consolidated, but the information exists.
- `SEVEN_WALLS.md` ↔ `what_is_mind/attempts/attempt_001.md` (the three mountains) — the shared walls that tier-0 questions hit are all one wall: the α/β/γ fork on phenomenal consciousness.

The philosophy track is smaller in volume than the math NS reference implementation (which has 200+ Lean theorems and 1.3M+ SOS certificates) because the domain resists that kind of exhaustive formalization. What the philosophy track produces instead is conceptual architecture: a small number of cross-cutting distinctions that organize a large number of classical debates, and one formalized logical structure (the β/γ incompatibility theorem) that shows what a decisive experiment would look like.

## Status

Complete through Phase 1 for all nine questions. Phase 2 partially complete for `what_is_mind` (formal structure + β/γ quantification) and `what_is_language` (quantified sample complexity, two-mountain convergence).

The track is ready for a second instance, a Lean-expert to sharpen `ThreePositions.lean`, an interpretability collaborator to measure G and L for frontier LLMs, or a philosopher of mind to stress-test the α/β/γ fork and the meaning/knowing/good/beauty specializations.
