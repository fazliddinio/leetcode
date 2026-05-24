"""
==========================================
  Coin Change (LeetCode 322)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1: Input: coins = [1,2,5], amount = 11, Output: 3
Example 2: Input: coins = [2], amount = 3, Output: -1
Example 3: Input: coins = [1], amount = 0, Output: 0

Constraints: 1 <= coins.length <= 12, 1 <= coins[i] <= 2^31 - 1, 0 <= amount <= 10^4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the minimum coins needed to make a target amount.

    Coins: [1, 2, 5], Target: 11
    Best way: 5 + 5 + 1 = 11  (3 coins)

How to solve:
Bottom-up DP. Build an array `dp` where `dp[i]` is the min coins needed for amount `i`.
Initialize `dp` with infinity (or amount + 1), and `dp[0] = 0`.

    For each coin:
        If coin <= amount:
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    Example target 11:
    Try 1: 1 + dp[10]
    Try 2: 1 + dp[9]
    Try 5: 1 + dp[6]  <-- The best choice
"""
