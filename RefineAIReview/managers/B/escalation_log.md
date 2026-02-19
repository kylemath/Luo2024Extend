# Escalation Log — Manager B

## Escalation Items

### ESCALATION 1: V(s1*) Notation Overload (C03)
- **Priority:** HIGH
- **Status:** NEEDS COORDINATION
- **Issue:** The symbol `V(s1*)` is used for two distinct objects:
  - Worst-case commitment payoff (Section 7.6, Proposition): 0.625
  - i.i.d. equilibrium payoff (comparison table, theorems): 0.777
- **Why escalated:** The notation change (`V_min`, `V_iid`, `V_Markov`) affects the entire paper, not just the worked example. Other managers' sections may reference `V(s1*)` and need to adopt consistent notation.
- **Proposed resolution:** Introduce `V_min(s1*)` for worst-case, `V_iid(s1*)` for i.i.d. equilibrium payoff, keep `V_Markov(s1*)` for Markov payoff. All managers should review their sections for `V(s1*)` usage.
- **Impact if not resolved:** Comparison table contains a false inequality (0.628 ≤ 0.625).

---

## Non-Escalated Items

### C08: BRThreshold and BRPayoff errors
- **Resolution:** Direct fix in stats.tex (0.60→0.40, 0.60→0.625)
- **Confidence:** HIGH — arithmetic is unambiguous
- **Cross-section impact:** Only affects Section 7.4 (belief-robust version)

### C09: Payoff gap vs belief gap conflation
- **Resolution:** New macro `\PayoffGapPayoff{0.149}`, text correction in Section 8.5
- **Confidence:** HIGH — arithmetic is unambiguous
- **Cross-section impact:** Section 8.5 only; `PayoffGapAbsolute` (0.094) remains valid for belief gap uses elsewhere

### C12: "Nearly identical" language
- **Resolution:** Revised caption and remark text
- **Confidence:** HIGH — descriptive language change only
- **Cross-section impact:** app_A_kl_verification.tex and sec_05_proof.tex

### C21: Missing C-payoff display
- **Resolution:** Full payoff table added to Section 7.1
- **Confidence:** HIGH — presentational improvement
- **Cross-section impact:** Section 7.1 only

---

## Stats.tex Changes Required

| Macro | Current | Proposed | Comment |
|-------|---------|----------|---------|
| `\BRThreshold` | 0.60 | 0.40 | C08: belief-robust condition |
| `\BRPayoff` | 0.60 | 0.625 | C08: V(s1*) = β/(α+β) |
| (NEW) `\PayoffGapPayoff` | — | 0.149 | C09: actual payoff gap |

Note: `\PayoffGapAbsolute` (0.094) is CORRECT for its intended purpose (belief gap formula). Do NOT change it. The issue is that Section 8.5 uses it where the payoff gap is needed.

---

## Verification Status

All 5 verification scripts: **PASS** (exit code 0)

No hallucinated values. All arithmetic independently confirmed.
