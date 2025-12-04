"""
# Move Zeroes

## Problem Description
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

## Approaches
1.  **Copy Array** (Brute Force/Alternative): Create a new array, copy non-zeros, fill rest with zeros, copy back.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n) (Strictly speaking, violates in-place constraint, but worth knowing).
2.  **Two Pointers** (Optimal): "Snowball" or Partition approach. `l` tracks position for next non-zero.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Two Pointers
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all 0's to the end of the array in-place.
        
        Args:
            nums: A list of integers.
        
        Returns:
            None.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

class SolutionCopy:
    """
    Alternative Solution: Extra Space
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves zeroes using extra space.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = []
        for n in nums:
            if n != 0:
                res.append(n)
        
        # Fill rest with zeros
        while len(res) < len(nums):
            res.append(0)
            
        # Copy back
        for i in range(len(nums)):
            nums[i] = res[i]
