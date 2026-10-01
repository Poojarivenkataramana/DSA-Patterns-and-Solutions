"""
================================================================================
Problem: Delivery Package Pair (Target Weight Pair)
Pattern: Two Pointers (Opposite Direction)
================================================================================

Scenario: Delivery Package Pair
A delivery company has a sorted list of package weights:
    weights = [5, 10, 15, 20, 25, 30, 35]
Target weight is 45.
Find two package weights whose sum is exactly 45.

Rules:
- Use two pointers (left at start, right at end).
- No nested loops.

Example:
    Input: weights = [5, 10, 15, 20, 25, 30, 35], target = 45
    Output: (10, 35)
    Explanation: 10 + 35 = 45.

Complexity:
- Time Complexity: O(n) - Single pass.
- Space Complexity: O(1) - In-place comparison with O(1) memory.
================================================================================
"""

def find_delivery_pair(weights: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    right = len(weights) - 1

    while left < right:
        current_sum = weights[left] + weights[right]
        if current_sum == target:
            return (weights[left], weights[right])
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return None


if __name__ == "__main__":
    weights = [5, 10, 15, 20, 25, 30, 35]
    target = 45
    pair = find_delivery_pair(weights, target)
    print(f"Package Weights: {weights}")
    print(f"Target Weight: {target}")
    print(f"Found Delivery Pair: {pair}")
