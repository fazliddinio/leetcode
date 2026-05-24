"""
Group Anagrams
LeetCode 49

Approach: Categorize by Sorted String
Time: O(n * k log k) — Sorting each string.
Space: O(n * k) — Storing groups.
Brute: O(n^2 * k) — Compare each pair using character count arrays.
"""

from typing import List
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
