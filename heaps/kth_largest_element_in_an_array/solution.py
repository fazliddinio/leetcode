"""
Kth Largest Element in an Array
LeetCode 215

Approach: Quickselect
Time: O(N) average, O(N^2) worst case — Partition-based selection.
Space: O(1) — In-place partitioning.
Brute: O(N log K) — Min-heap maintaining heap of size k.
"""

import random
from typing import List


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def quickselect(lo, hi):
            pivot_idx = random.randint(lo, hi)
            nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
            pivot = nums[hi]
            store = lo
            for i in range(lo, hi):
                if nums[i] <= pivot:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[store], nums[hi] = nums[hi], nums[store]
            if store == target:
                return nums[store]
            elif store < target:
                return quickselect(store + 1, hi)
            else:
                return quickselect(lo, store - 1)

        return quickselect(0, len(nums) - 1)
