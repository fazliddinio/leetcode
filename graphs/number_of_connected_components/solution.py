"""
Number of Connected Components in an Undirected Graph
LeetCode 323

Approach: Union-Find
Time: O(N * alpha(N)) — Path compression makes operations nearly constant.
Space: O(N) — Parent array.
Brute: O(N + E) — BFS/DFS from each unvisited node, counting connected components.
"""

from typing import List


class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        for u, v in edges:
            union(u, v)
        return count
