"""
Find First and Last Position of Element in Sorted Array
LeetCode 34

Approach: Two Binary Searches
Time: O(log n) — find start and end bounds separately
Space: O(1) — constant variable space
Brute: O(n) — linear scan to find first and last occurrence
"""

from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(is_first: bool) -> int:
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    idx = mid
                    if is_first:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return idx
            
        start = findBound(True)
        if start == -1:
            return [-1, -1]
        end = findBound(False)
        return [start, end]
