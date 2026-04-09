/-
  MedThermo — Medical Thermodynamics Library

  Lean 4 formalization of biological systems as dynamical systems
  grounded in thermodynamic principles.

  Architecture:
  - Thermodynamics: Free energy, chemical kinetics, non-equilibrium steady states
  - CellBiology: R > D inequality, viral persistence, immune privilege
  - Pharmacology: Drug PK, IC50/Hill equation, lysosomotropic accumulation
  - Theorems: The crown jewels — inequality reversal, clearance order, HLA paradox

  Part of the systematic approach campaign: <private repo>
-/

import MedThermo.Thermodynamics.ChemicalKinetics
import MedThermo.CellBiology.ReplicationDestruction
import MedThermo.Pharmacology.IC50
import MedThermo.Theorems.HLAParadox
import MedThermo.Theorems.ClearanceOrder
import MedThermo.Theorems.InequalityReversal
import MedThermo.CellBiology.ViralPersistence
import MedThermo.Thermodynamics.FreeEnergy
import MedThermo.CellBiology.ImmunePrivilege
-- import MedThermo.Thermodynamics.NonEquilibrium   -- planned: dissipative structures
import MedThermo.Pharmacology.Lysosomotropic
