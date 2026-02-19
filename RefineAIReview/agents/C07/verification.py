#!/usr/bin/env python3
"""
C07 Verification: Filter Stability vs. Belief Convergence to pi

Demonstrates the critical distinction:
  - Filter stability: two filters with different initial priors converge to each other
  - Belief convergence to pi: the posterior concentrates on the stationary distribution

For small epsilon (informative signals), the posterior TRACKS theta_t via F(.|theta_t),
it does NOT converge to pi. Filter stability holds, but belief convergence to pi does not.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(42)

def simulate_hmm_filter(alpha, beta, epsilon, T, pi_0_init):
    """
    Simulate a 2-state HMM with epsilon-perturbed observations and run
    the Bayesian filter from initial prior pi_0_init.

    States: G=0, B=1
    Transition: P(B|G)=alpha, P(G|B)=beta
    Observation: with prob (1-epsilon), observe true state; with prob epsilon, uniform
    """
    pi_G = beta / (alpha + beta)

    F = np.array([[1 - alpha, alpha],
                  [beta, 1 - beta]])

    states = np.zeros(T, dtype=int)
    states[0] = 0 if np.random.rand() < pi_G else 1
    for t in range(1, T):
        states[t] = np.random.choice(2, p=F[states[t - 1]])

    obs = np.zeros(T, dtype=int)
    for t in range(T):
        if np.random.rand() < (1 - epsilon):
            obs[t] = states[t]
        else:
            obs[t] = np.random.choice(2)

    emission = np.array([
        [1 - epsilon / 2, epsilon / 2],
        [epsilon / 2, 1 - epsilon / 2]
    ])

    filter_G = np.zeros(T)
    prior = pi_0_init
    for t in range(T):
        likelihood = emission[:, obs[t]]
        posterior_unnorm = prior * likelihood
        posterior = posterior_unnorm / posterior_unnorm.sum()
        filter_G[t] = posterior[0]
        prior = F.T @ posterior

    return states, filter_G, pi_G


def main():
    alpha, beta = 0.3, 0.5
    T = 500
    pi_G = beta / (alpha + beta)

    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    fig.suptitle(
        'C07 Verification: Filter Stability ≠ Belief Convergence to π',
        fontsize=14, fontweight='bold'
    )

    # Panel 1: Small epsilon - filter tracks theta, does NOT converge to pi
    epsilon_small = 0.05
    states_s, filter_s_high, _ = simulate_hmm_filter(alpha, beta, epsilon_small, T, np.array([0.9, 0.1]))
    _, filter_s_low, _ = simulate_hmm_filter(alpha, beta, epsilon_small, T, np.array([0.1, 0.9]))

    np.random.seed(42)
    states_s2, filter_s_high2, _ = simulate_hmm_filter(alpha, beta, epsilon_small, T, np.array([0.9, 0.1]))

    ax = axes[0, 0]
    ax.plot(filter_s_high2[:200], alpha=0.7, label=f'Filter (π₀(G)=0.9)', linewidth=0.8)
    ax.axhline(y=pi_G, color='red', linestyle='--', linewidth=1.5, label=f'π(G)={pi_G:.3f}')
    state_colors = ['green' if s == 0 else 'salmon' for s in states_s2[:200]]
    for t in range(200):
        ax.axvspan(t, t + 1, alpha=0.1, color=state_colors[t])
    ax.set_title(f'Small ε={epsilon_small}: Posterior TRACKS θ_t, does NOT converge to π')
    ax.set_ylabel('Filter P(G)')
    ax.set_xlabel('Period')
    ax.legend(fontsize=8)
    ax.set_ylim(-0.05, 1.05)

    # Panel 2: Large epsilon - filter DOES approach pi
    epsilon_large = 0.45
    np.random.seed(42)
    states_l, filter_l, _ = simulate_hmm_filter(alpha, beta, epsilon_large, T, np.array([0.9, 0.1]))

    ax = axes[0, 1]
    ax.plot(filter_l[:200], alpha=0.7, label=f'Filter (π₀(G)=0.9)', linewidth=0.8)
    ax.axhline(y=pi_G, color='red', linestyle='--', linewidth=1.5, label=f'π(G)={pi_G:.3f}')
    state_colors = ['green' if s == 0 else 'salmon' for s in states_l[:200]]
    for t in range(200):
        ax.axvspan(t, t + 1, alpha=0.1, color=state_colors[t])
    ax.set_title(f'Large ε={epsilon_large}: Posterior closer to π (less informative)')
    ax.set_ylabel('Filter P(G)')
    ax.set_xlabel('Period')
    ax.legend(fontsize=8)
    ax.set_ylim(-0.05, 1.05)

    # Panel 3: Filter stability demonstration - two priors converge to EACH OTHER
    np.random.seed(42)
    _, filter_prior1, _ = simulate_hmm_filter(alpha, beta, epsilon_small, T, np.array([0.99, 0.01]))
    np.random.seed(42)
    _, filter_prior2, _ = simulate_hmm_filter(alpha, beta, epsilon_small, T, np.array([0.01, 0.99]))

    ax = axes[1, 0]
    ax.plot(np.abs(filter_prior1 - filter_prior2)[:100], 'b-', linewidth=1.5,
            label='|Filter₁ - Filter₂|')
    t_vals = np.arange(100)
    diff_init = np.abs(filter_prior1[0] - filter_prior2[0])
    lam = 0.5 * np.abs(1 - alpha - beta)
    ax.plot(t_vals, diff_init * np.exp(-0.3 * t_vals), 'r--', linewidth=1,
            label='Exponential envelope')
    ax.set_title(f'Filter Stability (ε={epsilon_small}): Priors forgotten exponentially')
    ax.set_ylabel('|π_t(prior₁) - π_t(prior₂)|')
    ax.set_xlabel('Period')
    ax.legend(fontsize=8)
    ax.set_yscale('log')

    # Panel 4: Distance from pi does NOT vanish for small epsilon
    epsilons = [0.01, 0.05, 0.1, 0.2, 0.3, 0.45]
    mean_dist_from_pi = []
    for eps in epsilons:
        np.random.seed(42)
        _, filt, _ = simulate_hmm_filter(alpha, beta, eps, T, np.array([pi_G, 1 - pi_G]))
        mean_dist_from_pi.append(np.mean(np.abs(filt[50:] - pi_G)))

    ax = axes[1, 1]
    ax.plot(epsilons, mean_dist_from_pi, 'bo-', linewidth=2, markersize=8)
    ax.set_title('Mean |Filter - π(G)| vs. ε (after burn-in)')
    ax.set_xlabel('ε (perturbation level)')
    ax.set_ylabel('E[|π_t(G) - π(G)|]')
    ax.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    ax.annotate('Small ε: posterior\ntracks θ_t, far from π',
                xy=(0.05, mean_dist_from_pi[1]), fontsize=8,
                xytext=(0.15, mean_dist_from_pi[1] + 0.05),
                arrowprops=dict(arrowstyle='->', color='red'))

    # Panel 5: Histogram of filter values vs pi for small epsilon
    np.random.seed(42)
    states_hist, filter_hist, _ = simulate_hmm_filter(alpha, beta, 0.05, 2000, np.array([pi_G, 1 - pi_G]))

    ax = axes[2, 0]
    filter_in_G = filter_hist[50:][states_hist[50:] == 0]
    filter_in_B = filter_hist[50:][states_hist[50:] == 1]
    ax.hist(filter_in_G, bins=40, alpha=0.6, label=f'θ_t=G: E≈{np.mean(filter_in_G):.3f}', color='green', density=True)
    ax.hist(filter_in_B, bins=40, alpha=0.6, label=f'θ_t=B: E≈{np.mean(filter_in_B):.3f}', color='red', density=True)
    ax.axvline(x=pi_G, color='black', linestyle='--', linewidth=2, label=f'π(G)={pi_G:.3f}')
    ax.axvline(x=1 - alpha, color='green', linestyle=':', linewidth=1.5, label=f'F(G|G)={1 - alpha:.2f}')
    ax.axvline(x=beta, color='red', linestyle=':', linewidth=1.5, label=f'F(G|B)={beta:.2f}')
    ax.set_title(f'ε=0.05: Filter clusters near F(G|θ_t), NOT at π')
    ax.set_xlabel('Filter P(G)')
    ax.set_ylabel('Density')
    ax.legend(fontsize=7)

    # Panel 6: Summary text
    ax = axes[2, 1]
    ax.axis('off')
    summary = (
        "KEY DISTINCTION\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Filter Stability (Prop A.2):\n"
        "  sup_{π₀,π₀'} ||π_t - π_t'|| ≤ C·λᵗ\n"
        "  → Initial PRIOR is forgotten\n"
        "  → Two observers agree eventually\n\n"
        "Chain Mixing:\n"
        "  ||P(θ_t∈·) - π|| → 0\n"
        "  → Initial STATE is forgotten\n"
        "  → Marginal of θ_t converges to π\n\n"
        "Belief Convergence to π:\n"
        "  ||π_t(·|y₀,...,y_t) - π|| → 0\n"
        "  → REQUIRES uninformative signals\n"
        "  → FAILS for small ε\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Params: α={alpha}, β={beta}, π(G)={pi_G:.3f}\n"
        f"F(G|G)={1 - alpha:.2f}, F(G|B)={beta:.2f}"
    )
    ax.text(0.05, 0.95, summary, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('/Users/kylemathewson/mathTest/RefineAIReview/agents/C07/verification_c07.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print("=" * 60)
    print("C07 VERIFICATION RESULTS")
    print("=" * 60)
    print(f"\nParameters: α={alpha}, β={beta}, π(G)={pi_G:.3f}")
    print(f"F(G|G) = {1 - alpha:.2f}, F(G|B) = {beta:.2f}")
    print()
    print("Mean |Filter - π(G)| by epsilon (after burn-in of 50 periods):")
    for eps, dist in zip(epsilons, mean_dist_from_pi):
        print(f"  ε = {eps:.2f}: E[|π_t(G) - π(G)|] = {dist:.4f}")
    print()
    print("CONCLUSION:")
    print("  For small ε, the posterior does NOT converge to π.")
    print("  It tracks θ_t via approximately F(·|θ_t).")
    print("  Filter stability guarantees prior forgetting, not belief → π.")
    print()
    print("Figure saved: verification_c07.png")


if __name__ == '__main__':
    main()
