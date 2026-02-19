"""
C18 Verification: Strict supermodularity on the lifted space.

Demonstrates that under the first-coordinate order on theta_tilde = (theta_t, theta_{t-1}),
payoffs u1 that depend only on theta_t preserve strict supermodularity despite being
constant in theta_{t-1}.
"""


def check_strict_supermodularity(u, states_ordered, actions_ordered):
    """
    Check strict supermodularity: for all s > s' and a > a':
      u(s, a) - u(s, a') > u(s', a) - u(s', a')

    states_ordered and actions_ordered are lists in ascending order.
    u: dict (state, action) -> payoff
    """
    violations = []
    satisfied = []

    for i in range(len(states_ordered)):
        for j in range(i):
            s_H = states_ordered[i]
            s_L = states_ordered[j]
            for k in range(len(actions_ordered)):
                for l in range(k):
                    a_H = actions_ordered[k]
                    a_L = actions_ordered[l]

                    diff_H = u[(s_H, a_H)] - u[(s_H, a_L)]
                    diff_L = u[(s_L, a_H)] - u[(s_L, a_L)]

                    if diff_H > diff_L + 1e-10:
                        satisfied.append(f"  {s_H} vs {s_L}: diff_H={diff_H:.3f} > diff_L={diff_L:.3f} ✓")
                    elif abs(diff_H - diff_L) < 1e-10:
                        violations.append(f"  {s_H} vs {s_L}: diff_H={diff_H:.3f} = diff_L={diff_L:.3f} (weak, not strict)")
                    else:
                        violations.append(f"  {s_H} vs {s_L}: diff_H={diff_H:.3f} < diff_L={diff_L:.3f} ✗")

    return violations, satisfied


print("=" * 75)
print("C18 VERIFICATION: Supermodularity on the Lifted Space")
print("=" * 75)

# ---- Base payoffs (depend only on theta_t) ----
# u1(G, H) - u1(G, L) > u1(B, H) - u1(B, L)  [strict supermodularity in (theta_t, a1)]
u1_base = {
    ("B", "L"): 0.0,
    ("B", "H"): 0.3,
    ("G", "L"): 0.5,
    ("G", "H"): 1.0
}

print("\n--- Base payoffs u1(theta_t, a1) ---")
print(f"  u1(B, L) = {u1_base[('B','L')]}, u1(B, H) = {u1_base[('B','H')]}")
print(f"  u1(G, L) = {u1_base[('G','L')]}, u1(G, H) = {u1_base[('G','H')]}")
print(f"  diff at G = {u1_base[('G','H')] - u1_base[('G','L')]:.1f}")
print(f"  diff at B = {u1_base[('B','H')] - u1_base[('B','L')]:.1f}")
print(f"  Strictly supermodular in (theta_t, a1)? "
      f"{u1_base[('G','H')] - u1_base[('G','L')] > u1_base[('B','H')] - u1_base[('B','L')]}")

# ---- Lifted payoffs (using TOTAL order: lexicographic) ----
print("\n--- Lifted payoffs with LEXICOGRAPHIC order (WRONG approach) ---")
# Lexicographic: (B,B) < (B,G) < (G,B) < (G,G)
lifted_states_lex = ["(B,B)", "(B,G)", "(G,B)", "(G,G)"]
u1_lifted = {}
for s in lifted_states_lex:
    theta_t = s[1]  # first coordinate
    for a in ["L", "H"]:
        u1_lifted[(s, a)] = u1_base[(theta_t, a)]

print("Lifted u1 (depends only on theta_t):")
for s in lifted_states_lex:
    print(f"  {s}: u1(·,L)={u1_lifted[(s,'L')]:.1f}, u1(·,H)={u1_lifted[(s,'H')]:.1f}, "
          f"diff={u1_lifted[(s,'H')]-u1_lifted[(s,'L')]:.1f}")

violations, satisfied = check_strict_supermodularity(u1_lifted, lifted_states_lex, ["L", "H"])
print(f"\nStrict supermodularity check (lexicographic order):")
for s in satisfied:
    print(s)
for v in violations:
    print(v)

if violations:
    print("\nVIOLATIONS detected under lexicographic order!")
    print("This is because (B,G) and (G,B) are strictly ordered under lex,")
    print("but u1(B,G) = u1(B,·) and u1(G,B) = u1(G,·) have different diffs.")
    print("More importantly, (G,G) vs (G,B): same diffs → not STRICT.")

# ---- Lifted payoffs with FIRST-COORDINATE order (CORRECT approach) ----
print("\n--- Lifted payoffs with FIRST-COORDINATE order (CORRECT approach) ---")
print("Order: (theta_t, theta_{t-1}) >= (theta_t', theta_{t-1}') iff theta_t >= theta_t'")
print("\nComparable pairs (strictly ordered):")

lifted_states = ["(B,B)", "(B,G)", "(G,B)", "(G,G)"]
def first_coord(s):
    return s[1]  # "B" or "G"

strictly_ordered_pairs = []
incomparable_pairs = []

for i, s1 in enumerate(lifted_states):
    for j, s2 in enumerate(lifted_states):
        if i >= j:
            continue
        fc1 = first_coord(s1)
        fc2 = first_coord(s2)
        if fc1 != fc2:
            if fc2 > fc1:
                strictly_ordered_pairs.append((s1, s2))
            else:
                strictly_ordered_pairs.append((s2, s1))
        else:
            incomparable_pairs.append((s1, s2))

for s_L, s_H in strictly_ordered_pairs:
    diff_H = u1_lifted[(s_H, "H")] - u1_lifted[(s_H, "L")]
    diff_L = u1_lifted[(s_L, "H")] - u1_lifted[(s_L, "L")]
    print(f"  {s_H} > {s_L}: diff_H={diff_H:.1f}, diff_L={diff_L:.1f}, "
          f"strict ID? {diff_H > diff_L}")

print("\nIncomparable pairs (NO increasing-differences condition imposed):")
for s1, s2 in incomparable_pairs:
    print(f"  {s1} ~ {s2} (same first coordinate, incomparable)")
    diff1 = u1_lifted[(s1, "H")] - u1_lifted[(s1, "L")]
    diff2 = u1_lifted[(s2, "H")] - u1_lifted[(s2, "L")]
    print(f"    diffs: {diff1:.1f} and {diff2:.1f} (equal, but no constraint needed)")

print("\nUnder the first-coordinate order:")
print("- All strictly ordered pairs have the required strict increasing differences ✓")
print("- Incomparable pairs impose no constraint ✓")
print("- Strict supermodularity HOLDS on the lifted space ✓")

print("\n" + "=" * 75)
print("CONCLUSION")
print("=" * 75)
print("""
1. Under the LEXICOGRAPHIC order, strict supermodularity fails because
   pairs like (G,G) vs (G,B) have equal diffs (not strictly increasing).

2. Under the FIRST-COORDINATE (partial) order, (G,G) and (G,B) are
   INCOMPARABLE, so no increasing-differences condition is imposed.

3. All strictly ordered pairs (those with different first coordinates)
   DO satisfy strict increasing differences, because the payoff only
   depends on theta_t (the first coordinate).

4. The paper correctly uses the first-coordinate order but should
   EXPLICITLY state why constancy in theta_{t-1} is not a problem:
   incomparable states impose no constraint.
""")
