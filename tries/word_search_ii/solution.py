"""
Word Search II
LeetCode 212

Approach: Trie + Backtracking
Time: O(M*L + R*C*4^L) — M words, L len. R*C board.
Space: O(M*L) — Trie storage.
Brute: O(W*R*C*4^L) — Per-word DFS running a separate backtracking search for each word.
"""

from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None
        self.refs = 0


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            curr = root
            curr.refs += 1
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                curr.refs += 1
            curr.word = w
        rows, cols = (len(board), len(board[0]))
        res = []

        def prune(word):
            node = root
            node.refs -= 1
            for c in word:
                node = node.children[c]
                node.refs -= 1

        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children or node.children[char].refs == 0:
                return
            curr = node.children[char]
            if curr.word:
                res.append(curr.word)
                prune(curr.word)
                curr.word = None
            board[r][c] = '#'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = (r + dr, c + dc)
                if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] != '#'):
                    dfs(nr, nc, curr)
            board[r][c] = char
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res
