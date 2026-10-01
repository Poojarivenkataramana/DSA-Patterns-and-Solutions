"""
================================================================================
Problem: Customer Purchase Pair (Target Sum Pair)
Pattern: Two Pointers (Opposite Direction)
================================================================================

Scenario: Customer Purchase Pair
A company has a sorted list of purchase amounts:
    amounts = [10, 20, 30, 40, 50, 60, 70]
The required total is target = 90.
Find two purchase amounts whose sum equals the target.

Rules:
- Use two pointers.
- One starts from the beginning (left = 0).
- One starts from the end (right = len(amounts) - 1).
- No nested loops.

Example:
    Input: amounts = [10, 20, 30, 40, 50, 60, 70], target = 90
    Output: (20, 70)
    Explanation: 20 + 70 = 90.

Complexity:
- Time Complexity: O(n) - Single linear scan using two pointers.
- Space Complexity: O(1) - Constant space.
================================================================================
"""

def find_purchase_pair(amounts: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    right = len(amounts) - 1

    while left < right:
        current_sum = amounts[left] + amounts[right]
        if current_sum == target:
            return (amounts[left], amounts[right])
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return None


if __name__ == "__main__":
    amounts = [10, 20, 30, 40, 50, 60, 70]
    target = 90
    pair = find_purchase_pair(amounts, target)
    print(f"Purchase Amounts: {amounts}")
    print(f"Target Total: {target}")
    print(f"Found Purchase Pair: {pair}")
