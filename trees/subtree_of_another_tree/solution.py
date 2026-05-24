"""
Subtree of Another Tree
LeetCode 572

Approach: DFS (Naive Match)
Time: O(N * M) — N=root nodes, M=subRoot nodes. Worst case match every node.
Space: O(N) — Recursion stack (or O(H)).
Brute: O(N + M) — Serialize both trees to strings and check substring containment.
"""

from typing import Optional


class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self._isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def _isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and
                self._isSameTree(p.left, q.left) and
                self._isSameTree(p.right, q.right))
