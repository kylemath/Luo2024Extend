# C18: Failure of Strict Supermodularity on Lifted Space

## Assessment: GREEN

## Reviewer Comment
> "u₁(θ̃, a₁, α₂) = u₁(θ_t, a₁, α₂)" suggests tension with strict supermodularity since payoff is constant in second coordinate of θ̃ = (θ_t, θ_{t-1}).

The reviewer self-resolves: under the first-coordinate order, states differing only in θ_{t-1} are not strictly ordered, so strict increasing differences is preserved.

## Location
`sec_06_supermodular.tex`, Section 6.2, lines 19–23.

## Analysis

The reviewer correctly identifies a potential concern and then correctly resolves it. Here's the full analysis:

### The Apparent Tension

The lifted state is θ̃ = (θ_t, θ_{t-1}). Payoffs satisfy u₁(θ̃, a₁, α₂) = u₁(θ_t, a₁, α₂) — they depend only on the first coordinate. This means:

u₁((G, G), a₁, α₂) = u₁((G, B), a₁, α₂)

So u₁ is constant across θ̃ values that differ only in the second coordinate. This seems to violate strict supermodularity, which requires STRICT increasing differences between strictly ordered states.

### The Resolution (First-Coordinate Order)

The paper defines the order on θ̃ as the first-coordinate order:
(θ_t, θ_{t-1}) ≽ (θ_t', θ_{t-1}') iff θ_t ≽ θ_t'

Under this partial order:
- (G, G) and (G, B) are **not comparable** (both have the same first coordinate G, so neither is strictly above the other)
- (G, G) ≻ (B, B) ✓ (first coordinates G > B)
- (G, G) ≻ (B, G) ✓ (first coordinates G > B)
- (G, B) ≻ (B, B) ✓ (first coordinates G > B)
- (G, B) ≻ (B, G) ✓ (first coordinates G > B)

Strict supermodularity requires strict increasing differences only between **strictly ordered** pairs. Since (G, G) and (G, B) are not strictly ordered, no increasing-differences condition is imposed between them. The fact that u₁ is equal for these pairs is consistent with strict supermodularity.

### What the Paper Already Says

Section 6.2 (line 21) states:
> "The relevant order on θ̃ is the first-coordinate order: (θ_t, θ_{t-1}) ≽ (θ_t', θ_{t-1}') if and only if θ_t ≽ θ_t'. Under this order, the supermodularity condition is unchanged from the i.i.d. case."

This is correct but does not explicitly address WHY the constancy in the second coordinate doesn't violate strict supermodularity.

### The Fix

Add an explicit sentence explaining that under the first-coordinate order, states differing only in θ_{t-1} are incomparable, so no increasing-differences condition is imposed between them.

## Resolution

Minor editorial addition to Section 6.2. The mathematics is already correct; the paper just needs to be more explicit about this point.
