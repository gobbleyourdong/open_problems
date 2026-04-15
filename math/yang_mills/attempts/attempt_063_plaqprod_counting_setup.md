# Attempt 063 — Setting Up A₄(⟨Tr(P)·Tr(Q)⟩) Counting Correctly

**Date**: 2026-04-15
**Phase**: 5 (Executing the outstanding calculation from attempt_062)
**Track**: analytical + numerical

## Purpose

attempt_062 identified A₄(⟨Tr(P)·Tr(Q)⟩) as the one remaining rigorous
calculation needed to close strong-coupling GC > 0. attempt_061
heuristically estimated it at 1/64 via the SU(2) link-integration
identity. This attempt sets up the correct counting framework so the
calculation is unambiguous.

## What character expansion actually says about Wilson loop products

For a SINGLE Wilson loop W in fundamental rep, the character expansion
gives
  ⟨Tr U_W⟩ = Σ_{surfaces S: ∂S = ∂W} c^{|S|} · ∏_{internal edges} (1/2)
where "internal edges" are edges of S not on ∂W. The combinatorial
picture: at every edge of ∂W, one character is supplied by the Wilson
loop and one by the adjacent surface plaquette, integrating to 1 via
∫ χ_{1/2}(U) χ_{1/2}(U^{-1}) dU = 1. At internal edges, two surface
plaquettes meet; their characters pair and give 1/2.

For ⟨Tr U_P · Tr U_Q⟩ with P, Q sharing one edge e_{PQ}:

**Character count per edge**:
- Edges of P \ {e_{PQ}} (three edges): 1 character from Tr U_P.
  Need surface plaquette touching to get k ≥ 2.
- Edges of Q \ {e_{PQ}} (three edges): 1 character from Tr U_Q. Same.
- Shared edge e_{PQ}: 2 characters (1 from Tr U_P, 1 from Tr U_Q).
  If their orientations are the same: (χ_{1/2})² at that link.
  If opposite: χ_{1/2}·χ_{1/2}(U^{-1}) = 1 pair, contributing 1/2 factor.
- All other lattice edges: 0 characters from Wilson loops.

**Orientation of P, Q on the shared edge**: for plaquettes in different
planes (P in (0,1), Q in (0,2)) both traversed counterclockwise from
the standard orientation of their respective planes, the shared edge
in direction 0 is traversed by BOTH in the +0 direction (same
orientation). So the shared-edge Wilson loop characters are in the
SAME direction.

## The leading c² contribution

The minimal surface configuration covers every link with k ≥ 2 characters:

- Choose S_P = {P} (area 1, all of P's links now get an extra character).
- Choose S_Q = {Q} (area 1).
- Now every edge of P \ {e_{PQ}} has 2 characters (1 Wilson + 1 S_P).
- Edges of Q \ {e_{PQ}}: 2 characters each.
- Shared edge: 2 Wilson + 1 S_P + 1 S_Q = 4 characters.

Edge-by-edge Haar integral:
- 6 "single-loop + single-S" edges: each contributes 1 (∫χχ⁻¹ = 1 pair).
  Wait — but S_P plaquette traverses each P-edge in some direction. The
  single-loop Wilson character is at +orientation (CCW around P); the
  S_P character is at... also +orientation (same plaquette, same
  orientation). So each of P's 4 edges has 2 forward χ_{1/2}'s. That's
  ∫ (χ_{1/2}(U))² dU = 1.
  But this includes shared edge, which we already accounted for.
- Shared edge: 4 forward χ_{1/2}'s → ∫ (χ_{1/2})⁴ dU = 2 (from
  (1/2⊗1/2)² = 2·0 + 3·1 + 1·2, two singlets).

Hmm but this doesn't match the expected (c²) result.

Actually wait — the character expansion coefficient for a plaquette is
c_{1/2} per character insertion. So if I insert 2 characters at
plaquette P (1 from Wilson loop, 1 from S_P), the weight is c_{1/2}^2?
No. The Wilson loop character is NOT a coefficient — it's a FIXED
observable. Only Boltzmann-weight insertions (surface plaquettes)
contribute c factors.

Let me re-read the correct setup.

## Correcting the setup

The character expansion for the Boltzmann weight:
  exp(β Re Tr(U)/2) = Σ_j c_j(β) · d_j · χ_j(U)
where c_j(β) = I_{2j+1}(β)/I_1(β) is the expansion coefficient. At strong
coupling, c_{1/2} ≈ β/4 = c; c_0 = 1 (from normalization); c_1 ≈ c²/2;
etc.

For a Wilson loop: ⟨χ_{1/2}(U_W)⟩ = Σ over all rep assignments to all
plaquettes × Schur-integrate links. For leading strong coupling, keep
only j=0 or j=1/2 at each plaquette.

**Surface expansion rule (rep 1/2 everywhere)**: assign j=1/2 to
plaquettes of surface S bounded by W, j=0 elsewhere. Contribution:
  c_{1/2}^{|S|} · ∏_{links} (link integral)

At ∂W edges: 1 character from W + 1 from S = 2 characters (one each)
same orientation (since W and S are oriented consistently). ∫(χ_{1/2})² dU
= 1. Factor: 1.

Wait that's wrong — the Wilson loop W and surface S have consistent
orientations so that on ∂W edges, the combined characters cancel. That
means W's character goes in ONE direction and S's goes in the OPPOSITE
direction. Then ∫ χ_{1/2}(U A) χ_{1/2}(U^{-1} B) dU = (1/2) Tr(A B)
(the link integration identity), giving a factor 1/2 per ∂W edge.

Hmm. Let me just check the standard result. For a single plaquette P:
⟨Tr U_P⟩_{strong coupling leading} = c_{1/2} · (1/2)^{4 edges factor} · (4 edges)

Actually the standard result is ⟨Tr U_P⟩ = c at leading order. So
c_{1/2}^1 · (1/2)^? = c implies the (1/2)^? factor = 1, meaning NO
factors of 1/2 from edges? But there are 4 Wilson-loop edges...

I think the resolution is the convention difference: "c = c_{1/2}" or
"c = c_{1/2} · ∫ χ_{1/2}² dU" or similar. Let me just use the standard
RESULT without re-deriving:

⟨Tr U_P⟩ = c + c⁵/64 + O(c⁷)  [per attempt_061]
⟨Tr U_P · Tr U_Q⟩ = ???

For the PRODUCT, the combinatorics involves both Wilson loops at once.

## Pragmatic approach

Rather than re-derive from scratch, use an alternative approach:
compute ⟨Tr U_P · Tr U_Q⟩ using the **direct link integration** method.

The shared link U is contained in Tr U_P and Tr U_Q. Writing
  Tr U_P = Tr(U · A_P),     U_Q = Tr(U^{εQ} · A_Q)
where ε_Q = +1 if Q traverses shared link same direction as P, = -1 if
opposite. For standard chair geometry, ε_Q = +1.

The Wilson-loop PRODUCT is
  Tr(U A_P) Tr(U A_Q)    (ε_Q = +1 case)
or
  Tr(U A_P) Tr(U^{-1} A_Q)   (ε_Q = -1 case, the "chair" orientation).

For the gauge-theory expectation, the shared link U also appears in
the Boltzmann weight via all plaquettes containing it (in d=4: 6
plaquettes, including P and Q themselves).

**Strong-coupling leading order**: approximate the Boltzmann weight
by its j=0 term (= 1) EXCEPT at the plaquettes we're summing over for
the surface. The surface plaquettes carry j=1/2 rep and contribute
c_{1/2} each.

At leading c² for ⟨Tr U_P · Tr U_Q⟩: the 2 action-plaquettes needed
are P and Q themselves (the j=1/2 insertions at P and Q from the
Boltzmann expansion). Each contributes c_{1/2}. Then the full
expectation integrates to a finite number by closing all links.

⟨Tr U_P · Tr U_Q⟩_{leading c²} = c² · (closure factor)

The "closure factor" is a specific Haar integral over all links. For
both Wilson loops P and Q each covered by their own action-plaquette:
every link of ∂P ∪ ∂Q has 2 characters (Wilson + action).
- Non-shared edges of P: 2 characters (Wilson in one direction,
  action in opposite since S = P). ∫ χ_{1/2}(U) χ_{1/2}(U^{-1}) dU =
  1/2 · Tr(id) · Tr(id) / ... = actually 1/2 as the identity trace.
  Wait.
  
Let me just use: ∫ χ_{1/2}(U g) χ_{1/2}(U^{-1} h) dU = (1/2) χ_{1/2}(g h)
(SU(2) link integration identity). For g = h = 1 (or g h = 1): (1/2) χ_{1/2}(1) = 1.

For ε_Q = +1 (same direction): shared edge has 2 Wilson characters SAME
direction + 2 action characters (S_P and S_Q both containing the edge).
Σ 4 characters same direction: ∫(χ_{1/2})⁴ dU = 2.

For ε_Q = -1 (chair orientation, opposite direction): shared edge has
Wilson_P (forward) + Wilson_Q (backward) + S_P_action (forward) +
S_Q_action (backward). Net 2 forward + 2 backward. ∫ (χ_{1/2})² (χ_{1/2}(U^{-1}))² dU
= ∫ |χ_{1/2}|⁴ dU = 2 (2 singlets).

Either way, shared-edge contribution is the same (= 2 from the 2 singlets).

OK this is very deep. Let me stop setting up and just compute the
FULL specific number through a small SymPy script.

## Next step

Write a small Python script using sympy that:
1. Represents each plaquette as an ordered tuple of 4 links.
2. Represents Wilson loops as products of link variables.
3. Computes ∫ (Wilson loops · action plaquettes) ∏ dU_link symbolically
   for small configurations.
4. Extracts the c⁴ coefficient.

This is tractable for small lattice (2-3 plaquettes) via explicit SU(2)
integration of 2x2 matrix-valued variables.

## Leading-order calculation (corrected)

Doing the explicit Haar integral:

**Key identity (SU(2), verified)**:
  ∫ Tr(UA) Tr(UB) dU = (1/2)[Tr(A) Tr(B) − Tr(AB)]
  ∫ Tr(UAUB) dU     = (1/2)[Tr(AB) − Tr(A) Tr(B)]
  (note: opposite signs; these are NOT the same integral)

**⟨Tr U_P · Tr U_Q⟩ at leading c²**: assign j=1/2 to plaquettes P and Q
(the minimum action configuration), j=0 elsewhere. Contribution:

  c² · ∫ [Tr U_P]² · [Tr U_Q]² ∏_{links} dU

Use Tr(U_P)² = χ_0(U_P) + χ_1(U_P) = 1 + χ_1(U_P), similarly for Q.

  [1 + χ_1(U_P)] · [1 + χ_1(U_Q)]
  = 1 + χ_1(U_P) + χ_1(U_Q) + χ_1(U_P)·χ_1(U_Q)

Integrate over all links:

1. ∫ 1 ∏ dU = 1.
2. ∫ χ_1(U_P) ∏ dU = 0 (integrate over any non-shared P-link, any single
   rep-1 character integral vanishes).
3. ∫ χ_1(U_Q) ∏ dU = 0 (symmetric).
4. ∫ χ_1(U_P) · χ_1(U_Q) ∏ dU: integrate over ANY non-shared link of P
   first. χ_1(U_P) depends on that link; χ_1(U_Q) doesn't. So ∫ χ_1(U_P)
   over that one link = 0. Hence overall = 0.

Therefore:
  ⟨Tr U_P · Tr U_Q⟩_{leading c²} = c² · 1 = c².

This **matches** the disconnected product ⟨Tr U_P⟩ · ⟨Tr U_Q⟩ = c · c = c²
exactly. So:

**Cov(Tr P, Tr Q)_{leading c²} = 0** for adjacent plaquettes.

## This falsifies my attempt_061 heuristic

I claimed A₄(plaq·plaq) ≈ 1/64 from the link-integration identity. That
identity applies to the BARE scalar integral ∫ Tr(UA) Tr(UB) dU, which
is (1/2)[Tr A · Tr B − Tr(AB)]. For the FULL gauge-theory expectation,
the Wilson loop characters combine with the Boltzmann-weight action
plaquettes, and by character orthogonality the extra matrix structure
(Tr AB vs Tr A Tr B) all integrates through cleanly — leaving just c²
at leading order.

So at leading c² in ⟨Tr U_P · Tr U_Q⟩, the connected correlation is
ZERO, not c²/2 as my heuristic suggested. The first nonzero connected
contribution is at higher order in c.

## Implication for GC at c⁴

GC = (1/2)⟨Tr(chair)⟩ − (1/4)⟨Tr U_P · Tr U_Q⟩.

⟨Tr(chair)⟩ = c² + (1/32)c⁴ + O(c⁶)  [attempt_061, from the unique 3-cube]
⟨Tr U_P · Tr U_Q⟩ = c² + ?·c⁴ + O(c⁶)

For the plaquette-product, the c⁴ contribution must come from surface
configurations adding 2 more action plaquettes beyond the minimal
(S_P = {P}, S_Q = {Q}). Candidates:

(a) Upgrade both S_P and S_Q to rep j=1 (cost c_1 ≈ c²/2 each), giving
    effective c² · c² = c⁴ contribution. But this changes rep content
    at plaquettes P and Q — the shared edge now has 2 Wilson-loop χ_{1/2}
    plus 2 rep-1 characters. Different integral.

(b) Keep S_P = {P}, S_Q = {Q} in rep 1/2, add TWO more rep-1/2 plaquettes
    at other lattice locations. Need these to close up every link they
    touch. Since each additional plaquette has 4 links and those links
    need 2+ chars, typically need them adjacent to existing surface.

(c) Single 4-plaquette surface bounded by the "double" 1-chain
    ∂P + ∂Q (with shared edge doubled). This is the "connected chair-like"
    sector, analogous to ⟨Tr(chair)⟩'s area-4 surface.

Option (c) is the most likely source of a nonzero A₄(plaq·plaq). It
requires 4-plaquette 2-chains with boundary = ∂P + ∂Q (with shared edge
coefficient 2). These are DIFFERENT from chair-bounded 4-plaquette
surfaces (where the shared edge coefficient is 0, not 2).

## Next step

Enumerate area-4 2-chains with boundary = ∂P + ∂Q (shared edge
coefficient 2). This is a modification of area3_chair_enumeration.py's
target boundary. If count = 2 (similar to chair case, via some 3-cube
structure) and Schur weights combine to +1/64, the GC c⁴ result
(1/2)(1/32) − (1/4)(1/64) = 3/256 > 0 is preserved.

If count differs: the GC sign at c⁴ hinges on this direct calculation.

## Status (end of this cron fire)

- Confirmed ⟨Tr U_P · Tr U_Q⟩_{leading c²} = c² (disconnected).
- attempt_061's A₄(plaq·plaq) ≈ 1/64 heuristic does NOT hold at leading
  c² (connected = 0 there).
- A₄(plaq·plaq) as the c⁴ coefficient is still open; requires
  enumerating 4-plaquette surfaces bounded by ∂P + ∂Q with coefficient
  2 on the shared edge.
- Next cron fire: extend the enumerator to handle "double boundary on
  shared edge" target.
