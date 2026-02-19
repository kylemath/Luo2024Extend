# C05: Invalid Sufficient Condition for Supermodularity

## Assessment: GREEN

## Reviewer Comment
> "g(θ_t, a₁, h_t) is supermodular in (θ_t, a₁) whenever V_cont is increasing in θ_t for each a₁"

The reviewer correctly notes that monotonicity in θ_t for each a₁ does NOT imply increasing differences in (θ, a₁). Supermodularity requires:

g(θ_H, a_H) - g(θ_H, a_L) ≥ g(θ_L, a_H) - g(θ_L, a_L)

which is strictly stronger than g(θ_H, a₁) ≥ g(θ_L, a₁) for each a₁.

## Location
`sec_05_proof.tex`, Remark 5.4, line 72.

## Analysis

### The Mathematical Error

The paper claims in Remark 5.4:
> "g(θ_t, a₁, h_t) is supermodular in (θ_t, a₁) whenever V_cont is increasing in θ_t for each a₁ (which holds when higher states have higher continuation values)"

This is mathematically incorrect. A function f(x,y) can be increasing in x for each y without having increasing differences. Simple counterexample:

| | a_L | a_H |
|---|---|---|
| θ_L | 2 | 5 | (difference = 3)
| θ_H | 9 | 10 | (difference = 1)

This is monotone in θ for each a but has DECREASING differences (1 < 3).

### The Resolution: Action-Independence of State Transitions

However, the error is **recoverable** because in the paper's model, state transitions are exogenous (do not depend on actions). Specifically:

- The Markov chain θ_t evolves according to F(·|θ_{t-1}), independent of actions.
- Therefore, E[V(θ_{t+1}) | θ_t, a₁] = E[V(θ_{t+1}) | θ_t] = Σ_{θ'} F(θ'|θ_t) V(θ')

This means g(θ_t, a₁, h_t) = δ V_cont(θ_t) — **it does not depend on a₁ at all**.

When g depends only on θ (not on a₁), adding g to u₁ preserves supermodularity trivially:

[u₁(θ_H, a_H) + g(θ_H)] - [u₁(θ_H, a_L) + g(θ_H)] = u₁(θ_H, a_H) - u₁(θ_H, a_L)
[u₁(θ_L, a_H) + g(θ_L)] - [u₁(θ_L, a_L) + g(θ_L)] = u₁(θ_L, a_H) - u₁(θ_L, a_L)

The g terms cancel! The increasing differences of u₁ are preserved exactly.

### Caveat: Signal-Dependent Continuation

There IS a subtlety: in the one-shot deviation analysis, V_cont could depend on a₁ through the **signal** that a₁ generates (since the signal reveals a₁ to future SRs). If the deviation changes the signal, it changes future beliefs and hence future equilibrium play.

However, in the confound-defeating framework, the relevant comparison is between strategies that generate the SAME signal distribution (that's what confound-defeating means). So the continuation through signal effects is identical, and g effectively depends only on θ.

## Resolution

Replace the incorrect claim about monotonicity implying supermodularity with the correct argument: in the paper's model, g does not depend on a₁ (because state transitions are action-independent), so adding g to u₁ preserves supermodularity trivially without needing any condition on g.

This is a stronger and cleaner argument than the incorrect one.
