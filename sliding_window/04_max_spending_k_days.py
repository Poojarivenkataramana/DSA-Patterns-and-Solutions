# Problem 4 - Best Customer Spending Period
# Find the maximum spending over any 4 consecutive days.
spending = [120, 80, 150, 200, 90, 170, 130, 110]
k = 4
l = 0
r = k - 1

cur_win_sum = sum(spending[l : r + 1])
max_spent = cur_win_sum
while r < len(spending) - 1:
    cur_win_sum -= spending[l]
    l += 1
    r += 1
    cur_win_sum += spending[r]
    if cur_win_sum > max_spent:
        max_spent = cur_win_sum

print(f"The maximum spending over 4 consecutive days is: {max_spent}")

# Time & Space Complexity:
# Time Complexity: O(n) - linear time
# Space Complexity: O(1) - constant auxiliary space
