#!/bin/bash
# Full SOS certification run — generates all certificates for the NS regularity proof
# Estimated runtime: ~8-9 hours total on DGX Spark
# Output: ns_blowup/certs/N{3..13}_K{max}.json
#
# Run: nohup bash ns_blowup/run_full_certification.sh > ns_blowup/certification.log 2>&1 &

set -e
cd ~/ComfyUI/CelebV-HQ

echo "================================================================"
echo "NS Key Lemma — Full SOS Certification"
echo "Starting: $(date)"
echo "================================================================"

# Run test suite first
echo ""
echo "=== Running test suite ==="
python3 -u ns_blowup/test_certifier.py
echo ""

# N=3, K²≤18 — exhaustive (6,471 configs, ~90 min)
echo "=== N=3, K²≤18 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 3 --K2max 18 --save-certs

# N=4, K²≤9 — exhaustive (521,855 configs, ~7 hours)
# Uses --resume to survive restarts (checkpoints every 10%)
echo ""
echo "=== N=4, K²≤9 (exhaustive, resumable) ==="
python3 -u ns_blowup/sos_certifier.py --N 4 --K2max 9 --save-certs --resume

# N=5, K²≤3 — exhaustive (1,287 configs, ~3 min)
echo ""
echo "=== N=5, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 5 --K2max 3 --save-certs

# N=6, K²≤3 — exhaustive (1,716 configs, ~20 min)
echo ""
echo "=== N=6, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 6 --K2max 3 --save-certs

# N=7, K²≤3 — exhaustive (1,716 configs, ~30 min)
echo ""
echo "=== N=7, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 7 --K2max 3 --save-certs

# N=8, K²≤3 — exhaustive (1,287 configs, ~40 min)
echo ""
echo "=== N=8, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 8 --K2max 3 --save-certs

# N=9, K²≤3 — exhaustive (715 configs, ~30 min)
echo ""
echo "=== N=9, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 9 --K2max 3 --save-certs

# N=10, K²≤3 — exhaustive (286 configs, ~15 min)
echo ""
echo "=== N=10, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 10 --K2max 3 --save-certs

# N=11, K²≤3 — exhaustive (78 configs, ~5 min)
echo ""
echo "=== N=11, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 11 --K2max 3 --save-certs

# N=12, K²≤3 — exhaustive (13 configs, ~2 min)
echo ""
echo "=== N=12, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 12 --K2max 3 --save-certs

# N=13, K²≤3 — exhaustive (1 config, ~1 min)
echo ""
echo "=== N=13, K²≤3 (exhaustive) ==="
python3 -u ns_blowup/sos_certifier.py --N 13 --K2max 3 --save-certs

# Verify all certificates
echo ""
echo "=== Verifying all certificates ==="
python3 -u ns_blowup/verify_certificates.py ns_blowup/certs/

echo ""
echo "================================================================"
echo "Certification complete: $(date)"
echo "Certificates in: ns_blowup/certs/"
ls -lh ns_blowup/certs/
echo "================================================================"
