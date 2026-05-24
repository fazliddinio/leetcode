"""
Graph Valid Tree
LeetCode 261

Approach: Union-Find
Time: O(N * alpha(N)) — Proportional to N edges.
Space: O(N) — Parent array.
Brute: O(V + E) — DFS checking n-1 edges and full reachability from node 0.
"""

from typing import List


class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        count = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            rootX, rootY = (find(x), find(y))
            if rootX != rootY:
                parent[rootX] = rootY
                count -= 1
                return True
            return False
        for u, v in edges:
            if not union(u, v):
                return False
        return count == 1
