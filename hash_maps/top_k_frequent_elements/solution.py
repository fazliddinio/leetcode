"""
# Top K Frequent Elements

## Problem Description
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Approaches
1.  **Sorting** (Brute Force/Alternative): Count frequencies, then sort elements by frequency.
    *   Time Complexity: O(N log N)
    *   Space Complexity: O(N)
2.  **Max Heap** (Alternative): Use a max heap (or min heap of size k) to keep track of top k.
    *   Time Complexity: O(N log k)
    *   Space Complexity: O(N)
3.  **Bucket Sort** (Optimal): Use bucket sort where index represents frequency.
    *   Time Complexity: O(N)
    *   Space Complexity: O(N)
"""

from typing import List, Dict
import heapq
from collections import Counter

class Solution:
    """
    Optimal Solution: Bucket Sort
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.

        Args:
            nums: The list of integers.
            k: The number of frequent elements to return.

        Returns:
            A list containing the k most frequent elements.

        Time Complexity: O(n) - Using bucket sort (average case).
        Space Complexity: O(n) - Storing counts and buckets.
        """
        count: Dict[int, int] = {}
        freq: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

class SolutionSorting:
    """
    Alternative Solution: Sorting
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds top k by sorting frequencies.
        
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        """
        count = Counter(nums)
        # Sort keys by value (frequency) in descending order
        sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        return sorted_keys[:k]

class SolutionHeap:
    """
    Alternative Solution: Heap
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds top k using heap.
        
        Time Complexity: O(N log K)
        Space Complexity: O(N)
        """
        count = Counter(nums)
        # heapq.nlargest uses a heap under the hood of size k
        return heapq.nlargest(k, count.keys(), key=count.get)