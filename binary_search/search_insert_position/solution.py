"""
Search Insert Position
LeetCode 35

Approach: Binary Search
Time: O(log n) — standard binary search
Space: O(1) — constant variable space
Brute: O(n) — linear scan until element >= target
"""

from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
