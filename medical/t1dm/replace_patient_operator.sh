#!/usr/bin/env bash
# Replaces the whole word "Operator" → "Operator" across the t1dm/ tree.
#
# Usage:
#   ./replace_patient_operator.sh          # dry-run, shows what would change
#   ./replace_patient_operator.sh --apply  # actually edits files
#
# Notes:
#   - Case-sensitive, whole-word only (\bPatient\b). "operator" / "patients" / "OPERATOR" NOT touched.
#     "Patients" IS touched (the \b after t still matches before s in GNU sed's word boundary;
#      if you want only singular "Operator" as a word, change the pattern to \bPatient\b\>).
#   - Skips binary files, .pyc, .git, and hidden dirs.
#   - Known cross-dir dependency: t1dm/numerics/insulin_sensitivity_model.py defines class
#     `PatientZeroInsulin` which is imported by medical/numerics/patient_zero_simulator.py.
#     That class name contains "Operator" as a substring, NOT as a whole word, so this
#     script will NOT rename it. The import will keep working.

set -euo pipefail

TARGET_DIR="$(cd "$(dirname "$0")" && pwd)"
APPLY=0
if [[ "${1:-}" == "--apply" ]]; then APPLY=1; fi

# Find candidate files: text files only, skip .git/.lake/__pycache__/virtualenvs
mapfile -t FILES < <(
  grep -rlI --binary-files=without-match \
    --exclude-dir=.git --exclude-dir=.lake --exclude-dir=__pycache__ \
    --exclude-dir=node_modules --exclude-dir=.venv --exclude-dir=venv \
    --exclude='*.pyc' --exclude='*.png' --exclude='*.jpg' --exclude='*.pdf' \
    -iE '\bpatient\b' "$TARGET_DIR"
)

if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "No matches found."
  exit 0
fi

TOTAL=0
for f in "${FILES[@]}"; do
  COUNT=$(grep -c -iE '\bpatient\b' "$f" || true)
  TOTAL=$((TOTAL + COUNT))
  printf '%4d  %s\n' "$COUNT" "$f"
done
echo "---"
echo "Total whole-word matches (case-insensitive): $TOTAL across ${#FILES[@]} files"

if [[ $APPLY -eq 0 ]]; then
  echo
  echo "Dry run. Re-run with --apply to edit files in place."
  exit 0
fi

echo
echo "Applying replacement..."
for f in "${FILES[@]}"; do
  # GNU sed; word boundary \b works here. Three passes preserve case.
  sed -i -e 's/\bPATIENT\b/OPERATOR/g' \
         -e 's/\bPatient\b/Operator/g' \
         -e 's/\bpatient\b/operator/g' "$f"
done
echo "Done. Review with: git diff -- $TARGET_DIR"
