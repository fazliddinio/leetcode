# LeetCode 322: Coin Change
# Time: O(n * amount), Space: O(amount)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
