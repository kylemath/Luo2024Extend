# Extending Marginal Reputation to Persistent Markovian States

**Date**: 2/18/2026, 9:02:57 AM
**Domain**: social_sciences/economics
**Taxonomy**: academic/research_paper
**Filter**: Active comments

---

## Overall Feedback

Here are some overall reactions to the document.

**Alignment of predictive beliefs with short-run optimization**

In Sections 1.1 and 3, the manuscript defines the key Markov phenomenon via short-run learning $\theta_t$ and the predictive belief $F(\cdot\mid \theta_t)=\mathbb P(\theta_{t+1}=\cdot\mid \theta_t)$. This definition is central to the concept of belief-robustness (Definition 3.2) and the state-contingent Nash correspondence used in Theorems 4.3 and 4.6. However, the maintained primitives in Section 2.3 restrict payoffs to depend only on the *current* state, $u_1(\theta_t,a_1,\alpha_2)$. Because short-run players are typically modeled as maximizing current-period payoffs, readers will likely pause here: it is not immediately obvious why a one-step-ahead belief about $\theta_{t+1}$ enters the period-$t$ best response if the payoff function does not depend on the future state. This misalignment makes the correspondence $B(s_1^*,F(\cdot\mid\theta))$ difficult to interpret, as it does not clearly map to the optimization problem implied by the timeline and payoff dependence.

**Consistency between the lifted state construction and payoff bounds**

The paper builds its machinery on a lifted state space $\tilde{\Theta}=\Theta\times\Theta$ with a stationary distribution $\tilde{\rho}$, allowing for commitment strategies $s_1$ that condition on transition history. However, the core payoff bound in Definition 4.5 is formulated as $V_{\text{Markov}}(s_1^*)=\sum_{\theta\in\Theta}\pi(\theta)\inf u_1...$ which evaluates the strategy solely at $\theta$ and averages over the marginal distribution $\pi$. This creates a disconnect: if the strategy $s_1^*$ genuinely utilizes the lifted state (conditioning on $\theta_{t-1}$), the induced joint distribution over actions and states is a $\tilde{\rho}$-based object (as noted in Section 2.4). To ensure the bound is logically consistent with the confound-defeating condition and the commitment type's behavior, the payoff formulation likely needs to be defined on the same state space as the commitment strategy.

**Establishing supermodularity with endogenous continuation values**

Section 5.3 identifies a critical challenge in the extension: the one-shot deviation objective involves a history-dependent continuation term, taking the form $u_1(\tilde\theta,a_1,\alpha_2)+\delta g(\theta_t,a_1,h_t)$. As the review correctly notes, adding a state-dependent term can alter the optimal transport solution. The manuscript currently addresses this in Remark 5.4 by asserting that "$g$ preserves the supermodular structure." Since $g$ is an endogenous equilibrium object, this is a distinct property that requires formal proof; it is not immediate that equilibrium continuation values satisfy the specific monotonicity required to preserve the supermodularity of $u_1$. Similarly, the argument relying on "filter stability + $\delta\to 1$" requires more rigorous justification, as $\delta\to 1$ typically increases the weight of continuation values relative to stage payoffs. Because this step is foundational for the equilibrium-implication machinery, the validity of the extension rests on closing this gap formally.

**The logical necessity of belief-robustness for value equality**

The Abstract and Theorem 4.6 present the condition "if and only if belief-robustness holds" as the criterion for $V_{\text{Markov}}(s_1^*)=V(s_1^*)$. Belief-robustness is defined as the invariance of the short-run best-reply *sets* across beliefs (Definition 3.2). While set invariance is sufficient for the values to match, it is not obviously necessary; the infima of payoffs over different sets could coincide for other reasons. Furthermore, proving necessity would likely require additional regularity explicitly assumed in the hypothesis, such as uniqueness of best replies or strictness of the equilibrium. Without these provisions, the "if and only if" claim appears stronger than what the definitions logically support.

**Robustness of the "cost of persistence" and the worked example**

The "cost of persistence" is a central economic contribution of the paper, but the evidence supporting it in Section 7 invites close scrutiny. The worked example contains values (e.g., $\mu^*=0.60$ and $\beta=0.5$) that seem to conflict with the resulting analysis in Section 7.4. More largely, the derivation of the threshold $\mu^*$ and the short-run payoff function $u_2$ are not specified in enough detail to allow a reader to verify the calculation of $B(s_1^*,\mu)$. Additionally, Section 10.2 raises a conceptual risk: if an $\varepsilon$-perturbed commitment strategy forces beliefs to converge to stationarity via filter stability, the gap $V(s_1^*)-V_{\text{Markov}}(s_1^*)$ might vanish. If this cost is an artifact of perfectly state-revealing strategies that disappears with arbitrarily small noise, the economic interpretation of this cost as a robust feature of Markov persistence needs to be carefully qualified.

**Balancing the theoretical contribution with the methodological narrative**

Section 9 devotes substantial space to documenting the "human-AI collaboration" process, including timestamps and prompt strategies. While this transparency is novel, its prominence creates a tension with the theoretical objectives of the paper. Theoretically focused readers and reviewers typically look for mathematical closure on key steps—specifically the supermodularity issues in Section 5.3—and may view the extensive process documentation as a distraction from, or a substitute for, those proofs. To maximize the impact of the theoretical contribution, it would be beneficial to separate the proved theorems from the computational stress-tests, ensuring that the limits of what has been analytically established versus empirically simulated are sharply delineated.

**Status**: [Pending]

---

## Detailed Comments (21)

### 1. Incorrect scaling of continuation values

**Status**: [Pending]

**Quote**:
> Combined with $\delta \to 1$ (which makes the continuation value perturbation small relative to the stage-game payoff), this yields the result.

**Feedback**:
The sentence “Combined with $\delta \to 1$ (which makes the continuation value perturbation small relative to the stage-game payoff)” seems to use the wrong asymptotic intuition. Under the usual normalization with discounted average payoff, the one-shot deviation objective at a history is of the form
\[
(1-\delta)u_1(\theta_t,a_1,\alpha_2) + \delta \mathbb{E}[V(h_{t+1})]
\]
(or an equivalent rescaling). As $\delta \to 1$, the weight on continuation payoffs does not become small relative to the current-stage payoff; if anything, the continuation term becomes more important.

Here you appear to be combining filter stability (which makes the state distribution close to stationary in large $t$) with the fact that finitely many early periods receive vanishing weight in the normalized payoff as $\delta \to 1$. If the intended “perturbation” is the finite-horizon effect of periods before the filter has converged, it would be helpful to say that explicitly and avoid language suggesting that continuation payoffs are downweighted in the Bellman equation when $\delta$ is close to 1. 

Since this continuity-plus-$\delta\to 1$ route is presented as a way to handle the general Markov case without strengthening confound-defeating, a more precise explanation of how bounded continuation values, filter stability, and the $\delta \to 1$ limit interact would strengthen the argument. Otherwise, one may need to lean on the stronger confound-defeating assumption you mention earlier in the remark.

---

### 2. Incorrect Generalization of the Payoff Bound Inequality

**Status**: [Pending]

**Quote**:
> Theorem 1" (general case): the Markov commitment payoff $V_{\text {Markov }}\left(s_{1}^{*}\right)=\sum_{\theta} \pi(\theta)$. $\inf _{B\left(s_{1}^{*}, F(\cdot \mid \theta)\right)} u_{1} \leq V\left(s_{1}^{*}\right)$ provides the appropriate bound, with equality if and only if the game is belief-robust. The gap $V\left(s_{1}^{*}\right)-V_{\text {Markov }}$ quantifies the cost of persistence

**Feedback**:
The statement that $V_{\text{Markov}}(s_1^*) \leq V(s_1^*)$ holds generally, and the resulting interpretation of $V(s_1^*) - V_{\text{Markov}}(s_1^*)$ as a non‑negative “cost of persistence,” seem unjustified at the level of generality claimed. 

As defined, $V(s_1^*)$ is the i.i.d. commitment payoff under the stationary distribution $\pi$, while $V_{\text{Markov}}(s_1^*)$ averages state‑contingent commitment payoffs using the belief‑dependent correspondences $B(s_1^*,F(\cdot\mid\theta))$. It is not evident, and not proved in the paper, that for all supermodular games one must have $V_{\text{Markov}}(s_1^*) \le V(s_1^*)$. Indeed, in regimes where $\pi(G)$ lies below the SR cooperation threshold $\mu^*$ (so the i.i.d. benchmark yields defection and a low $V(s_1^*)$) but $F(G\mid G)>\mu^*$ while $F(G\mid B)<\mu^*$, persistence can permit cooperation in good states only. In such a case one can have $V_{\text{Markov}}(s_1^*)>V(s_1^*)$.

Unless additional structure is imposed that rules out such configurations and delivers $V_{\text{Markov}} \le V$ as a theorem, it would be better either to omit the inequality from Theorem 4.6 and the abstract, or to qualify it as holding only under clearly stated extra conditions (for example, in the specific deterrence parametrization you analyze). The main equilibrium guarantee $\liminf_{\delta\to 1}\underline U_1(\delta)\ge V_{\text{Markov}}(s_1^*)$ is unaffected by this adjustment.

---

### 3. Contradictory i.i.d. benchmark values in worked example

**Status**: [Pending]

**Quote**:
> Commitment payoff (i.i.d. benchmark): Under $s_{1}^{*}(G)=A, s_{1}^{*}(B)=F$:
$$
V\left(s_{1}^{*}\right)=\pi(G) \cdot u_{1}(G, A)+\pi(B) \cdot u_{1}(B, F)=0.625 \times 1+0.375 \times 0=0.625 .
$$
Comparison with i.i.d.: If the state were i.i.d. with $\mathbb{P}(G)=0.625$, the Stackelberg payoff would be identical ( $p=0.625$ ).

**Feedback**:
The worked example currently uses two different quantities as “i.i.d. benchmarks,” and this creates a numerical inconsistency with Theorem 4.6.

Section 7.6 computes
$$
V(s_1^*)=\pi(G)u_1(G,A)+\pi(B)u_1(B,F)=0.625,
$$
and describes this as both the “commitment payoff (i.i.d. benchmark)” and the Stackelberg payoff when the state is i.i.d. with $\mathbb{P}(G)=0.625$. In the next subsection and in Figure 2, however, the “Stationary beliefs (i.i.d. assumption)” payoff is given as 0.777. In addition, Section 1 and Section 8.5 present 0.777 (vs. 0.628) as the overestimated “commitment payoff” under the i.i.d. analysis.

Read together, this makes it unclear which number is supposed to be the commitment payoff $V(s_1^*)$ for the calibration used in 7.5–7.7. As written, the explicit computations $V_{\text{Markov}}(s_1^*)=0.628$ (in 7.5) and $V(s_1^*)=0.625$ (in 7.6) also appear to violate the theorem’s inequality $V_{\text{Markov}}(s_1^*)\le V(s_1^*)$.

It would help to reconcile these figures by (i) clearly identifying which value is $V(s_1^*)$ for the underlying deterrence payoffs, (ii) explaining how the 0.777 “stationary-beliefs payoff” relates to that benchmark (e.g., as an equilibrium payoff under a particular SR best response, not as the infimum over best responses), and (iii) ensuring that the displayed numerical values do satisfy $V_{\text{Markov}}(s_1^*)\le V(s_1^*)$ for the chosen parameters.

---

### 4. Incorrect formulation of Markov Commitment Payoff

**Status**: [Pending]

**Quote**:
> $$V_{\text {Markov }}\left(s_{1}^{*}\right):=\sum_{\theta \in \Theta} \pi(\theta) \cdot \inf _{\left(\alpha_{0}, \alpha_{2}\right) \in B\left(s_{1}^{*}, F(\cdot \mid \theta)\right)} u_{1}\left(\theta, s_{1}^{*}(\theta), \alpha_{2}\right) .$$

**Feedback**:
The definition of the Markov commitment payoff in Definition 4.5,
\[
V_{\text {Markov }}\left(s_{1}^{*}\right):=\sum_{\theta \in \Theta} \pi(\theta) \cdot \inf _{\left(\alpha_{0}, \alpha_{2}\right) \in B\left(s_{1}^{*}, F(\cdot \mid \theta)\right)} u_{1}\left(\theta, s_{1}^{*}(\theta), \alpha_{2}\right),
\]
pairs the belief argument of $B(\cdot)$ with the same state $\theta$ that enters the payoff $u_1(\theta,\cdot,\cdot)$. In a Markov environment with state-revealing strategies and the lifted state $(\theta_t,\theta_{t-1})$, it is not entirely transparent from the text whether the short-run player’s belief in period $t$ should be indexed by the *current* state $\theta_t$ or the *previous* state $\theta_{t-1}$, and how this aligns with the “current state” appearing in $u_1$.

If the short-run player in each period observes only history up to $t-1$ and uses the transition kernel to infer the distribution of the payoff-relevant state, then her belief about that state is naturally $F(\cdot\mid \theta_{t-1})$, while the payoff depends on $\theta_t$. In that case, the lower bound might be more naturally written in terms of the lifted stationary distribution $\tilde\rho(\theta_t,\theta_{t-1})$, with the best-response correspondence depending on the second coordinate and the payoff on the first.

On the other hand, if the intended timing is Stackelberg within each stage, with the short-run player observing (via $y_1$) the long-run player’s *current* action before choosing $a_2$, then a state-revealing $s_1^*$ makes her belief about the payoff-relevant state degenerate at $\theta_t$, and the current formulation using $\pi(\theta)$ and $B(s_1^*,F(\cdot\mid \theta))$ may be appropriate.

Because the paper does not spell out the stage timing and the mapping from $(\theta_t,\theta_{t-1})$ to the belief argument of $B(\cdot)$ in detail, it is hard to verify directly that Definition 4.5 is the unique correct expression for the Markov commitment payoff. It would be helpful to clarify explicitly which state the short-run player conditions on when forming beliefs, how that relates to the lifted state, and why the resulting bound reduces to the $\pi$-weighted average in (Definition 4.5) rather than an expression involving the joint distribution on $\tilde\Theta$.

---

### 5. Invalid sufficient condition for supermodularity

**Status**: [Pending]

**Quote**:
> Since $g\left(\theta_{t}, a_{1}, h_{t}\right)$ is supermodular in $\left(\theta_{t}, a_{1}\right)$ whenever $V_{\text {cont }}$ is increasing in $\theta_{t}$ for each $a_{1}$ (which holds when higher states have higher continuation values), the OT solution is unchanged.

**Feedback**:
The sentence
\[
\text{“Since } g(\theta_t,a_1,h_t)\text{ is supermodular in }(\theta_t,a_1)\text{ whenever }V_{\text{cont}}\text{ is increasing in }\theta_t\text{ for each }a_1\text{ …”}
\]
uses a condition that is too weak to guarantee supermodularity. Being increasing in $\theta_t$ for each fixed $a_1$ only ensures that $V_{\text{cont}}(\theta,a_1)$ is monotone in the state; it does not ensure increasing differences in $(\theta,a_1)$, which is the property equivalent to supermodularity in this finite setting.

Without additional structure (such as additive separability or an explicit increasing-differences assumption on $V_{\text{cont}}$), one can have $V_{\text{cont}}(\theta,a_1)$ increasing in $\theta$ for each $a_1$ but with *decreasing* differences across actions, so that $g$ is submodular, not supermodular. In that case, adding $g$ to $u_1$ can in principle change the optimal transport solution.

Since this point is used in Remark 5.4 to argue that, in the supermodular case, the continuation-value perturbation “is absorbed by the supermodular structure and the OT solution remains unchanged,” it would be helpful either to (i) strengthen the stated condition to something like “$g$ (or $V_{\text{cont}}$) has increasing differences in $(\theta_t,a_1)$,” or (ii) explicitly justify, for the specific supermodular applications considered (e.g., the deterrence game), why $g$ indeed satisfies the required supermodularity property. As written, the implication from mere monotonicity in $\theta_t$ to supermodularity is not valid in general.

---

### 6. Contradiction in one-shot deviation argument

**Status**: [Pending]

**Quote**:
> The strategy space is now Markov strategies on $\tilde{\Theta}$ instead of static strategies on $Y_0$, but the one-shot deviation argument is identical. ... In the Markov case, the continuation value $V_{\text {cont }}\left(\theta_{t}, a_{1}, h_{t}\right)$ depends on $\theta_{t}$ through the transition kernel $F$. ... and adding this $\theta_{t^{-}}$ dependent term can in principle change the OT solution.

**Feedback**:
The sentence “The strategy space is now Markov strategies on $\tilde{\Theta}$ instead of static strategies on $Y_0$, but the one-shot deviation argument is identical” sits uncomfortably next to the subsequent observation that in the Markov case the one-shot deviation objective becomes
\[
w(\tilde\theta,a_1) = u_1(\tilde\theta,a_1,\alpha_2) + \delta g(\theta_t,a_1,h_t),
\]
with $g$ depending on $\theta_t$ via the transition kernel, so that adding this term “can in principle change the OT solution.”

The first sentence can be read as claiming that the full one-shot deviation analysis carries over unchanged from the i.i.d. to the Markov environment, whereas the following discussion correctly emphasizes that the continuation term alters the objective and may therefore alter which $s_1$ is optimal. This tension obscures the fact that two distinct issues are in play: (i) conditional on a per-period objective $w(\tilde\theta,a_1)$, the OT/cyclical-monotonicity argument used in Luo–Wolitzky’s Lemma 1 does have the same structure on $\tilde\Theta$; but (ii) in the Markov case, the relevant $w$ is no longer simply $u_1$, and confound‑defeating with respect to $u_1$ need not suffice.

It would help readers if you explicitly disentangled these points: clarify that the deviation argument in Lemma 5.3 is “identical” only conditional on a given objective $w$, and then state clearly which additional conditions (such as supermodularity with belief‑robustness, or a strengthened confound-defeating requirement, or the continuity argument in Remark 5.4) are needed to ensure that $s_1^*$ is indeed optimal for the Markov one-shot objective $w(\tilde\theta,a_1)$.

---

### 7. Conceptual error regarding filter stability and belief convergence

**Status**: [Pending]

**Quote**:
> If the commitment type plays $s_{1}^{\varepsilon}(\theta)=(1-\varepsilon) s_{1}^{*}(\theta)+\varepsilon \cdot$ uniform for small $\varepsilon>0$, the strategy is no longer state-revealing, and filter stability (SA4) suggests that beliefs may converge to the stationary distribution. Whether $V_{\text {Markov }}\left(s_{1}^{\varepsilon}\right) \rightarrow V\left(s_{1}^{*}\right)$ as $\varepsilon \rightarrow 0$, uniformly in other parameters, would provide a "smoothing" route to the full bound that circumvents the belief-robustness requirement.

**Feedback**:
The suggestion that $\varepsilon$-perturbed strategies might cause beliefs to converge to the stationary distribution $\pi$ appears to rest on a misunderstanding of filter stability. Filter stability (as correctly defined in Appendix A.2) implies that the influence of the *initial prior* decays over time, not that the posterior converges to the unconditional mean of the state process. For small $\varepsilon$, the signals remain highly informative, causing the posterior belief $\mu_t$ to track the state $\theta_t$ rather than settling at $\pi$. Consequently, the SR best responses will likely still toggle state-by-state, and the payoff will remain close to $V_{\text{Markov}}$, not the i.i.d. bound $V(s_1^*)$.

---

### 8. Arithmetic error in belief-robust condition

**Status**: [Pending]

**Quote**:
> $\mu^{*}=0.60<\beta=0.5$

**Feedback**:
Statement $\mu^{*}=0.60<\beta=0.5$ in Section 7.4 (and similarly in Remark 3.4) is arithmetically inconsistent: with the baseline calibration $(\alpha,\beta)=(0.3,0.5)$ we have \$0.60>0.5$, and by Proposition 3.3 the game is then not belief-robust. The surrounding discussion makes it clear that the intent in “Version 1: Belief-Robust” is to consider a calibration with $\mu^*$ lying below the entire interval $[\beta,1-\alpha]$, so that SR always cooperates and belief-robustness holds. To avoid confusion, it would be helpful either to choose numerically consistent parameters (e.g. $\mu^*<0.5$ given $\alpha=0.3,\beta=0.5$) or to keep the condition in generic form (“$\mu^*<\beta$”) without plugging in the baseline value $\beta=0.5$.

---

### 9. Arithmetic error and variable confusion

**Status**: [Pending]

**Quote**:
> For the deterrence game with $\mu^{*}=0.60$, the cost equals \$0.777-0.628=0.094$, representing $23.7 \%$ of the i.i.d. payoff.

**Feedback**:
The numerical description of the “cost of persistence” in this sentence appears internally inconsistent. The difference \$0.777-0.628$ equals $0.149$, not $0.094$. Moreover, the 23.7% figure corresponds to \$0.149/0.628$ (the overestimation relative to the Markov payoff), whereas the text describes it as a percentage “of the i.i.d. payoff,” which would give about 19.2%. Since 0.094 is exactly the belief-gap statistic derived earlier from Equation (7), it seems that number was inadvertently substituted for the payoff gap here. It would help to correct the arithmetic and to state explicitly whether the “cost of persistence” is being measured in absolute payoff units ($V - V_{\text{Markov}}$) or as a percentage, and relative to which benchmark (Markov vs. i.i.d.).

---

### 10. Missing content in Appendix A.3

**Status**: [Pending]

**Quote**:
> A. 3 Monte Carlo Verification ..... 34
B Computational Framework ..... 34

**Feedback**:
In Appendix A, the subsection "A.3 Monte Carlo Verification" appears to be empty, consisting only of a header. The main text (Section 5.4) explicitly relies on this appendix to verify the KL counting bound. Please include the simulation details and results or integrate them into Appendix B.

---

### 11. Incorrect inference from filter stability

**Status**: [Pending]

**Quote**:
> If the commitment type plays $s_{1}^{\varepsilon}(\theta)=(1-\varepsilon) s_{1}^{*}(\theta)+\varepsilon \cdot$ uniform for small $\varepsilon>0$, the strategy is no longer state-revealing, and filter stability (SA4) suggests that beliefs may converge to the stationary distribution.

**Feedback**:
In the open-questions paragraph on $\varepsilon$-perturbed strategies in Section 10.2, the sentence “filter stability (SA4) suggests that beliefs may converge to the stationary distribution” seems to conflate two distinct notions. The filter stability result in Appendix A ensures exponential forgetting of the *initial prior* for the posterior process, but it does not by itself imply that the posterior $\mu_t$ converges to the unconditional stationary distribution $\pi$ of the Markov chain. For small $\varepsilon$, the signals under $s_1^\varepsilon$ remain very informative about $\theta_t$, so the belief process will typically continue to track the state and fluctuate rather than settle near $\pi$. It would be helpful to clarify exactly what kind of convergence you have in mind here (e.g., properties of the stationary distribution of beliefs as $\varepsilon$ varies) and to avoid suggesting that SA4 alone implies convergence of $\mu_t$ to $\pi$.

---

### 12. Contradiction between Figure 6 and its caption

**Status**: [Pending]

**Quote**:
> Figure 6: KL counting bound comparison: Markov vs. i.i.d. settings. Monte Carlo simulation with $N=500$ runs and $T=5000$ periods confirms the bound $\bar{T}\left(\eta, \mu_{0}\right)= -2 \log \mu_{0}\left(\omega_{s_{1}^{*}}\right) / \eta^{2}$ is valid and nearly identical in both settings.

**Feedback**:
The concern is that the text describes the empirical distributions of distinguishing-period counts as "nearly identical" across Markov and i.i.d. simulations, while Figure 6 shows sample means around 8.1 (i.i.d.) and 12.7 (Markov) and visibly shifted histograms. Although both processes generate very few distinguishing periods relative to the theoretical bound (921) and the horizon $T$, so the simulation still supports the analytic bound, the phrase "nearly identical" seems stronger than what the plotted data justify. It would be clearer to describe the simulations as showing that both processes yield similarly small counts (of the same order of magnitude and far below the bound), rather than implying empirical indistinguishability between the Markov and i.i.d. cases.

---

### 13. Confusion of reputation dynamics with state-belief dynamics

**Status**: [Pending]

**Quote**:
> the Nash correspondence $B\left(s_{1}^{*}\right)$ must be written as $B\left(s_{1}^{*}, \mu_{0}\left(h_{t}\right)\right)$—a dynamic, historydependent object. This renders the standard one-shot deviation argument inapplicable, since $\mu_{0}$ changes with each period's state revelation.

**Feedback**:
The description in this methodological paragraph of the “core issue” is potentially confusing and does not match the paper’s own notation. Earlier, $\mu_0$ is defined as the fixed prior over commitment types and posteriors are denoted $\mu_t(\cdot\mid h_t)$, while the state-belief driving the SR’s best response in the Markov setting is $F(\cdot\mid \theta_t)$ (or the corresponding filter over states). Writing the Nash correspondence as $B(s_1^*,\mu_0(h_t))$ and saying that the one-shot deviation argument fails “since $\mu_0$ changes with each period’s state revelation” therefore blurs the distinction between reputation over types and beliefs about states.

In the i.i.d. case the reputation $\mu_t$ already evolves with history and the original proof handles this. The genuinely new phenomenon in your Markov extension—as you describe correctly elsewhere—is that the *target* best-response correspondence becomes state-dependent, $B(s_1^*,F(\cdot\mid\theta_t))$, because the SR’s belief about $\theta_{t+1}$ differs across realized $\theta_t$. It would be helpful in this Phase 2 discussion to align the notation with the rest of the paper, explicitly refer to the state-belief, and clarify that it is this state-contingency of $B(\cdot)$, not the mere fact that beliefs change over time, that invalidates the original argument.

---

### 14. Ambiguous definition of best-response set in Lemma 5.8

**Status**: [Pending]

**Quote**:
> Lemma 5.8 (Extension of Lemma 4). There exist strictly positive functions $\zeta(\eta)$ and $\xi(\eta)$... such that if $h_{t} \in H_{t}^{\eta}$ and $\mu_{t}\left(\cdot \mid h_{t}\right) \in M_{\zeta(\eta)}$, then:
$$
\left(\sigma_{0}^{*}\left(h_{t}\right), \sigma_{2}^{*}\left(h_{t}\right)\right) \in \hat{B}_{\xi(\eta)}\left(s_{1}^{*}\right)
$$
Proof. This is a per-period argument combining Lemma 5.3 with the definition of $M_{\zeta}$ and the confirmed best response structure. ... The argument is identical to that of Luo \& Wolitzky (2024).

**Feedback**:
Statement $\hat{B}_{\xi(\eta)}(s_1^*)$ appears in Lemma 5.8 without being redefined in the Markov extension, and the proof is described as “identical” to Luo–Wolitzky’s. For readers who are not actively holding the original paper’s notation in mind, it may not be immediately clear that $\hat{B}$ here still refers to the static, type-based confirmed best-response set, whereas the state-dependent correspondences $B(s_1^*,F(\cdot\mid\theta))$ only enter later in the payoff step.

At first I found this a bit confusing, because the surrounding discussion emphasizes that in the Markov case the short-run player’s best response depends on the revealed state, and Section 5.7 then works with $B(s_1^*,F(\cdot\mid\theta_t))$ to define $V_{\text{Markov}}(s_1^*)$. Then I understood that Lemma 5.8 is only about static confirmed best responses to $s_1^*$ (as in Luo–Wolitzky), while the state-contingent structure is incorporated afterwards in the payoff bound.

It might still improve readability to (i) briefly recall how $\hat{B}(s_1^*)$ is defined in this extended setting, and (ii) make explicit in Section 5.7 how the fact that $(\sigma_0^*(h_t),\sigma_2^*(h_t))\in\hat{B}_{\xi(\eta)}(s_1^*)$ in good periods underpins the lower bounds formulated in terms of the state-contingent sets $B(s_1^*,F(\cdot\mid\theta_t))$.

---

### 15. Incorrect claim about confound-defeating conditions

**Status**: [Pending]

**Quote**:
> Persistence thus strengthens identification, making confound-defeating conditions easier to satisfy in the supermodular case.

**Feedback**:
This sentence in Section 8.6 could be read as asserting that the formal confound-defeating condition itself becomes weaker under Markov persistence. But in Section 6, for payoffs depending only on $\theta_t$, you show that the supermodularity/monotonicity characterization of confound-defeating strategies is unchanged relative to the i.i.d. case. In light of that result, it is unclear in what precise sense persistence makes the confound-defeating conditions “easier to satisfy,” beyond providing more informative temporal patterns in the observed actions. It would be helpful to clarify whether you mean that persistence improves identification or empirical verifiability of the confound-defeating property (as suggested by the earlier “easier to verify” wording in Section 7.6), rather than changing the mathematical condition itself.

---

### 16. Ambiguity in "Not Behaviorally Confounded" application

**Status**: [Pending]

**Quote**:
> Since $s_{1}^{*}$ is not behaviorally confounded, any type with the same asymptotic signal distribution must be $s_{1}^{*}$ itself, hence $\mu_{\infty}\left(\left\{\omega^{R}, \omega_{s_{1}^{*}}\right\} \mid h\right)=1$.

**Feedback**:
Statement (Part A of Lemma 5.7) that “Since $s_1^*$ is not behaviorally confounded, any type with the same asymptotic signal distribution must be $s_1^*$ itself” initially reads a bit quickly, because the “not behaviorally confounded” condition in Definition 4.2 is formulated in terms of the stationary distribution $\tilde\rho$, whereas the preceding discussion has been about convergence of the conditional per-period signal laws $p_{Y_1}(\cdot\mid h_t)$ along histories.

After thinking it through, one can see that under ergodicity and filter stability for each Markov strategy $s_1$, the conditional one-period signal distribution $p_{Y_1}(\sigma_0^*,s_1\mid h_t)$ converges (for $Q$-typical histories) to the stationary one-period marginal $p(\alpha_0,s_1,\alpha_2)$ associated with $\tilde\rho$. Together with the KL counting bound, this implies that any type with positive limiting posterior mass must induce the same stationary signal distribution as $s_1^*$, which is exactly what Definition 4.2 rules out unless $s_1'=s_1^*$.

Given this, the inference in the quoted sentence is correct, but it relies on the implicit identification between the asymptotic conditional signal distributions and the stationary $p(\alpha_0,s_1,\alpha_2)$. It might help some readers if you added a brief remark making that link explicit—i.e., that filter stability plus ergodicity ensure $p_{Y_1}(\cdot\mid h_t)$ converges to the stationary one-period law under each type—before invoking the “not behaviorally confounded” condition.

---

### 17. Confusing Motivation for Lifted State

**Status**: [Pending]

**Quote**:
> We employ a lifted state construction $\tilde{\theta}_{t}=\left(\theta_{t}, \theta_{t-1}\right)$, which provides a stationary distribution $\tilde{\rho}$ on the expanded space and allows the optimal transport framework to apply directly.

**Feedback**:
At first the phrase “which provides a stationary distribution $\tilde{\rho}$ on the expanded space and allows the optimal transport framework to apply directly” in Section 1.1 made me think that the lifting was being justified as if the original chain lacked a stationary distribution. Then I understood from Assumption 2.1, Proposition 2.5, and Remark 2.7 that $\theta_t$ already has a stationary distribution $\pi$, and the real role of the lifting is to define a “type space” $\tilde\Theta=\Theta\times\Theta$ with marginal $\tilde\rho$ that plays the role of the exogenous type distribution in the Luo–Wolitzky optimal transport formulation and accommodates transition‑dependent Markov strategies.

Given this, the current wording in the introduction is not wrong, but it is a bit compressed and could be misread as suggesting that stationarity itself only appears after lifting. It might improve clarity to phrase the motivation in Section 1.1 in terms of constructing a suitable lifted type space for Markov private information (with known stationary marginal $\tilde\rho$), rather than as “providing” stationarity per se.

---

### 18. Failure of strict supermodularity on lifted space

**Status**: [Pending]

**Quote**:
> If $u_{1}\left(\tilde{\theta}, a_{1}, \alpha_{2}\right)=u_{1}\left(\theta_{t}, a_{1}, \alpha_{2}\right)$, then $u_{1}$ is supermodular in ( $\tilde{\theta}, a_{1}$ ) if and only if it is supermodular in $\left(\theta_{t}, a_{1}\right)$... Computational evidence confirms this: for $\theta_{t}$-dependent payoffs, 4 out of 24 orderings of the lifted space $\tilde{\Theta}$ preserve supermodularity

**Feedback**:
At first sight, the discussion in Section 6.2 might suggest a tension with the strict supermodularity assumption used in Proposition 6.1, because $u_1(\tilde{\theta},a_1,\alpha_2)=u_1(\theta_t,a_1,\alpha_2)$ is constant in the second coordinate of $\tilde{\theta}$.

However, on closer reading you are explicitly ordering $\tilde{\Theta}$ by the first coordinate only:
\[
(\theta_t,\theta_{t-1}) \succeq (\theta_t',\theta_{t-1}') \iff \theta_t \succeq \theta_t'.
\]
With this order, states that differ only in $\theta_{t-1}$ are not strictly ordered, so the strict increasing-differences condition is never applied to such pairs. Strict supermodularity in $(\tilde{\theta},a_1)$ is therefore equivalent to strict supermodularity in $(\theta_t,a_1)$, as long as the underlying payoff has strictly increasing differences in $(\theta_t,a_1)$.

Given that Proposition 6.1 invokes strict supermodularity to appeal to the uniqueness result in optimal transport, it might nonetheless be helpful to state explicitly in Section 6.2 that, for $\theta_t$-only payoffs, strict supermodularity (in the sense used in Proposition 6.1) on $\tilde{\Theta}\times A_1$ is preserved under this first-coordinate order and coincides with the usual condition on $(\theta_t,a_1)$.

---

### 19. Imprecise terminology regarding filter stability

**Status**: [Pending]

**Quote**:
> This ensures that the initial condition of the Markov chain is "forgotten" exponentially fast, so the per-period signal distribution converges to a limit determined by the observation process alone

**Feedback**:
Statement "This ensures that the initial condition of the Markov chain is 'forgotten' exponentially fast" initially made me think the text was referring to mixing of the hidden chain (forgetting $\theta_0$), whereas Proposition A.2 is formally about the filter’s dependence on the initial prior $\pi_0$. The intended meaning can be inferred from the notation—"initial condition" as initial distribution—and the overall argument is correct, but it would be clearer to say explicitly that the stability result concerns forgetting of the initial prior for the filter, with ergodicity of $(\theta_t)$ providing the usual mixing of the underlying chain.

---

### 20. Missing discussion of Stackelberg well-definedness

**Status**: [Pending]

**Quote**:
> The partially accepted point concerns Stackelberg well-definedness for persuasion games, which is acknowledged as an open question in Section 10.

**Feedback**:
The Phase 5 description in Section 9.5 notes that the partially accepted critique on “Stackelberg well-definedness for persuasion games” is “acknowledged as an open question in Section 10.” However, Section 10.2 (“Open Questions”) as currently written does not explicitly mention Stackelberg well-definedness or persuasion games among the listed topics. It would be helpful either to add a short, explicit open question on this point in Section 10.2 or to adjust the wording in 9.5 so that the cross-reference accurately reflects what appears in Section 10.

---

### 21. Inconsistent payoffs and Stackelberg strategy

**Status**: [Pending]

**Quote**:
> Payoffs conditional on $a_2=D$ (or more generally against SR strategy $\alpha_2$) are:

$$
u_{1}(G, A)=1, \quad u_{1}(G, F)=x, \quad u_{1}(B, A)=y, \quad u_{1}(B, F)=0,
$$

with $x, y \in(0,1)$. ... The Stackelberg strategy is $s_1^{*}(G)=A, s_1^{*}(B)=F$

**Feedback**:
I initially had trouble reconciling the line “Payoffs conditional on $a_2 = D$ are $u_1(G,A)=1$, $u_1(G,F)=x$, $u_1(B,A)=y$, $u_1(B,F)=0$ with $x,y\in(0,1)$” with the statement that the Stackelberg strategy is $s_1^*(G)=A$, $s_1^*(B)=F$, because, looking only at these four numbers, $A$ appears to dominate $F$ in state $B$.

However, this is only the $D$-row of the payoff matrix, and the full deterrence specification (including the $C$-row) is imported from Luo–Wolitzky. Once one remembers that $u_1(B,F,C)$ and $u_1(B,A,C)$ are not specified here and can make $F$ optimal in $B$ under the Stackelberg problem, there is no actual inconsistency. The subsequent use of $u_1(B,F)=0$ in the commitment payoff calculation in 7.6 is naturally interpreted as using the worst-case (defection) payoff in the bad state, not as a claim about the payoff when $F$ induces cooperation.

Given that you assume familiarity with the deterrence game in Luo–Wolitzky, the abbreviated presentation is defensible. Still, you might consider adding a brief remark in Section 7.1 explicitly noting that only the $D$-row is being displayed and that, in the full $(g,l)$-matrix from Luo–Wolitzky, the missing $C$-payoffs are such that $s_1^*(G)=A$, $s_1^*(B)=F$ is indeed the Stackelberg strategy. This would preempt the kind of momentary confusion that can arise if a reader focuses only on the listed $D$-payoffs.

---
