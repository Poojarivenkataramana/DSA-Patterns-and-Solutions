# Question1:- Two sum

arr = [2, 4, 5, 7, 9, 11, 15]
left = 0
target = 16
right = len(arr) - 1

while left < right:
    if arr[left] + arr[right] == target:
        print((arr[left], arr[right]))
        break
    elif arr[left] + arr[right] > target:
        right -= 1
    elif arr[left] + arr[right] < target:
        left += 1

# Time and Space Complexity:
# Time Complexity: O(n) - Two pointers moving inward in a single pass
# Space Complexity: O(1) - Constant auxiliary space
