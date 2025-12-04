"""
# Container With Most Water

## Problem Description
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

## Approaches
1.  **Brute Force**: Compute the area for every possible pair of lines.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Two Pointers** (Optimal): Initialize max area to 0. Use two pointers at potential max widths, move the shorter line inward.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Two Pointers
    """
    def maxArea(self, height: List[int]) -> int:
        """
        Finds max water container.
        
        Args:
            height: A list of integers representing the height of lines.
            
        Returns:
            The maximum amount of water a container can store.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def maxArea(self, height: List[int]) -> int:
        """
        Finds max area using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        res = 0
        n = len(height)
        for l in range(n):
            for r in range(l + 1, n):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        return res