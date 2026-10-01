"""
================================================================================
Problem: Two Sum II - Input Array Is Sorted
Pattern: Two Pointers (Opposite Direction / Converging)
LeetCode: LC 167 - Two Sum II - Input Array Is Sorted
================================================================================

Problem Statement:
Given a 1-indexed (or 0-indexed) array of integers that is already sorted in 
non-decreasing order, find two numbers such that they add up to a specific target number.

Example:
    Input: arr = [2, 4, 5, 7, 9, 11, 15], target = 16
    Output: (5, 11)
    Explanation: 5 + 11 = 16.

Approach (Opposite Direction Two Pointers):
1. Place left pointer at index 0 and right pointer at len(arr) - 1.
2. Calculate current_sum = arr[left] + arr[right].
3. If current_sum == target:
     Found the pair, return (arr[left], arr[right]).
4. If current_sum > target:
     The sum is too large; decrement right pointer (move leftward to smaller numbers).
5. If current_sum < target:
     The sum is too small; increment left pointer (move rightward to larger numbers).
6. Repeat until left >= right.

Complexity:
- Time Complexity: O(n) - Single pass with converging pointers.
- Space Complexity: O(1) - Constant auxiliary space (no hash map needed).
================================================================================
"""

def two_sum_sorted(arr: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum > target:
            right -= 1
        else:
            left += 1

    return None


if __name__ == "__main__":
    arr = [2, 4, 5, 7, 9, 11, 15]
    target = 16
    result = two_sum_sorted(arr, target)
    print(f"Sorted Array: {arr}")
    print(f"Target Sum: {target}")
    print(f"Resulting Pair: {result}")
