"""
Two Sum
LeetCode 1

Approach: Hash Map
Time: O(n) — single pass with O(1) average lookup
Space: O(n) — hash map stores up to n-1 elements
Brute: O(n²) — check all pairs with nested loops
"""

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hash Map Approach"""
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
