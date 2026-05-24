"""
House Robber II
LeetCode 213

Approach: Linear DP on Two Subarrays
Time: O(N) — Run House Robber twice.
Space: O(1) — Constant variable space.
Brute: O(2^n) — Recurse on circular array choosing to rob or skip each house.
"""

from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self._rob_linear(nums[:-1]), self._rob_linear(nums[1:]))

    def _rob_linear(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2
