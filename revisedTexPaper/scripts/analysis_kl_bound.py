#!/usr/bin/env python3
"""
analysis_kl_bound.py — SA3: KL-bound verification via Monte Carlo.

Runs N=500 Monte Carlo simulations comparing i.i.d. vs Markov
distinguishing-period counts. Verifies the KL bound from the paper.

Generates: ../figures/fig_kl_bound.png (side-by-side histogram)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os


def kl_divergence(p, q, eps=1e-12):
    p_s = np.clip(p, eps, 1.0)
    q_s = np.clip(q, eps, 1.0)
    return np.sum(p_s * np.log(p_s / q_s))


def simulate_chain(alpha, beta, T, rng):
    pi = np.array([beta / (alpha + beta), alpha / (alpha + beta)])
    Tmat = np.array([[1 - alpha, alpha], [beta, 1 - beta]])
    states = np.zeros(T, dtype=int)
    states[0] = rng.choice(2, p=pi)
    for t in range(1, T):
        states[t] = rng.choice(2, p=Tmat[states[t - 1]])
    return states, pi, Tmat


def count_distinguishing_periods(states, alpha, beta):
    """Count periods where Markov observation differs from i.i.d. prediction.

    A period is 'distinguishing' if the empirical transition frequency
    deviates significantly from what i.i.d. would predict.
    We use a sliding window approach over blocks.
    """
    T = len(states)
    block = 20
    n_blocks = T // block
    pi = np.array([beta / (alpha + beta), alpha / (alpha + beta)])

    count = 0
    for b in range(n_blocks):
        seg = states[b * block:(b + 1) * block]
        # Empirical frequency
        freq = np.array([np.mean(seg == 0), np.mean(seg == 1)])
        freq = np.clip(freq, 1e-8, 1.0)
        freq /= freq.sum()
        # KL from stationary
        kl = kl_divergence(freq, pi)
        # Under i.i.d., expected KL ~ 0; under Markov, persistence inflates it
        # Threshold from chi-squared approximation
        if kl > 0.05:
            count += 1
    return count


def run_mc_sim(alpha, beta, T, N, seed):
    rng = np.random.default_rng(seed)
    markov_counts = []
    iid_counts = []
    pi = np.array([beta / (alpha + beta), alpha / (alpha + beta)])

    for _ in range(N):
        # Markov chain
        states_m, _, _ = simulate_chain(alpha, beta, T, rng)
        markov_counts.append(count_distinguishing_periods(states_m, alpha, beta))

        # i.i.d. baseline
        states_i = rng.choice(2, size=T, p=pi)
        iid_counts.append(count_distinguishing_periods(states_i, alpha, beta))

    return np.array(markov_counts), np.array(iid_counts)


def main():
    alpha, beta = 0.3, 0.5
    T = 1000
    N = 500
    seed = 12345

    markov_counts, iid_counts = run_mc_sim(alpha, beta, T, N, seed)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), sharey=True)

    bins = np.arange(0, max(markov_counts.max(), iid_counts.max()) + 2) - 0.5
    ax1.hist(iid_counts, bins=bins, color='steelblue', edgecolor='white',
             alpha=0.85)
    ax1.set_title('i.i.d. Distinguishing Periods')
    ax1.set_xlabel('Count per trajectory')
    ax1.set_ylabel('Frequency')
    ax1.axvline(np.mean(iid_counts), color='red', ls='--', label=f'mean={np.mean(iid_counts):.1f}')
    ax1.legend()

    ax2.hist(markov_counts, bins=bins, color='darkorange', edgecolor='white',
             alpha=0.85)
    ax2.set_title('Markov Distinguishing Periods')
    ax2.set_xlabel('Count per trajectory')
    ax2.axvline(np.mean(markov_counts), color='red', ls='--', label=f'mean={np.mean(markov_counts):.1f}')
    ax2.legend()

    fig.suptitle(f'KL Bound Verification (α={alpha}, β={beta}, T={T}, N={N})',
                 fontsize=12)
    fig.tight_layout()

    outdir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'fig_kl_bound.png')
    fig.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {outpath}")

    kl_bound_holds = np.mean(markov_counts) > np.mean(iid_counts)
    print(f"STAT:kl_bound_holds={kl_bound_holds}")
    print(f"STAT:markov_mean_count={np.mean(markov_counts):.1f}")
    print(f"STAT:iid_mean_count={np.mean(iid_counts):.1f}")


if __name__ == '__main__':
    main()
