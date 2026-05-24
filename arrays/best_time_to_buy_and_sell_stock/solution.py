"""
Best Time to Buy and Sell Stock
LeetCode 121

Approach: Single Pass
Time: O(n) — single pass through the array
Space: O(1) — only two variables used
Brute: O(n²) — check all pairs of buy/sell days
"""

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """Single Pass Approach"""
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit
