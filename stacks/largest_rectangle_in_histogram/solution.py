"""
# Largest Rectangle in Histogram

## Problem Description
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

## Approaches
1.  **Brute Force**: For each bar, extend left and right to find limits where height >= current height.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Monotonic Stack** (Optimal): Maintain stack of increasing heights. When smaller height seen, pop and calculate area.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Monotonic Stack
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Finds largest rectangle area.
        
        Args:
            heights: List of bar heights.
            
        Returns:
            Max area.
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        maxArea = 0
        stack = [] # pair: (index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
            
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

class SolutionBruteForce:
    """
    Naive Solution: Extend from center
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Finds area using brute force.
        Time Complexity: O(n^2)
        """
        n = len(heights)
        max_area = 0
        for i in range(n):
            min_h = heights[i]
            # Extend right
            for j in range(i, n):
                min_h = min(min_h, heights[j])
                max_area = max(max_area, min_h * (j - i + 1))
        return max_area
