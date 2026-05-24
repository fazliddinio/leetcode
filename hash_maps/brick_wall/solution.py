"""
Brick Wall
LeetCode 554

Approach: Hash Map (Prefix Sums)
Time: O(N * M) — Check every brick edge.
Space: O(N * M) — Map stores count of every cut position.
Brute: O(N * M * W) — Try every possible vertical line position.
"""

from typing import List
from collections import defaultdict


class Solution:

    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)
        for row in wall:
            current_pos = 0
            for width in row[:-1]:
                current_pos += width
                edge_counts[current_pos] += 1
        max_edges = max(edge_counts.values()) if edge_counts else 0
        return len(wall) - max_edges
