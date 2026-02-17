# Subagent 3 — Job 1: Deterrence Game with Markov Attacks

**Assigned by:** Agent 841  
**Deliverable:** `agent841_workspace/agent841subagent3Report.md`  
**Deadline:** ASAP (we have ~50 minutes total)

---

## Context

We are extending Theorem 1 of "Marginal Reputation" (Luo & Wolitzky, 2024) to Markovian states. The paper and first parse are in the repository.

## Your Task

**Work out the deterrence game (Section 2.1 of the paper) as a concrete example with Markov attacks.**

### The i.i.d. Deterrence Game (from the paper)

Each period:
- Short-run player chooses C (cooperate) or D (defect)
- Long-run player observes signal c or d, with Pr(c|C) = Pr(d|D) = p ∈ (0,1)
- Long-run player chooses A (accommodate) or F (fight)
- Payoff matrix for short-run: C→A gives 1, C→F gives -l, D→A gives 1+g, D→F gives 0
- Payoff matrix for long-run (depends on signal): c→A gives 1, c→F gives x, d→A gives y, d→F gives 0

Stackelberg strategy: (A,F) = accommodate after c, fight after d.
- If x + y < 1 (supermodular): long-run player secures Stackelberg payoff p
- If x + y > 1 (submodular): only gets minmax 1 - p + py

### The Markov Extension

Now suppose the **state** (or equivalently the signal structure) follows a Markov chain. Specifically:

**Setup:** Let the underlying state be θₜ ∈ {G, B} (Good or Bad), following a Markov chain:
- Pr(θₜ = G | θ_{t-1} = G) = 1 - α
- Pr(θₜ = B | θ_{t-1} = B) = 1 - β
- Stationary distribution: π(G) = β/(α+β), π(B) = α/(α+β)

The signal for the long-run player is still generated as before: Pr(c|C,θ=G) = Pr(d|D,θ=B) = p, but now the underlying state θ is persistent.

Alternatively (and more directly mapping to the paper): the signal y₀ ∈ {c, d} has a distribution that depends on (a₀, θₜ), and θₜ is Markov.

### What to work out

1. **Define the lifted state** θ̃ₜ = (θₜ, θ_{t-1}). Write out its stationary distribution ρ̃.

2. **Define the Stackelberg Markov strategy** s₁*: Θ × Θ → Δ(A₁). The natural Stackelberg strategy is still (A,F): accommodate after c, fight after d. But now the commitment type could condition on (θₜ, θ_{t-1}).
   - Consider: s₁*(c, ·) = A, s₁*(d, ·) = F (ignores θ_{t-1} — same as i.i.d.)
   - Or: s₁* that conditions on the transition (e.g., fight harder after (G→B) than after (B→B))

3. **Check confound-defeating on the expanded state space.** For the strategy that ignores θ_{t-1}:
   - The OT problem is OT(ρ̃, φ; α₂) where ρ̃ is the stationary distribution on Θ × Θ
   - γ(s₁*) is the joint distribution over (θ̃, a₁)
   - Is this the unique solution?
   
4. **Check supermodularity on the expanded state space.** Is u₁(θ̃, a₁, a₂) = u₁(θₜ, a₁, a₂) (payoff doesn't depend on θ_{t-1}) strictly supermodular in (θ̃, a₁)?
   - If u₁ only depends on θₜ, then u₁(θₜ, θ_{t-1}, a₁) is supermodular in ((θₜ, θ_{t-1}), a₁) iff it's supermodular in (θₜ, a₁) (since it doesn't depend on θ_{t-1}).
   - But we need an order on Θ × Θ. With Θ = {G, B}, the expanded state space is {(G,G), (G,B), (B,G), (B,B)}.
   - Need to find an order on this such that u₁ is supermodular.

5. **Compute the Stackelberg payoff** V(s₁*) in the Markov case.
   - The commitment payoff now depends on the stationary distribution ρ̃.
   - If the strategy is s₁*(c) = A, s₁*(d) = F (same as i.i.d.), the Stackelberg payoff is:
     V = π(G)·[Pr(c|C,G)·1 + Pr(d|D,G)·0] + π(B)·[Pr(c|C,B)·1 + Pr(d|D,B)·0]
     (need to work this out properly)

6. **State what the extended theorem says for this example:**
   - Under what conditions on (x, y, α, β, p) does the long-run player secure the Stackelberg payoff?
   - How does the result degrade as persistence increases (α, β → 0)?
   - In the limit of perfect persistence (α = β = 0), what happens? Does it connect to Pei (2020)?

7. **Connection to Pei (2020):** In the perfectly persistent case (θ drawn once), Pei shows results requiring binary short-run actions and prior conditions. Our Markov framework should interpolate between i.i.d. (large α, β) and Pei's setting (α = β → 0). When mixing time diverges, our bound T̄ should also diverge, suggesting the result weakens toward Pei's conditions.

## Deliverable Format

Write your report in `agent841_workspace/agent841subagent3Report.md` with:
1. **Model setup** with Markov states spelled out explicitly
2. **Lifted state space** with stationary distribution computed
3. **Confound-defeating check** on the expanded space
4. **Supermodularity check** on the expanded space
5. **Stackelberg payoff computation**
6. **Statement of the result** for this specific example
7. **Limiting cases** (i.i.d. recovery and perfect persistence)

Include explicit formulas. This is the key illustrative example.
