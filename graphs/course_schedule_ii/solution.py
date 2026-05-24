"""
Course Schedule II
LeetCode 210

Approach: Kahn's Algorithm
Time: O(V + E) — Build graph and BFS.
Space: O(V + E) — Adjacency list and queue.
Brute: O(V + E) — DFS post-order traversal then reverse for topological sort.
"""

from typing import List
from collections import deque


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return res if len(res) == numCourses else []
