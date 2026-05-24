"""
Find the Difference
LeetCode 389

Approach: XOR / Bit Manipulation
Time: O(n) — Single pass through both strings.
Space: O(1) — Constant variable space.
Brute: O(n) — Use frequency maps for both strings, then find the extra character.
"""


class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for c in s:
            res ^= ord(c)
        for c in t:
            res ^= ord(c)
        return chr(res)
