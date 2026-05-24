"""
Repeated Substring Pattern
LeetCode 459

Approach: String Concatenation Trick
Time: O(n) — Substring search in doubled string.
Space: O(n) — Concatenated string.
Brute: O(n^2) — Try every possible substring length and repeat to check equality.
"""


class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
