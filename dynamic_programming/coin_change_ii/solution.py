"""
Coin Change II
LeetCode 518

Approach: DP
Time: O(amount * N) — Fill table of size amount, iterating through coins.
Space: O(amount) — One-dimensional DP table.
Brute: O(N^amount) — Recursive backtracking enumerating all coin combinations.
"""

from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]
