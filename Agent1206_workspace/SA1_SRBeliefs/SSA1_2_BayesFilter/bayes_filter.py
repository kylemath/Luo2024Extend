#!/usr/bin/env python3
"""SSA1_2: Bayesian Filter for SR Player Beliefs under Markov state dynamics."""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from shared.markov_utils import (MarkovChain, DeterrenceGame, BayesianFilter,
                                  make_strategy_matrix, tv_distance, save_figure)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)

T_STEPS = 10000


def run_belief_tracking(alpha, beta, label, rng):
    """Run one belief-tracking simulation and return results."""
    mc = MarkovChain(alpha=alpha, beta=beta)
    game = DeterrenceGame()
    strategy_mat = make_strategy_matrix(game.stackelberg_strategy)

    # Simulate state sequence
    states = mc.simulate(T_STEPS, rng=rng)

    # Run Bayesian filter
    bf = BayesianFilter(mc)
    beliefs = np.zeros(T_STEPS)
    tv_distances = np.zeros(T_STEPS)

    beliefs[0] = bf.belief[0]
    tv_distances[0] = tv_distance(bf.belief, mc.pi)

    for t in range(1, T_STEPS):
        # SR observes action chosen by commitment type in state theta_t
        action = game.stackelberg_strategy(states[t])
        posterior = bf.update(signal=action, strategy_matrix=strategy_mat)
        beliefs[t] = posterior[0]  # Pr(G)
        tv_distances[t] = tv_distance(posterior, mc.pi)

    # Conditional beliefs: what SR SHOULD believe if they knew theta_{t-1}
    conditional_beliefs = np.zeros(T_STEPS)
    conditional_beliefs[0] = mc.pi[0]
    for t in range(1, T_STEPS):
        conditional_beliefs[t] = mc.T[states[t-1], 0]  # Pr(G | theta_{t-1})

    return {
        'states': states,
        'beliefs': beliefs,
        'tv_distances': tv_distances,
        'conditional_beliefs': conditional_beliefs,
        'pi_G': mc.pi[0],
        'alpha': alpha,
        'beta': beta,
        'label': label
    }


def plot_belief_trajectory(results_list):
    """Plot belief trajectories for multiple parameter settings."""
    n = len(results_list)
    fig, axes = plt.subplots(n, 1, figsize=(14, 5 * n), sharex=True)
    if n == 1:
        axes = [axes]

    for ax, res in zip(axes, results_list):
        t_range = np.arange(T_STEPS)
        t_show = min(2000, T_STEPS)

        # True state as background
        state_colors = np.where(res['states'][:t_show] == 0, 0.9, 0.1)
        ax.fill_between(t_range[:t_show], 0, 1, where=res['states'][:t_show] == 0,
                         alpha=0.15, color='green', label='State G')
        ax.fill_between(t_range[:t_show], 0, 1, where=res['states'][:t_show] == 1,
                         alpha=0.15, color='red', label='State B')

        # SR belief
        ax.plot(t_range[:t_show], res['beliefs'][:t_show],
                color='blue', linewidth=0.5, alpha=0.8, label='SR belief Pr(G)')

        # Stationary distribution
        ax.axhline(y=res['pi_G'], color='black', linestyle='--',
                    linewidth=1.5, label=f"π(G)={res['pi_G']:.3f}")

        # Conditional belief
        ax.plot(t_range[:t_show], res['conditional_beliefs'][:t_show],
                color='orange', linewidth=0.5, alpha=0.6, label='F(G|θ_{t-1})')

        ax.set_ylabel('Pr(G)')
        ax.set_title(f"{res['label']}: α={res['alpha']}, β={res['beta']}")
        ax.legend(loc='upper right', fontsize=8)
        ax.set_ylim(-0.05, 1.05)

    axes[-1].set_xlabel('Time step')
    fig.suptitle('SR Player Belief Trajectories Under Commitment Strategy', fontsize=13, y=1.01)
    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'belief_trajectory.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")


def plot_tv_distance(results_list):
    """Plot TV distance over time."""
    fig, axes = plt.subplots(len(results_list), 1, figsize=(14, 4 * len(results_list)),
                              sharex=True)
    if len(results_list) == 1:
        axes = [axes]

    for ax, res in zip(axes, results_list):
        t_range = np.arange(T_STEPS)

        # Raw TV distance
        ax.plot(t_range, res['tv_distances'], color='purple',
                linewidth=0.3, alpha=0.5, label='TV(belief, π)')

        # Rolling average
        window = 200
        if T_STEPS > window:
            rolling_avg = np.convolve(res['tv_distances'],
                                       np.ones(window) / window, mode='valid')
            ax.plot(t_range[window-1:], rolling_avg, color='darkred',
                    linewidth=1.5, label=f'Rolling avg (w={window})')

        mean_tv = np.mean(res['tv_distances'])
        ax.axhline(y=mean_tv, color='black', linestyle='--',
                    linewidth=1, label=f'Mean TV={mean_tv:.4f}')

        ax.set_ylabel('TV distance')
        ax.set_title(f"{res['label']}: α={res['alpha']}, β={res['beta']}")
        ax.legend(loc='upper right', fontsize=8)

    axes[-1].set_xlabel('Time step')
    fig.suptitle('TV Distance ‖belief − π‖ Over Time', fontsize=13, y=1.01)
    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'tv_distance_timeseries.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")


def write_report(results_list):
    """Generate report.md."""
    report = f"""# SSA1_2: Bayesian Filter for SR Player Beliefs — Report

## Summary

Simulated the deterrence game with commitment strategy s₁*(G)=A, s₁*(B)=F for T={T_STEPS}
periods. The SR player uses a Bayesian filter (HMM forward algorithm) to update beliefs
about the current state θ_t after observing each action.

## Results

| Setting | α | β | π(G) | Mean TV | Median TV | Min TV | Max TV | Converges to π? |
|---------|---|---|------|---------|-----------|--------|--------|-----------------|
"""
    for res in results_list:
        tv = res['tv_distances']
        converges = "NO" if np.mean(tv[-1000:]) > 0.01 else "YES"
        report += (f"| {res['label']} | {res['alpha']} | {res['beta']} | "
                   f"{res['pi_G']:.4f} | {np.mean(tv):.4f} | {np.median(tv):.4f} | "
                   f"{np.min(tv):.4f} | {np.max(tv):.4f} | {converges} |\n")

    report += """
## Key Findings

"""
    for res in results_list:
        tv_last = np.mean(res['tv_distances'][-1000:])
        report += f"""### {res['label']} (α={res['alpha']}, β={res['beta']})

- Mean TV distance over full run: **{np.mean(res['tv_distances']):.4f}**
- Mean TV distance in last 1000 steps: **{tv_last:.4f}**
- The commitment strategy s₁*(G)=A, s₁*(B)=F **fully reveals** the state to the SR player.
- After observing action at time t, the SR player knows θ_t exactly.
- Therefore, the SR player's belief about θ_{{t+1}} is F(·|θ_t), NOT π.
- The TV distance ‖F(·|θ_t) − π‖ does NOT converge to zero — it fluctuates around a nonzero value.

"""

    report += """## Interpretation

The Bayesian filter with a state-revealing strategy does NOT produce beliefs that converge
to the stationary distribution π. Instead, each period's observation reveals the state,
and the belief about the NEXT period is the conditional distribution F(·|θ_t), which
differs from π whenever the chain has persistence (α + β ≠ 1).

This is the fundamental issue: the paper's OT characterization assumes SR beliefs are
well-approximated by the stationary distribution ρ̃ on the lifted space, but in practice,
SR beliefs track F(·|θ_t) and never "forget" the last observation.

## Figures

![Belief Trajectory](figures/belief_trajectory.png)
![TV Distance](figures/tv_distance_timeseries.png)
"""

    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Saved: {report_path}")


if __name__ == '__main__':
    print("=" * 60)
    print("SSA1_2: Bayesian Filter for SR Player Beliefs")
    print("=" * 60)

    rng = np.random.default_rng(123)

    results_list = []

    # Baseline: (α, β) = (0.3, 0.5)
    print("\n--- Baseline: α=0.3, β=0.5 ---")
    res1 = run_belief_tracking(0.3, 0.5, "Baseline", rng)
    results_list.append(res1)
    print(f"  Mean TV distance: {np.mean(res1['tv_distances']):.4f}")
    print(f"  Last 1000 mean TV: {np.mean(res1['tv_distances'][-1000:]):.4f}")

    # High persistence: (α, β) = (0.1, 0.1)
    print("\n--- High persistence: α=0.1, β=0.1 ---")
    res2 = run_belief_tracking(0.1, 0.1, "High persistence", rng)
    results_list.append(res2)
    print(f"  Mean TV distance: {np.mean(res2['tv_distances']):.4f}")
    print(f"  Last 1000 mean TV: {np.mean(res2['tv_distances'][-1000:]):.4f}")

    plot_belief_trajectory(results_list)
    plot_tv_distance(results_list)
    write_report(results_list)
    print("\nDone.")
