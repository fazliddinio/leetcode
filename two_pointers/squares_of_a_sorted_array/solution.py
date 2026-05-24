"""
Squares of a Sorted Array
LeetCode 977

Approach: Two Pointers (outside-in)
Time: O(n) — single pass to compare and place elements
Space: O(n) — resulting array of size n
Brute: O(n log n) — square each element then sort the array
"""

from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] * nums[left]
                left += 1
            else:
                res[i] = nums[right] * nums[right]
                right -= 1
        return res
