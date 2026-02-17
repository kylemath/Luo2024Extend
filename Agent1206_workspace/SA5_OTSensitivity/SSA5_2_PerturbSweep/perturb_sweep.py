#!/usr/bin/env python3
"""
SSA5_2: Marginal Perturbation Sweep
Sweeps perturbations of the lifted stationary distribution and tracks
how the OT solution and its support change.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from shared.markov_utils import MarkovChain, DeterrenceGame, make_strategy_matrix, save_figure

FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)


def solve_ot(mu, phi, cost_matrix):
    """Solve OT LP: max sum gamma*cost s.t. row marginals=mu, col marginals=phi."""
    n, m = cost_matrix.shape
    c = -cost_matrix.flatten()
    n_vars = n * m

    A_eq = np.zeros((n + m, n_vars))
    b_eq = np.zeros(n + m)

    for i in range(n):
        for j in range(m):
            A_eq[i, i * m + j] = 1.0
        b_eq[i] = mu[i]

    for j in range(m):
        for i in range(n):
            A_eq[n + j, i * m + j] = 1.0
        b_eq[n + j] = phi[j]

    bounds = [(0, None)] * n_vars
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if not result.success:
        return None, None
    gamma = result.x.reshape(n, m)
    obj_val = -result.fun
    return gamma, obj_val


def get_support(gamma, threshold=1e-8):
    """Return set of (i, j) where gamma[i,j] > threshold."""
    support = set()
    for i in range(gamma.shape[0]):
        for j in range(gamma.shape[1]):
            if gamma[i, j] > threshold:
                support.add((i, j))
    return frozenset(support)


def build_payoff_matrix(mc, game):
    """Build U[lifted_state, action]."""
    U = np.zeros((mc.n_lifted, game.n_actions))
    for idx, (theta_t, _) in enumerate(mc.lifted_states):
        for a in range(game.n_actions):
            U[idx, a] = game.u1[theta_t, a]
    return U


def compute_action_marginal_from_mu(mu, mc, game):
    """
    Compute action marginal under Stackelberg strategy for a given state dist mu.
    phi[a] = sum_i mu[i] * sigma[theta_t(i), a]
    """
    strat = make_strategy_matrix(game.stackelberg_strategy)
    phi = np.zeros(game.n_actions)
    for idx, (theta_t, _) in enumerate(mc.lifted_states):
        for a in range(game.n_actions):
            phi[a] += mu[idx] * strat[theta_t, a]
    return phi


def build_perturbation_directions(mc):
    """
    Build 4 perturbation directions on the lifted state space.

    Returns dict name -> direction vector (sums to 0 to stay a valid perturbation).
    """
    rho = mc.rho_tilde
    directions = {}

    # Direction 1: more persistent good — increase (G,G), decrease (B,B)
    d1 = np.array([1.0, 0.0, 0.0, -1.0])
    d1 = d1 / np.abs(d1).sum()  # normalise so max perturbation is bounded
    directions["More persistent good"] = d1

    # Direction 2: more transitions — increase (G,B)+(B,G), decrease (G,G)+(B,B)
    d2 = np.array([-1.0, 1.0, 1.0, -1.0])
    d2 = d2 / np.abs(d2).sum()
    directions["More transitions"] = d2

    # Direction 3: toward F(·|G) — conditional on theta_t=G
    # F(lifted | theta_t = G) is proportional to rho restricted to theta_t=G states
    # After observing theta_t=G, the lifted states are (G,G) and (G,B)
    # Their conditional distribution under T: given theta_t=G,
    # P(theta_{t-1}=G | theta_t=G) = pi(G)*P(G|G) / P(theta_t=G)
    # = pi(G)*(1-alpha) / pi(G) = 1-alpha
    target_g = np.zeros(4)
    target_g[0] = 1.0 - mc.alpha  # (G,G)
    target_g[1] = mc.alpha         # (G,B) — wait, P(prev=B|cur=G) = pi(B)*beta/pi(G)
    # Actually: rho_tilde[0]/sum(rho_tilde with theta_t=G) and rho_tilde[1]/sum(...)
    g_states_mask = np.array([1, 1, 0, 0], dtype=float)
    pi_g = rho[0] + rho[1]  # probability of theta_t = G
    target_g = np.zeros(4)
    target_g[0] = rho[0] / pi_g
    target_g[1] = rho[1] / pi_g
    # Normalise as full distribution (conditional of just G-states spread over all 4)
    # Direction: from rho toward this conditional
    d3 = target_g - rho
    if np.abs(d3).sum() > 1e-12:
        d3 = d3 / np.abs(d3).sum()
    directions["Toward F(·|G)"] = d3

    # Direction 4: toward F(·|B) — conditional on theta_t=B
    pi_b = rho[2] + rho[3]
    target_b = np.zeros(4)
    target_b[2] = rho[2] / pi_b
    target_b[3] = rho[3] / pi_b
    d4 = target_b - rho
    if np.abs(d4).sum() > 1e-12:
        d4 = d4 / np.abs(d4).sum()
    directions["Toward F(·|B)"] = d4

    return directions


def main():
    print("=" * 60)
    print("SSA5_2: Marginal Perturbation Sweep")
    print("=" * 60)

    mc = MarkovChain(alpha=0.3, beta=0.5)
    game = DeterrenceGame(x=0.3, y=0.4)
    rho = mc.rho_tilde.copy()
    U = build_payoff_matrix(mc, game)

    print(f"Markov chain: α={mc.alpha}, β={mc.beta}")
    print(f"Lifted stationary ρ̃: {rho}")
    print(f"Game supermodular: {game.is_supermodular}")

    directions = build_perturbation_directions(mc)
    epsilons = np.arange(0, 0.301, 0.01)

    # Get baseline support
    phi_base = compute_action_marginal_from_mu(rho, mc, game)
    gamma_base, obj_base = solve_ot(rho, phi_base, U)
    support_base = get_support(gamma_base)

    lifted_labels = [f"({mc.states[t]},{mc.states[p]})" for t, p in mc.lifted_states]

    print(f"\nBaseline support: {[(lifted_labels[i], game.actions[j]) for i,j in sorted(support_base)]}")
    print(f"Baseline objective: {obj_base:.6f}")

    # Storage for results
    results = {}

    for dir_name, direction in directions.items():
        print(f"\n--- Direction: {dir_name} ---")
        print(f"  Direction vector: {direction}")

        objs = []
        supports = []
        gammas = []
        valid_eps = []
        support_changed_at = None

        for eps in epsilons:
            mu_pert = rho + eps * direction

            # Check validity (non-negative, sums to ~1)
            if np.any(mu_pert < -1e-10):
                break
            mu_pert = np.clip(mu_pert, 0, None)
            mu_pert = mu_pert / mu_pert.sum()

            phi_pert = compute_action_marginal_from_mu(mu_pert, mc, game)

            gamma, obj = solve_ot(mu_pert, phi_pert, U)
            if gamma is None:
                break

            supp = get_support(gamma)
            objs.append(obj)
            supports.append(supp)
            gammas.append(gamma.copy())
            valid_eps.append(eps)

            if supp != support_base and support_changed_at is None:
                support_changed_at = eps

        results[dir_name] = {
            'epsilons': np.array(valid_eps),
            'objectives': np.array(objs),
            'supports': supports,
            'gammas': gammas,
            'critical_eps': support_changed_at
        }

        if support_changed_at is not None:
            print(f"  Support CHANGED at ε* = {support_changed_at:.3f}")
        else:
            print(f"  Support STABLE across all ε ∈ [0, {valid_eps[-1]:.2f}]")
        print(f"  Objective range: [{min(objs):.6f}, {max(objs):.6f}]")

    # Plot 1: OT objective vs epsilon for each direction
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    for ax, (dir_name, res) in zip(axes.flatten(), results.items()):
        ax.plot(res['epsilons'], res['objectives'], 'b-', linewidth=2)
        if res['critical_eps'] is not None:
            ax.axvline(res['critical_eps'], color='red', linestyle='--', linewidth=1.5,
                       label=f"ε*={res['critical_eps']:.3f}")
            ax.legend(fontsize=10)
        ax.set_xlabel('ε', fontsize=12)
        ax.set_ylabel('OT Objective', fontsize=12)
        ax.set_title(dir_name, fontsize=13)
        ax.grid(True, alpha=0.3)
    fig.suptitle("OT Objective Value vs Perturbation Strength", fontsize=15, y=1.02)
    fig.tight_layout()
    save_figure(fig, os.path.join(FIGURES_DIR, 'ot_objective_vs_epsilon.png'))
    print(f"\nSaved: figures/ot_objective_vs_epsilon.png")

    # Plot 2: Support change thresholds
    fig, ax = plt.subplots(figsize=(8, 5))
    dir_names = list(results.keys())
    critical_eps_vals = []
    colors = []
    for dn in dir_names:
        ce = results[dn]['critical_eps']
        if ce is not None:
            critical_eps_vals.append(ce)
            colors.append('red')
        else:
            critical_eps_vals.append(results[dn]['epsilons'][-1])
            colors.append('green')

    bars = ax.barh(range(len(dir_names)), critical_eps_vals, color=colors, alpha=0.7)
    ax.set_yticks(range(len(dir_names)))
    ax.set_yticklabels(dir_names, fontsize=11)
    ax.set_xlabel('ε* (support change threshold)', fontsize=12)
    ax.set_title("Critical Perturbation Threshold by Direction\n(green = stable, red = changed)", fontsize=13)
    ax.grid(True, axis='x', alpha=0.3)

    for i, (val, col) in enumerate(zip(critical_eps_vals, colors)):
        label = f"{val:.3f}" if col == 'red' else "stable"
        ax.text(val + 0.005, i, label, va='center', fontsize=10, fontweight='bold')

    fig.tight_layout()
    save_figure(fig, os.path.join(FIGURES_DIR, 'support_change_threshold.png'))
    print(f"Saved: figures/support_change_threshold.png")

    # Generate report
    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write("# SSA5_2: Marginal Perturbation Sweep — Report\n\n")
        f.write("## Parameters\n")
        f.write(f"- Markov chain: α={mc.alpha}, β={mc.beta}\n")
        f.write(f"- Game: x={game.x}, y={game.y}, supermodular={game.is_supermodular}\n")
        f.write(f"- Perturbation range: ε ∈ [0, 0.30], step=0.01\n\n")

        f.write("## Perturbation Directions\n")
        for dn, d in directions.items():
            f.write(f"- **{dn}**: {d}\n")
        f.write("\n")

        f.write("## Results Summary\n\n")
        f.write("| Direction | Critical ε* | Objective Range | Status |\n")
        f.write("|-----------|------------|-----------------|--------|\n")
        for dn, res in results.items():
            ce = res['critical_eps']
            omin, omax = res['objectives'].min(), res['objectives'].max()
            status = f"Changed at {ce:.3f}" if ce is not None else "Stable"
            ce_str = f"{ce:.3f}" if ce is not None else "N/A"
            f.write(f"| {dn} | {ce_str} | [{omin:.4f}, {omax:.4f}] | {status} |\n")

        f.write("\n## Key Findings\n\n")

        # Analyse game-relevant directions
        game_relevant = ["Toward F(·|G)", "Toward F(·|B)"]
        for dn in game_relevant:
            res = results[dn]
            if res['critical_eps'] is not None:
                f.write(f"- **{dn}**: OT support CHANGES at ε*={res['critical_eps']:.3f}. ")
                f.write("This means the OT solution verified at ρ̃ may NOT be valid at the ")
                f.write("filtering distribution that SR players actually use.\n")
            else:
                f.write(f"- **{dn}**: OT support remains STABLE across all tested ε. ")
                f.write("The OT solution is robust to this perturbation.\n")

        f.write("\n## Interpretation\n\n")
        f.write("The game-relevant perturbation directions (Toward F(·|G) and Toward F(·|B)) ")
        f.write("represent the actual belief distributions that SR players condition on after ")
        f.write("observing specific states. If the OT support changes under these perturbations, ")
        f.write("it validates the critique that checking OT only at ρ̃ is insufficient.\n\n")

        f.write("## Figures\n")
        f.write("![OT Objective vs Epsilon](figures/ot_objective_vs_epsilon.png)\n\n")
        f.write("![Support Change Threshold](figures/support_change_threshold.png)\n")

    print(f"Report saved to: {report_path}")
    print("\nDone.")


if __name__ == '__main__':
    main()
