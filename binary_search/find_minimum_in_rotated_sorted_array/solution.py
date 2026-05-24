"""
Find Minimum in Rotated Sorted Array
LeetCode 153

Approach: Binary Search
Time: O(log n) — half the array is discarded each step
Space: O(1) — constant variable space
Brute: O(n) — linear scan to find the minimum
"""

from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
