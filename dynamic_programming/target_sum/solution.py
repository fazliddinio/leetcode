"""
Target Sum
LeetCode 494

Approach: Subset Sum (DP)
Time: O(N * S) — N=nums.length, S=sum(nums).
Space: O(S) — DP array size.
Brute: O(2^N) — Recursive backtracking trying +/- for each number.
"""

from typing import List


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total + target < 0 or (total + target) % 2 != 0:
            return 0
        subset_target = (total + target) // 2
        dp = [0] * (subset_target + 1)
        dp[0] = 1
        for num in nums:
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[subset_target]
