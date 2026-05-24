"""
Missing Number
LeetCode 268

Approach: XOR
Time: O(N) — single pass
Space: O(1) — constant variable space
Brute: O(N log N) — sort then scan for first gap
"""

from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res
