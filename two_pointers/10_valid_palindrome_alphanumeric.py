"""
================================================================================
Problem: Clean Transaction Code (Valid Palindrome with Alphanumeric Filtering)
Pattern: Two Pointers (Skipping Non-Alphanumeric Characters)
LeetCode: LC 125 - Valid Palindrome
================================================================================

Scenario: Clean Transaction Code
A payment system receives a transaction code that may contain spaces, 
punctuation, and mixed casing:
    code = "A man, a plan, a canal: Panama"

Determine whether it is a palindrome after considering only alphanumeric characters 
and ignoring case.

Rules:
- Do NOT create a reversed string.
- Left pointer starts at beginning (l = 0).
- Right pointer starts at end (r = len(code) - 1).
- If code[l] is not alphanumeric, move l += 1.
- If code[r] is not alphanumeric, move r -= 1.
- Compare code[l].lower() == code[r].lower().
  * If different -> return False.
  * If match -> move l += 1, r -= 1.

Example:
    Input: "A man, a plan, a canal: Panama"
    Filtered: "amanaplanacanalpanama"
    Output: True

Complexity:
- Time Complexity: O(n) - Two pointers meet in the middle in one pass.
- Space Complexity: O(1) - Evaluated in-place without generating a clean copy string.
================================================================================
"""

def is_palindrome_alphanumeric(code: str) -> bool:
    l = 0
    r = len(code) - 1

    while l <= r:
        if not code[l].isalnum():
            l += 1
        elif not code[r].isalnum():
            r -= 1
        elif code[l].lower() == code[r].lower():
            l += 1
            r -= 1
        else:
            return False

    return True


if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon"
    ]
    for text in test_cases:
        ans = is_palindrome_alphanumeric(text)
        print(f"Input: \"{text}\"\n  -> Is Palindrome: {ans}\n")
