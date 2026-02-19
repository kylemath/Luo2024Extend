"""
C04 Verification: Timing ambiguity in V_Markov formula.

Compares:
  Paper formula:    V_paper = Σ_θ π(θ) · inf_{B(s1*, F(·|θ))} u1(θ, s1*(θ), α2)
  Corrected formula: V_corr = Σ_{θ'} π(θ') · inf_{B(s1*, F(·|θ'))} Σ_θ F(θ|θ') u1(θ, s1*(θ,θ'), α2)

In the paper's formula, θ plays triple duty (weight, belief, payoff).
In the corrected formula, θ' = previous state (belief), θ = current state (payoff).
"""

import numpy as np


def deterrence_payoffs(theta, a1, a2):
    """
    Simple deterrence game payoffs for LR.
    State G: high payoff from cooperation.
    State B: low payoff from cooperation.
    """
    if a2 == "cooperate":
        return 1.0 if theta == "G" else 0.5
    else:
        return 0.3 if theta == "G" else 0.0


def compute_both_formulas(alpha, beta, mu_star):
    """
    Compare paper's V_Markov formula with corrected formula.
    """
    pi_G = beta / (alpha + beta)
    pi_B = alpha / (alpha + beta)
    F_G_given_G = 1 - alpha
    F_G_given_B = beta
    F_B_given_G = alpha
    F_B_given_B = 1 - beta

    states = ["G", "B"]
    pi = {"G": pi_G, "B": pi_B}
    F_G = {"G": F_G_given_G, "B": F_G_given_B}
    F_B = {"G": F_B_given_G, "B": F_B_given_B}
    F = {"G": {"G": F_G_given_G, "B": F_B_given_G},
         "B": {"G": F_G_given_B, "B": F_B_given_B}}

    def sr_action(belief_G):
        return "cooperate" if belief_G >= mu_star else "defect"

    # ---- Paper's formula ----
    # V_paper = Σ_θ π(θ) · inf_{B(s1*, F(·|θ))} u1(θ, s1*(θ), α2)
    # Here θ is used for both belief and payoff.
    V_paper = 0.0
    for theta in states:
        belief_G = F_G[theta]  # F(G|θ) = belief about next state
        a2 = sr_action(belief_G)
        payoff = deterrence_payoffs(theta, "fight", a2)
        V_paper += pi[theta] * payoff

    # ---- Corrected formula ----
    # V_corr = Σ_{θ'} π(θ') · inf_{B(s1*, F(·|θ'))} Σ_θ F(θ|θ') u1(θ, s1*(θ,θ'), α2)
    # θ' = previous state (belief), θ = current state (payoff)
    V_corr = 0.0
    for theta_prev in states:
        belief_G = F_G[theta_prev]
        a2 = sr_action(belief_G)
        expected_payoff = 0.0
        for theta_curr in states:
            expected_payoff += F[theta_prev][theta_curr] * deterrence_payoffs(theta_curr, "fight", a2)
        V_corr += pi[theta_prev] * expected_payoff

    return {
        'alpha': alpha, 'beta': beta,
        'pi_G': pi_G, 'mu_star': mu_star,
        'F_G_given_G': F_G_given_G, 'F_G_given_B': F_G_given_B,
        'V_paper': V_paper, 'V_corrected': V_corr,
        'difference': abs(V_paper - V_corr),
        'match': abs(V_paper - V_corr) < 1e-10,
        'sr_after_G': sr_action(F_G_given_G),
        'sr_after_B': sr_action(F_G_given_B)
    }


print("=" * 75)
print("C04 VERIFICATION: Paper's V_Markov vs Corrected V_Markov")
print("=" * 75)

# ---- Paper's baseline ----
print("\n--- Paper's Baseline (alpha=0.3, beta=0.5) ---")
r = compute_both_formulas(0.3, 0.5, 0.60)
print(f"pi(G)={r['pi_G']:.4f}, F(G|G)={r['F_G_given_G']:.2f}, F(G|B)={r['F_G_given_B']:.2f}")
print(f"SR after G: {r['sr_after_G']}, SR after B: {r['sr_after_B']}")
print(f"V_paper     = {r['V_paper']:.6f}")
print(f"V_corrected = {r['V_corrected']:.6f}")
print(f"Difference  = {r['difference']:.6f}")
print(f"Match?      = {r['match']}")

# ---- Systematic comparison ----
print("\n--- Systematic Comparison ---")
print(f"{'alpha':>6} {'beta':>6} {'mu*':>6} {'V_paper':>10} {'V_corr':>10} {'diff':>10} {'match':>6}")
print("-" * 60)

mismatch_count = 0
total_count = 0

for alpha_10 in range(1, 9):
    for beta_10 in range(1, 9):
        alpha = alpha_10 / 10
        beta = beta_10 / 10
        if alpha + beta >= 1.0:
            continue
        for mu_10 in range(2, 8):
            mu_star = mu_10 / 10
            r = compute_both_formulas(alpha, beta, mu_star)
            total_count += 1
            if not r['match']:
                mismatch_count += 1
                if mismatch_count <= 20:
                    print(f"{alpha:>6.2f} {beta:>6.2f} {mu_star:>6.2f} "
                          f"{r['V_paper']:>10.4f} {r['V_corrected']:>10.4f} "
                          f"{r['difference']:>10.4f} {'NO':>6}")

print(f"\nTotal: {total_count}, Mismatches: {mismatch_count} ({mismatch_count/total_count:.1%})")

# ---- When they DO match ----
print("\n--- When do the formulas agree? ---")
print("""
The formulas agree when:
  1. Payoffs are state-independent: u1(G,...) = u1(B,...) for same actions
  2. SR takes the same action after both states (belief-robust case)
  3. F is symmetric in a way that makes expectations cancel

With state-dependent payoffs and non-belief-robust games, the formulas
generically DISAGREE. The corrected formula uses the proper conditional
expectation over the current state given the previous state.
""")

# ---- Demonstrate the issue clearly ----
print("=" * 75)
print("Detailed Walkthrough: Why the Formulas Differ")
print("=" * 75)

alpha, beta = 0.3, 0.5
mu_star = 0.60
pi_G = beta / (alpha + beta)
pi_B = alpha / (alpha + beta)

print(f"\nalpha={alpha}, beta={beta}, mu*={mu_star}")
print(f"pi(G)={pi_G:.4f}, pi(B)={pi_B:.4f}")
print(f"F(G|G)={1-alpha:.2f}, F(B|G)={alpha:.2f}")
print(f"F(G|B)={beta:.2f}, F(B|B)={1-beta:.2f}")

print(f"\nSR after G: cooperate (F(G|G)={1-alpha:.2f} >= {mu_star})")
print(f"SR after B: defect    (F(G|B)={beta:.2f} < {mu_star})")

print(f"\n--- Paper's formula (same θ for belief and payoff) ---")
print(f"  θ=G: π(G) * u1(G, fight, cooperate) = {pi_G:.4f} * {deterrence_payoffs('G','fight','cooperate')} "
      f"= {pi_G * deterrence_payoffs('G','fight','cooperate'):.4f}")
print(f"  θ=B: π(B) * u1(B, fight, defect)    = {pi_B:.4f} * {deterrence_payoffs('B','fight','defect')} "
      f"= {pi_B * deterrence_payoffs('B','fight','defect'):.4f}")
V_paper = pi_G * deterrence_payoffs('G', 'fight', 'cooperate') + pi_B * deterrence_payoffs('B', 'fight', 'defect')
print(f"  V_paper = {V_paper:.4f}")

print(f"\n--- Corrected formula (θ' for belief, θ for payoff) ---")
print(f"  θ'=G (SR cooperates):")
exp_G = (1-alpha)*deterrence_payoffs('G','fight','cooperate') + alpha*deterrence_payoffs('B','fight','cooperate')
print(f"    E[u1|θ'=G,coop] = F(G|G)*u1(G,coop) + F(B|G)*u1(B,coop)")
print(f"                     = {1-alpha:.2f}*{deterrence_payoffs('G','fight','cooperate')} + {alpha:.2f}*{deterrence_payoffs('B','fight','cooperate')}")
print(f"                     = {exp_G:.4f}")
print(f"    Contribution: π(G)*{exp_G:.4f} = {pi_G*exp_G:.4f}")

print(f"  θ'=B (SR defects):")
exp_B = beta*deterrence_payoffs('G','fight','defect') + (1-beta)*deterrence_payoffs('B','fight','defect')
print(f"    E[u1|θ'=B,defect] = F(G|B)*u1(G,def) + F(B|B)*u1(B,def)")
print(f"                      = {beta:.2f}*{deterrence_payoffs('G','fight','defect')} + {1-beta:.2f}*{deterrence_payoffs('B','fight','defect')}")
print(f"                      = {exp_B:.4f}")
print(f"    Contribution: π(B)*{exp_B:.4f} = {pi_B*exp_B:.4f}")

V_corr = pi_G * exp_G + pi_B * exp_B
print(f"  V_corrected = {V_corr:.4f}")

print(f"\n  DIFFERENCE = {abs(V_paper - V_corr):.4f}")
if abs(V_paper - V_corr) > 1e-10:
    print("  The formulas DISAGREE → the paper's formula has a timing error.")
else:
    print("  The formulas agree for these parameters (coincidentally).")

print("\n" + "=" * 75)
print("CONCLUSION")
print("=" * 75)
print("""
1. The paper's V_Markov formula uses the SAME θ for SR's belief (F(·|θ))
   and for the payoff (u1(θ,...)). These should be DIFFERENT variables:
   - θ' = θ_{t-1}: previous state, determines SR belief F(·|θ')
   - θ  = θ_t:     current state, determines payoff u1(θ,...)

2. The corrected formula takes an expectation over θ_t given θ_{t-1}:
   V_Markov = Σ_{θ'} π(θ') inf_{B(s1*, F(·|θ'))} Σ_θ F(θ|θ') u1(θ, s1*(θ,θ'), α2)

3. The formulas disagree whenever payoffs are state-dependent AND
   belief-robustness fails (SR actions differ across states).

4. This is a real mathematical error, not just notation.
""")
