#!/usr/bin/env python3
"""
C09 Verification: Arithmetic error and variable confusion in cost of persistence
Checks: 0.777-0.628, belief gap formula, percentage base
"""

alpha = 0.3
beta = 0.5

pi_G = beta / (alpha + beta)
pi_B = alpha / (alpha + beta)

PayoffStationary = 0.777
PayoffFiltered = 0.628

print("=== C09: Cost of Persistence Arithmetic ===\n")

# Check 1: The subtraction
payoff_gap = PayoffStationary - PayoffFiltered
print(f"PayoffStationary - PayoffFiltered = {PayoffStationary} - {PayoffFiltered} = {payoff_gap:.3f}")
print(f"Paper claims: 0.094")
print(f"Correct: {payoff_gap:.3f}")
assert abs(payoff_gap - 0.149) < 1e-10
print(f"*** ERROR CONFIRMED: 0.777 - 0.628 = 0.149, NOT 0.094 ***\n")

# Check 2: The belief gap formula
belief_gap = 2 * alpha * beta * abs(1 - alpha - beta) / (alpha + beta)**2
print(f"Belief gap formula: 2*alpha*beta*|1-alpha-beta| / (alpha+beta)^2")
print(f"  = 2*{alpha}*{beta}*{abs(1-alpha-beta):.1f} / {(alpha+beta)**2:.2f}")
print(f"  = {2*alpha*beta*abs(1-alpha-beta):.4f} / {(alpha+beta)**2:.4f}")
print(f"  = {belief_gap:.6f}")
print(f"  ≈ {belief_gap:.3f}")
assert abs(belief_gap - 0.09375) < 1e-10
print(f"Belief gap = {belief_gap:.3f} (this is what PayoffGapAbsolute stores)")
print(f"Payoff gap = {payoff_gap:.3f} (this is the actual 0.777-0.628)")
print(f"*** These are DIFFERENT quantities conflated in Section 8.5 ***\n")

# Check 3: Percentage base
pct_of_iid = payoff_gap / PayoffStationary * 100
pct_of_markov = payoff_gap / PayoffFiltered * 100
print(f"Overestimation percentage:")
print(f"  As % of i.i.d. payoff:  {payoff_gap:.3f} / {PayoffStationary} = {pct_of_iid:.1f}%")
print(f"  As % of Markov payoff:  {payoff_gap:.3f} / {PayoffFiltered} = {pct_of_markov:.1f}%")
print(f"  Paper claims: 23.7%")
print(f"")
print(f"  23.7% matches % of Markov payoff ({pct_of_markov:.1f}%), NOT i.i.d. payoff ({pct_of_iid:.1f}%)")
assert abs(pct_of_markov - 23.7) < 0.1
print(f"*** ERROR CONFIRMED: 23.7% is relative to Markov payoff, not i.i.d. ***\n")

# Check 4: Verify the relationship between gaps
print(f"--- Relationship between belief gap and payoff gap ---")
print(f"Belief gap (TV distance): {belief_gap:.4f}")
print(f"Payoff gap (economic):    {payoff_gap:.4f}")
print(f"Amplification factor:     {payoff_gap/belief_gap:.2f}x")
print(f"The payoff gap exceeds the belief gap because the game's payoff")
print(f"structure amplifies the effect of belief differences.\n")

# Summary
print("=== SUMMARY OF ERRORS IN SECTION 8.5 ===")
print(f"1. '0.777 - 0.628 = 0.094' should be '0.777 - 0.628 = 0.149'")
print(f"2. 0.094 is the BELIEF gap, 0.149 is the PAYOFF gap")
print(f"3. '23.7% of the i.i.d. payoff' should be '23.7% relative to the Markov payoff'")

print("\n=== ALL C09 CHECKS COMPLETE ===")
