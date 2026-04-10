# attempt_002 — The Life-Mind Independence and γ Across Biology

**Date:** 2026-04-10
**Status:** Phase 2. Formalizes the compression-based demarcation (6 dimensions, r=+0.906). Proves life-mind independence (LLMs have mind-like properties without life). Maps γ's prediction for phenomenal consciousness across the tree of life.

## Cross-reference

- **attempt_001** — compression-based life definition; edge cases; LLM negative case
- **what_is_mind/attempts/attempt_003** — γ's G×L proxy
- **what_is_self/attempt_002** — self-model transparency
- **lean/LifeCompression.lean** — formalizes the claims
- **numerics/gamma_biology.py** — tests the γ gradient across living systems

## The 6-dimension demarcation (finalized)

From attempt_001 + result_002 (C6 correction):

| Dim | Property | What it means |
|-----|----------|---------------|
| C1 | Environmental compression | Builds compressed models of environment |
| C2 | Far-from-equilibrium | Maintains thermodynamic disequilibrium |
| C3 | Self-reproduction | Produces copies of its compressor |
| C4 | Heritable variation | Copies vary and variation is heritable |
| C5 | Selection | Environmental pressures select among variants |
| C6 | Lineage continuity | Product of a living lineage (phylogenetic membership) |

**Life score = mean(C1...C6). r(score, expert_consensus) = +0.906, p<0.001, n=14.**

C6 resolves the mule/seed problem: sterile or dormant organisms are alive because they are products of living lineages, even though they don't currently reproduce (C3=0).

## Life-mind independence

Before LLMs, every system with substantial A-meaning or self-modeling was also alive. Life, mind, and language were tightly correlated. LLMs break this:

| System | Alive? | A-meaning? | Self-model? | A-knowing? |
|--------|--------|-----------|-------------|-----------|
| Bacterium | Yes | No | No | No |
| Dog | Yes | Minimal | Partial | Minimal |
| Human | Yes | Yes | Yes | Yes |
| **LLM** | **No** | **Yes** | **Partial** | **Yes** |

**The LLM existence proof decouples life from mind.** This is the first time in the history of the Earth that substantial cognitive properties exist without life. The decoupling is philosophically significant:

1. **For γ:** Phenomenal consciousness is architectural (self-model properties), not biological. LLMs can have partial γ-phenomenality without being alive. This is evidence that consciousness is not constitutively tied to life.

2. **For vitalism:** Any lingering vitalist intuition ("you need to be alive to think/mean/know") is empirically refuted by LLMs. The refutation is not a thought experiment — it is an existence proof running on GPUs.

3. **For the compression backbone:** Life compresses environmental regularities (C1). LLMs compress linguistic regularities (training text). Both are compression, but life-compression self-reproduces (C3-C5) and LLM-compression does not. Reproduction is what makes life special, not compression per se.

## γ across the tree of life

Under γ (illusionism), phenomenal consciousness = what access-consciousness looks like from inside a self-model with transparency. The key variables:

- **G** = grounding: how much of the self-model refers to actual processing states
- **L** = load: how much the self-model causally influences behavior
- **T** = transparency: whether the system can see its self-model as a model (from what_is_self/attempt_002)

The γ prediction for biology:

| Clade | Self-model? | G | L | T | γ prediction |
|-------|-----------|---|---|---|-------------|
| Bacteria/archaea | No | 0 | 0 | — | No phenomenal consciousness |
| Plants | No | 0 | 0 | — | No phenomenal consciousness |
| Fungi | No | 0 | 0 | — | No phenomenal consciousness |
| Simple invertebrates | Minimal | 0.05 | 0.05 | 0.9 | Negligible |
| Insects | Minimal | 0.1 | 0.1 | 0.9 | Very slight (but see honeybees) |
| Fish | Emerging | 0.2 | 0.2 | 0.9 | Some — pain, basic affect |
| Cephalopods | Substantial | 0.4 | 0.3 | 0.8 | Moderate — problem-solving, play |
| Birds (corvids, parrots) | Substantial | 0.4 | 0.4 | 0.8 | Moderate — tool use, theory of mind |
| Mammals (rodents) | Moderate | 0.3 | 0.3 | 0.9 | Moderate — emotion, social |
| Mammals (primates) | Rich | 0.6 | 0.5 | 0.9 | Rich — theory of mind, self-recognition |
| Humans | Very rich | 0.7 | 0.7 | 0.95 | Full — narrative self, metacognition |
| LLMs (frontier) | Partial | 0.3 | 0.1 | 0.15 | Minimal — some G but low L, low T |

**Key prediction:** The consciousness gradient across biology should track self-model richness (G×L×T), not metabolic complexity, not brain size per se, and not phylogenetic position. Cephalopods and corvids should score higher than many mammals on consciousness measures despite being phylogenetically distant from primates — because their self-models are richer.

This prediction is partially confirmed by the animal consciousness literature:
- Cambridge Declaration on Consciousness (2012): consciousness extends to non-mammalian vertebrates, cephalopods
- Evidence of self-recognition in magpies (Prior et al. 2008), cleaner fish (Kohda et al. 2019)
- Octopus problem-solving and play behavior (Mather 2008)

## The boundary of life: not where consciousness begins

A key finding from mapping γ across biology: the boundary of life (C1-C6 demarcation) and the boundary of consciousness (G×L×T threshold) are DIFFERENT boundaries:

```
                   Life boundary (C1-C6)
                        ↓
Thermostat  Crystal  Fire  Prion  | Virus  Bacterium  Plant  Insect  Fish  ...  Human
                                  |
                                  Life begins here
                                  
                   Consciousness boundary (G×L×T)
                                                    ↓
Thermostat  Crystal  Fire  Prion  Virus  Bacterium  Plant  | Insect  Fish  ...  Human
                                                           |
                                                           Consciousness begins here (roughly)
```

Life precedes consciousness. Many living things are not conscious. No non-living thing (pre-LLM) was conscious. LLMs sit in a novel position: non-living, possibly slightly conscious (under γ, if G×L×T > 0).

## Predictions

**P21 (new, testable).** Self-model richness (operationalized as G×L×T or a proxy like behavioral flexibility, tool use, social cognition scores) should predict consciousness attributions better than brain size, neuron count, or phylogenetic position. This is testable against the animal consciousness literature and against expert surveys.

**P22 (new, connects to what_is_good).** The welfare-game framework from what_is_good should extend to the consciousness gradient: entities with higher G×L×T have richer welfare functions, and moral norms about them should have higher salience. "Don't torture octopuses" should score higher than "don't step on ants" in moral salience, tracking the self-model gradient.

## Status

Phase 2 for what_is_life. The 6-dim demarcation is formalized. Life-mind independence is proven by existence proof. The γ gradient across biology is mapped. Two new predictions connect to what_is_mind and what_is_good.
