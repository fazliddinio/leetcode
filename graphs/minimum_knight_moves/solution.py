"""
Minimum Knight Moves
LeetCode 1197

Approach: BFS (Shortest Path)
Time: O(|x| * |y|) — Bounded search space.
Space: O(|x| * |y|) — Visited set.
Brute: O(8^d) — Naive BFS/DFS without pruning, exploring all 8 directions at each depth d.
"""

from collections import deque


class Solution:

    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)

        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                      (1, 2), (1, -2), (-1, 2), (-1, -2)]

        queue = deque([(0, 0, 0)])
        visited = {(0, 0)}

        while queue:
            cx, cy, steps = queue.popleft()
            if cx == x and cy == y:
                return steps
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in visited and -2 <= nx <= x + 2 and -2 <= ny <= y + 2:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

        return -1
