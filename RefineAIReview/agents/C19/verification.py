#!/usr/bin/env python3
"""
C19 Verification: Chain Mixing vs. Filter Stability

Demonstrates the distinction between:
  1. Chain mixing: P(θ_t ∈ · | θ_0) → π  (initial STATE forgotten)
  2. Filter stability: π_t(π_0) → π_t(π_0')  (initial PRIOR forgotten)

Both happen, but they are mathematically distinct properties.
The paper's text in Appendix A ambiguously refers to "initial condition of the
Markov chain" when it means "initial prior of the filter."
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(42)


def chain_mixing(alpha, beta, T, theta_0):
    """
    Compute P(θ_t = G | θ_0) analytically.
    For a 2-state chain: P(θ_t=G) = π(G) + (1-α-β)^t * (I(θ_0=G) - π(G))
    """
    pi_G = beta / (alpha + beta)
    rho = 1 - alpha - beta
    indicator_G = 1.0 if theta_0 == 0 else 0.0
    t = np.arange(T)
    return pi_G + rho**t * (indicator_G - pi_G)


def filter_stability_sim(alpha, beta, epsilon, T, pi_0_G, seed=42):
    """
    Simulate filter from initial prior pi_0 = [pi_0_G, 1-pi_0_G].
    Returns filter trajectory.
    """
    rng = np.random.RandomState(seed)
    pi_G = beta / (alpha + beta)
    F_mat = np.array([[1 - alpha, alpha], [beta, 1 - beta]])
    emission = np.array([
        [1 - epsilon / 2, epsilon / 2],
        [epsilon / 2, 1 - epsilon / 2]
    ])

    states = np.zeros(T, dtype=int)
    states[0] = 0 if rng.rand() < pi_G else 1
    for t in range(1, T):
        states[t] = rng.choice(2, p=F_mat[states[t - 1]])

    obs = np.zeros(T, dtype=int)
    for t in range(T):
        if rng.rand() < (1 - epsilon):
            obs[t] = states[t]
        else:
            obs[t] = rng.choice(2)

    filter_G = np.zeros(T)
    prior = np.array([pi_0_G, 1 - pi_0_G])
    for t in range(T):
        likelihood = emission[:, obs[t]]
        posterior_unnorm = prior * likelihood
        posterior = posterior_unnorm / posterior_unnorm.sum()
        filter_G[t] = posterior[0]
        prior = F_mat.T @ posterior

    return states, filter_G


def main():
    alpha, beta = 0.3, 0.5
    pi_G = beta / (alpha + beta)
    T = 200
    epsilon = 0.1

    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    fig.suptitle(
        'C19 Verification: Chain Mixing (θ₀ forgotten) vs. Filter Stability (π₀ forgotten)',
        fontsize=13, fontweight='bold'
    )

    # Panel 1: Chain mixing - P(θ_t=G|θ_0) converges to π(G)
    ax = axes[0, 0]
    p_G_from_G = chain_mixing(alpha, beta, T, theta_0=0)
    p_G_from_B = chain_mixing(alpha, beta, T, theta_0=1)

    ax.plot(p_G_from_G[:50], 'g-', linewidth=2, label='P(θ_t=G | θ₀=G)')
    ax.plot(p_G_from_B[:50], 'r-', linewidth=2, label='P(θ_t=G | θ₀=B)')
    ax.axhline(y=pi_G, color='black', linestyle='--', linewidth=1.5, label=f'π(G)={pi_G:.3f}')
    ax.set_title('Chain Mixing: Initial STATE θ₀ Forgotten')
    ax.set_xlabel('Period t')
    ax.set_ylabel('P(θ_t = G)')
    ax.legend(fontsize=9)
    ax.annotate('Convergence rate: |1-α-β|ᵗ',
                xy=(15, (p_G_from_G[15] + p_G_from_B[15]) / 2),
                fontsize=9, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Panel 2: Filter stability - filters from different π₀ converge to EACH OTHER
    ax = axes[0, 1]
    states1, f_high = filter_stability_sim(alpha, beta, epsilon, T, pi_0_G=0.99, seed=42)
    _, f_low = filter_stability_sim(alpha, beta, epsilon, T, pi_0_G=0.01, seed=42)

    ax.plot(f_high[:80], 'g-', linewidth=1.2, alpha=0.8, label='Filter (π₀(G)=0.99)')
    ax.plot(f_low[:80], 'r-', linewidth=1.2, alpha=0.8, label='Filter (π₀(G)=0.01)')
    ax.set_title('Filter Stability: Initial PRIOR π₀ Forgotten')
    ax.set_xlabel('Period t')
    ax.set_ylabel('Filter π_t(G)')
    ax.legend(fontsize=9)
    ax.annotate('Filters converge\nto each other\n(not necessarily to π)',
                xy=(40, (f_high[40] + f_low[40]) / 2), fontsize=9, ha='center',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Panel 3: Decay rates compared
    ax = axes[1, 0]
    rho = abs(1 - alpha - beta)
    chain_diff = np.abs(p_G_from_G - p_G_from_B)
    filter_diff = np.abs(f_high - f_low)

    ax.semilogy(chain_diff[:50], 'b-', linewidth=2, label='Chain: |P(G|θ₀=G) - P(G|θ₀=B)|')
    ax.semilogy(filter_diff[:50], 'r-', linewidth=1.5, alpha=0.7,
                label='Filter: |π_t(π₀=0.99) - π_t(π₀=0.01)|')
    t_vals = np.arange(50)
    ax.semilogy(t_vals, rho**t_vals, 'k--', linewidth=1, alpha=0.5,
                label=f'|1-α-β|ᵗ = {rho:.1f}ᵗ')
    ax.set_title('Decay Rates: Both Exponential, Different Objects')
    ax.set_xlabel('Period t')
    ax.set_ylabel('Difference (log scale)')
    ax.legend(fontsize=8)

    # Panel 4: Summary of the distinction
    ax = axes[1, 1]
    ax.axis('off')
    summary = (
        "C19: TERMINOLOGY ISSUE\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Paper's text (App A, after Prop A.2):\n"
        "  'initial condition of the Markov chain\n"
        "   is forgotten exponentially fast'\n\n"
        "Problem: 'initial condition of the Markov\n"
        "  chain' ← sounds like θ₀ (chain mixing)\n\n"
        "Prop A.2 is actually about:\n"
        "  'initial prior of the filter'\n"
        "  ← i.e., π₀ (filter stability)\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "CHAIN MIXING:       FILTER STABILITY:\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "Forgets θ₀          Forgets π₀\n"
        "P(θ_t∈·|θ₀) → π    π_t(π₀) → π_t(π₀')\n"
        "Property of chain   Property of filter\n"
        "Rate: spectral gap  Rate: obs. channel\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"Parameters: α={alpha}, β={beta}, ε={epsilon}\n"
        f"|1-α-β| = {rho:.1f} (chain mixing rate)"
    )
    ax.text(0.02, 0.98, summary, transform=ax.transAxes, fontsize=8.5,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('/Users/kylemathewson/mathTest/RefineAIReview/agents/C19/verification_c19.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print("=" * 60)
    print("C19 VERIFICATION RESULTS")
    print("=" * 60)
    print(f"\nParameters: α={alpha}, β={beta}, π(G)={pi_G:.3f}, ε={epsilon}")
    print(f"|1-α-β| = {rho:.1f}")
    print()
    print("Chain mixing (initial STATE θ₀ forgotten):")
    print(f"  P(θ_5=G | θ₀=G) = {p_G_from_G[5]:.4f}")
    print(f"  P(θ_5=G | θ₀=B) = {p_G_from_B[5]:.4f}")
    print(f"  P(θ_20=G | θ₀=G) = {p_G_from_G[20]:.6f}")
    print(f"  P(θ_20=G | θ₀=B) = {p_G_from_B[20]:.6f}")
    print(f"  Converge to π(G) = {pi_G:.3f}")
    print()
    print("Filter stability (initial PRIOR π₀ forgotten):")
    print(f"  |f_high(5) - f_low(5)| = {abs(f_high[5] - f_low[5]):.6f}")
    print(f"  |f_high(20) - f_low(20)| = {abs(f_high[20] - f_low[20]):.8f}")
    print(f"  Filters converge to EACH OTHER (not necessarily to π)")
    print()
    print("The paper says 'initial condition of the Markov chain' (sounds like θ₀)")
    print("Prop A.2 is about 'initial prior of the filter' (i.e., π₀)")
    print("Fix: replace with precise language about π₀")
    print()
    print("Figure saved: verification_c19.png")


if __name__ == '__main__':
    main()
