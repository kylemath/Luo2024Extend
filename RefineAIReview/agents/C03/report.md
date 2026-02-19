# C03: Contradictory i.i.d. Benchmark Values

## Severity: HIGH
## Self-Assessment: YELLOW

## Reviewer Concern

The paper uses two different "i.i.d. benchmarks":
- Section 7.6 computes `V(s1*) = π(G)·u1(G,A) + π(B)·u1(B,F) = 0.625×1 + 0.375×0 = 0.625`
- Section 7.7 and Figure 2 give "Stationary beliefs" payoff as `0.777`

Additionally, `V_Markov = 0.628` and `V(s1*) = 0.625` gives `V_Markov > V(s1*)`, violating the stated relationship `V_Markov ≤ V(s1*)`.

## Independent Verification

### Arithmetic checks (all confirmed):
- `π(G) = β/(α+β) = 0.5/0.8 = 0.625` ✓
- `π(B) = α/(α+β) = 0.3/0.8 = 0.375` ✓
- `V(s1*) [against D] = 0.625×1 + 0.375×0 = 0.625` ✓
- `V(s1*) = β/(α+β) = 0.625` ✓ (matches Proposition formula)

### The three distinct quantities:

| Quantity | Value | Definition | SR behavior |
|----------|-------|------------|-------------|
| (A) Worst-case commitment payoff | 0.625 | `π(G)·u1(G,A,D) + π(B)·u1(B,F,D)` | SR always defects |
| (B) i.i.d. equilibrium payoff | 0.777 | `π(G)·u1(G,A,C) + π(B)·u1(B,F,C)` | SR cooperates (stationary belief π(G) > μ*) |
| (C) Markov equilibrium payoff | 0.628 | `π(G)·u1(G,A,C) + π(B)·u1(B,F,D)` | SR cooperates in G, defects in B |

### The ordering issue:
- Comparison table (Section 7.9) states: `V_Markov ≤ V(s1*)`
- If `V(s1*)` means (A) = 0.625: then `0.628 > 0.625` → **VIOLATED**
- If `V(s1*)` means (B) = 0.777: then `0.628 ≤ 0.777` → **SATISFIED**

## Root Cause

The paper overloads the notation `V(s1*)` with two meanings:
1. **Proposition 1 / Section 7.6**: `V(s1*) = β/(α+β) = 0.625` — the worst-case Stackelberg commitment payoff (minimum over all SR responses, using D-row payoffs)
2. **Comparison table / Theorems**: `V(s1*)` = the commitment payoff against the SR equilibrium best response — which equals 0.777 under i.i.d. beliefs (SR cooperates since π(G) > μ*)

These are genuinely different economic objects. The 0.625 is the **floor** guarantee regardless of SR behavior. The 0.777 is the **equilibrium** payoff when SR cooperates due to beliefs exceeding the threshold.

## Proposed Resolution

1. **Clarify Section 7.6**: Rename the 0.625 value to avoid conflating it with the theorem-level `V(s1*)`. Label it as the "worst-case commitment payoff" or "Stackelberg payoff against defection."
2. **Add a bridging paragraph** in Section 7.7 explaining the three quantities and their ordering: `V_min(s1*) = 0.625 ≤ V_Markov = 0.628 ≤ V_iid(s1*) = 0.777`
3. **Fix comparison table** to use consistent notation distinguishing worst-case bounds from equilibrium payoffs.

## What Is NOT Wrong

- The arithmetic in each individual computation is correct
- The formal theorem bound `V(s1*) = β/(α+β)` is valid as a lower bound
- The values 0.777 and 0.628 are correctly computed equilibrium payoffs
- The overestimation gap (0.777 vs 0.628) is a real economic effect
