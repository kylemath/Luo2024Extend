"""
C02 Verification: Counterexample showing V_Markov > V is possible.

The paper claims V_Markov <= V in general. We construct explicit counterexamples
and verify the paper's baseline parameters DO satisfy V_Markov <= V.
"""

import numpy as np


def compute_payoffs(alpha, beta, mu_star, u_coop, u_defect_G, u_defect_B):
    """
    Compute V(s1*) and V_Markov(s1*) for a deterrence game.

    Parameters
    ----------
    alpha : float
        P(B|G) transition probability
    beta : float
        P(G|B) transition probability
    mu_star : float
        SR threshold: SR cooperates iff P(G) >= mu_star
    u_coop : float
        LR payoff when SR cooperates (state-independent for simplicity)
    u_defect_G : float
        LR payoff when SR defects in state G
    u_defect_B : float
        LR payoff when SR defects in state B

    Returns
    -------
    dict with V, V_Markov, and diagnostics
    """
    pi_G = beta / (alpha + beta)
    pi_B = alpha / (alpha + beta)
    F_G_given_G = 1 - alpha
    F_G_given_B = beta

    # i.i.d. case: SR sees pi(G) and decides
    if pi_G >= mu_star:
        sr_iid = "cooperate"
        V = u_coop
    else:
        sr_iid = "defect"
        V = pi_G * u_defect_G + pi_B * u_defect_B

    # Markov case: SR sees F(G|theta_{t-1}) and decides per state
    if F_G_given_G >= mu_star:
        sr_after_G = "cooperate"
        payoff_after_G = u_coop
    else:
        sr_after_G = "defect"
        payoff_after_G = pi_G * u_defect_G + pi_B * u_defect_B  # simplified

    if F_G_given_B >= mu_star:
        sr_after_B = "cooperate"
        payoff_after_B = u_coop
    else:
        sr_after_B = "defect"
        payoff_after_B = pi_G * u_defect_G + pi_B * u_defect_B  # simplified

    # For a proper V_Markov, we need per-state payoffs.
    # Under state-contingent SR behavior, the expected payoff is:
    # V_Markov = pi(G) * [payoff when prev state G] + pi(B) * [payoff when prev state B]
    # where "payoff when prev state theta'" = E[u1(theta_t, s1*(theta_t), a2(theta'))
    #                                             | theta_{t-1} = theta']

    # Simplified: if SR cooperates, LR gets u_coop regardless of state.
    # If SR defects, LR gets E[u_defect | theta_{t-1}].

    if sr_after_G == "cooperate":
        exp_payoff_after_G = u_coop
    else:
        # Expected payoff when SR defects, conditional on theta_{t-1} = G
        exp_payoff_after_G = F_G_given_G * u_defect_G + (1 - F_G_given_G) * u_defect_B

    if sr_after_B == "cooperate":
        exp_payoff_after_B = u_coop
    else:
        exp_payoff_after_B = F_G_given_B * u_defect_G + (1 - F_G_given_B) * u_defect_B

    V_Markov = pi_G * exp_payoff_after_G + pi_B * exp_payoff_after_B

    return {
        'alpha': alpha, 'beta': beta,
        'pi_G': pi_G, 'pi_B': pi_B,
        'F_G_given_G': F_G_given_G, 'F_G_given_B': F_G_given_B,
        'mu_star': mu_star,
        'sr_iid': sr_iid,
        'sr_after_G': sr_after_G, 'sr_after_B': sr_after_B,
        'V': V, 'V_Markov': V_Markov,
        'V_Markov_leq_V': V_Markov <= V + 1e-12,
        'gap': V - V_Markov
    }


print("=" * 75)
print("C02 VERIFICATION: V_Markov vs V ordering")
print("=" * 75)

# ---- Paper's baseline parameters ----
print("\n--- Paper's Baseline Parameters ---")
result = compute_payoffs(
    alpha=0.3, beta=0.5, mu_star=0.60,
    u_coop=1.0, u_defect_G=0.3, u_defect_B=0.3
)
print(f"alpha={result['alpha']}, beta={result['beta']}")
print(f"pi(G) = {result['pi_G']:.4f}")
print(f"F(G|G) = {result['F_G_given_G']:.4f}, F(G|B) = {result['F_G_given_B']:.4f}")
print(f"mu* = {result['mu_star']}")
print(f"SR under i.i.d.: {result['sr_iid']} (pi(G)={result['pi_G']:.3f} vs mu*={result['mu_star']})")
print(f"SR after G: {result['sr_after_G']} (F(G|G)={result['F_G_given_G']:.3f} vs mu*={result['mu_star']})")
print(f"SR after B: {result['sr_after_B']} (F(G|B)={result['F_G_given_B']:.3f} vs mu*={result['mu_star']})")
print(f"V(s1*) = {result['V']:.4f}")
print(f"V_Markov(s1*) = {result['V_Markov']:.4f}")
print(f"V_Markov <= V? {result['V_Markov_leq_V']}")
print(f"Gap V - V_Markov = {result['gap']:.4f}")

# ---- Counterexample: V_Markov > V ----
print("\n--- Reviewer's Counterexample: pi(G) < mu* ---")
result2 = compute_payoffs(
    alpha=0.6, beta=0.3, mu_star=0.35,
    u_coop=1.0, u_defect_G=0.3, u_defect_B=0.3
)
print(f"alpha={result2['alpha']}, beta={result2['beta']}")
print(f"pi(G) = {result2['pi_G']:.4f}")
print(f"F(G|G) = {result2['F_G_given_G']:.4f}, F(G|B) = {result2['F_G_given_B']:.4f}")
print(f"mu* = {result2['mu_star']}")
print(f"SR under i.i.d.: {result2['sr_iid']} (pi(G)={result2['pi_G']:.3f} vs mu*={result2['mu_star']})")
print(f"SR after G: {result2['sr_after_G']} (F(G|G)={result2['F_G_given_G']:.3f} vs mu*={result2['mu_star']})")
print(f"SR after B: {result2['sr_after_B']} (F(G|B)={result2['F_G_given_B']:.3f} vs mu*={result2['mu_star']})")
print(f"V(s1*) = {result2['V']:.4f}")
print(f"V_Markov(s1*) = {result2['V_Markov']:.4f}")
print(f"V_Markov <= V? {result2['V_Markov_leq_V']}")
print(f"Gap V - V_Markov = {result2['gap']:.4f}")

# ---- Sharper counterexample ----
print("\n--- Sharper Counterexample ---")
result3 = compute_payoffs(
    alpha=0.7, beta=0.2, mu_star=0.25,
    u_coop=1.0, u_defect_G=0.0, u_defect_B=0.0
)
print(f"alpha={result3['alpha']}, beta={result3['beta']}")
print(f"pi(G) = {result3['pi_G']:.4f}")
print(f"F(G|G) = {result3['F_G_given_G']:.4f}, F(G|B) = {result3['F_G_given_B']:.4f}")
print(f"mu* = {result3['mu_star']}")
print(f"SR under i.i.d.: {result3['sr_iid']} (pi(G)={result3['pi_G']:.3f} vs mu*={result3['mu_star']})")
print(f"SR after G: {result3['sr_after_G']} (F(G|G)={result3['F_G_given_G']:.3f} vs mu*={result3['mu_star']})")
print(f"SR after B: {result3['sr_after_B']} (F(G|B)={result3['F_G_given_B']:.3f} vs mu*={result3['mu_star']})")
print(f"V(s1*) = {result3['V']:.4f}")
print(f"V_Markov(s1*) = {result3['V_Markov']:.4f}")
print(f"V_Markov <= V? {result3['V_Markov_leq_V']}")
print(f"Gap V - V_Markov = {result3['gap']:.4f}")

# ---- Systematic scan ----
print("\n--- Systematic Scan Over Parameter Space ---")
print(f"{'alpha':>6} {'beta':>6} {'pi_G':>6} {'mu*':>6} {'sr_iid':>10} "
      f"{'sr|G':>6} {'sr|B':>6} {'V':>8} {'V_M':>8} {'V_M<=V':>8}")
print("-" * 80)

counterexample_count = 0
total_count = 0

for alpha_100 in range(10, 90, 10):
    for beta_100 in range(10, 90, 10):
        alpha = alpha_100 / 100
        beta = beta_100 / 100
        if alpha + beta >= 1.0:
            continue
        for mu_100 in range(20, 80, 10):
            mu_star = mu_100 / 100
            r = compute_payoffs(alpha, beta, mu_star, 1.0, 0.0, 0.0)
            total_count += 1
            if not r['V_Markov_leq_V']:
                counterexample_count += 1
                print(f"{alpha:>6.2f} {beta:>6.2f} {r['pi_G']:>6.3f} {mu_star:>6.2f} "
                      f"{r['sr_iid']:>10} {r['sr_after_G']:>6} {r['sr_after_B']:>6} "
                      f"{r['V']:>8.4f} {r['V_Markov']:>8.4f} {'NO':>8}")

print(f"\nTotal parameter combinations: {total_count}")
print(f"Counterexamples (V_Markov > V): {counterexample_count}")
print(f"Fraction: {counterexample_count/total_count:.2%}")

# ---- Sufficient condition check ----
print("\n" + "=" * 75)
print("SUFFICIENT CONDITION: V_Markov <= V when pi(G) >= mu*")
print("=" * 75)
print("""
When pi(G) >= mu*, SR cooperates under i.i.d. (most favorable for LR).
State-contingent beliefs can only cause defection in some states, so
V_Markov <= V must hold.

When pi(G) < mu*, SR defects under i.i.d. (least favorable for LR).
State-contingent beliefs may enable cooperation in some states, so
V_Markov > V is possible.

This confirms the reviewer's counterexample and shows the paper's
general claim V_Markov <= V is INCORRECT.
""")

print("=" * 75)
print("CONCLUSION")
print("=" * 75)
print("""
1. The reviewer's counterexample is VALID: V_Markov > V when pi(G) < mu*
   but F(G|G) > mu*.
2. The paper's baseline parameters (alpha=0.3, beta=0.5, mu*=0.60)
   DO satisfy V_Markov <= V because pi(G) = 0.625 > mu* = 0.60.
3. The general claim "V_Markov <= V" in Theorem 4.8 and the abstract
   must be corrected: the ordering depends on parameter values.
4. Sufficient condition for V_Markov <= V: the stationary belief induces
   the most favorable SR behavior (e.g., pi(G) >= mu* in deterrence).
""")
