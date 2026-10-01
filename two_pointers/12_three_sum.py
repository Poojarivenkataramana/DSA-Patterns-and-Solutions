# Day 4 — Problem 4: Three-Item Budget Match
# Scenario:
# A shopping system has sorted item prices:
# prices = [-4, -1, 0, 1, 2, 5]
# The system wants to find three different items whose total price is 0.
# For example:
# -1 + 0 + 1 = 0
# -4 +  -1 + 5 = 0
# New pattern 🧠
# This time we'll combine:
# One fixed pointer + two pointers
# fixed →   left →       ← right
# For each fixed element, use two pointers to find the remaining two values.
# Rules:
# Array is sorted.
# Don't use three nested loops.
# Don't use set() for the main search.
# Return all valid triplets.

# --- Part 1: Three-Item Budget Match ---
values = [-4, -1, 0, 1, 2, 5]
for f in range(len(values)):
    left = f + 1
    right = len(values) - 1
    while left < right:
        if values[f] + values[left] + values[right] > 0:
            right -= 1
        elif values[f] + values[left] + values[right] < 0:
            left += 1
        elif values[f] + values[left] + values[right] == 0:
            print([values[f], values[left], values[right]])
            left += 1
            right -= 1


# --- Part 2: Unique 3Sum (Handling Duplicates) ---
# three_sum()
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
result = []

# now we need to initialize the loop for picking first fixed number
for fixed in range(len(nums) - 2):
    # we checking now if fixed number is comes again like duplicate
    if fixed > 0 and nums[fixed] == nums[fixed - 1]:
        continue

    left = fixed + 1
    right = len(nums) - 1

    while left < right:
        total = nums[fixed] + nums[left] + nums[right]

        if total == 0:
            result.append([nums[fixed], nums[left], nums[right]])
            # checking left is already used that value or not if used then we skip it
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            # checking right is already used that value or not if used then we skip it
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            # after checking those loop conditions we move both pointers
            left += 1
            right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

print(result)

# Time & Space Complexity:
# Time Complexity: O(n^2) - O(n log n) for sorting + O(n^2) for fixed pointer and two-pointer traversal
# Space Complexity: O(1) - Constant auxiliary space (excluding the output list)
