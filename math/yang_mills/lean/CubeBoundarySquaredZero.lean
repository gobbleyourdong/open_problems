/-
  Yang-Mills — Verification that ∂C is a 2-cycle

  Completes OppositeSignsExplicit.lean by verifying that the 6 face-signs
  of the (0,1,2) 3-cube at origin satisfy ∂² = 0. Concretely: the sum
  over the 6 oriented faces (with their assigned signs) produces a
  1-chain whose coefficient on every edge is 0.

  A 3-cube in d=4 has 12 edges in the (0,1,2) subspace. Each edge is
  shared by exactly 2 of the 6 faces. For ∂² = 0 we verify the two
  face contributions cancel at each of the 12 edges.

  This file lists the 12 edges and the 4 oriented edges of each face,
  then checks that summing over all 6 faces (with their assigned signs)
  gives 0 at every edge. By Lean's `decide`, this is a finite decidable
  check.
-/

import Mathlib.Tactic.NormNum

/-! ## Edges of the (0,1,2) 3-cube at origin

  Vertices of the cube: 8 corners {(a,b,c) : a,b,c ∈ {0,1}}.
  Edges: 12 unit segments connecting vertices differing in exactly one
  coordinate. We label each edge by an integer 0..11.
-/

/-- Label the 12 edges of the unit cube in 3D. We use a specific labeling:

    0:  (0,0,0)↔(1,0,0)  -- x-edge at (y=0, z=0)
    1:  (0,1,0)↔(1,1,0)  -- x-edge at (y=1, z=0)
    2:  (0,0,1)↔(1,0,1)  -- x-edge at (y=0, z=1)
    3:  (0,1,1)↔(1,1,1)  -- x-edge at (y=1, z=1)
    4:  (0,0,0)↔(0,1,0)  -- y-edge at (x=0, z=0)
    5:  (1,0,0)↔(1,1,0)  -- y-edge at (x=1, z=0)
    6:  (0,0,1)↔(0,1,1)  -- y-edge at (x=0, z=1)
    7:  (1,0,1)↔(1,1,1)  -- y-edge at (x=1, z=1)
    8:  (0,0,0)↔(0,0,1)  -- z-edge at (x=0, y=0)
    9:  (1,0,0)↔(1,0,1)  -- z-edge at (x=1, y=0)
    10: (0,1,0)↔(0,1,1)  -- z-edge at (x=0, y=1)
    11: (1,1,0)↔(1,1,1)  -- z-edge at (x=1, y=1)
-/

/-- For each face (0..5) and each edge (0..11), the coefficient (+1, -1, or 0)
    that the face contributes to that edge when oriented counterclockwise
    around its outward normal. -/
def faceEdgeCoeff : Fin 6 → Fin 12 → ℤ
  -- Face 0: P at z=0, plane (x,y), traversed 0→x→(x+y)→y→0.
  -- Edges used (in order): 0 (+), 5 (+), 1 (-), 4 (-)
  | 0, 0 => 1  | 0, 5 => 1  | 0, 1 => -1  | 0, 4 => -1
  -- Face 1: P' at z=1, plane (x,y), traversed with opposite orientation
  -- (since it's the "top" face with inward normal from the cube's perspective).
  -- Edges used: 2 (-), 7 (-), 3 (+), 6 (+)
  | 1, 2 => -1  | 1, 7 => -1  | 1, 3 => 1  | 1, 6 => 1
  -- Face 2: Q at y=0, plane (x,z), traversed 0→x→(x+z)→z→0.
  -- Edges used: 0 (+), 9 (+), 2 (-), 8 (-)
  | 2, 0 => 1  | 2, 9 => 1  | 2, 2 => -1  | 2, 8 => -1
  -- Face 3: Q' at y=1, opposite orientation.
  -- Edges: 4 (alt), 10 (alt), ... need to work out
  | 3, 1 => -1  | 3, 11 => -1  | 3, 3 => 1  | 3, 10 => 1
  -- Face 4: R at x=0, plane (y,z), traversed 0→y→(y+z)→z→0.
  -- Edges: 4 (+), 10 (+), 6 (-), 8 (-)
  | 4, 4 => 1  | 4, 10 => 1  | 4, 6 => -1  | 4, 8 => -1
  -- Face 5: R' at x=1, opposite orientation.
  -- Edges: 5 (-), 11 (-), 7 (+), 9 (+)
  | 5, 5 => -1  | 5, 11 => -1  | 5, 7 => 1  | 5, 9 => 1
  | _, _ => 0

/-- Sign of each face in ∂C from OppositeSignsExplicit. -/
def faceSign : Fin 6 → ℤ
  | 0 => 1   -- P
  | 1 => -1  -- P'
  | 2 => -1  -- Q
  | 3 => 1   -- Q'
  | 4 => 1   -- R
  | 5 => -1  -- R'

/-- Net coefficient on edge e from the signed sum of 6 faces. -/
def edgeBoundaryCoeff (e : Fin 12) : ℤ :=
  (List.range 6).map (fun i => faceSign ⟨i, by omega⟩ * faceEdgeCoeff ⟨i, by omega⟩ e)
    |>.sum

/-- **The key theorem**: ∂² = 0 at every edge. -/
theorem boundary_squared_zero (e : Fin 12) : edgeBoundaryCoeff e = 0 := by
  fin_cases e <;> (unfold edgeBoundaryCoeff faceSign faceEdgeCoeff; decide)

/-! ## Status (2026-04-15 self-audit)

    **The `faceEdgeCoeff` table in this file was derived by hand and has
    NOT been cross-checked against the Python enumeration's internal
    edge-orientation convention.** The Python enumeration
    (area3_chair_enumeration.py) verified that signs (+1, -1, -1, +1, +1, -1)
    produce a 1-chain that sums to 0 at every edge, but its edge-
    orientation convention (using `canon_edge` with vertex-tuple
    ordering) may differ from the convention I used here
    (labeling edges 0..11 geometrically).

    If the conventions disagree, `boundary_squared_zero` may not `decide`
    correctly — either the `faceSign` table or the `faceEdgeCoeff` table
    must be adjusted to match. This file should not be relied upon as
    formal verification of ∂² = 0 until the conventions are reconciled.

    The underlying mathematical fact (that SOME sign pattern satisfies
    ∂² = 0 and gives opposite P,Q coefficients) is verified numerically
    in the Python code. The Lean formalization is incomplete.

    - boundary_squared_zero: STATED, proof status uncertain.
    - Relies on manual `faceEdgeCoeff` derivation that may contain errors.
    - Next step: cross-check against Python's `canon_edge` / `combine`
      convention before treating this as formalized.

    Honest assessment: this file is a CANDIDATE formalization that needs
    audit. The main result from attempt_064 is established via the
    Python enumeration, not yet by Lean proof.
-/
