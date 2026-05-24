"""
Top K Frequent Elements
LeetCode 347

Approach: Heap
Time: O(N log K) — Build heap of size K.
Space: O(N) — Store counts.
Brute: O(n log n) — Count frequencies then sort all elements.
"""

from typing import List
from collections import Counter
import heapq


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
