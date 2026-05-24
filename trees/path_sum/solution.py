"""
Path Sum
LeetCode 112

Approach: DFS (Subtract Target)
Time: O(n) — Visit every node once.
Space: O(h) — Recursion stack.
Brute: O(n) — Iterative DFS with stack tracking (node, remaining_sum) pairs.
"""

from typing import Optional


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        remaining = targetSum - root.val
        if not root.left and (not root.right):
            return remaining == 0
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
