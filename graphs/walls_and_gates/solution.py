"""
Walls and Gates
LeetCode 286

Approach: Multi-source BFS
Time: O(M * N) — Visit every cell.
Space: O(M * N) — Queue size.
Brute: O(M * N * M * N) — BFS/DFS from each empty room to find nearest gate.
"""

from typing import List
from collections import deque


class Solution:

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        rows, cols = (len(rooms), len(rooms[0]))
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        dist = 0
        while queue:
            dist += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = (r + dr, c + dc)
                    if 0 <= nr < rows and 0 <= nc < cols and (rooms[nr][nc] == 2147483647):
                        rooms[nr][nc] = dist
                        queue.append((nr, nc))
