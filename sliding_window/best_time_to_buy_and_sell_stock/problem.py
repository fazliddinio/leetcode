"""
==========================================
  Best Time to Buy and Sell Stock (LeetCode 121)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1: Input: prices = [7,1,5,3,6,4], Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Buy low, sell high! You just need the biggest difference between a low point and a high point that comes AFTER it.

    Prices: [7, 1, 5, 3, 6, 4]
    Buy at 1, Sell at 6 -> Profit = 5.

Method: Two Pointers (Left and Right).
  Left pointer is the "buy" day. Right pointer is the "sell" day.
  Iterate Right through the array.
  If price[Left] > price[Right] -> We found a NEW lowest price! Move Left to Right!
  Else -> Calculate `price[Right] - price[Left]` and check if it's the max profit so far!
"""
