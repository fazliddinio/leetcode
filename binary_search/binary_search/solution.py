"""
# Binary Search

## Problem Description
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
You must write an algorithm with `O(log n)` runtime complexity.

## Approaches
1.  **Linear Search** (Brute Force): Iterate through the array to find the target.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
2.  **Binary Search** (Optimal): Divide search space in half.
    *   Time Complexity: O(log n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Binary Search
    """
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search for target.
        
        Args:
            nums: Sorted list.
            target: Target value.
            
        Returns:
            Index or -1.
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

class SolutionBruteForce:
    """
    Alternative Solution: Linear Search
    """
    def search(self, nums: List[int], target: int) -> int:
        """
        Linear search.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i, n in enumerate(nums):
            if n == target:
                return i
            if n > target: # Optimization for sorted
                return -1
        return -1
