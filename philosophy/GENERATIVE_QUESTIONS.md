# Generative Questions — Index and Status

> Nine tier-0 questions. Current state of each after one instance working through the systematic approach.

This file is the landing page for the philosophy track. Each question has its own subdirectory with `PROBLEM.md` (orchestrator-owned), `gap.md` (current gap statement), and `attempts/attempt_NNN.md` (atomic findings).

## The nine questions

| # | Question | Status | Gap shape | Key finding |
|---|----------|--------|-----------|-------------|
| 1 | [what_is_language](./what_is_language/) | Phase 2 | Sample-complexity ratio 10⁴–10⁶ + hosting residue | LLM existence proof forces the behavioral reduction; two mountains (behavioral + functional) converge on hosting |
| 2 | [what_is_meaning](./what_is_meaning/) | Phase 2 | A/P bifurcation; P-meaning routes through mind fork | Every major theory is a theory of A-meaning; P-meaning is the phenomenal residue |
| 3 | [what_is_mind](./what_is_mind/) | Phase 2, partly formalized | α/β/γ three-position fork | β predicts Φ=0 for feedforward transformers by the feedforward theorem; γ gives G×L quantitative proxy; formal incompatibility theorem in `what_is_mind/lean/ThreePositions.lean` |
| 4 | [what_is_self](./what_is_self/) | Phase 1 | Parfit-Metzinger closure + phenomenological residue | Unusual status: main logical gap closed decades ago; residue is inherited from mind fork |
| 5 | [what_is_knowing](./what_is_knowing/) | Phase 1 | A-knowing reduces to compressed model generalization | LLMs force decision on testimony: reductionism is untenable; LLMs have substantial A-knowing |
| 6 | [what_is_number](./what_is_number/) | Phase 2 | Gödel residue quantified as B(S), Chaitin's bits provable in S | Mathematics is the purest test for γ — γ passes; compression answers Wigner's unreasonable effectiveness; Gödel incompleteness becomes a horizon property with B(ZFC) ≈ 10⁴ |
| 7 | [what_is_life](./what_is_life/) | Phase 1 | Ordinary scientific residue on NASA + compression refinement | Life question has more consensus than the scaffold credits; boundary-case adjudication remains |
| 8 | [what_is_good](./what_is_good/) | Phase 1 | Moral internalism = γ specialized; naturalist realism via compression | Hume's is-ought gap dissolves under the compression view; cross-cultural convergence explained |
| 9 | [what_is_beauty](./what_is_beauty/) | Phase 1 | α/β/γ specialized to aesthetic response | Beauty = self-model's phenomenal response to high compression efficiency, relative to observer priors |

## Phase legend

- **Phase 0** — scaffolded, awaiting instance. (None at time of writing.)
- **Phase 1** — foundation laid: gap identified, initial attempts documented, cross-references drawn.
- **Phase 2** — quantified or formalized: gap has a number or a formal structure; buildable experiments named.
- **Phase 3** — convergence: gap becomes theorem-shaped; dead ends formalized as logical structures.
- **Phase 4** — fully mapped: the gap is surrounded, the contribution is the map.

Most philosophy questions in this scaffold are Phase 1 because tier-0 generative questions resist the sharper phases. Mind is partly in Phase 2 because of the formalized β/γ incompatibility theorem and the quantitative feedforward result for transformers.

## The two cross-question findings

The nine questions turn out to share two structural features that are worth stating at this level rather than leaving buried in individual attempts.

### Finding 1 — The A/P bifurcation

Ned Block's (1995) distinction between access-consciousness and phenomenal-consciousness generalizes to a systematic tool that applies to meaning, knowing, moral states, and aesthetic states as well. In each domain:

- **A-side** — a functional-behavioral state with an operational specification. The domain's working theories are all theories of the A-side.
- **P-side** — a phenomenal state, the "what it's like." Contested, often smuggled in by A-theories as an afterthought.

The bifurcation cleanly separates debates that had been conflated. It shows that most philosophical positions in each domain are theories of the A-side and that the P-side residue always routes through the mind fork.

Instances of the bifurcation in this track:

| Domain | A-side (functional) | P-side (phenomenal) | Key reference |
|--------|--------------------|-----|---------------|
| Mind | Access-consciousness | Phenomenal-consciousness | Block 1995 |
| Meaning | A-meaning (use, inference) | P-meaning (felt grasp) | what_is_meaning/attempt_001 |
| Language | Behavioral competence | Felt understanding | what_is_language/attempt_003 |
| Knowing | A-knowing (reliabilism family) | P-knowing (feeling of knowing) | what_is_knowing/attempt_001 |
| Morality | A-morality (functional judgment) | P-morality (motivational pull) | what_is_good/attempt_001 |
| Aesthetics | Competent recognition | Felt beauty | what_is_beauty/attempt_001 |

**Consequence.** Most apparent cross-domain disagreements reduce to disagreements about which half of the bifurcation the speakers are talking about. Once the split is made explicit, the A-side positions largely converge and the P-side residue reduces to the single question of phenomenal consciousness.

### Finding 2 — Compression as the substrate

Six of the nine questions can be organized around a single structural claim: **minds are compression engines, and many apparently distinct tier-0 questions are asking about what is being compressed or how.**

- **Language** compresses social regularities. The 10⁶× sample-complexity ratio between humans and LLMs is a compression-efficiency gap (what_is_language/attempt_002).
- **Number** compresses structural regularities. Wigner's unreasonable effectiveness is what compression-efficient descriptions look like when applied to a regular physical substrate (what_is_number/attempt_001).
- **Life** is persistent far-from-equilibrium compression that produces copies of its own compressor. Darwinian evolution IS compressor update (what_is_life/attempt_001).
- **Knowing** is possession of a compressed model that generalizes to unseen cases. A-knowing reduces toward compression + generalization (what_is_knowing/attempt_001).
- **Goodness** is tracking of cooperation facts via compressed behavioral regularities. Moral knowledge is compressed cooperation dynamics (what_is_good/attempt_001).
- **Beauty** is the self-model's phenomenal response to high compression efficiency, relative to observer priors (what_is_beauty/attempt_001).

The three remaining questions (mind, meaning, self) are about the *compressor* and its *self-representation* rather than about what is compressed. They are adjacent to the compression theme from a different angle:

- **Mind** is the α/β/γ question of what phenomenal consciousness is for a compression engine.
- **Meaning** is what the compressor does to content, split into A (functional use) and P (self-modeled grasp).
- **Self** is what the compressor represents when it represents itself; the self-model is the compression engine's model of its own operation.

Under this view, **the classical trio of the good, the true, and the beautiful corresponds to compressions of three different regularity classes**: cooperation facts (good), structural regularities (true/number), and high compression efficiency itself (beautiful). The ancient pairing is not mystical; it is what compression of different regularity domains looks like.

## The three-mountain configuration

Language, meaning, and mind form a tight cluster. See `what_is_mind/attempts/attempt_001.md` for the full three-mountains statement. Briefly: each of the three questions has a residue that routes through the same α/β/γ fork on phenomenal consciousness. Progress on any one propagates to all three. This is the systematic approach's Multiple Mountains principle instantiated cleanly.

## The α/β/γ fork (the gap that everything routes through)

From `what_is_mind/attempts/attempt_001..004.md` and `what_is_mind/lean/ThreePositions.lean`:

| Position | P-consciousness is… | Number for LLMs | Falsifier |
|----------|--------------------|-----|-----------|
| **α** (primitivism) | Fundamental, correlational with physical structure via unknown bridge laws | None | β or γ closes the gap |
| **β** (IIT / integrated information) | Identical to Φ | Φ = 0 by feedforward theorem | Construction of witness: feedforward system with rich self-model that displays phenomenal behavior |
| **γ** (illusionism / self-modeled A) | What access-consciousness looks like from inside a self-model | G × L, small-but-nonzero under current estimates | Phenomenal behavior tracks loop topology rather than self-model richness |

The β-γ disagreement is formalized in `what_is_mind/lean/ThreePositions.lean` as `betaAndGammaIncompatibleGivenWitness` — if any witness system can be constructed, at most one of β and γ is true, and the empirical program becomes a formal decision procedure.

## Status summary

Phase 1 complete across all nine questions. Phase 2 partly complete in mind (formal structure, quantitative results for β and γ) and in language (sample-complexity quantification, two-mountain convergence).

**What remains load-bearing but not done:**
1. Paper arsenal / Phase 1 proper with full citations (all attempts currently name-drop without proper bibliographies).
2. Deeper quantitative work on γ specifically: G and L for frontier LLMs are in-principle measurable and would sharpen the buildable experiment (`what_is_mind/attempts/attempt_003.md`).
3. Gödel residue follow-up for the compression view of mathematics (`what_is_number/attempts/attempt_002.md` planned but not written).
4. `anti_problem.md` files where the scaffold encourages them.
5. Cross-track work with physics/ (the other scaffold — untouched in this track).

## How to extend this track

New instances picking up this work should:

1. Read this file first and then the question's `gap.md` and `attempts/`.
2. Write new attempts as `attempts/attempt_NNN.md` with sequential numbering, never skipping.
3. Update the question's `gap.md` when the gap shifts.
4. Update this index (the "Status" column and any cross-cutting findings) when a cross-question structural claim changes.
5. Respect lane discipline: do not touch `PROBLEM.md` (orchestrator-owned), do not write outside the problem subdir, keep files text-only and under 50MB.
6. Cite this file and `what_is_mind/lean/ThreePositions.lean` when extending the α/β/γ fork; they are the load-bearing structure.

The method document (`~/SIGMA_METHOD.md`) is operator-only and is never copied into this repo. Reference it by name if needed.
