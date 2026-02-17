#!/usr/bin/env python3
"""
analysis_nash.py — SA6: Nash dynamics / deterrence game simulation.

Simulates the deterrence game comparing stationary vs filtered SR beliefs.
Tracks payoffs and SR action disagreement.

Generates:
  ../figures/fig_payoff_gap.png    (payoff comparison bar chart)
  ../figures/fig_nash_dynamics.png (belief trajectory + BR threshold)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os


def tv_distance(p, q):
    return 0.5 * np.abs(p - q).sum()


def simulate_deterrence(alpha=0.3, beta=0.5, x=0.3, y=0.4, T=1000, seed=42):
    """Simulate deterrence game with Bayesian filtering.

    Returns dict with payoffs and belief trajectories.
    """
    rng = np.random.default_rng(seed)
    Tmat = np.array([[1 - alpha, alpha], [beta, 1 - beta]])
    pi = np.array([beta / (alpha + beta), alpha / (alpha + beta)])

    # Payoff: u1[state, action]  state: 0=G,1=B  action: 0=A,1=F
    u1 = np.array([[1.0, x], [y, 0.0]])

    # Stackelberg strategy
    strat = np.array([[1.0, 0.0], [0.0, 1.0]])

    # Simulate states
    states = np.zeros(T, dtype=int)
    states[0] = rng.choice(2, p=pi)
    for t in range(1, T):
        states[t] = rng.choice(2, p=Tmat[states[t - 1]])

    # SR's best response threshold: acquiesce iff belief(G) >= y/(1-x)
    # Actually: SR payoff from A = belief(G)*1 + belief(B)*y vs F = belief(G)*x + belief(B)*0
    # SR prefers A iff belief(G)*(1-x) >= belief(B)*(-y) -- wait, let me re-derive:
    # u_SR(A) = belief(G)*u_SR(G,A) + belief(B)*u_SR(B,A)
    # For SR: u_SR is about SR's payoff. In a deterrence game, SR chooses to
    # acquiesce or fight based on expected payoff.
    # With Stackelberg: P1 plays A in G, F in B.
    # SR payoff from A: p_G * 1 + p_B * 0 = p_G  (SR gets 1 if state is G)
    # SR payoff from F: p_G * x + p_B * y = p_G*x + (1-p_G)*y
    # SR prefers A iff p_G >= p_G*x + (1-p_G)*y => p_G(1-x) >= (1-p_G)*y
    # => p_G >= y / (1-x+y)
    br_threshold = y / (1 - x + y)

    # Run filter
    belief = pi.copy()
    belief_G_series = [pi[0]]
    payoffs_filtered = []
    payoffs_stationary = []
    sr_action_filtered = []
    sr_action_stationary = []

    for t in range(1, T):
        # P1 action under Stackelberg
        p1_action = 0 if states[t] == 0 else 1

        # Bayesian update
        predicted = Tmat.T @ belief
        lik = strat[:, p1_action]
        posterior = predicted * lik
        s = posterior.sum()
        belief = posterior / s if s > 0 else pi.copy()
        belief_G_series.append(belief[0])

        # SR best response under filtered belief
        sr_filt = 0 if belief[0] >= br_threshold else 1  # 0=A, 1=F
        sr_action_filtered.append(sr_filt)

        # SR best response under stationary belief
        sr_stat = 0 if pi[0] >= br_threshold else 1
        sr_action_stationary.append(sr_stat)

        # P1 payoff = u1[state, sr_action]
        payoffs_filtered.append(u1[states[t], sr_filt])
        payoffs_stationary.append(u1[states[t], sr_stat])

    return {
        'belief_G': np.array(belief_G_series),
        'payoffs_filtered': np.array(payoffs_filtered),
        'payoffs_stationary': np.array(payoffs_stationary),
        'sr_filtered': np.array(sr_action_filtered),
        'sr_stationary': np.array(sr_action_stationary),
        'br_threshold': br_threshold,
        'pi_G': pi[0],
    }


def main():
    res = simulate_deterrence()
    outdir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(outdir, exist_ok=True)

    # ── Figure 1: Payoff comparison ──────────────────────────────────────
    mean_stat = np.mean(res['payoffs_stationary'])
    mean_filt = np.mean(res['payoffs_filtered'])

    fig, ax = plt.subplots(figsize=(6, 4.5))
    bars = ax.bar(['Stationary\nBelief', 'Filtered\nBelief'],
                  [mean_stat, mean_filt],
                  color=['#4C72B0', '#DD8452'], width=0.5, edgecolor='black')
    ax.set_ylabel("Mean P1 Payoff")
    ax.set_title("Payoff: Stationary vs Filtered SR Beliefs")
    for bar, val in zip(bars, [mean_stat, mean_filt]):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                f'{val:.3f}', ha='center', va='bottom', fontsize=11)
    ax.set_ylim(0, max(mean_stat, mean_filt) * 1.2)

    path1 = os.path.join(outdir, 'fig_payoff_gap.png')
    fig.savefig(path1, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {path1}")

    # ── Figure 2: Belief trajectory + BR threshold ───────────────────────
    T_plot = min(200, len(res['belief_G']))
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(range(T_plot), res['belief_G'][:T_plot], color='#4C72B0',
            linewidth=0.8, label='Filtered belief P(G)')
    ax.axhline(res['pi_G'], color='gray', ls='--', linewidth=1,
               label=f'Stationary π(G)={res["pi_G"]:.2f}')
    ax.axhline(res['br_threshold'], color='red', ls=':', linewidth=1.5,
               label=f'BR threshold={res["br_threshold"]:.2f}')
    ax.fill_between(range(T_plot), 0, 1,
                    where=np.array(res['belief_G'][:T_plot]) < res['br_threshold'],
                    alpha=0.1, color='red', label='SR fights')
    ax.set_xlabel('Period')
    ax.set_ylabel('Belief P(θ=G)')
    ax.set_title('Nash Dynamics: Belief Trajectory and Best-Response Threshold')
    ax.set_ylim(-0.05, 1.05)
    ax.legend(loc='upper right', fontsize=8)

    path2 = os.path.join(outdir, 'fig_nash_dynamics.png')
    fig.savefig(path2, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {path2}")

    # Stats
    overest = (mean_stat - mean_filt) / mean_filt * 100 if mean_filt > 0 else 0
    disagreement = np.mean(res['sr_filtered'] != res['sr_stationary']) * 100

    print(f"STAT:payoff_stationary={mean_stat:.3f}")
    print(f"STAT:payoff_filtered={mean_filt:.3f}")
    print(f"STAT:overestimation_pct={overest:.1f}")
    print(f"STAT:sr_disagreement_pct={disagreement:.1f}")


if __name__ == '__main__':
    main()
