"""
# Trapping Rain Water

## Problem Description
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Approaches
1.  **Brute Force**: For each element, find the max level to its left and right. Water at `i` is `min(max_left, max_right) - height[i]`.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Dynamic Programming** (Alternative): Precompute max_left and max_right arrays.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
3.  **Two Pointers** (Optimal): Use two pointers to track max_left and max_right on the fly.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Two Pointers
    """
    def trap(self, height: List[int]) -> int:
        """
        Computes how much water can be trapped.
        
        Args:
            height: Elevation map.
            
        Returns:
            Total water trapped.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(0, leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(0, rightMax - height[r])
        return res

class SolutionBruteForce:
    """
    Naive Solution: Nested Search
    """
    def trap(self, height: List[int]) -> int:
        """
        Computes water using brute force.
        Time Complexity: O(n^2)
        """
        if not height: return 0
        n = len(height)
        res = 0
        for i in range(1, n - 1):
            max_left = max(height[:i+1]) # O(i)
            max_right = max(height[i:])  # O(n-i)
            res += min(max_left, max_right) - height[i]
        return res

class SolutionDP:
    """
    Alternative Solution: Dynamic Programming
    """
    def trap(self, height: List[int]) -> int:
        """
        Computes water using precomputed arrays.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not height: return 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            
        right_max[n-1] = height[n-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
            
        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
