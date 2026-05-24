"""
Valid Anagram
LeetCode 242

Approach: Frequency Map
Time: O(n) — Single pass through both strings.
Space: O(1) — 26 lowercase English letters.
Brute: O(n log n) — Sort both strings and compare.
"""

from collections import Counter


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = Counter(s)
        for c in t:
            if count[c] == 0:
                return False
            count[c] -= 1
        return True
