"""
Course Schedule
LeetCode 207

Approach: Kahn's Algorithm (BFS)
Time: O(V + E) — Build graph and BFS.
Space: O(V + E) — Adjacency list and queue.
Brute: O(V + E) — DFS cycle detection marking nodes as visiting/visited.
"""

from typing import List
from collections import deque


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        processed = 0
        while queue:
            node = queue.popleft()
            processed += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return processed == numCourses
