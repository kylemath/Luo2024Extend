# Manager B Report: Numerical Errors and the Worked Example

**Manager:** Sub-Manager B
**Scope:** Comments C03, C08, C09, C12, C21
**Date:** February 18, 2026

---

## Executive Summary

All five reviewer comments in this group identify genuine issues. Three involve clear arithmetic or logical errors (C08, C09, C03), one involves misleading language (C12), and one is a presentational gap (C21). No comment was rejected. The errors concentrate in the worked example (Section 7) and the interpolation discussion (Section 8.5), suggesting these sections were not cross-checked against the formal results.

**Critical finding:** The errors in C08 and C09 are unambiguous arithmetic mistakes that must be corrected. C03 reveals a deeper notational issue (overloading of `V(s1*)`) that requires careful resolution. C12 and C21 are lower-severity fixes that improve clarity.

---

## Comment-Level Summary

| ID | Severity | Assessment | Status | Core Issue |
|----|----------|------------|--------|------------|
| C03 | HIGH | YELLOW | Resolved with proposed edits | Notational overload: V(s1*)=0.625 (worst-case) vs 0.777 (equilibrium) |
| C08 | HIGH | RED | Resolved with proposed edits | False inequality: 0.60 < 0.50 stated, 0.60 > 0.50 true |
| C09 | HIGH | RED | Resolved with proposed edits | Wrong arithmetic: 0.777−0.628=0.094 should be 0.149 |
| C12 | MEDIUM | GREEN | Resolved with proposed edits | "Nearly identical" for means differing 57% |
| C21 | LOW | GREEN | Resolved with proposed edits | D-payoffs only shown; A dominates F in state B without C-payoffs |

---

## Detailed Findings

### C03: Contradictory i.i.d. Benchmark Values (YELLOW)

**Issue:** Paper uses `V(s1*)` for two different quantities: the worst-case commitment payoff (0.625, against D) and the i.i.d. equilibrium payoff (0.777, with SR cooperation). The comparison table's claim `V_Markov ≤ V(s1*)` is violated when `V(s1*) = 0.625` (since `V_Markov = 0.628 > 0.625`) but satisfied when `V(s1*)` means the equilibrium payoff `0.777`.

**Resolution:** Introduce distinct notation: `V_min(s1*)` for the worst-case bound (0.625), `V_iid(s1*)` for the i.i.d. equilibrium payoff (0.777), and `V_Markov(s1*)` for the Markov payoff (0.628). The ordering `V_min ≤ V_Markov ≤ V_iid` holds correctly.

**Assessment:** YELLOW — the underlying mathematics is correct but the notation creates a genuine contradiction in the comparison table. Requires careful revision of Sections 7.6, 7.7, and 7.9.

### C08: Arithmetic Error in Belief-Robust Condition (RED)

**Issue:** Section 7.4 states `μ* = 0.60 < β = 0.50`, but `0.60 > 0.50`. The belief-robust condition requires `μ* ≤ min_θ F(G|θ) = β = 0.50`, so `μ* = 0.60` violates it. Additionally, `BRPayoff = 0.60` should be `0.625 = β/(α+β)`.

**Resolution:** Change `BRThreshold` from `0.60` to `0.40` and `BRPayoff` from `0.60` to `0.625` in stats.tex. All downstream text updates automatically via macros.

**Assessment:** RED — unambiguous arithmetic error. Root cause likely copy-paste from the SRThreshold value.

### C09: Arithmetic Error and Variable Confusion (RED)

**Issue:** Section 8.5 writes `0.777 - 0.628 = 0.094`, but `0.777 - 0.628 = 0.149`. The value `0.094` is the *belief gap* (TV distance from the formula `2αβ|1-α-β|/(α+β)²`), not the *payoff gap*. Additionally, "23.7% of the i.i.d. payoff" is wrong: `0.149/0.777 = 19.2%`, while `0.149/0.628 = 23.7%` (percentage of the Markov payoff).

**Resolution:** Add a `\PayoffGapPayoff{0.149}` macro, fix the subtraction in Section 8.5, correct the percentage base, and add a clarifying sentence distinguishing belief gap from payoff gap.

**Assessment:** RED — three distinct errors in one sentence. The `PayoffGapAbsolute` macro stores a belief gap but is used where a payoff gap is needed.

### C12: "Nearly Identical" Claim for Divergent Means (GREEN)

**Issue:** The KL bound figure caption and Section 5.2 remark describe Markov and i.i.d. distributions as "nearly identical," but means are 8.1 vs 12.7 (57% relative difference). The bound validity is unaffected (both << 921).

**Resolution:** Replace "nearly identical" with accurate language: "both well below the analytical bound" with explicit mean values cited.

**Assessment:** GREEN — language fix only. Mathematical claim (KL bound extends unchanged) is fully supported.

### C21: Missing C-Payoffs Make Strategy Appear Suboptimal (GREEN)

**Issue:** Only D-conditional payoffs are shown. Against D alone, `u1(B,A) = 0.4 > u1(B,F) = 0`, making `s1*(B) = F` look wrong. The full payoff matrix (including C-column) is needed to justify the Stackelberg strategy.

**Resolution:** Display the full payoff matrix with cooperation gain parameter `g`, and add a clarifying note that the Stackelberg strategy maximizes reputation payoffs (confound-defeating), not per-period payoffs against defection.

**Assessment:** GREEN — presentational gap. The referenced Luo & Wolitzky source has the full matrix, but readers should not need to look there.

---

## Cross-Cutting Issues

### 1. Macro hygiene in stats.tex
The `PayoffGapAbsolute` macro stores a belief gap (0.094) but its name suggests a payoff gap. Several macros (`BRThreshold`, `BRPayoff`) have incorrect values. A systematic audit of all stats.tex macros against their usage contexts is recommended.

### 2. Notational consistency for V(s1*)
The overloading of `V(s1*)` affects multiple sections (7.3, 7.6, 7.7, 7.9, 8.5). A global notation pass should ensure consistent usage throughout the paper.

### 3. Worked example cross-checking
Three of five errors (C03, C08, C09) are in the numerical worked example. This section was likely constructed by a different agent or at a different time from the formal results, and the two were not cross-validated. Future revisions should include automated cross-checks between symbolic formulas and numerical instantiations.

---

## Escalation Items

### ESCALATED: C03 notation (YELLOW)
The resolution requires a judgment call about notation: whether to introduce `V_min`, `V_iid`, and `V_Markov` as separate symbols, or to redefine `V(s1*)` consistently. This affects the entire paper and should be coordinated with the other managers.

### NOT ESCALATED: C08, C09 (RED but clear fix)
These have unambiguous corrections that can be applied directly to stats.tex.

### NOT ESCALATED: C12, C21 (GREEN)
Minor language and presentation fixes with no impact on formal results.

---

## Verification

All five verification scripts run successfully (exit code 0). Each script independently confirms the errors identified by the reviewers and validates the proposed corrections.

| Script | Result | Key Finding |
|--------|--------|-------------|
| C03/verification.py | PASS | Confirms V_Markov(0.628) > V(s1*)(0.625) violation |
| C08/verification.py | PASS | Confirms 0.60 > 0.50, proposes BRThreshold=0.40 |
| C09/verification.py | PASS | Confirms 0.777−0.628=0.149≠0.094; 23.7%=0.149/0.628 |
| C12/verification.py | PASS | Confirms 57% mean difference; both <1.5% of bound |
| C21/verification.py | PASS | Confirms A dominates F in state B against D-payoffs |
