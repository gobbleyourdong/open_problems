/-
  Axiom verification — run this to confirm clean axioms.

  Expected output for each theorem:
    depends on axioms: [propext, Classical.choice, Quot.sound]

  If `sorryAx` appears, the proof is incomplete.
  If any other axiom appears, the proof uses non-standard assumptions.
-/

import DepletionProof.SingleMode

#print axioms twiceStrainForm_eq
#print axioms single_mode_orthogonality
#print axioms single_mode_orthogonality_unconditional
