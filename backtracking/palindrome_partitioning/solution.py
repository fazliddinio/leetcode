"""
Palindrome Partitioning
LeetCode 131

Approach: Backtracking
Time: O(N * 2^N) — 2^N possible substrings, N to check palindrome/copy.
Space: O(N) — Recursion depth.
Brute: O(N^2 * 2^N) — Precompute palindrome table with DP, build partitions bottom-up.
"""

from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(ss):
            return ss == ss[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    path.append(sub)
                    backtrack(end, path)
                    path.pop()
        backtrack(0, [])
        return res
