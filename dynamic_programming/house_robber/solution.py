"""
House Robber
LeetCode 198

Approach: Space Optimized DP
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(2^n) — Recurse choosing to rob or skip each house without memoization.
"""

from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = (0, 0)
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
