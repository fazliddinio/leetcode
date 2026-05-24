"""
Combination Sum II
LeetCode 40

Approach: Backtracking
Time: O(2^N) — Worst case, check all subsets.
Space: O(N) — Recursion depth.
Brute: O(2^N) — Bitmask all subsets, filter those summing to target.
"""

from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, current_sum, path):
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, current_sum + candidates[i], path)
                path.pop()
        backtrack(0, 0, [])
        return res
