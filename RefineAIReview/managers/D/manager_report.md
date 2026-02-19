# Manager D Report: Notation, Clarity, and Structural Issues

## Overview

Manager D handled 5 reviewer comments addressing notation, clarity, and structural issues in the paper "Extending Marginal Reputation to Persistent Markovian States." These comments range from a significant content gap (C10, HIGH) to a minor wording issue (C17, LOW), with three MEDIUM-severity items in between.

## Summary Table

| ID  | Topic | Severity | Status | Confidence |
|-----|-------|----------|--------|------------|
| C10 | Missing Monte Carlo content in Appendix A.3 | HIGH | Resolved | HIGH |
| C14 | Ambiguous $\hat{B}$ notation in Lemma 5.8 | MEDIUM | Resolved | HIGH |
| C16 | Implicit NBC application bridge | MEDIUM | Resolved | HIGH |
| C17 | Misleading lifted-state motivation | LOW | Resolved | HIGH |
| C20 | Broken cross-reference (Stackelberg/persuasion) | MEDIUM | Resolved | HIGH |

## Detailed Comment Analysis

### C10: Missing Content in Appendix A.3 — Monte Carlo Verification (HIGH)

**Issue:** Appendix A.3 contains only a figure with a caption but no explanatory text. The main text (Section 5.2) relies on the Monte Carlo results.

**Resolution:** Added a detailed paragraph before the figure describing:
- Two parallel simulation processes (Markov chain vs. i.i.d.)
- Bayesian posterior tracking and distinguishing-period counting
- Key quantitative findings (mean counts and bound comparison)
- Connection to the theoretical KL counting bound

**Verification:** Python script implements the full Bayesian learning simulation. Results confirm:
- KL counting bound holds for all 500 runs in both processes
- Markov produces slightly more distinguishing periods (65.8 vs 0.0 for i.i.d.)
- Total KL is bounded near the theoretical -log(μ₀) = 3.0 for both
- No mixing-time correction needed

**Files affected:** `app_A_kl_verification.tex`

### C14: Ambiguous Best-Response Set Notation in Lemma 5.8 (MEDIUM)

**Issue:** $\hat{B}_{\xi(\eta)}(s_1^*)$ appears without redefinition in the Markov context. Readers may confuse it with the state-contingent $B(s_1^*, F(\cdot|\theta))$.

**Resolution:** Added Remark 5.6 (`rem:B_hat_notation`) before Lemma 5.8, distinguishing:
- $\hat{B}_{\xi}(s_1^*)$: the $\xi$-confirmed best-response set from Luo-Wolitzky (posterior-based)
- $B(s_1^*, F(\cdot|\theta))$: the state-contingent Nash correspondence (filtering-based)
- Note on collapse under belief-robustness

**Verification:** Script confirms the two objects differ for the baseline parameters when belief-robustness fails (B(s₁*,F(·|G)) = Cooperate, B(s₁*,F(·|B)) = Defect, while B-hat depends on posterior proximity).

**Files affected:** `sec_05_proof.tex`

### C16: Implicit NBC Application Bridge (MEDIUM)

**Issue:** The statement "Since s₁* is not behaviorally confounded, any type with the same asymptotic signal distribution must be s₁* itself" implicitly requires filter stability + ergodicity in the Markov case.

**Resolution:** Expanded Part A of Lemma 5.7 to make the logical chain explicit:
1. KL bound → per-period signal convergence (process-independent)
2. Filter stability (Prop. A.2) → filtering distribution converges to limit
3. Ergodicity → unique stationary signal distribution per strategy
4. NBC applied to stationary distributions → type identification

**Verification:** Script demonstrates the full logical chain: filter stability with exponential forgetting (|1-α-β|^t), distinct stationary signal distributions for different strategies, and NBC satisfaction.

**Files affected:** `sec_05_proof.tex`

### C17: Misleading Lifted-State Motivation (LOW)

**Issue:** "provides a stationary distribution" implies the original chain lacks one. In fact θ_t already has π.

**Resolution:** Revised the sentence in Section 1.1 to clarify:
- Original chain has π
- Lifting encodes Markov private information into a type space
- $\tilde\rho$ on $\tilde\Theta$ plays the role of the i.i.d. signal distribution

**Verification:** Script confirms both π (for θ_t) and $\tilde\rho$ (for the lifted chain) exist and sum to 1.

**Files affected:** `sec_01_intro.tex`

### C20: Broken Cross-Reference — Stackelberg Well-Definedness (MEDIUM)

**Issue:** Section 9.5 claims Stackelberg well-definedness for persuasion games is discussed in Section 10, but Section 10.2 doesn't mention it.

**Resolution:** Added a new open-question paragraph to Section 10.2 addressing:
- Persuasion games require concavification of the sender's value function
- Under Markov dynamics, the receiver's prior varies via filtering
- Whether a state-independent Stackelberg strategy exists remains open

**Verification:** Confirmed by text search: "Stackelberg" appears only in Section 10.3 (Conclusion), not 10.2 (Open Questions). "Persuasion" and "well-defined" do not appear in sec_10_discussion.tex open questions.

**Files affected:** `sec_10_discussion.tex`

## Cross-Comment Dependencies

- **C10 ↔ Section 5.2:** The KL counting bound remark in Section 5.2 references the Monte Carlo results. The C10 fix ensures the referenced content exists.
- **C14 ↔ C16:** Both involve the proof sketch (Section 5). C14 adds notation before Lemma 5.8 (Step 4); C16 expands Lemma 5.7 (Step 3). No conflict — different subsections.
- **C20 ↔ Section 9.5:** The C20 fix makes the cross-reference in Section 9.5 accurate.

## Escalation Items

None. All five comments are resolved with high confidence and low risk. No comments require changes to mathematical results or theorems.

## Files Modified (Summary)

| File | Comments | Edit Type |
|------|----------|-----------|
| `app_A_kl_verification.tex` | C10 | Add simulation methodology text |
| `sec_05_proof.tex` | C14, C16 | Add notation remark; expand NBC argument |
| `sec_01_intro.tex` | C17 | Revise one sentence |
| `sec_10_discussion.tex` | C20 | Add open-question paragraph |
