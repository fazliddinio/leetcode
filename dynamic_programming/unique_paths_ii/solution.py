# LeetCode 63: Unique Paths II
# Time: O(m * n), Space: O(n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        
        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        
        return dp[-1]
