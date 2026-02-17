#!/usr/bin/env bash
# run_analysis.sh — Run all 7 analysis scripts and extract stats.
# Uses the project venv Python interpreter.
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON="/Users/kylemathewson/mathTest/Agent1206_workspace/venv/bin/python"

echo "=== Running analysis scripts ==="
echo "Script dir: $SCRIPT_DIR"
echo "Python: $PYTHON"
echo ""

# Ensure figures directory exists
mkdir -p "$SCRIPT_DIR/../figures"

# Collect all STAT output
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
