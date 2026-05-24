"""
Move Zeroes
LeetCode 283

Approach: Two Pointers with Swaps
Time: O(n) — single pass through the array
Space: O(1) — in-place
Brute: O(n) — two passes: move non-zeros forward, then fill remaining with zeros
"""

from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
