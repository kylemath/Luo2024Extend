#!/usr/bin/env python3
"""
C03 Verification: Contradictory i.i.d. benchmark values
Checks V(s1*), PayoffStationary, PayoffFiltered, V_Markov, and their relationships.
"""

alpha = 0.3
beta = 0.5

# Stationary distribution
pi_G = beta / (alpha + beta)
pi_B = alpha / (alpha + beta)
print(f"pi(G) = {beta}/{alpha+beta} = {pi_G:.4f}")
print(f"pi(B) = {alpha}/{alpha+beta} = {pi_B:.4f}")
assert abs(pi_G - 0.625) < 1e-10
assert abs(pi_B - 0.375) < 1e-10

# Filtering beliefs (one-step-ahead predictive)
F_G_given_G = 1 - alpha  # P(G_{t+1} | theta_t = G)
F_G_given_B = beta        # P(G_{t+1} | theta_t = B)
print(f"\nF(G|G) = 1 - alpha = {F_G_given_G:.2f}")
print(f"F(G|B) = beta = {F_G_given_B:.2f}")
assert abs(F_G_given_G - 0.70) < 1e-10
assert abs(F_G_given_B - 0.50) < 1e-10

# Game payoffs (D-row only, from Section 7.1)
x, y = 0.3, 0.4
u1_GA_D = 1.0   # u1(G, A) when SR defects
u1_GF_D = x     # u1(G, F) when SR defects
u1_BA_D = y     # u1(B, A) when SR defects
u1_BF_D = 0.0   # u1(B, F) when SR defects

# Stackelberg strategy: s1*(G) = A, s1*(B) = F
# V(s1*) as computed in Section 7.6 (against D-row payoffs)
V_commitment_D = pi_G * u1_GA_D + pi_B * u1_BF_D
print(f"\n--- Section 7.6 Computation ---")
print(f"V(s1*) [against D] = pi(G)*u1(G,A,D) + pi(B)*u1(B,F,D)")
print(f"  = {pi_G:.3f}*{u1_GA_D} + {pi_B:.3f}*{u1_BF_D} = {V_commitment_D:.4f}")
assert abs(V_commitment_D - 0.625) < 1e-10

# V(s1*) = beta/(alpha+beta) from the proposition
V_formula = beta / (alpha + beta)
print(f"V(s1*) = beta/(alpha+beta) = {V_formula:.4f}")
assert abs(V_commitment_D - V_formula) < 1e-10
print("CONFIRMED: Section 7.6 V(s1*) = 0.625 = beta/(alpha+beta)")

# PayoffStationary = 0.777 from stats.tex
# This is the equilibrium payoff when SR always cooperates
# (because under stationary beliefs mu = pi(G) = 0.625 > mu* = 0.60)
PayoffStationary = 0.777
PayoffFiltered = 0.628

print(f"\n--- Section 7.7 Values ---")
print(f"PayoffStationary = {PayoffStationary}")
print(f"PayoffFiltered = {PayoffFiltered}")

# These must come from equilibrium payoffs including C-row.
# Under stationary beliefs: SR always cooperates → payoff = E[u1(theta, s1*(theta), C)]
# Under filtered beliefs: SR cooperates in G, defects in B
#   → payoff = pi(G)*u1(G,A,C) + pi(B)*u1(B,F,D)

# From PayoffFiltered: pi(G)*u1(G,A,C) + pi(B)*u1(B,F,D) = 0.628
# pi(B)*u1(B,F,D) = 0.375 * 0 = 0
# So u1(G,A,C) = 0.628 / 0.625 = 1.0048
u1_GA_C_implied = PayoffFiltered / pi_G
print(f"\nImplied u1(G,A,C) from PayoffFiltered: {u1_GA_C_implied:.4f}")

# From PayoffStationary: pi(G)*u1(G,A,C) + pi(B)*u1(B,F,C) = 0.777
u1_BF_C_implied = (PayoffStationary - pi_G * u1_GA_C_implied) / pi_B
print(f"Implied u1(B,F,C) from PayoffStationary: {u1_BF_C_implied:.4f}")

print(f"\n--- KEY RELATIONSHIP CHECK ---")
print(f"V(s1*) [Section 7.6]    = {V_commitment_D:.4f}")
print(f"PayoffFiltered [Sec 7.7] = {PayoffFiltered:.4f}")
print(f"PayoffStationary [Sec 7.7] = {PayoffStationary:.4f}")

print(f"\nPaper claims V_Markov <= V(s1*):")
print(f"  V_Markov = PayoffFiltered = {PayoffFiltered}")
print(f"  V(s1*)   = {V_commitment_D}")
print(f"  {PayoffFiltered} <= {V_commitment_D}? {PayoffFiltered <= V_commitment_D}")
if PayoffFiltered > V_commitment_D:
    print(f"  *** VIOLATION: V_Markov ({PayoffFiltered}) > V(s1*) ({V_commitment_D}) ***")
    print(f"  This occurs because V(s1*)=0.625 uses D-row payoffs only,")
    print(f"  while V_Markov=0.628 includes C-payoff in good states.")

print(f"\nIf V(s1*) means the i.i.d. equilibrium payoff (SR cooperates):")
print(f"  V(s1*) = PayoffStationary = {PayoffStationary}")
print(f"  V_Markov = {PayoffFiltered} <= {PayoffStationary}? {PayoffFiltered <= PayoffStationary}")
print(f"  CONSISTENT: {PayoffFiltered} <= {PayoffStationary}")

print(f"\n--- DIAGNOSIS ---")
print("The paper has two distinct objects both partially called 'V(s1*)':")
print(f"  (A) Commitment payoff against worst-case SR (D-row): beta/(alpha+beta) = {V_commitment_D:.4f}")
print(f"  (B) Equilibrium payoff when SR cooperates (stationary beliefs): {PayoffStationary}")
print(f"  (C) Equilibrium payoff under filtered beliefs (V_Markov): {PayoffFiltered}")
print(f"")
print(f"The ordering V_Markov <= V(s1*) is SATISFIED if V(s1*) means (B):")
print(f"  {PayoffFiltered} <= {PayoffStationary} ✓")
print(f"The ordering V_Markov <= V(s1*) is VIOLATED if V(s1*) means (A):")
print(f"  {PayoffFiltered} > {V_commitment_D} ✗")
print(f"")
print("Section 7.6 computes (A) = 0.625 and calls it 'V(s1*)'")
print("Section 7.7 computes (B) = 0.777 and calls it 'Stationary beliefs payoff'")
print("Section 7.5 computes (C) = 0.628 and calls it 'V_Markov'")
print("The comparison table claims (C) <= (A), i.e., 0.628 <= 0.625, which is FALSE.")
print("")
print("RESOLUTION: Section 7.6 should clarify that 0.625 is the worst-case (against D)")
print("commitment payoff, NOT the same as V(s1*) used in the theorems. The formal V(s1*)")
print("used in the theorem bound is 0.777 (equilibrium payoff with SR cooperation).")
print("Alternatively, fix the comparison to V_Markov <= PayoffStationary = 0.777.")

# Belief gap formula
belief_gap = 2 * alpha * beta * abs(1 - alpha - beta) / (alpha + beta)**2
print(f"\n--- Belief Gap ---")
print(f"2*alpha*beta*|1-alpha-beta|/(alpha+beta)^2")
print(f"= 2*{alpha}*{beta}*{abs(1-alpha-beta)}/{(alpha+beta)**2}")
print(f"= {2*alpha*beta*abs(1-alpha-beta):.4f}/{(alpha+beta)**2:.4f}")
print(f"= {belief_gap:.6f}")
print(f"Rounded: {belief_gap:.3f} (paper says 0.094)")
assert abs(belief_gap - 0.09375) < 1e-10

# Payoff difference
payoff_diff = PayoffStationary - PayoffFiltered
print(f"\nPayoff difference: {PayoffStationary} - {PayoffFiltered} = {payoff_diff:.3f}")
print(f"This is NOT equal to the belief gap {belief_gap:.3f}")

# KL bound
import math
mu0 = 0.01
eta = 0.1
T_bar = -2 * math.log(mu0) / eta**2
print(f"\n--- KL Bound ---")
print(f"T_bar = -2*log({mu0}) / {eta}^2 = {-2*math.log(mu0):.3f} / {eta**2} = {T_bar:.0f}")
assert abs(T_bar - 921) < 1

print("\n=== ALL C03 CHECKS COMPLETE ===")
