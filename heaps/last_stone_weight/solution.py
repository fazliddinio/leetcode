"""
Last Stone Weight
LeetCode 1046

Approach: Max-Heap
Time: O(N log N) — Processing stones.
Space: O(N) — Heap storage.
Brute: O(N^2 log N) — Sort each round, smash two heaviest, repeat.
"""

from typing import List
import heapq


class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y - x))
        return -heap[0] if heap else 0
