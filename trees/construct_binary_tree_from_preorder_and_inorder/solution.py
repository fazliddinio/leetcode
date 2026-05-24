"""
Construct Binary Tree from Preorder and Inorder
LeetCode 105

Approach: Hash Map for Inorder Indices
Time: O(n) — Build map and visit every node.
Space: O(n) — Hash map and recursion stack.
Brute: O(n^2) — Recursive with list slicing and index() lookups each time.
"""

from typing import List, Optional


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(inorder) - 1)
