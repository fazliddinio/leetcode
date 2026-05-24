"""
Unique Paths II
LeetCode 63

Approach: Space Optimized DP
Time: O(m * n) — Single pass through grid.
Space: O(n) — Store only one row.
Brute: O(2^(m+n)) — Recursive DFS exploring all paths, skipping obstacles.
"""

from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m, n = (len(obstacleGrid), len(obstacleGrid[0]))
        dp = [0] * n
        dp[n - 1] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]
