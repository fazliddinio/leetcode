"""
Contiguous Array
LeetCode 525

Approach: Prefix Sum & Hash Map
Time: O(n) — Single pass.
Space: O(n) — Map stores first occurrence of each count.
Brute: O(n^2) — Check all subarrays and count 0s/1s.
"""

from typing import List


class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        map_index = {0: -1}
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in map_index:
                max_len = max(max_len, i - map_index[count])
            else:
                map_index[count] = i
        return max_len
