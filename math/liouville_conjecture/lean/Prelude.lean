/-
  Liouville Lean Prelude — Minimal real number axioms for core Lean 4.

  Without Mathlib, ℝ doesn't exist. We axiomatize just enough to
  state the theorems: an ordered field with 0, 1, <, ≤, +, *.
  All analytical content is in the axioms of the individual files.
-/

axiom ℝ : Type
axiom ℝ_zero : ℝ
axiom ℝ_one : ℝ
noncomputable instance : OfNat ℝ 0 := ⟨ℝ_zero⟩
noncomputable instance : OfNat ℝ 1 := ⟨ℝ_one⟩
axiom ℝ_le : ℝ → ℝ → Prop
axiom ℝ_lt : ℝ → ℝ → Prop
instance : LE ℝ := ⟨ℝ_le⟩
instance : LT ℝ := ⟨ℝ_lt⟩
axiom ℝ_add : ℝ → ℝ → ℝ
axiom ℝ_mul : ℝ → ℝ → ℝ
noncomputable instance : Add ℝ := ⟨ℝ_add⟩
noncomputable instance : Mul ℝ := ⟨ℝ_mul⟩
