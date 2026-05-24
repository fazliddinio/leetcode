"""
Redundant Connection
LeetCode 684

Approach: Union-Find
Time: O(N * alpha(N)) — Proportional to N edges.
Space: O(N) — Parent array.
Brute: O(N^2) — For each edge, DFS/BFS to check if u and v are already connected.
"""

from typing import List


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []
