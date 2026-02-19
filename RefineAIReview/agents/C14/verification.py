#!/usr/bin/env python3
"""
C14 Verification: Notation check for B-hat vs B(s1*, F(.|theta)).

This is a notation/clarity issue, not a mathematical one.
This script verifies that the two best-response objects are distinct
by computing them for the deterrence game example and showing
they differ when belief-robustness fails.
"""

import numpy as np


def compute_B_hat(pi_G, mu_star, xi):
    """
    Compute the xi-confirmed best-response set B_hat_xi(s1*).

    In the deterrence game, B_hat_xi is the set of SR actions that
    remain best responses when the posterior is within xi of
    {omega^R, omega_{s1*}}.

    Returns the SR action ('C' for cooperate, 'D' for defect, or 'both').
    """
    if pi_G - xi > mu_star:
        return "C (cooperate)"
    elif pi_G + xi < mu_star:
        return "D (defect)"
    else:
        return "both (indeterminate within xi-ball)"


def compute_B_state_contingent(alpha, beta, mu_star):
    """
    Compute B(s1*, F(.|theta)) for each state theta.

    In the deterrence game, SR's best response depends on their belief
    about the next state, which is F(G|theta).
    """
    results = {}
    f_G_given_G = 1 - alpha  # P(G next | currently G)
    f_G_given_B = beta       # P(G next | currently B)

    for state, f_G in [("G", f_G_given_G), ("B", f_G_given_B)]:
        if f_G > mu_star:
            results[state] = f"C (cooperate), since F(G|{state})={f_G:.2f} > mu*={mu_star}"
        elif f_G < mu_star:
            results[state] = f"D (defect), since F(G|{state})={f_G:.2f} < mu*={mu_star}"
        else:
            results[state] = f"indifferent, since F(G|{state})={f_G:.2f} = mu*={mu_star}"

    return results


def main():
    print("=" * 65)
    print("  C14: B-hat (confirmed) vs B(s1*, F(.|theta)) (state-contingent)")
    print("=" * 65)

    alpha, beta = 0.3, 0.5
    mu_star = 0.60
    pi_G = beta / (alpha + beta)

    print(f"\nParameters: alpha={alpha}, beta={beta}, pi(G)={pi_G:.3f}, mu*={mu_star}")
    print(f"  F(G|G) = 1-alpha = {1-alpha:.2f}")
    print(f"  F(G|B) = beta    = {beta:.2f}")

    print(f"\n--- B-hat_xi(s1*): Confirmed Best-Response Set ---")
    for xi in [0.01, 0.05, 0.1, 0.2]:
        result = compute_B_hat(pi_G, mu_star, xi)
        print(f"  xi={xi:.2f}: {result}")

    print(f"\n--- B(s1*, F(.|theta)): State-Contingent Best-Response ---")
    b_state = compute_B_state_contingent(alpha, beta, mu_star)
    for state, desc in b_state.items():
        print(f"  State {state}: {desc}")

    belief_robust = all("C" in v for v in b_state.values()) or all("D" in v for v in b_state.values())
    print(f"\n--- Belief-Robustness Check ---")
    print(f"  B(s1*, F(.|G)) = B(s1*, F(.|B))? {'YES' if belief_robust else 'NO'}")
    if not belief_robust:
        print(f"  The state-contingent set VARIES across states.")
        print(f"  B-hat (confirmed set) and B(s1*, F(.|theta)) are DISTINCT objects.")
        print(f"  This confirms the reviewer's concern: notation must disambiguate.")
    else:
        print(f"  Under belief-robustness, both sets coincide.")

    print(f"\n--- Conclusion ---")
    print(f"  B-hat_xi(s1*): governs behavior near commitment-type posterior")
    print(f"  B(s1*, F(.|theta)): governs behavior conditional on revealed state")
    print(f"  These are distinct objects when belief-robustness fails.")
    print(f"  The proposed notation clarification in Remark before Lemma 5.8")
    print(f"  correctly distinguishes them.")


if __name__ == "__main__":
    main()
