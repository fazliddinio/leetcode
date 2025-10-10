# LeetCode 84: Largest Rectangle in Histogram
# Time: O(n), Space: O(n)

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        
        return max_area
