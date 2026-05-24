"""
Trapping Rain Water
LeetCode 42

Approach: Two Pointers
Time: O(n) — single pass from both ends
Space: O(1) — constant extra space for pointers and max trackers
Brute: O(n) — precompute left_max and right_max arrays using O(n) space
"""

from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water
