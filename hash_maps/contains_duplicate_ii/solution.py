"""
Contains Duplicate II
LeetCode 219

Approach: Hash Map
Time: O(n) — Single pass.
Space: O(n) — Map stores up to n elements.
Brute: O(n*k) — Check all pairs within distance k.
"""

from typing import List


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
