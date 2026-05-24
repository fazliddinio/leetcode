"""
Subsets II
LeetCode 90

Approach: Backtracking with Duplicates
Time: O(N * 2^N) — Worst case 2^N subsets.
Space: O(N) — Recursion depth.
Brute: O(N * 2^N) — Iteratively build all subsets, deduplicate with a set.
"""

from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0, [])
        return res
