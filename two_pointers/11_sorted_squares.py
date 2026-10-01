# Day 4 — Problem 3: Sorted Squared Values
# Scenario:
# A sensor records values that can be negative or positive. The values are already sorted:
# values = [-8, -3, -1, 2, 4, 7]
# We need to create a new list containing their squares in sorted order:
# [1, 4, 9, 16, 49, 64]
# Important twist 🧠
# Don't square everything and then call sort().
# Use Two Pointers.
# Why? The largest square can come from either:
# the largest positive at the right, or
# the most negative at the left.

values = [-8, -3, -1, 2, 4, 7]
left = 0
right = len(values) - 1

result = [0] * len(values)
p = len(result) - 1

while left <= right:
    if values[left] ** 2 > values[right] ** 2:
        result[p] = values[left] ** 2
        p -= 1
        left += 1
    elif values[left] ** 2 < values[right] ** 2:
        result[p] = values[right] ** 2
        p -= 1
        right -= 1
    else:
        result[p] = values[right] ** 2
        right -= 1
        left += 1
        p -= 1

print(result)

# Time and Space Complexity:
# Time Complexity: O(n) - Single pass filling result from back
# Space Complexity: O(n) - Output array of size n
