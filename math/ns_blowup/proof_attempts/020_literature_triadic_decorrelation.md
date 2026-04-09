---
source: Web/arXiv search round 4
type: Literature — triadic interactions and decorrelation
status: FOUND RELEVANT FRAMEWORK but no direct decorrelation bound
---

## Key Finding: Helical Decomposition

### "Disentangling the triadic interactions in NS" (arXiv 1510.09006)
Decomposes the NS nonlinearity into classes of triadic interactions
based on helicity content. Different triad classes have DIFFERENT
energy transfer properties.

**Critical insight:** When triads are restricted to modes with the
same helicity sign, the energy cascade REVERSES (goes to large scales).
The forward cascade (small scales, relevant for blowup) requires
triads with MIXED helicity signs.

**Connection to us:** Mixed-helicity triads have intrinsic cancellation
because the helicity signs fight each other. This is a STRUCTURAL
source of decorrelation — not random phases, but helical geometry.

### "Nonlinear phase synchronization" (arXiv 2507.14142, July 2025)
Shows that phase dynamics from neighboring triads influence each other.
Phase SYNCHRONIZATION is needed for coherent energy transfer.
Random phases = no transfer.

**Connection:** If phase synchronization decays with the number of
modes (which our data shows), the energy transfer weakens.
The "decorrelation" we need isn't spatial — it's PHASE decorrelation
in Fourier space.

### "Phase dynamics and energy flux" (arXiv 2507.03397, July 2025)
The dynamics of complex Fourier velocity PHASES determine the flux.
The phase ordering is what creates the cascade.

**KEY INSIGHT:** Our infection ratio measures where the phases are
ordered (stretching > dissipation) vs disordered (dissipation wins).
As N increases, maintaining phase order across MORE modes becomes
exponentially harder. The fraction of ordered points = infection ratio.

## New Proof Idea: Phase Entropy Argument

The stretching at a point requires PHASE COHERENCE across triads.
Define the "phase entropy" at point x as:
```
H(x) = -Σ_triads p_t log(p_t)
```
where p_t is the probability of triad t being in the "stretch > dissip" state.

For independent triads: H(x) = N_triads × h_single
where h_single is the per-triad entropy.

The fraction of points where Q(x) > 0 requires H(x) < H_critical.
By the entropy concentration theorem:
```
P(H < H_critical) ≤ exp(-c (H_mean - H_critical)²)
```

If H_mean grows with N (more triads = more entropy = more disorder),
then P(Q > 0) decays exponentially.

This is essentially the alignment-rarity argument (ChatGPT) rephrased
in information-theoretic language. The phase entropy grows with N because
each new mode adds entropy to the triadic interactions.

## Assessment
The helical decomposition literature confirms that:
1. Triadic interactions have geometric structure (helicity)
2. Mixed-helicity triads provide cancellation
3. Phase coherence is required for forward cascade
4. Phase coherence becomes harder with more modes

All of these support our observation. The proof gap (decorrelation)
maps to PHASE DECORRELATION in Fourier space, not spatial decorrelation.

## The Partial Proof (Updated)
What we can state:
1. Single-mode: zero stretching (PROVEN)
2. Per-triad alignment probability ~ 0.88 (COMPUTED)
3. Phase coherence across N triads: probability ~ 0.88^N (IF INDEPENDENT)
4. Independence follows from the Biot-Savart cross-product mixing helicities
5. Result: frac ~ exp(-N/8) (MATCHES DATA)

Gap: step 4 — proving the Biot-Savart cross product decorrelates phases.
The helical decomposition papers show this is PHYSICALLY true but don't
provide the quantitative bound we need.

## Next Steps
1. Read arXiv 1510.09006 for the helical triad classification
2. Check if the mixed-helicity cancellation provides a decorrelation bound
3. The "phase entropy" argument might be formalizable using
   information-theoretic tools (mutual information bounds)
