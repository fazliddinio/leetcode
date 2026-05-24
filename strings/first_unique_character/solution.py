"""
First Unique Character in a String
LeetCode 387

Approach: Frequency Map
Time: O(n) — Two passes.
Space: O(1) — 26 lowercase English letters.
Brute: O(n^2) — For each character, scan the entire string for duplicates.
"""

from collections import Counter


class Solution:

    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
