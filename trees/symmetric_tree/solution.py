"""
Symmetric Tree
LeetCode 101

Approach: Recursive Mirror Check
Time: O(n) — Visit every node once.
Space: O(h) — Recursion stack.
Brute: O(n) — Iterative BFS comparing mirror pairs with a queue.
"""

from typing import Optional


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self._isMirror(root.left, root.right)

    def _isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                self._isMirror(left.left, right.right) and
                self._isMirror(left.right, right.left))
