#!/bin/bash
# build.sh — Compile the paper (without rerunning analysis)
# Usage: bash build.sh

set -e

PAPER_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Building Paper ==="
echo "Directory: $PAPER_DIR"
cd "$PAPER_DIR"

# Compile LaTeX (3 passes for cross-references)
for pass in 1 2 3; do
    echo "Pass $pass/3..."
    if pdflatex -interaction=nonstopmode -halt-on-error main.tex > /dev/null 2>&1; then
        echo "  OK"
    else
        echo "  FAILED on pass $pass"
        echo ""
        echo "Error details (last 40 lines of main.log):"
        tail -40 main.log
        exit 1
    fi
done

# Report results
echo ""
if [ -f main.pdf ]; then
    PAGE_COUNT=$(pdfinfo main.pdf 2>/dev/null | grep "Pages:" | awk '{print $2}' || echo "unknown")
    FILE_SIZE=$(ls -lh main.pdf | awk '{print $5}')
    echo "SUCCESS: main.pdf"
    echo "  Pages: $PAGE_COUNT"
    echo "  Size:  $FILE_SIZE"
else
    echo "FAILURE: main.pdf was not generated"
    exit 1
fi
