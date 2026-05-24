"""
Contains Duplicate
LeetCode 217

Approach: Hash Set
Time: O(n) — single pass with O(1) average lookup
Space: O(n) — hash set stores up to n elements
Brute: O(n²) — compare every pair of elements
"""

from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        """Hash Set Approach"""
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
