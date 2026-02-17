#!/usr/bin/env python3
"""SSA2_2: Divergence Analysis — analytical and numerical study of the permanent belief gap."""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm

from shared.markov_utils import MarkovChain, DeterrenceGame, tv_distance, save_figure

FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)


def analytical_gap(alpha, beta):
    """Compute the expected TV gap analytically.

    When the state is revealed:
    - SR belief about θ_{t+1} after G: F(·|G) = (1-α, α)
    - SR belief about θ_{t+1} after B: F(·|B) = (β, 1-β)
    - Stationary: π = (β/(α+β), α/(α+β))

    TV distance = 0.5 * |F(·|θ) - π|_1

    For 2-state distributions, TV = |F(G|θ) - π(G)|

    Gap after G: |(1-α) - β/(α+β)| = |((1-α)(α+β) - β)/(α+β)|
                = |α+β - α² - αβ - β| / (α+β) = |α - α² - αβ| / (α+β)
                = α|1 - α - β| / (α+β)

    Gap after B: |β - β/(α+β)| = |β(α+β) - β| / (α+β) = |β(α+β-1)| / (α+β)
                = β|1 - α - β| / (α+β)

    Expected gap = π(G) * gap_G + π(B) * gap_B
                 = β/(α+β) * α|1-α-β|/(α+β) + α/(α+β) * β|1-α-β|/(α+β)
                 = 2αβ|1-α-β| / (α+β)²
    """
    if alpha + beta == 0:
        return 0.0, 0.0, 0.0

    pi_G = beta / (alpha + beta)
    pi_B = alpha / (alpha + beta)

    gap_G = alpha * abs(1 - alpha - beta) / (alpha + beta)
    gap_B = beta * abs(1 - alpha - beta) / (alpha + beta)

    expected_gap = pi_G * gap_G + pi_B * gap_B

    return gap_G, gap_B, expected_gap


def compute_heatmap():
    """Compute expected gap heatmap over fine grid."""
    print("Computing analytical gap heatmap...")
    n_pts = 200
    alphas = np.linspace(0.01, 0.99, n_pts)
    betas = np.linspace(0.01, 0.99, n_pts)
    heatmap = np.zeros((n_pts, n_pts))

    for i, alpha in enumerate(alphas):
        for j, beta in enumerate(betas):
            _, _, expected_gap = analytical_gap(alpha, beta)
            heatmap[i, j] = expected_gap

    fig, ax = plt.subplots(figsize=(9, 7))
    im = ax.imshow(heatmap, origin='lower', aspect='auto', cmap='magma',
                    extent=[0.01, 0.99, 0.01, 0.99])

    # Mark the i.i.d. line α + β = 1
    beta_line = np.linspace(0.01, 0.99, 200)
    alpha_line = 1 - beta_line
    valid = (alpha_line > 0.01) & (alpha_line < 0.99)
    ax.plot(beta_line[valid], alpha_line[valid], 'c--', linewidth=2,
            label='α+β=1 (gap=0, i.i.d.)')

    ax.set_xlabel('β (Pr(G|B))', fontsize=12)
    ax.set_ylabel('α (Pr(B|G))', fontsize=12)
    ax.set_title('Expected Belief Gap E[|F(G|θ_t) − π(G)|]\n(Analytical)', fontsize=13)
    ax.legend(fontsize=10, loc='upper right')

    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Expected Gap', fontsize=11)

    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'belief_gap_heatmap.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")
    return heatmap


def compute_1d_slice():
    """Plot gap along α = β diagonal and compare to simulation."""
    print("\nComputing 1D slice along α = β...")
    n_pts = 100
    params = np.linspace(0.01, 0.99, n_pts)

    analytical_gaps = np.zeros(n_pts)
    simulated_gaps = np.zeros(n_pts)

    rng = np.random.default_rng(111)
    T = 5000

    for i, p in enumerate(params):
        _, _, analytical_gaps[i] = analytical_gap(p, p)

        # Simulate for verification
        mc = MarkovChain(alpha=p, beta=p)
        states = mc.simulate(T, rng=rng)
        gaps = np.zeros(T - 1)
        for t in range(1, T):
            sr_belief_G = mc.T[states[t - 1], 0]
            gaps[t - 1] = abs(sr_belief_G - mc.pi[0])
        simulated_gaps[i] = np.mean(gaps)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: gap vs parameter
    ax = axes[0]
    ax.plot(params, analytical_gaps, 'b-', linewidth=2, label='Analytical')
    ax.plot(params, simulated_gaps, 'r.', markersize=3, alpha=0.6, label='Simulated')
    ax.axvline(x=0.5, color='green', linestyle='--', alpha=0.5,
                label='α=β=0.5 (i.i.d.: α+β=1)')
    ax.set_xlabel('α = β', fontsize=12)
    ax.set_ylabel('Expected belief gap', fontsize=12)
    ax.set_title('Gap Along α = β Diagonal', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)

    # Right: gap vs persistence measure (1 - α - β)
    persistence = 1 - 2 * params  # 1 - (α+β) when α=β
    ax = axes[1]
    ax.plot(persistence, analytical_gaps, 'b-', linewidth=2, label='Analytical')
    ax.plot(persistence, simulated_gaps, 'r.', markersize=3, alpha=0.6, label='Simulated')
    ax.axvline(x=0, color='green', linestyle='--', alpha=0.5, label='i.i.d. (1−α−β=0)')
    ax.set_xlabel('Persistence: 1 − α − β', fontsize=12)
    ax.set_ylabel('Expected belief gap', fontsize=12)
    ax.set_title('Gap vs Persistence (α = β)', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'gap_vs_persistence.png')
    save_figure(fig, fig_path)
    print(f"Saved: {fig_path}")

    return params, analytical_gaps, simulated_gaps


def write_report(params, analytical_gaps, simulated_gaps):
    """Generate report.md."""
    max_err = np.max(np.abs(analytical_gaps - simulated_gaps))
    iid_idx = np.argmin(np.abs(params - 0.5))
    gap_at_iid = analytical_gaps[iid_idx]

    # Find parameter with max gap
    max_gap_idx = np.argmax(analytical_gaps)
    max_gap_param = params[max_gap_idx]
    max_gap_val = analytical_gaps[max_gap_idx]

    report = f"""# SSA2_2: Divergence Analysis — Report

## Summary

Analytical and numerical study of the permanent belief gap that arises under state-revealing
strategies in the Markov deterrence game.

## Analytical Formulas

For a 2-state Markov chain with Pr(B|G) = α and Pr(G|B) = β:

- **Stationary distribution**: π(G) = β/(α+β)
- **Belief after observing state G**: F(G|G) = 1 − α
- **Belief after observing state B**: F(G|B) = β
- **Gap after G**: |F(G|G) − π(G)| = α·|1−α−β| / (α+β)
- **Gap after B**: |F(G|B) − π(G)| = β·|1−α−β| / (α+β)
- **Expected gap**: π(G)·gap_G + π(B)·gap_B = 2αβ|1−α−β| / (α+β)²

## When is the Gap Zero?

Both gap_G and gap_B share the factor |1−α−β|, so:
- gap_G = 0 ⟺ α = 0 or |1−α−β| = 0
- gap_B = 0 ⟺ β = 0 or |1−α−β| = 0

For non-degenerate chains (α,β > 0), the gap is zero **if and only if α + β = 1** (the i.i.d. case).
The expected gap = 2αβ|1−α−β|/(α+β)² is zero iff |1−α−β| = 0, confirming this.

## Numerical Verification

- Maximum analytical-simulation discrepancy: {max_err:.6f}
- Gap at α = β = 0.5 (i.i.d.): {gap_at_iid:.6f} (should be ≈ 0)
- Maximum gap along α = β diagonal: {max_gap_val:.4f} at α = β = {max_gap_param:.3f}

## Selected Parameter Values

| α | β | π(G) | Gap after G | Gap after B | Expected Gap |
|---|---|------|-------------|-------------|--------------|
"""
    for alpha, beta in [(0.1, 0.1), (0.3, 0.5), (0.5, 0.5), (0.1, 0.9), (0.05, 0.05)]:
        g_G, g_B, e_gap = analytical_gap(alpha, beta)
        pi_G = beta / (alpha + beta)
        report += f"| {alpha} | {beta} | {pi_G:.4f} | {g_G:.4f} | {g_B:.4f} | {e_gap:.4f} |\n"

    report += """
## Key Finding

**The belief gap is zero if and only if the Markov chain is i.i.d. (α + β = 1).**

For ANY persistent chain (α + β ≠ 1), there exists a permanent, non-vanishing discrepancy
between what the SR player actually believes (based on last observation) and the stationary
distribution π. This gap cannot be eliminated by longer time horizons or more observations.

This is a fundamental structural property of the observation process, not a convergence issue.

## Figures

![Belief Gap Heatmap](figures/belief_gap_heatmap.png)
![Gap vs Persistence](figures/gap_vs_persistence.png)

## Implication for the Paper

The paper's OT characterization relies on the lifted stationary distribution ρ̃ as if it
represents the SR player's effective belief distribution. But the actual per-period belief
is F(·|θ_t), which differs from the marginal of ρ̃ by the gap computed here. This means
confound-defeating at ρ̃ does not imply confound-defeating at the actual belief distribution,
invalidating the paper's main extension from i.i.d. to Markov states.
"""

    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Saved: {report_path}")


if __name__ == '__main__':
    print("=" * 60)
    print("SSA2_2: Divergence Analysis")
    print("=" * 60)

    heatmap = compute_heatmap()
    params, analytical_gaps, simulated_gaps = compute_1d_slice()

    # Print key results
    print("\nKey analytical results:")
    for alpha, beta in [(0.1, 0.1), (0.3, 0.5), (0.5, 0.5), (0.05, 0.05)]:
        g_G, g_B, e_gap = analytical_gap(alpha, beta)
        print(f"  α={alpha}, β={beta}: gap_G={g_G:.4f}, gap_B={g_B:.4f}, E[gap]={e_gap:.4f}")

    print(f"\nMax analytical-simulation discrepancy: "
          f"{np.max(np.abs(analytical_gaps - simulated_gaps)):.6f}")

    write_report(params, analytical_gaps, simulated_gaps)
    print("\nDone.")
