"""
SSA3_1: Signal Process Simulator

Simulates two signal processes on the same Markov state sequence:
  Q process: commitment type plays s1*(G)=A, s1*(B)=F deterministically
  P process: "confused" type plays s1'(G)=0.7A+0.3F, s1'(B)=0.4A+0.6F (mixed)

Computes per-period signal distributions q_t and p_t for KL computation.
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
    make_strategy_matrix, tv_distance, kl_divergence, save_figure
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(SCRIPT_DIR, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)


def simulate_signal_processes(T=2000, alpha=0.3, beta=0.5, seed=42):
    """
    Simulate Q and P signal processes on the same state sequence.

    Returns
    -------
    states : ndarray of shape (T,), state sequence (0=G, 1=B)
    q_dists : ndarray of shape (T, 2), q_t(y) for each period
    p_dists : ndarray of shape (T, 2), p_t(y) for each period
    q_signals : ndarray of shape (T,), realized signals under Q
    p_signals : ndarray of shape (T,), realized signals under P
    """
    rng = np.random.default_rng(seed)
    mc = MarkovChain(alpha=alpha, beta=beta)
    game = DeterrenceGame()

    # Strategy matrices
    # Q: commitment type — deterministic Stackelberg
    sigma_q = make_strategy_matrix(game.stackelberg_strategy)
    # P: confused type — mixed strategy
    sigma_p = np.array([
        [0.7, 0.3],   # State G: 70% A, 30% F
        [0.4, 0.6]    # State B: 40% A, 60% F
    ])

    # Simulate state sequence
    states = mc.simulate(T, rng=rng)

    # Bayesian filter for the SR player (used to compute p_t)
    # The SR player observes signals and updates beliefs about theta_t
    # For q_t: since commitment type is deterministic, q_t is degenerate
    # For p_t: depends on SR player's belief about theta_t given history

    # Under Q (commitment type): signals perfectly reveal state
    # q_t(A) = Pr(theta_t=G | h_t under Q), q_t(F) = Pr(theta_t=B | h_t under Q)
    # But since Q is deterministic, q_t is degenerate: q_t = delta_{s1*(theta_t)}

    # Under P (confused type): p_t(y) = sum_theta Pr(y|theta, sigma_p) * Pr(theta|h_t under P)
    # The SR player's belief depends on which type is generating signals

    # We compute q_t and p_t as the signal distributions given the history
    # For the KL bound, we need the one-step-ahead signal distributions

    q_dists = np.zeros((T, 2))
    p_dists = np.zeros((T, 2))
    q_signals = np.zeros(T, dtype=int)
    p_signals = np.zeros(T, dtype=int)

    # Filter for the SR player observing Q-signals (commitment type)
    filter_q = BayesianFilter(mc)
    # Filter for the SR player observing P-signals (confused type)
    filter_p = BayesianFilter(mc)

    for t in range(T):
        theta_t = states[t]

        # --- Q process (commitment type) ---
        # Signal distribution: deterministic given theta_t
        # But from SR's perspective, q_t(y) = sum_theta Pr(y|theta) * belief_q(theta)
        if t == 0:
            belief_q = mc.pi.copy()
        else:
            belief_q = filter_q.belief.copy()
            # Predict step
            belief_q = mc.T.T @ belief_q

        q_t = belief_q @ sigma_q  # q_t[y] = sum_theta belief_q[theta] * sigma_q[theta, y]
        q_dists[t] = q_t

        # Realize signal under Q
        q_signal = game.stackelberg_strategy(theta_t)  # deterministic
        q_signals[t] = q_signal

        # Update Q filter with observed signal
        filter_q.belief = belief_q  # set to predicted belief
        likelihood_q = sigma_q[:, q_signal]
        posterior_q = belief_q * likelihood_q
        if posterior_q.sum() > 0:
            posterior_q /= posterior_q.sum()
        filter_q.belief = posterior_q

        # --- P process (confused type) ---
        if t == 0:
            belief_p = mc.pi.copy()
        else:
            belief_p = filter_p.belief.copy()
            belief_p = mc.T.T @ belief_p

        p_t = belief_p @ sigma_p  # p_t[y] = sum_theta belief_p[theta] * sigma_p[theta, y]
        p_dists[t] = p_t

        # Realize signal under P
        p_signal = rng.choice(2, p=sigma_p[theta_t])
        p_signals[t] = p_signal

        # Update P filter with observed signal
        filter_p.belief = belief_p
        likelihood_p = sigma_p[:, p_signal]
        posterior_p = belief_p * likelihood_p
        if posterior_p.sum() > 0:
            posterior_p /= posterior_p.sum()
        filter_p.belief = posterior_p

    return states, q_dists, p_dists, q_signals, p_signals


def plot_signal_distributions(q_dists, p_dists, states, T_show=200):
    """Plot signal distributions over time for both processes."""
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

    t_range = np.arange(T_show)

    # Plot state sequence
    axes[0].fill_between(t_range, states[:T_show], alpha=0.3, color='gray',
                         step='mid', label='State (0=G, 1=B)')
    axes[0].set_ylabel('State')
    axes[0].set_title('State Sequence and Signal Distributions')
    axes[0].legend(loc='upper right')
    axes[0].set_ylim(-0.1, 1.1)

    # Plot q_t(A) — commitment type
    axes[1].plot(t_range, q_dists[:T_show, 0], 'b-', alpha=0.7, label='q_t(A)')
    axes[1].plot(t_range, q_dists[:T_show, 1], 'r-', alpha=0.7, label='q_t(F)')
    axes[1].set_ylabel('Probability')
    axes[1].set_title('Q Process (Commitment Type): Signal Distribution')
    axes[1].legend(loc='upper right')
    axes[1].set_ylim(-0.05, 1.05)

    # Plot p_t(A) — confused type
    axes[2].plot(t_range, p_dists[:T_show, 0], 'b-', alpha=0.7, label='p_t(A)')
    axes[2].plot(t_range, p_dists[:T_show, 1], 'r-', alpha=0.7, label='p_t(F)')
    axes[2].set_ylabel('Probability')
    axes[2].set_xlabel('Period t')
    axes[2].set_title('P Process (Confused Type): Signal Distribution')
    axes[2].legend(loc='upper right')
    axes[2].set_ylim(-0.05, 1.05)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'signal_distributions.png')
    save_figure(fig, path)
    return path


def plot_tv_comparison(q_dists, p_dists, T_show=500):
    """Plot TV distance between q_t and p_t over time."""
    T = min(len(q_dists), T_show)
    tv = np.array([tv_distance(q_dists[t], p_dists[t]) for t in range(T)])

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(np.arange(T), tv, 'k-', alpha=0.5, linewidth=0.5)
    # Rolling average
    window = 50
    if T > window:
        rolling = np.convolve(tv, np.ones(window)/window, mode='valid')
        ax.plot(np.arange(window-1, T), rolling, 'r-', linewidth=2,
                label=f'Rolling avg (w={window})')
    ax.set_xlabel('Period t')
    ax.set_ylabel('TV(q_t, p_t)')
    ax.set_title('Total Variation Distance Between Q and P Signal Distributions')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'tv_distance_preview.png')
    save_figure(fig, path)
    return path


def main():
    print("=" * 60)
    print("SSA3_1: Signal Process Simulator")
    print("=" * 60)

    T = 2000
    states, q_dists, p_dists, q_signals, p_signals = simulate_signal_processes(T=T)

    # Summary statistics
    print(f"\nSimulation: T={T}, alpha=0.3, beta=0.5")
    print(f"State frequencies: G={np.mean(states==0):.3f}, B={np.mean(states==1):.3f}")
    print(f"Stationary dist:  G={0.5/(0.3+0.5):.3f}, B={0.3/(0.3+0.5):.3f}")

    print(f"\nQ signals: A={np.mean(q_signals==0):.3f}, F={np.mean(q_signals==1):.3f}")
    print(f"P signals: A={np.mean(p_signals==0):.3f}, F={np.mean(p_signals==1):.3f}")

    # TV distances
    tv_vals = np.array([tv_distance(q_dists[t], p_dists[t]) for t in range(T)])
    print(f"\nTV(q_t, p_t) statistics:")
    print(f"  Mean:   {np.mean(tv_vals):.4f}")
    print(f"  Median: {np.median(tv_vals):.4f}")
    print(f"  Std:    {np.std(tv_vals):.4f}")
    print(f"  Min:    {np.min(tv_vals):.4f}")
    print(f"  Max:    {np.max(tv_vals):.4f}")

    # Per-period KL divergence preview
    kl_vals = np.array([kl_divergence(q_dists[t], p_dists[t]) for t in range(T)])
    print(f"\nD(q_t || p_t) statistics:")
    print(f"  Mean:   {np.mean(kl_vals):.6f}")
    print(f"  Median: {np.median(kl_vals):.6f}")
    print(f"  Cumulative sum at T={T}: {np.sum(kl_vals):.4f}")

    # Distinguishing periods counts
    for eta in [0.01, 0.05, 0.1, 0.2]:
        count = np.sum(tv_vals > eta)
        print(f"  #{'{t: TV>'+f'{eta}'+'}'}: {count} / {T} = {count/T:.3f}")

    # Generate plots
    fig1_path = plot_signal_distributions(q_dists, p_dists, states)
    print(f"\nFigure saved: {fig1_path}")

    fig2_path = plot_tv_comparison(q_dists, p_dists)
    print(f"Figure saved: {fig2_path}")

    # Save data for downstream scripts
    np.savez(os.path.join(SCRIPT_DIR, 'signal_data.npz'),
             states=states, q_dists=q_dists, p_dists=p_dists,
             q_signals=q_signals, p_signals=p_signals)
    print(f"\nData saved: {os.path.join(SCRIPT_DIR, 'signal_data.npz')}")

    # Generate report
    report = f"""# SSA3_1: Signal Process Simulator — Report

## Setup
- **Markov chain**: 2-state with alpha=0.3 (G->B), beta=0.5 (B->G)
- **Stationary distribution**: pi(G)={0.5/0.8:.3f}, pi(B)={0.3/0.8:.3f}
- **Simulation length**: T={T}

## Signal Processes
- **Q (commitment type)**: Deterministic Stackelberg — A in state G, F in state B
- **P (confused type)**: Mixed — s(G)=0.7A+0.3F, s(B)=0.4A+0.6F

## Key Finding
Since the commitment type plays deterministically, each signal perfectly reveals the state.
The confused type plays mixed strategies, so signals only partially reveal the state.
This creates an information asymmetry that the KL bound quantifies.

## Signal Distribution Statistics
| Metric | Value |
|--------|-------|
| Mean TV(q_t, p_t) | {np.mean(tv_vals):.4f} |
| Mean D(q_t \\|\\| p_t) | {np.mean(kl_vals):.6f} |
| Cumulative KL at T={T} | {np.sum(kl_vals):.4f} |

## Distinguishing Periods
| Threshold eta | Count | Fraction |
|---------------|-------|----------|
| 0.01 | {np.sum(tv_vals > 0.01)} | {np.mean(tv_vals > 0.01):.3f} |
| 0.05 | {np.sum(tv_vals > 0.05)} | {np.mean(tv_vals > 0.05):.3f} |
| 0.10 | {np.sum(tv_vals > 0.10)} | {np.mean(tv_vals > 0.10):.3f} |
| 0.20 | {np.sum(tv_vals > 0.20)} | {np.mean(tv_vals > 0.20):.3f} |

## Figures
- ![Signal Distributions](figures/signal_distributions.png)
- ![TV Distance Preview](figures/tv_distance_preview.png)

## Notes
The q_t distribution for the commitment type fluctuates with the SR player's belief
about the state. When the filter has high confidence in G, q_t(A) is close to 1.
The p_t distribution is smoother because the mixed strategy blurs state information.
"""
    report_path = os.path.join(SCRIPT_DIR, 'report.md')
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Report saved: {report_path}")
    print("\nDone.")


if __name__ == '__main__':
    main()
