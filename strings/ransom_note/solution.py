"""
Ransom Note
LeetCode 383

Approach: Frequency Map
Time: O(m + n) — Count both strings.
Space: O(1) — 26 lowercase English letters.
Brute: O(m * n) — For each ransom char, linear search and remove from magazine list.
"""

from collections import Counter


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        return st1 & st2 == st1
