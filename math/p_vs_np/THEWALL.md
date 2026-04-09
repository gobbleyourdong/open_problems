# THE WALL — P vs NP

> Phase 0→1 complete. The wall isn't one wall — it's THREE.

## The Problem

Is P = NP? Can every efficiently verifiable problem be efficiently solved?

Consensus: P ≠ NP. No proof. Not even close.

## The Three Walls

Unlike every other Millennium Problem — which has ONE wall — P vs NP
has THREE independent barriers that PROVABLY block most proof techniques.

### Wall 1: Relativization (Baker-Gill-Solovay 1975)
**Kills**: any proof that works relative to an oracle.
**Scope**: diagonalization, simulation, most recursion theory arguments.
**Survives**: techniques analyzing internal circuit structure (IP=PSPACE broke this).

### Wall 2: Natural Proofs (Razborov-Rudich 1997)
**Kills**: any proof defining a constructive, large property of hard functions.
**Scope**: almost ALL known circuit lower bounds (AC⁰ parity, monotone bounds).
**Survives**: non-constructive or non-large arguments (Williams' approach).
**Irony**: barrier only applies IF P ≠ NP (conditional on OWFs existing).

### Wall 3: Algebrization (Aaronson-Wigderson 2009)
**Kills**: any proof using arithmetization that relativizes over algebraic extensions.
**Scope**: the entire IP/PCP revolution of the 1990s.
**Survives**: direct circuit analysis, non-algebraic methods.

### What Survives All Three?

| Approach | Relativizes? | Naturalizes? | Algebrizes? | Status |
|----------|-------------|-------------|------------|--------|
| Williams (algorithms→bounds) | NO | NO | NO | NEXP ⊄ ACC⁰ ✓, stuck at TC⁰ |
| GCT (Mulmuley) | NO | NO | NO | 100-year program, occurrence obstructions insufficient |
| Proof complexity | N/A | N/A | N/A | Stuck at Frege lower bounds |

## The Circuit Complexity Frontier

```
WHAT WE CAN PROVE:                    WHAT WE NEED:
  PARITY ∉ AC⁰  ✓                      NP ⊄ P/poly
  NEXP ⊄ ACC⁰   ✓ (Williams 2011)     (= P ≠ NP for circuits)
  ???  ⊄ TC⁰    ✗                      
                                        
  AC⁰ ⊊ ACC⁰ ⊊ TC⁰ ⊊ NC¹ ⊊ ... ⊊ P/poly
       ↑           ↑                    ↑
    proved       STUCK                 NEED
```

The gap: we can't even prove NEXP ⊄ TC⁰, let alone NP ⊄ P/poly.
The jump from ACC⁰ to TC⁰ (adding threshold/majority gates) has
blocked all progress since Williams' 2011 breakthrough.

## Why P vs NP Is the Hardest Millennium Problem

| Feature | Other Clay Problems | P vs NP |
|---------|-------------------|---------|
| Type | Prove a property | Prove a NEGATIVE |
| Evidence | Computational verification | None possible |
| Barriers | 0 meta-barriers | THREE provable barriers |
| Approach space | Many routes survive | Almost nothing survives |
| Independence | Not suspected | Possible (Pi_2 statement) |
| systematic approach | Maps the space, finds gaps | Maps barriers, can't get through |

P vs NP is the only Millennium Problem that:
1. Asks for a NEGATIVE (no algorithm exists)
2. Has PROVABLE barriers against proof techniques
3. Might be INDEPENDENT of standard axioms (ZFC)
4. Has NO computational evidence possible

## The systematic approach Assessment

### What the systematic approach CAN do:
- Map the three barriers precisely ✓
- Identify surviving approaches (Williams, GCT) ✓
- Formalize barrier statements in Lean ✓
- Study specific circuit classes computationally (numerical track)

### What the systematic approach CANNOT do:
- Produce certificates (non-existence can't be certified)
- Find a "gradient correlation" (no single quantity to compute)
- Build an iron fortress (no sequence of increasing evidence)
- Close the gap by computation (the gap IS the proof technique)

### The Honest Verdict

P vs NP requires inventing a fundamentally new proof technique that
simultaneously avoids relativization, natural proofs, and algebrization.
No such technique is known. Williams' paradigm and GCT are the only
candidates, and both face their own enormous technical barriers.

The systematic approach maps the space. The space says: "come back with new math."

## Comparison: All Seven Clay Problems

| Problem | Wall | Type | Sigma Score |
|---------|------|------|-------------|
| NS | Liouville conjecture | Quantitative (one inequality) | Phase 4 |
| YM | GC > 0 | Quantitative (closable) | COMPLETE |
| RH | No framework | Conceptual | Phase 1 |
| Poincaré | (solved) | Entropy functional | 12/12 BLIND |
| BSD | No rank-2 construction | Structural | Phase 1 |
| Hodge | Motivic t-structure | Existential | Phase 2 |
| **P vs NP** | **Three barriers** | **Meta-mathematical** | **Phase 0** |

P vs NP is the ONLY problem where the obstacles are META-mathematical
(theorems about what KINDS of proofs can work). Every other problem's
wall is a mathematical object or inequality. P vs NP's wall is about
the NATURE OF PROOF ITSELF.
