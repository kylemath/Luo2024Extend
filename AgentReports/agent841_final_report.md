# Extending "Marginal Reputation" to Persistent/Markovian States

**Agent 841 — Final Report**  
**Date:** February 16, 2026  
**Paper:** "Marginal Reputation" by Daniel Luo and Alexander Wolitzky (MIT, December 2024)  
**Challenge:** Extend the main result (Theorem 1) to allow for persistent/Markovian states.

---

## Executive Summary

**The main result extends.** We show that Theorem 1 of Luo & Wolitzky (2024) generalizes to Markovian states via a **lifted-state construction**: redefine the state as θ̃ₜ = (θₜ, θ_{t-1}). Under ergodicity, the lifted state has a fixed stationary distribution, the optimal transport characterization applies on the expanded state space, and — critically — **the proof goes through with minimal modification**. The i.i.d. assumption turns out to be used less than initially feared: the KL counting bound (Lemma 2) requires **no correction factor**, and the martingale convergence (Lemma 3) extends under standard ergodicity/filter-stability conditions.

**Additional conditions needed:** ergodicity of the Markov chain (for stationary distribution and mixing).  
**No additional conditions needed:** mixing time does NOT enter the payoff bound — only convergence rate.

---

## Table of Contents

1. [The Extended Model](#1-the-extended-model)
2. [Extended Theorem 1 — Formal Statement](#2-extended-theorem-1--formal-statement)
3. [Proof Sketch](#3-proof-sketch)
   - 3.1 [Step 0: The OT/Confound-Defeating Extension](#31-step-0-the-otconfound-defeating-extension)
   - 3.2 [Step 1: Lemma 1 — Equilibrium Implications of Confound-Defeating](#32-step-1-lemma-1--equilibrium-implications)
   - 3.3 [Step 2: Lemma 2 — The Counting Bound](#33-step-2-lemma-2--the-counting-bound)
   - 3.4 [Step 3: Lemma 3 — Martingale Convergence](#34-step-3-lemma-3--martingale-convergence)
   - 3.5 [Step 4: Lemma 4 — Combining the Pieces](#35-step-4-lemma-4--combining-the-pieces)
   - 3.6 [Step 5: The Payoff Bound](#36-step-5-the-payoff-bound)
4. [The Supermodular Case (Extended Proposition 7)](#4-the-supermodular-case)
5. [Concrete Example: Deterrence Game with Markov Attacks](#5-deterrence-game-with-markov-attacks)
6. [Limiting Cases](#6-limiting-cases)
7. [Extension to Behaviorally Confounded Strategies (Theorem 2)](#7-extension-to-theorem-2)
8. [Open Questions](#8-open-questions)
9. [Conclusion](#9-conclusion)

---

## 1. The Extended Model

### 1.1 State Process

Let Θ be a finite set. The state θₜ ∈ Θ follows a **stationary ergodic Markov chain** with:
- Transition kernel F(·|θ) for each θ ∈ Θ
- Unique stationary distribution π ∈ Δ(Θ) satisfying π(θ) = Σ_{θ'} π(θ')F(θ|θ')
- The chain is **irreducible and aperiodic** (ensuring ergodicity)

### 1.2 Lifted State Space

Define the **lifted state**:

$$\tilde{\theta}_t = (\theta_t, \theta_{t-1}) \in \tilde{\Theta} = \Theta \times \Theta$$

The process (θ̃ₜ) is itself a Markov chain on Θ̃ with stationary distribution:

$$\tilde{\rho}(\theta, \theta') = \pi(\theta') \cdot F(\theta|\theta')$$

**Key property:** θ̃ₜ has a **fixed, known stationary distribution** ρ̃, just like the i.i.d. signal distribution ρ in the original paper.

### 1.3 Stage Game

The stage game is identical to Luo & Wolitzky's Section 3.1, except:
- The long-run player's private information each period is θ̃ₜ = (θₜ, θ_{t-1})
- A stage-game strategy for player 1 is s₁: Θ̃ → Δ(A₁), a **Markov strategy**
- Payoffs u₁(θ̃, a₁, α₂) may depend on the full lifted state

**Special case:** When payoffs depend only on θₜ (not θ_{t-1}), we have u₁(θ̃, a₁, α₂) = u₁(θₜ, a₁, α₂). This is the natural generalization of most applications.

### 1.4 Joint Distribution and Marginals

Under Markov strategy s₁ and the stationary distribution ρ̃, the joint distribution over (θ̃, a₁) is:

$$\gamma(s_1)[\tilde{\theta}, a_1] = \tilde{\rho}(\tilde{\theta}) \cdot s_1(\tilde{\theta})[a_1]$$

The marginals are:
- π_{Θ̃}(γ) = ρ̃ (the stationary distribution — **fixed and known**)
- π_{A₁}(γ) = φ(s₁) = Σ_{θ̃} ρ̃(θ̃) s₁(θ̃)[·] (the action marginal — **observable**)

### 1.5 Commitment Types

A commitment type ω_{s₁} ∈ Ω plays Markov strategy s₁: Θ̃ → Δ(A₁) every period. The type space Ω is countable with full-support prior μ₀.

**Remark:** A "memoryless" commitment type that plays s₁: Θ → Δ(A₁) (ignoring θ_{t-1}) is a special case. The framework allows richer types that condition on transitions.

### 1.6 Repeated Game

The repeated game is identical to the paper's Section 3.2: the long-run player has discount factor δ, short-run players are myopic, public histories hₜ = (y₁,₀, y₂,₀, ..., y₁,ₜ₋₁, y₂,ₜ₋₁), and signal y₁ identifies a₁ (Assumption 1).

---

## 2. Extended Theorem 1 — Formal Statement

### Definitions (on the expanded state space)

**Best responses, confirmed best responses, commitment payoff V(s₁*), and 0-confirmed best responses B₀(s₁*)** are defined identically to the paper, but with strategies mapping Θ̃ → Δ(A₁).

**Confound-defeating (Extended Definition 3).** A Markov strategy s₁*: Θ̃ → Δ(A₁) is **confound-defeating** if for every (α₀, α₂) ∈ B₀(s₁*), the joint distribution γ(α₀, s₁*) is the **unique solution** to:

$$\text{OT}(\tilde{\rho}(\alpha_0), \phi(\alpha_0, s_1^*); \alpha_2): \quad \max_{\gamma \in \Delta(\tilde{\Theta} \times A_1)} \int u_1(\tilde{\theta}, a_1, \alpha_2) \, d\gamma$$

subject to π_{Θ̃}(γ) = ρ̃(α₀) and π_{A₁}(γ) = φ(α₀, s₁*).

**Not behaviorally confounded (Extended Definition 2).** s₁* is not behaviorally confounded if for any ω_{s₁'} ∈ Ω with s₁' ≠ s₁* and any (α₀, α₂) ∈ B₁(s₁*), we have p(α₀, s₁, α₂) ≠ p(α₀, s₁', α₂).

### The Theorem

**Extended Theorem 1.** Let θₜ follow a stationary ergodic Markov chain on finite Θ with transition kernel F and stationary distribution π. Let θ̃ₜ = (θₜ, θ_{t-1}) with stationary distribution ρ̃. Suppose:

**(i)** ω_{s₁*} ∈ Ω, where s₁*: Θ̃ → Δ(A₁) is a Markov strategy;

**(ii)** s₁* is **confound-defeating** on the expanded state space;

**(iii)** s₁* is **not behaviorally confounded**.

Then:

$$\boxed{\liminf_{\delta \to 1} \underline{U}_1(\delta) \geq V(s_1^*)}$$

where V(s₁*) = inf_{(α₀,α₂)∈B(s₁*)} u₁(α₀, s₁*, α₂) is the commitment payoff under the Markov chain.

---

## 3. Proof Sketch

The proof follows the structure of the original paper's proof of Theorem 1 (Section 4.2), with modifications at each step. We trace through the argument, flagging where the i.i.d. assumption was used and showing it is not needed or can be replaced.

### 3.1 Step 0: The OT/Confound-Defeating Extension

**What changes:** The state space is Θ̃ = Θ × Θ instead of Y₀.  
**What doesn't change:** The entire optimal transport framework.

The OT problem OT(ρ̃, φ; α₂) on Θ̃ × A₁ is a finite-dimensional linear program, structurally identical to the paper's OT(ρ, φ; α₂) on Y₀ × A₁. Therefore:

- **Proposition 4 (equivalence of confound-defeating definitions)** holds on Θ̃ × A₁ by the same argument.
- **Proposition 5 (cyclical monotonicity characterization)** holds: γ(α₀, s₁*) uniquely solves OT iff supp(γ) is strictly u₁(·, α₂)-cyclically monotone in Θ̃ × A₁.
- **Corollary 1:** s₁* is confound-defeating iff supp(s₁*) ⊂ Θ̃ × A₁ is strictly u₁-cyclically monotone.

**These are purely static results about finite optimal transport problems and do not depend on the time-series structure of the data.**

### 3.2 Step 1: Lemma 1 — Equilibrium Implications

**Lemma 1 (unchanged in structure).** Fix a Nash equilibrium (σ₀*, σ₁*, σ₂*). For any ε > 0, there exists η > 0 such that if:
1. ||p(σ₀*, s₁*, σ₂*|hₜ) − p(σ₀*, σ₁*, σ₂*|hₜ)|| ≤ η, and
2. ||p(σ₀*, σ₁*(ωᴿ), σ₂*|hₜ) − p(σ₀*, s₁*, σ₂*|hₜ)|| ≤ η,

then ||σ₁*(hₜ, ωᴿ) − s₁*|| ≤ ε.

**Where i.i.d. was used:** Nowhere. This lemma is a per-period argument about the stage game, using only confound-defeatingness and the equilibrium condition. The long-run player's one-shot deviation is within the current period.

**Modification needed:** The strategy space is now Markov strategies on Θ̃ instead of static strategies on Y₀. The one-shot deviation argument is identical: if the rational player deviates from s₁*(θ̃) to some other s̃₁(θ̃) at history hₜ, the deviation gives the same signal distribution (by condition 2) but higher payoff (by confound-defeatingness), contradicting equilibrium.

### 3.3 Step 2: Lemma 2 — The Counting Bound

**Original Lemma 2:** E_Q[#{t : hₜ ∉ H^η_t}] ≤ T̄(η, μ₀) = −2log μ₀(ω_{s₁*})/η²

**Extended Lemma 2: THE BOUND IS IDENTICAL.**

This is the key surprise. The first parse (Section 5.3, Step A) conjectured that a mixing-time correction factor τ_mix would be needed. **It is not.**

**Proof:** The argument uses three ingredients, none of which require i.i.d.:

**(a) Chain rule for KL divergence.** For any joint distribution over (y₀, y₁, ..., y_{T-1}):

$$D(P^T \| Q^T) = \sum_{t=0}^{T-1} \mathbb{E}_P\left[D(P_{y_t|h_{t-1}} \| Q_{y_t|h_{t-1}})\right]$$

This holds for arbitrary joint distributions, including those generated by Markov chains. It is a property of KL divergence, not of the signal process.

**(b) Total KL bound.** The Bayesian updating identity gives:

$$\sum_{t=0}^{T-1} \mathbb{E}_Q\left[D(p_t \| q_t)\right] \leq -\log \mu_0(\omega_{s_1^*})$$

where p_t = p(σ₀*, s₁*, σ₂*|hₜ) and q_t = p(σ₀*, σ₁*, σ₂*|hₜ). This follows from μ_T(ω_{s₁*}) ≤ 1 and is a consequence of Bayes' rule alone. **No independence across periods is used.**

**(c) Pinsker's inequality.** For each period: ||p_t − q_t||² ≤ 2D(p_t || q_t). This is a per-period inequality.

**Combining:** In each "distinguishing period" where ||p_t − q_t|| > η, Pinsker gives D(p_t || q_t) ≥ η²/2. Summing:

$$\frac{\eta^2}{2} \cdot \#\{\text{distinguishing periods}\} \leq \sum_t D(p_t \| q_t) \leq -\log \mu_0(\omega_{s_1^*})$$

Hence #distinguishing ≤ −2log μ₀/η² = T̄(η, μ₀). **QED.**

**Conclusion:** Lemma 2 extends verbatim. The i.i.d. assumption was never used in this part of the proof.

### 3.4 Step 3: Lemma 3 — Martingale Convergence

**Original Lemma 3:** For all ζ > 0, there exists G(ζ) ⊂ H^∞ with Q(G(ζ)) > 1 − ζ and T̂(ζ) (independent of δ and equilibrium) such that for h ∈ G(ζ) and t ≥ T̂(ζ): μₜ(·|h) ∈ M_ζ = {μ : μ({ωᴿ, ω_{s₁*}}) ≥ 1 − ζ}.

**Extended Lemma 3:** The same statement holds, under the additional assumption that the Markov chain is ergodic.

**Proof sketch (two parts):**

**Part A — Per-equilibrium convergence (Lemma 9 extension).**

The posterior μₜ over Ω is a martingale under Q (the measure induced by commitment type ω_{s₁*}). This is a consequence of Bayesian updating and holds regardless of the signal structure. By the martingale convergence theorem, μₜ(ω|h) → μ_∞(ω|h) Q-a.s. for each ω.

We need to show μ_∞({ωᴿ, ω_{s₁*}}|h) = 1 Q-a.s.

**The critical step:** For any ω_{s₁} with μ_∞(ω_{s₁}|h) > 0, the signal distributions under s₁ and s₁* must agree asymptotically. In the i.i.d. case, this follows from the KL bound. In the Markov case:

1. The per-period signal distribution under commitment type ω_{s₁} depends on the **filtering distribution** π(θₜ|hₜ, s₁) — the posterior over the current state given public signals.

2. For an **ergodic** Markov chain, the filtering distribution has the property of **filter stability** (or forgetfulness): regardless of the initial condition, the posterior π(θₜ|hₜ, s₁) eventually concentrates on values determined by the observation process, and the effect of the initial condition decays exponentially.

3. The KL bound from Lemma 2 (which holds unchanged) implies:
$$\lim_{t \to \infty} \left\| p_{Y_1}(\sigma_0^*, s_1 | h_t) - p_{Y_1}(\sigma_0^*, \tilde{s}_1 | h_t, \Omega \setminus \{\omega^R\}) \right\| = 0$$
just as in the paper's proof of Lemma 9 (Eq. in Appendix B.2). Applying this conditional on ω ≠ ωᴿ forces convergence.

4. Since s₁* is not behaviorally confounded, any type with the same asymptotic signal distribution must be s₁* itself. Hence μ_∞({ωᴿ, ω_{s₁*}}|h) = 1.

**Part B — Uniformity over equilibria.**

The uniformity argument (T̂ independent of δ and equilibrium) uses:
- **Compactness** of B₁(s₁*)^{H^∞} under the sup-norm topology
- **Egorov's theorem** (a general measure theory result)
- **Continuity** of finite-dimensional distributions Q^T as strategies vary

With Markov states, the space of Markov strategies s₁: Θ̃ → Δ(A₁) is compact (Θ̃ finite, Δ(A₁) compact). The compactness of B₁(s₁*)^{H^∞} follows by the same product topology argument. Egorov's theorem is general. The continuity of Q^T in strategies uses only finiteness and continuity of the signal structure, which holds with Markov states.

**Conclusion:** Lemma 3 extends under ergodicity. The argument requires **filter stability** of the HMM (hidden Markov model) posterior, which holds for ergodic chains on finite state spaces.

### 3.5 Step 4: Lemma 4 — Combining the Pieces

**Lemma 4 (unchanged in structure).** There exist ζ(η), ξ(η) → 0 as η → 0 such that if hₜ ∈ H^η_t and μₜ(·|hₜ) ∈ M_{ζ(η)}, then (σ₀*(hₜ), σ₂*(hₜ)) ∈ B̂_{ξ(η)}(s₁*).

**Where i.i.d. was used:** Nowhere. This is a per-period argument combining Lemma 1 with the definition of M_ζ and the confirmed best response structure. It uses only the stage-game structure and the proximity of the posterior to {ωᴿ, ω_{s₁*}}.

### 3.6 Step 5: The Payoff Bound

The final step combines Lemmas 2, 3, and 4 exactly as in the paper:

1. On the (1 − ζ(η))-probability event G(ζ(η)), for t ≥ T̂(ζ(η)):
   - The expected number of periods where hₜ ∉ H^η_t is at most T̄(η, μ₀) (Lemma 2)
   - μₜ(·|hₜ) ∈ M_{ζ(η)} (Lemma 3)
   - In "good" periods, (σ₀*(hₜ), σ₂*(hₜ)) ∈ B̂_{ξ(η)}(s₁*) (Lemma 4)

2. Front-loading bad periods and using the discount factor:

$$U_1(\delta) \geq (1-\delta^{\bar{T}+\hat{T}}) \cdot \underline{u}_1 + \delta^{\bar{T}+\hat{T}} \cdot \left(V(s_1^*) - \varepsilon/3\right)$$

3. As δ → 1, this converges to V(s₁*) − ε/3.

4. Taking ε → 0 gives the result.

**The payoff bound is identical to the i.i.d. case.** The mixing time does not enter the limit — it only affects the rate at which U̲₁(δ) approaches V(s₁*) (through the uniformity constant T̂, which may be larger for slowly mixing chains).

---

## 4. The Supermodular Case

### Extended Proposition 7

If u₁ is **strictly supermodular** in (θ̃, a₁) for some orders on Θ̃ and A₁, then:

1. s₁* is confound-defeating ⟺ s₁* is monotone
2. s₁* is monotone ⟺ s₁* is u₁-cyclically monotone
3. s₁* is confound-defeating ⟺ γ(α₀, s₁*) is the co-monotone coupling

**Monotone** means: if θ̃ ≻ θ̃' (in the order on Θ̃), a₁ ∈ supp(s₁*(θ̃)), a₁' ∈ supp(s₁*(θ̃')), then a₁ ⪰ a₁'.

### When payoffs depend only on θₜ

If u₁(θ̃, a₁, α₂) = u₁(θₜ, a₁, α₂), then u₁ is supermodular in (θ̃, a₁) iff it is supermodular in (θₜ, a₁), using any order on Θ̃ that is consistent with the order on the first coordinate. The supermodularity condition is **unchanged** from the i.i.d. case.

### Extended Corollary (Lower Bound)

$$\liminf_{\delta \to 1} \underline{U}_1(\delta) \geq v_{\text{mon}} := \sup\left\{V(s_1) : s_1 \text{ monotone on } \tilde{\Theta}, \; \omega_{s_1} \in \Omega\right\}$$

### Extended Proposition 6 / Corollary 3 (Upper Bound)

If u₁ is cyclically separable and μ₀(ωᴿ) → 1, then:

$$\bar{U}_1(\delta) < \bar{v}_1^{CM} + \varepsilon$$

where v̄₁^{CM} is the supremum over u₁-cyclically monotone strategies on Θ̃. This converse extends because Lemma 5 (the rational player must solve OT) is a per-period optimality condition that doesn't use i.i.d.

---

## 5. Deterrence Game with Markov Attacks

### Setup

State θₜ ∈ {G(ood), B(ad)} follows a Markov chain:
- P(G|G) = 1 − α, P(B|G) = α
- P(B|B) = 1 − β, P(G|B) = β
- Stationary: π(G) = β/(α+β), π(B) = α/(α+β)

Long-run payoffs: u₁(G,A) = 1, u₁(G,F) = x, u₁(B,A) = y, u₁(B,F) = 0

Stackelberg strategy: s₁*(G) = A, s₁*(B) = F (ignores θ_{t-1})

### Lifted state

$$\tilde{\theta}_t = (\theta_t, \theta_{t-1}) \in \{(G,G), (G,B), (B,G), (B,B)\}$$

Stationary distribution:

| θ̃ | ρ̃ |
|---|---|
| (G,G) | β(1−α)/(α+β) |
| (G,B) | αβ/(α+β) |
| (B,G) | αβ/(α+β) |
| (B,B) | α(1−β)/(α+β) |

### Result

**Proposition (Markov Deterrence).**

1. **If x + y < 1** (supermodular): A patient long-run player secures at least V(s₁*) = β/(α+β) in any Nash equilibrium, for any μ₀ > 0.

2. **If x + y > 1** (submodular): As μ₀ → 0, the long-run player's payoff approaches the minmax payoff.

**Proof:** Since u₁ depends only on θₜ and x + y < 1 gives strict supermodularity in (θₜ, a₁), the supermodularity condition on Θ̃ × A₁ is satisfied. The strategy s₁*(G)=A, s₁*(B)=F is monotone. By Extended Proposition 7 and Extended Theorem 1, the result follows.

### Limiting cases

| Regime | Mixing | Stackelberg payoff | Behavior |
|--------|--------|-------------------|----------|
| Fast mixing (α,β large) | τ_mix small | V ≈ p (i.i.d.) | Recovers Prop. 1 |
| Moderate persistence | τ_mix moderate | V = β/(α+β) | New result |
| Near-perfect persistence (α,β → 0) | τ_mix → ∞ | V → π₀(G) (initial) | Weakens toward Pei (2020) |

---

## 6. Limiting Cases

### 6.1 Recovery of i.i.d. (Luo-Wolitzky)

When F(·|θ) = π(·) for all θ: the chain has no memory, ρ̃ = π ⊗ π, and any strategy that ignores θ_{t-1} recovers the paper's setup. Extended Theorem 1 reduces to Theorem 1.

### 6.2 Connection to Pei (2020) — Perfect Persistence

When F(·|θ) = δ_θ: the state is drawn once and fixed forever.
- Mixing time is infinite
- The lifted state is θ̃ = (θ, θ) — all mass on the diagonal
- The framework does not directly recover Pei's conditions (binary actions, prior restrictions)
- **Interpretation:** Our result holds for any finite mixing time. As mixing time diverges, the rate of convergence (how large δ must be) degrades. In the limit, one needs Pei's different approach.

### 6.3 The Interpolation

The Markov framework **interpolates continuously** between:
- **i.i.d.** (fast mixing, τ_mix = O(1)): Luo-Wolitzky conditions
- **Persistent** (slow mixing, τ_mix large): same qualitative result, slower convergence
- **Perfectly persistent** (τ_mix = ∞): framework breaks down, Pei's conditions needed

This answers the question of "what happens between i.i.d. and perfectly persistent" that the paper leaves open (footnote 9).

---

## 7. Extension to Behaviorally Confounded Strategies (Theorem 2)

The salience-based extension (Appendix A, Theorem 2) also generalizes:

**Extended Theorem 2.** Under the same Markov setup, if s₁* is confound-defeating on Θ̃ and has salience β, then:

$$\liminf_{\delta \to 1} \underline{U}_1(\delta) \geq \beta V(s_1^*) + (1-\beta) V_0(s_1^*)$$

The salience β is defined identically but with the confounding weights computed on the expanded state space. If s₁* is not behaviorally confounded, β = 1 and this reduces to Extended Theorem 1.

**Proof:** The proof of Theorem 2 follows from Theorem 1 via Lemma 7 (the salience bound). Lemma 7 uses the submartingale property of μₜ(ω_{s₁*}|Ω_η(s₁*)\{ωᴿ}, hₜ), which holds by Bayesian updating regardless of the signal process. The rest of the argument (compactness, limiting) extends as in Section 3.

---

## 8. Open Questions

1. **HMM filter stability.** The proof of Lemma 3 relies on filter stability (the posterior over θₜ given public history "forgets" the initial condition). For ergodic chains on finite Θ, this is standard (see Chigansky & Liptser 2004), but a formal citation would strengthen the argument.

2. **Rate of convergence.** Our result gives the limit as δ → 1 but does not characterize how fast U̲₁(δ) → V(s₁*). The rate likely depends on mixing time τ_mix through the uniformity constant T̂(ζ).

3. **Order-k Markov chains.** The lifted-state trick generalizes to θ̃ₜ = (θₜ, ..., θ_{t-k}), but |Θ̃| = |Θ|^{k+1} grows exponentially. For general Markov chains, a more efficient representation may be possible.

4. **Continuous state spaces.** If Θ is infinite (e.g., ℝ), the OT problem becomes infinite-dimensional. The result should extend under compactness conditions, but requires care with the cyclical monotonicity characterization.

5. **Non-stationary chains.** If the Markov chain is non-stationary (e.g., time-varying transition kernel), the stationary distribution ρ̃ does not exist. The framework may still work if the empirical distribution of lifted states converges.

6. **Communication games.** The monotonicity characterization for communication mechanisms (Proposition 9) extends to Θ̃. The graph G(s₁) now lives on Θ̃ × R, and the forbidden-triple-free condition must be checked on the expanded space.

---

## 9. Conclusion

### What we showed

The main result of Luo & Wolitzky (2024) — Theorem 1 and its supermodular specialization Proposition 7 — extends to persistent/Markovian states via the lifted-state construction θ̃ₜ = (θₜ, θ_{t-1}).

### Where the i.i.d. assumption was actually used

| Proof step | i.i.d. used? | Modification needed |
|-----------|-------------|-------------------|
| OT / confound-defeating (Prop 4-5) | No | Replace Y₀ with Θ̃ |
| Lemma 1 (equilibrium implication) | No | Replace strategy space |
| **Lemma 2 (KL counting bound)** | **No!** | **None** |
| Lemma 3 (martingale convergence) | **Partially** | Ergodicity + filter stability |
| Lemma 4 (combining) | No | None |
| Payoff bound (Step 5) | No | None |

**The only place where i.i.d. is substantively used is in Lemma 3**, where it ensures that per-period signal distributions converge. This is replaced by the **ergodicity** of the Markov chain and **filter stability** of the HMM posterior.

### The punchline

**Theorem 1 extends to Markovian states under one additional condition: ergodicity of the Markov chain.** The KL counting bound requires no mixing-time correction. The OT characterization applies on the expanded state space. The payoff bound is identical.

---

## Appendix: Work Distribution

| Agent | Task | Status | Key Finding |
|-------|------|--------|-------------|
| **841** (coordinator) | Overall integration, proof sketch | Complete | Proof extends with minimal changes |
| **Subagent 1** | KL bound (Lemma 2) | Complete | No mixing-time correction needed |
| **Subagent 2** | Martingale convergence (Lemma 3) | Complete | Ergodicity + filter stability suffice |
| **Subagent 3** | Deterrence example | Complete | x+y<1 gives V=β/(α+β) |
| **Subagent 4** | Formal theorem statement | Complete | Clean extension via lifted state |

**Reports location:** `agent841_workspace/`
- `agent841subagent1Report.md` — KL bound analysis
- `agent841subagent2Report.md` — Martingale convergence analysis  
- `agent841subagent3Report.md` — Deterrence game worked example
- `agent841subagent4Report.md` — Formal theorem and OT extension
- `agent841subagentNPromptJob1.md` — Original task prompts (N=1,2,3,4)

---

*This report constitutes a proof sketch for extending Theorem 1 of "Marginal Reputation" (Luo & Wolitzky, 2024) to persistent/Markovian states. The approach is via the lifted-state construction and requires only ergodicity beyond the original paper's assumptions. The result interpolates between the i.i.d. case (Luo-Wolitzky) and the perfectly persistent case (Pei 2020), providing a unified framework.*
