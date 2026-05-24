"""
Longest Common Prefix
LeetCode 14

Approach: Vertical Scanning
Time: O(S) — where S is sum of all characters.
Space: O(1) — Constant variable space.
Brute: O(S log n) — Sort strings and compare only the first and last.
"""

from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]
