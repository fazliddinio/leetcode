"""
Next Greater Element
LeetCode 496

Approach: Monotonic Stack + Hash Map
Time: O(n + m) — Process nums2 then nums1.
Space: O(m) — Map and stack.
Brute: O(n*m) — For each num in nums1, find it in nums2 and scan right for greater.
"""

from typing import List


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]
