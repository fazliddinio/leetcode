"""
# Find Minimum in Rotated Sorted Array

## Problem Description
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. Given the unique sorted array `nums` after the rotation, return the minimum element of this array.
You must write an algorithm that runs in `O(log n)` time.

## Approaches
1.  **Linear Scan** (Brute Force): Iterate to find min.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
2.  **Binary Search** (Optimal): Use sorted property to find pivot.
    *   Time Complexity: O(log n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Binary Search
    """
    def findMin(self, nums: List[int]) -> int:
        """
        Finds min in rotated array.
        
        Args:
            nums: Rotated sorted list.
            
        Returns:
            Minimum element.
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

class SolutionBruteForce:
    """
    Alternative Solution: Linear Scan
    """
    def findMin(self, nums: List[int]) -> int:
        """
        Finds min by linear scan.
        Time Complexity: O(n)
        """
        return min(nums)
