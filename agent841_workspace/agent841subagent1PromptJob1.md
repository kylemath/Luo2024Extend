# Subagent 1 — Job 1: KL Divergence Counting Bound for Markov Chains

**Assigned by:** Agent 841  
**Deliverable:** `agent841_workspace/agent841subagent1Report.md`  
**Deadline:** ASAP (we have ~50 minutes total)

---

## Context

We are extending the main result (Theorem 1) of "Marginal Reputation" by Luo & Wolitzky (2024) from **i.i.d. states** to **Markovian states**. The paper is in `paper/Marginal_Reputation Dec 17 2024.md` and the first parse summary is in `AgentReports/Feb16_840_firstParse.md`.

## Your Task

**Extend Lemma 2 (the KL divergence counting bound) to Markov chains.**

### What Lemma 2 says in the i.i.d. case

In the paper, Lemma 2 bounds the expected number of "distinguishing periods" — periods t where the equilibrium signal distribution p(σ₀*, σ₁*, σ₂*|hₜ) differs from the commitment-type signal distribution p(σ₀*, s₁*, σ₂*|hₜ) by more than η in total variation. The bound is:

$$\bar{T}(\eta, \mu_0) = \frac{-2\log\mu_0(\omega_{s_1^*})}{\eta^2}$$

This uses the fact that the KL divergence D(p(σ₀*, s₁*, σ₂*|hₜ) || p(σ₀*, σ₁*, σ₂*|hₜ)) sums to at most -log μ₀(ω_{s₁*}) across all periods (a standard result from the information-theoretic approach to reputation, originating in Gossner 2011). With i.i.d. states, per-period KL divergences are independent, so the sum telescopes cleanly.

### What you need to do

1. **State the problem precisely:** With Markov states θₜ ~ F(·|θ_{t-1}), the lifted state θ̃ₜ = (θₜ, θ_{t-1}) has stationary distribution ρ̃ but consecutive lifted states overlap (they share θₜ). Per-period signal distributions are no longer independent.

2. **Derive the analogous bound:** Show that the expected number of distinguishing periods is bounded by approximately:

$$\bar{T}(\eta, \mu_0, \tau_{\text{mix}}) \approx \frac{-2\log\mu_0(\omega_{s_1^*})}{\eta^2} \cdot C(\tau_{\text{mix}})$$

where C(τ_mix) is a correction factor depending on the mixing time.

3. **Key tools to use:**
   - The **data-processing inequality** for KL divergence
   - The **chain rule** for KL divergence: D(P_{X,Y} || Q_{X,Y}) = D(P_X || Q_X) + E_P[D(P_{Y|X} || Q_{Y|X})]
   - For Markov chains, the joint KL divergence over T periods decomposes as:
     D(P^T || Q^T) = Σ_{t=1}^T E_P[D(P_{y_t|h_{t-1}} || Q_{y_t|h_{t-1}})]
   - This decomposition holds even without i.i.d. because KL divergence has the **chain rule property for conditional distributions**.

4. **The key insight:** The total KL divergence bound -log μ₀(ω_{s₁*}) still holds regardless of whether states are i.i.d. or Markovian. This is because:
   - The Bayesian updating formula gives: μ_T(ω_{s₁*}) = μ₀(ω_{s₁*}) · Π_{t=0}^{T-1} [p(y_t | s₁*, hₜ) / p(y_t | σ₁*, hₜ)]
   - Taking logs: log(μ_T/μ₀) = Σ log-likelihood ratios
   - Since μ_T ≤ 1: Σ_{t=0}^{T-1} log(p(y_t|σ₁*,hₜ)/p(y_t|s₁*,hₜ)) ≤ -log μ₀(ω_{s₁*})
   - This is just Bayesian updating — it does NOT require i.i.d.!

5. **The correction needed:** With Markov states, even though the total KL bound holds, the per-period KL divergences D_t are NOT independent. To convert total KL ≤ K into a bound on the number of periods where ||p - p*|| > η, we need:
   - Pinsker's inequality: ||P-Q||² ≤ 2D(P||Q) (this is pointwise, no i.i.d. needed)
   - If D_t ≥ η²/2 at most T̄ periods, then Σ D_t ≥ T̄ · η²/2
   - Since Σ D_t ≤ -log μ₀, we get T̄ ≤ -2log μ₀/η²
   - **This bound holds without ANY i.i.d. assumption!**

6. **Conclusion to reach:** The counting bound T̄(η, μ₀) = -2log μ₀(ω_{s₁*})/η² holds **exactly as stated** in the Markov case. The i.i.d. assumption is NOT used in Lemma 2 — only the chain rule for KL divergence and Pinsker's inequality are needed, both of which hold for arbitrary (including Markov) signal distributions.

## Deliverable Format

Write your report in `agent841_workspace/agent841subagent1Report.md` with:
1. **Statement** of the extended Lemma 2
2. **Proof sketch** showing each step
3. **Key insight** explaining why i.i.d. is not needed here
4. **Verification** that the bound recovers the paper's version when F is independent of θ_{t-1}
5. **Any caveats** or additional conditions needed

Be rigorous but concise. We are writing a proof sketch, not a publication.
