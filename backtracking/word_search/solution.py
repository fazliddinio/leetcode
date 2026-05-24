"""
Word Search
LeetCode 79

Approach: Backtracking (DFS)
Time: O(M * N * 3^L) — Start from each cell, explore 3 directions (approx) for length L.
Space: O(L) — Recursion depth is length of word.
Brute: O(M * N * 4^L) — DFS with in-place board modification instead of visited set.
"""

from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = (len(board), len(board[0]))
        path = set()

        def backtrack(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or (c >= cols) or (board[r][c] != word[idx]) or ((r, c) in path):
                return False
            path.add((r, c))
            res = backtrack(r + 1, c, idx + 1) or backtrack(r - 1, c, idx + 1) or backtrack(r, c + 1, idx + 1) or backtrack(r, c - 1, idx + 1)
            path.remove((r, c))
            return res
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
