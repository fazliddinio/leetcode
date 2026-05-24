"""
Longest Palindromic Substring
LeetCode 5

Approach: Expand Around Center
Time: O(n^2) — Expand from each of the 2n-1 centers.
Space: O(1) — Simple variables used.
Brute: O(n^3) — Check every substring and verify if it's a palindrome.
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        for i in range(len(s)):
            l, r = (i, i)
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            l, r = (i, i + 1)
            while l >= 0 and r < len(s) and (s[l] == s[r]):
                if r - l + 1 > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
