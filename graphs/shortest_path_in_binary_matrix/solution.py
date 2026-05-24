"""
Shortest Path in Binary Matrix
LeetCode 1091

Approach: BFS (Level Order)
Time: O(N^2) — Each cell visited at most once.
Space: O(N^2) — Queue can hold all cells in worst case.
Brute: O(N^2 log N) — A* or Dijkstra-like approach with priority queue over all cells.
"""

from typing import List
from collections import deque


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        while queue:
            r, c, dist = queue.popleft()
            if r == n - 1 and c == n - 1:
                return dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))

        return -1
