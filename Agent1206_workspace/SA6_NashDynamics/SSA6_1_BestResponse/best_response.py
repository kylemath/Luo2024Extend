#!/usr/bin/env python3
"""
SSA6_1: SR Player Best Response Computation
Computes and visualises the short-run player's best response as a function
of their belief about the state, and analyses threshold crossings.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shared.markov_utils import (
    MarkovChain, DeterrenceGame, BayesianFilter,
    make_strategy_matrix, save_figure
)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)


# SR payoff parameters (from task.md)
# u2(G, C) = 1, u2(G, D) = 0, u2(B, C) = -1, u2(B, D) = 0.5
U2 = np.array([
    [1.0, 0.0],    # State G: [C, D]
    [-1.0, 0.5]    # State B: [C, D]
])

SR_ACTIONS = ['C', 'D']  # Cooperate, Defect


def sr_expected_payoff(mu, action_idx):
    """
    Expected SR payoff for action (C=0, D=1) given belief mu = Pr(theta=G).

    E[u2(C)] = mu * 1 + (1-mu) * (-1) = 2*mu - 1
    E[u2(D)] = mu * 0 + (1-mu) * 0.5  = 0.5*(1-mu)
    """
    if action_idx == 0:  # C
        return 2 * mu - 1
    else:  # D
        return 0.5 * (1 - mu)


def sr_best_response(mu):
    """
    Best response for SR given belief mu.
    C iff 2*mu - 1 > 0.5*(1-mu) iff mu > 3/5 = 0.6
    Returns: 0 (C), 1 (D), or -1 (indifferent at threshold)
    """
    payoff_c = sr_expected_payoff(mu, 0)
    payoff_d = sr_expected_payoff(mu, 1)

    if abs(payoff_c - payoff_d) < 1e-12:
        return -1  # indifferent
    elif payoff_c > payoff_d:
        return 0  # C
    else:
        return 1  # D


def compute_threshold():
    """Analytical threshold: mu* = 3/5 = 0.6"""
    return 3.0 / 5.0


def simulate_beliefs(mc, game, T=5000, rng=None):
    """
    Simulate the game and track SR Bayesian beliefs.

    LR plays Stackelberg (A in G, F in B).
    SR observes action and updates belief.
    """
    if rng is None:
        rng = np.random.default_rng(42)

    states = mc.simulate(T, rng=rng)
    strat_mat = make_strategy_matrix(game.stackelberg_strategy)

    bf = BayesianFilter(mc)
    beliefs = np.zeros(T)
    beliefs[0] = mc.pi[0]  # initial belief = stationary Pr(G)

    actions_lr = np.zeros(T, dtype=int)
    actions_sr = np.zeros(T, dtype=int)

    for t in range(T):
        # LR action
        actions_lr[t] = game.stackelberg_strategy(states[t])

        # SR belief and best response
        mu_t = bf.belief[0]  # Pr(G)
        beliefs[t] = mu_t
        actions_sr[t] = max(0, sr_best_response(mu_t))  # resolve indifference as C

        # Bayesian update with observed LR action
        if t < T - 1:
            bf.update(actions_lr[t], strat_mat)

    return states, beliefs, actions_lr, actions_sr


def main():
    print("=" * 60)
    print("SSA6_1: SR Player Best Response")
    print("=" * 60)

    mc = MarkovChain(alpha=0.3, beta=0.5)
    game = DeterrenceGame(x=0.3, y=0.4)

    threshold = compute_threshold()
    print(f"\nSR payoff from C: E[u2(C)] = 2μ - 1")
    print(f"SR payoff from D: E[u2(D)] = 0.5(1-μ)")
    print(f"Threshold μ* = {threshold:.4f}")
    print(f"SR plays C when μ > {threshold}, D when μ < {threshold}")

    # ---- Plot 1: Best response as function of belief ----
    mus = np.linspace(0, 1, 500)
    payoff_c = np.array([sr_expected_payoff(m, 0) for m in mus])
    payoff_d = np.array([sr_expected_payoff(m, 1) for m in mus])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [2, 1]})

    ax1.plot(mus, payoff_c, 'b-', linewidth=2.5, label='E[u₂(C)] = 2μ−1')
    ax1.plot(mus, payoff_d, 'r-', linewidth=2.5, label='E[u₂(D)] = 0.5(1−μ)')
    ax1.axvline(threshold, color='green', linestyle='--', linewidth=2,
                label=f'μ* = {threshold:.2f}')
    ax1.fill_betweenx([-1.5, 1.5], 0, threshold, alpha=0.08, color='red', label='D region')
    ax1.fill_betweenx([-1.5, 1.5], threshold, 1, alpha=0.08, color='blue', label='C region')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_xlabel('Belief μ = Pr(θ=G)', fontsize=13)
    ax1.set_ylabel('Expected SR Payoff', fontsize=13)
    ax1.set_title('SR Expected Payoffs and Best Response', fontsize=14)
    ax1.legend(fontsize=10, loc='upper left')
    ax1.grid(True, alpha=0.3)

    # Mark stationary belief
    pi_g = mc.pi[0]
    ax1.axvline(pi_g, color='purple', linestyle=':', linewidth=1.5)
    ax1.annotate(f'π(G)={pi_g:.3f}', xy=(pi_g, 0.8), fontsize=10,
                 color='purple', ha='center')

    # Bottom: BR mapping
    br_values = np.array([sr_best_response(m) for m in mus])
    br_labels = np.where(br_values == 0, 1, 0)  # 1 for C, 0 for D (for visual)
    ax2.fill_between(mus, 0, 1, where=(mus < threshold), alpha=0.3, color='red', label='D')
    ax2.fill_between(mus, 0, 1, where=(mus >= threshold), alpha=0.3, color='blue', label='C')
    ax2.axvline(threshold, color='green', linestyle='--', linewidth=2)
    ax2.set_xlim(0, 1)
    ax2.set_yticks([0.5])
    ax2.set_yticklabels(['Best\nResponse'])
    ax2.set_xlabel('Belief μ = Pr(θ=G)', fontsize=13)
    ax2.set_title('B(s₁, μ): Best Response Regions', fontsize=13)
    ax2.legend(fontsize=10, loc='center')

    fig.tight_layout()
    save_figure(fig, os.path.join(FIGURES_DIR, 'best_response_vs_belief.png'))
    print("Saved: figures/best_response_vs_belief.png")

    # ---- Simulation: track beliefs and threshold crossings ----
    print("\n--- Simulating belief dynamics ---")
    T = 5000
    states, beliefs, actions_lr, actions_sr = simulate_beliefs(mc, game, T=T)

    # Count threshold crossings
    above = beliefs > threshold
    crossings = np.where(np.diff(above.astype(int)) != 0)[0]
    n_crossings = len(crossings)
    crossing_rate = n_crossings / T

    # Time in each region
    frac_c_region = np.mean(beliefs > threshold)
    frac_d_region = np.mean(beliefs <= threshold)

    print(f"  Periods simulated: {T}")
    print(f"  Threshold crossings: {n_crossings}")
    print(f"  Crossing rate: {crossing_rate:.4f} per period")
    print(f"  Time in C region (μ>{threshold}): {frac_c_region*100:.1f}%")
    print(f"  Time in D region (μ≤{threshold}): {frac_d_region*100:.1f}%")
    print(f"  Mean belief: {beliefs.mean():.4f}")
    print(f"  Belief std: {beliefs.std():.4f}")
    print(f"  Stationary π(G): {mc.pi[0]:.4f}")

    # ---- Plot 2: Threshold crossings over time ----
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True)

    # Belief trajectory (first 500 periods for clarity)
    window = min(500, T)
    t_vals = np.arange(window)

    ax1.plot(t_vals, beliefs[:window], 'k-', linewidth=0.8, alpha=0.7)
    ax1.axhline(threshold, color='green', linestyle='--', linewidth=2, label=f'μ*={threshold}')
    ax1.axhline(mc.pi[0], color='purple', linestyle=':', linewidth=1.5, label=f'π(G)={mc.pi[0]:.3f}')
    ax1.fill_between(t_vals, 0, 1, where=(beliefs[:window] > threshold),
                     alpha=0.1, color='blue')
    ax1.fill_between(t_vals, 0, 1, where=(beliefs[:window] <= threshold),
                     alpha=0.1, color='red')
    ax1.set_ylabel('SR Belief μ_t', fontsize=12)
    ax1.set_title(f'SR Belief Trajectory and Threshold Crossings (first {window} periods)', fontsize=13)
    ax1.legend(fontsize=10)
    ax1.set_ylim(0, 1)
    ax1.grid(True, alpha=0.3)

    # Mark crossings
    cross_in_window = crossings[crossings < window]
    for c in cross_in_window:
        ax1.axvline(c, color='orange', linewidth=0.5, alpha=0.5)

    # Cumulative crossings
    cum_crossings = np.cumsum(np.abs(np.diff(above[:window].astype(int))))
    ax2.plot(t_vals[1:], cum_crossings, 'orange', linewidth=2)
    ax2.set_xlabel('Period t', fontsize=12)
    ax2.set_ylabel('Cumulative crossings', fontsize=12)
    ax2.set_title('Cumulative Threshold Crossings', fontsize=13)
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    save_figure(fig, os.path.join(FIGURES_DIR, 'threshold_crossings.png'))
    print("Saved: figures/threshold_crossings.png")

    # ---- Generate report ----
    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write("# SSA6_1: SR Player Best Response — Report\n\n")

        f.write("## SR Payoff Structure\n\n")
        f.write("| State | Action C | Action D |\n")
        f.write("|-------|----------|----------|\n")
        f.write("| G     | 1.0      | 0.0      |\n")
        f.write("| B     | -1.0     | 0.5      |\n\n")

        f.write("## Expected Payoffs\n\n")
        f.write("- E[u₂(C)] = μ·1 + (1−μ)·(−1) = **2μ − 1**\n")
        f.write("- E[u₂(D)] = μ·0 + (1−μ)·0.5 = **0.5(1−μ)**\n\n")

        f.write("## Best Response Threshold\n\n")
        f.write(f"SR plays C iff 2μ−1 > 0.5(1−μ) ⟺ **μ > μ* = {threshold}**\n\n")

        f.write("## Simulation Results\n\n")
        f.write(f"- Periods: {T}\n")
        f.write(f"- Threshold crossings: {n_crossings}\n")
        f.write(f"- Crossing rate: {crossing_rate:.4f}/period\n")
        f.write(f"- Time in C region: {frac_c_region*100:.1f}%\n")
        f.write(f"- Time in D region: {frac_d_region*100:.1f}%\n")
        f.write(f"- Mean belief: {beliefs.mean():.4f}\n")
        f.write(f"- Stationary π(G): {mc.pi[0]:.4f}\n\n")

        f.write("## Interpretation\n\n")
        f.write(f"The SR best-response threshold μ*={threshold} lies ")
        if threshold < mc.pi[0]:
            f.write(f"below the stationary belief π(G)={mc.pi[0]:.4f}. ")
            f.write("This means that at stationarity, SR would cooperate (play C). ")
        else:
            f.write(f"above the stationary belief π(G)={mc.pi[0]:.4f}. ")
            f.write("This means that at stationarity, SR would defect (play D). ")

        f.write("However, with Bayesian filtering, the belief μ_t fluctuates around π(G) ")
        f.write(f"and crosses the threshold {n_crossings} times in {T} periods. ")
        f.write("Each crossing changes SR's action, which affects LR's actual payoff.\n\n")

        f.write("This confirms that the filtering distribution matters: even when the stationary ")
        f.write("belief is in one BR region, the actual beliefs can cross into the other.\n\n")

        f.write("## Figures\n")
        f.write("![Best Response vs Belief](figures/best_response_vs_belief.png)\n\n")
        f.write("![Threshold Crossings](figures/threshold_crossings.png)\n")

    print(f"\nReport saved to: {report_path}")
    print("\nDone.")


if __name__ == '__main__':
    main()
