"""
K Closest Points to Origin
LeetCode 973

Approach: Max-Heap
Time: O(N log K) — Maintain heap of size K.
Space: O(K) — Heap stores K points.
Brute: O(N log N) — Sort all points by distance and take first k.
"""

from typing import List
import heapq


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = -(x * x + y * y)
            heapq.heappush(heap, (dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]
