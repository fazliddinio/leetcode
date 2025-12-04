"""
# Best Time to Buy and Sell Stock

## Problem Description
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Approaches
1.  **Brute Force**: Check every pair (buy_day, sell_day) such that sell_day > buy_day.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **One Pass** (Optimal): Iterate through the array, keeping track of the minimum price so far and the maximum profit.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: One Pass
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from buying and selling a stock once.

        Args:
            prices: A list of integers representing stock prices on different days.

        Returns:
            The maximum profit achievable. Returns 0 if no profit is possible.

        Time Complexity: O(n) - We iterate through the prices list once.
        Space Complexity: O(1) - We use constant extra space.
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return int(max_profit)

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates max profit using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        max_profit = 0
        n = len(prices)
        
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit
