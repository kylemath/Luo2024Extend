#!/usr/bin/env bash
# ===========================================================================
# run_all.sh — Run the full Agent1206 mathematical testing framework
# ===========================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/venv"
PYTHON="${VENV_DIR}/bin/python"

echo "============================================================"
echo "Agent1206 — Mathematical Testing Framework"
echo "============================================================"
echo "Workspace: ${SCRIPT_DIR}"
echo "Python:    ${PYTHON}"
echo "Started:   $(date)"
echo "============================================================"

# Activate virtual environment
if [ -f "${VENV_DIR}/bin/activate" ]; then
    source "${VENV_DIR}/bin/activate"
    echo "Virtual environment activated."
else
    echo "ERROR: Virtual environment not found at ${VENV_DIR}"
    exit 1
fi

# Set PYTHONPATH so shared modules are importable
export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH:-}"
echo "PYTHONPATH set to: ${PYTHONPATH}"

# Run the orchestrator
echo ""
echo "Running orchestrator..."
echo "------------------------------------------------------------"
"${PYTHON}" "${SCRIPT_DIR}/orchestrator.py"

echo ""
echo "============================================================"
echo "ALL DONE — Agent1206 framework completed."
echo "Final report: ${SCRIPT_DIR}/reports/final_report.md"
echo "Finished:     $(date)"
echo "============================================================"
