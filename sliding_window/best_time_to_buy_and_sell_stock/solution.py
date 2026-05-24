"""
Best Time to Buy and Sell Stock
LeetCode 121

Approach: Sliding Window / Two Pointers
Time: O(n) — single pass
Space: O(1) — constant variables
Brute: O(n²) — check all pairs of buy/sell days
"""

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """Sliding Window: Left=buy, Right=sell"""
        left = 0
        max_profit = 0
        for right in range(1, len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit, prices[right] - prices[left])
        return max_profit
