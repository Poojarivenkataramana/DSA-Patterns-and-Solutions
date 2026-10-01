# Problem statement is find the maximum total sales in any 3 consecutive days.
sales = [12, 8, 15, 20, 7, 18, 10]
k = 3
# initializing the starting window position
l = 0
# and initializing the ending position of a window
r = k - 1
# initializing the current window sum
curr_win = sum(sales[l : r + 1])
# assigning the current window sum to the max_sales means we believe current sum is the maximum sales
max_sales = curr_win

# Now initializing the loop
while r < len(sales) - 1: # r is initially the last index of the current window, and each iteration moves it one position right until it reaches the last valid index.
    curr_win -= sales[l] # we already have current window so that's why we remove left from current window and move
    l += 1 # l + 1 and
    r += 1 # r + 1 because we are moving window from left to right so if left move on epoint right also moves in this particular problem
    curr_win += sales[r]
    if curr_win > max_sales: # now condition check if current window sum is greater than maximum sales then
        max_sales = curr_win # we move current window value into maximum sales that's it

print("The maximum sales of 3 consecutive days is:", max_sales) # now displaying the output


# Time & Space Complexity:
# Time Complexity: O(n) - here we used only single loop and the condition checks value once
# Space Complexity: O(1) - constant auxiliary space
