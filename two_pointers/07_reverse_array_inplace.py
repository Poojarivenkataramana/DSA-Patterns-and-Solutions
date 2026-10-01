"""
================================================================================
Problem: Reverse an Array / List In-Place
Pattern: Two Pointers (Opposite Direction - Swapping)
LeetCode: LC 344 - Reverse String (Array Equivalent)
================================================================================

Scenario: Reverse Customer IDs
A system receives a list of customer IDs in the wrong order:
    ids = [101, 205, 309, 412, 518, 623]
Reverse the list in-place using Two Pointers.

Rules:
- One pointer starts at the beginning (left = 0).
- One pointer starts at the end (right = len(ids) - 1).
- Swap the values at the two pointers.
- Move both pointers toward the center (left += 1, right -= 1).
- Do not use [::-1] or an auxiliary list.

Example:
    Input: ids = [101, 205, 309, 412, 518, 623]
    Output: [623, 518, 412, 309, 205, 101]

Complexity:
- Time Complexity: O(n) - Visits each element at most once (n/2 swaps).
- Space Complexity: O(1) - In-place modification.
================================================================================
"""

def reverse_array_inplace(arr: list) -> list:
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    ids = [101, 205, 309, 412, 518, 623]
    print(f"Original IDs: {ids}")
    reverse_array_inplace(ids)
    print(f"Reversed IDs: {ids}")
