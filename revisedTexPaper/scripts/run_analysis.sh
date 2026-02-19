#!/usr/bin/env bash
# run_analysis.sh — Run all 7 analysis scripts and extract stats.
# Updated 2026-02-19: uses system python3, corrected for simultaneous-move timing.
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="python3"

echo "=== Running analysis scripts ==="
echo "Script dir: $SCRIPT_DIR"
echo "Python: $($PYTHON --version 2>&1)"
echo ""

mkdir -p "$SCRIPT_DIR/../figures"

STATS_FILE="$SCRIPT_DIR/stats_raw.txt"
> "$STATS_FILE"

SCRIPTS=(
    "analysis_beliefs.py"
    "analysis_state_reveal.py"
    "analysis_kl_bound.py"
    "analysis_filter.py"
    "analysis_ot.py"
    "analysis_nash.py"
    "analysis_monotonicity.py"
)

FAILED=0
for script in "${SCRIPTS[@]}"; do
    echo "--- Running $script ---"
    if "$PYTHON" "$SCRIPT_DIR/$script" 2>&1 | tee -a "$STATS_FILE"; then
        echo "  ✓ $script completed"
    else
        echo "  ✗ $script FAILED (exit code $?)"
        FAILED=$((FAILED + 1))
    fi
    echo ""
done

echo "=== Extracting stats ==="
"$PYTHON" "$SCRIPT_DIR/extract_stats.py" "$STATS_FILE"

echo ""
echo "=== Summary ==="
echo "Scripts run: ${#SCRIPTS[@]}"
echo "Failures: $FAILED"
echo "Stats file: $STATS_FILE"
echo "Figures directory: $SCRIPT_DIR/../figures/"
ls -la "$SCRIPT_DIR/../figures/" 2>/dev/null || echo "(no figures found)"
