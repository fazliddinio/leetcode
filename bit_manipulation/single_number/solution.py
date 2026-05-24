"""
Single Number
LeetCode 136

Approach: XOR
Time: O(N) — single pass
Space: O(1) — constant variable space
Brute: O(N) time O(N) space — use a hash set to track unpaired numbers
"""

from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
