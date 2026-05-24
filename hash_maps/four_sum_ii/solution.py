"""
4Sum II
LeetCode 454

Approach: Meet in the Middle (Hash Map)
Time: O(n^2) — Pair sums of first two arrays.
Space: O(n^2) — Map stores sums of pairs.
Brute: O(n^4) — Four nested loops checking all combinations.
"""

from typing import List
from collections import defaultdict


class Solution:

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count_ab = defaultdict(int)
        for a in nums1:
            for b in nums2:
                count_ab[a + b] += 1
        res = 0
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                res += count_ab[target]
        return res
