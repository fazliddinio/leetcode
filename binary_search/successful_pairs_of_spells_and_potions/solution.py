"""
Successful Pairs of Spells and Potions
LeetCode 2300

Approach: Sorting + Binary Search
Time: O(m log m + n log m) — sort potions, then binary search for each spell
Space: O(log m) — space used by sorting
Brute: O(n * m) — check every spell-potion pair
"""

from typing import List
import bisect


class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []
        
        for spell in spells:
            target = (success + spell - 1) // spell
            idx = bisect.bisect_left(potions, target)
            res.append(m - idx)
            
        return res
