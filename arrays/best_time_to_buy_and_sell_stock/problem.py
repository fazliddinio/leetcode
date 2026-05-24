"""
==========================================
  Best Time to Buy and Sell Stock (LeetCode 121)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are given an array `prices` where `prices[i]` is the price of a given
stock on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you
cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
                 profit = 6-1 = 5.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: No profitable transaction is possible.

Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Imagine you have a time machine, but it only works for stocks.
You see the stock prices for each day:

    Day:   1    2    3    4    5    6
    Price: $7   $1   $5   $3   $6   $4

You want to pick ONE day to buy and ONE later day to sell.
The goal is to make the most money possible.

    Buy here ($1)          Sell here ($6)
         |                       |
         v                       v
    $7   $1   $5   $3   [$6]  $4
              ↑                ↑
              profit = $6 - $1 = $5

How to think about it:
  - Keep track of the cheapest price you've seen so far.
  - At each day, ask: "If I sold TODAY, how much would I make?"
  - Track the best profit across all days.

    Day 1: min_price = 7, profit = 0
    Day 2: min_price = 1, profit = 0      (1 - 1 = 0)
    Day 3: min_price = 1, profit = 4      (5 - 1 = 4)
    Day 4: min_price = 1, profit = 4      (3 - 1 = 2, but 4 is still best)
    Day 5: min_price = 1, profit = 5  ★   (6 - 1 = 5!)
    Day 6: min_price = 1, profit = 5      (4 - 1 = 3, but 5 is still best)

Answer: 5
"""
