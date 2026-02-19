#!/bin/bash
# generate_paper.sh — Full pipeline: run analysis + extract stats + compile paper
# Updated 2026-02-19: runs analysis scripts directly instead of legacy workspace extraction.
# Usage: bash scripts/generate_paper.sh [--skip-analysis]

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PAPER_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "=== Generate Paper Pipeline ==="
echo "Paper directory: $PAPER_DIR"

# Step 1: Run analysis scripts and extract stats
if [ "$1" = "--skip-analysis" ]; then
    echo ""
    echo "--- Step 1: SKIPPED (--skip-analysis) ---"
    echo "Using existing stats.tex"
else
    echo ""
    echo "--- Step 1: Running analysis scripts ---"
    bash "$SCRIPT_DIR/run_analysis.sh"

    echo ""
    echo "--- Step 1b: Merging stats into stats.tex ---"
    cd "$PAPER_DIR"
    python3 scripts/extract_stats.py scripts/stats_raw.txt --output "$PAPER_DIR/stats.tex"
fi

# Step 2: Compile LaTeX (3 passes for cross-references)
echo ""
echo "--- Step 2: Compiling LaTeX (3 passes) ---"
cd "$PAPER_DIR"

for pass in 1 2 3; do
    echo "  Pass $pass/3..."
    if pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null 2>&1; then
        echo "  Pass $pass: OK"
    else
        echo "  Pass $pass: FAILED"
        echo "  See main.log for details."
        tail -30 main.log
        exit 1
    fi
done

# Step 3: Report results
echo ""
echo "--- Results ---"
if [ -f main.pdf ]; then
    PAGE_COUNT=$(pdfinfo main.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}' || echo "unknown")
    FILE_SIZE=$(ls -lh main.pdf | awk '{print $5}')
    echo "SUCCESS: main.pdf generated"
    echo "  Pages: $PAGE_COUNT"
    echo "  Size:  $FILE_SIZE"
else
    echo "FAILURE: main.pdf not generated"
    exit 1
fi
