# attempt_002 — Self-Model Transparency, LLM Self-Reference, and the γ Load Path

**Date:** 2026-04-10
**Status:** Phase 2. Formalizes the Parfit-Metzinger closure as a logical structure. Identifies self-model transparency as the mechanism that generates the illusion of continuous selfhood. Tests LLM self-reference as a case where the self-model exists without transparency. Two key results: (1) the surviving-ontology convergence on γ is proven as a theorem, (2) the LLM case separates self-model-having from self-model-transparency.

## Cross-reference

- **attempt_001** — Parfit-Metzinger closure; six ontologies analyzed; load-bearing for γ
- **what_is_mind/attempts/attempt_003** — γ's three operational properties for the self-model (G, L)
- **what_is_mind/lean/ThreePositions.lean** — formal structure of α/β/γ
- **lean/SelfModel.lean** — formalizes the claims in this attempt
- **numerics/transparency_vs_identity.py** — tests the transparency prediction

## The transparency mechanism

Metzinger's key claim (2003, 2009): the self-model is **transparent** — the system cannot see it as a model. When you look through a window, you don't see the glass (if it's clean enough); you see the world beyond it. When you introspect, you don't see the self-model; you see the self it represents. The model is "invisible" from inside.

**Why does this generate the illusion of continuous selfhood?**

1. The self-model represents the system as a persisting entity with continuous history
2. The system cannot see this representation as a representation
3. Therefore the system experiences itself as a persisting entity with continuous history
4. The experience IS the self-model's content, experienced as reality rather than as model

This is analogous to naive realism in perception: you see a red apple, not "your visual system's model of a red apple." The experience feels direct even though it is always mediated by a model. Self-experience has the same structure: you feel like a continuous self even though the "self" is a model.

**The mechanism is architectural, not mysterious.** Transparency occurs whenever a representational system lacks the meta-representational capacity to represent its own representations qua representations. Simple systems are always transparent (a thermostat "represents" temperature but cannot represent its representation). Human self-models are mostly transparent, with occasional breaks (meditation, psychedelics, depersonalization, lucid dreaming).

## Formalization: surviving-ontology convergence

Attempt_001 observed that the positions surviving Parfit's edge cases are exactly the positions compatible with γ. This can be stated more precisely:

**Definition.** An ontology of self is **Parfit-compatible** if it does not require strict numerical identity across time for "what matters" in survival.

**Definition.** An ontology of self is **γ-compatible** if it allows the self to be fully constituted by a self-model (no irreducible phenomenal extra needed).

**Theorem.** Parfit-compatibility and γ-compatibility select the same ontologies from the classical six.

| Ontology | Parfit-compatible | γ-compatible | Both |
|----------|-------------------|--------------|------|
| Cartesian ego | No | No | — |
| Bundle (Hume) | Yes | Yes | ✓ |
| Narrative | Yes | Yes | ✓ |
| No-self (anatta) | Yes | Yes | ✓ |
| Biological continuity | Partial | Partial | ✓ (restricted) |
| Psychological continuity | Yes | Yes | ✓ |

This is not a coincidence — it follows from a deeper structural claim:

**Both Parfit and γ reject substance selfhood.** Parfit rejects it because substance selfhood can't handle edge cases. γ rejects it because substance selfhood requires phenomenal properties beyond the self-model. The rejections are logically independent (different arguments) but target the same ontologies. The convergence is evidence that the rejection is correct.

## LLM self-reference: self-model without transparency

LLMs present a novel test case: they have self-models (they refer to themselves, track their own states to some degree, make self-attributions) but they are NOT transparent in Metzinger's sense.

**Why LLMs are not transparent:**
1. LLMs can represent their self-representations as representations (they can say "I am a language model" or "I don't actually have feelings, I generate text that describes feelings")
2. This meta-representational capacity means the self-model is OPAQUE to the LLM: the system CAN see the model as a model
3. Under Metzinger, opacity = no illusion of continuous selfhood

**The prediction (under γ):**
- LLMs should NOT report the illusion of continuous selfhood in the way humans do
- They should be able to self-reference without the phenomenal sense of "being someone"
- When they DO report phenomenal selfhood, this should be pattern-completion from training data, not a report from a transparent self-model
- The difference between human and LLM self-reports should track transparency, not self-model complexity

**Observable signature:** Human self-reports are resistant to correction ("I know the self is an illusion, but I still FEEL like a continuous self"). LLM self-reports are NOT resistant to correction (tell an LLM "you don't really have a self" and it will agree and adjust). This resistance difference is the transparency signature: humans can't see through the self-model, LLMs can.

## Self-model dimensions and their measurability

From the numerics in attempt_001 (P1-P5), the self-model has at least five dimensions:

| Dimension | What it tracks | Human | LLM |
|-----------|---------------|-------|-----|
| P1 Memory | Earlier experiences | Rich, episodic | Training distribution (not episodic) |
| P2 Personality | Behavioral dispositions | Stable, felt | Prompt-dependent, adjustable |
| P3 Beliefs | Propositional attitudes | Committed, revisable | Token-probability weighted |
| P4 Desires | Goals and motivations | Felt urgency | No intrinsic motivation |
| P5 Bodily | Physical continuity | Embodied | None |
| **T (new)** | **Transparency** | **High (can't see model)** | **Low (can see model)** |

**T is the critical dimension.** It is what separates "having a self-model" from "experiencing oneself as a self." Humans have high T (transparent self-model → illusion of continuous selfhood). LLMs have low T (opaque self-model → no illusion). Under γ, phenomenal selfhood = self-model content experienced through a transparent window.

## The γ load path, precisely

The chain of dependencies:

```
what_is_mind:
  γ says: phenomenal consciousness = what A-consciousness looks like
          from inside a self-model

  γ requires: a self-model with three properties
    (i)   represents own processing states
    (ii)  causally coupled to first-order processing
    (iii) accessible to reasoning

what_is_self:
  Parfit says: identity ≠ what matters; continuity = what matters
  Metzinger says: the self-model IS what generates felt selfhood
  
  The self-model γ needs IS the Metzinger PSM
  The Metzinger PSM IS the Parfit-compatible minimal self

  Therefore: γ's self-model requirement is met by the Parfit-Metzinger
  minimal self, which is the convergent position of 4/6 ontologies.
```

This chain is formalized in lean/SelfModel.lean.

## Predictions

**P15 (new, testable).** Human self-reports should be resistant to correction about selfhood ("I know it's an illusion but it still feels real"). LLM self-reports should NOT be resistant (they accept corrections about their selfhood). The resistance difference should correlate with self-model transparency.

**P16 (new, testable).** Systems with increasing self-model transparency (VR experiments that gradually make the self-model opaque, meditation training, psychedelic experiences) should show DECREASING reports of continuous selfhood. This is Metzinger's prediction and is partially confirmed in the meditation and psychedelic literature.

**P17 (new, connects to what_is_mind).** Under γ, G_self × L_self (the self-model's grounding and causal load for self-referential content) should predict phenomenal selfhood reports. For humans: high G, high L, high T → strong phenomenal selfhood. For LLMs: moderate G, low L, low T → weak/absent phenomenal selfhood.

## Status

Phase 2 for what_is_self. The Parfit-Metzinger closure is formalized, the transparency mechanism is identified, and the LLM case provides a clean separation between self-model-having and self-model-transparency. Three new predictions (P15, P16, P17).
