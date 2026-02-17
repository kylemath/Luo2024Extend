# Subagent 3 Report: Deterrence Game with Markov Attacks

**Deliverable for:** Agent 841, Job 1  
**Date:** February 16, 2026

---

## 1. Model Setup with Markov States

### 1.1 Stage Game (from paper Section 2.1)

Each period:
- **Short-run player** chooses C (Cooperate) or D (Defect).
- **Long-run player** observes a private signal y ∈ {c, d}, then chooses A (Accommodate) or F (Fight).

**Payoffs:**
- Short-run: C→A: 1, C→F: −l, D→A: 1+g, D→F: 0
- Long-run (depends on signal): (c,A)→1, (c,F)→x, (d,A)→y, (d,F)→0

Parameters: g, l > 0; x, y ∈ (0,1); p ∈ (0,1) with Pr(c|C) = Pr(d|D) = p.

### 1.2 Markov Extension

We introduce an underlying state **θₜ ∈ {G, B}** (Good/Bad) following a Markov chain:

- P(θₜ = G | θ_{t−1} = G) = 1 − α  
- P(θₜ = B | θ_{t−1} = G) = α  
- P(θₜ = B | θ_{t−1} = B) = 1 − β  
- P(θₜ = G | θ_{t−1} = B) = β  

**Signal structure:** The signal depends on (a₀, θₜ). We take the mapping where the state plays the role of the signal for payoffs:
- θ = G corresponds to "cooperation detected" (signal c)
- θ = B corresponds to "attack detected" (signal d)

So the long-run payoff matrix as a function of (θ, a₁) is:
- u₁(G, A) = 1, u₁(G, F) = x
- u₁(B, A) = y, u₁(B, F) = 0

(This matches the paper's (c,d) × (A,F) structure with G↔c, B↔d.)

Alternatively, the signal y₀ ∈ {c,d} can be drawn from a distribution that depends on (a₀, θₜ); we assume the marginal over (θ, a₁) is what matters for payoffs, so the analysis below holds.

---

## 2. Lifted State Space and Stationary Distribution

### 2.1 Lifted State

Define the lifted state
$$\tilde{\theta}_t = (\theta_t, \theta_{t-1}) \in \Theta \times \Theta = \{(G,G), (G,B), (B,G), (B,B)\}.$$

This makes the process a first-order Markov chain on the product space.

### 2.2 Stationary Distribution of θₜ

For the chain on {G, B}:
$$\pi(G) = \frac{\beta}{\alpha + \beta}, \quad \pi(B) = \frac{\alpha}{\alpha + \beta}.$$

### 2.3 Stationary Distribution ρ̃ on Θ × Θ

For (θₜ, θ_{t−1}) under the stationary measure:
$$\tilde{\rho}(\theta', \theta) = \pi(\theta) \cdot P(\theta' | \theta).$$

Explicitly:

$$\tilde{\rho}(G,G) = \pi(G)(1-\alpha) = \frac{\beta(1-\alpha)}{\alpha + \beta}$$

$$\tilde{\rho}(G,B) = \pi(B)\beta = \frac{\alpha\beta}{\alpha + \beta}$$

$$\tilde{\rho}(B,G) = \pi(G)\alpha = \frac{\alpha\beta}{\alpha + \beta}$$

$$\tilde{\rho}(B,B) = \pi(B)(1-\beta) = \frac{\alpha(1-\beta)}{\alpha + \beta}$$

**Check:** 
$$\tilde{\rho}(G,G) + \tilde{\rho}(G,B) + \tilde{\rho}(B,G) + \tilde{\rho}(B,B) = \frac{\beta(1-\alpha) + \alpha\beta + \alpha\beta + \alpha(1-\beta)}{\alpha+\beta} = \frac{\beta - \alpha\beta + 2\alpha\beta + \alpha - \alpha\beta}{\alpha+\beta} = \frac{\alpha + \beta}{\alpha+\beta} = 1.$$

---

## 3. Stackelberg Markov Strategy

### 3.1 Natural Strategy (ignores θ_{t−1})

The paper’s Stackelberg strategy is (A,F): accommodate after c (or G), fight after d (or B). The Markov version that ignores θ_{t−1} is:
$$s_1^*(c,\cdot) = A, \quad s_1^*(d,\cdot) = F$$
or, with θ as the state, s₁*(G,·) = A and s₁*(B,·) = F. On the lifted state space this is:
$$s_1^*(\theta_t, \theta_{t-1}) = s_1^*(\theta_t) = \begin{cases} A & \text{if } \theta_t = G \\ F & \text{if } \theta_t = B \end{cases}$$

### 3.2 Alternative: Conditioning on the Transition

One could instead let the commitment type depend on the transition, e.g.:
- s₁*(G,B) = F (fight when moving from B to G) vs s₁*(G,G) = A (accommodate when staying in G)

That would use the extra information in θ̃. The i.i.d.-like strategy above does not.

---

## 4. Confound-Defeating Check on the Expanded State Space

### 4.1 OT Problem

For (α₀, α₂) ∈ B₀(s₁*), the OT problem is
$$\max_{\gamma \in \Delta(\tilde{\Theta} \times A_1)} \int u_1(\tilde{\theta}, a_1, \alpha_2)\, d\gamma$$
subject to marginals γ_θ̃ = ρ̃ and γ_{a₁} = φ(α₀, s₁*).

### 4.2 Payoff Independence of θ_{t−1}

The long-run payoff depends on (θₜ, a₁), not on θ_{t−1}:
$$u_1(\tilde{\theta}, a_1, a_2) = u_1(\theta_t, a_1, a_2).$$

So the objective is effectively over (θₜ, a₁), and the marginal on θₜ is π.

### 4.3 Induced Coupling Under s₁*

Under s₁*(G)=A, s₁*(B)=F, the distribution of a₁ given θ̃ = (θₜ, θ_{t−1}) depends only on θₜ:
- P(a₁ = A | θₜ = G) = 1
- P(a₁ = F | θₜ = B) = 1

The action marginal is φ(A) = π(G), φ(F) = π(B).

Under ρ̃ and this strategy, the joint on (θ̃, a₁) is:
$$\gamma^*(\tilde{\theta}, a_1) = \tilde{\rho}(\tilde{\theta}) \cdot \mathbf{1}[a_1 = s_1^*(\theta_t)].$$

The marginal on θₜ is π, and the marginal on a₁ is φ. The coupling on (θₜ, a₁) is the monotone one: θₜ = G ⇒ A, θₜ = B ⇒ F.

### 4.4 Uniqueness and Confound-Defeating

When x + y < 1, u₁ is strictly supermodular in (θₜ, a₁) with the order G ≻ B and A ≻ F. Under strict supermodularity, the unique optimal coupling is the monotone one (Monge–Kantorovich), which is exactly γ*.

So the strategy s₁*(c)=A, s₁*(d)=F that ignores θ_{t−1} remains confound-defeating on the expanded state space under x + y < 1.

---

## 5. Supermodularity Check on the Expanded State Space

### 5.1 Payoff Structure

$$u_1(\theta_t, a_1) = \begin{cases} 1 & (\theta_t,a_1)=(G,A) \\ x & (\theta_t,a_1)=(G,F) \\ y & (\theta_t,a_1)=(B,A) \\ 0 & (\theta_t,a_1)=(B,F) \end{cases}$$

### 5.2 Supermodularity in (θₜ, a₁)

With G ≻ B and A ≻ F:
- u₁(G,A) − u₁(G,F) = 1 − x
- u₁(B,A) − u₁(B,F) = y − 0 = y

For increasing differences:
$$(1-x) - y > 0 \iff x + y < 1.$$

So u₁ is strictly supermodular in (θₜ, a₁) iff x + y < 1.

### 5.3 Supermodularity in (θ̃, a₁)

Since u₁(θ̃, a₁) = u₁(θₜ, a₁) does not depend on θ_{t−1}, we need an order on Θ × Θ such that u₁ is supermodular in (θ̃, a₁).

Use the product order where the first coordinate dominates: (θₜ, θ_{t−1}) ≻ (θₜ', θ'_{t−1}) iff θₜ ≻ θₜ' (or θₜ = θₜ' and θ_{t−1} ≻ θ'_{t−1} for tie-breaking). Because u₁ does not depend on the second coordinate, u₁ is supermodular in (θ̃, a₁) if and only if it is supermodular in (θₜ, a₁), i.e. iff x + y < 1.

So the supermodularity condition on the expanded space is unchanged: x + y < 1.

---

## 6. Stackelberg Payoff Computation

### 6.1 Commitment Payoff

Against the short-run best response (C when believing in Stackelberg), the long-run gets her Stackelberg payoff. Under s₁*(G)=A, s₁*(B)=F:
$$V(s_1^*) = \mathbb{E}_{\pi}[u_1(\theta_t, s_1^*(\theta_t))] = \pi(G) \cdot u_1(G,A) + \pi(B) \cdot u_1(B,F) = \pi(G) \cdot 1 + \pi(B) \cdot 0 = \pi(G).$$

### 6.2 Explicit Formula

$$V(s_1^*) = \pi(G) = \frac{\beta}{\alpha + \beta}.$$

So the Stackelberg payoff is the stationary probability of the Good state.

### 6.3 Relation to the i.i.d. Case

In the i.i.d. deterrence game, the Stackelberg payoff is p (the probability of signal c when short-run cooperates). Here, with θ as the state/signal and π(G) as the probability of G, we get V = π(G). In the i.i.d. limit, one can choose parameterizations so that π(G) = p (e.g. β/(α+β) = p). More generally, π(G) is the stationary probability of the “good” regime and is the natural analog of p.

---

## 7. Statement of the Result for This Example

### 7.1 Extended Theorem (Deterrence Game)

**Proposition (Markov Deterrence).** Suppose θₜ ∈ {G,B} follows an ergodic Markov chain with transitions above and stationary distribution π. Let θ̃ₜ = (θₜ, θ_{t−1}) with stationary distribution ρ̃. Let s₁*(G)=A, s₁*(B)=F.

1. **If x + y < 1 (supermodular):** A patient long-run player secures at least
   $$V(s_1^*) = \frac{\beta}{\alpha + \beta}$$
   in any Nash equilibrium, for any μ₀ > 0.

2. **If x + y > 1 (submodular):** As μ₀ → 0, the long-run player’s payoff approaches the minmax payoff in every equilibrium, for any δ < 1.

### 7.2 Conditions

- x + y < 1 (supermodularity)
- Markov chain ergodic (α, β > 0)
- Usual deterrence conditions on p, g, l, y for the short-run to prefer C when believing in Stackelberg

---

## 8. Limiting Cases

### 8.1 Recovery of the i.i.d. Case (α, β Large)

When α = β = 1/2, the chain is memoryless and
$$\pi(G) = \frac{1/2}{1/2+1/2} = \frac{1}{2}.$$

If instead we scale so that α + β is large while π(G) = p, we approach the i.i.d. setting. For instance, take β = p(α+β) and α = (1−p)(α+β) so that π(G) = p. As the chain mixes quickly, the analysis converges to the i.i.d. case and V → p.

### 8.2 Perfect Persistence (α, β → 0)

As α, β → 0:
- The chain stays in its initial state
- Mixing time τ_mix → ∞
- The bound T̄(η, μ₀, τ_mix) diverges
- The conclusion weakens toward Pei (2020)

### 8.3 Degradation with Persistence

As α, β decrease:
- τ_mix increases
- T̄ grows, so the number of “distinguishing periods” grows
- Reputation formation is slower
- In the limit (α = β = 0), we are in Pei’s perfectly persistent setting, where stronger prior restrictions and binary short-run actions are required.

### 8.4 Connection to Pei (2020)

The Markov setup bridges:
- **High α, β:** Fast mixing, close to i.i.d., Luo–Wolitzky style result
- **Low α, β:** Slow mixing, near-perfect persistence, Pei-style conditions

The condition x + y < 1 is preserved; what changes is the statistical argument and the role of mixing time.

---

## 9. Summary

| Item | Result |
|------|--------|
| **Lifted state** | θ̃ = (θₜ, θ_{t−1}) ∈ {(G,G),(G,B),(B,G),(B,B)} |
| **ρ̃** | ρ̃(θ',θ) = π(θ)·P(θ'\|θ) with π(G)=β/(α+β), π(B)=α/(α+β) |
| **Stackelberg strategy** | s₁*(G)=A, s₁*(B)=F (unchanged from i.i.d.) |
| **Confound-defeating** | Yes when x+y<1; product form γ* = ρ̃ ⊗ φ with monotone coupling on (θₜ,a₁) |
| **Supermodularity** | x+y<1 on expanded space (unchanged) |
| **Stackelberg payoff** | V = π(G) = β/(α+β) |
| **Result** | Long-run secures V if x+y<1; payoff degrades as α,β→0 |

---

*This report works through the deterrence game as a concrete example of the lifted-state Markov extension of Theorem 1 in Luo & Wolitzky (2024).*
