"""
================================================================================
Problem: Squares of a Sorted Array / Sorted Squared Values
Pattern: Two Pointers (Converging Pointers Filling Array from Back)
LeetCode: LC 977 - Squares of a Sorted Array
================================================================================

Scenario: Sensor Sorted Squared Values
A sensor records values that can be negative or positive. The values are already sorted:
    values = [-8, -3, -1, 2, 4, 7]
Create a new list containing their squares in non-decreasing sorted order:
    [1, 4, 9, 16, 49, 64]

Important Twist:
- Do NOT square everything and then call sort() (which would take O(n log n)).
- Use Two Pointers to achieve O(n) linear time.

Why Two Pointers?
Because the input array is already sorted, the largest squared numbers must originate 
either from the most negative numbers on the far left or the largest positive numbers 
on the far right.

Approach:
1. Initialize `left = 0`, `right = len(values) - 1`.
2. Allocate result array of size n, initialize placement pointer `p = n - 1`.
3. While left <= right:
   - If values[left] ** 2 > values[right] ** 2:
       result[p] = values[left] ** 2
       left += 1
   - Else:
       result[p] = values[right] ** 2
       right -= 1
   - Decrement p.
4. Return result.

Complexity:
- Time Complexity: O(n) - Single pass over the input.
- Space Complexity: O(n) - For storing the resulting sorted squares.
================================================================================
"""

def sorted_squares(values: list[int]) -> list[int]:
    left = 0
    right = len(values) - 1
    result = [0] * len(values)
    p = len(result) - 1

    while left <= right:
        left_sq = values[left] ** 2
        right_sq = values[right] ** 2

        if left_sq > right_sq:
            result[p] = left_sq
            left += 1
        else:
            result[p] = right_sq
            right -= 1
        p -= 1

    return result


if __name__ == "__main__":
    values = [-8, -3, -1, 2, 4, 7]
    ans = sorted_squares(values)
    print(f"Original Values: {values}")
    print(f"Sorted Squares : {ans}")
