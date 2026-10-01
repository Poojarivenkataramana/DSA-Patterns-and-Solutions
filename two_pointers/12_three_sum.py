"""
================================================================================
Problem: 3Sum / Three-Item Budget Match
Pattern: Fixed Pointer + Two Pointers (Opposite Direction)
LeetCode: LC 15 - 3Sum
================================================================================

Scenario 1: Three-Item Budget Match
A shopping system has sorted item prices:
    prices = [-4, -1, 0, 1, 2, 5]
Find three items whose total price is 0 (e.g., [-1, 0, 1] and [-4, -1, 5]).

Scenario 2: Classic Unique 3Sum Problem
Given an integer array nums, return all the unique triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Approach (Sort + Fixed Pointer + Two Pointers):
1. Sort the array in non-decreasing order: nums.sort().
2. Iterate `fixed` index from 0 to len(nums) - 3:
   - Duplicate Avoidance (Fixed): If fixed > 0 and nums[fixed] == nums[fixed - 1], skip it!
   - Initialize two pointers: left = fixed + 1, right = len(nums) - 1.
   - While left < right:
     * total = nums[fixed] + nums[left] + nums[right]
     * If total == 0:
         Append [nums[fixed], nums[left], nums[right]] to results.
         Skip duplicate left values: while left < right and nums[left] == nums[left + 1]: left += 1
         Skip duplicate right values: while left < right and nums[right] == nums[right - 1]: right -= 1
         Move both pointers: left += 1, right -= 1
     * If total < 0:
         Sum is too small -> left += 1
     * If total > 0:
         Sum is too large -> right -= 1
3. Return results.

Complexity:
- Time Complexity: O(n^2) - O(n log n) sorting + O(n^2) two-pointer exploration.
- Space Complexity: O(1) or O(n) depending on sort implementation (excluding output list).
================================================================================
"""

def three_sum_budget_match(prices: list[int]) -> list[list[int]]:
    """Finds all zero-sum triplets from an already sorted list of prices."""
    result = []
    for f in range(len(prices)):
        left = f + 1
        right = len(prices) - 1

        while left < right:
            total = prices[f] + prices[left] + prices[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                result.append([prices[f], prices[left], prices[right]])
                left += 1
                right -= 1

    return result


def three_sum_unique(nums: list[int]) -> list[list[int]]:
    """Finds all UNIQUE zero-sum triplets with duplicate handling (LeetCode 15)."""
    nums.sort()
    result = []

    for fixed in range(len(nums) - 2):
        # Skip duplicate fixed values
        if fixed > 0 and nums[fixed] == nums[fixed - 1]:
            continue

        left = fixed + 1
        right = len(nums) - 1

        while left < right:
            total = nums[fixed] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[fixed], nums[left], nums[right]])

                # Skip duplicate left elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate right elements
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == "__main__":
    # Test Budget Match
    prices = [-4, -1, 0, 1, 2, 5]
    print(f"Prices: {prices}")
    print(f"Zero-Sum Triplets: {three_sum_budget_match(prices)}\n")

    # Test Unique 3Sum
    nums = [-1, 0, 1, 2, -1, -4]
    print(f"Unsorted Numbers: {nums}")
    print(f"Unique 3Sum Triplets: {three_sum_unique(nums)}")
