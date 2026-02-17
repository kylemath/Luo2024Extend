# First Parse: Extending "Marginal Reputation" to Persistent/Markovian States

**Date:** February 16, 2026, 8:40 PM
**Paper:** "Marginal Reputation" by Daniel Luo and Alexander Wolitzky (MIT, December 2024)
**Challenge:** Daniel Luo offers $500 to anyone who can figure out how to extend the main result to allow for persistent/Markovian states in <5 hours. He and his coauthor suspect it is possible but never carried it out.

---

## 1. Understanding the Paper

### 1.1 The Setting

A long-run player (player 1, discount factor δ) faces a sequence of myopic short-run opponents in a repeated game. Each period:

1. A **private signal** y₀ (or state θ) is drawn — the long-run player observes it, short-run players do not.
2. The long-run player chooses an action a₁ based on y₀.
3. Short-run players observe the **history of past actions** (the marginal over a₁) but **not** the history of signals.

The long-run player is either **rational** (type ωᴿ) or one of countably many **commitment types** ω_{s₁}, each of which plays a fixed strategy s₁: Y₀ → Δ(A₁) every period. The type is drawn once from a full-support prior μ₀ and is perfectly persistent.

### 1.2 The Core Problem

The long-run player's strategy s₁ maps signals to actions, but short-run players only see the **marginal distribution over actions**, not the conditioning. Two very different strategies can produce identical observable behavior:

- **Stackelberg strategy:** "Fight when I detect an attack" (conditional on signal)
- **Confounding strategy:** "Fight 50% of the time regardless" (unconditional)

Both produce the same action marginal. Standard reputation results (Fudenberg-Levine 1992, Gossner 2011) bound payoffs using "0-confirmed best responses," but in this partially-identified setting, the set of 0-confirmed best responses is so large that these bounds are **vacuous**.

### 1.3 The Main Result (Theorem 1)

**Statement:** If the Stackelberg strategy s₁* is **confound-defeating** and **not behaviorally confounded**, then:

$$\liminf_{\delta \to 1} \underline{U}_1(\delta) \geq V(s_1^*)$$

where V(s₁*) is the commitment payoff (payoff from playing s₁* against the least favorable best response).

**Confound-defeating** means: for any best response (α₀, α₂) ∈ B₀(s₁*), the joint distribution γ(α₀, s₁*) over (signal, action) is the **unique solution** to the optimal transport problem:

$$\text{OT}(\rho(\alpha_0), \phi(\alpha_0, s_1^*); \alpha_2): \max_{\gamma \in \Delta(Y_0 \times A_1)} \int u_1(y_0, a_1, \alpha_2)\, d\gamma$$

subject to the marginals being ρ(α₀) and φ(α₀, s₁*).

**Intuition:** If the Stackelberg strategy is the *only* rational way to produce the observed action marginal, then short-run players who observe the Stackelberg marginal must conclude the long-run player is playing the Stackelberg strategy — and best respond accordingly.

### 1.4 Characterization via Cyclical Monotonicity

The confound-defeating property is equivalent to **strict cyclical monotonicity** of supp(s₁*) in Y₀ × A₁ (Proposition 5, Corollary 1). This connects reputation theory to classical optimal transport theory (Rochet 1987, Santambrogio 2015).

### 1.5 The Supermodular Case (Proposition 7)

When u₁ is strictly supermodular in (y₀, a₁), confound-defeating simplifies to **monotonicity**: higher signal → weakly higher action. This yields clean results:

- **Deterrence game:** If fighting is relatively more appealing when an attack is detected (x + y < 1), the long-run player secures her Stackelberg payoff. If reversed (x + y > 1), she gets only her minmax payoff.
- **Trust game:** If min{w, z} > 0 (supermodular), Stackelberg payoff is secured. If max{w, z} < 0 (submodular), only minmax.
- **Signaling game:** A patient sender secures commitment payoff from any monotone strategy when the signaling cost is submodular.

### 1.6 Upper Bound (Proposition 6 / Corollary 3)

If μ₀(ωᴿ) → 1, the long-run player's payoff cannot exceed that from some cyclically monotone strategy. This provides a converse: reputation cannot help you commit to non-monotone strategies.

### 1.7 Extension to Behaviorally Confounded Strategies (Appendix A, Theorem 2)

When s₁* is behaviorally confounded, the result weakens to:

$$\liminf_{\delta \to 1} \underline{U}_1(\delta) \geq \beta V(s_1^*) + (1-\beta) V_0(s_1^*)$$

where β is the "salience" of s₁* — the minimum probability that the weight on s₁* exceeds the confounding threshold.

### 1.8 Communication Games (Section 6)

Characterizes when a communication mechanism s₁: Θ → Δ(R) is monotone w.r.t. some order: iff the bipartite graph G(s₁) is **acyclic and forbidden-triple-free** (Proposition 9). This gives a reputational foundation for Bayesian persuasion solutions.

---

## 2. The Critical Assumption: States are i.i.d.

Throughout the paper, the private signal/state θ is drawn **i.i.d. across periods**. This assumption is used in at least four places in the proof:

### 2.1 Commitment types are stationary
A commitment type plays s₁ every period. This is meaningful because the stage game is identical each period (same distribution of θ). With Markov states, a "commitment type" would need to be redefined.

### 2.2 The signal distribution ρ is exogenous and fixed
The OT problem OT(ρ, φ; α₂) has ρ as a known, fixed marginal. With Markov states, the distribution of θₜ depends on the unobserved θ_{t-1}, so ρ becomes private information.

### 2.3 The KL-divergence counting bound (Lemma 2)
The bound on "distinguishing periods" is:

$$\bar{T}(\eta, \mu_0) = \frac{-2\log\mu_0(\omega_{s_1^*})}{\eta^2}$$

This relies on the signal distribution being the same each period, so that KL divergences are additive across periods. With Markov states, per-period KL divergences are not i.i.d.

### 2.4 The martingale convergence argument (Lemma 3)
The posterior μₜ converges because the per-period likelihood ratios are i.i.d. With Markov states, they are dependent.

### 2.5 What Pei (2020) does differently
Pei studies the **perfectly persistent** case (θ drawn once, fixed forever) — the opposite extreme from i.i.d. He finds broadly similar supermodular/submodular distinctions but requires binary short-run player actions and conditions on the prior. The paper notes (footnote 9) that their Proposition 2 "is roughly consistent with Pei's results."

The Markov case interpolates between i.i.d. (Luo-Wolitzky) and perfectly persistent (Pei).

---

## 3. The Twitter Challenge

Daniel Luo's challenge: **"figure out how to extend the main result to allow for persistent/markovian states"** in under 5 hours. He suspects it is possible but he and Wolitzky never did it.

### 3.1 What "extend the main result" likely means
- **Theorem 1** (or its generalization Theorem 2) should hold when θₜ follows a Markov chain F(·|θ_{t-1}) rather than being i.i.d.
- The result should recover the i.i.d. case when F is independent of θ_{t-1}.
- Ideally, it should also shed light on the connection to Pei (2020) in the perfectly persistent limit.

### 3.2 What would "suffice" to win
A convincing proof sketch (not necessarily publication-ready) that:
1. States the extended theorem precisely.
2. Identifies where the i.i.d. assumption is used in the existing proof.
3. Shows how to modify each step for the Markov case.
4. Identifies what additional conditions (if any) are needed (e.g., ergodicity, mixing rate).

---

## 4. Five Interpretations Considered

We identified five ways to interpret "persistent/Markovian states":

| # | Interpretation | Core Idea |
|---|---------------|-----------|
| 1 | Stationary ergodic Markov chain on θ | Most natural generalization; signal distribution becomes non-stationary from short-run players' perspective |
| 2 | Commitment types play Markov strategies | Strategy space expands to s₁(θₜ, θ_{t-1}); commitment type concept needs redefinition |
| 3 | Action autocorrelation as identification channel | Persistence creates temporal patterns in actions that help distinguish strategies |
| 4 | Payoffs depend on past states | u₁(θₜ, θ_{t-1}, a₁, a₂) with dynamic complementarities; new economic content |
| 5 | Mixing-time correction to statistical bounds | Replace i.i.d. KL bound with ergodic-theory bound; technical engine for the extension |

**Assessment:** The most promising approach combines elements of all five, but the key insight is what we call the **"lifted state" approach**.

---

## 5. The Proposed Solution Strategy: Lifted State Approach

### 5.1 The Core Idea

**Redefine the state as the pair** $\tilde{\theta}_t = (\theta_t, \theta_{t-1})$.

If the Markov chain is stationary and ergodic with transition kernel F, then:
- $\tilde{\theta}_t$ has a **fixed stationary distribution** $\tilde{\rho}$ on Θ × Θ
- A commitment type plays $s_1: \Theta \times \Theta \to \Delta(A_1)$ — a Markov strategy
- The payoff $u_1(\theta_t, \theta_{t-1}, a_{1,t}, a_{2,t})$ is naturally defined on the expanded state
- **The OT problem** becomes $\text{OT}(\tilde{\rho}, \phi; \alpha_2)$ with the expanded payoff — structurally identical to the paper's framework

### 5.2 What This Buys Us

- **The confound-defeating characterization** (Theorem 1) applies directly on the expanded state space
- **Cyclical monotonicity** characterizes confound-defeatingness on Θ × Θ × A₁
- **The supermodular case** gives new economic conditions: supermodularity of $u_1$ in $(\tilde{\theta}, a_1) = ((\theta_t, \theta_{t-1}), a_1)$ yields monotonicity in the expanded state

### 5.3 What Still Needs Work

The lifted-state trick handles the OT/confound-defeating part cleanly. The difficulty is in the **statistical/dynamic arguments**:

#### Step A: Counting bound (Lemma 2 adaptation)
- **Problem:** Consecutive expanded states $\tilde{\theta}_t$ and $\tilde{\theta}_{t+1}$ overlap (they share θₜ), so they are not independent.
- **Proposed fix:** Use the ergodic theorem for Markov chains. The expected number of distinguishing periods should be bounded by approximately:

$$\bar{T}(\eta, \mu_0, \tau_{\text{mix}}) \approx \frac{-2\log\mu_0(\omega_{s_1^*})}{\eta^2} \cdot \tau_{\text{mix}}$$

where $\tau_{\text{mix}}$ is the mixing time of the Markov chain. This is finite for ergodic chains and recovers the i.i.d. bound when F is independent of θ_{t-1}.

#### Step B: Martingale convergence (Lemma 3 adaptation)
- **Problem:** The likelihood ratios are no longer i.i.d.
- **Proposed fix:** The posterior μₜ is still a martingale (this is Bayesian updating, which doesn't require i.i.d.). The convergence argument (Lemma 9 in Appendix B) uses the martingale convergence theorem, which applies to any martingale. The key sub-argument that needs checking is whether $p_{Y_1}(\sigma_0^*, s_1 | h_t)$ and $p_{Y_1}(\sigma_0^*, s_1^* | h_t)$ still converge to the same limit — this should follow from ergodicity.

#### Step C: Uniformity over equilibria (Lemma 3's uniformity argument)
- **Problem:** The proof that $\hat{T}(\zeta)$ can be chosen independent of δ and the equilibrium uses compactness of the strategy space and continuity of measures. With Markov states, the strategy space is larger (Markov strategies rather than static strategies).
- **Proposed fix:** The space of Markov strategies $s_1: \Theta \times \Theta \to \Delta(A_1)$ is still a compact set (finite Θ). The compactness argument should go through with only notational changes.

### 5.4 Additional Conditions Needed

The extension should require:
1. **Ergodicity** of the Markov chain on Θ (ensures stationary distribution exists and mixing is finite)
2. **Finite mixing time** τ_mix (quantitative — enters the bound)
3. **Confound-defeatingness on the expanded state space** Θ × Θ (stronger than on Θ alone, since the strategy conditions on more information)

### 5.5 What the Extended Theorem Would Say

**Conjecture (Extended Theorem 1):** Let θₜ follow a stationary ergodic Markov chain with transition kernel F and stationary distribution π. Let $\tilde{\theta}_t = (\theta_t, \theta_{t-1})$ with stationary distribution $\tilde{\rho}$. If:
- The commitment type $\omega_{s_1^*}$ plays a Markov strategy $s_1^*: \Theta \times \Theta \to \Delta(A_1)$
- $s_1^*$ is confound-defeating on the expanded state space (i.e., γ(α₀, s₁*) uniquely solves $\text{OT}(\tilde{\rho}, \phi; \alpha_2)$ for all $(α₀, α₂) \in B_0(s_1^*)$)
- $s_1^*$ is not behaviorally confounded

Then:
$$\liminf_{\delta \to 1} \underline{U}_1(\delta) \geq V(s_1^*)$$

In the supermodular case, confound-defeating reduces to monotonicity of s₁* in the expanded state $(\theta_t, \theta_{t-1})$.

---

## 6. Key Risks and Open Questions

1. **Is the lifted-state trick legitimate?** The main concern is that $\tilde{\theta}_t$ is not i.i.d. even though its marginal distribution is stationary. The proof needs to handle temporal dependence.

2. **Does the KL bound generalize cleanly?** The standard KL divergence bound for i.i.d. observations has well-known Markov analogues (e.g., via the spectral gap of the chain), but the exact constants matter for the result.

3. **Is the confound-defeating condition checkable?** On the expanded state space Θ × Θ, cyclic monotonicity is harder to verify. For the supermodular case, we need supermodularity in $(\theta_t, \theta_{t-1}, a_1)$, which is a joint condition on the payoff function and the transition kernel.

4. **What happens as persistence → 1?** In the limit of perfect persistence, the mixing time diverges, the bound $\bar{T}$ diverges, and we should recover something like Pei's (2020) conditions (binary actions, prior conditions). Does the framework degrade gracefully?

5. **Can we handle order-k Markov chains?** The lifted-state trick generalizes: $\tilde{\theta}_t = (\theta_t, \theta_{t-1}, \ldots, \theta_{t-k})$. But the state space grows exponentially in k. Is there a cleaner approach for general Markov chains that doesn't blow up the state space?

---

## 7. Next Steps

1. **Write out the formal statement** of the extended theorem precisely, with all conditions.
2. **Trace through the proof of Theorem 1** step by step, marking each place where i.i.d. is used and writing the Markov replacement.
3. **Work out the KL bound** for Markov chains explicitly (this is the hardest technical step).
4. **Check the deterrence game** (Section 2.1) with Markov attacks as a concrete example.
5. **Write up a clean proof sketch** that could be sent to Luo as a response to the challenge.

---

*This document represents a first parse of the problem. The approach seems feasible but the details of the statistical arguments (Steps A-B above) require careful verification.*
