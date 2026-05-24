"""
Valid Palindrome
LeetCode 125

Approach: Two Pointers
Time: O(n) — single pass from both ends
Space: O(1) — constant variable space
Brute: O(n) — filter alphanumeric chars, reverse string, and compare
"""


class Solution:

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
