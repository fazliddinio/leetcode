"""
Kth Largest Element in a Stream
LeetCode 703

Approach: Min-Heap
Time: Add: O(log K) — Maintain heap of size K.
Space: O(K) — Heap size.
Brute: O(N log N) — Sort the entire list on each add and return k-th element.
"""

from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
