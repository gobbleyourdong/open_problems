# attempt_001 — Computation as K-Manipulation, and What Church-Turing Actually Claims

**Date:** 2026-04-09
**Status:** Foundation. Reframes computation as the physical process of K-information manipulation, reads Church-Turing as a compression claim, and argues that the "is the universe a computation" question becomes tractable once the S/K bifurcation from what_is_information is applied. Computation is not the substrate of reality — it is reality's dynamics viewed through the K lens.

## Cross-reference

- **physics/what_is_information/attempt_001** — the S/K bifurcation. This attempt applies it to computation.
- **philosophy/what_is_number/attempt_001** — Gödel incompleteness as a compression limit. Compression meets computability here.
- **philosophy/what_is_mind/attempt_003** — γ depends on self-modeling cognitive architectures; self-modeling is computation with a specific feedback structure.
- **philosophy/UNDERGROUND_CONNECTIONS.md** — the load graph.

## Computation as K-manipulation

Under the S/K bifurcation, information is either channel capacity (S) or structural compressibility (K). Computation operates on both but for different reasons.

**A computation, physically, is a dynamical process whose input and output states have definite S-content (some number of bits) and K-content (some degree of compressibility), and which implements a function mapping input K-content to output K-content.**

The function is what we call the "program" or "algorithm." The physical process is the substrate that implements the function. A computation is classified by:

- Its **S-capacity** — how many distinguishable input and output states it can handle. Measured in bits of I/O.
- Its **K-function** — the structural transformation it implements. This is what "what the program does" means.
- Its **resource cost** — time, energy, space required. The thermodynamics of computation (Landauer, Bennett) is mostly about S-manipulation cost; the algorithmic theory is about K-function complexity.

Examples:

- A sort routine takes a list (high S, medium K because the raw ordering has structure) to a sorted list (same S, higher K because the sorted structure is maximally compressible for this specific content). Its K-function is "produce the unique permutation that satisfies the total order."
- A random number generator takes a seed (low S input) to a long random string (high S output, maximal K content because it looks random). Its K-function is "amplify S; preserve or increase the output's K-content per input K-bit."
- A compressor takes a file (some S, some K) to a compressed file (lower S, same K modulo the compression's losslessness). Its K-function is "lossless transformation from higher-S to lower-S at the same K-content."
- A decompressor is the inverse.
- An LLM at inference takes a prompt (some S and K) to a next token prediction. Its K-function is "predict the next token given the distribution of text encoded in the weights." This is both S-manipulation (selecting one token from the vocabulary) and K-exercise (invoking compressed regularities about language).

Under this reading, **computation is the dynamics of K-content transformation**. The S aspects are about resource bookkeeping; the K aspects are about what the computation is *for*.

## Church-Turing as a compression claim

The Church-Turing thesis says: every "effectively calculable" function is computable by a Turing machine.

Reframed under K-manipulation:

> **Every function whose K-content can be finitely specified is implementable as a Turing machine program, which is itself a finite K-specification.**

This is not a different claim. It is the same claim with the compression ontology made explicit. "Effectively calculable" in the original formulation is notoriously imprecise; "finitely specifiable K-content" is sharper and gestures at why the thesis is plausible: a function IS its K-content, and a Turing machine IS a finite K-specification of a function, and these are the same object.

**Physical Church-Turing** is the stronger claim: every physically realizable function has a finite K-specification that can be run on a Turing machine. This is an empirical claim about the universe — specifically, that the universe's dynamics admit finite K-descriptions for everything physically instantiable.

**Is physical Church-Turing true?**

Almost certainly at the classical level, and probably at the quantum level up to BQP (the complexity class of bounded-error quantum polynomial time). Counter-claims (hypercomputation via black holes, Malament-Hogarth spacetimes, "computing with the continuum") exist but are speculative and require exotic physics.

Under the compression view, the physical Church-Turing thesis is asking: **is every physical regularity capturable by a finite K-specification?** This is the same question as "is physical reality fully compressible by a finite mind." If yes, physical Church-Turing holds. If no, reality exceeds computation in a specific way.

## The P vs NP question, in compression language

P is the class of decision problems solvable in polynomial time. NP is the class whose solutions can be VERIFIED in polynomial time. P ≠ NP is the conjecture that some NP problems cannot be solved in polynomial time, only verified.

Under the compression view:

> **P ≠ NP is the conjecture that for some regularity classes, finding the compression is much harder than verifying it.**

A compression is a K-specification that regenerates the target. An NP problem's solution is a "witness" — a short string that certifies a property of the input. Verification takes the witness and checks. Finding the witness is search over the space of possible witnesses. If compression-finding is computationally cheap, P = NP. If finding short descriptions is hard in general, P ≠ NP.

The fact that the problem has resisted proof for 50+ years is consistent with the observation that **the problem asks about the structure of compression-finding itself**, which is a meta-level claim about our own cognitive capacities as compressors. We are asking whether finding-the-compression is computationally easier than recognizing-it-once-found. Our intuition says no — finding is harder than checking — but proving it requires techniques that reach past the current barriers (relativization, natural proofs, algebrization).

The philosophical contribution of this attempt: **P vs NP is a claim about whether our situation as compressors is inherent to computation or an artifact of our specific architecture.** If P = NP, then what feels like "insight" (finding a proof) is no harder than "checking" (verifying a proof). If P ≠ NP, then insight is categorically harder than verification. The former would dissolve a lot of mystery about cognition; the latter preserves it.

## Gödel incompleteness, revisited through computation

From `philosophy/what_is_number/attempt_001`:

> Mathematics is cultural evolution of maximally compressed descriptions. Gödel shows that no finite compression captures all of arithmetic truth. The compression view predicts this because compression is necessarily finite in any actual cognitive system.

From computation's angle: **the set of arithmetic truths is computably enumerable but not decidable.** You can list theorems (run the proof system and enumerate provable statements), but you cannot in general decide whether a given statement is true. This is the computation-theoretic statement of incompleteness.

Under the K view: you cannot build a finite K-specification that decides all arithmetic truths. Any finite compressor misses some truths. Extensions exist (stronger axioms, larger cardinals) but each extension is itself finite, and each misses further truths.

**This is not a defect of compression. It is a structural fact about the arithmetic regularity class: it is too rich to compress finitely.** The compression view absorbs Gödel as a theorem about its own limits, not as a refutation.

## Is the universe a computation?

PROBLEM.md asks about pancomputationalism. Under the K view, the question bifurcates:

- **Strong pancomputationalism.** Every physical process IS a computation in the full sense, with a K-function that some observer could read off from the physical dynamics. Wolfram's "new kind of science" and Fredkin's digital physics are of this form.
- **Weak pancomputationalism.** Physical processes can be modeled as computations; this is a useful abstraction but not an ontological claim.

The weak form is trivially true and uninteresting. The strong form is the actual question.

**The S/K bifurcation sharpens the strong form.** The strong claim is that reality's dynamics have a finite K-specification that, if run, produces reality. This is equivalent to claiming that reality's laws are finitely compressible. Under current physics, the laws are finitely specified (equations of general relativity, quantum field theory, standard model). So the laws, at least, have a finite K-specification.

Whether that K-specification, when "run," reproduces reality in any substantive sense depends on what "run" means. If "run" means "a physical process in which the K-specification is instantiated and generates new states over time," then reality doing its thing IS running the K-specification. The distinction between "reality being governed by compressible laws" and "reality being a computation" collapses.

**The contribution of this attempt:** this framing dissolves much of the pancomputationalism debate. Once you accept that physical laws are K-specifications and that physical dynamics are the laws being instantiated, asking whether reality is a computation is asking whether instantiating a K-specification counts as running it. The answer depends on your taste in metaphysics, not on any further physical fact.

**Wheeler's "it from bit"** is the strong pancomputationalist position that the K-specification is not just a model of reality but its substance. Under the S/K bifurcation, this is a commitment to K-monism: reality is made of structural regularities, and structural regularities are what K-information is. It is a coherent position and it is consistent with the compression backbone from the philosophy track. It may be right.

## Quantum computation

BQP (the class of problems solvable by a quantum computer in polynomial time with bounded error) is believed to strictly contain P. This means quantum computers can do things classical computers cannot do efficiently, though not things classical computers cannot do at all. Quantum does not exceed classical in the Turing-completeness sense; it exceeds classical in the efficiency sense.

Under the K view: quantum computing allows access to a wider class of efficient K-functions. Specifically, problems like Shor's factoring have K-functions that are hard for classical computers but easy for quantum. The K-function itself is the same in both cases (the prime factorization of N); what differs is the resource cost of computing it.

**Interesting consequence.** If BQP is strictly more powerful than P, then the set of "efficiently K-computable" functions depends on substrate. Classical minds see one set of cheap K-operations; quantum minds would see a larger set. Whether this affects anything in the philosophy of mind is an open question — γ's G and L don't obviously depend on substrate type, so quantum minds might have the same phenomenal structure for different reasons. But the question is worth raising.

## The anti-problem

PROBLEM.md asks: what would a non-computational physical process look like?

Under the compression view: a non-computational physical process would be one whose dynamics cannot be captured by any finite K-specification. Such a process would have infinite K-content in finite time — it would do infinitely many things per moment in a way that no finite description could track.

Are there any such processes? We do not know. Physical realism of continuous fields suggests some kinds of infinities in physical theories, but those are mostly removed or regularized in working physics. The question of whether a physically realizable process can have truly infinite K-content is an open problem and is related to hypercomputation claims.

**Most plausibly, every physical process is computational in the K sense** — has a finite K-specification that describes its dynamics — and the anti-problem is empty. But the "most plausibly" is doing real work; no theorem guarantees it.

## Sky bridges

- **physics/what_is_information** — S/K bifurcation. Computation is K-manipulation; the K-specification of a computation is its "program."
- **physics/what_is_reality** — is reality a computation? Under the compression view, asking this is asking whether physical laws (finite K-specifications) plus initial conditions (finite K-specification) can generate all observed regularity. The answer is plausibly yes, and whether that counts as "being a computation" is metaphysical taste.
- **philosophy/what_is_number** — Gödel's incompleteness is the compression limit for arithmetic. The computation framing makes this a specific claim about computably enumerable but not decidable sets.
- **philosophy/what_is_mind** — minds are computations; γ specifies what kind of computations generate phenomenal self-reports.
- **philosophy/what_is_language** — LLMs are computations that compress social regularities. Their sample complexity is the K-extraction rate from text.
- **math/p_vs_np** — the compression reframing of P vs NP is available for the math track's Phase 0 work on this problem.

## The gap

After this attempt:

> **Computation is K-manipulation in finitely-specifiable form. Church-Turing (classical and physical versions) is the conjecture that all physically realizable K-functions have finite K-specifications. P vs NP is the conjecture that compression-finding is harder than compression-verifying, i.e., that our cognitive situation as compressors is inherent to computation rather than accidental. Both remain open; both are about the limits of compression as a general process.**

## What this attempt closes

- The six ontologies redistributed under the K view.
- Church-Turing restated as a compression claim.
- The pancomputationalism question dissolved by the law-as-K-specification move.
- P vs NP reframed in compression language.
- The cross-track bridge from computation to mind (via minds-as-compressors) and to language (via LLMs-as-computations).

## What remains

- Hypercomputation is undiscussed. If there are physically realizable processes with truly infinite K-content, the physical Church-Turing thesis fails. The literature here is thin and speculative.
- The relationship between BQP and the compression view. Does quantum computing access a different K-function space, or just a more efficient path to the same one?
- A proper engagement with the math track's `p_vs_np` Phase 0 work. The reframing here is a hypothesis that the math track can test with its formalization tools.

## Status

Phase 1. The physics track now has two attempts (information, computation), both extending the philosophy track's compression backbone cleanly. The method's Multiple Mountains principle is working here: the same argument, climbed from a different base (physics rather than philosophy of mind), confirms the same residue and the same substrate.
