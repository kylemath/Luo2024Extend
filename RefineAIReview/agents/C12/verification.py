#!/usr/bin/env python3
"""
C12 Verification: Figure 6 caption claims distributions are "nearly identical"
but means are 8.1 vs 12.7. Checks bound validity and assesses similarity claim.
"""

import math

print("=== C12: KL Bound Figure Caption Verification ===\n")

# Parameters from stats.tex
iid_mean = 8.1
markov_mean = 12.7
mu0 = 0.01
eta = 0.1

# KL bound
T_bar = -2 * math.log(mu0) / eta**2
print(f"Analytical bound: T_bar = -2*log({mu0}) / {eta}^2 = {T_bar:.0f}")

# Mean comparison
diff = markov_mean - iid_mean
rel_diff = diff / iid_mean * 100
print(f"\ni.i.d. mean count:   {iid_mean}")
print(f"Markov mean count:   {markov_mean}")
print(f"Absolute difference: {diff:.1f}")
print(f"Relative difference: {rel_diff:.1f}%")
print(f"*** A {rel_diff:.0f}% difference is NOT 'nearly identical' ***\n")

# Both well below bound
iid_pct = iid_mean / T_bar * 100
markov_pct = markov_mean / T_bar * 100
print(f"i.i.d. mean as % of bound:  {iid_pct:.2f}%")
print(f"Markov mean as % of bound:  {markov_pct:.2f}%")
print(f"Both are < 1.5% of the bound → bound holds with large margin ✓\n")

# Ratio of means
ratio = markov_mean / iid_mean
print(f"Markov/i.i.d. ratio: {ratio:.2f}")
print(f"Markov has ~{ratio:.1f}x as many distinguishing periods as i.i.d.")
print(f"This is consistent with autocorrelation creating more 'runs'")
print(f"of similar signals, increasing the number of distinguishing periods.\n")

# Assessment
print("--- Assessment ---")
print(f"'Nearly identical' is WRONG for describing the distributions")
print(f"  (means differ by {rel_diff:.0f}%)")
print(f"'Both well below the bound' is CORRECT")
print(f"  (both < 1.5% of T_bar = {T_bar:.0f})")
print(f"The mathematical claim (KL bound extends without modification)")
print(f"is FULLY SUPPORTED by the evidence.")
print(f"Only the descriptive language needs correction.")

print("\n=== ALL C12 CHECKS COMPLETE ===")
