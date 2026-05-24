"""
Kth Smallest Element in a BST
LeetCode 230

Approach: Iterative Inorder Traversal
Time: O(H + k) — Reach leftmost then process k nodes.
Space: O(H) — Stack height.
Brute: O(n) — Recursive inorder collecting all values into sorted list, return k-th.
"""

from typing import Optional


class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
