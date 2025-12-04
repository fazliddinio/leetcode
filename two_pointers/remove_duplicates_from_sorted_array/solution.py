"""
# Remove Duplicates from Sorted Array

## Problem Description
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Return `k` after placing the final result in the first `k` slots of `nums`.

## Approaches
1.  **Pop Duplicates** (Brute Force/Alternative): Iterate and pop duplicates. Popping from list is O(n), so total O(n^2).
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Two Pointers** (Optimal): Use one pointer to track unique position, other to scan.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Two Pointers
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place.
        
        Args:
            nums: A sorted list of integers.
        
        Returns:
            The number of unique elements (k).
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
            
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

class SolutionPop:
    """
    Alternative Solution: Pop Duplicates
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates by popping.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
