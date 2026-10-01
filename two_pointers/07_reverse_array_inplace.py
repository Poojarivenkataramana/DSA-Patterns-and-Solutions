# Day 3 — Problem 3: Reverse a Customer ID
# Scenario: Reverse a Customer ID
# A system receives a list of customer IDs in the wrong order:
# ids = [101, 205, 309, 412, 518, 623]
# Reverse the list in-place using Two Pointers.
# Rules:
# One pointer starts at the beginning.
# One pointer starts at the end.
# Swap the values.
# Move both pointers toward the center.
# Do not use [::-1] or another list.

ids = [101, 205, 309, 412, 518, 623]

left = 0
right = len(ids) - 1

while left < right:
    ids[left], ids[right] = ids[right], ids[left]
    left += 1
    right -= 1

print(ids)

# Time and Space Complexity:
# Time Complexity: O(n) - Single pass with n/2 swaps
# Space Complexity: O(1) - In-place modification without extra list
