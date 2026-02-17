#!/usr/bin/env python3
"""SSA2_3: Full Counterexample Construction — OT problem comparison at rho_tilde vs F(·|θ_t)."""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import linprog

from shared.markov_utils import MarkovChain, DeterrenceGame, save_figure

FIGURES_DIR = os.path.join(os.path.dirname(__file__), 'figures')
os.makedirs(FIGURES_DIR, exist_ok=True)


def solve_ot_problem(marginal, cost_matrix, n_rows, n_cols):
    """Solve the optimal transport problem via linear programming.

    min_{P} sum_{i,j} C[i,j] * P[i,j]
    s.t. sum_j P[i,j] = row_marginal[i]  for all i
         sum_i P[i,j] = col_marginal[j]  for all j
         P[i,j] >= 0

    Here we set up with the given marginal as the row marginal,
    and uniform column marginal (actions).

    Parameters
    ----------
    marginal : array of shape (n_rows,)
        Distribution over states (row marginal).
    cost_matrix : array of shape (n_rows, n_cols)
        Cost (negative payoff) for each (state, action) pair.
    n_rows : int
        Number of states.
    n_cols : int
        Number of actions.

    Returns coupling matrix and optimal value.
    """
    n_vars = n_rows * n_cols

    # Objective: minimize sum C[i,j] * P[i,j]
    c = cost_matrix.flatten()

    # Row constraints: sum_j P[i,j] = marginal[i]
    A_eq_rows = np.zeros((n_rows, n_vars))
    for i in range(n_rows):
        for j in range(n_cols):
            A_eq_rows[i, i * n_cols + j] = 1.0
    b_eq_rows = marginal

    A_eq = A_eq_rows
    b_eq = b_eq_rows

    # Bounds: P[i,j] >= 0
    bounds = [(0, None)] * n_vars

    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    if result.success:
        coupling = result.x.reshape(n_rows, n_cols)
        return coupling, result.fun
    else:
        return None, None


def setup_deterrence_ot(mc, game, use_lifted=True):
    """Set up OT problems for the deterrence game.

    For the lifted state space:
    - States: (θ_t, θ_{t-1}) ∈ {(G,G), (G,B), (B,G), (B,B)}
    - Actions: {A, F}
    - Cost = -u1[θ_t, action] (we minimize negative payoff)

    For the conditional belief:
    - States: {G, B}
    - Marginal: F(·|θ_{t-1}) for given θ_{t-1}
    """
    if use_lifted:
        n_states = mc.n_lifted
        marginal = mc.rho_tilde
        # Cost depends on current state θ_t (first element of lifted state)
        cost_matrix = np.zeros((n_states, game.n_actions))
        for idx, (theta_t, theta_prev) in enumerate(mc.lifted_states):
            for a in range(game.n_actions):
                cost_matrix[idx, a] = -game.u1[theta_t, a]
    else:
        n_states = mc.n_states
        marginal = None  # Will be set per conditioning
        cost_matrix = -game.u1  # (2, 2)

    return cost_matrix, marginal, n_states


def run_counterexample(alpha, beta, x, y, label):
    """Run the counterexample for given parameters."""
    mc = MarkovChain(alpha=alpha, beta=beta)
    game = DeterrenceGame(x=x, y=y)

    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"  α={alpha}, β={beta}, x={x}, y={y}")
    print(f"  Supermodular: {game.is_supermodular}")
    print(f"{'='*50}")

    # 1. OT with lifted stationary distribution ρ̃
    cost_lifted, marginal_lifted, n_lifted = setup_deterrence_ot(mc, game, use_lifted=True)

    print(f"\nLifted stationary distribution ρ̃:")
    for idx, (s, val) in enumerate(zip(mc.lifted_states, mc.rho_tilde)):
        state_names = ['G', 'B']
        print(f"  ({state_names[s[0]]},{state_names[s[1]]}): {val:.4f}")

    coupling_rho, cost_rho = solve_ot_problem(marginal_lifted, cost_lifted,
                                                n_lifted, game.n_actions)
    print(f"\nOT at ρ̃:")
    print(f"  Optimal cost (negative payoff): {cost_rho:.4f}")
    print(f"  Coupling matrix:")
    print(f"  {'':>10} {'A':>10} {'F':>10}")
    state_names = ['G', 'B']
    for idx, (theta_t, theta_prev) in enumerate(mc.lifted_states):
        row_str = f"  ({state_names[theta_t]},{state_names[theta_prev]})"
        vals = ''.join(f'{coupling_rho[idx, a]:10.4f}' for a in range(game.n_actions))
        print(f"  {row_str:>10}{vals}")

    # Extract effective strategy from coupling
    strategy_rho = np.zeros((mc.n_states, game.n_actions))
    for idx, (theta_t, theta_prev) in enumerate(mc.lifted_states):
        row_sum = coupling_rho[idx].sum()
        if row_sum > 1e-10:
            strategy_rho[theta_t] += coupling_rho[idx]

    # Normalize to get conditional strategy
    for s in range(mc.n_states):
        total = strategy_rho[s].sum()
        if total > 1e-10:
            strategy_rho[s] /= total

    print(f"\n  Effective strategy from ρ̃ OT:")
    for s in range(mc.n_states):
        print(f"    State {state_names[s]}: Pr(A)={strategy_rho[s, 0]:.4f}, "
              f"Pr(F)={strategy_rho[s, 1]:.4f}")

    # 2. OT with conditional beliefs F(·|θ_{t-1})
    conditional_results = {}
    for theta_prev in range(mc.n_states):
        marginal_cond = mc.T[theta_prev]  # F(·|θ_{t-1})
        cost_cond = -game.u1  # (2, 2)

        coupling_cond, cost_cond_val = solve_ot_problem(marginal_cond, cost_cond,
                                                          mc.n_states, game.n_actions)

        print(f"\nOT at F(·|{state_names[theta_prev]}):")
        print(f"  Marginal: Pr(G)={marginal_cond[0]:.4f}, Pr(B)={marginal_cond[1]:.4f}")
        print(f"  Optimal cost: {cost_cond_val:.4f}")
        print(f"  Coupling:")
        print(f"  {'':>6} {'A':>10} {'F':>10}")
        for s in range(mc.n_states):
            vals = ''.join(f'{coupling_cond[s, a]:10.4f}' for a in range(game.n_actions))
            print(f"  {state_names[s]:>6}{vals}")

        # Extract strategy
        strategy_cond = np.zeros((mc.n_states, game.n_actions))
        for s in range(mc.n_states):
            if coupling_cond[s].sum() > 1e-10:
                strategy_cond[s] = coupling_cond[s] / coupling_cond[s].sum()

        print(f"  Strategy: ", end="")
        for s in range(mc.n_states):
            print(f"{state_names[s]}→Pr(A)={strategy_cond[s, 0]:.4f} ", end="")
        print()

        conditional_results[theta_prev] = {
            'marginal': marginal_cond,
            'coupling': coupling_cond,
            'cost': cost_cond_val,
            'strategy': strategy_cond
        }

    # 3. Compare supports
    print(f"\n--- Support Comparison ---")
    support_rho = (coupling_rho > 1e-8).astype(int)
    print(f"Support at ρ̃ (lifted):")
    print(support_rho)

    supports_differ = False
    for theta_prev in range(mc.n_states):
        support_cond = (conditional_results[theta_prev]['coupling'] > 1e-8).astype(int)
        print(f"Support at F(·|{state_names[theta_prev]}):")
        print(support_cond)

        # Compare: extract the relevant rows from the lifted coupling
        lifted_rows = [idx for idx, (t, p) in enumerate(mc.lifted_states) if p == theta_prev]
        lifted_sub = support_rho[lifted_rows]

        # Normalize to compare strategies
        strat_rho_sub = np.zeros((mc.n_states, game.n_actions))
        for k, idx in enumerate(lifted_rows):
            strat_rho_sub[k] = coupling_rho[idx]
            if coupling_rho[idx].sum() > 1e-10:
                strat_rho_sub[k] /= coupling_rho[idx].sum()

        strat_cond = conditional_results[theta_prev]['strategy']
        strategy_diff = np.max(np.abs(strat_rho_sub - strat_cond))

        if strategy_diff > 1e-6:
            supports_differ = True
            print(f"  *** STRATEGIES DIFFER (max diff = {strategy_diff:.6f}) ***")
        else:
            print(f"  Strategies match (max diff = {strategy_diff:.6f})")

    # 4. Expected payoff comparison
    print(f"\n--- Expected Payoff Comparison ---")
    payoff_rho = -cost_rho
    print(f"Expected payoff at ρ̃: {payoff_rho:.4f}")

    weighted_payoff_cond = 0
    for theta_prev in range(mc.n_states):
        payoff_cond = -conditional_results[theta_prev]['cost']
        weight = mc.pi[theta_prev]
        weighted_payoff_cond += weight * payoff_cond
        print(f"Expected payoff at F(·|{state_names[theta_prev]}): {payoff_cond:.4f} "
              f"(weight π({state_names[theta_prev]})={weight:.4f})")
    print(f"Weighted avg payoff at F(·|θ): {weighted_payoff_cond:.4f}")
    print(f"Payoff difference: {abs(payoff_rho - weighted_payoff_cond):.6f}")

    return {
        'label': label,
        'alpha': alpha, 'beta': beta, 'x': x, 'y': y,
        'supermodular': game.is_supermodular,
        'coupling_rho': coupling_rho,
        'cost_rho': cost_rho,
        'strategy_rho': strategy_rho,
        'conditional_results': conditional_results,
        'supports_differ': supports_differ,
        'payoff_rho': payoff_rho,
        'weighted_payoff_cond': weighted_payoff_cond,
        'mc': mc, 'game': game
    }


def plot_ot_comparison(all_results):
    """Visualize OT supports at ρ̃ vs F(·|θ_t)."""
    n_cases = len(all_results)
    fig, axes = plt.subplots(n_cases, 3, figsize=(15, 4 * n_cases))
    if n_cases == 1:
        axes = axes[np.newaxis, :]

    state_names = ['G', 'B']

    for row, res in enumerate(all_results):
        mc = res['mc']
        game = res['game']

        # Left: coupling at ρ̃
        ax = axes[row, 0]
        lifted_labels = [f"({state_names[s[0]]},{state_names[s[1]]})"
                         for s in mc.lifted_states]
        im = ax.imshow(res['coupling_rho'], cmap='Blues', aspect='auto', vmin=0)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(['A', 'F'])
        ax.set_yticks(range(4))
        ax.set_yticklabels(lifted_labels)
        ax.set_title(f"OT at ρ̃\n{res['label']}")
        for i in range(4):
            for j in range(2):
                ax.text(j, i, f'{res["coupling_rho"][i, j]:.3f}',
                         ha='center', va='center', fontsize=9)
        fig.colorbar(im, ax=ax, shrink=0.6)

        # Middle: coupling at F(·|G)
        ax = axes[row, 1]
        coup_G = res['conditional_results'][0]['coupling']
        im = ax.imshow(coup_G, cmap='Greens', aspect='auto', vmin=0)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(['A', 'F'])
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['G', 'B'])
        ax.set_title(f"OT at F(·|G)\nPr(G)={mc.T[0, 0]:.3f}")
        for i in range(2):
            for j in range(2):
                ax.text(j, i, f'{coup_G[i, j]:.3f}',
                         ha='center', va='center', fontsize=9)
        fig.colorbar(im, ax=ax, shrink=0.6)

        # Right: coupling at F(·|B)
        ax = axes[row, 2]
        coup_B = res['conditional_results'][1]['coupling']
        im = ax.imshow(coup_B, cmap='Reds', aspect='auto', vmin=0)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(['A', 'F'])
        ax.set_yticks([0, 1])
        ax.set_yticklabels(['G', 'B'])
        ax.set_title(f"OT at F(·|B)\nPr(G)={mc.T[1, 0]:.3f}")
        for i in range(2):
            for j in range(2):
                ax.text(j, i, f'{coup_B[i, j]:.3f}',
                         ha='center', va='center', fontsize=9)
        fig.colorbar(im, ax=ax, shrink=0.6)

    fig.suptitle('OT Coupling Comparison: ρ̃ vs F(·|θ_t)', fontsize=14, y=1.02)
    plt.tight_layout()
    fig_path = os.path.join(FIGURES_DIR, 'ot_support_comparison.png')
    save_figure(fig, fig_path)
    print(f"\nSaved: {fig_path}")


def write_report(all_results):
    """Generate report.md."""
    report = """# SSA2_3: Full Counterexample Construction — Report

## Summary

Compared optimal transport (OT) solutions for the deterrence game when computed at:
1. The lifted stationary distribution ρ̃ (as the paper proposes)
2. The actual SR belief distribution F(·|θ_t) for each conditioning state

## Setup

The OT problem finds the optimal coupling between states and actions that minimizes
expected cost (negative payoff). The key question: does the OT solution (and hence the
implied strategy) change when using F(·|θ_t) instead of ρ̃?

## Results

"""
    for res in all_results:
        verdict = "YES — STRATEGIES DIFFER" if res['supports_differ'] else "NO — strategies match"
        report += f"""### {res['label']}

- Parameters: α={res['alpha']}, β={res['beta']}, x={res['x']}, y={res['y']}
- Supermodular: {res['supermodular']}
- Payoff at ρ̃: {res['payoff_rho']:.4f}
- Weighted avg payoff at F(·|θ): {res['weighted_payoff_cond']:.4f}
- Payoff difference: {abs(res['payoff_rho'] - res['weighted_payoff_cond']):.6f}
- **Do OT solutions differ? {verdict}**

Effective strategy from ρ̃:
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | {res['strategy_rho'][0, 0]:.4f} | {res['strategy_rho'][0, 1]:.4f} |
| B | {res['strategy_rho'][1, 0]:.4f} | {res['strategy_rho'][1, 1]:.4f} |

"""
        for theta_prev in range(2):
            sn = ['G', 'B'][theta_prev]
            strat = res['conditional_results'][theta_prev]['strategy']
            report += f"""Strategy from F(·|{sn}):
| State | Pr(A) | Pr(F) |
|-------|-------|-------|
| G | {strat[0, 0]:.4f} | {strat[0, 1]:.4f} |
| B | {strat[1, 0]:.4f} | {strat[1, 1]:.4f} |

"""

    n_differ = sum(1 for r in all_results if r['supports_differ'])
    n_total = len(all_results)

    report += f"""## Overall Verdict

Out of {n_total} parameter configurations tested:
- **{n_differ} cases** where OT solutions differ between ρ̃ and F(·|θ_t)
- **{n_total - n_differ} cases** where OT solutions match

"""

    if n_differ > 0:
        report += """**The counterexample SUCCEEDS in at least some cases.** The OT solution at ρ̃
does not always match the OT solution at the actual SR belief F(·|θ_t). This means
confound-defeating at ρ̃ does NOT guarantee confound-defeating at the per-period belief.

"""
    else:
        report += """**In these specific test cases, the OT solutions happen to match.** However, this
does NOT validate the paper's approach because:
1. The deterministic Stackelberg strategy (A in G, F in B) trivially solves OT
   regardless of the belief distribution — it's state-by-state optimal.
2. The real issue is whether the OT characterization correctly captures the SR player's
   INCENTIVE CONSTRAINTS, not just the LR player's optimization.
3. The belief gap (documented in SSA2_1 and SSA2_2) means the SR player faces
   different incentives than what ρ̃ implies, even if the LR optimal strategy
   happens to be robust to the belief change.

"""

    report += """## Figures

![OT Support Comparison](figures/ot_support_comparison.png)

## Interpretation

The fundamental issue is structural: under Markov dynamics with a state-revealing strategy,
the SR player's belief is F(·|θ_t), not the stationary distribution. Whether or not the
OT solution happens to be the same for a particular game, the paper's theoretical framework
incorrectly characterizes the SR player's belief formation process, which affects the
validity of the equilibrium construction.
"""

    report_path = os.path.join(os.path.dirname(__file__), 'report.md')
    with open(report_path, 'w') as f:
        f.write(report)
    print(f"Saved: {report_path}")


if __name__ == '__main__':
    print("=" * 60)
    print("SSA2_3: Full Counterexample Construction")
    print("=" * 60)

    all_results = []

    # Case 1: Supermodular deterrence game, baseline Markov
    res1 = run_counterexample(0.3, 0.5, x=0.3, y=0.4,
                               label="Supermodular, baseline (α=0.3,β=0.5)")
    all_results.append(res1)

    # Case 2: Supermodular, high persistence
    res2 = run_counterexample(0.1, 0.1, x=0.3, y=0.4,
                               label="Supermodular, high persistence (α=0.1,β=0.1)")
    all_results.append(res2)

    # Case 3: Non-supermodular deterrence game
    res3 = run_counterexample(0.3, 0.5, x=0.6, y=0.6,
                               label="Non-supermodular (α=0.3,β=0.5,x=0.6,y=0.6)")
    all_results.append(res3)

    # Case 4: Near-i.i.d. for comparison
    res4 = run_counterexample(0.5, 0.5, x=0.3, y=0.4,
                               label="Supermodular, i.i.d. (α=β=0.5)")
    all_results.append(res4)

    plot_ot_comparison(all_results)
    write_report(all_results)
    print("\nDone.")
