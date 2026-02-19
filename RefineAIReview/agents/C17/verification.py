#!/usr/bin/env python3
"""
C17 Verification: Demonstrate that the original chain already has a
stationary distribution, and the lifting creates the type space.

This is a LOW-severity wording issue. The script shows that pi exists
for theta_t, and tilde_rho for the lifted chain, confirming both exist.
"""

import numpy as np


def main():
    print("=" * 65)
    print("  C17: Original Chain vs. Lifted Chain Stationary Distributions")
    print("=" * 65)

    alpha, beta = 0.3, 0.5

    # Original chain stationary distribution
    pi_G = beta / (alpha + beta)
    pi_B = alpha / (alpha + beta)
    print(f"\nOriginal chain (theta_t):")
    print(f"  Transition: P(B|G)={alpha}, P(G|B)={beta}")
    print(f"  Stationary: pi(G)={pi_G:.4f}, pi(B)={pi_B:.4f}")
    print(f"  Sum = {pi_G + pi_B:.4f}")
    print(f"  The original chain ALREADY HAS a stationary distribution.")

    # Lifted chain stationary distribution
    print(f"\nLifted chain (tilde_theta_t = (theta_t, theta_{{t-1}})):")
    print(f"  tilde_rho(G,G) = pi(G) * F(G|G) = {pi_G:.4f} * {1-alpha:.2f} = {pi_G*(1-alpha):.4f}")
    print(f"  tilde_rho(B,G) = pi(G) * F(B|G) = {pi_G:.4f} * {alpha:.2f}   = {pi_G*alpha:.4f}")
    print(f"  tilde_rho(G,B) = pi(B) * F(G|B) = {pi_B:.4f} * {beta:.2f}   = {pi_B*beta:.4f}")
    print(f"  tilde_rho(B,B) = pi(B) * F(B|B) = {pi_B:.4f} * {1-beta:.2f} = {pi_B*(1-beta):.4f}")

    rho_sum = pi_G * (1 - alpha) + pi_G * alpha + pi_B * beta + pi_B * (1 - beta)
    print(f"  Sum = {rho_sum:.4f}")

    # Purpose of lifting
    print(f"\n--- Purpose of Lifting ---")
    print(f"  1. Type space: Markov strategies map tilde_Theta -> Delta(A_1),")
    print(f"     conditioning on the current transition (theta_t, theta_{{t-1}}).")
    print(f"  2. OT framework: tilde_rho plays the role of the i.i.d. signal")
    print(f"     distribution rho in Luo-Wolitzky's optimal transport formulation.")
    print(f"  3. The lifting does NOT 'create' stationarity; it encodes Markov")
    print(f"     private information into the type space.")
    print(f"\n  The reviewer's concern is correct: saying lifting 'provides a")
    print(f"  stationary distribution' is misleading since pi already exists.")


if __name__ == "__main__":
    main()
