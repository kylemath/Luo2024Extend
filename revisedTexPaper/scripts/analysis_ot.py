#!/usr/bin/env python3
"""
analysis_ot.py — SA5: Optimal transport robustness analysis.

For a grid of (alpha, beta), solves OT (Wasserstein-1) between the stationary
distribution and the filtered belief distribution, computes a stability
margin, and plots a heatmap.

Generates: ../figures/fig_ot_robustness.png (stability margin heatmap)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os


def wasserstein_1_binary(p, q):
    """Wasserstein-1 distance for distributions on {0, 1}."""
    return abs(p[0] - q[0])


def simulate_filtered_belief(alpha, beta, T=300, seed=42):
    """Simulate chain + Bayesian filter, return time-averaged belief."""
    rng = np.random.default_rng(seed)
    Tmat = np.array([[1 - alpha, alpha], [beta, 1 - beta]])
    pi = np.array([beta / (alpha + beta), alpha / (alpha + beta)])

    strat = np.array([[1.0, 0.0], [0.0, 1.0]])  # Stackelberg

    states = np.zeros(T, dtype=int)
    states[0] = rng.choice(2, p=pi)
    for t in range(1, T):
        states[t] = rng.choice(2, p=Tmat[states[t - 1]])

    belief = pi.copy()
    beliefs = []

    for t in range(1, T):
        predicted = Tmat.T @ belief
        action = 0 if states[t] == 0 else 1
        lik = strat[:, action]
        posterior = predicted * lik
        s = posterior.sum()
        belief = posterior / s if s > 0 else pi.copy()
        beliefs.append(belief.copy())

    return np.mean(beliefs, axis=0), pi


def ot_stability_margin(alpha, beta, T=300, seed=42):
    """Compute stability margin: 1 - W1(filtered, stationary)."""
    avg_belief, pi = simulate_filtered_belief(alpha, beta, T, seed)
    w1 = wasserstein_1_binary(avg_belief, pi)
    return 1.0 - w1


def main():
    N = 60
    alphas = np.linspace(0.05, 0.95, N)
    betas = np.linspace(0.05, 0.95, N)
    grid = np.zeros((N, N))

    for i, a in enumerate(alphas):
        for j, b in enumerate(betas):
            grid[j, i] = ot_stability_margin(a, b)

    fig, ax = plt.subplots(figsize=(7, 5.5))
    im = ax.imshow(grid, origin='lower', aspect='auto',
                   extent=[alphas[0], alphas[-1], betas[0], betas[-1]],
                   cmap='RdYlGn', vmin=0, vmax=1)
    fig.colorbar(im, ax=ax, label='Stability margin (1 − W₁)')
    ax.set_xlabel('α = Pr(B|G)')
    ax.set_ylabel('β = Pr(G|B)')
    ax.set_title('OT Robustness: Stability Margin')

    outdir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'fig_ot_robustness.png')
    fig.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {outpath}")

    stable_pct = 100.0 * np.mean(grid > 0.5)
    min_margin = np.min(grid)
    print(f"STAT:ot_stable_pct={stable_pct:.0f}")
    print(f"STAT:min_margin={min_margin:.1f}")


if __name__ == '__main__':
    main()
