"""
C05 Verification: Monotonicity does NOT imply supermodularity.

We demonstrate:
1. A counterexample where monotonicity holds but supermodularity fails
2. That in the paper's model (exogenous transitions), g doesn't depend on a1
3. Adding a function of theta alone preserves supermodularity
"""

import numpy as np


def check_supermodularity(g, states, actions):
    """
    Check if g(theta, a) has increasing differences.
    For all theta_H > theta_L and a_H > a_L:
      g(theta_H, a_H) - g(theta_H, a_L) >= g(theta_L, a_H) - g(theta_L, a_L)
    """
    violations = []
    for i, theta_H in enumerate(states):
        for j, theta_L in enumerate(states):
            if j >= i:
                continue
            for k, a_H in enumerate(actions):
                for l, a_L in enumerate(actions):
                    if l >= k:
                        continue
                    diff_H = g[i][k] - g[i][l]
                    diff_L = g[j][k] - g[j][l]
                    if diff_H < diff_L - 1e-10:
                        violations.append({
                            'theta_H': theta_H, 'theta_L': theta_L,
                            'a_H': a_H, 'a_L': a_L,
                            'diff_H': diff_H, 'diff_L': diff_L
                        })
    return len(violations) == 0, violations


def check_monotonicity(g, states, actions):
    """Check if g is increasing in theta for each a."""
    for k, a in enumerate(actions):
        for i in range(len(states) - 1):
            if g[i+1][k] < g[i][k] - 1e-10:
                return False
    return True


print("=" * 75)
print("C05 VERIFICATION: Monotonicity vs Supermodularity")
print("=" * 75)

# ---- Counterexample: monotone but not supermodular ----
print("\n--- Counterexample: Monotone but NOT Supermodular ---")
states = ["theta_L", "theta_H"]
actions = ["a_L", "a_H"]
g = [[2, 5],   # theta_L: g(L,L)=2, g(L,H)=5, diff=3
     [9, 10]]  # theta_H: g(H,L)=9, g(H,H)=10, diff=1

print("g(theta, a):")
print(f"           a_L    a_H    diff")
for i, s in enumerate(states):
    print(f"  {s:>8}: {g[i][0]:>5}  {g[i][1]:>5}    {g[i][1]-g[i][0]:>3}")

mono = check_monotonicity(g, states, actions)
supermod, violations = check_supermodularity(g, states, actions)

print(f"\nMonotone in theta for each a? {mono}")
print(f"Supermodular (increasing differences)? {supermod}")

if violations:
    for v in violations:
        print(f"  Violation: diff at {v['theta_H']} = {v['diff_H']}, "
              f"diff at {v['theta_L']} = {v['diff_L']}")
        print(f"  {v['diff_H']} < {v['diff_L']} → DECREASING differences")

print("\nThis confirms: MONOTONICITY does NOT imply SUPERMODULARITY.")

# ---- Paper's model: g doesn't depend on a1 ----
print("\n" + "=" * 75)
print("Paper's Model: Exogenous State Transitions")
print("=" * 75)

alpha, beta = 0.3, 0.5
delta = 0.95

F_G_given_G = 1 - alpha
F_B_given_G = alpha
F_G_given_B = beta
F_B_given_B = 1 - beta

# Suppose continuation values V(G) > V(B) (higher state = higher value)
V_G = 1.0
V_B = 0.3

# Continuation value conditional on current state
V_cont_G = F_G_given_G * V_G + F_B_given_G * V_B  # E[V(θ') | θ=G]
V_cont_B = F_G_given_B * V_G + F_B_given_B * V_B  # E[V(θ') | θ=B]

print(f"\nalpha={alpha}, beta={beta}, delta={delta}")
print(f"V(G)={V_G}, V(B)={V_B}")
print(f"V_cont(G) = F(G|G)*V(G) + F(B|G)*V(B) = {F_G_given_G}*{V_G} + {F_B_given_G}*{V_B} = {V_cont_G:.4f}")
print(f"V_cont(B) = F(G|B)*V(G) + F(B|B)*V(B) = {F_G_given_B}*{V_G} + {F_B_given_B}*{V_B} = {V_cont_B:.4f}")
print(f"\nV_cont does NOT depend on a1 (state transitions are exogenous).")
print(f"V_cont(G) = {V_cont_G:.4f} for ALL a1")
print(f"V_cont(B) = {V_cont_B:.4f} for ALL a1")

# g(theta, a1) = delta * V_cont(theta) -- independent of a1!
g_paper = [[delta * V_cont_B, delta * V_cont_B],   # theta=B
           [delta * V_cont_G, delta * V_cont_G]]    # theta=G

print(f"\ng(theta, a1) = delta * V_cont(theta):")
print(f"           a_L       a_H       diff")
for i, s in enumerate(["theta_B", "theta_G"]):
    print(f"  {s:>8}: {g_paper[i][0]:>8.4f}  {g_paper[i][1]:>8.4f}    {g_paper[i][1]-g_paper[i][0]:>8.4f}")

supermod_paper, _ = check_supermodularity(g_paper, ["B", "G"], ["a_L", "a_H"])
print(f"\nSupermodular? {supermod_paper} (trivially, since differences are all 0)")

# ---- Show that u1 + g preserves supermodularity ----
print("\n" + "=" * 75)
print("Adding g(theta) to supermodular u1(theta, a1)")
print("=" * 75)

u1 = [[0.0, 0.3],   # theta=B: u1(B,L)=0.0, u1(B,H)=0.3
      [0.5, 1.0]]    # theta=G: u1(G,L)=0.5, u1(G,H)=1.0

print("\nu1(theta, a1):")
print(f"           a_L      a_H      diff")
for i, s in enumerate(["theta_B", "theta_G"]):
    print(f"  {s:>8}: {u1[i][0]:>7.3f}  {u1[i][1]:>7.3f}    {u1[i][1]-u1[i][0]:>7.3f}")

supermod_u1, _ = check_supermodularity(u1, ["B", "G"], ["a_L", "a_H"])
print(f"  u1 supermodular? {supermod_u1} (diff_G={u1[1][1]-u1[1][0]:.3f} >= diff_B={u1[0][1]-u1[0][0]:.3f})")

w = [[u1[i][j] + g_paper[i][j] for j in range(2)] for i in range(2)]

print(f"\nw = u1 + g(theta):")
print(f"           a_L      a_H      diff")
for i, s in enumerate(["theta_B", "theta_G"]):
    print(f"  {s:>8}: {w[i][0]:>7.4f}  {w[i][1]:>7.4f}    {w[i][1]-w[i][0]:>7.4f}")

supermod_w, _ = check_supermodularity(w, ["B", "G"], ["a_L", "a_H"])
print(f"  w = u1 + g supermodular? {supermod_w}")
print(f"  diff_G = {w[1][1]-w[1][0]:.4f}, diff_B = {w[0][1]-w[0][0]:.4f}")
print(f"  The g terms cancel: diff_G(w) - diff_B(w) = diff_G(u1) - diff_B(u1) = "
      f"{(u1[1][1]-u1[1][0]) - (u1[0][1]-u1[0][0]):.4f}")

print("\n" + "=" * 75)
print("CONCLUSION")
print("=" * 75)
print("""
1. The reviewer is CORRECT: monotonicity does NOT imply supermodularity.
2. However, in the paper's model, g(theta, a1) = delta * V_cont(theta)
   does NOT depend on a1 (state transitions are exogenous).
3. Adding a function of theta alone to a supermodular u1 preserves
   supermodularity trivially (the g terms cancel in the diff comparison).
4. The paper should state this cleaner argument instead of the incorrect
   "monotonicity implies supermodularity" claim.
5. If the model were extended to action-dependent transitions, the correct
   condition would be increasing differences of g in (theta, a1).
""")
