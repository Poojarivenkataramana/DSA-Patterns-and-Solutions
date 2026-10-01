"""
================================================================================
Problem: Maximum Number of Even Transaction IDs in Any K-Day Window
Pattern: Sliding Window (Fixed Size - State Tracking)
================================================================================

Problem Statement:
You are analyzing daily transaction IDs:
    transactions = [12, 7, 4, 9, 10, 15, 8, 6], k = 3

For every consecutive k-day window, count how many transaction IDs are even,
and return the maximum number of even IDs found in any window.

Example:
    Input: transactions = [12, 7, 4, 9, 10, 15, 8, 6], k = 3
    Output: 2
    Explanation:
        Window [12, 7, 4]  -> Evens: 12, 4  -> Count = 2
        Window [7, 4, 9]   -> Evens: 4      -> Count = 1
        Window [4, 9, 10]  -> Evens: 4, 10  -> Count = 2
        Window [9, 10, 15] -> Evens: 10     -> Count = 1
        Window [10, 15, 8] -> Evens: 10, 8  -> Count = 2
        Window [15, 8, 6]  -> Evens: 8, 6   -> Count = 2
        Maximum even count = 2.

Approaches:
1. Brute Force Approach:
   - For every window of size k, scan all k elements and count even numbers.
   - Time Complexity: O(n * k), Space Complexity: O(1)

2. Optimized Sliding Window:
   - Count even elements in the first window of size k.
   - For each step moving forward:
     * If the leaving element (transactions[l]) is even, count -= 1.
     * Advance l and r.
     * If the entering element (transactions[r]) is even, count += 1.
     * Update max_even_count = max(max_even_count, even_count).
   - Time Complexity: O(n), Space Complexity: O(1)
================================================================================
"""

def max_even_ids_brute_force(transactions: list[int], k: int) -> int:
    """Brute force approach: O(n * k) time."""
    if not transactions or k <= 0 or k > len(transactions):
        return 0

    max_even_count = 0
    for i in range(len(transactions) - k + 1):
        curr_window = transactions[i : i + k]
        even_count = sum(1 for x in curr_window if x % 2 == 0)
        if even_count > max_even_count:
            max_even_count = even_count

    return max_even_count


def max_even_ids_optimized(transactions: list[int], k: int) -> int:
    """Optimized Sliding Window: O(n) time, O(1) space."""
    if not transactions or k <= 0 or k > len(transactions):
        return 0

    l = 0
    r = k - 1

    # Count evens in the initial window
    even_count = sum(1 for val in transactions[l : r + 1] if val % 2 == 0)
    max_even_count = even_count

    # Slide window
    while r < len(transactions) - 1:
        if transactions[l] % 2 == 0:
            even_count -= 1
        l += 1
        r += 1

        if transactions[r] % 2 == 0:
            even_count += 1

        if even_count > max_even_count:
            max_even_count = even_count

    return max_even_count


if __name__ == "__main__":
    transactions = [12, 7, 4, 9, 10, 15, 8, 6]
    k = 3

    print(f"Transactions: {transactions}")
    print(f"Window Size (k): {k}\n")

    bf_result = max_even_ids_brute_force(transactions, k)
    print(f"[Brute Force O(n*k)] Max even IDs count: {bf_result}")

    opt_result = max_even_ids_optimized(transactions, k)
    print(f"[Optimized O(n)]    Max even IDs count: {opt_result}")
