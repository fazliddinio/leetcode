"""
Intersection of Two Arrays
LeetCode 349

Approach: Set Intersection
Time: O(n + m) — Create two sets and intersect.
Space: O(n + m) — Store unique elements of both arrays.
Brute: O(n*m) — Nested loop checking each element pair.
"""

from typing import List


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))
