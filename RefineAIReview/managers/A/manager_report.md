# Manager A Report: Formal Mathematics and Core Theory

**Sub-Manager**: A
**Scope**: 7 comments on formal mathematics and core theory (C01, C02, C04, C05, C06, C15, C18)
**Date**: 2026-02-18

---

## Executive Summary

Of 7 assigned comments, **5 are GREEN** (fully resolvable with proposed edits), **2 are YELLOW** (resolvable but requiring substantive theorem/definition revisions), and **0 are RED or BLACK**. No hallucination was required. All proposed corrections are mathematically verified.

The two YELLOW items (C02 and C04) interact: they both affect the definition and properties of V_Markov. C04 identifies a timing error in the formula itself, and C02 shows the claimed inequality V_Markov ≤ V fails in general. These should be addressed together.

---

## Comment Status Table

| ID  | Priority | Status  | Summary |
|-----|----------|---------|---------|
| C01 | HIGH     | GREEN   | δ→1 claim is backwards in Remark 5.4; editorial fix, no formal results affected |
| C02 | HIGH     | YELLOW  | V_Markov ≤ V is NOT generally true; counterexample verified; theorem and abstract need revision |
| C04 | HIGH     | YELLOW  | V_Markov formula has timing error (same θ for belief and payoff); corrected formula uses double sum |
| C05 | HIGH     | GREEN   | Monotonicity ≠ supermodularity, but resolved because g doesn't depend on a₁ (exogenous transitions) |
| C06 | MEDIUM   | GREEN   | Apparent contradiction is imprecise scoping; structural vs. content claims need disentangling |
| C15 | MEDIUM   | GREEN   | "Easier to satisfy" should be "easier to verify empirically"; mathematical condition unchanged |
| C18 | LOW      | GREEN   | First-coordinate order makes incomparable states irrelevant; add explicit clarification |

---

## Detailed Assessments

### C01: Incorrect Scaling of Continuation Values — GREEN
**The error**: Remark 5.4 claims "δ→1 makes the continuation value perturbation small relative to the stage-game payoff." Under (1-δ)u₁ + δE[V], δ→1 makes continuation MORE important.
**The fix**: Replace with correct attribution: filter stability makes the perturbation vanish for large t; δ→1 (front-loading) makes the transient irrelevant.
**Impact**: Editorial only. Formal proof in Step 5 is unaffected.

### C02: Incorrect Generalization of V_Markov ≤ V — YELLOW
**The error**: The claim V_Markov(s₁*) ≤ V(s₁*) in Theorem 4.8 and the abstract is false in general. Verified counterexample: when π(G) < μ* but F(G|G) > μ*, persistence enables cooperation in good states, yielding V_Markov > V.
**The fix**: Remove the general inequality. State that the ordering depends on parameters. Add sufficient condition (V_Markov ≤ V when stationary belief induces the most favorable SR behavior). Note the paper's running example (π(G)=0.625 > μ*=0.60) DOES satisfy V_Markov ≤ V.
**Impact**: Requires revision to Theorem 4.8 statement and abstract. Core argument is unaffected (the bound ≥ V_Markov still holds regardless of the V_Markov vs V ordering). Actually strengthens the paper: V_Markov > V means persistence can sometimes BENEFIT the LR player.
**Escalation note**: Authors should verify whether any other results depend on V_Markov ≤ V.

### C04: Incorrect Formulation of V_Markov — YELLOW
**The error**: Definition 4.5 uses the same θ for SR's belief F(·|θ) and the payoff u₁(θ,...). But SR's belief at time t uses θ_{t-1} (previous state), while payoff uses θ_t (current state). Verified: formulas disagree by 0.0375 at baseline parameters.
**The fix**: Replace with double sum over (θ_{t-1}, θ_t) using the joint distribution. The corrected formula is:
V_Markov = Σ_{θ'} π(θ') · inf_{B(s₁*, F(·|θ'))} Σ_θ F(θ|θ') · u₁(θ, s₁*(θ,θ'), α₂)
**Impact**: Requires revision to Definition 4.5, abstract, and Step 5 proof. Interacts with C02.
**Escalation note**: Authors should verify all numerical claims using the corrected formula.

### C05: Invalid Sufficient Condition for Supermodularity — GREEN
**The error**: Monotonicity in θ for each a₁ does not imply supermodularity (increasing differences). The paper makes this incorrect claim in Remark 5.4.
**The fix**: In the paper's model, state transitions are exogenous (independent of actions), so g(θ_t, a₁) = δV_cont(θ_t) doesn't depend on a₁ at all. Adding a function of θ alone preserves supermodularity trivially. This is a STRONGER and CLEANER argument than the incorrect one.
**Impact**: Replace incorrect claim with correct (and simpler) argument. No formal results affected.

### C06: Contradiction in One-Shot Deviation Argument — GREEN
**The error**: "the one-shot deviation argument is identical" appears to contradict "adding this θ_t-dependent term can in principle change the OT solution."
**The fix**: These refer to different aspects: (i) the proof STRUCTURE is identical (for any fixed w, the OT logic carries over); (ii) the OBJECTIVE w = u₁ + g is different from w = u₁. Add transitional language to clarify this scoping.
**Impact**: Editorial only. Both statements are individually correct.

### C15: Incorrect Claim About Confound-Defeating Conditions — GREEN
**The error**: Claims persistence makes confound-defeating "easier to satisfy" but Section 6 shows the mathematical condition is unchanged.
**The fix**: Distinguish the mathematical condition (unchanged) from empirical verifiability (improved by persistence providing autocorrelation patterns). Replace "easier to satisfy" with "easier to verify empirically."
**Impact**: Editorial only. Verified computationally that persistence does improve statistical distinguishability (via autocorrelation gap).

### C18: Failure of Strict Supermodularity on Lifted Space — GREEN
**The error**: u₁ is constant in θ_{t-1}, appearing to violate strict supermodularity on θ̃.
**The fix**: Under the first-coordinate order (which the paper already uses), states differing only in θ_{t-1} are incomparable. Strict supermodularity imposes no condition between incomparable states. Add explicit sentence stating this.
**Impact**: One sentence addition. Mathematics already correct.

---

## Interactions Between Comments

- **C02 + C04**: Both affect V_Markov. C04 corrects the formula; C02 corrects the claimed ordering. Should be addressed together. The corrected formula from C04 may change the numerical values in C02's analysis, but the qualitative conclusion (V_Markov ≷ V is parameter-dependent) is robust.

- **C01 + C05 + C06**: All concern Remark 5.4 in sec_05_proof.tex. The remark needs a thorough rewrite addressing all three issues simultaneously: (i) correct the δ→1 claim (C01), (ii) correct the supermodularity argument (C05), (iii) clarify structural vs. content claims (C06).

- **C15 + C18**: Both concern Section 6 (supermodular case). C18 adds a clarifying sentence; C15 corrects a claim in Section 8 about the supermodular characterization.

---

## Risk Assessment

**Low risk**: C01, C05, C06, C15, C18 — editorial fixes that don't affect formal results.

**Medium risk**: C02, C04 — require changes to a theorem statement, a definition, and the abstract. The core contribution (reputation bound ≥ V_Markov) is unaffected. But all numerical claims (PayoffStationary, PayoffFiltered, PayoffGapAbsolute) should be reverified against the corrected V_Markov formula.

---

## Recommended Priority

1. **C04** (fix V_Markov formula first — other items depend on it)
2. **C02** (fix inequality claim using corrected formula)
3. **C01 + C05 + C06** (rewrite Remark 5.4 addressing all three)
4. **C15** (fix Section 8 claim)
5. **C18** (add clarifying sentence to Section 6)
