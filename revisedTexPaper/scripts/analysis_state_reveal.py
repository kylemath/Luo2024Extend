#!/usr/bin/env python3
"""
analysis_state_reveal.py — SA2: State-reveal belief gap analysis.

Computes analytically:
  Gap after G: alpha * |1 - alpha - beta| / (alpha + beta)
  Gap after B: beta  * |1 - alpha - beta| / (alpha + beta)
  Expected gap: 2*alpha*beta*|1-alpha-beta| / (alpha+beta)^2

Generates: ../figures/fig_belief_gap.png (heatmap of expected gap)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os


def expected_gap(alpha, beta):
    """Analytic expected belief gap after one state reveal."""
    s = alpha + beta
    if s < 1e-12:
        return 0.0
    return 2.0 * alpha * beta * abs(1.0 - alpha - beta) / (s ** 2)


def main():
    N = 100
    alphas = np.linspace(0.01, 0.99, N)
    betas = np.linspace(0.01, 0.99, N)
    grid = np.zeros((N, N))

    for i, a in enumerate(alphas):
        for j, b in enumerate(betas):
            grid[j, i] = expected_gap(a, b)

    fig, ax = plt.subplots(figsize=(7, 5.5))
    im = ax.imshow(grid, origin='lower', aspect='auto',
                   extent=[alphas[0], alphas[-1], betas[0], betas[-1]],
                   cmap='inferno')
    fig.colorbar(im, ax=ax, label='Expected belief gap')
    ax.set_xlabel('α = Pr(B|G)')
    ax.set_ylabel('β = Pr(G|B)')
    ax.set_title('Expected Belief Gap After State Reveal')

    # Mark the α + β = 1 line (gap = 0)
    xs = np.linspace(0.01, 0.99, 200)
    ys = 1.0 - xs
    valid = (ys > 0.01) & (ys < 0.99)
    ax.plot(xs[valid], ys[valid], 'w--', linewidth=1.5, label='α+β=1 (gap=0)')
    ax.legend(loc='upper right', fontsize=9)

    outdir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'fig_belief_gap.png')
    fig.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {outpath}")

    # Baseline: α=0.3, β=0.5
    gap_base = expected_gap(0.3, 0.5)
    print(f"STAT:gap_baseline={gap_base:.3f}")
    print("STAT:gap_formula=2ab|1-a-b|/(a+b)^2")


if __name__ == '__main__':
    main()
