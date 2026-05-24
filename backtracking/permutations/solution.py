"""
Permutations
LeetCode 46

Approach: Backtracking
Time: O(N * N!) — N! permutations, O(N) to copy each.
Space: O(N) — Recursion depth.
Brute: O(N * N!) — Iterative insertion of each number at every position.
"""

from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i + 1:])
                path.pop()
        backtrack([], nums)
        return res
