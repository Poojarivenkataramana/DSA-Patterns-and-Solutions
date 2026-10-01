# Day 3 — Problem 2: Delivery Pair
# Scenario:
# A delivery company has a sorted list of package weights:
# weights = [5, 10, 15, 20, 25, 30, 35]
# target = 45
# Find two package weights whose sum is exactly 45.
# Use:
# Two pointers
# left at the beginning
# right at the end
# No nested loops

weights = [5, 10, 15, 20, 25, 30, 35]
target = 45
left = 0
right = len(weights) - 1

while left < right:
    if weights[left] + weights[right] == target:
        print((weights[left], weights[right]))
        break
    elif weights[left] + weights[right] > target:
        right -= 1
    elif weights[left] + weights[right] < target:
        left += 1

# Time and Space Complexity:
# Time Complexity: O(n) - Single pass with two pointers
# Space Complexity: O(1) - Constant auxiliary space
