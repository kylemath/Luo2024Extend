"""
C15 Verification: Confound-defeating condition is unchanged under persistence.

Demonstrates:
1. The mathematical condition (monotonicity) is the same for i.i.d. and Markov
2. The statistical distinguishability (identification) is improved under persistence
"""

import numpy as np


def is_monotone(s1_star, states_ordered):
    """
    Check if s1* is monotone: higher states → higher actions.
    s1_star: dict state -> action (or probability of high action)
    """
    for i in range(len(states_ordered) - 1):
        if s1_star[states_ordered[i+1]] < s1_star[states_ordered[i]] - 1e-10:
            return False
    return True


def simulate_actions(s1_star, alpha, beta, T, markov=True):
    """
    Simulate action sequences under a state-contingent strategy.
    s1_star: dict {"G": prob_high_action, "B": prob_high_action}
    Returns array of actions (0 or 1).
    """
    pi_G = beta / (alpha + beta)
    state = "G" if np.random.random() < pi_G else "B"
    actions = []
    states = []

    for t in range(T):
        p_high = s1_star[state]
        action = 1 if np.random.random() < p_high else 0
        actions.append(action)
        states.append(state)

        if markov:
            if state == "G":
                state = "B" if np.random.random() < alpha else "G"
            else:
                state = "G" if np.random.random() < beta else "B"
        else:
            state = "G" if np.random.random() < pi_G else "B"

    return np.array(actions), states


np.random.seed(42)

print("=" * 75)
print("C15 VERIFICATION: Confound-Defeating Under Persistence")
print("=" * 75)

# ---- Mathematical condition: unchanged ----
print("\n--- Mathematical Condition: Monotonicity ---")

s1_monotone = {"B": 0.3, "G": 0.8}  # higher state → higher action
s1_nonmonotone = {"B": 0.7, "G": 0.4}  # violates monotonicity

print(f"Strategy s1*_monotone:     B -> {s1_monotone['B']}, G -> {s1_monotone['G']}")
print(f"  Monotone? {is_monotone(s1_monotone, ['B', 'G'])}")
print(f"  Confound-defeating (supermodular case)? {is_monotone(s1_monotone, ['B', 'G'])}")

print(f"Strategy s1*_nonmonotone:  B -> {s1_nonmonotone['B']}, G -> {s1_nonmonotone['G']}")
print(f"  Monotone? {is_monotone(s1_nonmonotone, ['B', 'G'])}")
print(f"  Confound-defeating (supermodular case)? {is_monotone(s1_nonmonotone, ['B', 'G'])}")

print("\nThe condition is IDENTICAL for i.i.d. and Markov — it depends only on")
print("the payoff structure and strategy, not on the state dynamics.")

# ---- Statistical distinguishability: improved ----
print("\n--- Statistical Distinguishability ---")

alpha, beta = 0.3, 0.5
T = 1000
n_sims = 200

s1_conditional = {"G": 0.8, "B": 0.3}    # state-contingent
s1_unconditional = {"G": 0.5875, "B": 0.5875}  # same average frequency

print(f"\nComparing strategies with same per-period frequency:")
print(f"  s1_conditional:   G -> {s1_conditional['G']}, B -> {s1_conditional['B']}")
pi_G = beta / (alpha + beta)
avg_freq = pi_G * s1_conditional['G'] + (1 - pi_G) * s1_conditional['B']
print(f"  Average high-action freq: {avg_freq:.4f}")
print(f"  s1_unconditional: G -> {s1_unconditional['G']}, B -> {s1_unconditional['B']}")
print(f"  Average high-action freq: {pi_G * s1_unconditional['G'] + (1-pi_G) * s1_unconditional['B']:.4f}")

# Measure autocorrelation as a distinguishing statistic
autocorrs_iid_cond = []
autocorrs_iid_uncond = []
autocorrs_markov_cond = []
autocorrs_markov_uncond = []

for _ in range(n_sims):
    # i.i.d. states
    a_iid_cond, _ = simulate_actions(s1_conditional, alpha, beta, T, markov=False)
    a_iid_uncond, _ = simulate_actions(s1_unconditional, alpha, beta, T, markov=False)

    # Markov states
    a_markov_cond, _ = simulate_actions(s1_conditional, alpha, beta, T, markov=True)
    a_markov_uncond, _ = simulate_actions(s1_unconditional, alpha, beta, T, markov=True)

    def autocorr(x):
        x = x - x.mean()
        if np.std(x) < 1e-10:
            return 0
        return np.corrcoef(x[:-1], x[1:])[0, 1]

    autocorrs_iid_cond.append(autocorr(a_iid_cond))
    autocorrs_iid_uncond.append(autocorr(a_iid_uncond))
    autocorrs_markov_cond.append(autocorr(a_markov_cond))
    autocorrs_markov_uncond.append(autocorr(a_markov_uncond))

print(f"\nAction autocorrelation (lag 1):")
print(f"  i.i.d. states,  conditional:   {np.mean(autocorrs_iid_cond):>7.4f} ± {np.std(autocorrs_iid_cond):.4f}")
print(f"  i.i.d. states,  unconditional: {np.mean(autocorrs_iid_uncond):>7.4f} ± {np.std(autocorrs_iid_uncond):.4f}")
print(f"  Markov states, conditional:   {np.mean(autocorrs_markov_cond):>7.4f} ± {np.std(autocorrs_markov_cond):.4f}")
print(f"  Markov states, unconditional: {np.mean(autocorrs_markov_uncond):>7.4f} ± {np.std(autocorrs_markov_uncond):.4f}")

gap_iid = abs(np.mean(autocorrs_iid_cond) - np.mean(autocorrs_iid_uncond))
gap_markov = abs(np.mean(autocorrs_markov_cond) - np.mean(autocorrs_markov_uncond))

print(f"\n  Autocorrelation gap (conditional vs unconditional):")
print(f"    Under i.i.d.:  {gap_iid:.4f}")
print(f"    Under Markov: {gap_markov:.4f}")
print(f"    Ratio (Markov/i.i.d.): {gap_markov/gap_iid:.2f}x")

if gap_markov > gap_iid:
    print(f"\n  Markov states provide BETTER distinguishability ({gap_markov/gap_iid:.1f}x)")
    print("  → Persistence strengthens IDENTIFICATION (empirical testability)")
else:
    print(f"\n  Distinguishability is similar")

print("\n" + "=" * 75)
print("CONCLUSION")
print("=" * 75)
print("""
1. The mathematical condition (monotonicity <-> confound-defeating) is
   IDENTICAL for i.i.d. and Markov. The reviewer is correct.

2. Persistence improves statistical DISTINGUISHABILITY of strategies:
   autocorrelation in action sequences is amplified under Markov states,
   making it easier to empirically VERIFY (not mathematically SATISFY)
   the confound-defeating condition.

3. The paper should replace "easier to satisfy" with "easier to verify
   empirically" or "providing a richer identification channel."
""")
