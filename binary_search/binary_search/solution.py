"""
Binary Search
LeetCode 704

Approach: Iterative Binary Search
Time: O(log n) — search space halves each iteration
Space: O(1) — constant variable space
Brute: O(log n) — recursive binary search with O(log n) call stack
"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
