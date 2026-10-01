"""
================================================================================
Problem: Maximum Daily Sales Window Sum (Sliding Window Intro)
Pattern: Sliding Window (Fixed Size)
LeetCode Equivalent: LC 643 - Maximum Average Subarray I
================================================================================

Problem Statement:
A shop records sales for 7 consecutive days:
    sales = [10, 20, 30, 40, 50, 60, 70]
Find the maximum total sales in any window of k = 3 consecutive days.

Example:
    Input: sales = [10, 20, 30, 40, 50, 60, 70], k = 3
    Output: 180
    Explanation: The last window [50, 60, 70] produces the maximum sum: 50 + 60 + 70 = 180.

Approach (Fixed-size Sliding Window):
1. Initialize left pointer at 0, right pointer at k - 1.
2. Calculate current_window_sum = sum(sales[left : right + 1]).
3. Set max_window_sum = current_window_sum.
4. While right < len(sales) - 1:
   - Subtract sales[left] from current_window_sum.
   - Advance left pointer by 1.
   - Advance right pointer by 1.
   - Add sales[right] to current_window_sum.
   - If current_window_sum > max_window_sum, update max_window_sum.
5. Return max_window_sum.

Complexity:
- Time Complexity: O(n) - Single pass through the array.
- Space Complexity: O(1) - Constant memory.
================================================================================
"""

def max_daily_sales_window(sales: list[int], k: int) -> int:
    if not sales or k <= 0 or k > len(sales):
        return 0

    left = 0
    right = k - 1

    current_window_sum = sum(sales[left : right + 1])
    max_window_sum = current_window_sum

    while right < len(sales) - 1:
        current_window_sum -= sales[left]
        left += 1
        right += 1
        current_window_sum += sales[right]

        if current_window_sum > max_window_sum:
            max_window_sum = current_window_sum

    return max_window_sum


if __name__ == "__main__":
    sales = [10, 20, 30, 40, 50, 60, 70]
    k = 3
    result = max_daily_sales_window(sales, k)
    print(f"Sales Records: {sales}")
    print(f"Window Size (k): {k}")
    print(f"Maximum Window Sum: {result}")
