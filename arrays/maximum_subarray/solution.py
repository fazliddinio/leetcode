"""
Maximum Subarray
LeetCode 53

Approach: Kadane's Algorithm
Time: O(n) — single pass through the array
Space: O(1) — only two variables used
Brute: O(n²) — check sum of every subarray
"""

from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        """Kadane's Algorithm Approach"""
        current_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
