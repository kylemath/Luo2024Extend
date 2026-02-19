# Escalation Log — Manager A

## YELLOW Escalations

### C02: V_Markov ≤ V is NOT generally true
**Status**: YELLOW — Resolvable but substantive
**What was found**: The claim V_Markov(s₁*) ≤ V(s₁*) in Theorem 4.8 (line 58) and the abstract is false in general. A valid counterexample exists: when π(G) < μ* but F(G|G) > μ*, state-contingent beliefs enable cooperation that the stationary belief does not, yielding V_Markov > V.
**What's proposed**: Remove the general inequality; characterize when V_Markov ≷ V; note the paper's running example does satisfy V_Markov ≤ V.
**What needs human verification**:
1. Confirm that no other results in the paper depend on V_Markov ≤ V (e.g., welfare comparisons, interpolation arguments in Section 8).
2. Verify that the "cost of persistence" discussion in Section 8.5 (which implicitly assumes V ≥ V_Markov) is appropriately qualified for the case V_Markov > V.
3. Decide whether to add a formal proposition characterizing the sign of V - V_Markov, or simply note the ambiguity.

### C04: Timing Error in V_Markov Formula
**Status**: YELLOW — Resolvable but substantive
**What was found**: Definition 4.5 uses the same θ for both the SR belief (F(·|θ)) and the payoff (u₁(θ,...)), conflating θ_{t-1} and θ_t. The corrected formula uses a double sum with the joint distribution over (θ_t, θ_{t-1}).
**What's proposed**: Replace Definition 4.5 with the corrected formula.
**What needs human verification**:
1. All numerical values (PayoffStationary=0.777, PayoffFiltered=0.628, PayoffGapAbsolute=0.094) should be reverified against the corrected formula. The verification script shows a 0.0375 discrepancy at baseline parameters with state-dependent payoffs.
2. The proof of Step 5 in Section 5 should be checked for consistency with the corrected formula.
3. The interaction with C02: once V_Markov is corrected, re-check the counterexample conditions.

---

## GREEN Items (No Escalation Needed)

| ID  | Summary |
|-----|---------|
| C01 | δ→1 claim is backwards; editorial fix to Remark 5.4 |
| C05 | Replace incorrect monotonicity→supermodularity claim with correct g-is-action-independent argument |
| C06 | Clarify structural vs. content claims in one-shot deviation discussion |
| C15 | Replace "easier to satisfy" with "easier to verify empirically" |
| C18 | Add sentence about incomparable states under first-coordinate order |

---

## RED / BLACK Items

**None.** All 7 comments are resolvable without fundamental issues.

---

## Cross-Comment Dependencies

```
C04 (fix V_Markov formula)
  └── C02 (fix inequality claim) — depends on corrected formula
  └── Section 8 numerical values — need reverification

C01 + C05 + C06 — all affect Remark 5.4 in sec_05_proof.tex
  └── Should be addressed together in a single rewrite of the remark

C15 + C18 — both concern supermodular characterization
  └── Independent fixes, no interaction
```
