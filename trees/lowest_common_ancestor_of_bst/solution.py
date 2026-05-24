"""
Lowest Common Ancestor of a BST
LeetCode 235

Approach: Iterative BST Search
Time: O(h) — Path from root to LCA.
Space: O(1) — Constant variable space.
Brute: O(h) — Recursive BST traversal letting the call stack guide to the split point.
"""

from typing import Optional


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None
