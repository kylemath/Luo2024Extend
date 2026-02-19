"""
C06 Verification: Illustrate how adding a theta-dependent g can change the OT solution.

This shows that even when u1 has a unique OT solution (co-monotone coupling
under supermodularity), adding g(theta, a1) with a1-dependence can change it.
But adding g(theta) without a1-dependence preserves the OT solution.
"""

import numpy as np
from itertools import product


def compute_ot_solution(payoff_matrix, marginals_theta, marginals_a):
    """
    Solve the discrete OT problem by brute force enumeration.
    Returns the coupling gamma that maximizes sum payoff(theta, a) * gamma(theta, a)
    subject to marginal constraints.

    payoff_matrix: dict (theta, a) -> payoff
    marginals_theta: dict theta -> probability
    marginals_a: dict a -> probability

    Returns best coupling as dict (theta, a) -> probability
    """
    thetas = sorted(marginals_theta.keys())
    actions = sorted(marginals_a.keys())
    n_theta = len(thetas)
    n_a = len(actions)

    best_obj = -np.inf
    best_gamma = None

    # For small problems, enumerate vertices of the transportation polytope
    # Simple 2x2 case: parameterize by one variable
    if n_theta == 2 and n_a == 2:
        t0, t1 = thetas
        a0, a1 = actions
        # gamma(t0, a0) = x, gamma(t0, a1) = marginals_theta[t0] - x
        # gamma(t1, a0) = marginals_a[a0] - x, gamma(t1, a1) = x - marginals_theta[t0] - marginals_a[a0] + 1
        lo = max(0, marginals_theta[t0] + marginals_a[a0] - 1)
        hi = min(marginals_theta[t0], marginals_a[a0])

        for x_100 in range(int(lo * 1000), int(hi * 1000) + 1):
            x = x_100 / 1000
            gamma = {
                (t0, a0): x,
                (t0, a1): marginals_theta[t0] - x,
                (t1, a0): marginals_a[a0] - x,
                (t1, a1): 1 - marginals_theta[t0] - marginals_a[a0] + x
            }

            if any(v < -1e-10 for v in gamma.values()):
                continue

            obj = sum(payoff_matrix.get((t, a), 0) * gamma[(t, a)]
                      for t in thetas for a in actions)

            if obj > best_obj:
                best_obj = obj
                best_gamma = gamma

    return best_gamma, best_obj


print("=" * 75)
print("C06 VERIFICATION: How g(theta) vs g(theta,a1) affects OT solution")
print("=" * 75)

# Setup: 2 states, 2 actions, supermodular u1
thetas = ["B", "G"]
actions = ["L", "H"]

u1 = {
    ("B", "L"): 0.0,
    ("B", "H"): 0.3,
    ("G", "L"): 0.5,
    ("G", "H"): 1.0
}

marginals_theta = {"B": 0.375, "G": 0.625}
marginals_a = {"L": 0.4, "H": 0.6}

print("\nu1(theta, a):")
print(f"       a_L    a_H")
for t in thetas:
    print(f"  {t}: {u1[(t,'L')]:>5.2f}  {u1[(t,'H')]:>5.2f}")

print(f"\nMarginals: theta={dict(marginals_theta)}, a={dict(marginals_a)}")

# Case 1: OT with u1 alone
gamma1, obj1 = compute_ot_solution(u1, marginals_theta, marginals_a)
print(f"\n--- Case 1: OT with u1 alone ---")
print(f"Optimal coupling:")
for t in thetas:
    for a in actions:
        print(f"  gamma({t},{a}) = {gamma1[(t,a)]:.4f}")
print(f"Objective = {obj1:.4f}")

# Case 2: OT with u1 + g(theta) (action-independent perturbation)
g_theta = {"B": 0.2, "G": 0.8}
w2 = {(t, a): u1[(t, a)] + g_theta[t] for t in thetas for a in actions}

gamma2, obj2 = compute_ot_solution(w2, marginals_theta, marginals_a)
print(f"\n--- Case 2: OT with u1 + g(theta) [action-INDEPENDENT] ---")
print(f"g(B)={g_theta['B']}, g(G)={g_theta['G']}")
print(f"Optimal coupling:")
for t in thetas:
    for a in actions:
        print(f"  gamma({t},{a}) = {gamma2[(t,a)]:.4f}")

coupling_match = all(abs(gamma1[(t, a)] - gamma2[(t, a)]) < 0.01
                     for t in thetas for a in actions)
print(f"Coupling matches Case 1? {coupling_match}")
print("(Adding g(theta) alone does NOT change the OT solution)")

# Case 3: OT with u1 + g(theta, a) that has DECREASING differences
g_theta_a = {
    ("B", "L"): 0.1,
    ("B", "H"): 0.5,   # diff at B = 0.4
    ("G", "L"): 0.7,
    ("G", "H"): 0.8    # diff at G = 0.1
}

w3 = {(t, a): u1[(t, a)] + g_theta_a[(t, a)] for t in thetas for a in actions}
gamma3, obj3 = compute_ot_solution(w3, marginals_theta, marginals_a)
print(f"\n--- Case 3: OT with u1 + g(theta,a) [action-DEPENDENT, decreasing diff] ---")
print(f"g(theta,a):")
for t in thetas:
    print(f"  {t}: g({t},L)={g_theta_a[(t,'L')]:.1f}, g({t},H)={g_theta_a[(t,'H')]:.1f}, "
          f"diff={g_theta_a[(t,'H')]-g_theta_a[(t,'L')]:.1f}")
print(f"Optimal coupling:")
for t in thetas:
    for a in actions:
        print(f"  gamma({t},{a}) = {gamma3[(t,a)]:.4f}")

coupling_match3 = all(abs(gamma1[(t, a)] - gamma3[(t, a)]) < 0.01
                      for t in thetas for a in actions)
print(f"Coupling matches Case 1? {coupling_match3}")
if not coupling_match3:
    print("(Adding g(theta,a) with decreasing differences CAN change the OT solution)")

print("\n" + "=" * 75)
print("Summary")
print("=" * 75)
print("""
Statement 1 ("argument is identical"):
  The STRUCTURE of the OT argument carries over for any objective w.
  Given w, the proof logic is identical. ✓

Statement 2 ("can change the OT solution"):
  The OBJECTIVE w = u1 + g differs from u1 when g depends on theta.
  Different w can yield different OT solutions. ✓

These are about different aspects:
  - Structure of proof (same) vs. Content of objective (different)
  - Not contradictory, but misleadingly juxtaposed.

Key resolution: In the paper's model (exogenous transitions), g depends
on theta alone (not a1), so the OT solution IS preserved.
""")
