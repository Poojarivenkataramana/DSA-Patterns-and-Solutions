# Sliding window - problem 1
# Scenario Daily Sales
# A shop records sales for 7 consecutive days:

sales = [10, 20, 30, 40, 50, 60, 70]
k = 3

left = 0
right = k - 1

current_window_sum = sum(sales[left : right + 1])
max_window_sum = current_window_sum

while right < len(sales) - 1:
    current_window_sum -= sales[left]
    left += 1

    right += 1
    current_window_sum += sales[right]
    
    if current_window_sum > max_window_sum:
        max_window_sum = current_window_sum

print("Maximum sum is:", max_window_sum)

# Time & Space Complexity:
# Time Complexity: O(n)
# Space Complexity: O(1)
