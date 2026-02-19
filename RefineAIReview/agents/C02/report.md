# C02: Incorrect Generalization of the Payoff Bound Inequality

## Assessment: YELLOW

## Reviewer Comment
> "V_Markov(s₁*) ≤ V(s₁*) holds generally"

The reviewer provides a counterexample: when π(G) < μ* but F(G|G) > μ* while F(G|B) < μ*, persistence enables cooperation in good states only, so V_Markov > V is possible.

## Location
- `sec_04_theorems.tex`, Theorem 4.8 (line 58): "V_Markov(s₁*) ≤ V(s₁*), with equality if and only if the game is belief-robust."
- `main.tex`, abstract (line 100): "V_Markov(s₁*) = ... ≤ V(s₁*)"

## Analysis

The reviewer is **correct**. The inequality V_Markov ≤ V does NOT hold in general.

### The Counterexample (verified)

Consider a deterrence game with parameters chosen so that:
- π(G) < μ* (SR defects under the stationary belief)
- F(G|G) = 1 - α > μ* (SR cooperates after observing G)
- F(G|B) = β < μ* (SR defects after observing B)

Under i.i.d. (stationary beliefs):
- SR believes P(θ_t = G) = π(G) < μ*, so SR always defects.
- V(s₁*) = payoff when SR always defects (low).

Under Markov (state-contingent beliefs):
- After θ_{t-1} = G: SR believes P(θ_t = G) = F(G|G) > μ*, SR cooperates.
- After θ_{t-1} = B: SR believes P(θ_t = G) = F(G|B) < μ*, SR defects.
- V_Markov = π(G) · payoff(cooperate) + π(B) · payoff(defect).

Since cooperation yields a better payoff for LR, and this occurs with probability π(G):
V_Markov > V(s₁*).

Concrete example: α = 0.6, β = 0.3.
- π(G) = β/(α+β) = 0.3/0.9 ≈ 0.333
- F(G|G) = 1-α = 0.4
- F(G|B) = β = 0.3
- With μ* = 0.35: π(G) = 0.333 < 0.35, but F(G|G) = 0.4 > 0.35

### Why the Paper's Claim Fails

The claim V_Markov ≤ V implicitly assumes that more information for the SR player always hurts the LR player. This is a form of "value of information always hurts the adversary." But this is false when the information can sometimes lead SR to take actions that are MORE favorable to LR.

In the deterrence example:
- When π(G) > μ*: SR cooperates under i.i.d. State-contingent beliefs may cause SR to defect in some states → V_Markov ≤ V. ✓
- When π(G) < μ*: SR defects under i.i.d. State-contingent beliefs may cause SR to cooperate in some states → V_Markov > V. ✗

### When DOES V_Markov ≤ V Hold?

**Sufficient condition**: V_Markov ≤ V when the i.i.d. best response is the "most favorable" for LR. Formally: when B(s₁*, π) yields the highest payoff among all possible state-contingent best responses. This holds when:
- π(G) > max_θ F(G|θ): impossible (since π is a convex combination of F(·|θ)).
- More precisely: when the stationary BR already yields cooperation, state-contingent BRs can only make things worse (defection in some states).

**The paper's running example** (α=0.3, β=0.5) DOES satisfy V_Markov ≤ V because π(G) = 0.625 > μ* = 0.60, so SR cooperates under i.i.d., and state persistence can only cause some states to trigger defection.

## What Needs to Change

1. **Theorem 4.8 (line 58)**: Remove the general claim "V_Markov ≤ V". Replace with a characterization of when V_Markov ≷ V.
2. **Abstract**: Remove or qualify "≤ V(s₁*)".
3. **Add a proposition** characterizing the sign of V - V_Markov.
4. **Remark on the running example**: Note that V_Markov ≤ V holds for the paper's baseline parameters.

## Why YELLOW (not GREEN)

The fix requires modifying a theorem statement and the abstract—substantive changes to the paper's main claims. The mathematics for the correction is clear, but the revised theorem needs careful phrasing to maintain the paper's contribution while being accurate. I provide proposed edits below, but the authors should verify that the revised statement correctly captures all cases.

## Interaction with C04

This issue interacts with C04 (timing ambiguity in V_Markov). The formula for V_Markov itself may need correction (see C04), which would affect the precise conditions under which V_Markov ≷ V. The analysis here assumes the corrected V_Markov formula from C04.
