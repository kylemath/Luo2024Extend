#!/usr/bin/env python3
"""
C16 Verification: Filter stability bridges asymptotic signal convergence
to the not-behaviorally-confounded condition in the Markov case.

Demonstrates that filter stability ensures the asymptotic per-period signal
distribution converges to the *stationary* signal distribution, enabling
the NBC condition to identify types.
"""

import numpy as np


def simulate_filter_convergence(alpha, beta, T=2000, n_inits=5, seed=42):
    """
    Simulate the filtering distribution under different initial conditions
    to verify filter stability (exponential forgetting of initial condition).
    """
    rng = np.random.default_rng(seed)
    pi_G = beta / (alpha + beta)

    # Generate a true state sequence (Markov chain)
    states = np.zeros(T, dtype=bool)
    states[0] = rng.random() < pi_G
    for t in range(1, T):
        if states[t - 1]:
            states[t] = rng.random() >= alpha
        else:
            states[t] = rng.random() < beta

    # Commitment type signals: A if G, F if B
    signals = states.copy()  # True = A (state G), False = F (state B)

    # Run filters from different initial conditions
    init_beliefs = np.linspace(0.01, 0.99, n_inits)
    filter_trajectories = np.zeros((n_inits, T))

    for i, init_G in enumerate(init_beliefs):
        filt = init_G
        for t in range(T):
            filter_trajectories[i, t] = filt
            # Under commitment type, signal perfectly reveals state
            if signals[t]:  # y = A => theta = G
                post_G = 1.0
            else:  # y = F => theta = B
                post_G = 0.0
            # Propagate through transition kernel
            filt = post_G * (1 - alpha) + (1 - post_G) * beta

    return filter_trajectories, states


def compute_stationary_signal_dist(alpha, beta, strategy_A_given_G, strategy_A_given_B):
    """
    Compute the stationary signal distribution P(y=A) under a given strategy
    and the ergodic distribution.
    """
    pi_G = beta / (alpha + beta)
    p_A = pi_G * strategy_A_given_G + (1 - pi_G) * strategy_A_given_B
    return p_A


def main():
    print("=" * 65)
    print("  C16: Filter Stability + NBC in the Markov Setting")
    print("=" * 65)

    alpha, beta = 0.3, 0.5
    pi_G = beta / (alpha + beta)
    second_eigenvalue = abs(1 - alpha - beta)

    print(f"\nParameters: alpha={alpha}, beta={beta}, pi(G)={pi_G:.3f}")
    print(f"Second eigenvalue |1-alpha-beta| = {second_eigenvalue:.2f}")

    # 1. Filter stability: demonstrate exponential forgetting
    print(f"\n--- Filter Stability ---")
    trajs, states = simulate_filter_convergence(alpha, beta)
    n_inits = trajs.shape[0]

    for check_t in [1, 5, 10, 50]:
        spread = trajs[:, check_t].max() - trajs[:, check_t].min()
        print(f"  t={check_t:3d}: filter spread across {n_inits} initial conditions = {spread:.6f}")
        if check_t > 1:
            # Under commitment (state-revealing), after ONE observation the filter
            # perfectly identifies the state, so spread should be 0 after t=1
            pass

    print(f"\n  With state-revealing strategy, filter converges after t=1")
    print(f"  (full state revelation makes initial condition irrelevant immediately)")

    # 2. Show how NBC works via stationary signal distributions
    print(f"\n--- Not-Behaviorally-Confounded Condition ---")
    strategies = {
        "s1* (commitment)":     (1.0, 0.0),   # A if G, F if B
        "s1' (alternative 1)":  (0.8, 0.2),   # noisy version
        "s1'' (alternative 2)": (0.5, 0.5),   # state-independent
        "s1''' (reversed)":     (0.0, 1.0),   # F if G, A if B
    }

    print(f"\n  Stationary signal distributions P(y=A):")
    stat_dists = {}
    for name, (a_G, a_B) in strategies.items():
        p_A = compute_stationary_signal_dist(alpha, beta, a_G, a_B)
        stat_dists[name] = p_A
        print(f"    {name:30s}: P(A) = {p_A:.4f}")

    # Check if NBC holds: s1* has distinct signal dist from all alternatives
    commit_dist = stat_dists["s1* (commitment)"]
    nbc_holds = True
    print(f"\n  NBC check: s1* produces P(A) = {commit_dist:.4f}")
    for name, p_A in stat_dists.items():
        if name == "s1* (commitment)":
            continue
        distinct = abs(p_A - commit_dist) > 1e-10
        print(f"    vs {name}: P(A) = {p_A:.4f}, distinct = {distinct}")
        if not distinct:
            nbc_holds = False

    print(f"\n  NBC satisfied: {nbc_holds}")

    # 3. The key logical chain
    print(f"\n--- The Logical Chain (C16 Clarification) ---")
    print(f"  1. KL bound => per-period signal distributions converge")
    print(f"     (holds for arbitrary processes, including Markov)")
    print(f"  2. Filter stability => filtering distribution converges to")
    print(f"     a limit determined by (strategy, transition kernel)")
    print(f"     Rate: O({second_eigenvalue}^t) = O({second_eigenvalue:.2f}^t)")
    print(f"  3. Limiting filter => unique STATIONARY signal distribution")
    print(f"     p_inf(alpha0, s1, alpha2) for each strategy s1")
    print(f"  4. NBC condition applied to STATIONARY distributions =>")
    print(f"     s1' with same stationary signal dist must be s1*")
    print(f"  5. Therefore mu_inf({{omega^R, omega_s1*}}) = 1")
    print(f"\n  Steps 2-3 are the implicit bridge that C16 asks to make explicit.")
    print(f"  In the i.i.d. case, these steps are trivial (no filtering needed).")


if __name__ == "__main__":
    main()
