# Practice 3 - Count High-Activity Periods
# Count how many windows of 3 consecutive days have a sum >= threshold
activity = [4, 7, 2, 9, 6, 3, 8, 5]
k = 3
threshold = 17
# step1 initializing the window starting index
l = 0
# step2 initializing the window ending index
r = k - 1
# step3 calculating the current window sum
cur_sum = sum(activity[l : r + 1])
# step4 creating the count variable
window_count = 0

# Check initial window
if cur_sum >= threshold:
    window_count += 1

# step5 loop condition
while r < len(activity) - 1:
    # step6 this is important step the window move if condition is True or False
    cur_sum -= activity[l]
    l += 1
    r += 1
    cur_sum += activity[r]
    # comparing the window sum and threshold if window sum is greater than or equal to threshold then we count that window
    if cur_sum >= threshold:
        window_count += 1

# step7 Now printing the window count
print(f"The window count: {window_count}")

# Time & Space Complexity:
# Time Complexity: O(n) - single pass over the array
# Space Complexity: O(1) - constant auxiliary space
