"""
Network Delay Time
LeetCode 743

Approach: Dijkstra's Algorithm
Time: O(E log V) — Standard Dijkstra complexity.
Space: O(V + E) — Adjacency list and heap.
Brute: O(V * E) — Bellman-Ford, relax all edges V-1 times.
"""

from typing import List
import heapq
from collections import defaultdict


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        min_heap = [(0, k)]
        visited = set()
        t = 0
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        return t if len(visited) == n else -1
