"""
Minimum Size Subarray Sum
LeetCode 209

Approach: Sliding Window
Time: O(n) — each element added and removed at most once
Space: O(1) — constant variable space
Brute: O(n²) — check all subarrays for sum >= target
"""

from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Sliding Window Approach"""
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
                
        return min_length if min_length != float('inf') else 0
