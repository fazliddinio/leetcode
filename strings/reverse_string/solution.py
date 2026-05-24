"""
Reverse String
LeetCode 344

Approach: Two Pointers (In-Place)
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(n) — Recursively swap from both ends, using O(n) stack space.
"""

from typing import List


class Solution:

    def reverseString(self, s: List[str]) -> None:
        left, right = (0, len(s) - 1)
        while left < right:
            s[left], s[right] = (s[right], s[left])
            left += 1
            right -= 1
