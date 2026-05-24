"""
Number of Islands
LeetCode 200

Approach: DFS
Time: O(M * N) — Visit every cell.
Space: O(M * N) — Recursion stack depth.
Brute: O(M * N) — BFS level-order traversal to flood-fill each island.
"""

from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = (len(grid), len(grid[0]))
        count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or (c >= cols) or (grid[r][c] == '0'):
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
