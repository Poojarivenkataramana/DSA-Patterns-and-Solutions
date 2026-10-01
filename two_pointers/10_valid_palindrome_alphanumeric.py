# Day 4 — Problem 2: Clean Transaction Code
# A payment system receives a transaction code that may contain spaces, punctuation, and mixed case:
# code = "A man, a plan, a canal: Panama"
# We need to determine whether it is a palindrome after considering only letters/numbers and ignoring case.
# For example:
# "A man, a plan, a canal: Panama"
#         ↓
# "amanaplanacanalpanama"
#         ↓
# palindrome ✅
# Your Two-Pointers approach
# Don't create a reversed string.
# Use:
# left → beginning
# right → end
# If the left character isn't alphanumeric → move left
# If the right character isn't alphanumeric → move right
# Otherwise compare them ignoring case
# If they differ → False
# If they match → move both

code = "A man, a plan, a canal: Panam a"

l = 0
r = len(code) - 1
is_palindrome = True

while l <= r:
    if not code[l].isalnum():
        l += 1
    elif not code[r].isalnum():
        r -= 1
    elif code[l].lower() == code[r].lower():
        l += 1
        r -= 1
    elif code[l].lower() != code[r].lower():
        is_palindrome = False
        break

if is_palindrome:
    print('True')
else:
    print('False')

# Time and Space Complexity:
# Time Complexity: O(n) - Single pass from both ends
# Space Complexity: O(1) - Evaluated in-place without creating extra strings
