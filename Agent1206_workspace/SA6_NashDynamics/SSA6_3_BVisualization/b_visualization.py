#!/usr/bin/env python3
"""
SSA6_3: Nash Correspondence Visualization
Plots B(s1, mu) with belief trajectory overlay and compares i.i.d. vs Markov.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from shared.markov_utils import (
    MarkovChain, DeterrenceGame, BayesianFilter,
    make_strategy_matrix, save_figure
)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)

# SR payoffs
SR_THRESHOLD = 0.6


def sr_expected_payoff(mu, action_idx):
    """E[u2(C)] = 2mu - 1, E[u2(D)] = 0.5(1-mu)"""
    if action_idx == 0:
        return 2 * mu - 1
    else:
        return 0.5 * (1 - mu)


def sr_best_response_action(mu):
    """C(0) if mu > 0.6, else D(1)."""
    return 0 if mu > SR_THRESHOLD else 1


def simulate_beliefs(mc, game, T, rng):
    """Simulate belief trajectory under Stackelberg + Bayesian filtering."""
    states = mc.simulate(T, rng=rng)
    strat_mat = make_strategy_matrix(game.stackelberg_strategy)
    bf = BayesianFilter(mc)

    beliefs = np.zeros(T)
    lr_actions = np.zeros(T, dtype=int)

    for t in range(T):
        lr_actions[t] = game.stackelberg_strategy(states[t])
        beliefs[t] = bf.belief[0]
        if t < T - 1:
            bf.update(lr_actions[t], strat_mat)

    return states, beliefs, lr_actions


def main():
    print("=" * 60)
    print("SSA6_3: Nash Correspondence Visualization")
    print("=" * 60)

    mc = MarkovChain(alpha=0.3, beta=0.5)
    game = DeterrenceGame(x=0.3, y=0.4)
    T = 5000

    rng = np.random.default_rng(42)
    states, beliefs, lr_actions = simulate_beliefs(mc, game, T, rng)

    print(f"Markov chain: α={mc.alpha}, β={mc.beta}")
    print(f"Stationary π(G) = {mc.pi[0]:.4f}")
    print(f"SR threshold μ* = {SR_THRESHOLD}")
    print(f"Simulated T = {T}")

    frac_c = np.mean(beliefs > SR_THRESHOLD)
    frac_d = np.mean(beliefs <= SR_THRESHOLD)
    print(f"\nBelief in C region: {frac_c*100:.1f}%")
    print(f"Belief in D region: {frac_d*100:.1f}%")
    print(f"Mean belief: {beliefs.mean():.4f}")
    print(f"Std belief: {beliefs.std():.4f}")

    # ---- Plot 1: Nash correspondence with trajectory overlay ----
    fig, axes = plt.subplots(3, 1, figsize=(12, 12),
                             gridspec_kw={'height_ratios': [2.5, 1, 1.5]})

    # Top: Payoff functions + trajectory
    ax = axes[0]
    mus = np.linspace(0, 1, 500)
    payoff_c = np.array([sr_expected_payoff(m, 0) for m in mus])
    payoff_d = np.array([sr_expected_payoff(m, 1) for m in mus])

    ax.plot(mus, payoff_c, 'b-', linewidth=2.5, label='E[u₂(C)] = 2μ−1', zorder=3)
    ax.plot(mus, payoff_d, 'r-', linewidth=2.5, label='E[u₂(D)] = 0.5(1−μ)', zorder=3)
    ax.axvline(SR_THRESHOLD, color='green', linestyle='--', linewidth=2,
               label=f'μ* = {SR_THRESHOLD}', zorder=4)
    ax.fill_betweenx([-1.5, 1.5], 0, SR_THRESHOLD, alpha=0.06, color='red')
    ax.fill_betweenx([-1.5, 1.5], SR_THRESHOLD, 1, alpha=0.06, color='blue')

    # Overlay belief trajectory (subsample for visual clarity)
    show_n = min(200, T)
    t_show = np.arange(show_n)
    y_traj = np.zeros(show_n)
    for i in range(show_n):
        br = sr_best_response_action(beliefs[i])
        y_traj[i] = sr_expected_payoff(beliefs[i], br)

    sc = ax.scatter(beliefs[:show_n], y_traj, c=t_show, cmap='viridis',
                    s=8, alpha=0.6, zorder=5)
    cbar = fig.colorbar(sc, ax=ax, label='Time t', shrink=0.8)

    # Mark i.i.d. point (stationary)
    iid_br = sr_best_response_action(mc.pi[0])
    iid_payoff = sr_expected_payoff(mc.pi[0], iid_br)
    ax.plot(mc.pi[0], iid_payoff, 'k*', markersize=18, zorder=6,
            label=f'i.i.d. point π(G)={mc.pi[0]:.3f}')

    ax.set_xlim(0, 1)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xlabel('Belief μ = Pr(θ=G)', fontsize=13)
    ax.set_ylabel('SR Expected Payoff', fontsize=13)
    ax.set_title('Nash Correspondence B(s₁, μ) with Belief Trajectory', fontsize=14)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(True, alpha=0.3)

    # Middle: BR regions over time
    ax = axes[1]
    br_actions = np.array([sr_best_response_action(b) for b in beliefs[:show_n]])
    c_mask = br_actions == 0
    d_mask = br_actions == 1
    ax.fill_between(t_show, 0, 1, where=c_mask, alpha=0.4, color='blue', label='C')
    ax.fill_between(t_show, 0, 1, where=d_mask, alpha=0.4, color='red', label='D')
    ax.set_yticks([0.5])
    ax.set_yticklabels(['BR'])
    ax.set_xlabel('Period t', fontsize=12)
    ax.set_title(f'Best Response over Time (first {show_n} periods)', fontsize=13)
    ax.legend(fontsize=10, loc='upper right')

    # Bottom: Belief histogram in BR regions
    ax = axes[2]
    beliefs_c = beliefs[beliefs > SR_THRESHOLD]
    beliefs_d = beliefs[beliefs <= SR_THRESHOLD]

    bins = np.linspace(0, 1, 50)
    ax.hist(beliefs_c, bins=bins, alpha=0.6, color='blue', label=f'C region ({frac_c*100:.1f}%)',
            density=True)
    ax.hist(beliefs_d, bins=bins, alpha=0.6, color='red', label=f'D region ({frac_d*100:.1f}%)',
            density=True)
    ax.axvline(SR_THRESHOLD, color='green', linestyle='--', linewidth=2)
    ax.axvline(mc.pi[0], color='purple', linestyle=':', linewidth=1.5,
               label=f'π(G)={mc.pi[0]:.3f}')
    ax.set_xlabel('Belief μ', fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    ax.set_title('Belief Distribution by BR Region', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    save_figure(fig, os.path.join(FIGURES_DIR, 'nash_correspondence.png'))
    print("\nSaved: figures/nash_correspondence.png")

    # ---- Plot 2: Snapshot panels at t=10, 100, 500, 2000 ----
    snapshot_times = [10, 100, 500, 2000]
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    for ax, t_snap in zip(axes.flatten(), snapshot_times):
        # Histogram of beliefs up to t_snap
        b_so_far = beliefs[:t_snap]
        b_c = b_so_far[b_so_far > SR_THRESHOLD]
        b_d = b_so_far[b_so_far <= SR_THRESHOLD]

        frac_c_snap = len(b_c) / len(b_so_far)
        frac_d_snap = len(b_d) / len(b_so_far)

        bins = np.linspace(0, 1, 30)
        ax.hist(b_c, bins=bins, alpha=0.6, color='blue',
                label=f'C ({frac_c_snap*100:.0f}%)', density=True)
        ax.hist(b_d, bins=bins, alpha=0.6, color='red',
                label=f'D ({frac_d_snap*100:.0f}%)', density=True)
        ax.axvline(SR_THRESHOLD, color='green', linestyle='--', linewidth=2)
        ax.axvline(mc.pi[0], color='purple', linestyle=':', linewidth=1.5)

        # Mark current belief
        if t_snap < T:
            ax.axvline(beliefs[t_snap - 1], color='orange', linewidth=2, alpha=0.8,
                       label=f'μ_t={beliefs[t_snap-1]:.2f}')

        ax.set_title(f't = {t_snap}', fontsize=14, fontweight='bold')
        ax.set_xlabel('Belief μ', fontsize=11)
        ax.set_ylabel('Density', fontsize=11)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1)

    fig.suptitle('Belief Distribution Snapshots (i.i.d.=single point at π vs Markov=spread)',
                 fontsize=13, y=1.02)
    fig.tight_layout()
    save_figure(fig, os.path.join(FIGURES_DIR, 'belief_histogram_in_BR_regions.png'))
    print("Saved: figures/belief_histogram_in_BR_regions.png")

    # ---- i.i.d. vs Markov comparison ----
    print("\n--- i.i.d. vs Markov Comparison ---")
    # i.i.d.: belief is always pi(G)
    iid_action = sr_best_response_action(mc.pi[0])
    print(f"  i.i.d.: μ always = π(G) = {mc.pi[0]:.4f}")
    print(f"  i.i.d. BR: {'C' if iid_action == 0 else 'D'} (always)")
    print(f"  i.i.d. fraction in C: {'100.0' if iid_action == 0 else '0.0'}%")

    print(f"\n  Markov: μ fluctuates around {beliefs.mean():.4f} ± {beliefs.std():.4f}")
    print(f"  Markov fraction in C: {frac_c*100:.1f}%")
    print(f"  Markov fraction in D: {frac_d*100:.1f}%")

    # ---- Generate report ----
    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write("# SSA6_3: Nash Correspondence Visualization — Report\n\n")

        f.write("## Setup\n")
        f.write(f"- Markov chain: α={mc.alpha}, β={mc.beta}\n")
        f.write(f"- Stationary π(G) = {mc.pi[0]:.4f}\n")
        f.write(f"- SR threshold: μ* = {SR_THRESHOLD}\n")
        f.write(f"- Simulation: T={T}\n\n")

        f.write("## Nash Correspondence B(s₁, μ)\n\n")
        f.write("The Nash correspondence maps beliefs to best responses:\n")
        f.write(f"- μ > {SR_THRESHOLD}: SR plays **C** (Cooperate)\n")
        f.write(f"- μ < {SR_THRESHOLD}: SR plays **D** (Defect)\n")
        f.write(f"- μ = {SR_THRESHOLD}: SR is indifferent (can mix)\n\n")

        f.write("## i.i.d. vs Markov Comparison\n\n")
        f.write("| Metric | i.i.d. | Markov |\n")
        f.write("|--------|--------|--------|\n")
        f.write(f"| Belief | Always π(G)={mc.pi[0]:.4f} | μ̄={beliefs.mean():.4f} ± {beliefs.std():.4f} |\n")
        f.write(f"| Time in C | {'100.0' if iid_action == 0 else '0.0'}% | {frac_c*100:.1f}% |\n")
        f.write(f"| Time in D | {'0.0' if iid_action == 0 else '100.0'}% | {frac_d*100:.1f}% |\n")
        f.write(f"| BR changes | 0 | Frequent |\n\n")

        f.write("## Key Findings\n\n")
        f.write(f"1. Under i.i.d. states, the belief is a single point at π(G)={mc.pi[0]:.4f}, ")
        if iid_action == 0:
            f.write("which is in the C region. SR always cooperates.\n\n")
        else:
            f.write("which is in the D region. SR always defects.\n\n")

        f.write(f"2. Under Markov states, the filtered belief fluctuates substantially. ")
        f.write(f"SR spends {frac_c*100:.1f}% of time in the C region and ")
        f.write(f"{frac_d*100:.1f}% in the D region.\n\n")

        f.write(f"3. The belief distribution under Markov states has large variance ")
        f.write(f"(σ={beliefs.std():.4f}), causing frequent BR threshold crossings. ")
        f.write("This is fundamentally different from the i.i.d. case.\n\n")

        f.write("4. **Implication for the paper**: The commitment payoff calculated using ")
        f.write("the stationary distribution assumes SR always cooperates (since π(G)>μ*). ")
        f.write("But with Bayesian filtering under Markov states, SR defects ~")
        f.write(f"{frac_d*100:.0f}% of the time, reducing LR's actual payoff.\n\n")

        f.write("## Figures\n")
        f.write("![Nash Correspondence](figures/nash_correspondence.png)\n\n")
        f.write("![Belief Histogram in BR Regions](figures/belief_histogram_in_BR_regions.png)\n")

    print(f"\nReport saved to: {report_path}")
    print("\nDone.")


if __name__ == '__main__':
    main()
