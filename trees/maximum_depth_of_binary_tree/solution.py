"""
Maximum Depth of Binary Tree
LeetCode 104

Approach: Recursive DFS
Time: O(n) — Visit every node once.
Space: O(h) — Recursion stack.
Brute: O(n) — BFS level-by-level counting with a queue.
"""

from typing import Optional


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
