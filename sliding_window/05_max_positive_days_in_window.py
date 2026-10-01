"""
================================================================================
Problem: Maximum Number of Positive Days in Any K-Day Window
Pattern: Sliding Window (Fixed Size - State Tracking)
================================================================================

Problem Statement:
Given an array representing daily profits (positive or negative) and a window 
size k, find the maximum number of positive profit days in any window of k 
consecutive days.

Example:
    Input: profits = [-2, 5, 3, -1, 4, 6, -3, 2], k = 3
    Output: 2
    Explanation:
        Window 1: [-2, 5, 3] -> 2 positive days
        Window 2: [5, 3, -1] -> 2 positive days
        Window 3: [3, -1, 4] -> 2 positive days
        Window 4: [-1, 4, 6] -> 2 positive days
        Window 5: [4, 6, -3] -> 2 positive days
        Window 6: [6, -3, 2] -> 2 positive days
        Maximum positive count in any 3-day window = 2.

Approaches:
1. Brute Force Approach:
   - For every subarray of size k, iterate through all k elements and count positive values.
   - Time Complexity: O(n * k), Space Complexity: O(1)

2. Optimized Sliding Window:
   - Count positive numbers in the first window of size k.
   - For subsequent windows:
     * If the leaving element (profits[l]) is positive, decrement count.
     * Increment l and r.
     * If the entering element (profits[r]) is positive, increment count.
     * Update max_pos_count = max(max_pos_count, cur_pos_count).
   - Time Complexity: O(n), Space Complexity: O(1)
================================================================================
"""

def max_positive_days_brute_force(profits: list[int], k: int) -> int:
    """Brute force approach: O(n * k) time."""
    if not profits or k <= 0 or k > len(profits):
        return 0

    max_pos_count = 0
    for i in range(len(profits) - k + 1):
        cur_window = profits[i : i + k]
        cur_pos_count = sum(1 for x in cur_window if x > 0)
        if cur_pos_count > max_pos_count:
            max_pos_count = cur_pos_count

    return max_pos_count


def max_positive_days_optimized(profits: list[int], k: int) -> int:
    """Optimized Sliding Window: O(n) time, O(1) space."""
    if not profits or k <= 0 or k > len(profits):
        return 0

    l = 0
    r = k - 1

    # Count positives in the first window
    cur_pos_count = sum(1 for val in profits[l : r + 1] if val > 0)
    max_pos_count = cur_pos_count

    # Slide the window
    while r < len(profits) - 1:
        if profits[l] > 0:
            cur_pos_count -= 1
        l += 1
        r += 1

        if profits[r] > 0:
            cur_pos_count += 1

        if cur_pos_count > max_pos_count:
            max_pos_count = cur_pos_count

    return max_pos_count


if __name__ == "__main__":
    profits = [-2, 5, 3, -1, 4, 6, -3, 2]
    k = 3

    print(f"Profits Data: {profits}")
    print(f"Window Size (k): {k}\n")

    bf_result = max_positive_days_brute_force(profits, k)
    print(f"[Brute Force O(n*k)] Max positive days: {bf_result}")

    opt_result = max_positive_days_optimized(profits, k)
    print(f"[Optimized O(n)]    Max positive days: {opt_result}")
