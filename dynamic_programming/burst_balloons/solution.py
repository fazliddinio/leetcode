"""
Burst Balloons
LeetCode 312

Approach: Interval DP
Time: O(N^3) — Three nested loops.
Space: O(N^2) — DP table size.
Brute: O(N!) — Try every permutation of balloon burst order.
"""

from typing import List


class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        vals = [1] + nums + [1]
        n = len(vals)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for k in range(left + 1, right):
                    coins = dp[left][k] + vals[left] * vals[k] * vals[right] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
        return dp[0][n - 1]
