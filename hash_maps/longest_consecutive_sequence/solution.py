# 128. Longest Consecutive Sequence
# Time: O(n)  – set lookup is O(1)
# Space: O(n) – hash set
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, best = set(nums), 0
        for v in s:
            if v - 1 not in s:          # start of a sequence
                cur = v
                while cur + 1 in s:
                    cur += 1
                best = max(best, cur - v + 1)
        return best