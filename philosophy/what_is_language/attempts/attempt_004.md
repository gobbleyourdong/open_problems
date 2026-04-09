# attempt_004 — Steelmanning the Constitutive Position

**Date:** 2026-04-09
**Status:** Dead-end mapping. Of seven variants of "LLMs don't really have language," five collapse either to consciousness or to quantitative claims already covered elsewhere. Two survive as principled positions but are weaker than their common formulations.

## Why steelman

attempts 002 and 003 pushed toward the conclusion that the language-specific gap between humans and LLMs has mostly closed, leaving only sample complexity, grounding-as-perception, and memory-as-host. The honest next move is to stress-test that conclusion by trying to save the opposite view: that LLMs *categorially* lack language, not just quantitatively.

If any version of that view survives, the survivors point at the true gap. If none survives, the behavioral-reducible framing of attempt_003 stands.

## The seven variants

For each variant I state the claim, the standard supporting argument, the strongest version, and where it lands under scrutiny.

### Variant 1 — Chinese Room (Searle 1980)

**Claim.** A system that manipulates symbols by rules has syntax without semantics. LLMs manipulate tokens by learned rules (the weights) without semantics. Therefore LLMs lack meaning.

**Strongest version.** The man in the room following a rulebook does not understand Chinese. If an LLM is relevantly like the man, neither does it.

**Scrutiny.** The "systems reply" — that the entire room including the rulebook understands, even if the man does not — has never been refuted, only dismissed as counterintuitive. The argument therefore cashes out as a clash of intuitions, not a demonstration. There is no operationalization under which Chinese Room predicts a measurable behavior the LLM cannot produce.

**Verdict.** Survives as intuition, not as argument. Not a decisive constitutive cut.

### Variant 2 — Derived vs. intrinsic intentionality (Dennett's reading of classical AI)

**Claim.** Any meaning an LLM appears to have is borrowed from the humans who generated the corpus. The LLM's intentionality is derived; human intentionality is intrinsic.

**Strongest version.** A thermostat "represents" temperature only because we ascribe that representation to it. Likewise an LLM "means" what its outputs mean only because we read meaning into them.

**Scrutiny.** Children also inherit language from adults; their meanings are trained on adult meanings. Where is the principled line between "inherited meaning that still counts" and "inherited meaning that does not"? Every available version of the line invokes consciousness, biological substrate, or agency in ways that beg the question.

**Verdict.** Collapses to consciousness. The only non-circular way to save it is to stipulate that intrinsic intentionality requires phenomenal experience. → Variant 6.

### Variant 3 — Embodiment-constitutive (Lakoff, Dreyfus, Glenberg)

**Claim.** Meaning is metaphor grounded in bodily experience. A disembodied system cannot mean anything.

**Strongest version.** All abstract concepts reduce to bodily schemas (containers, paths, forces). No body, no schemas, no meaning.

**Scrutiny.** Three problems. **(a)** Multimodal LLMs have perception if not action; the embodiment claim then has to be redrawn around action and it becomes much weaker. **(b)** Congenitally blind humans lack visual metaphor sources yet possess full meaning, including "visual" metaphors used non-phenomenally. **(c)** Domains like pure mathematics have meaning with no obvious embodied grounding for humans either. The strong version overcommits. The weak version reduces to: "LLMs are worse on topics where grounding helps," which is quantitative and already in attempt_003.

**Verdict.** Collapses to quantitative. Not a constitutive cut.

### Variant 4 — Social-constitutive (Wittgenstein, Brandom)

**Claim.** Meaning is use in a form of life. Participation in a linguistic practice constitutes meaning. LLMs do not participate.

**Strongest version.** Language-games are normative; to mean anything is to be accountable to a community that can correct you. An LLM that is merely queried and replies is not a participant.

**Scrutiny.** Deployed LLMs interact with humans, get feedback (explicit and implicit), influence conversations, and shape follow-up practice. Whether this counts as "participation" depends on the criterion. If the criterion is "being the kind of thing that can be held responsible," it presupposes agency and consciousness. If the criterion is "being an effective node in a communicative network," LLMs qualify. The position does not draw a non-circular line between the two.

**Verdict.** Either collapses to consciousness or is circular. Not a decisive cut by itself.

### Variant 5 — Causal-historical reference (Kripke, Putnam)

**Claim.** A word refers to its object via a causal chain from ostensive baptism to current use. LLMs' "words" do not touch their referents; the causal chain from water to the LLM passes only through texts about water.

**Strongest version.** Reference requires a direct causal-historical link. Twin Earth: a word means what its causal history grounds it in. LLMs lack the grounding link.

**Scrutiny.** The causal chain from "water" to an LLM is not absent — it runs through every human who wrote the training text, each of whom has a direct causal link to actual water. The LLM's chain is longer and mediated, but it exists. At what chain length does reference fail? There is no principled answer. A child who learns "dinosaur" from books has a longer causal chain to dinosaurs than one who sees a fossil, yet both refer.

**Verdict.** Survives as a principled position but the cut between "reference" and "no reference" is not currently drawable in a non-arbitrary way. This is a real constitutive position, just a blunt one. It predicts: multimodal LLMs with perceptual access should do better on reference tasks than text-only LLMs. This is empirically supported. It does NOT predict that LLMs in principle cannot refer.

**Verdict refined.** Partial survivor. Yields a quantitative-ish prediction rather than a categorial cut.

### Variant 6 — Phenomenal-constitutive (Chalmers, Block)

**Claim.** Meaning requires phenomenal consciousness. Without "what it is like" to use a word, there is no meaning, only behavior.

**Strongest version.** The hard problem applies to semantics. Functional equivalents of meaning behavior are zombies of meaning.

**Scrutiny.** **(a)** The claim is coherent but empirically untestable from the outside. It inherits every problem of the hard problem of consciousness. **(b)** It is not obvious that meaning requires phenomenology; one can imagine access-consciousness of linguistic content without phenomenal consciousness of linguistic content, and the two come apart in the literature. **(c)** If meaning does require phenomenology, then the language question is the consciousness question and we have identified the bridge.

**Verdict.** Coherent constitutive position. Reduces to the hard problem. If accepted, the language gap IS the consciousness gap — this is the sky bridge to what_is_mind.

### Variant 7 — Higher-order representation (Rosenthal, Gennaro)

**Claim.** Meaning requires the capacity to represent one's own representations. LLMs may process tokens but do not represent that they are representing.

**Scrutiny.** LLMs report their own states when asked, produce self-critique, catch their own errors, and adjust based on meta-prompts. Whether this constitutes *genuine* higher-order representation or a learned verbal surface is empirically open. Interpretability research is actively working on this.

**Verdict.** Empirically open. Not currently a decisive separator in either direction. Likely to be settled by mechanistic interpretability rather than philosophy.

## The pattern

| Variant | Fate |
|---------|------|
| 1. Chinese Room | Intuition, not argument |
| 2. Derived intentionality | Collapses to consciousness (→ 6) |
| 3. Embodiment constitutive | Collapses to quantitative (already in attempt_003) |
| 4. Social constitutive | Collapses to consciousness or is circular |
| 5. Causal-historical reference | **Partial survivor** — real but quantitative-ish |
| 6. Phenomenal constitutive | **Coherent but = hard problem** |
| 7. Higher-order | Empirically open |

**Five of seven collapse. Two survive.**

Of the two survivors, one (causal-historical reference) makes only soft, comparative claims that are compatible with the attempt_003 picture. The other (phenomenal) is a coherent constitutive position — but it is the consciousness problem wearing a language hat.

## What this confirms

- The behavioral reduction of attempt_003 is stable: no constitutive position rules it out except by invoking consciousness.
- The remaining irreducible residue is **phenomenal consciousness**. If phenomenal consciousness is necessary for meaning, the language gap *is* the consciousness gap. If it is not, the language gap has largely closed.

Either way, progress on **what_is_language** now goes through progress on **what_is_mind** and, more narrowly, **what_is_meaning**.

## Multiple Mountains reading

attempts 001–004 have been climbing one mountain: the behavioral-measurement mountain. That mountain shows a single wall — phenomenal consciousness — and the behavioral separators have mostly dissolved before reaching it.

The Sigma Method says: when one mountain hits a wall, find another. Candidate alternative mountains for the language question:

- **Mountain B — Diachronic / evolutionary.** How did language arise as a biological trait? What selection pressure fixed it? Comparative animal communication, protolanguage, gene candidates (FOXP2), cultural transmission dynamics. This mountain treats language as a natural-history object rather than a capacity.
- **Mountain C — Neural / substrate.** What does language look like in the brain? Broca, Wernicke, the arcuate fasciculus, aphasias as natural ablation studies, the neural code for syntax. This mountain treats language as a neurological artifact.
- **Mountain D — Function / adaptive.** What is language FOR? Coordinating cooperation, gossip, teaching, deception, thought scaffolding, cultural ratcheting. This mountain treats language as a tool whose identity is its function.
- **Mountain E — Formal / mathematical.** Type theory, Montague, CCG, dependency grammars, the relationship between language and computation. This mountain treats language as a mathematical object.

attempt_005 will pick one of these and climb it, looking for a different angle on the residue identified by attempts 002–004.

## Next attempt

**attempt_005** — climb Mountain D (function / adaptive). What is language for? If we can answer that, we may find that "having language" means "doing the thing language is for," which may cleave differently than behavioral benchmarks. The LLM existence proof will then have to be re-examined: do LLMs do the thing language is for, or only produce its surface?
