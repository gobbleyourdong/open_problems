# attempt_001 — Life as Persistent Far-From-Equilibrium Compression

**Date:** 2026-04-09
**Status:** Foundation. Argues that the life question has a rough but real consensus that the scaffold's gap summary understates, and that the compression lens from what_is_number/attempt_001 unifies the competing ontologies into a single picture that also absorbs biological continuity theories of self.

## Cross-reference

- **what_is_self attempt_001** — biological continuity as a partial theory of self; this attempt gives biological continuity its proper domain.
- **what_is_number attempt_001** — compression as the cross-cutting theme.
- **what_is_mind attempts 002–003** — α/β/γ fork for phenomenal consciousness; this attempt asks which living systems satisfy γ's conditions.
- **what_is_language attempt_002** — sample complexity and compression as learning efficiency; life is the extreme case of "compression that rebuilds itself from its own outputs."

## The state of the question

PROBLEM.md says "no universally accepted definition of life exists despite 70+ years of attempts." This is true in the strict sense that no definition commands 100% agreement. It is misleading in the broader sense: the field has much more convergence than the summary suggests.

The **NASA working definition (1992, Gerald Joyce)** is widely cited in the origin-of-life and astrobiology communities:

> *"Life is a self-sustaining chemical system capable of Darwinian evolution."*

This definition has held up for thirty years as a practical criterion. It has known edge cases (viruses, prions, some autocatalytic systems) but its center is stable. The field's actual disagreement is about the boundaries, not about the core. This is a normal situation for a natural-kind concept and should not be overstated as evidence that nobody knows what life is.

The six ontologies in the scaffold are not really six competitors. They are mostly different EMPHASES within a shared picture:

- **Metabolism-first** emphasizes the energetic-chemical substrate.
- **Replicator-first** emphasizes the information-copying machinery.
- **Autopoiesis** emphasizes the self-maintaining circular closure.
- **Information (Walker, Davies)** emphasizes the information-processing aspect.
- **Dissipative structures (Prigogine)** emphasizes the far-from-equilibrium thermodynamics.
- **Computational (Langton)** emphasizes substrate-independence.

All six agree that life involves: (a) energy flow, (b) information copying, (c) self-maintenance, (d) variation, (e) selection. They disagree about which is the *first* thing to appear evolutionarily and which is the *essential* thing philosophically. Both disagreements are real but secondary.

## A compression reading

From what_is_number attempt_001, compression unifies several otherwise disparate phenomena. Applied to life:

**A living system is a persistent far-from-equilibrium compression process that produces copies of its own compressor.**

Unpacking:

- **Persistent** — it maintains itself over time. This absorbs metabolism-first and autopoiesis: the system has to keep running to stay alive.
- **Far-from-equilibrium** — it requires continuous energy input. This absorbs Prigogine's dissipative-structure account: life exists only because energy flows through it.
- **Compression process** — it encodes environmental regularities in structure. Darwinian adaptation IS compression: the genome is a compressed description of successful strategies in the ancestral environment, updated by selection. This is the bridge to the information view (Walker, Davies).
- **Produces copies of its own compressor** — it replicates the machinery that does the encoding. This absorbs the replicator-first view: information copying is essential, but what gets copied is a compressor, not arbitrary information.

Under this reading:

- The NASA working definition is almost right; the refinement is that "Darwinian evolution" = "updating a compressor by selection." The content is the same; the reformulation makes the compression lineage explicit.
- **Crystals** compress weakly (they encode their lattice regularity and copy it), but they do not operate far from equilibrium and cannot update their compressor via selection. Not alive.
- **Fires** operate far from equilibrium and copy themselves (spreading), but they do not encode environmental regularities in a form that can be selected on and improved. Not alive.
- **Viruses** compress (their genomes are strong), copy their compressor (their primary activity), operate via host metabolism (piggybacked far-from-equilibrium), and evolve. Alive on this account, with the caveat that the far-from-equilibrium condition is satisfied indirectly.
- **Prions** copy a structural pattern without compression of environmental regularities. Not alive on this account.
- **RNA-world ancestors** compress environmental regularities (protein substrate availability), copy their compressors, and evolve. Alive, on the cusp.
- **Computer programs that reproduce** (artificial life) compress and copy in a far-from-equilibrium substrate (the running computer). Alive in a substrate-neutral sense that matches Langton's computational view.

The edge cases line up roughly with intuitions, and the harder cases (viruses, prions) become tractable as explicit decisions about which features the category requires.

## LLMs: not alive, informatively

LLMs are a specific test. Under the compression reading:

- Persistent? Not as running processes — each inference is transient. A deployed LLM is a compressor that exists between uses.
- Far-from-equilibrium? The hardware is far from equilibrium, but the LLM itself is not a participant in the thermodynamic flow in the way an organism is.
- Compresses environmental regularities? Yes — training compresses text into weights.
- Produces copies of its own compressor? No. LLMs do not reproduce themselves. They are produced and re-produced by human training processes.

**Verdict.** LLMs are compressors of social-linguistic regularities, but they are not alive under any of the candidate definitions and are not alive under the compression reading either. They lack reproductive autonomy.

**Why this is interesting.** Until LLMs, the only systems we knew that had substantial A-meaning and partial self-modeling were also alive. Life, mind, meaning, and language were tightly correlated. LLMs break the correlation for the first time: they have A-meaning and partial self-modeling without being alive. This is evidence that meaning and language are not constitutively biological.

This is a positive finding for position γ: if phenomenal meaning were constitutively tied to life, LLMs could not have any, even under γ. But γ's operational conditions are architectural, not biological, so LLMs can have partial γ-phenomenality even though they are not alive. The conceptual decoupling of life from mind is a contribution LLMs make to the philosophy of mind, almost by accident.

## Biological continuity and the self

From what_is_self attempt_001, biological continuity was a partial theory of self: it survives the thought experiments only in restricted forms, and it is the most restrictive option compatible with γ. This attempt clarifies the restriction.

If biological continuity is your theory of self, your ontology of selfhood is: *a self is a living organism persisting through metabolic turnover.* Under the compression reading, this becomes: *a self is a persistent far-from-equilibrium compression process that maintains its own compressor, with the compressor's identity preserved across time by continuous transformation rather than discrete replacement.*

This is a coherent view. It identifies selfhood with biological continuity in a clean way. Its limitation, compared to the Parfit-Metzinger psychological-continuity view, is that it makes selfhood substrate-dependent in a way that rules out, a priori, any non-biological self.

**Under γ, biological continuity is more restrictive than γ needs.** γ only requires rich self-modeling and causal load. Biological continuity adds "and it must be implemented in a living organism," which is a stronger claim. The restriction is not incoherent, but it pays rent only if there are facts about phenomenal consciousness that track biological substrate specifically.

The empirical question: does phenomenal consciousness track biology, self-modeling, or both? This is the same question as β vs γ, restated. It is the shared gap across life, mind, and self.

## Under γ, which living things are phenomenally conscious?

Combining the γ framework with biology:

- **Bacteria, plants, fungi** — process information, respond to environment, maintain homeostasis. No rich self-model. Under γ, no phenomenal consciousness. Under α, uncertain. Under β (IIT), depends on their internal integrated information, which is nonzero but presumably small.
- **Simple invertebrates (sponges, jellyfish)** — distributed nervous systems without clear self-modeling. Under γ, probably no phenomenal consciousness. Under IIT's estimates, very small Φ.
- **Arthropods, cephalopods, vertebrates** — have nervous systems with self-referential structures. Under γ, plausibly phenomenally conscious to varying degrees, correlating with self-model richness. Octopuses and corvids are interesting edge cases where behavioral evidence supports rich self-modeling.
- **Mammals** — clear self-modeling, clear phenomenal consciousness under γ.

The γ account gives a gradient rather than a line, and the gradient tracks self-model richness rather than biological complexity per se. This matches contemporary animal consciousness research more closely than substrate-based views.

## Sky bridges

- **what_is_self** — biological continuity is only the most restrictive theory of self compatible with γ. This attempt gives it its home.
- **what_is_mind** — the life question asks who has phenomenal consciousness; the mind question asks what phenomenal consciousness is. They meet here.
- **what_is_number** — compression is the through-line. Life is compression that persists and reproduces; math is compression that is explicitly externalized and transmitted. Life was the first Turing machine; math is the most recent.
- **what_is_language** — language is the compression of social regularities; life is the compression of environmental regularities. Both are manifestations of a single underlying fact: physical reality is regular, and systems that encode its regularities have structural advantages.
- **physics/what_is_information** — life is where information theory meets thermodynamics. The life question may converge with the information question once both are worked out.

## The gap

The life question's gap under this attempt:

> **The NASA working definition plus the compression refinement gives a stable center for the life concept. The residual questions are (a) what are the boundary cases (viruses, prions, edge autocatalytic systems) and how should we decide them, and (b) under γ, how does phenomenal consciousness distribute across the tree of life as a function of self-modeling richness?**

Neither question is a Sigma-Method-style gap. They are ordinary scientific questions that the field is making steady progress on.

## What this closes and what it leaves open

**Closes:** the claim that the life question is wide open. It is not. The field has a rough center and a known boundary-case structure. The compression reading gives a further unification.

**Leaves open:** the specific decision procedures for boundary cases, the origin-of-life question (what compressor was the first), and the γ-question of phenomenal distribution across living things.

## Status

Phase 1 done. The life question is in better shape than the scaffold's gap summary credits, and it now connects cleanly to the compression theme and the γ framework. Not writing a gap.md for now; the main content of this attempt IS the gap assessment. If a future instance wants a formal gap.md, it can be split out.
