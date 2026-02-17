#!/usr/bin/env python3
"""
SSA7_1: Multi-State Game Setup
==============================
Defines a 3-state, 3-action deterrence game and its lifted state space.
Tests whether the supermodular payoff structure extends to the lifted space
Theta_tilde = Theta x Theta (9 states).
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shared.markov_utils import save_figure

# ---------------------------------------------------------------------------
# 1. Define the 3-state game: Theta = {L, M, H} = {0, 1, 2}
# ---------------------------------------------------------------------------
STATE_NAMES = ['L', 'M', 'H']
ACTION_NAMES = ['l', 'm', 'h']
N_STATES = 3
N_ACTIONS = 3


def supermodular_payoff(theta, a):
    """
    Payoff u1(theta, a) = 1.5 * theta * a  (for theta, a in {0, 1, 2}).
    This has increasing differences:
      u1(theta', a') - u1(theta', a) - u1(theta, a') + u1(theta, a)
      = 1.5 * (theta' - theta) * (a' - a) >= 0  for theta' >= theta, a' >= a.
    """
    return 1.5 * theta * a


# Build payoff matrix u1[theta, a]
U1 = np.zeros((N_STATES, N_ACTIONS))
for th in range(N_STATES):
    for a in range(N_ACTIONS):
        U1[th, a] = supermodular_payoff(th, a)

# ---------------------------------------------------------------------------
# 2. Verify supermodularity of the base game
# ---------------------------------------------------------------------------
def check_increasing_differences(payoff_matrix):
    """
    Check increasing differences: for all theta' > theta, a' > a:
      payoff(theta', a') - payoff(theta', a) >= payoff(theta, a') - payoff(theta, a)
    Returns (is_supermodular, violations_list).
    """
    n_s, n_a = payoff_matrix.shape
    violations = []
    for th in range(n_s):
        for th_prime in range(th + 1, n_s):
            for a in range(n_a):
                for a_prime in range(a + 1, n_a):
                    diff_high = payoff_matrix[th_prime, a_prime] - payoff_matrix[th_prime, a]
                    diff_low = payoff_matrix[th, a_prime] - payoff_matrix[th, a]
                    if diff_high < diff_low - 1e-12:
                        violations.append((th, th_prime, a, a_prime,
                                           diff_high - diff_low))
    return len(violations) == 0, violations


base_supermod, base_violations = check_increasing_differences(U1)

# ---------------------------------------------------------------------------
# 3. Markov chain on {L, M, H}
# ---------------------------------------------------------------------------
# Transition matrix T[i, j] = Pr(state j | state i)
# A "persistence-biased" chain where staying in the same state is most likely.
ALPHA_STAY = 0.6
T = np.array([
    [ALPHA_STAY, 0.3, 0.1],       # From L
    [0.2, ALPHA_STAY, 0.2],       # From M
    [0.1, 0.3, ALPHA_STAY],       # From H
])

# Stationary distribution (left eigenvector for eigenvalue 1)
eigenvalues, eigenvectors = np.linalg.eig(T.T)
idx = np.argmin(np.abs(eigenvalues - 1.0))
pi_raw = eigenvectors[:, idx].real
pi = pi_raw / pi_raw.sum()

# ---------------------------------------------------------------------------
# 4. Lifted state space: Theta_tilde = Theta x Theta  (9 states)
# ---------------------------------------------------------------------------
# Lifted state (theta_t, theta_{t-1}) indexed as theta_t * 3 + theta_{t-1}
LIFTED_STATES = [(th_t, th_prev) for th_t in range(N_STATES) for th_prev in range(N_STATES)]
N_LIFTED = len(LIFTED_STATES)
LIFTED_NAMES = [f"({STATE_NAMES[s[0]]},{STATE_NAMES[s[1]]})" for s in LIFTED_STATES]

# Lifted stationary distribution:
# rho_tilde(theta_t, theta_{t-1}) = pi(theta_{t-1}) * T[theta_{t-1}, theta_t]
rho_tilde = np.zeros(N_LIFTED)
for idx_l, (th_t, th_prev) in enumerate(LIFTED_STATES):
    rho_tilde[idx_l] = pi[th_prev] * T[th_prev, th_t]
rho_tilde /= rho_tilde.sum()  # Normalize for numerical safety

# ---------------------------------------------------------------------------
# 5. Payoff on lifted state space (depends only on theta_t)
# ---------------------------------------------------------------------------
U1_lifted = np.zeros((N_LIFTED, N_ACTIONS))
for idx_l, (th_t, th_prev) in enumerate(LIFTED_STATES):
    for a in range(N_ACTIONS):
        U1_lifted[idx_l, a] = supermodular_payoff(th_t, a)

# ---------------------------------------------------------------------------
# 6. Transition-dependent payoff variant
# ---------------------------------------------------------------------------
def transition_dependent_payoff(th_t, th_prev, a):
    """
    Payoff that depends on both current and previous state:
    u1(theta_t, theta_{t-1}, a) = 1.5 * theta_t * a + 0.5 * (theta_t - theta_{t-1}) * a
    The transition bonus rewards "improvement" (moving to higher state).
    """
    return 1.5 * th_t * a + 0.5 * (th_t - th_prev) * a


U1_transition = np.zeros((N_LIFTED, N_ACTIONS))
for idx_l, (th_t, th_prev) in enumerate(LIFTED_STATES):
    for a in range(N_ACTIONS):
        U1_transition[idx_l, a] = transition_dependent_payoff(th_t, th_prev, a)

# ---------------------------------------------------------------------------
# 7. Define canonical orders on the lifted state space
# ---------------------------------------------------------------------------

# Lexicographic order: primary = theta_t, secondary = theta_{t-1}
lex_order = sorted(range(N_LIFTED), key=lambda i: (LIFTED_STATES[i][0], LIFTED_STATES[i][1]))

# First-coordinate order: by theta_t only, ties broken by theta_{t-1}
first_coord_order = sorted(range(N_LIFTED), key=lambda i: (LIFTED_STATES[i][0], LIFTED_STATES[i][1]))
# (Same as lex for this encoding, but conceptually different — groups by theta_t)

# Reverse-lex order: primary = theta_{t-1}, secondary = theta_t
reverse_lex_order = sorted(range(N_LIFTED), key=lambda i: (LIFTED_STATES[i][1], LIFTED_STATES[i][0]))

# ---------------------------------------------------------------------------
# 8. Print summary
# ---------------------------------------------------------------------------
print("=" * 60)
print("SSA7_1: Multi-State Game Setup")
print("=" * 60)

print("\n--- Base Game ---")
print(f"States: {STATE_NAMES}")
print(f"Actions: {ACTION_NAMES}")
print(f"\nPayoff matrix u1[theta, a]:")
header = "       " + "  ".join(f"{a:>6s}" for a in ACTION_NAMES)
print(header)
for i, s in enumerate(STATE_NAMES):
    row = f"  {s}:  " + "  ".join(f"{U1[i, j]:6.2f}" for j in range(N_ACTIONS))
    print(row)
print(f"\nBase game supermodular: {base_supermod}")
if base_violations:
    print(f"  Violations: {base_violations}")

print("\n--- Markov Chain ---")
print(f"Transition matrix T:")
for i, s in enumerate(STATE_NAMES):
    print(f"  {s}: {T[i]}")
print(f"\nStationary distribution pi: {pi}")

print("\n--- Lifted State Space (9 states) ---")
print(f"States: {LIFTED_NAMES}")
print(f"\nLifted stationary distribution rho_tilde:")
for i, name in enumerate(LIFTED_NAMES):
    print(f"  {name}: {rho_tilde[i]:.6f}")

print(f"\n--- Lexicographic Order ---")
print([LIFTED_NAMES[i] for i in lex_order])

print(f"\n--- Reverse-Lex Order (by theta_{{t-1}}) ---")
print([LIFTED_NAMES[i] for i in reverse_lex_order])

print(f"\n--- Lifted Payoff (theta_t only) ---")
for i, name in enumerate(LIFTED_NAMES):
    print(f"  {name}: {U1_lifted[i]}")

print(f"\n--- Transition-Dependent Payoff ---")
for i, name in enumerate(LIFTED_NAMES):
    print(f"  {name}: {U1_transition[i]}")

# ---------------------------------------------------------------------------
# 9. Figures
# ---------------------------------------------------------------------------
fig_dir = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(fig_dir, exist_ok=True)

# Figure 1: Base payoff heatmap
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Base payoff
im0 = axes[0].imshow(U1, cmap='YlOrRd', aspect='auto')
axes[0].set_xticks(range(N_ACTIONS))
axes[0].set_xticklabels(ACTION_NAMES)
axes[0].set_yticks(range(N_STATES))
axes[0].set_yticklabels(STATE_NAMES)
axes[0].set_xlabel('Action')
axes[0].set_ylabel('State')
axes[0].set_title('Base Payoff u1(θ, a)')
for i in range(N_STATES):
    for j in range(N_ACTIONS):
        axes[0].text(j, i, f'{U1[i, j]:.1f}', ha='center', va='center', fontsize=12)
plt.colorbar(im0, ax=axes[0])

# Lifted payoff (theta_t only)
im1 = axes[1].imshow(U1_lifted, cmap='YlOrRd', aspect='auto')
axes[1].set_xticks(range(N_ACTIONS))
axes[1].set_xticklabels(ACTION_NAMES)
axes[1].set_yticks(range(N_LIFTED))
axes[1].set_yticklabels(LIFTED_NAMES, fontsize=7)
axes[1].set_xlabel('Action')
axes[1].set_ylabel('Lifted State (θ_t, θ_{t-1})')
axes[1].set_title('Lifted Payoff (θ_t only)')
plt.colorbar(im1, ax=axes[1])

# Transition-dependent payoff
im2 = axes[2].imshow(U1_transition, cmap='RdBu_r', aspect='auto')
axes[2].set_xticks(range(N_ACTIONS))
axes[2].set_xticklabels(ACTION_NAMES)
axes[2].set_yticks(range(N_LIFTED))
axes[2].set_yticklabels(LIFTED_NAMES, fontsize=7)
axes[2].set_xlabel('Action')
axes[2].set_ylabel('Lifted State (θ_t, θ_{t-1})')
axes[2].set_title('Transition-Dependent Payoff')
plt.colorbar(im2, ax=axes[2])

plt.tight_layout()
path1 = os.path.join(fig_dir, 'payoff_matrices.png')
save_figure(fig, path1)
print(f"\nSaved: {path1}")

# Figure 2: Stationary distributions
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))

axes2[0].bar(STATE_NAMES, pi, color='steelblue', edgecolor='black')
axes2[0].set_title('Stationary Distribution π (Base Chain)')
axes2[0].set_ylabel('Probability')
for i, v in enumerate(pi):
    axes2[0].text(i, v + 0.01, f'{v:.4f}', ha='center', fontsize=9)

axes2[1].bar(range(N_LIFTED), rho_tilde, color='coral', edgecolor='black')
axes2[1].set_xticks(range(N_LIFTED))
axes2[1].set_xticklabels(LIFTED_NAMES, rotation=45, ha='right', fontsize=8)
axes2[1].set_title('Lifted Stationary Distribution ρ̃')
axes2[1].set_ylabel('Probability')
for i, v in enumerate(rho_tilde):
    axes2[1].text(i, v + 0.005, f'{v:.4f}', ha='center', fontsize=7)

plt.tight_layout()
path2 = os.path.join(fig_dir, 'stationary_distributions.png')
save_figure(fig2, path2)
print(f"Saved: {path2}")

# Figure 3: Transition matrix heatmap
fig3, ax3 = plt.subplots(figsize=(6, 5))
im3 = ax3.imshow(T, cmap='Blues', vmin=0, vmax=1)
ax3.set_xticks(range(N_STATES))
ax3.set_xticklabels(STATE_NAMES)
ax3.set_yticks(range(N_STATES))
ax3.set_yticklabels(STATE_NAMES)
ax3.set_xlabel('To State')
ax3.set_ylabel('From State')
ax3.set_title('Transition Matrix T')
for i in range(N_STATES):
    for j in range(N_STATES):
        ax3.text(j, i, f'{T[i, j]:.2f}', ha='center', va='center', fontsize=12)
plt.colorbar(im3, ax=ax3)
plt.tight_layout()
path3 = os.path.join(fig_dir, 'transition_matrix.png')
save_figure(fig3, path3)
print(f"Saved: {path3}")

# ---------------------------------------------------------------------------
# 10. Generate report.md
# ---------------------------------------------------------------------------
report_lines = [
    "# SSA7_1: Multi-State Game Setup — Report",
    "",
    "## Base Game",
    f"- **States:** Θ = {{{', '.join(STATE_NAMES)}}} with order L < M < H",
    f"- **Actions:** A₁ = {{{', '.join(ACTION_NAMES)}}} with order l < m < h",
    "- **Payoff:** u₁(θ, a) = 1.5 · θ · a  (θ, a ∈ {0, 1, 2})",
    f"- **Supermodular:** {base_supermod}",
    "",
    "### Payoff Matrix",
    "| | l | m | h |",
    "|---|---|---|---|",
]
for i, s in enumerate(STATE_NAMES):
    report_lines.append(f"| {s} | {U1[i,0]:.1f} | {U1[i,1]:.1f} | {U1[i,2]:.1f} |")

report_lines.extend([
    "",
    "## Markov Chain",
    f"- **Persistence parameter:** α_stay = {ALPHA_STAY}",
    f"- **Stationary distribution:** π = [{', '.join(f'{v:.4f}' for v in pi)}]",
    "",
    "## Lifted State Space",
    f"- **Θ̃ = Θ × Θ:** {N_LIFTED} states",
    f"- **States:** {', '.join(LIFTED_NAMES)}",
    "",
    "### Lifted Stationary Distribution",
    "| State | ρ̃ |",
    "|---|---|",
])
for i, name in enumerate(LIFTED_NAMES):
    report_lines.append(f"| {name} | {rho_tilde[i]:.6f} |")

report_lines.extend([
    "",
    "## Payoff Variants",
    "1. **θ_t-only payoff:** u₁(θ̃, a) = 1.5 · θ_t · a (ignores θ_{t-1})",
    "2. **Transition-dependent:** u₁(θ̃, a) = 1.5 · θ_t · a + 0.5 · (θ_t − θ_{t-1}) · a",
    "",
    "## Figures",
    "![Payoff Matrices](figures/payoff_matrices.png)",
    "![Stationary Distributions](figures/stationary_distributions.png)",
    "![Transition Matrix](figures/transition_matrix.png)",
    "",
    "## Key Observations",
    "- The base game is supermodular with increasing differences.",
    "- The lifted state space has 9 states, making exhaustive order enumeration feasible (9! = 362,880).",
    "- The θ_t-only payoff preserves the base game's structure for states grouped by θ_t.",
    "- The transition-dependent payoff introduces interactions between θ_t and θ_{t-1}.",
    "- These structures will be tested for supermodularity under various orders in SSA7_2.",
])

report_path = os.path.join(os.path.dirname(__file__), 'report.md')
with open(report_path, 'w') as f:
    f.write('\n'.join(report_lines))
print(f"\nReport saved: {report_path}")
print("\n[SSA7_1 COMPLETE]")
