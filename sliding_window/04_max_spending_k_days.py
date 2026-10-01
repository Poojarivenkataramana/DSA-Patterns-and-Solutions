"""
================================================================================
Problem: Best Customer Spending Period (Max Spending Over K Days)
Pattern: Sliding Window (Fixed Size)
LeetCode Equivalent: Sliding Window Max Subarray Sum
================================================================================

Problem Statement:
Find the maximum customer spending amount over any 4 consecutive days.

Example:
    Input: spending = [120, 80, 150, 200, 90, 170, 130, 110], k = 4
    Output: 610
    Explanation:
        Window [120, 80, 150, 200] -> sum = 550
        Window [80, 150, 200, 90]  -> sum = 520
        Window [150, 200, 90, 170] -> sum = 610 (Maximum)
        Window [200, 90, 170, 130] -> sum = 590
        Window [90, 170, 130, 110] -> sum = 500

Approach (Fixed-size Sliding Window):
1. Compute the sum of the first k spending entries.
2. Initialize max_spent with this sum.
3. Slide the window:
   - Subtract spending[l], increment l and r, add spending[r].
   - Update max_spent if cur_win_sum > max_spent.
4. Return max_spent.

Complexity:
- Time Complexity: O(n) - Single pass through the array.
- Space Complexity: O(1) - Constant auxiliary space.
================================================================================
"""

def max_spending_k_days(spending: list[int], k: int) -> int:
    if not spending or k <= 0 or k > len(spending):
        return 0

    l = 0
    r = k - 1
    cur_win_sum = sum(spending[l : r + 1])
    max_spent = cur_win_sum

    while r < len(spending) - 1:
        cur_win_sum -= spending[l]
        l += 1
        r += 1
        cur_win_sum += spending[r]

        if cur_win_sum > max_spent:
            max_spent = cur_win_sum

    return max_spent


if __name__ == "__main__":
    spending = [120, 80, 150, 200, 90, 170, 130, 110]
    k = 4
    result = max_spending_k_days(spending, k)
    print(f"Daily Spending: {spending}")
    print(f"Window Size (k): {k}")
    print(f"The maximum spending over {k} consecutive days is: {result}")
