"""
Find K Closest Elements
LeetCode 658

Approach: Binary Search for Window Start
Time: O(log(n - k) + k) — binary search for start, then slice
Space: O(1) — excluding output list
Brute: O(n log n) — sort all elements by distance to x
"""

from typing import List


class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
