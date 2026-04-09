#!/bin/bash
# Prep the certificate data for GitHub (split large files, copy to repo)
# Run AFTER the overnight certification completes.
#
# Usage: bash ns_blowup/prep_repo.sh

set -e
REPO=/home/jb/ns-regularity-sos
CERTS=ns_blowup/certs
MAX_MB=95

echo "=== Preparing certificate data for GitHub ==="
echo ""

# Verify the run completed
for f in N3_K18.json N4_K9.json N5_K3.json N6_K3.json N7_K3.json N8_K3.json N9_K3.json N10_K3.json N11_K3.json N12_K3.json N13_K3.json; do
    if [ ! -f "$CERTS/$f" ]; then
        echo "MISSING: $CERTS/$f — run not complete yet?"
        exit 1
    fi
done
echo "All 11 certificate files present."

# Clear old mock data from repo
rm -f $REPO/certs/*.json
echo "Cleared mock data from repo."

# Copy and split
for f in $CERTS/N*.json; do
    fname=$(basename $f)
    size_mb=$(du -m "$f" | cut -f1)

    if [ "$size_mb" -gt "$MAX_MB" ]; then
        # Split into chunks
        n_chunks=$(( (size_mb / MAX_MB) + 1 ))
        echo "Splitting $fname ($size_mb MB) into $n_chunks chunks..."

        # Use split with numeric suffixes
        split -b ${MAX_MB}m -d --additional-suffix=.json "$f" "$REPO/certs/${fname%.json}.part"

        # Rename: N3_K18.part00.json -> N3_K18.part00.json (already correct)
        echo "  Created: $(ls $REPO/certs/${fname%.json}.part* | wc -l) chunks"
    else
        # Small enough — copy directly
        cp "$f" "$REPO/certs/$fname"
        echo "Copied $fname ($size_mb MB)"
    fi
done

echo ""
echo "=== Repo certs directory ==="
ls -lh $REPO/certs/
echo ""

# Count total data
total=$(du -sh $REPO/certs/ | cut -f1)
n_files=$(ls $REPO/certs/*.json | wc -l)
echo "Total: $total in $n_files files (all under ${MAX_MB}MB)"
echo ""
echo "Next: update verify.py to handle chunked files, then push."
