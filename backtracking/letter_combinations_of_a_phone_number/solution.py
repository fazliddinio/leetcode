"""
Letter Combinations of a Phone Number
LeetCode 17

Approach: Backtracking
Time: O(4^N * N) — 4 is max mapping size. N is string length.
Space: O(N) — Recursion depth.
Brute: O(4^N * N) — Iterative BFS building combinations level by level.
"""

from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []

        def backtrack(idx, path):
            if idx == len(digits):
                res.append(''.join(path))
                return
            for char in mapping[digits[idx]]:
                path.append(char)
                backtrack(idx + 1, path)
                path.pop()
        backtrack(0, [])
        return res
