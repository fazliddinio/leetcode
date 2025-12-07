"""
# Minimum Size Subarray Sum

## Problem Description
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

## Approaches
1.  **Brute Force**: Check all subarrays.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Sliding Window** (Optimal): Expand right, shrink left when sum >= target.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Sliding Window
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds minimal length of subarray with sum >= target.
        
        Args:
            target: Target sum.
            nums: List of positive integers.
            
        Returns:
            Minimal length or 0.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l = 0
        total = 0
        res = float("inf")
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
        
        return 0 if res == float("inf") else int(res)
    
    

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds min length using brute force.
        Time Complexity: O(n^2)
        """
        n = len(nums)
        res = float("inf")
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum >= target:
                    res = min(res, j - i + 1)
                    break # Optimization: shortest from i found
        return 0 if res == float("inf") else int(res)
