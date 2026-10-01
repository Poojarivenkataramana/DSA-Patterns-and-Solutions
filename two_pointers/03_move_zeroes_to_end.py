"""
================================================================================
Problem: Move Zeroes to End (Payment Processing Clean-up)
Pattern: Two Pointers (Fast & Slow Pointers / Partitioning)
LeetCode: LC 283 - Move Zeroes
================================================================================

Scenario: Payment Processing System
A payment system stores transaction values:
    transactions = [0, 150, 0, 200, 350, 0, 500]
Here:
- 0 = failed/empty transaction
- Non-zero = valid transaction

Move all valid transactions to the beginning and all 0s to the end in-place 
while maintaining the relative order of non-zero elements.

Rules:
- Modify array in-place.
- Do not create another array.
- Do not use remove() or sort().
- Use Two Pointers.

Example:
    Input: transactions = [0, 150, 0, 200, 350, 0, 500]
    Output: [150, 200, 350, 500, 0, 0, 0]

Approach (Fast & Slow Pointer Swap):
1. Initialize `s` (slow pointer for placing next non-zero) and `f` (fast pointer for scanning) at index 0.
2. If transactions[f] == 0:
     Move `f` forward to find a non-zero element.
3. If transactions[f] != 0:
     Swap transactions[s] and transactions[f].
     Increment both `s` and `f`.
4. Continue until `f` reaches the end.

Complexity:
- Time Complexity: O(n) - Single pass through the array.
- Space Complexity: O(1) - In-place modification without extra memory.
================================================================================
"""

def move_zeroes_to_end(transactions: list[int]) -> list[int]:
    s = 0  # slow pointer: marks the position for the next non-zero element
    f = 0  # fast pointer: scans for non-zero elements

    while f < len(transactions):
        if transactions[f] != 0:
            transactions[s], transactions[f] = transactions[f], transactions[s]
            s += 1
        f += 1

    return transactions


if __name__ == "__main__":
    transactions = [0, 150, 0, 200, 350, 0, 500]
    print(f"Before: {transactions}")
    move_zeroes_to_end(transactions)
    print(f"After : {transactions}")
