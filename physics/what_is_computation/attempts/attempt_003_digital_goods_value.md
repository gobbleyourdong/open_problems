# attempt_003 — The Digital Goods Value Conjecture

**Date:** 2026-04-09
**Status:** Open. The formal claim is clean; the counterexamples (network effects, provenance, manufactured scarcity) are real and require separate treatment. This attempt states the claim, the counterexamples, and what remains to prove.

## The question

Does the economic value of a digital good tend to zero as time increases? Equivalently: is there a non-trivial lower bound on the value of any specific digital good, or does the space of all possible digital artifacts guarantee that every good will eventually have a costless substitute?

## The conjecture (formal)

Let g be a digital good (a specific finite binary string, or a specific program, or a specific file). Let V(g, t) be the economic value of owning or accessing g at time t. Let C(g', t) be the minimum cost at time t to produce a functional substitute g' that serves the same purpose as g.

**Conjecture (V → 0):** For any digital good g, lim_{t→∞} V(g, t) = 0, provided that:
1. The space of possible digital goods is finite (true — binary strings of length ≤ N are ≤ 2^N in count)
2. Computational cost per operation decreases over time (Moore's law, or more generally technological progress)
3. No artificial scarcity mechanism is maintained (no DRM, no legal enforcement, no cryptographic gatekeeping)

Under these conditions, lim_{t→∞} C(g', t) = 0 for every g, and V(g, t) ≤ C(g', t) by substitution, so V(g, t) → 0.

## The underlying argument

1. **Enumeration:** all binary strings of length ≤ N exist in the abstract. For any specific string s, there exists SOME procedure that produces s. The procedure might be slow, but it exists.

2. **Compute growth:** the cost to execute any given procedure decreases over time as hardware improves. Procedures that were infeasible in year Y become cheap in year Y + k for some k.

3. **Substitution:** for a digital good g whose value derives from its FUNCTION (not its identity), any functionally equivalent g' is a substitute. Functional equivalence is an equivalence relation, and the equivalence class of g is large.

4. **Convergence:** combining (1), (2), (3): for any g, the cost of a functional substitute g' eventually drops below any positive bound. Economic value bounded above by substitution cost therefore drops to zero.

## Known counterexamples (the hard part)

The conjecture as stated fails in multiple real cases. Each counterexample identifies a class of digital goods that resist the convergence:

### Network-effect goods
- **Bitcoin and similar cryptocurrencies.** The value is not in the bits but in the coordination: one specific chain that a critical mass of actors trust. A "functionally equivalent" copy (fork) is not a substitute because the network chose the original. The value comes from consensus, not from the bit pattern.
- **Platform tokens (Ethereum, etc.):** same argument. Value is coordination, not content.
- **Formal rebuttal shape:** for network-effect goods, the functional substitute g' must replicate the network, not just the bits. Replicating a network has super-linear cost in user count.

### Provenance-dependent goods
- **NFTs.** The "good" is the signed statement that a specific artist created or owned this specific token. A functional copy exists (the image can be downloaded), but the provenance cannot be duplicated without the signer.
- **Digital certificates.** A TLS certificate's value is in its signature by a trusted root. Any "functionally equivalent" cert would need the same signer.
- **Formal rebuttal shape:** the value is in the PROVENANCE RELATION, not the bits. The bits are a pointer into a trust hierarchy, and the hierarchy is the expensive part.

### Manufactured scarcity
- **Licensed software:** Adobe Photoshop, Microsoft Office. The bits are freely copyable, but legal enforcement prevents substitution. Value is maintained by contract, not by scarcity of information.
- **DRM-protected media:** the bits are gated by cryptographic enforcement. The value comes from the gating, not from the content.
- **Formal rebuttal shape:** the conjecture's precondition (no artificial scarcity) is explicitly violated. This counterexample is allowed by the conjecture, not a refutation.

### Time-sensitive goods
- **News, stock tips, weather forecasts:** the information is valuable NOW but worthless in a week. The conjecture predicts V → 0 at t → ∞, which is trivially true for time-sensitive goods but misses the point — the good had value in its window.
- **Formal note:** the conjecture is about long-run value, not short-run. Time-sensitive goods are not a counterexample to the long-run claim, but they are not INTERESTING cases of it either.

### Unique functional context
- **Custom software tailored to a specific business process:** the "functional equivalent" requires understanding the specific business, which is not in the bits. The cost of producing a substitute is the cost of business context transfer, not just compute.
- **Formal rebuttal shape:** the "functional equivalence" relation is not well-defined when the function itself depends on private context.

## The refined conjecture

Stripping out the counterexamples, the strongest defensible form is:

**Conjecture (V → 0, refined):** For a digital good g whose value derives purely from its bit pattern (not from network effects, provenance, artificial scarcity, or private context), V(g, t) → 0 as t → ∞, under the assumption of continued computational cost decrease.

In this form, the conjecture is essentially a statement that PURE content has no durable scarcity. All durable value in digital goods comes from SOMETHING OTHER than the content — coordination, trust, law, context.

This is a negative characterization of the digital economy: *digital goods are valuable only to the extent that they are not purely digital.*

## What would a proof look like

A full proof would:
1. Formalize the four exception categories (network, provenance, scarcity, context) as precise conditions.
2. Prove that outside those categories, substitution cost converges to zero.
3. Characterize "rate of convergence" — how fast does V drop in practice?
4. Test the refined conjecture against historical data (prices of software, media, information goods over 30+ years).

Step 3 is empirically tractable. Step 4 is a data analysis problem. Step 1-2 are definitional and may be where most of the work is.

## Meta-observation

The conjecture as originally stated (V → 0 for all digital goods) is FALSE because of the counterexamples. The refined conjecture (V → 0 for PURE content goods) may be TRUE but is close to tautological: it says content that is only content has no scarcity. The interesting question is whether the refined conjecture is tautological or whether it has surprising consequences (e.g., a lower bound on the fraction of digital economy that must come from non-content sources).

## Sky bridges

- **what_is_information** (S/K bifurcation) — pure content is K-content. The conjecture is that K-content has no durable economic value on its own.
- **what_is_good** (ethics of scarcity) — if all valuable content depends on artificial scarcity or trust, the ethics of digital property differ from physical property in specific ways.
- **what_is_number** (meaning vs pattern) — digital goods as finite strings, with "value" playing the role of "meaning." The same mechanism (selection, context, coordination) that gives numbers meaning also gives digital goods value.
- **conjectures/software_entropy** (adjacent) — related claim about maintenance/decay. Software_entropy is about TEMPORAL decay of function; digital_goods is about SUBSTITUTION of identity. Different axes.

## Numerical followups (to add to ../numerics/)

- `digital_good_pricing_history.py` — pull historical prices of specific digital goods (software, music, ebooks) and fit V(t) curves
- `substitute_cost_estimate.py` — model C(g', t) for a few concrete goods, project forward
- `network_effect_value.py` — formalize value-from-coordination for Bitcoin-like goods

## Status

Open. Formal claim stated; counterexamples catalogued; refined conjecture is the defensible version. The empirical test (fitting V(t) curves to historical data) is the next step. The theoretical gap is proving that the four exception categories are exhaustive — are there other ways content can have durable value?
