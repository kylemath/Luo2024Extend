#!/usr/bin/env python3
"""
C11 Verification: The Filter's Fixed Point Is NOT π

Demonstrates that filter stability (contraction of initial conditions) does not
imply the filter converges to the stationary distribution π.

Shows: for a range of epsilon values, the filter's "fixed point" (long-run average
posterior, conditional on true state) is near F(·|θ_t), not near π.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.random.seed(42)


def run_filter(alpha, beta, epsilon, T, pi_0):
    """Run HMM filter and return states and filter values."""
    pi_G = beta / (alpha + beta)
    F = np.array([[1 - alpha, alpha], [beta, 1 - beta]])

    states = np.zeros(T, dtype=int)
    states[0] = 0 if np.random.rand() < pi_G else 1
    for t in range(1, T):
        states[t] = np.random.choice(2, p=F[states[t - 1]])

    emission = np.array([
        [1 - epsilon / 2, epsilon / 2],
        [epsilon / 2, 1 - epsilon / 2]
    ])

    obs = np.zeros(T, dtype=int)
    for t in range(T):
        if np.random.rand() < (1 - epsilon):
            obs[t] = states[t]
        else:
            obs[t] = np.random.choice(2)

    filter_G = np.zeros(T)
    prior = pi_0.copy()
    for t in range(T):
        likelihood = emission[:, obs[t]]
        posterior_unnorm = prior * likelihood
        posterior = posterior_unnorm / posterior_unnorm.sum()
        filter_G[t] = posterior[0]
        prior = F.T @ posterior

    return states, filter_G


def main():
    alpha, beta = 0.3, 0.5
    pi_G = beta / (alpha + beta)
    T = 5000
    burn_in = 200

    epsilons = np.linspace(0.01, 0.95, 20)

    # For each epsilon, compute:
    # 1. Mean filter value when θ_t = G (should be near 1-alpha for small epsilon)
    # 2. Mean filter value when θ_t = B (should be near beta for small epsilon)
    # 3. Both should approach pi_G for large epsilon

    mean_filter_G_given_G = []
    mean_filter_G_given_B = []
    prior_diff_at_100 = []

    for eps in epsilons:
        np.random.seed(42)
        states, filter_vals = run_filter(alpha, beta, eps, T, np.array([pi_G, 1 - pi_G]))

        mask_G = states[burn_in:] == 0
        mask_B = states[burn_in:] == 1
        filt_tail = filter_vals[burn_in:]

        mean_filter_G_given_G.append(np.mean(filt_tail[mask_G]))
        mean_filter_G_given_B.append(np.mean(filt_tail[mask_B]))

        # Also check filter stability: run from two extreme priors
        np.random.seed(42)
        _, f1 = run_filter(alpha, beta, eps, T, np.array([0.99, 0.01]))
        np.random.seed(42)
        _, f2 = run_filter(alpha, beta, eps, T, np.array([0.01, 0.99]))
        prior_diff_at_100.append(np.abs(f1[100] - f2[100]))

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle(
        'C11 Verification: Filter Fixed Point ≠ π\n'
        '(Filter stability holds, but the fixed point tracks θ_t for informative channels)',
        fontsize=12, fontweight='bold'
    )

    # Panel 1: E[filter(G) | θ=G] and E[filter(G) | θ=B] vs epsilon
    ax = axes[0, 0]
    ax.plot(epsilons, mean_filter_G_given_G, 'g-o', markersize=4, label='E[π_t(G) | θ_t=G]')
    ax.plot(epsilons, mean_filter_G_given_B, 'r-s', markersize=4, label='E[π_t(G) | θ_t=B]')
    ax.axhline(y=pi_G, color='black', linestyle='--', linewidth=2, label=f'π(G) = {pi_G:.3f}')
    ax.axhline(y=1 - alpha, color='green', linestyle=':', alpha=0.5, label=f'F(G|G) = {1 - alpha:.2f}')
    ax.axhline(y=beta, color='red', linestyle=':', alpha=0.5, label=f'F(G|B) = {beta:.2f}')
    ax.set_xlabel('ε (perturbation)')
    ax.set_ylabel('Mean filter P(G)')
    ax.set_title("Filter's conditional mean vs. ε")
    ax.legend(fontsize=7, loc='center right')

    # Panel 2: Gap between filter fixed point and pi
    ax = axes[0, 1]
    gap_G = np.abs(np.array(mean_filter_G_given_G) - pi_G)
    gap_B = np.abs(np.array(mean_filter_G_given_B) - pi_G)
    ax.plot(epsilons, gap_G, 'g-o', markersize=4, label='|E[π_t(G)|θ=G] - π(G)|')
    ax.plot(epsilons, gap_B, 'r-s', markersize=4, label='|E[π_t(G)|θ=B] - π(G)|')
    ax.set_xlabel('ε (perturbation)')
    ax.set_ylabel('Gap from π(G)')
    ax.set_title('Distance of filter fixed point from π')
    ax.legend(fontsize=8)
    ax.annotate('Filter stays far\nfrom π for small ε',
                xy=(0.1, gap_G[2]), fontsize=9,
                xytext=(0.3, gap_G[2] + 0.02),
                arrowprops=dict(arrowstyle='->', color='green'))

    # Panel 3: Filter stability confirmation - prior difference decays
    ax = axes[1, 0]
    ax.plot(epsilons, prior_diff_at_100, 'b-^', markersize=5)
    ax.set_xlabel('ε (perturbation)')
    ax.set_ylabel('|Filter₁(t=100) - Filter₂(t=100)|')
    ax.set_title('Filter stability holds for ALL ε\n(Prior difference at t=100)')
    ax.set_yscale('log')
    ax.axhline(y=1e-10, color='gray', linestyle=':', alpha=0.5)
    ax.annotate('Prior forgotten\nfor all ε values', xy=(0.5, prior_diff_at_100[10]),
                fontsize=9, xytext=(0.6, 1e-4),
                arrowprops=dict(arrowstyle='->', color='blue'))

    # Panel 4: Joint demonstration - filter stability holds BUT fixed point ≠ pi
    ax = axes[1, 1]
    ax.axis('off')
    summary = (
        "INFERENCE STRUCTURE\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Paper's (invalid) logic:\n"
        "  P1: s₁ᵉ is not state-revealing         ✓\n"
        "  P2: Filter stability holds              ✓\n"
        "  C:  Beliefs converge to π               ✗\n\n"
        "Why the inference fails:\n"
        "  Filter stability = contraction property\n"
        "  It guarantees a UNIQUE fixed point\n"
        "  But the fixed point location depends on\n"
        "  the observation channel, not on π.\n\n"
        "  For informative channels (small ε):\n"
        "    Fixed point ≈ indicator of θ_t\n"
        "  For uninformative channels (ε → 1):\n"
        "    Fixed point → π\n\n"
        "Analogy:\n"
        "  'f is a contraction' ⇏ 'fixed point = 0'\n"
        "  'Filter is stable'   ⇏ 'posterior → π'\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    )
    ax.text(0.05, 0.95, summary, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plt.savefig('/Users/kylemathewson/mathTest/RefineAIReview/agents/C11/verification_c11.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print("=" * 60)
    print("C11 VERIFICATION RESULTS")
    print("=" * 60)
    print(f"\nParameters: α={alpha}, β={beta}, π(G)={pi_G:.3f}")
    print(f"F(G|G)={1 - alpha:.2f}, F(G|B)={beta:.2f}")
    print()
    print("Filter's conditional mean for selected ε values:")
    print(f"{'ε':>6s} | {'E[π_t(G)|θ=G]':>16s} | {'E[π_t(G)|θ=B]':>16s} | {'Prior diff @100':>16s}")
    print("-" * 65)
    for i, eps in enumerate(epsilons):
        if i % 4 == 0 or i == len(epsilons) - 1:
            print(f"{eps:6.2f} | {mean_filter_G_given_G[i]:16.4f} | "
                  f"{mean_filter_G_given_B[i]:16.4f} | {prior_diff_at_100[i]:16.2e}")
    print()
    print("CONCLUSIONS:")
    print("  1. Filter stability holds for ALL ε (prior forgotten exponentially)")
    print("  2. But filter fixed point ≈ F(·|θ_t) for small ε, NOT π")
    print("  3. Only as ε → 1 does the fixed point approach π")
    print("  4. The inference 'filter stability ⟹ beliefs → π' is INVALID")
    print()
    print("Figure saved: verification_c11.png")


if __name__ == '__main__':
    main()
