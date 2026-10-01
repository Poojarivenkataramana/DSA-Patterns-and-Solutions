# Practice 6 — Maximum number of even values
# You are analyzing daily transaction IDs:
# transactions = [12, 7, 4, 9, 10, 15, 8, 6]
# k = 3

# For every consecutive 3-day window, find how many transaction IDs are even, and return the maximum number of even IDs in any window.

# For example, first window:
# [12, 7, 4]
# Even values:
# 12 ✅
# 7  ❌
# 4  ✅
# So count = 2.

# --- 1. Brute Force Approach ---
transactions = [12, 7, 4, 9, 10, 15, 8, 6]
k = 3

l = 0
r = k - 1
current_window = transactions[l : r + 1]

even_count = 0

for value in current_window:
    if value % 2 == 0:
        even_count += 1
max_even_count = even_count

while r < len(transactions) - 1:
    r += 1
    l += 1
    curr_window = transactions[l : r + 1]
    even_count = 0
    for value in curr_window:
        if value % 2 == 0:
            even_count += 1

    if even_count > max_even_count:
        max_even_count = even_count

print("The maximum window even count is:", max_even_count)


# --- 2. Optimized Solution (Sliding Window) ---
transactions = [12, 7, 4, 9, 10, 15, 8, 6]
k = 3

l = 0
r = k - 1
current_window = transactions[l : r + 1]

even_count = 0

for value in current_window:
    if value % 2 == 0:
        even_count += 1
max_even_count = even_count

while r < len(transactions) - 1:
    if transactions[l] % 2 == 0:
        even_count -= 1
    l += 1
    r += 1
    if transactions[r] % 2 == 0:
        even_count += 1

    if even_count > max_even_count:
        max_even_count = even_count

print("Optimized - The maximum window even count is:", max_even_count)

# Time & Space Complexity:
# Time Complexity: O(n)
# Space Complexity: O(1)
