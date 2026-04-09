# attempt_002 — The Gödel Residue and the Horizon of Finite Compressors

**Date:** 2026-04-09
**Status:** Follow-up to attempt_001, delivering the promised treatment of Gödel incompleteness under the compression view. Argues that incompleteness is not a flaw in the compression account of mathematics — it IS the compression account, restated at the limit. Each finite compressor has a horizon of unreached truths; no specific truth is eternally inaccessible, but the totality of truths is never captured by any finite compressor. Chaitin's constant gives this a specific number for any specific compressor.

## Cross-reference

- **what_is_number/attempt_001** — introduced mathematics as compression of structural regularities; promised this follow-up.
- **what_is_number/gap.md** — states the Gödel residue as the main remaining question.
- **physics/what_is_computation/attempt_001** — computation as K-manipulation; the computation-theoretic form of Gödel is stated there.
- **philosophy/what_is_knowing/attempt_001** — A-knowing as compressed-model generalization; this attempt's claims about finite-compressor horizons bear on what it means for a mind to "know everything" about a domain.

## The question

attempt_001 framed mathematics as the cultural evolution of maximally compressed descriptions of regularity classes. It ended on a residue: does Gödel's first incompleteness theorem refute, limit, or complete the compression view? Specifically — is there mathematical content that is in principle inaccessible to any finite compression process, or does Gödel just describe the ordinary limits of finite compressors without making any compressor unable to reach any specific truth?

## Gödel, restated in compression language

Gödel's first incompleteness theorem says: any consistent formal system containing Peano arithmetic has true statements it cannot prove.

Under the compression view:

- A **formal system** is a finite compressor: its axioms and rules form a finite program whose outputs are the theorems.
- The **set of arithmetic truths** is computably enumerable (you can list provable statements by running the proof system) but not decidable (you cannot in general tell whether a given statement is true).
- Therefore, **no finite compressor captures all of arithmetic truth in a single consistent specification.** Every finite compressor enumerates a proper subset of the truths.

This is the compression-view form of Gödel. It is not news to anyone familiar with the theorems, but it forces a specific framing: **incompleteness is a property of finite compressors trying to cover a computably enumerable but undecidable set.** It is not a property of any specific mathematical content.

## Two questions it is easy to confuse

When people talk about Gödelian limits on knowledge or cognition, they often conflate two distinct questions:

**Q1.** Is there mathematical content that *no possible finite compressor can ever capture*?

**Q2.** Does *every specific finite compressor* have some content it cannot capture?

The answers are very different.

**Q2: Yes.** This is Gödel's theorem as usually stated. Every consistent finite system rich enough to express arithmetic has true statements it cannot prove. The Gödel sentence for system S is true but not provable in S.

**Q1: No (in the relevant sense).** For any specific true arithmetic statement X, there exists a finite compressor that captures X — namely, the system S + X (adding X as an axiom). If S was consistent and X is true, then S + X is also consistent (under reasonable conditions), and X is trivially provable in S + X. The Gödel sentence for S is not eternally inaccessible; it is inaccessible only *within* S. Move to S' = S + GödelSentence(S) and the sentence is now a theorem. (S' has its own Gödel sentence, and so on.)

**The compression view predicts this pattern exactly.** Each finite compressor covers a region of truth-space. Each extension covers a larger region. No single finite compressor covers the whole space. But the union of all possible finite extensions covers every specific truth, because every specific truth can be made the next axiom of some finite extension.

## The horizon metaphor

A useful way to think about this: every finite compressor has a **horizon** of truths it can reach. Inside the horizon, truths are provable; outside, they are not. The horizon is not a wall; it is the boundary of current coverage.

Extending the compressor (adding axioms, combining systems, learning new concepts) moves the horizon outward. Each extension captures new truths, including some that were beyond the previous horizon. This is what mathematical progress looks like: horizon-expansion through successive compressor extensions.

**Important point:** no single extension expands the horizon to cover everything. The horizon is always finite. The set of unreached truths is always infinite. But for any specific unreached truth, there is some extension that reaches it. Gödel tells us we can never be *done*; it does not tell us we are stuck in any specific place.

## Chaitin's constant — the gap as a number

Chaitin's halting probability Ω is a specific real number defined as the probability that a randomly generated program halts. Each bit of Ω encodes information about the halting status of specific programs.

**Chaitin's theorem (informal):** for any consistent formal system rich enough to express arithmetic (ZFC, for instance), only finitely many bits of Ω can be proved to have their actual values from within the system. The remaining bits are undecidable in the system.

For ZFC, the number of bits of Ω that ZFC can prove is small — typically cited as "about 10,000 bits," though the exact number depends on how you encode the system. Call this bound **B(ZFC) ≈ 10⁴**.

Now the systematic approach gets its number:

> **Under the compression view, B(S) is the specific quantitative horizon of a specific compressor S. It is finite. It can be computed (or at least bounded) for any given S. It represents the fraction of a maximally incompressible "master key" (Ω) that S can reach.**

This is the cleanest possible version of the Gödel residue: a specific finite number for each specific formal system. The gap is not ontological; it is a horizon with measurable position.

**Extension:** B(ZFC + LargeCardinalAxiom) > B(ZFC). Large-cardinal axioms move the horizon outward. But B(anything finite) is still finite. The hierarchy of large-cardinal axioms is exactly the hierarchy of horizon extensions, each strictly larger than the last, none of them infinite.

## What this says about mind under the compression view

From `what_is_mind/attempts/attempt_001` and attempt_003: minds are compressors. Under γ, phenomenal consciousness is self-modeled access-consciousness. What does this attempt add?

**Claim.** Minds are finite compressors, therefore they have horizons, therefore they always have unreached truths relative to any compressed domain. No specific truth is permanently inaccessible to any mind; every specific truth could be reached by some extension (learning, tool use, formal training, conceptual refinement). But no mind at any given moment has a completed horizon.

This matches the phenomenology of inquiry. Mathematicians describe their work in precisely these terms: there is always more to know, each result opens a new horizon, the specific truths that resist proof today are sometimes proven tomorrow by a conceptual extension. The description of mathematical discovery as horizon-expansion is not a metaphor on the compression view; it is the mechanism.

**Consequence for the "mathematical intuition" puzzle.** Gödel himself thought mathematical intuition was a faculty that somehow reached beyond any specific formal system. The compression view replies: yes, mathematical intuition reaches beyond any specific *current* formal system, but always into another *specific* system. It does not reach everything; it reaches the next extension. What feels like insight from outside the system is the act of moving the horizon one notch outward by adopting a new axiom or concept.

Under γ, this insight is phenomenally reported as understanding: the self-model represents the new extension as "seeing the truth" because the new compressor integrates the truth into its coverage. The mathematician who feels they "see" that the Gödel sentence of their system is true is correct about the seeing — they have just extended to a compressor that proves it, and the self-model reports the extension as insight.

## Consequence for LLMs

LLMs are finite compressors. Their training produces a specific compressor; their effective horizon is the set of content they can answer correctly within their training distribution. Outside the horizon:

- **Prompting** moves the horizon by providing new information at inference time.
- **Chain of thought** moves the horizon by unfolding compressed reasoning into explicit steps, sometimes reaching content the one-shot output could not.
- **Tool use** moves the horizon by offloading computation to external systems.
- **Retraining** moves the horizon by re-fitting the compressor on new data.

Each of these is a specific compression-extension in the same sense as adding an axiom. LLMs' "limitations" are not eternal — they are horizon-bounded in a way that extensions can move.

**Specific quantitative claim (speculative):** an LLM's horizon is bounded by a B-like quantity that depends on training compute, parameter count, and data composition. A sufficiently extended LLM system (LLM + tools + retrieval + CoT + retraining loops) has a horizon that expands over time, converging on the union of all human-reachable compressors plus whatever extensions the LLM can itself generate. Whether this converges on the full set of arithmetic truths depends on whether the extension process is systematic or ad-hoc. Gödel places no in-principle limit on this convergence; only the finiteness of any particular snapshot does.

## The systematic approach shape

This attempt delivers the systematic approach's favorite kind of result: **an infinite-looking gap becomes a finite number, and the finite number can be bounded for specific systems.**

- The number: B(S) = bits of Chaitin's constant provable in S.
- For ZFC: B(ZFC) ≈ 10⁴ bits.
- For extensions: B(S + extension) > B(S), always finite, always less than ℵ₀.
- The gap was never about any specific truth being inaccessible. The gap is that every finite compressor has a finite horizon, and the set of truths beyond the horizon is infinite.

This is a quantification of incompleteness that the standard Gödel presentation does not make explicit. The bound B(S) reframes "there exist undecidable truths" as "there is a specific horizon position, here is its value."

## Bridges

- **what_is_number/attempt_001** — mathematics as compression. This attempt completes it by giving the Gödel residue a quantitative form.
- **physics/what_is_computation/attempt_001** — Church-Turing and the computable-enumerable-but-undecidable structure of arithmetic. Same phenomenon in computation terms.
- **philosophy/what_is_knowing/attempt_001** — the A-knowing horizon for any finite mind.
- **philosophy/what_is_mind/attempt_001** — minds as compressors; this attempt adds that their horizons are always finite but always extensible.
- **philosophy/what_is_language/attempt_002** — the 10⁶× sample-complexity ratio is a specific B-like quantity: the compression-horizon of LLMs on linguistic regularity classes. Both are about the position of a horizon, measured in different units.
- **math/p_vs_np** — the compression reframing of P vs NP from physics/what_is_computation bears on whether horizon-extension is computationally tractable. If compression-finding is easy (P = NP), horizons expand cheaply; if hard (P ≠ NP), each extension is expensive.

## What this closes

- The Gödel residue is no longer a qualitative worry about the compression view. It is a specific quantitative feature: every finite compressor has a horizon B(S), and B(S) is bounded but extensible.
- The conflation of Q1 (is any content permanently inaccessible) and Q2 (does every compressor have some inaccessible content) is resolved. The answer is No to Q1 and Yes to Q2.
- The mathematical-intuition puzzle is reframed as horizon-extension, which is what the phenomenology actually describes.
- LLM "limitations" get a principled framing: they are horizon-bounds, not in-principle walls.

## What remains

- **The specific value of B(ZFC).** The "about 10⁴ bits" figure is the commonly cited estimate but I am not confident in the exact number. A more careful treatment would give tight bounds or point to the authoritative derivation.
- **Tight bounds on B(ZFC + X) for specific large-cardinal axioms X.** This is a technical question in proof theory with partial answers in the literature.
- **Whether the LLM horizon is more like B(ZFC) or like B(LargeCardinalExtension).** An LLM trained on human mathematics inherits the horizon of human formal systems, possibly extended by implicit knowledge in the training distribution. Measuring this would be a real empirical contribution.
- **The relationship between horizon-extension cost and P vs NP.** If finding new axioms that expand the horizon is NP-hard in general, mathematical progress is expensive in a specific, provable way.

## Status

Phase 2 on the specific Gödel question. The compression view now has a formally quantitative handle on incompleteness: horizons, measured by B(S), expandable but always finite. This completes the main residue from what_is_number/gap.md.
