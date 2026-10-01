# Problem 2 - Minimum Temperature
# Find the minimum sum of temperatures in 3 consecutive days
temperatures = [32, 28, 30, 25, 27, 29, 31]
k = 3
# step1: initializing the starting position of the window
l = 0
# step2: initializing the ending position of the window
r = k - 1
# step3: calculating the sum of current window temperatures
curr_temps = sum(temperatures[l : r + 1])
# step4: assigning the current window temperatures to minimum temps we believe this is the minimum temperatures of 3 consecutive days
min_temps = curr_temps
# step5: now loop condition
while r < len(temperatures) - 1:
    # step6: we have already assigned current window temperatures and now we just need to move window that's it
    curr_temps -= temperatures[l]
    l += 1
    r += 1
    curr_temps += temperatures[r]
    # step7: now compare current temperatures with minimum temperatures
    if curr_temps < min_temps:
        # if current sum of 3 consecutive temperatures days is less than current temperatures that are stored inside the min_temps then we move current temps to min temps
        min_temps = curr_temps
# step8: now last step displaying the output
print("The minimum sum of temperatures in 3 consecutive days:", min_temps)

# Time & Space Complexity:
# Time Complexity: O(n) - linear time as we traverse array with a sliding window
# Space Complexity: O(1) - constant auxiliary space
