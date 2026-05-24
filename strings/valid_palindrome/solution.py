"""
Valid Palindrome
LeetCode 125

Approach: Two Pointers
Time: O(n) — Single pass from both ends.
Space: O(1) — Constant variable space.
Brute: O(n) — Filter alphanumeric chars into a new list, then check reversed copy.
"""


class Solution:

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
