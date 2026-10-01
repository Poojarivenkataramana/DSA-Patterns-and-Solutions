# Day 4 — Two Pointers: Palindrome Pattern
# This is a new pattern from the ones you've solved so far.
# 🎯 Scenario: Transaction Code Verification
# A payment system receives a transaction code:
# code = "ABCDCBA"
# The system considers the code valid if it reads the same from left to right and right to left.
# For example:
# A B C D C B A
# ↑           ↑
# L           R
# We compare the characters at both pointers.

code = "ABCDCBA"
left = 0
right = len(code) - 1
is_palindrome = True

while left <= right:
    if code[left] != code[right]:
        is_palindrome = False
        break
    elif code[left] == code[right]:
        left += 1
        right -= 1

if is_palindrome:
    print("True")
else:
    print("False")

# Time and Space Complexity:
# Time Complexity: O(n) - Scans up to middle of string
# Space Complexity: O(1) - Constant auxiliary space
