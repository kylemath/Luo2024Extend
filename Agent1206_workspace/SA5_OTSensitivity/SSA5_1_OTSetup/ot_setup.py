#!/usr/bin/env python3
"""
SSA5_1: OT Problem Setup
Formulates and solves the optimal transport problem for the deterrence game
on the lifted state space at the stationary distribution.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from shared.markov_utils import (
    MarkovChain, DeterrenceGame, make_strategy_matrix, save_figure
)

FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)


def solve_ot_problem(mu, phi, cost_matrix):
    """
    Solve the optimal transport problem via linear programming.

    Maximise  sum_{i,j} gamma[i,j] * cost_matrix[i,j]
    subject to:
        sum_j gamma[i,j] = mu[i]   for each i  (state marginal)
        sum_i gamma[i,j] = phi[j]  for each j  (action marginal)
        gamma[i,j] >= 0

    Parameters
    ----------
    mu : array (n,)  — state marginal
    phi : array (m,) — action marginal
    cost_matrix : array (n, m) — payoff/cost

    Returns
    -------
    gamma : array (n, m) — optimal coupling
    obj_val : float — optimal objective value
    """
    n = len(mu)
    m = len(phi)

    # linprog minimises c^T x, so negate for maximisation
    c = -cost_matrix.flatten()

    # Equality constraints: A_eq @ x = b_eq
    # Row marginals: for each i, sum_j gamma[i,j] = mu[i]
    # Column marginals: for each j, sum_i gamma[i,j] = phi[j]
    n_vars = n * m
    n_eq = n + m
    A_eq = np.zeros((n_eq, n_vars))
    b_eq = np.zeros(n_eq)

    # Row marginals
    for i in range(n):
        for j in range(m):
            A_eq[i, i * m + j] = 1.0
        b_eq[i] = mu[i]

    # Column marginals
    for j in range(m):
        for i in range(n):
            A_eq[n + j, i * m + j] = 1.0
        b_eq[n + j] = phi[j]

    bounds = [(0, None)] * n_vars

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if not result.success:
        raise RuntimeError(f"LP solver failed: {result.message}")

    gamma = result.x.reshape(n, m)
    obj_val = -result.fun  # negate back

    return gamma, obj_val


def build_payoff_matrix(mc, game):
    """
    Build the payoff matrix u1[lifted_state, action] for the OT problem.

    Lifted states: (G,G)=0, (G,B)=1, (B,G)=2, (B,B)=3
    Payoff depends only on current state theta_t:
      u1(theta_t, a1)
    """
    n_lifted = mc.n_lifted
    n_actions = game.n_actions
    U = np.zeros((n_lifted, n_actions))

    for idx, (theta_t, theta_prev) in enumerate(mc.lifted_states):
        for a in range(n_actions):
            U[idx, a] = game.u1[theta_t, a]

    return U


def compute_action_marginal(mc, game):
    """
    Compute action marginal phi under the Stackelberg strategy at stationarity.

    Stackelberg: A in G, F in B.
    phi(A) = Pr(theta_t = G) = pi(G) summed over lifted states with theta_t=G
    phi(F) = Pr(theta_t = B)
    """
    strat_mat = make_strategy_matrix(game.stackelberg_strategy)

    # Action marginal: phi[a] = sum_{tilde_theta} rho_tilde[tilde_theta] * sigma[theta_t, a]
    phi = np.zeros(game.n_actions)
    for idx, (theta_t, theta_prev) in enumerate(mc.lifted_states):
        for a in range(game.n_actions):
            phi[a] += mc.rho_tilde[idx] * strat_mat[theta_t, a]

    return phi


def build_comonotone_coupling(mc, game):
    """
    Build the co-monotone coupling for a supermodular game.

    For the deterrence game with Stackelberg strategy:
      - States with theta_t = G are coupled with A
      - States with theta_t = B are coupled with F
    """
    n_lifted = mc.n_lifted
    n_actions = game.n_actions
    gamma = np.zeros((n_lifted, n_actions))

    for idx, (theta_t, theta_prev) in enumerate(mc.lifted_states):
        a = game.stackelberg_strategy(theta_t)
        gamma[idx, a] = mc.rho_tilde[idx]

    return gamma


def plot_coupling_heatmap(gamma, mc, game, title, filepath):
    """Plot a heatmap of the coupling matrix."""
    fig, ax = plt.subplots(figsize=(6, 5))

    lifted_labels = [f"({mc.states[t]},{mc.states[p]})" for t, p in mc.lifted_states]
    action_labels = game.actions

    im = ax.imshow(gamma, cmap='Blues', aspect='auto', vmin=0)
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label('Coupling weight γ(θ̃, a₁)')

    ax.set_xticks(range(len(action_labels)))
    ax.set_xticklabels(action_labels, fontsize=12)
    ax.set_yticks(range(len(lifted_labels)))
    ax.set_yticklabels(lifted_labels, fontsize=12)
    ax.set_xlabel('Action a₁', fontsize=13)
    ax.set_ylabel('Lifted state (θ_t, θ_{t-1})', fontsize=13)
    ax.set_title(title, fontsize=14)

    # Annotate cells
    for i in range(gamma.shape[0]):
        for j in range(gamma.shape[1]):
            val = gamma[i, j]
            color = 'white' if val > gamma.max() * 0.6 else 'black'
            ax.text(j, i, f'{val:.4f}', ha='center', va='center',
                    fontsize=11, color=color, fontweight='bold')

    fig.tight_layout()
    save_figure(fig, filepath)
    print(f"  Saved: {filepath}")


def main():
    print("=" * 60)
    print("SSA5_1: OT Problem Setup")
    print("=" * 60)

    mc = MarkovChain(alpha=0.3, beta=0.5)
    game = DeterrenceGame(x=0.3, y=0.4)

    print(f"\nMarkov chain: alpha={mc.alpha}, beta={mc.beta}")
    print(f"Stationary dist pi: G={mc.pi[0]:.4f}, B={mc.pi[1]:.4f}")
    print(f"Lifted stationary rho_tilde: {mc.rho_tilde}")
    print(f"Game: x={game.x}, y={game.y}, supermodular={game.is_supermodular}")

    # Build payoff matrix
    U = build_payoff_matrix(mc, game)
    print(f"\nPayoff matrix U[lifted_state, action]:")
    lifted_labels = [f"({mc.states[t]},{mc.states[p]})" for t, p in mc.lifted_states]
    print(f"  {'':>8}  {'A':>8}  {'F':>8}")
    for i, lbl in enumerate(lifted_labels):
        print(f"  {lbl:>8}  {U[i,0]:>8.2f}  {U[i,1]:>8.2f}")

    # Compute action marginal under Stackelberg
    phi = compute_action_marginal(mc, game)
    print(f"\nAction marginal phi under Stackelberg: A={phi[0]:.4f}, F={phi[1]:.4f}")

    # State marginal
    mu = mc.rho_tilde.copy()
    print(f"State marginal mu (rho_tilde): {mu}")

    # Verify marginals sum to 1
    print(f"\nMarginal checks: sum(mu)={mu.sum():.6f}, sum(phi)={phi.sum():.6f}")

    # Solve OT problem
    print("\n--- Solving OT problem via linprog ---")
    gamma_opt, obj_val = solve_ot_problem(mu, phi, U)
    print(f"Optimal objective: {obj_val:.6f}")
    print(f"\nOptimal coupling gamma*:")
    print(f"  {'':>8}  {'A':>8}  {'F':>8}")
    for i, lbl in enumerate(lifted_labels):
        print(f"  {lbl:>8}  {gamma_opt[i,0]:>8.5f}  {gamma_opt[i,1]:>8.5f}")

    # Identify support
    support_threshold = 1e-8
    support = []
    print(f"\nSupport of optimal coupling (threshold={support_threshold}):")
    for i in range(gamma_opt.shape[0]):
        for j in range(gamma_opt.shape[1]):
            if gamma_opt[i, j] > support_threshold:
                support.append((lifted_labels[i], game.actions[j]))
                print(f"  ({lifted_labels[i]}, {game.actions[j]}): {gamma_opt[i,j]:.6f}")

    # Build co-monotone coupling for comparison
    gamma_como = build_comonotone_coupling(mc, game)
    print(f"\nCo-monotone coupling (theoretical):")
    print(f"  {'':>8}  {'A':>8}  {'F':>8}")
    for i, lbl in enumerate(lifted_labels):
        print(f"  {lbl:>8}  {gamma_como[i,0]:>8.5f}  {gamma_como[i,1]:>8.5f}")

    # Verify match
    diff = np.abs(gamma_opt - gamma_como).max()
    match = diff < 1e-6
    print(f"\nMax difference from co-monotone: {diff:.2e}")
    print(f"Matches co-monotone coupling: {match}")

    # Co-monotone objective value
    como_obj = np.sum(gamma_como * U)
    print(f"Co-monotone objective: {como_obj:.6f}")

    # Plot coupling heatmap
    plot_coupling_heatmap(
        gamma_opt, mc, game,
        "Optimal OT Coupling at Stationary Distribution ρ̃",
        os.path.join(FIGURES_DIR, 'ot_coupling_stationary.png')
    )

    # Generate report
    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write("# SSA5_1: OT Problem Setup — Report\n\n")
        f.write("## Parameters\n")
        f.write(f"- Markov chain: α={mc.alpha}, β={mc.beta}\n")
        f.write(f"- Stationary distribution π: G={mc.pi[0]:.4f}, B={mc.pi[1]:.4f}\n")
        f.write(f"- Deterrence game: x={game.x}, y={game.y}, supermodular={game.is_supermodular}\n\n")

        f.write("## OT Problem Formulation\n")
        f.write("- **State space**: Lifted Θ̃ = {(G,G), (G,B), (B,G), (B,B)}\n")
        f.write("- **Action space**: A₁ = {A, F}\n")
        f.write("- **State marginal** μ = ρ̃ (lifted stationary distribution)\n")
        f.write(f"- **Action marginal** ϕ: A={phi[0]:.4f}, F={phi[1]:.4f}\n")
        f.write("- **Objective**: maximise Σ γ[θ̃, a₁] · u₁(θ̃, a₁)\n\n")

        f.write("## Results\n")
        f.write(f"- **Optimal objective value**: {obj_val:.6f}\n")
        f.write(f"- **Co-monotone objective value**: {como_obj:.6f}\n")
        f.write(f"- **Max difference from co-monotone**: {diff:.2e}\n")
        f.write(f"- **Matches co-monotone**: {match}\n\n")

        f.write("## Support of Optimal Coupling\n")
        for (s, a) in support:
            f.write(f"- ({s}, {a})\n")
        f.write("\n")

        f.write("## Interpretation\n")
        f.write("The OT solution at the stationary distribution ρ̃ matches the co-monotone coupling, ")
        f.write("which is expected for a supermodular game. The support assigns:\n")
        f.write("- All lifted states with θ_t = G → action A (Acquiesce)\n")
        f.write("- All lifted states with θ_t = B → action F (Fight)\n\n")
        f.write("This confirms the Stackelberg strategy is OT-optimal at ρ̃. ")
        f.write("The key question (addressed in SSA5_2) is whether this remains true when μ ≠ ρ̃.\n\n")

        f.write("## Figures\n")
        f.write("![OT Coupling Heatmap](figures/ot_coupling_stationary.png)\n")

    print(f"\n  Report saved to: {report_path}")
    print("\nDone.")


if __name__ == '__main__':
    main()
