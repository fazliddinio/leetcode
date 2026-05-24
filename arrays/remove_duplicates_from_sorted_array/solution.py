"""
Remove Duplicates from Sorted Array
LeetCode 26

Approach: Two Pointers
Time: O(n) — single pass
Space: O(1) — in-place modification
Brute: O(n log n) — use set to find uniques, then sort and copy back
"""

from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        """Two Pointers Approach"""
        if not nums:
            return 0
        write_pos = 1
        for read_pos in range(1, len(nums)):
            if nums[read_pos] != nums[read_pos - 1]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        return write_pos
