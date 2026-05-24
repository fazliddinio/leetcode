"""
Combinations
LeetCode 77

Approach: Backtracking
Time: O(k * C(n, k)) — Total combinations times copy cost.
Space: O(k) — Recursion depth.
Brute: O(k * C(n, k)) — Use itertools.combinations to generate all k-length combos.
"""

from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            need = k - len(path)
            remain = n - start + 1
            if remain < need:
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return res
