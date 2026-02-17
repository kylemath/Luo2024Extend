# Subagent 4 — Job 1: Formal Theorem Statement & OT Extension

**Assigned by:** Agent 841  
**Deliverable:** `agent841_workspace/agent841subagent4Report.md`  
**Deadline:** ASAP (we have ~50 minutes total)

---

## Context

We are extending Theorem 1 of "Marginal Reputation" (Luo & Wolitzky, 2024) to Markovian states. See `AgentReports/Feb16_840_firstParse.md` for the full first parse.

## Your Task

**Write the formal statement of the extended theorem and verify the OT / confound-defeating extension.**

### Part 1: Formal Extended Model

Write out the model precisely:

1. **State process:** θₜ ∈ Θ (finite) follows a stationary ergodic Markov chain with transition kernel F(·|θ) and unique stationary distribution π.

2. **Lifted state:** θ̃ₜ = (θₜ, θ_{t-1}) ∈ Θ̃ = Θ × Θ with stationary distribution:
   ρ̃(θ, θ') = π(θ') · F(θ|θ')

3. **Commitment types:** A commitment type ω_{s₁} plays a **Markov strategy** s₁: Θ̃ → Δ(A₁) every period. This means the commitment type can condition on (θₜ, θ_{t-1}).
   - Special case: "memoryless" commitment types play s₁: Θ → Δ(A₁), ignoring θ_{t-1}
   - The set Ω of commitment types is countable with full-support prior μ₀

4. **Signal structure:** Same as paper:
   - y₀ depends on a₀ via ρ(·|a₀), but now the distribution of y₀ is mediated through the lifted state
   - More precisely: the long-run player observes θ̃ₜ (or equivalently θₜ, with memory of θ_{t-1})
   - y₁ identifies a₁ (Assumption 1(2))

5. **Joint distribution:** γ(α₀, s₁) ∈ Δ(Θ̃ × A₁) where:
   γ(α₀, s₁)[θ̃, a₁] = ρ̃(θ̃) · s₁(θ̃)[a₁]
   
   Wait — this needs careful thought. In the original paper, γ is determined by α₀ and s₁:
   γ(α₀, s₁)[y₀, a₁] = Σ_{a₀} α₀(a₀) ρ(y₀|a₀) s₁(y₀)[a₁]
   
   In the Markov extension, if the long-run player's private information is θ̃ₜ, then:
   γ(s₁)[θ̃, a₁] = ρ̃(θ̃) · s₁(θ̃)[a₁]
   
   Note: if player 0 is absent (deterrence: A₀ singleton) or if player 0 is Nature (communication: α₀ is fixed), then the signal distribution ρ(θ̃) = ρ̃ is fixed. If player 0 is present, then the distribution of y₀ depends on α₀, but with Markov states, the state distribution is ρ̃ regardless.
   
   **Key difference from i.i.d.:** In the i.i.d. case, ρ(α₀) depends on α₀ (player 0's action affects the signal distribution). With Markov states, the state θₜ is NOT determined by player 0's action — it's exogenous. So the "signal" to the long-run player is θ̃ₜ, which has fixed stationary distribution ρ̃. Player 0 might still affect the long-run player's observation (e.g., in deterrence, the signal is noisy information about both θₜ and a₀).

   **Resolution:** The framework accommodates both cases. The general form is:
   - Long-run player observes y₀ (which may depend on both θₜ and a₀)
   - The joint distribution of (y₀, a₁) is γ(α₀, s₁)
   - The key difference is that the MARGINAL of y₀ is now:
     ρ(y₀|α₀) = Σ_{θ̃} ρ̃(θ̃) · Σ_{a₀} α₀(a₀) ρ(y₀|a₀, θ̃)
   - This is still fixed for given α₀ ✓

### Part 2: The OT Problem Extension

The OT problem in the paper is:

OT(ρ, φ; α₂): max_{γ ∈ Δ(Y₀ × A₁)} ∫ u₁(y₀, a₁, α₂) dγ
subject to π_{Y₀}(γ) = ρ and π_{A₁}(γ) = φ

The extended OT problem is:

OT(ρ̃, φ; α₂): max_{γ ∈ Δ(Θ̃ × A₁)} ∫ u₁(θ̃, a₁, α₂) dγ
subject to π_{Θ̃}(γ) = ρ̃ and π_{A₁}(γ) = φ

**Verify:**
1. The confound-defeating property (Definition 3) extends naturally: s₁* is confound-defeating iff γ(s₁*) uniquely solves OT(ρ̃, φ(s₁*); α₂) for all (α₀, α₂) ∈ B₀(s₁*).

2. Proposition 5 (characterization via cyclical monotonicity) applies directly on Θ̃ × A₁.

3. The supermodular case (Proposition 7): If u₁ is strictly supermodular in (θ̃, a₁) for some order on Θ̃ × A₁, then confound-defeating ⟺ monotone.

4. **Discuss what happens when u₁ depends only on θₜ (not θ_{t-1}):**
   - u₁(θ̃, a₁, α₂) = u₁(θₜ, a₁, α₂)
   - This may or may not be supermodular in θ̃ depending on the order on Θ̃
   - If u₁ is supermodular in (θₜ, a₁) and we use the product order on Θ̃ = Θ × Θ, then u₁ is trivially supermodular in θ̃ (since it doesn't depend on θ_{t-1})
   - But: the strategy s₁* can condition on θ_{t-1}, so the SUPPORT of s₁* lives in Θ̃ × A₁, and monotonicity means: if (θₜ, θ_{t-1}) ≻ (θₜ', θ_{t-1}') then a₁ ⪰ a₁'

### Part 3: Formal Statement

State the extended theorem precisely:

**Extended Theorem 1.** Let θₜ follow a stationary ergodic Markov chain on finite Θ with transition kernel F and stationary distribution π. Let θ̃ₜ = (θₜ, θ_{t-1}) with stationary distribution ρ̃(θ, θ') = π(θ')F(θ|θ'). Suppose:

(i) ω_{s₁*} ∈ Ω, where s₁*: Θ̃ → Δ(A₁) is a Markov strategy
(ii) s₁* is confound-defeating on the expanded state space: for any (α₀, α₂) ∈ B₀(s₁*), γ(α₀, s₁*) uniquely solves OT(ρ̃(α₀), φ(α₀, s₁*); α₂)
(iii) s₁* is not behaviorally confounded

Then: lim inf_{δ→1} U̲₁(δ) ≥ V(s₁*)

where V(s₁*) = inf_{(α₀,α₂)∈B(s₁*)} u₁(α₀, s₁*, α₂) is the commitment payoff from s₁* under the Markov chain.

**Extended Proposition 7 (Supermodular Case).** In addition to the above, if u₁ is strictly supermodular in (θ̃, a₁) for some orders on Θ̃ and A₁, then:
- Confound-defeating ⟺ monotone (w.r.t. these orders)
- Extended Theorem 1 applies to any monotone strategy

**Extended Corollary.** In the supermodular case:
lim inf_{δ→1} U̲₁(δ) ≥ v_mon := sup over monotone s₁ with ω_{s₁} ∈ Ω of V(s₁)

### Part 4: Additional Conditions

Carefully list what additional conditions are needed beyond the i.i.d. case:
1. **Ergodicity** of the Markov chain (for stationary distribution to exist)
2. **Stationarity** (for ρ̃ to be well-defined)
3. **What about mixing time?** — Check if it enters the result or only the rate of convergence
4. **What about the prior?** — Same as i.i.d. (full support)

### Part 5: Recovery of i.i.d. and Pei cases

Show:
- When F(·|θ) = π(·) for all θ (i.i.d.), ρ̃ = π ⊗ π and s₁* doesn't benefit from conditioning on θ_{t-1}, recovering the paper's Theorem 1
- When F is a point mass (perfect persistence), the mixing time is infinite and... what happens?

## Deliverable Format

Write your report in `agent841_workspace/agent841subagent4Report.md` with:
1. **Full formal model** with Markov states
2. **Extended OT problem** stated precisely  
3. **Extended Theorem 1** stated precisely
4. **Extended Proposition 7** (supermodular case)
5. **Additional conditions** needed
6. **Recovery of special cases**
7. **Open questions** and potential issues

This is the "statement" document — be precise and complete.
