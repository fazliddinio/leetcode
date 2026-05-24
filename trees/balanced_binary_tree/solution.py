"""
Balanced Binary Tree
LeetCode 110

Approach: Height Check (Bottom-Up)
Time: O(n) — Visit every node once.
Space: O(h) — Recursion stack (h=height).
Brute: O(n^2) — Top-down recomputing height at every node.
"""

from typing import Optional


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._checkHeight(root) != -1

    def _checkHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = self._checkHeight(node.left)
        if left == -1:
            return -1
        right = self._checkHeight(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
