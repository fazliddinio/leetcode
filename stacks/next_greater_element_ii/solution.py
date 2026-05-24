"""
Next Greater Element II
LeetCode 503

Approach: Monotonic Stack (Circular Array)
Time: O(n) — Traverse 2*n elements.
Space: O(n) — Stack storage.
Brute: O(n^2) — For each element, scan circularly to find next greater.
"""

from typing import List


class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            current_idx = i % n
            while stack and nums[stack[-1]] < nums[current_idx]:
                idx = stack.pop()
                res[idx] = nums[current_idx]
            if i < n:
                stack.append(i)
        return res
