# Subagent 2 Report: Martingale Convergence for Markov States

**Task:** Extend Lemma 3 (and its engine, Lemma 9) from i.i.d. states to Markovian states.

---

## 1. Extended Statement of Lemma 9 (Per-Equilibrium Convergence)

**Lemma 9 (Markov version).** Let θₜ follow an ergodic Markov chain on finite Θ with transition kernel F and unique stationary distribution π. Let θ̃ₜ = (θₜ, θ_{t-1}) with stationary distribution π̃ on Θ × Θ. Commitment types play Markov strategies s₁: Θ × Θ → Δ(A₁).

For any δ < 1, any strategy profile (σ₀*, σ₁*, σ₂*) where (σ₀*, σ₂*) ∈ B₁(s₁*) (and hence any Nash equilibrium), and any ζ > 0, there exists a set G(ζ) ⊂ H^∞ satisfying Q(G(ζ)) > 1 − ζ and a period T̂ such that, for any h ∈ G(ζ) and any t ≥ T̂:

μₜ(·|h) ∈ M_ζ = {μ ∈ Δ(Ω) : μ({ωᴿ, ω_{s₁*}}) ≥ 1 − ζ}

**Conditions required beyond the original paper:**
- (E1) F is irreducible and aperiodic on Θ (ergodicity)
- (E2) The "not behaviorally confounded" condition is evaluated at the stationary distribution π̃ (see §3)

---

## 2. Proof Sketch

### 2.1 Step 1: μₜ is a Q-martingale ✓ (No change needed)

The posterior μₜ(ω|hₜ) over the type space Ω is a bounded martingale under Q (and under any probability measure on H^∞). This is a consequence of the tower property of conditional expectation:

E_Q[μₜ₊₁(ω|hₜ₊₁) | hₜ] = P_Q(ω | hₜ) = μₜ(ω|hₜ)

**This is purely about Bayesian updating and does NOT depend on i.i.d.** It holds for any signal-generating process — Markov, non-stationary, or otherwise. The martingale convergence theorem then gives:

μₜ(ω|h) → μ_∞(ω|h) Q-a.s. for each ω ∈ Ω.

### 2.2 Step 2: μ_∞({ωᴿ, ω_{s₁*}}|h) = 1 (Main argument — changes flagged)

We must show that for Q-a.e. h, every ω_{s₁} ∈ Ω\{ωᴿ} with s₁ ≠ s₁* satisfies μ_∞(ω_{s₁}|h) = 0.

**Sub-step 2a: Convergence of conditional posteriors forces signal convergence.**

Suppose μ_∞(ω_{s₁}|h) > 0 for some s₁ ≠ s₁*. Then μₜ(ω_{s₁}|Ω\{ωᴿ}, hₜ) > c > 0 for all large t. The Bayesian update formula gives:

μₜ₊₁(ω_{s₁}|Ω\{ωᴿ}, hₜ, y₁) − μₜ(ω_{s₁}|Ω\{ωᴿ}, hₜ)
  = μₜ(ω_{s₁}|Ω\{ωᴿ}, hₜ) · [p_{Y₁}(s₁|hₜ)[y₁] − p_{Y₁}(s̃₁|hₜ, Ω\{ωᴿ})[y₁]] / p_{Y₁}(s̃₁|hₜ, Ω\{ωᴿ})[y₁]

Since the martingale converges, the increments vanish, forcing:

(★) lim_{t→∞} p_{Y₁}(s₁|hₜ)[y₁] − p_{Y₁}(s̃₁|hₜ, Ω\{ωᴿ})[y₁] = 0 for Q-a.e. h, all y₁ ∈ Y₁*

where s̃₁ denotes the mixture of commitment strategies weighted by μₜ(·|Ω\{ωᴿ}, hₜ) and Y₁* = supp(ρ(·|s₁*)).

**⚠ Where Markov states matter:** With i.i.d., p_{Y₁}(s₁|hₜ) = Σ_θ ρ(θ) Σ_{a₁} s₁(θ)[a₁] ρ(y₁|a₁), independent of hₜ (except through σ₀*). With Markov states:

p_{Y₁}(s₁|hₜ)[y₁] = Σ_{θ̃} π(θ̃|hₜ, s₁) Σ_{a₁} s₁(θ̃)[a₁] ρ(y₁|a₁)

where π(θ̃|hₜ, s₁) is the **filtering distribution** — the posterior over θ̃ₜ = (θₜ, θ_{t-1}) given hₜ under the hypothesis that the type is ω_{s₁}. **However, the derivation of (★) does not use i.i.d.** — it uses only Bayes' rule and martingale convergence.

**Sub-step 2b: KL bound forces mixture toward s₁*.**

Applying the argument of Lemma 2 conditional on ω ≠ ωᴿ:

lim_{t→∞} ||p_{Y₁}(s̃₁|hₜ, Ω\{ωᴿ}) − p_{Y₁}(s₁*|hₜ)|| = 0 for Q-a.e. h

**This step does not use i.i.d.** — it only uses the chain rule for KL divergence and Pinsker's inequality, which hold for arbitrary signal processes (as established in Subagent 1's report).

**Sub-step 2c: Combining.**

From (★) and (2b):

(★★) lim_{t→∞} ||p_{Y₁}(s₁|hₜ) − p_{Y₁}(s₁*|hₜ)|| = 0 for Q-a.e. h

**Sub-step 2d: Concluding s₁ = s₁*.**

**⚠ This is where the argument changes most for Markov states.**

With i.i.d., p_{Y₁}(s₁|hₜ) is independent of hₜ (modulo σ₀*), so (★★) immediately gives p(α₀, s₁, α₂) = p(α₀, s₁*, α₂), contradicting "not behaviorally confounded."

With Markov states, (★★) says the per-period conditional signal distributions converge to the same limit for Q-a.e. h. This is a strong asymptotic-indistinguishability condition on the two hidden Markov models (HMMs) defined by (F, s₁) and (F, s₁*).

**Claim:** Under ergodicity (E1) and signal identification (Assumption 1), (★★) implies s₁ = s₁*.

**Argument:** Suppose s₁ ≠ s₁*. Then there exists θ̃₀ = (θ₀, θ₀') ∈ Θ × Θ with F(θ₀|θ₀') > 0 such that:

Σ_{a₁} s₁(θ̃₀)[a₁] ρ(y₁|a₁) ≠ Σ_{a₁} s₁*(θ̃₀)[a₁] ρ(y₁|a₁)

(This uses signal identification: ρ(·|a₁) are linearly independent, so different mixed actions produce different signal distributions.)

By ergodicity, the lifted Markov chain visits θ̃₀ infinitely often. Each visit generates an observation from a different distribution under s₁ vs. s₁*. By standard HMM distinguishability theory (see e.g., Leroux 1992, "Maximum-likelihood estimation for hidden Markov models"), two HMMs with the same state dynamics but different emission distributions on a recurrent state generate statistically distinguishable observation processes.

**Key consequence:** The filtering distributions π(·|hₜ, s₁) and π(·|hₜ, s₁*) diverge on a set of Q-positive measure histories. The signal distributions p_{Y₁}(s₁|hₜ) and p_{Y₁}(s₁*|hₜ) therefore cannot converge for Q-a.e. h, contradicting (★★). Hence μ_∞(ω_{s₁}|h) = 0.

**Alternative route via ergodic averages:** Even without invoking HMM theory, we can argue:
By the ergodic theorem for the lifted chain under the Q-measure, the Cesàro averages satisfy:

(1/T) Σ_{t=1}^T p_{Y₁}(s|hₜ) → p̄(s) Q-a.s.

where p̄(s)[y₁] = Σ_{θ̃} π̃(θ̃) Σ_{a₁} s(θ̃)[a₁] ρ(y₁|a₁) is the **stationary signal distribution** under strategy s.

If (★★) holds, then the Cesàro averages of p_{Y₁}(s₁|hₜ) and p_{Y₁}(s₁*|hₜ) agree, giving p̄(s₁) = p̄(s₁*). Under the **not behaviorally confounded** condition adapted to the Markov case (see §3), this forces s₁ = s₁*. □

### 2.3 Step 3: Uniformity over equilibria (Lemma 3 from Lemma 9) ✓ (Minor changes)

The paper's uniformity argument uses:

**(a) Egorov's theorem:** If μₜ({ω_{s₁*}, ωᴿ}|h) → 1 Q-a.s., then for all ζ > 0, there exists G(ζ) with Q(G(ζ)) > 1 − ζ such that the convergence is uniform on G(ζ). **This is a general measure theory result — no i.i.d. needed.** ✓

**(b) Compactness of the strategy space B₁(s₁*)^{H^∞}:** The space of short-run player strategies mapping histories to actions in B₁(s₁*) is compact in the sup-norm topology. With Markov states, commitment types play Markov strategies s₁: Θ × Θ → Δ(A₁). Since Θ is finite, the space of Markov strategies is a compact subset of ℝ^{|Θ|²|A₁|}. The argument that B₁(s₁*)^{H^∞} is compact goes through identically. ✓

**(c) Continuity of finite-dimensional distributions:** As (σ₀, σ₂) → (σ₀^∞, σ₂^∞), the measures Q_{σ₀,σ₂} converge on finite-dimensional cylinders. This uses continuity of signal distributions in strategies, which holds for any signal structure (Markov or i.i.d.). ✓

**(d) Contradiction argument:** The proof constructs a sequence (σ₀^T, σ₂^T) → (σ₀^∞, σ₂^∞) such that convergence fails at time T for each T, and derives a contradiction with Lemma 9 for the limit strategies. The same argument applies verbatim. ✓

**Conclusion:** T̂(ζ) can be chosen independent of δ and the equilibrium, exactly as in the i.i.d. case.

---

## 3. The Filtering Subtlety

### 3.1 What the filter is

Under type ω_{s₁} with Markov states, the process is a hidden Markov model:
- Hidden state: θ̃ₜ = (θₜ, θ_{t-1}), evolving as a Markov chain with transition determined by F
- Observation: y₁ₜ ~ Σ_{a₁} s₁(θ̃ₜ)[a₁] ρ(·|a₁)

The **filtering distribution** π(θ̃|hₜ, s₁) = P(θ̃ₜ = θ̃ | y₁₀, ..., y₁,ₜ₋₁, ω = ω_{s₁}) is the Bayesian posterior over the current lifted state given the observation history and the type hypothesis.

### 3.2 Why the filter is NOT the stationary distribution

With i.i.d. states: π(θ|hₜ, s₁) = ρ(θ) for all hₜ — the filter is trivial because past observations carry no information about the current state.

With Markov states: past observations y₁₀, ..., y₁,ₜ₋₁ are informative about θ̃ₜ through the temporal dependence. The signal y₁,ₜ₋₁ reveals information about aₜ₋₁ (via signal identification), which reveals information about θ̃ₜ₋₁ = (θₜ₋₁, θₜ₋₂), and the Markov transition then constrains θₜ. So π(θ̃|hₜ, s₁) depends on the entire history.

### 3.3 Filter stability

For ergodic finite-state HMMs with "observable" emissions, the filter is **stable**: it forgets its initial condition exponentially fast. Formally, for any two initial distributions π₀, π₀':

||π(·|hₜ, s₁, π₀) − π(·|hₜ, s₁, π₀')||₁ → 0 exponentially in t

(See: Chigansky & Liptser, "Stability of nonlinear filters in nonmixing case," Ann. Appl. Probab. 2004.)

This means: regardless of what initial state distribution we assume, the filter converges to a unique trajectory determined by the observations. **This is important because it ensures that the per-period signal distribution p_{Y₁}(s₁|hₜ) is eventually independent of initial conditions.**

### 3.4 How the filter interacts with the convergence argument

The convergence (★★) says: the signal distributions p_{Y₁}(s₁|hₜ) and p_{Y₁}(s₁*|hₜ) agree asymptotically. These are computed using different filters (π(·|hₜ, s₁) and π(·|hₜ, s₁*)), because the emission models are different.

The filters under s₁ and s₁* process the same observations (the actual public history) but interpret them through different lenses. If s₁ ≠ s₁*, the filters will generally disagree about the current state, producing different predicted signal distributions. The convergence (★★) then provides a contradiction.

### 3.5 The key technical tool

The formal argument for Sub-step 2d relies on the **distinguishability of HMMs**: two finite-state HMMs with the same state dynamics but emission distributions that differ at some positively-recurrent state generate different observation laws. Under ergodicity (all states are positively recurrent) and signal identification (different actions give different emissions), this is guaranteed when s₁ ≠ s₁*.

References:
- Leroux (1992): MLE for HMMs (identifiability)
- Ito, Amari, Kobayashi (1992): identifiability of HMMs
- Petrie (1969): equivalence of finite-state HMMs

---

## 4. Ergodicity Condition — What We Need

### 4.1 Minimal condition

**(E1) Ergodicity:** The Markov chain F on Θ is irreducible and aperiodic.

This ensures:
- Unique stationary distribution π on Θ with π(θ) > 0 for all θ
- Unique stationary distribution π̃ on Θ × Θ for the lifted chain, with π̃(θ, θ') = π(θ') F(θ|θ') > 0 whenever F(θ|θ') > 0
- Geometric ergodicity (exponential mixing): ||P^t(·|θ₀) − π||₁ ≤ C r^t for some r < 1
- Filter stability for the HMM

### 4.2 For the "not behaviorally confounded" condition

**(E2) Full-support transitions (optional, for strongest results):** F(θ|θ') > 0 for all θ, θ' ∈ Θ.

This ensures π̃ has full support on Θ × Θ. Without this, π̃(θ, θ') = 0 for some pairs, and two strategies that differ only on zero-probability state pairs would be indistinguishable. With (E2), the "not behaviorally confounded" condition reduces to: s₁' ≠ s₁* as functions on Θ × Θ (given signal identification).

If (E2) fails (some transitions have probability 0), the condition becomes: for some (θ, θ') with F(θ|θ') > 0, the signal distributions under s₁'(θ, θ') and s₁*(θ, θ') differ.

### 4.3 Quantitative requirements

The mixing time τ_mix enters the bounds as follows:
- **Counting bound (Lemma 2):** T̄(η, μ₀) = −2 log μ₀(ω_{s₁*})/η² — does NOT depend on τ_mix (as Subagent 1 establishes)
- **Martingale convergence (Lemma 9):** The rate of convergence of μₜ to μ_∞ depends on the filter convergence rate, which is controlled by min(spectral gap of F, signal identification strength). But the existence of convergence only requires ergodicity (no quantitative mixing time).
- **Uniformity (Lemma 3):** T̂(ζ) depends on the rate of almost-sure convergence in Lemma 9, which in turn depends on τ_mix. But T̂(ζ) is finite for any ergodic chain with finite Θ.

### 4.4 Recovery of i.i.d. case

When F is independent of θ_{t-1} (i.e., F(θ|θ') = ρ(θ) for all θ'), the chain has mixing time τ_mix = 0, the filter is trivial (π(θ̃|hₜ, s₁) = π̃(θ̃) for all hₜ), and all results reduce to the paper's versions. ✓

### 4.5 Behavior as persistence → ∞

As the Markov chain approaches perfect persistence (F(θ|θ) → 1 for all θ):
- τ_mix → ∞
- The filter becomes very "sticky" — it takes many observations to update beliefs about the hidden state
- T̂(ζ) → ∞ (convergence becomes arbitrarily slow)
- The bounds remain valid but become vacuous in the limit

This is consistent with Pei (2020), who studies the perfectly persistent limit and finds that reputation effects require different (and more restrictive) conditions.

---

## 5. Extended Statement of Lemma 3

**Lemma 3 (Markov version).** Let θₜ follow an ergodic Markov chain (E1) on finite Θ. For all ζ > 0, there exists a set G(ζ) ⊂ H^∞ satisfying Q(G(ζ)) > 1 − ζ and a period T̂(ζ) — independent of δ and the choice of equilibrium — such that, for any h ∈ G(ζ) and any t ≥ T̂(ζ):

μₜ(·|h) ∈ M_ζ = {μ ∈ Δ(Ω) : μ({ωᴿ, ω_{s₁*}}) ≥ 1 − ζ}

**Proof sketch:** Lemma 9 (Markov version) gives Q-a.s. convergence for each equilibrium. Egorov's theorem gives uniform convergence on a large-measure set. The compactness argument makes T̂ independent of the equilibrium and δ. All three steps go through without i.i.d. as detailed in §2. □

---

## 6. Gaps and Risks

### 6.1 Risk: HMM distinguishability with misspecified models (Medium)

The convergence argument operates under Q, where the actual observations are generated by a **mixture** of types. The filters π(·|hₜ, s₁) and π(·|hₜ, s₁*) are both "misspecified" relative to the true data-generating process (the Q-mixture). The standard HMM distinguishability results assume correctly specified models. We need that under Q-typical histories, the predicted signal distributions under two different types eventually differ. While this should hold under ergodicity and signal identification (because the Q-mixture is absolutely continuous with respect to each type's measure), a rigorous proof requires careful analysis of filter behavior under model misspecification.

**Mitigation:** The alternative "ergodic averages" argument (end of Sub-step 2d) avoids this issue by working with Cesàro averages, which converge to the stationary signal distributions regardless of filter behavior.

### 6.2 Risk: "Not behaviorally confounded" condition may be too strong (Low)

In the i.i.d. case, "not behaviorally confounded" is about the marginal signal distribution at the stationary state distribution ρ. In the Markov case, the condition at the stationary distribution π̃ is the natural analogue. However, this might exclude some strategies that are actually distinguishable via temporal patterns (even though their stationary signal distributions agree).

**Assessment:** This is a feature, not a bug. The theorem statement uses a clean, easily stated condition. A sharper condition involving temporal distinguishability would be strictly weaker but harder to state and verify.

### 6.3 Risk: Aperiodicity assumption (Low)

Aperiodicity is used for geometric ergodicity and filter stability. If the chain is periodic (period d), the filter oscillates with period d, but the time-d subsequence is still ergodic. The results would hold along subsequences, and the overall conclusion (μ_∞ concentrates on {ωᴿ, ω_{s₁*}}) is unaffected. Aperiodicity is assumed for cleanness, not necessity.

### 6.4 Gap: Explicit dependence of T̂ on chain parameters

The bound T̂(ζ) depends on the mixing time of F and the filter convergence rate, but we have not computed this dependence explicitly. For applications, one would want:

T̂(ζ, τ_mix) ≤ C(ζ) · poly(τ_mix)

This is plausible given that filter stability is geometric for ergodic HMMs, but the explicit constants would need to be worked out.

### 6.5 Summary assessment

| Component | Status | i.i.d. needed? |
|-----------|--------|----------------|
| μₜ is Q-martingale | ✅ Goes through | No |
| Martingale convergence | ✅ Goes through | No |
| Bayesian update → signal convergence (★) | ✅ Goes through | No |
| KL bound → mixture convergence | ✅ Goes through | No |
| Signal convergence → s₁ = s₁* | ⚠️ Needs adapted "not b.c." condition | Replaced by ergodicity |
| Egorov's theorem | ✅ Goes through | No |
| Compactness of B₁(s₁*)^{H^∞} | ✅ Goes through | No |
| Uniformity of T̂ | ✅ Goes through | No |

**Bottom line:** Lemma 3 extends to Markov states under ergodicity (E1), with the "not behaviorally confounded" condition evaluated at the stationary distribution π̃. The proof structure is essentially unchanged; the only substantive modification is in Sub-step 2d, where the original paper uses the history-independence of i.i.d. signal distributions, and we instead invoke HMM distinguishability (or, more elementarily, the ergodic theorem for Cesàro averages).
