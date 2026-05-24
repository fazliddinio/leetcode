"""
Diameter of Binary Tree
LeetCode 543

Approach: DFS (Height Calculation)
Time: O(n) — Visit every node once.
Space: O(h) — Recursion stack.
Brute: O(n^2) — Top-down recomputing height at every node to find max diameter.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)
        height(root)
        return self.max_diameter
