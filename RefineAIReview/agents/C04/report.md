# C04: Incorrect Formulation of Markov Commitment Payoff

## Assessment: YELLOW

## Reviewer Comment
> Definition 4.5 pairs belief argument B(·) with same state θ that enters u₁(θ,·,·). Timing ambiguity—is the SR belief indexed by current state θ_t or previous state θ_{t-1}?

## Location
`sec_04_theorems.tex`, Definition 4.5 (`def:V_markov`), lines 46–51.

## Analysis

The reviewer identifies a **genuine timing ambiguity** in the formula for V_Markov. The paper writes:

```
V_Markov(s₁*) := Σ_{θ ∈ Θ} π(θ) · inf_{(α₀,α₂) ∈ B(s₁*, F(·|θ))} u₁(θ, s₁*(θ), α₂)
```

The variable θ appears in three roles:
1. **π(θ)**: weight from the stationary distribution
2. **F(·|θ)**: the filtering belief (transition from θ)
3. **u₁(θ, s₁*(θ), α₂)**: the stage-game payoff in state θ

### The Timing Problem

In the game, at period t:
1. State θ_t is realized
2. LR observes θ̃_t = (θ_t, θ_{t-1}) and plays s₁*(θ̃_t)
3. SR chooses a₂ based on history h_{t-1} (which reveals θ_{t-1} if s₁* is state-revealing)
4. Payoffs u₁(θ_t, a₁, a₂) accrue

Key: **SR's belief about θ_t is F(·|θ_{t-1})** — the transition from the PREVIOUS state. But **payoffs depend on θ_t** — the CURRENT state.

The paper's formula uses the **same** θ for both the belief F(·|θ) and the payoff u₁(θ,...). This conflates θ_{t-1} (which determines SR's belief) with θ_t (which determines payoffs).

### Correct Formula

The correct formula should use the joint distribution of (θ_t, θ_{t-1}):

```
V_Markov(s₁*) := Σ_{θ' ∈ Θ} π(θ') · inf_{α₂ ∈ B₂(s₁*, F(·|θ'))}
                  [ Σ_{θ ∈ Θ} F(θ|θ') · u₁(θ, s₁*(θ,θ'), α₂) ]
```

where:
- θ' = θ_{t-1}: the previous state (known to SR)
- θ = θ_t: the current state (affecting payoffs)
- π(θ'): marginal distribution of the previous state
- B₂(s₁*, F(·|θ')): SR best response given belief F(·|θ') about current state
- F(θ|θ') · u₁(θ, ...): expected payoff over current state given previous state

Or equivalently using the lifted-state stationary distribution ρ̃:

```
V_Markov(s₁*) := Σ_{θ' ∈ Θ} π(θ') · inf_{α₂ ∈ B₂(s₁*, F(·|θ'))}
                  Σ_{θ} F(θ|θ') · u₁(θ, s₁*(θ,θ'), α₂)
```

### Quantitative Impact

For the paper's baseline parameters (α=0.3, β=0.5):
- When SR cooperates after G: payoff = E[u₁(θ_t,...) | θ_{t-1}=G] = Σ_θ F(θ|G) u₁(θ,...)
  ≠ u₁(G,...) unless payoffs are state-independent
- The difference depends on how much u₁ varies across states

### When the Formula IS Correct

The paper's formula IS correct in the special case where SR's best response depends on the CURRENT state θ_t rather than the previous state. This could happen if:
- The SR model has sequential timing (SR observes LR's action before choosing)
- The SR directly observes the state

But the standard reputation game has simultaneous moves, and SR only has access to h_{t-1}.

### Alternative Resolution

If the paper adopts the convention that payoffs u₁ are state-independent (depend only on actions), then the timing issue vanishes because u₁(θ, a₁, α₂) = u₁(a₁, α₂). But the paper explicitly states u₁ depends on θ_t (sec_02_model.tex, line 73).

## Why YELLOW

The formula requires a mathematical correction (adding an expectation over the current state), not just editorial cleanup. This interacts with C02's analysis (the corrected formula may change when V_Markov ≷ V). The fix is clear but requires careful revision of Definition 4.5 and the proof of Step 5.
