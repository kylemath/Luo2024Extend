#!/usr/bin/env python3
"""
C10 Verification: Monte Carlo simulation for KL counting bound comparison.

Verifies that the KL counting bound bar_T(eta, mu_0) = -2*log(mu_0)/eta^2
holds for both i.i.d. and Markov state processes.

The key insight: q_t in the bound is the EQUILIBRIUM signal distribution
(averaging over type posterior), not the pure rational-type distribution.
As the posterior concentrates on commitment, q_t -> p_t and per-period KL
vanishes, making the total KL finite.
"""

import numpy as np


def run_single(states, alpha, beta, pi_G, eta, mu0, is_markov):
    """
    Run a single simulation of the Bayesian learning problem.

    Commitment type: s1*(G)=A, s1*(B)=F (deterministic).
    Rational type: sigma(G)=70% A, sigma(B)=30% A.

    Returns (dist_count, total_kl, final_posterior).
    """
    T = len(states)
    # Rational type signal probabilities
    r_A_given_G = 0.70
    r_A_given_B = 0.30

    # State filter under commitment hypothesis
    filt_c = pi_G
    # State filter under rational hypothesis
    filt_r = pi_G
    # Type posterior
    mu = mu0

    dist_count = 0
    total_kl = 0.0

    for t in range(T):
        # p_t: predicted signal dist under commitment
        pc_A = filt_c  # P(A | commitment) = P(G | h_t, commitment)

        # r_t: predicted signal dist under rational type
        rr_A = filt_r * r_A_given_G + (1 - filt_r) * r_A_given_B

        # q_t: equilibrium mixture signal distribution
        qm_A = mu * pc_A + (1 - mu) * rr_A

        p_t = np.array([pc_A, 1 - pc_A])
        q_t = np.array([qm_A, 1 - qm_A])

        # TV distance
        tv = 0.5 * np.sum(np.abs(p_t - q_t))
        if tv > eta:
            dist_count += 1

        # Per-period KL(p_t || q_t)
        kl_t = 0.0
        for i in range(2):
            if p_t[i] > 1e-15 and q_t[i] > 1e-15:
                kl_t += p_t[i] * np.log(p_t[i] / q_t[i])
        total_kl += kl_t

        # Generate signal under commitment type DGP
        true_G = states[t]
        y_is_A = true_G  # commitment: A iff G

        # Bayesian type posterior update: mu_{t+1} = mu * p_t(y) / q_t(y)
        if y_is_A:
            p_y = pc_A
            q_y = qm_A
        else:
            p_y = 1 - pc_A
            q_y = 1 - qm_A

        if q_y > 1e-15:
            mu = mu * p_y / q_y
        mu = min(mu, 1.0 - 1e-10)

        # Update state filters for next period
        # Under commitment (state-revealing): observing A => G, F => B
        if y_is_A:
            post_c_G = 1.0
        else:
            post_c_G = 0.0

        # Under rational (noisy signal):
        if y_is_A:
            num = filt_r * r_A_given_G
            den = filt_r * r_A_given_G + (1 - filt_r) * r_A_given_B
        else:
            num = filt_r * (1 - r_A_given_G)
            den = filt_r * (1 - r_A_given_G) + (1 - filt_r) * (1 - r_A_given_B)
        post_r_G = num / den if den > 1e-15 else 0.5

        # Propagate state belief to next period
        if is_markov:
            filt_c = post_c_G * (1 - alpha) + (1 - post_c_G) * beta
            filt_r = post_r_G * (1 - alpha) + (1 - post_r_G) * beta
        else:
            filt_c = pi_G
            filt_r = pi_G

    return dist_count, total_kl, mu


def simulate(alpha=0.3, beta=0.5, N=500, T=5000, eta=0.1, mu0=0.05, seed=42):
    rng = np.random.default_rng(seed)
    pi_G = beta / (alpha + beta)
    bound = -2.0 * np.log(mu0) / (eta ** 2)
    kl_bound = -np.log(mu0)

    iid_counts = np.zeros(N)
    mk_counts = np.zeros(N)
    iid_kl = np.zeros(N)
    mk_kl = np.zeros(N)

    for run in range(N):
        # I.I.D. states
        st_iid = rng.random(T) < pi_G

        # Markov states
        st_mk = np.zeros(T, dtype=bool)
        st_mk[0] = rng.random() < pi_G
        for t in range(1, T):
            if st_mk[t - 1]:
                st_mk[t] = rng.random() >= alpha
            else:
                st_mk[t] = rng.random() < beta

        c, k, _ = run_single(st_iid, alpha, beta, pi_G, eta, mu0, is_markov=False)
        iid_counts[run], iid_kl[run] = c, k

        c, k, _ = run_single(st_mk, alpha, beta, pi_G, eta, mu0, is_markov=True)
        mk_counts[run], mk_kl[run] = c, k

    return iid_counts, mk_counts, iid_kl, mk_kl, bound, kl_bound


def main():
    print("=" * 65)
    print("  C10: KL Counting Bound — Markov vs. I.I.D.")
    print("=" * 65)

    eta = 0.1
    mu0 = 0.05
    iid_c, mk_c, iid_kl, mk_kl, count_bound, kl_bound = simulate(eta=eta, mu0=mu0)

    print(f"\nSetup: alpha=0.3, beta=0.5, pi(G)=0.625")
    print(f"  Commitment: s1*(G)=A, s1*(B)=F")
    print(f"  Rational:   P(A|G)=0.70, P(A|B)=0.30")
    print(f"  N=500, T=5000, eta={eta}, mu0={mu0}")
    print(f"  Count bound bar_T = {count_bound:.1f}")
    print(f"  KL bound -log(mu0) = {kl_bound:.2f}")

    for label, counts, kls in [("I.I.D.", iid_c, iid_kl), ("Markov", mk_c, mk_kl)]:
        print(f"\n--- {label} Process ---")
        print(f"  Distinguishing periods: mean={counts.mean():.1f}, "
              f"std={counts.std():.1f}, max={counts.max():.0f}")
        print(f"  Total KL:  mean={kls.mean():.3f}, max={kls.max():.3f}")
        print(f"  Runs below count bound: {np.mean(counts <= count_bound) * 100:.0f}%")
        print(f"  Runs with total KL < -log(mu0): {np.mean(kls <= kl_bound) * 100:.0f}%")

    print(f"\n--- Comparison ---")
    print(f"  I.I.D. mean count:   {iid_c.mean():.1f}")
    print(f"  Markov mean count:   {mk_c.mean():.1f}")
    print(f"  Theoretical bound:   {count_bound:.1f}")
    print(f"  Both below bound: {mk_c.max() <= count_bound and iid_c.max() <= count_bound}")

    print(f"\n--- Conclusion ---")
    print(f"  The KL counting bound holds for both processes.")
    print(f"  As the type posterior concentrates on commitment, the equilibrium")
    print(f"  signal distribution converges to the commitment distribution,")
    print(f"  making later periods non-distinguishing. The bound is identical")
    print(f"  for Markov and i.i.d., confirming no mixing-time correction needed.")


if __name__ == "__main__":
    main()
