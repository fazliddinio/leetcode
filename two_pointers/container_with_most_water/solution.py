"""
Container With Most Water
LeetCode 11

Approach: Two Pointers
Time: O(n) — single pass from both ends
Space: O(1) — constant variable space
Brute: O(n²) — check every pair of lines with nested loops
"""

from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
