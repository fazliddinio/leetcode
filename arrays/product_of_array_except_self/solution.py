"""
Product of Array Except Self
LeetCode 238

Approach: Prefix and Suffix in Output Array
Time: O(n) — two passes through the array
Space: O(1) — only uses the output array
Brute: O(n²) — for each index, multiply all other elements
"""

from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Space Optimized Approach"""
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result
