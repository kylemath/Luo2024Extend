#!/usr/bin/env python3
"""
SSA7_2: Supermodularity Checker
================================
Checks whether the supermodularity (increasing differences) property holds
for payoffs on the lifted state space under various total orders.

Tests:
1. Lexicographic order on (theta_t, theta_{t-1})
2. First-coordinate order (by theta_t, ties broken by theta_{t-1})
3. Reverse-lex order (by theta_{t-1}, then theta_t)
4. Sampled random orders (10,000 of 9! = 362,880 possible)
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shared.markov_utils import save_figure

np.random.seed(42)

# ---------------------------------------------------------------------------
# 1. Define the 3-state game (matching SSA7_1)
# ---------------------------------------------------------------------------
N_STATES = 3
N_ACTIONS = 3
STATE_NAMES = ['L', 'M', 'H']
ACTION_NAMES = ['l', 'm', 'h']

LIFTED_STATES = [(th_t, th_prev) for th_t in range(N_STATES) for th_prev in range(N_STATES)]
N_LIFTED = len(LIFTED_STATES)
LIFTED_NAMES = [f"({STATE_NAMES[s[0]]},{STATE_NAMES[s[1]]})" for s in LIFTED_STATES]


def payoff_theta_t_only(th_t, th_prev, a):
    """Payoff depending only on theta_t: u1 = 1.5 * theta_t * a."""
    return 1.5 * th_t * a


def payoff_transition_dependent(th_t, th_prev, a):
    """Payoff depending on transition: u1 = 1.5*theta_t*a + 0.5*(theta_t - theta_{t-1})*a."""
    return 1.5 * th_t * a + 0.5 * (th_t - th_prev) * a


def payoff_strong_history(th_t, th_prev, a):
    """Payoff with strong history dependence: u1 = theta_t*a + theta_{t-1}*a."""
    return th_t * a + th_prev * a


# Build payoff matrices for all variants
def build_lifted_payoff(payoff_fn):
    """Build N_LIFTED x N_ACTIONS payoff matrix."""
    U = np.zeros((N_LIFTED, N_ACTIONS))
    for idx, (th_t, th_prev) in enumerate(LIFTED_STATES):
        for a in range(N_ACTIONS):
            U[idx, a] = payoff_fn(th_t, th_prev, a)
    return U


PAYOFF_VARIANTS = {
    'theta_t_only': build_lifted_payoff(payoff_theta_t_only),
    'transition_dep': build_lifted_payoff(payoff_transition_dependent),
    'strong_history': build_lifted_payoff(payoff_strong_history),
}

# ---------------------------------------------------------------------------
# 2. Supermodularity checker under a given total order
# ---------------------------------------------------------------------------
def check_supermod_under_order(payoff_matrix, order):
    """
    Check increasing differences of payoff_matrix[state, action] where
    states are ordered according to `order` (a permutation of indices)
    and actions are ordered 0 < 1 < 2.

    For all i < j in the order and a < a':
      payoff[order[j], a'] - payoff[order[j], a] >= payoff[order[i], a'] - payoff[order[i], a]

    Returns (is_supermod, n_violations).
    """
    n = len(order)
    n_a = payoff_matrix.shape[1]
    violations = 0

    for i_idx in range(n):
        for j_idx in range(i_idx + 1, n):
            s_low = order[i_idx]
            s_high = order[j_idx]
            for a in range(n_a):
                for a_prime in range(a + 1, n_a):
                    diff_high = payoff_matrix[s_high, a_prime] - payoff_matrix[s_high, a]
                    diff_low = payoff_matrix[s_low, a_prime] - payoff_matrix[s_low, a]
                    if diff_high < diff_low - 1e-12:
                        violations += 1
    return violations == 0, violations


# ---------------------------------------------------------------------------
# 3. Define canonical orders
# ---------------------------------------------------------------------------
# Lexicographic: (theta_t, theta_{t-1}), both ascending
lex_order = sorted(range(N_LIFTED), key=lambda i: (LIFTED_STATES[i][0], LIFTED_STATES[i][1]))

# First-coordinate: by theta_t, ties broken by theta_{t-1}
first_coord_order = sorted(range(N_LIFTED), key=lambda i: (LIFTED_STATES[i][0], LIFTED_STATES[i][1]))

# Reverse-lex: (theta_{t-1}, theta_t), both ascending
reverse_lex_order = sorted(range(N_LIFTED), key=lambda i: (LIFTED_STATES[i][1], LIFTED_STATES[i][0]))

# "Sum" order: by theta_t + theta_{t-1}, ties broken by theta_t
sum_order = sorted(range(N_LIFTED), key=lambda i: (LIFTED_STATES[i][0] + LIFTED_STATES[i][1], LIFTED_STATES[i][0]))

CANONICAL_ORDERS = {
    'lexicographic': lex_order,
    'first_coord': first_coord_order,
    'reverse_lex': reverse_lex_order,
    'sum_order': sum_order,
}

# ---------------------------------------------------------------------------
# 4. Test canonical orders
# ---------------------------------------------------------------------------
print("=" * 60)
print("SSA7_2: Supermodularity Checker")
print("=" * 60)

canonical_results = {}
for order_name, order in CANONICAL_ORDERS.items():
    print(f"\n--- Order: {order_name} ---")
    print(f"  Order: {[LIFTED_NAMES[i] for i in order]}")
    for payoff_name, payoff_mat in PAYOFF_VARIANTS.items():
        is_sm, n_viol = check_supermod_under_order(payoff_mat, order)
        canonical_results[(order_name, payoff_name)] = (is_sm, n_viol)
        status = "YES" if is_sm else f"NO ({n_viol} violations)"
        print(f"  {payoff_name}: supermodular = {status}")

# ---------------------------------------------------------------------------
# 5. Sample random orders and check supermodularity
# ---------------------------------------------------------------------------
N_SAMPLES = 10000
base_perm = list(range(N_LIFTED))
random_results = {name: 0 for name in PAYOFF_VARIANTS}

print(f"\n--- Sampling {N_SAMPLES} random orders ---")
for _ in range(N_SAMPLES):
    perm = np.random.permutation(N_LIFTED).tolist()
    for payoff_name, payoff_mat in PAYOFF_VARIANTS.items():
        is_sm, _ = check_supermod_under_order(payoff_mat, perm)
        if is_sm:
            random_results[payoff_name] += 1

print("\nFraction of random orders where supermodularity holds:")
fractions = {}
for payoff_name, count in random_results.items():
    frac = count / N_SAMPLES
    fractions[payoff_name] = frac
    print(f"  {payoff_name}: {count}/{N_SAMPLES} = {frac:.4f}")

# ---------------------------------------------------------------------------
# 6. Exhaustive enumeration for the theta_t-only payoff
# ---------------------------------------------------------------------------
# Since payoffs depend only on theta_t, any order that preserves
# the theta_t ranking should work. Let's count exactly.
# Group states by theta_t: groups of 3 (for each theta_t value).
# Within each group, any permutation is fine, but between groups
# the theta_t order must be preserved.

from itertools import permutations

# For tractability, enumerate all 9! = 362880 permutations
print("\n--- Exhaustive enumeration (9! = 362,880 orders) ---")
print("(This may take a moment...)")

exhaustive_counts = {name: 0 for name in PAYOFF_VARIANTS}
total_perms = 0

# Use a more efficient approach: iterate permutations
# For 9! this is feasible (362880 permutations)
for perm in permutations(range(N_LIFTED)):
    total_perms += 1
    perm_list = list(perm)
    for payoff_name, payoff_mat in PAYOFF_VARIANTS.items():
        is_sm, _ = check_supermod_under_order(payoff_mat, perm_list)
        if is_sm:
            exhaustive_counts[payoff_name] += 1

print(f"\nTotal permutations checked: {total_perms}")
print("\nExact fractions where supermodularity holds:")
exact_fractions = {}
for payoff_name, count in exhaustive_counts.items():
    frac = count / total_perms
    exact_fractions[payoff_name] = frac
    print(f"  {payoff_name}: {count}/{total_perms} = {frac:.6f}")

# ---------------------------------------------------------------------------
# 7. Figures
# ---------------------------------------------------------------------------
fig_dir = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(fig_dir, exist_ok=True)

# Figure 1: Fraction of valid orders per payoff type (exhaustive)
fig, ax = plt.subplots(figsize=(9, 6))
payoff_names = list(exact_fractions.keys())
payoff_labels = ['θ_t only', 'Transition\ndependent', 'Strong\nhistory']
frac_values = [exact_fractions[n] for n in payoff_names]
count_values = [exhaustive_counts[n] for n in payoff_names]

bars = ax.bar(payoff_labels, frac_values, color=['#2196F3', '#FF9800', '#4CAF50'],
              edgecolor='black', linewidth=1.2)
ax.set_ylabel('Fraction of Orders with Supermodularity', fontsize=12)
ax.set_title('Supermodularity Under Random Total Orders on Lifted Space\n'
             f'(Exhaustive: all {total_perms:,} permutations)', fontsize=13)
ax.set_ylim(0, max(frac_values) * 1.3 if max(frac_values) > 0 else 1.0)

for bar, frac, cnt in zip(bars, frac_values, count_values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
            f'{frac:.4f}\n({cnt:,}/{total_perms:,})',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.axhline(y=1.0 / total_perms * 6, color='gray', linestyle='--', alpha=0.5)
plt.tight_layout()
path1 = os.path.join(fig_dir, 'supermod_fraction_by_payoff.png')
save_figure(fig, path1)
print(f"\nSaved: {path1}")

# Figure 2: Canonical order results as a table-like heatmap
fig2, ax2 = plt.subplots(figsize=(9, 5))
order_names = list(CANONICAL_ORDERS.keys())
payoff_names_list = list(PAYOFF_VARIANTS.keys())

result_matrix = np.zeros((len(order_names), len(payoff_names_list)))
for i, oname in enumerate(order_names):
    for j, pname in enumerate(payoff_names_list):
        is_sm, _ = canonical_results[(oname, pname)]
        result_matrix[i, j] = 1.0 if is_sm else 0.0

im = ax2.imshow(result_matrix, cmap='RdYlGn', vmin=0, vmax=1, aspect='auto')
ax2.set_xticks(range(len(payoff_names_list)))
ax2.set_xticklabels(['θ_t only', 'Transition dep.', 'Strong history'], fontsize=10)
ax2.set_yticks(range(len(order_names)))
ax2.set_yticklabels(order_names, fontsize=10)
ax2.set_title('Supermodularity Under Canonical Orders', fontsize=13)

for i in range(len(order_names)):
    for j in range(len(payoff_names_list)):
        is_sm, n_viol = canonical_results[(order_names[i], payoff_names_list[j])]
        txt = "✓" if is_sm else f"✗ ({n_viol})"
        color = 'white' if not is_sm else 'black'
        ax2.text(j, i, txt, ha='center', va='center', fontsize=12,
                 fontweight='bold', color=color)

plt.colorbar(im, ax=ax2, label='Supermodular (1=Yes, 0=No)')
plt.tight_layout()
path2 = os.path.join(fig_dir, 'canonical_order_results.png')
save_figure(fig2, path2)
print(f"Saved: {path2}")

# ---------------------------------------------------------------------------
# 8. Generate report.md
# ---------------------------------------------------------------------------
report_lines = [
    "# SSA7_2: Supermodularity Checker — Report",
    "",
    "## Objective",
    "Check whether increasing differences (supermodularity) of payoffs extends",
    "from the base 3-state game to the lifted state space Θ̃ = Θ × Θ (9 states)",
    "under various total orderings.",
    "",
    "## Payoff Variants",
    "1. **θ_t-only:** u₁(θ̃, a) = 1.5 · θ_t · a",
    "2. **Transition-dependent:** u₁(θ̃, a) = 1.5·θ_t·a + 0.5·(θ_t − θ_{t-1})·a",
    "3. **Strong history:** u₁(θ̃, a) = θ_t·a + θ_{t-1}·a",
    "",
    "## Canonical Order Results",
    "",
    "| Order | θ_t only | Transition dep. | Strong history |",
    "|-------|----------|-----------------|----------------|",
]

for oname in order_names:
    row = f"| {oname} |"
    for pname in payoff_names_list:
        is_sm, n_viol = canonical_results[(oname, pname)]
        cell = " ✓ |" if is_sm else f" ✗ ({n_viol} viol.) |"
        row += cell
    report_lines.append(row)

report_lines.extend([
    "",
    "## Exhaustive Enumeration (All 362,880 Orders)",
    "",
    "| Payoff Type | Valid Orders | Fraction |",
    "|-------------|-------------|----------|",
])

for pname in payoff_names_list:
    cnt = exhaustive_counts[pname]
    frac = exact_fractions[pname]
    label = {'theta_t_only': 'θ_t only', 'transition_dep': 'Transition dep.',
             'strong_history': 'Strong history'}[pname]
    report_lines.append(f"| {label} | {cnt:,} | {frac:.6f} |")

report_lines.extend([
    "",
    "## Figures",
    "![Supermodularity Fraction](figures/supermod_fraction_by_payoff.png)",
    "![Canonical Order Results](figures/canonical_order_results.png)",
    "",
    "## Key Findings",
    "",
    f"1. **θ_t-only payoff:** Supermodularity holds under {exhaustive_counts['theta_t_only']:,} of "
    f"{total_perms:,} orders ({exact_fractions['theta_t_only']:.4%}). "
    "Any order that respects the θ_t ranking preserves supermodularity, since the payoff ignores θ_{t-1}.",
    "",
    f"2. **Transition-dependent payoff:** Only {exhaustive_counts['transition_dep']:,} of "
    f"{total_perms:,} orders preserve supermodularity ({exact_fractions['transition_dep']:.4%}). "
    "The coupling between θ_t and θ_{t-1} makes it harder to find a consistent order.",
    "",
    f"3. **Strong history payoff:** {exhaustive_counts['strong_history']:,} of "
    f"{total_perms:,} orders work ({exact_fractions['strong_history']:.4%}). "
    "Since both coordinates contribute symmetrically, sum-based orders perform well.",
    "",
    "4. **Implication for the paper:** Monotonicity/supermodularity does NOT automatically extend",
    "   to the lifted state space for all payoff structures. The choice of order on Θ̃ is crucial.",
    "   For payoffs depending only on θ_t, any θ_t-consistent order suffices; but for",
    "   transition-dependent payoffs, valid orders may be rare or non-existent.",
])

report_path = os.path.join(os.path.dirname(__file__), 'report.md')
with open(report_path, 'w') as f:
    f.write('\n'.join(report_lines))
print(f"\nReport saved: {report_path}")
print("\n[SSA7_2 COMPLETE]")
