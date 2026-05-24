"""
Intersection of Two Arrays II
LeetCode 350

Approach: Hash Map
Time: O(n + m) — count elements in one array and iterate the other
Space: O(min(n, m)) — hash map stores counts of the smaller array
Brute: O(n * m) — for each element in nums1, search nums2 linearly
"""

from typing import List
from collections import Counter


class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Hash Map Approach"""
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        count = Counter(nums1)
        res = []
        for n in nums2:
            if count[n] > 0:
                res.append(n)
                count[n] -= 1
        return res
