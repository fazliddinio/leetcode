"""
# Search in Rotated Sorted Array

## Problem Description
There is an integer array `nums` sorted in ascending order (with distinct values).
Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`).
Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.
You must write an algorithm with `O(log n)` runtime complexity.

## Approaches
1.  **Linear Search** (Brute Force): Scan for target.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
2.  **Binary Search** (Optimal): Adjusted binary search handling rotation.
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
        Searches target in rotated array.
        
        Args:
            nums: Rotated sorted list.
            target: Target value.
            
        Returns:
            Index or -1.
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            # Left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

class SolutionBruteForce:
    """
    Alternative Solution: Linear Search
    """
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches using linear scan.
        Time Complexity: O(n)
        """
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1
