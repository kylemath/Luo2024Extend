#!/usr/bin/env python3
"""
analysis_beliefs.py — SA1: Belief deviation from stationarity.

For a grid of (alpha, beta) values, runs Bayesian filtering with the
Stackelberg strategy s1*(G)=A, s1*(B)=F, then computes the mean TV distance
||belief - pi|| over a simulation trajectory.

Generates: ../figures/fig_belief_deviation.png (heatmap)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# ── Inline utilities ──────────────────────────────────────────────────────────

def tv_distance(p, q):
    return 0.5 * np.abs(p - q).sum()


def simulate_chain(alpha, beta, T, rng, theta_0=None):
    pi = np.array([beta / (alpha + beta), alpha / (alpha + beta)])
    Tmat = np.array([[1 - alpha, alpha], [beta, 1 - beta]])
    states = np.zeros(T, dtype=int)
    states[0] = theta_0 if theta_0 is not None else rng.choice(2, p=pi)
    for t in range(1, T):
        states[t] = rng.choice(2, p=Tmat[states[t - 1]])
    return states, pi, Tmat


def bayesian_filter_run(alpha, beta, T=500, seed=42):
    """Run Bayesian filtering and return mean TV distance from pi."""
    rng = np.random.default_rng(seed)
    states, pi, Tmat = simulate_chain(alpha, beta, T, rng)

    # Stackelberg strategy: A (0) in G (0), F (1) in B (1)
    strat = np.array([[1.0, 0.0],   # state G -> action A w.p.1
                       [0.0, 1.0]])  # state B -> action F w.p.1

    belief = pi.copy()
    tv_vals = []

    for t in range(1, T):
        predicted = Tmat.T @ belief
        action = 0 if states[t] == 0 else 1
        likelihood = strat[:, action]
        posterior = predicted * likelihood
        s = posterior.sum()
        if s > 0:
            posterior /= s
        else:
            posterior = pi.copy()
        belief = posterior
        tv_vals.append(tv_distance(belief, pi))

    return np.mean(tv_vals) if tv_vals else 0.0


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    N = 50
    alphas = np.linspace(0.05, 0.95, N)
    betas = np.linspace(0.05, 0.95, N)
    grid = np.zeros((N, N))

    for i, a in enumerate(alphas):
        for j, b in enumerate(betas):
            grid[j, i] = bayesian_filter_run(a, b)

    fig, ax = plt.subplots(figsize=(7, 5.5))
    im = ax.imshow(grid, origin='lower', aspect='auto',
                   extent=[alphas[0], alphas[-1], betas[0], betas[-1]],
                   cmap='viridis')
    cb = fig.colorbar(im, ax=ax, label='Mean TV distance from π')
    ax.set_xlabel('α = Pr(B|G)')
    ax.set_ylabel('β = Pr(G|B)')
    ax.set_title('Belief Deviation from Stationarity')

    outdir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'fig_belief_deviation.png')
    fig.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {outpath}")

    tv_mean = np.mean(grid)
    # High-persistence region: alpha < 0.2 and beta < 0.2
    hp_mask = (alphas < 0.2)
    hp_j = np.where(betas < 0.2)[0]
    hp_i = np.where(alphas < 0.2)[0]
    hp_vals = grid[np.ix_(hp_j, hp_i)]
    tv_hp = np.mean(hp_vals) if hp_vals.size > 0 else 0.0

    print(f"STAT:tv_mean={tv_mean:.3f}")
    print(f"STAT:tv_mean_high_persist={tv_hp:.3f}")


if __name__ == '__main__':
    main()
