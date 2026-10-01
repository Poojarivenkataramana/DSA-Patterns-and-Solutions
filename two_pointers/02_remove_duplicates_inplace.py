"""
================================================================================
Problem: Remove Duplicates from Sorted Array In-Place
Pattern: Two Pointers (Fast & Slow Pointers - Same Direction)
LeetCode: LC 26 - Remove Duplicates from Sorted Array
================================================================================

Scenario: Customer IDs Cleanup
A company receives customer IDs in sorted order from its database:
    ids = [1, 1, 2, 2, 2, 3, 4, 4, 5]
Because of a data-processing issue, some customer IDs appear multiple times.
Remove duplicates in-place so that every customer ID appears only once at the 
beginning of the array.

Constraints:
- The array is already sorted.
- Modify the existing array in-place.
- Do NOT create another array.
- Do NOT use set() or dict.
- Use Two Pointers.

Example:
    Input: ids = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    Output: [1, 2, 3, 4, 5] with length 5.

Approach (Fast & Slow Pointer):
1. `slow` pointer keeps track of the last unique element placed (starts at 0).
2. `fast` pointer scans through the array (starts at 1).
3. If ids[fast] == ids[slow]:
     It's a duplicate; advance `fast`.
4. If ids[fast] != ids[slow]:
     Found a new unique element:
     - Increment `slow` (slow += 1).
     - Overwrite ids[slow] with ids[fast].
     - Increment `fast` (fast += 1).
5. Return the number of unique elements (slow + 1).

Complexity:
- Time Complexity: O(n) - Fast pointer scans the list once.
- Space Complexity: O(1) - Modifies array in-place with zero extra memory.
================================================================================
"""

def remove_duplicates_inplace(ids: list[int]) -> int:
    if not ids:
        return 0

    slow = 0
    fast = 1

    while fast < len(ids):
        if ids[fast] != ids[slow]:
            slow += 1
            ids[slow] = ids[fast]
        fast += 1

    return slow + 1


if __name__ == "__main__":
    ids = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print(f"Original IDs: {ids}")
    k = remove_duplicates_inplace(ids)
    print(f"Unique Count: {k}")
    print(f"Array after in-place modification: {ids[:k]}")
