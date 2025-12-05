# LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
# Time: O(n), Space: O(1)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sold = 0
        held = float('-inf')
        rest = 0
        
        for price in prices:
            prev_sold = sold
            sold = held + price
            held = max(held, rest - price)
            rest = max(rest, prev_sold)
        
        return max(sold, rest)
