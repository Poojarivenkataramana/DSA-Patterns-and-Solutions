"""
================================================================================
Problem: Count High-Activity Periods (Subarrays with Sum >= Threshold)
Pattern: Sliding Window (Fixed Size with Condition)
LeetCode Equivalent: Sliding Window Subarray Counting
================================================================================

Problem Statement:
Count how many windows of k consecutive days have a total activity sum >= threshold.

Example:
    Input: activity = [4, 7, 2, 9, 6, 3, 8, 5], k = 3, threshold = 17
    Output: 3
    Explanation:
        Window [4, 7, 2] -> sum = 13 (No)
        Window [7, 2, 9] -> sum = 18 >= 17 (Yes, count = 1)
        Window [2, 9, 6] -> sum = 17 >= 17 (Yes, count = 2)
        Window [9, 6, 3] -> sum = 18 >= 17 (Yes, count = 3)
        Window [6, 3, 8] -> sum = 17 >= 17 (Yes, count = 4)
        Window [3, 8, 5] -> sum = 16 (No)
        Total matching windows: 4

Approach (Fixed-size Sliding Window):
1. Compute the initial window sum of the first k days.
2. Initialize window_count = 0.
3. Check the first window against the threshold: if cur_sum >= threshold: window_count += 1.
4. Loop through the remaining elements, sliding the window:
   - Subtract activity[l], increment l.
   - Increment r, add activity[r].
   - If cur_sum >= threshold, increment window_count.
5. Return window_count.

Complexity:
- Time Complexity: O(n) - Single pass over the array.
- Space Complexity: O(1) - Constant auxiliary space.
================================================================================
"""

def count_high_activity_windows(activity: list[int], k: int, threshold: int) -> int:
    if not activity or k <= 0 or k > len(activity):
        return 0

    l = 0
    r = k - 1
    cur_sum = sum(activity[l : r + 1])
    window_count = 0

    # Check the initial window
    if cur_sum >= threshold:
        window_count += 1

    # Slide window through the remaining elements
    while r < len(activity) - 1:
        cur_sum -= activity[l]
        l += 1
        r += 1
        cur_sum += activity[r]

        if cur_sum >= threshold:
            window_count += 1

    return window_count


if __name__ == "__main__":
    activity = [4, 7, 2, 9, 6, 3, 8, 5]
    k = 3
    threshold = 17
    result = count_high_activity_windows(activity, k, threshold)
    print(f"Activity Data: {activity}")
    print(f"Window Size (k): {k}, Threshold: {threshold}")
    print(f"Number of high-activity periods (sum >= {threshold}): {result}")
