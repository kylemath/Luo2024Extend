# Marginal Reputation

**Daniel Luo and Alexander Wolitzky**

**MIT∗**

**December 17, 2024**

**Abstract**

Stackelberg payoff if distinct commitment types are statistically distinguishable and the Stackelberg strategy is confound-defeating. This property holds if and only if the Stackelberg strategy is the unique solution to an optimal transport problem. If the long-run player’s payoff is supermodular in one-dimensional signals and actions, she secures the Stackelberg payoff if and only if the Stackelberg strategy is monotone. An application of our results provides a reputational foundation for a class of Bayesian persuasion solutions when the sender has a small lying cost. Our results extend to the case where distinct commitment types may be indistinguishable but the Stackelberg type is salient under the prior. Keywords. Reputation, repeated games, confound-defeating, optimal transport, cyclical monotonicity, signaling, Bayesian persuasion. JEL Codes. C73, D83 ∗For helpful comments, we thank Sandeep Baliga, Ian Ball, V. Bhaskar, Drew Fudenberg, Eric Gao, Navin Kartik, Anton Kolotilin, Stephen Morris, David Pearce, Harry Pei, and Tom Wiseman.


1 Introduction This paper considers reputation formation in settings where one desires a reputation not only for taking certain actions, but for acting in the right circumstances. Our main applications are to deterrence, trust, and communication games, where the importance of establishing a reputation for conditional action has long been accepted in the informal liter-


$$
ature. For example, Schelling (1966) writes,
$$

“any coercive threat requires corresponding assurances; the object of a threat is to give somebody a choice. To say, “One more step and I shoot,” can be a deterrent threat only if accompanied by the implicit assurance, “And if you stop I won’t.” Giving notice of unconditional intent to shoot gives him no choice.” Similarly, when an informed sender asks a receiver to take an action that the sender prefers, the request is persuasive only if the receiver believes that the sender tends to make it only when compliance is in the receiver’s interest. To study reputation formation in these settings, we consider a model where a long-run player facing a sequence of short-run opponents repeatedly observes private signals and takes actions. For example, in the deterrence context, the signal is whether the long-run player detects an attack by a short-run player who moves first, and the action is whether she fights back. In the communication context, the long-run player is the first-mover, the signal is a payoff-relevant state variable, and the action is a signal or message to a short-run player who moves second. The long-run player is either rational or is one of a number of possible commitment types that play a fixed mapping from signals to actions in each period. The set of possible commitment types includes the Stackelberg type that plays the long-run player’s most-preferred commitment strategy. In this setup, if short-run players observe the history of the long-run player’s past actions and signals, standard results imply a patient long-run player is assured at least her Stack- elberg (best commitment) payoff in every Nash equilibrium (Fudenberg and Levine 1989; 1992). We instead consider the case where the long-run player’s actions are observed, but her signals are not. In the deterrence context, this says that potential attackers know when the long-run player has fought in the past, but not whether this fighting was a response to detected attacks. In the communication context, it says that receivers observe the history of messages sent by the long-run player, but not the history of states. Existing results say little about the outcomes of these games. The key issue is that the long run player’s strategy—how she maps signals to actions—is not identified by the observed 1


marginal distribution over her actions. This implies that existing payoff bounds for reputation games with imperfect monitoring (Fudenberg and Levine, 1992; Gossner, 2011) are extremely loose and often trivial in our setting. For example, suppose that in the deterrence context the long-run player follows her (pure) Stackelberg strategy of fighting if and only if she detects an attack. This strategy results in the long-run player fighting a certain fraction of the time, say 50%. However, after seeing her fight half the time, potential attackers need not come to believe that she is playing the Stackelberg strategy—they might instead believe that she is playing a different strategy with the same marginal over actions, such as fighting half the time independent of her signal. Which inference potential attackers draw is critical for the long-run player, as they will be deterred if they believe she is playing the Stackelberg strategy of fighting when she detects an attack, but not if they believe she is randomly fighting half the time. As existing results do not restrict the short-run players’ inferences in this situation, they make no non-trivial predictions about the long-run player’s payoff. Formally, in this example attacking and not attacking are both “0-confirmed best responses” to the Stackelberg strategy, so Fudenberg and Levine’s (1992) lower bound is vacuous. Our main result provides conditions for a patient long-run player to secure her Stackel- berg payoff when only the marginal over actions is identified. The key sufficient condition is that the Stackelberg strategy is confound-defeating: against any 0-confirmed best response, the Stackelberg strategy is uniquely optimal among strategies that induce the same marginal over actions. Intuitively, if the Stackelberg strategy is confound-defeating then the rational long-run player never plays a different strategy that induces the same marginal in any Nash equilibrium. Therefore, establishing a reputation for playing the “Stackelberg marginal” suf- fices to establish a reputation for playing the Stackelberg strategy. A strategy is confound-defeating if and only if the induced joint distribution over the long-run player’s signal and action is uniquely optimal among all distributions with the same marginals: that is, if and only if it is the unique solution to the optimal transport problem of maximizing the long-run player’s payoff subject to given marginals over her signal and action. Adapting standard optimal transport results, we show that this holds if and only if the support of the induced joint distribution satisfies a strict version of cyclical monotonicity (Rochet, 1987). We also use cyclical monotonicity to provide a converse to our main result: if the long-run player is rational with high probability, her payoff in any equilibrium cannot exceed that from some cyclically monotone strategy. The cyclical monotonicity characterization makes confound-defeatingness easy to check in many games. In particular, if the long-run player’s payoff is supermodular in one-dimensional 2


signals and actions, a strategy is confound-defeating if and only if every selection from its support is monotone. Applied to the deterrence game, this says that the long-run player can secure her Stackelberg payoff if fighting is relatively more appealing when an attack is detected. Conversely, if the long-run player is rational with high probability, her payoff cannot exceed that from a monotone strategy in any Nash equilibrium. For example, in the deterrence game, the long-run player obtains close to her minmax payoff in every Nash equilibrium if fighting is more appealing when an attack is not detected. Our results have strong implications for repeated communication games. An immediate implication is that, in repeated signaling games where the sender’s payoff is additively sepa- rable in the receiver’s action and supermodular in her own type and action, a patient sender can secure her best commitment payoff from any monotone signaling strategy.1 We then consider repeated cheap talk games with state-independent sender preferences (which coin- cide with Bayesian persuasion when the sender has commitment power). Here, we show that perturbing the sender’s payoff by adding a small submodular “lying cost” yields a reputa- tional foundation for any communication mechanism that is monotone with respect to some order on states and receiver actions. While not fully general, this class includes all partitions


$$
(deterministic communication mechanisms) and all linear partitions with randomization at
$$

the boundaries. We are thus able to provide a reputational foundation for a general class of communication mechanisms, even when the history of realized states is unobserved. Our exposition assumes that distinct commitment types in the support of the short-run players’ prior are statistically distinguishable. Without this assumption, non-Stackelberg play by commitment types with the same marginal as the Stackelberg strategy can hinder repu- tation formation. Nonetheless, we show in Appendix A that our results extend without this assumption, so long as the Stackelberg type is sufficiently salient under the prior. Roughly, this condition says that the Stackelberg type has sufficiently high prior weight relative to other commitment types that induce the same marginal but different best responses. In the deterrence context, this says that short-run players believe that, conditional on the long-run player being irrational, she is more much likely to play the strategy “fight if and only if an attack is detected” than the strategy “fight half the time independent of the signal.” 1The results of Fudenberg and Levine (1992) imply the sender can secure her Stackelberg payoff in repeated signaling games where actions and states are observed at the end of each period. Our results imply the same conclusion holds when only actions are observed, if the Stackelberg strategy is monotone and the sender’s payoff is additively separable in the receiver’s action and supermodular in her own type and action. 3


Related Literature. We contribute to the literature on reputation formation with im- perfect monitoring, introduced by Fudenberg and Levine (1992). They show that a patient long-run player can ensure her commitment payoff against the least favorable of her oppo- nent’s 0-confirmed best responses. In our partially identified setting, the set of 0-confirmed best responses is typically large, so this payoff lower bound is weak and often vacuous. Goss- ner (2011) gives a different proof—which we build on—of a similar lower bound, which is also too weak in our setting for the same reason. Fudenberg and Levine and Gossner also give upper bounds on a patient long-run player’s payoffs, which Ely and Valimaki (2003) show is much too loose in a class of games where short-run players have outside options. In contrast, we show that their lower bounds are much too loose in a class of games where the long-run player observes private signals and the Stackelberg strategy is confound-defeating.2 Pei (2020) studies a reputation model with interdependent values, where a possibly com- mitted long-run player privately observes a perfectly persistent, payoff-relevant state. Our model instead covers (as a special case) the case where the state is i.i.d.: see Section 2.2. In both papers, supermodularity-type conditions are important for securing the Stackelberg payoff, but the precise conditions and arguments are very different.3 Other papers in the reputation literature where super/submodularity conditions play key roles in deriving payoff bounds include Liu (2011), Liu and Skrzypacz (2014), and Pei (2024). We also relate to a diverse literature on games and mechanisms where strategies are par- tially identified, so certain deviations are undetectable. The connection between incentive compatibility and optimal transport in such settings dates to Rochet (1987); Rahman (2024) gives an alternative interpretation and proof. Applications include quota mechanisms (Jack- son and Sonnenschein, 2007; Matsushima, Miyazaki, and Yagi, 2010; Escobar and Toikka, 2013; Frankel, 2014; Ball and Kattwinkel, 2024), multidimensional or repeated cheap talk (Chakraborty and Harbaugh, 2010; Renault, Solan, and Vieille, 2013; Margaria and Smolin, 2018; Meng, 2021), and repeated random matching games (Takahashi, 2010; Heller and Mohlin, 2018; Clark, Fudenberg, and Wolitzky, 2021). A particularly related paper is Lin and Liu (2024), who study optimal information disclosure when only the marginal distribu- tion over signals is observed. In their setting, a joint distribution over states and receiver 2Ely, Fudenberg, and Levine (2008) add “good commitment types” to Ely and Valimaki (2003) and show that this does not restore the long-run player’s commimtent payoff. The reason for the difference from our results is that we assume that the long-run player’s action is always identified, whereas in Ely and Valimaki (2003) and Ely, Fudenberg, and Levine (2008) it is not identified when the short-run player exits. 3For example, Pei’s Stackelberg payoff theorem requires binary actions for the short-run player and a condition on the prior, while we require no such conditions. 4


actions is implementable if it maximizes the sender’s payoff over all joint distributions with the same marginals. In contrast, our confound-defeating property requires the joint distri- bution over states and sender actions to uniquely maximize the sender’s payoff over all joint distributions with the same marginals, for any receiver best response. The two conditions are thus related, but involve different objects (distributions over states and receiver actions vs. sender actions) and come from different strategic considerations (static information disclo- sure subject to a “credibility” constraint vs. long-run reputation formation). They also apply to different classes of communication games: Lin and Liu’s “credibility” constraint has bite only if the sender’s utility is state-dependent, while our commitment payoff theorem applies only if the sender’s utility is state-independent. We are also not the first to discuss reputational foundations for the Bayesian persuasion commitment assumption. The commitment assumption has been controversial ever since its introduction by Rayo and Segal (2010) and Kamenica and Gentzkow (2011). Rayo and Segal (2010) suggested reputation effects as a possible foundation. Mathevet, Pearce, and Stac- chetti (2024) observe that reputation effects provide a valid foundation for the commitment payoff when a long-run sender faces a sequence of short-run receivers who observe the history of messages and states. In this setting, they study whether the sender’s behavior likewise coincides with the commitment solution. We instead ask when reputation effects yield the commitment payoff when receivers observe past messages but not states. Farther afield, Pei (2023) and Best and Quigley (2024) show that the commitment payoff arises as one of many equilibrium payoffs in repeated communication game with lying costs and coarse information on histories, respectively; Kuvalekar, Lipnowski, and Ramos (2022) study repeated sender- receiver games with two long-run players and unobserved past states, without commitment types; and Fudenberg, Gao, and Pei (2022) provide a foundation for the commitment payoff in a model where the long-run player sends messages before taking actions and can develop a reputation for “honesty” about the action they are about to take. Organization. Section 2 analyzes the deterrence game discussed above, as well as re- peated trust and signaling games. Section 3 develops the general model. Section 4 presents the confound-defeating property and our main result: the long-run player can secure her Stackelberg payoff if the Stackelberg strategy is confound-defeating. Section 5 characterizes confound-defeatingness via cyclical monotonicity, gives a converse to the main result, and applies our results to one-dimensional supermodular games. Section 6 considers communica- tion games. Section 7 summarizes the paper and discusses some extensions and directions for 5


future work. Appendix A extends our results to allow indistinguishable commitment types by introducing our salience notion. Appendix B contains omitted proofs. 2 Motivating Examples We begin with three examples: a deterrence game, a trust (or “product choice”) game, and a signaling game. These examples illustrate our main results in simple settings. Among other simplifications, we assume here that the long-run player has a single commitment type, which plays a pure strategy. The general analysis relaxes these assumptions. 2.1 Deterrence


$$
We start with a deterrence game.4 A long-run player with discount factor \delta faces a
$$

sequence of short-run opponents. Each period, the short-run player first chooses whether to Cooperate (C) or Defect (D). The long-run player then observes a private signal, c or


$$
d, generated with conditional probability Pr(c|C) = Pr(d|D) = p \in(0, 1), before choosing
$$

whether to Accommodate (A) or Fight (F). The short-run player observes the history of the long-run player’s past actions, but not her signals. The short-run player’s payoff is specified as a function of both players’ actions while the long-run player’s payoff is specified as a function of her action and private signal as follows.5


## C


## D


## A

1 1 + g


## F

−l 0 Short-Run Player Payoff c d


## A

1 y


## F

x 0 Long-Run Player Payoff


$$
Assume that g, l > 0 and x, y \in(0, 1), so that D is dominant for the short-run player and
$$

A is dominant for the long-run player. Assume also that p is sufficiently large that the short- run player strictly prefers to take C if the long-run player plays the “deterrence” strategy, 4The stage game in this subsection is an example of an inspection game (Avenhaus, von Stengel, and Zamir (2002)). Acemoglu and Wolitzky (2024) survey deterrence and related games in economics and political science, emphasizing the role of private signals. 5An interpretation of the dependence of the long-run player’s payoff on her signal rather than the short- run player’s action is that each period’s short-run player is “crazy” with probability 2(1 −p), independently across periods, in which case she mixed 50-50 between her actions, and this is the only source of noise. In this case, the long-run player’s “signal” is just the short-run player’s action, accounting for the crazy types. 6


(A after c; F after d), which we denote as (A, F); and that the long-run player would rather play (A, F) against C than play (A, A) against D, so that (A, F) is the long-run player’s pure Stackelberg strategy.6 Finally, assume that the long-run player is committed to (A, F) with probability µ0 and is rational otherwise.


$$
What can be said about the equilibria of this game when the discount factor \delta is close
$$

to 1? A first observation is that, in Fudenberg and Levine’s (1992) terminology, both C and D are “0-confirmed best responses” to the Stackelberg strategy (A, F). (We review this definition in Section 3.) For example, if the short-run player takes D, the long-run player ends up fighting with probability p when she plays (A, F), but also when she fights with probability p after each signal. Since D is a best response to the latter strategy, it is also a


$$
0-confirmed best response to (A, F).
$$

The results of Fudenberg and Levine (1992) (Theorem 3.1) and Gossner (2011) (Corollary


$$
1) state that, as \delta \to1, the long-run player’s payoff in any Nash equilibrium is at least her
$$

payoff from playing the Stackelberg strategy against the least favorable 0-confirmed best response. (See Theorem 0 in Section 3.2.) Since D is a 0-confirmed best response to (A, F), these results say only that the long-run player’s payoff is above 1 −p. When noise is small, so that p is close to 1, this just says that the long-run player’s payoff is feasible.7 In contrast, we have the following result. Note that the long-run player’s pure Stackelberg payoff is p, while her minmax payoff is 1 −p + py.


$$
Proposition 1. Let U 1(\delta) and ¯U1(\delta) be the infimum and supremum of the long-run player’s
$$

payoff in any Nash equilibrium. The following hold:


$$
(1) If x + y < 1 then lim inf\delta\to1 U 1(\delta) \geqp for all µ0 > 0.
$$


$$
(2) If x + y > 1 then limµ0\to0 U 1(\delta) = 1 −p + py for all \delta < 1.
$$

That is, if x + y < 1, a patient long-run player is assured at least her Stackelberg payoff in any Nash equilibrium; while if x + y > 1, the long-run player obtains close to her minmax payoff whenever the prior commitment probability is small. In particular, when noise is small, the long-run player is assured her best feasible payoff in the first case and her minmax payoff in the second. To see why it matters whether x + y is below or above 1, note that the long-run player’s payoff is strictly supermodular in her signal and action in the first case (with the order


$$
6These two conditions holds iff p > max{ 1+g+l
$$

2+g+l, 1 2−y}. 7Fudenberg and Levine and Gossner also give payoff upper bounds in terms of the mixed Stackelberg action. Our general results similarly allow mixed commitment types. 7



$$
A \succF, c \succd) and is strictly submodular in the second. In the strictly supermodular case, F
$$

is relatively more appealing when d is observed. This implies that the Stackelberg strategy (A, F) strictly outperforms any other strategy that induces the same marginal over actions, and hence is “confound-defeating.” As we show in Theorem 1, this implies that establishing a reputation for playing the Stackelberg marginal over actions suffices to establish a reputation for playing the Stackelberg strategy, and hence secures the Stackelberg payoff. Conversely, in the strictly submodular case, F is relatively more appealing when c is observed. This implies that the rational long-run player always plays F with (weakly) higher probability when c is observed, and plays A with higher probability when d is observed. Such a strategy encourages the short-run player to take D rather than deterring him, so the short-run player must take D whenever he believes that the long-run player is rational with high probability. Finally, since beliefs are martingale, it follows that the short-run player usually takes D when the ex ante commitment probability is small.8 2.2 Trust Now suppose that the stage game is the following “trust game” (or “product choice


$$
game”) adapted from Pei (2020). There is a state \theta \in{G(ood), B(ad)}, drawn i.i.d. across
$$

periods with equal probability on each state. In each period, the long-run player observes


$$
\theta before taking an action a1 \in{H(igh) Effort, L(ow) Effort}. Simultaneously (and having
$$

observed the history of past actions, but not states), the short-run player takes an action


$$
a2 \in{T(rust), N(ot Trust)}. Payoffs in each state are given by the following matrices, with
$$

the long-run player’s payoff listed first in each entry.


## T


## N


## H

1, 2 −1, 0


## L

2, −1 0, 0


$$
Payoffs in State \theta = G
$$


## T


## N


## H

1 −w, −1 −1 −z, 0


## L

2, −1 0, 0


$$
Payoffs in State \theta = B
$$

Assume that w, z > −1, so that L is dominant for the long-run player, and the unique stage-game Nash equilibrium outcome is (L, N) in both states. Note that T is optimal for


$$
the short-run player only if he believes that, with high enough probability, both \theta = G and
$$


$$
a1 = H. For example, suppose that player 1 is the chef of a seafood restaurant, \theta is the
$$

quality of the day’s catch, and player 2 is a customer who wants to eat only fish that is 8The submodular case of Proposition 1 follows from Corollary 3 in Section 5.3. 8


both of high quality and carefully cooked. Note that the long-run player’s pure Stackelberg strategy is (H, L) (as this strategy lets the long-run player enjoy taking L in state B while inducing the short-run player to take T), and assume that she is committed to this strategy with probability µ0. Note also that the long-run player’s pure Stackelberg payoff is 3/2, while her minmax payoff is 0. Proposition 2. The following hold:


$$
(1) If min{w, z} > 0 then lim inf\delta\to1 U 1(\delta) \geq3/2 for all µ0 > 0.
$$


$$
(2) If max{w, z} < 0 then limµ0\to0 U 1(\delta) = 0 for all \delta < 1.
$$

While the timing of the deterrence and trust games are different (e.g., the short-run player moves first in the former and simultaneously with the long-run player in the latter), the logic of Proposition 2 is similar to that of Proposition 1. If min{w, z} > 0 then the


$$
long-run player’s payoff is strictly supermodular in (\theta, a1) for any a2, which we show lets
$$

her secure her Stackelberg payoff when she is patient. If instead max{w, z} < 0 then the


$$
long-run player’s payoff is strictly submodular in (\theta, a1) for any a2, which we show limits her
$$

to her minmax payoff when the prior commitment probability is small.9 2.3 Signaling


$$
Finally, suppose the stage game is a signaling game. The state \theta \in\Theta \subsetR is drawn
$$


$$
i.i.d. across periods. In each period, the long-run player observes \theta before taking an action
$$


$$
a1 \inA1 \subsetR. The short-run player observes the current action a1 (but not \theta) and the history
$$


$$
of past actions (but not past states) and then takes an action r \inR in response. Assume \Theta,
$$


$$
A1, and R are finite, the long-run player’s payoff is given by (1 −\lambda)v(r) −\lambdaw(a1, \theta) for some
$$


$$
functions v and w and some \lambda \in(0, 1), and w is strictly submodular. Thus, the long-run
$$


$$
player’s preferences over the short-run player’s action r are independent of the state \theta, and
$$


$$
the parameter \lambda measures the weight on the long-run player’s signaling cost w(a1, \theta) relative
$$

to her payoff from the short-run player’s action v(r). Recall that submodularity of w is a


$$
standard assumption in signaling theory: for example, in Spence (1973), w(a1, \theta) = a1/\theta.10
$$


$$
9If one of {w, z} is positive and the other negative, the long-run player’s payoff is supermodular in (\theta, a1)
$$


$$
for one a2 \in{T, N} and submodular for the other. Our results do not cover this case. We also note that
$$


$$
Proposition 2 is roughly consistent with Pei’s (2020) results for the case where \theta is perfectly persistent: Pei
$$

shows that the long-run player can fail to secure her Stackelberg payoff in the submodular product choice game, but does secure it in the supermodular case (under an additional condition on the prior).


$$
10Our analysis of signaling games remains valid for more general preferences of the form (1 −\lambda)v(a1, r) −
$$


$$
\lambdaw(a1, \theta). That is, v can depend on a1 as well as r.
$$

9



$$
A strategy for the long-run player is now a mapping s1 : \Theta \to\Delta(A1). Assume that the
$$

long-run player is committed to some strategy ˆs1 with probability µ0 > 0 and is rational otherwise. Let ˆv1 be the long-run player’s payoff when she takes ˆs1 and the short-run player takes his least favorable best response. Finally, say that a strategy s1 is monotone if any


$$
selection from supp(s1(\theta)) is monotone in \theta.
$$

Just as in the deterrence game, standard results say little here. In particular, they cannot imply that a patient long-run player benefits from signaling, because any best response to the “babbling” strategy that takes actions a1 with the same marginal as ˆs but does so


$$
independently of \theta is a 0-confirmed best response to ˆs. However, we have the following.
$$


$$
Proposition 3. If ˆs1 is monotone then lim inf\delta\to1 U 1(\delta) \geqˆv1.
$$

The logic is similar to the supermodular cases of Propositions 1 and 2: strict submodu- larity of w implies that the rational long-run player prefers ˆs1 to any strategy that induces the same marginal over actions, so establishing a reputation for the Stackelberg marginal suffices to establish a reputation for the Stackelberg strategy. In particular, if ˆs1 is the long-


$$
run player’s Stackelberg strategy for the limiting payoffs where \lambda = 0 (i.e., the Bayesian
$$

persuasion solution) and this strategy is monotone, then Proposition 3 implies that the long-


$$
run player secures a payoff only slightly below her Stackelberg payoff when \lambda is small. This
$$

result provides a foundation for the Bayesian persuasion solution when the sender’s payoff is state-independent and the persuasion solution is monotone. In Section 6, we strengthen this result by characterizing all communication mechanisms that are monotone with respect to some order on states and receiver actions. Finally, Corollary 3 in Section 5.3 implies a partial converse to Proposition 3: if all Bayesian persuasion solutions are non-monotone, then even the long-run player’s best equi-


$$
librium payoff is bounded away from her commitment payoff for all \lambda > 0. The logic is that
$$

strict submodularity of w implies the long-run player must play a monotone strategy in any equilibrium and thus cannot establish a reputation for playing a non-monotone strategy. 3 Model We consider repeated games where a possibly-committed long-run player faces a sequence of short-run opponents. To cover both applications where a short-run player moves first (like deterrence games) and those where a short-run player moves simultaneously with or after the long-run player (like trust or communication games), we consider repeated three-player 10


games, where one short-run player (player 0) moves first, and then the long-run player (player 1) and another short-run player (player 2) move simultaneously. In deterrence games, the second short-run player is absent. In trust games, the first short-run player is absent. In communication games, the first short-run player is Nature, and the second short-run player’s action is a mapping from the long-run player’s action to a set of possible responses. We first describe the stage game, followed by the repeated game. 3.1 The Stage Game


$$
There are three players, i \in{0, 1, 2}. Player 1 is the long-run player; players 0 and 2
$$

are short-run players. Each player i has a finite action set Ai with generic element ai. Each action ai generates a signal in a finite set Yi, with independent conditional probabilities


$$
\rho(·|ai) \in\Delta(Yi). The signals satisfy the following assumption.
$$

Assumption 1.


$$
(1) The signal y0 has a full support distribution: \rho(y0|a0) > 0 for all y0 \inY0, a0 \inA0.
$$


$$
(2) The signal y1 statistically identifies the long-run player’s action: the |A1| vectors \rho(·|a1)a1\inA1
$$

are linearly independent in R|Y0|. The stage game timing is as follows. (1) Player 0 takes an action a0. This generates a signal y0, drawn from \rho(·|a0), which is observed by player 1 only. (2) Players 1 and 2 simultaneously take actions a1 and a2. This generates signals y1 and


$$
y2, drawn independently from \rho(·|a1) and \rho(·|a2), respectively, and publicly observed
$$

by all players.


$$
Thus, stage game strategies for players 0 and 2 are simply mixed actions \alpha0 \in\Delta(A0)
$$


$$
and \alpha2 \in\Delta(A2), respectively, while a stage game strategy for player 1 is a function s1 :
$$


$$
Y0 \to\Delta(A1). Note that a strategy profile (\alpha0, s1, \alpha2) induces a joint distribution \gamma(\alpha0, s1) \in
$$


$$
\Delta(Y0 \times A1) (independent of \alpha2) over player 1’s private signal y0 and action a1 according to
$$


$$
\gamma(\alpha0, s1)[y0, a1] =
$$


## X


$$
a0\inA0
$$


$$
\alpha0(a0)\rho(y0|a0)s1(y0)[a1],
$$

11



$$
and it induces a joint distribution p(\alpha0, s1, \alpha2) \in\Delta(Y1 \times Y2) over the public signals y1 and
$$

y2 according to


$$
p(\alpha0, s1, \alpha2)[y1, y2] =
$$


## X


$$
a0\inA0
$$


## X


$$
y0\inY0
$$


## X


$$
a1\inA1
$$


## X


$$
a2\inA2
$$


$$
\alpha0(a0)\rho(y0|a0)s1(y0)[a1]\rho(y1|a1)\alpha2(a2)\rho(y2|a2).
$$

We emphasize a key point: while the public signals (y1, y2) identify player 1’s action a1 by


$$
Assumption 1, they do not identify her strategy s1 (whenever |Y0|\geq2), because y0 is player
$$


$$
1’s private information.
$$


$$
Throughout the paper, for any joint distribution \chi \in\Delta(X1 \times X2) over a product set
$$


$$
X1 \times X2, \piXi(\chi) denotes its marginal on Xi. With slight abuse of notation, we also denote
$$


$$
the marginal of \gamma(\alpha0, s1) over Y0 (which depends only on \alpha0) by \rho(\alpha0) = \piY0(\gamma(\alpha0, s1)), and
$$


$$
we denote its marginal over A1 by ϕ(\alpha0, s1) = \piA1(\gamma(\alpha0, s1)).
$$

The players’ payoff functions are given by u0 : A0\timesA1 \toR for player 0 and ui : Y0\timesA1\times


$$
A2 \toR for players i \in{1, 2}. Thus, player 0’s payoff depends on his own action and player
$$

1’s action, while the payoffs of players 1 and 2 depend on their actions and the signal y0. The assumption that player 0’s payoff does not depend on player 2’s action simplifies the analysis


$$
and is satisfied in our applications.11 Finally, we write ui(\alpha0, s1, \alpha2) for player i’s expected
$$


$$
payoff at stage-game strategy profile (\alpha0, s1, \alpha2), and we let u1 = mina0,s1,a2 u1(a0, s1, a2) and
$$


$$
¯u1 = maxa0,s1,a2 u1(a0, s1, a2).
$$

Deterrence games fit this framework by making A2 a singleton, which effectively drops player 2 from the model. Trust games fit by making A0 a singleton (i.e., making player 0


$$
Nature). Communication games fit by making A0 a singleton; viewing \rho(y0) as the prior
$$


$$
distribution of a payoff-relevant state y0; letting \rho(y1|a1) = 1({y1 = a1}) (so a1 is perfectly
$$

monitored); viewing a2 as a mapping from a1 to a finite set of responses R; and assuming


$$
that u1 and u2 depend on a2 only through the induced response a2(a1) \inR.
$$

We conclude this subsection by adapting some definitions from Fudenberg and Levine (1992). For any strategy s1, let B(s1) \subset\Delta(A0) \times \Delta(A2) be the set of short-run player


$$
strategies (\alpha0, \alpha2) satisfying
$$


$$
supp(\alpha0) \subsetargmax
$$


$$
a0\inA0
$$


$$
u0(a0, s1)
$$

and


$$
supp(\alpha2) \subsetargmax
$$


$$
a2\inA2
$$


$$
u2(\alpha0, s1, a2),
$$


$$
so that player 0 best responds to s1, and player 2 best responds to \alpha0 and s1. With this
$$

11However, none of our results requires this assumption, with the exception of Theorem 2 in Appendix A. 12


notation, the long-run player’s (lower) Stackelberg payoff is v∗


$$
1 =
$$


$$
sup
$$


$$
s1\in\Delta(A1)Y0
$$


$$
inf
$$


$$
(\alpha0,\alpha2)\inB(s1) u1(\alpha0, s1, \alpha2).
$$

We refer to a strategy that attains this supremum as a Stackelberg strategy. More generally, for any strategy s1, we denote the corresponding lower commitment payoff by


$$
V (s1) =
$$


$$
inf
$$


$$
(\alpha0,\alpha2)\inB(s1) u1(\alpha0, s1, \alpha2).12
$$

Finally, we employ the following definition13.


$$
Definition 1. For any long-run player strategy s1 and any \eta \geq0, a short-run player strategy
$$


$$
(\alpha0, \alpha2) \in\Delta(A0) \times \Delta(A2) is an \eta-confirmed best response to s1 if there exists s′
$$

1 such that


$$
(1) (\alpha0, \alpha2) \inB(s′
$$

1), and


$$
(2) ||p(\alpha0, s1, \alpha2) −p(\alpha0, s′
$$


$$
1, \alpha2)||\leq\eta.
$$

For any s′


$$
1 that satisfies these conditions, we say that it \eta-confirms (\alpha0, \alpha2) against s1.
$$

Let B\eta(s1) be the set of \eta-confirmed best responses to s1. Note that B1(s1) \supsetB\eta′(s1) \supset


$$
B\eta(s1) \supsetB(s1) for all \eta′ \geq\eta \geq0, where B0(s1) = B(s1) if s1 is identified (which, again, is
$$


$$
not the case in our model whenever |Y0|\geq2), and B1(s1) is the set of all short-run player
$$

strategies that best respond to some long-run player strategy. In addition, B\eta(s1) ↓B0(s1)


$$
as \eta \to0, by upper hemi-continuity of the short-run players’ best-response correspondences.
$$

Finally, for any strategy s1, we denote the lower commitment payoff when the short-run players take a 0-confirmed best response by


$$
V0(s1) =
$$


$$
inf
$$


$$
(\alpha0,\alpha2)\inB0(s1) u1(\alpha0, s1, \alpha2).
$$


$$
Note that V (s1) \geqV0(s1) for each s1, since B(s1) \subsetB0(s1).
$$

3.2 The Repeated Game The stage game is repeated in each period t = 0, 1, 2, . . . . Player 1 is a long-lived player


$$
with discount factor \delta \in(0, 1), while players 0 and 2 are short-lived and take myopic best
$$

12Recall that the lower (resp., upper) commitment payoff results from the least favorable (resp., most favorable) short-run best response. 13Here and throughout the paper, ||·|| denotes the sup norm. 13


replies after observing only the public history of signals. A period-t public history is denoted


$$
ht = (y1,t′, y2,t′)t−1
$$


$$
t′=0 \in(Y1 \times Y2)t. Let Ht be the set of period-t (public) histories, H = S
$$

t Ht


$$
the set of all finite histories, and H\infty= (Y1 \times Y2)\inftythe set of infinite histories. A repeated
$$


$$
game strategy \sigmai for player i maps public histories to stage game strategies: formally, \sigmai is a
$$


$$
function from H to \Delta(Ai) for i \in{0, 2}, and is a function from H to \Delta(A1)Y0 for i = 1.14
$$


$$
The long-run player’s type, denoted \omega \inΩ, is either rational (\omega = \omegaR) or is one of a
$$

countable number of commitment types indexed by a (potentially mixed) stage game strategy


$$
s1 \in(\Delta(A1))Y0, where type \omegas1 plays s1 in every period.15 The type \omega is drawn according to
$$


$$
a full-support prior µ0 \in\Delta(Ω) at the start of the game and is perfectly persistent. We study
$$


$$
U 1(\delta) and ¯U1(\delta), the infimum and supremum of the long-run player’s payoff in any Nash
$$


$$
equilibrium (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2) of this incomplete-information repeated game. (Here and throughout


$$
the paper, \sigma∗
$$

1 denotes player 1’s strategy unconditional on her type, with the rational type’s


$$
strategy denoted \sigma∗
$$


$$
1(\omegaR).)
$$

The key prior result in this context is the following.


$$
Theorem 0 (Fudenberg and Levine, 1992). If \omegas∗
$$


$$
1 \inΩ, then
$$


$$
lim inf
$$


$$
\delta\to1
$$


$$
U 1(\delta) \geqV0(s∗
$$

1). Our main contribution is providing conditions on s∗ 1 under which this bound can be improved to V (s∗ 1). As we saw in Section 2, this improvement can mean the difference between securing the minmax payoff and the Stackelberg payoff. 3.3 Behavioral Confounding We make use of the following definition.


$$
Definition 2. A strategy s1 is not behaviorally confounded if, for any \omegas′
$$


$$
1 \inΩsuch that
$$

s′


$$
1 \neq s1 and any (\alpha0, \alpha2) \inB1(s1), we have p(\alpha0, s1, \alpha2) \neq p(\alpha0, s′
$$


$$
1, \alpha2).
$$

Thus, a strategy is not behaviorally confounded if the public signals distinguish it from any other commitment type, whenever the short-run players take actions that best respond 14In principle, the long-run player could condition on her past private signal realizations and actions in addition to the public history, but allowing this does not affect the set of equilibrium payoffs, because short-run player strategies are measurable with respect to the public history and long-run player payoffs are independent of past signals and actions. We also note that the signal y2 is irrelevant for the analysis and is included only for generality. 15We thus assume that there is only one rational type (unlike Fudenberg and Levine (1992), who allow multiple rational types). We discuss the extension to multiple rational types in Section 7. 14


to some long-run player strategy. Note that the definition allows the possibility that s1 is


$$
indistinguishable from a mixture of two commitment types \omegas′
$$


$$
1, \omegas′
$$


$$
2 \inΩ.16 Note also that if
$$


$$
there is only one commitment type \omegas1 then s1 is not behaviorally confounded.
$$

Our results in the body of the paper assume that desired commitment strategies are not behaviorally confounded. In games without a player 0 (like trust and communication games),


$$
this is fairly innocuous, as \alpha0 is exogenous, so the identification condition p(\alpha0, s1, \alpha2) \neq
$$


$$
p(\alpha0, s′
$$


$$
1, \alpha2) for all \alpha2 \inB0(s1) holds for generic s1 \neq s′
$$


## 1. In games with a player 0, it is


$$
much more restrictive, because \alpha0 is endogenous, so the identification condition need not
$$

hold generically. For example, in the deterrence game in Section 2.1, the pure Stackelberg


$$
strategy (A, F) is not behaviorally confounded iff each other type \omegas′
$$


$$
1 \inΩsatisfies either
$$

ps′ 1(A|c) + (1 −p)s′ 1(A|d) > p and (1 −p)s′ 1(A|c) + ps′ 1(A|d) > 1 −p, or ps′ 1(A|c) + (1 − p)s′ 1(A|d) < p and (1 −p)s′ 1(A|c) + ps′ 1(A|d) < 1 −p. Nonetheless, in Appendix A we show that our results extend even if the Stackelberg type is behaviorally confounded, so long as it has sufficiently high prior weight relative to


$$
any behavioral confound that induces an \eta-confirmed best response that is not also a best
$$

response to s∗


## 1. In fact, we establish a payoff lower bound that linearly interpolates between

V (s∗ 1) and V0(s∗ 1) as a function of this prior weight. 4 The Commitment Payoff Theorem This section presents the confound-defeating property and our main result: a patient long- run player can secure the commitment payoff V (s∗ 1) corresponding to any strategy s∗


$$
1 \inΩ
$$

that is confounding-defeating and not behaviorally confounded. 4.1 The Confound-Defeating Property We first introduce the confound-defeating property. We give two equivalent definitions of confound-defeatingness. The first definition is more useful for proving our main result. The second definition is more elegant and is easier to characterize in applications (as we do in Sections 5 and 6). The second definition is stated in optimal transport terms: for any two


$$
distributions \rho \in\Delta(Y0) and ϕ \in\Delta(A1), and any strategy for player 2 \alpha2 \in\Delta(A2), define
$$

16Ruling out this possibility would simplify the proof of Lemma 3 and would also let us replace B1(s1) with B0(s1) in Definition 2. That is, all of our results go through with the alternative definition that s1 is


$$
not behaviorally confounded if, for any (\alpha0, \alpha2) \inB0(s1), p(\alpha0, s1, \alpha2) lies outside the convex hull of the set
$$


## S

s′


$$
1\neqs1:\omegas′
$$


$$
1\inΩp(\alpha0, s′
$$


$$
1, \alpha2).
$$

15


the optimal transport problem


$$
OT(\rho, ϕ; \alpha2) :
$$


$$
max
$$


$$
\gamma\in\Delta(Y0\timesA1)
$$


## Z


$$
u1(y0, a1, \alpha2)d\gamma
$$

s.t.


$$
\piY0(\gamma) = \rho and \piA1(\gamma) = ϕ.
$$

Definition 3. Strategy s∗ 1 is confound-defeating if it satisfies one of the following conditions:


$$
(1) For all \varepsilon > 0, there exists \eta > 0 such that for any (\alpha0, \alpha2) \inB\eta(s∗
$$

1) and any s′ 1 satisfying ||s′ 1 −s∗


$$
1||> \varepsilon but ||p(\alpha0, s′
$$


$$
1, \alpha2) −p(\alpha0, s∗
$$


$$
1, \alpha2)||< \eta, there exists ˜s1 satisfying
$$


$$
p(\alpha0, ˜s1, \alpha2) = p(\alpha0, s′
$$


$$
1, \alpha2) and u1(\alpha0, ˜s1, \alpha2) > u1(\alpha0, s′
$$


$$
1, \alpha2).
$$


$$
(2) For any (\alpha0, \alpha2) \inB0(s∗
$$


$$
1), \gamma(\alpha0, s∗
$$


$$
1) is the unique solution to OT(\rho(\alpha0), ϕ(\alpha0, s∗
$$


$$
1); \alpha2).
$$

The first definition says that a strategy s∗ 1 is confound-defeating if any strategy s′ 1 that is a possible confound—in that it differs significantly from s∗ 1 but induces a similar marginal


$$
over signals against some \eta-confirmed best response—is undetectably dominated—in that
$$

the long-run player is strictly better-off under a different strategy ˜s that induces the same marginal. The second definition says that s∗


$$
1 itself undetectably dominates any strategy s′
$$

1 that induces the same marginal over signals against some 0-confirmed best response. The two definitions are equivalent, as we now show.17 Proposition 4. The two definitions of confound-defeatingness are equivalent.


$$
Proof. If the second definition fails, there exist (\alpha0, \alpha2) \inB0(s∗
$$

1), \varepsilon > 0, and a strategy s′ 1 satisfying ||s′ 1 −s∗


$$
1||> \varepsilon such that \gamma(\alpha0, s′
$$


$$
1) solves OT(\rho(\alpha0), ϕ(\alpha0, s∗
$$


$$
1); \alpha2). Since B0(s∗
$$

1) \subset B\eta(s∗


$$
1) for all \eta > 0, this implies that the first definition fails.
$$


$$
Conversely, if the first definition fails, there exists \varepsilon > 0 such that for all \eta > 0,
$$

there exist s\eta


$$
1 and (\alpha\eta
$$


$$
0, \alpha\eta
$$


$$
2) \inB\eta(s∗
$$

1) where ||s\eta 1 −s∗


$$
1||> \varepsilon, ||p(\alpha\eta
$$

0, s\eta


$$
1, \alpha\eta
$$


$$
2) −p(\alpha\eta
$$

0, s∗


$$
1, \alpha\eta
$$

2)||< \eta, and s\eta


$$
1 is not undetectably dominated: u1(\alpha\eta
$$

0, s\eta


$$
1, \alpha\eta
$$


$$
2) \gequ1(\alpha0, ˜s1, \alpha\eta
$$

2) for all ˜s1 such


$$
that p(\alpha\eta
$$

0, s\eta


$$
1, \alpha\eta
$$


$$
2) = p(\alpha\eta
$$


$$
0, ˜s, \alpha\eta
$$


$$
2). Since a1 is identified, p(\alpha\eta
$$


$$
0, s\eta, \alpha\eta
$$


$$
2) = p(\alpha\eta
$$


$$
0, ˜s, \alpha\eta
$$

2) implies


$$
ϕ(\alpha\eta
$$

0, s\eta


$$
1) = ϕ(\alpha\eta
$$

0, ˜s1), and hence s\eta


$$
1 solves OT(\rho(\alpha\eta
$$


$$
0), ϕ(\alpha\eta
$$

0, s\eta


$$
1); \alpha\eta
$$


$$
2). Now, since B\eta(s1) ↓
$$


$$
B0(s1), \Delta(A0)\times(\Delta(A1))Y0 \times\Delta(A2) is compact, and OT(\rho(\alpha0), ϕ(\alpha0, s1); \alpha2) is jointly upper
$$


$$
hemi-continuous in (\alpha0, s1, \alpha2), passing to the limit yields s0
$$


$$
1 and (\alpha0, \alpha2) \inB0(s∗
$$

1) such that ||s0 1 −s∗


$$
1||\geq\varepsilon and s0
$$


$$
1 solves OT(\rho(\alpha0), ϕ(\alpha0, s∗
$$


$$
1); \alpha2). Thus, the second definition fails.
$$

17The converse direction of Proposition 4 is the only point where we use Assumption 1(2) (player 1’s action is identified). Thus, without identification, the first definition of confound-defeatingness still gives a commitment payoff theorem, but it is more difficult to check and needs not reduce to monotonicity in


$$
one-dimensional supermodular games.
$$

16


The following lemma gives the key implication of confound-defeatingness: in any Nash equilibrium, at any history where the marginal over signals is close to that induced by a confound-defeating strategy s∗ 1—both unconditionally and conditional on the event the long-run player is rational—the rational long-run player must play a strategy close to s∗ 1


$$
itself. Here and throughout the paper, given a repeated game strategy profile (\sigma0, \sigma1, \sigma2) and
$$


$$
a period-t history ht, we abbreviate p(\sigma0(ht), \sigma1(ht), \sigma2(ht)) to p(\sigma0, \sigma1, \sigma2|ht).
$$


$$
Lemma 1. Fix a Nash equilibrium (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2) and suppose that s∗ 1 is confound-defeating. Then for all \varepsilon > 0, there exists \eta > 0 such that, for any history ht where


$$
(1) ||p(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$


$$
2|ht) −p(\sigma∗
$$

0, s∗


$$
1, \sigma∗
$$

2|ht)||< \eta, and


$$
(2) ||p(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1(\omegaR), \sigma∗
$$


$$
2|ht) −p(\sigma∗
$$

0, s∗


$$
1, \sigma∗
$$

2|ht)||< \eta,


$$
we have ||\sigma∗
$$


$$
1(ht, \omegaR) −s∗
$$


$$
1||\leq\varepsilon.
$$

Proof. Suppose not, so there exists a history ht where conditions (1) and (2) hold, but


$$
||\sigma∗
$$


$$
1(ht, \omegaR) −s∗
$$


$$
1||> \varepsilon. Condition (1) and the fact (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2) is an equilibrium imply that


$$
(\sigma∗
$$


$$
0(ht), \sigma∗
$$

2(ht)) is an \eta-confirmed best reply to s∗


$$
1, as \sigma∗
$$


$$
1(ht) \eta-confirms it against s∗
$$


## 1. Hence,


$$
condition (2) along with ||\sigma∗
$$


$$
1(ht, \omegaR) −s∗
$$


$$
1||> \varepsilon and confound-defeatingness imply that there
$$


$$
exists some strategy ˜s1 such that p(\sigma∗
$$


$$
0, ˜s1, \sigma∗
$$


$$
2|ht) = p(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1(\omegaR), \sigma∗
$$


$$
2|ht) and u1(\sigma∗
$$


$$
0, ˜s1, \sigma∗
$$

2|ht) >


$$
u1(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1(\omegaR), \sigma∗
$$


$$
2|ht). But this implies that if the long-run player deviates from \sigma∗
$$


$$
1(ht, \omegaR) to
$$

˜s1 at* ht, her continuation payoff is unchanged while her stage game payoff increases. So, this


$$
deviation is profitable, contradicting the assumption that (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2) is an equilibrium. 4.2 Payoff Lower Bound We are now prepared to state our main result.


$$
Theorem 1. If \omegas∗
$$


$$
1 \inΩand s∗
$$

1 is confound-defeating and not behaviorally confounded, then


$$
lim inf
$$


$$
\delta\to1
$$


$$
U 1(\delta) \geqV (s∗
$$

1). In particular, if s∗ 1 is a Stackelberg strategy, Theorem 1 implies that a patient long-run player can secure her Stackelberg payoff v∗ 1. The logic of Theorem 1 is as follows. Fix any equilibrium, and suppose player 1 deviates by taking s∗ 1 in every period. By standard arguments (Fudenberg and Levine, 1992; Sorin, 1999; Gossner, 2011), the short-run players eventually come to expect the signal distribution 17



$$
p(\sigma∗
$$


$$
0(ht), s∗
$$


$$
1, \sigma∗
$$


$$
2(ht)) at public history ht. Since s∗
$$

1 is confound-defeating, by Lemma 1, the short-run players additionally come to expect that if player 1 is rational, she plays a stage game strategy close to s∗


## 1. Since s∗

1 is not behaviorally confounded, the short-run players


$$
also eventually learn that player 1 is not some commitment type other than \omegas∗
$$

1.18 In total,


$$
the short-run players come to believe that player 1 is either the commitment type \omegas∗
$$

1 or is rational and plays a stage game strategy close to s∗


## 1. This leads the short-run players to best

respond to s∗ 1, which ensures the long-run player a payoff of at least V (s∗ 1).


$$
Proof. Fix any \varepsilon > 0. We show that there exists ¯\delta < 1 such that for all \delta > ¯\delta, we have
$$


$$
U 1(\delta) \geqV (s∗
$$


$$
1) −\varepsilon. To do so, we fix any Nash equilibrium (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2) and show that player 1’s payoff from deviating by always taking s∗ 1 is at least V (s∗ 1)−\varepsilon. Let P denote the equilibrium


$$
probability measure over infinite histories H\infty, and let Q denote the corresponding measure
$$

under this deviation.


$$
For any \eta > 0, define the set of period-t histories where the equilibrium signal distribution
$$


$$
is within \eta of that under the deviation by
$$

Ht


$$
\eta =
$$

n


$$
ht : ||p(\sigma∗
$$

0, s∗


$$
1, \sigma∗
$$


$$
2|ht) −p(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$


$$
2|ht)||\leq\eta
$$

o . We first recall a standard bound (essentially due to Gossner (2011)) on the expected number


$$
of periods t where ht /\inHt
$$


$$
\eta. We include a proof in Appendix B.1.
$$

Lemma 2. We have EQ h # n


$$
t : ht /\inHt
$$

\eta) oi


$$
< ¯T(\eta, µ0) := −2 log µ0(\omegas∗
$$

1) \eta2 . Next, for any \zeta > 0, denote the set of beliefs with at most \zeta weight on commitment types other than s∗ 1 by


$$
M\zeta =
$$

n


$$
µ \in\Delta(Ω) : µ
$$




$$
{\omegaR, \omegas∗
$$

1} 


$$
\geq1 −\zeta
$$

o . The next lemma shows that beliefs under Q concentrate on M0 with high probability, uni-


$$
formly in \delta. The proof, which relies on the martingale convergence theorem and the as-
$$

sumption y0 has a full support distribution for any a0, is deferred to Appendix B.2. In what


$$
follows, given a history h, µt(·|h) \in\Delta(Ω) denotes the posterior belief over Ωconditional on
$$

the period t truncation ht of h. (We also write µt(·|ht) for beliefs at period-t history ht.) 18This step is not trivial, for example because we allow s∗ 1 to be indistinguishable from a mixture of commitment types. 18



$$
Lemma 3. For all \zeta > 0, there exists a set of infinite histories G(\zeta) \subsetH\inftysatisfying
$$


$$
Q(G(\zeta)) > 1 −\zeta and a period ˆT(\zeta) (independent of \delta and the choice of equilibrium) such
$$


$$
that, for any h \inG(\zeta) and any t \geqˆT(\zeta), we have µt(·|h) \inM\zeta.
$$


$$
Now, for any ξ > 0, we say that a short-run player strategy (\alpha0, \alpha2) is a ξ-close best
$$

response to s∗


$$
1 (denoted (\alpha0, \alpha2) \inˆBξ(s∗
$$


$$
1)) if (\alpha0, \alpha2) \inB(s1) for some s1 such that ||s1−s∗
$$

1||< ξ. Since ˆBξ(s∗ 1) is upper hemi-continuous and ˆB0(s∗


$$
1) = B(s∗
$$

1), we have


$$
lim inf
$$

ξ\to0


$$
inf
$$


$$
(\alpha0,\alpha2)\inˆBξ(s∗
$$


$$
1) u1(\alpha0, s∗
$$


$$
1, \alpha2) =
$$


$$
inf
$$


$$
(\alpha0,\alpha2)\inB(s∗
$$


$$
1) u1(\alpha0, s∗
$$


$$
1, \alpha2) = V (s∗
$$

1). The next lemma shows that if the short-run players expect the marginal induced by s∗ 1 and believe that player 1 is either the s∗ 1 commitment type or rational, they will take a ξ-close best response to s∗


## 1. Its proof (deferred to Appendix B.3) crucially relies on Lemma 1.


$$
Lemma 4. There exist strictly positive functions \zeta(\eta) and ξ(\eta), satisfying lim\eta\to0 \zeta(\eta) =
$$


$$
lim\eta\to0 ξ(\eta) = 0, such that if ht \inHt
$$


$$
\eta and µt(·|ht) \inM\zeta(\eta) then (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inˆBξ(\eta)(s∗
$$

1). We can now complete the proof of Theorem 1. By Lemmas 2 and 3, conditional on the


$$
(at least) probability 1 −\zeta(\eta) event that h \inG(\zeta(\eta), the expected number of periods where
$$


$$
either ht /\inHt
$$


$$
\eta or µt(·|ht) /\inM\zeta(\eta) is at most ¯T(\eta, µ0) + ˆT(\zeta(\eta)). By Lemma 4, in any period
$$


$$
where ht \inHt
$$


$$
\eta and µt(·|ht) \inM\zeta(\eta), we have (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inˆBξ(\eta)(s∗
$$

1), and hence, for any sufficiently small \eta,


$$
u1(\sigma∗
$$


$$
0(ht), s∗
$$


$$
1, \sigma∗
$$


$$
2(ht)) \geqlim inf
$$

\eta\to0


$$
inf
$$


$$
(\alpha0,\alpha2)\inˆBξ(\eta)(s∗
$$


$$
1) u1(\alpha0, s∗
$$


$$
1, \alpha2) −\varepsilon
$$


$$
3 = V (s∗
$$

1) −\varepsilon 3.


$$
Front-loading the expected periods where ht /\inHt
$$


$$
\eta or µt(·|ht) /\inM\zeta(\eta) (and positing the
$$

minimum payoff of u1 in these periods) gives a lower bound for player 1’s payoff of 


$$
1 −\delta
$$

¯T(\eta,µ0)+ ˆT(\zeta(\eta))


$$
u1 + \delta
$$

¯T(\eta,µ0)+ ˆT(\zeta(\eta))  (1 −\zeta(\eta))¯V (s∗ 1) + \zeta(\eta)u1 −\varepsilon 3 


$$
As \delta \to1, this lower bound converges to
$$

(1 −\zeta(\eta))¯V (s∗ 1) + \zeta(\eta)u1 −\varepsilon 3.


$$
By continuity, at a cost of \varepsilon/3, this bound stays valid for all large enough \delta < 1. Finally,
$$


$$
taking \eta to be small enough so \zeta(\eta)|u1−¯V (s∗
$$

1)|< \varepsilon/3 gives the desired bound of V (s∗ 1)−\varepsilon. 19


In Appendix A, we generalize Theorem 1 to the case where s∗ 1 is behaviorally confounded.


$$
There, we show that if \omegas∗
$$


$$
1 \inΩand s∗
$$

1 is confound-defeating, then


$$
lim inf
$$


$$
\delta\to1
$$


$$
U 1(\delta) \geq\beta(s∗
$$

1; µ0)V (s∗


$$
1) + (1 −\beta(s∗
$$

1; µ0))V0(s∗ 1),


$$
for some function \beta(s∗
$$


$$
1; µ0) (constructed explicitly in Appendix A), where \beta(s∗
$$


$$
1; µ0) = 1 if s∗
$$

1


$$
is not behaviorally confounded, and \beta(s∗
$$

1; µ0) \to1 as the prior weight on s∗ 1 relative to that on confounding commitment types that induce best responses outside B(s∗ 1) converges to 1. 5 Cyclical Monotonicity and Supermodular Games This section characterizes confound-defeating strategies in terms of the support of the


$$
joint distributions over Y0 \times A1 they induce, and uses this characterization to develop a
$$

partial converse to Theorem 1. We then explain the implications of these results for one- dimensional supermodular games. These include the proofs of the claimed results for our motivating examples, Propositions 1–3. 5.1 Cyclical Monotonicity Our characterization is based on the following strict version of the familiar notion of cyclical monotonicity (Rochet, 1987). The definition and subsequent characterization are elementary, but we are not aware of a reference.19


$$
Definition 4. Fix finite sets X, Y and a function u : X \times Y \toR. A set S \subsetX \times Y is
$$

strictly u-cyclically monotone if for any finite collection of pairs {(xi, yi)N i=1} \subsetS such that n


$$
(xi, yi)N
$$


$$
i=1
$$

o \neq n (xi, yi+1)N


$$
i=1
$$

o


$$
(with convention yN+1 = y1),
$$


## N


## X


$$
i=1
$$


$$
u(xi, yi) >
$$


## N


## X


$$
i=1
$$

u(xi, yi+1).


$$
Proposition 5. A joint distribution \gamma \in\Delta(X \times Y ) satisfying \piX(\gamma) = \rho and \piY (\gamma) = ϕ is
$$

the unique solution to the optimal transport problem OT(\rho, ϕ) :


$$
max
$$


$$
\gamma′\in\Delta(X\timesY )
$$


## Z


$$
u(x, y)d\gamma′
$$

s.t.


$$
\piX(\gamma′) = \rho and \piY (\gamma′) = ϕ
$$

19The closest argument we are aware of is the proof of Lemma 2 of Ball and Kattwinkel (2024). We thank Ian Ball for pointing out this connection and suggesting the proof of Proposition 5. 20



$$
if and only if its support supp(\gamma) \subsetX \times Y is strictly u-cyclically monotone.
$$

We apply Proposition 5 to our setting with X = Y0 and Y = A1 and use the OT definition of confound-defeatingness to characterize confound-defeatingness in terms of the support of


$$
\gamma(\alpha0, s∗
$$

1). Since we has assumed that the distribution of y0 has full support, this set depends only on s∗ 1, so we write it as


$$
supp(s∗
$$


$$
1) := {(y0, a1) \inY0 \times A1 : a1 \insupp(s∗
$$


$$
1(y0))} .
$$


$$
In addition, letting u1(·, \alpha2) denote player 1’s utility u1(y0, a1, \alpha2) as a function of (y0, a1)
$$


$$
for a fixed player 2 strategy \alpha2, we say that u1 is strictly cyclically separable if whenever a
$$


$$
set S \subsetY0 \times A1 is strictly u1(·, \alpha2)-cyclically monotone for some \alpha2, it is strictly u1(·, \alpha2)-
$$


$$
cyclically monotone for all \alpha2. In this case, the strict u1-cyclical monotonicty of a set S \subset
$$


$$
Y0 \times A1 is well-defined independent of \alpha2.20 Finally, we say that a strategy s∗
$$

1 is strictly


$$
u1(·, \alpha2) (resp., u1)-cyclically monotone if supp(s∗
$$


$$
1) \subsetY0 \times A1 is strictly u1(·, \alpha2) (resp.,
$$

u1)-cyclically monotone. We obtain the following characterization. Corollary 1. A strategy s∗


$$
1 is confound-defeating if and only if it is strictly u1(·, \alpha2)-cyclically
$$


$$
monotone for all (\alpha0, \alpha2) \inB0(s∗
$$

1). Moreover, if u1 is strictly cyclically separable, a strategy s∗ 1 is confound-defeating if and only if it is strictly u1-cyclically monotone. Together with Theorem 1, we obtain the following corollary, where (when u1 is cycli- cally separable) we denote the long-run player’s greatest lower commitment payoff from any strictly u1-cyclically monotone strategy by vCM 1


$$
:=
$$


$$
sup
$$

s1:


$$
\omegas1 \inΩand s1 is strictly u1-cyclically
$$

monotone and not behaviorally confounded


$$
min
$$


$$
(\alpha0,\alpha2)\inB(s1) u1(\alpha0, s1, \alpha2).
$$


$$
Corollary 2. If u1 is strictly cyclically separable, \omegas1 \inΩ, and s1 is strictly u1-cyclically
$$

monotone and not behaviorally confounded, then


$$
lim inf
$$


$$
\delta\to1
$$


$$
U 1(\delta) \geqV (s∗
$$

1). In particular,


$$
lim inf
$$


$$
\delta\to1
$$


$$
U 1(\delta) \geqvCM
$$

1 . 20Note that this case always applies in games without a player 2, such as deterrence games. 21


5.2 Payoff Upper Bound We now give a partial converse to Corollary 2: if the long-run player is rational with high probability, her payoff is bounded above by her greatest upper commitment payoff from any u1-cyclically monotone strategy, defined by ¯vCM 1


$$
:=
$$


$$
sup
$$

s1 : s1 is u1-cyclically monotone


$$
max
$$


$$
(\alpha0,\alpha2)\inB(s1) u1(\alpha0, s1, \alpha2),
$$

where s1 is u1-cyclically monotone if supp(s1) satisfies the usual definition of u1-cyclically monotonicity (i.e., Definition 4 with the strict inequality replaced by a weak one). The idea is that if a strategy s1 is not u1-cyclically monotone strategy, then the rational long-run player has a profitable and undetectable deviation from s∗ 1, so the short-run players cannot expect to face a strategy close to s1 with high probability when the long-run player is rational with high probability.


$$
In the following statement, u1 is cyclically separable if whenever a set S \subsetY0 \times A1 is
$$


$$
u1(·, \alpha2)-cyclically monotone for some \alpha2, it is u1(·, \alpha2)-cyclically monotone for all \alpha2.
$$

Proposition 6. Suppose u1 is cyclically separable. Then for all \varepsilon > 0, there exists κ > 0


$$
such that, for any prior µ0 satisfying µ0(\omegaR) > 1 −κ and any \delta < 1,
$$


$$
¯U1(\delta) < ¯vCM
$$

1 + \varepsilon. The key step in the proof of Proposition 6 is the following lemma, which says that a rational long-run player with a cyclically separable utility must play a cyclically monotone stage game strategy at every history in any repeated game Nash equilibrium. We record the lemma and its (short) proof, as it applies equally to any repeated game, with or without


$$
multiple long-run players and incomplete information.
$$


$$
Lemma 5. For any Nash equilibrium (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$


$$
2) and any history ht, \sigma∗
$$


$$
1(ht, \omegaR) is u1-
$$

cyclically monotone.


$$
Proof. Note that \sigma∗
$$


$$
1(ht, \omegaR) must solve
$$


$$
OT(\sigma∗
$$


$$
0(ht), ϕ(\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
1(ht, \omegaR)), \sigma∗
$$


$$
2(ht)).
$$

This holds because, otherwise, there exists a strategy s1 that gives player 1 a strictly higher


$$
payoff at history ht than \sigma∗
$$


$$
1(ht, \omegaR) does, but gives the same signal distribution, and hence
$$

22


the same continuation payoff. By a standard optimal transport result (e.g., Theorem 1.38 in


$$
Santambrogio, 2015), this implies that supp(\gamma(\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
1(ht, \omegaR))) is u1(·, \sigma∗
$$


$$
2(ht))-cyclically
$$


$$
monotone. Hence, by cyclical separability, \sigma∗
$$


$$
1(ht, \omegaR) is u1-cyclically monotone.
$$

Combining Corollary 2 and Proposition 6 gives a fairly tight characterization of a patient long-run player’s payoff when u1 is cyclically and strictly cyclically separable: it is at least her lower commitment payoff from any non-behaviorally confounded, strictly u1-cyclically monotone commitment type strategy, and at most her greatest upper commitment payoff from any u1-cyclically monotone strategy. 5.3 One-Dimensional Supermodular Games We now show how our results apply in games where the long-run player’s utility is super- modular in a one-dimensional signal and action. This class of games includes the deterrence, trust, and signaling examples of Section 2.


$$
The relevant supermodularity notion is strict supermodularity in (y0, a1) for all \alpha2.
$$

Definition 5. The long-run player’s payoff u1 is strictly supermodular if there exist total orders (\succeqY0, \succeqA1) such that


$$
u1(y0, a1, a2) −u1(y0, a′
$$

1, a2) > u1(y′ 0, a1, a2) −u1(y′ 0, a′ 1, a2) for all y0 \succy′ 0, a1 \succa′ 1, a2. We say that a (possibly mixed) strategy s1 : Y0 \to\Delta(A1) is monotone if any selection from its graph is monotone. Formally,


$$
Definition 6. A long-run player strategy s1 is monotone if, for any y0 \succy′
$$


$$
0, a1 \insupp(s1(y0)),
$$

and a′


$$
1 \insupp(s1(y′
$$

0)), we have a1 \succeqa′ 1. The following is the key result of this subsection. Proposition 7. Suppose u1 is strictly supermodular. Then, for any strategy s∗ 1, the following are equivalent:


$$
(1) s∗
$$

1 is confound-defeating.


$$
(2) s∗
$$

1 is monotone.


$$
(3) s∗
$$

1 is u1-cyclically monotone. 23


Proof. The key step is the following standard result from optimal transport.


$$
Lemma 6. Suppose u1 is strictly supermodular. Then, for any (\alpha0, \alpha2), s∗
$$

1 is monotone iff


$$
\gamma(\alpha0, s∗
$$


$$
1) is the unique solution to OT(\rho(\alpha0), ϕ(\alpha0, s∗
$$


$$
1); \alpha2).
$$


$$
Proof. By Lemma 2.8 in Santambrogio (2015), if s∗
$$


$$
1 is monotone then \gamma(\alpha0, s∗
$$

1) is the unique


$$
co-monotone transport plan between \rho(\alpha0) and ϕ(\alpha0, s∗
$$

1)—that is, the unique joint distribu-


$$
tion \gamma \in\Delta(Y0 \times A1) with marginals \rho(\alpha0) and ϕ(\alpha0, s∗
$$


$$
1) such that, according to \gamma, y0 and
$$


$$
a1 are co-monotone random variables. Conversely, since \rho(\alpha0) has full support, if s∗
$$

1 is not


$$
monotone then \gamma(\alpha0, s∗
$$

1) is not co-monotone. Finally, by Theorem 2.9 and Exercise 10 in Santambrogio (2015), when u1 is strictly supermodular, the co-monotone transport plan is


$$
the unique solution to OT(\rho(\alpha0), ϕ(\alpha0, s∗
$$


$$
1); \alpha2).
$$

By Lemma 6, if s∗


$$
1 is confound-defeating then \gamma(\alpha0, s∗
$$

1) is the unique solution to


$$
OT(\rho(\alpha0), ϕ(\alpha0, s∗
$$


$$
1); \alpha2) for any (\alpha0, \alpha2) \inB0(s∗
$$

1), and hence is monotone; and, conversely, if s∗


$$
1 is monotone then it is the unique solution to OT(\rho(\alpha0), ϕ(\alpha0, s∗
$$


$$
1); \alpha2) for any (\alpha0, \alpha2),
$$

and hence is confound-defeating. Moreover, s∗


$$
1 is monotone if and only if \gamma(\alpha0, s∗
$$

1) is co-


$$
monotone, as shown in the proof of Lemma 6, and \gamma(\alpha0, s∗
$$

1) is co-monotone if and only if it is u1-cyclically monotone, by Lemma 1 of Lin and Liu (2024) (see also Proposition 1 of Rochet (1987)). This establishes the desired three-way equivalence. Denote the long-run player’s lower commitment payoff from any non-behaviorally con- founded, monotone commitment type strategy and her upper commitment payoff from any monotone strategy, respectively, by vmon 1


$$
=
$$


$$
sup
$$

s1:


$$
\omegas1 \inΩand s1 is monotone
$$

and not behaviorally confounded


$$
min
$$


$$
(\alpha0,\alpha2)\inB(s1) u1(\alpha0, s1, \alpha2),
$$

¯vmon 1


$$
=
$$


$$
sup
$$

s1: s1 is monotone


$$
max
$$


$$
(\alpha0,\alpha2)\inB(s1) u1(\alpha0, s1, \alpha2).
$$

Combining Theorem 1 and Propositions 6 and 7, we obtain the following corollary. Corollary 3. Suppose u1 is strictly supermodular. Then


$$
lim inf
$$


$$
\delta\to1
$$


$$
U 1(\delta) \geqvmon
$$

1 .


$$
Conversely, for all \varepsilon > 0, there exists κ > 0 such that for any prior µ0 satisfying µ0(\omegaR) >
$$


$$
1 −κ and any \delta < 1,
$$


$$
¯U1(\delta) < ¯vmon
$$

1 + \varepsilon. 24


Corollary 3 is a main conclusion of this paper: a patient long-run player is assured at least her commitment payoff from any monotone, non-behaviorally confounded strategy s1 such


$$
that µ0(\omegas1) > 0. This implies the supermodular cases of Proposition 1 (as in the deterrence
$$

game u1 is strictly supermodular with the order A \succF and C \succD when x + y < 1)


$$
and Proposition 2 (as in the trust game u1 is strictly supermodular with the order H \succL
$$


$$
and T \succN when min{w, z} > 0), as well as Proposition 3 (as in a signaling game u1 =
$$


$$
(1 −\lambda)v(a2(a1)) −\lambdaw(a1, \theta) is strictly supermodular in (a1, \theta) for any function a2 : a1 \toR
$$

if w if strictly submodular). Moreover, it does not require the assumption in Section 2 that there is only one commitment type that plays a pure strategy. Thus, Corollary 3 implies that, in general repeated signaling games with strictly submodular signaling costs and state- independent sender preferences, a patient long-run sender is assured at least her commitment


$$
payoff from any monotone, non-behaviorally confounded strategy s1 such that µ0(\omegas1) > 0,
$$

even if short-run players observe only past actions and not past state realizations.21 At the same time, the converse direction of Corollary 3 implies the submodular cases of Propositions 1 and 2. For example, in the deterrence game, if x + y > 1 (the “submodular


$$
case”) then u1 is strictly supermodular with the order F \succA and C \succD. Since any
$$

long-run player strategy that is monotone with this order takes F with higher probability after c, the unique short-run player best response to any such strategy is D, implying that ¯vmon 1 = 1 −p + py. The argument for the submodular case of Proposition 2 is similar. Finally, in games where vmon 1


$$
= ¯vmon
$$

1 (which holds if the short-run players have a unique best response to any monotone strategy s1), Corollary 3 gives a unique payoff prediction as


$$
µ0(\omegaR) and \delta both approach 1. For example, this holds in the deterrence and trust games.
$$

6 Communication Games We now consider implications of our results for repeated communication games. Recall


$$
that the model covers communication games by dropping player 0; viewing \rho(y0) as the prior
$$


$$
distribution of a payoff-relevant state y0; letting \rho(y1|a1) = 1({y1 = a1}) (so a1 is perfectly
$$

monitored); viewing a2 as a mapping from a1 to a finite set of responses R; and assuming


$$
that u1 and u2 depend on a2 only through the induced response a2(a1) \inR. In this section,
$$


$$
we refer to player 1 as the sender and player 2 as the receiver, and we relabel y0 as \theta.
$$

We have already observed that if the sender’s preferences are state-independent, meaning


$$
that u1(\theta, a1, r) = (1−\lambda)v(a1, r)−\lambdaw(a1, \theta) for some functions v and w and some \lambda \in(0, 1),
$$


$$
21Moreover, this result extends to preferences of the form u1(a1, r, \theta) = (1 −\lambda)v(a1, r) −\lambdaw(a1, \theta).
$$

25



$$
and if w is strictly submodular, then lim sup\delta\to1 ¯U1(\delta) \geqvmon. Thus, a patient sender with
$$

state-independent preferences over the receiver’s action and a strictly submodular signaling cost can secure her best commitment payoff from any monotone signaling strategy. We now turn to the following question. Consider a cheap talk game with a state-independent


$$
utility v(r) for the sender and a utility u2(\theta, r) for the receiver, so the sender’s action a1 is
$$


$$
payoff irrelevant. In this game, the sender’s utility u1(\theta, a1, r) is independent of a1 and hence
$$


$$
cannot be strictly supermodular in (˜r, \theta). However, suppose that the sender has a “grain of
$$

commitment power,” in that she can publicly adjust her preferences at the beginning of the


$$
game by committing to pay a small communication cost w(a1, \theta) whenever she takes action
$$


$$
a1 in state \theta. We ask what commitment payoffs V (s1) can be secured by leveraging such a
$$

grain of commitment. By a standard revelation principle argument, for any set of sender actions A1 and any


$$
strategy ˆs1 : \Theta \to\Delta(A1), there exists a direct communication mechanism s1 : \Theta \to\Delta(R)
$$

such that V (s1) = V (ˆs1). We thus assume for the rest of this section that A1 = R, so the sender’s message a1 = ˜r can be interpreted as a recommended action for the receiver. The following result provides a general sufficient condition for the commitment payoff V (s1) from


$$
a communication mechanism s1 : \Theta \to\Delta(R) to be approximately securable.
$$


$$
Proposition 8. If a communication mechanism s1 : \Theta \to\Delta(R) is monotone with respect to
$$


$$
some order (\succeq\Theta, \succeqR) and is such that \omegas1 \inΩand s1 is not behaviorally confounded, then
$$

for any \varepsilon > 0 and any strictly submodular cost function w : R \times \Theta \to[0, 1],


$$
lim inf
$$


$$
\delta\to1
$$


$$
U w(\delta) \geq(1 −\varepsilon)V (s1) −\varepsilon,
$$


$$
where U w(\delta) is the infimum of the long-run player’s payoff in any Nash equilibrium in the
$$

repeated game where her utility is given by


$$
u1(\theta, ˜r, r) = (1 −\varepsilon)v(r) −\varepsilonw(˜r, \theta).
$$

Proof. Immediately from Corollary 3.


$$
An interpretation of the communication cost w(˜r, \theta) is that this represents a “lying cost”
$$

(Chen, Kartik, and Sobel, 2008; Kartik, 2009) incurred by a sender who recommends action


$$
˜r in state \theta. In particular, if R = \Theta and the receiver’s optimal action in state \theta is r = \theta,
$$


$$
we can interpret the sender’s message ˜r \in\Theta as a report of the state, and we can interpret
$$


$$
w(˜r, \theta) as the lying cost associated with misreporting state \theta as ˜r. This example matches the
$$

26



$$
main example in Kartik (2009), where it is likewise assumed that the lying cost w(˜r, \theta) is
$$

strictly submodular. Proposition 8 thus implies that augmenting repeated cheap talk with a small lying cost provides a reputational foundation for any communication mechanism that is monotone with respect to some order over states and actions.22


$$
To operationalize Proposition 8, it remains to characterize what mechanisms s1 : \Theta \to
$$

\Delta(R) are monotone with respect to some order (\succeq\Theta, \succeqR). Our last result provides this characterization. To state it, let G(s1) be the bipartite graph with vertices \Theta and R, where


$$
a state \theta and an action r are linked if r \insupp(s1(\theta)). We will see that if s1 is monotone
$$

then G(s1) is acyclic and also does not contain what we call a “forbidden triple.”


$$
Definition 7. A forbidden triple for a mechanism s1 : \Theta \to\Delta(R) is either
$$


$$
(1) A set of three distinct actions {r1, r2, r3} and four distinct state {\theta1, \theta2, \theta3, \theta4} where
$$


$$
rk \insupp(s1(\thetak)) for k \in{1, 2, 3} and {r1, r2, r3} \subsetsupp(s1(\theta4)); or
$$


$$
(2) A set of three distinct states {\theta1, \theta2, \theta3} and four distinct actions {r1, r2, r3, r4} where
$$


$$
{rk, r4} \insupp(s1(\thetak)) for k \in{1, 2, 3}.
$$


$$
\theta1
$$


$$
\theta2
$$


$$
\theta3
$$


$$
\theta4
$$

r1 r2 r3 \Theta


## R

Figure 1: A Type (1) Forbidden Triple


$$
Notes. Monotonicity is violated for any placement of \theta4 in the order \succeq\Theta.
$$

For example, if a Type (1) forbidden triple exists, where without loss r1 \precr2 \precr3 and


$$
\theta1 \prec\theta2 \prec\theta3, then s1 cannot be monotone with respect to any order, as if \theta4 \prec\theta2 then s1
$$

22For example, adding a Stackelberg commitment type and a small lying cost in the infinitely-repeated “political correctness” game of Morris (2001) suffices to secure the Stackelberg payoff, in contrast to Morris’s negative result. 27



$$
is non-monotone because r3 \insupp(s1(\theta4)) but r2 \insupp(s1(\theta2)); and if \theta4 \succ\theta2 then s1 is
$$


$$
non-monotone because r1 \insupp(s1(\theta4)) but r2 \insupp(s1(\theta2)). See Figure 1.
$$

Our final result is that, conversely, if G(s1) is acyclic and does not contain a forbidden triple, then s1 : \Theta \to\Delta(R) is monotone with respect to some order.


$$
Proposition 9. A communication mechanism s1 : \Theta \to\Delta(R) is monotone with respect to
$$


$$
some order (\succeq\Theta, \succeqR) if and only if G(s1) is acyclic and does not contain a forbidden triple.
$$

Proposition 9 implies that the set of mechanisms that are monotone with respect to


$$
some order includes, for example, all partitions (i.e., deterministic mechanisms s1 : \Theta \toR)
$$

and all linear partitions with randomization at the endpoints. This set includes the set of all monotone partitions, which are shown to be optimal in certain persuasion problems by Kolotilin (2018) and Dworczak and Martini (2019). However, it does not always include the


$$
optimal mechanism. For example, if the receiver’s optimal action is r = E[\theta] and \theta \in{0, 1}
$$


$$
with equal probability, and the sender’s utility is 1({r \in{1/3, 2/3}}), then the unique
$$


$$
optimal mechanism induces r \in{1/3, 2/3} with equal probability, but this mechanism is
$$

not monotone with respect to any order because the corresponding graph G(s1) contains the cycle (0, 1/3), (1, 1/3), (1, 2/3), (0, 2/3).23 Proposition 9 is a general mathematical result that could have other applications (and that may have been previously noted in other contexts, although we have not found a ref- erence). It characterizes when a Markov transition matrix f : X \toY is consistent with


$$
a joint distribution over X \times Y that is co-monotone with respect to some order (\succeqX, \succeqY ).
$$

Alternatively, it characterizes when the vertices of a bipartite graph can be drawn on two straight lines so that no edges cross. 7 Discussion This paper has studied reputation-formation when a player desires a reputation for con- ditional action. The main result is that if a strategy is confound-defeating and either not behaviorally confounded or salient, a patient long-run player can secure the corresponding commitment payoff. A strategy is confound-defeating if and only if it is the unique solu- tion to an optimal transport problem. In one-dimensional supermodular games, a strategy 23This example is a discrete version of a “bi-pooling” policy. With a continuous state, Kleiner, Moldovanu, and Strack (2021) and Arieli et al. (2023) show that the bi-pooling policies are those that are uniquely optimal in some persuasion problem. 28


is confound-defeating if and only if it is monotone. In repeated signaling games with state- independent sender preferences and a strictly submodular signaling cost, a patient sender can secure her commitment payoff from any monotone strategy. Finally, we characterized the communication strategies that are monotone with respect to some order, and that are thus implementable with a small “lying cost.” We mention some possible extensions of our results. First, the connection between un- observed deviations and optimal transport is not specific to the long-run/short-run model we study and could also be applied to repeated games with multiple long-run players, with or without incomplete information. Second, extending the model to allow multiple short- run players and to allow u0 to depend on a2 would encompass reputation-formation by a long-run mediator who coordinates play among multiple short-run players. This extension can potentially provide a reputational foundation for a general static mediation solution, as in Myerson (1982). Third, our results extend to the case with multiple rational types with different preferences, so long as they all have the same Stackelberg strategy and it is confound-defeating for all of them. A possible extension to the case with multiple rational types with different Stackelberg strategies that are confound-defeating only for some types would require additional analysis and qualifications. Fourth, cyclical monotonicity can be ex- plored in multidimensional games, for example communication games with multidimensional states or actions. In particular, we are not sure if Proposition 8 has a useful multidimensional analogue. Fifth, in signaling games, we gave conditions under which the sender can secure her commitment payoff from any monotone strategy. An open question is when the Stackelberg signaling strategy is monotone. Finally, Watson (1993) and Battigalli and Watson (1997) show that the classic reputation results of Fudenberg and Levine (1989; 1992) require only two rounds of iterated deletion of dominated strategies, rather than the full force of Nash equilibrium. Our results instead require three rounds of deletion: under our conditions, the long-run player secures the Stackelberg payoff by best responding to any short-run player best response to any long-run player strategy that is not undetectably dominated.


## A

Appendix: Salience This appendix generalizes Theorem 1 to the case where s∗ 1 is behaviorally confounded. As


$$
noted in the text, this extension is particularly important for games where \alpha0 is endogenous,
$$

like the deterrence game in Section 2.1, as in these games s∗ 1 is often behaviorally confounded when there are multiple commitment types. 29


Our approach to extending Theorem 1 is as follows. If s∗ 1 is behaviorally confounded, we calculate the minimum weight on s∗ 1 that ensures that once short-run players learn the desired signal distribution, they best respond to s∗ 1 (rather than a confounding strategy).


$$
Then we calculate the minimum probability \beta that the long-run weight on s∗
$$

1 exceeds this


$$
level under the deviation measure Q. We call \beta the “salience” of s∗
$$

1, and we establish a lower


$$
bound for a patient long-run player’s payoff as a function of \beta. If s∗
$$

1 is not behaviorally confounded then its salience is 1, in which case we recover Theorem 1. Before defining salience, we require a preliminary definition. In what follows, given a


$$
belief µ \in\Delta(Ω) and a subset Ω′ \subsetΩ, we denote the conditional distribution of µ over Ω′
$$


$$
by µ(·|Ω′). In addition, given a belief µ \in\Delta(Ω\ {\omegaR}), we slightly abuse notation by also
$$

denoting by µ the strategy ˜s1 given by ˜s1(y0)[a1] =


## P


$$
\omegas1\inΩ\{\omegaR} µ(\omegas1)s1(y0)[a1].
$$


$$
Definition 8. For any \eta, ς > 0, a number c \in[0, 1] is an (\eta, ς)-confounding weight if there
$$


$$
exists a belief µ \in\Delta(Ω) satisfying the following conditions.
$$


$$
(1) µ(\omegaR) < 1.
$$


$$
(2) There exists s1 \in\Delta(A1)Y0 such that ||µ(·|Ω\ {\omegaR}) −s1||< ς and B(s1) \ B(s∗
$$

1) \neq \emptyset.


$$
(3) µ(Ω\eta(s∗
$$

1)) > 1 −\eta, where Ω\eta(s∗


$$
1) = {\omegas1 \inΩ\{\omegaR} : ||p(\alpha0, s1, \alpha2)−p(\alpha0, s∗
$$


$$
1, \alpha2)||< \eta for some (\alpha0, \alpha2) \inB1(s∗
$$


$$
1)}\cup{\omegaR}.
$$


$$
(4) µ(s∗
$$


$$
1|Ω\ {\omegaR}) = c.
$$


$$
Let c\eta,ς = sup{c : c is (\eta, ς)-confounding}, with the convention that if no (\eta, ς)-confounding
$$


$$
weight exists, then c\eta,ς = −\infty. Finally, let c0 = limς\to0 lim\eta\to0 cς,\eta.
$$


$$
Condition (1) implies that µ(·|Ω\ {\omegaR}) is well-defined. Condition (2) says that µ(·|Ω\
$$


$$
{\omegaR}) is within ς of a belief to which the short-run players have a best response outside
$$

B(s∗


$$
1). Condition (3) says that µ puts at most \eta weight on commitment types that induce
$$


$$
signals that are not \eta close to those induced by s∗
$$


## 1. Condition (4) says that µ(·|Ω\ {\omegaR})

assigns probability c to s∗


## 1. Note that c0 < 1, by upper hemi-continuity of the best-response

correspondence B(·). In addition, the sets Ω\eta(s∗ 1) are nested and all contain s∗ 1, which implies that the set Ω0(s∗


$$
1) :=
$$

\


$$
\eta>0
$$

Ω\eta(s∗ 1)


$$
is well-defined and contains {\omegas∗
$$


$$
1, \omegaR}.
$$

30


Definition 9. The salience of a strategy s∗


$$
1 \inΩis
$$


$$
\beta = max
$$

(µ0(s∗ 1|Ω0(s∗


$$
1) \ {\omegaR}) −c0
$$

1 −c0 , 0 ) ,


$$
with the convention that if c0 = −\inftythen \beta = 1.
$$

The logic of this definition is that conditional on the long-run player being irrational, c0 is the minimum weight on s∗ 1 that ensures short-run players best respond to s∗ 1, and (by


$$
Bayes’ rule) \beta is the minimum probability the long-run weight on s∗
$$

1 strictly exceeds c0. The general version of our main result is as follows.


$$
Theorem 2. If \omegas∗
$$


$$
1 \inΩand s∗
$$


$$
1 is confound-defeating and has salience \beta, then
$$


$$
lim inf
$$


$$
\delta\to1
$$


$$
U 1(\delta) \geq\betaV (s∗
$$


$$
1) + (1 −\beta)V0(s∗
$$

1). Note that if s∗ 1 is not behaviorally confounded then Ω0(s∗


$$
1) = {\omegas∗
$$


$$
1, \omegaR} for sufficiently
$$


$$
small \eta. By upper hemi-continuity of B(·), this implies that c\eta,ς = −\inftyfor sufficiently small
$$


$$
\eta and ς, so \beta = 1. Theorem 2 therefore generalizes Theorem 1.
$$


$$
Moreover, since c0 < 1, we have \beta \to1 whenever µ0|Ω0(s∗
$$


$$
1)\{\omegaR}(s∗
$$


$$
1) \to1, in which case
$$

Theorem 2 recovers the conclusion of Theorem 1 even if s∗ 1 is behaviorally confounded. In fact, Theorem 1 delivers much more than continuity of the payoff lower bound at µ0|Ω0(s∗


$$
1)\{\omegaR}(s∗
$$


$$
1) =
$$

1—it gives an explicit lower bound that declines linearly with µ0|Ω0(s∗


$$
1)\{\omegaR}(s∗
$$

1).24 For example, consider the deterrence game from Section 2.1 with two commitment types, the pure Stackelberg type (A, F) and the type s1 that takes A with probability p for each signal. In this example, c0 is the probability such that the short-run player is indifferent between C and D when the long-run player plays (A, F) with probability c0 and plays s1 with probability 1−c0, which is given by c0 = pg+(1−p)l (2p−1)(1+g). The salience of type (A, F) is then


$$
\beta = max
$$

 µ0|Ω0(s∗


$$
1)\{\omegaR}((A,F))−c0
$$

1−c0 , 0 


$$
, and Theorem 2 implies that as \delta \to1 the long-run player
$$


$$
is assured a payoff of at least \betap + (1 −\beta)(1 −p). In particular, whenever C is the unique
$$

best response to (A, F), we have c0 < 1, so that as the prior weight on (A, F) relative to s1


$$
increases, \beta converges to 1 and the long-run player is assured her pure Stackelberg payoff p.
$$

24This feature contrasts with the approach of Ely, Fudenberg, and Levine (2008), who show that intro- ducing a sufficiently high conditional probability of the Stackelberg type overturns Ely and Valimaki’s 2003 bad reputation result, but require an unbounded likelihood ratio between the Stackelberg type and the “bad commitment type.” 31



$$
The proof of Theorem 2 follows from the proof of Theorem 1 and the fact that (\alpha0, \alpha2) \in
$$

B\eta(s∗


$$
1) (and hence u1(\sigma∗
$$

0, s∗


$$
1, \sigma∗
$$


$$
2) \geqinf(\alpha0,\alpha2)\inB\eta(s∗
$$


$$
1) u1(\alpha0, s∗
$$


$$
1, \alpha2)) for all ht \inHt
$$

\eta, once we replace Lemma 4 with the following lemma.


$$
Lemma 7. For any \eta sufficiently small, any t > ¯T(\eta) (chosen as in Theorem 1), and any
$$


$$
Nash equilibrium (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2), we have


$$
lim inf
$$

ξ\to0


$$
Q(h \inH\infty: (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inˆBξ(s∗
$$


$$
1)) \geq\beta.
$$

The proof of Lemma 7 in turn relies on the following technical lemma, which will be used to show that if B(µ) \subsetB(s∗ 1) and d(˜µ, conv({µ, s∗ 1}) < ϑ (where d(·, ·) denotes distance


$$
from a point to a set, and conv(·) denotes convex hull), then B(˜µ) \subsetB(s∗
$$

1), where ϑ can be chosen uniformly over a certain set of beliefs µ.


$$
Lemma 8. For any s1 \in\Delta(A1)Y0 and ς > 0, let
$$


$$
Cς(s1) = {s′
$$

1 : B(s′′


$$
1) \subsetB(s1) for all s′′
$$

1 s.t. ∥s′ 1 −s′′


$$
1∥\leqς}.
$$


$$
Then, there exists ϑ(ς, s1) > 0, vanishing as ς \to0, such that for all ˜s1, s′
$$

1 such that s′


$$
1 \in
$$


$$
Cς(s1) and d(˜s1, conv({s1, s′
$$


$$
1})) \leqϑ(ς, s1), we have B(˜s1) \subsetB(s1).
$$


$$
Proof. We first show that B(˜s1) \subsetB(s1) if ϑ(ς, s1) = 0, so that ˜s1 \inconv({s1, s′
$$

1}). To see this, note that since B(s′


$$
1) \subsetB(s1), the set of player 0 best responses at any ˜s1 \in
$$

conv({s1, s′ 1}) (other than s′ 1) is the same as that at s′ 1, by the sure-thing principle. This then implies the same conclusion for player 2, so B(˜s1) = B(s′


$$
1) \subsetB(s1).
$$

Next, we show there exists some ϑ(ς, s1) > 0, which can be chosen independently of s′


$$
1 \inCς(s1), such that if d(˜s1, conv({s1, s′
$$


$$
1})) \leqϑ(ς, s1) then B(˜s1) \subsetB(s1). For any ς, note
$$

that if s′′


$$
1 \inCς(s1) (the closure of Cς(s1)), then B(s′′
$$


$$
1) \subsetB(s1). From here, suppose no such
$$

ϑ > 0 has the desired property for all s′


$$
1 \inCς(s1). Then there exists a sequence (sn
$$

1, ˜sn 1) such that sn


$$
1 \inCς(s1), d(˜sn
$$

1, conv(sn 1, s1)) < 1 n, and B(˜sn


$$
1) \ B(s1) \neq \emptysetfor large enough n. Taking
$$

a subsequence, this implies there exists (snk 1 , ˜snk 1 ) \to(s′ 1, ˜s1) such that s′


$$
1 \inCς(s1) (since this
$$

set is closed) and d(˜s1, conv(s′ 1, s1)) = 0, but B(˜s1)\B(s1) \neq \emptyset. But this contradicts the fact,


$$
established above, that B(˜s1) \subsetB(s1) when ˜s1 \inconv({s1, s′
$$

1}), completing the proof.


$$
Proof of Lemma 7. We show there exists strictly positive functions \zeta(\eta) and ξ(\eta), vanishing
$$

32


as \eta \to0, and ¯T(\eta) such that, for all t > ¯T(\eta),


$$
Q(h \inH\infty: (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inˆBξ(\eta)(s∗
$$


$$
1))) \geq(1 −\zeta(\eta))\beta\zeta,\eta, where
$$


$$
\betaς,\eta = (1 −\eta)µ0|Ω0(s∗
$$


$$
1)\{\omegaR}(s∗
$$

1) −c\eta,ς 1 −\eta −c\eta,ς . Lemma 2 and an appropriate modification of Lemma 3 (with Ω\eta(s∗


$$
1) in place of {\omegas∗
$$

1}) imply


$$
that, on a set of histories G(\zeta(\eta)) satisfying Q(G(\zeta(\eta))) > 1 −\zeta(\eta), both ht \inHt
$$

\eta and µt(Ω\eta(s∗


$$
1) \ {\omegaR}|ht) > 1 −\eta for all t > ¯T(\eta), independent of the choice of the equilibrium
$$

strategy and discount factor. Suppose these two conditions are satisfied and t > ¯T(\eta). We


$$
consider three possible cases, and show for sufficiently small \eta, that in the first two cases
$$


$$
(\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inˆBξ(\eta)(s∗
$$


$$
1) and the third arises with probability at most 1 −\betaς,\eta. This then
$$


$$
implies, in total, Q(h \inH\infty: (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inˆBξ(\eta)(s∗
$$


$$
1))) is no less than (1 −\zeta(\eta))\beta\zeta,\eta,
$$

completing the proof.


$$
First, suppose that µt({\omegaR, \omegas∗
$$


$$
1}|ht) > 1 −\zeta(\eta). Then, for \zeta(\eta) and ξ(\eta) chosen as in
$$


$$
Lemma 4, we have that (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inˆBξ(\eta)(s∗
$$

1).


$$
Second, suppose that µt({\omegaR, \omegas∗
$$


$$
1}|ht) \leq1−\zeta(\eta) but µt(·|ht, Ω\{\omegaR}) \inCς(s∗
$$

1), for some


$$
ς > 0 fixed independent of \eta. Since ht \inHt
$$

\eta and µt(Ω\eta(s∗ 1)|ht) > µt(Ω\eta(s∗


$$
1) \ {\omegaR}) > 1 −\eta,
$$


$$
an argument identical to the proof of Lemma 4 implies that the minimum of µt(\omegaR|ht) and
$$


$$
||\sigma∗
$$


$$
1(ht) −s∗
$$

1|| is bounded above by a function that vanishes as \eta \to0. Thus, as \eta vanishes,


$$
d(\sigma∗
$$


$$
1(ht), conv({µt(·|ht, Ω\eta(s∗
$$


$$
1) \ {\omegaR}), s∗
$$


$$
1})) \leqϑ(ς, s∗
$$

1) where ϑ(·, ·) is defined in Lemma 8.


$$
Since µt(·|ht, Ω\{\omegaR}) \inCς(s∗
$$


$$
1), Lemma 8 then implies (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inB(s∗
$$

1) \subsetˆBξ(\eta)(s∗ 1).


$$
Third, suppose that µt({\omegaR, \omegas∗
$$


$$
1}|ht) \leq1 −\zeta(\eta) and µt(·|ht, Ω\ {\omegaR}) \inCς(s∗
$$

1). The former condition implies that µt(·|ht) satisfies Condition (1) of Definition 8, while the latter


$$
condition implies that it also satisfies Condition (2). Moreover, since µt(Ω\eta(s∗
$$


$$
1)|ht) \geq1 −\eta
$$


$$
(as t > ¯T(\eta)), it also satisfies Condition (3). Thus, by the definition of (\eta, ς)-confounding
$$


$$
weights, µt(\omegas∗
$$


$$
1|ht, Ω\ {\omegaR}) \leqcς,\eta. Now, since \omegas∗
$$


$$
1 \inΩ\eta(s∗
$$


$$
1) \ {\omegaR} \subsetΩ\ {\omegaR}, we have
$$


$$
µt(\omegas∗
$$


$$
1|ht, Ω\ {\omegaR}) = µt(\omegas∗
$$

1|ht, Ω\eta(s∗


$$
1) \ {\omegaR})µt(Ω\eta(s∗
$$


$$
1) \ {\omegaR}|ht).
$$


$$
Since µt(\omegas∗
$$


$$
1|ht, Ω\ {\omegaR}) \leqcς,\eta and µt(Ω\eta(s∗
$$


$$
1) \ {\omegaR}|ht) \geq1 −\eta, we have
$$


$$
µt(\omegas∗
$$

1|ht, Ω\eta(s∗


$$
1) \ {\omegaR}) \leq
$$

cς,\eta 1 −\eta. 33


Hence, the probability that h lies in this third case is at most


$$
q\eta,ς := Q
$$



$$
h \inH\infty: µt(\omegas∗
$$

1|ht, Ω\eta(s∗


$$
1) \ {\omegaR}) \leq
$$

c\eta,ς 1 −\eta ! . Thus, because µt(s∗ 1|ht, Ω\eta(s∗


$$
1) \ {\omegaR}) is a Q-submartingale, we have
$$

q\eta,ς c\eta,ς 1 −\eta !


$$
+ (1 −q\eta,ς)(1) \geqµ0(s∗
$$

1|Ω\eta(s∗


$$
1) \ {\omegaR})
$$

\Leftarrow\Rightarrow


$$
q\eta,ς \leqmin
$$

   1 −µ0(s∗ 1|Ω\eta(s∗


$$
1) \ {\omegaR})
$$

1 −c\eta,ς 1−\eta , 1  


$$
= 1 −\beta\eta,ς,
$$

completing the proof.


## B

Appendix: Omitted Proofs


## B.1

Proof of Lemma 2 For any two signal distributions p and q, let d(p||q) = R log (p/q) dp denote the relative entropy from q to p. By Lemma 4 of Gossner (2011) and a standard application of the chain rule for relative entropy,


## X

t EQ h


$$
d(p(\sigma∗
$$

0, s∗


$$
1, \sigma∗
$$


$$
2|ht)||p(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2|ht)) i


$$
\leq−log µ0(\omegas∗
$$

1). Hence, by Markov’s inequality,


## EQ

" # (


$$
t : d(p(\sigma∗
$$

0, s∗


$$
1, \sigma∗
$$


$$
2|ht)||p(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2|ht)) > \eta2 2 )#


$$
< −2 log µ0(\omegas∗
$$

1) \eta2 . On the other hand, by Pinsker’s inequality, d 


$$
p(\sigma∗
$$

0, s∗


$$
1, \sigma∗
$$

2|ht)



$$
p(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2|ht) 


$$
\leq\eta2
$$

2


$$
=\Rightarrowht \inHt
$$

\eta. This gives the desired bound. 34



## B.2

Proof of Lemma 3


$$
We first show that the desired conclusion holds for each \delta and each equilibrium, and then
$$


$$
show that ˆT can be fixed independent of the choice of \delta and the equilibrium.
$$


$$
Lemma 9. For any \delta < 1, any strategy profile (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$


$$
2) where (\sigma∗
$$


$$
0, \sigma∗
$$


$$
2) \inB1(s∗
$$

1)H (and


$$
hence, any Nash equilibrium), and any \zeta > 0, there exists a set of infinite histories G(\zeta) \subset
$$


$$
H\inftysatisfying Q(G(\zeta)) > 1 −\zeta and a period ˆT such that, for any h \inG(\zeta) and any t \geqˆT,
$$


$$
we have µt(·|h) \inM\zeta.
$$

Proof. Since Q is absolutely continuous relative to P and µt(·|h) is a martingale relative to


$$
P, µt(·|h) converges Q-almost surely to some limit distribution µ\infty(·|h) (e.g., Mailath and
$$


$$
Samuelson (2006), Lemma 15.4.2).
$$


$$
We show that, for Q-almost all histories h \inH\infty, µ\infty({\omegaR, \omegas∗
$$

1}|h) = 1. Suppose that


$$
µ\infty(Ω\ {\omegaR}|h) > 0, let \omegas1 \inΩ\ {\omegaR} satisfy µ\infty(\omegas1|h) > 0, and let c > 0 and T satisfy
$$


$$
µt(\omegas1|h) > c for all t > T. Suppose also that the set of signals y1 that realize infinitely often
$$

in h is precisely Y ∗


$$
1 = supp(\rho(·|s∗
$$

1(Y0))), the set of signals that arise with positive probability when player 1 plays s∗


## 1. This supposition is without loss as \rho(·|a0) has full support, so such


$$
histories occur Q-almost surely. Next, for any Ω′ \subseteqΩ\ {\omegaR}, let pY1(\sigma∗
$$

0, ˜s1|ht, Ω′) denote the


$$
equilibrium distribution of y1 conditional on reaching history ht and the event \omega \inΩ′; when
$$


$$
Ω′ is a singleton, Ω′ = {ˆs1}, we write this as pY1(\sigma∗
$$


$$
0, ˆs1|ht). Then, for any y1 \inY ∗
$$

1 , we have


$$
µt+1(\omegas1|Ω\ {\omegaR}, ht, y1) −µt(\omegas1|Ω\ {\omegaR}, ht)
$$



$$
=
$$



$$
pY1(\sigma∗
$$


$$
0, s1|ht)[y1]µt(\omegas1|Ω\ {\omegaR}, ht)
$$


$$
pY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR})[y1]
$$


$$
−µt(\omegas1|Ω\ {\omegaR}, ht)
$$



$$
=
$$


$$
µt(\omegas1|Ω\ {\omegaR}, ht)
$$


$$
pY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR})[y1]
$$


$$
pY1(\sigma∗
$$


$$
0, s1|ht)[y1] −pY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR})[y1]
$$


>c


$$
pY1(\sigma∗
$$


$$
0, s1|ht)[y1] −pY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR})[y1]
$$

. Since µt(·|h) converges, y1 realizes infinitely often, and c > 0, this implies


$$
lim
$$


$$
t\to\infty
$$


$$
pY1(\sigma∗
$$


$$
0, s1|ht)[y1] −pY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR})[y1]
$$


$$
= 0.
$$


$$
At the same time, applying the argument in Lemma 2 conditional on the event \omega \neq \omegaR
$$


$$
implies that, for Q-almost all histories h \inH\infty,
$$


$$
lim
$$


$$
t\to\infty
$$



$$
pY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR}) −pY1(\sigma∗
$$

0, s∗ 1|ht)



$$
= 0.
$$

35



$$
In particular, since pY1(\sigma∗
$$

0, s∗


$$
1|ht)[y1] = 0 for all y1 /\inY ∗
$$


$$
1 , this implies that, for all y1 /\inY ∗
$$

1 ,


$$
lim
$$


$$
t\to\inftypY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR})[y1] = 0.
$$


$$
Since we have already shown that pY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR})[y1] and pY1(\sigma∗
$$

0, s1|ht)[y1] have the


$$
same limit for all y1 \inY ∗
$$

1 , we have


$$
lim
$$


$$
t\to\infty
$$


$$
pY1(\sigma∗
$$


$$
0, s1|ht) −pY1(\sigma∗
$$


$$
0, ˜s1|ht, Ω\ {\omegaR})
$$


$$
= 0.
$$

Thus, by the triangle inequality,


$$
lim
$$


$$
t\to\infty
$$



$$
pY1(\sigma∗
$$


$$
0, s1|ht) −pY1(\sigma∗
$$

0, s∗ 1|ht)



$$
= 0.
$$


$$
Finally, since \omegas1 \inΩand s∗
$$

1 is not behaviorally confounded, this implies that s1 = s∗ 1, and


$$
hence µ\infty({\omegaR, \omegas∗
$$


$$
1}|h) = 1.
$$

To complete the proof, recall that Egorov’s theorem shows that if a sequence of functions


$$
fn : H\infty\toR converges Q-almost surely to f, then for all \zeta > 0, there exists G(\zeta) \subsetH\infty
$$


$$
satisfying µ(G(\zeta)) \geq1 −\zeta such that fn \tof uniformly on G(\zeta). Thus, Lemma 9 follows
$$


$$
from Egorov’s theorem applied to the sequence of conditional beliefs µt({\omegas∗
$$


$$
1, \omegaR}|h) and the
$$

definition of uniform convergence.


$$
We now show that ˆT can be chosen as a function only of \zeta and not of \delta or the equilibrium
$$


$$
strategies. To this end, let Q\sigma0,\sigma2 be the probability measure on H\inftyinduced by strategies
$$


$$
(\sigma0, s∗
$$


$$
1, \sigma2), and let µ\sigma0,\sigma2
$$

t


$$
(\omegas∗
$$


$$
1|Ω\ {\omegaR}, ht) be the conditional belief that the long-run player
$$


$$
is of type \omegas∗
$$

1 conditional on being irrational. This is well-defined because, conditional on the


$$
event Ω\{\omegaR}, the rational long-run player’s strategy does not affect µ\sigma0,\sigma2
$$

t


$$
once (\sigma0, \sigma2) are
$$


$$
given. Next, let L\sigma0,\sigma2 \subsetH\inftybe the set of all histories h where µ\sigma0,\sigma2
$$

t


$$
(\omegas∗
$$


$$
1|Ω\ {\omegaR}, ht) \to1
$$


$$
as t \to\infty. By Lemma 9, Q\sigma0,\sigma2 (L\sigma0,\sigma2) = 1 for all (\sigma0, \sigma2) \inB1(s∗
$$


## 1)H.

We show that B1(s∗ 1)H is compact in an appropriate topology. Endow B1(s∗ 1)H with the topology induced by the metric


$$
d((\sigma0, \sigma2), (\sigma′
$$


$$
0, \sigma′
$$


$$
2)) = sup
$$


$$
h\inH
$$


$$
( \infty
$$


## X


$$
t=0
$$

1


$$
2t||(\sigma0(ht), \sigma2(ht)) −(\sigma′
$$


$$
0(ht), \sigma′
$$


$$
2(ht))||
$$

) .


$$
This is the sup-norm over undominated short-run player strategies (\sigma0, \sigma2) : H \toB1(s∗
$$

1). 36



$$
Endowing H\inftywith the product topology, we have that H is a dense subset of H\infty25. We can
$$

thus continuously extend B1(s∗ 1)H to the larger space B1(s∗


$$
1)H\infty, that is, the space B1(s∗
$$


$$
1)H\infty
$$


$$
is the set of all continuous functions from infinite sequences of signals H\inftyinto sequences of
$$

strategies B1(s∗


$$
1)\inftyunder the sup norm. Thus, since H\inftyhas countable dense subset H, a
$$

standard diagonalization argument implies that the space (B1(s∗


$$
1)H\infty, d) is compact.
$$


$$
We are now ready to prove that ˆT(\zeta, \sigma∗
$$


$$
0, \sigma∗
$$

2) can be chosen independent of the choice of


$$
(\sigma∗
$$


$$
0, \sigma∗
$$


$$
2) (and hence also independent of \delta). Suppose for contradiction that there exists \zeta > 0
$$


$$
such that for each T \inN, there exist (\sigmaT
$$


$$
0 , \sigmaT
$$


$$
2 ) \inB1(s∗
$$


$$
1)H and a set of histories ET(\zeta) \subsetH\infty
$$


$$
such that Q\sigmaT
$$


$$
0 ,\sigmaT
$$


$$
2 (ET(\zeta)) > \zeta but µT(·|h) \inM\zeta for all h \inET(\zeta). Taking a subsequence if nec-
$$

essary and using compactness of B1(s∗


$$
1)H, we have (\sigmaT
$$


$$
0 , \sigmaT
$$


$$
2 ) \to(\sigma\infty
$$


$$
0 , \sigma\infty
$$


$$
2 ) \inB1(s∗
$$

1)H. Since µT depends only on the history up to time T, this implies that Q


$$
\sigmaT
$$


$$
0 ,\sigmaT
$$

2


## T ′


$$
(ET(\zeta)) > \zeta for all T ′ \geqT.
$$


$$
Thus, since QT ′ is continuous in strategies as a finite-dimensional measure, passing (\sigmaT
$$


$$
0 , \sigmaT
$$

2 )


$$
to the limit (while fixing the time T ′ and the set of histories ET(\zeta)) gives Q
$$


$$
\sigma\infty
$$


$$
0 ,\sigma\infty
$$

2


## T ′

(ET(\zeta)) > \zeta


$$
for all T ′ sufficiently large; and then taking T ′ \to\inftygives Q\sigma\infty
$$


$$
0 ,\sigma\infty
$$

2 (ET(\zeta)) > \zeta. As this holds


$$
for all T, we have a sequence of events {ET(\zeta)}T\inN such that Q\sigma\infty
$$


$$
0 ,\sigma\infty
$$

2 (ET(\zeta)) > \zeta for all T. From here, we can conclude26


$$
Q\sigma\infty
$$


$$
0 ,\sigma\infty
$$

2



$$
lim sup
$$


$$
T\to\inftyET(\zeta)
$$

!


$$
\geqlim sup
$$


$$
n\to\infty
$$

Pn


$$
k=1 Q\sigma\infty
$$


$$
0 ,\sigma\infty
$$

2 (Ek(\zeta)) 2


## P


$$
1\leqj,k\leqT ′ Q\sigma\infty
$$


$$
0 ,\sigma\infty
$$


$$
2 (Ej(\zeta) \capEk(\zeta)) \geqn2\zeta2
$$

n2


$$
= \zeta2.
$$


$$
Thus, for any history h \inlim supT\to\inftyET(\zeta), there is a sequence of times {Tn} such that
$$


$$
µTn(·|h) /\inM\zeta for all n. Since \zeta2 < \zeta, this implies that µTn(·|h) \neq M\zeta2. Thus, for any h \in
$$


$$
E\infty(\zeta), µt(·|h) /\inM\zeta2 for infinitely many T; but Q\sigma\infty
$$


$$
0 ,\sigma\infty
$$


$$
2 (E\infty(\zeta)) > \zeta2. But this contradicts
$$


$$
Lemma 9 for the strategies (\sigma\infty
$$


$$
0 , \sigma\infty
$$


$$
2 ) \inB1(s∗
$$

1)H, completing the proof.


## B.3

Proof of Lemma 4


$$
Note that if ht \inHt
$$


$$
\eta and µt(·|ht) \inM0 then
$$


$$
|µt(\omegaR|ht)|
$$



$$
p(\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
1(ht, \omegaR), \sigma∗
$$


$$
2(ht)) −p(\sigma∗
$$

0, s∗


$$
1, \sigma∗
$$

2|ht)


< \eta


$$
and (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inB\eta(s∗
$$


$$
1). Thus, since p(\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
1, \sigma∗
$$

2(ht)) is continuous in µt(·|ht), there


$$
exists a strictly positive function \zeta(\eta) satisfying lim\eta\to0 \zeta(\eta) = 0 such that if ht \inHt
$$

\eta and


$$
25Formally, H = S
$$


$$
t Ht is isomorphic to the set of finite cylinders that generate H\infty.
$$

26This is a consequence of the Kochen-Stone Theorem; see, for example, Theorem 1.3 of Arthan and Oliva (2021). We thank Eric Gao for pointing us to this result. 37



$$
µt(·|ht) \inM\zeta(\eta) then
$$


$$
|µt(\omegaR|ht)|
$$



$$
p(\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
1(ht, \omegaR), \sigma∗
$$


$$
2(ht)) −p(\sigma∗
$$


$$
0(ht), s∗
$$


$$
1, \sigma∗
$$


$$
2(ht))
$$


< 2\eta


$$
and (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inB2\eta(s∗
$$

1).


$$
Now fix any c > 0. If µt(\omegaR|ht) \geqc then
$$



$$
p(\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
1(ht, \omegaR), \sigma∗
$$


$$
2(ht)) −p(\sigma∗
$$


$$
0(ht), s∗
$$


$$
1, \sigma∗
$$


$$
2(ht))
$$


< 2\eta c .


$$
Hence, as \eta \to0, Lemma 1 implies that ||\sigma∗
$$


$$
1(ht, \omegaR) −s∗
$$


$$
1||\to0, and hence (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \in
$$

ˆBξ1(\eta)(s∗


$$
1) for some strictly positive function ξ1(\eta) satisfying ξ1(\eta) \to0. If instead µt(\omegaR|ht) <
$$


$$
c then ||\sigma∗
$$


$$
1(ht) −s∗
$$


$$
1||\leq1 −\zeta(\eta) −c, and hence (\sigma∗
$$


$$
0(ht), \sigma∗
$$


$$
2(ht)) \inˆB\zeta(\eta)+c(s∗
$$


$$
1). Taking ξ(\eta) =
$$

max{ξ1(\eta), \zeta(\eta) + c} completes the proof.


## B.4

Proof of Proposition 5


$$
Let \gamma be feasible in OT(\rho, ϕ) and supp(\gamma) not strictly u-CM. Let {(xi, yi)N
$$


$$
i=1} \subsetsupp(\gamma)
$$


$$
be a collection of pairs witnessing a violation and set \varepsilon = mini \gamma((xi, yi)). Define \gamma′ \in
$$

\Delta(X \times Y ) by


$$
\gamma′(x, y) =
$$

          


$$
\gamma(x, y) −\varepsilon
$$


$$
if (x, y) \in
$$

n


$$
(xi, yi)N
$$


$$
i=1
$$

o \ n (xi, yi+1)N


$$
i=1
$$

o ,


$$
\gamma(x, y) + \varepsilon
$$


$$
if (x, y) \in
$$

n (xi, yi+1)N


$$
i=1
$$

o \ n


$$
(xi, yi)N
$$


$$
i=1
$$

o ,


$$
\gamma(x, y)
$$

otherwise.


$$
Then \gamma′ \neq \gamma is feasible in OT(\rho, ϕ) and
$$


$$
R u(x, y)d\gamma \leq
$$


$$
R u(x, y)d\gamma′ (since {(xi, yi)N
$$


$$
i=1} wit-
$$


$$
nesses a violation of strict u-cyclical monotonicity), so \gamma does not uniquely solve OT(\rho, ϕ).
$$


$$
Conversely, if \gamma is feasible in OT(\rho, ϕ) and strictly u-cyclically monotone, consider any
$$


$$
\gamma′ \neq \gamma that is feasible in OT(\rho, ϕ). Since \gamma and \gamma′ are both feasible in OT(\rho, ϕ) and \gamma \neq \gamma′,
$$


$$
there exists {(xi, yi)N
$$


$$
i=1} \subsetsupp(\gamma) such that {(xi, yi+1)N
$$


$$
i=1} \subsetsupp(\gamma′). (To see this, let
$$


$$
(x1, y1) be any pair such that \gamma(x1, y1) > \gamma′(x1, y1). Since \gamma and \gamma′ transport the same mass
$$


$$
into y1, there exists x2 such that \gamma(x2, y1) < \gamma′(x2, y1). But now, since \gamma and \gamma′ transport
$$


$$
the same mass out of x2, there exists y2 such that \gamma(x2, y2) > \gamma′(x2, y2). Continuing in this
$$

38



$$
manner and using finiteness of X \times Y yields a cycle.) Let \varepsilon = mini \gamma′(xi, yi+1), and let
$$


$$
\gamma′′(x, y) =
$$

          


$$
\gamma′(x, y) −\varepsilon
$$


$$
if (x, y) \in
$$

n (xi, yi+1)N


$$
i=1
$$

o \ n


$$
(xi, yi)N
$$


$$
i=1
$$

o ,


$$
\gamma′(x, y) + \varepsilon
$$


$$
if (x, y) \in
$$

n


$$
(xi, yi)N
$$


$$
i=1
$$

o \ n (xi, yi+1)N


$$
i=1
$$

o ,


$$
\gamma′(x, y)
$$

otherwise.


$$
Then \gamma′′ is feasible in OT(\rho, ϕ) and
$$


$$
R u(x, y)d\gamma′′ >
$$


$$
R u(x, y)d\gamma′ (since
$$

n


$$
(xi, yi)N
$$


$$
i=1
$$

o is contained


$$
in the strictly u-cyclically monotone set supp(\gamma)), so \gamma′ does not solve OT(\rho, ϕ). Thus, since
$$


$$
no \gamma′ \neq \gamma solves OT(\rho, ϕ), and OT(\rho, ϕ) has a solution as a continuous maximization problem
$$


$$
over a compact set, \gamma must uniquely solve OT(\rho, ϕ).
$$


## B.5

Proof of Proposition 6 The result is obvious if ¯vCM 1


$$
\geq¯u1, so suppose ¯vCM
$$

1


$$
< ¯u1, and fix \varepsilon < 2(¯u1 −¯vCM
$$

1 ), a prior


$$
µ0 with µ0(\omegaR) > 0, and an equilibrium (\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$

2). We start with an additional lemma. Lemma 10. For all ξ > 0, there exists ς > 0 such that, for any u1-cyclically monotone strategy s1, any strategy s′ 1 satisfying ||s1 −s′


$$
1||< ς, and any (\alpha0, \alpha2) \inB(s1), we have
$$


$$
u1(\alpha0, s1, \alpha2) < ¯vCM
$$

1 + ξ. Proof. Suppose for contradiction that there exists \varepsilon > 0 and a sequence of strategies ˜sn 1, each within 1/n of a u1-cyclically monotone strategy sn


$$
1, and (\alphan
$$


$$
0, \alphan
$$


$$
2) \inB(˜sn
$$

1) such that


$$
u1(\alphan
$$

0, sn


$$
1, \alphan
$$

2) > ¯vCM 1 + ξ. Taking a subsequence if necessary and noting that the set of u1-cyclically monotone strategies is closed (as they are characterized by their support), sn 1 converges to a u1-cyclically monotone strategy s1. Moreover, ˜sn 1 also converges to s1, by the triangle inequality. But this yields a contradiction, as ¯vCM 1


$$
+ ξ \leqlim sup
$$


$$
n\to\inftyu1(\alphan
$$

0, ˜sn


$$
1, \alphan
$$


$$
2) \leq
$$


$$
sup
$$


$$
(\alpha0,\alpha2)\inB(s1)
$$


$$
u1(\alpha0, s1, \alpha2) \leq¯vCM
$$

1 , where the second inequality follows because B(·) is upper hemi-continuous and u1 is contin- uous, and the third inequality follows because s1 is u1-cyclically monotone.


$$
Now, note that at any history ht where µt(\omegaR|ht) > 1−ς, we have ||\sigma∗
$$


$$
1(ht)−\sigma∗
$$


$$
1(ht, \omegaR)||<
$$


$$
ς. Thus, by Lemmas 5 and 10, there exists ς > 0 such that at any history ht where µt(\omegaR|ht) >
$$

39



$$
1 −ς, we have u1(\sigma∗
$$


$$
0, \sigma∗
$$


$$
1, \sigma∗
$$


$$
2|ht, \omegaR) < ¯vCM
$$

1


$$
+ \varepsilon/2. Since µt(\omegaR|ht, \omegaR) is a P-submartingale,
$$


$$
(1 −P(µt(\omegaR|ht, \omegaR) > 1 −ς))(1 −ς) + P(µt(\omegaR|ht, \omegaR) > 1 −ς)(1) \geqµ0(\omegaR)
$$

\Leftarrow\Rightarrow


$$
P(µt(\omegaR|ht, \omegaR) > 1 −ς) \geq1 −1 −µ0(\omegaR)
$$

ς . Therefore, the long-run player’s expected payoff in each period t is at most



$$
1 −1 −µ0(\omegaR)
$$

ς !  ¯vCM 1 + \varepsilon 2 


$$
+ 1 −µ0(\omegaR)
$$

ς ¯u1. This payoff is less than ¯vCM 1 + \varepsilon whenever


$$
µ0(\omegaR) > 1 −
$$

\varepsilonς 2(¯u1 −¯vCM 1 ) −\varepsilon, completing the proof.


## B.6

Proof of Proposition 9 Suppose that s1 : \Theta \to\Delta(R) is monotone with respect to (\succeq\Theta, \succeqR).


$$
First, G(s1) cannot contain a cycle (\theta1, r1), (\theta2, r1), . . . , (\thetaK, rK), (\theta1, rK). To see this, sup-
$$


$$
pose otherwise, and let \theta1 \prec. . . \prec\thetaK, without loss. Since rk \insupp(s1(\thetak))\capsupp(s1(\thetak+1))
$$


$$
for k \in{1, . . . , K −1} and rK \insupp(s1(\thetaK)), monotonicity requires r1 \prec. . . \precrK. But
$$


$$
this gives a contradiction, since rK \insupp(s1(\theta1)) and r1 \insupp(s1(\theta2)).
$$

Next, G(s1) cannot contain a forbidden triple. We have already explained why it cannot contain a Type (1) forbidden triple. The argument for why it cannot contain a Type (2) forbidden triple is identical, with the roles of states and actions interchanged. Conversely, suppose that G(s1) is acyclic and does not contain a forbidden triple. It suffices to consider the case where G(s1) is connected, as otherwise the orders on the states and actions in each connected component of G(s1) can be appended to one another. So


$$
suppose that G(s1) is connected, and let (\theta1, r1), (\theta2, r1), . . . , (\thetaK, rK) be any maximum path
$$

in G(s1) (i.e., any path of maximum length), supposing that such a path ends with an action. (The argument for the case where all maximum paths both start and end at actions or at


$$
states is almost identical.) Define the orders \prec\Theta on {\theta1, . . . , \thetaK} and \precR on {r1, . . . , rK} by
$$


$$
\theta1 \prec\Theta . . . \prec\Theta \thetaK and r1 \precR . . . \precR rK.
$$


$$
We claim that for any \theta \in\Theta \ {\theta1, . . . , \thetaK}, there exists k \in{1, . . . , K −1} such that
$$

40



$$
supp(s1(\theta)) = {rk}. Note such a state \theta is linked to at most one rk \in{r1, . . . , rK−1}, as if \theta is
$$

linked to distinct rk, r′


$$
k then appending \theta to both ends of the path from rk to r′
$$

k forms a cycle.


$$
In addition, \theta cannot be linked to rK, as then it could be appended to the maximum path.
$$


$$
Finally, \theta cannot be linked to both some rk \in{r1, . . . , rK−1} and some r \inR\{r1, . . . , rK−1}.
$$


$$
For, if k = 1 then replacing (\theta1, r1) with (\theta, r), (\theta, r1) at the beginning of the maximum
$$


$$
path would lengthen it; and if k \geq2 then the set of states {\thetak, \theta, \thetak+1} together with the
$$


$$
set of actions {r, rk−1, rk, rk+1} would be a forbidden triple, as {rk−1, rk} \insupp(s1(\thetak)),
$$


$$
{r, rk} \insupp(s1(\theta)), and {rk, rk+1} \insupp(s1(\thetak+1)) (see Figure 2).
$$


$$
\theta1
$$


$$
\theta2
$$


$$
\theta
$$


$$
\theta3
$$

r1 r2 r3 r \Theta


## R


$$
\theta1
$$


$$
\theta2
$$


$$
\theta
$$


$$
\theta3
$$

r1 r2 r3 r \Theta


## R


$$
Figure 2: Each State \theta /\in{\theta1, . . . , \thetaK} Has Only One Neighbor
$$


$$
Notes. If \theta /\in{\theta1, . . . , \thetaK} is linked to rk \in{r1, . . . , rK} and r /\in{r1, . . . , rK}, then
$$


$$
{\thetak, \theta, \thetak+1} together with {r, rk−1, rk, rk+1} is a forbidden triple.
$$


$$
Given this claim, we can extend \prec\Theta to \Theta by ordering each \theta \in\Theta\{\theta1, . . . , \thetaK} such that
$$


$$
supp(s1(\theta)) = {rk} in between \thetak and \thetak+1 (and ordering multiple such states arbitrarily
$$


$$
between \thetak and \thetak+1).
$$


$$
Similarly, for any r \inR \ {r1, . . . , rK}, there exists k \in{2, . . . , K} such that rk is linked
$$


$$
only to \thetak in G(s1). Extend \precR to R by ordering each such r in between rk−1 and rk.
$$


$$
Note that for any k \geq2 and any r \insupp(s1(\thetak)), we have rk−1 ≾R r ≾R rk. This follows
$$


$$
because if r /\in{r1, . . . , rK} then rk−1 ≾R r ≾R rk by construction, and if r = r˜k for some
$$


$$
˜k /\in{k −1, k}, then G(s1) contains a cycle starting with (\thetak, r˜k) and then following the
$$


$$
maximum path back to \thetak.
$$


$$
Finally, we claim that s1 is monotone with respect to (\succeq\Theta, \succeqR). To see this, fix any
$$


$$
\theta \succ\Theta \theta′. Let ˜k = max{k : \theta \succeq\Theta \thetak}. If \theta \succ\Theta \theta˜k \succeq\Theta \theta′, then supp(s1(\theta)) = {r˜k} and r˜k \succeqR r
$$

41



$$
for all r \insupp(s1(\theta′)). If \theta = \theta˜k \succ\Theta \theta′, then r\theta˜k−1 is the lowest action in supp(s1(\theta)),
$$


$$
and no action in supp(s1(\theta′)) is above r\theta˜k−1. Lastly, if \theta \succ\Theta \theta′ \succeq\Theta \theta˜k, then supp(s1(\theta)) =
$$


$$
supp(s1(\theta′)) = {r˜k}. Thus, in all cases, monotonicity holds.
$$

References Acemoglu, Daron, and Alexander Wolitzky. 2024. “Mistrust, Misperception, and Mis- understanding: Imperfect Information and Conflict Dynamics.” Handbook of the Economics of Conflict. Arieli, Itai, Yakov Babichenko, Rann Smorodinsky, and Takuro Yamashita. 2023.


$$
“Optimal Persuasion via Bi-Pooling.” Theoretical Economics 18 (1): 15–36.
$$

Arthan, Rob, and Paulo Oliva. 2021. “On the Borel-Cantelli Lemmas, the Erdős–Rényi Theorem, and the Kochen-Stone Theorem.” Journal of Logic and Analysis 13 (6): . Avenhaus, Rudolf, Bernhard von Stengel, and Shmuel Zamir. 2002. “Inspection Games.” In Handbook of Game Theory with Economic Applications, Volume 3. Chap. 51 1947–1987, Elsevier. Ball, Ian, and Deniz Kattwinkel. 2024. “Quota Mechanisms: Finite-Sample Optimality and Robustness.” Working Paper. Battigalli, Pierpaolo, and Joel Watson. 1997. “On “reputation” refinements with het- erogeneous beliefs.” Econometrica 369–374. Best, James, and Daniel Quigley. 2024. “Persuasion for the Long Run.” Journal of


$$
Political Economy 132 (5): 1305–1337.
$$

Chakraborty, Archishman, and Rick Harbaugh. 2010. “Persuasion by Cheap Talk.”


$$
American Economic Review 100 (5): 2361–2382.
$$

Chen, Ying, Navin Kartik, and Joel Sobel. 2008. “Selecting cheap-talk equilibria.”


$$
Econometrica 76 (1): 117–136.
$$

Clark, Daniel, Drew Fudenberg, and Alexander Wolitzky. 2021. “Record-Keeping and Cooperation in Large Societies.” The Review of Economic Studies 88 (5): 2179–2209. 42


Dworczak, Piotr, and Giorgio Martini. 2019. “The simple economics of optimal per-


$$
suasion.” Journal of Political Economy 127 (5): 1993–2048.
$$

Ely, Jeffrey, Drew Fudenberg, and David K Levine. 2008. “When is reputation bad?”


$$
Games and Economic Behavior 63 (2): 498–526.
$$

Ely, Jeffrey, and Juuso Valimaki. 2003. “Bad Reputation.” Quarterly Journal of Eco-


$$
nomics 118 (3): 785–814.
$$

Escobar, Juan F., and Juuso Toikka. 2013. “Efficiency in Games with Markovian Private


$$
Information.” Econometrica 81 (5): 1737–1767.
$$

Frankel, Alexander. 2014. “Aligned Delegation.” American Economic Review 104 (1): 66– 83. Fudenberg, Drew, Ying Gao, and Harry Pei. 2022. “A Reputation for Honesty.” Journal of Economic Theory 204 105508. Fudenberg, Drew, and David Levine. 1989. “Reputation and Equilibrium Selection in Games with a Patient Player.” Econometrica 57 (4): 759–778. Fudenberg, Drew, and David Levine. 1992. “Maintaining a Reputation when Strategies are Imperfectly Observed.” Review of Economic Studies 59 (3): 561–579. Gossner, Olivier. 2011. “Simple Bounds on the Value of a Reputation.” Econometrica 79


$$
(5): 1627–1641.
$$

Heller, Yuval, and Erik Mohlin. 2018. “Observations on Cooperation.” The Review of


$$
Economic Studies 85 (4): 2253–2282.
$$

Jackson, Matthew O., and Hugo F. Sonnenschein. 2007. “Overcoming Incentive Con-


$$
straints by Linking Decisions.” Econometrica 75 (1): 241–257.
$$

Kamenica, Emir, and Matthew Gentzkow. 2011. “Bayesian Persuasion.” American


$$
Economic Review 101 (6): 2590–2615.
$$

Kartik, Navin. 2009. “Strategic communication with lying costs.” The Review of Economic


$$
Studies 76 (4): 1359–1395.
$$

Kleiner, Andreas, Benny Moldovanu, and Philipp Strack. 2021. “Extreme Points


$$
and Majorization: Economic Applications.” Econometrica 89 (5): 1671–1700.
$$

43


Kolotilin, Anton. 2018. “Optimal information disclosure: A linear programming approach.”


$$
Theoretical Economics 13 (2): 607–635.
$$

Kuvalekar, Aditya, Elliot Lipnowski, and Joao Ramos. 2022. “Goodwill in commu- nication.” Journal of Economic Theory 203 105467. Lin, Xiao, and Ce Liu. 2024. “Credible Persuasion.” Journal of Political Economy 132


$$
(7): .
$$

Liu, Qingmin. 2011. “Information acquisition and reputation dynamics.” The Review of


$$
Economic Studies 78 (4): 1400–1425.
$$

Liu, Qingmin, and Andrzej Skrzypacz. 2014. “Limited Records and Reputation Bub- bles.” Journal of Economic Theory 151 2–29. Mailath, George J., and Larry Samuelson. 2006. Repeated Games and Reputations: Long-Run Relationships. Oxford University Press.


$$
Margaria, Chiara, and Alex Smolin. 2018. “Dynamic Communication with Biased
$$

Senders.” Games and Economic Behavior 110 330–339. Mathevet, Laurent, David Pearce, and Ennio Stacchetti. 2024. “Reputation and Information Design.” Working Paper. Matsushima, Hitoshi, Koichi Miyazaki, and Nobuyuki Yagi. 2010. “Role of Linking Mechanisms in Multitask Agency with Hidden Information.” Journal of Economic Theory


$$
145 (6): 2241–2259.
$$

Meng, Delong. 2021. “On the value of repetition for communication games.” Games and Economic Behavior 127 227–246. Morris, Stephen. 2001. “Political correctness.” Journal of Political Economy 109 (2): 231– 265. Myerson, Roger B. 1982. “Optimal coordination mechanisms in generalized principal–


$$
agent problems.” Journal of mathematical economics 10 (1): 67–81.
$$

Pei, Harry. 2020. “Reputation Effects Under Interdependent Values.” Econometrica 88 (5): 1671–1700. 44


Pei, Harry. 2023. “Repeated Communication with Private Lying Costs.” Journal of Eco- nomic Theory 210 105668. Pei, Harry. 2024. “Reputation Effects under Short Memories.” Journal of Political Economy


$$
132 (10): .
$$

Rahman, David M. 2024. “Detecting Profitable Deviations.” Journal of Mathematical Economics 111 102946. Rayo, Luis, and Ilya Segal. 2010. “Optimal Information Disclosure.” Journal of Political


$$
Economy 118 (5): 949–987.
$$

Renault, Jérôme, Eilon Solan, and Nicolas Vieille. 2013. “Dynamic Sender–Receiver


$$
Games.” Journal of Economic Theory 148 (2): 502–534.
$$

Rochet, Jean-Charles. 1987. “A Necessary and Sufficient Condition for Rationalizability in a Quasi-Linear Context.” Journal of Mathematical Economics 16 (2): 191–200. Santambrogio, Filippo. 2015. “Optimal transport for applied mathematicians.” Birkäuser,


## NY 55 (58-63): 94.

Schelling, Thomas C. 1966. Arms and Influence. Chap. 1 74, The Henry L. Stimson Lectures Series, Yale University Press. Sorin, Sylvain. 1999. “Merging, Reputation, and Repeated Games with Incomplete Infor- mation.” Games and Economic Behavior 29 274–308. Spence, Michael. 1973. “Job Market Signaling.” The Quarterly Journal of Economics 87


$$
(3): 355–374.
$$

Takahashi, Satoru. 2010. “Community enforcement when players observe partners’ past


$$
play.” Journal of Economic Theory 145 (1): 42–62.
$$

Watson, Joel. 1993. “A “reputation” refinement without equilibrium.” Econometrica 199– 205. 45

