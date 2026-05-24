"""
Remove Element
LeetCode 27

Approach: Two Pointers (Reader/Writer)
Time: O(n) — single pass
Space: O(1) — in-place modification
Brute: O(n²) — shift elements left on each removal
"""

from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        """Reader/Writer Approach"""
        writer = 0
        for reader in range(len(nums)):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1
        return writer
