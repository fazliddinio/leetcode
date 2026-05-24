"""
Max Consecutive Ones III
LeetCode 1004

Approach: Sliding Window with Zero Count
Time: O(n) — single pass
Space: O(1) — constant variable space
Brute: O(n²) — try all subarrays, count zeros in each
"""

from typing import List


class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        """Sliding Window with target count"""
        left = 0
        zeros_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
                
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
