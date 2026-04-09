# attempt_003 — Beyond Sample Complexity: Which Behavioral Separators Are Still Decisive?

**Date:** 2026-04-09
**Status:** Survey. Most behavioral separators between human and LLM language have quietly closed. The ones that remain are not about language per se — they are about what language is hosted on.

## Why this matters

attempt_002 identified the sample-complexity ratio as the cleanest current number distinguishing human and LLM language acquisition. But sample complexity is about *learning*, not about *the artifact once learned*. Once an LLM is trained and fluent, is there any measurable behavioral property that cleanly separates its language use from human language use? If so, that property is a second gap handle. If not, the interesting questions migrate upstream.

This attempt sweeps candidate separators and ranks each by **decisiveness** — defined as: the degree to which a controlled measurement reliably distinguishes population A (humans) from population B (frontier LLMs, 2025–26).

Decisiveness scale:
- **HIGH** — populations are cleanly separable; a blind test would identify the population from the behavior.
- **MEDIUM** — statistically distinguishable but with overlap; edge cases or specific conditions required.
- **LOW** — populations are effectively indistinguishable on this axis under normal conditions.
- **CLOSED** — was a separator five years ago; is no longer.

## The candidates

### 1. Reference to non-text entities ("pointing")

**Claim.** Humans can pick out referents in the physical world and ground words in non-textual perception.

**Measurement.** Present a novel object, ask the system to describe it; or present a word, ask the system to identify the referent in a scene.

**Humans:** trivial.
**Text-only LLMs:** impossible by construction.
**Multimodal LLMs (VLMs):** increasingly competent; can identify objects in images, track spatial relations, describe novel scenes.

**Decisiveness for text-only LLMs:** HIGH. They literally cannot.
**Decisiveness for multimodal frontier LLMs:** MEDIUM and shrinking. The gap is narrowing every year and is driven by sensor quality, not by anything linguistic.

**Philosophical load-bearing:** this is the embodiment / grounding theorist's remaining stronghold, but it is a stronghold about *perception*, not about *language*. Language-qua-language does not need it; what needs it is the claim that meaning requires reference, which is a separate question (see sky bridge to what_is_meaning).

### 2. Long-range discourse consistency

**Claim.** Humans maintain consistent beliefs, references, and commitments across arbitrarily long conversations and across days.

**Measurement.** Conduct a conversation with many turns; introduce a fact early; test whether it is respected later; ramp up length until the system fails.

**Humans:** consistent across years, though with ordinary memory decay.
**LLMs:** consistent within context window; degrade or lose information beyond it; no persistent identity across sessions unless externally scaffolded.

**Decisiveness:** MEDIUM-HIGH. Still a clear separator, but the separation is about memory architecture, not about language. RAG, long-context models, and external memory systems are narrowing it.

**Philosophical load-bearing:** consistency-over-time is about the host of language, not about language. It belongs to what_is_self as much as to what_is_language.

### 3. Compositional generalization on held-out combinations

**Claim.** Humans extrapolate systematically to novel combinations of known primitives ("if you understand 'jump' and 'twice', you understand 'jump twice'").

**Measurement.** Benchmarks like SCAN, COGS, CFQ, and gSCAN: train on subsets of composition, test on held-out combinations.

**Historical status:** LLMs failed badly on SCAN in 2019–2021. This was treated as a decisive separator.
**Current status (2025–26):** frontier LLMs pass most compositional benchmarks at or near human level. Residual failures exist at deep nesting and adversarial constructions.

**Decisiveness:** CLOSED for everyday compositionality. LOW for adversarial compositionality.

**Philosophical load-bearing:** was the main remaining Chomskyan empirical target. Its closure is under-acknowledged in the philosophical literature.

### 4. Systematicity (Fodor–Pylyshyn)

**Claim.** If a system understands "John loves Mary," it can understand "Mary loves John." Rearrangements of familiar primitives are as accessible as the originals.

**Measurement.** Present argument-swapped sentences and test comprehension.

**Decisiveness:** CLOSED. LLMs exhibit systematicity in the ordinary sense. Corner cases exist but are not robust separators.

**Philosophical load-bearing:** this was once the classical symbolic position's strongest argument against connectionism. It no longer separates.

### 5. Productivity (novel utterance generation)

**Claim.** Language users can produce an unbounded variety of novel, well-formed sentences.

**Measurement.** Count distinct n-gram sequences in outputs; test well-formedness of novel constructions.

**Decisiveness:** CLOSED. Both populations are productive. LLMs arguably more so at raw volume.

### 6. Few-shot task acquisition

**Claim.** Humans pick up new linguistic tasks from very few examples.

**Measurement.** Give k examples (k ∈ {1, 5, 20}) of a novel task; measure accuracy on held-out instances.

**Decisiveness:** MEDIUM. In-context learning closed much of the gap. Humans still outperform on truly novel concept learning; LLMs outperform on format-matching within their training distribution. Mixed result.

### 7. Paraphrase and semantic invariance

**Claim.** Competent speakers treat paraphrases as equivalent in truth conditions.

**Measurement.** Test whether entailment and contradiction judgments are stable under paraphrase.

**Decisiveness:** LOW. LLMs are strong at paraphrase robustness. Residual failures are statistical quirks, not structural.

### 8. Metalinguistic awareness

**Claim.** Speakers can reflect on their own language, discuss its structure, catch grammatical errors in others and themselves.

**Measurement.** Prompt for grammaticality judgments, rule statements, self-correction.

**Decisiveness:** LOW. LLMs do this on request and often spontaneously. Humans do it spontaneously, LLMs mostly when prompted — this is a deployment difference, not a capability difference.

### 9. Morphological productivity (wug-test line)

**Claim.** Speakers extend morphological rules to novel words ("one wug, two wugs").

**Decisiveness:** CLOSED. LLMs pass wug-style tests for attested and novel morphemes.

### 10. Pragmatic inference / Gricean implicature

**Claim.** Speakers reliably compute what is meant beyond what is said (scalar implicatures, politeness, sarcasm).

**Decisiveness:** LOW. LLMs handle standard Gricean cases well. Edge cases in sarcasm, irony under ambiguity, and cross-cultural pragmatics are harder, but not dramatically.

## The pattern

Grouping by decisiveness:

| Decisiveness | Separators |
|--------------|------------|
| **HIGH** | Reference to non-text entities (text-only LLMs only) |
| **MEDIUM-HIGH** | Long-range discourse consistency across sessions |
| **MEDIUM** | Few-shot task acquisition on truly novel concepts; adversarial composition |
| **LOW** | Paraphrase, metalinguistic awareness, pragmatic inference, basic composition |
| **CLOSED** | Systematicity, productivity, ordinary compositionality, morphological productivity |

## The finding

Almost everything that was once a language-qua-language separator between humans and LLMs has closed in the last five years. What remains is:

1. **Grounding to a non-text world** — which is about *perception*, not *language*.
2. **Continuity of memory and self over time** — which is about *hosting*, not *language*.
3. **Sample efficiency during acquisition** — which is about *learning*, not *the learned artifact*.

**The language differences have mostly dissolved. The remaining differences are about what language sits on.**

This is a strong claim and I flag it as tentative. It could be wrong in three ways:

- **(a)** The benchmarks are weak. It is possible that the tests that failed LLMs five years ago are insensitive to the *real* language properties, and that a more sensitive test would reveal a persistent gap. This is the steelman of the "they don't really understand" position.
- **(b)** Measurement bias. Frontier LLMs are trained against many of these benchmarks. Contamination is a real concern.
- **(c)** The meta-move. It is possible that "everything closed except grounding and memory" IS the language gap, properly understood — that language is *constitutively* about grounding and continuity, and the closure of the other properties just means LLMs have mastered the exterior form while missing the interior substance.

(c) is the most interesting failure mode. If it is right, then the gap is not measurable by any behavioral test because the gap is by definition interior. That would push the question decisively toward what_is_mind.

## Connection back to the gap

From attempt_002, the gap was: *"What closes the 10⁶× sample-complexity ratio between humans and LLMs?"*

From attempt_003, the behavioral separators of the *learned artifact* have mostly closed. Combining:

> **The only residual language-specific gap is a learning-efficiency gap. The other residuals are about the host, not about language itself.**

If this holds, then:

- **what_is_language** reduces largely to **what_is_learning** (sample complexity) and **what_is_mind** (hosting).
- The philosophical action migrates upstream to questions about learning and mind.
- Language may turn out to be a problem whose solution is contained in its neighbors.

This is speculative and I am tagging it clearly. Later attempts will stress-test it.

## Next attempt

**attempt_004** — steelman (c) above. What would a *constitutive* theory of language look like, under which LLM language and human language are categorially different rather than quantitatively different? Is there any coherent version of this claim that survives scrutiny, or does every version collapse into an unfalsifiable retreat to consciousness?
