# Subagent 1 Report: KL Divergence Counting Bound for Markov Chains

**Task:** Extend Lemma 2 of Luo & Wolitzky (2024) from i.i.d. states to Markovian states.  
**Result:** The bound holds **exactly as stated** — no correction factor is needed.

---

## 1. Statement of Extended Lemma 2

**Lemma 2 (Markov Extension).** Fix a Nash equilibrium $(\sigma_0^*, \sigma_1^*, \sigma_2^*)$ and let $Q$ denote the probability measure over infinite histories induced by the deviation where the long-run player plays $s_1^*$ in every period (while players 0 and 2 continue to play equilibrium strategies). Let $\theta_t$ follow a stationary ergodic Markov chain with transition kernel $F(\cdot | \theta_{t-1})$ and stationary distribution $\pi$. Then:

$$E_Q\left[\#\left\{t : h_t \notin H_t^\eta\right\}\right] < \bar{T}(\eta, \mu_0) := \frac{-2\log \mu_0(\omega_{s_1^*})}{\eta^2}$$

where $H_t^\eta = \{h_t : \|p(\sigma_0^*, s_1^*, \sigma_2^* | h_t) - p(\sigma_0^*, \sigma_1^*, \sigma_2^* | h_t)\| \leq \eta\}$.

**This is identical to the i.i.d. bound.** No mixing-time correction $C(\tau_{\text{mix}})$ is required.

---

## 2. Proof Sketch

The proof has two steps: (A) a total KL divergence bound from Bayesian updating, and (B) conversion to a counting bound via Pinsker's inequality. Neither step uses i.i.d.

### Step A: Total KL Divergence Bound

**Claim.** For any $T \geq 1$:

$$\sum_{t=0}^{T-1} E_Q\left[D\!\left(p(\sigma_0^*, s_1^*, \sigma_2^* | h_t) \;\|\; p(\sigma_0^*, \sigma_1^*, \sigma_2^* | h_t)\right)\right] \leq -\log \mu_0(\omega_{s_1^*})$$

**Proof.** Let $P$ be the equilibrium measure (mixture over all types weighted by $\mu_0$) and $Q = P_{\omega_{s_1^*}}$ be the measure conditional on the long-run player being the commitment type $\omega_{s_1^*}$.

**Step A.1 (Bayes' rule).** By Bayes' rule, the posterior on $\omega_{s_1^*}$ satisfies:

$$\mu_T(\omega_{s_1^*} | h_T) = \mu_0(\omega_{s_1^*}) \cdot \frac{dQ^T(h_T)}{dP^T(h_T)}$$

where $dQ^T / dP^T$ is the Radon-Nikodym derivative (likelihood ratio) of the first $T$ signals under $Q$ versus $P$. Since $\mu_T(\omega_{s_1^*}) \leq 1$:

$$\frac{dQ^T(h_T)}{dP^T(h_T)} \leq \frac{1}{\mu_0(\omega_{s_1^*})}$$

**Step A.2 (Chain rule for log-likelihoods).** The log-likelihood ratio decomposes along the signal sequence:

$$\log \frac{dQ^T}{dP^T}(h_T) = \sum_{t=0}^{T-1} \log \frac{q_t(y_t | h_t)}{p_t(y_t | h_t)}$$

where $q_t(\cdot | h_t) = p(\sigma_0^*, s_1^*, \sigma_2^* | h_t)$ and $p_t(\cdot | h_t) = p(\sigma_0^*, \sigma_1^*, \sigma_2^* | h_t)$ are the period-$t$ signal distributions under $Q$ and $P$, respectively. **This decomposition is the chain rule for conditional densities and holds for any stochastic process** — it does not require independence across periods.

**Step A.3 (Taking expectations).** Taking $E_Q$ of both sides:

$$E_Q\left[\log \frac{dQ^T}{dP^T}\right] = \sum_{t=0}^{T-1} E_Q\left[E_Q\left[\log \frac{q_t(y_t | h_t)}{p_t(y_t | h_t)} \;\bigg|\; h_t\right]\right] = \sum_{t=0}^{T-1} E_Q\left[D(q_t(\cdot|h_t) \| p_t(\cdot|h_t))\right]$$

From Step A.1, $\log(dQ^T / dP^T) \leq -\log \mu_0(\omega_{s_1^*})$ pointwise, and since this holds for every history:

$$\sum_{t=0}^{T-1} E_Q\left[D(q_t(\cdot|h_t) \| p_t(\cdot|h_t))\right] \leq -\log \mu_0(\omega_{s_1^*})$$

**Crucially:** Steps A.1–A.3 use only Bayes' rule and the chain rule for conditional distributions. The state process $\{\theta_t\}$ can be i.i.d., Markov, or any adapted stochastic process — the bound is unchanged. $\square$

### Step B: Counting Bound via Pinsker's Inequality

**Claim.** If $h_t \notin H_t^\eta$, then $D(q_t(\cdot|h_t) \| p_t(\cdot|h_t)) > \eta^2/2$.

**Proof.** By Pinsker's inequality (a pointwise inequality, no distributional assumptions):

$$\|q_t(\cdot|h_t) - p_t(\cdot|h_t)\|_{TV} \leq \sqrt{2\,D(q_t(\cdot|h_t) \| p_t(\cdot|h_t))}$$

Contrapositive: if $\|q_t - p_t\| > \eta$, then $D(q_t \| p_t) > \eta^2 / 2$. $\square$

**Combining Steps A and B.** Let $\bar{N}$ be the expected number of periods where $h_t \notin H_t^\eta$. At each such period, $D_t := D(q_t(\cdot|h_t) \| p_t(\cdot|h_t)) > \eta^2/2$. Since KL divergences are non-negative:

$$\bar{N} \cdot \frac{\eta^2}{2} \leq \sum_{t=0}^{T-1} E_Q[D_t] \leq -\log \mu_0(\omega_{s_1^*})$$

$$\implies \bar{N} \leq \frac{-2\log \mu_0(\omega_{s_1^*})}{\eta^2} = \bar{T}(\eta, \mu_0)$$

This completes the proof. $\square$

---

## 3. Key Insight: Why i.i.d. Is Not Needed

The original proof of Lemma 2 **never uses the i.i.d. assumption**. The two ingredients are:

| Ingredient | What it requires | i.i.d. needed? |
|---|---|---|
| Total KL bound $\sum D_t \leq -\log \mu_0$ | Bayes' rule + chain rule for KL | **No.** Bayes' rule is valid for any stochastic process. The chain rule $D(P_{X,Y} \| Q_{X,Y}) = D(P_X \| Q_X) + E_P[D(P_{Y|X} \| Q_{Y|X})]$ holds for arbitrary joint distributions. |
| Pinsker's inequality $D \geq \eta^2/2$ when $\|P-Q\| > \eta$ | Pointwise property of divergence | **No.** Pinsker's inequality is a property of individual distributions, not of sequences. |
| Counting argument: if each "bad" period contributes $\geq \eta^2/2$ to a sum bounded by $K$, there are $\leq 2K/\eta^2$ bad periods | Arithmetic | **No.** This is just the pigeonhole principle. |

**The confusion about needing a mixing-time correction** arises from conflating two different uses of independence:

1. **KL divergence summation** (used here): The chain rule $D(Q^T \| P^T) = \sum E_Q[D(q_t \| p_t)]$ holds for **any** sequential process. This is because it is simply the telescoping of conditional KL divergences. Independence is irrelevant.

2. **Concentration inequalities** (NOT used here): Bounds like Hoeffding's inequality or the law of large numbers for $\frac{1}{T}\sum X_t$ do require independence or mixing. But Lemma 2 does not use concentration — it uses a **total sum bound**, not a rate-of-convergence bound.

The i.i.d. assumption in the paper is used elsewhere (Lemma 3's martingale convergence, the stationarity of the stage game), but Lemma 2 stands alone without it.

---

## 4. Verification: Recovery of the i.i.d. Case

When $F(\cdot | \theta_{t-1}) = \pi(\cdot)$ for all $\theta_{t-1}$ (i.i.d. states):

- The Markov chain has mixing time $\tau_{\text{mix}} = 0$ (already mixed).
- The lifted state $\tilde{\theta}_t = (\theta_t, \theta_{t-1})$ has distribution $\pi \otimes \pi$ (product, since states are independent).
- The bound reduces to $\bar{T}(\eta, \mu_0) = -2\log\mu_0(\omega_{s_1^*})/\eta^2$, which is **exactly** the paper's Lemma 2.

Since the bound is identical in the Markov and i.i.d. cases, recovery is trivially verified.

---

## 5. Caveats and Additional Remarks

### 5.1 No additional conditions needed for Lemma 2

The counting bound requires **no** ergodicity, stationarity, or finite mixing time. It holds for **any** state process — even non-stationary, non-ergodic, or adversarially chosen states. The only requirement is that the commitment type $\omega_{s_1^*}$ exists in the type space $\Omega$ with prior probability $\mu_0(\omega_{s_1^*}) > 0$.

### 5.2 What the commitment type plays in the Markov case

In the i.i.d. case, the commitment type plays $s_1^*: Y_0 \to \Delta(A_1)$ every period. In the Markov case with the lifted-state approach, the commitment type should play a **Markov strategy** $s_1^*: \Theta \times \Theta \to \Delta(A_1)$ (conditioning on $(\theta_t, \theta_{t-1})$). However, this does not affect Lemma 2 at all — the bound depends only on $\mu_0(\omega_{s_1^*})$, not on the form of $s_1^*$.

For the simpler case where the commitment type conditions only on $\theta_t$ (i.e., $s_1^*: \Theta \to \Delta(A_1)$, ignoring $\theta_{t-1}$), the bound still holds with no change.

### 5.3 The mixing time enters elsewhere, not here

The mixing time $\tau_{\text{mix}}$ is relevant for:
- **Lemma 3** (martingale convergence / belief merging): The rate at which the posterior $\mu_t$ concentrates on $\{\omega_R, \omega_{s_1^*}\}$ may depend on mixing properties when signals are dependent.
- **The OT / confound-defeating analysis**: The stationary distribution $\tilde{\rho}$ on the lifted state space determines the optimal transport problem.
- **The uniformity argument**: Compactness of the strategy space now involves Markov strategies.

But for Lemma 2 specifically, **the mixing time is irrelevant**.

### 5.4 Intuition for why the bound is process-independent

The KL divergence bound $\sum D_t \leq -\log \mu_0$ is fundamentally a statement about **Bayesian learning capacity**: there are only $-\log \mu_0$ "nats" of surprise available for distinguishing the commitment type from the equilibrium play. Each distinguishing period "uses up" at least $\eta^2/2$ nats. This budget constraint is purely information-theoretic and has nothing to do with the temporal structure of the signal-generating process.

---

## 6. Summary

| | i.i.d. case (paper) | Markov case (extension) |
|---|---|---|
| **Bound** | $\bar{T} = -2\log\mu_0(\omega_{s_1^*})/\eta^2$ | $\bar{T} = -2\log\mu_0(\omega_{s_1^*})/\eta^2$ |
| **Proof tools** | Bayes' rule + KL chain rule + Pinsker | Bayes' rule + KL chain rule + Pinsker |
| **Correction factor** | None | **None** |
| **Additional conditions** | $\mu_0(\omega_{s_1^*}) > 0$ | $\mu_0(\omega_{s_1^*}) > 0$ |

**Bottom line:** Lemma 2 extends to the Markov case **verbatim**. The i.i.d. assumption is not used in its proof. The first-parse conjecture that a mixing-time correction $C(\tau_{\text{mix}})$ would be needed was incorrect — the bound is tighter than initially expected.
