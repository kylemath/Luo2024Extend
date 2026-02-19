#!/usr/bin/env python3
"""
C08 Verification: Arithmetic error in belief-robust condition
Checks mu* = BRThreshold < beta = BaseBeta.
"""

alpha = 0.3
beta = 0.5

BRThreshold = 0.60
BaseBeta = beta

print("=== C08: Belief-Robust Condition Check ===\n")

print(f"Paper claims: mu* = {BRThreshold} < beta = {BaseBeta}")
print(f"Truth: {BRThreshold} < {BaseBeta}? {BRThreshold < BaseBeta}")
print(f"*** ERROR: {BRThreshold} > {BaseBeta} (0.60 > 0.50) ***\n")

# Filtering beliefs
F_G_given_G = 1 - alpha  # 0.70
F_G_given_B = beta        # 0.50

print("Filtering beliefs:")
print(f"  F(G|G) = 1-alpha = {F_G_given_G:.2f}")
print(f"  F(G|B) = beta = {F_G_given_B:.2f}")

print(f"\nBelief-robust requires: mu* <= F(G|theta) for ALL theta")
print(f"  mu* <= F(G|G)? {BRThreshold} <= {F_G_given_G}? {BRThreshold <= F_G_given_G}")
print(f"  mu* <= F(G|B)? {BRThreshold} <= {F_G_given_B}? {BRThreshold <= F_G_given_B}")
print(f"  *** FAILS for theta=B: {BRThreshold} > {F_G_given_B} ***\n")

# For belief-robust, we need mu* < beta = F(G|B)
print("For belief-robustness, need mu* < beta:")
print(f"  Current: mu* = {BRThreshold}, beta = {beta}")
print(f"  Need: mu* < {beta}\n")

# Proposed fix: BRThreshold = 0.40
BRThreshold_new = 0.40
print(f"--- Proposed Fix: BRThreshold = {BRThreshold_new} ---")
print(f"  mu* = {BRThreshold_new} < beta = {beta}? {BRThreshold_new < beta} ✓")
print(f"  mu* = {BRThreshold_new} <= F(G|G) = {F_G_given_G}? {BRThreshold_new <= F_G_given_G} ✓")
print(f"  mu* = {BRThreshold_new} <= F(G|B) = {F_G_given_B}? {BRThreshold_new <= F_G_given_B} ✓")

# Check BRPayoff
pi_G = beta / (alpha + beta)
pi_B = alpha / (alpha + beta)
V_s1star = pi_G * 1 + pi_B * 0  # Against D
print(f"\nV(s1*) [against D] = {V_s1star:.4f}")
print(f"BRPayoff from stats.tex = 0.60")
print(f"V(s1*) = beta/(alpha+beta) = {beta/(alpha+beta):.4f}")
print(f"*** BRPayoff should be 0.625, not 0.60 ***")

# Also check: the section says the bound is "exact and identical to i.i.d. case"
# This is consistent: under belief-robustness, V(s1*) is the correct bound.
# But BRPayoff = 0.60 is wrong — should be 0.625.

# Alternative fix: change both BRThreshold and BRPayoff
print(f"\n--- Full Proposed Fix ---")
print(f"  BRThreshold: 0.60 → 0.40")
print(f"  BRPayoff: 0.60 → 0.625 (= beta/(alpha+beta))")
print(f"  Section 7.4 text: 'mu* = 0.40 < beta = 0.50' ✓")

print("\n=== ALL C08 CHECKS COMPLETE ===")
