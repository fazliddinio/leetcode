"""
Invert Binary Tree
LeetCode 226

Approach: Recursive DFS
Time: O(n) — Visit every node once.
Space: O(h) — Recursion stack.
Brute: O(n) — Iterative BFS swapping children level by level with a queue.
"""

from typing import Optional


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = (root.right, root.left)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
