#!/usr/bin/env python3
"""SSA2_1: State-Revealing Strategy Simulation — demonstrates persistent belief gap."""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from shared.markov_utils import MarkovChain, DeterrenceGame, tv_distance, save_figure

FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)

T_STEPS = 5000


def run_revealing_sim(alpha, beta, rng):
    """Simulate the state-revealing strategy and track belief gaps."""
    mc = MarkovChain(alpha=alpha, beta=beta)
    game = DeterrenceGame()

    states = mc.simulate(T_STEPS, rng=rng)

    # Under s₁*(G)=A, s₁*(B)=F, observing the action reveals θ_t exactly.
    # SR player's belief about θ_{t+1} is F(·|θ_t), not π.
    sr_belief_G = np.zeros(T_STEPS)  # Pr(G next period) as believed by SR
    pi_G = mc.pi[0]
    belief_gap = np.zeros(T_STEPS)

    # At t=0, SR starts with prior π
    sr_belief_G[0] = pi_G
    belief_gap[0] = 0.0

    for t in range(1, T_STEPS):
        # After observing action at time t-1, SR knows θ_{t-1}
        theta_prev = states[t - 1]
        # SR belief about θ_t is F(·|θ_{t-1})
        sr_belief_G[t] = mc.T[theta_prev, 0]  # Pr(G | θ_{t-1})
        belief_gap[t] = abs(sr_belief_G[t] - pi_G)

    # Theoretical gaps
    gap_after_G = abs((1 - alpha) - pi_G)
    gap_after_B = abs(beta - pi_G)
    expected_gap = pi_G * gap_after_G + (1 - pi_G) * gap_after_B

    return {
        'states': states,
        'sr_belief_G': sr_belief_G,
        'belief_gap': belief_gap,
        'pi_G': pi_G,
        'alpha': alpha,
        'beta': beta,
        'gap_after_G': gap_after_G,
        'gap_after_B': gap_after_B,
        'expected_gap': expected_gap,
        'F_G_given_G': 1 - alpha,
        'F_G_given_B': beta,
    }


def plot_revealed_belief(results):
    """Plot belief trajectory showing it tracks F(·|θ_t), not π."""
    t_show = 500
    t_range = np.arange(t_show)

    fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

    # Top: SR belief vs π
    ax = axes[0]
    ax.fill_between(t_range, 0, 1, where=results['states'][:t_show] == 0,
                     alpha=0.15, color='green', label='State G')
    ax.fill_between(t_range, 0, 1, where=results['states'][:t_show] == 1,
                     alpha=0.15, color='red', label='State B')

    ax.plot(t_range, results['sr_belief_G'][:t_show], 'b-', linewidth=1.2,
            label='SR belief Pr(G next)')
    ax.axhline(y=results['pi_G'], color='black', linestyle='--', linewidth=2,
                label=f"π(G) = {results['pi_G']:.3f}")
    ax.axhline(y=results['F_G_given_G'], color='green', linestyle=':',
                linewidth=1.5, label=f"F(G|G) = {results['F_G_given_G']:.3f}")
    ax.axhline(y=results['F_G_given_B'], color='red', linestyle=':',
                linewidth=1.5, label=f"F(G|B) = {results['F_G_given_B']:.3f}")

    ax.set_ylabel('Pr(G next period)', fontsize=12)
    ax.set_title(f"State-Revealing Strategy: SR Belief ≠ π "
                 f"(α={results['alpha']}, β={results['beta']})", fontsize=13)
    ax.legend(loc='upper right', fontsize=9)
    ax.set_ylim(-0.05, 1.05)

    # Bottom: belief gap
    ax = axes[1]
    ax.plot(t_range, results['belief_gap'][:t_show], 'purple', linewidth=1.0)
    ax.axhline(y=results['expected_gap'], color='red', linestyle='--', linewidth=2,
                label=f"E[gap] = {results['expected_gap']:.4f}")
    ax.axhline(y=results['gap_after_G'], color='green', linestyle=':',
                linewidth=1.5, label=f"Gap after G = {results['gap_after_G']:.4f}")
    ax.axhline(y=results['gap_after_B'], color='darkred', linestyle=':',
                linewidth=1.5, label=f"Gap after B = {results['gap_after_B']:.4f}")

    ax.set_ylabel('|SR belief − π(G)|', fontsize=12)
    ax.set_xlabel('Time step', fontsize=12)
    ax.set_title('Persistent Belief Gap: NEVER Converges to Zero', fontsize=13)
    ax.legend(loc='upper right', fontsize=9)

    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'revealed_belief_trajectory.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")


def plot_gap_persistent(results_list):
    """Plot belief gap over full trajectory for multiple parameter settings."""
    fig, ax = plt.subplots(figsize=(14, 5))

    for res in results_list:
        label = f"α={res['alpha']}, β={res['beta']} (E[gap]={res['expected_gap']:.4f})"
        # Rolling average of gap
        window = 100
        gap = res['belief_gap']
        rolling = np.convolve(gap, np.ones(window) / window, mode='valid')
        ax.plot(np.arange(len(rolling)), rolling, linewidth=1.2, label=label)

    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.set_xlabel('Time step', fontsize=12)
    ax.set_ylabel('Rolling avg |SR belief − π(G)|', fontsize=12)
    ax.set_title(f'Belief Gap is Persistent Across Parameter Settings (T={T_STEPS})',
                  fontsize=13)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'belief_gap_persistent.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")


def write_report(results_list):
    """Generate report.md."""
    report = f"""# SSA2_1: State-Revealing Strategy Simulation — Report

## Summary

When the LR player uses the commitment strategy s₁*(G)=A, s₁*(B)=F, the action at each
period reveals the state θ_t to the SR player. Therefore, the SR player's belief about
θ_{{t+1}} is the conditional distribution F(·|θ_t), NOT the stationary distribution π.

## Analytical Results

For a 2-state Markov chain with parameters (α, β):
- F(G|G) = 1 − α, F(G|B) = β
- π(G) = β/(α+β)
- Gap after state G: |F(G|G) − π(G)| = |(1−α) − β/(α+β)| = α·|1−α−β|/(α+β)
- Gap after state B: |F(G|B) − π(G)| = |β − β/(α+β)| = α·β/(α+β)
- Expected gap: π(G)·gap_G + π(B)·gap_B

## Numerical Results

| α | β | π(G) | F(G|G) | F(G|B) | Gap after G | Gap after B | Expected Gap | Empirical Mean Gap |
|---|---|------|--------|--------|-------------|-------------|--------------|-------------------|
"""
    for res in results_list:
        emp_mean_gap = np.mean(res['belief_gap'][1:])
        report += (f"| {res['alpha']} | {res['beta']} | {res['pi_G']:.4f} | "
                   f"{res['F_G_given_G']:.4f} | {res['F_G_given_B']:.4f} | "
                   f"{res['gap_after_G']:.4f} | {res['gap_after_B']:.4f} | "
                   f"{res['expected_gap']:.4f} | {emp_mean_gap:.4f} |\n")

    report += """
## Key Finding

**The belief gap is PERMANENT.** Under a state-revealing strategy:
- Every period, the SR player learns the current state exactly.
- Their belief about the next state is F(·|θ_t), not π.
- The gap |F(·|θ_t) − π| never shrinks because new observations always override
  any convergence toward π.
- This gap is zero ONLY when α + β = 1 (i.e., the chain is i.i.d.).

This directly contradicts the paper's implicit assumption that SR beliefs can be
characterized by the stationary distribution on the lifted state space.

## Figures

![Revealed Belief Trajectory](figures/revealed_belief_trajectory.png)
![Persistent Gap](figures/belief_gap_persistent.png)
"""

    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Saved: {report_path}")


if __name__ == '__main__':
    print("=" * 60)
    print("SSA2_1: State-Revealing Strategy Simulation")
    print("=" * 60)

    rng = np.random.default_rng(789)

    param_sets = [
        (0.3, 0.5),   # baseline
        (0.1, 0.1),   # high persistence
        (0.05, 0.05), # very high persistence
        (0.5, 0.5),   # near i.i.d. (α+β=1)
    ]

    results_list = []
    for alpha, beta in param_sets:
        print(f"\n--- α={alpha}, β={beta} ---")
        res = run_revealing_sim(alpha, beta, rng)
        results_list.append(res)
        emp_gap = np.mean(res['belief_gap'][1:])
        print(f"  π(G) = {res['pi_G']:.4f}")
        print(f"  F(G|G) = {res['F_G_given_G']:.4f}, F(G|B) = {res['F_G_given_B']:.4f}")
        print(f"  Gap after G = {res['gap_after_G']:.4f}, after B = {res['gap_after_B']:.4f}")
        print(f"  Expected gap = {res['expected_gap']:.4f}, empirical = {emp_gap:.4f}")

    plot_revealed_belief(results_list[0])
    plot_gap_persistent(results_list)
    write_report(results_list)
    print("\nDone.")
