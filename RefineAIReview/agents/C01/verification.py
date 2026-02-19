"""
C01 Verification: Confirm that delta->1 makes continuation MORE important, not less.

Under (1-delta)*u1 + delta*E[V]:
  - Stage-game weight: (1-delta) -> 0 as delta -> 1
  - Continuation weight: delta -> 1 as delta -> 1

The paper incorrectly claims delta->1 makes the continuation value perturbation
small relative to the stage-game payoff. This script verifies the opposite.
"""

import numpy as np

def bellman_weights(delta):
    """Return (stage_game_weight, continuation_weight) for discount factor delta."""
    return (1 - delta, delta)

def continuation_perturbation_ratio(delta, g_variation, u1_variation):
    """
    Ratio of continuation perturbation to stage-game payoff variation.

    Under the Bellman equation V = (1-delta)*u1 + delta*E[V],
    the one-shot deviation gain is:
      (1-delta)*Delta_u1 + delta*Delta_V_cont

    Parameters
    ----------
    delta : float
        Discount factor
    g_variation : float
        Variation of continuation value perturbation g(theta, a1) across states
    u1_variation : float
        Variation of stage-game payoff u1(theta, a1) across states

    Returns
    -------
    ratio : float
        delta * g_variation / ((1-delta) * u1_variation)
    """
    if u1_variation == 0:
        return float('inf')
    return (delta * g_variation) / ((1 - delta) * u1_variation)

print("=" * 70)
print("C01 VERIFICATION: Bellman equation weights as delta -> 1")
print("=" * 70)

deltas = [0.5, 0.7, 0.9, 0.95, 0.99, 0.999, 0.9999]

print(f"\n{'delta':>10} | {'stage (1-delta)':>15} | {'continuation (delta)':>20} | {'ratio cont/stage':>16}")
print("-" * 70)
for d in deltas:
    sw, cw = bellman_weights(d)
    ratio = cw / sw if sw > 0 else float('inf')
    print(f"{d:>10.4f} | {sw:>15.6f} | {cw:>20.6f} | {ratio:>16.2f}")

print("\nAs delta -> 1, the continuation weight goes to 1 and the stage-game")
print("weight goes to 0. The RATIO continuation/stage diverges to infinity.")
print("This confirms the reviewer: delta->1 makes continuation MORE important.\n")

print("=" * 70)
print("Perturbation ratio (continuation perturbation / stage-game variation)")
print("=" * 70)
g_var = 0.1  # typical continuation value variation across states
u1_var = 1.0  # typical stage-game payoff variation

print(f"\ng_variation = {g_var}, u1_variation = {u1_var}")
print(f"\n{'delta':>10} | {'perturbation ratio':>20}")
print("-" * 40)
for d in deltas:
    r = continuation_perturbation_ratio(d, g_var, u1_var)
    print(f"{d:>10.4f} | {r:>20.4f}")

print("\nThe perturbation ratio INCREASES with delta, confirming the reviewer's point.")
print("The paper's claim that delta->1 makes the perturbation small is incorrect.\n")

print("=" * 70)
print("What DOES make the perturbation small: FILTER STABILITY")
print("=" * 70)

alpha, beta = 0.3, 0.5
persistence = abs(1 - alpha - beta)

print(f"\nBaseline parameters: alpha={alpha}, beta={beta}")
print(f"Persistence |1-alpha-beta| = {persistence}")
print(f"Filter forgetting rate ~ {persistence}")

periods = np.arange(1, 51)
g_variation_over_time = persistence ** periods

print(f"\n{'period t':>10} | {'g variation ~ |1-a-b|^t':>25} | {'filter converged?':>17}")
print("-" * 60)
for t in [1, 2, 5, 10, 20, 50]:
    gv = persistence ** t
    converged = "YES" if gv < 0.01 else "no"
    print(f"{t:>10d} | {gv:>25.6f} | {converged:>17}")

print("\nFilter stability drives the theta-dependent perturbation to zero")
print("over time, regardless of delta. This is the correct mechanism.\n")

print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print("""
1. The reviewer is CORRECT: delta->1 makes continuation MORE important.
2. Filter stability (not delta->1) makes the theta-dependent perturbation small.
3. delta->1 makes the TRANSIENT period (before filter stability kicks in) negligible.
4. These are two distinct mechanisms; the paper conflated them.
5. The formal proof (Step 5, front-loading argument) is unaffected.
""")
