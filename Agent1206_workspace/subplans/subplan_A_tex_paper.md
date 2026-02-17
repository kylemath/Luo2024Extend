# Subplan A: Modular LaTeX Paper + Build Automation

## Deliverables
1. `revisedTexPaper/main.tex` — master file that \input's section files
2. `revisedTexPaper/sections/` — one .tex file per section
3. `revisedTexPaper/build.sh` — compiles PDF
4. `revisedTexPaper/scripts/extract_stats.py` — pulls stats from analysis into \newcommand macros
5. `revisedTexPaper/scripts/run_analysis.sh` — runs all 7 consolidated analysis scripts
6. `revisedTexPaper/scripts/generate_paper.sh` — runs analysis → extracts stats → compiles PDF
7. 7 consolidated analysis scripts in `revisedTexPaper/scripts/`

## Section Structure
- sec_01_intro.tex
- sec_02_model.tex
- sec_03_belief_robustness.tex (NEW — the fix)
- sec_04_theorems.tex
- sec_05_proof.tex
- sec_06_supermodular.tex
- sec_07_example.tex
- sec_08_interpolation.tex
- sec_09_methodology.tex
- sec_10_discussion.tex
- app_A_kl_verification.tex
- app_B_computational.tex
