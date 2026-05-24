"""
Rotting Oranges
LeetCode 994

Approach: BFS
Time: O(M * N) — Visit every cell.
Space: O(M * N) — Queue size.
Brute: O((M * N)^2) — Repeatedly scan entire grid each minute to spread rot.
"""

from typing import List
from collections import deque


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = (len(grid), len(grid[0]))
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = (r + dr, c + dc)
                    if 0 <= nr < rows and 0 <= nc < cols and (grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        return minutes if fresh == 0 else -1
