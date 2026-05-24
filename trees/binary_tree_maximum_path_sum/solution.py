"""
Binary Tree Maximum Path Sum
LeetCode 124

Approach: DFS (Post-order)
Time: O(n) — Visit every node once.
Space: O(h) — Recursion stack.
Brute: O(n) — Iterative post-order computing max gain per node using a hash map.
"""

from typing import Optional


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return self.max_sum
