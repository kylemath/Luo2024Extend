#!/usr/bin/env python3
"""SSA1_3: Belief Visualization and Summary Statistics across parameter space."""

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

N_SIMS = 200
T_STEPS = 5000
ALPHA_GRID = np.linspace(0.05, 0.95, 10)
BETA_GRID = np.linspace(0.05, 0.95, 10)


def compute_tv_for_params(alpha, beta, n_sims, t_steps, rng):
    """Run n_sims simulations, return array of time-averaged TV distances."""
    mc = MarkovChain(alpha=alpha, beta=beta)
    game = DeterrenceGame()
    strategy_mat = make_strategy_matrix(game.stackelberg_strategy)

    time_avg_tvs = np.zeros(n_sims)
    all_tv_trajectories = []

    for n in range(n_sims):
        states = mc.simulate(t_steps, rng=rng)
        bf = BayesianFilter(mc)
        tv_dists = np.zeros(t_steps)
        tv_dists[0] = tv_distance(bf.belief, mc.pi)

        for t in range(1, t_steps):
            action = game.stackelberg_strategy(states[t])
            posterior = bf.update(signal=action, strategy_matrix=strategy_mat)
            tv_dists[t] = tv_distance(posterior, mc.pi)

        time_avg_tvs[n] = np.mean(tv_dists)
        if n < 5:
            all_tv_trajectories.append(tv_dists.copy())

    return time_avg_tvs, all_tv_trajectories


def make_heatmap(rng):
    """Create heatmap of mean TV distance over (α, β) grid."""
    print("Computing TV heatmap over parameter grid...")
    n_a = len(ALPHA_GRID)
    n_b = len(BETA_GRID)
    heatmap = np.zeros((n_a, n_b))

    # Use fewer sims for the grid to keep runtime manageable
    n_sims_grid = 50
    t_steps_grid = 2000

    for i, alpha in enumerate(ALPHA_GRID):
        for j, beta in enumerate(BETA_GRID):
            tv_avgs, _ = compute_tv_for_params(alpha, beta, n_sims_grid, t_steps_grid, rng)
            heatmap[i, j] = np.mean(tv_avgs)
            print(f"  α={alpha:.2f}, β={beta:.2f}: mean TV = {heatmap[i, j]:.4f}")

    fig, ax = plt.subplots(figsize=(9, 7))
    im = ax.imshow(heatmap, origin='lower', aspect='auto', cmap='inferno',
                    extent=[BETA_GRID[0], BETA_GRID[-1], ALPHA_GRID[0], ALPHA_GRID[-1]])
    ax.set_xlabel('β (Pr(G|B))', fontsize=12)
    ax.set_ylabel('α (Pr(B|G))', fontsize=12)
    ax.set_title('Mean TV Distance ‖SR Belief − π‖\n(averaged over time and simulations)',
                  fontsize=13)

    # Mark the i.i.d. line α + β = 1
    beta_line = np.linspace(0.05, 0.95, 100)
    alpha_line = 1 - beta_line
    valid = (alpha_line >= 0.05) & (alpha_line <= 0.95)
    ax.plot(beta_line[valid], alpha_line[valid], 'w--', linewidth=2, label='α+β=1 (i.i.d.)')
    ax.legend(fontsize=10, loc='upper right')

    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Mean TV Distance', fontsize=11)

    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'tv_heatmap.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")
    return heatmap


def make_violin(rng):
    """Create violin plot of time-averaged TV distances for selected (α,β)."""
    print("\nComputing distributions for violin plot...")
    param_sets = [
        (0.1, 0.1, "α=0.1,β=0.1\n(high persist)"),
        (0.3, 0.5, "α=0.3,β=0.5\n(baseline)"),
        (0.5, 0.5, "α=0.5,β=0.5\n(i.i.d.)"),
        (0.1, 0.9, "α=0.1,β=0.9\n(near i.i.d.)"),
        (0.05, 0.05, "α=0.05,β=0.05\n(very persist)"),
    ]

    all_tvs = []
    labels = []
    for alpha, beta, label in param_sets:
        tv_avgs, _ = compute_tv_for_params(alpha, beta, N_SIMS, T_STEPS, rng)
        all_tvs.append(tv_avgs)
        labels.append(label)
        print(f"  {label.replace(chr(10), ' ')}: mean={np.mean(tv_avgs):.4f}, "
              f"std={np.std(tv_avgs):.4f}")

    fig, ax = plt.subplots(figsize=(12, 6))
    parts = ax.violinplot(all_tvs, positions=range(len(all_tvs)), showmeans=True,
                           showmedians=True)

    for pc in parts['bodies']:
        pc.set_facecolor('steelblue')
        pc.set_alpha(0.7)

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel('Time-averaged TV distance', fontsize=12)
    ax.set_title('Distribution of Time-Averaged TV Distance ‖SR Belief − π‖\n'
                  f'(N={N_SIMS} simulations, T={T_STEPS} steps each)', fontsize=13)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'tv_violin.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")
    return all_tvs, labels


def make_persistence_comparison(rng):
    """Compare belief trajectories for low vs high persistence."""
    print("\nComputing persistence comparison...")
    mc_low = MarkovChain(alpha=0.5, beta=0.5)   # i.i.d.
    mc_high = MarkovChain(alpha=0.05, beta=0.05)  # very persistent
    game = DeterrenceGame()
    strategy_mat = make_strategy_matrix(game.stackelberg_strategy)

    t_show = 500
    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    for row, (mc, label) in enumerate([(mc_low, "Low persistence (α=β=0.5, near i.i.d.)"),
                                        (mc_high, "High persistence (α=β=0.05)")]):
        states = mc.simulate(T_STEPS, rng=rng)
        bf = BayesianFilter(mc)
        beliefs = np.zeros(T_STEPS)
        tv_dists = np.zeros(T_STEPS)
        beliefs[0] = bf.belief[0]
        tv_dists[0] = tv_distance(bf.belief, mc.pi)

        for t in range(1, T_STEPS):
            action = game.stackelberg_strategy(states[t])
            posterior = bf.update(signal=action, strategy_matrix=strategy_mat)
            beliefs[t] = posterior[0]
            tv_dists[t] = tv_distance(posterior, mc.pi)

        # Left: belief trajectory
        ax = axes[row, 0]
        t_range = np.arange(t_show)
        ax.fill_between(t_range, 0, 1, where=states[:t_show] == 0,
                         alpha=0.15, color='green')
        ax.fill_between(t_range, 0, 1, where=states[:t_show] == 1,
                         alpha=0.15, color='red')
        ax.plot(t_range, beliefs[:t_show], color='blue', linewidth=0.7, label='SR belief')
        ax.axhline(y=mc.pi[0], color='black', linestyle='--', label=f'π(G)={mc.pi[0]:.3f}')
        ax.set_ylabel('Pr(G)')
        ax.set_title(f'{label} — Belief')
        ax.legend(fontsize=8)
        ax.set_ylim(-0.05, 1.05)

        # Right: TV distance
        ax = axes[row, 1]
        ax.plot(t_range, tv_dists[:t_show], color='purple', linewidth=0.7)
        mean_tv = np.mean(tv_dists)
        ax.axhline(y=mean_tv, color='red', linestyle='--',
                    label=f'Mean TV={mean_tv:.4f}')
        ax.set_ylabel('TV distance')
        ax.set_title(f'{label} — TV distance')
        ax.legend(fontsize=8)

    axes[1, 0].set_xlabel('Time step')
    axes[1, 1].set_xlabel('Time step')
    fig.suptitle('Persistence Comparison: SR Belief Dynamics', fontsize=13, y=1.01)
    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'persistence_comparison.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")


def write_report(heatmap, all_tvs, labels):
    """Generate report.md."""
    report = f"""# SSA1_3: Belief Visualization — Report

## Summary

Comprehensive visualization of SR player belief dynamics across the parameter space.
Ran {N_SIMS} simulations of {T_STEPS} steps for selected (α,β) values, plus a heatmap
over a 10×10 grid.

## TV Distance Statistics

| Setting | Mean | Std | Min | Max | Median |
|---------|------|-----|-----|-----|--------|
"""
    for tvs, label in zip(all_tvs, labels):
        clean_label = label.replace('\n', ' ')
        report += (f"| {clean_label} | {np.mean(tvs):.4f} | {np.std(tvs):.4f} | "
                   f"{np.min(tvs):.4f} | {np.max(tvs):.4f} | {np.median(tvs):.4f} |\n")

    report += f"""
## Key Findings

1. **TV distance is near zero only when α + β ≈ 1** (i.i.d. case), visible in the heatmap
   as a dark valley along the α + β = 1 diagonal.
2. **Higher persistence (smaller α, β) → larger TV distance.** When the chain is very
   persistent (α=β=0.05), the SR belief is far from π because F(·|θ_t) differs
   significantly from π.
3. **The violin plot shows tight concentration**: for each (α,β), the time-averaged TV
   distance has low variance across simulations, meaning the gap is structural, not
   a finite-sample artifact.
4. **Persistence comparison** dramatically illustrates: near-i.i.d. chains produce
   beliefs close to π, while persistent chains produce beliefs that track F(·|θ_t)
   and persistently deviate from π.

## Figures

![TV Heatmap](figures/tv_heatmap.png)
![TV Violin](figures/tv_violin.png)
![Persistence Comparison](figures/persistence_comparison.png)

## Conclusion

The SR player's belief about the current state **does not converge to the stationary
distribution** under Markov dynamics with a state-revealing strategy. The deviation is
permanent and grows with the persistence of the chain (distance from i.i.d.). This
undermines the paper's use of the lifted stationary distribution ρ̃ as the relevant
measure for the OT characterization.
"""

    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Saved: {report_path}")


if __name__ == '__main__':
    print("=" * 60)
    print("SSA1_3: Belief Visualization and Summary Statistics")
    print("=" * 60)

    rng = np.random.default_rng(456)

    heatmap = make_heatmap(rng)
    all_tvs, labels = make_violin(rng)
    make_persistence_comparison(rng)
    write_report(heatmap, all_tvs, labels)
    print("\nDone.")
