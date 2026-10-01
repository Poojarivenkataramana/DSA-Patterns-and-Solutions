"""
================================================================================
Problem: Maximum Total Sales in Any K Consecutive Days (Max Sum Subarray)
Pattern: Sliding Window (Fixed Size)
LeetCode Equivalent: LC 643 - Maximum Average Subarray I (Variant)
================================================================================

Problem Statement:
Given a list of daily sales figures and a window size k, find the maximum total sales 
in any k consecutive days.

Example:
    Input: sales = [12, 8, 15, 20, 7, 18, 10], k = 3
    Output: 45
    Explanation: The window [20, 7, 18] gives the maximum sum: 20 + 7 + 18 = 45.

Approach (Fixed-size Sliding Window):
1. Calculate the sum of the first k elements (initial window from index 0 to k-1).
2. Set max_sales = initial window sum.
3. Slide the window one position to the right at each step:
   - Subtract the element leaving the window (sales[l]).
   - Increment left and right pointers (l += 1, r += 1).
   - Add the new element entering the window (sales[r]).
   - Update max_sales if the current window sum is greater.
4. Return max_sales.

Complexity:
- Time Complexity: O(n) - We traverse the array once.
- Space Complexity: O(1) - Constant auxiliary memory.
================================================================================
"""

def max_sales_k_days(sales: list[int], k: int) -> int:
    if not sales or k <= 0 or k > len(sales):
        return 0

    # Step 1: Initialize the starting and ending window boundaries
    l = 0
    r = k - 1

    # Step 2: Calculate the sum of the first window
    curr_win = sum(sales[l : r + 1])
    max_sales = curr_win

    # Step 3: Slide the window across the array
    while r < len(sales) - 1:
        curr_win -= sales[l]  # Remove left element
        l += 1
        r += 1                # Move right boundary
        curr_win += sales[r]  # Add new right element

        if curr_win > max_sales:
            max_sales = curr_win

    return max_sales


if __name__ == "__main__":
    sales = [12, 8, 15, 20, 7, 18, 10]
    k = 3
    result = max_sales_k_days(sales, k)
    print(f"Sales Data: {sales}")
    print(f"Window Size (k): {k}")
    print(f"The maximum sales of {k} consecutive days is: {result}")
