#!/bin/bash
# Sync all data from H200 RunPod to Spark
# Run every 30 min: cron or watch -n 1800 ./sync_h200.sh
#
# UPDATE THESE for each new pod:
HOST="root@103.207.149.109"
PORT="18976"
KEY="~/.ssh/id_ed25519"
DEST=~/ComfyUI/CelebV-HQ/ns_blowup/results/h200_run2/

mkdir -p $DEST
SCP="scp -o StrictHostKeyChecking=no -P $PORT -i $KEY"

echo "[$(date)] Syncing from $HOST:$PORT..."

# Grab ALL json and log files
$SCP $HOST:/root/*.json $DEST 2>/dev/null
$SCP $HOST:/root/*.log $DEST 2>/dev/null

# Grab results from each GPU worker
for gpu in 0 1 2 3 4 5 6 7; do
    $SCP $HOST:/root/gpu${gpu}/*.json $DEST 2>/dev/null
done

echo "[$(date)] Files:"
ls -lt $DEST/*.json 2>/dev/null | head -20
echo "[$(date)] Done."
