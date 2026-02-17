**Extending "Marginal Reputation" (Luo & Wolitzky 2024) to Markov States**
*Kyle Mathewson — University of Alberta, Faculty of Science*

**Claim.** Lemma 2's KL counting bound holds verbatim for $\theta_t \sim F(\cdot|\theta_{t-1})$. No mixing-time correction.

$$E_Q\!\left[\#\{t : \|q_t - p_t\| > \eta\}\right] < \bar{T} := \frac{-2\log \mu_0(\omega_{s_1^*})}{\eta^2}$$

**Proof.** Let $P$ = equilibrium measure, $Q = P_{\omega_{s_1^*}}$ = commitment-type measure, $q_t,p_t$ = period-$t$ signal distributions given $h_t$.

**(1) Bayes.** $\mu_T(\omega_{s_1^*}|h_T) = \mu_0(\omega_{s_1^*})\cdot\frac{dQ^T}{dP^T} \leq 1 \;\implies\; \frac{dQ^T}{dP^T} \leq \frac{1}{\mu_0(\omega_{s_1^*})}$

**(2) Chain rule.** $\log\frac{dQ^T}{dP^T} = \sum_{t=0}^{T-1}\log\frac{q_t(y_t|h_t)}{p_t(y_t|h_t)}$ — telescoping identity, valid for *any* process.

**(3) Expectation.** $\sum_{t=0}^{T-1}E_Q\!\left[D(q_t\|p_t)\right] \leq -\log\mu_0(\omega_{s_1^*})$ — follows from (1)+(2).

**(4) Pinsker.** $\|q_t - p_t\|>\eta \implies D(q_t\|p_t)>\eta^2/2$ — pointwise, no independence needed.

**(5) Counting.** $\bar{N}\cdot\frac{\eta^2}{2} \leq \sum E_Q[D_t] \leq -\log\mu_0 \implies \bar{N} \leq \frac{-2\log\mu_0(\omega_{s_1^*})}{\eta^2} = \bar{T}$ $\;\square$

**Key insight:** The bound is a total KL *budget* constraint ($-\log\mu_0$ nats), not a rate-of-convergence result. Bayes' rule, KL chain rule, and Pinsker are all process-independent. The mixing-time conjecture confused KL summation (any process) with concentration inequalities (needs independence).

For full Thm 1: lift $\tilde{\theta}_t=(\theta_t,\theta_{t-1})$, stationary dist $\tilde{\rho}$ on $\Theta\!\times\!\Theta$. OT problem + confound-defeating carry over. Supermodular case $\Rightarrow$ monotonicity in $(\theta_t,\theta_{t-1})$. Full PDF dropping shortly.
