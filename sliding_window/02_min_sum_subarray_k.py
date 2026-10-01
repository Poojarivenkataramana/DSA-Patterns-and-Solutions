"""
================================================================================
Problem: Minimum Temperature Sum in Any K Consecutive Days (Min Sum Subarray)
Pattern: Sliding Window (Fixed Size)
LeetCode Equivalent: Sliding Window Min Subarray Sum
================================================================================

Problem Statement:
Find the minimum sum of recorded temperatures in any 3 consecutive days.

Example:
    Input: temperatures = [32, 28, 30, 25, 27, 29, 31], k = 3
    Output: 81
    Explanation: The window [25, 27, 29] gives the minimum sum: 25 + 27 + 29 = 81.

Approach (Fixed-size Sliding Window):
1. Compute the sum of the first k temperatures [0 to k-1].
2. Set min_temps to this initial sum.
3. Slide the window one step at a time:
   - Subtract the temperature leaving from the left (temperatures[l]).
   - Increment pointers l and r.
   - Add the temperature entering from the right (temperatures[r]).
   - Update min_temps if the current window sum is lower.
4. Return min_temps.

Complexity:
- Time Complexity: O(n) - Single pass over the array.
- Space Complexity: O(1) - Constant auxiliary space.
================================================================================
"""

def min_temp_k_days(temperatures: list[int], k: int) -> int:
    if not temperatures or k <= 0 or k > len(temperatures):
        return 0

    # Step 1: Initialize window boundaries
    l = 0
    r = k - 1

    # Step 2: Sum of first window
    curr_temps = sum(temperatures[l : r + 1])
    min_temps = curr_temps

    # Step 3: Slide window to the end
    while r < len(temperatures) - 1:
        curr_temps -= temperatures[l]
        l += 1
        r += 1
        curr_temps += temperatures[r]

        if curr_temps < min_temps:
            min_temps = curr_temps

    return min_temps


if __name__ == "__main__":
    temperatures = [32, 28, 30, 25, 27, 29, 31]
    k = 3
    result = min_temp_k_days(temperatures, k)
    print(f"Temperatures: {temperatures}")
    print(f"Window Size (k): {k}")
    print(f"The minimum sum of temperatures in {k} consecutive days is: {result}")
