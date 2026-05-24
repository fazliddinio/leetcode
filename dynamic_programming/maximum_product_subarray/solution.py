"""
Maximum Product Subarray
LeetCode 152

Approach: Kadane's Algorithm Variant
Time: O(N) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(n^2) — Check product of every subarray with nested loops.
"""

from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = max(nums)
        curr_min, curr_max = (1, 1)
        for n in nums:
            if n == 0:
                curr_min, curr_max = (1, 1)
                continue
            tmp = curr_max * n
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(tmp, n * curr_min, n)
            res = max(res, curr_max)
        return res
