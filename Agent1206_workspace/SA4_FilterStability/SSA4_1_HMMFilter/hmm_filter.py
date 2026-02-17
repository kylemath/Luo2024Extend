"""
SSA4_1: HMM Filter Implementation

Implements forward filtering for a 2-state HMM with both deterministic
and noisy observation models. Compares filter behavior across noise levels.
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
    make_strategy_matrix, tv_distance, save_figure
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(SCRIPT_DIR, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)


def make_noisy_strategy(noise_level):
    """
    Create a strategy matrix with given noise level.
    noise_level=0 -> deterministic, noise_level=0.5 -> uniform random.
    s(G) = (1-noise)A + noise*F
    s(B) = noise*A + (1-noise)F
    """
    return np.array([
        [1.0 - noise_level, noise_level],        # State G
        [noise_level, 1.0 - noise_level]          # State B
    ])


def run_filter(mc, strategy_matrix, T, prior=None, seed=42):
    """
    Run HMM forward filter on a simulated sequence.

    Returns
    -------
    states : ndarray, true states
    signals : ndarray, observed signals
    beliefs : ndarray of shape (T, 2), filter beliefs at each step
    errors : ndarray, |belief(G) - true_state_is_G| at each step
    """
    rng = np.random.default_rng(seed)
    states = mc.simulate(T, rng=rng)

    bf = BayesianFilter(mc, prior=prior)
    beliefs = np.zeros((T, 2))
    signals = np.zeros(T, dtype=int)

    for t in range(T):
        theta_t = states[t]
        signal = rng.choice(2, p=strategy_matrix[theta_t])
        signals[t] = signal
        posterior = bf.update(signal, strategy_matrix)
        beliefs[t] = posterior

    # Filter error: |belief(G) - indicator(state=G)|
    true_g = (states == 0).astype(float)
    errors = np.abs(beliefs[:, 0] - true_g)

    return states, signals, beliefs, errors


def plot_deterministic_vs_noisy(mc, T=500, seed=42):
    """Compare filter behavior for deterministic vs noisy strategies."""
    rng = np.random.default_rng(seed)
    states = mc.simulate(T, rng=rng)

    noise_levels = [0.0, 0.2, 0.4]
    fig, axes = plt.subplots(len(noise_levels) + 1, 1, figsize=(12, 3*(len(noise_levels)+1)),
                             sharex=True)

    # Plot true states
    axes[0].fill_between(np.arange(T), (states == 0).astype(float),
                         alpha=0.3, color='green', step='mid', label='State G')
    axes[0].fill_between(np.arange(T), (states == 1).astype(float),
                         alpha=0.3, color='red', step='mid', label='State B')
    axes[0].set_ylabel('True State')
    axes[0].set_title('True State Sequence')
    axes[0].legend(loc='upper right')

    for i, noise in enumerate(noise_levels):
        sigma = make_noisy_strategy(noise)
        bf = BayesianFilter(mc)

        beliefs_g = np.zeros(T)
        for t in range(T):
            theta_t = states[t]
            signal = rng.choice(2, p=sigma[theta_t])
            posterior = bf.update(signal, sigma)
            beliefs_g[t] = posterior[0]

        ax = axes[i + 1]
        ax.plot(np.arange(T), beliefs_g, 'b-', linewidth=0.8, alpha=0.8)
        ax.fill_between(np.arange(T), (states == 0).astype(float),
                        alpha=0.1, color='green', step='mid')
        ax.set_ylabel('Belief(G)')
        label = 'Deterministic' if noise == 0 else f'Noise={noise}'
        ax.set_title(f'Filter Belief: {label}')
        ax.set_ylim(-0.05, 1.05)

        # Compute mean absolute error
        true_g = (states == 0).astype(float)
        mae = np.mean(np.abs(beliefs_g - true_g))
        ax.text(0.98, 0.95, f'MAE={mae:.3f}', transform=ax.transAxes,
                ha='right', va='top', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    axes[-1].set_xlabel('Period t')
    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'filter_deterministic_vs_noisy.png')
    save_figure(fig, path)
    return path


def main():
    print("=" * 60)
    print("SSA4_1: HMM Filter Implementation")
    print("=" * 60)

    mc = MarkovChain(alpha=0.3, beta=0.5)
    T = 2000
    seed = 42

    print(f"\nMarkov chain: alpha={mc.alpha}, beta={mc.beta}")
    print(f"Stationary: pi(G)={mc.pi[0]:.3f}, pi(B)={mc.pi[1]:.3f}")
    print(f"Simulation length: T={T}")

    noise_levels = [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
    print(f"\n--- Filter Performance by Noise Level ---")
    print(f"{'Noise':>6} | {'MAE':>8} | {'Mean Bel(G)':>11} | {'Std Bel(G)':>10}")
    print("-" * 50)

    all_results = {}
    for noise in noise_levels:
        sigma = make_noisy_strategy(noise)
        states, signals, beliefs, errors = run_filter(mc, sigma, T, seed=seed)
        mae = np.mean(errors)
        mean_bel = np.mean(beliefs[:, 0])
        std_bel = np.std(beliefs[:, 0])
        print(f"{noise:>6.2f} | {mae:>8.4f} | {mean_bel:>11.4f} | {std_bel:>10.4f}")
        all_results[noise] = {
            'mae': mae, 'mean_bel': mean_bel, 'std_bel': std_bel,
            'beliefs': beliefs, 'errors': errors
        }

    # Key observations
    print(f"\n--- Key Observations ---")
    det_mae = all_results[0.0]['mae']
    print(f"Deterministic (noise=0): MAE={det_mae:.4f}")
    print(f"  -> Filter collapses to point mass each period (perfect state knowledge)")

    noisy_mae = all_results[0.2]['mae']
    print(f"Noisy (noise=0.2): MAE={noisy_mae:.4f}")
    print(f"  -> Filter has non-trivial dynamics, beliefs persist across periods")

    uniform_mae = all_results[0.5]['mae']
    print(f"Uninformative (noise=0.5): MAE={uniform_mae:.4f}")
    print(f"  -> Signals carry no information, filter relies only on transition model")

    # Generate plot
    fig_path = plot_deterministic_vs_noisy(mc, T=500, seed=seed)
    print(f"\nFigure saved: {fig_path}")

    # Generate report
    report = f"""# SSA4_1: HMM Filter Implementation — Report

## Setup
- **Markov chain**: alpha={mc.alpha}, beta={mc.beta}
- **Stationary distribution**: pi(G)={mc.pi[0]:.3f}, pi(B)={mc.pi[1]:.3f}
- **Simulation length**: T={T}

## Filter Performance by Noise Level

| Noise Level | MAE | Mean Belief(G) | Std Belief(G) |
|-------------|-----|----------------|---------------|
"""
    for noise in noise_levels:
        r = all_results[noise]
        report += f"| {noise:.2f} | {r['mae']:.4f} | {r['mean_bel']:.4f} | {r['std_bel']:.4f} |\n"

    report += f"""
## Key Findings

### Deterministic Strategy (noise=0)
When the strategy is deterministic (A in G, F in B), each signal perfectly reveals
the current state. The filter collapses to a point mass after each observation.
**Filter stability is trivially satisfied** because there is no information to "forget" —
each period provides complete state knowledge.

### Noisy Strategy (noise > 0)
When the strategy is stochastic, signals only partially reveal the state. The filter
maintains non-degenerate beliefs that evolve smoothly. **This is where filter stability
becomes non-trivial** — the filter must combine prior beliefs (from the transition model)
with new noisy evidence.

### Uninformative Strategy (noise=0.5)
When noise = 0.5, signals are independent of the state (pure noise). The filter
relies entirely on the Markov transition structure. Beliefs converge toward the
stationary distribution and vary only due to the transition model predictions.

### Implication for the Paper
The paper's extension claims filter stability holds for Markov states. This is
**trivially true for deterministic strategies** (which the paper focuses on) but
**substantively important for stochastic strategies**. The critique may be pointing
out that the interesting case (stochastic strategies) deserves more attention.

## Figures
- ![Deterministic vs Noisy](figures/filter_deterministic_vs_noisy.png)
"""
    report_path = os.path.join(SCRIPT_DIR, 'report.md')
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Report saved: {report_path}")
    print("\nDone.")


if __name__ == '__main__':
    main()
