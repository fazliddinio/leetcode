"""
Maximum Average Subarray I
LeetCode 643

Approach: Fixed Sliding Window
Time: O(n) — single pass
Space: O(1) — constant variable space
Brute: O(n * k) — recompute sum for each window from scratch
"""

from typing import List


class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """Fixed Sliding Window Approach"""
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        return max_sum / k
