# attempt_001 — The Third Bifurcation: Noise vs Compressibility

**Date:** 2026-04-09
**Status:** Foundation. Argues that the anti-problem in `PROBLEM.md` — noise has high Shannon entropy but zero usefulness — is the third instance of the same structural bifurcation seen in philosophy/what_is_meaning and philosophy/what_is_mind. "Information" bundles two genuinely distinct properties, and separating them resolves the multiple-formalizations problem while also bridging to the compression-as-substrate theme.

## Cross-reference

This attempt opens the physics track as a deliberate extension of the philosophy track's argument chain. Specifically:

- **philosophy/what_is_meaning/attempt_001** — the A/P bifurcation as a general tool.
- **philosophy/what_is_number/attempt_001** — compression as the substrate for mathematics and for tier-0 questions in general.
- **philosophy/GENERATIVE_QUESTIONS.md** — the compression backbone across six of the nine philosophy questions.
- **philosophy/UNDERGROUND_CONNECTIONS.md** — the cross-question load graph.

The hypothesis tested here: the same bifurcation-plus-compression architecture that clarified meaning, knowing, goodness, beauty, and life also clarifies the information question. If this is right, the physics/ track inherits the philosophy/ argument chain directly, and "information" joins "meaning" and "consciousness" as a concept that was doing two jobs until the existence proofs forced a split.

## The anti-problem, stated sharply

From PROBLEM.md:

> *Is random noise the absence of information or maximal information? The paradox (noise has high Shannon entropy but zero usefulness) reveals that "information" is doing two different jobs.*

The paradox is real and it is the forcing function for this attempt. Random noise has maximum Shannon entropy (by definition — uniform distribution maximizes entropy over any finite alphabet). But random noise has zero compressibility: its shortest description is itself. And it has zero usefulness: no pattern to learn, no regularity to extract, no prediction to support.

So "more information" in the Shannon sense ≠ "more information" in any usefulness or compressibility sense. The word is doing two jobs.

## The bifurcation

Propose:

- **S-information (Shannon-information)** — the capacity of a channel to transmit distinguishable states. Measured by Shannon entropy H(X) = -Σ p(x) log p(x). This is a *capacity* concept: it counts how many bits can pass, not whether those bits mean anything. Random noise has maximal S-information because every state is equally probable and therefore equally distinguishable.

- **K-information (Kolmogorov-information, or compressibility)** — the degree to which a string has a description shorter than itself. Measured by Kolmogorov complexity K(X) (or its computable approximations). This is a *regularity* concept: it counts how much structure the content has. Random noise has minimal K-information because it has no short description.

These are both called "information" and they are orthogonal.

| Content | Shannon entropy | Kolmogorov complexity | Compressibility |
|---------|----------------|---|---|
| Random noise | MAX | MAX | ZERO |
| A single repeated character | ZERO | MIN | MAX |
| A compressible structured string | HIGH | MEDIUM | HIGH |
| A natural-language paragraph | HIGH | MEDIUM | HIGH |
| A Chaitin constant | HIGH | MAX | ZERO |

The paradox dissolves. Noise is S-rich and K-poor. A poem is S-rich and K-moderate. A blank page is S-poor. These are three genuinely different conditions and they were being conflated.

## Why the bifurcation has the same shape as A/P

The bifurcations encountered so far in the philosophy track:

- **Meaning:** A-meaning (functional use) vs P-meaning (felt grasp).
- **Knowing:** A-knowing (functional competence) vs P-knowing (felt grasp).
- **Mind:** Access-consciousness vs phenomenal-consciousness.
- **Information (this attempt):** S-information (channel capacity) vs K-information (compressibility / structure).

The information bifurcation is structurally the same even though it is not phenomenological. In every case, a word was doing a functional job (capacity, use, access) AND a richer job (structure, grasp, phenomenology), and the cases where they came apart forced the split.

**The same principle:** there is a functional/capacity side that is operationalizable and well-studied, and there is a structure/grasp side that is harder to pin down but that the working concept was secretly also tracking. When a new existence proof (LLMs, random noise, etc.) comes along and decouples the two, the split becomes unavoidable.

## How each classical ontology sits relative to the bifurcation

### Shannon (syntactic)

**Is a theory of S-information.** Shannon explicitly disclaimed any attempt to capture meaning or structure; his 1948 paper says the "semantic aspects of communication are irrelevant to the engineering problem." The theory is about channel capacity and coding bounds. Its success is exactly the success of a clean A-side theory.

### Kolmogorov (algorithmic)

**Is a theory of K-information.** Kolmogorov complexity measures how much structure a string has by asking for its shortest generating program. It directly captures the compressibility/structure side that Shannon disclaimed.

### Physical (Landauer)

**Applies to both sides but differently.** Landauer's principle (erasing one bit costs kT ln 2 of heat) talks about S-information in the sense that each erasable bit is a channel state. But the physical significance of information-erasure depends on whether the bit is *meaningful* (part of a structured computation) or *random* (unused channel capacity). For random bits, erasure is just noise dissipation. For structured bits, erasure discards compressible content. The Landauer bound applies uniformly, but its consequences differ.

### Fisher information

**Is an A-side refinement.** Fisher information measures how much a probability distribution's likelihood changes with a parameter — it's a statistical-estimation quantity, closely related to Shannon but tailored to parametric inference. Still capacity/distinguishability in character.

### Semantic information (Dretske, Floridi)

**Attempts to capture the K-side plus aboutness.** The insight that "bits alone aren't information" is exactly the observation that S-information alone is not enough. Semantic theories try to add a reference relation to fix this. Under the bifurcation, they are attempting to capture K-information plus an additional aboutness property — similar to how P-meaning theories try to capture A-meaning plus felt grasp.

### It-from-bit (Wheeler)

**Is an ontological commitment to S-information as the substrate of reality.** Wheeler's claim is that reality is constituted by bits, with physical objects being manifestations of information-theoretic structure. Under the bifurcation, it is a bet that S-information is the fundamental furniture. The compression view suggests this is almost right but off: what is fundamental is not channel capacity but regularity, and regularity is K-information.

## The compression view, unified

From the philosophy track:

> Minds are compressors. Mathematics is compression of structural regularities. Language is compression of social regularities. Life is compression of environmental regularities. Beauty is high compression efficiency. Knowing is compressed-model generalization. Good is compressed cooperation dynamics.

Applied here:

> **Information in the substantive sense — the sense that matters for meaning, knowledge, and structure — is K-information. Information in the engineering sense is S-information. Reality's "information content" in the cosmological sense (holographic bound, black hole entropy) is S-information about physical states. The K-content of a region is the compressibility of that state, which depends on the laws that govern it.**

This dissolves several apparent puzzles:

1. **"Information is physical" (Landauer, Bennett)** — physical when it is S-information, in the sense that channel capacity has thermodynamic consequences. Not necessarily physical in the K sense, because K-content is a description-relative property.
2. **"It from bit" (Wheeler)** — is half right. Reality is made of structure, and structure is captured by K-information. S-information is the measure of how much state space is available; K-information is the measure of how much of that state space has regularity.
3. **Holographic bound** — bounds S-information in a region (number of distinguishable states). Does not bound K-information, which depends on what structure those states actually have.
4. **Black hole entropy** — measures S-information across the event horizon. Tells us about state space dimensionality, not about compressibility of actual contents.

## Bridges to the philosophy track

- **what_is_meaning** — A-meaning is the functional use of compressible content. Meaning requires content that has K-information, not just S-information. "Bits alone aren't meaning" is the meaning version of "bits alone aren't K-information."
- **what_is_number** — mathematics is K-information about structural patterns, externalized and culturally transmitted. The unreasonable effectiveness of mathematics is about K-information generalization across regularity classes.
- **what_is_life** — life is a process that accumulates K-information about its environment and stabilizes it against entropy. The "information-based" theories of life (Walker, Davies) are K-information theories.
- **what_is_knowing** — knowing is having K-information about a target domain. A-knowing is the compressed-model generalization that K-information enables.
- **what_is_beauty** — beauty is the self-model's phenomenal response to K-information-rich content that was initially presented as S-information-rich.

## Testable claims

The bifurcation yields specific, empirically approachable claims:

1. **Compression benchmarks should track human utility judgments of "informativeness," not Shannon entropy.** A random string and a structured string with the same Shannon entropy should be judged very differently. This is already known in the compression literature but is rarely stated as evidence for the S/K bifurcation.

2. **LLMs are compression processes for K-information over text.** Their training loss approximates cross-entropy, which is Shannon-flavored, but what actually gets stored in the weights is K-content: compressed regularity. LLM sample complexity is the K-information-rate achievable from static text. This is the bridge to `philosophy/what_is_language/attempt_002`.

3. **Physical information theory (black holes, Landauer) should carry over cleanly to S-information and not carry over cleanly to K-information.** Predictions about black hole entropy should be S-predictions. Predictions about the "complexity" of a region's contents are K-predictions and do not follow from S-theorems.

4. **The holographic principle bounds S, not K.** A region has a maximum amount of distinguishable states scaling with boundary area. The K-content of those states is a separate question; no general bound on K is implied.

## The anti-problem, resolved

From PROBLEM.md:

> *What would uninformation look like? Is random noise the absence of information or maximal information?*

**Answer under the bifurcation.** Noise is maximal S-information and minimal K-information. Whether you call it "maximal" or "no" information depends on which side of the bifurcation you care about. Both readings are right once the split is explicit.

For most intuitive purposes (learning, understanding, usefulness), noise is "no information" because it has zero K-content. For engineering purposes (channel utilization, state-counting), noise is "maximal information" because it saturates the channel.

## The gap

The gap for the information question, after this attempt:

> **The multiple-formalizations problem is resolved by the S/K bifurcation. S-information is Shannon-like capacity; K-information is Kolmogorov-like structure. The remaining open question is: (a) what is the exact relationship between K-information and the compression-backbone cross-cutting theme from philosophy, and (b) what physical quantities bound K-information in a region?**

Both are tractable programs. (a) is philosophical synthesis already largely done. (b) is an open problem in theoretical physics with partial results (computational complexity bounds, circuit lower bounds, thermodynamic arguments about reversible computation).

## What this attempt closes

- The S/K bifurcation, stated sharply.
- The six ontologies from PROBLEM.md redistributed across the bifurcation, with each shown to be a theory of one side.
- The anti-problem resolved.
- The bridge to the philosophy track's compression backbone made explicit.

## What remains

- Physical bounds on K-information (holographic, thermodynamic, computational).
- The relationship between Wheeler's "it from bit" and the compression substrate — specifically, whether Wheeler was closer to an S-ontology or a K-ontology, and whether either is correct.
- Cross-track work with the remaining physics questions (reality, time, nothing, change, computation) that should now follow the same pattern: identify bifurcations, apply compression, locate the residue.

## Status

Phase 1. This is the first attempt in the physics track; further attempts should test whether the pattern established here (bifurcation + compression + load on the mind fork for phenomenal residue) generalizes to reality, time, computation, change, and nothing.
