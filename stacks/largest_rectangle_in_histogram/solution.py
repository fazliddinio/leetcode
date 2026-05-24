"""
Largest Rectangle in Histogram
LeetCode 84

Approach: Monotonic Increasing Stack
Time: O(n) — Each element pushed/popped once.
Space: O(n) — Stack storage.
Brute: O(n^2) — For each bar, extend left and right while height allows.
"""

from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights = heights + [0]
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
