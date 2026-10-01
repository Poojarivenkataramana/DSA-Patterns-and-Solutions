# 🎯 Scenario 1 — Customer IDs
# A company receives customer IDs in sorted order from its database:
# ids = [1, 1, 2, 2, 2, 3, 4, 4, 5]
# Because of a data-processing issue, some customer IDs appear multiple times.
# You need to remove the duplicates in-place so that every customer ID appears only once at the beginning of the array.
# Expected:
# [1, 2, 3, 4, 5, ...]

# Constraints
# The array is already sorted.
# Modify the existing array.
# Don't create another array.
# Don't use set().
# Don't use dict.
# Use Two Pointers.

# Two Pointer approach : I use fast and slow pointers in same direction. one is for scanning and another one is takes unique elements
ids = [1, 1, 2, 2, 2, 3, 4, 4, 5]

fast = 1
slow = 0

while fast < len(ids):
    if ids[fast] == ids[slow]:
        fast += 1
    elif ids[fast] != ids[slow]:
        slow += 1
        ids[slow] = ids[fast]
        fast += 1

print(ids[:slow + 1])

# Time and Space Complexity:
# Time Complexity: O(n) - Fast pointer scans the array once
# Space Complexity: O(1) - Modifies array in-place without extra space
