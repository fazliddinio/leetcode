"""
Palindromic Substrings
LeetCode 647

Approach: Expand Around Center
Time: O(n^2) — Each character and gap is a center.
Space: O(1) — Constant extra space.
Brute: O(n^3) — Check every substring and verify if it's a palindrome.
"""


class Solution:

    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l, r = (i, i)
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
            l, r = (i, i + 1)
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
        return res
