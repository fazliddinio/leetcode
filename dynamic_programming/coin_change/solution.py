"""
Coin Change
LeetCode 322

Approach: DP Bottom-Up
Time: O(amount * len(coins)) — Fill table of size amount, iterating through coins.
Space: O(amount) — DP table size.
Brute: O(S^n) — Recurse trying every coin at every remaining amount without memoization.
"""

from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != float('inf') else -1
