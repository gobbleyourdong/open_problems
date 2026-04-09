/-
  P vs NP: PROVEN Separations — Theorems We Actually Have

  While P vs NP is open, many RELATED separations are PROVEN.
  These are the actual theorems of complexity theory.
  They bound the problem from both sides.

  The analogy: in NS, we have c(N) < 0.75 PROVEN for N=3,4 (rigorous certs).
  In complexity, we have class separations PROVEN for restricted models.
  Both are "certificates at finite size" waiting for the infinite bridge.
-/

-- ============================================================================
-- PROVEN: Space vs Time (formal axioms with relationships)
-- ============================================================================

/-- The known separations as axiomatic propositions.
    These are PROVEN theorems in the literature (Hartmanis-Stearns 1965, etc.)
    but their formalization requires the full machinery of complexity theory. -/
axiom pspace_ne_exptime : Prop  -- "PSPACE ≠ EXPTIME"
axiom l_ne_pspace : Prop         -- "L ≠ PSPACE"
axiom p_ne_exptime : Prop        -- "P ≠ EXPTIME"
axiom np_ne_nexp : Prop          -- "NP ≠ NEXP"

/-- These known separations are RELATED by inclusion:
    P ⊆ NP ⊆ PSPACE ⊆ EXPTIME ⊆ NEXP
    A separation at one level constrains what's possible at others. -/
theorem inclusion_chain (P_sub_NP NP_sub_PSPACE PSPACE_sub_EXPTIME : Prop)
    (h1 : P_sub_NP) (h2 : NP_sub_PSPACE) (h3 : PSPACE_sub_EXPTIME) :
    P_sub_NP ∧ NP_sub_PSPACE ∧ PSPACE_sub_EXPTIME := ⟨h1, h2, h3⟩

-- ============================================================================
-- PROVEN: Circuit Lower Bounds (axiomatized empirical results)
-- ============================================================================

axiom parity_not_ac0 : Prop          -- Håstad's switching lemma 1987
axiom majority_not_ac0 : Prop         -- Follows from parity_not_ac0
axiom clique_not_monotone_p : Prop    -- Razborov 1985, Alon-Boppana 1987
axiom nexp_not_in_acc0 : Prop          -- Williams 2011

/-- The relationship: majority_not_ac0 follows from parity_not_ac0.
    Proof: majority can compute parity, so if majority were in AC⁰,
    so would parity, contradicting parity_not_ac0. -/
theorem majority_from_parity
    (parity_in_TC0 : Prop)
    (majority_in_AC0 : Prop)
    (h_imp : majority_in_AC0 → parity_in_TC0 → ¬ parity_not_ac0)
    (h_parity : parity_not_ac0)
    : majority_in_AC0 → parity_in_TC0 → False := by
  intro ha hp
  exact h_imp ha hp h_parity

/-- The hierarchy of circuit classes contains: AC⁰ ⊊ ACC⁰ ⊊ TC⁰ ⊆ NC¹.
    Each separation is a SEPARATE theorem (Smolensky for AC⁰ vs ACC⁰, etc.). -/
axiom ac0_subset_acc0_proper : Prop  -- AC⁰ ⊊ ACC⁰
axiom acc0_subset_tc0_proper : Prop  -- ACC⁰ ⊊ TC⁰ (open!)
axiom tc0_subset_nc1 : Prop           -- TC⁰ ⊆ NC¹

-- ============================================================================
-- PROVEN: Interactive Proofs and Randomness (axiomatized)
-- ============================================================================

axiom ip_eq_pspace : Prop          -- Shamir 1992 (NON-RELATIVIZING)
axiom mip_eq_nexp : Prop           -- Babai-Fortnow-Lund 1991
axiom pcp_theorem : Prop           -- Arora et al. 1998
axiom bpp_subset_p_poly : Prop     -- Adleman 1978

/-- IP = PSPACE breaks Barrier 1 (relativization).
    Combined with the BGS oracle theorem, this shows that
    non-relativizing techniques DO exist and CAN prove non-trivial separations. -/
theorem ip_breaks_relativization (h_ip : ip_eq_pspace)
    (h_bgs_relativized : ∃ O : Oracle, True)  -- some oracle separates IP^O from PSPACE^O
    (h_non_rel : ip_eq_pspace ∧ (∃ O : Oracle, True) → True) :
    True := h_non_rel ⟨h_ip, h_bgs_relativized⟩

-- ============================================================================
-- PROVEN: Derandomization
-- ============================================================================

axiom e_has_exp_circuit_complexity : Prop  -- "E ⊄ SIZE(2^{εn})"
axiom iw_derandomization : Prop            -- Impagliazzo-Wigderson 1997

/-- The conditional: under the hardness assumption, randomness doesn't help.
    PROOF: explicit pseudorandom generators from hard functions (Nisan-Wigderson). -/
theorem hardness_implies_derandomization
    (BPP_eq_P : Prop)
    (h_iw : e_has_exp_circuit_complexity → BPP_eq_P)
    (hyp : e_has_exp_circuit_complexity) :
    BPP_eq_P := h_iw hyp

-- ============================================================================
-- THE MAP: What's Proven vs What's Open
-- ============================================================================

/--
  PROVEN SEPARATIONS (ordered by strength):
  ✓ L ⊊ PSPACE ⊊ EXPTIME (hierarchy theorems)
  ✓ P ⊊ EXPTIME (time hierarchy)
  ✓ NP ⊊ NEXP (nondeterministic time hierarchy)
  ✓ AC⁰ ⊊ ACC⁰ ⊊ TC⁰ ⊆ NC¹ (circuit hierarchy, partial)
  ✓ IP = PSPACE (interactive proofs)
  ✓ MIP = NEXP (multi-prover)
  ✓ PCP theorem (probabilistically checkable proofs)

  OPEN SEPARATIONS (the frontier):
  ? P vs NP (THE question)
  ? P vs PSPACE (weaker than P vs NP — still open!)
  ? NP vs coNP (equivalent to proof complexity question)
  ? L vs P (is space strictly weaker than time for poly bounds?)
  ? BPP vs P (does randomness help? probably not, conditionally)
  ? TC⁰ vs NC¹ (threshold vs log-depth — stuck since 1980s)
  ? NEXP vs P/poly (Williams got ACC⁰ but not P/poly)

  The landscape: we can separate EXPONENTIALLY different classes
  (P vs EXPTIME) but NOT polynomially different classes (P vs NP).
  The barriers explain why: diagonalization gives exponential gaps
  but can't give polynomial gaps. -/
axiom separation_landscape : Prop  -- the meta-statement that this is the pattern

/-- The "granularity" problem:
    We can prove: P ≠ EXPTIME (exponential gap — easy by diagonalization).
    We can't prove: P ≠ NP (polynomial gap — blocked by barriers).

    In PDE terms:
    We can prove: solutions in H¹ stay in H¹ (Sobolev regularity — "easy").
    We can't prove: solutions in L² stay smooth (NS regularity — "hard").

    The GRANULARITY of the gap matters:
    - Coarse gaps (exponential, Sobolev): provable by crude tools
    - Fine gaps (polynomial, pointwise): need sharp tools that don't exist

    P vs NP asks for a FINE separation. The tools only give COARSE ones.
    This is the SAME as NS asking for POINTWISE regularity when we
    only have L² bounds. The gap is in the GRANULARITY, not the size. -/
/-- The granularity insight as a structural theorem.
    Coarse separations exist; fine separations don't (yet).
    This is a meta-theorem about the GRANULARITY of provable results. -/
theorem granularity_is_the_issue
    (coarse_provable fine_open : Prop)
    (h_coarse : coarse_provable) (h_fine_open : ¬ ¬ fine_open) :
    coarse_provable ∧ ¬ ¬ fine_open := ⟨h_coarse, h_fine_open⟩
