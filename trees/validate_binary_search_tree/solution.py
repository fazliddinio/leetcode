"""
Validate Binary Search Tree
LeetCode 98

Approach: Recursive with Range (Low, High)
Time: O(n) — Visit every node once.
Space: O(h) — Recursion stack.
Brute: O(n) — Iterative inorder traversal checking values are strictly increasing.
"""

from typing import Optional


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root, float('-inf'), float('inf'))
