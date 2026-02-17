#!/bin/bash
# generate_paper.sh — Full pipeline: extract stats + compile paper
# Usage: bash scripts/generate_paper.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PAPER_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "=== Generate Paper Pipeline ==="
echo "Paper directory: $PAPER_DIR"

# Step 1: Extract statistics from SA reports
echo ""
echo "--- Step 1: Extracting statistics ---"
cd "$PAPER_DIR"
python3 scripts/extract_stats.py \
    --workspace "$PAPER_DIR/../Agent1206_workspace" \
    --output "$PAPER_DIR/stats.tex"

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
        # Show last 30 lines of log for debugging
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
