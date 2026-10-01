"""
================================================================================
Problem: Valid Palindrome (Transaction Code Verification)
Pattern: Two Pointers (Opposite Direction String Verification)
LeetCode: LC 125 - Valid Palindrome (Basic Exact Match Variant)
================================================================================

Scenario: Transaction Code Verification
A payment system receives a transaction code:
    code = "ABCDCBA"
The system considers the code valid if it reads the same from left to right 
and right to left (a palindrome).

Example:
    Input: code = "ABCDCBA"
    Output: True

    Input: code = "ABCDEBA"
    Output: False

Approach (Opposite Direction Two Pointers):
1. Place left pointer at index 0 and right pointer at len(code) - 1.
2. While left <= right:
   - If code[left] != code[right], return False immediately.
   - Else, move left += 1 and right -= 1.
3. If loop finishes without mismatch, return True.

Complexity:
- Time Complexity: O(n) - Single scan up to the middle of the string.
- Space Complexity: O(1) - Constant auxiliary space.
================================================================================
"""

def is_valid_palindrome_basic(code: str) -> bool:
    left = 0
    right = len(code) - 1

    while left <= right:
        if code[left] != code[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    test_cases = ["ABCDCBA", "RACECAR", "HELLO", "A"]
    for code in test_cases:
        result = is_valid_palindrome_basic(code)
        print(f"Code: '{code}' -> Is Palindrome? {result}")
