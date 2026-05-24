"""
Subsets
LeetCode 78

Approach: Backtracking
Time: O(N * 2^N) — 2^N subsets, O(N) to copy each.
Space: O(N) — Recursion depth.
Brute: O(N * 2^N) — Bit masking to enumerate all 2^N inclusion/exclusion combos.
"""

from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res
