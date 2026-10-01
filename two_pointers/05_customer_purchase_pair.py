# Day 3 — Two Pointers
# 🎯 Scenario: Customer Purchase Pair
# A company has a sorted list of purchase amounts:
# amounts = [10, 20, 30, 40, 50, 60, 70]
# The required total is:
# target = 90
# We need to find two purchase amounts whose sum equals the target.
# Rules:
# Use two pointers
# One starts from the beginning
# One starts from the end
# No nested loops

amounts = [10, 20, 30, 40, 50, 60, 70]
target = 90
left = 0
right = len(amounts) - 1

while left < right:
    if amounts[left] + amounts[right] == target:
        print((amounts[left], amounts[right]))
        break
    elif amounts[left] + amounts[right] > target:
        right -= 1
    else:
        left += 1

# Time and Space Complexity:
# Time Complexity: O(n) - Single pass with two pointers
# Space Complexity: O(1) - Constant auxiliary space
