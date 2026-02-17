#!/usr/bin/env python3
"""
SSA6_2: Full Game Simulation with Belief-Dependent SR Responses
Compares LR payoffs when SR uses stationary vs filtered beliefs.
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

# SR payoff matrix (same as SSA6_1)
U2 = np.array([
    [1.0, 0.0],    # State G: [C, D]
    [-1.0, 0.5]    # State B: [C, D]
])
SR_THRESHOLD = 0.6  # mu* = 3/5


def sr_best_response_action(mu):
    """SR best response: C (0) if mu > threshold, D (1) otherwise."""
    if mu > SR_THRESHOLD:
        return 0  # C
    else:
        return 1  # D


def lr_payoff(state, lr_action, sr_action, game):
    """
    LR payoff depends on state and both actions.
    We model LR payoff as:
      - Base payoff u1(state, lr_action) from the deterrence game
      - Bonus/penalty from SR cooperation:
        if SR plays C, LR gets full u1; if SR plays D, LR gets reduced payoff
    For simplicity: LR payoff = u1(state, lr_action) * (1 if sr=C, else 0.5)
    Actually, to keep it clean, let's use u1 directly and add SR effect:
    LR_payoff = u1(state, lr_action) if SR cooperates
    LR_payoff = u1(state, lr_action) * 0.5 if SR defects
    """
    base = game.u1[state, lr_action]
    if sr_action == 0:  # C
        return base
    else:  # D
        return base * 0.5


def simulate_scenario(mc, game, T, use_filtering, rng):
    """
    Simulate one scenario.

    Parameters
    ----------
    use_filtering : bool
        If True, SR uses Bayesian filtering. If False, SR always uses pi(G).
    """
    states = mc.simulate(T, rng=rng)
    strat_mat = make_strategy_matrix(game.stackelberg_strategy)

    bf = BayesianFilter(mc) if use_filtering else None

    beliefs = np.zeros(T)
    lr_actions = np.zeros(T, dtype=int)
    sr_actions = np.zeros(T, dtype=int)
    lr_payoffs = np.zeros(T)

    for t in range(T):
        # LR plays Stackelberg
        lr_actions[t] = game.stackelberg_strategy(states[t])

        # SR belief
        if use_filtering and bf is not None:
            mu_t = bf.belief[0]
        else:
            mu_t = mc.pi[0]  # always stationary

        beliefs[t] = mu_t

        # SR best response
        sr_actions[t] = sr_best_response_action(mu_t)

        # LR payoff
        lr_payoffs[t] = lr_payoff(states[t], lr_actions[t], sr_actions[t], game)

        # Update filter
        if use_filtering and bf is not None and t < T - 1:
            bf.update(lr_actions[t], strat_mat)

    return {
        'states': states,
        'beliefs': beliefs,
        'lr_actions': lr_actions,
        'sr_actions': sr_actions,
        'lr_payoffs': lr_payoffs,
    }


def main():
    print("=" * 60)
    print("SSA6_2: Full Game Simulation")
    print("=" * 60)

    mc = MarkovChain(alpha=0.3, beta=0.5)
    game = DeterrenceGame(x=0.3, y=0.4)
    T = 5000
    n_runs = 20  # multiple runs for robustness

    print(f"\nParameters: α={mc.alpha}, β={mc.beta}, T={T}, runs={n_runs}")
    print(f"SR threshold: μ* = {SR_THRESHOLD}")
    print(f"Stationary π(G) = {mc.pi[0]:.4f}")

    # Run multiple simulations
    payoff_diffs = []
    action_disagree_rates = []

    # Single detailed run for plotting
    rng = np.random.default_rng(42)
    res_stat = simulate_scenario(mc, game, T, use_filtering=False, rng=np.random.default_rng(42))
    res_filt = simulate_scenario(mc, game, T, use_filtering=True, rng=np.random.default_rng(42))

    # Same state sequence because same seed
    assert np.array_equal(res_stat['states'], res_filt['states']), \
        "State sequences should match for same seed"

    for run in range(n_runs):
        seed = 1000 + run
        r_stat = simulate_scenario(mc, game, T, use_filtering=False, rng=np.random.default_rng(seed))
        r_filt = simulate_scenario(mc, game, T, use_filtering=True, rng=np.random.default_rng(seed))

        avg_payoff_stat = r_stat['lr_payoffs'].mean()
        avg_payoff_filt = r_filt['lr_payoffs'].mean()
        payoff_diffs.append(avg_payoff_stat - avg_payoff_filt)

        disagree = np.mean(r_stat['sr_actions'] != r_filt['sr_actions'])
        action_disagree_rates.append(disagree)

    payoff_diffs = np.array(payoff_diffs)
    action_disagree_rates = np.array(action_disagree_rates)

    # Summary stats
    print("\n--- Results across runs ---")
    print(f"  LR avg payoff (stationary): {res_stat['lr_payoffs'].mean():.4f}")
    print(f"  LR avg payoff (filtered):   {res_filt['lr_payoffs'].mean():.4f}")
    print(f"\n  Payoff difference (stat - filt):")
    print(f"    Mean: {payoff_diffs.mean():.4f}")
    print(f"    Std:  {payoff_diffs.std():.4f}")
    print(f"    Min:  {payoff_diffs.min():.4f}")
    print(f"    Max:  {payoff_diffs.max():.4f}")
    print(f"\n  SR action disagreement rate:")
    print(f"    Mean: {action_disagree_rates.mean():.4f}")
    print(f"    Std:  {action_disagree_rates.std():.4f}")

    # ---- Plot 1: Payoff comparison ----
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Cumulative average payoff
    ax = axes[0, 0]
    cum_stat = np.cumsum(res_stat['lr_payoffs']) / np.arange(1, T + 1)
    cum_filt = np.cumsum(res_filt['lr_payoffs']) / np.arange(1, T + 1)
    ax.plot(cum_stat, 'b-', linewidth=1.5, label='Stationary belief', alpha=0.8)
    ax.plot(cum_filt, 'r-', linewidth=1.5, label='Filtered belief', alpha=0.8)
    ax.set_xlabel('Period', fontsize=11)
    ax.set_ylabel('Cumulative avg LR payoff', fontsize=11)
    ax.set_title('Cumulative Average LR Payoff', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # Rolling average payoff (window=100)
    ax = axes[0, 1]
    window = 100
    if T >= window:
        roll_stat = np.convolve(res_stat['lr_payoffs'], np.ones(window)/window, mode='valid')
        roll_filt = np.convolve(res_filt['lr_payoffs'], np.ones(window)/window, mode='valid')
        ax.plot(roll_stat, 'b-', linewidth=1, label='Stationary', alpha=0.7)
        ax.plot(roll_filt, 'r-', linewidth=1, label='Filtered', alpha=0.7)
    ax.set_xlabel('Period', fontsize=11)
    ax.set_ylabel(f'Rolling avg (w={window})', fontsize=11)
    ax.set_title(f'Rolling Average LR Payoff', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # Payoff difference histogram across runs
    ax = axes[1, 0]
    ax.hist(payoff_diffs, bins=15, color='purple', alpha=0.7, edgecolor='black')
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(payoff_diffs.mean(), color='red', linestyle='--', linewidth=2,
               label=f'Mean={payoff_diffs.mean():.4f}')
    ax.set_xlabel('Payoff difference (stationary − filtered)', fontsize=11)
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title(f'LR Payoff Difference Distribution (n={n_runs})', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # Action disagreement histogram
    ax = axes[1, 1]
    ax.hist(action_disagree_rates, bins=15, color='orange', alpha=0.7, edgecolor='black')
    ax.axvline(action_disagree_rates.mean(), color='red', linestyle='--', linewidth=2,
               label=f'Mean={action_disagree_rates.mean():.4f}')
    ax.set_xlabel('SR action disagreement rate', fontsize=11)
    ax.set_ylabel('Count', fontsize=11)
    ax.set_title('SR Action Disagreement Across Runs', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.suptitle('LR Payoff: Stationary vs Filtered Beliefs', fontsize=15, y=1.02)
    fig.tight_layout()
    save_figure(fig, os.path.join(FIGURES_DIR, 'payoff_comparison.png'))
    print("\nSaved: figures/payoff_comparison.png")

    # ---- Plot 2: Detailed disagreement analysis ----
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    # SR actions over time (first 300 periods)
    ax = axes[0]
    show_t = min(300, T)
    t_vals = np.arange(show_t)

    disagree_mask = res_stat['sr_actions'][:show_t] != res_filt['sr_actions'][:show_t]
    ax.scatter(t_vals[disagree_mask], np.ones(disagree_mask.sum()) * 0.5,
               color='red', s=15, alpha=0.5, label='Disagreement', zorder=5)
    ax.plot(t_vals, res_filt['beliefs'][:show_t], 'k-', linewidth=0.7, alpha=0.5,
            label='Filtered belief')
    ax.axhline(SR_THRESHOLD, color='green', linestyle='--', linewidth=2,
               label=f'μ*={SR_THRESHOLD}')
    ax.axhline(mc.pi[0], color='purple', linestyle=':', linewidth=1.5,
               label=f'π(G)={mc.pi[0]:.3f}')
    ax.set_xlabel('Period', fontsize=11)
    ax.set_ylabel('SR belief / Disagreement', fontsize=11)
    ax.set_title(f'SR Action Disagreements (first {show_t} periods)', fontsize=13)
    ax.legend(fontsize=9, loc='upper right')
    ax.grid(True, alpha=0.3)

    # Cumulative disagreement
    ax = axes[1]
    disagree_full = (res_stat['sr_actions'] != res_filt['sr_actions']).astype(float)
    cum_disagree = np.cumsum(disagree_full) / np.arange(1, T + 1)
    ax.plot(cum_disagree, 'red', linewidth=2)
    ax.set_xlabel('Period', fontsize=11)
    ax.set_ylabel('Cumulative disagreement rate', fontsize=11)
    ax.set_title('Cumulative SR Action Disagreement Rate', fontsize=13)
    ax.grid(True, alpha=0.3)
    ax.axhline(action_disagree_rates.mean(), color='orange', linestyle='--',
               linewidth=1.5, label=f'Cross-run mean={action_disagree_rates.mean():.4f}')
    ax.legend(fontsize=10)

    fig.tight_layout()
    save_figure(fig, os.path.join(FIGURES_DIR, 'sr_action_disagreement.png'))
    print("Saved: figures/sr_action_disagreement.png")

    # ---- Generate report ----
    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write("# SSA6_2: Full Game Simulation — Report\n\n")

        f.write("## Setup\n")
        f.write(f"- Markov chain: α={mc.alpha}, β={mc.beta}\n")
        f.write(f"- Game: x={game.x}, y={game.y}\n")
        f.write(f"- Periods: T={T}, Runs: {n_runs}\n")
        f.write(f"- LR strategy: Stackelberg (A in G, F in B)\n")
        f.write(f"- SR threshold: μ* = {SR_THRESHOLD}\n")
        f.write(f"- Stationary π(G) = {mc.pi[0]:.4f}\n\n")

        f.write("## Two Scenarios\n\n")
        f.write("| Scenario | Description |\n")
        f.write("|----------|-------------|\n")
        f.write("| (a) Stationary | SR always believes μ = π(G) — paper's assumption |\n")
        f.write("| (b) Filtered | SR uses Bayesian filter on observed actions — reality |\n\n")

        f.write("## Key Results\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| LR avg payoff (stationary) | {res_stat['lr_payoffs'].mean():.4f} |\n")
        f.write(f"| LR avg payoff (filtered) | {res_filt['lr_payoffs'].mean():.4f} |\n")
        f.write(f"| Mean payoff difference | {payoff_diffs.mean():.4f} ± {payoff_diffs.std():.4f} |\n")
        f.write(f"| Mean SR disagreement rate | {action_disagree_rates.mean():.4f} ± {action_disagree_rates.std():.4f} |\n\n")

        f.write("## Analysis\n\n")
        avg_disagree = action_disagree_rates.mean()
        if avg_disagree > 0.01:
            f.write(f"The SR player's action differs between stationary and filtered scenarios ")
            f.write(f"in **{avg_disagree*100:.1f}%** of periods on average. ")
            f.write(f"This means the paper's assumption (that SR always uses π) leads to ")
            f.write(f"incorrect SR actions a non-trivial fraction of the time.\n\n")

            if abs(payoff_diffs.mean()) > 0.01:
                direction = "higher" if payoff_diffs.mean() > 0 else "lower"
                f.write(f"The stationary assumption gives LR a {direction} average payoff by ")
                f.write(f"{abs(payoff_diffs.mean()):.4f}, which suggests the paper's commitment ")
                f.write(f"payoff calculation is {'optimistic' if payoff_diffs.mean() > 0 else 'pessimistic'}.\n\n")
            else:
                f.write("Despite the action disagreements, the average LR payoff difference is small. ")
                f.write("This suggests the disagreements may roughly cancel out over time.\n\n")
        else:
            f.write("The SR action disagreement rate is very low. For these parameters, the ")
            f.write("stationary assumption is a good approximation of filtered beliefs.\n\n")

        f.write("## Figures\n")
        f.write("![Payoff Comparison](figures/payoff_comparison.png)\n\n")
        f.write("![SR Action Disagreement](figures/sr_action_disagreement.png)\n")

    print(f"\nReport saved to: {report_path}")
    print("\nDone.")


if __name__ == '__main__':
    main()
