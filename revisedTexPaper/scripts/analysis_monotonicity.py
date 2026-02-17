#!/usr/bin/env python3
"""
analysis_monotonicity.py — SA7: Supermodularity / increasing differences check.

Enumerates orderings of the lifted state space (theta_t, theta_{t-1}) and
checks increasing differences for theta_t-only vs transition-dependent payoffs.

Generates: ../figures/fig_monotonicity.png (fraction by payoff type)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from itertools import permutations
import os


def check_increasing_differences(payoff_fn, order, actions):
    """Check increasing differences (supermodularity) for a given state order.

    For all s < s' in the order and a < a' in actions:
      payoff(s', a') - payoff(s', a) >= payoff(s, a') - payoff(s, a)

    Returns True if the condition holds for all pairs.
    """
    n = len(order)
    for i in range(n):
        for j in range(i + 1, n):
            s_lo = order[i]
            s_hi = order[j]
            for ai in range(len(actions)):
                for aj in range(ai + 1, len(actions)):
                    a_lo = actions[ai]
                    a_hi = actions[aj]
                    lhs = payoff_fn(s_hi, a_hi) - payoff_fn(s_hi, a_lo)
                    rhs = payoff_fn(s_lo, a_hi) - payoff_fn(s_lo, a_lo)
                    if lhs < rhs - 1e-10:
                        return False
    return True


def main():
    # Lifted states: (theta_t, theta_{t-1})
    # (0,0)=GG, (0,1)=GB, (1,0)=BG, (1,1)=BB
    lifted = [(0, 0), (0, 1), (1, 0), (1, 1)]
    actions = [0, 1]  # A, F

    # Game params
    x, y = 0.3, 0.4

    # Payoff type 1: theta_t-only (standard supermodular game)
    def payoff_theta_only(state_idx, action):
        theta_t = lifted[state_idx][0]
        u = np.array([[1.0, x], [y, 0.0]])
        return u[theta_t, action]

    # Payoff type 2: transition-dependent payoff
    # Adds a bonus/penalty based on whether state changed
    def payoff_transition(state_idx, action):
        theta_t, theta_prev = lifted[state_idx]
        u = np.array([[1.0, x], [y, 0.0]])
        base = u[theta_t, action]
        transition_bonus = 0.1 if theta_t != theta_prev else 0.0
        return base + transition_bonus * (1 - action)  # bonus for A when state changed

    # Enumerate all orderings of the 4 lifted states
    all_perms = list(permutations(range(4)))
    total = len(all_perms)

    valid_theta_only = 0
    valid_transition = 0

    for perm in all_perms:
        if check_increasing_differences(payoff_theta_only, perm, actions):
            valid_theta_only += 1
        if check_increasing_differences(payoff_transition, perm, actions):
            valid_transition += 1

    # ── Figure ──
    fig, ax = plt.subplots(figsize=(6, 4.5))
    categories = ['θ_t-only\n(standard)', 'Transition-\ndependent']
    counts = [valid_theta_only, valid_transition]
    fracs = [c / total * 100 for c in counts]

    bars = ax.bar(categories, counts, color=['#55A868', '#C44E52'],
                  width=0.5, edgecolor='black')
    ax.set_ylabel('# Valid orderings (supermodular)')
    ax.set_title(f'Supermodularity Check ({total} total orderings)')

    for bar, cnt, frac in zip(bars, counts, fracs):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                f'{cnt}\n({frac:.1f}%)', ha='center', va='bottom', fontsize=10)

    ax.set_ylim(0, max(counts) * 1.3)
    ax.axhline(total, color='gray', ls='--', alpha=0.5, label=f'Total = {total}')
    ax.legend()

    outdir = os.path.join(os.path.dirname(__file__), '..', 'figures')
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'fig_monotonicity.png')
    fig.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {outpath}")

    # Use the more relevant count (theta_t-only is the standard check)
    print(f"STAT:supermod_valid={valid_theta_only}")
    print(f"STAT:supermod_total={total}")


if __name__ == '__main__':
    main()
