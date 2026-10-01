# Problem 5 - Maximum Number of Positive Days
# For every window of 3 days, count how many values are positive. Return the maximum number of positive days in any window
profits = [-2, 5, 3, -1, 4, 6, -3, 2]
k = 3

# --- 1. Brute Force Approach ---
l = 0
r = k - 1
cur_pos_count = 0
cur_window = profits[l : r + 1]
for value in cur_window:
    if value > 0:
        cur_pos_count += 1
max_pos_count = cur_pos_count
while r < len(profits) - 1:
    l += 1
    r += 1
    curr_window = profits[l : r + 1]
    positive_count = 0
    for value in curr_window:
        if value > 0:
            positive_count += 1
    if positive_count > max_pos_count:
        max_pos_count = positive_count

print("The maximum positive count is:", max_pos_count)

# Brute force complexities:
# Time Complexity : O(n * k)
# Space Complexity : O(1)


# --- 2. Optimized Version (Sliding Window) ---
profits = [-2, 5, 3, -1, 4, 6, -3, 2]
k = 3
l = 0
r = k - 1
cur_pos_count = 0
cur_window = profits[l : r + 1]

for value in cur_window:
    if value > 0:
        cur_pos_count += 1
max_pos_count = cur_pos_count

while r < len(profits) - 1:
    if profits[l] > 0:
        cur_pos_count -= 1
    l += 1
    r += 1

    if profits[r] > 0:
        cur_pos_count += 1
    if cur_pos_count > max_pos_count:
        max_pos_count = cur_pos_count

print("Optimized - The maximum positive count is:", max_pos_count)

# Time and Space Complexities:
# Time Complexity : O(n)
# Space Complexity : O(1)
