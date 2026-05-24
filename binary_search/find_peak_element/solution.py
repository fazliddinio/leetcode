"""
Find Peak Element
LeetCode 162

Approach: Binary Search
Time: O(log n) — find peak in log steps
Space: O(1) — constant variable space
Brute: O(n) — linear scan comparing adjacent elements
"""

from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
