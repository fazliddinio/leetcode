"""
Longest Increasing Path in a Matrix
LeetCode 329

Approach: DFS with Memoization
Time: O(M * N) — Each cell computed once.
Space: O(M * N) — Memoization table.
Brute: O(4^(M*N)) — Pure DFS without memoization, recomputing every path.
"""

from typing import List


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        rows, cols = (len(matrix), len(matrix[0]))
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[r, c]
            curr = matrix[r][c]
            res = 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = (r + dr, c + dc)
                if 0 <= nr < rows and 0 <= nc < cols and (matrix[nr][nc] > curr):
                    res = max(res, 1 + dfs(nr, nc))
            memo[r, c] = res
            return res
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))
        return ans
