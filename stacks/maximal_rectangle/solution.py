"""
Maximal Rectangle
LeetCode 85

Approach: Histogram for Each Row
Time: O(rows * cols) — Compute histogram for each row.
Space: O(cols) — Height array + Stack.
Brute: O(rows^2 * cols^2) — Check all sub-rectangles by enumerating corners.
"""

from typing import List


class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        rows, cols = (len(matrix), len(matrix[0]))
        heights = [0] * cols
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, self._largest_rectangle(heights))
        return max_area

    def _largest_rectangle(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        extended = heights + [0]
        for i, h in enumerate(extended):
            while stack and extended[stack[-1]] > h:
                height = extended[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
