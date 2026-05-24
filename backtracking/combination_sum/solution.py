"""
Combination Sum
LeetCode 39

Approach: Backtracking
Time: O(N^(T/M)) — N=candidates, T=target, M=min(candidates). Exponential.
Space: O(T/M) — Recursion depth based on target/min_value.
Brute: O(N^(T/M)) — BFS queue exploring all combinations level by level.
"""

from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, current_sum, path):
            if current_sum == target:
                res.append(path[:])
                return
            if current_sum > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, current_sum + candidates[i], path)
                path.pop()
        backtrack(0, 0, [])
        return res
